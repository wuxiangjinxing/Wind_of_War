slot_agent_bonus_ammo = 24
slot_agent_bonus_cooldown = 27
#Values for agent_get_combat_state
cs_free                      = 0
cs_target_in_sight           = 1     # ranged units
cs_guard                     = 2     # no shield
cs_wield                     = 3     # reach out weapon, preparing to strike, melee units
cs_fire                      = 3     # ranged units
cs_swing                     = 4     # cut / thrust, melee units
cs_load                      = 4     # crossbow units
cs_still                     = 7     # melee units, happens, not always (seems to have something to do with the part of body hit), when hit
cs_no_visible_targets        = 7     # ranged units or blocking iwth a shield
cs_target_on_right_hand_side = 8     # horse archers



#amf_use_defend_speed instead of amf_use_weapon_speed to discount main-hand weapon
 ["ready_pistol_alt", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_defend_parry|amf_use_defend_speed|amf_keep|amf_client_owner_prediction|amf_rider_rot_throw,
   [0.3, "shoot_pistol", 0, 15, arf_blend_in_8],
 ],
 #amf_rider_rot_throw to get left side, acf_rot_vertical_bow to get vertical flexibility
 ["shoot_pistol", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_throw|amf_use_defend_speed|amf_play|amf_client_owner_prediction|amf_rider_rot_throw|amf_continue_to_next,
   [0.42, "shoot_pistol", 0, 27, arf_blend_in_6],
 ],
 # ["unused_human_anim_46", 0, 0, [1.0, "anim_human", 0, 1, 0]],
 ["reload_pistol_alt", 0, amf_priority_reload|amf_use_defend_speed|amf_play|amf_hide_weapon,
   [2.7, "shoot_pistol",  28, 237, arf_blend_in_8],
 ],
 
 
 
 common_secondary_fire = [
    #test for ammo when spawned
    (ti_on_agent_spawn, 0, 0, [],
      [
      (store_trigger_param_1, ":agent_no"),
      (agent_is_human, ":agent_no"),
      (call_script, "script_agent_init_secondary_ammo", ":agent_no"),
      ]
    ),

    #ai loop
    (2, 0, 0, [],
    [
    (try_for_agents, ":agent_no"),
      
      (agent_is_active, ":agent_no"),
      (agent_is_human, ":agent_no"),
      (agent_is_alive, ":agent_no"),
      (agent_is_non_player, ":agent_no"),

      #(agent_slot_ge, ":agent_no", slot_agent_bonus_ammo, 1),
      (agent_get_wielded_item, ":pistol", ":agent_no", 1),
      (eq, ":pistol", "itm_flintlock_shield"),
      (agent_get_slot, ":interval", ":agent_no", slot_agent_bonus_cooldown),
      (agent_get_slot, ":ammo", ":agent_no", slot_agent_bonus_ammo),
      (try_begin),  #reloading
        (lt, ":ammo", 0),
        (gt, ":interval", 100),
        (val_sub, ":interval", 10),
        (val_add, ":ammo", 1),
        (val_mul, ":ammo", -1),
        (agent_set_slot, ":agent_no", slot_agent_bonus_ammo, ":ammo"),
        (str_store_string, s2, "@reloading"),
        (agent_set_animation, ":agent_no", "anim_reload_pistol_alt"),
        (agent_set_animation_progress, ":agent_no", 0),
      (else_try), #decreasing
        (gt, ":interval", 0),
        (agent_get_troop_id, ":troop_no", ":agent_no"),
        (store_skill_level, ":skill", "skl_weapon_master", ":troop_no"),
        (val_add, ":skill", 3),
        (val_sub, ":interval", ":skill"),
        (str_clear, s2),
      (else_try), #targeting
        (le, ":interval", 0),
        (gt, ":ammo", 0),
        (try_begin),
          (call_script, "script_cf_agent_secondary_target", ":agent_no"),
          (store_random_in_range, ":interval", 150, 300),
          (str_store_string, s2, "@shooting"),
        (else_try), #failed target
          (store_random_in_range, ":random_no", 30, 75),
          (val_add, ":interval", ":random_no"),
          (str_store_string, s2, "@waiting"),
        (try_end),
      (try_end),
      (val_max, ":interval", 0),
      (try_begin),
        (neg|str_is_empty, s2),
        (str_store_agent_name, s1, ":agent_no"),
        (assign, reg0, ":agent_no"),
        (assign, reg1, ":ammo"),
        (assign, reg2, ":interval"),
        (display_message, "@{reg0}:{s1} has {reg1} extra ammo left with {reg2} interval while {s2}"),
      (try_end),
      (agent_set_slot, ":agent_no", slot_agent_bonus_cooldown, ":interval"),
    (try_end),
    
    ]),

      #separate handler for actual firing
      (1, 3, 5, [
        # (get_player_agent_no, "$g_player_agent"),
        (agent_is_alive, "$g_player_agent"),
        (agent_get_animation, ":animation", "$g_player_agent", 1),
        (eq, ":animation", "anim_ready_pistol_alt"), #ready state, not interrupted
        (neg|game_key_is_down, gk_defend),
        (agent_get_slot, ":ammo", "$g_player_agent", slot_agent_bonus_ammo),
        (gt, ":ammo", 0), #has shots left, not reloading
        (agent_get_wielded_item, ":pistol", "$g_player_agent", 1),
        (eq, ":pistol", "itm_flintlock_shield"),
        (call_script, "script_agent_secondary_fire", "$g_player_agent"), #ammo is flipped here
      ],
      #finish reload action after 3 seconds - animation can become interrupted but who cares
      [
        (get_player_agent_no, "$g_player_agent"),
        #do slot usage
        (agent_get_slot, ":ammo", "$g_player_agent", slot_agent_bonus_ammo),
        (val_mul, ":ammo", -1), #renormalize count
        (val_sub, ":ammo", 1),
        (try_begin), #depleted bonus ammo, going into regular pool
          (le, ":ammo", 0),
          (assign, ":ammo", -1),
          (try_for_range, ":item_slots", ek_item_0, ek_head),
            (agent_get_item_slot, ":cur_item", "$g_player_agent", ":item_slots"),
            (gt, ":cur_item", 0),
            (item_get_type, ":cur_type", ":cur_item"),
            (eq, ":cur_type", itp_type_bullets),
            (agent_get_ammo_for_slot, ":cur_ammo", "$g_player_agent", ":item_slots"),
            (val_add, ":ammo", ":cur_ammo"),
          (try_end),
          (try_begin),
            (neq, ":ammo", -1),
            (agent_set_ammo, "$g_player_agent", "itm_cartridges", ":ammo"), #this line might change to accomodate other types
            (assign, ":ammo", 1), #take bullet from main ammo stack
          (else_try),
            (assign, ":ammo", 0),
          (try_end),
        (try_end),
        # (val_max, ":ammo", 0),
        (agent_set_slot, "$g_player_agent", slot_agent_bonus_ammo, ":ammo"),

        # (agent_set_ammo, ":player_agent", "itm_cartridges", ":ammo"),
        # (presentation_set_duration, 0), #remove the crosshair
        # (try_begin),
          # (eq, ":ammo", 0),
          # (display_message, "@No more secondary ammo...", 0xff99aa),
        # (try_end),
        # (call_script, "script_agent_secondary_fire", ":player_agent"),
      ]
      ),
      #try not to check every frame to prevent sticky triggers
      (0.5, 0, 5, [
        (game_key_is_down, gk_defend),
        # (get_player_agent_no, "$g_player_agent"),
        (agent_is_alive, "$g_player_agent"),

        (agent_get_wielded_item, ":pistol", "$g_player_agent", 1),
        (eq, ":pistol", "itm_flintlock_shield"), #test for first behaviour
        (agent_get_animation, ":animation", "$g_player_agent", 1),
        #not already reloading (either hands)
        (neg|is_between, ":animation", "anim_ready_pistol_alt", "anim_unused_human_anim_47"),
        (neg|is_between, ":animation", "anim_ready_pistol", "anim_ready_swingright_fist"),
      ],
      [
        # (get_player_agent_no, "$g_player_agent"),
        (agent_get_slot, ":ammo", "$g_player_agent", slot_agent_bonus_ammo),
        (try_begin),
          (gt, ":ammo", 0), #has shots left
          # (agent_get_animation, ":animation", "$g_player_agent", 1),
          # (try_begin), #make sure the priority is higher?
            # (eq, ":animation", "anim_ready_pistol_alt"), #now handled in separate release trigger
            # (call_script, "script_agent_secondary_fire", "$g_player_agent"),
          # (else_try), #the ready animation already has a high piority to override the defend from shields
          (agent_set_animation, "$g_player_agent", "anim_ready_pistol_alt", 1), #keep position
          # (try_end),
          (try_begin), #do crosshair jittering somehow
            (neg|is_presentation_active, "prsnt_cross_hair"),
            (start_presentation, "prsnt_cross_hair"),
          (try_end),
        (else_try), #check for leftover ammunition from cartridges instead
          (is_presentation_active, "prsnt_cross_hair"),
          (display_message, "@Out of secondary ammo", 0xFF99AA),
          # (overlay_animate_to_alpha, "$g_quick_battle_map", 1500, 0),
          (presentation_set_duration, 0),
        (try_end),
      ]
      ),

      #doing the rising/falling edge here is probably preferrable to perpetual checking in presentations

      (ti_on_item_unwielded, 0, 0, [

        (store_trigger_param_1, ":agent_no"),
        # (get_player_agent_no, ":player_agent"),
        (eq, ":agent_no", "$g_player_agent"),

      ],
      [
        (store_trigger_param_2, ":item_no"),
        (eq, ":item_no", "itm_flintlock_shield"),
        # # (try_begin),
          # (is_presentation_active, "prsnt_cross_hair"),
          # (gt, "$g_quick_battle_map", 0),
          # (store_add, ":display", "$g_quick_battle_map", 1),
          # (overlay_animate_to_alpha, "$g_quick_battle_map", 500, 0),
          # # (overlay_set_alpha, "$g_quick_battle_map", 0),
          # (overlay_set_display, ":display", 0),
          # (store_add, ":tableau", ":display", 1),
          # (overlay_set_display, ":tableau", 0),
        # # (try_end),
         (presentation_set_duration, 0),
      ]),

      (ti_on_item_wielded, 0, 0, [

        (store_trigger_param_1, ":agent_no"),
        # (get_player_agent_no, ":player_agent"),
        (eq, ":agent_no", "$g_player_agent"),

      ],
      [
        (store_trigger_param_2, ":item_no"),
        (eq, ":item_no", "itm_flintlock_shield"),
        (start_presentation, "prsnt_cross_hair"),
        # (try_begin),
          # (neg|is_presentation_active, "prsnt_cross_hair"),
          # (start_presentation, "prsnt_cross_hair"),
        # (else_try),
          # (gt, "$g_quick_battle_map", 0),
          # (store_add, ":display", "$g_quick_battle_map", 1),
          # (overlay_animate_to_alpha, "$g_quick_battle_map", 750, 0xFF),
          # # (overlay_set_alpha, "$g_quick_battle_map", 0xFF),
          # (overlay_set_display, ":display", 1),
          # (store_add, ":tableau", ":display", 1),
          # (overlay_set_display, ":tableau", 1),
        # (try_end),
      ]),

      (ti_on_item_dropped, 0, 0, [

        (store_trigger_param_1, ":agent_no"),
        # (get_player_agent_no, ":player_agent"),
        (eq, ":agent_no", "$g_player_agent"),

      ],
      [ (store_trigger_param_1, ":player_agent"),
        (store_trigger_param_2, ":item_no"),
        (eq, ":item_no", "itm_flintlock_shield"),
        (store_trigger_param_3, ":prop_no"),
        (try_begin), #no additional cartridges
          (agent_get_slot, ":ammo", ":player_agent", slot_agent_bonus_ammo),
          (is_between, ":ammo", 0, 5),
          (scene_prop_set_slot, ":prop_no", scene_prop_slots_end, ":ammo"),
          (agent_set_slot, ":player_agent", slot_agent_bonus_ammo, 0),
        (else_try), #average of 5 bullets left
          (gt, ":ammo", 5),
          (val_sub, ":ammo", 5),
          (scene_prop_set_slot, ":prop_no", scene_prop_slots_end, 5),
          (agent_set_slot, ":player_agent", slot_agent_bonus_ammo, ":ammo"),
        (try_end),
      ]),

      (ti_on_item_picked_up, 0, 0, [
        (store_trigger_param_1, ":agent_no"),
        # (get_player_agent_no, ":player_agent"),
        (eq, ":agent_no", "$g_player_agent"),
      ],
      [ (store_trigger_param_1, ":player_agent"),
        (store_trigger_param_2, ":item_no"),
        (eq, ":item_no", "itm_flintlock_shield"),
        (store_trigger_param_3, ":prop_no"),

        (scene_prop_get_slot, ":ammo", ":prop_no", scene_prop_slots_end),
        (agent_get_slot, ":cur_ammo", ":player_agent", slot_agent_bonus_ammo),
        (val_add, ":cur_ammo", ":ammo"),
        (agent_set_slot, ":player_agent", slot_agent_bonus_ammo, ":cur_ammo"),
      ]),
]




  #script_agent_init_secondary_ammo
  #gets the total ammunition (bullets) for an agent
  #call this when the agent spawns or refills ammo (including player chests?), do not allow picking up cartridges (duh)
  ("agent_init_secondary_ammo",
    [
    (store_script_param, ":agent_no", 1),
    (assign, ":ammo", 0),
    (try_for_range, ":item_slots", ek_item_0, ek_head),
      (agent_get_item_slot, ":cur_item", ":agent_no", ":item_slots"),
      (gt, ":cur_item", 0),
      # (item_get_type, ":cur_type", ":cur_item"),
      (try_begin),
        # (eq, ":cur_type", itp_type_shield),
        (eq, ":cur_item", "itm_flintlock_shield"),
        (agent_get_troop_id, ":troop_no", ":agent_no"),

        (store_random_in_range, ":cur_ammo", 4, 7),
        (val_add, ":ammo", ":cur_ammo"),
        #bonus ammo from weapon proficiency?
      # (else_try),
        # (eq, ":cur_type", itp_type_bullets),
        # (agent_get_ammo_for_slot, ":cur_ammo", ":agent_no", ":item_slots"),
        # (val_add, ":ammo", ":cur_ammo"),
      # (try_end),
      (try_end),
    (try_end),
    (try_begin),
      (gt, ":ammo", 0),
      (store_skill_level, ":cur_ammo", "skl_weapon_master", ":troop_no"),
      (val_div, ":cur_ammo", 3),
      (val_add, ":ammo", ":cur_ammo"),
      (agent_set_slot, ":agent_no", slot_agent_bonus_ammo, ":ammo"),
      # #this is initialized for usage in later logic loops
      # (store_sub, "$g_shooter_agent", ":agent_no", 1),
      # (str_store_agent_name, s1, ":agent_no"),
      # (assign, reg1, ":ammo"),
      # (display_message, "@{s1} has {reg1} bonus ammo"),
      (try_begin),
        (neg|agent_is_non_player, ":agent_no"),
        (start_presentation, "prsnt_cross_hair"),
      (else_try), #frames between shots
        (store_random_in_range, ":cur_ammo", 10, 100),
        (agent_set_slot, ":agent_no", slot_agent_bonus_cooldown, ":cur_ammo"),
      (try_end),
    (try_end),
    ]
  ),
  ("agent_secondary_fire",
    [
    (store_script_param, ":agent_no", 1),
    # (store_script_param, ":item_no", 2),
    # (store_script_param, ":ammo_no", 3),
    (assign, ":item_no", "itm_flintlock_pistol"),
    (assign, ":ammo_no", "itm_cartridges2"),
    (set_fixed_point_multiplier, 1000),
    (agent_get_speed, pos1, ":agent_no"),
    (position_get_x, ":speed_x", pos1),
    (store_pow, ":speed_x", ":speed_x", 2),
    # (val_mul, ":speed_x", ":speed_x"),
    (position_get_y, ":speed_y", pos1),
    (store_pow, ":speed_y", ":speed_y", 2),
    # (val_mul, ":speed_y", ":speed_y"),
    (val_add, ":speed_x", ":speed_y"),
    (store_sqrt, ":speed", ":speed_x"),
    (val_mul, ":speed", 100),

    #the average "speed" should be around 5000
    (store_random_in_range, ":speed_x", 0, ":speed"),
    (store_random_in_range, ":speed_y", 0, ":speed"),
    (val_add, ":speed_x", 91000), #upper limit
    (val_mul, ":speed_y", -1),
    (val_add, ":speed_y", 89000), #lower limit
    #too lazy to do "inaccuracy" jittering, so speed modulation is fine for now

    (store_random_in_range, ":speed", ":speed_y", ":speed_x"),

    #position offsets from http://forums.taleworlds.com/index.php/topic,144557.msg3475169.html
    (agent_get_look_position, pos1, ":agent_no"),
    (position_move_y, pos1, 80, 0),

    (try_begin), #also do arc restriction here
       (agent_get_horse, ":horse", ":agent_no"),
       (gt, ":horse", 0),
       (position_move_z, pos1, 240, 0),
       (try_begin), #arc of about 70 to the right, 150 to the left
         (agent_get_position, pos2, ":horse"),
         (position_get_rotation_around_z, ":base", pos2),
         (position_get_rotation_around_z, ":turn", pos1),
         (store_sub, ":angle", ":base", ":turn"),
         (assign, ":color", 0xFFFFFF),
         (assign, ":rotation", 0),
         (try_begin), #right of horse
           (is_between, ":angle", 70, 135),
           (store_sub, ":rotation", ":angle", 70),
           (position_rotate_z, pos1, ":rotation"),
           (assign, ":color", 0xFFBB88),
         (else_try), #right of horse
           (is_between, ":angle", -290, -225),
           (store_add, ":rotation", ":angle", 290),
           (position_rotate_z, pos1, ":rotation"),
           (assign, ":color", 0xFF88BB),
         (else_try), #left of horse
           (is_between, ":angle", -235, -150),
           (store_add, ":rotation", ":angle", 150),
           (position_rotate_z, pos1, ":rotation"),
           (assign, ":color", 0x99AAFF),
         (else_try), #left of horse
           (is_between, ":angle", 135, 210),
           (store_sub, ":rotation", ":angle", 210),
           (position_rotate_z, pos1, ":rotation"),
           (assign, ":color", 0xAA99FF),
         (try_end),
         (assign, reg1, ":angle"),
         (assign, reg2, ":rotation"),
         (assign, reg3, ":base"),
         (assign, reg4, ":turn"),
         (position_get_rotation_around_z, reg5, pos1),
         (display_message, "@angle of {reg1}, corrected by {reg2} from {reg3}-{reg4} to {reg5}", ":color"),
       (try_end),
    (else_try),
        #do ground-based wandering here as well - weaponmaster based?
       (position_move_z, pos1, 150, 0),
    (try_end),

    #random spin direction
    (store_random_in_range, ":y_rotation", 0, 360),
    (position_rotate_y, pos1, ":y_rotation"),
    # #do the "important" stuff

    # (init_position, pos2),
    # (position_move_y, pos2, 500), #50 cm ahead?
    # (position_rotate_z, pos2, 120), #lift up slightly
    # (position_transform_position_to_parent, pos1, pos1, pos2),
    (add_missile, ":agent_no", pos1, ":speed", ":item_no", 0, ":ammo_no", 0),
    (agent_set_animation, ":agent_no", "anim_shoot_pistol", 1), #this will continue automatically into reload

    # #particle system (highly rotational dependent, could make do without it?
    (agent_play_sound, ":agent_no","snd_pistol_shot"),
    # (agent_get_position, pos1, ":agent_no"),
    (init_position, pos2),
    # (position_move_z, pos2, 150), #around chest level?
    # #do horse here if position is incorrect (scaled up by fixed point)
    # (try_begin),
      # (agent_get_horse, ":agent_horse", ":agent_no"),
      # (gt, ":agent_horse", 0),
      # (position_move_z, pos2, 123),
      # #also need to do angle restrictions from shooting the right side of the horse
    # (try_end),

    (position_set_x, pos2, -150),
    (position_set_y, pos2, 1100),
    (position_set_z, pos2, -1400),
    (position_transform_position_to_parent, pos1, pos1, pos52),
    # #might not do rotation properly?
    # # (add_missile, ":agent_no", pos1, ":speed", ":item_no", 0, "itm_cartridges", 0),
    # (set_spawn_position, pos1),
    # (spawn_scene_prop, "spr_tutorial_flag_red"),

    (particle_system_burst, "psys_new_pistol_smoke", pos1, 15),
    (particle_system_burst, "psys_new_pistol_flare", pos1, 10),
    # (agent_get_ammo, reg0, ":agent_no", 0),
    # (assign, reg1, ":speed"),
    # (agent_get_slot, reg2, ":agent_no", slot_agent_bonus_ammo),
    # (display_message, "@total 'ammo' is {reg0} + {reg2}, shot with speed {reg1}"),
    #cleanup - fiddle around with ammunition
    # (try_for_range, ":item_slots", ek_item_0, ek_head),
      # (agent_get_item_slot, ":cur_item", ":agent_no", ":item_slots"),
      # (gt, ":cur_item", 0),
      # (agent_get_ammo_for_slot, reg2, ":agent_no", ":item_slots"),
      # (try_begin),
        # (this_or_next|eq, ":cur_item", "itm_lute"),
        # (eq, ":cur_item", "itm_flintlock_shield"),
      # (try_end),
      # (item_get_type, ":cur_type", ":cur_item"),
      # (assign, reg1, ":item_slots"),
      # (str_store_item_name, s1, ":cur_item"),

      # #quite possibly amount LEFT in weapon, not for ammo
      # (agent_get_item_cur_ammo, reg3, ":agent_no", ":item_slots"),
      # (display_message, "@using {s1} in slot {reg1} with {reg2} slot and {reg3} cur"),
    # (try_end),
    #flip ammo count for reload
    (agent_get_slot, ":ammo", ":agent_no", slot_agent_bonus_ammo),
    (val_mul, ":ammo", -1),
    (agent_set_slot, ":agent_no", slot_agent_bonus_ammo, ":ammo"),

    # (val_sub, ":total_ammo", 1),
    # (agent_set_ammo, ":agent_no", ":ammo_item", ":total_ammo"),
    ]
  ),
  ("cf_agent_secondary_victim",
    [
    (store_script_param, ":target_agent", 1),
    (store_script_param, ":agent_no", 2),
    (store_script_param, ":cur_team", 3), #1 more operation to re-fetch?

    #state check
    (agent_is_active, ":target_agent"),
    # (agent_is_human, ":target_agent"),
    (agent_is_alive, ":target_agent"),
    (neq, ":target_agent", ":agent_no"),
    (agent_get_team, ":target_team", ":target_agent"),
    (teams_are_enemies, ":target_team", ":cur_team"),
    
    #position check
    (agent_get_position, pos52, ":target_agent"),
    (get_sq_distance_between_positions_in_meters, ":distance", pos52, pos51),
    (le, ":distance", 30),
    (position_move_z, pos52, 175, 0),
    (position_has_line_of_sight_to_position, pos51, pos52), #visibility
    # (position_is_behind_position, pos52, pos51), #no backshooting
    
    (ge, ":target_agent", 0),
    (assign, reg0, ":target_agent"),
    ]
  ),

  ("find_next_shooter_agent",
  [
    (assign, ":cur_agent", -1),
    (try_for_agents, ":new_agent"),
      (eq, ":cur_agent", -1),
      # (ge, ":new_agent", "$g_shooter_agent"),
      (agent_is_active, ":new_agent"),
      (agent_is_human, ":new_agent"),
      (agent_is_alive, ":new_agent"),
      (agent_is_non_player, ":new_agent"),
      (agent_slot_ge, ":new_agent", slot_agent_bonus_ammo, 1),
      (assign, ":cur_agent", ":new_agent"),
      # (assign, "$g_shooter_agent", ":cur_agent"),
    (try_end),
  ]),
  ("cf_agent_secondary_target",
    [
    (store_script_param_1, ":agent_no"),
    (set_fixed_point_multiplier, 1000),
    # (store_add, "$g_shooter_agent", ":agent_no", 1), #incrementing
    # (try_begin), #lower boundary
      # (le, "$g_shooter_agent", 0),
      # (call_script, "script_find_next_shooter_agent"),
      # (assign, ":agent_no", "$g_shooter_agent"),
    # (try_end),
    
    # (agent_is_active, ":agent_no"),
    # (agent_is_human, ":agent_no"),
    # (agent_is_alive, ":agent_no"),
    # (agent_is_non_player, ":agent_no"),
    # (str_store_agent_name, s1, ":agent_no"),
    # (agent_slot_ge, ":agent_no", slot_agent_bonus_ammo, 1),
    # (agent_get_wielded_item, ":pistol", ":agent_no", 1),
    # (eq, ":pistol", "itm_flintlock_shield"),
    #(str_store_string, s1, "@{s1} gear"),
    (str_store_agent_name, s1, ":agent_no"),
    # #state check for agent
    (agent_get_combat_state, ":cur_state", ":agent_no"),
    (neq, ":cur_state", cs_load), #not reloading main-hand pistol
    (neg|is_between, ":cur_state", cs_still, cs_target_on_right_hand_side),
    (assign, ":target_agent", -1),
    

    #state check for team/div
    (agent_get_team, ":cur_team", ":agent_no"),
    (agent_get_division, ":cur_class", ":agent_no"),
    (team_get_hold_fire_order, ":order", ":cur_team", ":cur_class"),
    (neq, ":order", aordr_hold_your_fire),
    (team_get_weapon_usage_order, ":order", ":cur_team", ":cur_class"),
    (neq, ":order", wordr_use_blunt_weapons),
    (str_store_string, s1, "@{s1} order"),
    
    (set_fixed_point_multiplier, 1000),
    (agent_get_look_position, pos51, ":agent_no"),
    (position_move_z, pos51, 175, 0),
    (try_begin), #already targetting
      (agent_ai_get_look_target, ":target_agent", ":agent_no"),
      (call_script, "script_cf_agent_secondary_victim", ":target_agent", ":agent_no", ":cur_team"),
      (str_store_string, s1, "@{s1} look"),
    (else_try),
      (assign, ":agent_count", 0),
      (str_store_string, s1, "@{s1} find"),

      (try_for_agents, ":new_agent"),
        (val_add, ":agent_count", 1),
        (eq, ":target_agent", -1),
        (call_script, "script_cf_agent_secondary_victim", ":new_agent", ":agent_no", ":cur_team"),
        (assign, ":target_agent", reg0),
      (try_end),
    (try_end),

    (ge, ":target_agent", 0),
    (agent_get_position, pos52, ":target_agent"),
    (position_move_z, pos52, 150, 0),
    (agent_set_look_target_position, ":agent_no", pos52),
    (str_store_agent_name, s2, ":target_agent"),
    (str_store_string, s1, "@{s1} {s2}"),
    (display_message, s1),
    (call_script, "script_agent_secondary_fire", ":agent_no"),
    ]
  ),
  
  
  
  
  
    ("cross_hair", prsntf_read_only, 0, [
    (ti_on_presentation_load,
     [
      (set_fixed_point_multiplier, 1000),
      (create_mesh_overlay, "$g_quick_battle_map", "mesh_crosshair"),
      (init_position, pos1),
      (position_set_x, pos1, 500),
      (position_set_y, pos1, 375),
      (overlay_set_position, "$g_quick_battle_map", pos1),
      # #triggering needs some work
      # (try_begin),
        # (game_key_is_down, gk_defend),
        # (overlay_animate_to_alpha, ":overlay", 3000, 0xFF),
      # (else_try),
        # (overlay_animate_to_alpha, ":overlay", 1500, 0),
      # (try_end),
      # (overlay_animate_to_alpha, "$g_quick_battle_map", 1000, 0xFF),
      (get_player_agent_no, ":player_agent"),
      (agent_get_slot, ":ammo", ":player_agent", slot_agent_bonus_ammo),
      (agent_get_wielded_item, ":shield", ":player_agent", 1),
      (gt, ":ammo", 0), #has shots left
      (assign, reg1, ":ammo"),
      (create_text_overlay, ":display", "@+{reg1}", tf_with_outline),
      (position_set_x, pos1, 1500),
      (position_set_y, pos1, 1500),
      (overlay_set_size, ":display", pos1),
      (position_set_x, pos1, 950),
      (position_set_y, pos1, 75),
      (overlay_set_position, ":display", pos1),
      (overlay_set_color, ":display", 0xFFFFFF),
      (try_begin),
        (eq, ":shield", "itm_flintlock_shield"),
        (create_mesh_overlay_with_item_id, ":tableau", ":shield"),
        # (position_move_y, pos1, 90),
        (position_set_y, pos1, 180),
        (overlay_set_position, ":tableau", pos1),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, ":tableau", pos1),
        (presentation_set_duration, 999999),
      (else_try),
        (create_mesh_overlay, ":tableau", "mesh_white_plane"),
      (try_end),
      
      ]),
      (ti_on_presentation_run,
      [
        (get_player_agent_no, ":player_agent"),
        # (gt, "$g_quick_battle_map", 0),
        (store_add, ":display", "$g_quick_battle_map", 1),
        # (store_add, ":tableau", ":display", 1),
        (agent_get_slot, ":ammo", ":player_agent", slot_agent_bonus_ammo),
        (try_begin), #reloading phase
          (lt, ":ammo", 0),
          (overlay_animate_to_alpha, "$g_quick_battle_map", 1000, 0),
          # (overlay_set_alpha, "$g_quick_battle_map", 0x00),
          # (overlay_set_alpha, ":display", 0x00),
          (overlay_set_color, ":display", 0xFFFAA99),
        (else_try), #actually out of ammo
          (eq, ":ammo", 0),
          (overlay_set_color, ":display", 0xFFF0000),
          (overlay_set_text, ":display", "@N/A"),
        (else_try), #activated and fully visible
          (game_key_is_down, gk_defend),
          # (agent_get_animation, ":animation", ":player_agent", 1),
          # (eq, ":animation", "anim_ready_pistol_alt"),
          (overlay_set_alpha, "$g_quick_battle_map", 0xFF),
          (assign, reg1, ":ammo"),
          (overlay_set_text, ":display", "@+{reg1}"),
          (overlay_set_color, ":display", 0xFFFFFF),
          #jittering based on agent speed / wpf / combat situation can be done here
        (try_end),
      
      ]),
    ]
    ),
    
    
    ("crosshair", 0, "crosshair", 0, 0, 0, 0, 0, 0, 1, 1, 1),
    
    
    ["flintlock_pistol2", "Flintlock Pistol", [("flintlock_pistol",0),("pistol_carry_new", ixmesh_carry),], itp_type_pistol |itp_merchandise|itp_primary ,itcf_shoot_pistol|itcf_reload_pistol|itc_scimitar|itcf_carry_buckler_left|itcf_show_holster_when_drawn, 230 , weight(1.5)|difficulty(0)|spd_rtng(25) | shoot_speed(160) | thrust_damage(45 ,pierce)|max_ammo(1)|accuracy(65),imodbits_none,
 [(ti_on_weapon_attack, [(store_trigger_param_1, ":agent_no"),
 (agent_play_sound, ":agent_no","snd_pistol_shot"),
 (position_move_x, pos1,27),(position_move_y, pos1,36),
 (particle_system_burst, "psys_new_pistol_smoke", pos1, 15),
 (particle_system_burst, "psys_torch_fire_sparks", pos1, 15),
 (store_trigger_param_1, ":agent_no"),
 (assign, reg0, ":agent_no"),
 (str_store_agent_name, s1, ":agent_no"),
 (agent_get_slot, reg1, ":agent_no", slot_agent_bonus_ammo),
 (agent_get_slot, reg2, ":agent_no", slot_agent_bonus_cooldown),
 (display_message, "@{reg0}:{s1} has {reg1} bonus ammo left with {reg2} interval"),
 (try_begin), #quick shot
   #(eq, 1, 0),
   (is_between, reg2, 0, 100),
   (agent_is_non_player, ":agent_no"),
   (agent_get_wielded_item, ":item", ":agent_no", 1),
   (eq, ":item", "itm_flintlock_shield"),
   (call_script, "script_agent_secondary_fire", ":agent_no"),
   (store_random_in_range, ":interval", 150, 200),
   (agent_set_slot, ":agent_no", slot_agent_bonus_cooldown, ":interval"),
 (try_end),
 ])]], 
 ["flintlock_shield","Flintlock Pistol Guard", [("copy_flintlock_pistol",0)], itp_type_shield|itp_force_attach_left_hand|itp_wooden_parry, itcf_carry_revolver_right, 118 , weight(2.5)|hit_points(80)|body_armor(1)|spd_rtng(28)|shield_height(1)|shield_width(1), imodbits_shield ],
 ["cartridges2","Waxed Cartridges", [("cartridge_c",0)], itp_type_bullets|itp_can_penetrate_shield|itp_unique|itp_no_pick_up_from_ground, 0, 12,weight(0.25)|abundance(30)|weapon_length(3)|thrust_damage(3,pierce)|max_ammo(4),imodbits_missile,],
 
 
 
 
    ("new_pistol_flare", psf_billboard_3d, "prt_mesh_fire_1",
     30, 0.2, 0.2, 0.0, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 1.0), (1, 0),        #alpha keys
     (0, 1.0), (0.4, 0.7),      #red keys
     (0, 0.5),(0.4, 0.1),       #green keys
     (0, 0.3), (0.4, 0.2),      #blue keys
     (0, 0.4),   (1, 1.0),   #scale keys
     (0.04, 0.04, 0.01),      #emit box size
     (0, 3, 0),               #emit velocity
     0.2,                       #emit dir randomness
     200,                       #rotation speed
     0.2                        #rotation damping
    ),

    ("new_pistol_smoke", psf_billboard_3d, "prt_mesh_dust_1",
     5, 4, 0.6, 0, 80.0, 2,  #(was 30. 1.5)   #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
    #for testing purposes of the below, life has been changed to 5.
     (0.0, 0.3), (1, 0),       #alpha keys
     (0.0, 0.62), (1, 0.3),      #red keys
     (0.0, 0.63),(1, 0.31),       #green keys
     (0.0, 0.63), (1, 0.4),      #blue keys
     (0, 2.5),   (1, 20.0),   #scale keys
     (0.1, 0.1, 0.1),           #emit box size
     (0, 1.5, 0),                 #emit velocity
     0.23                        #emit dir randomness
    ),
   
   ("new_pistol_smoke_large", psf_billboard_3d|psf_global_emit_dir, "prt_mesh_dust_1",
     1, 20, 0, -0.01, 80.0, 1,  #(was 30. 1.5)   #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 0.3), (1, 0),       #alpha keys
     (0.0, 0.3), (1, 0.3),      #red keys
     (0.0, 0.31),(1, 0.31),       #green keys
     (0.0, 0.4), (1, 0.4),      #blue keys
     (0, 2.5),   (0.3, 10.0),   #scale keys
     (1, 1, 1),           #emit box size
     (0.5, 1.5, 0),                 #emit velocity
     0.1                        #emit dir randomness
    ),