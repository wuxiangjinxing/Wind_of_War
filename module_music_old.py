from header_music import *
####################################################################################################################
#  Each track record contains the following fields:
#  1) Track id: used for referencing tracks.
#  2) Track file: filename of the track
#  3) Track flags. See header_music.py for a list of available flags
#  4) Continue Track flags: Shows in which situations or cultures the track can continue playing. See header_music.py for a list of available flags
####################################################################################################################

# WARNING: You MUST add mtf_module_track flag to the flags of the tracks located under module directory

tracks = [
##  ("losing_battle", "alosingbattle.mp3", sit_calm|sit_action),
##  ("reluctant_hero", "reluctanthero.mp3", sit_action),
##  ("the_great_hall", "thegreathall.mp3", sit_calm),
##  ("requiem", "requiem.mp3", sit_calm),
##  ("silent_intruder", "silentintruder.mp3", sit_calm|sit_action),
##  ("the_pilgrimage", "thepilgrimage.mp3", sit_calm),
##  ("ambushed", "ambushed.mp3", sit_action),
##  ("triumph", "triumph.mp3", sit_action),

##  ("losing_battle", "alosingbattle.mp3", mtf_sit_map_travel|mtf_sit_attack),
##  ("reluctant_hero", "reluctanthero.mp3", mtf_sit_attack),
##  ("the_great_hall", "thegreathall.mp3", mtf_sit_map_travel),
##  ("requiem", "requiem.mp3", mtf_sit_map_travel),
##  ("silent_intruder", "silentintruder.mp3", mtf_sit_map_travel|mtf_sit_attack),
##  ("the_pilgrimage", "thepilgrimage.mp3", mtf_sit_map_travel),
##  ("ambushed", "ambushed.mp3", mtf_sit_attack),
##  ("triumph", "triumph.mp3", mtf_sit_attack),
  ("bogus", "cant_find_this.ogg", 0, 0),
  ("Mainmenu_1", "Mainmenu.mp3", mtf_module_track|mtf_sit_main_title|mtf_start_immediately, 0),
  ("Mainmenu_2", "main_menu.mp3", mtf_module_track|mtf_sit_main_title|mtf_start_immediately, 0),
  ("Mainmenu_3", "MainMenuWoG.mp3", mtf_module_track|mtf_sit_main_title|mtf_start_immediately, 0),

  ("fight_music_1", "Combat01.mp3",  mtf_sit_siege|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, 0),
  ("fight_music_2", "Combat02.mp3",  mtf_sit_arena|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, 0),
  ("fight_music_3", "Combat03.mp3",  mtf_sit_siege|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, 0),
  ("fight_music_4", "Combat04.mp3",  mtf_sit_arena|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, 0),

  ("ambushed_by_neutral", "Combat01.mp3", mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_multiplayer_fight),
  ("ambushed_by_khergit", "Battle_Stronghold1.mp3", mtf_culture_3|mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
  ("ambushed_by_nord",    "elves_amb3.ogg", mtf_culture_4|mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
  ("ambushed_by_rhodok",  "Battle_Undead1.mp3", mtf_culture_5|mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
  ("ambushed_by_swadian", "Battle_Haven1.mp3", mtf_culture_1|mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
  ("ambushed_by_vaegir",  "Battle_Fortress1.mp3", mtf_culture_2|mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
  ("ambushed_by_sarranid", "Battle_Inferno1.mp3", mtf_culture_6|mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),


  ("arena_1", "Combat02.mp3", mtf_sit_arena|mtf_module_track, 0),
  #("arena_2", "Combat02.mp3", mtf_looping|mtf_sit_arena|mtf_module_track, 0),
  ("armorer", "armorer.ogg", mtf_sit_travel, 0),
  ("bandit_fight", "bandit_fight.ogg", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),

  #("calm_night_1", "calm_night_2.ogg", mtf_sit_night, mtf_sit_town|mtf_sit_tavern|mtf_sit_travel),
  ("calm_night_1", "AITheme0.mp3", mtf_sit_night|mtf_module_track, mtf_sit_town|mtf_sit_tavern|mtf_sit_travel),
  ("calm_night_2", "Aitheme1.mp3", mtf_sit_night|mtf_module_track, mtf_sit_town|mtf_sit_tavern|mtf_sit_travel),
  ("calm_night_3", "CampainMusic02.mp3", mtf_sit_night|mtf_module_track, mtf_sit_town|mtf_sit_tavern|mtf_sit_travel),
  #("captured", "capture.ogg", mtf_persist_until_finished, 0),
  ("captured", "UltimateLose.mp3", mtf_persist_until_finished|mtf_module_track, 0),
  
  ("defeated_by_neutral", "defeated_by_neutral.ogg",mtf_persist_until_finished|mtf_sit_killed, 0),
  ("defeated_by_neutral_2", "defeated_by_neutral_2.ogg", mtf_persist_until_finished|mtf_sit_killed, 0),
  ("defeated_by_neutral_3", "defeated_by_neutral_3.ogg", mtf_persist_until_finished|mtf_sit_killed, 0),

  ("empty_village", "empty_village.ogg", mtf_persist_until_finished|mtf_module_track, 0),
  ("encounter_hostile_nords", "encounter_hostile_nords.ogg", mtf_persist_until_finished|mtf_sit_encounter_hostile, 0),
  #("escape", "escape.ogg", mtf_persist_until_finished, 0),
  ("escape", "Surrende_Battle.mp3", mtf_persist_until_finished|mtf_module_track, 0),
## CC
  #("music_old_1", "triumph.mp3",        mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, 0),
  #("music_old_2", "alosingbattle.mp3",  mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, 0),
  #("music_old_3", "ambushed.mp3",       mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, 0),
  #("music_old_4", "reluctanthero.mp3",  mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, 0),
## CC

  ("fight_1", "First_Battle.mp3", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, 0),
  ("fight_2", "Sword_and_Faith.mp3", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, 0),
  ("fight_3", "Crusade.mp3", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, 0),
  ("fight_as_khergit", "Battle_Stronghold2.mp3", mtf_culture_3|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, mtf_culture_all),
  ("fight_4",  "Last_Fortress.mp3", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, 0),  
  ("fight_5",  "The_Die_is_Cast.mp3", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, 0),  
  ("fight_as_nord", "elves_battle1.ogg", mtf_culture_4|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, mtf_culture_all),
  ("fight_as_rhodok", "Battle_Undead1.mp3", mtf_culture_5|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, mtf_culture_all),
  ("fight_as_swadian", "Battle_Haven2.mp3", mtf_culture_1|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_module_track, mtf_culture_all),

  ("fight_as_vaegir", "Battle_Fortress2.mp3", mtf_culture_2|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, mtf_culture_all),
  ("fight_as_sarranid", "Battle_Inferno2.mp3", mtf_culture_6|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, mtf_culture_all),
  
  ("fight_while_mounted_1", "Pride_or_Pain.mp3",  mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, 0),
  ("fight_while_mounted_2", "Swadian_Riders.mp3",  mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, 0),
  ("fight_while_mounted_3", "March_of_Honor.mp3", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, 0),
  
  ("infiltration_khergit", "infiltration_khergit.ogg", mtf_culture_3|mtf_sit_town_infiltrate, mtf_culture_all),

  ("killed_by_khergit", "killed_by_khergit.ogg", mtf_persist_until_finished|mtf_culture_3|mtf_sit_killed, 0),
  ("killed_by_swadian", "killed_by_swadian.ogg", mtf_persist_until_finished|mtf_culture_1|mtf_sit_killed, 0),
  
  ("lords_hall_khergit", "lords_hall_khergit.ogg", mtf_culture_3|mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern|mtf_culture_all),
  ("lords_hall_music", "Castle_Dance.mp3",   mtf_sit_travel|mtf_module_track, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),
  ("lords_hall_music2", "thegreathall.mp3", mtf_sit_travel|mtf_module_track, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),

  
  ("travel_music_1", "Bard's_Tale.mp3",   mtf_sit_town|mtf_sit_travel|mtf_sit_feast|mtf_module_track, mtf_sit_tavern|mtf_sit_night),
  ("travel_music_2", "Braveheart.mp3",    mtf_sit_town|mtf_sit_travel|mtf_module_track, mtf_sit_tavern|mtf_sit_night),
  ("travel_music_3", "New_Begining.mp3",  mtf_sit_town|mtf_sit_travel|mtf_module_track, mtf_sit_tavern),
  ("travel_music_4", "Where_my_Heart_is.mp3",  mtf_sit_town|mtf_sit_travel|mtf_module_track, mtf_sit_tavern|mtf_sit_night),
  ("travel_music_5", "Water.mp3",         mtf_sit_town|mtf_sit_travel|mtf_module_track, 0),

  ("travel_music_6", "Dove_in_the_Sky.mp3",  mtf_sit_town|mtf_sit_travel|mtf_sit_night|mtf_module_track, 0),
  ("travel_music_7", "Handful_of_Sorrow.mp3",  mtf_sit_town|mtf_sit_travel|mtf_module_track, mtf_sit_tavern|mtf_sit_night),
  ("travel_music_8", "minstrelosity.mp3",  mtf_sit_town|mtf_sit_travel|mtf_module_track, mtf_sit_tavern),
  

  
  ("retreat", "Retreat_Battle.mp3", mtf_persist_until_finished|mtf_sit_killed|mtf_module_track, 0),
  ("retreat_2", "Surrende_Battle.mp3", mtf_persist_until_finished|mtf_sit_killed|mtf_module_track, 0),
  ("retreat_3", "LoseCombat.mp3", mtf_persist_until_finished|mtf_sit_killed|mtf_module_track, 0),

  ("seige_neutral", "seige_neutral.wma",               mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed),
  ("enter_the_juggernaut", "enter_the_juggernaut.wma", mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed),  
  ("crazy_battle_music", "crazy_battle_music.wma",     mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed),
  ("fight_music_1", "Combat01.mp3",  mtf_sit_siege|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, 0),
  ("fight_music_2", "Combat02.mp3",  mtf_sit_arena|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, 0),
  ("fight_music_3", "Combat03.mp3",  mtf_sit_siege|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, 0),
  ("fight_music_4", "Combat04.mp3",  mtf_sit_arena|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, 0),

  ("tavern_1", "Echo_in_Eternity.mp3",   mtf_sit_tavern|mtf_sit_feast|mtf_module_track, 0),
  ("tavern_2", "NeutralTheme.mp3",   mtf_sit_tavern|mtf_sit_feast|mtf_module_track, 0),
    
  ("town_neutral", "ElemTown.mp3", mtf_module_track|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night),
  ("town_khergit", "StrongHold.mp3", mtf_module_track|mtf_culture_3|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("town_nord", "Rampart.mp3", mtf_module_track|mtf_culture_4|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("town_rhodok", "necroTown.mp3", mtf_module_track|mtf_culture_5|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("town_swadian", "CstleTown.mp3", mtf_module_track|mtf_culture_1|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("town_vaegir", "TowerTown.mp3", mtf_module_track|mtf_culture_2|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("town_sarranid", "InfernoTown.mp3", mtf_module_track|mtf_culture_6|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),


  ("travel_khergit", "Dirt.mp3", mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_neutral", "Grass.mp3", mtf_module_track|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night),
  ("travel_nord",    "travel_nord.ogg",    mtf_module_track|mtf_culture_4|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_rhodok",  "Rough.mp3",  mtf_module_track|mtf_culture_5|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_swadian", "GoodTheme.mp3", mtf_module_track|mtf_culture_1|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_vaegir",  "Snow.mp3",  mtf_module_track|mtf_culture_2|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_sarranid", "Sand.mp3",          mtf_module_track|mtf_culture_6|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),

  ("travel_rhodok2",  "death.mp3",  mtf_module_track|mtf_culture_5|mtf_sit_town|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_swadian2", "life.mp3", mtf_module_track|mtf_culture_1|mtf_sit_town|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_nord2", "nature.mp3", mtf_module_track|mtf_culture_4|mtf_sit_town|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),



  ("uncertain_homestead", "uncertain_homestead.ogg", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),
  ("hearth_and_brotherhood", "hearth_and_brotherhood.ogg", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),
  ("tragic_village", "tragic_village.ogg", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),

  ("victorious_evil", "victorious_evil.ogg", mtf_persist_until_finished|mtf_start_immediately|mtf_module_track, 0),
  #("victorious_evil", "victorious_evil.ogg", mtf_persist_until_finished, 0),
  ("won_music", "Win_Battle.mp3",             mtf_persist_until_finished|mtf_sit_victorious|mtf_module_track, 0),
  ("won_music_2", "Defend_Castle.mp3",        mtf_persist_until_finished|mtf_sit_victorious|mtf_module_track, 0),
  ("won_music_3", "WinScenario.mp3",          mtf_persist_until_finished|mtf_sit_victorious|mtf_module_track, 0),
  ("won_music_4", "victorious_neutral_1.wma", mtf_persist_until_finished|mtf_sit_victorious|mtf_module_track, 0),
  ("won_music_5", "victorious_neutral_2.wma", mtf_persist_until_finished|mtf_sit_victorious|mtf_module_track, 0),
  ("won_music_6", "victorious_neutral_3.wma", mtf_persist_until_finished|mtf_sit_victorious|mtf_module_track, 0),
  ("won_music_7", "victorious_swadian.wma",   mtf_persist_until_finished|mtf_culture_1|mtf_sit_victorious|mtf_module_track, 0),
  ("won_music_8", "victorious_vaegir.wma",     mtf_persist_until_finished|mtf_culture_2|mtf_sit_victorious|mtf_module_track, 0),
  ("won_music_9", "victorious_vaegir_2.wma", mtf_persist_until_finished|mtf_culture_2|mtf_sit_victorious|mtf_module_track, 0),

  ("wedding", "wedding.ogg", mtf_persist_until_finished, 0),

  #("coronation", "coronation.ogg", mtf_persist_until_finished, 0),
  ("coronation", "WinScenario.ogg", mtf_persist_until_finished|mtf_module_track, 0),
  
]
# modmerger_start version=201 type=4
try:
    component_name = "music"
    var_set = { "tracks":tracks, }
    from modmerger import modmerge
    modmerge(var_set, component_name)
except:
    raise
# modmerger_end
