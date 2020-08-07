menu_panel_comandante|开 始 战 斗 前 …
mno_choice_1comm|鼓 舞 ： 对 你 的 士 兵 进 行 一 次 鼓 舞 。 
mno_choice_2comm|劝 降 ： 对 你 的 敌 人 进 行 一 次 演 讲 。 
mno_choice_3comm|游 击 ： 派 你 的 人 去 搅 扰 敌 军 的 前 进 。 
mno_choice_4comm|献 祭 ： 杀 死 10个 俘 虏 ，向 众 神 献 祭 。 
mno_choice_5comm|施 法 ： 消 耗 灵 魂 释 放 一 个 强 大 的 法 术 来 削 弱 敌 人 。 
mno_choice_6comm|算 了 。 


  #panel comandante chief
  (
    "panel_comandante",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "Before the battle begins...",
    "none",
    [
      (set_background_mesh, "mesh_pic_post_battle_menu"),
      
    ],
    [
      ("choice_1comm",[
          (eq, "$g_empieza_discurso", 0),
        ],"Impassion your men with a rousing speech.",
        [
          (store_random_in_range, ":rand", 0, 16),
          (party_get_skill_level, ":leadership", "p_main_party", skl_leadership),
          (try_begin),
            (eq, ":rand", 0),
            (ge, ":leadership", 8),
            (jump_to_menu,"mnu_discurso_1"),
          (else_try),
            (eq, ":rand", 1),
            (ge, ":leadership", 4),
            (jump_to_menu,"mnu_discurso_2"),
          (else_try),
            (eq, ":rand", 2),
            (ge, ":leadership", 4),
            (jump_to_menu,"mnu_discurso_3"),
          (else_try),
            (eq, ":rand", 3),
            (ge, ":leadership", 4),
            (jump_to_menu,"mnu_discurso_4"),
          (else_try),
            (eq, ":rand", 4),
            (jump_to_menu,"mnu_discurso_5"),
          (else_try),
            (eq, ":rand", 5),
            (ge, ":leadership", 4),
            (jump_to_menu,"mnu_discurso_6"),
          (else_try),
            (eq, ":rand", 6),
            (jump_to_menu,"mnu_discurso_7"),
          (else_try),
            (eq, ":rand", 7),
            (ge, ":leadership", 4),
            (jump_to_menu,"mnu_discurso_8"),
          (else_try),
            (eq, ":rand", 8),
            (ge, ":leadership", 4),
            (jump_to_menu,"mnu_discurso_9"),
          (else_try),
            (eq, ":rand", 9),
            (ge, ":leadership", 4),
            (jump_to_menu,"mnu_discurso_10"),
          (else_try),
            (eq, ":rand", 10),
            (jump_to_menu,"mnu_discurso_11"),
          (else_try),
            (eq, ":rand", 11),
            (jump_to_menu,"mnu_discurso_12"),
          (else_try),
            (jump_to_menu,"mnu_discurso_off"),
          (try_end),
        ]
      ),
      
      ("choice_2comm",[(eq, "$g_empieza_campeon", 0),
          (party_slot_eq, "$g_enemy_party", slot_party_type, spt_kingdom_hero_party),
        ],"Call your enemy forward for a duel of honour.",
        [
          (store_random_in_range, ":rand", 0, 5),
          (party_get_skill_level, ":leadership", "p_main_party", skl_leadership),
          (try_begin),
            (eq, ":rand", 0),
            (ge, ":leadership", 2),
            (jump_to_menu,"mnu_lucha_1_p"),
          (else_try),
            (eq, ":rand", 1),
            (ge, ":leadership", 2),
            (jump_to_menu,"mnu_lucha_1_d"),
          (else_try),
            (eq, ":rand", 2),
            (ge, ":leadership", 2),
            (jump_to_menu,"mnu_lucha_2_v"),
          (else_try),
            (eq, ":rand", 3),
            (jump_to_menu,"mnu_lucha_2_no"),
          (else_try),
            (jump_to_menu,"mnu_lucha_2_no"),
          (try_end),
        ]
      ),
      
      
      ("choice_3comm",[
          (eq, "$g_empieza_campeon", 0),
          (party_get_skill_level, ":tactics", "p_main_party", skl_tactics),
          (ge, ":tactics", 6),
        ],"Skirmishers: Send your men to hinder the enemy's advance.",
        [
          (assign, ":g_escaramuza_result2", 0),    #MOTO chief rewrite
          (try_begin),
            (troop_is_hero, "$g_talk_troop"),
            
            (party_get_skill_level, ":leadership", "p_main_party",      skl_tactics),
            (store_skill_level, ":leadership2", skl_tactics,      "$g_talk_troop"),
            (store_sub, reg0, ":leadership", ":leadership2"),
            
            (try_begin),
              (lt, reg0, -1),    #AI better than player?
              (assign, ":g_escaramuza_result2", 1),
            (else_try),
              (gt, reg0, 1),    #player better than AI?
              (assign, ":g_escaramuza_result2", 2),
            (try_end),
          (try_end),
          #MOTO rewrite end
          
          (store_random_in_range, ":rand", 0, 3),
          (try_begin),
            (eq, ":rand", 0),
            (eq, ":g_escaramuza_result2", 1),    #MOTO chief rewrite
            (jump_to_menu,"mnu_escaramuza_1"),
          (else_try),
            (eq, ":rand", 1),
            (eq, ":g_escaramuza_result2", 2),    #MOTO rewrite
            (jump_to_menu,"mnu_escaramuza_2"),
          (else_try),
            (eq, ":rand", 2),
            (jump_to_menu,"mnu_escaramuza_2"),
          (else_try),
            (jump_to_menu,"mnu_escaramuza_3"),
          (try_end),
        ]
      ),
      ("choice_4comm",[(le, "$g_empieza_discurso", 0),
          (eq, "$g_player_faith", 2),
        ],"Make a sacrifice to the gods.",
        [
          (store_random_in_range, ":rand", 0, 5),
          (party_get_skill_level, ":leadership", "p_main_party", skl_leadership),
          (try_begin),
            (eq, ":rand", 0),
            (ge, ":leadership", 4),
            (jump_to_menu,"mnu_sacrificio_1"),
          (else_try),
            (eq, ":rand", 1),
            (ge, ":leadership", 4),
            (jump_to_menu,"mnu_sacrificio_2"),
          (else_try),
            (eq, ":rand", 2),
            (ge, ":leadership", 4),
            (jump_to_menu,"mnu_sacrificio_3"),
          (else_try),
            (eq, ":rand", 3),
            (ge, ":leadership", 4),
            (jump_to_menu,"mnu_sacrificio_4"),
          (else_try),
            (jump_to_menu,"mnu_sacrificio_off"),
          (try_end),
        ]
      ),
      ("choice_5comm",[],"Do nothing.",
        [
          (jump_to_menu,"mnu_simple_encounter"),
        ]
      ),
    ]
  ),


  #panel comandante chief
  (
    "order_skirmish",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "Before the battle begins...",
    "none",
    [
      (set_background_mesh, "mesh_pic_post_battle_menu"),
      
    ],
    [

      ("order_skirmish_1",[
          (eq, "$g_empieza_campeon", 0),
          (party_get_skill_level, ":tactics", "p_main_party", skl_tactics),
          (ge, ":tactics", 3),
          (call_script, "script_party_count_troop_power_by_type", "p_main_party", 0),
          (gt, reg2, 10),
        ],"Skirmishers: Send your men to hinder the enemy's advance.",
        [
          (assign, ":g_escaramuza_result2", 0),    #MOTO chief rewrite
          (try_begin),
            (troop_is_hero, "$g_talk_troop"),
            
            (party_get_skill_level, ":lider", "p_main_party", skl_tactics),
            (store_skill_level, ":lider2", skl_tactics, "$g_talk_troop"),
            (store_sub, reg0, ":lider", ":lider2"),
            
            (try_begin),
              (lt, reg0, -1),    #AI better than player?
              (assign, ":g_escaramuza_result2", 1),
            (else_try),
              (gt, reg0, 1),    #player better than AI?
              (assign, ":g_escaramuza_result2", 2),
            (try_end),
          (try_end),
          #MOTO rewrite end
          
          (store_random_in_range, ":rand", 0, 3),
          (try_begin),
            (is_between, ":rand", 1, 3),
            (eq, ":g_escaramuza_result2", 0),    #MOTO rewrite
            (jump_to_menu,"mnu_escaramuza_2"),
          (else_try),
            (eq, ":rand", 0),
            (eq, ":g_escaramuza_result2", 1),    #MOTO chief rewrite
            (jump_to_menu,"mnu_escaramuza_1"),
          (else_try),
            (eq, ":rand", 1),
            (eq, ":g_escaramuza_result2", 2),    #MOTO rewrite
            (jump_to_menu,"mnu_escaramuza_2"),
          (else_try),
            (eq, ":rand", 2),
            (jump_to_menu,"mnu_escaramuza_2"),
          (else_try),
            (jump_to_menu,"mnu_escaramuza_3"),
          (try_end),
        ]
      ),

      ("order_skirmish_2",[
          (eq, "$g_empieza_campeon", 0),
          (party_get_skill_level, ":tactics", "p_main_party", skl_tactics),
          (ge, ":tactics", 3),
        ],"Skirmishers: Send your Horse Archers and Flying soldier to hinder the enemy's advance.",
        [
          (assign, ":g_escaramuza_result2", 0),    #MOTO chief rewrite
          (try_begin),
            (troop_is_hero, "$g_talk_troop"),
            
            (party_get_skill_level, ":lider", "p_main_party",      skl_tactics),
            (store_skill_level, ":lider2", skl_tactics,      "$g_talk_troop"),
            (store_sub, reg0, ":lider", ":lider2"),
            
            (try_begin),
              (lt, reg0, -1),    #AI better than player?
              (assign, ":g_escaramuza_result2", 1),
            (else_try),
              (gt, reg0, 1),    #player better than AI?
              (assign, ":g_escaramuza_result2", 2),
            (try_end),
          (try_end),
          #MOTO rewrite end
          
          (store_random_in_range, ":rand", 0, 3),
          (try_begin),
            (is_between, ":rand", 1, 3),
            (eq, ":g_escaramuza_result2", 0),    #MOTO rewrite
            (jump_to_menu,"mnu_escaramuza_2"),
          (else_try),
            (eq, ":rand", 0),
            (eq, ":g_escaramuza_result2", 1),    #MOTO chief rewrite
            (jump_to_menu,"mnu_escaramuza_1"),
          (else_try),
            (eq, ":rand", 1),
            (eq, ":g_escaramuza_result2", 2),    #MOTO rewrite
            (jump_to_menu,"mnu_escaramuza_2"),
          (else_try),
            (eq, ":rand", 2),
            (jump_to_menu,"mnu_escaramuza_2"),
          (else_try),
            (jump_to_menu,"mnu_escaramuza_3"),
          (try_end),
        ]
      ),



      ("choice_6comm",[],"Do nothing.",
        [
          (jump_to_menu,"mnu_simple_encounter"),
        ]
      ),
    ]
  ),


  ###escaramuza chief
  (
    "escaramuza_1",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "{reg59?Lady:Sir}, the enemy commander overcame your tactical skills. Before we were prepared, we were surprised by enemy missile troops. They caused numerous casualties.^^Your casualties: {s8}",
    "none",
    [
      (set_background_mesh, "mesh_pic_charge"),
      (call_script, "script_inflict_casualties_to_party", "p_main_party", 2),
      (call_script, "script_collect_friendly_parties"),
    ],
    [
      ("defendiendo_1e",[],"Damn!",
        [
          (assign, "$g_empieza_campeon", 1),
          (jump_to_menu,"mnu_simple_encounter"),
        ]
      ),
    ]
  ),
  (
    "escaramuza_2",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "Our men were deployed in time and closed with the enemy, causing them heavy casualties, before returning.^^Enemy casualties: {s8}",
    "none",
    [
      (set_background_mesh, "mesh_pic_charge"),
      (call_script, "script_inflict_casualties_to_party", "$g_enemy_party", 2),
      (party_collect_attachments_to_party, "$g_enemy_party", "p_collective_enemy"),
    ],
    [
      ("defendiendo_2e",[],"Well done.",
        [
          (assign, "$g_empieza_campeon", 1),
          (jump_to_menu,"mnu_simple_encounter"),
        ]
      ),
    ]
  ),
  (
    "escaramuza_3",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "Upon approaching the enemy, our men found the enemy commander had deployed missile troops to protect his army's advance. To avoid losing men, your soldiers did not attack and returned.",
    "none",
    [(set_background_mesh, "mesh_pic_charge"),
    ],
    [
      ("defendiendo_3e",[],"Right.",
        [
          (assign, "$g_empieza_campeon", 1),
          (jump_to_menu,"mnu_simple_encounter"),
        ]
      ),
    ]
  ),
  
