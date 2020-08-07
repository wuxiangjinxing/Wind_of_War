common_shua_huojianpao_fashe = (
    0.125, 0, 0,[
        # (neg|game_key_is_down,gk_attack),
        ],[
          (set_fixed_point_multiplier, 100),
    (try_for_prop_instances,":cannonball_type", "spr_mm_rocket_code_only"),
        (scene_prop_get_slot,":ball_instance_id",":cannonball_type", scene_prop_slot_huojianpao),
    (prop_instance_get_position, pos33, ":ball_instance_id"),
        # (position_rotate_z, pos33, 90),
        (position_get_z, ":ball_z",pos33),
        (scene_prop_get_slot,":in_use",":ball_instance_id", scene_prop_slot_in_use),
        (eq,":in_use",1),
        (scene_prop_get_slot,":time",":ball_instance_id",slot_huojianpao_prop),
        
        #############feixinggaodu
                (copy_position,pos35,pos33),
        (copy_position,pos34,pos33),
        (position_set_z_to_ground_level,pos34),
        (position_get_z,":ground_z",pos34),
        # (val_add, ":ground_z", 10), 
        ##############
        (scene_prop_get_slot,":move",":cannonball_type", scene_prop_slot_huojianfashe),
        (eq,":move",1),
        
        (scene_prop_get_slot,":cur_x_vel",":ball_instance_id", scene_prop_slot_x_value),
    (scene_prop_get_slot,":cur_y_vel",":ball_instance_id", scene_prop_slot_y_value),
    (scene_prop_get_slot,":cur_z_vel",":ball_instance_id", scene_prop_slot_z_value),

#################wulixiaoguo######################
                (try_begin),
          (eq,":move",1),
          (set_fixed_point_multiplier, 100),

          (position_get_x,":ball_x",pos33),
          (position_get_y,":ball_y",pos33),

          (try_begin),
            (this_or_next|lt,":ball_x","$g_scene_min_x"),
            (this_or_next|gt,":ball_x","$g_scene_max_x"),
            (this_or_next|lt,":ball_y","$g_scene_min_y"),
            (gt,":ball_y","$g_scene_max_y"),

            (call_script, "script_clean_up_prop_instance", ":ball_instance_id"),
            # (assign,":time",-1),
            (assign,":move",0),
            (assign,":check_walls",0),
            (assign,":check_agents",0),
          (else_try),
            # Animate first

            (assign,reg29,":cur_x_vel"),
            (assign,reg30,":cur_z_vel"),
            (assign,reg31,":cur_y_vel"),
                         (assign,reg32,":time"),


            (position_move_x,pos33,":cur_x_vel"),
            (position_move_y,pos33,":cur_y_vel"),
            (position_move_z,pos33,":cur_z_vel"),

            (try_begin),
              # (eq,":ammo_type",cannon_ammo_type_rocket),
              (try_begin),
                (ge,":time", 0),
                (store_random_in_range,":rand_z",-4,4),
                (position_rotate_z,pos33,":rand_z"),
                (store_random_in_range,":rand_y",-1,5),
                (position_rotate_y,pos33,":rand_y"),
                                (store_random_in_range,":rand_x",-1,1),
                (position_rotate_x,pos33,":rand_x"),
              (try_end),
              (prop_instance_animate_to_position, ":ball_instance_id", pos33, 25),
                          # (particle_system_burst,"psys_rocket_smoke",pos33,8),
            (else_try),
              (prop_instance_animate_to_position, ":ball_instance_id", pos33, 40),
                          # (particle_system_burst,"psys_rocket_smoke",pos33,8),
            (try_end),
              (try_begin),
              # (eq,":ammo_type",cannon_ammo_type_rocket),
              (try_begin),
                (le,":time", 280),
                (val_add, ":cur_x_vel", 150),
              (else_try),
                (val_mul, ":cur_x_vel", 99), 
                (val_div, ":cur_x_vel", 100), # value * 99 / 100 = - 99% of speed due to friction per 0.5 sec so 2% friction per second
              (try_end),
              (try_begin),
                (gt,":time",0),
                (val_sub,":cur_z_vel", 59), 
              (try_end),
            (else_try),
              # Then apply gravity and friction
              ## -196 cm per second so # 0.981 per half
              (val_sub,":cur_z_vel", 118), 
              (val_max,":cur_z_vel",-1700),
              (val_mul, ":cur_x_vel", 99), 
              (val_div, ":cur_x_vel", 100), # value * 99 / 100 = - 99% of speed due to friction per 0.5 sec so 2% friction per second
            (try_end),
            (try_begin),
                         (le,":ball_z", ":ground_z"),
                        (assign,":cur_x_vel",0),
            (assign,":cur_z_vel",0),
            (assign,":cur_y_vel",0),
                        (scene_prop_set_slot,":ball_instance_id",scene_prop_slot_in_use,0),
                        (else_try),
                        (gt,":time", 290),
                        (val_sub,":cur_z_vel",120),
                        # (scene_prop_set_slot,":ball_instance_id",scene_prop_slot_in_use,0),
                        (else_try),
                        (gt,":time", 280),
                        (scene_prop_set_slot,":ball_instance_id",scene_prop_slot_in_use,0),
                        (try_end),
            (scene_prop_set_slot,":ball_instance_id", scene_prop_slot_x_value, ":cur_x_vel"),
            (scene_prop_set_slot,":ball_instance_id", scene_prop_slot_y_value, ":cur_y_vel"),
            (scene_prop_set_slot,":ball_instance_id", scene_prop_slot_z_value, ":cur_z_vel"),
                        
          (try_end),
        (try_end),
        (try_end),        
                                         
        ]
        )