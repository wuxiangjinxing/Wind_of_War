Adding a scene to multiplayer maps list is something that we or someone who has access to the module system code can do. So if you could send me your map code (the long hexadecimal number) and sco file, I can test if snowy terrain works or not.

Entry point information
------------------------------------------------------------------------------------------------
0..63: Player spawn points
------------------------------------------------------------------------------------------------
0: Team 1 base point. In Battle and Siege modes, the whole team spawns from this point. Right and behind of this point must be empty in order to spawn at least 32 men at the same time.

1: Team 1 second base point. Not used at the moment, but we keep this entry point close to the base. This entry point should be around 20-50 meters away from the first base point.

32: Team 2 base point. In Battle and Siege modes, the whole team spawns from this point. Right and behind of this point must be empty in order to spawn at least 32 men at the same time.

33: Team 2 second base point. Not used at the moment, but we keep this entry point close to the base. This entry point should be around 20-50 meters away from the first base point.
------------------------------------------------------------------------------------------------
64: Team 1's flag point in Capture the Flag mode. In general, it is very close to entry point 0, unless there is a specific flag point (ie. the top of a tower) on that map.

65: Team 2's flag point in Capture the Flag mode. In general, it is very close to entry point 0, unless there is a specific flag point (ie. the top of a tower) on that map.
------------------------------------------------------------------------------------------------
66: Castle's flag point in Siege mode. There is no need for this entry point unless the map supports Siege mode.
------------------------------------------------------------------------------------------------
67, 68, 69: Possible flag points for the 2 flags that appear usually at the middle of the map when Master of Field starts in Battle mode.
------------------------------------------------------------------------------------------------
100..109: Entry points that shows ladders' initial positions. Ladders must be designed as raised initially. The order of the entry points are not important, because the ladders will find the closest entry point and use that one.

Passages have a "Entry No" and a "Menu Item No". It is pretty important to not mix them up!
From the inside or outside scenes your passage has to have the following "Menu Item No" to bring you to:
0 - castle (NATIVE: 0, related Entry Point from interior scene:2)
Don't use 1 to 5!!
2 - Castle, related Entry Point in the street/courtyard:2
3 - Town center, related entry point in the street depends on the place, the player comes from
4 - Tavern, related Entry Point in the street:4
5 - Shop, related Entry pointin the street: 5
6 - Arena, related Entry in the street: 6
7 - Dungeon, related Entry in the street/courtyard:7
8 - Castle courtyard

Entry numbers from OUTSIDE are "0".
Now from interiors to the outside you simply have to give the "Entry No" the number of the entry point you put into the scene your passage leads to.
For example, you are inside the castle and you give the passage "Menu Item No: 7" and "Entry No: 5" you simply have to put the entry point "Entry No: 5" in front of the castle within the street scene.
Just make sure you do not use the reserved Entry points such as player entry / guild master / guard etc.

Villages
0 - Player when entering village as normal
1 - Player when "defending" the village
2 - Player when training peasants
3 - Enemies
4 - Peasants when training (Attacked at night? Need more info.)
11 - Village Elder
30 - 40 - Village Walkers
45 - Fugitive from Lord quest

Town Centers (Cities)
0 - Player when entering on foot
1 - Player when entering on horseback
2 - Player when leaving the keep (Passages)
3 - Player instance (Crushing street resistance?)
4 - Player leaving Tavern(Passages) / Enemy ambusher
5 - Player when leaving shop (Passages)
6 - Player when leaving arena (Passages)
7 - Player when leaving the dungeon (Passages)
9 - Armor Merchant
10 - Weaponsmith
11 - Guild Master / Enemy Ambusher
12 - Horse Merchant
23 - Castle Guard
24 - Prison Guard
25&26 - High Level Guards
27&28 - Low Level Guards / Enemy Ambushers
30-40 - Town Walkers

Town walls (City Siege)
0 - Attackers
3 - Sally
10 - Defenders infantry gathering point
11 - Player when defending / Defenders Infantry spawn point
15 - Reinforcement for the defenders
40-46 - Archers
50-55 Siege towers path

Keep Indoors (Cities/Castles)
0 - Player
6 - Castle Guard
7 - Castle Guard / Nurse when 'visiting a lady'
16 - Chancellor / Tournament Knight / "Lady", when 'visiting a lady'
17-31 - Lords and Ladies

Castle Outdoors (Includes Siege)
0 - Attackers
1 - Player
2 - Player when leaving the keep (Passages)
3 - Sally point
7 - Player when leaving the dungeons (Passages)
10 - Defenders "gathering point"
11 - Player when defending / Defenders Infantry spawn
15 - Defenders reinforcements
24 - Prison Guard
40-46 - Guards
50-55 - Path for Siege Towers

Taverns
0 - Player
9 - Tavern Keeper
17 - Mercenary
18 - Mercenary / Companion
19 - Ransom Broker / Companion Traveller
20 - Ransom Broker / Traveller / Bard / Companion
21 - Ransom Broker
22 - Traveller

Dungeons
0 - Player
16-31 Prisoners

Shops
0 - Player
9 - Merchant

Bandit Lair
0 Player
1-10 Bandits

Arena - Needs verified.
0-7 Team 1
8-15 Team 2
16-23 Team 3
24-31 Team 4
32-39 ???
50 Player watching
51 ???
52 Tournament Master
56-59 ???

Opening Scene/Alley
0-Player
3- NPC (bandit, merchant, etc.)

Castle siege fall back:

0 - player
6 - player troops
7 - player troops

16 - 20 - enemies

Town siege fall back:

0 - player and player troops

2 - enemies
23-28 - enemies

["drinking_ani", "{!}glove_animation", [("drinkingL", 0)], itp_type_hand_armor, 0, 0, weight(1)|abundance(100), imodbits_none], 
["eating_ani", "{!}glove_animation", [("eatingL", 0)], itp_type_hand_armor, 0, 0, weight(1)|abundance(100), imodbits_none], 
["sitting_working_1_ani", "{!}glove_animation", [("sitting_working_1_L", 0)], itp_type_hand_armor, 0, 0, weight(1)|abundance(100), imodbits_none], 
["sitting_working_2_ani", "{!}glove_animation", [("sitting_working_2_L", 0)], itp_type_hand_armor, 0, 0, weight(1)|abundance(100), imodbits_none], 
["sitting_working_3_ani", "{!}glove_animation", [("sitting_working_3_L", 0)], itp_type_hand_armor, 0, 0, weight(1)|abundance(100), imodbits_none], 
["fishing_ani", "{!}glove_animation", [("fishingL", 0)], itp_type_hand_armor, 0, 0, weight(1)|abundance(100), imodbits_none], 
["sharpening_1_ani", "{!}glove_animation", [("sharpening_1_L", 0)], itp_type_hand_armor, 0, 0, weight(1)|abundance(100), imodbits_none], 
["reading_ani", "{!}glove_animation", [("readingL", 0)], itp_type_hand_armor, 0, 0, weight(1)|abundance(100), imodbits_none], 
["woodcutting_2_ani", "{!}glove_animation", [("woodcutting_2_L", 0)], itp_type_hand_armor, 0, 0, weight(1)|abundance(100), imodbits_none], 
["brooming_ani", "{!}glove_animation", [("broomingL", 0)], itp_type_hand_armor, 0, 0, weight(1)|abundance(100), imodbits_none], 
["field_working_1_ani", "{!}glove_animation", [("field_working_1_L", 0)], itp_type_hand_armor, 0, 0, weight(1)|abundance(100), imodbits_none], 
["field_working_2_ani", "{!}glove_animation", [("field_working_2_L", 0)], itp_type_hand_armor, 0, 0, weight(1)|abundance(100), imodbits_none], 
["grinding_ani", "{!}glove_animation", [("grindingL", 0)], itp_type_hand_armor, 0, 0, weight(1)|abundance(100), imodbits_none], 
["smithing_ani", "{!}glove_animation", [("smithingL", 0)], itp_type_hand_armor, 0, 0, weight(1)|abundance(100), imodbits_none], 



  ["shield_taunt", acf_enforce_all|acf_rot_vertical_sword, 176160828, 
    [1, "shield_taunt", 0, 12, arf_blend_in_0|arf_blend_in_7],
  ],

  ["sitting", acf_enforce_all, 67108959, 
    [24, "sitting", 0, 40, arf_cyclic|arf_use_stand_progress],
  ],

  ["sitting_drinking", acf_enforce_all, 67108959, 
    [20, "sitting_drinking", 0, 30, arf_cyclic|arf_use_stand_progress],
  ],

  ["sitting_eating", acf_enforce_all, 67108959, 
    [2.5, "sitting_eating", 0, 15, arf_cyclic|arf_use_stand_progress],
  ],

  ["sitting_working_1", acf_enforce_all, 67108959, 
    [3, "sitting_working_1", 0, 14, arf_cyclic|arf_use_stand_progress],
  ],

  ["sitting_working_2", acf_enforce_all, 67108959, 
    [1.2, "sitting_working_2", 0, 12, arf_cyclic|arf_use_stand_progress],
  ],

  ["sitting_working_3", acf_enforce_all, 67108959, 
    [1, "sitting_working_3", 0, 4, arf_cyclic|arf_use_stand_progress],
  ],

  ["sitting_fishing", acf_enforce_all, 67108959, 
    [2.5, "sitting_fishing", 0, 8, arf_cyclic|arf_use_stand_progress],
  ],

  ["sitting_child_1", acf_enforce_all, 67108959, 
    [2, "sitting_child_1", 0, 8, arf_cyclic|arf_use_stand_progress],
  ],

  ["sitting_sharpening_1", acf_enforce_all, 67108959, 
    [1.5, "sitting_sharpening_1", 0, 4, arf_cyclic|arf_use_stand_progress],
  ],

  ["sitting_reading", acf_enforce_all, 67108959, 
    [14, "sitting_reading", 0, 22, arf_cyclic|arf_use_stand_progress],
  ],

  ["woodcutting_2", acf_enforce_all, 67108959, 
    [1, "woodcutting_2", 0, 15, arf_cyclic|arf_use_stand_progress],
  ],

  ["brooming", acf_enforce_all, 67108959, 
    [1.6, "brooming", 0, 36, arf_cyclic|arf_use_stand_progress],
  ],

  ["field_working_1", acf_enforce_all, 67108959, 
    [1.3, "field_working_1", 1, 7, arf_cyclic|arf_use_stand_progress],
  ],

  ["field_working_2", acf_enforce_all, 67108959, 
    [2, "field_working_2", 0, 5, arf_cyclic|arf_use_stand_progress],
  ],

  ["field_working_3", acf_enforce_all, 67108959, 
    [2.3, "field_working_3", 0, 5, arf_cyclic|arf_use_stand_progress],
  ],

  ["grinding", acf_enforce_all, 67108959, 
    [1.2, "grinding", 0, 4, arf_cyclic|arf_use_stand_progress],
  ],

  ["smithing", acf_enforce_all, 67108959, 
    [0.75, "smithing", 0, 9, arf_cyclic|arf_use_stand_progress],
  ],


("cf_prop_spawn_agent",
[
    (ge, "$can_spawn_commoners", 1),
    (this_or_next|eq, "$can_spawn_commoners", 1),
    (eq, "$g_mt_mode", 2),
    (this_or_next|eq, "$talk_context", 14),
    (this_or_next|eq, "$talk_context", 1),
    (eq, "$talk_context", 0),
    (this_or_next|eq, "$talk_context", 14),
    (neg|is_currently_night),
    (store_trigger_param, ":var_0", 1),
    (prop_instance_get_scene_prop_kind, ":var_1", ":var_0"),
    (assign, ":var_2", -1),
    (prop_instance_get_variation_id, ":var_3", ":var_0"),
    (prop_instance_get_variation_id_2, ":var_4", ":var_0"),
    (try_begin),
        (eq, ":var_4", 0),
        (assign, ":var_4", 33),
    (try_end),
    (store_random_in_range, ":var_5", 0, 100),
    (store_current_hours, ":var_6"),
    (val_mod, ":var_6", 10000),
    (val_mul, ":var_5", ":var_6"),
    (val_mod, ":var_5", 100),
    (assign, ":var_7", -1),
    (try_begin),
        (this_or_next|neg|ge, ":var_5", ":var_4"),
        (eq, ":var_4", 1),
        (try_begin),
            (eq, ":var_1", "spr_z_entry_priest_sitting"),
            (try_begin),
                (neg|is_between, ":var_3", 1, 2),
                (store_random_in_range, ":var_3", 1, 2),
                (val_mul, ":var_3", ":var_6"),
                (val_mod, ":var_3", 1),
                (val_add, ":var_3", 1),
            (try_end),
            (assign, ":var_2", "trp_monjes"),
            (try_begin),
                (assign, ":var_8", "itm_reading_ani"),
                (assign, ":var_9", "anim_sitting_reading"),
            (try_end),
        (else_try),
            (eq, ":var_1", "spr_z_entry_military_sitting"),
            (try_begin),
                (neg|is_between, ":var_3", 1, 2),
                (store_random_in_range, ":var_3", 1, 2),
                (val_mul, ":var_3", ":var_6"),
                (val_mod, ":var_3", 1),
                (val_add, ":var_3", 1),
            (try_end),
            (store_faction_of_party, ":var_10", "$current_town"),
            (store_random_in_range, ":var_11", 0, 5),
            (val_mul, ":var_11", ":var_6"),
            (val_mod, ":var_11", 5),
            (val_add, ":var_11", 41),
            (faction_get_slot, ":var_2", ":var_10", ":var_11"),
            (try_begin),
                (assign, ":var_8", "itm_sharpening_1_ani"),
                (assign, ":var_9", "anim_sitting_sharpening_1"),
                (assign, ":var_7", "snd_agent_anim_sharpening_1"),
            (try_end),
        (else_try),
            (eq, ":var_1", "spr_z_entry_child_sitting"),
            (assign, ":var_8", -1),
            (assign, ":var_9", "anim_sitting_child_1"),
            (store_random_in_range, ":var_2", 0, 2),
            (val_mul, ":var_2", ":var_6"),
            (val_mod, ":var_2", 2),
            (val_add, ":var_2", "trp_nino_varon"),
        (else_try),
            (eq, ":var_1", "spr_z_entry_smith"),
            (assign, ":var_2", "trp_village_walker_3a"),
            (assign, ":var_8", "itm_smithing_ani"),
            (assign, ":var_9", "anim_smithing"),
            (assign, ":var_7", "snd_agent_anim_smithing"),
        (else_try),
            (this_or_next|eq, ":var_1", "spr_z_entry_field_working_1"),
            (this_or_next|eq, ":var_1", "spr_z_entry_field_working_2"),
            (this_or_next|eq, ":var_1", "spr_z_entry_field_working_3"),
            (this_or_next|eq, ":var_1", "spr_z_entry_fisherman_sitting"),
            (this_or_next|eq, ":var_1", "spr_z_entry_woodcutting"),
            (this_or_next|eq, ":var_1", "spr_z_entry_tavern_sitting"),
            (this_or_next|eq, ":var_1", "spr_z_entry_village_sitting"),
            (eq, ":var_1", "spr_z_entry_grinding"),
            (try_begin),
                (neg|is_between, ":var_3", 1, 4),
                (store_random_in_range, ":var_3", 1, 4),
                (val_mul, ":var_3", ":var_6"),
                (val_mod, ":var_3", 3),
                (val_add, ":var_3", 1),
            (try_end),
            (store_current_scene, ":var_12"),
            (try_begin),
                (is_between, ":var_12", "scn_monasterio1_normal", "scn_caravanatacada"),
                (assign, ":var_2", "trp_monjes"),
            (else_try),
                (store_random_in_range, ":var_11", 0, 8),
                (val_mul, ":var_11", ":var_6"),
                (val_mod, ":var_11", 8),
                (val_add, ":var_11", 160),
                (party_get_slot, ":var_2", "$current_town", ":var_11"),
                (try_begin),
                    (eq, ":var_2", 0),
                    (store_random_in_range, ":var_2", "trp_village_walker_1", "trp_spy_walker_1"),
                (try_end),
                (try_begin),
                    (eq, ":var_2", "trp_village_walker_1"),
                    (assign, ":var_2", "trp_village_walker_1a"),
                (else_try),
                    (eq, ":var_2", "trp_village_walker_3"),
                    (assign, ":var_2", "trp_village_walker_3a"),
                (else_try),
                    (eq, ":var_2", "trp_village_walker_5"),
                    (assign, ":var_2", "trp_village_walker_5a"),
                (try_end),
            (try_end),
            (try_begin),
                (eq, ":var_1", "spr_z_entry_field_working_1"),
                (assign, ":var_8", "itm_field_working_1_ani"),
                (assign, ":var_9", "anim_field_working_1"),
                (assign, ":var_7", "snd_agent_anim_field_working_1"),
            (else_try),
                (eq, ":var_1", "spr_z_entry_field_working_2"),
                (assign, ":var_8", "itm_field_working_2_ani"),
                (assign, ":var_9", "anim_field_working_2"),
            (else_try),
                (eq, ":var_1", "spr_z_entry_field_working_3"),
                (assign, ":var_8", -1),
                (assign, ":var_9", "anim_field_working_3"),
            (else_try),
                (eq, ":var_1", "spr_z_entry_grinding"),
                (assign, ":var_8", "itm_grinding_ani"),
                (assign, ":var_9", "anim_grinding"),
            (else_try),
                (eq, ":var_1", "spr_z_entry_fisherman_sitting"),
                (assign, ":var_8", "itm_fishing_ani"),
                (assign, ":var_9", "anim_sitting_fishing"),
            (else_try),
                (eq, ":var_1", "spr_z_entry_woodcutting"),
                (assign, ":var_8", "itm_woodcutting_2_ani"),
                (assign, ":var_9", "anim_woodcutting_2"),
                (assign, ":var_7", "snd_agent_anim_woodcutting_2"),
            (else_try),
                (eq, ":var_1", "spr_z_entry_tavern_sitting"),
                (store_random_in_range, ":var_13", 0, 25),
                (val_mul, ":var_13", ":var_6"),
                (val_mod, ":var_13", 25),
                (try_begin),
                    (neg|ge, ":var_13", 5),
                    (neg|is_between, "$current_town", "p_village_1", "p_salt_mine"),
                    (store_faction_of_party, ":var_10", "$current_town"),
                    (val_add, ":var_13", 41),
                    (faction_get_slot, ":var_2", ":var_10", ":var_13"),
                (try_end),
                (try_begin),
                    (eq, ":var_3", 1),
                    (assign, ":var_8", -1),
                    (assign, ":var_9", "anim_sitting"),
                (else_try),
                    (eq, ":var_3", 2),
                    (assign, ":var_8", "itm_drinking_ani"),
                    (assign, ":var_9", "anim_sitting_drinking"),
                (else_try),
                    (eq, ":var_3", 3),
                    (assign, ":var_8", "itm_eating_ani"),
                    (assign, ":var_9", "anim_sitting_eating"),
                (try_end),
            (else_try),
                (eq, ":var_1", "spr_z_entry_village_sitting"),
                (try_begin),
                    (eq, ":var_3", 1),
                    (assign, ":var_8", "itm_sitting_working_1_ani"),
                    (assign, ":var_9", "anim_sitting_working_1"),
                (else_try),
                    (eq, ":var_3", 2),
                    (assign, ":var_8", "itm_sitting_working_2_ani"),
                    (assign, ":var_9", "anim_sitting_working_2"),
                (else_try),
                    (eq, ":var_3", 3),
                    (assign, ":var_8", "itm_sitting_working_3_ani"),
                    (assign, ":var_9", "anim_sitting_working_3"),
                (try_end),
            (try_end),
        (else_try),
            (eq, ":var_1", "spr_z_entry_brooming"),
            (assign, ":var_2", "trp_village_walker_6"),
            (assign, ":var_8", "itm_brooming_ani"),
            (assign, ":var_9", "anim_brooming"),
        (else_try),
            (eq, ":var_1", "spr_z_entry_cow"),
            (prop_instance_get_position, pos0, ":var_0"),
            (set_spawn_position, pos0),
            (store_random_in_range, ":var_8", 0, 2),
            (val_add, ":var_8", "itm_cow1"),
            (spawn_horse, ":var_8"),
        (else_try),
            (eq, ":var_1", "spr_z_entry_horse"),
            (prop_instance_get_position, pos0, ":var_0"),
            (set_spawn_position, pos0),
            (store_random_in_range, ":var_8", "itm_common_horse", "itm_cow1"),
            (spawn_horse, ":var_8"),
        (try_end),
    (try_end),
    (gt, ":var_2", 0),
    (prop_instance_get_position, pos0, ":var_0"),
    (set_spawn_position, pos0),
    (spawn_agent, ":var_2"),
    (assign, ":var_14", reg0),
    (try_begin),
        (gt, ":var_8", 0),
        (agent_get_item_slot, ":var_15", ":var_14", 7),
        (try_begin),
            (gt, ":var_15", 0),
            (agent_unequip_item, ":var_14", ":var_15"),
        (try_end),
        (agent_equip_item, ":var_14", ":var_8"),
    (try_end),
    (agent_set_team, ":var_14", 7),
    (agent_set_stand_animation, ":var_14", ":var_9"),
    (agent_set_animation, ":var_14", ":var_9"),
    (assign, ":var_16", 1),
    (convert_to_fixed_point, ":var_16"),
    (store_random_in_range, ":var_17", 0, ":var_16"),
    (agent_set_animation_progress, ":var_14", ":var_17"),
    (2077, ":var_14", 0),
    (agent_set_slot, ":var_14", 34, ":var_0"),
    (try_begin),
        (gt, ":var_7", 0),
        (agent_play_sound, ":var_14", ":var_7"),
        (agent_set_slot, ":var_14", 35, 2),
    (else_try),
        (eq, ":var_1", "spr_z_entry_child_sitting"),
        (agent_set_slot, ":var_14", 35, 2),
    (else_try),
        (agent_set_slot, ":var_14", 35, 1),
    (try_end),

]),


509, 快速放箭
      (try_begin),
        (eq, ":weapon_type", itp_type_bow),
        (agent_get_ammo, ":ammo_num", ":agent_no", 0),
        (agent_get_attack_action, ":is_attacking", ":agent_no"),
        (agent_get_combat_state, ":combat_stat", ":agent_no"),

        (try_begin),
          (eq, ":is_attacking", 1),
          (agent_get_slot, ":quick_shoot", ":agent_no", 509),
          (val_add, ":quick_shoot", 1),
          (agent_set_slot, ":agent_no", 509, ":quick_shoot"),
          (try_begin),
            (gt, ":quick_shoot", 10),
            (agent_set_attack_action, ":agent_no", 3, 0),
            (agent_set_slot, ":agent_no", 509, 1),
          (try_end),
        (else_try),
          (eq, ":combat_stat", 1),
          (agent_get_slot, ":quick_shoot", ":agent_no", 509),
          (val_add, ":quick_shoot", 1),
          (agent_set_slot, ":agent_no", 509, ":quick_shoot"),
          (try_begin),
            (agent_set_attack_action, ":agent_no", 3, 1),
            (agent_set_slot, ":agent_no", 509, 1),
          (try_end),
        (else_try),
          (agent_set_slot, ":agent_no", 509, 1),
          (try_begin)
            (eq, ":is_attacking", 0),
            (agent_get_speed, pos29, ":agent_no"),
            (position_get_y, ":agent_speed", pos29),
            (eq, ":agent_speed", 0),
            (agent_force_rethink, ":agent_no"),
          (try_end),
        (try_end),
      (try_end),



    ("game_water_splash_3", psf_emit_at_water_level , "prt_mesh_water_wave_1",
     5, 2.0, 0, 0.0, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.03, 0.2), (1, 0.0),        #alpha keys
     (1.0, 1.0), (1, 1.0),      #red keys
     (1.0, 1.0), (1, 1.0),      #green keys
     (1.0, 1.0), (1, 1.0),      #blue keys
     (0.0, 3),   (1.0, 10),   #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0, 0, 0),                 #emit velocity
     0.0,                       #emit dir randomness
     0,                       #rotation speed
     0.5                        #rotation damping
    ),

地面光环效果