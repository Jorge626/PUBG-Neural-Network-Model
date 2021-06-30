import torch
import json
import pandas as pd
import datetime


# Reads in the json file from wireshark and returns a list of timestamps and the byte data
def get_bytes_list(network_traffic_file):
    with open(network_traffic_file) as file:
        data = json.load(file)
        byte_data = []
        timestamps = []
        for packet in data:
            timestamp = packet['_source']['layers']['frame']['frame.time'][13:28]
            timestamps.append(timestamp)
            packet_bytes = packet['_source']['layers']['data']['data.data']
            byte_data.append(packet_bytes)
        file.close()

    return byte_data, timestamps


# Reads in the csv file for player positions and returns a list while dropping the header row
def get_players_pos_list(player_pos_file):
    df = pd.read_csv(player_pos_file)
    df = df.drop([0], axis=0)
    df_list = df.values.tolist()
    return df_list


# Takes in two files, one json from wireshark and another csv from player positions and returns the data in tensors
def get_tensors(player_pos_file, network_traffic_file):
    data, timestamps = get_bytes_list(network_traffic_file)
    final_byte_data = []
    for byte_string in data:
        byte_row = []
        for i in range(0, len(byte_string), 3):
            string = byte_string[i:i+2]
            bit = int(string, 16)
            bit = float(bit)
            bit /= 240.0
            byte_row.append(bit)
        if len(byte_row) < 756:
            for j in range(756 - len(byte_row)):
                byte_row.append(float(0.0))
        final_byte_data.append(byte_row)

    player_pos = get_players_pos_list(player_pos_file)
    final_player_pos = []
    datetime_thresh_max = datetime.timedelta(milliseconds=900)
    datetime_thresh_min = datetime.timedelta(milliseconds=0)
    it = 0
    for timestamp in timestamps:
        hr = int(timestamp[:2])
        mins = int(timestamp[3:5])
        sec = int(timestamp[6:8])
        mill = int(timestamp[9:])
        datetime_key = datetime.time(hr, mins, sec, mill)
        datetime_key = datetime.datetime.combine(datetime.date(1, 1, 1), datetime_key)

        for positions in player_pos[it:]:
            hr = int(positions[0][11:13])
            mins = int(positions[0][14:16])
            sec = int(positions[0][17:19])
            mill = positions[0][20:23]
            if ':' in mill:
                mill = 0
            else:
                mill = int(mill)
            datetime_player = datetime.time(hr, mins, sec, mill)
            datetime_player = datetime.datetime.combine(datetime.date(1, 1, 1), datetime_player)
            time_diff = datetime_key - datetime_player
            if datetime_thresh_min <= time_diff <= datetime_thresh_max:
                player_pos_row = []
                for i in range(1, 316, 3):
                    if i >= len(player_pos[0]):
                        player_pos_row.append(float(0.0))
                        player_pos_row.append(float(0.0))
                        player_pos_row.append(float(0.0))
                    elif player_pos[it][i] == '':
                        player_pos_row.append(float(0.0))
                        player_pos_row.append(float(0.0))
                        player_pos_row.append(float(0.0))
                    else:
                        player_pos_row.append(float(player_pos[it][i]))
                        player_pos_row.append(float(player_pos[it][i + 1]))
                        player_pos_row.append(float(player_pos[it][i + 2]))
                break
            elif time_diff < datetime_thresh_max:
                break
            it += 1
        final_player_pos.append(player_pos_row)

    x = torch.FloatTensor(final_byte_data)
    y = torch.FloatTensor(final_player_pos)
    return x, y
