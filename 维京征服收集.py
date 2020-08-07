dedal_priest_regen = (3, 0, 0,[(multiplayer_is_server)],[
    (neq, "$g_multiplayer_game_type", multiplayer_game_type_deathmatch),
    (neq, "$g_multiplayer_game_type", multiplayer_game_type_duel),
    (neq, "$g_multiplayer_game_type", multiplayer_game_type_thor),
    (set_fixed_point_multiplier, 100),
    (try_for_agents,":priest"),
      (agent_is_alive,":priest"),
      (agent_is_human,":priest"),
      (agent_get_troop_id,":troop",":priest"),
      
      (this_or_next|eq,":troop","trp_norse_priest"),
      (this_or_next|eq,":troop","trp_saxon_priest"),
      (this_or_next|eq,":troop","trp_angle_priest"),
      (this_or_next|eq,":troop","trp_briton_priest"),
      (this_or_next|eq,":troop","trp_irish_priest"),
      (eq,":troop","trp_scotch_priest"),
      (agent_get_position,pos1,":priest"),
      (agent_get_team,":priest_team",":priest"),
      (try_for_agents,":agent",pos1,700),
        (agent_is_alive,":agent"),
        (agent_is_human,":agent"),
        (neq,":agent",":priest"),
        (agent_get_team,":team",":agent"),
        (eq,":priest_team",":team"),
        (store_agent_hit_points,":hp",":agent",0),
        (lt,":hp",100),
        (store_agent_hit_points,":hp",":agent",1),
        (val_add,":hp",1),
        (agent_set_hit_points,":agent",":hp",1),
      (try_end),
    (try_end),
])



dedal_falling_from_horse = (ti_on_agent_dismount, 0, 0, [
    (this_or_next|neg|game_in_multiplayer_mode),
    (multiplayer_is_server),
    (call_script,"script_check_falling_from_horse")],[])
    
  ("check_falling_from_horse", [
      (store_trigger_param,":rider",1),
      (store_trigger_param,":horse",2),
      (try_begin),
        (this_or_next|neg|game_in_multiplayer_mode),
        #(eq,"$g_multiplayer_allow_fall_from_horse_dmg",1),
        (agent_is_active,":horse"),
        (neg|agent_is_alive,":horse"),
        (agent_is_active,":rider"),
        (agent_is_alive,":rider"),
        
        (agent_get_speed,pos1,":horse"),
        (position_get_y,":speed",pos1),
        
        (convert_from_fixed_point,":speed"),
        (val_mul,":speed",5),
        (store_random_in_range,":damage",0,":speed"),
        
        (gt,":damage",0),
        (store_agent_hit_points,":hp",":rider",1),
        (val_sub,":hp",":damage"),
        (val_max,":hp",1),
        (agent_set_hit_points,":rider",":hp",1),
      (try_end),
  ]),
    
dedal_dehorsing = (ti_on_agent_hit, 0, 0, [
    (this_or_next|neg|game_in_multiplayer_mode),
    (multiplayer_is_server),
    (call_script,"script_check_dehorsing")],[])
  ("check_dehorsing", [
      (store_trigger_param,":victim",1),
      (store_trigger_param,":damage",3),
      (assign,":weapon",reg0),
      
      (try_begin),
        (eq,"$g_multiplayer_allow_fall_from_horse",1),
        (agent_is_active,":victim"),
        (agent_is_alive,":victim"),
        (this_or_next|agent_is_non_player,":victim"),#players can only be dehorsed once per spawn, otherwise collision bugs appear
        (agent_slot_eq,":victim",slot_agent_was_dehorsed,0),
        (agent_is_human,":victim"),
        (agent_get_horse,":horse",":victim"),
        (agent_is_active,":horse"),
        (agent_is_alive,":horse"),
                
        (ge,":damage",10),
        (store_agent_hit_points,":hp",":victim",1),
        (gt,":hp",":damage"),
        (store_random_in_range,":r",8,50),
        (gt,":damage",":r"),
        
        (item_get_type,":weapon_type",":weapon"),
        (neq,":weapon_type",itp_type_crossbow),
        (neq,":weapon_type",itp_type_bow),
        
        (agent_start_running_away,":horse"),
        (agent_stop_running_away,":horse"),
        
        (store_random_in_range,":anim","anim_rider_fall_right","anim_strike_chest_front_stop"),
        (agent_set_animation,":victim",":anim"),
        (agent_set_slot,":victim",slot_agent_was_dehorsed,1),
        
        (try_begin),
          (game_in_multiplayer_mode),
          (try_for_players,":i",1),
            (multiplayer_send_3_int_to_player,":i",multiplayer_event_agent, me_agent_play_animation, ":victim",":anim"),
          (try_end),
        (try_end),
        
      (try_end),
  ]),
    
    
dedal_horse_blunt = (ti_on_agent_hit, 0, 0, [
    (this_or_next|neg|game_in_multiplayer_mode),
    (multiplayer_is_server),
    (call_script,"script_check_horse_blunt_damage")],[])
  ("check_horse_blunt_damage", [
      (store_trigger_param,":victim",1),
      (store_trigger_param,":dealer",2),
      (store_trigger_param,":damage",3),
      (assign,":weapon",reg0),
      
      (try_begin),
        (gt,":weapon",0),
        (agent_is_active,":victim"),
        (agent_is_alive,":victim"),
        (neg|agent_is_human,":victim"),
        (agent_is_active,":dealer"),
        (agent_get_action_dir,":swing",":dealer"),
        (is_between,":swing",1,3),#left or right
        (item_get_swing_damage_type,":dam_type",":weapon"),
        (eq,":dam_type",blunt),
        (val_div,":damage",2),
        (set_trigger_result,":damage"),
      (try_end),
      (assign,reg0,":damage"),
  ]),
  
dedal_shield_taunt = (0, 0, 1, [
    (neg|multiplayer_is_dedicated_server),
    (game_key_is_down,gk_quests_window),#####block movement? change key?
    (game_key_is_down,gk_defend),
    ],[
    (call_script,"script_shield_taunt_trigger")])
    
    
dedal_shield_taunt_sp = (0, 0, 1, [######Singleplayer version (action key)
    (neg|multiplayer_is_dedicated_server),
    (game_key_is_down,gk_action),###########!!!
    (game_key_is_down,gk_defend),
    ],[
    (call_script,"script_shield_taunt_trigger")])
    
  ("shield_taunt_trigger", [
      (get_player_agent_no,":agent"),
      (try_begin),
        (agent_is_active,":agent"),
        (agent_is_alive,":agent"),
        (agent_get_wielded_item,":item",":agent",1),
        (gt,":item",0),#has shield
        (agent_get_wielded_item,":item",":agent",0),
        (gt,":item",0),#has weapon
        (item_get_type,":item_type",":item"),
        (this_or_next|eq,":item_type",itp_type_polearm),
        (eq,":item_type",itp_type_one_handed_wpn),
        (agent_get_horse,":horse",":agent"),
        (eq,":horse",-1),#not on horse
        (try_begin),
          (game_in_multiplayer_mode),
          (multiplayer_send_int_to_server, multiplayer_event_agent, me_agent_shield_taunt),
        (else_try),
          (agent_set_animation, ":agent", "anim_shield_taunt", 1),
          (agent_play_sound, ":agent", "snd_shield_taunt"),
        (try_end),
      (try_end),
  ]),
    
dedal_shield_bash = (0, 0.35, 1,[
    (game_key_is_down,gk_defend),
    (game_key_clicked,gk_attack),
    #(game_key_is_down,gk_attack),
    (eq,"$g_multiplayer_allow_shield_bash",1),
    ],[
    (game_key_is_down,gk_defend),
    #(game_key_is_down,gk_attack),
    (call_script,"script_shield_bash_trigger")])
  ("shield_bash_trigger", [
      (get_player_agent_no,":agent"),
      (try_begin),
        (agent_is_active,":agent"),
        (agent_is_alive,":agent"),
        (agent_get_horse,":horse",":agent"),
        (eq,":horse",-1),#not on horse
        (agent_get_wielded_item,":item",":agent",1),
        (gt,":item",0),#has shield
        (agent_get_animation,":anim",":agent",0),
        (neg|is_between,":anim","anim_walk_forward_crouch","anim_ride_0"),#is not crouching
        (try_begin),
          (agent_slot_eq,":agent",slot_agent_shieldbash_cooldown,0), #colldown for sp vc-2854
          (call_script,"script_shield_bash_script",1,":agent",0),
        (try_end),
      (try_end),
  ]),
    
dedal_shield_bash_AI = (2, 0, 0,[],[
    (eq,"$g_multiplayer_allow_shield_bash",1),
    (this_or_next|neg|game_in_multiplayer_mode),
    (multiplayer_is_server),
    (call_script,"script_shield_bash_AI_trigger")])

  ("shield_bash_AI_trigger", [
      
      # (try_begin),
      # (game_in_multiplayer_mode),
      # (eq,"$g_multiplayer_game_type",multiplayer_game_type_deathmatch),
      # (assign,":check_teams",0),
      # (else_try),
      # (assign,":check_teams",1),
      # (try_end),
      
      (try_for_agents,":agent"),
        (agent_is_alive,":agent"),
        (agent_is_human,":agent"),
        (try_begin),
          (agent_get_slot,":cooldown",":agent",slot_agent_shieldbash_cooldown),
          (gt,":cooldown",0),
          (val_sub,":cooldown",1),
          (agent_set_slot,":agent",slot_agent_shieldbash_cooldown,":cooldown"),
        (try_end),
        (agent_slot_eq,":agent",slot_agent_shieldbash_cooldown,0),
        (agent_is_non_player,":agent"),
        (agent_get_horse,":horse",":agent"),
        (eq,":horse",-1),#not on horse
        (agent_get_wielded_item,":item",":agent",1),
        (gt,":item",0),#has shield
        # (agent_get_team,":team",":agent"),
        (agent_get_position,pos1,":agent"),
        
        (assign,":enemies_close",0),
        (assign,":enemies_in_range",0),
        (agent_ai_get_num_cached_enemies, ":num_nearby_agents", ":agent"),
        (try_for_range, reg0, 0, ":num_nearby_agents"),
          (agent_ai_get_cached_enemy, ":i", ":agent", reg0),
          # (try_for_agents,":i"),
          (agent_is_alive,":i"),
          (agent_is_human,":i"),
          # (neq,":i",":agent"),
          # (agent_get_team,":i_team",":i"),
          # (this_or_next|eq,":check_teams",0),
          # (neq,":team",":i_team"),
          # (this_or_next|eq,":check_teams",0),
          # (teams_are_enemies,":team",":i_team"),
          (agent_get_horse,":horse",":i"),
          (eq,":horse",-1),#not on horse
          (agent_get_position,pos2,":i"),
          (neg|position_is_behind_position,pos2,pos1),
          (get_distance_between_positions,":dist",pos1,pos2),
          (lt,":dist",200),
          (val_add,":enemies_close",1),
          (lt,":dist",140),
          (val_add,":enemies_in_range",1),
        (try_end),
        (gt,":enemies_in_range",0),
        (val_add,":enemies_in_range",":enemies_close"),
        (val_mul,":enemies_in_range",3),
        (val_add,":enemies_in_range",7),
        
        (store_random_in_range,":r",0,50),
        (lt,":r",":enemies_in_range"),
        (call_script,"script_shield_bash_script",1,":agent",0),
      (try_end),
  ]),

  ("shield_bash_script", [
      (store_script_param,":continue",1),
      (store_script_param,":agent",2),
      (store_script_param,":player",3),
      
      (try_begin),
        (eq,":continue",0),#is not singleplayer
        (agent_is_alive,":agent"),
        (agent_slot_eq,":agent",slot_agent_shieldbash_cooldown,0),
        (agent_get_horse,":horse",":agent"),
        (eq,":horse",-1),#not on horse
        (agent_get_wielded_item,":item",":agent",1),
        (gt,":item",0),#has shield
        (assign,":continue",2),
      (try_end),
      
      (try_begin),
        (ge,":continue",1),
        (agent_get_position,pos1,":agent"),
        (agent_set_animation,":agent","anim_shield_bash"),
        (agent_set_slot,":agent",slot_agent_shieldbash_cooldown,shielbash_miss_cooldown),# 1x2= 2sec
        
        (try_begin),
          (eq,":continue",2),#multi
          (try_for_players,":i",1),
            (multiplayer_send_3_int_to_player,":i",multiplayer_event_agent,me_agent_play_animation,":agent","anim_shield_bash"),
          (try_end),
          (player_get_gender,":gender",":player"),
        (else_try),
          (agent_get_troop_id,":troop",":agent"),
          (troop_get_type,":gender",":troop"),
          (val_mod,":gender",2),
        (try_end),
        (try_begin),
          (eq,":gender",0),
          (agent_play_sound,":agent","snd_man_shield_bash"),
        (else_try),
          (agent_play_sound,":agent","snd_woman_shield_bash"),
        (try_end),
        
        (assign,":victim",-1),
        (assign,":min_dist",125),#125cm
        (try_begin),#Players
          (neg|agent_is_non_player,":agent"),
          (try_for_agents,":i"),
            (neq,":i",":agent"),
            (agent_is_alive,":i"),
            (agent_is_human,":i"),
            (agent_get_position,pos2,":i"),
            (get_distance_between_positions,":dist",pos1,pos2),
            (le,":dist",":min_dist"),
            (neg|position_is_behind_position,pos2,pos1),
            (assign,":victim",":i"),
            (assign,":min_dist",":dist"),
          (try_end),
        (else_try),#AI
          (agent_ai_get_num_cached_enemies, ":num_nearby_agents", ":agent"),
          (try_for_range, reg0, 0, ":num_nearby_agents"),
            (agent_ai_get_cached_enemy, ":i", ":agent", reg0),
            (neq,":i",":agent"),
            (agent_is_alive,":i"),
            (agent_is_human,":i"),
            (agent_get_position,pos2,":i"),
            (get_distance_between_positions,":dist",pos1,pos2),
            (le,":dist",":min_dist"),
            (neg|position_is_behind_position,pos2,pos1),
            (assign,":victim",":i"),
            (assign,":min_dist",":dist"),
          (try_end),
        (try_end),
        (agent_is_active,":victim"),
        (agent_get_horse,":horse",":victim"),
        (eq,":horse",-1),#not on horse
        
        (agent_set_slot,":agent",slot_agent_shieldbash_cooldown,shielbash_hit_cooldown),# 10x2= 20sec after successful hit
        (agent_set_animation,":victim","anim_shield_bash_hit"),
        (agent_play_sound,":victim","snd_shield_hit_wood_wood"),
        (try_begin),
          (eq,":continue",2),#multi
          (try_for_players,":i",1),
            (multiplayer_send_3_int_to_player,":i",multiplayer_event_agent,me_agent_play_animation,":victim","anim_shield_bash_hit"),
          (try_end),
        (try_end),
      (try_end),
  ]),
  ("berserk_trigger", [
      (try_begin),
        (this_or_next|neg|game_in_multiplayer_mode),
        (neq,"$g_multiplayer_game_type",multiplayer_game_type_duel),
        (get_player_agent_no,":agent"),
        (agent_is_active,":agent"),
        (agent_is_alive,":agent"),
        (call_script,"script_cf_agent_is_not_peasant",":agent"),
        (try_begin),
          (game_in_multiplayer_mode),
          (multiplayer_send_int_to_server,multiplayer_event_agent,me_agent_berserk),
        (else_try),
          (eq,"$berserk_cooldown",0),
          (assign,"$berserk_cooldown",180),#once per 3 min
          
          (troop_get_type, ":is_female", "trp_player"),
          (val_mod, ":is_female", 2),
          (try_begin),
            (eq, ":is_female", 1), #player is female
            (agent_play_sound,":agent","snd_woman_yell"),###ARCRY SOUND
          (else_try),
            (agent_play_sound,":agent","snd_man_warcry"),###ARCRY SOUND
          (try_end),
          
          (agent_set_damage_modifier,":agent",125),
          (call_script, "script_advanced_agent_set_speed_modifier",":agent",110),
          (agent_set_accuracy_modifier,":agent",50),
          (agent_set_reload_speed_modifier,":agent",50),
          (agent_set_slot,":agent",slot_agent_berserk_cooldown,50),
          (agent_set_slot,":agent",slot_agent_horn_cooldown,0),
          (display_message,"@You unleash your battle rage!",0x000000),
          (assign,"$is_berserk",1),
        (else_try),
          (display_message,"@You are too exhausted to go into a battle rage."),
        (try_end),
      (try_end),
  ]),
  ("berserk_cooldown_trigger", [##SP only
      (try_begin),
        (get_player_agent_no,":agent"),
        (agent_is_active,":agent"),
        (agent_is_alive,":agent"),
        (agent_get_slot,":cooldown",":agent",slot_agent_berserk_cooldown),
        (try_begin),
          (gt,":cooldown",0),
          (val_sub,":cooldown",1),
          (agent_set_slot,":agent",slot_agent_berserk_cooldown,":cooldown"),
          (try_begin),
            (eq,":cooldown",35),#is tired
            (agent_set_damage_modifier,":agent",60),
            (call_script, "script_advanced_agent_set_speed_modifier",":agent",70),
            (display_message,"@You feel exhausted after the rage.",0xff3333),
            (assign,"$is_berserk",-1),
            (mission_cam_animate_to_screen_color, 0x55000000, 2000),
          (else_try),
            (eq,":cooldown",0),#back to normal
            (agent_set_damage_modifier,":agent",100),
            (call_script, "script_advanced_agent_set_speed_modifier",":agent",100),
            (agent_set_accuracy_modifier,":agent",100),
            (agent_set_reload_speed_modifier,":agent",100),
            (display_message,"@Your strength is back.",0x88FF88),
            (assign,"$is_berserk",0),
            (mission_cam_animate_to_screen_color, 0x00000000, 2000),
          (try_end),
        (try_end),
      (try_end),
  ]),
  
  ("horn_sp_trigger", [#singleplayer only
      (get_player_agent_no,":agent"),
      (try_begin),
        (agent_is_active,":agent"),
        (agent_is_alive,":agent"),
        (agent_play_sound,":agent","snd_horn"),
        (agent_get_horse,":horse",":agent"),
        (try_begin),
          (agent_is_active,":horse"),
          (agent_set_animation,":agent","anim_horn",1),
        (else_try),
          (agent_set_animation,":agent","anim_horn",0),
        (try_end),
        
        ###horn effect
        #(call_script, "script_apply_courage_bonus", 2),
        (call_script, "script_change_courage_around_agent", 50, ":agent"),	#still needs to get balanced
      (try_end),
  ]),




dedal_priest_regen = (3, 0, 0,[(multiplayer_is_server)],[
    (neq, "$g_multiplayer_game_type", multiplayer_game_type_deathmatch),
    (neq, "$g_multiplayer_game_type", multiplayer_game_type_duel),
    (neq, "$g_multiplayer_game_type", multiplayer_game_type_thor),
    (set_fixed_point_multiplier, 100),
    (try_for_agents,":priest"),
      (agent_is_alive,":priest"),
      (agent_is_human,":priest"),
      (agent_get_troop_id,":troop",":priest"),
      
      (this_or_next|eq,":troop","trp_norse_priest"),
      (this_or_next|eq,":troop","trp_saxon_priest"),
      (this_or_next|eq,":troop","trp_angle_priest"),
      (this_or_next|eq,":troop","trp_briton_priest"),
      (this_or_next|eq,":troop","trp_irish_priest"),
      (eq,":troop","trp_scotch_priest"),
      (agent_get_position,pos1,":priest"),
      (agent_get_team,":priest_team",":priest"),
      (try_for_agents,":agent",pos1,700),
        (agent_is_alive,":agent"),
        (agent_is_human,":agent"),
        (neq,":agent",":priest"),
        (agent_get_team,":team",":agent"),
        (eq,":priest_team",":team"),
        (store_agent_hit_points,":hp",":agent",0),
        (lt,":hp",100),
        (store_agent_hit_points,":hp",":agent",1),
        (val_add,":hp",1),
        (agent_set_hit_points,":agent",":hp",1),
      (try_end),
    (try_end),
])





