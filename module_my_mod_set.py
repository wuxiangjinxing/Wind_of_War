from header_operations import *
from ID_items import *
from ID_troops import *
from ID_strings import *
from module_constants import *
from module_items import *
from header_item_modifiers import *

###################################################
# module_my_mod_set.py
# This file contains many defines of my own mod.
###################################################

def get_hrd_weight(y):
  a = (y >> ibf_weight_bits) & ibf_armor_mask
  return int(25 * a)

def set_item_score():
  item_score = []
  for i_item in xrange(len(items)):
    ## armor type
    if items[i_item][7] == imodbits_cloth:
      item_score.append((item_set_slot, i_item, slot_armor_type, armor_cloth))
    elif items[i_item][7] == imodbits_armor:
      item_score.append((item_set_slot, i_item, slot_armor_type, armor_armor))
    elif items[i_item][7] == imodbits_plate:
      item_score.append((item_set_slot, i_item, slot_armor_type, armor_plate))
    
  ## item_modifier
  for i_modifier in xrange(len(modifiers)):
    item_score.append((item_set_slot, i_modifier, slot_item_modifier_multiplier, modifiers[i_modifier][1]))
    item_score.append((item_set_slot, i_modifier, slot_item_modifier_quality, modifiers[i_modifier][2]))
    
  return item_score[:]

modifiers = [
  (imod_plain, 100, 0), 
  (imod_cracked, 50, -1), 
  (imod_rusty, 55, -1), 
  (imod_bent, 65, -1), 
  (imod_chipped, 72, -1), 
  (imod_battered, 75, -1), 
  (imod_poor, 80, -1), 
  (imod_crude, 83, -1), 
  (imod_old, 86, -1), 
  (imod_cheap, 50, -1), 
  
  (imod_fine, 190, 1), 
  (imod_well_made, 400, 1), 
  (imod_sharp, 160, 1), 
  (imod_balanced, 350, 1), 
  (imod_tempered, 350, 1), 
  (imod_deadly, 500, 1), 
  (imod_exquisite, 750, 1), 
  (imod_masterwork, 870, 1), 
  
  (imod_heavy, 190, 1), 
  (imod_strong, 400, 1), 
  (imod_powerful, 350, 1), 
  
  (imod_tattered, 50, -1), 
  (imod_ragged, 70, -1), 
  (imod_rough, 60, -1), 
  (imod_sturdy, 170, 1), 
  
  (imod_thick, 260, 1), 
  (imod_hardened, 400, 1), 
  (imod_reinforced, 600, 1), 
  (imod_superb, 600, 1), 
  (imod_lordly, 1000, 1), 
  
  (imod_lame, 40, -1), 
  (imod_swaybacked, 60, -1), 
  (imod_stubborn, 90, 1), 
  (imod_timid, 150, 1), 
  (imod_meek, 150, -1), 
  
  (imod_spirited, 400, 1), 
  (imod_champion, 800, 1), 
  
  (imod_fresh, 100, 1), 
  (imod_day_old, 100, -1), 
  (imod_two_day_old, 90, -1), 
  (imod_smelling, 40, -1), 
  (imod_rotten, 5, -1), 
  (imod_large_bag, 190, 1)
]

def keys_array():
  keys_list = []
  for key_no in xrange(len(keys)):
    keys_list.append((troop_set_slot, "trp_temp_array_a", key_no, keys[key_no]))
    keys_list.append((troop_set_slot, "trp_temp_array_b", key_no, str_key_0+key_no))
  return keys_list[:]

keys = [key_0, key_1, key_2, key_3, key_4, key_5, key_6, key_7, key_8, key_9, key_a, key_b, key_c, key_d, key_e, key_f, key_g, key_h, key_i, key_j, key_k, key_l, key_m, key_n, key_o, key_p, key_q, key_r, key_s, key_t, key_u, key_v, key_w, key_x, key_y, key_z, key_numpad_0, key_numpad_1, key_numpad_2, key_numpad_3, key_numpad_4, key_numpad_5, key_numpad_6, key_numpad_7, key_numpad_8, key_numpad_9, key_num_lock, key_numpad_slash, key_numpad_multiply, key_numpad_minus, key_numpad_plus, key_numpad_enter, key_numpad_period, key_insert, key_delete, key_home, key_end, key_page_up, key_page_down, key_up, key_down, key_left, key_right, key_f1, key_f2, key_f3, key_f4, key_f5, key_f6, key_f7, key_f8, key_f9, key_f10, key_f11, key_f12, key_space, key_escape, key_enter, key_tab, key_back_space, key_open_braces, key_close_braces, key_comma, key_period, key_slash, key_back_slash, key_equals, key_minus, key_semicolon, key_apostrophe, key_tilde, key_caps_lock, key_left_shift, key_right_shift, key_left_control, key_right_control, key_left_alt, key_right_alt]

def set_key_config():
   key_config = []
   for i in xrange(len(keys_list)):
      key_config.append((troop_set_slot, key_config_data, slot_default_keys_begin+i, keys_list[i][1]))      
   for i in xrange(len(all_keys_list)):
      key_config.append((troop_set_slot, key_config_data, slot_key_defs_begin+i, all_keys_list[i]))
   return key_config[:]   

# Global Variables -> Slots   
def read_key_config():
   global_key = []
   for i in xrange(len(keys_list)):
      global_key.append((troop_set_slot, key_config_data, slot_keys_begin+i, keys_list[i][0]))      
   return global_key[:]   
   
# Slots -> Global Variables   
def write_key_config():
   global_key = []
   for i in xrange(len(keys_list)):
      global_key.append((troop_get_slot, keys_list[i][0], key_config_data, slot_keys_begin+i))      
   return global_key[:]      
#-- Dunde's Key Config END

def set_commensalism_troops():
  result_list = []
  for row_no in xrange(len(commensalism_troops)):
    if len(commensalism_troops[row_no]) == 3:
      result_list.append((troop_set_slot, commensalism_troops[row_no][0], slot_troop_commensalism_troop, commensalism_troops[row_no][2]))
      result_list.append((troop_set_slot, commensalism_troops[row_no][1], slot_troop_commensalism_troop, commensalism_troops[row_no][2]))
    else:
      result_list.append((troop_set_slot, commensalism_troops[row_no][0], slot_troop_commensalism_troop, commensalism_troops[row_no][1]))
      result_list.append((troop_set_slot, commensalism_troops[row_no][1], slot_troop_commensalism_troop, commensalism_troops[row_no][0]))
  return result_list[:]

commensalism_troops = [
  #("trp_black_khergit_guard", "trp_black_khergit_raidmaster"),
  #("trp_sea_raider_viking", "trp_norman_cavalry"),
  #("trp_camel_cavalry", "trp_camel_mamluke"),
  #("trp_sea_raider_veteran", "trp_sea_raider_captain"),
  #("trp_forest_brigand", "trp_forest_bandit_leader"),
  #("trp_taiga_brigand", "trp_taiga_bandit_leader"),
  #("trp_mountain_bandit", "trp_mountain_bandit_leader"),

  #("trp_forest_hunter", "trp_sherwood_archer"),
  #("trp_sarranid_horseman", "trp_sarranid_mamluke"),
]

def set_magic_type():
  result_list = []
  for row_no in xrange(len(magic_type)):
    result_list.append((item_set_slot, magic_type[row_no][0], slot_item_magic_cost,   magic_type[row_no][1]))
    result_list.append((item_set_slot, magic_type[row_no][0], slot_item_magic_type,   magic_type[row_no][2]))
    result_list.append((item_set_slot, magic_type[row_no][0], slot_item_magic_cooldown,   magic_type[row_no][3]))
    result_list.append((item_set_slot, magic_type[row_no][0], slot_item_magic_difficulty,   magic_type[row_no][4]))
    result_list.append((item_set_slot, magic_type[row_no][0], slot_item_is_magic_spell,   magic_type[row_no][5]))
  return result_list[:]

magic_type = [
  ("itm_voice_clear_skies", 0, voice, 10, 0, 1),
  ("itm_voice_cyclone", 0, voice, 30, 0, 1),
  ("itm_voice_unrelenting_force", 0, voice, 20, 0, 1),
  ("itm_voice_become_ethereal", 0, voice, 16, 0, 1),
  ("itm_voice_slow_time", 0, voice, 25, 0, 1),
  ("itm_voice_animal_allegiance", 0, voice, 45, 0, 1),
  ("itm_voice_storm_call", 0, voice, 60, 0, 1),
  ("itm_voice_call_dragon", 0, voice, 60, 0, 1),
  ("itm_voice_call_of_valor", 0, voice, 60, 0, 1),
  ("itm_voice_disarm", 0, voice, 25, 0, 1),
  ("itm_voice_dismaying_shout", 0, voice, 40, 0, 1),
  ("itm_voice_bend_will", 0, voice, 60, 0, 1),
  ("itm_voice_fire_breath", 0, voice, 20, 0, 1),
  ("itm_voice_whirlwind_sprint", 0, voice, 10, 0, 1),
  ("itm_voice_frost_breath", 0, voice, 30, 0, 1),
  ("itm_voice_ice_form", 0, voice, 20, 0, 1),
  ("itm_voice_marked_for_death", 0, voice, 15, 0, 1),
  ("itm_voice_soul_tear", 0, voice, 25, 0, 1),
  ("itm_voice_drain_vitality", 0, voice, 20, 0, 1),

  ("itm_magic_ice_ray", 15, quick_spell, 0, 0, 1),
  ("itm_magic_curse", 10, quick_spell, 0, 0, 1),
  ("itm_magic_slow", 10, quick_spell, 0, 0, 1),
  ("itm_magic_weakness", 25, quick_spell, 0, 0, 1),
  ("itm_magic_poison", 10, quick_spell, 0, 0, 1),
  ("itm_magic_heal", 5, quick_spell, 0, 0, 1),
  ("itm_magic_sun_ray", 10, quick_spell, 0, 0, 1),
  ("itm_magic_heaven_fist_dummy", 10, quick_spell, 0, 0, 1),
  ("itm_magic_poison_dummy", 10, quick_spell, 0, 0, 1),
  
  ("itm_magic_arrow", 0, quick_spell, 0, 0, 1),
  ("itm_magic_shrapmetal", 0, quick_spell, 0, 0, 1),
  ("itm_magic_ice_ray_dummy", 1, quick_spell, 0, 0, 1),
  ("itm_magic_sun_ray_dummy", 1, quick_spell, 0, 0, 1),
  ("itm_magic_fire_ray_dummy", 1, quick_spell, 0, 0, 1),
  
  ("itm_magic_flamehand", 0, quick_spell, 0, 0, 1),
  ("itm_magic_icehand", 0, quick_spell, 0, 0, 1),
  ("itm_magic_spark", 10, quick_spell, 0, 0, 1),
  
  
  ("itm_magic_summon_neutral_near_ememy", 33, spell, 0, 0, 1),
  ("itm_magic_summon_demon", 50, spell, 0, 0, 1),
  ("itm_magic_summon_demon_near_ememy", 50, spell, 0, 0, 1),
  ("itm_magic_summon_undead", 33, spell, 0, 0, 1),
  ("itm_magic_summon_undead_near_ememy", 33, spell, 0, 0, 1),
  ("itm_magic_soulhunter", 0, spell, 0, 0, 1),
  ("itm_magic_zombie_lord", 0, spell, 0, 0, 1),
  
  ("itm_magic_death_cloud_dummy", 15, spell, 0, 0, 1),
  ("itm_magic_death_cloud", 0, spell, 0, 0, 1),
  
  ("itm_magic_deep_freeze", 30, spell, 0, 0, 1),
  ("itm_magic_arcane_orb", 40, spell, 0, 0, 1),
  ("itm_magic_fireball", 25, spell, 0, 0, 1),



  ("itm_magic_soul_leech", 25, spell, 0, 0, 1),
  ("itm_magic_frost_cloud", 0, spell, 0, 0, 1),
  ("itm_magic_frost_cloud_dummy", 15, spell, 0, 0, 1),
  ("itm_magic_deadly_cold", 40, spell, 0, 0, 1),
  ("itm_magic_frozen_orb", 25, spell, 0, 0, 1),
  ("itm_magic_blizzard", 0, spell, 0, 0, 1),
  ("itm_magic_paralysis_cloud", 30, spell, 0, 0, 1),
  
  ("itm_magic_entangling", 25, spell, 0, 0, 1),
  ("itm_magic_web", 25, spell, 0, 0, 1),
  ("itm_magic_dispel_magic", 25, spell, 0, 0, 1),
  ("itm_magic_lightning", 10, spell, 0, 0, 1),
  ("itm_magic_black_hold", 25, spell, 0, 0, 1),
  ("itm_magic_black_hold_2", 25, spell, 0, 0, 1),
  ("itm_magic_lightning_burst", 25, spell, 0, 0, 1),
  ("itm_magic_lightningball", 25, spell, 0, 0, 1),
  
  ("itm_magic_lightningball", 0, spell, 0, 0, 1),
  ("itm_magic_summon_blade", 0, spell, 0, 0, 1),
  ("itm_magic_fireball_2", 30, spell, 0, 0, 1),
  ("itm_magic_pyroblast", 33, spell, 0, 0, 1),
  ("itm_magic_dragon_breath", 0, spell, 0, 0, 1),
  
  ("itm_magic_meteor_shower", 0, spell, 0, 0, 1),
  ("itm_magic_meteor_shower_dummy", 0, spell, 0, 0, 1),
  
  ("itm_magic_incediary_cloud", 0, spell, 0, 0, 1),
  ("itm_magic_incediary_cloud_dummy", 20, spell, 0, 0, 1),
  
  ("itm_magic_heaven_fist", 0, spell, 0, 0, 1),
  ("itm_magic_column_of_fire", 0, spell, 0, 0, 1),
  
  ("itm_magic_armageddon", 0, spell, 0, 0, 1),
  ("itm_magic_armageddon_dummy", 0, spell, 0, 0, 1),

  ("itm_magic_teleport", 15, spell, 0, 0, 1),
  
  
  

  ("itm_skill_inspire", 0, special_ability, 0, 0, 1),
  ("itm_skill_warcry", 0, special_ability, 0, 0, 1),
  ("itm_skill_taunt", 0, special_ability, 0, 0, 1),
  ("itm_skill_battlecry", 0, special_ability, 0, 0, 1),
  ("itm_skill_fright_aura", 0, special_ability, 0, 0, 1),
  ("itm_skill_bloodlust", 0, special_ability, 0, 0, 1),
  ("itm_skill_call_storm", 0, special_ability, 0, 0, 1),
  ("itm_skill_summon_neutral", 0, special_ability, 0, 0, 1),
  ("itm_skill_summon_demon", 0, special_ability, 0, 0, 1),
  ("itm_skill_summon_hallow", 0, special_ability, 0, 0, 1),
  ("itm_skill_dive", 0, special_ability, 0, 0, 1),
  ("itm_skill_mummy_curse", 0, special_ability, 0, 0, 1),
  ("itm_skill_shadowking", 0, special_ability, 0, 0, 1),
  ("itm_skill_divine_strength", 0, special_ability, 0, 0, 1),
  ("itm_skill_regeneration", 0, special_ability, 0, 0, 1),
  ("itm_skill_stoneskin", 0, special_ability, 0, 0, 1),
  ("itm_skill_dragons_fear", 0, special_ability, 0, 0, 1),
  ("itm_skill_weakness", 0, special_ability, 0, 0, 1),
  ("itm_skill_avatar", 0, special_ability, 0, 0, 1),
  ("itm_skill_multishot", 0, special_ability, 0, 0, 1),
  ("itm_skill_shadow_blade", 0, special_ability, 0, 0, 1),
  
  ("itm_skill_summon_undead", 0, special_ability_extra, 0, 0, 1),
  ("itm_skill_entangle", 0, special_ability_extra, 0, 0, 1),
  ("itm_skill_grasp", 0, special_ability_extra, 0, 0, 1),
  ("itm_skill_spell_dispel", 0, special_ability_extra, 0, 0, 1),
  ("itm_skill_heal", 0, special_ability_extra, 0, 0, 1),
  ("itm_skill_mass_heal", 0, special_ability_extra, 0, 0, 1),
  ("itm_skill_forst_ring", 0, special_ability_extra, 0, 0, 1),
  ("itm_skill_dragon_voice", 0, special_ability_extra, 0, 0, 1),
  ("itm_skill_divine_ruling", 0, special_ability_extra, 0, 0, 1),
  ("itm_skill_divine_ruling", 0, special_ability_extra, 0, 0, 1),
  
  ("itm_skill_ironshield", 0, special_ability_passive, 0, 0, 1),
  ("itm_skill_battlerage", 0, special_ability_passive, 0, 0, 1),
  ("itm_skill_cleave", 0, special_ability_passive, 0, 0, 1),
  ("itm_skill_deadly_strike", 0, special_ability_passive, 0, 0, 1),
  ("itm_skill_fear_attack", 0, special_ability_passive, 0, 0, 1),
  ("itm_skill_master_of_ice", 0, special_ability_passive, 0, 0, 1),
  ("itm_skill_master_of_storms", 0, special_ability_passive, 0, 0, 1),
  ("itm_skill_master_of_fire", 0, special_ability_passive, 0, 0, 1),
  ("itm_skill_spirit_link", 0, special_ability_passive, 0, 0, 1),
  ("itm_skill_confession", 0, special_ability_passive, 0, 0, 1),
  ("itm_skill_mummy", 0, special_ability_passive, 0, 0, 1),
  ("itm_skill_counter_strike", 0, special_ability_passive, 0, 0, 1),
  ("itm_skill_life_drain", 0, special_ability_passive, 0, 0, 1),
  ("itm_skill_skeletal", 0, special_ability_passive, 0, 0, 1),
  ("itm_skill_retribution", 0, special_ability_passive, 0, 0, 1),
  ("itm_skill_magic_mirror", 0, special_ability_passive, 0, 0, 1),
  ("itm_skill_fire_shield", 0, special_ability_passive, 0, 0, 1),
  ("itm_skill_meditation", 0, special_ability_passive, 0, 0, 1),
  ("itm_skill_counter", 0, special_ability_passive, 0, 0, 1),



  ("itm_skill_shadowstep", 0, special_ability, 0, 0, 1),
  ("itm_skill_shadow_blade", 0, special_ability_extra, 0, 0, 1),
  
  ("itm_skill_rage_strike", 0, special_ability, 0, 0, 1),
  ("itm_skill_rage_charge", 0, special_ability_extra, 0, 0, 1),
  
  ("itm_skill_awaken", 0, special_ability, 0, 0, 1),
  ("itm_skill_charge", 0, special_ability_extra, 0, 0, 1),
  
  ("itm_skill_mass_slow", 0, special_ability, 0, 0, 1),
  ("itm_skill_slow", 0, special_ability_extra, 0, 0, 1),
  
  ("itm_skill_mass_haste", 0, special_ability, 0, 0, 1),
  ("itm_skill_haste", 0, special_ability_extra, 0, 0, 1),
  
  ("itm_skill_dragron_flame_burst", 0, special_ability, 0, 0, 1),
  ("itm_skill_flame_burst", 0, special_ability_extra, 0, 0, 1),

  
  ("itm_skill_rush", 0, special_ability_extra, 0, 0, 1),
  ("itm_skill_powercharge", 0, special_ability_passive, 0, 0, 1),
  
  ("itm_skill_rend", 0, special_ability_extra, 0, 0, 1),
  ("itm_skill_wound_strike", 0, special_ability_passive, 0, 0, 1),
  
  ("itm_skill_power_blade", 0, special_ability_extra, 0, 0, 1),
  ("itm_skill_earth_shock", 0, special_ability_passive, 0, 0, 1),
  
  ("itm_skill_power_strike", 0, special_ability_extra, 0, 0, 1),
  ("itm_skill_cull_the_weak", 0, special_ability_passive, 0, 0, 1),
  
  ("itm_skill_roll", 0, special_ability_extra, 0, 0, 1),
  ("itm_skill_block", 0, special_ability_passive, 0, 0, 1),
  
  ("itm_skill_flamestrike", 0, special_ability_extra, 0, 0, 1),
  ("itm_skill_flameswave", 0, special_ability_passive, 0, 0, 1),
  
  ("itm_skill_call_lightning", 0, special_ability_extra, 0, 0, 1),
  ("itm_skill_lightning_attack", 0, special_ability_passive, 0, 0, 1),
  
  ("itm_skill_smite_evil", 0, special_ability_extra, 0, 0, 1),
  ("itm_skill_bane_evil", 0, special_ability_passive, 0, 0, 1),
  
  ("itm_skill_smite_undead", 0, special_ability_extra, 0, 0, 1),
  ("itm_skill_bane_undead", 0, special_ability_passive, 0, 0, 1),
  
  ("itm_skill_smite_orc", 0, special_ability_extra, 0, 0, 1),
  ("itm_skill_bane_orc", 0, special_ability_passive, 0, 0, 1),
  
  ("itm_skill_head_hunted", 0, special_ability_extra, 0, 0, 1),
  ("itm_skill_smite_human", 0, special_ability_passive, 0, 0, 1),
  
  ("itm_skill_smite_outsider", 0, special_ability_extra, 0, 0, 1),
  ("itm_skill_bane_outsider", 0, special_ability_passive, 0, 0, 1),
  
  ("itm_skill_reaper", 0, special_ability_extra, 0, 0, 1),
  ("itm_skill_smite_life", 0, special_ability_passive, 0, 0, 1),
  
  ("itm_skill_flamestrike", 0, special_ability_extra, 0, 0, 1),
  ("itm_skill_flameswave", 0, special_ability_passive, 0, 0, 1),
  
  ("itm_skill_sinper_shot", 0, special_ability_extra, 0, 0, 1),
  ("itm_skill_steady_aim", 0, special_ability_passive, 0, 0, 1),
  
  
  
  ("itm_skill_wrath", 0, special_ability, 0, 0, 1),
  ("itm_skill_berserk", 0, special_ability_extra, 0, 0, 1),
  ("itm_skill_frenzy", 0, special_ability_passive, 0, 0, 1),
  
  ("itm_skill_insight", 0, special_ability, 0, 0, 1),
  ("itm_skill_focus", 0, special_ability_extra, 0, 0, 1),
  ("itm_skill_ambush", 0, special_ability_passive, 0, 0, 1),
  
  ("itm_skill_windforce", 0, special_ability, 0, 0, 1),
  ("itm_skill_master_archer", 0, special_ability_extra, 0, 0, 1),
  ("itm_skill_arrow_of_slaying", 0, special_ability_passive, 0, 0, 1),
    
  ("itm_skill_hero_dreams", 0, special_ability, 0, 0, 1),
  ("itm_skill_charm", 0, special_ability_extra, 0, 0, 1),
  ("itm_skill_bubble_dreams", 0, special_ability_passive, 0, 0, 1),
  
  ("itm_skill_khorne_blessing", 0, special_ability, 0, 0, 1),
  ("itm_skill_mana_burn", 0, special_ability_extra, 0, 0, 1),
  ("itm_skill_mark_of_khorne", 0, special_ability_passive, 0, 0, 1),
  
  ("itm_skill_nurgle_blessing", 0, special_ability, 0, 0, 1),
  ("itm_skill_curse_of_the_leper", 0, special_ability_extra, 0, 0, 1),
  ("itm_skill_poisoned_attacks", 0, special_ability_passive, 0, 0, 1),
  
  ("itm_skill_tzeentch_arcane", 0, special_ability, 0, 0, 1),
  ("itm_skill_mana_burst", 0, special_ability_extra, 0, 0, 1),
  ("itm_skill_diffusal_blade", 0, special_ability_passive, 0, 0, 1),
  
  ("itm_skill_ground_stomp", 0, special_ability, 0, 0, 1),
  ("itm_skill_seismic_slam", 0, special_ability_extra, 0, 0, 1),
  ("itm_skill_power_cleave", 0, special_ability_passive, 0, 0, 1),
  
  ("itm_skill_holy_light", 0, special_ability, 0, 0, 1),
  ("itm_skill_divine_ruling", 0, special_ability_extra, 0, 0, 1),
  ("itm_skill_revelation", 0, special_ability_passive, 0, 0, 1),
  
  ("itm_skill_it_is_high_noon", 0, special_ability, 0, 0, 1),
  ("itm_skill_sidearm_1", 0, special_ability_extra, 0, 0, 1),
  ("itm_skill_sidearm_2", 0, special_ability_passive, 0, 0, 1),
  
  ("itm_skill_luanwu", 0, special_ability, 0, 0, 1),
  ("itm_skill_wushuang", 0, special_ability_extra, 0, 0, 1),
  ("itm_skill_undead_horse", 0, special_ability_passive, 0, 0, 1),
  
  ("itm_skill_dragon_blade_slash", 0, special_ability, 0, 0, 1),
  ("itm_skill_swift_strike", 0, special_ability_extra, 0, 0, 1),
  ("itm_skill_deflect", 0, special_ability_passive, 0, 0, 1),
  
  
  ("itm_bash_shadow_blade", 0, bash, 0, 0, 1),
  ("itm_bash_rush", 0, bash, 0, 0, 1),
  ("itm_bash_cleave", 0, bash, 0, 0, 1),
  ("itm_bash_power_strike", 0, bash, 0, 0, 1),
  ("itm_bash_roll", 0, bash, 0, 0, 1),
  ("itm_bash_seismic_slam", 0, bash, 0, 0, 1),
  ("itm_bash_earth_shock", 0, bash, 0, 0, 1),
  ("itm_bash_flame_burst", 0, bash, 0, 0, 1),
  ("itm_bash_forst_ring", 0, bash, 0, 0, 1),
  
  ("itm_bash_grasp", 0, bash, 0, 0, 1),
  ("itm_bash_summon_undead", 0, bash, 0, 0, 1),
  ("itm_bash_swift_strike", 0, bash, 0, 0, 1),
  ("itm_bash_sidearm_1", 0, bash, 0, 0, 1),
  ("itm_bash_shield_bash", 0, bash, 0, 0, 1),
  ("itm_bash_kick", 0, bash, 0, 0, 1),
  ("itm_skill_dragon_blade_slash", 0, bash, 0, 0, 1),
  ("itm_skill_dragon_blade_slash", 0, bash, 0, 0, 1),
  ("itm_skill_dragon_blade_slash", 0, bash, 0, 0, 1),
  
  ("itm_bash_smite_evil", 0, bash, 0, 0, 1),
  ("itm_bash_smite_undead", 0, bash, 0, 0, 1),
  ("itm_bash_smite_orc", 0, bash, 0, 0, 1),
  ("itm_bash_head_hunted", 0, bash, 0, 0, 1),
  ("itm_bash_smite_outsider", 0, bash, 0, 0, 1),







  
]
    


def set_follower_troops():
  troop_score = []
  for i_follower_troops in xrange(len(follower_troops)):
    troop_score.append((troop_set_slot, follower_troops[i_follower_troops][0], slot_troop_special_troop, follower_troops[i_follower_troops][1]))
    
  return troop_score[:]
  
follower_troops = [
  
  ("trp_quick_battle_troop_1", "trp_ninjia_adv"),
  ("trp_quick_battle_troop_2", "trp_sissofbattle_s"),
  ("trp_quick_battle_troop_3", "trp_teutonic_horse_3"),
  ("trp_quick_battle_troop_4", "trp_german_twohander_4"),
  ("trp_quick_battle_troop_5", "trp_nord_champion"),
  ("trp_quick_battle_troop_6", "trp_woodelf_sharpshooter"),
  ("trp_quick_battle_troop_7", "trp_grandelf_arcane_guard"),
  ("trp_quick_battle_troop_8", "trp_drowelf_assassin_2"),
  ("trp_quick_battle_troop_9", "trp_rus_palace_guard"),
  ("trp_quick_battle_troop_10", "trp_dullahan"),
  ("trp_quick_battle_troop_11", "trp_german_reitern_2"),
  ("trp_quick_battle_troop_12", "trp_huge_inferno"),
  ("trp_npc1", "trp_rus_palace_guard"),
  ("trp_npc2", "trp_merchant_cavalry_militia"),
  ("trp_npc3", "trp_sissofbattle_r"),
  ("trp_npc4", "trp_demon_human_4"),
  ("trp_npc5", "trp_black_khergit_lancer"),
  ("trp_npc6", "trp_hospitaller_knight_2"),
  ("trp_npc7", "trp_sherwood_archer"),
  ("trp_npc8", "trp_nord_valkyrie_3"),
  ("trp_npc9", "trp_grandelf_mage_2"),
  ("trp_npc10", "trp_woodelf_sharpshooter"), 
  ("trp_npc11", "trp_sword_sister"),  
  ("trp_npc12", "trp_lava_dragon"),  
  ("trp_npc13", "trp_drowelf_which_2"),    
  ("trp_npc14", "trp_dwarf_guard_3"),
  ("trp_npc15", "trp_human_magic_3"),  
  ("trp_npc16", "trp_ninjia_adv"),    
  ("trp_npc17", "trp_france_horse_4"),
  ("trp_npc18", "trp_minotaur_3"),
  ("trp_npc19", "trp_drowelf_raider_2"),
  ("trp_npc20", "trp_teutonic_dis_knight"),
  ("trp_npc21", "trp_death"),
  ("trp_npc22", "trp_cannon_man"),
  ("trp_npc23", "trp_sissofbattle_s"),
  ("trp_npc24", "trp_titan_2"),
  
  ("trp_adventurer_troop_1", "trp_death"),
  ("trp_adventurer_troop_2", "trp_we_recruit"),
  ("trp_adventurer_troop_3", "trp_polish_knight_4"),
  ("trp_adventurer_troop_4", "trp_lich_dragon"),
  ("trp_adventurer_troop_5", "trp_orc_big_boss"),
  ("trp_adventurer_troop_6", "trp_france_knight_4"),
  ("trp_adventurer_troop_7", "trp_dawnguard_2"),
  ("trp_adventurer_troop_8", "trp_france_horse_2"),
  ("trp_adventurer_troop_9", "trp_undead_horse_3"),
  ("trp_adventurer_troop_10", "trp_grandelf_arcane_guard"),
  ("trp_adventurer_troop_11", "trp_demon_7"),
  ("trp_adventurer_troop_12", "trp_demon_human_5_2"),
  ("trp_adventurer_troop_13", "trp_orc_big_boss"),
  ("trp_adventurer_troop_14", "trp_cyclop"),
  ("trp_adventurer_troop_15", "trp_demon_8"),
  
  ("trp_adventurer_troop_16", "trp_witch_hunter"),
  ("trp_adventurer_troop_17", "trp_teutonic_dis_halbbruder"),
  
  
  ("trp_kingdom_1_lord", "trp_archangle"),
  ("trp_kingdom_3_lord", "trp_nazgul"),
  ("trp_kingdom_4_lord", "trp_gold_dragon"),
  ("trp_kingdom_5_lord", "trp_lich_dragon"),
  
  ("trp_kingdom_7_lord", "trp_titan_2"),
  ("trp_kingdom_8_lord", "trp_polish_knight_4"),
  ("trp_kingdom_9_lord", "trp_demon_human_5_1"),
  ("trp_kingdom_10_lord", "trp_lava_dragon"),

  ("trp_knight_1_1", "trp_france_knight_4"),
  ("trp_knight_1_2", "trp_france_horse_2"),
  ("trp_knight_1_3", "trp_france_horse_4"),
  ("trp_knight_1_4", "trp_cannon_man"),
  ("trp_knight_1_5", "trp_hospitaller_knight_2"),
  ("trp_knight_1_6", "trp_france_horse_3"),
  ("trp_knight_1_7", "trp_hospitaller_knight"),
  ("trp_knight_1_9", "trp_healer"),
  ("trp_knight_1_8", "trp_dunedain_ranger"),
  
  ("trp_knight_1_19", "trp_france_crossbow_4"),

  ("trp_knight_3_1", "trp_nazgul"),
  #("trp_knight_3_2", "trp_nazgul"),
  #("trp_knight_3_3", "trp_nazgul"),
  
  ("trp_knight_3_16", "trp_nazgul"),
  ("trp_knight_3_17", "trp_demon_4_3"),
  #("trp_knight_3_18", "trp_nazgul"),
  
  #("trp_knight_3_11", "trp_nazgul"),
  #("trp_knight_3_12", "trp_nazgul"),
  
  ("trp_knight_3_4", "trp_me_hand_gunner"),
  ("trp_knight_3_5", "trp_ogre_cannon"),
  ("trp_knight_3_9", "trp_goblin_knight"),
  ("trp_knight_3_10", "trp_orc_big_boss"),
  ("trp_knight_3_14", "trp_ogre_mega"),
  ("trp_knight_3_15", "trp_cyclop"),
  ("trp_knight_3_8", "trp_troll_2"),
  ("trp_knight_3_19", "trp_ninjia_adv"),
  ("trp_knight_3_20", "trp_khergit_general"),
  
  ("trp_knight_4_5", "trp_woodelf_cavalry"),
  
  ("trp_knight_4_4", "trp_sherwood_archer"),
  
  ("trp_knight_4_9", "trp_woodelf_swordman"),
  ("trp_knight_4_10", "trp_woodelf_sworddancer"),
  
  ("trp_knight_4_14", "trp_england_knight_4"),
  ("trp_knight_4_15", "trp_woodelf_druid_2"),
  
  ("trp_knight_4_19", "trp_sherwood_archer"),
  ("trp_knight_4_20", "trp_england_swordsman_3"),
  
  ("trp_knight_5_5", "trp_vampire_4"),
  ("trp_knight_5_10", "trp_undead_horse_3"),
  ("trp_knight_5_15", "trp_wraith"),
  ("trp_knight_5_20", "trp_lich_2"),
  
  ("trp_knight_5_4", "trp_vampire_2"),
  ("trp_knight_5_9", "trp_undead_horse_2"),
  ("trp_knight_5_14", "trp_ghost_dragon"),
  ("trp_knight_5_19", "trp_lich_1"),
  
  ("trp_knight_5_1", "trp_skeleton_lord"),
  ("trp_knight_5_9", "trp_dullahan"),
  ("trp_knight_5_11", "trp_skeleton_lord"),
  ("trp_knight_5_16", "trp_wraith"),
  
  ("trp_knight_7_1", "trp_iberian_town_footman_3"),
  ("trp_knight_7_2", "trp_human_magic_4"),
  ("trp_knight_7_3", "trp_grey_knight_inquisitor"),
  ("trp_knight_7_4", "trp_sissofbattle_s"),

  ("trp_knight_7_5", "trp_german_twohander_4"),
  ("trp_knight_7_6", "trp_german_crossbow_5"),
  ("trp_knight_7_7", "trp_grey_knight_terminator"),
  ("trp_knight_7_8", "trp_witch_hunter"),

  ("trp_knight_8_4", "trp_rus_palace_guard"),
  ("trp_knight_8_9", "trp_werewolf_huge"),
  ("trp_knight_8_10", "trp_red_dragon"),
  
  ("trp_knight_8_5", "trp_drowelf_raider_2"),
  ("trp_knight_8_14", "trp_drowelf_assassin_3"),
  ("trp_knight_8_15", "trp_minotaur_3"),
  ("trp_knight_8_19", "trp_drowelf_which_2"),
  ("trp_knight_8_20", "trp_undead_magic_1"),
  ("trp_knight_8_11", "trp_drowelf_infantry_2"),



  ("trp_knight_2_1", "trp_polish_knight_4"),
  ("trp_knight_6_1", "trp_mummy_4"),
  ("trp_knight_11_1", "trp_dwarf_musketeer_3"),
  ("trp_knight_13_1", "trp_grandelf_cavalry"),
  ("trp_knight_14_1", "trp_german_twohander_4"),
  

  ("trp_knight_9_4", "trp_naffatun"),
  ("trp_knight_9_5", "trp_mummy_3"),
  ("trp_knight_9_9", "trp_sarranid_assasin_2"),
  ("trp_knight_9_10", "trp_demon_4"),
  ("trp_knight_9_14", "trp_demon_5"),
  ("trp_knight_9_15", "trp_demon_human_5_1"),
  ("trp_knight_9_19", "trp_demon_human_5_2"),
  ("trp_knight_9_20", "trp_demon_6"),

  ("trp_knight_10_4", "trp_dawnguard_1"),
  ("trp_knight_10_5", "trp_dwarf_musketeer_2_2"),
  
  ("trp_knight_10_9", "trp_werewolf_berserker"),
  ("trp_knight_10_10", "trp_dawnguard_2"),
  ("trp_knight_10_14", "trp_lich_3"),
  ("trp_knight_10_15", "trp_nord_valkyrie_3"),
  ("trp_knight_10_19", "trp_dwarf_guard_3"),
  ("trp_knight_10_20", "trp_giant_3"),
  ("trp_knight_10_13", "trp_giant_2"),
  
]
def set_troop_upgrade_troops():
  result_list = []
  for row_no in xrange(len(troop_upgrade_troops)):
    result_list.append((troop_set_slot, troop_upgrade_troops[row_no][0], slot_troop_upgrade_1,  troop_upgrade_troops[row_no][1]))
  return result_list[:]

troop_upgrade_troops = [
#kingdom_1
  ("trp_scottish_guard", "trp_scottish_swordman"),
  ("trp_france_horse_4", "trp_france_knight_3"),
  ("trp_france_horse_3", "trp_france_pikeman_3"),
  ("trp_france_horse_2", "trp_teutonic_dis_knight"),
  
  ("trp_hospitaller_knight_2", "trp_france_knight_4"),
  ("trp_hospitaller_knight", "trp_france_knight_4"),
  
  ("trp_grandelf_mage_1", "trp_grandelf_swordman_adv"),
  
  ("trp_angle", "trp_sword_sister"),
  ("trp_dunedain_ranger", "trp_france_crossbow_3"),
#kingdom_2
  ("trp_polish_horse_4", "trp_balkan_cav_3"),
#kingdom_3
  ("trp_khergit_heavy", "trp_khergit_dismounted_lancer"),
  ("trp_khergit_guard", "trp_khergit_heavy_archer"),
  ("trp_orc_big_boss", "trp_orc_blackorc_boss"),
  ("trp_troll_2", "trp_troll_1"),
  ("trp_troll_3", "trp_troll_1"),
  ("trp_ogre_mega", "trp_ogre"),
  ("trp_ogre_war2", "trp_ogre_war"),
  
  
  ("trp_goblin_bomber", "trp_goblin_infantry"),
  
#kingdom_4
  ("trp_sherwood_archer", "trp_england_longbowm_3"),
  ("trp_custom_sergeant", "trp_champion_swordsman"),
  ("trp_england_swordsman_3", "trp_england_billmen_2"),
  ("trp_woodelf_stinger", "trp_welsh_longbowm_3"),
  ("trp_green_dragon", "trp_england_knight_3"),
  ("trp_woodelf_cavalry", "trp_woodelf_swordman"),
  ("trp_lich_3", "trp_lich_2"),
  ("trp_gold_dragon", "trp_green_dragon"),
  ("trp_woodelf_sharpshooter", "trp_woodelf_stinger"),
  ("trp_woodelf_druid_1", "trp_woodelf_stinger"),
  ("trp_woodelf_druid_2", "trp_woodelf_sharpshooter"),
#kingdom_5
  ("trp_italian_town_footman_2", "trp_se_billman_2"),
  ("trp_mercenary_pavise_crossbow_captain", "trp_italian_crossbow_3"),
  
  ("trp_ghost", "trp_italian_town_footman_1"),

  ("trp_custom_cannon_man", "trp_musket_ranger"),
  ("trp_cannon_man", "trp_musket_ranger"),
  ("trp_hand_gunner", "trp_musket_line_infantry"),
  ("trp_death", "trp_wraith"),

  ("trp_musket_ranger", "trp_polish_crossbow_3_2"),

  ("trp_lich_dragon", "trp_ghost_dragon"),

  ("trp_undead_horse_2", "trp_italian_horse_4"),
  ("trp_lich_1", "trp_human_magic_3"),

  ("trp_se_pikeman_2", "trp_zombie_1"),

  ("trp_human_magic_4", "trp_human_magic_3"),
#kingdom_6
  ("trp_me_hand_gunner", "trp_me_mercenary_swordsman_2"),
  ("trp_naffatun", "trp_me_mercenary_swordsman_1"),
  ("trp_sarranid_assasin", "trp_custom_infantry"),
#kingdom_7
  ("trp_german_knight_2", "trp_iberian_knight_2"),
  ("trp_german_reitern_2", "trp_musket_cavalry"),
  ("trp_german_twohander_2", "trp_mercenary_swordsman"),
  ("trp_german_twohander_4", "trp_german_knight_4"),
  ("trp_german_reitern_3", "trp_german_reitern_2"),
  ("trp_german_crossbow_5", "trp_german_crossbow_4"),
  
  ("trp_witch_hunter", "trp_german_crossbow_4"),
  
  ("trp_sissofbattle", "trp_sword_sister"),
  ("trp_grey_knight_terminator", "trp_german_knight_4"),
  ("trp_grey_knight_inquisitor", "trp_german_knight_4"),
#kingdom_8
  #("trp_hungary_knight_3", "trp_we_knight_3"),
  ("trp_custom_cavalry", "trp_polish_horse_3"),
  ("trp_drowelf_raider_1", "trp_drowelf_infantry_1"),
  ("trp_red_dragon", "trp_polish_knight_3"),
  ("trp_polish_knight_4", "trp_polish_knight_3"),
  
  ("trp_polish_which_1", "trp_sword_sister"),
  
  ("trp_drowelf_infantry_1", "trp_drowelf_assassin_1"),
  ("trp_drowelf_which_2", "trp_drowelf_which_1"),
#kingdom_9

#kingdom_10
  ("trp_nord_knight_2", "trp_nord_raider"),
  ("trp_nord_axeman_1", "trp_nord_veteran"),
  ("trp_dwarf_guard_3", "trp_nord_halberd_2"),
  ("trp_mercenary_elite_axeman", "trp_nord_champion"),
  ("trp_nord_valkyrie_1", "trp_fighter_woman"),
  ("trp_werewolf_berserker", "trp_god_choosen_berserker"),
  ("trp_dwarf_bear_rider", "trp_nord_halberd_1"),
  ("trp_dawnguard_1", "trp_nord_knight_3"),
  ("trp_dawnguard_2", "trp_nord_knight_3"),
  ("trp_draugr_lord", "trp_draugr_3"),

#kingdom_11

#kingdom_12
  ("trp_marinid_camel_2", "trp_turk_cav_2"),
  ("trp_demon_human_2", "trp_ghazis_2"),
  ("trp_demon_human_5_2", "trp_sword_sister"),
  ("trp_demon_3", "trp_demon_1_2"),
  
  ("trp_rat_5_3", "trp_rat_4"),
  
  ("trp_ogre_war", "trp_ogre"),
  ("trp_ogre", "trp_ogre_young"),
  
  ("trp_mamluke_horseman_2", "trp_turk_cav_3"),
  ("trp_turk_sipahi_lance", "trp_mamluke_horseman_3"),
  
  ("trp_demon_magic_2", "trp_human_magic_1"),
  ("trp_mummy_3", "trp_mummy_2"),
  ("trp_mummy_4", "trp_werewolf_1_a"),
  ("trp_demon_7", "trp_turk_roy_sipahi"),
  ("trp_demon_human_5_1", "trp_turk_roy_sipahi"),
#kingdom_13
  
  #("trp_rat_5_1", "trp_rat_4"),
  #("trp_rat_5_2", "trp_rat_4"),
  
  ("trp_dullahan", "trp_zombie_2"),
  
  ("trp_rus_dvor_cavalry", "trp_rus_cossack_2"),
]

      
def set_party_template_type():
  result_list = []
  for row_no in xrange(len(party_template_type)):
    result_list.append((party_template_set_slot, party_template_type[row_no][0], slot_party_template_type,   party_template_type[row_no][1]))
    result_list.append((party_template_set_slot, party_template_type[row_no][0], slot_party_template_basic_gold,   party_template_type[row_no][2]))
    result_list.append((party_template_set_slot, party_template_type[row_no][0], slot_party_template_bonus_gold,   party_template_type[row_no][3]))
    result_list.append((party_template_set_slot, party_template_type[row_no][0], slot_party_template_extra_troop,   party_template_type[row_no][4]))
    result_list.append((party_template_set_slot, party_template_type[row_no][0], slot_party_template_extra_troop_num,   party_template_type[row_no][5]))
  return result_list[:]

party_template_type = [
  ("pt_experiance_stone", experiance_stone, 1000, 500, 0, 0),

  ("pt_obelisk_1", obelisk, 1000, 500, 0, 0),
  ("pt_obelisk_2", obelisk, 1000, 500, 0, 0),
  ("pt_obelisk_3", obelisk, 1000, 500, 0, 0),
  ("pt_obelisk_4", obelisk, 1000, 500, 0, 0),
  ("pt_obelisk_5", obelisk, 1000, 500, 0, 0),
  ("pt_obelisk_6", obelisk, 1000, 500, 0, 0),
  ("pt_obelisk_7", obelisk, 1000, 500, 0, 0),
  ("pt_obelisk_8", obelisk, 1000, 500, 0, 0),
  ("pt_obelisk_9", obelisk, 1000, 500, 0, 0),
  ("pt_obelisk_10", obelisk, 1000, 500, 0, 0),
  ("pt_obelisk_11", obelisk, 1000, 500, 0, 0),
  ("pt_obelisk_12", obelisk, 1000, 500, 0, 0),
  ("pt_obelisk_13", obelisk, 1000, 500, 0, 0),
  ("pt_obelisk_14", obelisk, 1000, 500, 0, 0),
  ("pt_obelisk_15", obelisk, 1000, 500, 0, 0),
  ("pt_obelisk_16", obelisk, 1000, 500, 0, 0),
  ("pt_obelisk_17", obelisk, 1000, 500, 0, 0),
  ("pt_obelisk_18", obelisk, 1000, 500, 0, 0),
  ("pt_obelisk_19", obelisk, 1000, 500, 0, 0),
  
  

  ("pt_camp_fire", treasure, 100, 100, 0, 0),
  ("pt_gold_pile", treasure, 1000, 100, 0, 0),
  ("pt_treasure_chest_1", treasure, 500, 500, 0, 0),
  ("pt_treasure_chest_2", treasure, 500, 500, 0, 0),
  ("pt_treasure_chest_3", treasure, 500, 500, 0, 0),
  ("pt_dragon_utopia", bank, 20000, 10000, 0, 0),
  ("pt_crypt", bank, 2000, 1000, 0, 0),
  ("pt_ruins", bank, 2000, 1000, 0, 0),
  ("pt_keep_1", bank, 2000, 1000, 0, 0),
  ("pt_keep_2", bank, 2000, 1000, 0, 0),
  ("pt_keep_3", bank, 2000, 1000, 0, 0),
  ("pt_keep_4", bank, 2000, 1000, 0, 0),
  ("pt_keep_5", bank, 2000, 1000, 0, 0),
  ("pt_keep_6", bank, 2000, 1000, 0, 0),

  ("pt_orc_tower", bank, 2000, 1000, 0, 0),
  ("pt_ivory_tower", bank, 2500, 1500, "trp_golem_4", 8),
  ("pt_evil_tower", bank, 2500, 1500, 0, 0),
  ("pt_pyramid", bank, 2500, 1500, 0, 0),

  ("pt_imp_cache_2", bank, 2500, 1500, 0, 0),
  ("pt_dwarven_treasury", bank, 2500, 1500, 0, 0),
  ("pt_treetop_tower", bank, 2500, 1500, 0, 0),
  ("pt_subterranean_gate", bank, 2500, 1500, 0, 0),
  ("pt_elemental_conservatory", bank, 2500, 1500, 0, 0),
  ("pt_treant_thicket", bank, 2500, 1500, 0, 0),
  ("pt_hall_of_shadows", bank, 2500, 1500, 0, 0),
  ("pt_derelict_ship_1", bank, 2500, 1500, 0, 0),
  ("pt_derelict_ship_2", bank, 1500, 1500, 0, 0),
  ("pt_derelict_ship_3", bank, 1500, 1500, 0, 0),
  ("pt_derelict_ship_4", bank, 5000, 5000, 0, 0),
  ("pt_derelict_ship_5", bank, 3000, 1000, 0, 0),
  ("pt_derelict_ship_6", bank, 3000, 1000, 0, 0),
  ("pt_derelict_ship_7", bank, 4000, 1500, 0, 0),
  ("pt_derelict_ship_8", bank, 5000, 1000, 0, 0),
  ("pt_derelict_ship_9", bank, 5000, 1000, 0, 0),
  ("pt_derelict_ship_10", bank, 5000, 2500, 0, 0),

  ("pt_golem_factory", lair, 0, 0, "trp_gargoyle", 4),
  ("pt_dragon_fly_hive", lair, 0, 0, "trp_lizard_dragon", 2),
  ("pt_genie_lamp", lair, 0, 0, "trp_we_recruit", 4),
  ("pt_genie_lamp_2", lair, 0, 0, "trp_demon_4", 4),

  ("pt_cloud_temple_2", lair, 500, 500, "trp_giant_3", 4),
  ("pt_dragon_cave_5", lair, 500, 500, "trp_giant_2", 4),
  ("pt_portal_of_glory", lair, 500, 500, "trp_angle", 4),
  ("pt_portal_of_glory_2", lair, 500, 500, "trp_sissofbattle", 16),
  ("pt_portal_of_glory_3", lair, 500, 500, "trp_nord_valkyrie_3", 4),
  ("pt_cloud_temple_3", lair, 500, 500, "trp_titan_0", 4),
  ("pt_cyclops_cave", lair, 500, 500, "trp_cyclop", 4),
  ("pt_troll_bridge", lair, 500, 500, "trp_troll_1", 4),
  ("pt_behemoth_cave", lair, 500, 500, "trp_demon_4_2", 4),
  ("pt_forsaken_palace_1", lair, 500, 500, "trp_demon_7", 4),
  ("pt_forsaken_palace_2", lair, 500, 500, "trp_demon_human_5_1", 4),
  ("pt_forsaken_palace_3", lair, 500, 500, "trp_demon_9", 4),
  ("pt_forsaken_palace_4", lair, 500, 500, "trp_demon_human_5_2", 4),
  ("pt_vampire_palace_1", lair, 500, 500, "trp_lich_1", 4),
  ("pt_vampire_palace_2", lair, 500, 500, "trp_undead_horse_2", 4),
  ("pt_vampire_palace_3", lair, 500, 500, "trp_vampire_3", 4),
  ("pt_witch_hut_2", lair, 500, 500, "trp_polish_which_1", 4),
  ("pt_school_of_magic_2", lair, 500, 500, "trp_human_magic_4", 4),
  ("pt_pyramid_2", lair, 500, 500, "trp_mummy_4", 4),
  ("pt_sepulcher", lair, 500, 500, "trp_wraith", 4),
  ("pt_dragon_vault", lair, 500, 500, "trp_bone_dragon", 4),
  ("pt_dragon_cave_1", lair, 500, 500, "trp_red_dragon", 4),
  ("pt_dragon_cave_2", lair, 500, 500, "trp_green_dragon", 4),
  ("pt_dragon_cave_3", lair, 500, 500, "trp_fire_dragon", 4),
  ("pt_dragon_cave_4", lair, 500, 500, "trp_gold_dragon", 4),
  ("pt_golem_factory_2", lair, 500, 500, "trp_gargoyle", 4),
]
    
def set_party_template_type_2():
  result_list = []
  for row_no in xrange(len(party_template_type_2)):
    result_list.append((party_template_set_slot, party_template_type_2[row_no][0], slot_party_template_rewards_type,   party_template_type_2[row_no][1]))
    result_list.append((party_template_set_slot, party_template_type_2[row_no][0], slot_party_template_rewards_num,   party_template_type_2[row_no][2]))
  return result_list[:]

party_template_type_2 = [
  
  #("pt_treasure_chest_2", "itm_trophy_c", 1),
  ("pt_treasure_chest_3", "itm_trophy_c", 1),

  ("pt_dragon_utopia", "itm_sg_blood", 4),
  
  ("pt_crypt", "itm_trophy_c", 1),
  ("pt_ruins", "itm_trophy_c", 1),
  ("pt_keep_1", "itm_trophy_c", 1),
  ("pt_keep_2", "itm_trophy_c", 1),
  ("pt_keep_3", "itm_trophy_c", 1),
  ("pt_keep_4", "itm_trophy_c", 1),
  ("pt_keep_5", "itm_trophy_c", 1),
  ("pt_keep_6", "itm_trophy_c", 1),
  ("pt_orc_tower", "itm_trophy_c", 1),
  
  ("pt_obelisk_1", "itm_trophy_c", 1),
  ("pt_obelisk_2", "itm_trophy_c", 1),
  ("pt_obelisk_3", "itm_trophy_c", 1),
  ("pt_obelisk_4", "itm_trophy_c", 1),
  ("pt_obelisk_5", "itm_trophy_c", 1),
  ("pt_obelisk_6", "itm_trophy_c", 1),
  ("pt_obelisk_7", "itm_trophy_c", 1),
  ("pt_obelisk_8", "itm_trophy_c", 1),
  ("pt_obelisk_9", "itm_trophy_c", 1),
  ("pt_obelisk_10", "itm_trophy_c", 1),
  ("pt_obelisk_11", "itm_trophy_c", 1),
  ("pt_obelisk_12", "itm_trophy_c", 1),
  ("pt_obelisk_13", "itm_trophy_c", 1),
  ("pt_obelisk_14", "itm_trophy_c", 1),
  ("pt_obelisk_15", "itm_trophy_c", 1),
  ("pt_obelisk_16", "itm_trophy_c", 1),
  ("pt_obelisk_17", "itm_trophy_c", 1),
  ("pt_obelisk_18", "itm_trophy_c", 1),
  ("pt_obelisk_19", "itm_trophy_c", 1),
  
  ("pt_pyramid", "itm_diamonds", 1),

  ("pt_elemental_conservatory", "itm_trophy_b", 1),

  ("pt_imp_cache_2", "itm_trophy_b", 1),
  ("pt_dwarven_treasury", "itm_trophy_b", 1),
  ("pt_treetop_tower", "itm_trophy_b", 1),
  ("pt_subterranean_gate", "itm_trophy_b", 1),
  ("pt_treant_thicket", "itm_trophy_b", 1),
  ("pt_hall_of_shadows", "itm_trophy_b", 1),

  ("pt_derelict_ship_1", "itm_sg_human_small", 1),
  ("pt_derelict_ship_2", "itm_trophy_b", 1),
  ("pt_derelict_ship_3", "itm_trophy_b", 1),
  ("pt_derelict_ship_4", "itm_trophy_c", 1),
  
  ("pt_derelict_ship_5", "itm_trophy_a", 1),
  ("pt_derelict_ship_6", "itm_trophy_a", 1),
  
  ("pt_derelict_ship_7", "itm_sg_black_small", 1),
  ("pt_derelict_ship_8", "itm_sg_black_small", 1),
  
  ("pt_derelict_ship_9", "itm_sg_human_big", 1),
  ("pt_derelict_ship_10", "itm_sg_human_big", 1),

]
            
def set_faction_upgrade_troops():
  result_list = []
  for row_no in xrange(len(faction_upgrade_troops)):
    result_list.append((faction_set_slot, faction_upgrade_troops[row_no][0], slot_faction_upgrade_troop_1,   faction_upgrade_troops[row_no][1]))
    result_list.append((faction_set_slot, faction_upgrade_troops[row_no][0], slot_faction_upgrade_troop_2,   faction_upgrade_troops[row_no][2]))
    result_list.append((faction_set_slot, faction_upgrade_troops[row_no][0], slot_faction_upgrade_troop_3,   faction_upgrade_troops[row_no][3]))
    result_list.append((faction_set_slot, faction_upgrade_troops[row_no][0], slot_faction_upgrade_troop_4,   faction_upgrade_troops[row_no][4]))
  return result_list[:]

faction_upgrade_troops = [
  ("fac_kingdom_1", "trp_angle", "trp_france_horse_2", "trp_france_horse_4", "trp_france_horse_3"),
  ("fac_kingdom_3", "trp_troll_2", "trp_ogre_mega", "trp_orc_big_boss", "trp_naffatun"),
  ("fac_kingdom_4", "trp_welsh_longbowm_3", "trp_custom_sergeant", "trp_england_swordsman_3", "trp_woodelf_stinger"),
  ("fac_kingdom_5", "trp_undead_horse_2", "trp_lich_1", "trp_custom_cannon_man", "trp_cannon_man"),

  ("fac_kingdom_7", "trp_german_twohander_4", "trp_grey_knight_inquisitor", "trp_sissofbattle", "trp_grey_knight_terminator"),
  ("fac_kingdom_8", "trp_polish_horse_4", "trp_custom_cavalry", "trp_drowelf_raider_1", "trp_red_dragon"),
  ("fac_kingdom_9", "trp_mummy_4", "trp_demon_human_5_2", "trp_naffatun", "trp_demon_human_5_1"),
  ("fac_kingdom_10", "trp_nord_knight_2", "trp_dwarf_guard_3", "trp_nord_valkyrie_1", "trp_nord_axeman_1"),


]



def set_init_troops():
  troop_score = []
  for i_init_troops in xrange(len(init_troops)):
    troop_score.append((faction_set_slot, init_troops[i_init_troops][0], init_troops[i_init_troops][2], init_troops[i_init_troops][1]))
    troop_score.append((faction_set_slot, init_troops[i_init_troops][0], init_troops[i_init_troops][3], init_troops[i_init_troops][4]))
  return troop_score[:]
  
init_troops = [

  ("fac_kingdom_1", "trp_france_pikeman_1", slot_faction_infantry_1_troop, slot_faction_infantry_1_number, 21),
  ("fac_kingdom_1", "trp_teutonic_sword", slot_faction_infantry_2_troop, slot_faction_infantry_2_number, 7),
  ("fac_kingdom_1", "trp_angle", slot_faction_infantry_3_troop, slot_faction_infantry_3_number, 1),

  ("fac_kingdom_1", "trp_france_crossbow_2", slot_faction_range_1_troop, slot_faction_range_1_number, 20),
  ("fac_kingdom_1", "trp_sissofbattle", slot_faction_range_2_troop, slot_faction_range_2_number, 7),
  ("fac_kingdom_1", "trp_clerics", slot_faction_range_3_troop, slot_faction_range_3_number, 3),

  ("fac_kingdom_1", "trp_france_knight_1", slot_faction_cavalry_1_troop, slot_faction_cavalry_1_number, 8),
  ("fac_kingdom_1", "trp_teutonic_horse_2", slot_faction_cavalry_2_troop, slot_faction_cavalry_2_number, 5),
  ("fac_kingdom_1", "trp_france_knight_3", slot_faction_cavalry_3_troop, slot_faction_cavalry_3_number, 2),

  ("fac_kingdom_1", "trp_france_knight_1", slot_faction_elite_cavalry_1_troop, 0,0),
  ("fac_kingdom_1", "trp_france_knight_2", slot_faction_elite_cavalry_2_troop, 0,0),
  ("fac_kingdom_1", "trp_france_knight_3", slot_faction_elite_cavalry_3_troop, 0,0),

###############################################################################################################

  ("fac_kingdom_3", "trp_orc_boy", slot_faction_infantry_1_troop, slot_faction_infantry_1_number, 24),
  ("fac_kingdom_3", "trp_ogre", slot_faction_infantry_2_troop, slot_faction_infantry_2_number, 7),
  ("fac_kingdom_3", "trp_demon_4_2", slot_faction_infantry_3_troop, slot_faction_infantry_3_number, 1),

  ("fac_kingdom_3", "trp_arrer_youngun", slot_faction_range_1_troop, slot_faction_range_1_number, 20),
  ("fac_kingdom_3", "trp_khergit_horse_archer", slot_faction_range_2_troop, slot_faction_range_2_number, 8),
  ("fac_kingdom_3", "trp_ogre_mega", slot_faction_range_3_troop, slot_faction_range_3_number, 3),

  ("fac_kingdom_3", "trp_khergit_horseman", slot_faction_cavalry_1_troop, slot_faction_cavalry_1_number, 12),
  ("fac_kingdom_3", "trp_orc_boar_boy", slot_faction_cavalry_2_troop, slot_faction_cavalry_2_number, 7),
  ("fac_kingdom_3", "trp_khergit_general", slot_faction_cavalry_3_troop, slot_faction_cavalry_3_number, 3),

  ("fac_kingdom_3", "trp_khergit_guard", slot_faction_elite_cavalry_1_troop, 0,0),
  ("fac_kingdom_3", "trp_khergit_heavy", slot_faction_elite_cavalry_2_troop, 0,0),
  ("fac_kingdom_3", "trp_khergit_general", slot_faction_elite_cavalry_3_troop, 0,0),

###############################################################################################################

  ("fac_kingdom_4", "trp_england_militia", slot_faction_infantry_1_troop, slot_faction_infantry_1_number, 21),
  ("fac_kingdom_4", "trp_woodelf_spearman", slot_faction_infantry_2_troop, slot_faction_infantry_2_number, 7),
  ("fac_kingdom_4", "trp_ent_2", slot_faction_infantry_3_troop, slot_faction_infantry_3_number, 1),

  ("fac_kingdom_4", "trp_england_longbowm_2", slot_faction_range_1_troop, slot_faction_range_1_number, 20),
  ("fac_kingdom_4", "trp_woodelf_hunter", slot_faction_range_2_troop, slot_faction_range_2_number, 6),
  ("fac_kingdom_4", "trp_woodelf_druid_1", slot_faction_range_3_troop, slot_faction_range_3_number, 1),

  ("fac_kingdom_4", "trp_england_horse_1", slot_faction_cavalry_1_troop, slot_faction_cavalry_1_number, 12),
  ("fac_kingdom_4", "trp_woodelf_cavalry", slot_faction_cavalry_2_troop, slot_faction_cavalry_2_number, 4),
  ("fac_kingdom_4", "trp_england_knight_3", slot_faction_cavalry_3_troop, slot_faction_cavalry_3_number, 2),
  
  ("fac_kingdom_4", "trp_england_knight_1", slot_faction_elite_cavalry_1_troop, 0,0),
  ("fac_kingdom_4", "trp_england_knight_2", slot_faction_elite_cavalry_2_troop, 0,0),
  ("fac_kingdom_4", "trp_england_knight_3", slot_faction_elite_cavalry_3_troop, 0,0),

###############################################################################################################

  ("fac_kingdom_5", "trp_se_pikeman_1", slot_faction_infantry_1_troop, slot_faction_infantry_1_number, 25),
  ("fac_kingdom_5", "trp_italian_town_footman_1", slot_faction_infantry_2_troop, slot_faction_infantry_2_number, 10),
  ("fac_kingdom_5", "trp_vampire_3", slot_faction_infantry_3_troop, slot_faction_infantry_3_number, 3),

  ("fac_kingdom_5", "trp_se_musketeer_1", slot_faction_range_1_troop, slot_faction_range_1_number, 18),
  ("fac_kingdom_5", "trp_italian_crossbow_2", slot_faction_range_2_troop, slot_faction_range_2_number, 14),
  ("fac_kingdom_5", "trp_lich_1", slot_faction_range_3_troop, slot_faction_range_3_number, 2),

  ("fac_kingdom_5", "trp_ghost", slot_faction_cavalry_1_troop, slot_faction_cavalry_1_number, 10),
  ("fac_kingdom_5", "trp_undead_horse_2", slot_faction_cavalry_2_troop, slot_faction_cavalry_2_number, 2),
  ("fac_kingdom_5", "trp_bone_dragon", slot_faction_cavalry_3_troop, slot_faction_cavalry_3_number, 1),

  ("fac_kingdom_5", "trp_undead_horse_1", slot_faction_elite_cavalry_1_troop, 0,0),
  ("fac_kingdom_5", "trp_undead_horse_2", slot_faction_elite_cavalry_2_troop, 0,0),
  ("fac_kingdom_5", "trp_undead_horse_3", slot_faction_elite_cavalry_3_troop, 0,0),

###############################################################################################################

  ("fac_kingdom_7", "trp_german_pikeman_1", slot_faction_infantry_1_troop, slot_faction_infantry_1_number, 21),
  ("fac_kingdom_7", "trp_german_twohander_2", slot_faction_infantry_2_troop, slot_faction_infantry_2_number, 7),
  ("fac_kingdom_7", "trp_gargoyle", slot_faction_infantry_3_troop, slot_faction_infantry_3_number, 1),

  ("fac_kingdom_7", "trp_german_crossbow_2", slot_faction_range_1_troop, slot_faction_range_1_number, 20),
  ("fac_kingdom_7", "trp_iberian_town_footman_2", slot_faction_range_2_troop, slot_faction_range_2_number, 7),
  ("fac_kingdom_7", "trp_human_magic_2", slot_faction_range_3_troop, slot_faction_range_3_number, 3),

  ("fac_kingdom_7", "trp_iberian_dragoon_1", slot_faction_cavalry_1_troop, slot_faction_cavalry_1_number, 8),
  ("fac_kingdom_7", "trp_german_knight_2", slot_faction_cavalry_2_troop, slot_faction_cavalry_2_number, 3),
  ("fac_kingdom_7", "trp_titan_0", slot_faction_cavalry_3_troop, slot_faction_cavalry_3_number, 1),

  ("fac_kingdom_7", "trp_german_knight_1", slot_faction_elite_cavalry_1_troop, 0,0),
  ("fac_kingdom_7", "trp_german_knight_2", slot_faction_elite_cavalry_2_troop, 0,0),
  ("fac_kingdom_7", "trp_german_knight_3", slot_faction_elite_cavalry_3_troop, 0,0),

###############################################################################################################

  ("fac_kingdom_8", "trp_polish_crossbow_1", slot_faction_infantry_1_troop, slot_faction_infantry_1_number, 21),
  ("fac_kingdom_8", "trp_balkan_billman_2", slot_faction_infantry_2_troop, slot_faction_infantry_2_number, 7),
  ("fac_kingdom_8", "trp_drowelf_infantry_1", slot_faction_infantry_3_troop, slot_faction_infantry_3_number, 2),

  ("fac_kingdom_8", "trp_rus_cossack_1", slot_faction_range_1_troop, slot_faction_range_1_number, 20),
  ("fac_kingdom_8", "trp_drowelf_assassin_1", slot_faction_range_2_troop, slot_faction_range_2_number, 7),
  ("fac_kingdom_8", "trp_polish_which_1", slot_faction_range_3_troop, slot_faction_range_3_number, 2),

  ("fac_kingdom_8", "trp_polish_horse_2", slot_faction_cavalry_1_troop, slot_faction_cavalry_1_number, 18),
  ("fac_kingdom_8", "trp_drowelf_raider_1", slot_faction_cavalry_2_troop, slot_faction_cavalry_2_number, 5),
  ("fac_kingdom_8", "trp_polish_knight_2", slot_faction_cavalry_3_troop, slot_faction_cavalry_3_number, 3),

  ("fac_kingdom_8", "trp_polish_knight_1", slot_faction_elite_cavalry_1_troop, 0,0),
  ("fac_kingdom_8", "trp_polish_knight_2", slot_faction_elite_cavalry_2_troop, 0,0),
  ("fac_kingdom_8", "trp_polish_knight_3", slot_faction_elite_cavalry_3_troop, 0,0),

###############################################################################################################

  ("fac_kingdom_9", "trp_turk_spearman", slot_faction_infantry_1_troop, slot_faction_infantry_1_number, 21),
  ("fac_kingdom_9", "trp_janissary_retainer", slot_faction_infantry_2_troop, slot_faction_infantry_2_number, 7),
  ("fac_kingdom_9", "trp_sarranid_assasin", slot_faction_infantry_3_troop, slot_faction_infantry_3_number, 3),

  ("fac_kingdom_9", "trp_turk_archer_1", slot_faction_range_1_troop, slot_faction_range_1_number, 20),
  ("fac_kingdom_9", "trp_janissary_musketeer_1", slot_faction_range_2_troop, slot_faction_range_2_number, 6),
  ("fac_kingdom_9", "trp_demon_human_5_1", slot_faction_range_3_troop, slot_faction_range_3_number, 1),

  ("fac_kingdom_9", "trp_turk_cav_2", slot_faction_cavalry_1_troop, slot_faction_cavalry_1_number, 18),
  ("fac_kingdom_9", "trp_turk_sipahi_lance", slot_faction_cavalry_2_troop, slot_faction_cavalry_2_number, 3),
  ("fac_kingdom_9", "trp_demon_7", slot_faction_cavalry_3_troop, slot_faction_cavalry_3_number, 1),

  ("fac_kingdom_9", "trp_turk_sipahi", slot_faction_elite_cavalry_1_troop, 0,0),
  ("fac_kingdom_9", "trp_turk_sipahi_lance", slot_faction_elite_cavalry_2_troop, 0,0),
  ("fac_kingdom_9", "trp_turk_roy_sipahi", slot_faction_elite_cavalry_3_troop, 0,0),

###############################################################################################################

  ("fac_kingdom_10", "trp_nord_warrior", slot_faction_infantry_1_troop, slot_faction_infantry_1_number, 18),
  ("fac_kingdom_10", "trp_nord_swordsmen", slot_faction_infantry_2_troop, slot_faction_infantry_2_number, 8),
  ("fac_kingdom_10", "trp_dwarf_ironbreaker", slot_faction_infantry_3_troop, slot_faction_infantry_3_number, 3),

  ("fac_kingdom_10", "trp_nord_crossbow_1", slot_faction_range_1_troop, slot_faction_range_1_number, 9),
  ("fac_kingdom_10", "trp_nord_valkyrie_2", slot_faction_range_2_troop, slot_faction_range_2_number, 4),
  ("fac_kingdom_10", "trp_giant_1_3", slot_faction_range_3_troop, slot_faction_range_3_number, 1),

  ("fac_kingdom_10", "trp_nord_mounted_scout", slot_faction_cavalry_1_troop, slot_faction_cavalry_1_number, 8),
  ("fac_kingdom_10", "trp_nord_knight_2", slot_faction_cavalry_2_troop, slot_faction_cavalry_2_number, 3),
  ("fac_kingdom_10", "trp_giant_1_2", slot_faction_cavalry_3_troop, slot_faction_cavalry_3_number, 1),

  ("fac_kingdom_10", "trp_nord_knight_1", slot_faction_elite_cavalry_1_troop, 0,0),
  ("fac_kingdom_10", "trp_nord_knight_2", slot_faction_elite_cavalry_2_troop, 0,0),
  ("fac_kingdom_10", "trp_nord_knight_3", slot_faction_elite_cavalry_3_troop, 0,0),  

]

