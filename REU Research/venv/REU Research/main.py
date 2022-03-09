from chicken_dinner.pubgapi import PUBG
import packet_sniffer
import pubg_info
import pubg_csv
import pubg_plots
import pubg_tensors
import preparedata
import csv


# Main function
def main():
    api_key = ""
    pubg = PUBG(api_key, "pc-na")

    # players = pubg.players_from_names(["Oogie_", "V0ida"])
    # Oogie_ = players[1]
    # current_season = pubg.current_season()
    # match_id = pubg_info.get_season_duo_match_ids(Oogie_, current_season)

    # match = pubg.match('d5957ce8-ae38-4460-9ad5-048663424955')
    # telemetry = match.get_telemetry()
    # pubg_csv.player_position_csv(telemetry, 'PlayerPositions/player_pos_7_22_1518.csv')
    # pubg_csv.fill_csv('PlayerPositions/player_pos_7_22_1518.csv')

    x, y, timestamps = pubg_tensors.get_tensors('PlayerPositions/player_pos_7_22_1134.csv', 'NetworkPackets/packets_7_22_1134.json')

    # timestamps = preparedata.prepare_data_training(x, y, timestamps)
    preparedata.prepare_data_valuation(x, y)
    csv_writer = csv.writer(open('tensor_timestamps.csv', 'w', newline=''))
    for timestamp in timestamps:
        csv_writer.writerow([timestamp])


if __name__ == "__main__":
    main()
