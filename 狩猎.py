  # RAMARAUNT SCRIPT HUNTING OSP
  # script_initialize_hunting_time
  # Input: hunting_party_leader
  # Output: reg0 (hour to stop hunting)
  ("initialize_hunting_time",
    [
    (store_script_param_1,":hunting_party_leader"),
    (store_script_param_2,":party"),
    (assign, ":hours", 0),
    (assign, ":tracking_skill", 0),
    (assign, ":differentiation", 0),
    (assign, ":lowerorhighertest", 0),
    (assign, reg0, 0),
    (store_skill_level, ":tracking_skill", "skl_tracking", ":hunting_party_leader"),
    (try_begin),
      (lt, ":tracking_skill",11),
      (store_sub, ":hours" ,11 , ":tracking_skill"),
      (store_mul, ":hours" ,6 , ":hours"),
      (try_begin),
         (le, ":tracking_skill", 7),
         (store_random_in_range, ":differentiation", 0, 18),#Great differentiation for levels 7 and lower.
         (store_random_in_range, ":lowerorhighertest", 0, 1),
         (try_begin),
            (eq, ":lowerorhighertest",0), #MEANS GO DOWN
            (store_sub, ":hours", ":hours", ":differentiation"),
          (else_try),
              (eq, ":lowerorhighertest",1),#MEANS GO UP
              (store_add, ":hours", ":hours", ":differentiation"),
          (try_end),
          (else_try),
             (ge, ":tracking_skill", 8),
             (store_random_in_range, ":differentiation",0, 6), #Smaller differentiation for levels 8 through 10
             (store_random_in_range, ":lowerorhighertest", 0, 1),
          (try_begin),
            (eq, ":lowerorhighertest",0), #MEANS GO DOWN
            (store_sub, ":hours", ":hours", ":differentiation"),
          (else_try),
              (eq, ":lowerorhighertest",1),#MEANS GO UP
              (store_add, ":hours", ":hours", ":differentiation"),
          (try_end),
     (try_end),
  (try_end),
  (store_current_hours, ":cur_hours"),   
  (store_add, ":new_hours", ":cur_hours", ":hours"),
 #slots
 (party_set_slot, ":party", slot_party_hunting_time, ":new_hours"),
     ] 
  ),  
  
    # RAMARAUNT SCRIPT HUNTING OSP
  # script_set_hunting_found
  # Input: hunting_party
  # Output: reg0 (id of found troop)
  ("set_hunting_found",
    [
        (store_script_param_1, ":party"),
        
            #now pick deers or boars (or unicorns)
            (store_random_in_range, ":choice", 1, 101),
            
            (try_begin),
                (gt, ":choice", 70),#boar
                (party_set_slot, ":party", slot_party_hunting_found, 2),
                (store_random_in_range, ":amount", 2, 6),
                (party_set_slot, ":party", slot_party_hunting_amount, ":amount"),
            (else_try),
                (eq, ":choice", 50), #unicorns
                (party_set_slot, ":party", slot_party_hunting_found, 3),
                (party_set_slot, ":party", slot_party_hunting_amount, 1),
            (else_try), #deers
                (party_set_slot, ":party", slot_party_hunting_found, 1),
                (store_random_in_range, ":amount", 2, 10),
                (party_set_slot, ":party", slot_party_hunting_amount, ":amount"),
            (try_end),
    ] 
  ),  
  
  
  
#hunting triggers RAMARAUNT
     (1,
   [
   (try_for_parties, ":cur_party"),
      #(party_is_active, ":cur_party"),
      (party_get_slot, ":slot_answer", ":cur_party", slot_party_is_hunting),
      (this_or_next|eq, ":slot_answer",1), #hunting
      (eq,":slot_answer",2), #poaching
      (party_get_slot, ":slot_time", ":cur_party", slot_party_hunting_time),
      (store_current_hours, ":cur_hours"),
      (ge,":cur_hours",":slot_time"),

      
      #now its time to finish hunting.
      (try_begin),
         (eq, ":cur_party", "p_main_party"), #if its the player
         (rest_for_hours_interactive, 0), #interupt rest
         
         #fix messed up relations if poaching (you got away free!)
         (try_begin),
            (eq, ":slot_answer", 2),
            #(call_script, "script_change_player_relation_with_faction", "fac_manhunters", 15),
            (party_get_slot, ":enemy_fac", ":cur_party", slot_party_hunting_land),
            (call_script, "script_change_player_relation_with_faction", ":enemy_fac", 15),
         (try_end),
         
         #resset slots (so trigger ignores next time)
         (party_set_slot, "p_main_party", slot_party_is_hunting, 0),
         (call_script, "script_set_hunting_found", "p_main_party"),   
         #fix text
         (party_set_extra_text, "p_main_party", "@Holding"),
         
         (party_get_slot, ":slot_type", "p_main_party", slot_party_hunting_found),
         
         (try_begin),
            (eq, ":slot_type", 1),
            (jump_to_menu, "mnu_deer_herd"),
         (else_try),
            (eq, ":slot_type", 2),
            (jump_to_menu, "mnu_boar_herd"),
         (else_try),
            (eq, ":slot_type", 3),
            (jump_to_menu, "mnu_unicorn_herd"),
         (try_end),
         

         
         
      (else_try), #if its an npc
                            #YOU CAN CODE YOUR OWN NPC HUNTERS AND POACHERS HERE - RAMARAUNT
      (try_end),
      
   (try_end),
   
   
    ]),
    
    
    
slot_party_is_hunting = 351 #HUNTING MOD ADD RAMARAUNT 1 = hunting 2 = poaching
slot_party_hunting_time = 352 #HUNTING MOD ADD RAMARAUNT end time of hunt
slot_party_hunting_land = 353 #HUNTING MOD ADD RAMARAUNT land hunting in
slot_party_hunting_found = 354 #HUNTING MOD ADD RAMARAUNT animal type found 1 = deer 2 = boar 3 = unicorn
slot_party_hunting_amount = 355 #HUNTING MOD ADD RAMARAUNT animal amount found

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#Hunting Mod begin#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
("camp_hunting_or_poaching", mnf_scale_picture, "{s5}", "none",
[
	(set_background_mesh, "mesh_pic_hunting"), #set background pic
	#First determine if it is a good climate to hunt here (not desert)
	(party_get_current_terrain, ":terrain" , "p_main_party"),
	(try_begin), #if terrain is not desert
		#conditions
		(neq, ":terrain", rt_desert),
		
		#actions
		(str_store_string, s11, "str_hunt_possible"),
		# Find the closest town, village, or castle to the player's party
		
		#initialization of closest determinationtion
		(assign, ":closest_settlement", 0),
		(assign, ":closest_distance", 9999999999),
		(party_get_position, pos10, "p_main_party"),
		(str_store_string, s6, "str_the_settlement_of"),
		
		#first try towns
		(try_for_range, ":cur_town", towns_begin, towns_end),
			(party_get_position, pos11, ":cur_town"),
			(get_distance_between_positions, ":cur_distance", pos10, pos11),
			(lt, ":cur_distance", ":closest_distance"),
			(assign, ":closest_distance", ":cur_distance"),
			(assign, ":closest_settlement", ":cur_town"),
			(str_store_string, s6, "str_the_town_of"),
		(try_end),
		
		#now castles
		(try_for_range, ":cur_castle", castles_begin, castles_end),
			(party_get_position, pos11, ":cur_castle"),
			(get_distance_between_positions, ":cur_distance", pos10, pos11),
			(lt, ":cur_distance", ":closest_distance"),
			(assign, ":closest_distance", ":cur_distance"),
			(assign, ":closest_settlement", ":cur_castle"),
			(str_store_string, s6, "str_the_castle_of"),
		(try_end),
		
		#finally villages
		(try_for_range, ":cur_village", villages_begin, villages_end),
			(party_get_position, pos11, ":cur_village"),
			(get_distance_between_positions, ":cur_distance", pos10, pos11),
			(lt, ":cur_distance", ":closest_distance"),
			(assign, ":closest_distance", ":cur_distance"),
			(assign, ":closest_settlement", ":cur_village"),
			(str_store_string, s6, "str_the_village_of"),
		(try_end),
		
		#final calculations and stuff
		(store_faction_of_party, reg7, ":closest_settlement"), #get the faction of the closest settlement
		(str_store_faction_name, s7, reg7), #store the name of the faction in s7
		(str_store_party_name, s8, ":closest_settlement"), #store the name of the closest settlement in s8
		(str_store_string, s9, "str_you_are_closest"),
		(try_begin),
			#conditions
			(eq, "$players_kingdom", reg7), #player is in kingdom
			(eq, "$player_has_homage", 1), #player is vassal
			
			#actions
			(str_store_string, s10, "str_hunting_allowed"),
			(assign,reg31, 0),
		(else_try),
			#conditions
			(neq, "$players_kingdom", reg7), #player is not in kingdom 
			
			#actions
			(str_store_string, s10, "str_hunting_common"),
			(assign, reg31, 1),
		(else_try),
			#conditions
			(neq, "$player_has_homage", 1), #player is not vassal (but is a mercenary)
			
			#actions
			(str_store_string, s10, "str_hunting_merc"),
			(assign, reg31, 2),
		(try_end),
		
		#finally, build the string to display
		(str_store_string, s5, "str_hunt_menu_final"),
		
	(else_try), #if the terrain is desert
		#conditions
		(eq, ":terrain", rt_desert),
		
		#actions
		(str_store_string,s5,"str_area_is_desert_so_no_hunting"),
		(assign, reg31, -1),
		
	(else_try), #if the terrain is ocean or river
		#conditions
		(this_or_next|eq,":terrain",rt_water),
		(eq,":terrain",rt_river),
		
		#actions
		(str_store_string,s5,"str_area_is_water_so_no_hunting"),
		(assign, reg31, -1),
		
	(try_end),
	
	
	
],
[

	   ("start_poaching",[
			(this_or_next|eq, reg31, 1),
			(eq, reg31, 2),
	   ],"{!}Attempt to poach for some animals.",
       [
			(jump_to_menu, "mnu_poaching"),		
        ]
       ),
	   
	   	   ("start_hunting",[
				(eq, reg31, 0),
	   ],"{!}Attempt to hunt for some animals.",
       [
			(jump_to_menu, "mnu_hunting"),
        ]
       ),
	   
		#Return to the camp menu.
	   ("back_to_camp_menu",[],"{!}Back to camp menu.",
       [
         (jump_to_menu, "mnu_camp"),
        ]
       ),
],
),

("poaching", mnf_scale_picture, "You prepare for the poach. {s5}", "none",
[
		(set_background_mesh, "mesh_pic_hunting"), #set background pic
		(call_script, "script_get_max_skill_of_player_party", "skl_tracking"),
		(assign, ":max_skill", reg0),
		(assign, ":max_skill_owner", reg1),
		(assign, reg2, ":max_skill"),
		(str_store_troop_name, s11, ":max_skill_owner"),
		
		(try_begin),
			(eq, ":max_skill_owner", "trp_player"),
			(str_store_string,s5, "str_poach_you_have_the_highest_tracking"),
		(else_try),
			(str_store_string,s5, "str_poach_companion_has_highest_tracking"),
		(try_end),
],
[

		#Actually begin to poach
	   ("start_poach",[],"{!}Start your poach.",
       [
         	(call_script,"script_initialize_hunting_time", reg1, "p_main_party"),
			
			#slots
			(party_set_slot, "p_main_party", slot_party_is_hunting, 2),
			(party_set_slot, "p_main_party", slot_party_hunting_land, reg7),	
			
			#relations (only changed in poaching, so changed here)
			#(call_script, "script_change_player_relation_with_faction", "fac_manhunters", -15),
			(call_script, "script_change_player_relation_with_faction", reg7, -15),
			
			#log
			(str_store_troop_name, s9,reg1),
			(display_log_message, "str_you_begin_hunt",0x0000FF),
			(party_set_extra_text, "p_main_party", "@Poaching"),
			     

           (assign, "$g_infinite_camping", 0),
		   
           (rest_for_hours, 9999999, 5, 1), #rest while attackable, interupted by simple_trigger
		   (change_screen_return),
        ]
       ),
	   
		#Return to the camp menu.
	   ("back_to_camp_menu",[],"{!}Back to camp menu.",
       [
         (jump_to_menu, "mnu_camp"),
        ]
       ),
],
),

("hunting", mnf_scale_picture, "You prepare for the hunt. {s5}", "none",
[
		(set_background_mesh, "mesh_pic_hunting"), #set background pic
		(call_script, "script_get_max_skill_of_player_party", "skl_tracking"),
		(assign, ":max_skill", reg0),
		(assign, ":max_skill_owner", reg1),
		(assign, reg2, ":max_skill"),
		(str_store_troop_name, s11, ":max_skill_owner"),
		
		(try_begin),
			(eq, ":max_skill_owner", "trp_player"),
			(str_store_string,s5, "str_hunt_you_have_the_highest_tracking"),
		(else_try),
			(str_store_string,s5, "str_hunt_companion_has_highest_tracking"),
		(try_end),
],
[

		#Actually begin to hunt.
	   ("start_hunt",[],"{!}Start your hunt.",
       [
			(call_script,"script_initialize_hunting_time", reg1, "p_main_party"),
			(call_script,"script_set_hunting_found","p_main_party"),
			#slots
			(party_set_slot, "p_main_party", slot_party_is_hunting, 1),
			(party_set_slot, "p_main_party", slot_party_hunting_land, reg7),	
			
			#relations (only changed in poaching, so not changed here)
			#(call_script, "script_change_player_relation_with_faction", "fac_manhunters", -15),
			#(call_script, "script_change_player_relation_with_faction", reg7, -15),
			
			#log
			(str_store_troop_name, s9,reg1),
			(display_log_message, "str_you_begin_hunt",0x0000FF),
			(party_set_extra_text, "p_main_party", "@Hunting"),
			     

           (assign, "$g_infinite_camping", 0),
		   
           (rest_for_hours, 9999999, 5, 1), #rest while attackable, interupted by simple_trigger
		   (change_screen_return),
        ]
       ),
	   
		#Return to the camp menu.
	   ("back_to_camp_menu",[],"{!}Back to camp menu.",
       [
         (jump_to_menu, "mnu_camp"),
        ]
       ),
],
),



  ("deer_herd",mnf_scale_picture,
   "{s10}",
   "none",
   [
   	(party_get_slot, ":amount", "p_main_party", slot_party_hunting_amount),
   (try_begin),
      (gt, "$num_deers_killed",0),
	  (val_sub, ":amount", "$num_deers_killed"),
	  (party_set_slot, "p_main_party", slot_party_hunting_amount, ":amount"),
      (troop_clear_inventory, "trp_temp_troop"),
      (troop_add_items, "trp_temp_troop", "itm_deer_meat", "$num_deers_killed"),
	  (troop_add_items, "trp_temp_troop", "itm_raw_leather", "$num_deers_killed"),

      (party_get_num_companions, ":num_deers", "$g_encountered_party"),
      (assign,"$num_deers_killed",0),
      (troop_sort_inventory, "trp_temp_troop"),
	  (change_screen_loot,"trp_temp_troop"),
    (try_end),
	(assign,reg5, ":amount"),
	(try_begin),
		(gt, 1, ":amount"),
		(str_store_string, s10, "str_you_run_into_deer"),
	(else_try),
		(eq, 1, ":amount"),
		(str_store_string, s10, "str_you_run_into_a_deer"),
	(else_try),
		(str_store_string, s10, "str_hunting_done"),
	(try_end),
    (set_background_mesh, "mesh_pic_cattle"),
   ],
    [
      ("deer_kill",
      [
	  	  (party_get_slot, ":num_boars", "p_main_party", slot_party_hunting_amount),
	  (gt,":num_boars", 0),
      ]
      ,"Hunt some of the animals.",
       [
       (set_jump_mission,"mt_deer_hunting"),
       (jump_to_scene,"scn_random_scene_plain_forest"),
       (change_screen_mission),
        ]
       ),
      ("leave",[],"Leave.",
       [(change_screen_map),
        ]
       ),
      ]
  ),
  ("deer_herd_kill_end",0,
   "You shouldn't be reading this.",
   "none",
   [(change_screen_map)],
    [
      ]
  ),
  ("boar_herd",mnf_scale_picture,
   "{10}",
   "none",
   [
   (party_get_slot, ":amount", "p_main_party", slot_party_hunting_amount),
   (try_begin),
      (gt, "$num_boars_killed",0),
	  (val_sub, ":amount", "$num_boars_killed"),
	  (party_set_slot, "p_main_party", slot_party_hunting_amount, ":amount"),
      (troop_clear_inventory, "trp_temp_troop"),
      (troop_add_items, "trp_temp_troop", "itm_boar_meat", "$num_boars_killed"),
	  (troop_add_items, "trp_temp_troop", "itm_raw_leather", "$num_deers_killed"),

      (assign,"$num_boars_killed",0),
      (troop_sort_inventory, "trp_temp_troop"),
	  (change_screen_loot,"trp_temp_troop"),
    (try_end),
	(assign,reg5, ":amount"),
	(try_begin),
		(gt, 1, ":amount"),
		(str_store_string, s10, "str_you_run_into_boars"),
	(else_try),
		(eq, 1, ":amount"),
		(str_store_string, s10, "str_you_run_into_a_boar"),
	(else_try),
		(str_store_string, s10, "str_hunting_done"),
	(try_end),
    (set_background_mesh, "mesh_pic_cattle"),
   ],
    [
      ("boar_kill",[  
	  	  (party_get_slot, ":num_boars", "p_main_party", slot_party_hunting_amount),
	  (gt,":num_boars", 0),
      ],"Hunt some of the animals.",
       [
       (set_jump_mission,"mt_boar_hunting"),
       (jump_to_scene,"scn_random_scene_plain_forest"),
       (change_screen_mission),
        ]
       ),
      ("leave",[],"Leave.",
       [(change_screen_map),
        ]
       ),
      ]
  ),
  ("boar_herd_kill_end",0,
   "You shouldn't be reading this.",
   "none",
   [(change_screen_map)],
    [
      ]
  ),
  
  ("unicorn_herd",mnf_scale_picture,
   "{s10}",
   "none",
   [
   (party_get_slot, ":amount", "p_main_party", slot_party_hunting_amount),
   (try_begin),
      (gt, "$num_boars_killed",0),
	  (val_sub, ":amount", "$num_boars_killed"),
	  (party_set_slot, "p_main_party", slot_party_hunting_amount, ":amount"),
      (troop_clear_inventory, "trp_temp_troop"),
      (troop_add_items, "trp_temp_troop", "itm_magical_meat", "$num_boars_killed"),
	  (troop_add_items, "trp_temp_troop", "itm_unicorn_horn", "$num_deers_killed"),
	  (troop_add_items, "trp_temp_troop", "itm_raw_leather", "$num_deers_killed"),

      (assign,"$num_boars_killed",0),
      (troop_sort_inventory, "trp_temp_troop"),
	  (change_screen_loot,"trp_temp_troop"),
    (try_end),
	(assign,reg5, ":amount"),
	(try_begin),
		(gt, 1, ":amount"),
		(str_store_string, s10, "str_you_run_into_unicorns"),
	(else_try),
		(eq, 1, ":amount"),
		(str_store_string, s10, "str_you_run_into_unicorn"),
	(else_try),
		(str_store_string, s10, "str_hunting_done"),
	(try_end),
    (set_background_mesh, "mesh_pic_cattle"),
   ],
    [
      ("boar_kill",[  
	  (party_get_slot, ":num_boars", "p_main_party", slot_party_hunting_amount),
	  (gt,":num_boars", 0),
      ],"Hunt some of the animals.",
       [
       (set_jump_mission,"mt_unicorn_hunting"),
       (jump_to_scene,"scn_random_scene_plain_forest"),
       (change_screen_mission),
        ]
       ),
      ("leave",[],"Leave.",
       [(change_screen_map),
        ]
       ),
      ]
  ),
  ("boar_herd_kill_end",0,
   "You shouldn't be reading this.",
   "none",
   [(change_screen_map)],
    [
      ]
  ),
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#Hunting Mod end#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

    #-#-#-#-#-#-#-#-#-#-#-#-#-#-#
    #-#-#-#Hunting Mod begin#-#-#
    #-#-#-#-#-#-#-#-#-#-#-#-#-#-#
      ("camp_go_hunting",
       [],
       "Go hunting in the local area.",
       [(jump_to_menu, "mnu_camp_hunting_or_poaching"),
        ],
       ),
    #-#-#-#-#-#-#-#-#-#-#-#-#-#-#
    #-#-#-#Hunting Mod end#-#-#-#
    #-#-#-#-#-#-#-#-#-#-#-#-#-#-#
    
    
    #-#-#-#-#-#-#-#-#-#-#-#-#-#-#
    #-#-#-#Hunting Mod begin#-#-#
    #-#-#-#-#-#-#-#-#-#-#-#-#-#-#
    
    #initial menu
    ("area_is_desert_so_no_hunting", "You are in the middle of the desert, so it is impossible for you to hunt here."),
    ("area_is_water_so_no_hunting", "You are in the middle of the water, so it is impossible for you to find boar or deer here!"),
    ("hunt_possible", "From the look of this land, it is safe for you to guess there is plenty of game for you to hunt here."),
    
    ("hunting_merc","You may fight for the {s7}, but only as a mercenary and not as a vassal. So, hunting here would be illegal for you."),
    ("hunting_common","You are not a member of the {s7} nobility, so you are not allowed to hunt in these lands. If you do so, there is a possibility you will be caught in the act and face charges."),
    ("hunting_allowed","You are a member of the {s7} nobility, so by the laws of the land, you are allowed to hunt here as you please."),
    
    ("the_castle_of", ""),
    ("the_village_of", "the village of "),
    ("the_town_of", "the town of "),
    ("the_settlement_of", "the settlement of "), #fallback option
    
    ("you_are_closest", "You are closest to {s6} {s8}, which is owned by {s7}."),
    ("hunt_menu_final", "{s11} {s9} {s10}"),
    
    #hunting menu
    ("hunt_you_have_the_highest_tracking", "As the party member with the highest tarcking skill ({reg3}), you will lead the hunt. You will be frozen in place until hunting is finished, and you will not be able to abort. Would you like to begin?"),
    ("hunt_companion_has_highest_tracking", "As the party member with the highest tracking skill ({reg3}), {s11} will lead the hunt. You will be frozen in place until hunting is finished, and you will not be able to abort. Would you like to begin?"),
    ("you_begin_hunt", "{s9} leads your party on a hunt..."),

    
    #poaching menu
    ("poach_you_have_the_highest_tracking", "As the party member with the highest tarcking skill ({reg3}), you will lead the poach. You will be frozen in place until hunting is finished, and you will not be able to abort. Would you like to begin?"),
    ("poach_companion_has_highest_tracking", "As the party member with the highest tracking skill ({reg3}), {s11} will lead the poach. You will be frozen in place until hunting is finished, and you will not be able to abort. Would you like to begin?"),
    
    #approach menu
    ("you_run_into_deer", "You run into a herd of {reg5} foraging deer. You can now move in for the kill."),
    ("you_run_into_a_deer", "You run into a single deer. You can now move in for the kill."),
    ("you_run_into_unicorns", "You run into a herd of frolicking unicorns. How amazing! Time to murder them."),
    ("you_run_into_unicorn", "You run into a frolicking unicorn. How beautiful it is, just like you heard in old legends when you were growing up. Shall we murder the creature of the forest, and take its valuable horn?"),
    ("you_run_into_boars", "You run into a herd of {reg5} foraging deer. You can now move in for the kill."),
    ("you_run_into_a_boar", "You run into a single foraging boar. This creature is alone, and must have been kicked out of its herd. You can now move in for the kill."),
    ("animals_left", "If there were animals here at one point, they are no longer here."),
    ("hunting_done", "There are no remaining animals to slay."),
    
    #-#-#-#-#-#-#-#-#-#-#-#-#-#-#
    #-#-#-#Hunting Mod end#-#-#-#
    #-#-#-#-#-#-#-#-#-#-#-#-#-#-#
    
    
    
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#Hunting Mod begin#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
 
  (
    "deer_hunting",mtf_battle_mode,-1,
    "You lead your deers to battle.",
    [
     (1,mtef_team_0|mtef_leader_only,0,aif_start_alarmed,12,[]),
     (4,mtef_visitor_source,0,aif_start_alarmed,0,[]),
     ],
    [
      (ti_tab_pressed, 0, 0, [
      (set_trigger_result,1)], []), #leaving area
      (0, 0, ti_once, [ #spawing deers
             (party_get_slot, ":num_deers", "p_main_party", slot_party_hunting_amount),
             (val_sub,":num_deers",1),
             (ge,":num_deers",0),
                     (assign,"$num_deers_killed",0),
                     (get_scene_boundaries, pos10,pos11),
                     (position_get_x, ":scene_min_x", pos10),
                     (position_get_x, ":scene_max_x", pos11),
                     (position_get_y, ":scene_min_y", pos10),
                     (position_get_y, ":scene_max_y", pos11),
             (store_div,":border_x",":scene_max_x",10),
             (val_add,":scene_min_x",":border_x"),
             (val_sub,":scene_max_x",":border_x"),
             (store_div,":border_y",":scene_max_y",10),
             (val_add,":scene_min_y",":border_y"),
             (val_sub,":scene_max_y",":border_y"),
             (store_random_in_range,":x_pos",":scene_min_x",":scene_max_x"),
             (store_random_in_range,":y_pos",":scene_min_y",":scene_max_y"),
                     (init_position, pos1),
             (position_set_x,pos1,":x_pos"),
             (position_set_y,pos1,":y_pos"),
             (position_set_z,pos1,10000),
             (position_set_z_to_ground_level,pos1),
                     (set_spawn_position, pos1),
                     (spawn_horse, "itm_deer"),
             (assign,"$leading_deer",reg0),
             (try_for_range,":unused",0,":num_deers"),
                       (init_position, pos1),
               (store_random_in_range,":x_pos_add",0,1000),
               (store_random_in_range,":y_pos_add",0,1000),
               (val_add,":x_pos_add",":x_pos"),
               (val_add,":y_pos_add",":y_pos"),
               (position_set_x,pos1,":x_pos_add"),
               (position_set_y,pos1,":y_pos_add"),
               (position_set_z,pos1,10000),
               (position_set_z_to_ground_level,pos1),
               (set_spawn_position, pos1),
                       (spawn_horse, "itm_deer"),
             (try_end),
                 ], []),
      (1,0,0,[], #wounded deers move slower
      [(try_for_agents,reg(1)),
       (agent_get_item_id,reg(2),reg(1)),
       (eq,reg(2),"itm_deer"),
       (store_agent_hit_points,reg(2),reg(1)),
       (store_mul,reg(3),20,reg(2)),
       (val_div,reg(3),40),
       (agent_set_speed_limit,reg(1),reg(3)),
       (try_end),
      ]),
      (5,0,0,
      [
      (neg|agent_is_alive,"$leading_deer"),
      ],
      [
      (try_for_agents,reg(1)),
        (agent_get_item_id,reg(2),reg(1)),
    (eq,reg(2),"itm_deer"),
    (assign,"$leading_deer",reg(1)),
      (try_end),
      ]),
      (1,0,0,[],
      [
              (assign,":num_kills",0),
          (try_for_agents,reg(1)),
            (agent_get_item_id,reg(2),reg(1)),
            (eq,reg(2),"itm_deer"),
                (store_agent_hit_points,reg(2),reg(1)),
        (eq,reg(2),0),
        (val_add,":num_kills",1),
          (try_end),    
          (gt,":num_kills","$num_deers_killed"),         
                     (get_scene_boundaries, pos10,pos11),
                     (position_get_x, ":scene_min_x", pos10),
                     (position_get_x, ":scene_max_x", pos11),
                     (position_get_y, ":scene_min_y", pos10),
                     (position_get_y, ":scene_max_y", pos11),
             (store_div,":border_x",":scene_max_x",10),
             (val_add,":scene_min_x",":border_x"),
             (val_sub,":scene_max_x",":border_x"),
             (store_div,":border_y",":scene_max_y",10),
             (val_add,":scene_min_y",":border_y"),
             (val_sub,":scene_max_y",":border_y"),
             (store_random_in_range,":x_pos",":scene_min_x",":scene_max_x"),
             (store_random_in_range,":y_pos",":scene_min_y",":scene_max_y"),
                     (init_position, pos1),
             (position_set_x,pos1,":x_pos"),
             (position_set_y,pos1,":y_pos"),
             (position_set_z,pos1,10000),
             (position_set_z_to_ground_level,pos1),
                     (agent_set_scripted_destination,"$leading_deer",pos1),
                 (assign,"$num_deers_killed",":num_kills"),
      ]),
      (5,0,0,[],
      [
      (agent_get_position,pos1,"$leading_deer"),
      (position_get_x,":x_pos",pos1),
      (position_get_y,":y_pos",pos1),
      (this_or_next|le,":x_pos",5000),
      (this_or_next|le,":y_pos",5000),
      (this_or_next|ge,":x_pos",38000),
      (ge,":y_pos",38000),
                     (get_scene_boundaries, pos10,pos11),
                     (position_get_x, ":scene_min_x", pos10),
                     (position_get_x, ":scene_max_x", pos11),
                     (position_get_y, ":scene_min_y", pos10),
                     (position_get_y, ":scene_max_y", pos11),
             (store_div,":border_x",":scene_max_x",10),
             (val_add,":scene_min_x",":border_x"),
             (val_sub,":scene_max_x",":border_x"),
             (store_div,":border_y",":scene_max_y",10),
             (val_add,":scene_min_y",":border_y"),
             (val_sub,":scene_max_y",":border_y"),
             (store_random_in_range,":x_pos",":scene_min_x",":scene_max_x"),
             (store_random_in_range,":y_pos",":scene_min_y",":scene_max_y"),
                     (init_position, pos1),
             (position_set_x,pos1,":x_pos"),
             (position_set_y,pos1,":y_pos"),
             (position_set_z,pos1,10000),
             (position_set_z_to_ground_level,pos1),
                     (agent_set_scripted_destination,"$leading_deer",pos1),
      ]),
      (1,0,0,[],
      [
      (try_for_agents,reg(1)),
    (agent_get_item_id,reg(2),reg(1)),
    (eq,reg(2),"itm_deer"),
    (store_agent_hit_points,":health",reg(1)),
    (store_sub,":damage",100,":health"),
    (agent_get_slot,":prev_damage",reg(1),1),
    (neq,":prev_damage",":damage"),
    (agent_set_slot,reg(1),1,":damage"),
        (agent_get_position,pos1,reg(1)),
        (position_get_x,":x_pos",pos1),
    (position_get_y,":y_pos",pos1),
        (store_random_in_range,":x_pos_add",0,1000),
        (store_random_in_range,":y_pos_add",0,1000),
    (val_add,":x_pos",":x_pos_add"),
    (val_add,":y_pos",":y_pos_add"),
    (position_set_x,pos1,":x_pos"),
    (position_set_y,pos1,":y_pos"),
        (agent_set_scripted_destination,reg(1),pos1),
      (try_end),
      ]),
      (0.5,0,0, #deer travelling
      [],
      [
      (get_player_agent_no,reg(1)),
      (agent_get_position,pos1,reg(1)),
      (agent_get_position,pos4,"$leading_deer"),
      (position_get_x,":x_pos",pos4),
      (position_get_y,":y_pos",pos4),
      (try_for_agents,reg(1)),
    (agent_get_item_id,reg(2),reg(1)),
    (eq,reg(2),"itm_deer"),
        (agent_get_position,pos2,reg(1)),
    (get_distance_between_positions,reg(3),pos1,pos2),
    (try_begin),
            (position_get_x,":pos_x",pos2),
            (position_get_x,":pos_y",pos2),
             (position_get_x, ":scene_min_x", pos10),
                     (position_get_x, ":scene_max_x", pos11),
                     (position_get_y, ":scene_min_y", pos10),
                     (position_get_y, ":scene_max_y", pos11),
             (store_div,":border_x",":scene_max_x",10),
             (val_add,":scene_min_x",":border_x"),
             (val_sub,":scene_max_x",":border_x"),
             (store_div,":border_y",":scene_max_y",10),
             (val_add,":scene_min_y",":border_y"),
             (val_sub,":scene_max_y",":border_y"),
        (this_or_next|gt,":pos_x",":scene_max_x"),
        (this_or_next|lt,":pos_x",":scene_min_x"),
        (this_or_next|gt,":pos_y",":scene_max_y"),
        (lt,":pos_y",":scene_min_y"),
        (store_random_in_range,":x_pos",":scene_min_x",":scene_max_x"),
        (store_random_in_range,":y_pos",":scene_min_y",":scene_max_y"),
                (init_position, pos1),
        (position_set_x,pos1,":x_pos"),
        (position_set_y,pos1,":y_pos"),
        (position_set_z,pos1,10000),
        (position_set_z_to_ground_level,pos1),
                (agent_set_scripted_destination,reg(1),pos1),
    (else_try),
        (le,reg(3),2500),
        (position_get_x,reg(4),pos1),
        (position_get_x,reg(5),pos2),
        (store_sub,":x_dist",reg(5),reg(4)),
        (val_mul,":x_dist",10),
        (position_get_y,reg(6),pos1),
        (position_get_y,reg(7),pos2),
        (store_sub,":y_dist",reg(7),reg(6)),
        (val_mul,":y_dist",10),
        (init_position,pos3),
        (val_add,":x_dist",reg(5)),
        (val_add,":y_dist",reg(7)),
        (position_set_x,pos3,":x_dist"),
        (position_set_y,pos3,":y_dist"),
            (position_set_z,pos3,10000),
            (position_set_z_to_ground_level,pos3),
        (agent_set_scripted_destination,reg(1),pos3),
    (else_try),
        (get_distance_between_positions,reg(3),pos4,pos2),
        (ge,reg(3),2000),
                       (init_position, pos6),
               (store_random_in_range,":x_pos_add",0,1000),
               (store_random_in_range,":y_pos_add",0,1000),
               (val_add,":x_pos_add",":x_pos"),
               (val_add,":y_pos_add",":y_pos"),
               (position_set_x,pos6,":x_pos_add"),
               (position_set_y,pos6,":y_pos_add"),
               (position_set_z,pos6,10000),
               (position_set_z_to_ground_level,pos6),
               (agent_set_scripted_destination,reg(1),pos6),
    (try_end),
      (try_end),
      ]),
    ]),
 
   
  (
    "unicorn_hunting",mtf_battle_mode,-1,
    "You lead your unicorns to battle.",
    [
     (1,mtef_team_0|mtef_leader_only,0,aif_start_alarmed,12,[]),
     (4,mtef_visitor_source,0,aif_start_alarmed,0,[]),
     ],
    [
      (ti_tab_pressed, 0, 0, [ (set_trigger_result,1)], []), #leaving area
      (0, 0, ti_once, [ #spawing boars
             (party_get_slot, ":num_boars", "p_main_party", slot_party_hunting_amount),
             (val_sub,":num_boars",1),
             (ge,":num_boars",0),
                     (assign,"$num_boars_killed",0),
                     (get_scene_boundaries, pos10,pos11),
                     (position_get_x, ":scene_min_x", pos10),
                     (position_get_x, ":scene_max_x", pos11),
                     (position_get_y, ":scene_min_y", pos10),
                     (position_get_y, ":scene_max_y", pos11),
             (store_div,":border_x",":scene_max_x",10),
             (val_add,":scene_min_x",":border_x"),
             (val_sub,":scene_max_x",":border_x"),
             (store_div,":border_y",":scene_max_y",10),
             (val_add,":scene_min_y",":border_y"),
             (val_sub,":scene_max_y",":border_y"),
             (store_random_in_range,":x_pos",":scene_min_x",":scene_max_x"),
             (store_random_in_range,":y_pos",":scene_min_y",":scene_max_y"),
                     (init_position, pos1),
             (position_set_x,pos1,":x_pos"),
             (position_set_y,pos1,":y_pos"),
             (position_set_z,pos1,10000),
             (position_set_z_to_ground_level,pos1),
                     (set_spawn_position, pos1),
                     (spawn_horse, "itm_boar"),
             (assign,"$leading_boar",reg0),
             (try_for_range,":unused",0,":num_boars"),
                       (init_position, pos1),
               (store_random_in_range,":x_pos_add",0,1000),
               (store_random_in_range,":y_pos_add",0,1000),
               (val_add,":x_pos_add",":x_pos"),
               (val_add,":y_pos_add",":y_pos"),
               (position_set_x,pos1,":x_pos_add"),
               (position_set_y,pos1,":y_pos_add"),
               (position_set_z,pos1,10000),
               (position_set_z_to_ground_level,pos1),
               (set_spawn_position, pos1),
                       (spawn_horse, "itm_boar"),
             (try_end),
                 ], []),
      (1,0,0,[], #wounded boars move slower
      [(try_for_agents,reg(1)),
       (agent_get_item_id,reg(2),reg(1)),
       (eq,reg(2),"itm_boar"),
       (store_agent_hit_points,reg(2),reg(1)),
       (store_mul,reg(3),20,reg(2)),
       (val_div,reg(3),100),
       (agent_set_speed_limit,reg(1),reg(3)),
       (try_end),
      ]),
      (5,0,0,
      [
      (neg|agent_is_alive,"$leading_boar"),
      ],
      [
      (try_for_agents,reg(1)),
        (agent_get_item_id,reg(2),reg(1)),
    (eq,reg(2),"itm_boar"),
    (assign,"$leading_boar",reg(1)),
      (try_end),
      ]),
      (1,0,0,[],
      [
              (assign,":num_kills",0),
          (try_for_agents,reg(1)),
            (agent_get_item_id,reg(2),reg(1)),
            (eq,reg(2),"itm_boar"),
                (store_agent_hit_points,reg(2),reg(1)),
        (eq,reg(2),0),
        (val_add,":num_kills",1),
          (try_end),    
          (gt,":num_kills","$num_boars_killed"),         
                     (get_scene_boundaries, pos10,pos11),
                     (position_get_x, ":scene_min_x", pos10),
                     (position_get_x, ":scene_max_x", pos11),
                     (position_get_y, ":scene_min_y", pos10),
                     (position_get_y, ":scene_max_y", pos11),
             (store_div,":border_x",":scene_max_x",10),
             (val_add,":scene_min_x",":border_x"),
             (val_sub,":scene_max_x",":border_x"),
             (store_div,":border_y",":scene_max_y",10),
             (val_add,":scene_min_y",":border_y"),
             (val_sub,":scene_max_y",":border_y"),
             (store_random_in_range,":x_pos",":scene_min_x",":scene_max_x"),
             (store_random_in_range,":y_pos",":scene_min_y",":scene_max_y"),
                     (init_position, pos1),
             (position_set_x,pos1,":x_pos"),
             (position_set_y,pos1,":y_pos"),
             (position_set_z,pos1,10000),
             (position_set_z_to_ground_level,pos1),
                     (agent_set_scripted_destination,"$leading_boar",pos1),
                 (assign,"$num_boars_killed",":num_kills"),
      ]),
      (5,0,0,[],
      [
      (agent_get_position,pos1,"$leading_boar"),
      (position_get_x,":x_pos",pos1),
      (position_get_y,":y_pos",pos1),
      (this_or_next|le,":x_pos",5000),
      (this_or_next|le,":y_pos",5000),
      (this_or_next|ge,":x_pos",38000),
      (ge,":y_pos",38000),
                     (get_scene_boundaries, pos10,pos11),
                     (position_get_x, ":scene_min_x", pos10),
                     (position_get_x, ":scene_max_x", pos11),
                     (position_get_y, ":scene_min_y", pos10),
                     (position_get_y, ":scene_max_y", pos11),
             (store_div,":border_x",":scene_max_x",10),
             (val_add,":scene_min_x",":border_x"),
             (val_sub,":scene_max_x",":border_x"),
             (store_div,":border_y",":scene_max_y",10),
             (val_add,":scene_min_y",":border_y"),
             (val_sub,":scene_max_y",":border_y"),
             (store_random_in_range,":x_pos",":scene_min_x",":scene_max_x"),
             (store_random_in_range,":y_pos",":scene_min_y",":scene_max_y"),
                     (init_position, pos1),
             (position_set_x,pos1,":x_pos"),
             (position_set_y,pos1,":y_pos"),
             (position_set_z,pos1,10000),
             (position_set_z_to_ground_level,pos1),
                     (agent_set_scripted_destination,"$leading_boar",pos1),
      ]),
      (1,0,0,[],
      [
      (try_for_agents,reg(1)),
    (agent_get_item_id,reg(2),reg(1)),
    (eq,reg(2),"itm_boar"),
    (store_agent_hit_points,":health",reg(1)),
    (store_sub,":damage",100,":health"),
    (agent_get_slot,":prev_damage",reg(1),1),
    (neq,":prev_damage",":damage"),
    (agent_set_slot,reg(1),1,":damage"),
        (agent_get_position,pos1,reg(1)),
        (position_get_x,":x_pos",pos1),
    (position_get_y,":y_pos",pos1),
        (store_random_in_range,":x_pos_add",0,1000),
        (store_random_in_range,":y_pos_add",0,1000),
    (val_add,":x_pos",":x_pos_add"),
    (val_add,":y_pos",":y_pos_add"),
    (position_set_x,pos1,":x_pos"),
    (position_set_y,pos1,":y_pos"),
        (agent_set_scripted_destination,reg(1),pos1),
      (try_end),
      ]),
      (0.5,0,0, #boar travelling
      [],
      [
      (get_player_agent_no,reg(1)),
      (agent_get_position,pos1,reg(1)),
      (agent_get_position,pos4,"$leading_boar"),
      (position_get_x,":x_pos",pos4),
      (position_get_y,":y_pos",pos4),
      (try_for_agents,reg(1)),
    (agent_get_item_id,reg(2),reg(1)),
    (eq,reg(2),"itm_boar"),
        (agent_get_position,pos2,reg(1)),
    (get_distance_between_positions,reg(3),pos1,pos2),
    (try_begin),
            (position_get_x,":pos_x",pos2),
            (position_get_x,":pos_y",pos2),
             (position_get_x, ":scene_min_x", pos10),
                     (position_get_x, ":scene_max_x", pos11),
                     (position_get_y, ":scene_min_y", pos10),
                     (position_get_y, ":scene_max_y", pos11),
             (store_div,":border_x",":scene_max_x",10),
             (val_add,":scene_min_x",":border_x"),
             (val_sub,":scene_max_x",":border_x"),
             (store_div,":border_y",":scene_max_y",10),
             (val_add,":scene_min_y",":border_y"),
             (val_sub,":scene_max_y",":border_y"),
        (this_or_next|gt,":pos_x",":scene_max_x"),
        (this_or_next|lt,":pos_x",":scene_min_x"),
        (this_or_next|gt,":pos_y",":scene_max_y"),
        (lt,":pos_y",":scene_min_y"),
        (store_random_in_range,":x_pos",":scene_min_x",":scene_max_x"),
        (store_random_in_range,":y_pos",":scene_min_y",":scene_max_y"),
                (init_position, pos1),
        (position_set_x,pos1,":x_pos"),
        (position_set_y,pos1,":y_pos"),
        (position_set_z,pos1,10000),
        (position_set_z_to_ground_level,pos1),
                (agent_set_scripted_destination,reg(1),pos1),
    (else_try),
        (le,reg(3),2500),
        (position_get_x,reg(4),pos1),
        (position_get_x,reg(5),pos2),
        (store_sub,":x_dist",reg(5),reg(4)),
        (val_mul,":x_dist",10),
        (position_get_y,reg(6),pos1),
        (position_get_y,reg(7),pos2),
        (store_sub,":y_dist",reg(7),reg(6)),
        (val_mul,":y_dist",10),
        (init_position,pos3),
        (val_add,":x_dist",reg(5)),
        (val_add,":y_dist",reg(7)),
        (position_set_x,pos3,":x_dist"),
        (position_set_y,pos3,":y_dist"),
            (position_set_z,pos3,10000),
            (position_set_z_to_ground_level,pos3),
        (agent_set_scripted_destination,reg(1),pos3),
    (else_try),
        (get_distance_between_positions,reg(3),pos4,pos2),
        (ge,reg(3),2000),
                       (init_position, pos6),
               (store_random_in_range,":x_pos_add",0,1000),
               (store_random_in_range,":y_pos_add",0,1000),
               (val_add,":x_pos_add",":x_pos"),
               (val_add,":y_pos_add",":y_pos"),
               (position_set_x,pos6,":x_pos_add"),
               (position_set_y,pos6,":y_pos_add"),
               (position_set_z,pos6,10000),
               (position_set_z_to_ground_level,pos6),
               (agent_set_scripted_destination,reg(1),pos6),
    (try_end),
      (try_end),
      ]),
    ]),
    
      (
    "boar_hunting",mtf_battle_mode,-1,
    "You lead your boars to battle.",
    [
     (1,mtef_team_0|mtef_leader_only,0,aif_start_alarmed,12,[]),
     (4,mtef_visitor_source,0,aif_start_alarmed,0,[]),
     ],
    [
      (ti_tab_pressed, 0, 0, [ (set_trigger_result,1)], []), #leaving area
      (0, 0, ti_once, [ #spawing boars
             (party_get_slot, ":num_boars", "p_main_party", slot_party_hunting_amount),
             (val_sub,":num_boars",1),
             (ge,":num_boars",0),
                     (assign,"$num_boars_killed",0),
                     (get_scene_boundaries, pos10,pos11),
                     (position_get_x, ":scene_min_x", pos10),
                     (position_get_x, ":scene_max_x", pos11),
                     (position_get_y, ":scene_min_y", pos10),
                     (position_get_y, ":scene_max_y", pos11),
             (store_div,":border_x",":scene_max_x",10),
             (val_add,":scene_min_x",":border_x"),
             (val_sub,":scene_max_x",":border_x"),
             (store_div,":border_y",":scene_max_y",10),
             (val_add,":scene_min_y",":border_y"),
             (val_sub,":scene_max_y",":border_y"),
             (store_random_in_range,":x_pos",":scene_min_x",":scene_max_x"),
             (store_random_in_range,":y_pos",":scene_min_y",":scene_max_y"),
                     (init_position, pos1),
             (position_set_x,pos1,":x_pos"),
             (position_set_y,pos1,":y_pos"),
             (position_set_z,pos1,10000),
             (position_set_z_to_ground_level,pos1),
                     (set_spawn_position, pos1),
                     (spawn_horse, "itm_boar"),
             (assign,"$leading_boar",reg0),
             (try_for_range,":unused",0,":num_boars"),
                       (init_position, pos1),
               (store_random_in_range,":x_pos_add",0,1000),
               (store_random_in_range,":y_pos_add",0,1000),
               (val_add,":x_pos_add",":x_pos"),
               (val_add,":y_pos_add",":y_pos"),
               (position_set_x,pos1,":x_pos_add"),
               (position_set_y,pos1,":y_pos_add"),
               (position_set_z,pos1,10000),
               (position_set_z_to_ground_level,pos1),
               (set_spawn_position, pos1),
                       (spawn_horse, "itm_boar"),
             (try_end),
                 ], []),
      (1,0,0,[], #wounded boars move slower
      [(try_for_agents,reg(1)),
       (agent_get_item_id,reg(2),reg(1)),
       (eq,reg(2),"itm_boar"),
       (store_agent_hit_points,reg(2),reg(1)),
       (store_mul,reg(3),20,reg(2)),
       (val_div,reg(3),100),
       (agent_set_speed_limit,reg(1),reg(3)),
       (try_end),
      ]),
      (5,0,0,
      [
      (neg|agent_is_alive,"$leading_boar"),
      ],
      [
      (try_for_agents,reg(1)),
        (agent_get_item_id,reg(2),reg(1)),
    (eq,reg(2),"itm_boar"),
    (assign,"$leading_boar",reg(1)),
      (try_end),
      ]),
      (1,0,0,[],
      [
              (assign,":num_kills",0),
          (try_for_agents,reg(1)),
            (agent_get_item_id,reg(2),reg(1)),
            (eq,reg(2),"itm_boar"),
                (store_agent_hit_points,reg(2),reg(1)),
        (eq,reg(2),0),
        (val_add,":num_kills",1),
          (try_end),    
          (gt,":num_kills","$num_boars_killed"),         
                     (get_scene_boundaries, pos10,pos11),
                     (position_get_x, ":scene_min_x", pos10),
                     (position_get_x, ":scene_max_x", pos11),
                     (position_get_y, ":scene_min_y", pos10),
                     (position_get_y, ":scene_max_y", pos11),
             (store_div,":border_x",":scene_max_x",10),
             (val_add,":scene_min_x",":border_x"),
             (val_sub,":scene_max_x",":border_x"),
             (store_div,":border_y",":scene_max_y",10),
             (val_add,":scene_min_y",":border_y"),
             (val_sub,":scene_max_y",":border_y"),
             (store_random_in_range,":x_pos",":scene_min_x",":scene_max_x"),
             (store_random_in_range,":y_pos",":scene_min_y",":scene_max_y"),
                     (init_position, pos1),
             (position_set_x,pos1,":x_pos"),
             (position_set_y,pos1,":y_pos"),
             (position_set_z,pos1,10000),
             (position_set_z_to_ground_level,pos1),
                     (agent_set_scripted_destination,"$leading_boar",pos1),
                 (assign,"$num_boars_killed",":num_kills"),
      ]),
      (5,0,0,[],
      [
      (agent_get_position,pos1,"$leading_boar"),
      (position_get_x,":x_pos",pos1),
      (position_get_y,":y_pos",pos1),
      (this_or_next|le,":x_pos",5000),
      (this_or_next|le,":y_pos",5000),
      (this_or_next|ge,":x_pos",38000),
      (ge,":y_pos",38000),
                     (get_scene_boundaries, pos10,pos11),
                     (position_get_x, ":scene_min_x", pos10),
                     (position_get_x, ":scene_max_x", pos11),
                     (position_get_y, ":scene_min_y", pos10),
                     (position_get_y, ":scene_max_y", pos11),
             (store_div,":border_x",":scene_max_x",10),
             (val_add,":scene_min_x",":border_x"),
             (val_sub,":scene_max_x",":border_x"),
             (store_div,":border_y",":scene_max_y",10),
             (val_add,":scene_min_y",":border_y"),
             (val_sub,":scene_max_y",":border_y"),
             (store_random_in_range,":x_pos",":scene_min_x",":scene_max_x"),
             (store_random_in_range,":y_pos",":scene_min_y",":scene_max_y"),
                     (init_position, pos1),
             (position_set_x,pos1,":x_pos"),
             (position_set_y,pos1,":y_pos"),
             (position_set_z,pos1,10000),
             (position_set_z_to_ground_level,pos1),
                     (agent_set_scripted_destination,"$leading_boar",pos1),
      ]),
      (1,0,0,[],
      [
      (try_for_agents,reg(1)),
    (agent_get_item_id,reg(2),reg(1)),
    (eq,reg(2),"itm_boar"),
    (store_agent_hit_points,":health",reg(1)),
    (store_sub,":damage",100,":health"),
    (agent_get_slot,":prev_damage",reg(1),1),
    (neq,":prev_damage",":damage"),
    (agent_set_slot,reg(1),1,":damage"),
        (agent_get_position,pos1,reg(1)),
        (position_get_x,":x_pos",pos1),
    (position_get_y,":y_pos",pos1),
        (store_random_in_range,":x_pos_add",0,1000),
        (store_random_in_range,":y_pos_add",0,1000),
    (val_add,":x_pos",":x_pos_add"),
    (val_add,":y_pos",":y_pos_add"),
    (position_set_x,pos1,":x_pos"),
    (position_set_y,pos1,":y_pos"),
        (agent_set_scripted_destination,reg(1),pos1),
      (try_end),
      ]),
      (0.5,0,0, #boar travelling
      [],
      [
      (get_player_agent_no,reg(1)),
      (agent_get_position,pos1,reg(1)),
      (agent_get_position,pos4,"$leading_boar"),
      (position_get_x,":x_pos",pos4),
      (position_get_y,":y_pos",pos4),
      (try_for_agents,reg(1)),
    (agent_get_item_id,reg(2),reg(1)),
    (eq,reg(2),"itm_boar"),
        (agent_get_position,pos2,reg(1)),
    (get_distance_between_positions,reg(3),pos1,pos2),
    (try_begin),
            (position_get_x,":pos_x",pos2),
            (position_get_x,":pos_y",pos2),
             (position_get_x, ":scene_min_x", pos10),
                     (position_get_x, ":scene_max_x", pos11),
                     (position_get_y, ":scene_min_y", pos10),
                     (position_get_y, ":scene_max_y", pos11),
             (store_div,":border_x",":scene_max_x",10),
             (val_add,":scene_min_x",":border_x"),
             (val_sub,":scene_max_x",":border_x"),
             (store_div,":border_y",":scene_max_y",10),
             (val_add,":scene_min_y",":border_y"),
             (val_sub,":scene_max_y",":border_y"),
        (this_or_next|gt,":pos_x",":scene_max_x"),
        (this_or_next|lt,":pos_x",":scene_min_x"),
        (this_or_next|gt,":pos_y",":scene_max_y"),
        (lt,":pos_y",":scene_min_y"),
        (store_random_in_range,":x_pos",":scene_min_x",":scene_max_x"),
        (store_random_in_range,":y_pos",":scene_min_y",":scene_max_y"),
                (init_position, pos1),
        (position_set_x,pos1,":x_pos"),
        (position_set_y,pos1,":y_pos"),
        (position_set_z,pos1,10000),
        (position_set_z_to_ground_level,pos1),
                (agent_set_scripted_destination,reg(1),pos1),
    (else_try),
        (le,reg(3),2500),
        (position_get_x,reg(4),pos1),
        (position_get_x,reg(5),pos2),
        (store_sub,":x_dist",reg(5),reg(4)),
        (val_mul,":x_dist",10),
        (position_get_y,reg(6),pos1),
        (position_get_y,reg(7),pos2),
        (store_sub,":y_dist",reg(7),reg(6)),
        (val_mul,":y_dist",10),
        (init_position,pos3),
        (val_add,":x_dist",reg(5)),
        (val_add,":y_dist",reg(7)),
        (position_set_x,pos3,":x_dist"),
        (position_set_y,pos3,":y_dist"),
            (position_set_z,pos3,10000),
            (position_set_z_to_ground_level,pos3),
        (agent_set_scripted_destination,reg(1),pos3),
    (else_try),
        (get_distance_between_positions,reg(3),pos4,pos2),
        (ge,reg(3),2000),
                       (init_position, pos6),
               (store_random_in_range,":x_pos_add",0,1000),
               (store_random_in_range,":y_pos_add",0,1000),
               (val_add,":x_pos_add",":x_pos"),
               (val_add,":y_pos_add",":y_pos"),
               (position_set_x,pos6,":x_pos_add"),
               (position_set_y,pos6,":y_pos_add"),
               (position_set_z,pos6,10000),
               (position_set_z_to_ground_level,pos6),
               (agent_set_scripted_destination,reg(1),pos6),
    (try_end),
      (try_end),
      ]),
    ]),
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#Hunting Mod end#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
