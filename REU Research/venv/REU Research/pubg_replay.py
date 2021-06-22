from chicken_dinner.pubgapi import PUBG
import csv
import pandas as pd
import matplotlib.pyplot as plt


# Displays player info
def get_player_info(player):
    print("Player Info\n~~~~~~~~~~~")
    print("Player name: " + player.name)
    print("Player ID: " + player.id)
    print("Player URL: " + player.url)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# Displays solo stats fpp
def get_solo_stats(player):
    player_season = player.get_current_season()
    solo_fpp_stats = player_season.game_mode_stats("solo", "fpp")
    print("Solo First Person Perspective Stats\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for key, value in solo_fpp_stats.items():
        print("{0}: {1}".format(key, value))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# Displays duo stats fpp
def get_duo_stats(player):
    player_season = player.get_current_season()
    duo_fpp_stats = player_season.game_mode_stats("duo", "fpp")
    print("Duo First Person Perspective Stats\n~~~~~~~~~~~~~~~~~~~~~~\n")
    for key, value in duo_fpp_stats.items():
        print("{0}: {1}".format(key, value))


# Displays squad stats fpp
def get_squad_stats(player):
    player_season = player.get_current_season()
    squad_fpp_stats = player_season.game_mode_stats("squad", "fpp")
    print("Squad First Person Perspective Stats\n~~~~~~~~~~~~~~~~~~~~~~\n")
    for key, value in squad_fpp_stats.items():
        print("{0}: {1}".format(key, value))


# Displays solo season match ID's fpp & returns latest match ID
def get_season_solo_match_ids_fpp(player, season):
    player_season = season.get_player(player.id)
    it = 0
    print("Solo Match IDS\n~~~~~~~~~~~~~~")
    for ids in player_season.match_ids("solo", "fpp"):
        print("ID {0}: {1}".format(it, ids))
        it += 1
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    return player_season.match_ids("solo", "fpp")[0]


# Displays solo season match tpp ID's & returns latest match ID
def get_season_solo_match_ids_tpp(player, season):
    player_season = season.get_player(player.id)
    it = 0
    print("Solo Match IDS\n~~~~~~~~~~~~~~")
    for ids in player_season.match_ids("solo", "tpp"):
        print("ID {0}: {1}".format(it, ids))
        it += 1
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    return player_season.match_ids("solo", "tpp")[0]


# Displays solo seasons match ID's for both fpp and tpp and returns latest match ID
def get_season_solo_match_ids(player, season):
    player_season = season.get_player(player.id)
    it = 0
    print("Solo Match IDS\n~~~~~~~~~~~~~~")
    for ids in player_season.match_ids("solo"):
        print("ID {0}: {1}".format(it, ids))
        it += 1
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    return player_season.match_ids("solo")[0]


# Displays season match ID's & returns latest match ID
def get_season_duo_match_ids(player, season):
    player_season = season.get_player(player.id)
    it = 0
    print("Duo Match IDS\n~~~~~~~~~~~~~~")
    for ids in player_season.match_ids("duo", "fpp"):
        print("ID {0}: {1}".format(it, ids))
        it += 1
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    return player_season.match_ids("duo", "fpp")[0]


# Displays match info
def get_match_id_info(match):
    print("Match Info\n~~~~~~~~~~")
    print("Match ID = {0}".format(match.id))
    print("Match Asset: {0}".format(match.asset_id))
    print("Date Created: {0}".format(match.created_at))
    print("Match Duration: {0}".format(match.duration))
    print("Game Mode: {0}".format(match.game_mode))
    print("Custom Game: {0}".format(match.is_custom))
    print("Map ID: {0}".format(match.map_id))
    print("Map Name: {0}".format(match.map_name))
    print("Match Roster: {0}".format(match.rosters_player_names))
    print("Telemetry URL: {0}".format(match.telemetry_url))
    print("Match URL: {0}".format(match.url))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# Displays telemetry info
def get_telemetry_info(telemetry):
    print("Match Info\n~~~~~~~~~~")
    print("All event types: {0}".format(telemetry.event_types()))
    # Can filter by any event, this case I filter by care package for example
    care_package_spawn = telemetry.filter_by("log_player_position")
    print("Care Package Spawn: {0}".format(care_package_spawn))
    print("Telemetry Map ID: {0}".format(telemetry.map_id()))
    print("Telemetry Map Name: {0}".format(telemetry.map_name()))
    print("Number of Players: {0}".format(telemetry.num_players()))
    print("Number of Teams: {0}".format(telemetry.num_teams()))
    print("Platform: {0}".format(telemetry.platform))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# Displays event info
def get_events_info(telemetry):
    events = telemetry.events
    event = events[0]
    print("Event Info\n~~~~~~~~~~")
    print("Event Type: {0}".format(event.event_type))
    print("Event Timestamp: {0}".format(event.timestamp))
    print("Event as Dictionary: {0}".format(event.to_dict()))
    print("Event Dumps: {0}".format(event.dumps()))
    print("Ping Quality: {0}".format(event.ping_quality))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# Displays event info as an object
def get_objects_info(telemetry):
    print("Event as Object Info\n~~~~~~~~~~~~~~~~~~~~")
    kill_events = telemetry.filter_by("log_player_kill")
    kill = kill_events[0]
    print("Event type: {0}".format(kill))
    print("Event Keys: {0}".format(kill.keys()))
    killer = kill.killer
    print("Telemetry Object: {0}".format(killer))
    print("Object Keys: {0}".format(killer.keys()))
    print("Object Name: {0}".format(killer.name))
    victim = kill.victim
    print("Telemetry Object: {0}".format(victim))
    print("Object Keys: {0}".format(victim.keys()))
    print("Object Name: {0}".format(victim.name))
    print("Object as Dictionary: {0}".format(victim.to_dict()))
    print("Object Items: ")
    for key, value in victim.items():
        print("{0}: {1}".format(key, value))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# Generates an HTML5 animation with ffmpeg
def create_playback(telemetry):
    print("Creating playback...")
    telemetry.playback_animation(
        "match_playback3.html",
        zoom=True,
        labels=True,
        label_players=["Oogie_", "Thats_Schnic3"],
        highlight_winner=True,
        label_highlights=True,
        size=6,
        end_frames=60,
        use_hi_res=False,
        color_teams=True,  # use True for teams, False for solos
        interpolate=True,
        damage=True,
        interval=2,
        fps=30,
    )
    print("Playback created!")


# Creates a csv file of player positions given telemetry object
def player_position_csv(telemetry):
    csv_file_name = 'csv_player_pos.csv'
    new_file = open(csv_file_name, 'w', newline='')
    csv_header = ['timestamp']
    for i in range(1, 102):
        csv_header.append('player{0}_x'.format(i))
        csv_header.append('player{0}_y'.format(i))
        csv_header.append('player{0}_z'.format(i))

    csv_writer = csv.DictWriter(new_file, fieldnames=csv_header, restval="")
    csv_writer.writeheader()

    player_positions = telemetry.filter_by("log_player_position")
    characters = []
    timestamps = []
    for players in player_positions:
        current_character_name = players.character.name
        if current_character_name not in characters:
            characters.append(current_character_name)
        timestamp = players.timestamp[:19]
        if timestamp not in timestamps:
            timestamps.append(timestamp)
            csv_writer.writerow({'timestamp': timestamp})

    new_file.close()
    csv_reader = csv.reader(open(csv_file_name))
    csv_list = list(csv_reader)

    for timestamp in timestamps:
        for players in player_positions:
            if players.timestamp[:19] == timestamp:
                character_name = players.character.name
                character_index = characters.index(character_name)
                start_index = (character_index * 2) + (character_index + 1)
                time_index = timestamps.index(timestamp) + 1
                csv_list[time_index][start_index] = character_name + '_x:' + str(players.character.location.x)
                csv_list[time_index][start_index + 1] = character_name + '_y:' + str(players.character.location.y)
                csv_list[time_index][start_index + 2] = character_name + '_z:' + str(players.character.location.z)

    csv_writer = csv.writer(open(csv_file_name, 'w', newline=''))
    csv_writer.writerows(csv_list)
    return csv_file_name


# Updates csv file so that the csv file has previous known player positions
def update_player_positions(file_name):
    csv_reader = csv.reader(open(file_name))
    csv_list = list(csv_reader)

    for rows in range(2, len(csv_list)):
        for columns in range(len(csv_list[rows])):
            if csv_list[rows][columns] == '' and csv_list[rows - 1][columns] != '':
                csv_list[rows][columns] = csv_list[rows - 1][columns]

    csv_writer = csv.writer(open(file_name, 'w', newline=''))
    csv_writer.writerows(csv_list)


def plot_player(file_name, player_num):
    start_index = (player_num * 2) + (player_num + 1)
    csv_reader = csv.reader(open(file_name))
    csv_list = list(csv_reader)
    x = []
    y = []
    char_name = ''
    for rows in range(1, len(csv_list)):
        if csv_list[rows][start_index] != '':
            split = csv_list[rows][start_index].index(':') + 1
            x_ = csv_list[rows][start_index][split:]
            y_ = csv_list[rows][start_index + 1][split:]
            if x_ not in x and y_ not in y:
                x.append(float(x_))
                y.append(float(y_))
            if char_name == '':
                split = csv_list[rows][start_index].index('_x')
                char_name = csv_list[rows][start_index][:split]

    plt.style.use('seaborn')
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('\'{0}\' Coordinates'.format(char_name))
    plt.plot(x, y)
    plt.axvline(0, c='black', ls='--')
    plt.axhline(0, c='black', ls='--')
    plt.tight_layout()
    plt.show()


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
    players = pubg.players_from_names(["Oogie_"])
    Oogie_ = players[0]
    # get_player_info(Oogie_)
    # get_solo_stats(Oogie_)
    current_season = pubg.current_season()
    # match_id = get_season_solo_match_ids(Oogie_, current_season)
    # match_id = get_season_solo_match_ids_tpp(Oogie_, current_season)
    match_id = get_season_duo_match_ids(Oogie_, current_season)
    match = pubg.match(match_id)
    # get_match_id_info(match)
    telemetry = match.get_telemetry()
    # get_telemetry_info(telemetry)
    # get_events_info(telemetry)
    # get_objects_info(telemetry)
    # create_playback(telemetry)
    csv_file_name = player_position_csv(telemetry)
    update_player_positions(csv_file_name)
    plot_player('csv_player_pos.csv', 56)


if __name__ == "__main__":
    main()
