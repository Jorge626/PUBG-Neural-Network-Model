import matplotlib.pyplot as plt
import pandas as pd
import json
import datetime
import csv


# Plots player position on a line graph
def plot_player(file_name, player_name):
    df = pd.read_csv(file_name)
    plt.style.use('seaborn')
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('\'{0}\' Coordinates'.format(player_name))
    plt.plot(df[player_name + '_x'], df[player_name + '_y'], '-')
    plt.axvline(0, c='black', ls='--')
    plt.axhline(0, c='black', ls='--')
    plt.show()


def plot_bit_len_vs_players(json_file, csv_file, player_name):
    with open(json_file) as file:
        data = json.load(file)
        packets = {}
        ticks = []
        total_bytes = []
        count = 0
        for packet in data:
            key = packet['_source']['layers']['frame']['frame.time'][13:28]
            value = int(packet['_source']['layers']['data']['data.len'])
            packets[key] = value
            count += 1
            ticks.append(count)
            total_bytes.append(value)
        file.close()

    df = pd.read_csv(csv_file)
    csv_timestamps = df['timestamp']
    csv_reader = csv.reader(open(csv_file))
    csv_list = list(csv_reader)
    player_index = csv_list[0].index(player_name + '_x')
    date = datetime.date(1, 1, 1)
    datetime_thresh_max = datetime.timedelta(milliseconds=100)
    datetime_thresh_min = datetime.timedelta(milliseconds=0)
    nearby_10 = []
    nearby_50 = []
    nearby_100 = []
    nearby_200 = []
    nearby_500 = []
    nearby_1000 = []
    it = 0
    for key in packets:
        hr = int(key[:2])
        mins = int(key[3:5])
        sec = int(key[6:8])
        mill = int(key[9:])
        datetime_key = datetime.time(hr, mins, sec, mill)
        datetime_key = datetime.datetime.combine(date, datetime_key)

        total_10 = 0
        total_50 = 0
        total_100 = 0
        total_200 = 0
        total_500 = 0
        total_1000 = 0
        for timestamp in csv_timestamps[it:]:
            it += 1
            hr = int(timestamp[11:13])
            mins = int(timestamp[14:16])
            sec = int(timestamp[17:19])
            mill = timestamp[20:23]
            if ':' in mill:
                mill = 0
            else:
                mill = int(mill)
            datetime_player = datetime.time(hr, mins, sec, mill)
            datetime_player = datetime.datetime.combine(date, datetime_player)
            time_diff = datetime_key - datetime_player
            if datetime_thresh_min <= time_diff <= datetime_thresh_max:
                if csv_list[it][player_index] == '':
                    continue
                else:
                    player_x = float(csv_list[it][player_index])
                    player_y = float(csv_list[it][player_index + 1])
                    player_z = float(csv_list[it][player_index + 2])
                    for i in range(1, len(csv_list[0]), 3):
                        if i == player_index:
                            continue
                        elif csv_list[it][i] == '':
                            continue
                        else:
                            x = float(csv_list[it][i])
                            y = float(csv_list[it][i + 1])
                            z = float(csv_list[it][i + 2])
                            x_diff = player_x - x
                            y_diff = player_y - y
                            z_diff = player_z - z
                            if -10 < x_diff < 10 and -10 < y_diff < 10 and -10 < z_diff < 10:
                                total_10 += 1
                            if -50 < x_diff < 50 and -50 < y_diff < 50 and -50 < z_diff < 50:
                                total_50 += 1
                            if -100 < x_diff < 100 and -100 < y_diff < 100 and -100 < z_diff < 100:
                                total_100 += 1
                            if -200 < x_diff < 200 and -200 < y_diff < 200 and -200 < z_diff < 200:
                                total_200 += 1
                            if -500 < x_diff < 500 and -500 < y_diff < 500 and -500 < z_diff < 50:
                                total_500 += 1
                            if -1000 < x_diff < 1000 and -1000 < y_diff < 1000 and -1000 < z_diff < 1000:
                                total_1000 += 1

            elif time_diff < datetime_thresh_max:
                break

        nearby_10.append(total_10)
        nearby_50.append(total_50)
        nearby_100.append(total_100)
        nearby_200.append(total_200)
        nearby_500.append(total_500)
        nearby_1000.append(total_1000)

    plt.style.use('seaborn')
    plt.xlabel('Ticks')
    plt.ylabel('Total Bytes/Players')
    plt.title('Total Bytes and Nearby Players')
    plt.plot(ticks, total_bytes, color='b', marker='.', label='Total Bytes')
    plt.plot(ticks, nearby_10, color='w', linewidth=3, label='Players within 10 meters')
    plt.plot(ticks, nearby_50, color='g', linewidth=2, label='Players within 50 meters')
    plt.plot(ticks, nearby_100, color='r', label='Players within 100 meters')
    plt.plot(ticks, nearby_200, color='c', label='Players within 200 meters')
    plt.plot(ticks, nearby_500, color='m', label='Players within 500 meters')
    plt.plot(ticks, nearby_1000, color='k', label='Players within 1000 meters')
    plt.legend()
    plt.tight_layout()
    plt.show()

    data = [total_bytes, nearby_10, nearby_50, nearby_100, nearby_200, nearby_500, nearby_1000]
    csv_writer = csv.writer(open('bytes_vs_nearby_players.csv', 'w', newline=''))
    csv_writer.writerows(data)
