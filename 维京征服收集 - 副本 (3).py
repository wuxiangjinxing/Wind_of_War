
  ("hunting",0,
    "You have encountered {s1}. What do you want to do?",
    "none",
    [
      (set_background_mesh, "mesh_pic_road_with_grove"),
      (assign, "$hunted_today", 1),
      
      (party_get_num_companions, reg6, "$g_encountered_party"),
      (try_begin),
        (eq, "$g_encountered_party_template", "pt_boar_herd"),
        (eq, reg6, 1),
        (str_store_string, s1, "@a lone boar"),
      (else_try),
        (eq, "$g_encountered_party_template", "pt_boar_herd"),
        (str_store_string, s1, "@a herd of {reg6} boar"),
      (else_try),
        (str_store_string, s1, "@a herd of {reg6} wild animals"),
      (end_try),
      
    ],


  ("hunting",mnf_scale_picture,
   "{10}",
   "none",
   [
       (party_get_slot, ":amount", "p_main_party", slot_party_hunting_amount),
       (party_get_slot, ":item", "p_main_party", slot_party_hunting_found),
       (str_store_item_name, s1, ":item"),
       (assign,"$hunted_animals",0),
       (assign,reg5, ":amount"),
       (try_begin),
         (gt, 1, ":amount"),
         (str_store_string, s10, "You have encountered a herd of {reg5}{s1}. What do you want to do?"),
       (else_try),
         (eq, 1, ":amount"),
         (str_store_string, s10, "You have encountered a lone {s1}. What do you want to do?"),
       (else_try),
         (str_store_string, s10, "@There are no remaining animals to slay."),
       (try_end),
       (set_background_mesh, "mesh_pic_cattle"),
   ],
    [
      ("hunt_go",[  
       (party_get_slot, ":num_boars", "p_main_party", slot_party_hunting_amount),
       (gt,":num_boars", 0),
      ],"Hunt some of the animals.",
       [
          (assign, "$loot_screen_shown", 0),
          (troop_clear_inventory, "trp_temp_troop"),
          
          (set_jump_mission,"mt_hunting"),
          (set_jump_entry, 0),
          (call_script, "script_setup_random_scene"),
          (jump_to_menu, "mnu_after_hunt"),
          (change_screen_mission),
        ]
       ),
      ("leave",[],"Leave.",
       [(change_screen_map),
        ]
       ),
       
       
       
       
      ]
  ),
  
  ("after_hunt",0,
    "{s1}",
    "none",
    [
      (set_background_mesh, "mesh_pic_cattle"),
       (party_get_slot, ":amount", "p_main_party", slot_party_hunting_amount),
       (party_get_slot, ":item", "p_main_party", slot_party_hunting_found),
       (str_store_item_name, s2, ":item"),
          
          
      (try_begin),
        (eq, "$loot_screen_shown", 0),
        (assign, "$loot_screen_shown", 1),
        (gt, "$hunted_animals", 0),
        (val_sub, ":amount", "$hunted_animals"),
        (party_set_slot, "p_main_party", slot_party_hunting_amount, ":amount"),
        (troop_clear_inventory, "trp_temp_troop"),
        (troop_add_items, "trp_temp_troop", "itm_boar_meat", "$hunted_animals"),
        (troop_add_items, "trp_temp_troop", "itm_raw_leather", "$hunted_animals"),

        (troop_sort_inventory, "trp_temp_troop"),
        (change_screen_loot, "trp_temp_troop"),
      (else_try),
        (gt, "$hunted_animals", 0),
        (assign, reg6, "$hunted_animals"),
        (str_store_string, s1, "@You successfully hunted {reg6} {s2}."),
      (else_try),
        (str_store_string, s1, "@You have lost track of the animals."),
      (end_try),
      
    ],
    [
      ("continue",[],"Continue.",
        [
          (change_screen_map),
        ]
      ),
      
    ]
  ),
  
  
  





















  ("hunting", mtf_battle_mode, 0,
    "You go hunting.",
    [
      (0,mtef_leader_only,af_override_horse, 0,1,[]),        #|af_override_weapons|af_override_head    #[itm_practice_bow_2,itm_barbed_arrows,itm_practice_lance,itm_practice_dagger]
      
    ],  
    [
      common_remove_banner_and_pole,
      cannot_spawn_commoners,
      #common_inventory_not_available,
      (ti_inventory_key_pressed, 0, 0, [],
        [
          (set_trigger_result, 1),
      ]),
      
      #1. Spawn the animals
      (ti_on_agent_spawn, 0, ti_once, [],
        [
          (assign, "$animals_flee", 0),
          
          (store_trigger_param, ":agent_no", 1),
          (set_fixed_point_multiplier, 100),
          (agent_get_position, pos1, ":agent_no"),
          (store_random_in_range, ":rand", 6000, 9000),
          (position_move_y, pos1, ":rand"),
          (store_random_in_range, ":rand", -1500, 1500),
          (position_move_x, pos1, ":rand"),
          (store_random_in_range, ":rand", 0, 360),
          (position_rotate_z, pos1, ":rand"),
          #(get_player_agent_no, ":player_agent"),
          #(agent_get_position, pos1, ":player_agent"),
          (set_spawn_position, pos1),
          (assign, reg1, 0),
          (assign, reg2, imod_cracked),
          (shuffle_range, 1, 3),
          (spawn_horse, "itm_animal_boar", reg1),
          (assign, "$alpha_animal", reg0),
          (party_get_num_companions, ":herd_size", "$g_encountered_party"),
          (gt, ":herd_size", 1),
          (try_for_range, ":unused", 1, ":herd_size"),
            (copy_position, pos2, pos1),
            (store_random_in_range, ":rand", -500, 500),
            (position_move_x, pos2, ":rand"),
            (store_random_in_range, ":rand", -500, 500),
            (position_move_y, pos2, ":rand"),
            (store_random_in_range, ":rand", -3000, 3000),
            (position_rotate_z, pos2, ":rand"),
            (set_spawn_position, pos2),
            (assign, reg1, 0),
            (assign, reg2, imod_cracked),
            (shuffle_range, 1, 3),
            (spawn_horse, "itm_animal_boar", reg1),
          (end_try),
      ]),
      
      #2. Animals wandering
      (5, 0, 0,
        [
          (eq, "$animals_flee", 0),
          (agent_is_alive, "$alpha_animal"),
          (store_random_in_range, ":rand", 0, 3),
          (eq, ":rand", 0),
        ],
        [
          #(display_message, "@Animals wander!"),
          (set_fixed_point_multiplier, 100),
          (agent_get_position, pos1, "$alpha_animal"),
          (store_random_in_range, ":rand", -3000, 3000),
          (position_move_x, pos1, ":rand"),
          (store_random_in_range, ":rand", -3000, 3000),
          (position_move_y, pos1, ":rand"),
          (store_random_in_range, ":rand", 0, 360),
          (position_rotate_z, pos1, ":rand"),
          (try_for_agents, ":agent"),
            (neg|agent_is_human, ":agent"),
            (agent_is_alive, ":agent"),
            #(agent_set_speed_modifier, ":agent", 10),
            #(agent_set_horse_speed_factor, ":agent", 25),
            (copy_position, pos2, pos1),
            (store_random_in_range, ":rand", -500, 500),
            (position_move_x, pos2, ":rand"),
            (store_random_in_range, ":rand", -500, 500),
            (position_move_y, pos2, ":rand"),
            (store_random_in_range, ":rand", -3000, 3000),
            (position_rotate_z, pos2, ":rand"),
            (set_spawn_position, pos2),
            (agent_set_speed_limit, ":agent", 1),
            (agent_set_scripted_destination, ":agent", pos2, 1),
          (end_try),
      ]),
      
      #3. Animals react on player
      (0.5, 0, 0,
        [
          (try_begin),
            (gt, "$animals_flee", 1),
            (val_sub, "$animals_flee", 1),
          (end_try),
          (agent_is_alive, "$alpha_animal"),
        ],
        [
          (set_fixed_point_multiplier, 100),
          (agent_get_position, pos1, "$alpha_animal"),
          (get_player_agent_no, ":player_agent"),
          (agent_get_position, pos2, ":player_agent"),
          (get_distance_between_positions, ":distance", pos1, pos2),
          (try_begin),
            (eq, "$player_is_creeping", 1),
            (val_add, ":distance", 500),
          (end_try),
          (try_begin),
            (eq, "$animals_flee", 0),
            (lt, ":distance", 2500),
            (assign, reg1, 6),
            (assign, reg2, 4),
            (assign, reg3, -1),
            (shuffle_range, 1, 4),
            (assign, "$animals_flee", reg1),
            #(display_message, "@Animals react on low distance!"),
            (try_for_agents, ":agent"),
              (neg|agent_is_human, ":agent"),
              (agent_is_alive, ":agent"),
              #run:
              (agent_clear_scripted_mode, ":agent"),
              (agent_set_speed_limit, ":agent", 100),
              (agent_start_running_away, ":agent", 0),
            (end_try),
          (else_try),
            (eq, "$animals_flee", 1),
            (lt, ":distance", 5000),
            (assign, "$animals_flee", 0),
            (try_for_agents, ":agent"),
              (neg|agent_is_human, ":agent"),
              (agent_is_alive, ":agent"),
              #stop:
              (agent_set_speed_limit, ":agent", 1),
              (agent_stop_running_away, ":agent"),
            (end_try),
          (else_try),
            (eq, "$animals_flee", -1),    # =animals attack
            (try_for_agents, ":agent"),
              (neg|agent_is_human, ":agent"),
              (agent_is_alive, ":agent"),
              (agent_get_position, pos1, ":agent"),
              (copy_position, pos3, pos1),
              (position_move_y, pos3, -10),    #-10cm
              (get_distance_between_positions, ":back_distance", pos2, pos3),
              (position_move_y, pos3, 25),    #+15cm
              (get_distance_between_positions, ":front_distance", pos2, pos3),
              (this_or_next|lt, ":front_distance", ":back_distance"),
              (gt, ":distance", 1000),
              (call_script, "script_point_y_toward_position", pos1, pos2),
              (set_fixed_point_multiplier, 100),
              (position_move_y, pos1, 5000),    #50m
              (agent_start_running_away, ":agent", pos1),
            (end_try),
          (end_try),
      ]),
      
      (ti_on_agent_hit, 0, 0, [],
        [
          # Animals react on hit
          (assign, reg1, -1),
          (assign, reg2, -1),
          (assign, reg3, 4),
          (shuffle_range, 1, 4),
          (assign, "$animals_flee", reg1),
          #(display_message, "@Animals react on hit!"),
          (try_for_agents, ":agent"),
            (neg|agent_is_human, ":agent"),
            (agent_is_alive, ":agent"),
            #run:
            (agent_clear_scripted_mode, ":agent"),
            (agent_set_speed_limit, ":agent", 100),
            (agent_start_running_away, ":agent", 0),
          (end_try),
          
          (store_trigger_param, ":inflicted_agent_id", 1),
          (agent_is_active, ":inflicted_agent_id"),
          (agent_is_alive, ":inflicted_agent_id"),
          (try_begin),
            #Player stops creeping on hit
            (agent_is_human, ":inflicted_agent_id"),
            (assign, "$player_is_creeping", 0),
          (else_try),
            # Wounded animals get slower
            (store_agent_hit_points, ":agent_hp", ":inflicted_agent_id", 0),
            #(agent_set_speed_modifier, ":inflicted_agent_id", ":agent_hp"),
            #(agent_set_horse_speed_factor, ":agent", ":agent_hp"),
            (agent_set_speed_limit, ":inflicted_agent_id", ":agent_hp"),
          (end_try),
      ]),
      
      # Kill count
      (ti_on_agent_killed_or_wounded, 0, 0, [],
        [
          (store_trigger_param, ":agent_no", 1),
          (neg|agent_is_human, ":agent_no"),
          (val_add, "$hunted_animals", 1),
          (troop_add_items, "trp_temp_troop", "itm_venison", 1),
          
          (eq, "$alpha_animal", ":agent_no"),
          (try_for_agents, ":agent"),
            (neg|agent_is_human, ":agent"),
            (agent_is_alive, ":agent"),
            (assign, "$alpha_animal", ":agent"),
          (end_try),
          (eq, "$alpha_animal", ":agent_no"),
          #(finish_mission, 10),
          (assign,"$g_battle_won", 1),
          
      ]),
      
      # If alpha animal flee
      (1, 0, 2,
        [
          (this_or_next|neg|agent_is_alive, "$alpha_animal"),
          (neg|agent_is_active, "$alpha_animal"),
        ],
        [
          (try_for_agents, ":agent"),
            (neg|agent_is_human, ":agent"),
            (agent_is_alive, ":agent"),
            (agent_is_active, ":agent"),
            (assign, "$alpha_animal", ":agent"),
          (end_try),
          (this_or_next|neg|agent_is_alive, "$alpha_animal"),
          (neg|agent_is_active, "$alpha_animal"),
          #(finish_mission, 10),
          (assign,"$g_battle_won", 1),
          
      ]),
      
      
      
      # End
      (3, 0, ti_once,
        [
          (this_or_next|main_hero_fallen),
          (eq, "$g_battle_won", 1),
        ],
        [
          (try_begin),    #VC-2635
            (main_hero_fallen),
            (assign, "$hunted_animals", 0),
            (troop_clear_inventory, "trp_temp_troop"),
          (try_end),
          (finish_mission, 10),
      ]),
      
      (ti_tab_pressed, 0, 0, [],
        [
          (set_trigger_result, 1),
      ]),
      
      (0, 0, ti_once, [],
        [
          (assign, "$animals_flee", 0),
          (assign, "$hunted_animals", 0),
          (assign, "$player_is_creeping", 0),
          
          (play_sound,"snd_ambient_day_forest_loop"),
          (assign,"$g_battle_won",0),
          #(call_script, "script_music_set_situation_with_culture", mtf_sit_travel),
          (music_set_situation, 0),
      ]),
      
      (ti_before_mission_start, 0, 0, [],
        [
          (team_set_relation, 0, 2, 1),
          (team_set_relation, 1, 3, 1),
          
          (party_clear, "p_routed_enemies"),
          
          (assign, "$g_latest_order_1", 1),
          (assign, "$g_latest_order_2", 1),
          (assign, "$g_latest_order_3", 1),
          (assign, "$g_latest_order_4", 1),
      ]),
      
    ]
  ),
