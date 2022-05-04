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

    # This block of code gets players as well as current season, used to get match id of latest game played by player

    players = pubg.players_from_names(["Oogie_"])
    Oogie_ = players[0]
    current_season = pubg.current_season()
    # match_id = pubg_info.get_season_duo_match_ids(Oogie_, current_season)

    # This line of code is used if you have the match id of a certain match.
    match_id = pubg.match('d5957ce8-ae38-4460-9ad5-048663424955')

    # This block of code creates a csv file for player positions given the match_id. User must manually enter file
    # location for csv in second parameter.
    telemetry = match_id.get_telemetry()
    pubg_csv.player_position_csv(telemetry, 'PlayerPositions/player_pos_7_22_1518.csv')
    pubg_csv.fill_csv('PlayerPositions/player_pos_7_22_1518.csv')

    # This line of code creates tensors for player positions: x for byte data and y for player positions. It also
    # returns a list of timestamps that match the packet received and player positions at that timestamp
    x, y, timestamps = pubg_tensors.get_tensors('PlayerPositions/player_pos_7_22_1134.csv', 'NetworkPackets/packets_7_22_1134.json')

    # This block of code either prepares the data for training the model or for evaluating the predicted coordinates
    # User most comment one out for whatever they are trying to do.
    # timestamps = preparedata.prepare_data_training(x, y, timestamps)
    preparedata.prepare_data_valuation(x, y)

    # This block of code creates a csv file for the timestamps
    csv_writer = csv.writer(open('tensor_timestamps.csv', 'w', newline=''))
    for timestamp in timestamps:
        csv_writer.writerow([timestamp])


if __name__ == "__main__":
    main()
