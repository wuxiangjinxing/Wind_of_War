from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_party_templates import *
from ID_map_icons import *

####################################################################################################################
#  Each party record contains the following fields:
#  1) Party id: used for referencing parties in other files.
#     The prefix p_ is automatically added before each party id.
#  2) Party name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Party-template. ID of the party template this party belongs to. Use pt_none as the default value.
#  6) Faction.
#  7) Personality. See header_parties.py for an explanation of personality flags.
#  8) Ai-behavior
#  9) Ai-target party
# 10) Initial coordinates.
# 11) List of stacks. Each stack record is a triple that contains the following fields:
#   11.1) Troop-id. 
#   11.2) Number of troops in this stack. 
#   11.3) Member flags. Use pmf_is_prisoner to note that this member is a prisoner.
# 12) Party direction in degrees [optional]
####################################################################################################################

no_menu = 0
#pf_town = pf_is_static|pf_always_visible|pf_hide_defenders|pf_show_faction
pf_town = pf_is_static|pf_always_visible|pf_show_faction|pf_label_large
pf_castle = pf_is_static|pf_always_visible|pf_show_faction|pf_label_medium
pf_village = pf_is_static|pf_always_visible|pf_hide_defenders|pf_label_small

#sample_party = [(trp_swadian_knight,1,0), (trp_swadian_peasant,10,0), (trp_swadian_crossbowman,1,0), (trp_swadian_man_at_arms, 1, 0), (trp_swadian_footman, 1, 0), (trp_swadian_militia,1,0)]

# NEW TOWNS:
# NORMANDY: Rouen, Caen, Bayeux, Coutances, Evreux, Avranches
# Brittany: Rennes, Nantes,
# Maine: Le Mans
# Anjou: Angers


parties = [
  ("main_party","Main Party",icon_player|pf_limit_members, no_menu, pt_none,fac_player_faction,0,ai_bhvr_hold,0,(17, 52.5),[(trp_player,1,0)]),
  ("temp_party","{!}temp_party",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
  ("camp_bandits","{!}camp_bandits",pf_disabled, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(1,1),[(trp_temp_troop,3,0)]),
#parties before this point are hardwired. Their order should not be changed.

  ("temp_party_2","{!}temp_party_2",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
#Used for calculating casulties.
  ("temp_casualties","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_casualties_2","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_casualties_3","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_wounded","{!}enemies_wounded",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_killed", "{!}enemies_killed", pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("main_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("encountered_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
#  ("ally_party_backup","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("player_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("ally_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

  ("collective_enemy","{!}collective_enemy",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  #TODO: remove this and move all to collective ally
  ("collective_ally","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
   
  ("total_enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]), #ganimet hesaplari icin #new:
  ("routed_enemies","{!}routed_enemies",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]), #new:  

#  ("village_reinforcements","village_reinforcements",pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

  ("town_merc_1","{!}sargoth_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_2","{!}tihr_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_3","{!}veluca_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_4","{!}suno_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_5","{!}jelkala_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_6","{!}praven_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_7","{!}uxkhal_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_8","{!}reyvadin_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_9","{!}khudan_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_10","{!}tulga_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_11","{!}curaw_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_12","{!}wercheg_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_13","{!}rivacheg_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_14","{!}halmar_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_15","{!}yalen_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_16","{!}dhirim_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_17","{!}ichamur_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_18","{!}narra_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_19","{!}Shariz_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_20","{!}Durquba_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_21","{!}Ahmerrad_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_22","{!}Bariyye_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_23","{!}Ahmerrad_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_24","{!}Bariyye_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_25","{!}Oasis3", pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
 # ("town_merc_26","{!}Oasis4", pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
###############################################################  
  ("zendar","Zendar",pf_disabled|icon_town|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18,60),[]),

  ("town_1","Flammschrein",  icon_city_swadia|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(51.8782,-58.2464),[], 170),
  ("town_2","Veith City",     icon_colony_fortified_c|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(11.9814,-91.0642),[], 120),
  ("town_3","Edgewater",   icon_viking_town_walled|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(78.5312,-108.669),[], 80),
  ("town_4","Claxton",     icon_town_normal|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-124.016,-84.3363),[], 290),
  ("town_5","Dark Eternal",  icon_town_5|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(107.213,112.66),[], 90),
  ("town_6","Volen City",   icon_town_6|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-1.29142,-12.5568),[], 155),
  ("town_7","Jade belt Port",   icon_viking_fort1|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(180.055,-148.595),[], 240),

  ("town_8","Fallen Star", icon_town_snow|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-40.1632,-241.33),[], 175),
  ("town_9","Equinox Port",   icon_viking_snow_town_port|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-5.57971,-167.641),[], 90),
  ("town_10","Emerald Moor",   icon_town_10|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-83.2798,43.3689),[], 310),
  ("town_11","Silverspire",   icon_town_vaegir_khudan|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-99.8678,-168.442),[], 150),
  ("town_12","Greenwood", icon_colony_fortified_a|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(81.9307,8.25315),[], 25),
  ("town_13","Morgan heim",icon_town_volencia|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(163.74,245.08),[], 60),
  ("town_14","Western Hill",  icon_town_14|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-160.06,89.6271),[], 135),

  ("town_15","Ghost wind",  icon_town_15|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(61.5496,151.234),[], 45),
  ("town_16","Green Flatland",  icon_viking_town_port|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(138.583,-136.774),[], 0),
  ("town_17","High Valley",  icon_town_17|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(207.359,176.174),[], 90),
  ("town_18","The LAN",  icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(100.00,239.00),[], 135),

  ("town_19","Dark burrow", icon_town_19|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-24.2556,97.4525),[], 45),
  ("town_20","Moon Island Port", icon_town_20|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(200.0,140.0),[], 270),
  #("town_20","Moon Island Port", icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-178.65,149.352),[], 270),
  ("town_21","Sand flash", icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.1106,140.92),[], 330),
  ("town_22","Oasis", icon_town_22|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(9.19489,209.238),[], 225),
##yifeng add new
  ("town_23","Cloudspire", icon_city_rhodok|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-143.83,-2.01),[], 225),
  ("town_24","Daemon Gate", icon_city_sarranid|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.61,211.09),[], 225),
  ("town_25","Death's Gate", icon_town_normal_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(25.07,77),[], 225),
 # ("town_26","Oasis4", icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(9.19489,209.238),[], 225),


#   Aztaq_Castle       
#  Malabadi_Castle
  ("castle_1","Culmarr_Castle",icon_castle_x_4|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(123.563,76.1891),[],50),
  ("castle_2","Malayurg_Castle",icon_castle_desert_7|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.9751,45.0736),[],75),
  ("castle_3","Bulugha_Castle",icon_castle_x_19|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(83.9533,-243.008),[],100),
  ("castle_4","Radoghir_Castle",icon_castle_wood_3|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(42.4936,-216.108),[],180),
  ("castle_5","Tehlrog_Castle",icon_castle_x_17|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-5.09241,-130.507),[],90),
  ("castle_6","Tilbaut_Castle",icon_castle_x_12|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-56.0588,-72.6165),[],55),
  ("castle_7","Sungetche_Castle",icon_castle_y_1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-9.88624,38.2641),[],45),
  ("castle_8","Jeirbe_Castle",icon_castle_x_2|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(4.5859,-155.605),[],30),
  ("castle_9","Jamiche_Castle",icon_castle_desert_9|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(75.4597,80.5175),[],100),
  ("castle_10","Alburq_Castle",icon_castle_x_12|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-11.4916,-52.6421),[],110), 
  
  ("castle_11","Curin_Castle",icon_castle_x_13|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(49.2966,-1.89536),[],75),
  ("castle_12","Chalbek_Castle",icon_castle_x_22|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(126.23,-55.1208),[],95),
  ("castle_13","Kelredan_Castle",icon_castle_x_22|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-80.4726,-88.3525),[],115),
  ("castle_14","Maras_Castle",icon_castle_hillfort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(157.453,118.504),[],90),
  ("castle_15","Ergellon_Castle",icon_castle_x_5|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(127.737,149.285),[],235),
  ("castle_16","Almerra_Castle",icon_castle_wood_5|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(79.7761,128.071),[],45),
  ("castle_17","Distar_Castle",icon_castle_desert_10|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-26.9329,66.7549),[],260),
  ("castle_18","Ismirala_Castle",icon_castle_y_4|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-8.41715,-206.208),[],300),
  ("castle_19","Yruma_Castle",icon_castle_y_3|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(16.393,-240.713),[],280),
  ("castle_20","Derchios_Castle",icon_castle_x_6|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-193.474,-131.262),[],260),
  
  ("castle_21","Ibdeles_Castle",icon_castle_x_22|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(50.5659,95.8036),[],260),
  ("castle_22","Unuzdaq_Castle",icon_castle_x_3|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(25.914,105.793),[],80),
  ("castle_23","Tevarin_Castle",icon_castle_x_1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-155.812,-109.318),[],80),
  ("castle_24","Reindi_Castle",icon_castle_x_22|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-30.9522,-26.0885),[],260),
  ("castle_25","Ryibelet_Castle",icon_castle_x_16|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-62.8464,-30.5722),[],260),
  ("castle_26","Senuzgda_Castle",icon_castle_x_22|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(169.355,-261.913),[],260),
  ("castle_27","Rindyar_Castle",icon_castle_x_15|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-77.7604,109.221),[],260),
  ("castle_28","Grunwalder_Castle",icon_castle_x_20|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(65.25,196.867),[],260),

  ("castle_29","Nelag_Castle",icon_castle_y_4|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-31.7445,-206.013),[],280),
  ("castle_30","Asugan_Castle",icon_castle_desert_2|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-105.297,25.994),[],100),
  ("castle_31","Vyincourd_Castle",icon_castle_x_17|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(208.81,232.57),[],260),
  ("castle_32","Knudarr_Castle",icon_castle_x_17|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(103.579,37.0756),[],260),
  ("castle_33","Etrosq_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(133.127,206.682),[],80),
  ("castle_34","Hrus_Castle",icon_castle_x_22|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(45.1225,22.2525),[],260),
  ("castle_35","Haringoth_Castle",icon_castle_x_13|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(126.712,-201.869),[],260),
  ("castle_36","Jelbegi_Castle",icon_castle_x_1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(117.328,-5.24083),[],260),
  ("castle_37","Dramug_Castle",icon_castle_hillfort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-72.666,-176.74),[],260),
  ("castle_38","Tulbuk_Castle",icon_castle_desert_7|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-144.355,107.258),[],110),
  ("castle_39","Slezkh_Castle",icon_castle_y_1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-101.943,-226.838),[],280),
  ("castle_40","Uhhun_Castle",icon_castle_desert_10|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-163.882,58.8647),[],95),
  
  ("castle_41","Jameyyed_Castle",icon_castle_desert_3|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(178.129,-173.357),[],15),
  
  ("castle_42","Teramma_Castle",icon_castle_desert_3|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(120.407,-161.964),[],260),
  
  ("castle_43","Sharwa_Castle",icon_castle_desert_6|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(101.22,-90.0495),[],260),
  ("castle_44","Durrin_Castle",icon_castle_desert_10|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-99.3075,131.267),[],260),
  ("castle_45","Caraf_Castle",icon_castle_desert_11|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(232.13,156.00),[],260),
  #("castle_45","Caraf_Castle",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-195.814,193.638),[],260),
  ("castle_46","Weyyah_Castle",icon_castle_desert_3|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(4.2489,135.847),[],260),
  ("castle_47","Samarra_Castle",icon_castle_desert_7|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-59.1933,129.604),[],260),
  ("castle_48","Bardaq_Castle",icon_castle_desert_10|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-84.5256,173.509),[],260),

  ("castle_49","Deglan_Castle",icon_castle_x_4|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(147.391,-103.555),[],260),
  
  ("castle_50","Tredian_Castle",icon_castle_x_16|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(106.006,-142.639),[],260),
  ("castle_51","Grainwad_Castle",icon_castle_x_14|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-174.722,-9.15365),[],75),
  
  ("castle_52","Ryis_Castle",icon_castle_x_7|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(74.4635,-143.055),[],260),
  ("castle_53","Stamar_Castle",icon_castle_x_8|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-78.5246,-11.113),[],115),
  ("castle_54","Doru_Castle",icon_castle_y_1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-157.218,-219.402),[],90),
  ("castle_55","Gastya_Castle",icon_castle_y_5|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-143.929,-169.317),[],235),

  ("castle_56","Sebula_Castle",icon_castle_desert_1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(29.52,32.6),[],260),

  ("castle_57","Turegor_Castle",icon_castle_x_14|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(182.715,-25.5448),[],260),
  ("castle_58","Rayeck_Castle",icon_castle_wood_4|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(91.9191,-6.37691),[],260),

  ("castle_59","Reland_Castle",icon_castle_x_15|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(196.136,210.387),[],280),
  ("castle_60","Falsevor_Castle",icon_castle_wood_4|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(200.0,104.0),[],260),
  ("castle_61","Reichsin_Castle",icon_castle_wood_5|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(49.232,51.72),[],80),

  ("castle_62","Ghulassen_Castle",icon_castle_desert_1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-15.3372,182.14),[],260),
  ("castle_63","Muhnir_Castle",icon_castle_desert_10|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-111.247,199.911),[],260),
  ("castle_64","Biliya_Castle",icon_castle_desert_6|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(44.3551,216.439),[],260),
##yifeng
##add new
  ("castle_65","Biliya111_Castle",icon_castle_x_7|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-140.2,-58.6),[],260),
  ("castle_66","Biliya222_Castle",icon_castle_x_15|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-39.2,7.74),[],260),
  ("castle_67","Biliya333_Castle",icon_castle_y_2|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(97.74,178.95),[],260),
  ("castle_68","Biliya444_Castle",icon_castle_desert_2|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(172.31,141.14),[],260),
  ("castle_69","Biliya555_Castle",icon_castle_x_16|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(23.35,-29.25),[],260),
  ("castle_70","Biliya666_Castle",icon_castle_desert_2|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-58.9,190.15),[],260),
  ("castle_71","Biliya777_Castle",icon_castle_x_11|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(57.5505,-117.142),[],260),

  ("castle_72","Saren_Castle",icon_castle_x_6|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0,(105.13, 24.65),[], 80), # castle_33
  # Sarranid 
  
  ("castle_73","Rushdigh_Castle",icon_castle_desert_7|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0,(17.3045,184.635),[], 260), # castle_43 *siege tower*
  ("castle_74","Sekhtem_Castle",icon_castle_desert_5|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0,(154.50, 202.88),[], 260), # castle_45
  ("castle_75","Mawiti_Castle",icon_castle_desert_8|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0,(138.0, 249.0),[], 80), # castle_42 *siege tower*
#     Rinimad      
#              Rietal Derchios Gerdus
# Tuavus   Pamir   vezona 
  
  ("village_1", "Yaragar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-201.636,-137.245),[], 100),
  ("village_2", "Burglen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-160.194,-92.7685),[], 110),
  ("village_3", "Azgad",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-114.95,-62.133),[], 120),
  ("village_4", "Nomar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-126.931,-100.932),[], 130),
  ("village_5", "Kulum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-83.2941,-69.811),[], 170),
  ("village_6", "Emirin",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-35.9853,-70.5323),[], 100),
  ("village_7", "Amere",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-155.056,-24.8026),[], 110),
  ("village_8", "Haen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-117.589,10.2628),[], 120),
  ("village_9", "Buvran",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-155.2,43.4912),[], 130),
  ("village_10","Mechin",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-140.322,66.8131),[], 170),

  ("village_11","Dusturil",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-183.141,90.9156),[], 100),
  ("village_12","Emer",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-132.818,106.154),[], 110),
  ("village_13","Nemeja",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-105.989,-17.6112),[], 120),
  ("village_14","Sumbuja",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-80.5982,-41.2067),[], 130),
  ("village_15","Ryibelet",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-47.7096,-43.8978),[], 170),
  ("village_16","Shapeshte",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-48.2391,22.4005),[], 170),
  ("village_17","Mazen",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-12.6297,-7.50261),[], 35),
  ("village_18","Ulburban",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-3.45109,26.2576),[], 170),
  ("village_19","Hanun",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-58.5836,46.0043),[], 170),
  ("village_20","Uslum",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(213.50,245.47),[], 170),

  ("village_21","Bazeck",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-62.0387,36.3679),[], 100),
  ("village_22","Shulus",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-110.118,42.2121),[], 110),
  ("village_23","Ilvia",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-30.0096,-256.839),[], 120),
  ("village_24","Ruldi",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-66.0477,-243.916),[], 130),
  ("village_25","Dashbigha",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(2.0456,-231.212),[], 170),
  ("village_26","Pagundur",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(8.46537,-202.84),[], 170),
  ("village_27","Glunmar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-28.802,-185.121),[], 170),
  ("village_28","Tash_Kulun",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(152.82,227.66),[], 170),
  ("village_29","Buillin",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-91.5038,-185.961),[], 170),

  ("village_30","Ruvar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-4.40894,-146.98),[], 170),
  ("village_31","Ambean",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.8096,-153.793),[], 100),
  ("village_32","Tosdhar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-26.1698,-178.482),[], 110),
  ("village_33","Ruluns",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-126.758,-239.966),[], 120),
  ("village_34","Ehlerdah",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-128.956,-156.533),[], 130),
  ("village_35","Fearichen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-120.162,-181.436),[], 170),
  ("village_36","Jayek",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-151.575,-186.659),[], 170),
  ("village_37","Ada_Kulun",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-184.362,-219.584),[], 170),
  ("village_38","Ibiran",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(81.2043,-262.717),[], 170),
  ("village_39","Reveran",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(54.7429,-228.774),[], 170),
  ("village_40","Saren",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(196.71,243.48),[], 170),

  ("village_41","Dugan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(192.018,-251.564),[], 100),
  ("village_42","Dirigh_Aban",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(116.907,-180.103),[], 110),
  ("village_43","Zagush",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(162.262,-175.069),[], 120),
  ("village_44","Peshmi",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(102.672,-162.186),[], 130),
  ("village_45","Bulugur",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(142.787,-157.417),[], 170),
  ("village_46","Fedner",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(133.806,-125.385),[], 170),
  ("village_47","Epeshe",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(166.111,-156.233),[], 170),
  ("village_48","Veidar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(173.882,-127.818),[], 170),
  ("village_49","Tismirr",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(123.40,232.00),[], 10),
  ("village_50","Karindi",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(90.00,239.00),[], 170),

  ("village_51","Jelbegi",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(129.244,-105.054),[], 100),
  ("village_52","Amashke",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(96.6919,-78.0402),[], 110),
  ("village_53","Balanli",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(62.9186,-107.145),[], 120),
  ("village_54","Chide",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(92.901,-104.294),[], 130),
  ("village_55","Tadsamesh",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(56.5643,-128.358),[], 170),
  ("village_56","Fenada",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(85.0524,-154.657),[], 170),
  ("village_57","Ushkuru",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(100.958,-130.91),[], 170),
  ("village_58","Vezin",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(139.522,-46.3569),[], 170),
  ("village_59","Dumar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-18.3244,-124.982),[], 170),
  ("village_60","Tahlberl",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-2.5588,-82.5596),[], 170),

  ("village_61","Aldelen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(17.1359,-73.7357),[], 100),
  ("village_62","Rebache",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(11.9836,-51.299),[], 100),
  ("village_63","Rduna",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(80.1549,-55.3367),[], 100),
  ("village_64","Serindiar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(146.846,-28.516),[], 100),
  ("village_65","Iyindah",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(129.349,15.5446),[], 100),
  ("village_66","Fisdnar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(82.1617,44.4976),[], 100),
  ("village_67","Tebandra",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(104.861,-19.109),[], 100),
  ("village_68","Ibdeles",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(49.4186,33.9794),[], 100),
  ("village_69","Kwynn",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(75.6535,21.8335),[], 100),
  ("village_70","Dirigsene",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(93.4651,10.2141),[], 100),

  ("village_71","Tshibtin",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(75.7047,-8.82634),[], 20),
  ("village_72","Elberl",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(32.5529,10.72),[], 60),
  ("village_73","Chaeza",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(72.13,-36.36),[], 55),
  ("village_74","Ayyike",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(57.4402,-22.4075),[], 15),
  ("village_75","Bhulaban",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(107.057,74.9787),[], 10),
  ("village_76","Kedelke",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41.1005,56.2938),[], 35),
  ("village_77","Rizi",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(61.1458,76.8795),[], 160),
  ("village_78","Sarimish",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(65.567,106.779),[], 180),
  ("village_79","Istiniar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(84.8228,101.306),[], 0),
  ("village_80","Vayejeg",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(135.793,105.405),[], 40),

  ("village_81","Odasan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(160.413,95.2285),[], 20),
  ("village_82","Yalibe",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(155.888,150.325),[], 60),
  ("village_83","Gisim",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(97.176,137.877),[], 55),
  ("village_84","Chelez",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(85.3871,140.77),[], 15),
  ("village_85","Ismirala",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(53.6596,167.715),[], 10),
  ("village_86","Slezkh",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(87.5098,205.12),[], 35),
  ("village_87","Udiniad",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(153.355,208.673),[], 160),
  ("village_88","Tulbuk",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(184.387,214.413),[], 180),
  ("village_89","Uhhun",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(217.637,215.202),[], 0),
  ("village_90","Jamiche",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(203.904,191.542),[], 40),

  ("village_91","Ayn Assuadi",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(215.0,105.0),[], 20),
  ("village_92","Dhibbain",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(8.66933,93.7427),[], 60),
  ("village_93","Qalyut",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-47.7769,78.5037),[], 55),
  ("village_94","Mazigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41.7078,111.869),[], 15),
  ("village_95","Tamnuh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-51.2801,90.2278),[], 10),
  ("village_96","Habba",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-99.8896,98.3358),[], 35),
  ("village_97","Sekhtem",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(203.00,132.00),[], 160),
  ("village_98","Mawiti",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(238.00,149.00),[], 180),
  #("village_97","Sekhtem",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-168.934,160.635),[], 160),
  #("village_98","Mawiti",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-180.556,183.978),[], 180),

  ("village_99","Fishara",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-102.346,149.092),[], 0),
  ("village_100","Iqbayl",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-74.3314,142.427),[], 40),

  ("village_101","Uzgha",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-18.3614,124.301),[], 20),
  ("village_102","Shibal Zumr",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-43.8501,173.535),[], 60),
  ("village_103","Mijayet",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(28.9149,224.37),[], 55),
  ("village_104","Tazjunat",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.1556,226.871),[], 15),
  ("village_105","Aab",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-92.3645,215.203),[], 10),
  ("village_106","Hawaha",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-105.638,168.568),[], 35),
  ("village_107","Unriya",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-0.220223,153.888),[], 160),
  ("village_108","Mit Nun",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-106.644,120.485),[], 180),
  ("village_109","Tilimsal",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(9.24,178.26),[], 0),
  ("village_110","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-81.295,151.539),[], 40), 
##yifeng add new
  ("village_111","Rushdigh1",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-128.96,-23.94),[], 40), 
  ("village_112","Rushdigh2",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-118.1,-48.4),[], 40), 
  ("village_113","Rushdigh3",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-108.71,228.8),[], 40), 
  ("village_114","Rushdigh4",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-67.55,187.11),[], 40), 
  ("village_115","Rushdigh5",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(90.8,160.9),[], 40), 
  ("village_116","Rushdigh6",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(151.34,132),[], 40), 
  ("village_117","Rushdigh7",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(7.82,63.85),[], 40), 
  ("village_118","Rushdigh8",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(16.07,19.92),[], 40), 
  ("village_119","Rushdigh9",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(4.52,-34.6),[], 40), 
  ("village_120","Rushdigh0",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-47.4,-7.8),[], 40), 
  

  ("salt_mine","Salt_Mine",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.2, -31),[]),
  ("four_ways_inn","Four_Ways_Inn",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(4.8, -39.6),[]),
  ("test_scene","test_scene",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -19.6),[]),
  #("test_scene","test_scene",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -19.6),[]),
  ("battlefields","battlefields",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -16.6),[]),
  ("dhorak_keep","Dhorak_Keep",icon_town|pf_disabled|pf_is_static|pf_always_visible|pf_no_label|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-50,-58),[]),

  ("training_ground","Training Ground",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(3, -7),[]),

  ("training_ground_1", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(98.3126,-52.6042),[], 100),
  ("training_ground_2", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-127.092,-243.786),[], 100),
  ("training_ground_3", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-119.032,-17.292),[], 100),
  ("training_ground_4", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-48.2311,90.6989),[], 100),
  ("training_ground_5", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(138.366,130.144),[], 100),

## ZZ Manor begin useless
  ("manor_1","Manor",  icon_village_c|pf_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(49.2966,-11.89536),[], 170),
  
#  bridge_a
  ("Bridge_1","{!}1",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-86.68,-8.73),[], 70.8),
  ("Bridge_2","{!}2",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-73.0088,-377.616),[], 4.28),
  ("Bridge_3","{!}3",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-73.0088,-377.616),[], 64.5),
  ("Bridge_4","{!}4",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-73.0088,-377.616),[], -2.13),
  ("Bridge_5","{!}5",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-73.0088,-377.616),[], 21.5),
  ("Bridge_6","{!}6",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-73.0088,-377.616),[], -73.5),
  ("Bridge_7","{!}7",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-73.0088,-377.616),[], -64),
  ("Bridge_8","{!}8",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-73.0088,-377.616),[], 1.72),
  ("Bridge_9","{!}9",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-73.0088,-377.616),[], -33.76),
  ("Bridge_10","{!}10",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-73.0088,-377.616),[], -44.07),
  ("Bridge_11","{!}11",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-73.0088,-377.616),[], 81.3),
  ("Bridge_12","{!}12",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-73.0088,-377.616),[], -35.5),
  ("Bridge_13","{!}13",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-73.0088,-377.616),[], -17.7),
  ("Bridge_14","{!}14",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-73.0088,-377.616),[], 66.6),

  ("looter_spawn_point"   ,"{!}looter_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(27.6347,36.0298),[(trp_looter,15,0)]),
  ("steppe_bandit_spawn_point"  ,"the steppes",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(143.158,131.105),[(trp_looter,15,0)]),
  ("taiga_bandit_spawn_point"   ,"the tundra",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-124.938,-248.586),[(trp_looter,15,0)]),
##  ("black_khergit_spawn_point"  ,"black_khergit_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(47.1, -73.3),[(trp_looter,15,0)]),
  ("forest_bandit_spawn_point"  ,"the forests",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(115.81,3.19674),[(trp_looter,15,0)]),
  ("mountain_bandit_spawn_point","the highlands",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(89.4337,-147.96),[(trp_looter,15,0)]),
  ("sea_raider_spawn_point_1"   ,"the coast",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-136.994,3.79212),[(trp_looter,15,0)]),
  ("sea_raider_spawn_point_2"   ,"the coast",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(163.159,204.368),[(trp_looter,15,0)]),
  ("desert_bandit_spawn_point"  ,"the deserts",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(33.9838,176.518),[(trp_looter,15,0)]),
 # add extra towns before this point 

  ("spawn_points_end"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0, 0),[(trp_looter,15,0)]),
  ("reserved_1"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0, 0),[(trp_looter,15,0)]),
  ("reserved_2"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0, 0),[(trp_looter,15,0)]),
  ("reserved_3"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0, 0),[(trp_looter,15,0)]),
  ("reserved_4"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0, 0),[(trp_looter,15,0)]),
  ("reserved_5"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0, 0),[(trp_looter,15,0)]),

  ("player_party_backup","player_party_backup",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ]
# modmerger_start version=201 type=2
try:
    component_name = "parties"
    var_set = { "parties" : parties }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
