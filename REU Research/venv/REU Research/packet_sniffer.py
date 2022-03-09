import scapy.all as scapy
import time
from scapy.layers import http


# Port used in training: udp port 4380 or udp portrange 27000-27040
# Full PUBG ports: tcp portrange 27015-27030 or tcp portrange 27037 or udp port 4380 or udp portrange 27000-27031 or
# udp port 27036
def main():
    packets = scapy.sniff(count=1, filter="udp port 4380 or udp portrange 27000-27040")
    # print(packets)
    packets.show()
    packets.nsummary()
    packets.hexdump()

    for packet in packets:
        packet.show()
        # packet.nsummary()
        # packet.hexdump()
        print(packet.payload.src)
        print(packet.payload.payload.payload.load)


if __name__ == "__main__":
    main()
