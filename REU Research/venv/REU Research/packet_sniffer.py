import scapy.all as scapy
import model, torch
from scapy.layers import http

coordinates = []


# Port used in training: udp port 4380 or udp portrange 27000-27040
# Full PUBG ports: tcp portrange 27015-27030 or tcp portrange 27037 or udp port 4380 or udp portrange 27000-27031 or
# udp port 27036
def main():
    global coordinates
    print('Packet Sniffer Sniffs')
    m = model.load()
    while True:
        coordinates = get_predictions(m)
        if coordinates is not None:
            print(coordinates)


def get_predictions(m):
    local_ip = scapy.get_if_addr(scapy.conf.iface)
    packet = scapy.sniff(count=1, filter="udp port 4380 or udp portrange 27000-27040")
    # packet.hexdump()

    if packet[0].payload.src != local_ip:
        print("You received a packet!")
        data = packet[0].payload.payload.payload.load
        if 756 > len(data) > 100:
            byte_data = []
            for bits in data:
                bit = float(bits)
                bit /= 240.0
                byte_data.append(bit)
            if len(byte_data) < 756:
                for j in range(756 - len(byte_data)):
                    byte_data.append(float(0.0))
            tensor = torch.FloatTensor(byte_data)
            prediction = m(tensor).tolist()
            coordinates = []
            for i in range(0, len(prediction), 3):
                x = prediction[i]
                y = prediction[i + 1]
                if x > 0.0001 and y > 0.0001:
                    coordinates.append((x, y))
            return coordinates
    else:
        print("You sent a packet!")


if __name__ == "__main__":
    main()
