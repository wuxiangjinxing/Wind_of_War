# -*- coding: UTF-8 -*-
from header_factions import *

####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix  is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################

## CC
default_kingdom_relations = [("outlaws",-0.2),("peasant_rebels", -0.1),("deserters", -0.1),("sea_raiders",-0.2),("khergits", -0.2),("desert_bandits",-0.2),("undeads_2", -1),("demon", -1),("orc", -1),("cossack", -0.1),]
## CC

factions = [
  ("no_faction","No Faction",0, 0.9, [], []),
  ("commoners","Commoners",0, 0.1,[("player_faction",0.1)], []),
  ("outlaws","Outlaws", max_player_rating(-30), 0.5,[("commoners",-0.6),("player_faction",-0.15),("player_supporters_faction",-0.15),("dark_knights", -1)], [], 0xcc66cc),
# Factions before this point are hardwired into the game end their order should not be changed.

  ("neutral","Neutral",0, 0.1,[("player_faction",0.0)], [],0xFFFFFF),
  ("innocents","Innocents", ff_always_hide_label, 0.5,[("outlaws",-0.05)], []),
  ("merchants","Merchants", ff_always_hide_label, 0.5,[("outlaws",-0.5),("deserters", -0.5),("sea_raiders",-0.5),("khergits", -0.5),("desert_bandits",-0.5),("cossack", -0.5),], [],0xADD451),

## CC

## CC
  ("culture_1",  "{!}west euro", 0, 0.9, 
  [
     ("kingdom_1",1),
     ("kingdom_4",1),
     ("kingdom_7",1),
     ("kingdom_13",1),
  ], []),
  ("culture_2",  "{!}south euro", 0, 0.9, 
  [

  ], []),
  ("culture_3",  "{!}east euro", 0, 0.9, 
  [
     ("kingdom_2",1),
     ("kingdom_3",1),
     ("kingdom_14",1),
  ], []),
  ("culture_4",  "{!}culture_4", 0, 0.9, 
  [
  
  ], []),
  ("culture_5",  "{!}viking", 0, 0.9, 
  [
     ("kingdom_10",1),
     ("kingdom_7",1),
     ("kingdom_8",1),
  ], []),
  ("culture_6",  "{!}culture_6", 0, 0.9, 
  [
     ("kingdom_3",1),
     #("kingdom_6",1),
     ("kingdom_9",1),
     #("kingdom_12",1),
  ], []),
  ("culture_7",  "{!}euro faction", 0, 0.9, 
  [
     ("kingdom_1",1),

     ("kingdom_7",1),

  ], []),
    
  ("culture_8",  "{!}culture_8", 0, 0.9, 
  [
  
  ], []),
  ("culture_9",  "{!}culture_9", 0, 0.9, 
  [
  
  ], []),
  ("culture_10",  "{!}culture_10", 0, 0.9, [], []),
  ("culture_11",  "{!}culture_11", 0, 0.9, [], []),
  ("culture_12",  "{!}culture_12", 0, 0.9, [], []),

  ("culture_13",  "{!}culture_13", 0, 0.9, [], []),
  ("culture_14",  "{!}culture_14", 0, 0.9, [], []),
  ("culture_15",  "{!}culture_15", 0, 0.9, [], []),
  ("culture_16",  "{!}culture_16", 0, 0.9, [], []),
  ("culture_17",  "{!}culture_17", 0, 0.9, [], []),
  ("culture_18",  "{!}culture_18", 0, 0.9, [], []),
  ("culture_19",  "{!}culture_19", 0, 0.9, [], []),
  ("culture_20",  "{!}culture_20", 0, 0.9, [], []),
  ("teutonic_knights",  "{!}teutonic_knights", 0, 0.9, [], []),
#  ("swadian_caravans","Swadian Caravans", 0, 0.5,[("outlaws",-0.8), ("dark_knights",-0.2)], []),
#  ("vaegir_caravans","Vaegir Caravans", 0, 0.5,[("outlaws",-0.8), ("dark_knights",-0.2)], []),

  ("player_faction","Player Faction",0, 0.9, [], []),
  ("player_supporters_faction","Player's Supporters",0, 0.9, [("player_faction",1.00),("outlaws",-0.05),("deserters", -0.02)], [], 0xFF4433), #changed name so that can tell difference if shows up on map
  #("kingdom_1",  "Kingdom_of_France", 0, 0.9, default_kingdom_relations, [], 0x3254B5),
  #("kingdom_2",  "Polish_and_Lithuania",0, 0.9, default_kingdom_relations, [], 0xFF0000),
  #("kingdom_3",  "Golden_Horde", 0, 0.9, default_kingdom_relations, [], 0xCC99FF),
  #("kingdom_4",  "Kingdom_of_England", 0, 0.9, default_kingdom_relations, [], 0x931124),
  #("kingdom_5",  "Kingdom of Italy",  0, 0.9, default_kingdom_relations, [], 0x33DD33),
  ##("kingdom_6",  "Mamluk_Sultanate",  0, 0.9, default_kingdom_relations, [], 0x0000CD),
  #("kingdom_7",  "Holy_Roman_Empire", 0, 0.9, default_kingdom_relations, [], 0xFFCC00),
  #("kingdom_8",  "Kingdom_of_Hungary",    0, 0.9, default_kingdom_relations, [], 0x289326),
  #("kingdom_9",  "Ottoman Empire", 0, 0.9, default_kingdom_relations, [], 0x04C9AB),
  #("kingdom_10",  "Kalmar Union",    0, 0.9, default_kingdom_relations, [], 0x33DDDD),
  #("kingdom_11",  "Spain_States",  0, 0.9, default_kingdom_relations, [], 0xDB7093),
  ##("kingdom_12",  "The Moors",  0, 0.9, default_kingdom_relations, [], 0xA48460),
  #("kingdom_13",  "Teutonic_Order",  0, 0.9, default_kingdom_relations, [], 0xE9E9E9),
  ("kingdom_2",  "undead faction",0, 0.9, 
   [
    ("demon", 1),
    ("dwarf", -1),
    ("elf", -1),
    ("beast",-1),
    
    
    ("outlaws",-0.2),
    ("peasant_rebels", -0.1),
    ("forest_ranger", -0.1),
    ("deserters", -0.1),
    ("sea_raiders",-0.2),
    ("khergits", -0.2),
    ("desert_bandits",-0.2),
   ]+default_kingdom_relations, [], 0xFF2400),
  ("kingdom_6",  "orc faction",  0, 0.9, 
   [
   ("dwarf", -1),
   ("undeads_2", -1),

    
   ("outlaws",-0.2),
   ("peasant_rebels", -0.1),
   ("deserters", -0.1),
   ("sea_raiders",-0.2),
   ("khergits", 0.2),
   ("beast", 0.2),
   ("desert_bandits",-0.2),
   ("player_faction",-0.5)
   ]+default_kingdom_relations, [], 0x66CCCC),
  ("kingdom_11",  "merc facion",  0, 0.9, 
   [
   
   ("undeads_2", 0.5),
   ("cossack", 0.5),
   ("scotland", 0.5),
   ("dark_knights", 0.5),
   ("demon", -1.0),
   ("outlaws", -1.0),

   
   ("dwarf", -1),
   ("mountain_tribe",-1),
   ]+default_kingdom_relations, [], 0xCC6600),
  
  ("kingdom_12",  "sea raider faction",  0, 0.9, 
   [
      ("sea_raiders",1.0),
      
      ("demon", 0.0),
      ("outlaws", 0.0),
      ("undeads_2", 0.0),
      ("demon", -1.0),
      ("orc", -0.5),
      ("elf", -0.5),
      ("forest_ranger", -0.5),
      ("beast", -1),
      ("dwarf", 1),
      ("welsh", -0.5)
   ]+default_kingdom_relations, [], 0x22D8A7),
  
  ("kingdom_13",  "elf faction",  0, 0.9, 
   [
   ("cossack",-0.4),
  
   ("undeads_2", -1),
   ("demon", -1),
   ("elf", -0.4),
   ("player_faction",-0.10),
   ("player_supporters_faction",-0.10),
   ("sea_raiders", -0.4),
   ("desert_bandits", -0.4),
   ("outlaws", -.5),
   ("mountain_tribe", -0.4),
   ("scotland", -0.4),
   ("gaelic", -0.4),
   ("swiss", -0.4),
   ("dark_knights", -0.4),
   ("orc", 0.5),
   ("beast", 1.0),
   ("khergits", 0.5),   ]+default_kingdom_relations, [], 0x6B8E23),
  
  ("kingdom_14",  "drow faction",  0, 0.9, 
   [
    ("dwarf", -1),
    ("undeads_2", -1),
    ("demon", -1),
    ("elf", -1),
    #("outlaws",-0.2),
   

    ("peasant_rebels", -0.1),
    ("forest_ranger", -0.1),
    ("cossack", -0.1),
    ("manhunters", -0.1),
    ("dark_knights", -0.1),
    ("swiss", -0.1),
    ("scotland", -0.1),
    #("deserters", -0.1),
    ("sea_raiders",0.0),
    ("khergits", 0.0),
   ]+default_kingdom_relations, [], 0x9817CE),


  ("kingdom_1",  "Kingdom_of_France", 0, 0.9, 
   [
     ("kingdom_4",-1.00),
     ("kingdom_5",-1.00),
     ("kingdom_7",1),
     ("hospitalier_knights",1.0),
   ]+default_kingdom_relations, [], 0xEEF7ED),
  
  
  ("kingdom_3",  "Golden_Horde", 0, 0.9, 
   [
     ("cossack",-0.4),
     ("khergits",0.5),
     ("kingdom_8",-0.5),
     ("kingdom_5",-0.5),
   ]+default_kingdom_relations, [], 0xCC99FF),
  
  ("kingdom_4",  "Kingdom_of_England", 0, 0.9, 
  [
     ("kingdom_1",-1.00),
     ("kingdom_7",1.00),
     ("kingdom_8",1.00),
     
     ("kingdom_10",-1.00),
     ("forest_ranger",1.0),
     ("welsh",1.00),
  ]+default_kingdom_relations, [], 0xff0040),
  
  ("kingdom_5",  "Kingdom of Italy",  0, 0.9, 
   [
     ("undeads_2",1.0),
     ("demon",1.0),

     #("kingdom_8",-0.40),
     ("kingdom_9",-0.40)
   ]+default_kingdom_relations, [], 0x33DD33),
   
  ("kingdom_7",  "Holy_Roman_Empire", 0, 0.9, 
   [
     ("kingdom_8",1.0),

     ("hospitalier_knights",1.0),
     #("kingdom_5",-0.40),
     ("kingdom_10",-0.2),
     ("kingdom_9",-0.2),
     
     
   ]+default_kingdom_relations, [], 0xFFCC00),
  
  ("kingdom_8",  "Kingdom_of_Hungary",    0, 0.9, 
   [
     ("hospitalier_knights",1.0),
     ("kingdom_9",-1.00),
   ]+default_kingdom_relations, [], 0x9696FF),
  
  ("kingdom_9",  "Ottoman Empire", 0, 0.9, 
   [
     #("kingdom_6",-0.50),
   ]+default_kingdom_relations, [], 0x0000CD),
  
  ("kingdom_10",  "Kalmar Union",    0, 0.9, 
   [
     ("kingdom_4",-1.00),
     ("hospitalier_knights",1.0),
     ("kingdom_7",-0.2),
     ("cossack",1),
   ]+default_kingdom_relations, [], 0x33DDDD),
  
  
  ("kingdoms_end","{!}kingdoms_end", 0, 0,[], []),

  ("robber_knights",  "robber_knights", 0, 0.1, 
   [("player_faction",-0.1),
    ("outlaws",0.2),
    ("peasant_rebels", 0.1),
    ("deserters", -0.1),
    ("sea_raiders",0.2),
    ("khergits", 0.2),
    ("desert_bandits",0.2),
    ("cossack", 0.1),
    ("undeads_2", 1),
    ("demon", 1),
    ("beast", 1),
    ("orc", 1),
    ("dark_knights", -0.4),
    ("dwarf", -0.4),
    ("demon_hunters", -0.4),
   ], [], 0xff8080),

  ("khergits","Khergits", 0, 0.5,
   [
    ("player_faction",-0.15),
    
    ("kingdom_2",1),
    ("kingdom_3",1),
    ("kingdom_14",1),
    ("beast",1),
    ("orc",1),
    ("kingdom_9",0.5),
    ("khergits",0.5),
    ("dark_knights",-0.4),
    ("manhunters",-0.4),
    ("demon_hunters",-0.4),
    ("hospitalier_knights",-0.4),
    ("mountain_tribe",-0.4),
    
    ("dwarf",-0.4),
    ("outlaws",0.2),
    ("cossack",-0.4),
    ("deserters", -0.1),
    ("sea_raiders",-0.2),
    ("desert_bandits",-0.2),
    ("undeads_2", -1),
    ("demon", -1),
    ("orc", -1),
    ("cossack", -0.1),
   ], [], 0x60A4F4),

  ("manhunters","Manhunters", 0, 0.5,
  [
   ("player_faction",0.1),
   ("dark_knights", 0.4),
   ("demon_hunters",1.00),
   ("forest_ranger", 0.4),
   ("dwarf", 0.4),
  ]+default_kingdom_relations, [], 0x80ff80),
  
  ("deserters","Deserters", 0, 0.5,
  [
   ("manhunters",-0.6),
   ("merchants",-0.5),
   ("player_faction",-0.1),
   ("cossack",0.4),
   ("dark_knights", -0.4),
   ("desert_bandits", -0.4)
  ], [], 0xff8080),
  
  ("welsh","Welsh", 0, 0.5,
  [
   ("kingdom_4",1.0),
   ("kingdom_8",1.0),
   
   ("mountain_tribe", -0.4),
   ("scotland", -0.4),
   ("gaelic", -0.4),

   ("kingdom_14", -0.4),
   ("kingdom_1", -0.4),
   ("kingdom_5", -0.4),
   ("kingdom_9", -0.4),
   #("kingdom_12", -0.4),
   
   ("swiss", -0.4),
   ("dark_knights", -0.4),
   ("undeads_2", -1),
   ("demon", -1),
   ("orc", 0.5),
   ("beast", 1.0),
   ("khergits", 0.5),
   ("forest_ranger", 0.5),
   ("player_faction",0.0)
  ]+default_kingdom_relations,[],0x238E6B),
  
  ("swiss","Swiss", 0, 0.,
  [
   ("kingdom_1", 0.5),
   ("kingdom_7", 0.5),
   ("kingdom_8", 0.5),
   ("kingdom_5", 0.5),
   
   
   ("undeads_2", 0.5),
   ("cossack", 0.5),
   ("scotland", 0.5),
   ("dark_knights", 0.5),
   ("demon", -1.0),
   ("outlaws", -1.0),

   ("kingdom_3",-1.0),
   ("kingdom_4",-1.0),
   ("kingdom_9",-1.0),
   ("kingdom_10",-1.0),   
   
   ("dwarf", -1),
   ("mountain_tribe",-1),
   ("player_faction",0.0)
  ]+default_kingdom_relations,[],0xCC6600),
  
  ("scotland",  "Kingdom of Scotland",
    0, 0.9,
    [
    
      ("kingdom_10", 1),
      ("kingdom_7", 1),
      ("kingdom_1", 1),
      ("kingdom_8", 0),
      ("kingdom_9", -1),
      ("kingdom_5", -1),
    
      ("kingdom_4",-1.0),
      ("kingdom_10",1.0),
      ("sea_raiders",1.0),
      
      ("demon", 0.0),
      ("outlaws", 0.0),
      ("undeads_2", 0.0),
      ("demon", -1.0),
      ("orc", -0.5),
      ("elf", -0.5),
      ("forest_ranger", -0.5),
      ("beast", -1),
      ("dwarf", 1),
      ("welsh", -0.5)
    ]+default_kingdom_relations,
    [],0x22D8A7),
    
  ("gaelic",  "Gaelic Kingdoms",
    0, 0.9,
    [
      ("kingdom_4",-1.0),
      ("kingdom_5",-1.0),
      ("welsh", -0.5),
      ("dwarf", 1),
      ("forest_ranger", 0.05)
    ]+default_kingdom_relations, [],0x77b322),

  ("dark_knights","Dark Knights", 0, 0.5,
  [
   ("outlaws", -1),
   ("kingdom_1",1.00),
   ("kingdom_2",1.00),
   ("kingdom_7",1.00),
   ("kingdom_13",1.00),
   ("kingdom_11",1.00),
   ("scotland",1.00),
   ("swiss",1.00),
   ("manhunters",1.00),
   ("cossack",1.00),
   ("demon_hunters",1.00),
   ("hospitalier_knights",1.00),
   ("mountain_tribe",1.00),
   ("dwarf",1.00),
   ("neutral",1.00),
   
   ("kingdom_8",-1.00),
   ("kingdom_3",-1.00),
   ("kingdom_9",-1.00),
   ("kingdom_10",-1.00),
   ("orc", -.5),
   ("beast", -.5),
   ("elf", -.5),
   ("welsh", -.5),
   ("forest_ranger", -.5),
   ("mountain_tribe", -.5),
   ("deserters", -1),
   ("khergits", -0.1),
   ("sea_raiders", -0.4),
   ("desert_bandits",-0.1),
   ("cossack",-0.1)
  ], [], 0x00ffff),

  ("forest_ranger","forest_ranger",0, 0.1,
  [("cossack",-0.4),
  
   ("kingdom_4",1.00),
   ("kingdom_8",1.0),
   ("kingdom_2",1.0),
   
   ("kingdom_14",-1.00),
   ("kingdom_1",-1.00),
   ("kingdom_7",-1.00),
   ("kingdom_5", -0.4),
   ("kingdom_9", -0.4),
   #("kingdom_12", -0.4),
   ("undeads_2", -1),
   ("demon", -1),
   ("elf", -0.4),
   ("player_faction",-0.10),
   ("player_supporters_faction",-0.10),
   ("sea_raiders", -0.4),
   ("desert_bandits", -0.4),
   ("outlaws", -.5),
   ("mountain_tribe", -0.4),
   ("scotland", -0.4),
   ("gaelic", -0.4),
   ("swiss", -0.4),
   ("dark_knights", -0.4),
   ("orc", 0.5),
   ("beast", 1.0),
   ("khergits", 0.5),
   ("player_faction",0.0)
   
  ], [],0x6B8E23),

  
  ("elf","elf",0, 0.1,
  [
   ("undeads_2", -1),
   ("demon", -1),
   ("orc", -1),
   ("outlaws",-0.2),
   
    ("kingdom_9", -1),
    ("kingdom_5", -1),
    ("kingdom_3", -1),
    ("kingdom_4", -1),
    
    ("kingdom_1", 1),
    ("kingdom_7", 1),
   
    ("kingdom_10", 0),
    ("kingdom_8", 0),
   
   ("peasant_rebels", -0.1),
   ("deserters", -0.1),
   ("sea_raiders",-0.2),
   ("desert_bandits",-0.2),
   
   ("kingdom_4",1.0),
   ("kingdom_8",1.0),
   
   ("mountain_tribe", -0.4),
   ("scotland", -0.4),
   ("gaelic", -0.4),
   
   ("swiss", -0.4),
   ("dark_knights", -0.4),

   ("khergits", 0.5),
   
   
  ], [],0x00ff00),

  ("dwarf","dwarf", 0, 0.5,
  [
   ("undeads_2", -1),
   ("demon", -1),
   ("orc", -1),
   ("beast",-1),
   ("outlaws",-0.2),
   
    #("kingdom_6", -1),
    #("kingdom_12", -1),
    ("kingdom_9", -1),
    ("kingdom_5", -1),
    ("kingdom_3", -1),
    ("kingdom_1", -1),

    ("kingdom_4", 0),
    ("kingdom_8", 0),

    ("kingdom_7", 1),
   
    ("kingdom_4", 1),
    ("kingdom_10", 1),
   
   ("mountain_tribe", 1),
   ("hospitalier_knights", 1),
   ("dark_knights", 1),

   ("cossack",-1),
      
   ("peasant_rebels", -0.1),
   ("deserters", -0.1),
   ("sea_raiders",0.2),
   ("khergits", -0.2),
   ("desert_bandits",-0.2),
  ], [], 0xDDA0DD),
  
  ("orc","orc",0, 0.1,
  [
   ("dwarf", -1),
   ("undeads_2", -1),

    #("kingdom_14", 1),
    #("kingdom_6", 1),
    #("kingdom_12", 1),
    #("kingdom_9", 1),
    ("kingdom_8", -1),
    ("kingdom_1", -1),
    ("kingdom_7", -1),
    ("kingdom_3", 1),
    ("kingdom_2", 1),
    
    ("kingdom_9", 0),
    ("kingdom_5", 0),
    
   ("outlaws",-0.2),
   ("peasant_rebels", -0.1),
   ("deserters", -0.1),
   ("sea_raiders",-0.2),
   ("khergits", 0.2),
   ("beast", 0.2),
   ("desert_bandits",-0.2),
   ("player_faction",-0.5)
  ], [],0x66CCCC),

  ("undeads_2","Undeads", max_player_rating(-30), 0.5,
   [("commoners",-0.7),
    ("player_faction",-0.5),
    ("demon", 1),
    ("dwarf", -1),
    ("elf", -1),
    ("beast",-1),
    
    #("kingdom_6", 1),
    #("kingdom_12", 1),
    ("kingdom_9", 1),
    ("kingdom_5", 1),
    ("kingdom_3", 1),
    ("kingdom_2", 0),
    
    ("kingdom_4", 0),
    ("kingdom_7", 0),
    
    ("outlaws",-0.2),
    ("peasant_rebels", -0.1),
    ("forest_ranger", -0.1),
    ("deserters", -0.1),
    ("sea_raiders",-0.2),
    ("khergits", -0.2),
    ("desert_bandits",-0.2),
   ], [],0xFFFFFF),

  ("demon","Demon", max_player_rating(-30), 0.5,
   [("commoners",-0.7),
    ("player_faction",-0.5),
    ("dwarf", -1),
    ("elf", -1),
    ("beast",-1),
    
    ("kingdom_10", 0),
    ("kingdom_8", 0),
    
    #("kingdom_6", 1),
    #("kingdom_12", 1),
    ("kingdom_9", 1),
    ("kingdom_5", 1),
    ("kingdom_3", 1),
    ("kingdom_2", 0),
   ("outlaws",-0.2),
   ("peasant_rebels", -0.1),
   ("forest_ranger", -0.1),
   ("deserters", -0.1),
   ("sea_raiders",-0.2),
   ("khergits", -0.2),
   ("desert_bandits",-0.2),
   ], [],0xFF2400),

  ("beast","beast", 0, 0.5,
   [
    ("player_faction",-0.15),
    ("dwarf", -1),
    ("undeads_2", -1),
    ("demon", -1),
    ("elf", -1),
    #("outlaws",-0.2),
   
    ("kingdom_10", 0),
    ("kingdom_9", 0),
   
    ("kingdom_3", 1),
    ("kingdom_4", 1),
    ("kingdom_8", 1),
    ("kingdom_11",-1),
   
    ("kingdom_5", -1),
    #("kingdom_9", -1),
    ("kingdom_1", -1),
    ("kingdom_7", -1),

    ("peasant_rebels", -0.1),
    ("forest_ranger", -0.1),
    ("cossack", -0.1),
    ("manhunters", -0.1),
    ("dark_knights", -0.1),
    ("swiss", -0.1),
    ("scotland", -0.1),
    #("deserters", -0.1),
    ("sea_raiders",0.0),
    ("khergits", 0.0),
    #("desert_bandits",-0.2),
   ], [], 0x9817CE),

  ("demon_hunters","demon_hunters", 0, 0.5,
  [
   ("dwarf", 1),
   ("mountain_tribe", 1),
   ("hospitalier_knights", 1),
   ("dark_knights", 1),

   ("undeads_2", -1),
   ("demon", -1),
   ("khergits", -1),
   ("orc", -1),
   ("beast",-1),
   ("cossack",-1),

   ("kingdom_8", 0),
   ("kingdom_10", 0),

   ("kingdom_1", 1),
   ("kingdom_7", 1),
   ("kingdom_11", 1),
   ("kingdom_13", 1),
   
   ("kingdom_2", -1),
   ("kingdom_3", -1),
   #("kingdom_6", -1),
   ("kingdom_5", -1),
   ("kingdom_9", -1),
   #("kingdom_12", -1),
   
   ("outlaws", -1),
   ("peasant_rebels", -1),
   ("desert_bandits",-1),
  ], [], 0xED1C24),


  ("hospitalier_knights",  "Order of the hospitalier",  0, 0.9, 
   [
     ("beast",-1),
     
     ("kingdom_7", 1),
     ("kingdom_11", 1),
     ("kingdom_13", 1),
     ("kingdom_8", 1),
     #("kingdom_5", 1),
     ("kingdom_1", 1),

     ("kingdom_3",-1.00),
     ("kingdom_9",-1.00),
     ("kingdom_5", -1),
     #("kingdom_6",-1.00),
     #("kingdom_12",-1.00),
     ("dark_knights",1.0)
   ]+default_kingdom_relations, [], 0x800000),

  ("mountain_tribe","mountain_tribe", 0, 0.5,
  [
   ("cossack",-0.4),
   ("dwarf", 1),
   ("khergits", -0.4),
   ("forest_ranger", -0.4),
   ("sea_raiders", -0.4),
   ("desert_bandits", -0.4),
   ("outlaws", -.5),
   ("deserters", -0.01) 
  ], [], 0xFF7040),

  ("cossack","cossack",0, 0.1,
  [
  
   ("elf", -1),
   ("undeads_2", -1),
   ("demon", -1),
   ("orc", -1),
   
   ("kingdom_7", 0),
   ("kingdom_5", 0),
   ("kingdom_10", 0),
   
   ("khergits", -0.4),
   ("forest_ranger", 0.4),
   ("mountain_tribe", -0.4),
   ("sea_raiders", -0.4),
   ("desert_bandits", -0.4),
   ("outlaws", -.5),
   ("kingdom_9", -0.4),
   ("kingdom_8", 1),
   ("kingdom_14", 1),
   ("kingdom_3", -0.4) 
  ], [],0x66CCCC),
  
  ("sea_raiders","sea_raiders", 0, 0.5,
   [ 
    ("player_faction",-0.15),
    
    ("orc", -1),
    ("demon", -1),
    ("cossack",-0.4),
    ("khergits", -0.4),
    ("forest_ranger", -0.4),
    ("mountain_tribe", -0.4),
    ("desert_bandits", -0.4),
    ("outlaws", -.5),
    
    ("kingdom_10", 1),
    ("kingdom_4", -0.4) 
   ], [], 0x999966),
  
  ("desert_bandits","desert_bandits", 0, 0.5,
   [
    ("player_faction",-0.15),
    ("cossack",-0.4),
    ("khergits", -0.4),
    ("forest_ranger", -0.4),
    ("mountain_tribe", -0.4),
    ("sea_raiders", -0.4),
    ("outlaws", -.5),
    #("kingdom_12", 1), 
    #("kingdom_6", -0.4) 
   ], [], 0x0066CC),
    
  #("black_khergits","Black Khergits", 0, 0.5,[("kingdom_3",0.5),("outlaws", -0.01),("deserters", -0.01)], [], 0x993300),

#  ("mountain_bandits","Mountain Bandits", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0x888888),
#  ("forest_bandits","Forest Bandits", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0x888888),
  #("khergits","{!}Khergits", 0, 0.5,[("player_faction",0.0)], []),
##  ("rebel_peasants","Rebel Peasants", 0, 0.5,[("vaegirs",-0.5),("player_faction",0.0)], []),
  ("undeads","Undeads", max_player_rating(-30), 0.5,[("commoners",-0.7),("player_faction",-0.5)], []),
  ("slavers","{!}Slavers", 0, 0.1, [], []),
  ("peasant_rebels","{!}Peasant Rebels", 0, 1.0,[("noble_refugees",-1.0),("player_faction",-0.4)], []),
  ("noble_refugees","{!}Noble Refugees", 0, 0.5,[], []),
  

  
]
# modmerger_start version=201 type=4
try:
    component_name = "factions"
    var_set = { "factions":factions,"default_kingdom_relations":default_kingdom_relations, }
    from modmerger import modmerge
    modmerge(var_set, component_name)
except:
    raise
# modmerger_end
