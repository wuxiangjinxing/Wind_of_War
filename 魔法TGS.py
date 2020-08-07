#############################################################
##### troop_ratio_bar (with added bar for channeling stamina)
#############################################################
  ("troop_ratio_bar",prsntf_read_only,0,[
      (ti_on_presentation_load,
       [
        (assign, "$presentation_troop_ratio_bar_active", 1),
        (set_fixed_point_multiplier, 1000),
        



        ### ADDED THIS FOR TGS CHANNELING STAMINA BAR
        (try_begin),
        (troop_slot_eq, "$g_tgs_player_troop", slot_troop_player_knows_channeling, 1),
        

        ### END ADDED THIS FOR TGS CHANNELING STAMINA BAR

        ### ADDED THIS FOR THE CHANNELING CHANGE WEAVE MESHES

            (position_set_x, pos1, 930),
            (position_set_y, pos1, 205),

            (position_set_x, pos2, 1),
            (position_set_y, pos2, 1),
        
            (create_mesh_overlay, "$g_presentation_obj_21", "mesh_weave_air_blast"),
            (overlay_set_position, "$g_presentation_obj_21", pos1),
            (overlay_set_size, "$g_presentation_obj_21", pos2),
        
            (create_mesh_overlay, "$g_presentation_obj_22", "mesh_weave_freeze_blast"),
            (overlay_set_position, "$g_presentation_obj_22", pos1),
            (overlay_set_size, "$g_presentation_obj_22", pos2),
        
            (create_mesh_overlay, "$g_presentation_obj_23", "mesh_weave_heal"),
            (overlay_set_position, "$g_presentation_obj_23", pos1),
            (overlay_set_size, "$g_presentation_obj_23", pos2),
        
            (create_mesh_overlay, "$g_presentation_obj_24", "mesh_weave_fire_ball"),
            (overlay_set_position, "$g_presentation_obj_24", pos1),
            (overlay_set_size, "$g_presentation_obj_24", pos2),
        
            (create_mesh_overlay, "$g_presentation_obj_25", "mesh_weave_unravel"),
            (overlay_set_position, "$g_presentation_obj_25", pos1),
            (overlay_set_size, "$g_presentation_obj_25", pos2),
        
            (create_mesh_overlay, "$g_presentation_obj_26", "mesh_weave_defensive_blast"),
            (overlay_set_position, "$g_presentation_obj_26", pos1),
            (overlay_set_size, "$g_presentation_obj_26", pos2),
        
            (create_mesh_overlay, "$g_presentation_obj_27", "mesh_weave_ranged_earth_blast"),
            (overlay_set_position, "$g_presentation_obj_27", pos1),
            (overlay_set_size, "$g_presentation_obj_27", pos2),
        
            (create_mesh_overlay, "$g_presentation_obj_28", "mesh_weave_bind"),
            (overlay_set_position, "$g_presentation_obj_28", pos1),
            (overlay_set_size, "$g_presentation_obj_28", pos2),
        
            (create_mesh_overlay, "$g_presentation_obj_29", "mesh_weave_chain_lightning"),
            (overlay_set_position, "$g_presentation_obj_29", pos1),
            (overlay_set_size, "$g_presentation_obj_29", pos2),
        
            (create_mesh_overlay, "$g_presentation_obj_30", "mesh_weave_fire_curtain"),
            (overlay_set_position, "$g_presentation_obj_30", pos1),
            (overlay_set_size, "$g_presentation_obj_30", pos2),
        
            (create_mesh_overlay, "$g_presentation_obj_31", "mesh_weave_shield"),
            (overlay_set_position, "$g_presentation_obj_31", pos1),
            (overlay_set_size, "$g_presentation_obj_31", pos2),
        
            (create_mesh_overlay, "$g_presentation_obj_32", "mesh_weave_seeker"),
            (overlay_set_position, "$g_presentation_obj_32", pos1),
            (overlay_set_size, "$g_presentation_obj_32", pos2),
        
            (create_mesh_overlay, "$g_presentation_obj_33", "mesh_weave_compulsion"),
            (overlay_set_position, "$g_presentation_obj_33", pos1),
            (overlay_set_size, "$g_presentation_obj_33", pos2),
        
            (create_mesh_overlay, "$g_presentation_obj_34", "mesh_weave_balefire"),
            (overlay_set_position, "$g_presentation_obj_34", pos1),
            (overlay_set_size, "$g_presentation_obj_34", pos2),

            (position_set_x, pos1, 860),
            (position_set_y, pos1, 205),
        

        
            (create_mesh_overlay, "$g_presentation_obj_39", "mesh_weave_select_all"),
            (overlay_set_position, "$g_presentation_obj_39", pos1),
            (overlay_set_size, "$g_presentation_obj_39", pos2),

        (try_end),        
        ### END ADDED THIS FOR THE CHANNELING CHANGE WEAVE MESHES
        
        (presentation_set_duration, 999999),
       ]),
      (ti_on_presentation_run,
       [
        (store_trigger_param_1, ":cur_time"),
        
        (set_fixed_point_multiplier, 1000),




        ### ADDED THIS FOR TGS CHANNELING STAMINA BAR

        (get_player_agent_no, ":player_agent"),
        (agent_get_wielded_item,":player_item_wielded",":player_agent",0),  # check weapon wielded in right hand
        (try_begin),
        (troop_slot_eq, "$g_tgs_player_troop", slot_troop_player_knows_channeling, 1),
        (this_or_next|agent_has_item_equipped, ":player_agent", "itm_power_player"),
        (eq, ":player_item_wielded","itm_power_player"),        






        ### ADDED THIS FOR THE CHANNELING CHANGE WEAVE MESHES

            (position_set_x, pos1, 800),
            (position_set_y, pos1, 1200),

            (position_set_x, pos2, 1),
            (position_set_y, pos2, 1),

            (try_begin),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_active_weave, AIR_BLAST_WEAVE),
                (overlay_set_size, "$g_presentation_obj_21", pos1),
        
#                (overlay_set_size, "$g_presentation_obj_21", pos2),
                (overlay_set_size, "$g_presentation_obj_22", pos2),
                (overlay_set_size, "$g_presentation_obj_23", pos2),
                (overlay_set_size, "$g_presentation_obj_24", pos2),
                (overlay_set_size, "$g_presentation_obj_25", pos2),
                (overlay_set_size, "$g_presentation_obj_26", pos2),
                (overlay_set_size, "$g_presentation_obj_27", pos2),
                (overlay_set_size, "$g_presentation_obj_28", pos2),
                (overlay_set_size, "$g_presentation_obj_29", pos2),
                (overlay_set_size, "$g_presentation_obj_30", pos2),
                (overlay_set_size, "$g_presentation_obj_31", pos2),
                (overlay_set_size, "$g_presentation_obj_32", pos2),
                (overlay_set_size, "$g_presentation_obj_33", pos2),
                (overlay_set_size, "$g_presentation_obj_34", pos2),
            (else_try),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_active_weave, FREEZE_WEAVE),
                (overlay_set_size, "$g_presentation_obj_22", pos1),
        
                (overlay_set_size, "$g_presentation_obj_21", pos2),
#                (overlay_set_size, "$g_presentation_obj_22", pos2),
                (overlay_set_size, "$g_presentation_obj_23", pos2),
                (overlay_set_size, "$g_presentation_obj_24", pos2),
                (overlay_set_size, "$g_presentation_obj_25", pos2),
                (overlay_set_size, "$g_presentation_obj_26", pos2),
                (overlay_set_size, "$g_presentation_obj_27", pos2),
                (overlay_set_size, "$g_presentation_obj_28", pos2),
                (overlay_set_size, "$g_presentation_obj_29", pos2),
                (overlay_set_size, "$g_presentation_obj_30", pos2),
                (overlay_set_size, "$g_presentation_obj_31", pos2),
                (overlay_set_size, "$g_presentation_obj_32", pos2),
                (overlay_set_size, "$g_presentation_obj_33", pos2),
                (overlay_set_size, "$g_presentation_obj_34", pos2),
            (else_try),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_active_weave, HEAL_WEAVE),
                (overlay_set_size, "$g_presentation_obj_23", pos1),
        
                (overlay_set_size, "$g_presentation_obj_21", pos2),
                (overlay_set_size, "$g_presentation_obj_22", pos2),
#                (overlay_set_size, "$g_presentation_obj_23", pos2),
                (overlay_set_size, "$g_presentation_obj_24", pos2),
                (overlay_set_size, "$g_presentation_obj_25", pos2),
                (overlay_set_size, "$g_presentation_obj_26", pos2),
                (overlay_set_size, "$g_presentation_obj_27", pos2),
                (overlay_set_size, "$g_presentation_obj_28", pos2),
                (overlay_set_size, "$g_presentation_obj_29", pos2),
                (overlay_set_size, "$g_presentation_obj_30", pos2),
                (overlay_set_size, "$g_presentation_obj_31", pos2),
                (overlay_set_size, "$g_presentation_obj_32", pos2),
                (overlay_set_size, "$g_presentation_obj_33", pos2),
                (overlay_set_size, "$g_presentation_obj_34", pos2),
            (else_try),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_active_weave, FIREBALL_WEAVE),
                (overlay_set_size, "$g_presentation_obj_24", pos1),
        
                (overlay_set_size, "$g_presentation_obj_21", pos2),
                (overlay_set_size, "$g_presentation_obj_22", pos2),
                (overlay_set_size, "$g_presentation_obj_23", pos2),
#                (overlay_set_size, "$g_presentation_obj_24", pos2),
                (overlay_set_size, "$g_presentation_obj_25", pos2),
                (overlay_set_size, "$g_presentation_obj_26", pos2),
                (overlay_set_size, "$g_presentation_obj_27", pos2),
                (overlay_set_size, "$g_presentation_obj_28", pos2),
                (overlay_set_size, "$g_presentation_obj_29", pos2),
                (overlay_set_size, "$g_presentation_obj_30", pos2),
                (overlay_set_size, "$g_presentation_obj_31", pos2),
                (overlay_set_size, "$g_presentation_obj_32", pos2),
                (overlay_set_size, "$g_presentation_obj_33", pos2),
                (overlay_set_size, "$g_presentation_obj_34", pos2),
            (else_try),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_active_weave, UNRAVEL_WEAVE),
                (overlay_set_size, "$g_presentation_obj_25", pos1),
        
                (overlay_set_size, "$g_presentation_obj_21", pos2),
                (overlay_set_size, "$g_presentation_obj_22", pos2),
                (overlay_set_size, "$g_presentation_obj_23", pos2),
                (overlay_set_size, "$g_presentation_obj_24", pos2),
#                (overlay_set_size, "$g_presentation_obj_25", pos2),
                (overlay_set_size, "$g_presentation_obj_26", pos2),
                (overlay_set_size, "$g_presentation_obj_27", pos2),
                (overlay_set_size, "$g_presentation_obj_28", pos2),
                (overlay_set_size, "$g_presentation_obj_29", pos2),
                (overlay_set_size, "$g_presentation_obj_30", pos2),
                (overlay_set_size, "$g_presentation_obj_31", pos2),
                (overlay_set_size, "$g_presentation_obj_32", pos2),
                (overlay_set_size, "$g_presentation_obj_33", pos2),
                (overlay_set_size, "$g_presentation_obj_34", pos2),
            (else_try),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_active_weave, DEFENSIVE_BLAST_WEAVE),
                (overlay_set_size, "$g_presentation_obj_26", pos1),
        
                (overlay_set_size, "$g_presentation_obj_21", pos2),
                (overlay_set_size, "$g_presentation_obj_22", pos2),
                (overlay_set_size, "$g_presentation_obj_23", pos2),
                (overlay_set_size, "$g_presentation_obj_24", pos2),
                (overlay_set_size, "$g_presentation_obj_25", pos2),
#                (overlay_set_size, "$g_presentation_obj_26", pos2),
                (overlay_set_size, "$g_presentation_obj_27", pos2),
                (overlay_set_size, "$g_presentation_obj_28", pos2),
                (overlay_set_size, "$g_presentation_obj_29", pos2),
                (overlay_set_size, "$g_presentation_obj_30", pos2),
                (overlay_set_size, "$g_presentation_obj_31", pos2),
                (overlay_set_size, "$g_presentation_obj_32", pos2),
                (overlay_set_size, "$g_presentation_obj_33", pos2),
                (overlay_set_size, "$g_presentation_obj_34", pos2),
            (else_try),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_active_weave, EARTH_BLAST_WEAVE),
                (overlay_set_size, "$g_presentation_obj_27", pos1),
        
                (overlay_set_size, "$g_presentation_obj_21", pos2),
                (overlay_set_size, "$g_presentation_obj_22", pos2),
                (overlay_set_size, "$g_presentation_obj_23", pos2),
                (overlay_set_size, "$g_presentation_obj_24", pos2),
                (overlay_set_size, "$g_presentation_obj_25", pos2),
                (overlay_set_size, "$g_presentation_obj_26", pos2),
#                (overlay_set_size, "$g_presentation_obj_27", pos2),
                (overlay_set_size, "$g_presentation_obj_28", pos2),
                (overlay_set_size, "$g_presentation_obj_29", pos2),
                (overlay_set_size, "$g_presentation_obj_30", pos2),
                (overlay_set_size, "$g_presentation_obj_31", pos2),
                (overlay_set_size, "$g_presentation_obj_32", pos2),
                (overlay_set_size, "$g_presentation_obj_33", pos2),
                (overlay_set_size, "$g_presentation_obj_34", pos2),
            (else_try),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_active_weave, BIND_WEAVE),
                (overlay_set_size, "$g_presentation_obj_28", pos1),
        
                (overlay_set_size, "$g_presentation_obj_21", pos2),
                (overlay_set_size, "$g_presentation_obj_22", pos2),
                (overlay_set_size, "$g_presentation_obj_23", pos2),
                (overlay_set_size, "$g_presentation_obj_24", pos2),
                (overlay_set_size, "$g_presentation_obj_25", pos2),
                (overlay_set_size, "$g_presentation_obj_26", pos2),
                (overlay_set_size, "$g_presentation_obj_27", pos2),
#                (overlay_set_size, "$g_presentation_obj_28", pos2),
                (overlay_set_size, "$g_presentation_obj_29", pos2),
                (overlay_set_size, "$g_presentation_obj_30", pos2),
                (overlay_set_size, "$g_presentation_obj_31", pos2),
                (overlay_set_size, "$g_presentation_obj_32", pos2),
                (overlay_set_size, "$g_presentation_obj_33", pos2),
                (overlay_set_size, "$g_presentation_obj_34", pos2),
            (else_try),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_active_weave, CHAIN_LIGHTNING_WEAVE),
                (overlay_set_size, "$g_presentation_obj_29", pos1),
        
                (overlay_set_size, "$g_presentation_obj_21", pos2),
                (overlay_set_size, "$g_presentation_obj_22", pos2),
                (overlay_set_size, "$g_presentation_obj_23", pos2),
                (overlay_set_size, "$g_presentation_obj_24", pos2),
                (overlay_set_size, "$g_presentation_obj_25", pos2),
                (overlay_set_size, "$g_presentation_obj_26", pos2),
                (overlay_set_size, "$g_presentation_obj_27", pos2),
                (overlay_set_size, "$g_presentation_obj_28", pos2),
#                (overlay_set_size, "$g_presentation_obj_29", pos2),
                (overlay_set_size, "$g_presentation_obj_30", pos2),
                (overlay_set_size, "$g_presentation_obj_31", pos2),
                (overlay_set_size, "$g_presentation_obj_32", pos2),
                (overlay_set_size, "$g_presentation_obj_33", pos2),
                (overlay_set_size, "$g_presentation_obj_34", pos2),
            (else_try),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_active_weave, FIRE_CURTAIN_WEAVE),
                (overlay_set_size, "$g_presentation_obj_30", pos1),
        
                (overlay_set_size, "$g_presentation_obj_21", pos2),
                (overlay_set_size, "$g_presentation_obj_22", pos2),
                (overlay_set_size, "$g_presentation_obj_23", pos2),
                (overlay_set_size, "$g_presentation_obj_24", pos2),
                (overlay_set_size, "$g_presentation_obj_25", pos2),
                (overlay_set_size, "$g_presentation_obj_26", pos2),
                (overlay_set_size, "$g_presentation_obj_27", pos2),
                (overlay_set_size, "$g_presentation_obj_28", pos2),
                (overlay_set_size, "$g_presentation_obj_29", pos2),
#                (overlay_set_size, "$g_presentation_obj_30", pos2),
                (overlay_set_size, "$g_presentation_obj_31", pos2),
                (overlay_set_size, "$g_presentation_obj_32", pos2),
                (overlay_set_size, "$g_presentation_obj_33", pos2),
                (overlay_set_size, "$g_presentation_obj_34", pos2),
            (else_try),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_active_weave, SHIELD_WEAVE),
                (overlay_set_size, "$g_presentation_obj_31", pos1),
        
                (overlay_set_size, "$g_presentation_obj_21", pos2),
                (overlay_set_size, "$g_presentation_obj_22", pos2),
                (overlay_set_size, "$g_presentation_obj_23", pos2),
                (overlay_set_size, "$g_presentation_obj_24", pos2),
                (overlay_set_size, "$g_presentation_obj_25", pos2),
                (overlay_set_size, "$g_presentation_obj_26", pos2),
                (overlay_set_size, "$g_presentation_obj_27", pos2),
                (overlay_set_size, "$g_presentation_obj_28", pos2),
                (overlay_set_size, "$g_presentation_obj_29", pos2),
                (overlay_set_size, "$g_presentation_obj_30", pos2),
#                (overlay_set_size, "$g_presentation_obj_31", pos2),
                (overlay_set_size, "$g_presentation_obj_32", pos2),
                (overlay_set_size, "$g_presentation_obj_33", pos2),
                (overlay_set_size, "$g_presentation_obj_34", pos2),
            (else_try),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_active_weave, SEEKER_WEAVE),
                (overlay_set_size, "$g_presentation_obj_32", pos1),
        
                (overlay_set_size, "$g_presentation_obj_21", pos2),
                (overlay_set_size, "$g_presentation_obj_22", pos2),
                (overlay_set_size, "$g_presentation_obj_23", pos2),
                (overlay_set_size, "$g_presentation_obj_24", pos2),
                (overlay_set_size, "$g_presentation_obj_25", pos2),
                (overlay_set_size, "$g_presentation_obj_26", pos2),
                (overlay_set_size, "$g_presentation_obj_27", pos2),
                (overlay_set_size, "$g_presentation_obj_28", pos2),
                (overlay_set_size, "$g_presentation_obj_29", pos2),
                (overlay_set_size, "$g_presentation_obj_30", pos2),
                (overlay_set_size, "$g_presentation_obj_31", pos2),
#                (overlay_set_size, "$g_presentation_obj_32", pos2),
                (overlay_set_size, "$g_presentation_obj_33", pos2),
                (overlay_set_size, "$g_presentation_obj_34", pos2),
            (else_try),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_active_weave, COMPULSION_WEAVE),
                (overlay_set_size, "$g_presentation_obj_33", pos1),
        
                (overlay_set_size, "$g_presentation_obj_21", pos2),
                (overlay_set_size, "$g_presentation_obj_22", pos2),
                (overlay_set_size, "$g_presentation_obj_23", pos2),
                (overlay_set_size, "$g_presentation_obj_24", pos2),
                (overlay_set_size, "$g_presentation_obj_25", pos2),
                (overlay_set_size, "$g_presentation_obj_26", pos2),
                (overlay_set_size, "$g_presentation_obj_27", pos2),
                (overlay_set_size, "$g_presentation_obj_28", pos2),
                (overlay_set_size, "$g_presentation_obj_29", pos2),
                (overlay_set_size, "$g_presentation_obj_30", pos2),
                (overlay_set_size, "$g_presentation_obj_31", pos2),
                (overlay_set_size, "$g_presentation_obj_32", pos2),
#                (overlay_set_size, "$g_presentation_obj_33", pos2),
                (overlay_set_size, "$g_presentation_obj_34", pos2),
            (else_try),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_active_weave, BALEFIRE_WEAVE),
                (overlay_set_size, "$g_presentation_obj_34", pos1),
        
                (overlay_set_size, "$g_presentation_obj_21", pos2),
                (overlay_set_size, "$g_presentation_obj_22", pos2),
                (overlay_set_size, "$g_presentation_obj_23", pos2),
                (overlay_set_size, "$g_presentation_obj_24", pos2),
                (overlay_set_size, "$g_presentation_obj_25", pos2),
                (overlay_set_size, "$g_presentation_obj_26", pos2),
                (overlay_set_size, "$g_presentation_obj_27", pos2),
                (overlay_set_size, "$g_presentation_obj_28", pos2),
                (overlay_set_size, "$g_presentation_obj_29", pos2),
                (overlay_set_size, "$g_presentation_obj_30", pos2),
                (overlay_set_size, "$g_presentation_obj_31", pos2),
                (overlay_set_size, "$g_presentation_obj_32", pos2),
                (overlay_set_size, "$g_presentation_obj_33", pos2),
#                (overlay_set_size, "$g_presentation_obj_34", pos2),
            (try_end),

        

#            (try_begin),
#            (eq, "$g_weave_toggle_mode", 1),
#                (overlay_set_size, "$g_presentation_obj_35", pos1),
        
#                #(overlay_set_size, "$g_presentation_obj_35", pos2),
#                (overlay_set_size, "$g_presentation_obj_36", pos2),
#                (overlay_set_size, "$g_presentation_obj_37", pos2),
#                (overlay_set_size, "$g_presentation_obj_38", pos2),
#                (overlay_set_size, "$g_presentation_obj_39", pos2),
#            (else_try),
#            (eq, "$g_weave_toggle_mode", 2),
#                (overlay_set_size, "$g_presentation_obj_36", pos1),
        
#                (overlay_set_size, "$g_presentation_obj_35", pos2),
#                #(overlay_set_size, "$g_presentation_obj_36", pos2),
#                (overlay_set_size, "$g_presentation_obj_37", pos2),
#                (overlay_set_size, "$g_presentation_obj_38", pos2),
#                (overlay_set_size, "$g_presentation_obj_39", pos2),
#            (else_try),
#            (eq, "$g_weave_toggle_mode", 3),
#                (overlay_set_size, "$g_presentation_obj_37", pos1),
        
#                (overlay_set_size, "$g_presentation_obj_35", pos2),
#                (overlay_set_size, "$g_presentation_obj_36", pos2),
#                #(overlay_set_size, "$g_presentation_obj_37", pos2),
#                (overlay_set_size, "$g_presentation_obj_38", pos2),
#                (overlay_set_size, "$g_presentation_obj_39", pos2),
#            (else_try),
#            (eq, "$g_weave_toggle_mode", 4),
#                (overlay_set_size, "$g_presentation_obj_38", pos1),
        
#                (overlay_set_size, "$g_presentation_obj_35", pos2),
#                (overlay_set_size, "$g_presentation_obj_36", pos2),
#                (overlay_set_size, "$g_presentation_obj_37", pos2),
#                #(overlay_set_size, "$g_presentation_obj_38", pos2),
#                (overlay_set_size, "$g_presentation_obj_39", pos2),
#            (else_try),
#            (eq, "$g_weave_toggle_mode", 5),
#                (overlay_set_size, "$g_presentation_obj_39", pos1),
        
#                (overlay_set_size, "$g_presentation_obj_35", pos2),
#                (overlay_set_size, "$g_presentation_obj_36", pos2),
#                (overlay_set_size, "$g_presentation_obj_37", pos2),
#                (overlay_set_size, "$g_presentation_obj_38", pos2),
#                #(overlay_set_size, "$g_presentation_obj_39", pos2),
#            (try_end),

            # show the channeling 'wheel' icon when the item is active
            (try_begin),
            (eq, ":player_item_wielded","itm_power_player"),
                (overlay_set_size, "$g_presentation_obj_39", pos1),
            (else_try),
                (overlay_set_size, "$g_presentation_obj_39", pos2),
            (try_end),

        (try_end),


        ### END ADDED THIS FOR THE CHANNELING CHANGE WEAVE MESHES
        
        
        (try_begin),
        (eq, "$presentation_troop_ratio_bar_active", 1),
        (gt, ":cur_time", 200),
        (game_key_clicked, gk_view_orders),
            (assign, "$presentation_troop_ratio_bar_active", 0),
            (presentation_set_duration, 0),
            (start_presentation, "prsnt_battle"),
        (else_try),
        (eq, "$presentation_troop_ratio_bar_active", 1),
        (key_is_down, "$key_weave_toggle"),
        (troop_slot_eq, "$g_tgs_player_troop", slot_troop_player_knows_channeling, 1),
            (assign, "$presentation_troop_ratio_bar_active", 0),
            (presentation_set_duration, 0),
            (start_presentation, "prsnt_battle_time_weave_selection"),
        (try_end),
       ]),
       
     ]),
#############################################################
##### troop_ratio_bar (with added bar for channeling stamina)
#############################################################


#############################################################
##### troop_ratio_bar (with added bar for channeling stamina)
#############################################################
  ("battle_time_weave_selection",prsntf_manual_end_only,0,[
      (ti_on_presentation_load,
       [
        (assign, "$g_run_battle_time_weave_selection", 1),
        (set_fixed_point_multiplier, 1000),





        ### ADDED THIS FOR THE CHANNELING CHANGE WEAVE MESHES

        (position_set_x, pos1, 930),
        (position_set_y, pos1, 205),

        (position_set_x, pos2, 1),
        (position_set_y, pos2, 1),
        
        (create_mesh_overlay, "$g_presentation_obj_21", "mesh_weave_air_blast"),
        (overlay_set_position, "$g_presentation_obj_21", pos1),
        (overlay_set_size, "$g_presentation_obj_21", pos2),
        
        (create_mesh_overlay, "$g_presentation_obj_22", "mesh_weave_freeze_blast"),
        (overlay_set_position, "$g_presentation_obj_22", pos1),
        (overlay_set_size, "$g_presentation_obj_22", pos2),
        
        (create_mesh_overlay, "$g_presentation_obj_23", "mesh_weave_heal"),
        (overlay_set_position, "$g_presentation_obj_23", pos1),
        (overlay_set_size, "$g_presentation_obj_23", pos2),
        
        (create_mesh_overlay, "$g_presentation_obj_24", "mesh_weave_fire_ball"),
        (overlay_set_position, "$g_presentation_obj_24", pos1),
        (overlay_set_size, "$g_presentation_obj_24", pos2),
        
        (create_mesh_overlay, "$g_presentation_obj_25", "mesh_weave_unravel"),
        (overlay_set_position, "$g_presentation_obj_25", pos1),
        (overlay_set_size, "$g_presentation_obj_25", pos2),
        
        (create_mesh_overlay, "$g_presentation_obj_26", "mesh_weave_defensive_blast"),
        (overlay_set_position, "$g_presentation_obj_26", pos1),
        (overlay_set_size, "$g_presentation_obj_26", pos2),
        
        (create_mesh_overlay, "$g_presentation_obj_27", "mesh_weave_ranged_earth_blast"),
        (overlay_set_position, "$g_presentation_obj_27", pos1),
        (overlay_set_size, "$g_presentation_obj_27", pos2),
        
        (create_mesh_overlay, "$g_presentation_obj_28", "mesh_weave_bind"),
        (overlay_set_position, "$g_presentation_obj_28", pos1),
        (overlay_set_size, "$g_presentation_obj_28", pos2),
        
        (create_mesh_overlay, "$g_presentation_obj_29", "mesh_weave_chain_lightning"),
        (overlay_set_position, "$g_presentation_obj_29", pos1),
        (overlay_set_size, "$g_presentation_obj_29", pos2),
        
        (create_mesh_overlay, "$g_presentation_obj_30", "mesh_weave_fire_curtain"),
        (overlay_set_position, "$g_presentation_obj_30", pos1),
        (overlay_set_size, "$g_presentation_obj_30", pos2),
        
        (create_mesh_overlay, "$g_presentation_obj_31", "mesh_weave_shield"),
        (overlay_set_position, "$g_presentation_obj_31", pos1),
        (overlay_set_size, "$g_presentation_obj_31", pos2),
        
        (create_mesh_overlay, "$g_presentation_obj_32", "mesh_weave_seeker"),
        (overlay_set_position, "$g_presentation_obj_32", pos1),
        (overlay_set_size, "$g_presentation_obj_32", pos2),
        
        (create_mesh_overlay, "$g_presentation_obj_33", "mesh_weave_compulsion"),
        (overlay_set_position, "$g_presentation_obj_33", pos1),
        (overlay_set_size, "$g_presentation_obj_33", pos2),
        
        (create_mesh_overlay, "$g_presentation_obj_34", "mesh_weave_balefire"),
        (overlay_set_position, "$g_presentation_obj_34", pos1),
        (overlay_set_size, "$g_presentation_obj_34", pos2),

        (position_set_x, pos1, 860),
        (position_set_y, pos1, 205),
        
#        (create_mesh_overlay, "$g_presentation_obj_35", "mesh_weave_select_non_ranged"),
#        (overlay_set_position, "$g_presentation_obj_35", pos1),
#        (overlay_set_size, "$g_presentation_obj_35", pos2),
        
#        (create_mesh_overlay, "$g_presentation_obj_36", "mesh_weave_select_ranged"),
#        (overlay_set_position, "$g_presentation_obj_36", pos1),
#        (overlay_set_size, "$g_presentation_obj_36", pos2),
        
#        (create_mesh_overlay, "$g_presentation_obj_37", "mesh_weave_select_support"),
#        (overlay_set_position, "$g_presentation_obj_37", pos1),
#        (overlay_set_size, "$g_presentation_obj_37", pos2),
        
#        (create_mesh_overlay, "$g_presentation_obj_38", "mesh_weave_select_advanced"),
#        (overlay_set_position, "$g_presentation_obj_38", pos1),
#        (overlay_set_size, "$g_presentation_obj_38", pos2),
        
        (create_mesh_overlay, "$g_presentation_obj_39", "mesh_weave_select_all"),
        (overlay_set_position, "$g_presentation_obj_39", pos1),
        (overlay_set_size, "$g_presentation_obj_39", pos2),
        
        ### END ADDED THIS FOR THE CHANNELING CHANGE WEAVE MESHES

        ### ADDED FOR BATTLE-TIME WEAVE SELECTION

		#Little Pos Helper by Kuba begin
		#(create_text_overlay, "$g_little_pos_helper", "@00,00"),
		#(overlay_set_color, "$g_little_pos_helper", 0xFFFFFFFF),
		#(position_set_x, pos1, 10),
		#(position_set_y, pos1, 650),
		#(overlay_set_position, "$g_little_pos_helper", pos1),
		#Little Pos Helper by Kuba end


        (position_set_x, pos2, 1),
        (position_set_y, pos2, 1),

        (position_set_x, pos1, 350),
        (position_set_y, pos1, 400),        

        (create_mesh_overlay, "$g_presentation_obj_41", "mesh_weave_air_blast"),
        (overlay_set_position, "$g_presentation_obj_41", pos1),
        (overlay_set_size, "$g_presentation_obj_41", pos2),

        (position_set_x, pos1, 390),
        (position_set_y, pos1, 400),               
        
        (create_mesh_overlay, "$g_presentation_obj_42", "mesh_weave_freeze_blast"),
        (overlay_set_position, "$g_presentation_obj_42", pos1),
        (overlay_set_size, "$g_presentation_obj_42", pos2),

        (position_set_x, pos1, 430),
        (position_set_y, pos1, 400),               
        
        (create_mesh_overlay, "$g_presentation_obj_43", "mesh_weave_heal"),
        (overlay_set_position, "$g_presentation_obj_43", pos1),
        (overlay_set_size, "$g_presentation_obj_43", pos2),

        (position_set_x, pos1, 470),
        (position_set_y, pos1, 400),               
        
        (create_mesh_overlay, "$g_presentation_obj_44", "mesh_weave_fire_ball"),
        (overlay_set_position, "$g_presentation_obj_44", pos1),
        (overlay_set_size, "$g_presentation_obj_44", pos2),

        (position_set_x, pos1, 510),
        (position_set_y, pos1, 400),               
        
        (create_mesh_overlay, "$g_presentation_obj_45", "mesh_weave_unravel"),
        (overlay_set_position, "$g_presentation_obj_45", pos1),
        (overlay_set_size, "$g_presentation_obj_45", pos2),

        (position_set_x, pos1, 550),
        (position_set_y, pos1, 400),          
        
        (create_mesh_overlay, "$g_presentation_obj_46", "mesh_weave_defensive_blast"),
        (overlay_set_position, "$g_presentation_obj_46", pos1),
        (overlay_set_size, "$g_presentation_obj_46", pos2),

        (position_set_x, pos1, 590),
        (position_set_y, pos1, 400),          
        
        (create_mesh_overlay, "$g_presentation_obj_47", "mesh_weave_ranged_earth_blast"),
        (overlay_set_position, "$g_presentation_obj_47", pos1),
        (overlay_set_size, "$g_presentation_obj_47", pos2),

        (position_set_x, pos1, 350),
        (position_set_y, pos1, 350),          
        
        (create_mesh_overlay, "$g_presentation_obj_48", "mesh_weave_bind"),
        (overlay_set_position, "$g_presentation_obj_48", pos1),
        (overlay_set_size, "$g_presentation_obj_48", pos2),

        (position_set_x, pos1, 390),
        (position_set_y, pos1, 350),          
        
        (create_mesh_overlay, "$g_presentation_obj_49", "mesh_weave_chain_lightning"),
        (overlay_set_position, "$g_presentation_obj_49", pos1),
        (overlay_set_size, "$g_presentation_obj_49", pos2),

        (position_set_x, pos1, 430),
        (position_set_y, pos1, 350),         
        
        (create_mesh_overlay, "$g_presentation_obj_50", "mesh_weave_fire_curtain"),
        (overlay_set_position, "$g_presentation_obj_50", pos1),
        (overlay_set_size, "$g_presentation_obj_50", pos2),

        (position_set_x, pos1, 470),
        (position_set_y, pos1, 350),         
        
        (create_mesh_overlay, "$g_presentation_obj_51", "mesh_weave_shield"),
        (overlay_set_position, "$g_presentation_obj_51", pos1),
        (overlay_set_size, "$g_presentation_obj_51", pos2),

        (position_set_x, pos1, 510),
        (position_set_y, pos1, 350),         
        
        (create_mesh_overlay, "$g_presentation_obj_52", "mesh_weave_seeker"),
        (overlay_set_position, "$g_presentation_obj_52", pos1),
        (overlay_set_size, "$g_presentation_obj_52", pos2),

        (position_set_x, pos1, 550),
        (position_set_y, pos1, 350),         
        
        (create_mesh_overlay, "$g_presentation_obj_53", "mesh_weave_compulsion"),
        (overlay_set_position, "$g_presentation_obj_53", pos1),
        (overlay_set_size, "$g_presentation_obj_53", pos2),

        (position_set_x, pos1, 590),
        (position_set_y, pos1, 350),         
        
        (create_mesh_overlay, "$g_presentation_obj_54", "mesh_weave_balefire"),
        (overlay_set_position, "$g_presentation_obj_54", pos1),
        (overlay_set_size, "$g_presentation_obj_54", pos2),        



        
        ### END ADDED FOR BATTLE-TIME WEAVE SELECTION
        
        (presentation_set_duration, 999999),
       ]),
      (ti_on_presentation_run,
       [
        (store_trigger_param_1, ":cur_time"),
        
        (set_fixed_point_multiplier, 1000),




        ### ADDED THIS FOR TGS CHANNELING STAMINA BAR

        (get_player_agent_no, ":player_agent"),
        (agent_get_wielded_item,":player_item_wielded",":player_agent",0),  # check weapon wielded in right hand
        (try_begin),
        (this_or_next|agent_has_item_equipped, ":player_agent", "itm_power_player"),
        (eq, ":player_item_wielded","itm_power_player"),        




        ### ADDED THIS FOR THE CHANNELING CHANGE WEAVE MESHES

            (position_set_x, pos1, 800),
            (position_set_y, pos1, 1200),

            (position_set_x, pos2, 1),
            (position_set_y, pos2, 1),

            (try_begin),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_active_weave, AIR_BLAST_WEAVE),
                (overlay_set_size, "$g_presentation_obj_21", pos1),
        
#                (overlay_set_size, "$g_presentation_obj_21", pos2),
                (overlay_set_size, "$g_presentation_obj_22", pos2),
                (overlay_set_size, "$g_presentation_obj_23", pos2),
                (overlay_set_size, "$g_presentation_obj_24", pos2),
                (overlay_set_size, "$g_presentation_obj_25", pos2),
                (overlay_set_size, "$g_presentation_obj_26", pos2),
                (overlay_set_size, "$g_presentation_obj_27", pos2),
                (overlay_set_size, "$g_presentation_obj_28", pos2),
                (overlay_set_size, "$g_presentation_obj_29", pos2),
                (overlay_set_size, "$g_presentation_obj_30", pos2),
                (overlay_set_size, "$g_presentation_obj_31", pos2),
                (overlay_set_size, "$g_presentation_obj_32", pos2),
                (overlay_set_size, "$g_presentation_obj_33", pos2),
                (overlay_set_size, "$g_presentation_obj_34", pos2),
            (else_try),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_active_weave, FREEZE_WEAVE),
                (overlay_set_size, "$g_presentation_obj_22", pos1),
        
                (overlay_set_size, "$g_presentation_obj_21", pos2),
#                (overlay_set_size, "$g_presentation_obj_22", pos2),
                (overlay_set_size, "$g_presentation_obj_23", pos2),
                (overlay_set_size, "$g_presentation_obj_24", pos2),
                (overlay_set_size, "$g_presentation_obj_25", pos2),
                (overlay_set_size, "$g_presentation_obj_26", pos2),
                (overlay_set_size, "$g_presentation_obj_27", pos2),
                (overlay_set_size, "$g_presentation_obj_28", pos2),
                (overlay_set_size, "$g_presentation_obj_29", pos2),
                (overlay_set_size, "$g_presentation_obj_30", pos2),
                (overlay_set_size, "$g_presentation_obj_31", pos2),
                (overlay_set_size, "$g_presentation_obj_32", pos2),
                (overlay_set_size, "$g_presentation_obj_33", pos2),
                (overlay_set_size, "$g_presentation_obj_34", pos2),
            (else_try),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_active_weave, HEAL_WEAVE),
                (overlay_set_size, "$g_presentation_obj_23", pos1),
        
                (overlay_set_size, "$g_presentation_obj_21", pos2),
                (overlay_set_size, "$g_presentation_obj_22", pos2),
#                (overlay_set_size, "$g_presentation_obj_23", pos2),
                (overlay_set_size, "$g_presentation_obj_24", pos2),
                (overlay_set_size, "$g_presentation_obj_25", pos2),
                (overlay_set_size, "$g_presentation_obj_26", pos2),
                (overlay_set_size, "$g_presentation_obj_27", pos2),
                (overlay_set_size, "$g_presentation_obj_28", pos2),
                (overlay_set_size, "$g_presentation_obj_29", pos2),
                (overlay_set_size, "$g_presentation_obj_30", pos2),
                (overlay_set_size, "$g_presentation_obj_31", pos2),
                (overlay_set_size, "$g_presentation_obj_32", pos2),
                (overlay_set_size, "$g_presentation_obj_33", pos2),
                (overlay_set_size, "$g_presentation_obj_34", pos2),
            (else_try),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_active_weave, FIREBALL_WEAVE),
                (overlay_set_size, "$g_presentation_obj_24", pos1),
        
                (overlay_set_size, "$g_presentation_obj_21", pos2),
                (overlay_set_size, "$g_presentation_obj_22", pos2),
                (overlay_set_size, "$g_presentation_obj_23", pos2),
#                (overlay_set_size, "$g_presentation_obj_24", pos2),
                (overlay_set_size, "$g_presentation_obj_25", pos2),
                (overlay_set_size, "$g_presentation_obj_26", pos2),
                (overlay_set_size, "$g_presentation_obj_27", pos2),
                (overlay_set_size, "$g_presentation_obj_28", pos2),
                (overlay_set_size, "$g_presentation_obj_29", pos2),
                (overlay_set_size, "$g_presentation_obj_30", pos2),
                (overlay_set_size, "$g_presentation_obj_31", pos2),
                (overlay_set_size, "$g_presentation_obj_32", pos2),
                (overlay_set_size, "$g_presentation_obj_33", pos2),
                (overlay_set_size, "$g_presentation_obj_34", pos2),
            (else_try),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_active_weave, UNRAVEL_WEAVE),
                (overlay_set_size, "$g_presentation_obj_25", pos1),
        
                (overlay_set_size, "$g_presentation_obj_21", pos2),
                (overlay_set_size, "$g_presentation_obj_22", pos2),
                (overlay_set_size, "$g_presentation_obj_23", pos2),
                (overlay_set_size, "$g_presentation_obj_24", pos2),
#                (overlay_set_size, "$g_presentation_obj_25", pos2),
                (overlay_set_size, "$g_presentation_obj_26", pos2),
                (overlay_set_size, "$g_presentation_obj_27", pos2),
                (overlay_set_size, "$g_presentation_obj_28", pos2),
                (overlay_set_size, "$g_presentation_obj_29", pos2),
                (overlay_set_size, "$g_presentation_obj_30", pos2),
                (overlay_set_size, "$g_presentation_obj_31", pos2),
                (overlay_set_size, "$g_presentation_obj_32", pos2),
                (overlay_set_size, "$g_presentation_obj_33", pos2),
                (overlay_set_size, "$g_presentation_obj_34", pos2),
            (else_try),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_active_weave, DEFENSIVE_BLAST_WEAVE),
                (overlay_set_size, "$g_presentation_obj_26", pos1),
        
                (overlay_set_size, "$g_presentation_obj_21", pos2),
                (overlay_set_size, "$g_presentation_obj_22", pos2),
                (overlay_set_size, "$g_presentation_obj_23", pos2),
                (overlay_set_size, "$g_presentation_obj_24", pos2),
                (overlay_set_size, "$g_presentation_obj_25", pos2),
#                (overlay_set_size, "$g_presentation_obj_26", pos2),
                (overlay_set_size, "$g_presentation_obj_27", pos2),
                (overlay_set_size, "$g_presentation_obj_28", pos2),
                (overlay_set_size, "$g_presentation_obj_29", pos2),
                (overlay_set_size, "$g_presentation_obj_30", pos2),
                (overlay_set_size, "$g_presentation_obj_31", pos2),
                (overlay_set_size, "$g_presentation_obj_32", pos2),
                (overlay_set_size, "$g_presentation_obj_33", pos2),
                (overlay_set_size, "$g_presentation_obj_34", pos2),
            (else_try),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_active_weave, EARTH_BLAST_WEAVE),
                (overlay_set_size, "$g_presentation_obj_27", pos1),
        
                (overlay_set_size, "$g_presentation_obj_21", pos2),
                (overlay_set_size, "$g_presentation_obj_22", pos2),
                (overlay_set_size, "$g_presentation_obj_23", pos2),
                (overlay_set_size, "$g_presentation_obj_24", pos2),
                (overlay_set_size, "$g_presentation_obj_25", pos2),
                (overlay_set_size, "$g_presentation_obj_26", pos2),
#                (overlay_set_size, "$g_presentation_obj_27", pos2),
                (overlay_set_size, "$g_presentation_obj_28", pos2),
                (overlay_set_size, "$g_presentation_obj_29", pos2),
                (overlay_set_size, "$g_presentation_obj_30", pos2),
                (overlay_set_size, "$g_presentation_obj_31", pos2),
                (overlay_set_size, "$g_presentation_obj_32", pos2),
                (overlay_set_size, "$g_presentation_obj_33", pos2),
                (overlay_set_size, "$g_presentation_obj_34", pos2),
            (else_try),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_active_weave, BIND_WEAVE),
                (overlay_set_size, "$g_presentation_obj_28", pos1),
        
                (overlay_set_size, "$g_presentation_obj_21", pos2),
                (overlay_set_size, "$g_presentation_obj_22", pos2),
                (overlay_set_size, "$g_presentation_obj_23", pos2),
                (overlay_set_size, "$g_presentation_obj_24", pos2),
                (overlay_set_size, "$g_presentation_obj_25", pos2),
                (overlay_set_size, "$g_presentation_obj_26", pos2),
                (overlay_set_size, "$g_presentation_obj_27", pos2),
#                (overlay_set_size, "$g_presentation_obj_28", pos2),
                (overlay_set_size, "$g_presentation_obj_29", pos2),
                (overlay_set_size, "$g_presentation_obj_30", pos2),
                (overlay_set_size, "$g_presentation_obj_31", pos2),
                (overlay_set_size, "$g_presentation_obj_32", pos2),
                (overlay_set_size, "$g_presentation_obj_33", pos2),
                (overlay_set_size, "$g_presentation_obj_34", pos2),
            (else_try),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_active_weave, CHAIN_LIGHTNING_WEAVE),
                (overlay_set_size, "$g_presentation_obj_29", pos1),
        
                (overlay_set_size, "$g_presentation_obj_21", pos2),
                (overlay_set_size, "$g_presentation_obj_22", pos2),
                (overlay_set_size, "$g_presentation_obj_23", pos2),
                (overlay_set_size, "$g_presentation_obj_24", pos2),
                (overlay_set_size, "$g_presentation_obj_25", pos2),
                (overlay_set_size, "$g_presentation_obj_26", pos2),
                (overlay_set_size, "$g_presentation_obj_27", pos2),
                (overlay_set_size, "$g_presentation_obj_28", pos2),
#                (overlay_set_size, "$g_presentation_obj_29", pos2),
                (overlay_set_size, "$g_presentation_obj_30", pos2),
                (overlay_set_size, "$g_presentation_obj_31", pos2),
                (overlay_set_size, "$g_presentation_obj_32", pos2),
                (overlay_set_size, "$g_presentation_obj_33", pos2),
                (overlay_set_size, "$g_presentation_obj_34", pos2),
            (else_try),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_active_weave, FIRE_CURTAIN_WEAVE),
                (overlay_set_size, "$g_presentation_obj_30", pos1),
        
                (overlay_set_size, "$g_presentation_obj_21", pos2),
                (overlay_set_size, "$g_presentation_obj_22", pos2),
                (overlay_set_size, "$g_presentation_obj_23", pos2),
                (overlay_set_size, "$g_presentation_obj_24", pos2),
                (overlay_set_size, "$g_presentation_obj_25", pos2),
                (overlay_set_size, "$g_presentation_obj_26", pos2),
                (overlay_set_size, "$g_presentation_obj_27", pos2),
                (overlay_set_size, "$g_presentation_obj_28", pos2),
                (overlay_set_size, "$g_presentation_obj_29", pos2),
#                (overlay_set_size, "$g_presentation_obj_30", pos2),
                (overlay_set_size, "$g_presentation_obj_31", pos2),
                (overlay_set_size, "$g_presentation_obj_32", pos2),
                (overlay_set_size, "$g_presentation_obj_33", pos2),
                (overlay_set_size, "$g_presentation_obj_34", pos2),
            (else_try),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_active_weave, SHIELD_WEAVE),
                (overlay_set_size, "$g_presentation_obj_31", pos1),
        
                (overlay_set_size, "$g_presentation_obj_21", pos2),
                (overlay_set_size, "$g_presentation_obj_22", pos2),
                (overlay_set_size, "$g_presentation_obj_23", pos2),
                (overlay_set_size, "$g_presentation_obj_24", pos2),
                (overlay_set_size, "$g_presentation_obj_25", pos2),
                (overlay_set_size, "$g_presentation_obj_26", pos2),
                (overlay_set_size, "$g_presentation_obj_27", pos2),
                (overlay_set_size, "$g_presentation_obj_28", pos2),
                (overlay_set_size, "$g_presentation_obj_29", pos2),
                (overlay_set_size, "$g_presentation_obj_30", pos2),
#                (overlay_set_size, "$g_presentation_obj_31", pos2),
                (overlay_set_size, "$g_presentation_obj_32", pos2),
                (overlay_set_size, "$g_presentation_obj_33", pos2),
                (overlay_set_size, "$g_presentation_obj_34", pos2),
            (else_try),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_active_weave, SEEKER_WEAVE),
                (overlay_set_size, "$g_presentation_obj_32", pos1),
        
                (overlay_set_size, "$g_presentation_obj_21", pos2),
                (overlay_set_size, "$g_presentation_obj_22", pos2),
                (overlay_set_size, "$g_presentation_obj_23", pos2),
                (overlay_set_size, "$g_presentation_obj_24", pos2),
                (overlay_set_size, "$g_presentation_obj_25", pos2),
                (overlay_set_size, "$g_presentation_obj_26", pos2),
                (overlay_set_size, "$g_presentation_obj_27", pos2),
                (overlay_set_size, "$g_presentation_obj_28", pos2),
                (overlay_set_size, "$g_presentation_obj_29", pos2),
                (overlay_set_size, "$g_presentation_obj_30", pos2),
                (overlay_set_size, "$g_presentation_obj_31", pos2),
#                (overlay_set_size, "$g_presentation_obj_32", pos2),
                (overlay_set_size, "$g_presentation_obj_33", pos2),
                (overlay_set_size, "$g_presentation_obj_34", pos2),
            (else_try),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_active_weave, COMPULSION_WEAVE),
                (overlay_set_size, "$g_presentation_obj_33", pos1),
        
                (overlay_set_size, "$g_presentation_obj_21", pos2),
                (overlay_set_size, "$g_presentation_obj_22", pos2),
                (overlay_set_size, "$g_presentation_obj_23", pos2),
                (overlay_set_size, "$g_presentation_obj_24", pos2),
                (overlay_set_size, "$g_presentation_obj_25", pos2),
                (overlay_set_size, "$g_presentation_obj_26", pos2),
                (overlay_set_size, "$g_presentation_obj_27", pos2),
                (overlay_set_size, "$g_presentation_obj_28", pos2),
                (overlay_set_size, "$g_presentation_obj_29", pos2),
                (overlay_set_size, "$g_presentation_obj_30", pos2),
                (overlay_set_size, "$g_presentation_obj_31", pos2),
                (overlay_set_size, "$g_presentation_obj_32", pos2),
#                (overlay_set_size, "$g_presentation_obj_33", pos2),
                (overlay_set_size, "$g_presentation_obj_34", pos2),
            (else_try),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_active_weave, BALEFIRE_WEAVE),
                (overlay_set_size, "$g_presentation_obj_34", pos1),
        
                (overlay_set_size, "$g_presentation_obj_21", pos2),
                (overlay_set_size, "$g_presentation_obj_22", pos2),
                (overlay_set_size, "$g_presentation_obj_23", pos2),
                (overlay_set_size, "$g_presentation_obj_24", pos2),
                (overlay_set_size, "$g_presentation_obj_25", pos2),
                (overlay_set_size, "$g_presentation_obj_26", pos2),
                (overlay_set_size, "$g_presentation_obj_27", pos2),
                (overlay_set_size, "$g_presentation_obj_28", pos2),
                (overlay_set_size, "$g_presentation_obj_29", pos2),
                (overlay_set_size, "$g_presentation_obj_30", pos2),
                (overlay_set_size, "$g_presentation_obj_31", pos2),
                (overlay_set_size, "$g_presentation_obj_32", pos2),
                (overlay_set_size, "$g_presentation_obj_33", pos2),
#                (overlay_set_size, "$g_presentation_obj_34", pos2),
            (try_end),

        
            # show the channeling 'wheel' icon when the item is active
            (try_begin),
            (eq, ":player_item_wielded","itm_power_player"),
                (overlay_set_size, "$g_presentation_obj_39", pos1),
            (else_try),
                (overlay_set_size, "$g_presentation_obj_39", pos2),
            (try_end),        

        ### END ADDED THIS FOR THE CHANNELING CHANGE WEAVE MESHES


        ### ADDED FOR BATTLE-TIME WEAVE SELECTION
        

        #Little Pos Helper by Kuba begin
        #(mouse_get_position, pos1),
        #(position_get_x, reg1, pos1),
        #(position_get_y, reg2, pos1),
        #(overlay_set_text, "$g_little_pos_helper", "@{reg1},{reg2}"),
        #Little Pos Helper by Kuba end


            (position_set_x, pos1, 800),
            (position_set_y, pos1, 1200),

            (position_set_x, pos2, 1),
            (position_set_y, pos2, 1),
        
            (try_begin),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_air_blast_known, 1),
                (overlay_set_size, "$g_presentation_obj_41", pos1),
            (else_try),
                (overlay_set_size, "$g_presentation_obj_41", pos2),
            (try_end),
        
            (try_begin),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_freeze_known, 1),
                (overlay_set_size, "$g_presentation_obj_42", pos1),
            (else_try),
                (overlay_set_size, "$g_presentation_obj_42", pos2),
            (try_end),
        
            (try_begin),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_heal_known, 1),
                (overlay_set_size, "$g_presentation_obj_43", pos1),
            (else_try),
                (overlay_set_size, "$g_presentation_obj_43", pos2),
            (try_end),

            (try_begin),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_fireball_known, 1),
                (overlay_set_size, "$g_presentation_obj_44", pos1),
            (else_try),
                (overlay_set_size, "$g_presentation_obj_44", pos2),
            (try_end),

            (try_begin),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_unravel_known, 1),
                (overlay_set_size, "$g_presentation_obj_45", pos1),
            (else_try),
                (overlay_set_size, "$g_presentation_obj_45", pos2),
            (try_end),

            (try_begin),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_defensive_blast_known, 1),
                (overlay_set_size, "$g_presentation_obj_46", pos1),
            (else_try),
                (overlay_set_size, "$g_presentation_obj_46", pos2),
            (try_end),

            (try_begin),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_earth_blast_known, 1),
                (overlay_set_size, "$g_presentation_obj_47", pos1),
            (else_try),
                (overlay_set_size, "$g_presentation_obj_47", pos2),
            (try_end),

            (try_begin),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_bind_known, 1),
                (overlay_set_size, "$g_presentation_obj_48", pos1),
            (else_try),
                (overlay_set_size, "$g_presentation_obj_48", pos2),
            (try_end),

            (try_begin),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_chain_lightning_known, 1),
                (overlay_set_size, "$g_presentation_obj_49", pos1),
            (else_try),
                (overlay_set_size, "$g_presentation_obj_49", pos2),
            (try_end),

            (try_begin),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_fire_curtain_known, 1),
                (overlay_set_size, "$g_presentation_obj_50", pos1),
            (else_try),
                (overlay_set_size, "$g_presentation_obj_50", pos2),
            (try_end),

            (try_begin),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_shield_known, 1),
                (overlay_set_size, "$g_presentation_obj_51", pos1),
            (else_try),
                (overlay_set_size, "$g_presentation_obj_51", pos2),
            (try_end),

            (try_begin),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_seeker_known, 1),
                (overlay_set_size, "$g_presentation_obj_52", pos1),
            (else_try),
                (overlay_set_size, "$g_presentation_obj_52", pos2),
            (try_end),

            (try_begin),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_compulsion_known, 1),
                (overlay_set_size, "$g_presentation_obj_53", pos1),
            (else_try),
                (overlay_set_size, "$g_presentation_obj_53", pos2),
            (try_end),

            (try_begin),
            (troop_slot_eq, "$g_tgs_player_troop", slot_troop_balefire_known, 1),
                (overlay_set_size, "$g_presentation_obj_54", pos1),
            (else_try),
                (overlay_set_size, "$g_presentation_obj_54", pos2),
            (try_end),       
        
            (mouse_get_position, pos1),
            (position_get_x, "$g_weave_select_x", pos1),
            (position_get_y, "$g_weave_select_y", pos1),
        
        
        ### END ADDED FOR BATTLE-TIME WEAVE SELECTION
        
        (try_end),        

        
        (try_begin),
        (eq, "$g_run_battle_time_weave_selection", 1),
        (gt, ":cur_time", 200),
        (neg|key_is_down, "$key_weave_toggle"),
          (assign, "$g_run_battle_time_weave_selection", 0),
          (presentation_set_duration, 0),
          (start_presentation, "prsnt_troop_ratio_bar"),
        (try_end),
       ]),
       
     ]),
#############################################################
##### troop_ratio_bar (with added bar for channeling stamina)
############################################################# 
