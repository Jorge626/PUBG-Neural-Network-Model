from chicken_dinner.pubgapi import PUBG
import pubg_info
import pubg_csv
import pubg_plots


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
    players = pubg.players_from_names(["Oogie_", "V0ida"])
    Oogie_ = players[0]
    current_season = pubg.current_season()
    match_id = pubg_info.get_season_duo_match_ids(Oogie_, current_season)
    match = pubg.match(match_id)
    telemetry = match.get_telemetry()
    # pubg_info.create_playback(telemetry)
    # csv_file_name = pubg_csv.player_position_csv(telemetry)
    # pubg_csv.fill_csv(csv_file_name)
    # pubg_plots.plot_player(csv_file_name, 'Oogie_')
    pubg_plots.plot_bit_len_vs_players('6_23_21_1458.json', 'csv_player_pos.csv', 'Oogie_')


if __name__ == "__main__":
    main()
