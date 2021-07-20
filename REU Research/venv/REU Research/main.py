from chicken_dinner.pubgapi import PUBG
import pubg_info
import pubg_csv
import pubg_plots
import pubg_tensors
import preparedata
import csv


# Main function
def main():
    api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9" \
              ".eyJqdGkiOiJkZmFlNjgwMC1hYjk0LTAxMzk" \
              "tZTQ1ZC0wMDcxY2ZkMzhmMTQiLCJpc3MiOiJ" \
              "nYW1lbG9ja2VyIiwiaWF0IjoxNjIzMjcyOTU" \
              "2LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjo" \
              "icHViZyIsImFwcCI6Im5zZi1yZXUtcmVzZWF" \
              "yIn0.uZbZugduaGpgeVvSZ2Of4e9k7qMZm-C" \
              "kKKcZW2R_aAM "
    pubg = PUBG(api_key, "pc-na")

    # players = pubg.players_from_names(["Oogie_", "V0ida"])
    # Oogie_ = players[1]
    # current_season = pubg.current_season()
    # match_id = pubg_info.get_season_duo_match_ids(Oogie_, current_season)

    # match = pubg.match('68722bc8-6749-4337-a6a2-cfff18aafc18')
    # telemetry = match.get_telemetry()
    # pubg_csv.player_position_csv(telemetry, 'PlayerPositions/player_pos_7_19_1348.csv')
    # pubg_csv.fill_csv('PlayerPositions/player_pos_7_19_1348.csv')

    x, y, timestamps = pubg_tensors.get_tensors('PlayerPositions/player_pos_7_19_1348.csv', 'NetworkPackets/packets_7_19_1348.json')

    # timestamps = preparedata.prepare_data_training(x, y, timestamps)
    preparedata.prepare_data_valuation(x, y)
    csv_writer = csv.writer(open('tensor_timestamps.csv', 'w', newline=''))
    for timestamp in timestamps:
        csv_writer.writerow([timestamp])
    print('Timestamps length: {0}'.format(len(timestamps)))


if __name__ == "__main__":
    main()
