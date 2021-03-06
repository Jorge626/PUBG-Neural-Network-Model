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


def get_season_squad_match_ids(player, season):
    player_season = season.get_player(player.id)
    it = 0
    print("Squad Match IDS\n~~~~~~~~~~~~~~")
    for ids in player_season.match_ids("squad", "fpp"):
        print("ID {0}: {1}".format(it, ids))
        it += 1
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    return player_season.match_ids("squad", "fpp")[0]


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
    phase_change = telemetry.filter_by("log_phase_change")
    print("Care Package Spawn: {0}".format(phase_change))
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
        "match_playback.html",
        zoom=True,
        labels=True,
        label_players=["Oogie_", "V0ida"],
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
