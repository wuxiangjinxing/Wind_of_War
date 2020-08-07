qstr_While_working_in_the|当 在 矿 井 工 作 时，你 发 现 了 一 处 新 的 盐 矿 床 并 且 因 此 发 现 受 到 奖 赏。
qstr_While_working_in_the_|当 在 矿 井 工 作 时，你 发 现 了 一 处 铁 矿 床 并 且 因 此 发 现 受 到 奖 赏。
qstr_While_working_in_the_m|当 在 矿 井 工 作 时，你 发 现 了 一 处 银 矿 床 并 且 因 此 发 现 受 到 奖 赏。
qstr_While_working_in_the_mi|当 在 矿 井 工 作 时，你 发 现 了 一 处 金 矿 床 并 且 因 此 发 现 受 到 奖 赏。
qstr_While_working_in_the_min|当 在 矿 井 工 作 时，你 发 现 了 一 处 稀 矿 矿 床 并 且 因 此 发 现 受 到 奖 赏。
qstr_While_working_in_the_mine|当 在 矿 井 工 作 时，你 在 一 次 小 型 塌 方 中 受 了 伤。
qstr_While_working_in_the_mine_|当 在 矿 井 工 作 时，你 在 一 次 塌 方 中 受 了 伤。
qstr_While_working_in_the_mine_y|当 在 矿 井 工 作 时，你 在 一 次 塌 方 中 差 点 丧 了 命。
qstr_While_working_in_the_mine_yo|当 在 矿 井 工 作 时，你 的 部 队 在 塌 方 中 受 了 伤。
qstr_While_working_in_the_mine_a|当 在 矿 井 工 作 时，一 次 塌 方 给 你 的 部 队 带 来 了 重 创。 

qstr___{reg1}_scillingas_| ({reg1} 先 令 每 天)
qstr_You_are_in_no_condit|你 现 在 的 情 形 没 法 工 作。
qstr_You_are_paid_for_you| 你 付 出 了 劳 动
qstr___Currently_{reg1}_p| (当 前 有 {reg1} 俘 虏 在 工 作)
qstr___Currently_{reg1}_g| (当 前 有 {reg1}名 守 卫 在 执 勤)
qstr_Some_of_the_prisoner|一 些 在 在 盐 矿 工 作 的 俘 虏 逃 跑 了^剩 下 的 俘 虏 这 周 为 你 挣 得 了 {reg1} 先 令。
qstr_The_prisoners_you_ha|在 盐 矿 工 作 的俘 虏 这 周 为 你 挣 得 了 {reg1} 先 令。

menu_salt_mine|你 进 入 了 盐 矿。 
mno_enter|进 入。 
mno_enter_door|退 出 营 帐
mno_talk_merchant|与 盐 矿 商 人 交 谈
mno_talk_merchant_door|退 出 营 帐.
mno_work_mines|志 愿 在 盐 矿 工 作 {s1}.
mno_add_prisoners|把 俘 虏 送 到 盐 矿 工 作{s1}.
mno_add_guards|配 置 守 卫 来 监 督 俘 虏{s1}.
menu_slave_labor|{s1}


 (
    "salt_mine",mnf_enable_hot_keys,
    "You arrive at a small mining camp.",
    "none",
    [(reset_price_rates,0),(set_price_rate_for_item,"itm_salt",55)],
    [
      ("enter",[],"Approach the camp.",[(set_jump_mission,"mt_town_center"),(jump_to_scene,"scn_salt_mine"),(change_screen_mission)]),
      ("talk_merchant",[]
          ,"Talk to the Mine Merchant.",
          [
              (assign, "$talk_context", 0),
           (assign, ":override_state", af_override_horse),
              (mission_tpl_entry_set_override_flags, "mt_town_center", 0, ":override_state"),
              (mission_tpl_entry_set_override_flags, "mt_town_center", 2, ":override_state"),
              (mission_tpl_entry_set_override_flags, "mt_town_center", 3, ":override_state"),
              (mission_tpl_entry_set_override_flags, "mt_town_center", 4, ":override_state"),
              (mission_tpl_entry_set_override_flags, "mt_town_center", 5, ":override_state"),
              (mission_tpl_entry_set_override_flags, "mt_town_center", 6, ":override_state"),
              (mission_tpl_entry_set_override_flags, "mt_town_center", 7, ":override_state"),
              (jump_to_scene, "scn_salt_mine"),
              (change_screen_map_conversation, "trp_salt_mine_merchant"),
           ],"Exit to the camp."),
      ("work_mines",
       [
           (store_troop_health, "$g_player_health","trp_player", 1),
         (str_clear, s1),
           (party_get_num_companions, ":num_men", "p_main_party"),
           (store_mul, reg1, ":num_men", 4),
           (val_add, reg1, 1),
           (str_store_string, s1, "@ ({reg1} denars per day)"),
        ],
         "Volunteer to work in the mines{s1}.",
         [
           (try_begin),
           (neg|gt, "$g_player_health", 20),
          (display_message, "@You are in no condition to work."),
          (jump_to_menu,"mnu_salt_mine"),
         (else_try),
           (assign, "$g_is_working", 1),
           (assign, "$g_last_rest_payment_until", -1),
             (rest_for_hours_interactive, 24, 5, 1), #rest while attackable
             (change_screen_return),
         (try_end),
          ]),
          
      ("add_prisoners",
       [
         (str_clear, s1),
         (party_get_num_prisoners, "$g_num_prisoners", "p_salt_mine"),
         (assign, reg1, "$g_num_prisoners"),
           (str_store_string, s1, "@ (Currently {reg1} prisoners working)"),
        ],
         "Put prisoners to work in the mines{s1}.",
         [
           (change_screen_exchange_members, 0),
          ]),
          
      ("add_guards",
       [
         (str_clear, s1),
         (party_get_num_companions, "$g_num_guards", "p_salt_mine"),
         (assign, reg1, "$g_num_guards"),
           (str_store_string, s1, "@ (Currently {reg1} guards on duty)"),
        ],
         "Station guards to watch over prisoners{s1}.",
         [
           (change_screen_exchange_members, 0),
          ]),
      ("leave",[],"Leave.",[(leave_encounter),(change_screen_return)]),
    ]
  ),

  (
    "slave_labor",mnf_disable_all_keys,
    "{s1}",
    "none",
    [
          (str_clear, s1),
        (assign, reg1, "$g_earnings"),
          (troop_add_gold, "trp_player", "$g_earnings"),
        (try_begin),
          (gt, "$g_num_escapees", 0),
         (str_store_string, s1, "@Some of the prisoners you have working in the mine managed to escape.^The remaining prisoners earned you {reg1} denars this week."),
        (else_try),
          (str_store_string, s1, "@The prisoners you have working in the mine earned you {reg1} denars this week."),
        (try_end),
      ],
    [
      ("continue",[], "Continue...",
       [
           (change_screen_return),
        ]),
    ],
  ),

In module_simple_triggers:
 (click to show/hide)
  # Pay denars to player while working in mines
  (1,
   [(try_begin),
      (eq, "$g_is_working", 1),
      (neg|map_free),
      (is_currently_night),
      (store_current_hours, ":cur_hours"),
      (ge, ":cur_hours", "$g_last_rest_payment_until"),
      (store_add, "$g_last_rest_payment_until", ":cur_hours", 24),
      (party_get_num_companions, ":num_men", "p_main_party"),
      (store_mul, ":total_pay", ":num_men", 4),
      (val_add, ":total_pay", 1),
      (display_message, "@You are paid for your labor."),
      (troop_add_gold, "trp_player", ":total_pay"),
     (call_script, "script_mine_work"),
     (assign, "$g_is_working", 0),
   (try_end),
    ]),

# Pay slave labor earnings and check for prisoners escaping
   (24 * 7,
   [
    (try_begin),
     (gt, "$g_num_prisoners", 0),
     (assign, "$g_earnings", 0),
     (assign, "$g_num_escapees", 0),
      (try_for_range, ":center_no", "p_salt_mine", "p_test_scene"),
       (party_get_num_companions,"$g_num_guards",":center_no"),
       (party_get_num_prisoners, "$g_num_prisoners", ":center_no"),
        (store_sub, ":difference", "$g_num_prisoners", "$g_num_guards"),
      (try_begin),
        (gt, ":difference", 0),
        (store_random_in_range, ":random", 0, ":difference"),
        (try_begin),
          (gt, ":random", 5),
         (store_random_in_range, ":escapees", 0, ":difference"),
         (try_begin),
           (eq, ":escapees", 0),
           (assign, ":escapees", 1),
         (try_end),
         (assign, "$g_num_escapees", ":escapees"),
            (party_get_num_prisoner_stacks, ":num_stacks", ":center_no"),
            (try_for_range_backwards, ":troop_iterator", 0, ":num_stacks"),
              (party_prisoner_stack_get_troop_id, ":cur_troop_id", ":center_no", ":troop_iterator"),
              (party_prisoner_stack_get_size, ":stack_size", ":center_no", ":troop_iterator"),
           (try_begin),
             (gt, ":escapees", 0),
             (try_begin),
               (gt, ":stack_size", ":escapees"),
                  (store_sub, ":stack_sub", ":stack_size", ":escapees"),
              (val_sub, ":escapees", ":stack_sub"),
              (party_remove_prisoners, ":center_no", ":cur_troop_id", ":stack_sub"),
            (try_end),
           (try_end),
            (try_end),
        (try_end),
      (try_end),
      (party_get_num_prisoners, "$g_num_prisoners", ":center_no"),
      (store_mul, ":earnings", 10, "$g_num_prisoners"),
        (val_add, "$g_earnings", ":earnings"),
      (jump_to_menu,"mnu_slave_labor"),
      (try_end),
    (try_end),
    ]),

In module_scripts:
 (click to show/hide)
# Working in the mines
  ("mine_work",
   [(assign, ":party_no", "p_main_party"),
    (party_get_num_companion_stacks, ":num_stacks", ":party_no"),
    (store_random_in_range, ":random", 0, 10),
    (try_begin),
      (le, ":random", 3),
     (troop_set_health, "trp_player", 80),
   (else_try),
     (eq, ":random", 4),
     (troop_set_health, "trp_player", 70),
     (store_random_in_range, ":random_gold", 0, 10),
     (try_begin),
       (le, ":random_gold", 5),
      (display_message, "@While working in the mine, you found a new salt deposit and are rewarded for the discovery."),
      (store_random_in_range, ":random_amount", 10, 100),
      (troop_add_gold, "trp_player", ":random_amount"),
     (else_try),
       (eq, ":random_gold", 6),
      (display_message, "@While working in the mine, you found an iron deposit and are rewarded for the discovery."),
      (store_random_in_range, ":random_amount", 50, 200),
      (troop_add_gold, "trp_player", ":random_amount"),
     (else_try),
       (eq, ":random_gold", 7),
      (display_message, "@While working in the mine, you found a silver deposit and are rewarded for the discovery."),
      (store_random_in_range, ":random_amount", 75, 300),
      (troop_add_gold, "trp_player", ":random_amount"),
     (else_try),
       (eq, ":random_gold", 8 ),
      (display_message, "@While working in the mine, you found a gold deposit and are rewarded for the discovery."),
      (store_random_in_range, ":random_amount", 100, 400),
      (troop_add_gold, "trp_player", ":random_amount"),
     (else_try),
       (eq, ":random_gold", 9),
      (display_message, "@While working in the mine, you found a deposit of rare minerals and are rewarded for the discovery."),
      (store_random_in_range, ":random_amount", 150, 500),
      (troop_add_gold, "trp_player", ":random_amount"),
     (try_end),
   (else_try),
     (eq, ":random", 5),
     (troop_set_health, "trp_player", 50),
     (display_message, "@While working in the mine, you were injured during a minor cave-in."),
   (else_try),
     (eq, ":random", 6),
     (troop_set_health, "trp_player", 30),
     (display_message, "@While working in the mine, you were hurt during a cave-in."),
   (else_try),
     (eq, ":random", 7),
     (troop_set_health, "trp_player", 1),
     (display_message, "@While working in the mine, you were nearly killed during a cave-in."),
   (else_try),
     (eq, ":random", 8 ),
     (try_begin),
       (gt, ":num_stacks", 0),
       (call_script, "script_party_wound_all_members", ":party_no"),
       (display_message, "@While working in the mine, you and your troops are wounded during a cave-in."),
     (else_try),
       (troop_set_health, "trp_player", 1),
       (display_message, "@While working in the mine, you were nearly killed during a cave-in."),
     (try_end),
   (else_try),
     (eq, ":random", 9),
     (try_begin),
       (gt, ":num_stacks", 0),
       (troop_set_health, "trp_player", 50),
      (store_random_in_range, ":random_deaths", 1, 10),
        (inflict_casualties_to_party_group, ":party_no", ":random_deaths", "p_temp_casualties"),
        (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
      (str_store_string_reg, s8, s0),
      (display_message, "@While working in the mine, a massive cave-in caused your party casualties: {s8}"),
     (else_try),
       (troop_set_health, "trp_player", 1),
       (display_message, "@While working in the mine, you were nearly killed during a cave-in."),
     (try_end),
   (try_end),
  ]),
  
  
  
  

  ["salt_mine_merchant", "Barezan","Barezan",                tf_hero|tf_is_merchant, scn_salt_mine|entry(1),0, fac_commoners,        [ ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c528601ea69b6e46dbdb6],


  ["salt_mine_merchant", "Barezan","Barezan",                tf_hero|tf_is_merchant, scn_salt_mine|entry(1),0, fac_commoners,        [itm_salt, itm_salt, itm_salt, itm_salt, itm_salt, itm_salt, itm_salt, itm_salt, itm_salt, itm_salt, itm_salt, itm_salt, itm_salt],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c528601ea69b6e46dbdb6],


Code: [Select]

Code: [Select]
  ("salt_mine", "Salt Mine", icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(99.66, -80.8),[]),

Explain;
salt_mine = The ID of salt mine.
Salt Mine = The name of salt mine.
icon_village_a = Icon.
pf_is_static = Static.
pf_always_visible = Always visible.
(99.66, -80.8) = Coordinates.

Ok, us village is finish. Save and close file and go to next process.
Now we open module_dialogs.py file and find this;
Code: [Select]
#Goods Merchants

Add after;
Code: [Select]
  #Salt merchant by Porshy.
  [trp_salt_mine_merchant,"start", [], "Hello my {sir/madam}.", "salt_mine_merchant_talk", []],
  [trp_salt_mine_merchant|plyr, "salt_mine_merchant_talk", [], "Hello.", "salt_mine_merchant_talk2", []],
  [trp_salt_mine_merchant,"salt_mine_merchant_talk2", [], "How can i help you?", "salt_mine_merchant_talk3", []],

  #This is trade window.
  [trp_salt_mine_merchant|plyr,"salt_mine_merchant_talk3", [], "I need some salt", "salt_mine_merchant_talk4", []],
  [trp_salt_mine_merchant,"salt_mine_merchant_talk4", [], "Sure, sure... Here, have a look at my stock...", "salt_mine_merchant_talk4_c", [[change_screen_trade]]],
  [trp_salt_mine_merchant,"salt_mine_merchant_talk4_c", [], "Anything else {sir/madam}?", "salt_mine_merchant_talk3", []],

  #This is stupid window :p
  [trp_salt_mine_merchant|plyr,"salt_mine_merchant_talk3", [], "What do you sell here?", "salt_mine_merchant_talk5", []],
  [trp_salt_mine_merchant,"salt_mine_merchant_talk5", [], "We sell only salt here my {sir/madam}.", "salt_mine_merchant_talk6", []],
  [trp_salt_mine_merchant|plyr,"salt_mine_merchant_talk6", [], "Okey.", "salt_mine_merchant_talk6_c", []],
  [trp_salt_mine_merchant,"salt_mine_merchant_talk6_c", [], "Anything else {sir/madam}?", "salt_mine_merchant_talk3", []],

  #This is cancel window :)
  [trp_salt_mine_merchant|plyr,"salt_mine_merchant_talk3", [], "Nothing", "close_window", []],


dlga_start:salt_mine_merchant_talk|Hello my {sir/madam}.
dlga_salt_mine_merchant_talk:salt_mine_merchant_talk2|Hello.
dlga_salt_mine_merchant_talk2:salt_mine_merchant_talk3|How can i help you?
dlga_salt_mine_merchant_talk3:salt_mine_merchant_talk4|I want some salt
dlga_salt_mine_merchant_talk4:salt_mine_merchant_talk4_c|Sure, sure... Here, have a look at my stock...
dlga_salt_mine_merchant_talk4_c:salt_mine_merchant_talk3|Anything else my {sir/madam}?
dlga_salt_mine_merchant_talk3:salt_mine_merchant_talk5|What do you sell here?
dlga_salt_mine_merchant_talk5:salt_mine_merchant_talk6|We sell only salt here my {sir/madam}.
dlga_salt_mine_merchant_talk6:salt_mine_merchant_talk6_c|Okey.
dlga_salt_mine_merchant_talk6_c:salt_mine_merchant_talk3|Anything else my {sir/madam}?
dlga_salt_mine_merchant_talk3:close_window|Nothing.



now, we finish all. Enjoy it :p