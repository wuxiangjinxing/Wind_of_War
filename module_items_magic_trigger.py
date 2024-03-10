# -*- coding: UTF-8 -*-
from header_common import *
from module_constants import *
from ID_factions import *
from header_items import  *
from header_operations import *
from header_troops import *
from header_triggers import *
from header_skills import *




cast_magic_burning_gaze = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_burning_gaze", ":shooter"),
    ])]

cast_magic_blinding_light = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_blinding_light", ":shooter"),
    ])]

cast_magic_net_of_amyntok = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_net_of_amyntok", ":shooter"),
    ])]

cast_magic_light_of_battle = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_light_of_battle", ":shooter"),
    ])]

cast_magic_phas_protection = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_phas_protection", ":shooter"),
    ])]

cast_magic_bironas_timewarp = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_bironas_timewarp", ":shooter"),
    ])]

cast_magic_banishment = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_banishment", ":shooter"),
    ])]
    
    
    
cast_magic_harmonic_convergence = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_harmonic_convergence", ":shooter"),
    ])]

cast_magic_curse_of_the_midnight_wind = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_curse_of_the_midnight_wind", ":shooter"),
    ])]

cast_magic_cascading_fire_cloak = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_cascading_fire_cloak", ":shooter"),
    ])]

cast_magic_cascading_fire_cloak = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_cascading_fire_cloak", ":shooter"),
    ])]
cast_magic_flaming_sword_of_rhuin = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_flaming_sword_of_rhuin", ":shooter"),
    ])]

cast_magic_turn_vampire = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_turn_vampire", ":shooter"),
    ])]

cast_magic_summon_neutral = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_summon_neutral", ":shooter"),
    ])]


cast_magic_summon_air_elemental = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_summon_air_elemental", ":shooter"),
    ])]
cast_magic_summon_fire_elemental = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_summon_fire_elemental", ":shooter"),
    ])]
cast_magic_summon_water_elemental = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_summon_water_elemental", ":shooter"),
    ])]
cast_magic_summon_earth_elemental = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_summon_earth_elemental", ":shooter"),
    ])]
cast_magic_summon_golem = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_summon_golem", ":shooter"),
    ])]

cast_magic_regrowth = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_regrowth", ":shooter"),
    ])]

cast_magic_flesh_to_stone = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_flesh_to_stone", ":shooter"),
    ])]

cast_magic_wyssans_wildform = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_wyssans_wildform", ":shooter"),
    ])]

cast_magic_panns_impenetrable_belt = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_panns_impenetrable_belt", ":shooter"),
    ])]

cast_magic_okkams_mindrazor = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_okkams_mindrazor", ":shooter"),
    ])]

cast_magic_soulblight = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_soulblight", ":shooter"),
    ])]

cast_magic_transmutation_of_lead = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_transmutation_of_lead", ":shooter"),
    ])]

cast_magic_curse_of_anraheir = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_curse_of_anraheir", ":shooter"),
    ])]

cast_magic_wind_blast = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_wind_blast", ":shooter"),
    ])]

cast_magic_comet_of_casandora = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_comet_of_casandora", ":shooter"),
    ])]
    
cast_magic_burnished_gauntlet = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_burnished_gauntlet", ":shooter"),
    ])]

cast_magic_plague_of_rust = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_plague_of_rust", ":shooter"),
    ])]

cast_magic_final_transmutation = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_final_transmutation", ":shooter"),
    ])]

cast_magic_earth_blood = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_earth_blood", ":shooter"),
    ])]
   
cast_magic_animal_mastery = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_animal_mastery", ":shooter"),
    ])]

cast_magic_animate_tree = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_animate_tree", ":shooter"),
    ])]
    
cast_magic_amber_spear = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_amber_spear", ":shooter"),
    ])]

cast_magic_bray_scream = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_bray_scream", ":shooter"),
    ])]

cast_magic_savage_dominion = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_savage_dominion", ":shooter"),
    ])]
    
cast_magic_shadow_bolt = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_shadow_bolt", ":shooter"),
    ])]

cast_melkoths_mystifying_miasma = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_melkoths_mystifying_miasma", ":shooter"),
    ])]
   
cast_magic_steed_of_shadows = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_steed_of_shadows", ":shooter"),
    ])]
   
cast_magic_penumbral_pendulum = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_penumbral_pendulum", ":shooter"),
    ])]
   
cast_magic_spirit_leech = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_spirit_leech", ":shooter"),
    ])]


cast_magic_doom_and_darkness = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_doom_and_darkness", ":shooter"),
    ])]

cast_magic_gaze_of_nagash = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_gaze_of_nagash", ":shooter"),
    ])]

cast_magic_ryze_the_grave_call = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_ryze_the_grave_call", ":shooter"),
    ])]
    
cast_magic_summon_Zombie_Lord = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_summon_Zombie_Lord", ":shooter"),
    ])]
    
cast_magic_doom_bolt = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_doom_bolt", ":shooter"),
    ])]

cast_magic_power_of_darkness = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_power_of_darkness", ":shooter"),
    ])]

cast_magic_word_of_pain = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_word_of_pain", ":shooter"),
    ])]

cast_magic_apotheosis = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_apotheosis", ":shooter"),
    ])]
   
cast_magic_soul_quench = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_soul_quench", ":shooter"),
    ])]

cast_magic_hand_of_glory = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_hand_of_glory", ":shooter"),
    ])]

cast_magic_curse_of_arrow_attraction = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_curse_of_arrow_attraction", ":shooter"),
    ])]

cast_magic_frostblade = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_frostblade", ":shooter"),
    ])]

cast_magic_shield_of_cold = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_shield_of_cold", ":shooter"),
    ])]


   
cast_magic_arcane_unforging = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_arcane_unforging", ":shooter"),
    ])]

cast_magic_mana_tempest = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_mana_tempest", ":shooter"),
    ])]
    
cast_magic_mana_tempest_2 = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_mana_tempest_2", ":shooter"),
    ])]
        
cast_magic_LightningBolt = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_LightningBolt", ":shooter"),
    ])]

cast_magic_lightning = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_lightning", ":shooter"),

    ])]


cast_magic_fire_ray_dummy = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_fire_ray_dummy", ":shooter"),
    ])]
        
cast_magic_fire_ray = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_fire_ray", ":shooter"),
    ])]
        
        
cast_magic_fire_ball = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_fire_ball", ":shooter"),
    ])]

cast_magic_fire_ball_2 = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_fire_ball_2", ":shooter"),
    ])]
    
    
cast_magic_fire_ball_3 = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_fire_ball_3", ":shooter"),
    ])]

cast_magic_Pyroblast = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_Pyroblast", ":shooter"),
    ])]

cast_magic_apocalypse = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_apocalypse", ":shooter"),
    ])]

cast_magic_incediary_cloud = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_incediary_cloud", ":shooter"),
    ])]
    
cast_magic_incediary_cloud_2 = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_incediary_cloud_2", ":shooter"),
    ])]
        
cast_magic_Entangling = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_Entangling", ":shooter"),
    ])]


cast_magic_black_hold_long = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_black_hold_long", ":shooter"),
    ])]
    
cast_magic_black_hold = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_black_hold", ":shooter"),
    ])]
   
cast_magic_summon_undead = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_summon_undead", ":shooter"),
    ])]
    
cast_magic_summon_undead_weak = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (store_trigger_param_1, ":shooter"),(gt,":shooter",-1),(assign,":caster", ":shooter"),
      (copy_position,pos5,pos52),
      (assign,":spawn_troop_id",0),
      (store_random_in_range, ":r", 0, 3),
      (try_begin),
        (eq, ":r", 0),
        (store_random_in_range, ":spawn_troop_id", "trp_se_tribesman", "trp_zombie_5"),
      (else_try),
        (eq, ":r", 1),
        (store_random_in_range, ":spawn_troop_id", "trp_draugr_1", "trp_zombie_5"),
      (else_try),
        (store_random_in_range, ":spawn_troop_id", "trp_skeleton_spearman", "trp_skeleton_cav"),
      (try_end),
      (call_script,"script_cf_agent_spawn_agent_to_pos51", ":caster", ":spawn_troop_id", 1),
    ])]


cast_magic_death_cloud = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_death_cloud", ":shooter"),
    ])]
    
cast_magic_death_cloud_2 = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_death_cloud_2", ":shooter"),
    ])]
    
cast_magic_deep_freeze = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_deep_freeze", ":shooter"),
    ])]

cast_magic_summon_blade = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_summon_blade", ":shooter"),
    ])]
    
cast_magic_soul_Leech = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_soul_Leech", ":shooter"),
    ])]
    
   
cast_magic_Dispel_Magic = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_Dispel_Magic", ":shooter"),
    ])]

cast_magic_frozen_ground = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_frozen_ground", ":shooter"),
    ])]

cast_magic_Frost_cloud = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_Frost_cloud", ":shooter"),
    ])]
    
cast_magic_Frost_cloudr = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_Frost_cloudr", ":shooter"),
    ])]
        
cast_magic_frozen_orb = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_frozen_orb", ":shooter"),
    ])]
    
cast_magic_blizzard = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_blizzard", ":shooter"),
    ])]
    
cast_magic_ice_ray_dummy = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_ice_ray_dummy", ":shooter"),
    ])]

cast_magic_ice_ray = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_ice_ray", ":shooter"),
    ])]

cast_magic_DEADLY_COLD = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_DEADLY_COLD", ":shooter"),
    ])]


cast_magic_lightningball = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_lightningball", ":shooter"),
    ])]

cast_magic_lightning_burst = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_lightning_burst", ":shooter"),
    ])]
    
cast_magic_summon_Soulhunter = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_summon_Soulhunter", ":shooter"),
    ])]

cast_magic_Petrification = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_Petrification", ":shooter"),
    ])]
    
cast_magic_summon_demon = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_summon_demon", ":shooter"),
    ])]
    

cast_magic_summon_demon_k = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_summon_demon_k", ":shooter"),
    ])]
cast_magic_summon_demon_t = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_summon_demon_t", ":shooter"),
    ])]
cast_magic_summon_demon_s = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_summon_demon_s", ":shooter"),
    ])]
cast_magic_summon_demon_n = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_summon_demon_n", ":shooter"),
    ])]
    
    
cast_magic_armageddon = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_armageddon", ":shooter"),
    ])]
    
cast_magic_column_of_fire = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_column_of_fire", ":shooter"),
    ])]
    
cast_magic_heaven_fist = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_heaven_fist", ":shooter"),
    ])]
    
    
cast_magic_glean_magic = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_glean_magic", ":shooter"),
    ])]
    
cast_magic_treason_of_tzeentch = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_treason_of_tzeentch", ":shooter"),
    ])]
cast_magic_infernal_gateway = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_infernal_gateway", ":shooter"),
    ])]
    
    
cast_magic_acquiescence = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_acquiescence", ":shooter"),
    ])]
cast_magic_pavane_of_slaanesh = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_pavane_of_slaanesh", ":shooter"),
    ])]
cast_magic_hysterical_frenzy = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_hysterical_frenzy", ":shooter"),
    ])]
cast_magic_phantasmogoria = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_phantasmogoria", ":shooter"),
    ])]
cast_magic_phantom_forces = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_phantom_forces", ":shooter"),
    ])]
cast_magic_miasma_of_pestilence = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_miasma_of_pestilence", ":shooter"),
    ])]
cast_magic_blight_boil = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_blight_boil", ":shooter"),
    ])]
cast_magic_blades_of_putrefaction = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_blades_of_putrefaction", ":shooter"),
    ])]
cast_magic_fleshy_abundance = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_fleshy_abundance", ":shooter"),
    ])]
    
blue_fire_of_tzeentch_dummy = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
              
      (try_begin),
        (assign,":max_range",200),
        (assign,":damage",100),
      (try_end),
      
      (try_for_agents,":possable_agent"),
        (agent_is_alive,":possable_agent"),
        (this_or_next|agent_is_ally,":shooter"),
        (agent_is_ally,":possable_agent"),
        (this_or_next|neg|agent_is_ally,":possable_agent"),
        (neg|agent_is_ally,":shooter"),
        (agent_get_position,pos3,":possable_agent"),
        (get_distance_between_positions,":dist",pos5,pos3),
        (le,":dist",":max_range"),
        (assign,":agent",":possable_agent"),
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":damage", thunder, 5, 5),
      (try_end),
    ])]

stream_of_corruption_dummy = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
              
      (try_begin),
        (assign,":max_range",200),
        (assign,":damage",100),
      (try_end),
      
      (try_for_agents,":possable_agent"),
        (agent_is_alive,":possable_agent"),
        (this_or_next|agent_is_ally,":shooter"),
        (agent_is_ally,":possable_agent"),
        (this_or_next|neg|agent_is_ally,":possable_agent"),
        (neg|agent_is_ally,":shooter"),
        (agent_get_position,pos3,":possable_agent"),
        (get_distance_between_positions,":dist",pos5,pos3),
        (le,":dist",":max_range"),
        (assign,":agent",":possable_agent"),
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":damage", poison, 5, 5),
      (try_end),
    ])]
    
lash_of_slaanesh_dummy = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
              
      (try_begin),
        (assign,":max_range",200),
        (assign,":damage",100),
      (try_end),
      
      (try_for_agents,":possable_agent"),
        (agent_is_alive,":possable_agent"),
        (this_or_next|agent_is_ally,":shooter"),
        (agent_is_ally,":possable_agent"),
        (this_or_next|neg|agent_is_ally,":possable_agent"),
        (neg|agent_is_ally,":shooter"),
        (agent_get_position,pos3,":possable_agent"),
        (get_distance_between_positions,":dist",pos5,pos3),
        (le,":dist",":max_range"),
        (assign,":agent",":possable_agent"),
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":damage", wound, 5, 5),
      (try_end),
    ])]


cast_magic_teleport = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (assign,":damage",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
            
      (assign, ":cost_stamina", 15),
      (try_begin),
        (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
        (ge, ":stamina", ":cost_stamina"),
        (val_sub, ":stamina", ":cost_stamina"),
        (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
      (else_try),
        (assign, ":power", 0),
      (try_end),
            
      (try_begin),
        (assign,":max_range",100),
        #(assign,":damage",60),
        (assign,":damage",30),
        (store_random_in_range, ":randon_damage", 25, 36),
        (store_mul,":range_add",":power", 20),
        (store_mul,":damage_add",":power", ":randon_damage"),
        (val_add,":max_range",":range_add"),
        (val_add,":damage",":damage_add"),
      (try_end),
      
      (try_begin),
        (eq, ":weapon", "itm_bishop_staff"),
        (store_mul,":damage_add",":power", 10),
        (val_add,":damage",":damage_add"),
      (else_try),
        (eq, ":weapon", "itm_bishop_staff_2"),
        (store_mul,":damage_add",":power", 20),
        (val_add,":damage",":damage_add"),
      (try_end),
      
      (try_for_agents,":possable_agent"),
        (gt,":damage",0),
        (gt,":power",0),
        (agent_is_alive,":possable_agent"),
        (this_or_next|agent_is_ally,":shooter"),
        (agent_is_ally,":possable_agent"),
        (this_or_next|neg|agent_is_ally,":possable_agent"),
        (neg|agent_is_ally,":shooter"),

        (agent_get_position,pos3,":possable_agent"),
        (copy_position, pos4, pos3),
        
        (get_distance_between_positions,":dist",pos5,pos3),
        (le,":dist",":max_range"),
        
        (assign,":agent",":possable_agent"),
        (val_add,":power",-1),
        
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":damage", power_jump, ":power", ":power"),
        (agent_set_slot, ":agent", slot_agent_special_damage_type, power_jump),
        (agent_set_slot, ":agent", slot_agent_special_damage_power, 5),
        (agent_set_slot, ":agent", slot_agent_special_damage_time, ":power"),
      (try_end),
    ])]

cast_magic_tzeentch_firestorm = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_tzeentch_firestorm", ":shooter"),
    ])]
cast_magic_pink_fire_of_tzeentch = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos52,pos1),
      (call_script, "script_cf_burst_pos52_magic_pink_fire_of_tzeentch", ":shooter"),
    ])]


