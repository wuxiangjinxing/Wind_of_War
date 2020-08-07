from module_constants import *
from ID_factions import *
from header_items import  *
from header_operations import *
from header_troops import *
from header_triggers import *
from header_skills import *
####################################################################################################################
#  Each item record contains the following fields:
#  1) Item id: used for referencing items in other files.
#     The prefix itm_ is automatically added before each item id.
#  2) Item name. Name of item as it'll appear in inventory window
#  3) List of meshes.  Each mesh record is a tuple containing the following fields:
#    3.1) Mesh name.
#    3.2) Modifier bits that this mesh matches.
#     Note that the first mesh record is the default.
#  4) Item flags. See header_items.py for a list of available flags.
#  5) Item capabilities. Used for which animations this item is used with. See header_items.py for a list of available flags.
#  6) Item value.
#  7) Item stats: Bitwise-or of various stats about the item such as:
#      weight, abundance, difficulty, head_armor, body_armor,leg_armor, etc...
#  8) Modifier bits: Modifiers that can be applied to this item.
#  9) [Optional] Triggers: List of simple triggers to be associated with the item.
#  10) [Optional] Factions: List of factions that item can be found as merchandise.
####################################################################################################################

# Some constants for ease of use.
imodbits_none = 0
# CC
imodbits_horse_basic = imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_heavy|imodbit_stubborn|imodbit_timid
# CC
imodbits_horse_adv = imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_heavy|imodbit_stubborn|imodbit_timid|imodbit_champion

imodbits_horse_armor = imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_heavy|imodbit_stubborn|imodbit_timid|imodbit_reinforced|imodbit_lordly

imodbits_cloth  = imodbit_tattered| imodbit_ragged| imodbit_sturdy| imodbit_thick|imodbit_well_made|imodbit_superb| imodbit_hardened|imodbit_lordly

imodbits_armor  = imodbit_rusty| imodbit_battered| imodbit_sturdy| imodbit_crude| imodbit_thick|imodbit_well_made|imodbit_superb| imodbit_hardened| imodbit_reinforced|imodbit_lordly
imodbits_plate  = imodbit_cracked| imodbit_rusty| imodbit_sturdy| imodbit_battered| imodbit_crude| imodbit_thick|imodbit_well_made|imodbit_superb| imodbit_hardened| imodbit_reinforced|imodbit_lordly

imodbits_good_plate  = imodbit_sturdy|imodbit_well_made|imodbit_superb|imodbit_thick|imodbit_hardened|imodbit_reinforced|imodbit_lordly





imodbits_polearm = imodbit_cracked| imodbit_bent| imodbit_balanced| imodbit_deadly| imodbit_fine|imodbit_sharp|imodbit_tempered|imodbit_masterwork
imodbits_shield  = imodbit_cracked| imodbit_battered|imodbit_thick| imodbit_reinforced| imodbit_heavy| imodbit_lordly
imodbits_sword   = imodbit_rusty| imodbit_chipped| imodbit_balanced|imodbit_tempered| imodbit_heavy| imodbit_fine| imodbit_powerful| imodbit_sharp
imodbits_sword_high   = imodbit_rusty| imodbit_chipped| imodbit_balanced|imodbit_tempered|imodbit_masterwork| imodbit_deadly| imodbit_sharp
imodbits_axe   = imodbit_rusty| imodbit_chipped| imodbit_heavy| imodbit_fine| imodbit_tempered| imodbit_deadly| imodbit_strong
imodbits_mace   = imodbit_rusty| imodbit_chipped| imodbit_heavy| imodbit_fine| imodbit_sharp| imodbit_tempered| imodbit_strong
imodbits_pick   = imodbit_rusty| imodbit_chipped| imodbit_heavy| imodbit_fine| imodbit_balanced| imodbit_powerful| imodbit_strong
imodbits_bow = imodbit_cracked| imodbit_bent| imodbit_strong|imodbit_masterwork| imodbit_fine|imodbit_tempered| imodbit_deadly| imodbit_sharp
imodbits_crossbow = imodbit_cracked| imodbit_bent| imodbit_heavy| imodbit_masterwork| imodbit_large_bag| imodbit_fine| imodbit_powerful| imodbit_deadly
#imodbits_missile   = imodbit_bent| imodbit_large_bag| imodbit_fine| imodbit_balanced|imodbit_masterwork
imodbits_missile   = imodbit_bent| imodbit_large_bag| imodbit_fine

imodbits_thrown   = imodbit_bent| imodbit_heavy| imodbit_balanced| imodbit_large_bag
imodbits_thrown_minus_heavy = imodbit_bent| imodbit_heavy| imodbit_fine| imodbit_deadly| imodbit_large_bag| imodbit_strong
imodbits_thrown_2   =   imodbit_heavy| imodbit_large_bag| imodbit_fine| imodbit_deadly| imodbit_strong
imodbits_gun = imodbit_cracked| imodbit_rusty|imodbit_masterwork|imodbit_tempered| imodbit_large_bag| imodbit_sharp| imodbit_fine| imodbit_balanced| imodbit_deadly| imodbit_strong
imodbits_magic_staff = imodbit_cracked|imodbit_fine|imodbit_sharp|imodbit_tempered|imodbit_balanced|imodbit_masterwork| imodbit_large_bag

imodbits_horse_good = imodbit_spirited|imodbit_heavy 
imodbits_good   = imodbit_sturdy| imodbit_thick| imodbit_hardened| imodbit_reinforced| imodbit_lordly
imodbits_bad    = imodbit_rusty| imodbit_chipped| imodbit_tattered| imodbit_ragged| imodbit_cracked| imodbit_bent

imodbits_cloth_2   = imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite|imodbit_masterwork|imodbit_tattered|imodbit_ragged|imodbit_rough|imodbit_sturdy

itc_claymore       = itc_cut_two_handed|itc_parry_two_handed|itcf_thrust_polearm|itcf_carry_sword_back| itcf_horseback_slashright_onehanded| itcf_horseback_overswing_left_onehanded
itc_side_sword     = itcf_thrust_onehanded| itc_parry_onehanded| itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded| itcf_horseback_thrust_onehanded

we_faction = [fac_kingdom_1, fac_kingdom_4, fac_kingdom_7]
ee_faction = [fac_kingdom_2, fac_kingdom_3, fac_kingdom_8, fac_kingdom_14]
ne_faction = [fac_kingdom_4, fac_kingdom_10, fac_kingdom_13]
se_faction = [fac_kingdom_5, fac_kingdom_8, fac_kingdom_11]
me_faction = [fac_kingdom_2, fac_kingdom_8]
arab_factions = [fac_kingdom_6, fac_kingdom_9, fac_kingdom_12]
tatar_faction = [fac_kingdom_3, fac_kingdom_9]
euro_factions = [fac_kingdom_1, fac_kingdom_2, fac_kingdom_4, fac_kingdom_5, fac_kingdom_7, fac_kingdom_8, fac_kingdom_10, fac_kingdom_11]
throw_factions = [fac_kingdom_2, fac_kingdom_3,fac_kingdom_4, fac_kingdom_8, fac_kingdom_9,fac_kingdom_10, fac_kingdom_11, fac_kingdom_12, fac_kingdom_14]
firearm_factions = [fac_kingdom_2, fac_kingdom_5, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_11, fac_kingdom_12, fac_dwarf]
crossbow_factions = [fac_kingdom_1, fac_kingdom_5, fac_kingdom_7, fac_kingdom_8, fac_kingdom_9, fac_kingdom_11, fac_kingdom_12, fac_kingdom_13]
bow_factions = [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_6, fac_kingdom_8, fac_kingdom_9, fac_kingdom_12, fac_kingdom_14]
all_factions = [fac_kingdom_4,fac_kingdom_5,fac_kingdom_6,fac_kingdom_7,fac_kingdom_8,fac_kingdom_9,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_13,fac_kingdom_1,fac_kingdom_2,fac_kingdom_3, fac_kingdom_14]

cloth_tier_0 = weight(1)|abundance(30)|head_armor(0)|body_armor(10)|leg_armor(5)|difficulty(0)
cloth_tier_1 = weight(5)|abundance(30)|head_armor(0)|body_armor(17)|leg_armor(10)|difficulty(1)
cloth_tier_2 = weight(11)|abundance(40)|head_armor(0)|body_armor(21)|leg_armor(10)|difficulty(3)
cloth_tier_3 = weight(11)|abundance(50)|head_armor(0)|body_armor(25)|leg_armor(14)|difficulty(4)
cloth_tier_4 = weight(11)|abundance(60)|head_armor(0)|body_armor(31)|leg_armor(14)|difficulty(5)

mail_armor_tier_1 = weight(16)|abundance(50)|head_armor(0)|body_armor(33)|leg_armor(14)|difficulty(6)
mail_armor_tier_2 = weight(18)|abundance(65)|head_armor(0)|body_armor(41)|leg_armor(17)|difficulty(6)
mail_armor_tier_3 = weight(21)|abundance(70)|head_armor(0)|body_armor(50)|leg_armor(20)|difficulty(9)
mail_armor_tier_4 = weight(26)|abundance(65)|head_armor(0)|body_armor(58)|leg_armor(24)|difficulty(12)
mail_armor_tier_5 = weight(30)|abundance(50)|head_armor(0)|body_armor(64)|leg_armor(29)|difficulty(15)

lamellar_armor_tier_1 = weight(18)|abundance(70)|head_armor(0)|body_armor(48)|leg_armor(17)|difficulty(7)
lamellar_armor_tier_2 = weight(25)|abundance(80)|head_armor(0)|body_armor(63)|leg_armor(26)|difficulty(12)
lamellar_armor_tier_3 = weight(30)|abundance(60)|head_armor(0)|body_armor(68)|leg_armor(32)|difficulty(15)
lamellar_armor_tier_4 = weight(35)|abundance(40)|head_armor(0)|body_armor(73)|leg_armor(35)|difficulty(18)

breastplate_tier_0 = weight(12)|abundance(40)|head_armor(0)|body_armor(38)|leg_armor(10)|difficulty(10)
breastplate_tier_1 = weight(16)|abundance(50)|head_armor(0)|body_armor(48)|leg_armor(10)|difficulty(11)
breastplate_tier_2 = weight(20)|abundance(60)|head_armor(0)|body_armor(57)|leg_armor(10)|difficulty(12)
breastplate_tier_2e = weight(20)|abundance(60)|head_armor(0)|body_armor(57)|leg_armor(22)|difficulty(12)
breastplate_tier_3 = weight(20)|abundance(70)|head_armor(0)|body_armor(64)|leg_armor(23)|difficulty(13)
breastplate_tier_4 = weight(25)|abundance(60)|head_armor(0)|body_armor(70)|leg_armor(24)|difficulty(14)
breastplate_tier_5 = weight(25)|abundance(50)|head_armor(0)|body_armor(75)|leg_armor(25)|difficulty(15)

full_plate_armor_tier_1 = weight(25)|abundance(50)|head_armor(0)|body_armor(65)|leg_armor(30)|difficulty(13)
full_plate_armor_tier_2 = weight(25)|abundance(60)|head_armor(0)|body_armor(71)|leg_armor(35)|difficulty(15)

full_plate_armor_tier_2e = weight(25)|abundance(50)|head_armor(0)|body_armor(73)|leg_armor(37)|difficulty(15)

full_plate_armor_tier_3 = weight(30)|abundance(40)|head_armor(0)|body_armor(76)|leg_armor(40)|difficulty(17)
full_plate_armor_tier_4 = weight(30)|abundance(20)|head_armor(0)|body_armor(80)|leg_armor(45)|difficulty(18)

merc_body_armor = itp_merchandise|itp_type_body_armor|itp_covers_legs
itp_type_fullhelm = itp_type_head_armor|itp_civilian|itp_covers_head
itp_type_full_body_armor = itp_civilian|itp_covers_head|itp_unique|itp_type_body_armor|itp_covers_legs|itp_replaces_helm|itp_replaces_shoes
itp_type_half_body_armor = itp_civilian|itp_unique|itp_type_body_armor|itp_covers_legs|itp_replaces_shoes


def shield_hit_points(x):
  return hit_points(x/2)


## CC
missile_distance_trigger = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter_agent"),
      #(store_trigger_param_2, ":hit_object_type"),
      (agent_get_wielded_item, ":weapon", ":shooter_agent", 0),
      (try_begin),
        (eq, ":weapon", "itm_auriels_bow"),
        (copy_position,pos51,pos1),
        (call_script, "script_magic_deliver_area_damage", ":shooter_agent", 200, 5, 14),
      (try_end),
      
      #(neg|eq, ":weapon", "itm_drawf_musket_8barrel1"),
      #(neg|eq, ":weapon", "itm_rat_musket_8barrel"),
      
      #(eq, "$g_report_shot_distance", 1),
      #(get_player_agent_no, ":player_agent"),
      #(try_begin),
      #  (eq, ":shooter_agent", ":player_agent"),
      #  (eq, ":hit_object_type", 1), # 1 = hostile agent
      #  (agent_get_position, pos2, ":shooter_agent"),
      #  (agent_get_horse, ":horse_agent", ":player_agent"),
      #  (try_begin),
      #    (gt, ":horse_agent", -1),
      #    (position_move_z, pos2, 200),
      #  (else_try),
      #    (position_move_z, pos2, 150),
      #  (try_end),
      #  (get_distance_between_positions, ":distance", pos1, pos2),
      #  (store_div, reg61, ":distance", 100),
      #  (store_mod, reg62, ":distance", 100),
      #  (val_div, reg62, 10),
      #  (str_store_string, s1, "@{reg61}.{reg62}"),
      #  (display_message, "@Shot distance: {s1} meters.", 0xCCCCCC),
      #(try_end),
      
    ])
    ]
       
shield_broken_trigger_2 = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter_agent"),
      (copy_position, pos10, pos1),
      (try_begin),
        (assign, ":agent", -1),
        (try_for_agents, ":possable_agent"),
          (eq, ":agent", -1),
          (neg|eq, ":shooter_agent", ":possable_agent"),
          (agent_is_alive, ":possable_agent"),
          (agent_is_human, ":possable_agent"),
          
          (this_or_next|agent_is_ally,":shooter"),
          (agent_is_ally,":possable_agent"),
          (this_or_next|neg|agent_is_ally,":possable_agent"),
          (neg|agent_is_ally,":shooter"),
          
          (agent_get_position, pos2, ":possable_agent"),
          (position_move_z, pos2, 130),
          (neg|position_is_behind_position, 10, 2),
          (get_distance_between_positions, ":var_6", pos10, pos2),
          (neg|ge, ":var_6", 200),
          (agent_get_wielded_item, ":has_shield", ":possable_agent", 1),
          (ge, ":has_shield", 1),
          (agent_get_defend_action, ":var_8", ":possable_agent"),
          (ge, ":var_8", 1),
          (assign, ":agent", ":possable_agent"),
        (try_end),
        (try_begin),
          (ge, ":agent", 0),
          (ge, ":has_shield", 1),
          (agent_play_sound, ":agent", "snd_shield_broken"),
          (agent_get_horse, ":var_9", ":agent"),
          (try_begin),
            (ge, ":var_9", 0),
            (agent_set_animation, ":agent", "anim_strike3_abdomen_front", 1),
          (else_try),
            (agent_set_animation, ":agent", "anim_strike3_abdomen_front", 0),
          (try_end),
          (agent_unequip_item, ":agent", ":has_shield"),
        (try_end),
      (try_end),
    ])]
       
# trigger param 1 = defender agent_id
# trigger param 2 = attacker agent_id
# trigger param 3 = inflicted damage
# trigger param 4 = weapon item_id (ranged weapon in case of ranged attack)
# trigger param 5 = missile item_id (ammo in case of ranged attack)
shield_hit_trigger = [
  (ti_on_shield_hit, 
    [
      (store_trigger_param, ":defender_agent", 1),
      #(store_trigger_param, ":attacker_agent", 2),
      (store_trigger_param, ":inflicted_damage", 3),
      (store_trigger_param, ":weapon_id", 4),
      (store_trigger_param, ":missile_id", 5),
      

      (assign, ":dest_damage", ":inflicted_damage"),
      (try_begin),
        (try_begin),
          (gt, ":weapon_id",0),
          (this_or_next|eq, ":weapon_id", "itm_ebony_bow"),
          (this_or_next|eq, ":weapon_id","itm_granata"),
          (this_or_next|eq, ":weapon_id","itm_granata_medium"),
          (this_or_next|eq, ":weapon_id","itm_granata_small"),
          (this_or_next|eq, ":weapon_id","itm_light_throwing_axes"),
          (this_or_next|eq, ":weapon_id","itm_throwing_axes"),
          (this_or_next|eq, ":weapon_id","itm_heavy_throwing_axes"),
          (this_or_next|eq, ":weapon_id","itm_mjolnir"),
          (this_or_next|eq, ":weapon_id","itm_throwing_gungnir"),
          (this_or_next|eq, ":weapon_id","itm_holy_granata"),
          (this_or_next|eq, ":weapon_id","itm_granata_poison"),
          (this_or_next|eq, ":weapon_id","itm_troll_stones"),
          (this_or_next|eq, ":weapon_id","itm_skeleton_throwing_pike"),
          (this_or_next|eq, ":weapon_id","itm_chaos_throw1"),
          (this_or_next|eq, ":weapon_id","itm_chaos_throw2"),
          (this_or_next|eq, ":weapon_id","itm_ebony_throwing_pike"),
          (eq, ":weapon_id","itm_sissofbattle_holy_granata"),
          (val_mul, ":dest_damage", 10),
        (try_end),
        (try_begin),
          (gt, ":missile_id",0),
          (this_or_next|eq, ":missile_id","itm_cartridges_cannon"),
          (this_or_next|eq, ":missile_id","itm_cartridges_cannon_1"),
          (this_or_next|eq, ":missile_id","itm_cartridges_sissofbattle_bolter"),
          (this_or_next|eq, ":missile_id","itm_cartridges_sissofbattle_bolter_2"),
          (this_or_next|eq, ":missile_id","itm_elven_arrows_fire"),
          (this_or_next|eq, ":missile_id","itm_elven_arrows_explove"),
          (eq, ":missile_id","itm_demon_arrow"),
          (val_mul, ":dest_damage", 10),
        (else_try),
          (gt, ":missile_id",0),
          (this_or_next|eq, ":missile_id","itm_swadian_steel_bolts"),
          (this_or_next|eq, ":missile_id","itm_cartridges_thrust"),
          (this_or_next|eq, ":missile_id","itm_van_helsing_crossbow_bolt"),
          (eq, ":missile_id","itm_cartridges_sissofbattle_holy"),
          (val_mul, ":dest_damage", 4),
        (else_try),
          (gt, ":missile_id",0),
          (this_or_next|eq, ":missile_id","itm_sldequiver"),
          (this_or_next|eq, ":missile_id","itm_cartridges_flame"),
          (this_or_next|eq, ":missile_id","itm_cartridges_sissofbattle_flame"),
          (eq, ":missile_id","itm_cartridges_sissofbattle_flame_2"),
          (val_mul, ":dest_damage", 100),
        (try_end),
      
        (get_player_agent_no, ":player_agent"),
        (try_begin),
          (eq, ":defender_agent", ":player_agent"),
          (options_get_damage_to_player, ":damage_ratio"),
          (try_begin),
            (eq, ":damage_ratio", 0),
            (val_div, ":dest_damage", 4),
          (else_try),
            (eq, ":damage_ratio", 1),
            (val_div, ":dest_damage", 2),
          (try_end),
        (try_end),
        (set_trigger_result, ":dest_damage"),
        # message
        #(neg|game_in_multiplayer_mode),
        #(eq, "$g_report_shot_distance", 1),
        #(try_begin),
        #  (eq, ":defender_agent", ":player_agent"),
        #  (assign, reg4, ":dest_damage"),
        #  (display_message, "@Shield received {reg4} damage."),
        #(else_try),
        #  (eq, ":attacker_agent", ":player_agent"),
        #  (assign, reg4, ":dest_damage"),
        #  (display_message, "@Delivered {reg4} damage to shield."),
        #(try_end),
      (try_end),
      
    ])]
## CC
   
Akarat_hit_trigger = [
  (ti_on_shield_hit, 
    [
      (store_trigger_param, ":defender_agent", 1),
      #(store_trigger_param, ":attacker_agent", 2),

      (store_random_in_range, ":receiver_agent", 0,4),
      
      (try_begin),
        (eq, ":receiver_agent", 0),
        (agent_get_slot, ":timer_2", ":defender_agent", slot_agent_special_ability_extra_cooldown),
        (gt, ":timer_2", 0),
        (val_sub, ":timer_2", 1),
        (agent_set_slot, ":defender_agent", slot_agent_special_ability_extra_cooldown, ":timer_2"),
      (try_end),
      
      (try_begin),
        (eq, ":receiver_agent", 1),
        (agent_get_slot, ":timer_2", ":defender_agent", slot_agent_special_ability_cooldown),
        (gt, ":timer_2", 0),
        (val_sub, ":timer_2", 1),
        (agent_set_slot, ":defender_agent", slot_agent_special_ability_cooldown, ":timer_2"),
      (try_end),

      (try_begin),
        (eq, ":receiver_agent", 2),
        (agent_get_slot, ":timer_2", ":defender_agent", slot_agent_special_ability_passiv_cooldown),
        (gt, ":timer_2", 0),
        (val_sub, ":timer_2", 1),
        (agent_set_slot, ":defender_agent", slot_agent_special_ability_passiv_cooldown, ":timer_2"),
      (try_end),

    ])]

Hellskull_hit_trigger = [
  (ti_on_shield_hit, 
    [
      (store_trigger_param, ":defender_agent", 1),

      (try_begin),
        (agent_get_slot, ":stamina", ":defender_agent", slot_agent_stamina),
        (val_add, ":stamina", 1),
        (val_clamp, ":stamina", 0, 101),
        (agent_set_slot, ":defender_agent", slot_agent_stamina, ":stamina"),
      (try_end),
      (try_begin),
        (store_agent_hit_points, ":hp", ":defender_agent", 1),
        (val_add, ":hp", 10),
        (agent_set_hit_points, ":defender_agent", ":hp", 1),
      (try_end),
    ])]

freeze_shield_hit_trigger = [
  (ti_on_shield_hit, 
    [
      #(store_trigger_param, ":defender_agent", 1),
      (store_trigger_param, ":attacker_agent", 2),
      (try_begin),
        (gt, ":attacker_agent", -1),
        (agent_is_human, ":attacker_agent"),
        (agent_set_slot, ":attacker_agent", slot_agent_special_damage_type, freeze),
        (agent_set_slot, ":attacker_agent", slot_agent_special_damage_time, 5),
        (agent_set_slot, ":attacker_agent", slot_agent_special_damage_power, 1),
      (try_end),
    ])]
    
    
dragon_shield_2_hit_trigger = [
  (ti_on_shield_hit, 
    [
      #(store_trigger_param, ":defender_agent", 1),
      (store_trigger_param, ":attacker_agent", 2),
      (store_random_in_range, ":receiver_agent", 0,4),
      (try_begin),
        (eq, ":receiver_agent", 2),
        (gt, ":attacker_agent", -1),
        (agent_is_human, ":attacker_agent"),
        (agent_set_slot, ":attacker_agent", slot_agent_special_ability_affect_type, dragon_voice),
        (agent_set_slot, ":attacker_agent", slot_agent_special_ability_affect_time, 2),
      (try_end),
    ])]
    
    
tynan_dagger_trigger = [
  (ti_on_shield_hit, 
    [

      (store_trigger_param, ":receiver_agent", 1),
      #(store_trigger_param, ":shooter_agent", 2),
      #(store_trigger_param, ":has_shield", 4),
      
        (try_begin),
          (ge, ":receiver_agent", 0),
          #(eq, ":has_shield", "itm_tynan_dagger"),
          (agent_play_sound, ":receiver_agent", "snd_shield_hit_wood_wood"),
          (agent_get_horse,":horse",":receiver_agent"),
          (neg|gt,":horse",0),
          (call_script,"script_cf_agent_shield_bash",":receiver_agent",-1),
        (try_end),
    ])]
        
powergun_trigger = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt, ":weapon", 0),
      (assign,":max_damage",0),
      (copy_position,pos51,pos1),
      (try_begin),
        (eq, ":weapon", "itm_colt1855"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 150, 6, 16),   
        (assign,":max_damage",3),
      (else_try),
        (this_or_next|eq, ":weapon", "itm_drawf_musket_8barrel2"),
        (eq, ":weapon", "itm_hand_cannon"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 200, 10, 0),   
        (assign,":max_damage",2),
      (else_try),
        (eq, ":weapon", "itm_hand_cannon_2"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 250, 9, 0),     
        (assign,":max_damage",4),
        (eq, ":weapon", "itm_hand_cannon_3"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 300, 8, 0),   
        (assign,":max_damage",6),
      (else_try),
        (eq, ":weapon", "itm_hand_cannon_4"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 350, 7, 0),     
        (assign,":max_damage",8),
      (else_try),
        (eq, ":weapon", "itm_sissofbattle_A295_heavy"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 350, 7, 0),     
        (assign,":max_damage",8),
      (else_try),
        (this_or_next|eq, ":weapon", "itm_dwarf_pistol_3"),
        (this_or_next|eq, ":weapon", "itm_drawf_flame_caster"),
        (eq, ":weapon", "itm_musket_hand_gun"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 150, 10, 15),
        (assign,":max_damage",1),
      (else_try),
        (eq, ":weapon", "itm_zlmg"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 100, 5, 16),        
        (assign,":max_damage",-1),
      (else_try),
        (eq, ":weapon", "itm_musket_rifle"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 200, 4, 16),    
        (assign,":max_damage",-1),
      (else_try),
        (this_or_next|eq, ":weapon", "itm_flintlock_pistol_elite_1"),
        (this_or_next|eq, ":weapon", "itm_flintlock_pistol_elite_2"),
        (eq, ":weapon", "itm_flintlock_pistol_elite"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 100, 3, 15),        
      (try_end),
      
        (position_get_distance_to_ground_level, ":distance", pos51),
        (try_begin),
          (lt, ":distance", 0),
          (position_set_z_to_ground_level, pos51),
          (position_move_z, pos51, 200),
        (try_end),                
      (try_begin), 
        (gt,":max_damage",0),
        #(position_move_z, pos52, 100),
        (try_for_range, ":unused", 0, ":max_damage"),
          (copy_position, pos2, pos51),
          (store_random_in_range, ":x_offset", 15, 61),#Random Rotation of X
          (position_rotate_x, pos2, ":x_offset"),    
          (store_random_in_range, ":y_offset", 1, 361),#Random Rotation of Y
          (position_rotate_y, pos2, ":y_offset"),    
          (store_random_in_range, ":z_offset", 1, 361),#Random Rotation of Z
          (position_rotate_z, pos2, ":z_offset"),   
          (set_fixed_point_multiplier,10),
          (add_missile, ":shooter", pos2, 50, ":weapon", 0, "itm_cannon_dummy", 0),
        (try_end), 
      (try_end),
        
    ])]
   
powergun_trigger3 = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt, ":weapon", 0),
      (copy_position,pos51,pos1),
      (try_begin),
        (eq, ":weapon", "itm_colt1855"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 150, 6, 16),   
      (else_try),
        (this_or_next|eq, ":weapon", "itm_drawf_musket_8barrel2"),
        (eq, ":weapon", "itm_hand_cannon"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 300, 7, 0),   
      (else_try),
        (eq, ":weapon", "itm_hand_cannon_2"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 400, 7, 0),     
      (else_try),
        (eq, ":weapon", "itm_hand_cannon_3"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 500, 7, 0),   
      (else_try),
        (eq, ":weapon", "itm_hand_cannon_4"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 600, 7, 0),     
      (else_try),
        (eq, ":weapon", "itm_sissofbattle_A295_heavy"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 400, 7, 0),     
      (else_try),
        (this_or_next|eq, ":weapon", "itm_dwarf_pistol_3"),
        (this_or_next|eq, ":weapon", "itm_drawf_flame_caster"),
        (eq, ":weapon", "itm_musket_hand_gun"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 250, 10, 15),
      (else_try),
        (eq, ":weapon", "itm_zlmg"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 100, 5, 16),        
      (else_try),
        (eq, ":weapon", "itm_musket_rifle"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 200, 4, 16),    
      (else_try),
        (this_or_next|eq, ":weapon", "itm_flintlock_pistol_elite_1"),
        (this_or_next|eq, ":weapon", "itm_flintlock_pistol_elite_2"),
        (eq, ":weapon", "itm_flintlock_pistol_elite"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 100, 3, 15),        
      (try_end),
              
    ])]
   
   
powergun_trigger2 = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt, ":weapon", 0),
      (assign,":max_damage",0),
      (copy_position,pos51,pos1),
      (try_begin),
        (eq, ":weapon", "itm_colt1855"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 150, 6, 16),   
        (assign,":max_damage",1),
      (else_try),
        (this_or_next|eq, ":weapon", "itm_drawf_musket_8barrel2"),
        (eq, ":weapon", "itm_hand_cannon"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 200, 8, 15),   
        (assign,":max_damage",2),
      (else_try),
        (eq, ":weapon", "itm_hand_cannon_2"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 250, 8, 15),     
        (assign,":max_damage",3),
      (else_try),
        (eq, ":weapon", "itm_hand_cannon_3"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 300, 9, 15),   
        (assign,":max_damage",4),
      (else_try),
        (eq, ":weapon", "itm_hand_cannon_4"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 400, 10, 15),     
        (assign,":max_damage",5),
      (else_try),
        (eq, ":weapon", "itm_sissofbattle_A295_heavy"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 350, 7, 16),     
      (else_try),
        (this_or_next|eq, ":weapon", "itm_dwarf_pistol_3"),
        (this_or_next|eq, ":weapon", "itm_drawf_flame_caster"),
        (eq, ":weapon", "itm_musket_hand_gun"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 200, 10, 15),
        (assign,":max_damage",2),
      (else_try),
        (eq, ":weapon", "itm_zlmg"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 100, 5, 16),        
        (assign,":max_damage",1),
      (else_try),
        (eq, ":weapon", "itm_musket_rifle"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 200, 4, 16),    
        (assign,":max_damage",1),
      (else_try),
        (this_or_next|eq, ":weapon", "itm_flintlock_pistol_elite_1"),
        (this_or_next|eq, ":weapon", "itm_flintlock_pistol_elite_2"),
        (eq, ":weapon", "itm_flintlock_pistol_elite"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 100, 3, 16),       
        (assign,":max_damage",1),
      (try_end),
      
        (position_get_distance_to_ground_level, ":distance", pos51),
        (try_begin),
          (lt, ":distance", 0),
          (position_set_z_to_ground_level, pos51),
          (position_move_z, pos51, 200),
        (try_end),                
      (try_begin), 
        (gt,":max_damage",0),
        (store_random_in_range,":num_fragments",15,26),
        (val_mul,":num_fragments",":max_damage"),
        (try_for_range, ":unused", 0, ":num_fragments"),
          (copy_position, pos2, pos51),
          (position_move_z,pos2,30),
          (store_random_in_range,":x_change",0,76),
          (store_random_in_range,":z_change",0,361),
          (position_rotate_x, pos2, ":x_change"),
          (position_rotate_z, pos2, ":z_change"),
          (store_random_in_range,":fragment_speed",150,1000),
          (set_fixed_point_multiplier,10),
          (add_missile, ":shooter", pos2, ":fragment_speed", ":weapon", 0, "itm_granata_dummy", 0),
        (try_end), 
      (try_end),
        
    ])]
   
   
powergun_flame_trigger = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt, ":weapon", 0),
      (copy_position,pos51,pos1),
      (try_begin),
        (eq, ":weapon", "itm_colt1855"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 150, 6, 12),   
      (else_try),
        (this_or_next|eq, ":weapon", "itm_drawf_musket_8barrel2"),
        (eq, ":weapon", "itm_hand_cannon"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 150, 10, 12),   
      (else_try),
        (eq, ":weapon", "itm_hand_cannon_2"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 180, 9, 12),     
      (else_try),
        (eq, ":weapon", "itm_hand_cannon_3"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 210, 8, 12),   
      (else_try),
        (eq, ":weapon", "itm_hand_cannon_4"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 240, 7, 12),     
      (else_try),
        (eq, ":weapon", "itm_sissofbattle_A295_heavy"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 240, 7, 12),     
      (else_try),
        (this_or_next|eq, ":weapon", "itm_dwarf_pistol_3"),
        (this_or_next|eq, ":weapon", "itm_drawf_flame_caster"),
        (eq, ":weapon", "itm_musket_hand_gun"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 100, 10, 12),        
      (else_try),
        (eq, ":weapon", "itm_zlmg"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 100, 5, 12),        
      (else_try),
        (eq, ":weapon", "itm_sissofbattle_A295"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 200, 3, 7),    
      (else_try),
        (eq, ":weapon", "itm_sissofbattle_e5"),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 200, 3, 7),        
      (try_end),
    ])]
   
cast_magic_Arcane_Orb = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      
      (assign,":damage",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      

      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
      
      (assign, ":cost_stamina", 40),
      
      (try_begin),
        (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
        (ge, ":stamina", ":cost_stamina"),
        (val_sub, ":stamina", ":cost_stamina"),
        (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
      (else_try),
        (assign, ":power", 0),
      (try_end),
              
      (try_begin),
        (assign,":max_range",200),
        (assign,":damage",200),
        (store_random_in_range, ":randon_damage", 80, 121),
        (store_mul,":range_add",":power", 30),
        (store_mul,":damage_add",":power", ":randon_damage"),
        (val_add,":max_range",":range_add"),
        (store_add,":max_damage",":damage",":damage_add"),
      (try_end),
      (copy_position,pos6,pos5),
      (position_move_z,pos6,300),
      (particle_system_burst, "psys_arcane_explosion", pos6, 5),
      (try_for_agents,":possable_agent"),
        (gt,":damage",0),
        (gt,":power",0),
        (agent_is_alive,":possable_agent"),
        (this_or_next|agent_is_ally,":shooter"),
        (agent_is_ally,":possable_agent"),
        (this_or_next|neg|agent_is_ally,":possable_agent"),
        (neg|agent_is_ally,":shooter"),

        (agent_get_position,pos3,":possable_agent"),
        (get_distance_between_positions,":dist",pos5,pos3),
        (le,":dist",":max_range"),
        (assign,":agent",":possable_agent"),
        
        (val_add,":power",-1),
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":max_damage", thunder, ":power", ":power"),
        (try_begin),
          (agent_has_item_equipped,":shooter","itm_magic_book_2"),
          (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":max_damage", thunder, ":power", ":power"),
        (try_end),
        
        
        (assign,":max_damage",":damage_add"),
      (try_end),
    ])]

cast_magic_black_hold_long = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt,":weapon",0),
      (assign,":damage",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
                                
      (try_begin),
        (assign,":range",100),
        (store_mul,":range_add",":power", 15),
        (store_div,":damage",":power", 4),
        (val_add,":range",":range_add"),
        (val_add,":damage",2),
      (try_end),
              
        (assign,":victim",-1),        
        (try_begin),
          (get_player_agent_no,":player"),
          (neq, ":player",":shooter"),
          (store_trigger_param_2, ":hit_object_type"),
          (neg|eq, ":hit_object_type", 1), # 1 = hostile agent
          (agent_ai_get_look_target, ":target", ":shooter"),
          (gt,":target",0),
          (neg|eq, ":shooter",":player"),
          (agent_is_alive,":target"),
          (assign,":victim",":target"),
        (try_end),
        
        (try_for_agents,":agent"),
          (agent_is_alive,":agent"),
          (agent_is_human,":agent"),
          (eq,":victim",-1),
          
          (this_or_next|agent_is_ally,":shooter"),
          (agent_is_ally,":agent"),
          (this_or_next|neg|agent_is_ally,":agent"),
          (neg|agent_is_ally,":shooter"),
                              
          (agent_get_position, pos2, ":agent"),
          (get_distance_between_positions,":distance",pos2,pos5),
          (le,":distance",":range"),
          (call_script, "script_agent_get_num_companion_nearby", ":agent", 400),
          (assign, ":num_enemies", reg0),
          (this_or_next|le, ":num_enemies", 1),
          (ge, ":num_enemies", 6),
          (assign,":victim",":agent"),
        (try_end),
        (try_begin),
          (ge,":victim",0),
          (agent_get_position, pos5, ":victim"),
        (try_end),
        (copy_position,pos4,pos5),
        (try_for_range,":posz",0,":damage"),
          (try_begin),
            (store_add,":max_damage",":posz",1),
            (ge,":max_damage",":damage"),
            (val_add,":max_damage",1),
            (val_mul,":max_damage",500),
            (position_move_z,pos4,":max_damage"),
            (add_missile, ":shooter", pos4, 0, ":weapon", 0, "itm_magic_arcane_orb", 0),
          (try_end),
          (val_mul,":posz",500),
          (position_move_z,pos4,":posz"),
          (add_missile, ":shooter", pos4, 0, ":weapon", 0, "itm_magic_black_hold_2", 0),
        (try_end),
    ])]
    


cast_magic_black_hold = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      
      (assign,":damage",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      

      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
      
      (assign, ":cost_stamina", 25),
      
      (try_begin),
        (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
        (ge, ":stamina", ":cost_stamina"),
        (val_sub, ":stamina", ":cost_stamina"),
        (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
      (else_try),
        (assign, ":power", 0),
      (try_end),
              
      (try_begin),
        (assign,":max_range",200),
        (assign,":damage",50),
        (store_random_in_range, ":randon_damage", 40, 61),
        (store_mul,":range_add",":power", 100),
        (store_mul,":damage_add",":power", ":randon_damage"),
        (val_add,":max_range",":range_add"),
        (store_add,":max_damage",":damage",":damage_add"),
      (try_end),
            
      (copy_position,pos6,pos5),
      (position_move_z,pos6,300),
      (particle_system_burst, "psys_black_hold", pos6, 5),
      (try_for_agents,":possable_agent"),
        (gt,":damage",0),
        (gt,":power",0),
        (agent_is_alive,":possable_agent"),
        (this_or_next|agent_is_ally,":shooter"),
        (agent_is_ally,":possable_agent"),
        (this_or_next|neg|agent_is_ally,":possable_agent"),
        (neg|agent_is_ally,":shooter"),

        (agent_get_position,pos3,":possable_agent"),
        (get_distance_between_positions,":dist",pos5,pos3),
        (le,":dist",":max_range"),
        (assign,":agent",":possable_agent"),
        
        (agent_get_horse, ":target_horse", ":agent"),
        (try_begin),
          (gt, ":target_horse", 0),
          (agent_set_position, ":target_horse", pos5),
          (agent_set_animation, ":target_horse", "anim_horse_rear"),
        (else_try),
          (agent_set_position, ":agent", pos5),
        (try_end),
        
        (val_add,":power",-1),
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":max_damage", thunder, ":power", ":power"),
        (assign,":max_damage",":damage_add"),
      (try_end),
    ])]
   
   
cast_magic_Frost_cloud = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt,":weapon",0),
      (assign,":damage",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
                                
      (try_begin),
        (assign,":range",100),
        (store_mul,":range_add",":power", 15),
        (store_div,":damage",":power", 3),
        (val_add,":range",":range_add"),
        (val_add,":damage",2),
      (try_end),
              
        (assign,":victim",-1),        
        (try_begin),
          (get_player_agent_no,":player"),
          (neq, ":player",":shooter"),
          (store_trigger_param_2, ":hit_object_type"),
          (neg|eq, ":hit_object_type", 1), # 1 = hostile agent
          (agent_ai_get_look_target, ":target", ":shooter"),
          (gt,":target",0),
          (neg|eq, ":shooter",":player"),
          (agent_is_alive,":target"),
          (assign,":victim",":target"),
        (try_end),
        
        (try_for_agents,":agent"),
          (agent_is_alive,":agent"),
          (agent_is_human,":agent"),
          (eq,":victim",-1),
          
          (this_or_next|agent_is_ally,":shooter"),
          (agent_is_ally,":agent"),
          (this_or_next|neg|agent_is_ally,":agent"),
          (neg|agent_is_ally,":shooter"),
                              
          (agent_get_position, pos2, ":agent"),
          (get_distance_between_positions,":distance",pos2,pos5),
          (le,":distance",":range"),
          (call_script, "script_agent_get_num_companion_nearby", ":agent", 400),
          (assign, ":num_enemies", reg0),
          (this_or_next|le, ":num_enemies", 1),
          (ge, ":num_enemies", 6),
          (assign,":victim",":agent"),
        (try_end),
        (try_begin),
          (ge,":victim",0),
          (agent_get_position, pos5, ":victim"),
        (try_end),
        (copy_position,pos4,pos5),
        (try_for_range,":posz",0,":damage"),
          (store_random_in_range, ":posx", -2,3),
          (store_random_in_range, ":posy", -2,3),
          (val_mul,":posx",20),
          (val_mul,":posy",20),
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_plague_staff_1"),
        (val_mul,":posx",100),
        (val_mul,":posy",100),
      (try_end),
          (val_mul,":posz",500),
          (position_move_x,pos4,":posx"),
          (position_move_y,pos4,":posy"),
          (position_move_z,pos4,":posz"),
          (add_missile, ":shooter", pos4, 0, ":weapon", 0, "itm_magic_frost_cloud_dummy", 0),
        (try_end),
    ])]
    
cast_magic_Frost_cloudr = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt,":weapon",0),
      
      (assign,":max_damage",0),
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
        (assign,":max_range",200),
        (assign,":damage",50),
        (store_mul,":range_add",":power", 40),
        (store_mul,":damage_add",":power", 30),
        (val_add,":max_range",":range_add"),
        (store_add,":max_damage",":damage",":damage_add"),
        (store_mul,":spec_power",":power", 3),
      (try_end),
      
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_magic_book_3"),
        (val_mul,":max_damage",2),
        (val_add,":max_range",":range_add"),
      (try_end),
      
      
        (particle_system_burst, "psys_Ice_Storm", pos5, 10),

      
      (try_for_agents,":possable_agent"),
        (gt,":max_damage",0),
        (agent_is_alive,":possable_agent"),
        (this_or_next|agent_is_ally,":shooter"),
        (agent_is_ally,":possable_agent"),
        (this_or_next|neg|agent_is_ally,":possable_agent"),
        (neg|agent_is_ally,":shooter"),

        (agent_get_position,pos3,":possable_agent"),
        (get_distance_between_positions,":dist",pos5,pos3),
        (le,":dist",":max_range"),
        (assign,":agent",":possable_agent"),
        (store_div,":half_damage",":max_damage",2),
        (store_random_in_range, ":damage", ":half_damage",":max_damage"),
        #(agent_deliver_damage_to_agent,":shooter",":agent", ":damage"),
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":damage", freeze, ":spec_power", ":power"),
      (try_end),
    ])]
    
   
   

cast_magic_deep_freeze = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      
      (assign,":damage",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      

      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
      
      (assign, ":cost_stamina", 30),
      
      (try_begin),
        (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
        (ge, ":stamina", ":cost_stamina"),
        (val_sub, ":stamina", ":cost_stamina"),
        (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
      (else_try),
        (assign, ":power", 2),
      (try_end),
              
      (try_begin),
        (assign,":max_range",200),
        (assign,":damage",100),
        (store_mul,":range_add",":power", 40),
        (store_mul,":damage_add",":power", 100),
        (val_add,":max_range",":range_add"),
        (store_add,":max_damage",":damage",":damage_add"),
      (try_end),
            
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_magic_book_3"),
        (val_mul,":max_damage",2),
        (val_add,":max_range",":range_add"),
      (try_end),
            
      (try_begin),
        (eq, "$g_weapon_fire_particle", 0),
        (gt,":damage",0),
        (particle_system_burst, "psys_Ice_Storm", pos5, 10),
      (else_try),  
        (gt,":damage",0),
        (particle_system_burst, "psys_Ice_Storm", pos5, 5),
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
        (get_distance_between_positions,":dist",pos5,pos3),
        (le,":dist",":max_range"),
        (assign,":agent",":possable_agent"),
        
        (val_add,":power",-1),
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":max_damage", freeze, ":power", ":power"),
        (assign,":max_damage",":damage_add"),
        
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_magic_book_3"),
        (store_agent_hit_points, ":inflicted_agent_hp", ":agent", 0),
        (store_mul,":dead_power",":power", 5),
        (ge, ":dead_power", ":inflicted_agent_hp"),
        (agent_set_hit_points,":agent",0,0),
        (agent_deliver_damage_to_agent, ":shooter", ":agent", 100),
      (try_end),
        
        
      (try_end),
    ])]

    
cast_magic_frozen_orb = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt,":weapon",0),
      (assign,":damage",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
          
      (assign, ":cost_stamina", 25),
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_magic_book_2"),
        (assign, ":cost_stamina", 15),
      (try_end),
      
      (try_begin),
        (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
        (ge, ":stamina", ":cost_stamina"),
        (val_sub, ":stamina", ":cost_stamina"),
        (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
      (else_try),
        (assign, ":power", 0),
      (try_end),
      
      
      (try_begin),
        (assign,":max_range",200),
        (assign,":damage",100),
        (store_random_in_range, ":randon_damage", 50, 151),
        (store_mul,":range_add",":power", 40),
        (store_mul,":damage_add",":power", ":randon_damage"),
        (val_add,":max_range",":range_add"),
        (store_add,":max_damage",":damage",":damage_add"),
        (store_mul,":add_missile",":power", 3),
        (val_add,":add_missile",5),
      (try_end),
      
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_magic_book_2"),
        (val_mul,":add_missile",2),
      (try_end),
      
      (position_get_distance_to_ground_level, ":distance", pos5),
      (try_begin),
        (lt, ":distance", 0),
        (position_set_z_to_ground_level, pos5),
        (position_move_z, pos5, 200),
      (try_end),                
      (try_begin),
        (eq, "$g_weapon_fire_particle", 0),
        (gt,":damage",0),
        (particle_system_burst, "psys_Ice_Storm", pos5, 50),
      (else_try),  
        (gt,":damage",0),
        (particle_system_burst, "psys_Ice_Storm", pos5, 5),
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
        (get_distance_between_positions,":dist",pos5,pos3),
        (le,":dist",":max_range"),
        (assign,":agent",":possable_agent"),
        
        (val_add,":power",-1),
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":max_damage", freeze, ":power", ":power"),
        (try_begin),
          (agent_has_item_equipped,":shooter","itm_magic_book_2"),
          (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":max_damage", freeze, ":power", ":power"),
        (try_end),
        (assign,":max_damage",":damage_add"),
      (try_end),
      
      (position_move_z, pos5, 200),
      (play_sound_at_position, "snd_cannon_shot", pos5),          
      (try_for_range, ":unused", 0, ":add_missile"),
        (copy_position, pos2, pos5),
        (store_random_in_range, ":x_offset", 1, 61),#Random Rotation of X
        (position_rotate_x, pos2, ":x_offset"),    
        (store_random_in_range, ":y_offset", 1, 361),#Random Rotation of Y
        (position_rotate_y, pos2, ":y_offset"),    
        (store_random_in_range, ":z_offset", 1, 361),#Random Rotation of Z
        (position_rotate_z, pos2, ":z_offset"),   
        (set_fixed_point_multiplier,10),
        (add_missile, ":shooter", pos2, 100, ":weapon", 0, "itm_magic_ice_ray_dummy", 0),
      (try_end),    
    ])]
    
cast_magic_blizzard = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt,":weapon",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
      (assign,":damage",0),
      
      (try_begin),
        (store_mul,":damage",":power", 4),
        (val_add,":damage",5),
        (assign,":range",100),
        (store_mul,":range_add",":power", 15),
        (val_add,":range",":range_add"),
      (try_end),
      
        (assign,":victim",-1),
        (try_begin),
          (get_player_agent_no,":player"),
          (neq, ":player",":shooter"),
          (store_trigger_param_2, ":hit_object_type"),
          (neg|eq, ":hit_object_type", 1), # 1 = hostile agent
          (agent_ai_get_look_target, ":target", ":shooter"),
          (gt,":target",0),
          (neg|eq, ":shooter",":player"),
          (agent_is_alive,":target"),
          (assign,":victim",":target"),
        (try_end),
        
        (try_begin),
          (ge,":victim",0),
          (agent_get_position, pos5, ":victim"),
        (try_end),
      
        (try_for_range,":unused",0,":damage"),
          (assign, ":cost_stamina", 2),
          (try_begin),
            (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
            (ge, ":stamina", ":cost_stamina"),
            (val_sub, ":stamina", ":cost_stamina"),
            (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
          (else_try),
            (assign, ":power", 1),
          (try_end),
          (copy_position,pos4,pos5),
          (store_random_in_range, ":posx", -15,16),
          (store_random_in_range, ":posy", -15,16),
          (store_random_in_range, ":posz", 30,70),
          (val_mul,":posx",50),
          (val_mul,":posy",50),
          (val_mul,":posz",100),
          (position_move_x,pos4,":posx"),
          (position_move_y,pos4,":posy"),
          (position_move_z,pos4,":posz"),
          #(position_move_z,pos5,":posz"),
          (add_missile, ":shooter", pos4, 0, ":weapon", 0, "itm_magic_ice_ray_dummy", 0),
          (try_begin),
            (eq, "$g_weapon_fire_particle", 0),
            (gt,":damage",0),
            (particle_system_burst, "psys_Ice_Storm", pos4, 5),
          (else_try),  
            (gt,":damage",0),
            (particle_system_burst, "psys_Ice_Storm", pos4, 1),
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
            (get_distance_between_positions,":dist",pos4,pos3),
            (le,":dist",250),
            (assign,":agent",":possable_agent"),
            (val_add,":power",-1),
            (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", 200, freeze, ":power", 5),
          (try_end),
        (try_end),
    ])]
    
cast_magic_ice_ray_dummy = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      
      (assign,":damage",0),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
      
      (assign, ":cost_stamina", 1),
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_magic_book_3"),
        (assign,":cost_stamina",0),
      (try_end),
      (try_begin),
        (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
        (ge, ":stamina", ":cost_stamina"),
        (val_sub, ":stamina", ":cost_stamina"),
        (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
      (else_try),
        (assign, ":power", 0),
      (try_end),
      
      (try_begin),
        (assign,":max_range",150),
        (assign,":damage",50),
        (store_mul,":damage_add",":power", 50),
        (store_add,":max_damage",":damage",":damage_add"),
        (store_mul,":range_add",":power", 10),
        (val_add,":max_range",":range_add"),
      (try_end),
      
      (try_begin),
        (eq, "$g_weapon_fire_particle", 0),
        (gt,":damage",0),
        (particle_system_burst, "psys_Freezing_Trail", pos5, 15),
      (else_try),  
        (gt,":damage",0),
        (particle_system_burst, "psys_Freezing_Trail", pos5, 3),
      (try_end),
      (try_for_agents,":possable_agent"),
        (gt,":max_damage",0),
        (gt,":power",0),
        (agent_is_alive,":possable_agent"),
        (this_or_next|agent_is_ally,":shooter"),
        (agent_is_ally,":possable_agent"),
        (this_or_next|neg|agent_is_ally,":possable_agent"),
        (neg|agent_is_ally,":shooter"),

        (agent_get_position,pos3,":possable_agent"),
        (get_distance_between_positions,":dist",pos5,pos3),
        (le,":dist",":max_range"),
        (assign,":agent",":possable_agent"),
        
        (val_add,":power",-1),
        
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_magic_book_3"),
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":max_damage", freeze, ":power", 5),
      (else_try),  
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":max_damage", ice, ":power", 5),
      (try_end),
        
      (try_end),
    ])]

    
cast_magic_ice_ray = [
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
        (eq, ":weapon", "itm_warlock_staff_1"),
        (val_add,":power",1),
      (else_try),
        (eq, ":weapon", "itm_thunder_staff_1"),
        (val_add,":power",2),
      (try_end),
      
      (try_begin),
        (assign,":max_range",100),
        (assign,":damage",50),
        (store_mul,":range_add",":power", 20),
        (store_mul,":damage_add",":power", 100),
        (val_add,":max_range",":range_add"),
        (store_add,":max_damage",":damage",":damage_add"),
      (try_end),
      
      (copy_position,pos6,pos5),
      (position_move_z,pos6,200),
      (particle_system_burst, "psys_frost_nails", pos6, 5),
      (try_for_agents,":possable_agent"),
        (gt,":damage",0),
        (gt,":power",0),
        (agent_is_alive,":possable_agent"),
        (this_or_next|agent_is_ally,":shooter"),
        (agent_is_ally,":possable_agent"),
        (this_or_next|neg|agent_is_ally,":possable_agent"),
        (neg|agent_is_ally,":shooter"),

        (agent_get_position,pos3,":possable_agent"),
        (get_distance_between_positions,":dist",pos5,pos3),
        (le,":dist",":max_range"),
        (assign,":agent",":possable_agent"),
        
        (val_add,":power",-1),
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":max_damage", ice, ":power", ":power"),
        
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_magic_book_3"),
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":max_damage", freeze, ":power", 5),
      (else_try),  
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":max_damage", ice, ":power", 5),
        (assign,":max_damage",50),
      (try_end),
        
      (try_end),
    ])]

cast_magic_DEADLY_COLD = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      
      (assign,":damage",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
      
      (assign, ":cost_stamina", 40),
      (try_begin),
        (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
        (ge, ":stamina", ":cost_stamina"),
        (val_sub, ":stamina", ":cost_stamina"),
        (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
      (else_try),
        (assign, ":power", 0),
      (try_end),
            
      (try_begin),
        (assign,":max_range",200),
        (assign,":damage",100),
        (store_mul,":range_add",":power", 50),
        (store_mul,":damage_add",":power", 150),
        (val_add,":max_range",":range_add"),
        (store_add,":max_damage",":damage",":damage_add"),
        (store_mul,":dest_damage",":power", 100),
      (try_end),
      
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_magic_book_3"),
        (val_add,":max_range",":range_add"),
      (try_end),

      (copy_position,pos6,pos5),
      (particle_system_burst, "psys_Freezing_Trail", pos6, 5),
      (try_for_agents,":possable_agent"),
        (gt,":damage",0),
        (gt,":power",0),
        (agent_is_alive,":possable_agent"),
        (this_or_next|agent_is_ally,":shooter"),
        (agent_is_ally,":possable_agent"),
        (this_or_next|neg|agent_is_ally,":possable_agent"),
        (neg|agent_is_ally,":shooter"),

        (agent_get_position,pos3,":possable_agent"),
        (get_distance_between_positions,":dist",pos5,pos3),
        (le,":dist",":max_range"),
        (assign,":agent",":possable_agent"),
        
        (val_add,":power",-1),
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":max_damage", ice, ":power", ":power"),
        
        (agent_get_troop_id, ":inflicted_troop", ":agent"),
        (store_skill_level, ":defence", skl_magic_defence, ":inflicted_troop"),
        (try_begin),
          (agent_has_item_equipped,":shooter","itm_magic_book_3"),
          (val_add,":defence",-3),
        (try_end),
        (le,":defence",8),
        (troop_get_slot, ":inflicted_troop_max_hp", ":inflicted_troop", slot_troop_max_hp),
            
        (store_random_in_range, ":random_no", 0, ":inflicted_troop_max_hp"),
        (store_agent_hit_points, ":inflicted_agent_hp", ":agent", 1),
            
        (this_or_next|ge,":random_no", ":inflicted_agent_hp"),
        (ge, ":dest_damage", ":inflicted_troop_max_hp"),
        (agent_set_hit_points,":agent",0,0),
        (agent_deliver_damage_to_agent, ":shooter", ":agent", 100),
      (try_end),
    ])]

cast_magic_Dispel_Magic = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
      
      (assign, ":cost_stamina", 25),
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
        (store_mul,":range_add",":power", 50),
        (val_add,":max_range",":range_add"),
      (try_end),
      
      (copy_position,pos6,pos5),
      (position_move_z,pos6,200),
      (particle_system_burst, "psys_frost_nails", pos6, 5),
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
        
        (agent_get_slot, ":special", ":agent", slot_agent_special_ability_affect_type),
        (assign, ":continue", 0),
        (try_begin),
          (this_or_next|agent_is_ally,":shooter"),
          (agent_is_ally,":agent"),
          (this_or_next|neg|agent_is_ally,":agent"),
          (neg|agent_is_ally,":shooter"),      
          (this_or_next|eq,":special", divine_strength),
          (this_or_next|eq,":special", haste),
          (this_or_next|eq,":special", regeneration),
          (this_or_next|eq,":special", haste_reload),
          (this_or_next|eq,":special", berserk),
          (this_or_next|eq,":special", battlecry),
          (this_or_next|eq,":special", inspire),
          (agent_slot_ge, ":agent", slot_agent_spawned, 1), 
          (assign, ":continue", 1),
        (else_try),
          (this_or_next|agent_is_ally,":shooter"),
          (neg|agent_is_ally,":agent"),
          (this_or_next|agent_is_ally,":agent"),
          (neg|agent_is_ally,":shooter"),
          (this_or_next|eq,":special", weakness),
          (this_or_next|eq,":special", slow),
          (this_or_next|eq,":special", mummy_curse),
          (this_or_next|eq,":special", entangle),
          (this_or_next|eq,":special", warcry),
          (this_or_next|eq,":special", grasp),
          (this_or_next|eq,":special", fright_aura),
          (agent_slot_ge, ":agent", slot_agent_special_damage_time, 1), 
          (assign, ":continue", 2),
        (try_end),
        (ge, ":continue", 1),
        
        (agent_get_slot, ":special", ":agent", slot_agent_special_ability_affect_type),
        (try_begin),
          (eq, ":continue", 1),
          (agent_set_slot, ":agent", slot_agent_special_ability_affect_type, 0),
          (agent_set_slot, ":agent", slot_agent_special_ability_affect_time, 0),
        (else_try),
          (eq, ":continue", 2),
          (neg|agent_slot_eq, ":agent", slot_agent_is_running_away, 0),
          (agent_stop_running_away, ":agent"),
          (agent_clear_scripted_mode,":agent"),
          (agent_set_slot, ":agent",  slot_agent_is_running_away, 0),
          (agent_set_slot, ":agent", slot_agent_special_ability_affect_type, 0),
          (agent_set_slot, ":agent", slot_agent_special_ability_affect_time, 0),
          (agent_set_slot, ":agent", slot_agent_special_damage_type, 0),
          (agent_set_slot, ":agent", slot_agent_special_damage_power, 0),
          (agent_set_slot, ":agent", slot_agent_special_damage_time, 0),
        (try_end),   
        (agent_play_sound, ":agent", "snd_spell_dispel"),
        (try_begin),
          (this_or_next|agent_is_ally,":shooter"),
          (agent_is_ally,":agent"),
          (this_or_next|neg|agent_is_ally,":agent"),
          (neg|agent_is_ally,":shooter"),      
          (agent_slot_ge, ":agent", slot_agent_spawned, 1), 
          (agent_fade_out, ":agent"),
        (try_end),      
      (try_end),
    ])]


cast_magic_LightningBolt = [
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
        (assign,":damage",50),
        (store_mul,":range_add",":power", 20),
        (store_mul,":damage_add",":power", 60),
        (val_add,":max_range",":range_add"),
        (store_add,":max_damage",":damage",":damage_add"),
      (try_end),
      
        (try_begin),
          (agent_has_item_equipped,":shooter","itm_magic_book_2"),
          (val_add,":max_range",":range_add"),
          (val_add,":max_range",":damage_add"),
        (try_end),
      
      (copy_position,pos6,pos5),
      (position_move_z,pos6,150),
        (particle_system_burst, "psys_spark_explosion_small", pos6, 5),
      (try_for_agents,":possable_agent"),
        (gt,":damage",0),
        (gt,":power",0),
        (agent_is_alive,":possable_agent"),
        (this_or_next|agent_is_ally,":shooter"),
        (agent_is_ally,":possable_agent"),
        (this_or_next|neg|agent_is_ally,":possable_agent"),
        (neg|agent_is_ally,":shooter"),

        (agent_get_position,pos3,":possable_agent"),
        (get_distance_between_positions,":dist",pos5,pos3),
        (le,":dist",":max_range"),
        (assign,":agent",":possable_agent"),
        
        (try_begin),
          (agent_has_item_equipped,":shooter","itm_magic_book_2"),
          (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":max_damage", thunder, ":power", ":power"),
        (else_try),
          (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":max_damage", thunder, ":power", ":power"),
          (assign,":max_damage",100),
        (try_end),
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
      (try_begin),
        (agent_is_human, ":agent"),
        (agent_is_active, ":agent"),
        (agent_is_alive, ":agent"),
        (agent_set_animation, ":agent", "anim_power_jump", 0),
      (try_end),
        (val_add,":power",-1),
        
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":damage", power_jump, ":power", ":power"),
        (agent_set_slot, ":agent", slot_agent_special_damage_type, power_jump),
        (agent_set_slot, ":agent", slot_agent_special_damage_power, ":power"),
        (agent_set_slot, ":agent", slot_agent_special_damage_time, ":power"),
      (try_end),
    ])]


cast_magic_sun_ray = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (assign,":damage",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),

      (assign, ":cost_stamina", 10),
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_magic_book_4"),
        (assign, ":cost_stamina", 0),
      (try_end),
      (try_begin),
        (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
        (ge, ":stamina", ":cost_stamina"),
        (val_sub, ":stamina", ":cost_stamina"),
        (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
      (else_try),
        (assign, ":power", 0),
      (try_end),

      (try_begin),
        (eq, ":weapon", "itm_bishop_staff"),
        (val_add,":power",3),
      (else_try),
        (eq, ":weapon", "itm_war_clerics_warhammer_cast"),
        (val_add,":power",3),
      (else_try),
        (eq, ":weapon", "itm_war_clerics_warhammer_cast_2"),
        (val_add,":power",4),
      (else_try),
        (eq, ":weapon", "itm_bishop_staff_2"),
        (val_add,":power",5),
      (try_end),
      
      (try_begin),
        (assign,":max_range",100),
        (assign,":damage",50),
        (store_mul,":range_add",":power", 50),
        (store_mul,":damage_add",":power", 70),
        (val_add,":max_range",":range_add"),
        (store_add,":damage",":damage_add"),
      (try_end),
      
      (try_begin),
        (eq, "$g_weapon_fire_particle", 0),
        (gt,":damage",0),
        (particle_system_burst, "psys_Burning_Trail_holy", pos5, 15),
      (else_try),  
        (gt,":damage",0),
        (particle_system_burst, "psys_Burning_Trail_holy", pos5, 1),
      (try_end),
      (try_for_agents,":possable_agent"),
        (gt,":damage",0),
        (agent_is_alive,":possable_agent"),
        (this_or_next|agent_is_ally,":shooter"),
        (agent_is_ally,":possable_agent"),
        (this_or_next|neg|agent_is_ally,":possable_agent"),
        (neg|agent_is_ally,":shooter"),

        (agent_get_position,pos3,":possable_agent"),
        (get_distance_between_positions,":dist",pos5,pos3),
        (le,":dist",":max_range"),
        (assign,":agent",":possable_agent"),
        
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":damage", holy_fire, ":power", 5),
        (assign,":damage",50),
      (try_end),
    ])]

holy_weapon_trigger = [
  (ti_on_weapon_attack, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (try_begin),
        (eq, ":weapon", "itm_bishop_staff_melee"),
        (assign,":power",7),
        (assign,":max_range",120),
        (assign,":damage",70),
      (else_try),
        (this_or_next|eq, ":weapon", "itm_sissofbattle_sword"),
        (eq, ":weapon", "itm_bishop_staff_2_melee"),
        (assign,":power",8),
        (assign,":max_range",130),
        (assign,":damage",80),
      (else_try),
        (this_or_next|eq, ":weapon", "itm_sissofbattle_sword_alt"),
        (eq, ":weapon", "itm_war_clerics_warhammer"),
        (assign,":power",9),
        (assign,":max_range",140),
        (assign,":damage",90),
      (else_try),
        (this_or_next|eq, ":weapon", "itm_bastard_sword_c"),
        (this_or_next|eq, ":weapon", "itm_angel_blade"),
        (eq, ":weapon", "itm_war_clerics_warhammer_2"),
        (assign,":power",10),
        (assign,":max_range",150),
        (assign,":damage",100),
      (else_try),
        (assign,":power",5),
        (assign,":max_range",110),
        (assign,":damage",50),
      (try_end),

      (try_begin),
        (gt,":damage",0),
        (particle_system_burst, "psys_Burning_Trail_holy", pos5, ":power"),
      (try_end),
      (try_for_agents,":possable_agent"),
        (gt,":damage",0),
        (agent_is_alive,":possable_agent"),
        (this_or_next|agent_is_ally,":shooter"),
        (agent_is_ally,":possable_agent"),
        (this_or_next|neg|agent_is_ally,":possable_agent"),
        (neg|agent_is_ally,":shooter"),

        (agent_get_position,pos3,":possable_agent"),
        (get_distance_between_positions,":dist",pos5,pos3),
        (le,":dist",":max_range"),
        (assign,":agent",":possable_agent"),
        
        (agent_get_troop_id, ":inflicted_troop", ":agent"),
        
        (troop_get_type, ":agent_gender", ":inflicted_troop"),
        (this_or_next|eq, ":agent_gender", tf_undead),
        (eq, ":agent_gender", tf_vampire),
        
        #(this_or_next|is_between, ":inflicted_troop", "trp_skeleton","trp_taiga_bandit"),
        #(this_or_next|is_between, ":inflicted_troop", "trp_mummy_1","trp_undead_human"),
        #(this_or_next|is_between, ":inflicted_troop", "trp_lich_1","trp_minotaur_1"),
        #(eq, ":inflicted_troop", "trp_vampire_assassin"),
        
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":damage", holy_fire, ":power", 5),
      (try_end),
    ])]

dragon_weapon_trigger = [
  (ti_on_weapon_attack, 
    [
        (store_trigger_param_1, ":shooter"),
        (agent_get_troop_id, ":troop", ":shooter"),
        (assign,":power",0),
        (try_begin),
          (eq, ":troop", "trp_red_dragon"),
          (assign,":power",3),
        (else_try),
          (eq, ":troop", "trp_black_dragon"),
          (assign,":power",5),
        (else_try),
          (eq, ":troop", "trp_green_dragon"),
          (assign,":power",2),
        (else_try),
          (eq, ":troop", "trp_lizard_dragon"),
          (assign,":power",2),
        (else_try),
          (eq, ":troop", "trp_gold_dragon"),
          (assign,":power",4),
        (else_try),
          (eq, ":troop", "trp_fire_dragon"),
          (assign,":power",4),
        (else_try),
          (eq, ":troop", "trp_lava_dragon"),
          (assign,":power",5),
        (else_try),
          (agent_get_wielded_item, ":weapon", ":shooter", 0),
          (eq, ":weapon", "itm_dragon_knight_lance"),
          (assign,":power",3),
        (else_try),
          (agent_get_wielded_item, ":weapon", ":shooter", 0),
          (eq, ":weapon", "itm_scottish_claymore"),
          (assign,":power",2),
        (try_end),
        (gt,":power",0),

        (val_add,":power",2),

        (store_random_in_range, ":r1", 0, 15),
        (store_random_in_range, ":r2", 1, ":power"),
        (try_begin),
          (eq, ":r1", 1),
          (call_script, "script_cf_agent_excalibur_light", ":shooter", ":power"),
        (else_try),
          (ge, ":r1", 10),
          (call_script, "script_cf_agent_excalibur_light", ":shooter", 1),
        (else_try),
          (call_script, "script_cf_agent_excalibur_light", ":shooter", ":r2"),
        (try_end),
        
        
       # (agent_get_position, pos1, ":shooter"),
       # (agent_get_position, pos10, ":shooter"),
       # (position_move_z, pos1, 100),
       # (position_move_y, pos1, 60),
       # (position_rotate_z, pos1, 80),
       # (store_random_in_range, ":var_1", 0, 41),

       # (position_rotate_z, pos1, ":var_1"),
       # (particle_system_burst, "psys_fire_smierc", pos1, 5),
       # (position_move_y, pos10, -60),
       # (multiplayer_is_server),
       # (try_for_agents, ":possable_agent"),
       #   (this_or_next|agent_is_ally,":shooter"),
       #   (agent_is_ally,":possable_agent"),
       #   (this_or_next|neg|agent_is_ally,":possable_agent"),
       #   (neg|agent_is_ally,":shooter"),
       #   (agent_is_alive, ":possable_agent"),
       #   (agent_get_position, pos2, ":possable_agent"),
       #   (get_distance_between_positions, ":var_3", pos1, pos2),
       #   (neg|gt, ":var_3", 500),
       #   (get_distance_between_positions, ":var_4", pos10, pos2),
       #   (ge, ":var_4", ":var_3"),
       #   (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":possable_agent", ":damage", ":damage_type", ":power", 5),
       # (try_end),
        
        
        
    ])]


thunder_weapon_trigger = [
   (ti_on_missile_hit, 
     [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos51,pos1),
      (agent_get_troop_id, ":troop_no", ":shooter"),
      (store_attribute_level,":int",":troop_no",ca_intelligence),
      (store_character_level,":damage",":troop_no"),
      
      (store_skill_level, ":power", skl_magic_power, ":troop_no"),
      (try_begin),
        (le, ":power", 5),
        (assign,":power",5),
      (try_end),
      (try_begin),
        (val_add,":damage",":int"),
        (store_mul,":damage_add",":power", ":damage"),
      (try_end),
      
      (particle_system_burst, "psys_thunder", pos51, 1),
      (play_sound_at_position, "snd_thunder_hit", pos51),
      (try_for_agents,":possable_agent"),
        (gt,":damage_add",0),
        (agent_is_alive,":possable_agent"),
        (this_or_next|agent_is_ally,":shooter"),
        (agent_is_ally,":possable_agent"),
        (this_or_next|neg|agent_is_ally,":possable_agent"),
        (neg|agent_is_ally,":shooter"),

        (agent_get_position,pos3,":possable_agent"),
        (get_distance_between_positions,":dist",pos51,pos3),
        (le,":dist",500),
        (assign,":agent",":possable_agent"),
        
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":damage_add", thunder, ":power", ":power"),
      (try_end),
     ])]
  
thunder_weapon_trigger_2 = [
   (ti_on_weapon_attack, 
     [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos51,pos1),
      (agent_get_troop_id, ":troop_no", ":shooter"),
      (store_attribute_level,":int",":troop_no",ca_intelligence),
      (store_character_level,":damage",":troop_no"),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (store_random_in_range, ":randon_damage", 0, 100),
      (this_or_next|eq,":weapon", "itm_mjolnir_melee"),
      (le, ":randon_damage", 30),
      
      (store_skill_level, ":power", skl_magic_power, ":troop_no"),
      (try_begin),
        (le, ":power", 5),
        (assign,":power",5),
      (try_end),
      (try_begin),
        (val_add,":damage",":int"),
        (store_mul,":damage_add",":power", ":damage"),
      (try_end),
      
      (particle_system_burst, "psys_thunder", pos51, 1),
      (play_sound_at_position, "snd_thunder_hit", pos51),
      (try_for_agents,":possable_agent"),
        (gt,":damage_add",0),
        (agent_is_alive,":possable_agent"),
        (this_or_next|agent_is_ally,":shooter"),
        (agent_is_ally,":possable_agent"),
        (this_or_next|neg|agent_is_ally,":possable_agent"),
        (neg|agent_is_ally,":shooter"),

        (agent_get_position,pos3,":possable_agent"),
        (get_distance_between_positions,":dist",pos51,pos3),
        (le,":dist",500),
        (assign,":agent",":possable_agent"),
        
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":damage_add", thunder, ":power", ":power"),
      (try_end),
     ])]
          
mjolnir_trigger = [
(ti_on_weapon_attack,[(store_trigger_param_1, ":shooter"),(agent_set_ammo,":shooter","itm_mjolnir",2),]),
(ti_on_init_item, [(eq, "$g_weapon_fire_particle", 0),(set_position_delta,0,65,0),(store_trigger_param_2, ":troop_no"),(troop_is_hero, ":troop_no"),(particle_system_add_new, "psys_mjolnir_lightning"),
])]   

  
gungnir_trigger = [(ti_on_weapon_attack,[(store_trigger_param_1, ":shooter"),(agent_set_ammo,":shooter","itm_throwing_gungnir",2)])]     
cast_magic_column_of_fire = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt,":weapon",0),
      (assign,":damage",0),
      #(item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
      
      (assign, ":cost_stamina", 30),
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_magic_book_4"),
        (assign, ":cost_stamina", 20),
      (try_end),
      (try_begin),
        (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
        (ge, ":stamina", ":cost_stamina"),
        (val_sub, ":stamina", ":cost_stamina"),
        (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
      (else_try),
        (assign, ":power", 0),
      (try_end),
      
      (try_begin),
        (eq, ":weapon", "itm_bishop_staff"),
        (val_add,":power",3),
      (else_try),
        (eq, ":weapon", "itm_war_clerics_warhammer_cast"),
        (val_add,":power",3),
      (else_try),
        (eq, ":weapon", "itm_war_clerics_warhammer_cast_2"),
        (val_add,":power",4),
      (else_try),
        (eq, ":weapon", "itm_bishop_staff_2"),
        (val_add,":power",5),
      (try_end),
      
      (try_begin),
        (assign,":max_range",100),
        (assign,":damage",100),
        (store_mul,":range_add",":power", 100),
        (val_add,":max_range",":range_add"),
        (store_mul,":damage_add",":power", 50),
        (store_add,":damage",":damage_add"),
        (store_mul,":spec_power",":power", 3),
      (try_end),
      
      (try_begin),
        (eq, ":weapon", "itm_bishop_staff"),
        (val_add,":max_range",50),
      (else_try),
        (eq, ":weapon", "itm_war_clerics_warhammer_cast"),
        (val_add,":max_range",80),
      (else_try),
        (eq, ":weapon", "itm_war_clerics_warhammer_cast_2"),
        (val_add,":max_range",110),
      (else_try),
        (eq, ":weapon", "itm_bishop_staff_2"),
        (val_add,":max_range",110),
      (try_end),
      
        (assign,":victim",-1),
        (try_begin),
          (get_player_agent_no,":player"),
          (store_trigger_param_2, ":hit_object_type"),
          (neg|eq, ":hit_object_type", 1), # 1 = hostile agent
          (try_begin),
            (eq, ":player",":shooter"),
            (agent_get_slot, ":target", ":player", slot_agent_player_target),
          (else_try),
            (agent_ai_get_look_target, ":target", ":shooter"),
          (try_end),
          (gt,":target",0),
          (agent_is_alive,":target"),
          (neg|eq, ":player",":target"),
          (assign,":victim",":target"),
        (try_end),
        
        (try_begin),
          (ge,":victim",0),
          (agent_get_position, pos5, ":victim"),
        (try_end),
      
      (try_begin),
        (gt,":damage",0),
        (copy_position, pos40, pos5),
        (position_move_z, pos40, 400),
        (particle_system_burst, "psys_fright_aura2", pos40, 1),
        #(particle_system_burst, "psys_Freezing_Trail", pos5, 35),
      (try_end),
      (try_for_agents,":possable_agent"),
        (gt,":damage",0),
        (agent_is_alive,":possable_agent"),
        (this_or_next|agent_is_ally,":shooter"),
        (agent_is_ally,":possable_agent"),
        (this_or_next|neg|agent_is_ally,":possable_agent"),
        (neg|agent_is_ally,":shooter"),

        (agent_get_position,pos3,":possable_agent"),
        (get_distance_between_positions,":dist",pos5,pos3),
        (le,":dist",":max_range"),
        (assign,":agent",":possable_agent"),
        
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":damage", holy_fire, ":spec_power", ":power"),
      (try_end),
      (position_get_distance_to_ground_level, ":distance", pos5),
      (try_begin),
        (lt, ":distance", 0),
        (position_set_z_to_ground_level, pos5),
        (position_move_z, pos5, 200),
      (try_end),                
    (try_begin),
      (neg|eq, ":weapon", "itm_archangle_sword_2"),
      (neg|eq, ":weapon", "itm_angle_sword_2"),
      (neg|eq, ":weapon", "itm_gold_dragon_sword"),
      (store_mul,":damage",":power", 10),

      (play_sound_at_position, "snd_cannon_shot", pos5),  
        (position_move_z, pos5, 500),
        (particle_system_burst, "psys_explosive_explosion_sparks_a", pos5, 35),
        (particle_system_burst, "psys_explosive_explosion_sparks_b", pos5, 35),
      (try_for_range, ":unused", 0, ":damage"),
        (copy_position, pos2, pos5),
        (store_random_in_range, ":x_offset", 1, 361),#Random Rotation of X
        (position_rotate_x, pos2, ":x_offset"),    
        (store_random_in_range, ":y_offset", 1, 361),#Random Rotation of Y
        (position_rotate_y, pos2, ":y_offset"),    
        (store_random_in_range, ":z_offset", 1, 361),#Random Rotation of Z
        (position_rotate_z, pos2, ":z_offset"),   
        (set_fixed_point_multiplier,10),
        (add_missile, ":shooter", pos2, 1000, ":weapon", 0, "itm_magic_sun_ray_dummy", 0),
      (try_end),    
    (try_end),    
    ])]
    
cast_magic_Entangling = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),

      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
      
      (assign, ":cost_stamina", 25),
      (try_begin),
        (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
        (ge, ":stamina", ":cost_stamina"),
        (val_sub, ":stamina", ":cost_stamina"),
        (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
      (else_try),
        (assign, ":power", 0),
      (try_end),
            
      (try_begin),
        (assign,":max_range",50),
        (store_mul,":range_add",":power", 50),
        (val_add,":max_range",":range_add"),
        (store_mul,":spec_time",":power", 5),
      (try_end),
              

        (try_for_agents,":possable_agent"),
          (agent_is_active,":possable_agent"),
          (agent_is_alive,":possable_agent"),   
          (agent_get_position,pos6,":possable_agent"),
          (get_distance_between_positions,":dist",pos5,pos6),
          (lt,":dist",":max_range"),            	
          (try_begin),
            (neg|agent_is_human, ":possable_agent"),#stop if not human
            (agent_get_rider,":rider_agent",":possable_agent"),
            (assign, ":continue", 0),
            (try_begin),
              (gt,":rider_agent",-1),
              (agent_is_ally, ":rider_agent"),
              (neg|agent_is_ally, ":shooter"),
              (assign, ":continue", 1),
            (else_try),
              (gt,":rider_agent",-1),
              (neg|agent_is_ally, ":rider_agent"),
              (agent_is_ally, ":shooter"),
              (assign, ":continue", 1),
            (else_try),
              (le,":rider_agent",-1),
              (assign, ":continue", 1),
            (try_end),
            (eq, ":continue", 1),
            (agent_get_rider,":rider_agent",":possable_agent"),
            (try_begin),
              (gt,":rider_agent",-1),
              (agent_set_animation, ":rider_agent", "anim_bash_knocked"),  
              (agent_set_slot, ":rider_agent", slot_agent_special_ability_affect_type, entangle),
              (agent_set_slot, ":rider_agent", slot_agent_special_ability_affect_time, ":spec_time"),
              (agent_set_hit_points,":possable_agent",0,0),
              (agent_deliver_damage_to_agent,":shooter",":possable_agent"),
            (else_try),
              (le,":rider_agent",-1),
              (agent_set_hit_points,":possable_agent",0,0),
              (agent_deliver_damage_to_agent,":shooter",":possable_agent"),
            (try_end),
          (else_try),
            (assign, ":continue", 0),
            (try_begin),
              (agent_is_ally, ":possable_agent"),
              (neg|agent_is_ally, ":shooter"),
              (assign, ":continue", 1),
            (else_try),
              (neg|agent_is_ally, ":possable_agent"),
              (agent_is_ally, ":shooter"),
              (assign, ":continue", 1),
            (try_end),
            (eq, ":continue", 1),
            (agent_is_human, ":possable_agent"),
            (position_move_z, pos62, 200),
            (particle_system_burst,"psys_stun_effect",pos62,1),
            (agent_set_animation, ":possable_agent", "anim_bash_knocked"),  
            (agent_set_slot, ":possable_agent", slot_agent_special_ability_affect_type, entangle),
            (agent_set_slot, ":possable_agent", slot_agent_special_ability_affect_time, ":spec_time"),
        (try_end),
    ])]

cast_magic_web = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),

      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
      
      (assign, ":cost_stamina", 25),
      (try_begin),
        (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
        (ge, ":stamina", ":cost_stamina"),
        (val_sub, ":stamina", ":cost_stamina"),
        (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
      (else_try),
        (assign, ":power", 0),
      (try_end),
            
      (try_begin),
        (assign,":max_range",200),
        (store_mul,":range_add",":power", 100),
        (val_add,":max_range",":range_add"),
      (try_end),
              

        (try_for_agents,":possable_agent"),
          (agent_is_active,":possable_agent"),
          (agent_is_alive,":possable_agent"),   
          (agent_get_position,pos6,":possable_agent"),
          (get_distance_between_positions,":dist",pos5,pos6),
          (lt,":dist",":max_range"),            	
          (try_begin),
            (neg|agent_is_human, ":possable_agent"),#stop if not human
            (agent_get_rider,":rider_agent",":possable_agent"),
            (assign, ":continue", 0),
            (try_begin),
              (gt,":rider_agent",-1),
              (agent_is_ally, ":rider_agent"),
              (neg|agent_is_ally, ":shooter"),
              (assign, ":continue", 1),
            (else_try),
              (gt,":rider_agent",-1),
              (neg|agent_is_ally, ":rider_agent"),
              (agent_is_ally, ":shooter"),
              (assign, ":continue", 1),
            (else_try),
              (le,":rider_agent",-1),
              (assign, ":continue", 1),
            (try_end),
            (eq, ":continue", 1),
            (agent_get_rider,":rider_agent",":possable_agent"),
            (try_begin),
              (gt,":rider_agent",-1),
              (agent_set_animation, ":rider_agent", "anim_bash_knocked"),  
              (agent_set_slot, ":rider_agent", slot_agent_special_ability_affect_type, entangle),
              (agent_set_slot, ":rider_agent", slot_agent_special_ability_affect_time, 3),
            (try_end),
          (else_try),
            (assign, ":continue", 0),
            (try_begin),
              (agent_is_ally, ":possable_agent"),
              (neg|agent_is_ally, ":shooter"),
              (assign, ":continue", 1),
            (else_try),
              (neg|agent_is_ally, ":possable_agent"),
              (agent_is_ally, ":shooter"),
              (assign, ":continue", 1),
            (try_end),
            (eq, ":continue", 1),
            (agent_is_human, ":possable_agent"),
            (position_move_z, pos62, 200),
            (particle_system_burst,"psys_stun_effect",pos62,1),
            (agent_set_animation, ":possable_agent", "anim_bash_knocked"),  
            (agent_set_slot, ":possable_agent", slot_agent_special_ability_affect_type, entangle),
            (agent_set_slot, ":possable_agent", slot_agent_special_ability_affect_time, 3),
        (try_end),
    ])]

   
    
cast_magic_Pyroblast = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (assign,":damage",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
      
      (assign, ":cost_stamina", 33),
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_magic_book_4"),
        (assign, ":cost_stamina", 20),
      (try_end),
      (try_begin),
        (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
        (ge, ":stamina", ":cost_stamina"),
        (val_sub, ":stamina", ":cost_stamina"),
        (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
      (else_try),
        (assign, ":power", 0),
      (try_end),
            
      (try_begin),
        (assign,":max_range",200),
        (assign,":damage",200),

        (store_mul,":range_add",":power", 50),
        (store_mul,":damage_add",":power", 100),
        (val_add,":max_range",":range_add"),
        (store_add,":max_damage",":damage",":damage_add"),
        (store_div,":spec_power",":power", 2),
        (val_add,":spec_power",1),
        (store_div,":spec_time",":power", 3),
        (val_add,":spec_time",2),
      (try_end),
              
      (copy_position,pos6,pos5),
      (position_move_z,pos6,150),
      (try_begin),
        (eq, "$g_weapon_fire_particle", 0),
        (gt,":damage",0),
        (gt,":power",0),
        (particle_system_burst, "psys_flame_explosion",pos5,50),
        (particle_system_burst, "psys_explosive_explosion_sparks_a", pos5, 35),
        (particle_system_burst, "psys_incediary_cloud", pos5, 35),
      (else_try),  
        (gt,":damage",0),
        (gt,":power",0),
        (particle_system_burst, "psys_flame_explosion",pos5,5),
        (particle_system_burst, "psys_explosive_explosion_sparks_a", pos5, 5),
        (particle_system_burst, "psys_incediary_cloud", pos5, 5),
      (try_end),
      (try_for_agents,":possable_agent"),
        (gt,":damage",0),
        (agent_is_alive,":possable_agent"),
        (this_or_next|agent_is_ally,":shooter"),
        (agent_is_ally,":possable_agent"),
        (this_or_next|neg|agent_is_ally,":possable_agent"),
        (neg|agent_is_ally,":shooter"),

        (agent_get_position,pos3,":possable_agent"),
        (get_distance_between_positions,":dist",pos5,pos3),
        (le,":dist",":max_range"),
        (assign,":agent",":possable_agent"),
        (try_begin),
          (agent_has_item_equipped,":shooter","itm_magic_book_4"),
          (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":max_damage", severe_burn, ":spec_power", ":spec_time"),        
        (try_end),
        
        
        (val_add,":spec_time",-1),
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":max_damage", severe_burn, ":spec_power", ":spec_time"),        
      (try_end),
    ])]

cast_magic_demon_arrow = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
        (copy_position,pos51,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt,":weapon",0),
      (assign,":damage",0),
      (this_or_next|eq,":weapon","itm_ebony_bow"),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
      (store_skill_level, ":skill_level", "skl_power_draw", ":shooter_troop"),
      (val_add,":power",":skill_level"),

      (item_get_thrust_damage, ":basic_damage", ":weapon"),
      (val_mod, ":basic_damage", 256),
      (val_div,":power",2),
      
      (try_begin),
        (assign,":max_range",300),
        (assign,":damage",200),
        (store_mul,":range_add",":power", 5),
        (store_mul,":damage_add",":power", ":basic_damage"),
        (val_add,":max_range",":range_add"),
        (store_add,":max_damage",":damage",":damage_add"),
        (val_div,":max_range",100),
      (try_end),
       
      
      (try_begin),
        (gt,":max_damage",0),
        (call_script, "script_magic_deliver_area_damage", ":shooter", ":max_damage", ":max_range", 15),
      (try_end),
      
    ])]

cast_magic_fire_ball = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt,":weapon",0),
      (assign,":damage",0),
      (this_or_next|eq,":weapon","itm_ebony_bow"),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
      
      (assign, ":cost_stamina", 25),
      (try_begin),
        (eq,":weapon","itm_ebony_bow"),
        (assign, ":cost_stamina", 0),
      (try_end),
      (try_begin),
        (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
        (ge, ":stamina", ":cost_stamina"),
        (val_sub, ":stamina", ":cost_stamina"),
        (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
      (else_try),
        (assign, ":power", 0),
      (try_end),
      
      (try_begin),
        (eq, ":weapon", "itm_warlock_staff_1"),
        (val_add,":power",1),
      (else_try),
        (eq, ":weapon", "itm_thunder_staff_1"),
        (val_add,":power",1),
      (else_try),
        (eq, ":weapon", "itm_pit_lord_sword"),
        (val_add,":power",3),
      (else_try),
        (eq, ":weapon", "itm_balor_sword"),
        (val_add,":power",2),
      (try_end),
      
      (try_begin),
        (assign,":max_range",300),
        (assign,":damage",200),
        (store_random_in_range, ":randon_damage", 50, 75),
        (store_mul,":range_add",":power", 60),
        (store_mul,":damage_add",":power", ":randon_damage"),
        (val_add,":max_range",":range_add"),
        (store_add,":max_damage",":damage",":damage_add"),
        (store_mul,":spec_power",":power", 2),
      (try_end),
       
      (copy_position,pos6,pos5),
      (position_move_z,pos6,150),
      (try_begin),
        (eq, "$g_weapon_fire_particle", 0),
        (gt,":damage",0),
        (gt,":power",0),
        (particle_system_burst, "psys_flame_explosion",pos5,50),
        (particle_system_burst, "psys_explosive_explosion_sparks_a", pos5, 35),
        (particle_system_burst, "psys_explosive_explosion_sparks_b", pos5, 35),
      (else_try),  
        (gt,":damage",0),
        (gt,":power",0),
        (particle_system_burst, "psys_flame_explosion",pos5,5),
        (particle_system_burst, "psys_explosive_explosion_sparks_a", pos5, 5),
        (particle_system_burst, "psys_explosive_explosion_sparks_b", pos5, 5),
      (try_end),
      (try_for_agents,":possable_agent"),
        (gt,":damage",0),
        (agent_is_alive,":possable_agent"),
        (this_or_next|agent_is_ally,":shooter"),
        (agent_is_ally,":possable_agent"),
        (this_or_next|neg|agent_is_ally,":possable_agent"),
        (neg|agent_is_ally,":shooter"),

        (agent_get_position,pos3,":possable_agent"),
        (get_distance_between_positions,":dist",pos5,pos3),
        (le,":dist",":max_range"),
        (assign,":agent",":possable_agent"),
        (val_add,":power",-1),
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":max_damage", burn, ":spec_power", ":power"),
        (try_begin),
          (agent_has_item_equipped,":shooter","itm_magic_book_2"),
          (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":max_damage", burn, ":spec_power", ":power"),
        (try_end),
        
        #(call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":damage", ice, 1, 15),
      (try_end),
    ])]

cast_magic_fire_ball_2 = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt,":weapon",0),
      (assign,":damage",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
          
      (assign, ":cost_stamina", 10),
      (try_begin),
        (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
        (ge, ":stamina", ":cost_stamina"),
        (val_sub, ":stamina", ":cost_stamina"),
        (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
      (else_try),
        (assign, ":power", 0),
      (try_end),
      
      
      (try_begin),
        (assign,":max_range",300),
        (assign,":damage",150),
        (store_mul,":range_add",":power", 50),
        (store_mul,":damage_add",":power", 60),
        (val_add,":max_range",":range_add"),
        (store_add,":max_damage",":damage",":damage_add"),
        (store_mul,":spec_power",":power", 2),

        (store_mul,":add_missile",":power", 1),
        (val_add,":add_missile",1),
      (try_end),
      
        (try_begin),
          (agent_has_item_equipped,":shooter","itm_magic_book_2"),
          (val_mul,":add_missile",2),
        (try_end),
        
      (position_get_distance_to_ground_level, ":distance", pos5),
      (try_begin),
        (lt, ":distance", 0),
        (position_set_z_to_ground_level, pos5),
        (position_move_z, pos5, 200),
      (try_end),                
      (try_begin),
        (eq, "$g_weapon_fire_particle", 0),
        (gt,":damage",0),
        (gt,":power",0),
        (particle_system_burst, "psys_flame_explosion",pos5,50),
        (particle_system_burst, "psys_explosive_explosion_sparks_a", pos5, 35),
        (particle_system_burst, "psys_explosive_explosion_sparks_b", pos5, 35),
      (else_try),  
        (gt,":damage",0),
        (gt,":power",0),
        (particle_system_burst, "psys_flame_explosion",pos5,5),
        (particle_system_burst, "psys_explosive_explosion_sparks_a", pos5, 5),
        (particle_system_burst, "psys_explosive_explosion_sparks_b", pos5, 5),
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
        (get_distance_between_positions,":dist",pos5,pos3),
        (le,":dist",":max_range"),
        (assign,":agent",":possable_agent"),
        
        (val_add,":power",-1),
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":max_damage", burn, ":spec_power", ":power"),
      (try_end),
      
      
      (play_sound_at_position, "snd_cannon_shot", pos5),          
      (position_move_z, pos5, 150),
      (try_for_range, ":unused", 0, ":add_missile"),
        (copy_position, pos2, pos5),
        (store_random_in_range, ":x_offset", 1, 361),#Random Rotation of X
        (position_rotate_x, pos2, ":x_offset"),    
        (store_random_in_range, ":y_offset", 1, 361),#Random Rotation of Y
        (position_rotate_y, pos2, ":y_offset"),    
        (store_random_in_range, ":z_offset", -10, 11),#Random Rotation of Z
        (position_rotate_z, pos2, ":z_offset"),   
        (set_fixed_point_multiplier,10),
        (add_missile, ":shooter", pos2, 80, ":weapon", 0, "itm_magic_poison_dummy", 0),
      (try_end),    
    ])]
    
    
cast_magic_fire_ball_3 = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt,":weapon",0),
      (assign,":damage",0),
      
      #(this_or_next|item_has_property,":weapon",itp_type_crossbow),
      #(item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
         
      (assign, ":cost_stamina", 10),
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_nilfurs_boast"),
        (assign, ":cost_stamina", 3),
      (try_end),
        (try_begin),
          (agent_has_item_equipped,":shooter","itm_magic_book_4"),
          (assign, ":cost_stamina", 3),
        (try_end),
      (try_begin),
        (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
        (ge, ":stamina", ":cost_stamina"),
        (val_sub, ":stamina", ":cost_stamina"),
        (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
      (else_try),
        (assign, ":power", 0),
      (try_end),
            
      (try_begin),
        (assign,":max_range",300),
        (assign,":damage",100),
        (store_mul,":range_add",":power", 30),
        (store_mul,":damage_add",":power", 50),
        (val_add,":max_range",":range_add"),
        (store_add,":max_damage",":damage",":damage_add"),
      (try_end),
      
      
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_magic_book_4"),
        (val_add,":max_damage",":damage_add"),
        (val_add,":max_range",":range_add"),
      (try_end),
      
      (try_begin),
        (eq, "$g_weapon_fire_particle", 0),
        (gt,":damage",0),
        (gt,":power",0),
         (particle_system_burst,"psys_bomb_fire_1",pos5,35),
         (particle_system_burst,"psys_Burning_Trail",pos5,50),
      (else_try),  
        (gt,":damage",0),
        (gt,":power",0),
         (particle_system_burst,"psys_bomb_fire_1",pos5,5),
         (particle_system_burst,"psys_Burning_Trail",pos5,5),
      (try_end),
            
      (try_for_agents,":possable_agent"),
        (gt,":damage",0),
        (agent_is_alive,":possable_agent"),
        (this_or_next|agent_is_ally,":shooter"),
        (agent_is_ally,":possable_agent"),
        (this_or_next|neg|agent_is_ally,":possable_agent"),
        (neg|agent_is_ally,":shooter"),

        (agent_get_position,pos3,":possable_agent"),
        (get_distance_between_positions,":dist",pos5,pos3),
        (le,":dist",":max_range"),
        (assign,":agent",":possable_agent"),
        (val_add,":power",-1),
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":max_damage", burn, ":power", 10),
         (try_begin),
           (neg|agent_is_human,":agent"),
           (agent_set_animation,":agent","anim_horse_rear"), 
           (agent_play_sound,":agent","snd_metal_hit_high_armor_high_damage"),
           (agent_deliver_damage_to_agent,":shooter",":agent"),
         (try_end),
      (try_end),
    ])]


cast_magic_lightning = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (assign,":damage",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
            
      (assign, ":cost_stamina", 10),
      (try_begin),
        (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
        (ge, ":stamina", ":cost_stamina"),
        (val_sub, ":stamina", ":cost_stamina"),
        (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
      (else_try),
        (assign, ":power", 0),
      (try_end),
            
      (try_begin),
        (assign,":max_range",120),
        (assign,":damage",100),
        (store_random_in_range, ":randon_damage", 25, 101),
        (store_mul,":range_add",":power", 30),
        (store_mul,":damage_add",":power", ":randon_damage"),
        (val_add,":max_range",":range_add"),
        (store_add,":max_damage",":damage",":damage_add"),
      (try_end),
      
        (assign,":victim",-1),
        (try_begin),
          (get_player_agent_no,":player"),
          (store_trigger_param_2, ":hit_object_type"),
          (neg|eq, ":hit_object_type", 1), # 1 = hostile agent
          (try_begin),
            (eq, ":player",":shooter"),
            (agent_get_slot, ":target", ":player", slot_agent_player_target),
          (else_try),
            (agent_ai_get_look_target, ":target", ":shooter"),
          (try_end),
          (gt,":target",0),
          (agent_is_alive,":target"),
          (neg|eq, ":player",":target"),
          (assign,":victim",":target"),
        (try_end),
        (try_begin),
          (ge,":victim",0),
          (agent_get_position, pos5, ":victim"),
        (else_try),
          (position_move_z,pos5,100),
        (try_end),
      
      
      #(position_move_z,pos5,100),
      (try_begin),
        (gt,":damage",0),
        (particle_system_burst, "psys_thunder", pos5, 1),
        (play_sound_at_position, "snd_thunder_hit", pos5),
      (try_end),
      (try_for_agents,":possable_agent"),
        (gt,":damage",0),
        (agent_is_alive,":possable_agent"),
        (this_or_next|agent_is_ally,":shooter"),
        (agent_is_ally,":possable_agent"),
        (this_or_next|neg|agent_is_ally,":possable_agent"),
        (neg|agent_is_ally,":shooter"),

        (agent_get_position,pos3,":possable_agent"),
        (get_distance_between_positions,":dist",pos5,pos3),
        (le,":dist",":max_range"),
        (assign,":agent",":possable_agent"),

        #(agent_deliver_damage_to_agent,":shooter",":agent", ":damage"),
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":max_damage", thunder, ":power", 15),
        #(agent_set_slot, ":agent", slot_agent_special_damage_type, poison),
        #(agent_set_slot, ":agent", slot_agent_special_damage_time, 15),
      (try_end),

    ])]

cast_magic_poison = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      
      (assign,":damage",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
            
      (assign, ":cost_stamina", 10),
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_plague_staff_1"),
        (assign, ":cost_stamina", 1),
      (try_end),
      (try_begin),
        (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
        (ge, ":stamina", ":cost_stamina"),
        (val_sub, ":stamina", ":cost_stamina"),
        (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
      (else_try),
        (assign, ":power", 0),
      (try_end),
            
      (try_begin),
        (assign,":max_range",200),
        (assign,":damage",50),
        (store_mul,":range_add",":power", 10),
        (store_mul,":damage_add",":power", 30),
        (val_add,":max_range",":range_add"),
        (store_add,":max_damage",":damage",":damage_add"),
        (store_mul,":spec_power",":power", 3),
      (try_end),
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_magic_book_8"),
        (val_add,":max_range",":range_add"),
        (val_mul,":spec_power",":power", 2),
      (try_end),
      
        (assign,":victim",-1),
        (try_begin),
          (get_player_agent_no,":player"),
          (store_trigger_param_2, ":hit_object_type"),
          (neg|eq, ":hit_object_type", 1), # 1 = hostile agent
          (try_begin),
            (eq, ":player",":shooter"),
            (agent_get_slot, ":target", ":player", slot_agent_player_target),
          (else_try),
            (agent_ai_get_look_target, ":target", ":shooter"),
          (try_end),
          (gt,":target",0),
          (agent_is_alive,":target"),
          (neg|eq, ":player",":target"),
          (assign,":victim",":target"),
        (try_end),
        (try_begin),
          (ge,":victim",0),
          (agent_get_position, pos5, ":victim"),
        (try_end),

      (try_begin),
        (eq, "$g_weapon_fire_particle", 0),
        (gt,":damage",0),
        (particle_system_burst, "psys_poison_cloud", pos5, 30),
      (else_try), 
        (gt,":damage",0),
        (particle_system_burst, "psys_poison_cloud", pos5, 3),
      (try_end),
      (try_for_agents,":possable_agent"),
        (gt,":damage",0),
        (agent_is_alive,":possable_agent"),
        (this_or_next|agent_is_ally,":shooter"),
        (agent_is_ally,":possable_agent"),
        (this_or_next|neg|agent_is_ally,":possable_agent"),
        (neg|agent_is_ally,":shooter"),

        (agent_get_position,pos3,":possable_agent"),
        (get_distance_between_positions,":dist",pos5,pos3),
        (le,":dist",":max_range"),
        (assign,":agent",":possable_agent"),

        #(agent_deliver_damage_to_agent,":shooter",":agent", ":damage"),
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":max_damage", poison, ":spec_power", 15),
      (try_end),
    ])]

cast_magic_Petrification = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt,":weapon",0),
      
      (assign,":max_damage",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
           
      (assign, ":cost_stamina", 30),

      (try_begin),
        (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
        (ge, ":stamina", ":cost_stamina"),
        (val_sub, ":stamina", ":cost_stamina"),
        (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
      (else_try),
        (assign, ":power", 0),
      (try_end),
            
      (try_begin),
        (assign,":max_range",200),
        (assign,":damage",100),
        (store_mul,":range_add",":power", 40),
        (store_mul,":damage_add",":power", 50),
        (val_add,":max_range",":range_add"),
        (store_add,":max_damage",":damage",":damage_add"),
        (store_mul,":spec_power",":power", 3),
      (try_end),
      
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_magic_book_8"),
        (val_add,":max_damage",":damage_add"),
        (val_add,":max_range",":range_add"),
        (val_mul,":spec_power",":power", 2),
      (try_end),
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_magic_book_9"),
        (val_add,":max_damage",":damage_add"),
        (val_add,":max_range",":range_add"),
        (val_mul,":spec_power",":power", 2),
      (try_end),
        (particle_system_burst, "psys_death_cloud", pos5, 10),
        (agent_play_sound,":shooter","snd_death_cld"),
      
      (try_for_agents,":possable_agent"),
        (gt,":max_damage",0),
        (agent_is_alive,":possable_agent"),
        (this_or_next|agent_is_ally,":shooter"),
        (agent_is_ally,":possable_agent"),
        (this_or_next|neg|agent_is_ally,":possable_agent"),
        (neg|agent_is_ally,":shooter"),

        (agent_get_position,pos3,":possable_agent"),
        (get_distance_between_positions,":dist",pos5,pos3),
        (le,":dist",":max_range"),
        (assign,":agent",":possable_agent"),
        (store_div,":half_damage",":max_damage",2),
        (store_random_in_range, ":damage", ":half_damage",":max_damage"),
        #(agent_deliver_damage_to_agent,":shooter",":agent", ":damage"),
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":damage", power_poison, ":power", ":spec_power"),
      (try_end),
    ])]
    

cast_magic_lightningball = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (assign,":damage",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
      
      (assign, ":cost_stamina", 25),
      (try_begin),
        (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
        (ge, ":stamina", ":cost_stamina"),
        (val_sub, ":stamina", ":cost_stamina"),
        (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
      (else_try),
        (assign, ":power", 0),
      (try_end),
            
      (try_begin),
        (assign,":max_range",300),
        (assign,":damage",90),
        (store_random_in_range, ":randon_damage", 10, 51),
        (store_mul,":range_add",":power", 40),
        (store_mul,":damage_add",":power", ":randon_damage"),
        (val_add,":max_range",":range_add"),
        (store_add,":max_damage",":damage",":damage_add"),
        (store_mul,":spec_power",":power", 2),
      (try_end),
      
      (try_begin),
        (this_or_next|eq, ":shooter_troop", "trp_knight_9_20"),
        (agent_has_item_equipped,":shooter","itm_magic_book_2"),
        (val_add,":max_range",":range_add"),
        (val_mul,":spec_power",":power", 2),
      (try_end),
      
      (try_begin),
        (eq, ":shooter_troop", "trp_knight_9_20"),
        (val_mul,":max_damage",":power", 4),
      (try_end),
      
      (copy_position,pos6,pos5),
      (position_move_z,pos6,300),
      (particle_system_burst, "psys_spark_explosion_small", pos6, 5),
      (try_for_agents,":possable_agent"),
        (gt,":damage",0),
        (agent_is_alive,":possable_agent"),
        (this_or_next|agent_is_ally,":shooter"),
        (agent_is_ally,":possable_agent"),
        (this_or_next|neg|agent_is_ally,":possable_agent"),
        (neg|agent_is_ally,":shooter"),

        (agent_get_position,pos3,":possable_agent"),
        (get_distance_between_positions,":dist",pos5,pos3),
        (le,":dist",":max_range"),
        (assign,":agent",":possable_agent"),
        (val_add,":power",-1),
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":max_damage", thunder, ":spec_power", ":power"),
        #(call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":damage", ice, 1, 15),
      (try_end),
    ])]

cast_magic_lightning_burst = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt,":weapon",0),
      (assign,":damage",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
                                
      (try_begin),
        (assign,":range",100),
        (store_mul,":range_add",":power", 15),
        (store_div,":damage",":power", 3),
        (val_add,":range",":range_add"),
        (val_add,":damage",1),
      (try_end),
     
      (try_begin),
        (eq, ":shooter_troop", "trp_knight_9_20"),
        (val_add,":damage", 3),
      (try_end),
              
        (assign,":victim",-1),        
        (try_begin),
          (get_player_agent_no,":player"),
          (neq, ":player",":shooter"),
          (store_trigger_param_2, ":hit_object_type"),
          (neg|eq, ":hit_object_type", 1), # 1 = hostile agent
          (agent_ai_get_look_target, ":target", ":shooter"),
          (gt,":target",0),
          (neg|eq, ":shooter",":player"),
          (agent_is_alive,":target"),
          (assign,":victim",":target"),
        (try_end),
        
        (try_for_agents,":agent"),
          (agent_is_alive,":agent"),
          (agent_is_human,":agent"),
          (eq,":victim",-1),
          
          (this_or_next|agent_is_ally,":shooter"),
          (agent_is_ally,":agent"),
          (this_or_next|neg|agent_is_ally,":agent"),
          (neg|agent_is_ally,":shooter"),
                              
          (agent_get_position, pos2, ":agent"),
          (get_distance_between_positions,":distance",pos2,pos5),
          (le,":distance",":range"),
          (call_script, "script_agent_get_num_companion_nearby", ":agent", 400),
          (assign, ":num_enemies", reg0),
          (this_or_next|le, ":num_enemies", 1),
          (ge, ":num_enemies", 6),
          (assign,":victim",":agent"),
        (try_end),
        (try_begin),
          (ge,":victim",0),
          (agent_get_position, pos5, ":victim"),
        (try_end),
        (copy_position,pos4,pos5),
        (try_for_range,":posz",0,":damage"),
          (store_random_in_range, ":posx", -2,3),
          (store_random_in_range, ":posy", -2,3),
          (val_mul,":posx",20),
          (val_mul,":posy",20),
          (val_mul,":posz",500),
          (position_move_x,pos4,":posx"),
          (position_move_y,pos4,":posy"),
          (position_move_z,pos4,":posz"),
          (add_missile, ":shooter", pos4, 0, ":weapon", 0, "itm_magic_lightningball", 0),
        (try_end),
    ])]
    

    
cast_magic_death_cloud = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt,":weapon",0),
      (assign,":damage",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
                                
      (try_begin),
        (assign,":range",100),
        (store_mul,":range_add",":power", 15),
        (store_div,":damage",":power", 3),
        (val_add,":range",":range_add"),
        (val_add,":damage",2),
      (try_end),
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_plague_staff_1"),
        (val_mul,":damage",2),
      (try_end),
              
        (assign,":victim",-1),        
        (try_begin),
          (get_player_agent_no,":player"),
          (neq, ":player",":shooter"),
          (store_trigger_param_2, ":hit_object_type"),
          (neg|eq, ":hit_object_type", 1), # 1 = hostile agent
          (agent_ai_get_look_target, ":target", ":shooter"),
          (gt,":target",0),
          (neg|eq, ":shooter",":player"),
          (agent_is_alive,":target"),
          (assign,":victim",":target"),
        (try_end),
        
        (try_for_agents,":agent"),
          (agent_is_alive,":agent"),
          (agent_is_human,":agent"),
          (eq,":victim",-1),
          
          (this_or_next|agent_is_ally,":shooter"),
          (agent_is_ally,":agent"),
          (this_or_next|neg|agent_is_ally,":agent"),
          (neg|agent_is_ally,":shooter"),
                              
          (agent_get_position, pos2, ":agent"),
          (get_distance_between_positions,":distance",pos2,pos5),
          (le,":distance",":range"),
          (call_script, "script_agent_get_num_companion_nearby", ":agent", 400),
          (assign, ":num_enemies", reg0),
          (this_or_next|le, ":num_enemies", 1),
          (ge, ":num_enemies", 6),
          (assign,":victim",":agent"),
        (try_end),
        (try_begin),
          (ge,":victim",0),
          (agent_get_position, pos5, ":victim"),
        (try_end),
        (copy_position,pos4,pos5),
        (try_for_range,":posz",0,":damage"),
          (store_random_in_range, ":posx", -2,3),
          (store_random_in_range, ":posy", -2,3),
          (val_mul,":posx",20),
          (val_mul,":posy",20),
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_plague_staff_1"),
        (val_mul,":posx",100),
        (val_mul,":posy",100),
      (try_end),
          (val_mul,":posz",500),
          (position_move_x,pos4,":posx"),
          (position_move_y,pos4,":posy"),
          (position_move_z,pos4,":posz"),
          (add_missile, ":shooter", pos4, 0, ":weapon", 0, "itm_magic_death_cloud_dummy", 0),
        (try_end),
    ])]
    
cast_magic_death_cloud_2 = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt,":weapon",0),
      
      (assign,":max_damage",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
           
      (assign, ":cost_stamina", 15),
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_plague_staff_1"),
        (assign, ":cost_stamina", 5),
      (try_end),
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_magic_book_8"),
        (assign, ":cost_stamina", 5),
      (try_end),
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_magic_book_9"),
        (assign, ":cost_stamina", 5),
      (try_end),
      
      (try_begin),
        (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
        (ge, ":stamina", ":cost_stamina"),
        (val_sub, ":stamina", ":cost_stamina"),
        (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
      (else_try),
        (assign, ":power", 0),
      (try_end),
            
      (try_begin),
        (assign,":max_range",200),
        (assign,":damage",50),
        (store_mul,":range_add",":power", 40),
        (store_mul,":damage_add",":power", 30),
        (val_add,":max_range",":range_add"),
        (store_add,":max_damage",":damage",":damage_add"),
        (store_mul,":spec_power",":power", 3),
      (try_end),
      
        (particle_system_burst, "psys_death_cloud", pos5, 10),
        (agent_play_sound,":shooter","snd_death_cld"),
      
      (try_for_agents,":possable_agent"),
        (gt,":max_damage",0),
        (agent_is_alive,":possable_agent"),
        (this_or_next|agent_is_ally,":shooter"),
        (agent_is_ally,":possable_agent"),
        (this_or_next|neg|agent_is_ally,":possable_agent"),
        (neg|agent_is_ally,":shooter"),

        (agent_get_position,pos3,":possable_agent"),
        (get_distance_between_positions,":dist",pos5,pos3),
        (le,":dist",":max_range"),
        (assign,":agent",":possable_agent"),
        (store_div,":half_damage",":max_damage",2),
        (store_random_in_range, ":damage", ":half_damage",":max_damage"),
        #(agent_deliver_damage_to_agent,":shooter",":agent", ":damage"),
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_magic_book_8"),
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":damage", power_poison, ":spec_power", ":power"),
      (else_try),
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":damage", poison, ":spec_power", ":power"),
      (try_end),
        (try_begin),
          (agent_has_item_equipped,":shooter","itm_magic_book_9"),
          (store_agent_hit_points, ":inflicted_agent_hp", ":agent", 0),
          (store_mul,":dead_power",":power", 5),
          (ge, ":dead_power", ":inflicted_agent_hp"),
          (agent_set_hit_points,":agent",0,0),
          (agent_deliver_damage_to_agent, ":shooter", ":agent", 100),
        (try_end),
        
      (try_end),
    ])]
    
cast_magic_incediary_cloud = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt,":weapon",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
      (assign,":damage",0),
      
      
      (try_begin),
        (eq, ":weapon", "itm_pit_lord_sword"),
        (val_add,":power",3),
      (try_end),
      
      (try_begin),
        (assign,":range",100),
        (store_mul,":range_add",":power", 15),
        (store_div,":damage",":power", 3),
        (val_add,":range",":range_add"),
        (val_add,":damage",1),
      (try_end),
      
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_magic_book_4"),
        (val_mul,":damage",2),
      (try_end),
        
        (assign,":victim",-1),
        (try_begin),
          (get_player_agent_no,":player"),
          (neq, ":player",":shooter"),
          (store_trigger_param_2, ":hit_object_type"),
          (neg|eq, ":hit_object_type", 1), # 1 = hostile agent
          (agent_ai_get_look_target, ":target", ":shooter"),
          (gt,":target",0),
          (neg|eq, ":shooter",":player"),
          (agent_is_alive,":target"),
          (assign,":victim",":target"),
        (try_end),
        (try_for_agents,":agent"),
          (agent_is_alive,":agent"),
          (agent_is_human,":agent"),
          (eq,":victim",-1),
          
          (this_or_next|agent_is_ally,":shooter"),
          (agent_is_ally,":agent"),
          (this_or_next|neg|agent_is_ally,":agent"),
          (neg|agent_is_ally,":shooter"),
                              
          (agent_get_position, pos2, ":agent"),
          (get_distance_between_positions,":distance",pos2,pos5),
          (le,":distance",":range"),
          (call_script, "script_agent_get_num_companion_nearby", ":agent", 400),
          (assign, ":num_enemies", reg0),
          (this_or_next|le, ":num_enemies", 1),
          (ge, ":num_enemies", 6),
          (assign,":victim",":agent"),
        (try_end),
        (try_begin),
          (ge,":victim",0),
          (agent_get_position, pos5, ":victim"),
        (try_end),
        (copy_position,pos4,pos5),
        (try_for_range,":posz",0,":damage"),
          (store_random_in_range, ":posx", -2,3),
          (store_random_in_range, ":posy", -2,3),
          (val_mul,":posx",20),
          (val_mul,":posy",20),
          (val_mul,":posz",500),
          (position_move_x,pos4,":posx"),
          (position_move_y,pos4,":posy"),
          (position_move_z,pos4,":posz"),
          (add_missile, ":shooter", pos4, 0, ":weapon", 0, "itm_magic_incediary_cloud_dummy", 0),
        (try_end),
    ])]
    
cast_magic_incediary_cloud_2 = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt,":weapon",0),
      
      (assign,":max_damage",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
      
      (assign, ":cost_stamina", 20),
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_magic_book_4"),
        (assign, ":cost_stamina", 10),
      (try_end),
      (try_begin),
        (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
        (ge, ":stamina", ":cost_stamina"),
        (val_sub, ":stamina", ":cost_stamina"),
        (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
      (else_try),
        (assign, ":power", 0),
      (try_end),
      
      (try_begin),
        (eq, ":weapon", "itm_pit_lord_sword"),
        (val_add,":power",3),
      (try_end),
      
      (try_begin),
        (assign,":max_range",200),
        (assign,":damage",50),
        (store_mul,":range_add",":power", 40),
        (store_mul,":damage_add",":power", 40),
        (val_add,":max_range",":range_add"),
        (store_add,":max_damage",":damage",":damage_add"),
        (store_div,":spec_power",":power", 2),
        (val_add,":spec_power",1),
        (store_div,":spec_time",":power", 3),
        (val_add,":spec_time",2),
      (try_end),


      (particle_system_burst, "psys_incediary_cloud", pos5, 10),
      (try_for_agents,":possable_agent"),
        (gt,":max_damage",0),
        (agent_is_alive,":possable_agent"),
        (this_or_next|agent_is_ally,":shooter"),
        (agent_is_ally,":possable_agent"),
        (this_or_next|neg|agent_is_ally,":possable_agent"),
        (neg|agent_is_ally,":shooter"),

        (agent_get_position,pos3,":possable_agent"),
        (get_distance_between_positions,":dist",pos5,pos3),
        (le,":dist",":max_range"),
        (assign,":agent",":possable_agent"),

        #(agent_set_slot, ":agent", slot_agent_special_damage_type, severe_burn),
        #(agent_set_slot, ":agent", slot_agent_special_damage_time, 3),
        
        (store_div,":half_damage",":max_damage",2),
        (store_random_in_range, ":damage", ":half_damage",":max_damage"),
        #(agent_deliver_damage_to_agent,":shooter",":agent", ":damage"),
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":damage", severe_burn, ":spec_power", ":spec_time"),
      (try_end),
    ])]
        
cast_magic_apocalypse = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt,":weapon",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
      (assign,":damage",0),
      
      (try_begin),
        (store_mul,":damage",":power", 6),
        (val_add,":damage",5),
        (assign,":range",100),
        (store_mul,":range_add",":power", 15),
        (val_add,":range",":range_add"),
      (try_end),
      
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_magic_book_4"),
        (val_mul, ":damage", 4),
        (val_add,":range",":range_add"),
      (try_end),
      
        (assign,":victim",-1),
        (try_begin),
          (get_player_agent_no,":player"),
          (neq, ":player",":shooter"),
          (store_trigger_param_2, ":hit_object_type"),
          (neg|eq, ":hit_object_type", 1), # 1 = hostile agent
          (agent_ai_get_look_target, ":target", ":shooter"),
          (gt,":target",0),
          (neg|eq, ":shooter",":player"),
          (agent_is_alive,":target"),
          (assign,":victim",":target"),
        (try_end),
        (try_begin),
          (ge,":victim",0),
          (agent_get_position, pos5, ":victim"),
        (try_end),
      
        (try_for_range,":unused",0,":damage"),
          (assign, ":cost_stamina", 3),
          (try_begin),
            (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
            (ge, ":stamina", ":cost_stamina"),
            (val_sub, ":stamina", ":cost_stamina"),
            (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
          (else_try),
            (assign, ":power", 1),
          (try_end),
          (copy_position,pos4,pos5),
          (store_random_in_range, ":posx", -25,26),
          (store_random_in_range, ":posy", -25,26),
          (store_random_in_range, ":posz", 30,70),
          (val_mul,":posx",50),
          (val_mul,":posy",50),
          (val_mul,":posz",100),
          (position_move_x,pos4,":posx"),
          (position_move_y,pos4,":posy"),
          (position_move_z,pos4,":posz"),
          #(position_move_z,pos5,":posz"),
          (add_missile, ":shooter", pos4, 0, ":weapon", 0, "itm_magic_fire_ray_dummy", 0),
          (try_begin),
            (eq, "$g_weapon_fire_particle", 0),
            (gt,":damage",0),
            (particle_system_burst, "psys_incediary_cloud", pos4, 5),
          (else_try),  
            (gt,":damage",0),
            (particle_system_burst, "psys_incediary_cloud", pos4, 1),
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
            (get_distance_between_positions,":dist",pos4,pos3),
            (le,":dist",250),
            (assign,":agent",":possable_agent"),
            (val_add,":power",-1),
            (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", 200, severe_burn, ":power", 5),
          (try_end),
        (try_end),
    ])]
cast_magic_fire_ray_dummy = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      
      (assign,":damage",0),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
      
      (assign, ":cost_stamina", 1),
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_magic_book_4"),
        (assign, ":cost_stamina", 0),
      (try_end),
      (try_begin),
        (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
        (ge, ":stamina", ":cost_stamina"),
        (val_sub, ":stamina", ":cost_stamina"),
        (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
      (else_try),
        (assign, ":power", 0),
      (try_end),
      
      (try_begin),
        (assign,":max_range",150),
        (assign,":damage",50),
        (store_mul,":damage_add",":power", 50),
        (store_add,":max_damage",":damage",":damage_add"),
        (store_mul,":range_add",":power", 20),
        (val_add,":max_range",":range_add"),
      (try_end),
      
      (try_begin),
        (eq, "$g_weapon_fire_particle", 0),
        (gt,":damage",0),
        (particle_system_burst, "psys_Burning_Trail", pos5, 15),
      (else_try),  
        (gt,":damage",0),
        (particle_system_burst, "psys_Burning_Trail", pos5, 3),
      (try_end),
      (try_for_agents,":possable_agent"),
        (gt,":max_damage",0),
        (gt,":power",0),
        (agent_is_alive,":possable_agent"),
        (this_or_next|agent_is_ally,":shooter"),
        (agent_is_ally,":possable_agent"),
        (this_or_next|neg|agent_is_ally,":possable_agent"),
        (neg|agent_is_ally,":shooter"),

        (agent_get_position,pos3,":possable_agent"),
        (get_distance_between_positions,":dist",pos5,pos3),
        (le,":dist",":max_range"),
        (assign,":agent",":possable_agent"),
        
        (val_add,":power",-1),
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":max_damage", burn, ":power", 5),
      (try_end),
    ])]
        
sldequiver_fire_trigger = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),

      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt,":weapon",0),
      
      (assign,":max_damage",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),


      (try_begin),
        (assign,":max_range",200),
        (assign,":damage",90),
        (store_mul,":range_add",":power", 40),
        (store_mul,":damage_add",":power", 50),
        (val_add,":max_range",":range_add"),
        (store_add,":max_damage",":damage",":damage_add"),
        (store_div,":spec_power",":power", 2),
        (val_add,":spec_power",1),
      (try_end),

      #(agent_get_wielded_item, ":weapon", ":shooter", 0),
         (particle_system_burst,"psys_arrows_fire_big",pos5,10),
         (particle_system_burst, "psys_incediary_cloud", pos5, 5),
      
      (try_for_agents,":possable_agent"),
         (gt,":max_damage",0),
         (agent_is_alive,":possable_agent"),
         (this_or_next|agent_is_ally,":shooter"),
         (agent_is_ally,":possable_agent"),
         (this_or_next|neg|agent_is_ally,":possable_agent"),
         (neg|agent_is_ally,":shooter"),			      

         (agent_get_position,pos3,":possable_agent"),
         (get_distance_between_positions,":dist",pos5,pos3),
         (neg|position_is_behind_position,pos5,pos3),
         (le,":dist",":max_range"),
         (assign,":agent",":possable_agent"),

         (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":damage", severe_burn, ":spec_power", ":power"),

         (try_begin),
           (neg|agent_is_human,":agent"),
           (agent_set_animation,":agent","anim_horse_rear"), 
           (agent_play_sound,":agent","snd_metal_hit_high_armor_high_damage"),
           (agent_deliver_damage_to_agent,":shooter",":agent"),
         (try_end),
        
      (try_end),
    ]),
    (ti_on_init_item, 
      [
        (set_position_delta, 0, 100, 0),
        (particle_system_add_new, "psys_torch_fire"),
        (particle_system_add_new, "psys_torch_smoke"),
        (set_current_color, 150, 130, 70),
        (add_point_light, 10, 30),
      ]),
]
    
cast_magic_armageddon = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt,":weapon",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
      (assign,":damage",0),
      
      (assign, ":cost_stamina", 60),
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_nilfurs_boast"),
        (assign, ":cost_stamina", 20),
      (try_end),
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_magic_book_4"),
        (assign,":cost_stamina",30),
      (try_end),
      (try_begin),
        (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
        (ge, ":stamina", ":cost_stamina"),
        (val_sub, ":stamina", ":cost_stamina"),
        (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
      (else_try),
        (assign, ":power", 0),
      (try_end),
      
      (try_begin),
        (store_div,":spec_power",":power", 2),
        (val_add,":damage",":spec_power"),
        (val_add,":damage",1),
      (try_end),
            
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_magic_book_7"),
        (val_add,":damage",":spec_power"),
      (try_end),
      
        (copy_position, pos51, pos5),
        (call_script,"script_cf_agent_spawn_agent_to_pos51", ":shooter", "trp_huge_inferno", 1),
        
        (store_mul,":damage_2",":damage", -1),
        (val_add,":damage_2",1),
        (try_for_range,":unused",0,":damage"),
          (copy_position,pos4,pos5),
          (store_random_in_range, ":posx", ":damage_2",":damage"),
          (store_random_in_range, ":posy", ":damage_2",":damage"),
          (store_random_in_range, ":posz", 10,100),
          (val_mul,":posx",50),
          (val_mul,":posy",50),
          (val_mul,":posz",200),
          (position_move_x,pos4,":posx"),
          (position_move_y,pos4,":posy"),
          (position_move_z,pos4,":posz"),
          #(position_move_z,pos5,":posz"),
          (add_missile, ":shooter", pos4, 0, ":weapon", 0, "itm_magic_armageddon_dummy", 0),
        (try_end),
      
      
    ])]
    
cast_magic_armageddon_2 = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (copy_position,pos51,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (ge, ":weapon", -1),
      
      (assign,":damage",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
      
      (assign, ":cost_stamina", 0),
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
        (assign,":damage",166),
        (store_mul,":range_add",":power", 50),
        (store_mul,":damage_add",":power", 36),
        (val_add,":max_range",":range_add"),
        (store_add,":max_damage",":damage",":damage_add"),
        (store_div,":spec_power",":power", 2),
        (val_add,":spec_power",1),
      (try_end),
      
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_magic_book_4"),
        (val_mul,":max_damage",2),
        (val_mul,":max_range",2),
      (try_end),
      
      (try_begin),
        (gt,":power",1),
        (eq, "$g_weapon_fire_particle", 0),
        
        (particle_system_burst, "psys_bomb_fire_1", pos5, 20),
        (particle_system_burst, "psys_bomb_smoke", pos5, 20),
        (particle_system_burst, "psys_bomb_dust", pos5, 10),
        
        (copy_position, pos51, pos5),
        (try_begin),
          (agent_has_item_equipped,":shooter","itm_nilfurs_boast"),
          (assign, ":troop", "trp_huge_inferno"),
        (else_try),
          (assign, ":troop", "trp_inferno"),
        (try_end),
        (call_script,"script_cf_agent_spawn_agent_to_pos51", ":shooter", ":troop", 1),
      (try_end),
      (position_move_z,pos5,90),
      (try_for_agents,":possable_agent"),
        (gt,":max_damage",0),
        (agent_is_alive,":possable_agent"),
        (this_or_next|agent_is_ally,":shooter"),
        (agent_is_ally,":possable_agent"),
        (this_or_next|neg|agent_is_ally,":possable_agent"),
        (neg|agent_is_ally,":shooter"),

        (agent_get_position,pos3,":possable_agent"),
        (get_distance_between_positions,":dist",pos5,pos3),
        (le,":dist",":max_range"),
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":possable_agent", ":max_damage", severe_burn, ":spec_power", ":power"),
      (try_end),
    ])]
    
cast_magic_meteor_shower = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt,":weapon",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
      (assign,":damage",0),
      
      (assign, ":cost_stamina", 30),
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_nilfurs_boast"),
        (assign, ":cost_stamina", 10),
      (try_end),
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_magic_book_4"),
        (val_add, ":cost_stamina", -10),
      (try_end),
      
      
      (try_begin),
        (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
        (ge, ":stamina", ":cost_stamina"),
        (val_sub, ":stamina", ":cost_stamina"),
        (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
      (else_try),
        (assign, ":power", 0),
      (try_end),
      
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_nilfurs_boast"),
        (val_mul,":power",2),
      (try_end),
      (try_begin),
        (this_or_next|eq, ":weapon", "itm_pit_lord_sword"),
        (this_or_next|eq, ":weapon", "itm_bishop_staff_2"),
        (eq, ":weapon", "itm_archlich_staff_1"),
        (val_add,":power",3),
      (try_end),
      
      (try_begin),
        (assign,":range",100),
        (assign,":damage",3),
        (store_mul,":damage",":power", 2),
        (store_mul,":range_add",":power", 30),
        (val_add,":range",":range_add"),
        (val_add,":damage",":power"),
      (try_end),
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_magic_book_4"),
        (val_add,":range",":range_add"),
        (val_add,":damage",":power"),
      (try_end),
        
        (assign,":victim",-1),
        (try_begin),
          (get_player_agent_no,":player"),
          (neq, ":player",":shooter"),
          (store_trigger_param_2, ":hit_object_type"),
          (neg|eq, ":hit_object_type", 1), # 1 = hostile agent
          (agent_ai_get_look_target, ":target", ":shooter"),
          (gt,":target",0),
          (neg|eq, ":shooter",":player"),
          (agent_is_alive,":target"),
          (assign,":victim",":target"),
        (try_end),
        (try_begin),
          (ge,":victim",0),
          (agent_get_position, pos5, ":victim"),
        (try_end),
        #(val_mul,":damage",2),
        (try_for_range,":unused",0,":damage"),
          (copy_position,pos4,pos5),
          (store_random_in_range, ":posx", -50,51),
          (store_random_in_range, ":posy", -50,51),
          (store_random_in_range, ":posz", 10,100),
          (val_mul,":posx",30),
          (val_mul,":posy",30),
          (val_mul,":posz",100),
          (position_move_x,pos4,":posx"),
          (position_move_y,pos4,":posy"),
          (position_move_z,pos4,":posz"),
          #(position_move_z,pos5,":posz"),
          #(add_missile, ":shooter", pos4, 0, ":weapon", 0, "itm_magic_meteor_shower_dummy", 0),
          (add_missile, ":shooter", pos4, 80, ":weapon", 0, "itm_magic_poison_dummy", 0),
        (try_end),
    ])]
    
cast_magic_heaven_fist = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt,":weapon",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
      (assign,":damage",0),
      
      (try_begin),
        (eq, ":weapon", "itm_bishop_staff"),
        (val_add,":power",2),
      (else_try),
        (eq, ":weapon", "itm_bishop_staff_2"),
        (val_add,":power",3),
      (try_end),
      
      (try_begin),
        (assign,":range",100),
        (assign,":damage",3),
        (store_mul,":range_add",":power", 30),
        (val_add,":range",":range_add"),
        (val_add,":damage",":power"),
        (val_div,":damage",3),
        (val_add,":damage",1),
      (try_end),

      (try_begin),
        (agent_has_item_equipped,":shooter","itm_magic_book_4"),
        (val_add,":range",":range_add"),
        (val_add,":damage",2),
      (try_end),

      (try_begin),
        (eq, ":weapon", "itm_war_clerics_warhammer_cast"),
        (assign,":damage",1),
      (else_try),
        (eq, ":weapon", "itm_war_clerics_warhammer_cast_2"),
        (assign,":damage",1),
      (try_end),

        (assign,":victim",-1),
        (try_begin),
          (get_player_agent_no,":player"),
          (store_trigger_param_2, ":hit_object_type"),
          (neg|eq, ":hit_object_type", 1), # 1 = hostile agent
          (try_begin),
            (eq, ":player",":shooter"),
            (agent_get_slot, ":target", ":player", slot_agent_player_target),
          (else_try),
            (agent_ai_get_look_target, ":target", ":shooter"),
          (try_end),
          (gt,":target",0),
          (agent_is_alive,":target"),
          (neg|eq, ":player",":target"),
          (assign,":victim",":target"),
        (try_end),
        (try_for_agents,":agent"),
          (agent_is_alive,":agent"),
          (agent_is_human,":agent"),
          (eq,":victim",-1),
          
          (this_or_next|agent_is_ally,":shooter"),
          (agent_is_ally,":agent"),
          (this_or_next|neg|agent_is_ally,":agent"),
          (neg|agent_is_ally,":shooter"),
                              
          (agent_get_position, pos2, ":agent"),
          (get_distance_between_positions,":distance",pos2,pos5),
          (le,":distance",":range"),
          (call_script, "script_agent_get_num_companion_nearby", ":agent", 700),
          (assign, ":num_enemies", reg0),
          (this_or_next|le, ":num_enemies", 1),
          (ge, ":num_enemies", 6),
          (assign,":victim",":agent"),
        (try_end),
        (try_begin),
          (ge,":victim",0),
          (agent_get_position, pos5, ":victim"),
        (try_end),
        
        (position_move_z,pos5,500),
        (try_for_range,":posz",0,":damage"),
          (copy_position,pos4,pos5),
          (store_random_in_range, ":posx", -10,11),
          (store_random_in_range, ":posy", -10,11),
          (val_mul,":posx",5),
          (val_mul,":posy",5),
          (val_mul,":posz",100),
          (position_move_x,pos4,":posx"),
          (position_move_y,pos4,":posy"),
          (position_move_z,pos4,":posz"),
          (position_move_z,pos5,":posz"),
          (add_missile, ":shooter", pos4, 0, ":weapon", 0, "itm_magic_heaven_fist_dummy", 0),
        (try_end),
    ])]
    
cast_magic_heaven_fist_2 = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt,":weapon",0),
      (assign,":damage",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
      
      (assign, ":cost_stamina", 10),
      (try_begin),
        (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
        (ge, ":stamina", ":cost_stamina"),
        (val_sub, ":stamina", ":cost_stamina"),
        (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
      (else_try),
        (assign, ":power", 0),
      (try_end),
      
      (try_begin),
        (eq, ":weapon", "itm_bishop_staff"),
        (val_add,":power",1),
      (else_try),
        (eq, ":weapon", "itm_bishop_staff_2"),
        (val_add,":power",2),
      (else_try),
        (eq, ":weapon", "itm_war_clerics_warhammer_cast"),
        (val_add,":power",1),
      (else_try),
        (eq, ":weapon", "itm_war_clerics_warhammer_cast_2"),
        (val_add,":power",2),
      (try_end),
      
      (try_begin),
        (assign,":max_range",100),
        (assign,":damage",50),
        (store_mul,":range_add",":power", 30),
        (store_mul,":damage_add",":power", 30),
        (val_add,":max_range",":range_add"),
        (store_add,":max_damage",":damage",":damage_add"),
        (store_div,":spec_power",":power", 2),
        (val_add,":spec_power",1),
      (try_end),
      
            
      (try_begin),
        (gt,":max_damage",0),
        (particle_system_burst, "psys_holy_fire", pos5, 50),
      (try_end),
      (try_for_agents,":possable_agent"),
        (gt,":max_damage",0),
        (agent_is_alive,":possable_agent"),
        (this_or_next|agent_is_ally,":shooter"),
        (agent_is_ally,":possable_agent"),
        (this_or_next|neg|agent_is_ally,":possable_agent"),
        (neg|agent_is_ally,":shooter"),

        (agent_get_position,pos3,":possable_agent"),
        (get_distance_between_positions,":dist",pos5,pos3),
        (le,":dist",":max_range"),
        (assign,":agent",":possable_agent"),

        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":max_damage", holy_fire, ":spec_power", ":power"),
      (try_end),
    ])]
    
cast_magic_heaven_fist_3 = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt,":weapon",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
      (assign,":damage",0),
      
      (try_begin),
        (assign,":range",100),
        (assign,":damage",3),
        (store_mul,":range_add",":power", 30),
        (val_add,":range",":range_add"),
        (val_add,":damage",":power"),
        (val_div,":damage",3),
        (val_add,":damage",1),
      (try_end),
        
        (position_move_z,pos5,500),
        (try_for_range,":posz",0,":damage"),
          (copy_position,pos4,pos5),
          (store_random_in_range, ":posx", -10,11),
          (store_random_in_range, ":posy", -10,11),
          (val_mul,":posx",5),
          (val_mul,":posy",5),
          (val_mul,":posz",100),
          (position_move_x,pos4,":posx"),
          (position_move_y,pos4,":posy"),
          (position_move_z,pos4,":posz"),
          (position_move_z,pos5,":posz"),
          (add_missile, ":shooter", pos4, 0, "itm_magic_heaven_fist_throw_1", 0, "itm_magic_heaven_fist_throw_1", 0),
        (try_end),
    ])]

    
natalyas_mark = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos51,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt,":weapon",0),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
      (assign,":damage",0),
      
      (assign, ":cost_stamina", 10),
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_natalya_slayer"),
        (assign, ":cost_stamina", 0),
      (try_end),
      
      
      (try_begin),
        (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
        (ge, ":stamina", ":cost_stamina"),
        (val_sub, ":stamina", ":cost_stamina"),
        (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
      (else_try),
        (assign, ":power", 0),
      (try_end),
      
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_nilfurs_boast"),
        (val_mul,":power",2),
      (try_end),
      
        (assign,":damage",3),
        (val_add,":damage",":power"),
      
      
      (position_get_distance_to_ground_level, ":distance", pos51),
      (try_begin),
        (lt, ":distance", 0),
        (position_set_z_to_ground_level, pos51),
        (position_move_z, pos51, 200),
      (try_end),                
        
        (assign,":victim",-1),
        (try_begin),
          (get_player_agent_no,":player"),
          (neq, ":player",":shooter"),
          (store_trigger_param_2, ":hit_object_type"),
          (neg|eq, ":hit_object_type", 1), # 1 = hostile agent
          (agent_ai_get_look_target, ":target", ":shooter"),
          (gt,":target",0),
          (neg|eq, ":shooter",":player"),
          (agent_is_alive,":target"),
          (assign,":victim",":target"),
        (try_end),
        (try_begin),
          (ge,":victim",0),
          (agent_get_position, pos51, ":victim"),
        (try_end),
        
        (store_mul,":damage_2",":damage", -1),
        (val_add,":damage_2",1),
        
        (try_for_range, ":posz", 0, ":damage"),
          (copy_position, pos52, pos51),
          (assign, ":cost_stamina", 10),
          (try_begin),
            (agent_has_item_equipped,":shooter","itm_natalya_slayer"),
            (assign, ":cost_stamina", 5),
          (try_end),
          (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
          (ge, ":stamina", ":cost_stamina"),
          (val_sub, ":stamina", ":cost_stamina"),
          (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
        
          (store_random_in_range, ":posx", ":damage_2",":damage"),
          (store_random_in_range, ":posy", ":damage_2",":damage"),
          (val_mul,":posx",50),
          (val_mul,":posy",50),
          (val_mul,":posz",100),
          (position_move_x,pos52,":posx"),
          (position_move_y,pos52,":posy"),
          (position_move_z,pos52,":posz"),
          (position_move_z,pos51,":posz"),
          (set_fixed_point_multiplier,1),
          (add_missile, ":shooter", pos52, 0, ":weapon", 0, "itm_magic_meteor_shower_dummy", 0),
        (try_end), 
    ])]
    
cast_magic_summon_blade = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt,":weapon",0),
      (assign,":number",10),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_necromancy, ":shooter_troop"),
      (val_add,":power",1),
        (val_mul,":number",2),
        (store_mul,":number_2",":number", -1),
        (val_add,":number_2",1),
        (try_for_range,":unused",0,":power"),
          (copy_position,pos51,pos5),
          (store_random_in_range, ":posx", ":number_2",":number"),
          (store_random_in_range, ":posy", ":number_2",":number"),
          (val_mul,":posx",50),
          (val_mul,":posy",50),
          (position_move_x,pos51,":posx"),
          (position_move_y,pos51,":posy"),
          (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
          (ge, ":stamina", 5),
          (val_sub, ":stamina", 5),
          (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
          (call_script,"script_cf_agent_spawn_agent_to_pos51", ":shooter", "trp_mercenaries_end", 1),
        (try_end),
    ])]
    
cast_magic_summon_Zombie_Lord = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt,":weapon",0),
      (assign,":number",10),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_necromancy, ":shooter_troop"),
      (val_add,":power",1),
        (val_mul,":number",2),
        (store_mul,":number_2",":number", -1),
        (val_add,":number_2",1),
        (try_for_range,":unused",0,":power"),
          (copy_position,pos51,pos5),
          (store_random_in_range, ":posx", ":number_2",":number"),
          (store_random_in_range, ":posy", ":number_2",":number"),
          (val_mul,":posx",50),
          (val_mul,":posy",50),
          (position_move_x,pos51,":posx"),
          (position_move_y,pos51,":posy"),
          (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
          (ge, ":stamina", 5),
          (val_sub, ":stamina", 5),
          (try_begin),
            (eq, ":shooter_troop", "trp_lich_dragon"),
            (val_add, ":stamina", 5),
          (try_end),
          (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
          (store_random_in_range, ":r", 0, 3),
          (assign,":number",1),
          (try_begin),
            (eq, ":r", 0),
            (store_random_in_range, ":spawn_troop_id", "trp_zombie_1", "trp_skeleton"),
          (else_try),
            (store_random_in_range, ":spawn_troop_id", "trp_draugr_1", "trp_mummy_2_1"),
          (try_end),
          (call_script,"script_cf_agent_spawn_agent_to_pos51", ":shooter", ":spawn_troop_id", 1),
        (try_end),
    ])]
    
cast_magic_summon_Soulhunter = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt,":weapon",0),
      (assign,":number",10),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_necromancy, ":shooter_troop"),
      (call_script,"script_cf_agent_spawn_agent_to_pos51", ":shooter", "trp_wraith", 1),
      (val_add,":power",1),
      (val_mul,":number",2),
      (store_mul,":number_2",":number", -1),
      (val_add,":number_2",1),
        (try_for_range,":unused",0,":power"),
          (copy_position,pos51,pos5),
          (store_random_in_range, ":posx", ":number_2",":number"),
          (store_random_in_range, ":posy", ":number_2",":number"),
          (val_mul,":posx",50),
          (val_mul,":posy",50),
          (position_move_x,pos51,":posx"),
          (position_move_y,pos51,":posy"),
          (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
          (ge, ":stamina", 5),
          (val_sub, ":stamina", 5),
          (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
          (store_random_in_range, ":r", 0, 2),
          (assign,":number",1),
          (try_begin),
            (eq, ":r", 0),
            (assign, ":spawn_troop_id", "trp_ghost"),
          (else_try),
            (assign, ":spawn_troop_id", "trp_wight"),
          (try_end),
          (call_script,"script_cf_agent_spawn_agent_to_pos51", ":shooter", ":spawn_troop_id", 1),
        (try_end),
    ])]
    
    
cast_magic_summon_undead = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt,":weapon",0),
      (assign,":spawn_troop_id",0),
      (assign,":number",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_necromancy, ":shooter_troop"),
      
      (assign, ":cost_stamina", 33),
      (try_begin),
        (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
        (ge, ":stamina", ":cost_stamina"),
        (val_sub, ":stamina", ":cost_stamina"),
        (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
      (else_try),
        (assign, ":power", 0),
      (try_end),
      
      (store_character_level,":troop_level",":shooter_troop"),
      (val_mul,":power",5),
      (val_add,":power",":troop_level"),
      (try_begin),
        (ge, ":power", 60),
        (store_random_in_range, ":r", 0, 10),
        (assign,":number",3),
        (try_begin),
          (ge, ":r", 6),
          (assign,":spawn_troop_id","trp_draugr_lord"),
          (assign,":number",2),
        (else_try),
          (ge, ":r", 4),
          (assign,":spawn_troop_id","trp_wight"),
        (else_try),
          (assign,":spawn_troop_id","trp_dullahan"),
        (try_end),
      (else_try),
        (ge, ":power", 45),
        (store_random_in_range, ":r", 0, 10),
        (assign,":number",2),
        (try_begin),
          (ge, ":r", 6),
          (assign,":spawn_troop_id","trp_draugr_lord"),
          (assign,":number",1),
        (else_try),
          (ge, ":r", 4),
          (assign,":spawn_troop_id","trp_wight"),
        (else_try),
          (assign,":spawn_troop_id","trp_dullahan"),
        (try_end),
      (else_try),
        (ge, ":power", 30),
        (store_random_in_range, ":r", 0, 10),
        (assign,":number",1),
        (try_begin),
          (ge, ":r", 6),
          (assign,":spawn_troop_id","trp_dullahan"),
        (else_try),
          (ge, ":r", 4),
          (assign,":spawn_troop_id","trp_skeleton_lord"),
        (else_try),
          (assign,":spawn_troop_id","trp_draugr_3"),
        (try_end),
      (else_try),
        (ge, ":power", 15),
        (store_random_in_range, ":r", 0, 10),
        (assign,":number",2),
        (try_begin),
          (ge, ":r", 8),
          (assign,":spawn_troop_id","trp_draugr_2"),
        (else_try),
          (ge, ":r", 4),
          (assign,":spawn_troop_id","trp_skeleton_warrior"),
          (assign,":number",1),
        (else_try),
          (assign,":spawn_troop_id","trp_zombie_2"),
        (try_end),
      (else_try),
        (store_random_in_range, ":r", 0, 10),
        (assign,":number",2),
          (try_begin),
            (ge, ":r", 8),
            (assign,":spawn_troop_id","trp_draugr_1"),
          (else_try),
            (ge, ":r", 5),
            (assign,":spawn_troop_id","trp_se_billman_1"),
          (else_try),
            (assign,":spawn_troop_id","trp_zombie_1"),
          (try_end),
      (try_end),
      
      (try_begin),
        (eq, ":shooter_troop", "trp_mummy_3"),
        (assign,":spawn_troop_id","trp_mummy_2"),
        (assign,":number",2),
      (else_try),
        (eq, ":shooter_troop", "trp_adventurer_troop_15"),
        (assign,":spawn_troop_id","trp_demon_8"),
        (assign,":number",2),
      (else_try),
        (eq, ":shooter_troop", "trp_adventurer_troop_1"),
        (store_random_in_range, ":r", 0, 10),
        (assign,":number",2),
        (try_begin),
          (ge, ":r", 6),
          (assign,":spawn_troop_id","trp_wight"),
        (else_try),
          (assign,":spawn_troop_id","trp_ghost"),
          (assign,":number",4),
        (try_end),
      (else_try),
        (eq, ":shooter_troop", "trp_polish_which_1"),
        (store_random_in_range, ":r", 0, 10),
        (assign,":number",1),
        (try_begin),
          (ge, ":r", 6),
          (assign,":spawn_troop_id","trp_air_elemental"),
        (else_try),
          (assign,":spawn_troop_id","trp_ghost"),
          (assign,":number",2),
        (try_end),
      (else_try),
        (eq, ":shooter_troop", "trp_polish_which_2"),
        (store_random_in_range, ":r", 0, 10),
        (assign,":number",1),
        (try_begin),
          (ge, ":r", 5),
          (assign,":spawn_troop_id","trp_demon_4"),
        (else_try),
          (assign,":spawn_troop_id","trp_wight"),
          (assign,":number",2),
        (try_end),
      (else_try),
        (this_or_next|eq,":weapon","itm_dragonpriest_staff_1"),
        (this_or_next|eq, ":shooter_troop", "trp_lich_3"),
        (eq, ":shooter_troop", "trp_knight_10_14"),
        (assign,":spawn_troop_id","trp_draugr_lord"),
        (assign,":number",2),
      (else_try),
        (eq, ":shooter_troop", "trp_mummy_4"),
        (store_random_in_range, ":r", 0, 10),
        (assign,":number",2),
        (try_begin),
          (ge, ":r", 9),
          (assign,":spawn_troop_id","trp_werewolf_1_a"),
          (assign,":number",1),
        (else_try),
          (ge, ":r", 7),
          (assign,":spawn_troop_id","trp_werewolf_1"),
        (else_try),
          (ge, ":r", 5),
          (assign,":spawn_troop_id","trp_mummy_2_1"),
        (else_try),
          (assign,":spawn_troop_id","trp_mummy_2"),
        (try_end),
      (try_end),
      
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_magic_book_9"),
        (store_random_in_range, ":r", 0, 10),
        (assign,":number",2),
        (try_begin),
          (ge, ":r", 8),
          (assign,":spawn_troop_id","trp_mummy_4"),
        (else_try),
          (ge, ":r", 5),
          (assign,":spawn_troop_id","trp_werewolf_1_a"),
        (else_try),
          (assign,":spawn_troop_id","trp_mummy_3"),
        (try_end),
      (else_try),
        (agent_has_item_equipped,":shooter","itm_magic_book_6"),
        (store_random_in_range, ":ran", 0, 8),
        (assign,":number",1),
        (try_begin),
          (eq,":ran",0),
          (assign,":spawn_troop_id","trp_lich_2"),
        (else_try),  
          (eq,":ran",1),
          (assign,":spawn_troop_id","trp_ghost_dragon"),
        (else_try),  
          (eq,":ran",2),
          (assign,":spawn_troop_id","trp_lich_dragon"),
        (else_try),  
          (eq,":ran",3),
          (assign,":spawn_troop_id","trp_wraith"),
        (else_try),  
          (eq,":ran",4),
          (assign,":spawn_troop_id","trp_death"),
        (else_try),  
          (eq,":ran",5),
          (assign,":spawn_troop_id","trp_bone_dragon"),
          (assign,":number",2),
        (else_try),  
          (eq,":ran",6),
          (assign,":spawn_troop_id","trp_draugr_lord"),
        (else_try),  
          (eq,":ran",7),
          (assign,":spawn_troop_id","trp_mummy_3"),
        (try_end),  
      (try_end),
      
      
      (gt,":spawn_troop_id",0),
      (gt,":number",0),
        
        (copy_position, pos51, pos5),
        (call_script,"script_cf_agent_spawn_agent_to_pos51", ":shooter", ":spawn_troop_id", ":number"),
    ])]
    
goblin_summon = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),

      (particle_system_burst, "psys_bomb_dust", pos5, 5),
      (assign,":spawn_troop_id",0),
      (assign,":number",0),
      (store_random_in_range, ":r", 0, 10),
      (assign,":number",1),
      (try_begin),
          (ge, ":r", 9),
          (assign,":spawn_troop_id","trp_goblin_bomber"),
      (else_try),
          (ge, ":r", 6),
          (assign,":spawn_troop_id","trp_goblin_guard"),
      (else_try),
          (ge, ":r", 4),
          (assign,":spawn_troop_id","trp_goblin_infantry"),
      (else_try),
          (assign,":spawn_troop_id","trp_goblin_footman"),
      (try_end),
        
      (gt,":spawn_troop_id",0),
      (gt,":number",0),
        
      (copy_position, pos51, pos5),
      (call_script,"script_cf_agent_spawn_agent_to_pos51", ":shooter", ":spawn_troop_id", ":number"),
    ])]
    
    
cast_magic_summon_neutral = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt,":weapon",0),
      (assign,":spawn_troop_id",0),
      (assign,":number",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_necromancy, ":shooter_troop"),
      
      (assign, ":cost_stamina", 33),
      (try_begin),
        (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
        (ge, ":stamina", ":cost_stamina"),
        (val_sub, ":stamina", ":cost_stamina"),
        (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
      (else_try),
        (assign, ":power", 0),
      (try_end),
            
      (store_character_level,":troop_level",":shooter_troop"),
      (val_mul,":power",5),
      (val_add,":power",":troop_level"),
      (try_begin),
        (ge, ":power", 60),
        (store_random_in_range, ":r", 0, 10),
        (assign,":number",1),
        (try_begin),
          (ge, ":r", 8),
          (assign,":spawn_troop_id","trp_fire_elemental_3"),
        (else_try),
          (ge, ":r", 6),
          (assign,":spawn_troop_id","trp_earth_elemental_3"),
        (else_try),
          (ge, ":r", 4),
          (assign,":spawn_troop_id","trp_water_elemental_3"),
        (else_try),
          (assign,":spawn_troop_id","trp_golem_4"),
        (try_end),
      (else_try),
        (ge, ":power", 40),
        (store_random_in_range, ":r", 0, 10),
        (assign,":number",1),
        (try_begin),
          (ge, ":r", 8),
          (assign,":spawn_troop_id","trp_gargoyle"),
        (else_try),
          (ge, ":r", 6),
          (assign,":spawn_troop_id","trp_earth_elemental_2"),
        (else_try),
          (ge, ":r", 4),
          (assign,":spawn_troop_id","trp_fire_elemental_2"),
        (else_try),
          (assign,":spawn_troop_id","trp_water_elemental_2"),
        (try_end),
      (else_try),
        (ge, ":power", 20),
        (store_random_in_range, ":r", 0, 10),
        (assign,":number",1),
        (try_begin),
          (ge, ":r", 8),
          (assign,":spawn_troop_id","trp_air_elemental_2"),
        (else_try),
          (ge, ":r", 6),
          (assign,":spawn_troop_id","trp_water_elemental"),
        (else_try),
          (ge, ":r", 4),
          (assign,":spawn_troop_id","trp_mercenaries_end"),
          (assign,":number",2),
        (else_try),
          (assign,":spawn_troop_id","trp_golem_3"),
        (try_end),
      (else_try),
        (store_random_in_range, ":r", 0, 10),
        (assign,":number",1),
        (try_begin),
          (eq, ":r", 1),
          (assign,":spawn_troop_id","trp_air_elemental"),
        (else_try),
          (ge, ":r", 8),
          (assign,":spawn_troop_id","trp_golem_1"),
        (else_try),
          (ge, ":r", 6),
          (assign,":spawn_troop_id","trp_firefly"),
          (assign,":number",2),
        (else_try),
          (assign,":spawn_troop_id","trp_dragonfly"),
          (assign,":number",2),
        (try_end),
      (try_end),
      
      (try_begin),
        (eq,"$background_answer_2",cb2_apprentice),
        (eq,"$background_answer_3",cb3_craftsman),
        (lt, ":power", 40),
        (assign,":spawn_troop_id","trp_golem_3"),
        (assign,":number",1),
      (else_try),
        (lt, ":power", 20),
        (eq,"$background_answer_3",cb3_craftsman),
        (assign,":spawn_troop_id","trp_golem_1"),
        (assign,":number",1),
      (try_end),
            
      (try_begin),
        (eq, ":shooter_troop", "trp_grandelf_mage_1"),
        (store_random_in_range, ":r", 0, 10),
        (try_begin),
          (assign, ":spawn_troop_id","trp_earth_elemental_3"),
          (assign,":number",2),
        (else_try),
          (assign, ":spawn_troop_id","trp_earth_elemental_2"),
          (assign,":number",2),
        (try_end),
      (else_try),
        (eq, ":shooter_troop", "trp_grandelf_mage_2"),
        (store_random_in_range, ":r", 0, 10),
        (try_begin),
          (ge, ":r", 6),
          (assign, ":spawn_troop_id","trp_ent_1"),
          (assign,":number",1),
        (else_try),
          (assign, ":spawn_troop_id","trp_pixie"),
          (assign,":number",2),
        (try_end),
      (else_try),
        (eq, ":shooter_troop", "trp_woodelf_druid_2"),
        (store_random_in_range, ":r", 0, 10),
        (try_begin),
          (ge, ":r", 9),
          (store_random_in_range, ":spawn_troop_id","trp_red_dragon","trp_werewolf_1"),
          (assign,":number",1),
        (else_try),
          (ge, ":r", 4),
          (assign, ":spawn_troop_id","trp_ent_2"),
          (assign,":number",1),
        (else_try),
          (store_random_in_range, ":spawn_troop_id","trp_air_elemental_2","trp_air_elemental_3"),
          (assign,":number",2),
        (try_end),
      (else_try),
        (eq, ":shooter_troop", "trp_woodelf_druid_1"),
        (store_random_in_range, ":r", 0, 10),
        (try_begin),
          (ge, ":r", 6),
          (assign, ":spawn_troop_id","trp_ent_2"),
          (assign,":number",1),
        (else_try),
          (ge, ":r", 4),
          (store_random_in_range, ":spawn_troop_id","trp_air_elemental","trp_air_elemental_2"),
          (assign,":number",2),
        (else_try),
          (assign, ":spawn_troop_id","trp_dryad"),
          (assign,":number",3),
        (try_end),
      (else_try),
        (eq, ":shooter_troop", "trp_human_magic_2"),
        (assign,":spawn_troop_id","trp_golem_1"),
        (assign,":number",2),
      (else_try),
        (eq, ":shooter_troop", "trp_human_magic_3"),
        (assign,":spawn_troop_id","trp_golem_3"),
        (assign,":number",2),
      (else_try),
        (eq, ":shooter_troop", "trp_human_magic_4"),
        (assign,":spawn_troop_id","trp_we_recruit"),
        (assign,":number",1),
      (try_end),
      
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_magic_book_5"),
        (store_random_in_range, ":r", 0, 4),
        (assign,":number",2),
        (try_begin),
          (ge, ":r", 1),
          (assign,":spawn_troop_id","trp_fire_elemental_3"),
        (else_try),
          (ge, ":r", 2),
          (assign,":spawn_troop_id","trp_earth_elemental_3"),
        (else_try),
          (ge, ":r", 3),
          (assign,":spawn_troop_id","trp_water_elemental_3"),
        (else_try),
          (assign,":spawn_troop_id","trp_air_elemental_3"),
          (assign,":number",3),
        (try_end),
      (try_end),
      
      (gt,":spawn_troop_id",0),
      (gt,":number",0),
        
        (copy_position, pos51, pos5),
        (call_script,"script_cf_agent_spawn_agent_to_pos51", ":shooter", ":spawn_troop_id", ":number"),
    ])]
    
cast_magic_summon_demon = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt,":weapon",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_necromancy, ":shooter_troop"),
      
      (assign, ":cost_stamina", 50),
      (try_begin),
        (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
        (ge, ":stamina", ":cost_stamina"),
        (val_sub, ":stamina", ":cost_stamina"),
        (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
      (else_try),
        (assign, ":power", 0),
      (try_end),
      
      (assign,":spawn_troop_id",0),
      (assign,":number",0),
      (store_character_level,":troop_level",":shooter_troop"),
      (val_mul,":power",5),
      (val_add,":power",":troop_level"),
      (try_begin),
        (ge, ":power", 60),
        (store_random_in_range, ":r", 0, 10),
        (assign,":number",1),
        (try_begin),
          (ge, ":r", 9),
          (assign,":spawn_troop_id","trp_demon_6"),
        (else_try),
          (ge, ":r", 6),
          (assign,":spawn_troop_id","trp_demon_8"),
        (else_try),
          (ge, ":r", 4),
          (assign,":spawn_troop_id","trp_demon_5"),
        (else_try),
          (assign,":spawn_troop_id","trp_demon_human_5_2"),
        (try_end),
      (else_try),
        (ge, ":power", 45),
        (store_random_in_range, ":r", 0, 10),
        (assign,":number",2),
        (try_begin),
          (ge, ":r", 8),
          (assign,":spawn_troop_id","trp_werewolf_1_a"),
        (else_try),
          (ge, ":r", 6),
          (assign,":spawn_troop_id","trp_demon_4_2"),
        (else_try),
          (ge, ":r", 4),
          (assign,":spawn_troop_id","trp_huge_inferno"),
        (else_try),
          (assign,":spawn_troop_id","trp_demon_4"),
        (try_end),
      (else_try),
        (ge, ":power", 30),
        (store_random_in_range, ":r", 0, 10),
        (assign,":number",2),
        (try_begin),
          (ge, ":r", 8),
          (assign,":spawn_troop_id","trp_demon_human_4"),
        (else_try),
          (ge, ":r", 6),
          (assign,":spawn_troop_id","trp_demon_4"),
        (else_try),
          (ge, ":r", 4),
          (assign,":spawn_troop_id","trp_demon_3"),
        (else_try),
          (assign,":spawn_troop_id","trp_inferno"),
        (try_end),
      (else_try),
        (store_random_in_range, ":r", 0, 10),
        (assign,":number",2),
        (try_begin),
          (ge, ":r", 7),
          (assign,":spawn_troop_id","trp_demon_2"),
        (else_try),
          (ge, ":r", 3),
          (assign,":spawn_troop_id","trp_demon_1_2"),
        (else_try),
          (assign,":spawn_troop_id","trp_demon_1"),
        (try_end),
      (try_end),
     
        (try_begin),
          (eq, ":weapon", "itm_pit_lord_sword"),
          (store_random_in_range, ":r", 0, 10),
          (assign,":number",2),
          (try_begin),
            (ge, ":r", 9),
            (assign,":spawn_troop_id","trp_demon_6"),
          (else_try),
            (ge, ":r", 6),
            (assign,":spawn_troop_id","trp_demon_8"),
          (else_try),
            (ge, ":r", 4),
            (assign,":spawn_troop_id","trp_demon_5"),
          (else_try),
            (assign,":spawn_troop_id","trp_demon_human_5_2"),
          (try_end),
        (else_try),
          (eq, ":weapon", "itm_balor_sword"),
          (store_random_in_range, ":r", 0, 10),
          (assign,":number",2),
          (try_begin),
            (ge, ":r", 8),
            (assign,":spawn_troop_id","trp_demon_4_2"),
          (else_try),
            (ge, ":r", 6),
            (assign,":spawn_troop_id","trp_werewolf_1_a"),
          (else_try),
            (ge, ":r", 4),
            (assign,":spawn_troop_id","trp_huge_inferno"),
          (else_try),
            (assign,":spawn_troop_id","trp_demon_4"),
          (try_end),
        (else_try),
          (eq, ":weapon", "itm_mark_chaos_1"),
          (store_random_in_range, ":r", 0, 10),
          (assign,":number",1),
          
          (try_begin),
            (ge, ":r", 8),
            (assign,":spawn_troop_id","trp_demon_4_2"),
          (else_try),
            (ge, ":r", 6),
            (assign,":spawn_troop_id","trp_werewolf_1_a"),
          (else_try),
            (ge, ":r", 4),
            (assign,":spawn_troop_id","trp_huge_inferno"),
          (else_try),
            (assign,":spawn_troop_id","trp_demon_4"),
          (try_end),
        (else_try),
          (eq, ":weapon", "itm_shaman_staff_1"),
          (assign,":spawn_troop_id","trp_fire_elemental"),
          (assign,":number",2),
        (else_try),
          (eq, ":weapon", "itm_sorcerer_staff_1"),
          (store_random_in_range, ":r", 0, 10),
          (try_begin),
            (ge, ":r", 8),
            (assign,":spawn_troop_id","trp_demon_4"),
            (assign,":number",1),
          (else_try),
            (ge, ":r", 6),
            (assign,":spawn_troop_id","trp_demon_3"),
            (assign,":number",1),
          (else_try),
            (ge, ":r", 3),
            (assign,":spawn_troop_id","trp_demon_1_2"),
            (assign,":number",2),
          (else_try),
            (assign,":spawn_troop_id","trp_demon_1"),
            (assign,":number",2),
          (try_end),
        (else_try),
          (eq, ":weapon", "itm_demon_staff_1"),
          (store_random_in_range, ":r", 0, 10),
          (try_begin),
            (eq, ":r", 9),
            (assign,":spawn_troop_id","trp_demon_4_2"),
            (assign,":number",1),
          (else_try),
            (eq, ":r", 8),
            (assign,":spawn_troop_id","trp_werewolf_1_a"),
            (assign,":number",1),
          (else_try),
            (ge, ":r", 6),
            (assign,":spawn_troop_id","trp_demon_4"),
            (assign,":number",1),
          (else_try),
            (ge, ":r", 4),
            (assign,":spawn_troop_id","trp_demon_3"),
            (assign,":number",2),
          (else_try),
            (ge, ":r", 2),
            (assign,":spawn_troop_id","trp_demon_2"),
            (assign,":number",2),
          (else_try),
            (assign,":spawn_troop_id","trp_demon_1_2"),
            (assign,":number",3),
          (try_end),
          
        (try_end),
        
        
      (gt,":spawn_troop_id",0),
      (gt,":number",0),
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_magic_book_7"),
        (gt,":spawn_troop_id",0),
        (val_add,":number",2),
      (try_end),
        (copy_position, pos51, pos5),
        (call_script,"script_cf_agent_spawn_agent_to_pos51", ":shooter", ":spawn_troop_id", ":number"),
    ])]
    
cast_magic_basic_curse = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),

      
        (try_for_agents,":possable_agent"),
          (agent_is_alive,":possable_agent"),
          (this_or_next|agent_is_ally,":shooter"),
          (agent_is_ally,":possable_agent"),
          (this_or_next|neg|agent_is_ally,":possable_agent"),
          (neg|agent_is_ally,":shooter"),

          (agent_get_position,pos3,":possable_agent"),
          (get_distance_between_positions,":dist",pos5,pos3),
          (le,":dist",200),
          (assign,":agent",":possable_agent"),

          #(agent_deliver_damage_to_agent,":shooter",":agent", ":damage"),
          (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", 20, curse, 1, 1),
        (try_end),
    ])]
   
    
cast_magic_curse = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt,":weapon",0),
      (assign,":damage",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
      
      (assign, ":cost_stamina", 10),
      (try_begin),
        (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
        (ge, ":stamina", ":cost_stamina"),
        (val_sub, ":stamina", ":cost_stamina"),
        (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
      (else_try),
        (assign, ":power", 0),
      (try_end),
      
      (try_begin),
        (eq, ":weapon", "itm_lich_staff_1"),
        (val_add,":power",1),
      (else_try),
        (eq, ":weapon", "itm_archlich_staff_1"),
        (val_add,":power",2),
      (try_end),
      
      (try_begin),
        (assign,":max_range",100),
        (assign,":damage",50),
        (store_mul,":range_add",":power", 20),
        (store_mul,":damage_add",":power", 50),
        (val_add,":max_range",":range_add"),
        (store_add,":max_damage",":damage",":damage_add"),
      (try_end),
      (copy_position,pos6,pos5),
      (position_move_z,pos6,200),
      (particle_system_burst, "psys_magic_curse_small", pos6, 3),
      
        (try_for_agents,":possable_agent"),
          (gt,":damage",0),
          (agent_is_alive,":possable_agent"),
          (this_or_next|agent_is_ally,":shooter"),
          (agent_is_ally,":possable_agent"),
          (this_or_next|neg|agent_is_ally,":possable_agent"),
          (neg|agent_is_ally,":shooter"),

          (agent_get_position,pos3,":possable_agent"),
          (get_distance_between_positions,":dist",pos5,pos3),
          (le,":dist",":max_range"),
          (assign,":agent",":possable_agent"),

          #(agent_deliver_damage_to_agent,":shooter",":agent", ":damage"),
          (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":max_damage", curse, ":power", 15),
          (agent_set_slot, ":agent", slot_agent_special_ability_affect_type, mummy_curse),
          (agent_set_slot, ":agent", slot_agent_special_ability_affect_time, 15),
          
          
          (assign,":max_damage",100),
        (try_end),
    ])]
   
cast_magic_soul_Leech = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (copy_position,pos51,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt,":weapon",0),
      
      (assign,":max_damage",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
           
      (assign, ":cost_stamina", 25),
      (try_begin),
        (agent_has_item_equipped,":shooter","itm_plague_staff_1"),
        (assign, ":cost_stamina", 5),
      (try_end),
      (try_begin),
        (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
        (ge, ":stamina", ":cost_stamina"),
        (val_sub, ":stamina", ":cost_stamina"),
        (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
      (else_try),
        (assign, ":power", 0),
      (try_end),
      (assign, ":num_hit", 1),
      (try_begin),
        (assign,":max_range",200),
        (assign,":damage",50),
        (assign,":heal",50),
        (store_mul,":range_add",":power", 40),
        (store_mul,":damage_add",":power", 30),
        (val_add,":max_range",":range_add"),
        (store_add,":max_damage",":damage",":damage_add"),
        (store_mul,":spec_power",":power", 3),
        (val_add,":heal",":damage_add"),
      (try_end),
        (try_begin),
          (agent_has_item_equipped,":shooter","itm_magic_book_8"),
          (val_add,":max_range",":range_add"),
        (try_end),
        (try_begin),
          (agent_has_item_equipped,":shooter","itm_magic_book_9"),
          (val_add,":max_range",":range_add"),
        (try_end),
      
        (particle_system_burst, "psys_death_cloud_blue", pos5, 10),
        (agent_play_sound,":shooter","snd_death_cld"),
        (store_div,":half_damage",":max_damage",2),
      (try_for_agents,":possable_agent"),
        (gt,":max_damage",0),
        (agent_is_alive,":possable_agent"),
        (this_or_next|agent_is_ally,":shooter"),
        (agent_is_ally,":possable_agent"),
        (this_or_next|neg|agent_is_ally,":possable_agent"),
        (neg|agent_is_ally,":shooter"),

        (agent_get_position,pos3,":possable_agent"),
        (get_distance_between_positions,":dist",pos5,pos3),
        (le,":dist",":max_range"),
        (assign,":agent",":possable_agent"),
        (store_random_in_range, ":damage", ":half_damage",":max_damage"),
        #(agent_deliver_damage_to_agent,":shooter",":agent", ":damage"),
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":damage", curse, ":spec_power", ":power"),
        (val_add, ":num_hit", 1),
        (try_begin),
          (agent_has_item_equipped,":shooter","itm_magic_book_9"),
          (store_agent_hit_points, ":inflicted_agent_hp", ":agent", 0),
          (store_mul,":dead_power",":power", 5),
          (ge, ":dead_power", ":inflicted_agent_hp"),
          (agent_set_hit_points,":agent",0,0),
          (agent_deliver_damage_to_agent, ":shooter", ":agent", 100),
        (try_end),
        (try_begin),
          (agent_has_item_equipped,":shooter","itm_magic_book_8"),
          (store_agent_hit_points, ":hp", ":agent"),
          (le, ":hp", 5),
          (store_random_in_range, ":r", 0, 2),
          (try_begin),
            (eq, ":r", 0),
            (store_random_in_range, ":spawn_troop_id", "trp_zombie_1", "trp_skeleton"),
          (else_try),
            (store_random_in_range, ":spawn_troop_id", "trp_draugr_1", "trp_mummy_2_1"),
          (try_end),
          (call_script,"script_cf_agent_spawn_agent_to_pos51", ":shooter", ":spawn_troop_id", 1),
        (try_end),
        
      (try_end),
        
      (store_agent_hit_points, ":hp", ":shooter"),
      (store_mul,":spec_power",":num_hit", 25),
      (val_add, ":hp", 50),
      (val_add, ":hp", ":spec_power"),
      (agent_set_hit_points, ":shooter", ":hp"),
        
      (agent_get_position,pos6,":shooter"),
      (try_for_agents,":possable_agent"),
          (gt,":num_hit",0),
          (agent_is_alive,":possable_agent"),

          (this_or_next|agent_is_ally,":shooter"),
          (neg|agent_is_ally,":possable_agent"),
          (this_or_next|agent_is_ally,":possable_agent"),
          (neg|agent_is_ally,":shooter"),


          (agent_get_position,pos3,":possable_agent"),
          (get_distance_between_positions,":dist",pos6,pos3),
          (le,":dist",":max_range"),
          (assign,":agent",":possable_agent"),
          (val_add, ":num_hit", -1),
          (store_agent_hit_points, ":hp", ":agent"),
          (val_add, ":hp", ":heal"),
          (agent_set_hit_points, ":agent", ":hp"),
          (position_move_z,pos3,100),
          (particle_system_burst, "psys_heal_effect", pos3, 30), 
      (try_end),
      
      
    ])]
    
   

cast_magic_Slow = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt,":weapon",0),
      (assign,":damage",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
      
      (assign, ":cost_stamina", 10),
      (try_begin),
        (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
        (ge, ":stamina", ":cost_stamina"),
        (val_sub, ":stamina", ":cost_stamina"),
        (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
      (else_try),
        (assign, ":power", 0),
      (try_end),
      
      (try_begin),
        (eq, ":weapon", "itm_lich_staff_1"),
        (val_add,":power",1),
      (else_try),
        (eq, ":weapon", "itm_archlich_staff_1"),
        (val_add,":power",2),
      (try_end),
      
      (try_begin),
        (assign,":max_range",100),
        (assign,":damage",50),
        (store_mul,":range_add",":power", 20),
        (store_mul,":damage_add",":power", 50),
        (val_add,":max_range",":range_add"),
        (store_add,":max_damage",":damage",":damage_add"),
      (try_end),
      (copy_position,pos6,pos5),
      (position_move_z,pos6,200),
      (particle_system_burst, "psys_magic_curse_small", pos6, 3),
      
        (try_for_agents,":possable_agent"),
          (gt,":damage",0),
          (agent_is_alive,":possable_agent"),
          (this_or_next|agent_is_ally,":shooter"),
          (agent_is_ally,":possable_agent"),
          (this_or_next|neg|agent_is_ally,":possable_agent"),
          (neg|agent_is_ally,":shooter"),

          (agent_get_position,pos3,":possable_agent"),
          (get_distance_between_positions,":dist",pos5,pos3),
          (le,":dist",":max_range"),
          (assign,":agent",":possable_agent"),

          #(agent_deliver_damage_to_agent,":shooter",":agent", ":damage"),
          (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":max_damage", curse, ":power", 15),
          (agent_set_slot, ":agent", slot_agent_special_ability_affect_type, slow),
          (agent_set_slot, ":agent", slot_agent_special_ability_affect_time, 15),
          (assign,":max_damage",100),
        (try_end),
    ])]
   

cast_magic_weakness = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt,":weapon",0),
      (assign,":damage",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
      
      (assign, ":cost_stamina", 25),
      (try_begin),
        (agent_get_slot, ":stamina", ":shooter", slot_agent_mana),
        (ge, ":stamina", ":cost_stamina"),
        (val_sub, ":stamina", ":cost_stamina"),
        (agent_set_slot, ":shooter", slot_agent_mana, ":stamina"),
      (else_try),
        (assign, ":power", 0),
      (try_end),
      
      (try_begin),
        (eq, ":weapon", "itm_lich_staff_1"),
        (val_add,":power",1),
      (else_try),
        (eq, ":weapon", "itm_archlich_staff_1"),
        (val_add,":power",2),
      (try_end),
      
      (try_begin),
        (assign,":max_range",100),
        (assign,":damage",50),
        (store_mul,":range_add",":power", 20),
        (store_mul,":damage_add",":power", 50),
        (val_add,":max_range",":range_add"),
        (store_add,":max_damage",":damage",":damage_add"),
      (try_end),
      (copy_position,pos6,pos5),
      (position_move_z,pos6,200),
      (particle_system_burst, "psys_magic_curse_small", pos6, 3),
      
        (try_for_agents,":possable_agent"),
          (gt,":damage",0),
          (agent_is_alive,":possable_agent"),
          (this_or_next|agent_is_ally,":shooter"),
          (agent_is_ally,":possable_agent"),
          (this_or_next|neg|agent_is_ally,":possable_agent"),
          (neg|agent_is_ally,":shooter"),

          (agent_get_position,pos3,":possable_agent"),
          (get_distance_between_positions,":dist",pos5,pos3),
          (le,":dist",":max_range"),
          (assign,":agent",":possable_agent"),

          #(agent_deliver_damage_to_agent,":shooter",":agent", ":damage"),
          (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":max_damage", curse, ":power", 15),
          (agent_set_slot, ":agent", slot_agent_special_ability_affect_type, weakness),
          (agent_set_slot, ":agent", slot_agent_special_ability_affect_time, 15),
          (assign,":max_damage",100),
        (try_end),
    ])]
   


cast_magic_heal = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (assign,":heal",0),
      (gt,":weapon",0),
      
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
            
      (try_begin),
        (assign,":max_range",100),
        (assign,":heal",50),
        (store_mul,":range_add",":power", 40),
        (store_mul,":damage_add",":power", 10),
        (val_add,":max_range",":range_add"),
        (val_add,":heal",":damage_add"),
      (try_end),
      
        (try_for_agents,":possable_agent"),
          (gt,":heal",0),
          (agent_is_alive,":possable_agent"),

          (this_or_next|agent_is_ally,":shooter"),
          (neg|agent_is_ally,":possable_agent"),
          (this_or_next|agent_is_ally,":possable_agent"),
          (neg|agent_is_ally,":shooter"),


          (agent_get_position,pos3,":possable_agent"),
          (get_distance_between_positions,":dist",pos5,pos3),
          (le,":dist",":max_range"),
          (assign,":agent",":possable_agent"),

          (store_agent_hit_points, ":hp", ":agent"),
          (val_add, ":hp", ":heal"),
          (agent_set_hit_points, ":agent", ":hp"),
          (position_move_z,pos3,100),
          (particle_system_burst, "psys_heal_effect", pos3, 30), 
        (try_end),
    ])]
   
magic_cast_trigger = [
  (ti_on_weapon_attack, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos51,pos1),
      (play_sound,"snd_spell_cast"),
      (call_script, "script_cf_magic_cast_trigger", ":shooter"),
    ])]

magic_bow_trigger = [
  (ti_on_weapon_attack, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos51,pos1),
      (call_script, "script_cf_magic_bow_trigger", ":shooter"),
    ])]

flame_cast_trigger = [
  (ti_on_weapon_attack, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos51,pos1),
      
      (assign,":cur_ammo_id","itm_cartridges"),#as default
      (assign,":item_slot_num",4),
      (try_for_range,":cur_item_slot",0,":item_slot_num"),
        (agent_get_item_slot, ":item_no", ":shooter", ":cur_item_slot"),
        (gt,":item_no",-1),
        (item_get_type, ":item_type", ":item_no"),
        (eq,":item_type",itp_type_bullets),
        (agent_get_item_cur_ammo, ":cur_ammo", ":shooter", ":cur_item_slot"),
        (gt,":cur_ammo",0),
        (assign,":cur_ammo_id",":item_no"),
        (assign,":item_slot_num",0),#break
      (try_end),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt, ":weapon", 0),
      (try_begin),
        (eq,":cur_ammo_id","itm_cartridges_thrust"),
        (call_script, "script_musket_damage_agent", ":shooter"), 
        (play_sound,"snd_release_musket"),
      (else_try),  
        (eq,":cur_ammo_id","itm_cartridges_burst"),
        (call_script, "script_musket_damage_agent_1151", ":shooter"), 
        (play_sound,"snd_release_musket"),
      (else_try),  
        (this_or_next|eq,":cur_ammo_id","itm_cartridges_sissofbattle_bolter_2"),
        (this_or_next|eq,":cur_ammo_id","itm_cartridges_sissofbattle_bolter"),
        (eq,":cur_ammo_id","itm_cartridges_sissofbattle_holy"),
        (play_sound,"snd_release_musket"),
      (else_try),  
        (this_or_next|eq,":cur_ammo_id","itm_cartridges_sissofbattle_flame_cannon"),
        (this_or_next|eq,":cur_ammo_id","itm_cartridges_sissofbattle_flame"),
        (this_or_next|eq,":cur_ammo_id","itm_gold_dragon_breath"),
        (this_or_next|eq,":cur_ammo_id","itm_red_dragon_breath"),
        (this_or_next|eq,":cur_ammo_id","itm_red_dragon_breath_2"),
        (this_or_next|eq,":cur_ammo_id","itm_fire_dragon_breath"),
        (this_or_next|eq,":cur_ammo_id","itm_lava_dragon_breath"),
        (eq,":cur_ammo_id","itm_cartridges_flame"),
        (play_sound,"snd_cannon_shot"),
        (call_script, "script_flame_cast_trigger", ":shooter", ":cur_ammo_id"),
      (try_end),  
    ])]


hand_cannon_trigger=  [
 (ti_on_weapon_attack,
  [
  
      (store_trigger_param_1, ":shooter"),
      (assign,":cur_ammo_id","itm_cartridges"),#as default
      (assign,":item_slot_num",4),
      (try_for_range,":cur_item_slot",0,":item_slot_num"),
        (agent_get_item_slot, ":item_no", ":shooter", ":cur_item_slot"),
        (gt,":item_no",-1),
        (item_get_type, ":item_type", ":item_no"),
        (eq,":item_type",itp_type_bullets),
        (agent_get_item_cur_ammo, ":cur_ammo", ":shooter", ":cur_item_slot"),
        (gt,":cur_ammo",0),
        (assign,":cur_ammo_id",":item_no"),
        (assign,":item_slot_num",0),#break
      (try_end),
      (call_script, "script_musket_damage_agent", ":shooter"), 
      (try_begin),
        (eq,":cur_ammo_id","itm_cartridges_thrust"),
        (call_script, "script_thrust_damage_agent", ":shooter"), 
      (else_try),  
        (eq,":cur_ammo_id","itm_cartridges_burst"),
        (call_script, "script_musket_damage_agent_1151", ":shooter"), 
      (try_end),  
      (play_sound,"snd_cannon_shot"),
            
      (try_begin),
        (eq, "$g_weapon_fire_particle", 0),
        (position_move_x,pos1,0),
        (position_move_y,pos1,130),
        (particle_system_burst_no_sync,"psys_musket_smoke",pos1,4),
        (particle_system_burst_no_sync,"psys_musket_ogon",pos1,20),
        (particle_system_burst_no_sync,"psys_cannon_fire",pos1,24),   

        (position_move_x, pos1, -4),
        (position_move_y, pos1,-120),
        (position_move_z, pos1,3),
        (particle_system_burst_no_sync, "psys_musket_powder_a", pos1, 4),
        (particle_system_burst_no_sync, "psys_pistol_powder_b", pos1, 7),
      (else_try),  
        (position_move_x,pos1,0),
        (position_move_y,pos1,130),
        (particle_system_burst_no_sync,"psys_musket_smoke",pos1,1),
        (particle_system_burst_no_sync,"psys_musket_ogon",pos1,20),
        (particle_system_burst_no_sync,"psys_cannon_fire",pos1,24),   
      (try_end),  
 ])]    
      
bullet_dust_trigger = [
  (ti_on_missile_hit, 
    [
    (try_begin),
      (eq, "$g_weapon_fire_particle", 0),
      (particle_system_burst_no_sync, "psys_musket_hit", pos1, 10),
      (particle_system_burst_no_sync, "psys_musket_hit_particle", pos1, 10),
    (else_try),  
      (particle_system_burst_no_sync, "psys_musket_hit", pos1, 5),
      (particle_system_burst_no_sync, "psys_musket_hit_particle", pos1, 5),
    (try_end),  
    ])]
        
laser_trigger = [
  (ti_on_weapon_attack, 
    [
      (store_trigger_param_1, ":shooter"),
      (eq,":shooter",":shooter"), # fix compiler bug warning.
      (assign,":cur_ammo_id","itm_laser_bolt_red"),#as default
      (assign,":item_slot_num",4),
      (try_for_range,":cur_item_slot",0,":item_slot_num"),
        (agent_get_item_slot, ":item_no", ":shooter", ":cur_item_slot"),
        (gt,":item_no",-1),
        (item_get_type, ":item_type", ":item_no"),
        (eq,":item_type",itp_type_bullets),
        (assign,":cur_ammo_id",":item_no"),
        (assign,":item_slot_num",0),#break
      (try_end),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt, ":weapon", 0),
  
      (assign,":cur_weapon_slot",-1),
      (assign,":item_slot_num",4),
      (try_for_range,":cur_item_slot",0,":item_slot_num"),
        (eq,":cur_weapon_slot",-1),
        (agent_get_item_slot, ":item_no", ":shooter", ":cur_item_slot"),
        (eq,":item_no",":weapon"),
        (assign,":cur_weapon_slot",":cur_item_slot"),
        (assign,":item_slot_num", 0),
      (try_end),
    
      (agent_get_horse,":horse",":shooter"),
      (agent_get_look_position,pos3,":shooter"),
      (agent_get_position,pos4,":shooter"),
      (position_copy_rotation,pos4,pos3),
      (try_begin), 
        (gt, ":horse", -1),
        (position_move_z,pos4,270),
      (else_try),
        (neg|gt, ":horse", -1),
        (position_move_z,pos4,170),
      (try_end),
      (position_move_y,pos4,110),
        
      (copy_position,pos22,pos4),
      (try_for_range,":unused",0,2), #2 extra bullets + 1 original = 3 bullets in one shot :D
#      (try_for_range,":unused",0,0), #2 extra bullets + 1 original = 3 bullets in one shot :D
        (this_or_next|eq,":cur_ammo_id","itm_laser_bolt_blue"),
        (eq,":cur_ammo_id","itm_laser_bolt_red"),
  
        (copy_position,pos23,pos22),
        (store_random_in_range,":x_change",-300,301),
        (store_random_in_range,":z_change",-300,301),
        (position_move_x, pos23, ":x_change"),
        (position_move_z, pos23, ":z_change"),
        (store_random_in_range,":x_change",-30,31),
        (store_random_in_range,":z_change",-30,31),
        (position_rotate_z,pos23,":x_change"),
        (position_rotate_x,pos23,":z_change"),
        
        (set_fixed_point_multiplier,100),
        (add_missile, ":shooter", pos23, ":bullet_speed", ":weapon", 0, ":cur_ammo_id", 0),
        (play_sound,"snd_release_laser"),
      (try_end),            
      (play_sound,"snd_release_laser"),
      
    ])]
        
musket_trigger = [
  (ti_on_weapon_attack, 
    [
      (store_trigger_param_1, ":shooter"),
      (assign,":cur_ammo_id","itm_cartridges"),#as default
      (assign,":item_slot_num",4),
      (try_for_range,":cur_item_slot",0,":item_slot_num"),
        (agent_get_item_slot, ":item_no", ":shooter", ":cur_item_slot"),
        (gt,":item_no",-1),
        (item_get_type, ":item_type", ":item_no"),
        (eq,":item_type",itp_type_bullets),
        (agent_get_item_cur_ammo, ":cur_ammo", ":shooter", ":cur_item_slot"),
        (gt,":cur_ammo",0),
        (assign,":cur_ammo_id",":item_no"),
        (assign,":item_slot_num",0),#break
      (try_end),
            
      (try_begin),
        (eq,":cur_ammo_id","itm_cartridges_thrust"),
        (call_script, "script_thrust_damage_agent", ":shooter"), 
      (else_try),  
        (eq,":cur_ammo_id","itm_cartridges_burst"),
        (call_script, "script_musket_damage_agent_1151", ":shooter"), 
      (try_end),  
      (play_sound,"snd_release_musket"),
      
      (try_begin),
        (eq, "$g_weapon_fire_particle", 0),
        (position_move_x,pos1,0),
        (position_move_y,pos1,130),
        (particle_system_burst_no_sync,"psys_musket_smoke",pos1,4),
        (particle_system_burst_no_sync,"psys_musket_ogon",pos1,7),
        (particle_system_burst_no_sync,"psys_musket_svet",pos1,7),

        (position_move_x, pos1, -4),
        (position_move_y, pos1,-120),
        (position_move_z, pos1,3),
        (particle_system_burst_no_sync, "psys_musket_powder_a", pos1, 4),
        (particle_system_burst_no_sync, "psys_pistol_powder_b", pos1, 7),
      (else_try),  
        (position_move_x,pos1,0),
        (position_move_y,pos1,130),
        (particle_system_burst_no_sync,"psys_musket_smoke",pos1,1),
        (particle_system_burst_no_sync,"psys_musket_ogon",pos1,7),
        (particle_system_burst_no_sync,"psys_musket_svet",pos1,7),
      (try_end),  
    ])]

pistol_trigger = [
  (ti_on_weapon_attack, 
    [
      (store_trigger_param_1, ":shooter"),
      (assign,":cur_ammo_id","itm_cartridges"),#as default
      (assign,":item_slot_num",4),
      (try_for_range,":cur_item_slot",0,":item_slot_num"),
        (agent_get_item_slot, ":item_no", ":shooter", ":cur_item_slot"),
        (gt,":item_no",-1),
        (item_get_type, ":item_type", ":item_no"),
        (eq,":item_type",itp_type_bullets),
        (agent_get_item_cur_ammo, ":cur_ammo", ":shooter", ":cur_item_slot"),
        (gt,":cur_ammo",0),
        (assign,":cur_ammo_id",":item_no"),
        (assign,":item_slot_num",0),#break
      (try_end),
      
      (try_begin),
        (agent_get_wielded_item, ":weapon", ":shooter", 0),
        (eq,":weapon","itm_zlmg"),
        (agent_get_horse,":horse",":shooter"),
        (agent_get_look_position,pos3,":shooter"),
        (agent_get_position,pos4,":shooter"),
        (position_copy_rotation,pos4,pos3),
        (try_begin), 
          (gt, ":horse", -1),
          (position_move_z,pos4,270),
        (else_try),
          (neg|gt, ":horse", -1),
          (position_move_z,pos4,170),
        (try_end),
        (position_move_y,pos4,110),
        (set_fixed_point_multiplier, 100),
        (store_random_in_range,":bullet_speed",5000,10000),
        (add_missile, ":shooter", pos4, ":bullet_speed", ":weapon", 0, ":cur_ammo_id", 0),
        
      (try_end),  
      
      (try_begin),
        (eq,":cur_ammo_id","itm_cartridges_thrust"),
        (call_script, "script_thrust_damage_agent", ":shooter"), 
      (else_try),  
        (eq,":cur_ammo_id","itm_cartridges_burst"),
        (call_script, "script_musket_damage_agent_1151", ":shooter"), 
      (try_end),  
      (play_sound,"snd_release_musket_medium"),
      
      (try_begin),
        (eq, "$g_weapon_fire_particle", 0),
        (position_move_x,pos1,27),
        (position_move_y,pos1,36),
        (particle_system_burst_no_sync,"psys_pistol_smoke",pos1,4),
        (particle_system_burst_no_sync,"psys_pistol_ogon",pos1,4),
        (particle_system_burst_no_sync,"psys_pistol_svet",pos1,4),   

        (position_move_x, pos1,-30),
        (position_move_y, pos1,-30),
        (position_move_z, pos1,3),
        (particle_system_burst_no_sync, "psys_musket_powder_a", pos1, 4),
        (particle_system_burst_no_sync, "psys_pistol_powder_b", pos1, 7),
      (else_try),  
        (position_move_x,pos1,27),
        (position_move_y,pos1,36),
        (particle_system_burst_no_sync,"psys_pistol_smoke",pos1,1),
        (particle_system_burst_no_sync,"psys_pistol_ogon",pos1,4),
        (particle_system_burst_no_sync,"psys_pistol_svet",pos1,4),   
      (try_end),  
    ])]

missile_weak_poison_trigger = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt,":weapon",0),
      #(item_has_property, ":weapon", itp_is_magic_staff),
      #(agent_get_troop_id, ":shooter_troop", ":shooter"),
      #(store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
      (assign,":max_damage",150),
      (assign,":damage",50),
      (try_begin),
         (eq, "$g_weapon_fire_particle", 0),
         (particle_system_burst,"psys_poison_smoke_small",pos5,10),
        (particle_system_burst, "psys_poison_cloud", pos5, 35),
      (else_try),  
         (particle_system_burst,"psys_poison_smoke_small",pos5,1),
        (particle_system_burst, "psys_poison_cloud", pos5, 3),
      (try_end),
      
      (try_for_agents,":possable_agent"),
        (gt,":damage",0),
        (agent_is_alive,":possable_agent"),
        (this_or_next|agent_is_ally,":shooter"),
        (agent_is_ally,":possable_agent"),
        (this_or_next|neg|agent_is_ally,":possable_agent"),
        (neg|agent_is_ally,":shooter"),

        (agent_get_position,pos3,":possable_agent"),
        (get_distance_between_positions,":dist",pos5,pos3),
        (le,":dist",150),
        (assign,":agent",":possable_agent"),
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":max_damage", poison, 5, 15),
        (assign,":max_damage",":damage"),
        
      (try_end),
      
    ])]



missile_poison_trigger = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (assign,":damage",0),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt,":weapon",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
      (val_add,":power",1),
      (try_begin),
        (assign,":max_range",100),
        (assign,":damage",100),
        (store_mul,":range_add",":power", 10),
        (store_mul,":damage_add",":power", 50),
        (val_add,":max_range",":range_add"),
        (store_add,":max_damage",":damage",":damage_add"),
        (store_mul,":spec_power",":power", 3),
      (try_end),

      (try_begin),
        (gt,":damage",0),
        (eq, "$g_weapon_fire_particle", 0),
        (particle_system_burst,"psys_poison_smoke_small",pos5,10),
        (particle_system_burst, "psys_poison_cloud", pos5, 35),
      (else_try),  
        (gt,":damage",0),
        (particle_system_burst,"psys_poison_smoke_small",pos5,1),
        (particle_system_burst, "psys_poison_cloud", pos5, 3),
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
        (get_distance_between_positions,":dist",pos5,pos3),
        (le,":dist",":max_range"),
        (assign,":agent",":possable_agent"),

        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":max_damage", poison, ":spec_power", 15),
        (assign,":max_damage",":damage"),
        
      (try_end),
      
    ])]

missile_power_poison_trigger = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (assign,":damage",0),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (gt,":weapon",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
      (val_add,":power",1),
      (try_begin),
        (assign,":max_range",200),
        (assign,":damage",100),
        (store_mul,":range_add",":power", 40),
        (store_mul,":damage_add",":power", 50),
        (val_add,":max_range",":range_add"),
        (store_add,":max_damage",":damage",":damage_add"),
        (store_mul,":spec_power",":power", 3),
      (try_end),

      (try_begin),
        (gt,":damage",0),
        (eq, "$g_weapon_fire_particle", 0),
        (particle_system_burst,"psys_poison_smoke_small",pos5,10),
        (particle_system_burst, "psys_death_cloud", pos5, 35),
      (else_try),  
        (gt,":damage",0),
        (particle_system_burst,"psys_poison_smoke_small",pos5,1),
        (particle_system_burst, "psys_death_cloud", pos5, 3),
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
        (get_distance_between_positions,":dist",pos5,pos3),
        (le,":dist",":max_range"),
        (assign,":agent",":possable_agent"),

        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":max_damage", power_poison, ":power", ":spec_power"),
        (assign,":max_damage",":damage"),
        
      (try_end),
      
    ])]


nahptha_fire_trigger = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),

      (get_player_agent_no, ":player_agent"),

      #(agent_get_wielded_item, ":weapon", ":shooter", 0),
      (try_begin),
         (eq, "$g_weapon_fire_particle", 0),
         (particle_system_burst,"psys_arrows_fire_big",pos5,100),
         (particle_system_burst,"psys_arrows_fire_smoke_big",pos5,50),
      (else_try),  
         (particle_system_burst,"psys_arrows_fire_big",pos5,10),
         (particle_system_burst,"psys_arrows_fire_smoke_big",pos5,5),
      (try_end),
      
      (try_for_agents,":possable_agent"),
         (agent_is_alive,":possable_agent"),
         (this_or_next|eq,":shooter",":player_agent"),
         (this_or_next|agent_is_ally,":shooter"),
         (agent_is_ally,":possable_agent"),
         (this_or_next|eq,":shooter",":player_agent"),
         (this_or_next|neg|agent_is_ally,":possable_agent"),
         (neg|agent_is_ally,":shooter"),			      

         (agent_get_position,pos3,":possable_agent"),
         (get_distance_between_positions,":dist",pos5,pos3),
         (neg|position_is_behind_position,pos5,pos3),
         (le,":dist",500),
         (assign,":agent",":possable_agent"),
         #(store_random_in_range, ":thrust_damage", 25, 50),  

         (store_random_in_range, ":damage", 50, 150),  
         #(agent_deliver_damage_to_agent,":shooter",":agent", ":thrust_damage"),
         (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":damage", severe_burn, 5, 15),

         #(agent_deliver_damage_to_agent,":shooter",":agent", ":thrust_damage"),
         #(store_agent_hit_points, ":hp", ":agent", 1),
         #(val_sub, ":hp", ":thrust_damage"),
         #(val_max, ":hp", 0),
         #(agent_set_hit_points,":agent",":hp",1),
         #(try_begin),
           #(agent_get_wielded_item, ":weapon", ":shooter", 0),
           #(this_or_next|eq,":weapon","itm_nahptha_bomb"),
           #(this_or_next|eq,":weapon","itm_elven_bow"),
           #(le, ":hp", 1),
           #(agent_deliver_damage_to_agent,":shooter",":agent"),
         #(try_end),  
         #(agent_set_slot, ":agent", slot_agent_special_damage_type, severe_burn),
         #(agent_set_slot, ":agent", slot_agent_special_damage_time, 15),

         #(try_begin),
         #  (this_or_next|eq,":weapon","itm_nahptha_bomb"),
         #  (eq,":weapon","itm_elven_bow"),
         #  (agent_set_slot, ":agent", slot_agent_special_damage_type, severe_burn),
         #(try_end),  

         (try_begin),
           (neg|agent_is_human,":agent"),
           (agent_set_animation,":agent","anim_horse_rear"), 
           (agent_play_sound,":agent","snd_metal_hit_high_armor_high_damage"),
           (agent_deliver_damage_to_agent,":shooter",":agent"),
         (try_end),
        
         #(try_begin),
         #  (lt, ":hp", 1),
         #  (agent_deliver_damage_to_agent,":shooter",":agent"),
         #(try_end),  
      (try_end),
    ])]
      

missile_force_trigger = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (assign,":damage",0),
      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
      
      (try_begin),
        (assign,":max_range",200),
        (assign,":damage",50),
        (store_div,":range_add",":power", 50),
        (store_mul,":damage_add",":power", 20),
        (val_add,":max_range",":range_add"),
        (store_add,":max_damage",":damage",":damage_add"),
      (try_end),
     
     (try_begin),
        (gt,":max_damage",0),
        (particle_system_burst, "psys_bomb_dust", pos5, 15),
     (try_end),
     
      (try_for_agents,":possable_agent"),
        (gt,":max_damage",0),
        (agent_is_alive,":possable_agent"),
        (this_or_next|agent_is_ally,":shooter"),
        (agent_is_ally,":possable_agent"),
        (this_or_next|neg|agent_is_ally,":possable_agent"),
        (neg|agent_is_ally,":shooter"),

        (agent_get_position,pos3,":possable_agent"),
        (get_distance_between_positions,":dist",pos5,pos3),
        (le,":dist",":max_range"),
        (assign,":agent",":possable_agent"),

        (agent_is_alive,":agent"), 
        (try_begin),
          (agent_is_human,":agent"), 
          (agent_set_animation, ":agent", "anim_explove_fly"),
          (agent_get_position, pos30, ":agent"),
          (position_move_z, pos30, 200),
          (particle_system_burst, "psys_stun_effect", pos30, 1),
        (else_try),
          (agent_set_animation, ":agent", "anim_horse_rear"),
        (try_end),

        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":max_damage", 0, 0, 0),
      (try_end),
     
    ])]



missile_freezing_trigger = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      
      (assign,":damage",0),
      (item_has_property, ":weapon", itp_is_magic_staff),

      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
                    
      (try_begin),
        (assign,":max_range",200),
        (assign,":damage",50),
        (store_random_in_range, ":randon_damage", 25, 76),
        (store_mul,":range_add",":power", 40),
        (store_mul,":damage_add",":power", ":randon_damage"),
        (val_add,":max_range",":range_add"),
        (store_add,":max_damage",":damage",":damage_add"),
      (try_end),
            
      (try_begin),
        (eq, "$g_weapon_fire_particle", 0),
        (gt,":damage",0),
        (particle_system_burst, "psys_Ice_Storm", pos5, 50),
      (else_try),  
        (gt,":damage",0),
        (particle_system_burst, "psys_Ice_Storm", pos5, 5),
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
        (get_distance_between_positions,":dist",pos5,pos3),
        (le,":dist",":max_range"),
        (assign,":agent",":possable_agent"),
        
        (val_add,":power",-1),
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":max_damage", freeze, ":power", ":power"),
        (assign,":max_damage",":damage_add"),
      (try_end),
    ]),
    
    (ti_on_init_item, 
      [
        (set_position_delta, 0, 100, 0),
        (particle_system_add_new, "psys_torch_snow"),
        (particle_system_add_new, "psys_torch_snow_smoke"),
      ]),
    
]





missile_ice_trigger = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      #(agent_get_wielded_item, ":weapon", ":shooter", 0),
      (try_begin),
         (eq, "$g_weapon_fire_particle", 0),
         (particle_system_burst,"psys_Freezing_Trail",pos5,30),
      (else_try),  
         (particle_system_burst,"psys_Freezing_Trail",pos5,5),
      (try_end),
      
      (try_for_agents,":possable_agent"),
         (agent_is_alive,":possable_agent"),
           (this_or_next|agent_is_ally,":shooter"),
           (agent_is_ally,":possable_agent"),
           (this_or_next|neg|agent_is_ally,":possable_agent"),
           (neg|agent_is_ally,":shooter"),			  
           (neg|eq,":shooter",":possable_agent"),
         (agent_get_position,pos3,":possable_agent"),
         (get_distance_between_positions,":dist",pos5,pos3),
         (neg|position_is_behind_position,pos5,pos3),
         (le,":dist",200),
         (assign,":agent",":possable_agent"),
         (store_random_in_range, ":thrust_damage", 30, 50),  
         (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":thrust_damage", ice, 5, 15),
         
         (try_begin),
           (neg|agent_is_human,":agent"),
           (agent_set_animation,":agent","anim_horse_rear"), 
           (agent_play_sound,":agent","snd_metal_hit_high_armor_high_damage"),
           (agent_deliver_damage_to_agent,":shooter",":agent"),
         (try_end),
        
      (try_end),
    ]),
    
    (ti_on_init_item, 
      [
        (set_position_delta, 0, 100, 0),
        (particle_system_add_new, "psys_torch_snow"),
        (particle_system_add_new, "psys_torch_snow_smoke"),
      ]),
]


missile_fire_trigger = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      #(agent_get_wielded_item, ":weapon", ":shooter", 0),
      (try_begin),
         (eq, "$g_weapon_fire_particle", 0),
         (particle_system_burst,"psys_arrows_fire_small",pos5,50),
         (particle_system_burst,"psys_arrows_fire_smoke_small",pos5,50),
      (else_try),  
         (particle_system_burst,"psys_arrows_fire_small",pos5,5),
         (particle_system_burst,"psys_arrows_fire_smoke_small",pos5,5),
      (try_end),
      
      (try_for_agents,":possable_agent"),
         (agent_is_alive,":possable_agent"),
           (this_or_next|agent_is_ally,":shooter"),
           (agent_is_ally,":possable_agent"),
           (this_or_next|neg|agent_is_ally,":possable_agent"),
           (neg|agent_is_ally,":shooter"),			  
           (neg|eq,":shooter",":possable_agent"),
         (agent_get_position,pos3,":possable_agent"),
         (get_distance_between_positions,":dist",pos5,pos3),
         (neg|position_is_behind_position,pos5,pos3),
         (le,":dist",150),
         (assign,":agent",":possable_agent"),
         #(store_random_in_range, ":thrust_damage", 5, 10),  
         (store_random_in_range, ":thrust_damage", 30, 50),  
         (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":thrust_damage", burn, 3, 15),
         
         (try_begin),
           (neg|agent_is_human,":agent"),
           (agent_set_animation,":agent","anim_horse_rear"), 
           (agent_play_sound,":agent","snd_metal_hit_high_armor_high_damage"),
           (agent_deliver_damage_to_agent,":shooter",":agent"),
         (try_end),
        
      (try_end),
    ]),
    
    (ti_on_init_item, 
      [
        (set_position_delta, 0, 100, 0),
        (particle_system_add_new, "psys_torch_fire"),
        (particle_system_add_new, "psys_torch_smoke"),
        (set_current_color, 150, 130, 70),
        (add_point_light, 10, 30),
      ]),
]

missile_fire_2_trigger = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (assign,":damage",0),

      (item_has_property, ":weapon", itp_is_magic_staff),
      (agent_get_troop_id, ":shooter_troop", ":shooter"),
      (store_skill_level, ":power", skl_magic_power, ":shooter_troop"),
      
      
      (try_begin),
        (assign,":max_range",300),
        (assign,":damage",200),
        (store_random_in_range, ":randon_damage", 50, 75),
        (store_mul,":range_add",":power", 60),
        (store_mul,":damage_add",":power", ":randon_damage"),
        (val_add,":max_range",":range_add"),
        (store_add,":max_damage",":damage",":damage_add"),
        (store_mul,":spec_power",":power", 2),
      (try_end),
       
      (copy_position,pos6,pos5),
      (position_move_z,pos6,150),
      (try_begin),
        (eq, "$g_weapon_fire_particle", 0),
        (gt,":damage",0),
        (gt,":power",0),
        (particle_system_burst, "psys_flame_explosion",pos5,50),
        (particle_system_burst, "psys_explosive_explosion_sparks_a", pos5, 35),
        (particle_system_burst, "psys_explosive_explosion_sparks_b", pos5, 35),
      (else_try),  
        (gt,":damage",0),
        (gt,":power",0),
        (particle_system_burst, "psys_flame_explosion",pos5,5),
        (particle_system_burst, "psys_explosive_explosion_sparks_a", pos5, 5),
        (particle_system_burst, "psys_explosive_explosion_sparks_b", pos5, 5),
      (try_end),
      (try_for_agents,":possable_agent"),
        (gt,":damage",0),
        (agent_is_alive,":possable_agent"),
        (this_or_next|agent_is_ally,":shooter"),
        (agent_is_ally,":possable_agent"),
        (this_or_next|neg|agent_is_ally,":possable_agent"),
        (neg|agent_is_ally,":shooter"),

        (agent_get_position,pos3,":possable_agent"),
        (get_distance_between_positions,":dist",pos5,pos3),
        (le,":dist",":max_range"),
        (assign,":agent",":possable_agent"),
        (val_add,":power",-1),
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":max_damage", burn, ":spec_power", ":power"),
        #(call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":damage", ice, 1, 15),
      (try_end),
    ]),
    
    (ti_on_init_item, 
      [
        (set_position_delta, 0, 100, 0),
        (particle_system_add_new, "psys_torch_fire"),
        (particle_system_add_new, "psys_torch_smoke"),
        (set_current_color, 150, 130, 70),
        (add_point_light, 10, 30),
      ]),
    ]



missile_holy_fire_trigger = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      #(agent_get_wielded_item, ":weapon", ":shooter", 0),
      #(agent_get_troop_id, ":shooter_troop", ":shooter"),
      #(store_skill_level, ":power", "skl_magic_power", ":shooter_troop"),
      #(ge,":power",1),
      (try_begin),
         (eq, "$g_weapon_fire_particle", 0),
         (particle_system_burst,"psys_holy_fire",pos5,50),
         #(particle_system_burst,"psys_arrows_fire_smoke_small",pos5,50),
      (else_try),  
         (particle_system_burst,"psys_holy_fire",pos5,5),
      (try_end),
      
      (try_for_agents,":possable_agent"),
         (agent_is_alive,":possable_agent"),
         (agent_get_position,pos3,":possable_agent"),
         (get_distance_between_positions,":dist",pos5,pos3),
         (neg|position_is_behind_position,pos5,pos3),
         (le,":dist",150),
         (assign,":agent",":possable_agent"),
         #(store_random_in_range, ":thrust_damage", 5, 10),  
         (store_random_in_range, ":thrust_damage", 30, 50),  
         
         (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":thrust_damage", holy_fire, 5, 15),

         (try_begin),
           (neg|agent_is_human,":agent"),
           (agent_set_animation,":agent","anim_horse_rear"), 
           (agent_play_sound,":agent","snd_metal_hit_high_armor_high_damage"),
           (agent_deliver_damage_to_agent,":shooter",":agent"),
         (try_end),
        
      (try_end),
    ]),
]
  
missile_holy_fire_trigger_1 = [
    (ti_on_init_item, 
      [
        (set_position_delta, 0, 100, 0),
        (particle_system_add_new, "psys_torch_holy"),
        (set_current_color, 150, 130, 70),
        (add_point_light, 10, 30),
      ]),
]
 
missile_holy_fire_trigger_2 = [
    (ti_on_init_item, 
      [
        (set_position_delta, 0, -100, 0),
        (particle_system_add_new, "psys_torch_holy"),
        (set_current_color, 150, 130, 70),
        (add_point_light, 10, 30),
      ]),
]
  
## CC
# Replace winged mace/spiked mace with: Flanged mace / Knobbed mace?
# Fauchard (majowski glaive) 
items = [
# item_name, mesh_name, item_properties, item_capabilities, slot_no, cost, bonus_flags, weapon_flags, scale, view_dir, pos_offset
["no_item","INVALID ITEM", [("invalid_item",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],

["tutorial_spear", "Spear", [("spear",0)], itp_type_polearm| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear, 0 , weight(4.5)|difficulty(0)|spd_rtng(80)| weapon_length(158)|swing_damage(0 , cut)| thrust_damage(19 ,  pierce),imodbits_polearm ],
["tutorial_club", "Club", [("club",0)], itp_type_one_handed_wpn| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 0 , weight(2.5)|difficulty(0)|spd_rtng(95)| weapon_length(95)|swing_damage(11 , blunt)| thrust_damage(0 ,  pierce),imodbits_none ],
["tutorial_battle_axe", "Battle Axe", [("battle_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(5)|difficulty(0)|spd_rtng(88)| weapon_length(108)|swing_damage(27 , cut)| thrust_damage(0 ,  pierce),imodbits_axe ],
["tutorial_arrows","Arrows", [("arrow",0),("flying_arrow",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(3)|abundance(160)|weapon_length(95)|thrust_damage(5,pierce)|max_ammo(20),imodbits_missile,missile_distance_trigger],
["tutorial_bolts","Bolts", [("toumingtou",0),("van_helsing_crossbow_bolt_copy",ixmesh_flying_ammo),("van_helsing_crossbow_bolt_bag", ixmesh_carry),("van_helsing_crossbow_bolt_bag", ixmesh_carry|imodbit_large_bag)], itp_type_bolts|itp_can_penetrate_shield|itp_bonus_against_shield|itp_is_magic_staff, itcf_carry_quiver_right_vertical, 5000,weight(2.25)|abundance(35)|weapon_length(55)|thrust_damage(40,pierce)|max_ammo(30),imodbits_missile,missile_poison_trigger+missile_distance_trigger],
["tutorial_short_bow", "Short Bow", [("short_bow",0),("short_bow_carry",ixmesh_carry)], itp_type_bow|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 0 , weight(1)|difficulty(0)|spd_rtng(98)| shoot_speed(49)| thrust_damage(12 ,  pierce  ),imodbits_bow ],
["tutorial_crossbow", "Crossbow", [("crossbow",0)], itp_type_crossbow|itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0 , weight(3)|difficulty(0)|spd_rtng(42)|  shoot_speed(68)| thrust_damage(39,pierce)|max_ammo(1),imodbits_crossbow ],
["tutorial_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown|itp_primary ,itcf_throw_knife, 0 , weight(3.5)|difficulty(0)|spd_rtng(102)| shoot_speed(25)| thrust_damage(16 ,  cut)|max_ammo(14)|weapon_length(0),imodbits_missile,missile_distance_trigger],
["tutorial_saddle_horse", "Saddle Horse", [("saddle_horse",0)], itp_type_horse, 0, 0,abundance(90)|body_armor(3)|difficulty(0)|horse_speed(40)|horse_maneuver(38)|horse_charge(8),imodbits_horse_basic],
["tutorial_shield", "Kite Shield", [("shield_kite_a",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|shield_hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(150),imodbits_shield ],
["tutorial_staff_no_attack","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_parry_polearm|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120)| weapon_length(115)|swing_damage(0,blunt)| thrust_damage(0,blunt),imodbits_none],
["tutorial_staff","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_long_glaive|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120)| weapon_length(115)|swing_damage(16,blunt)| thrust_damage(16,blunt),imodbits_none],
["tutorial_sword", "Sword", [("long_sword",0),("scab_longsw_a",ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 0, weight(1.5)|difficulty(0)|spd_rtng(100)|weapon_length(102)|swing_damage(18,cut)|thrust_damage(15,pierce), imodbits_sword,],
["tutorial_axe", "Axe", [("iron_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(4)|difficulty(0)|spd_rtng(91)| weapon_length(108)|swing_damage(19 , cut)| thrust_damage(0 ,  pierce),imodbits_axe ],

["tutorial_dagger","Dagger", [("practice_dagger",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(40)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],


["horse_meat","Horse Meat", [("raw_meat",0)], itp_type_goods|itp_consumable|itp_food, 0, 12,weight(40)|food_quality(30)|max_ammo(40),imodbits_none],
# Items before this point are hardwired and their order should not be changed!
["practice_sword","Practice Sword", [("practice_sword",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_wooden_parry|itp_wooden_attack, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(22,blunt)|thrust_damage(20,blunt),imodbits_none],
["heavy_practice_sword","Heavy Practice Sword", [("heavy_practicesword",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_greatsword,    21, weight(6.25)|spd_rtng(94)|weapon_length(128)|swing_damage(30,blunt)|thrust_damage(24,blunt),imodbits_none],
["practice_dagger","Practice Dagger", [("practice_dagger",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry|itp_wooden_attack, itc_dagger|itcf_carry_dagger_front_left, 2,weight(0.5)|spd_rtng(110)|weapon_length(47)|swing_damage(16,blunt)|thrust_damage(14,blunt),imodbits_none],
["practice_axe", "Practice Axe", [("hatchet",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 24 , weight(2)| spd_rtng(95)| weapon_length(75)| swing_damage(24, blunt)| thrust_damage(0, pierce), imodbits_axe],
["arena_axe", "Axe", [("arena_axe",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 137 , weight(1.5)|spd_rtng(100)| weapon_length(69)|swing_damage(24 , blunt)| thrust_damage(0 ,  pierce),imodbits_axe ],
["arena_sword", "Sword", [("arena_sword_one_handed",0),("sword_medieval_b_scabbard", ixmesh_carry),], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 243 , weight(1.5)|spd_rtng(99)| weapon_length(95)|swing_damage(22 , blunt)| thrust_damage(20 ,  blunt),imodbits_sword_high ],
["arena_sword_two_handed",  "Two Handed Sword", [("arena_sword_two_handed",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 670 , weight(2.75)|spd_rtng(93)| weapon_length(110)|swing_damage(30 , blunt)| thrust_damage(24 ,  blunt),imodbits_sword_high ],
["arena_lance",         "Lance", [("arena_lance",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_long_glaive|itcf_carry_spear, 90 , weight(2.5)|spd_rtng(96)| weapon_length(150)|swing_damage(20 , blunt)| thrust_damage(25 ,  blunt),imodbits_polearm ],
["practice_staff","Practice Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_long_glaive|itcf_carry_sword_back,9, weight(2.5)|spd_rtng(103)| weapon_length(118)|swing_damage(18,blunt)| thrust_damage(18,blunt),imodbits_none],
["practice_lance","Practice Lance", [("joust_of_peace",0)], itp_couchable|itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack|itp_crush_through, itc_greatlance, 18,weight(4.25)|spd_rtng(58)|weapon_length(240)|swing_damage(0,blunt)|thrust_damage(21,blunt),imodbits_none],
["practice_shield","Practice Shield", [("shield_round_a",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 20,weight(3.5)|body_armor(1)|shield_hit_points(200)|spd_rtng(100)|shield_width(50),imodbits_none],
["practice_bow","Practice Bow", [("hunting_bow",0), ("hunting_bow_carry",ixmesh_carry)], itp_type_bow|itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back, 0, weight(1.5)|spd_rtng(90)| shoot_speed(57)| thrust_damage(20, blunt),imodbits_bow ],

["practice_crossbow", "Practice Crossbow", [("crossbow_a",0)], itp_type_crossbow|itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0, weight(3)|spd_rtng(42)| shoot_speed(68)| thrust_damage(39,blunt)|max_ammo(1),imodbits_crossbow],
["practice_javelin", "Practice Javelins", [("javelin",0),("javelins_quiver_new", ixmesh_carry)], itp_type_thrown|itp_primary|itp_next_item_as_melee,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 0, weight(5)| spd_rtng(91)| shoot_speed(28)| thrust_damage(27, blunt)| max_ammo(50)| weapon_length(75), imodbits_thrown,missile_distance_trigger],
["practice_javelin_melee", "practice_javelin_melee", [("javelin",0)], itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry , itc_staff, 0, weight(1)|difficulty(0)|spd_rtng(91)|swing_damage(12, blunt)| thrust_damage(14,  blunt)|weapon_length(75),imodbits_polearm ],
["practice_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown|itp_primary ,itcf_throw_knife, 0 , weight(3.5)|spd_rtng(102)| shoot_speed(25)| thrust_damage(16, blunt)|max_ammo(10)|weapon_length(0),imodbits_thrown,missile_distance_trigger],
["practice_throwing_daggers_100_amount", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown|itp_primary ,itcf_throw_knife, 0 , weight(3.5)|spd_rtng(102)| shoot_speed(25)| thrust_damage(16, blunt)|max_ammo(100)|weapon_length(0),imodbits_thrown,missile_distance_trigger],
# ["cheap_shirt","Cheap Shirt", [("shirt",0)], itp_type_body_armor|itp_covers_legs, 0, 4,weight(1.25)|body_armor(3),imodbits_none],
["practice_horse","Practice Horse", [("saddle_horse",0)], itp_type_horse, 0, 37,body_armor(10)|horse_speed(40)|horse_maneuver(37)|horse_charge(14),imodbits_none],
["practice_arrows","Practice Arrows", [("arena_arrow",0),("flying_arrow",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(80)|thrust_damage(5,pierce),imodbits_missile,missile_distance_trigger],
## ["practice_arrows","Practice Arrows", [("arrow",0),("flying_arrow",ixmesh_flying_ammo)], itp_type_arrows, 0, 31,weight(1.5)|weapon_length(95)|max_ammo(80),imodbits_none],
["practice_bolts","Practice Bolts", [("bolt",0),("flying_bolt",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|weapon_length(55)|max_ammo(49)|thrust_damage(10,pierce),imodbits_missile,missile_distance_trigger],
["practice_arrows_10_amount","Practice Arrows", [("arrow",0),("flying_arrow",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(10)|thrust_damage(5,pierce),imodbits_missile,missile_distance_trigger],
["practice_arrows_100_amount","Practice Arrows", [("arrow",0),("flying_arrow",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(100),imodbits_missile,missile_distance_trigger],
["practice_bolts_9_amount","Practice Bolts", [("bolt",0),("flying_bolt",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|weapon_length(55)|max_ammo(9)|thrust_damage(5,pierce),imodbits_missile,missile_distance_trigger],
["practice_boots", "Practice Boots", [("boot_nomad_a",0)], itp_type_foot_armor|itp_civilian| itp_attach_armature,0, 11 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10), imodbits_cloth ],
["red_tourney_armor","Red Tourney Armor", [("mail_long_surcoat_new",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
["blue_tourney_armor","Blue Tourney Armor", [("mail_shirt_a",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
["green_tourney_armor","Green Tourney Armor", [("tattered_leather_armor_a",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
["gold_tourney_armor","Gold Tourney Armor", [("padded_armor",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
["red_tourney_helmet","Red Tourney Helmet",[("flattop_helmet_new",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],
["blue_tourney_helmet","Blue Tourney Helmet",[("segmented_helm_new",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],
["green_tourney_helmet","Green Tourney Helmet",[("hood_newgrn",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],
["gold_tourney_helmet","Gold Tourney Helmet",[("hood_new",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],

["arena_shield_red", "Shield", [("arena_shield_red",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|shield_hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
["arena_shield_blue", "Shield", [("arena_shield_blue",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|shield_hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
["arena_shield_green", "Shield", [("arena_shield_green",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|shield_hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
["arena_shield_yellow", "Shield", [("arena_shield_yellow",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|shield_hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],

["arena_armor_white", "Arena Armor White", [("arena_armorW_new",0)], itp_type_body_armor|itp_covers_legs ,0, 2704,mail_armor_tier_2,imodbits_armor ],
["arena_armor_red", "Arena Armor Red", [("arena_armorR_new",0)], itp_type_body_armor|itp_covers_legs ,0, 2704,mail_armor_tier_2,imodbits_armor],
["arena_armor_blue", "Arena Armor Blue", [("arena_armorB_new",0)], itp_type_body_armor|itp_covers_legs ,0, 2704,mail_armor_tier_2,imodbits_armor ],
["arena_armor_green", "Arena Armor Green", [("arena_armorG_new",0)], itp_type_body_armor|itp_covers_legs ,0, 2704,mail_armor_tier_2,imodbits_armor],
["arena_armor_yellow", "Arena Armor Yellow", [("arena_armorY_new",0)], itp_type_body_armor|itp_covers_legs ,0, 2704,mail_armor_tier_2,imodbits_armor ],

["arena_tunic_white", "Arena Tunic White ", [("arena_tunicW_new",0)], itp_type_body_armor|itp_covers_legs ,0, 100,cloth_tier_1,imodbits_cloth ],
["arena_tunic_red", "Arena Tunic Red", [("arena_tunicR_new",0)], itp_type_body_armor|itp_covers_legs ,0, 100,cloth_tier_1,imodbits_cloth ],
["arena_tunic_blue", "Arena Tunic Blue", [("arena_tunicB_new",0)], itp_type_body_armor|itp_covers_legs ,0, 100,cloth_tier_1,imodbits_cloth ],
["arena_tunic_green", "Arena Tunic Green", [("arena_tunicG_new",0)], itp_type_body_armor|itp_covers_legs ,0, 100,cloth_tier_1,imodbits_cloth],
["arena_tunic_yellow", "Arena Tunic Yellow", [("arena_tunicY_new",0)], itp_type_body_armor|itp_covers_legs ,0, 100,cloth_tier_1,imodbits_cloth],
#headwear
["arena_helmet_red", "Arena Helmet Red", [("arena_helmetR",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_helmet_blue", "Arena Helmet Blue", [("arena_helmetB",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_helmet_green", "Arena Helmet Green", [("arena_helmetG",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_helmet_yellow", "Arena Helmet Yellow", [("arena_helmetY",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["steppe_helmet_white", "Steppe Helmet White", [("steppe_helmetW",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ],
["steppe_helmet_red", "Steppe Helmet Red", [("steppe_helmetR",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ],
["steppe_helmet_blue", "Steppe Helmet Blue", [("steppe_helmetB",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ],
["steppe_helmet_green", "Steppe Helmet Green", [("steppe_helmetG",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ],
["steppe_helmet_yellow", "Steppe Helmet Yellow", [("steppe_helmetY",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_white", "Tourney Helm White", [("tourney_helmR",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_red", "Tourney Helm Red", [("tourney_helmR",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_blue", "Tourney Helm Blue", [("tourney_helmB",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_green", "Tourney Helm Green", [("tourney_helmG",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_yellow", "Tourney Helm Yellow", [("tourney_helmY",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_red", "Arena Turban", [("tuareg_open",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate],
["arena_turban_blue", "Arena Turban", [("tuareg_open",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_green", "Arena Turban", [("tuareg_open",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_yellow", "Arena Turban", [("tuareg_open",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],

# A treatise on The Method of Mechanical Theorems Archimedes

#This book must be at the beginning of readable books
["book_tactics","De Re Militari", [("book_a",0)], itp_type_book, 0, 4000,weight(2)|abundance(100),imodbits_none],
["book_persuasion","Rhetorica ad Herennium", [("book_b",0)], itp_type_book, 0, 5000,weight(2)|abundance(100),imodbits_none],
["book_leadership","The Life of Alixenus the Great", [("book_d",0)], itp_type_book, 0, 4200,weight(2)|abundance(100),imodbits_none],
["book_intelligence","Essays on Logic", [("book_e",0)], itp_type_book, 0, 2900,weight(2)|abundance(100),imodbits_none],
## CC
["book_prisoner_management","Ramun's Note", [("m_book",0)], itp_type_book, 0, 5000,weight(2)|abundance(100),imodbits_none],
## CC
["book_trade","A Treatise on the Value of Things", [("book_f",0)], itp_type_book, 0, 3100,weight(2)|abundance(100),imodbits_none],
["book_weapon_mastery", "On the Art of Fighting with Swords", [("m_book2",0)], itp_type_book, 0, 4200,weight(2)|abundance(100),imodbits_none],
["book_engineering","Method of Mechanical Theorems", [("book_open",0)], itp_type_book, 0, 4000,weight(2)|abundance(100),imodbits_none],

#Reference books
#This book must be at the beginning of reference books
["book_wound_treatment_reference","The Book of Healing", [("inv_church_book_a",0)], itp_merchandise|itp_type_book, 0, 7000,weight(2)|abundance(100),imodbits_none],
["book_surgery_reference","The Great Book of Surgery", [("inv_church_book_b",0)], itp_merchandise|itp_type_book, 0, 14000,weight(2)|abundance(100),imodbits_none],
## CC
["book_first_aid_reference","The General Knowledge of First Aid", [("inv_church_book_c",0)], itp_merchandise|itp_type_book, 0, 7000,weight(2)|abundance(100),imodbits_none],
["book_training_reference","Manual of Arms", [("inv_church_book_d",0)], itp_merchandise|itp_type_book, 0, 14000,weight(2)|abundance(100),imodbits_none],
["book_spotting_reference","The General Knowledge of Spotting", [("inv_church_book_e",0)], itp_merchandise|itp_type_book, 0, 7000,weight(2)|abundance(100),imodbits_none],
["book_pathfinding_reference","The Atlas of Calradia", [("inv_church_book_f",0)], itp_merchandise|itp_type_book, 0, 7000,weight(2)|abundance(100),imodbits_none],
## CC


#other trade goods (first one is spice)
  # Common trade goods

  ["spice","Spice", [("spice_sack",0), ("goods_spices", ixmesh_inventory)], itp_merchandise|itp_type_goods|itp_consumable, 0, 1760,weight(40)|abundance(25)|max_ammo(100),imodbit_large_bag|imodbit_exquisite],
  ["salt","Salt", [("salt_sack",0), ("goods_salt", ixmesh_inventory)], itp_merchandise|itp_type_goods, 0, 510,weight(50)|abundance(120),imodbit_large_bag],
  ["oil","Oil", [("oil",0), ("goods_oil", ixmesh_inventory)], itp_merchandise|itp_type_goods|itp_consumable, 0, 900,weight(50)|abundance(60)|max_ammo(100),imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite],
  ["pottery","Pottery", [("jug",0), ("goods_pottery", ixmesh_inventory)], itp_merchandise|itp_type_goods, 0, 200,weight(50)|abundance(90),imodbit_cracked|imodbit_crude|imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite|imodbit_lordly|imodbit_rough|imodbit_sturdy],
  ["raw_flax","Flax Bundle", [("raw_flax",0)], itp_merchandise|itp_type_goods, 0, 300,weight(40)|abundance(90),imodbit_fine|imodbit_exquisite],
  ["linen","Linen", [("linen",0), ("goods_linen", ixmesh_inventory)], itp_merchandise|itp_type_goods, 0, 500,weight(40)|abundance(90),imodbits_cloth_2],
  ["wool","Wool", [("wool_sack",0), ("goods_wool", ixmesh_inventory)], itp_merchandise|itp_type_goods, 0, 260,weight(40)|abundance(90),imodbit_fine|imodbit_exquisite],
  ["wool_cloth","Wool Cloth", [("wool_cloth",0), ("goods_cloth", ixmesh_inventory)], itp_merchandise|itp_type_goods, 0, 500,weight(40)|abundance(90),imodbits_cloth_2],
  ["raw_silk","Raw Silk", [("raw_silk_bundle",0), ("goods_raw_silk", ixmesh_inventory)], itp_merchandise|itp_type_goods, 0, 1200,weight(30)|abundance(90),imodbit_fine|imodbit_exquisite],
  ["raw_dyes","Dyes", [("dyes",0), ("goods_dyes", ixmesh_inventory)], itp_merchandise|itp_type_goods, 0, 400,weight(10)|abundance(90),imodbit_fine|imodbit_well_made|imodbit_exquisite|imodbit_masterwork],
  ["velvet","Velvet", [("velvet",0), ("goods_velvet", ixmesh_inventory)], itp_merchandise|itp_type_goods, 0, 2050,weight(40)|abundance(30),imodbit_fine|imodbit_well_made|imodbit_exquisite|imodbit_masterwork, [], [fac_kingdom_10]],

  ["iron","Iron", [("iron",0), ("goods_iron", ixmesh_inventory)], itp_merchandise|itp_type_goods, 0,528,weight(60)|abundance(60),imodbit_rusty|imodbit_poor|imodbit_well_made|imodbit_tempered|imodbit_hardened],
  ["tools","Tools", [("iron_hammer",0), ("goods_tools", ixmesh_inventory)], itp_merchandise|itp_type_goods, 0, 820,weight(50)|abundance(90),imodbit_rusty|imodbit_crude|imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite|imodbit_masterwork|imodbit_sturdy|imodbit_hardened],
  ["raw_leather","Hides", [("leatherwork_inventory",0), ("goods_hide", ixmesh_inventory)], itp_merchandise|itp_type_goods, 0, 240,weight(40)|abundance(90),imodbit_fine|imodbit_exquisite|imodbit_tattered|imodbit_ragged|imodbit_sturdy|imodbit_thick, [], [fac_kingdom_8]],
  ["leatherwork","Leatherwork", [("leatherwork_frame",0)], itp_merchandise|itp_type_goods, 0, 440,weight(40)|abundance(90),imodbits_cloth_2|imodbit_thick],
  ["raw_date_fruit","Date Fruit", [("date_inventory",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 240,weight(40)|food_quality(10)|max_ammo(10),imodbit_cheap|imodbit_fine|imodbit_exquisite],
  ["furs","Furs", [("fur_pack",0), ("goods_furs", ixmesh_inventory)], itp_merchandise|itp_type_goods, 0, 782,weight(40)|abundance(90),imodbit_cheap|imodbit_fine|imodbit_exquisite|imodbit_tattered|imodbit_ragged|imodbit_sturdy|imodbit_thick, [], [fac_kingdom_8]],



  # Food consumables

  ["smoked_fish","Smoked Fish", [("smoked_fish",0), ("goods_fish", ixmesh_inventory)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 130,weight(15)|abundance(110)|food_quality(50)|max_ammo(100),imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite],
  ["cheese","Cheese", [("cheese_b",0), ("goods_cheese", ixmesh_inventory)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 150,weight(6)|abundance(110)|food_quality(40)|max_ammo(60),imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite],
  ["honey","Honey", [("honey_pot",0), ("goods_honey", ixmesh_inventory)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 440,weight(5)|abundance(110)|food_quality(40)|max_ammo(60),imodbit_cheap|imodbit_fine|imodbit_exquisite],
  ["sausages","Sausages", [("sausages",0), ("goods_sausages", ixmesh_inventory)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 170,weight(10)|abundance(110)|food_quality(40)|max_ammo(80),imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite],
  ["cabbages","Cabbages", [("cabbage",0), ("goods_cabbage", ixmesh_inventory)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 60,weight(15)|abundance(110)|food_quality(40)|max_ammo(100),imodbit_cheap|imodbit_fine|imodbit_exquisite],
  ["dried_meat","Dried Meat", [("smoked_meat",0), ("goods_meat", ixmesh_inventory)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 170,weight(15)|abundance(100)|food_quality(70)|max_ammo(100),imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite],
  ["apples","Fruit", [("apple_basket",0), ("goods_fruit", ixmesh_inventory)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 88,weight(20)|abundance(110)|food_quality(40)|max_ammo(100),imodbit_cheap|imodbit_fine|imodbit_exquisite],
  ["raw_grapes","Grapes", [("grapes_inventory",0), ("goods_grapes", ixmesh_inventory)], itp_merchandise|itp_consumable|itp_type_goods, 0, 150,weight(40)|abundance(90)|food_quality(10)|max_ammo(20),imodbits_none], #x2 for imodbit_cheap|imodbit_fine|imodbit_exquisite
  ["raw_olives","Olives", [("olive_inventory",0), ("goods_olives", ixmesh_inventory)], itp_merchandise|itp_consumable|itp_type_goods, 0, 200,weight(40)|abundance(90)|food_quality(10)|max_ammo(20),imodbits_none], #x3 for imodbit_cheap|imodbit_fine|imodbit_exquisite
  ["grain","Grain", [("wheat_sack",0), ("goods_grain", ixmesh_inventory)], itp_merchandise|itp_type_goods|itp_consumable, 0, 60,weight(30)|abundance(110)|food_quality(40)|max_ammo(100),imodbit_cheap|imodbit_fine|imodbit_exquisite|imodbit_large_bag],
  ["cattle_meat","Beef", [("raw_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 160,weight(20)|abundance(100)|food_quality(80)|max_ammo(100),imodbits_none],
  ["bread","Bread", [("bread_a",0), ("goods_bread_a", ixmesh_inventory)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 100,weight(30)|abundance(110)|food_quality(40)|max_ammo(100),imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite],
  ["chicken","Chicken", [("chicken",0), ("goods_chicken", ixmesh_inventory)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 190,weight(10)|abundance(110)|food_quality(40)|max_ammo(100),imodbits_none],
  ["pork","Pork", [("pork",0), ("goods_pork", ixmesh_inventory)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 150,weight(15)|abundance(100)|food_quality(70)|max_ammo(100),imodbits_none],
  ["butter","Butter", [("butter_pot",0), ("goods_butter", ixmesh_inventory)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 300,weight(6)|abundance(110)|food_quality(40)|max_ammo(60),imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite],


  # Drinking consumables

  ["wine","Wine", [("amphora_slim",0), ("goods_wine", ixmesh_inventory)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 440,weight(30)|abundance(60)|max_ammo(100),imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite],
  ["ale","Ale", [("ale_barrel",0), ("goods_ale", ixmesh_inventory)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 240,weight(30)|abundance(70)|max_ammo(100),imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite|imodbit_lordly],




#Would like to remove flour altogether and reduce chicken, pork and butter (perishables) to non-trade items. Apples could perhaps become a generic "fruit", also representing dried fruit and grapes
# Armagan: changed order so that it'll be easier to remove them from trade goods if necessary.
#************************************************************************************************
# ITEMS before this point are hardcoded into item_codes.h and their order should not be changed!
#************************************************************************************************

# Quest Items

["siege_supply","Supplies", [("chest_simple",0), ("goods_supply", ixmesh_inventory)], itp_type_goods|itp_consumable|itp_food, 0, 1000,weight(40)|abundance(70)|food_quality(70)|max_ammo(500),imodbits_none],
["quest_wine","Wine", [("amphora_slim",0)], itp_type_goods, 0, 440,weight(40)|abundance(60)|max_ammo(50),imodbits_none],
["quest_ale","Ale", [("ale_barrel",0)], itp_type_goods, 0, 240,weight(40)|abundance(70)|max_ammo(50),imodbits_none],


# Tutorial Items

["drow_armor", "Light_Leather", [("drow_armor", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 924, weight(10)|abundance(10)|difficulty(4)|head_armor(0)|body_armor(45)|leg_armor(14), imodbits_armor, [], [fac_beast] ],
["drow_elite_armor", "drow_elite_armor", [("drow_elite_armor", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 7425, weight(16)|abundance(10)|difficulty(8)|head_armor(0)|body_armor(60)|leg_armor(20), imodbits_armor, [], [fac_beast] ],
["drow_elite_armor_1", "drow_elite_armor", [("dark_armor_low", 0)], merc_body_armor, 0, 7310, weight(20)|abundance(50)|head_armor(0)|body_armor(65)|leg_armor(30)|difficulty(13), imodbits_armor, [], [fac_beast] ],
["drow_elite_armor_2", "drow_elite_armor", [("dark_armor_med", 0)], merc_body_armor, 0, 9216, weight(20)|abundance(60)|head_armor(0)|body_armor(71)|leg_armor(35)|difficulty(15), imodbits_armor, [], [fac_beast] ],

["drow_elite_gloves","drow_elite_gloves", [("drow_elite_gloves_L",0)], itp_merchandise|itp_type_hand_armor,0,  1450, weight(1.25)|abundance(100)|body_armor(12)|difficulty(0),imodbits_armor,  [] , [fac_beast]],
["grim_raider_armor_1", "Grim Raider_Armor", [("dark_armor", 0)], merc_body_armor, 0, 10868, weight(20)|abundance(20)|head_armor(0)|body_armor(80)|leg_armor(45)|difficulty(18), imodbits_good_plate ,[], [fac_beast]],

["grim_raider_armor_2", "Grim Raider_Armor", [("DELFbody2_combined",0)], itp_civilian|itp_type_body_armor|itp_covers_legs|itp_replaces_shoes, 0, 20000, weight(20)|abundance(100)|head_armor(20)|body_armor(90)|leg_armor(80)|difficulty(20), imodbits_good_plate ,[], [fac_beast]],
["mistress_armor", "Mistress_armor", [("DELFbody1_combined",0)], itp_civilian|itp_type_body_armor|itp_covers_legs|itp_replaces_shoes, 0, 24000, weight(28)|abundance(100)|head_armor(20)|body_armor(100)|leg_armor(90)|difficulty(20), imodbits_good_plate ,[], [fac_beast]],
["drow_shield", "drow_shield", [("drow_shield", 0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 2156, weight(2)|shield_width(50)|shield_height(70)|abundance(10)|hit_points(1000)|body_armor(20)|spd_rtng(82), imodbits_shield, [], [fac_beast] ],
["drow_round_shield", "drow_round_shield", [("drow_round_shield", 0)], itp_merchandise|itp_type_shield|itp_wooden_parry, 0, 1685, weight(1)|shield_width(40)|shield_height(40)|abundance(10)|hit_points(700)|body_armor(30)|spd_rtng(96), imodbits_shield , [], [fac_beast]],
["drow_shield_rider", "drow_shield", [("sh_snake", 0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 4000, weight(2)|shield_width(30)|shield_height(60)|abundance(10)|hit_points(800)|body_armor(40)|spd_rtng(92), imodbits_shield , [], [fac_beast]],

["drow_crossbow", "Crossbow", [("drow_crossbow",0)], itp_merchandise|itp_type_crossbow|itp_primary|itp_is_magic_staff, itcf_shoot_pistol|itcf_reload_pistol, 1200, weight(3)|spd_rtng(50)|shoot_speed(100)|thrust_damage(65,pierce)|max_ammo(6), imodbits_crossbow , [], [fac_beast]],

#["flintlock_pistol", "Flintlock Pistol", [("flintlock_pistol",0)], itp_type_pistol|itp_merchandise|itp_primary ,itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_pistol_front_left, 

# Horses: sumpter horse/ pack horse, saddle horse, steppe horse, warm blood, geldling, stallion,   war mount, charger,
# Carthorse, hunter, heavy hunter, hackney, palfrey, courser, destrier.
["sumpter_horse","Sumpter Horse", [("sumpter_horse",0)], itp_merchandise|itp_type_horse, 0, 100,abundance(90)|hit_points(100)|body_armor(14)|difficulty(1)|horse_speed(37)|horse_maneuver(39)|horse_charge(9)|horse_scale(100),imodbits_horse_basic],

["mule","mule", [("lv",0)], itp_merchandise|itp_type_horse, 0, 100,abundance(90)|hit_points(100)|body_armor(14)|difficulty(1)|horse_speed(37)|horse_maneuver(42)|horse_charge(12)|horse_scale(100),imodbits_horse_basic],
#["donkey","donkey", [("luozi3",0)], itp_merchandise|itp_type_horse, 0, 100,abundance(90)|hit_points(100)|body_armor(14)|difficulty(1)|horse_speed(45)|horse_maneuver(30)|horse_charge(20)|horse_scale(100),imodbits_horse_basic],

["saddle_horse","Saddle Horse", [("saddle_horse",0)], itp_merchandise|itp_type_horse, 0, 120,abundance(90)|hit_points(110)|body_armor(12)|difficulty(1)|horse_speed(45)|horse_maneuver(44)|horse_charge(14)|horse_scale(104),imodbits_horse_basic, [], euro_factions],
["horse_euro","Saddle Horse", [("horse_c",0)], itp_merchandise|itp_type_horse, 0, 300,abundance(80)|body_armor(22)|hit_points(140)|difficulty(2)|horse_speed(48)|horse_maneuver(44)|horse_charge(20)|horse_scale(106),imodbits_horse_adv, [], we_faction],
["courser","Courser", [("courser",0)], itp_merchandise|itp_type_horse, 0, 300,abundance(70)|body_armor(18)|hit_points(120)|difficulty(2)|horse_speed(50)|horse_maneuver(44)|horse_charge(14)|horse_scale(106),imodbits_horse_adv, [], euro_factions],
["hunter","Hunter", [("hunting_horse",0)], itp_merchandise|itp_type_horse, 0, 410,abundance(60)|hit_points(170)|body_armor(32)|difficulty(3)|horse_speed(43)|horse_maneuver(44)|horse_charge(26)|horse_scale(108),imodbits_horse_adv, [], euro_factions],


["nord_horse","northerner Horse", [("northerner_horse",0)], itp_merchandise|itp_type_horse, 0, 740,abundance(80)|body_armor(24)|hit_points(200)|difficulty(2)|horse_speed(45)|horse_maneuver(44)|horse_charge(25)|horse_scale(112),imodbits_horse_adv, [], ne_faction],

["nord_courser","northerner Courser", [("northerner_horse_white",0)], itp_merchandise|itp_type_horse, 0, 800,abundance(70)|body_armor(20)|hit_points(180)|difficulty(2)|horse_speed(47)|horse_maneuver(44)|horse_charge(20)|horse_scale(112),imodbits_horse_adv, [], ne_faction],

["nord_hunter","northerner Hunter", [("northerner_horse_hunter",0)], itp_merchandise|itp_type_horse, 0, 800,abundance(60)|hit_points(250)|body_armor(34)|difficulty(3)|horse_speed(40)|horse_maneuver(44)|horse_charge(30)|horse_scale(112),imodbits_horse_adv, [], ne_faction],

["saddle_horse_steppe","Saddle Horse", [("steppe_horse",0)], itp_merchandise|itp_type_horse, 0, 120,abundance(90)|hit_points(120)|body_armor(8)|difficulty(1)|horse_speed(45)|horse_maneuver(44)|horse_charge(12)|horse_scale(98),imodbits_horse_basic, [], ee_faction+tatar_faction],
["steppe_horse","Steppe Horse", [("WTribal9",0)], itp_merchandise|itp_type_horse, 0, 120,abundance(80)|hit_points(140)|body_armor(10)|difficulty(2)|horse_speed(42)|horse_maneuver(51)|horse_charge(10)|horse_scale(98),imodbits_horse_basic, [], ee_faction+tatar_faction],
["courser_steppe","Courser", [("WTribal1",0)], itp_merchandise|itp_type_horse, 0, 300,abundance(70)|body_armor(12)|hit_points(130)|difficulty(2)|horse_speed(52)|horse_maneuver(44)|horse_charge(14)|horse_scale(98),imodbits_horse_adv, [], ee_faction+tatar_faction],
["hunter_steppe","Hunter", [("WTribal6",0)], itp_merchandise|itp_type_horse, 0, 410,abundance(60)|hit_points(180)|body_armor(18)|difficulty(3)|horse_speed(45)|horse_maneuver(44)|horse_charge(26)|horse_scale(98),imodbits_horse_adv, [], ee_faction+tatar_faction],
["hunter_steppe_good","Hunter", [("WTribal8",0)], itp_merchandise|itp_type_horse, 0, 410,abundance(60)|hit_points(200)|body_armor(18)|difficulty(3)|horse_speed(47)|horse_maneuver(44)|horse_charge(28)|horse_scale(98),imodbits_horse_adv, [], ee_faction+tatar_faction],

["coursera1", "Courser", [("exp_warhorse_w",0)], itp_type_horse|itp_merchandise, 0, 900, abundance(70)|body_armor(22)|hit_points(120)|difficulty(2)|horse_speed(50)|horse_maneuver(44)|horse_charge(16)|horse_scale(106), imodbits_horse_armor , [], tatar_faction],
["coursera2", "Courser", [("exp_charger_w",0)], itp_type_horse|itp_merchandise, 0, 1600, abundance(70)|body_armor(32)|hit_points(130)|difficulty(3)|horse_speed(50)|horse_maneuver(44)|horse_charge(20)|horse_scale(106), imodbits_horse_armor , [], tatar_faction],

["huntera1", "Hunter", [("harad_horse01",0),("harad_horse01",imodbits_horse_good)], itp_type_horse|itp_merchandise, 0, 1210, abundance(60)|hit_points(285)|body_armor(26)|difficulty(3)|horse_speed(47)|horse_maneuver(44)|horse_charge(32)|horse_scale(108), imodbits_horse_armor, [], tatar_faction],
["huntera2", "Hunter", [("harad_horse02",0),("harad_horse02",imodbits_horse_good)], itp_type_horse|itp_merchandise, 0, 1610, abundance(60)|hit_points(355)|body_armor(40)|difficulty(4)|horse_speed(47)|horse_maneuver(44)|horse_charge(34)|horse_scale(108), imodbits_horse_armor , [], tatar_faction],



["arabian_horse_a","Desert Horse", [("arabian_horse_a",0)], itp_merchandise|itp_type_horse, 0, 225,abundance(80)|hit_points(110)|body_armor(10)|difficulty(2)|horse_speed(42)|horse_maneuver(50)|horse_charge(12)|horse_scale(100),imodbits_horse_adv, [], arab_factions],
["arabian_horse_b","Sarranid Horse", [("arabian_horse_b",0)], itp_merchandise|itp_type_horse, 0, 350,abundance(80)|hit_points(120)|body_armor(10)|difficulty(3)|horse_speed(43)|horse_maneuver(54)|horse_charge(16)|horse_scale(100),imodbits_horse_adv, [], arab_factions],
["drow_basilisk", "Basilisk", [("Dark_Basilisk_2",0)], itp_merchandise|itp_type_horse|itp_disable_agent_sounds|itp_is_pike, 0, 4000, abundance(40)|hit_points(200)|body_armor(50)|difficulty(5)|horse_speed(35)|horse_maneuver(50)|horse_charge(30)|horse_scale(112), imodbits_horse_armor, [], [fac_beast]],
["lizard_basilisk", "Basilisk", [("Lizard_Dark_Basilisk_2",0)], itp_merchandise|itp_type_horse|itp_disable_agent_sounds|itp_is_pike, 0, 4000, abundance(40)|hit_points(200)|body_armor(50)|difficulty(5)|horse_speed(35)|horse_maneuver(50)|horse_charge(30)|horse_scale(112), imodbits_horse_armor, [], [fac_beast]],


["boar_mount_charge","boar_mount_charge", [("boar_mount_saddled",0)],itp_merchandise|itp_type_horse|itp_disable_agent_sounds|itp_is_pike, 0, 1411,abundance(40)|hit_points(300)|body_armor(45)|difficulty(3)|horse_speed(35)|horse_maneuver(32)|horse_charge(27),imodbits_horse_adv, [], [fac_orc]],

["warboar", "War_Boar", [("heavy_boar", 0)], itp_merchandise|itp_type_horse|itp_disable_agent_sounds|itp_is_pike, 0, 2950, abundance(50)|difficulty(4)|hit_points(300)|body_armor(65)|horse_speed(36)|horse_maneuver(36)|horse_charge(35)|horse_scale(0), imodbits_horse_armor, [], [fac_orc]],

["pegasus", "Pegasus", [("Pegasus",0)], itp_type_horse|itp_merchandise|itp_is_magic_staff, 0, 3000, abundance(70)|body_armor(32)|hit_points(200)|difficulty(3)|horse_speed(50)|horse_maneuver(44)|horse_charge(20)|horse_scale(106), imodbits_horse_armor , [], [fac_forest_ranger,fac_elf]],
["charger_pegasus","Charger Pegasus", [("charge_Pegasus",0)], itp_merchandise|itp_type_horse|itp_is_magic_staff, 0, 4000,abundance(40)|hit_points(200)|body_armor(65)|difficulty(5)|horse_speed(45)|horse_maneuver(46)|horse_charge(35)|horse_scale(112),imodbits_horse_armor, [], [fac_kingdom_4]],

["unicorn", "unicorn", [("unicorn",0)], itp_merchandise|itp_type_horse|itp_is_pike, 0, 4000, abundance(40)|hit_points(300)|body_armor(50)|difficulty(6)|horse_speed(50)|horse_maneuver(46)|horse_charge(25)|horse_scale(112), imodbits_horse_armor, [], [fac_forest_ranger,fac_elf]],
#["unicorn", "unicorn", [("unicorn",0)], itp_merchandise|itp_type_horse, 0, 4000, abundance(40)|hit_points(300)|body_armor(50)|difficulty(6)|horse_speed(50)|horse_maneuver(46)|horse_charge(35)|horse_scale(112), imodbits_horse_armor, [], [fac_forest_ranger,fac_elf]],
["bear","goar_mount", [("arhar_armor",0)],itp_merchandise|itp_type_horse|itp_disable_agent_sounds|itp_is_pike, 0, 8000,abundance(40)|hit_points(300)|body_armor(60)|difficulty(5)|horse_speed(35)|horse_maneuver(50)|horse_charge(45),imodbits_horse_armor, [], [fac_dwarf]],

["gorgon_1", "Gorgon", [("gorgonka", 0)], itp_type_horse|itp_merchandise|itp_disable_agent_sounds|itp_is_pike, 0, 8000, abundance(40)|difficulty(4)|hit_points(350)|body_armor(42)|horse_speed(35)|horse_maneuver(42)|horse_charge(40)|horse_scale(115), imodbits_horse_armor, [], [fac_scotland]], 
["gorgon_2", "Mighty_Gorgon", [("upg_gorgonka", 0)], itp_type_horse|itp_merchandise|itp_disable_agent_sounds|itp_is_pike, 0, 10000, abundance(40)|difficulty(5)|hit_points(350)|body_armor(50)|horse_speed(42)|horse_maneuver(42)|horse_charge(45)|horse_scale(120), imodbits_horse_armor, [], [fac_scotland]], 

["griffin", "griffin", [("griffin",0)], itp_merchandise|itp_type_horse|itp_disable_agent_sounds|itp_is_magic_staff|itp_is_pike, 0, 4000, abundance(40)|hit_points(300)|body_armor(50)|difficulty(4)|horse_speed(50)|horse_maneuver(33)|horse_charge(35)|horse_scale(120), imodbits_horse_armor, [], [fac_kingdom_1,fac_kingdom_7,fac_dwarf]],
["armor_griffin", "armor_griffin", [("armor_griffin",0)], itp_merchandise|itp_type_horse|itp_disable_agent_sounds|itp_is_magic_staff|itp_is_pike, 0, 6000, abundance(20)|hit_points(500)|body_armor(90)|difficulty(6)|horse_speed(50)|horse_maneuver(30)|horse_charge(50)|horse_scale(120), imodbits_horse_armor, [], [fac_kingdom_1]],
["armor_demi_griffin","Charger", [("demigryph",0)], itp_merchandise|itp_type_horse|itp_disable_agent_sounds|itp_is_pike, 0, 5000,abundance(40)|hit_points(300)|body_armor(80)|difficulty(5)|horse_speed(45)|horse_maneuver(40)|horse_charge(35)|horse_scale(100),imodbits_horse_armor, [], [fac_kingdom_7]],




["camel","Pack camel", [("camel",0)], itp_merchandise|itp_type_horse|itp_disable_agent_sounds, 0, 487,abundance(90)|hit_points(150)|body_armor(12)|difficulty(0)|horse_speed(32)|horse_maneuver(58)|horse_charge(14)|horse_scale(123),imodbits_horse_adv, [], arab_factions],
["camel2","Riding camel", [("camel2",0)], itp_merchandise|itp_type_horse|itp_disable_agent_sounds, 0, 1011,abundance(80)|hit_points(200)|body_armor(15)|difficulty(2)|horse_speed(39)|horse_maneuver(63)|horse_charge(15)|horse_scale(125),imodbits_horse_adv, [], arab_factions],

["wolf_mount_white","wolf_mount_white", [("warg1",0)],itp_merchandise|itp_type_horse|itp_disable_agent_sounds|itp_is_pike, 0, 1411,abundance(40)|hit_points(150)|body_armor(30)|difficulty(2)|horse_speed(50)|horse_maneuver(50)|horse_charge(25),imodbits_horse_adv, [], [fac_orc]],

["wolf_mount_black","wolf_mount_black", [("warg",0)],itp_merchandise|itp_type_horse|itp_disable_agent_sounds|itp_is_pike, 0, 1411,abundance(40)|hit_points(150)|body_armor(30)|difficulty(2)|horse_speed(47)|horse_maneuver(50)|horse_charge(20),imodbits_horse_adv, [], [fac_orc]],
["drow_basilisk_2", "Armor_Basilisk", [("Dark_Basilisk",0)], itp_merchandise|itp_type_horse|itp_disable_agent_sounds|itp_is_pike, 0, 6000, abundance(20)|hit_points(300)|body_armor(65)|difficulty(6)|horse_speed(40)|horse_maneuver(50)|horse_charge(40)|horse_scale(112), imodbits_horse_armor, [], [fac_beast]],
["lizard_basilisk_2", "Armor_Basilisk", [("Lizard_Dark_Basilisk",0)], itp_merchandise|itp_type_horse|itp_disable_agent_sounds|itp_is_pike, 0, 6000, abundance(20)|hit_points(300)|body_armor(65)|difficulty(6)|horse_speed(40)|horse_maneuver(50)|horse_charge(40)|horse_scale(112), imodbits_horse_armor, [], [fac_beast]],

["spider","spider", [("spider",0)],itp_merchandise|itp_type_horse|itp_disable_agent_sounds|itp_is_pike, 0, 1411,abundance(40)|hit_points(200)|body_armor(30)|difficulty(3)|horse_speed(37)|horse_maneuver(70)|horse_charge(25),imodbits_horse_adv, [], [fac_orc,fac_beast]],


["nightmare", "nightmare", [("nightmarep",0)], itp_merchandise|itp_type_horse|itp_is_magic_staff, 0, 4000, abundance(40)|hit_points(300)|body_armor(50)|difficulty(6)|horse_speed(50)|horse_maneuver(46)|horse_charge(35)|horse_scale(112), imodbits_horse_armor, [], [fac_kingdom_9,fac_kingdom_3]],
["hell_nightmare", "nightmare", [("nightmare",0)], itp_merchandise|itp_type_horse|itp_is_magic_staff|itp_is_pike, 0, 8000, abundance(20)|hit_points(500)|body_armor(50)|difficulty(7)|horse_speed(50)|horse_maneuver(58)|horse_charge(40)|horse_scale(120), imodbits_horse_armor, [], [fac_demon]],
["nightmare_armor", "nightmare_armor", [("nightmare_armor",0)], itp_merchandise|itp_type_horse|itp_is_magic_staff, 0, 8000, abundance(30)|hit_points(300)|body_armor(80)|difficulty(7)|horse_speed(45)|horse_maneuver(52)|horse_charge(50)|horse_scale(112), imodbits_horse_armor, [], [fac_kingdom_9]],


["black_dragon","Black Dragon", [("anheilong",0)], itp_merchandise|itp_type_horse|itp_disable_agent_sounds|itp_is_magic_staff|itp_is_pike, 0, 8000,abundance(20)|hit_points(500)|body_armor(80)|difficulty(6)|horse_speed(60)|horse_maneuver(90)|horse_charge(45)|horse_scale(112),imodbits_horse_armor, [], [fac_kingdom_8]],
["bonedrake","bone drake", [("bonedrake",0)], itp_merchandise|itp_type_horse|itp_disable_agent_sounds|itp_is_magic_staff|itp_is_pike, 0, 8000,abundance(20)|hit_points(500)|body_armor(80)|difficulty(6)|horse_speed(60)|horse_maneuver(90)|horse_charge(45)|horse_scale(112),imodbits_horse_armor, [], [fac_undeads_2]],


["undead_charger","bone drake", [("nightmare2",0)], itp_merchandise|itp_type_horse|itp_is_magic_staff|itp_is_pike, 0, 8000,abundance(20)|hit_points(500)|body_armor(80)|difficulty(6)|horse_speed(60)|horse_maneuver(90)|horse_charge(55)|horse_scale(112),imodbits_horse_armor, [], [fac_undeads_2]],
#["undead_charger","bone drake", [("dark_charger_d",0)], itp_merchandise|itp_type_horse, 0, 8000,abundance(20)|hit_points(500)|body_armor(80)|difficulty(6)|horse_speed(60)|horse_maneuver(90)|horse_charge(55)|horse_scale(112),imodbits_horse_armor, [], [fac_undeads_2]],
["undead_charger_2","Charger", [("dark_charger_a",0)], itp_merchandise|itp_type_horse, 0, 5000,abundance(40)|hit_points(350)|body_armor(80)|difficulty(6)|horse_speed(47)|horse_maneuver(50)|horse_charge(40)|horse_scale(112),imodbits_horse_armor, [], [fac_undeads_2]],
["undead_charger_plate","Charger", [("dark_charger_c",0)], itp_merchandise|itp_type_horse, 0, 6000,abundance(30)|hit_points(400)|body_armor(80)|difficulty(7)|horse_speed(45)|horse_maneuver(52)|horse_charge(50)|horse_scale(112),imodbits_horse_armor, [], [fac_undeads_2]],



["camel3","war camel", [("camel3",0)], itp_merchandise|itp_type_horse|itp_disable_agent_sounds, 0,1555,abundance(70)|hit_points(300)|body_armor(25)|difficulty(3)|horse_speed(32)|horse_maneuver(58)|horse_charge(25)|horse_scale(127),imodbits_horse_armor, [], arab_factions],

["armored_horse_france", "armored_horse", [("armored_horse_france",0)], itp_type_horse|itp_merchandise, 0, 1210, abundance(60)|hit_points(170)|body_armor(29)|difficulty(3)|horse_speed(43)|horse_maneuver(44)|horse_charge(27)|horse_scale(108), imodbits_horse_armor , [], [fac_kingdom_1]],
["armored_horse_german", "armored_horse", [("armored_horse_german",0)], itp_type_horse|itp_merchandise, 0, 1210, abundance(60)|hit_points(170)|body_armor(29)|difficulty(3)|horse_speed(43)|horse_maneuver(44)|horse_charge(27)|horse_scale(108), imodbits_horse_armor , [], [fac_kingdom_7]],

["barded_horse_green","barded Horse", [("barded8W",0)], itp_merchandise|itp_type_horse, 0, 1724,abundance(55)|hit_points(165)|body_armor(40)|difficulty(3)|horse_speed(40)|horse_maneuver(45)|horse_charge(24)|horse_scale(110),imodbits_horse_armor, [], [fac_kingdom_5]],
["barded_horse_red","barded Horse", [("barded_england",0)], itp_merchandise|itp_type_horse, 0, 1724,abundance(55)|hit_points(165)|body_armor(40)|difficulty(3)|horse_speed(40)|horse_maneuver(45)|horse_charge(24)|horse_scale(110),imodbits_horse_armor, [], [fac_kingdom_4]],
["barded_horse_german","barded Horse", [("barded_german",0)], itp_merchandise|itp_type_horse, 0, 1724,abundance(55)|hit_points(165)|body_armor(40)|difficulty(3)|horse_speed(40)|horse_maneuver(45)|horse_charge(24)|horse_scale(110),imodbits_horse_armor, [], [fac_kingdom_7]],
["barded_horse_teuton","barded Horse", [("da_warhorse02",0)], itp_merchandise|itp_type_horse, 0, 1724,abundance(55)|hit_points(165)|body_armor(40)|difficulty(3)|horse_speed(40)|horse_maneuver(45)|horse_charge(24)|horse_scale(110),imodbits_horse_armor, [], [fac_kingdom_1]],

["warhorse_england","War Horse", [("horse5_4",0)], itp_merchandise|itp_type_horse, 0, 1824,abundance(50)|hit_points(175)|body_armor(50)|difficulty(4)|horse_speed(40)|horse_maneuver(41)|horse_charge(28)|horse_scale(110),imodbits_horse_armor, [], [fac_kingdom_4]],
["warhorse_england_2","War Horse", [("horse5_4_a",0)], itp_merchandise|itp_type_horse, 0, 2000,abundance(50)|hit_points(190)|body_armor(55)|difficulty(4)|horse_speed(40)|horse_maneuver(41)|horse_charge(32)|horse_scale(110),imodbits_horse_armor, [], [fac_kingdom_4]],
["warhorse_france","War Horse", [("gondor_warhorse01",0)], itp_merchandise|itp_type_horse, 0, 1824,abundance(50)|hit_points(165)|body_armor(50)|difficulty(4)|horse_speed(40)|horse_maneuver(41)|horse_charge(28)|horse_scale(110),imodbits_horse_armor, [], [fac_kingdom_1]],
["warhorse_german","War Horse", [("horse7",0)], itp_merchandise|itp_type_horse, 0, 1824,abundance(50)|hit_points(165)|body_armor(50)|difficulty(4)|horse_speed(40)|horse_maneuver(41)|horse_charge(28)|horse_scale(110),imodbits_horse_armor, [], [fac_kingdom_7]],


["warhorse_teuton","War Horse", [("da_warhorse01",0)], itp_merchandise|itp_type_horse, 0, 1824,abundance(50)|hit_points(165)|body_armor(50)|difficulty(4)|horse_speed(40)|horse_maneuver(41)|horse_charge(28)|horse_scale(110),imodbits_horse_armor, [], [fac_kingdom_1]],

["charger_england","Charger", [("charge_england",0)], itp_merchandise|itp_type_horse, 0, 2511,abundance(40)|hit_points(200)|body_armor(65)|difficulty(4)|horse_speed(37)|horse_maneuver(46)|horse_charge(35)|horse_scale(112),imodbits_horse_armor, [], [fac_kingdom_4]],
["charger_france","Charger", [("horse_gondor",0)], itp_merchandise|itp_type_horse, 0, 2511,abundance(40)|hit_points(165)|body_armor(60)|difficulty(4)|horse_speed(40)|horse_maneuver(44)|horse_charge(33)|horse_scale(112),imodbits_horse_armor, [], [fac_kingdom_1]],
["charger_france_2","Charger", [("charge_gondor",0)], itp_merchandise|itp_type_horse, 0, 2511,abundance(40)|hit_points(250)|body_armor(70)|difficulty(5)|horse_speed(47)|horse_maneuver(44)|horse_charge(45)|horse_scale(112),imodbits_horse_armor, [], [fac_kingdom_1]],


["charger_german","Charger", [("charge_german",0)], itp_merchandise|itp_type_horse, 0, 2511,abundance(40)|hit_points(170)|body_armor(60)|difficulty(4)|horse_speed(40)|horse_maneuver(44)|horse_charge(33)|horse_scale(112),imodbits_horse_armor, [], [fac_kingdom_7]],

["charger_teuton","Charger", [("horse_dolamroth",0)], itp_merchandise|itp_type_horse, 0, 2511,abundance(40)|hit_points(180)|body_armor(60)|difficulty(4)|horse_speed(40)|horse_maneuver(44)|horse_charge(33)|horse_scale(112),imodbits_horse_armor, [], [fac_kingdom_1]],
["charger_teuton_2","Charger", [("horse_dolamroth",0)], itp_merchandise|itp_type_horse, 0, 2511,abundance(40)|hit_points(180)|body_armor(60)|difficulty(4)|horse_speed(40)|horse_maneuver(44)|horse_charge(33)|horse_scale(112),imodbits_horse_armor, [], [fac_kingdom_1]],

["charger_plate_german","Charger", [("horse6",0)], itp_merchandise|itp_type_horse, 0, 3511,abundance(40)|hit_points(200)|body_armor(80)|difficulty(5)|horse_speed(35)|horse_maneuver(40)|horse_charge(50)|horse_scale(112),imodbits_horse_armor, [], [fac_kingdom_7]],

["charger_noble","Charger", [("horse4",0)], itp_merchandise|itp_type_horse, 0, 3511,abundance(40)|hit_points(200)|body_armor(75)|difficulty(5)|horse_speed(40)|horse_maneuver(40)|horse_charge(40)|horse_scale(112),imodbits_horse_armor, [], euro_factions],


["warhorse","War Horse", [("horse5_3",0)], itp_merchandise|itp_type_horse, 0, 1824,abundance(50)|hit_points(200)|body_armor(55)|difficulty(4)|horse_speed(40)|horse_maneuver(41)|horse_charge(28)|horse_scale(110),imodbits_horse_armor, [], euro_factions],
["nord_warhorse","nord War Horse", [("war_horse_09",0)], itp_merchandise|itp_type_horse, 0, 1824,abundance(50)|hit_points(230)|body_armor(65)|difficulty(4)|horse_speed(33)|horse_maneuver(35)|horse_charge(50)|horse_scale(110),imodbits_horse_armor , [], ne_faction],
["charger_old","Charger", [("horse3",0)], itp_merchandise|itp_type_horse, 0, 3511,abundance(40)|hit_points(200)|body_armor(80)|difficulty(5)|horse_speed(35)|horse_maneuver(40)|horse_charge(50)|horse_scale(112),imodbits_horse_armor, [], euro_factions],

["charger","Charger", [("horse5_3_a",0)], itp_merchandise|itp_type_horse, 0, 2511,abundance(40)|hit_points(200)|body_armor(60)|difficulty(4)|horse_speed(40)|horse_maneuver(44)|horse_charge(33)|horse_scale(112),imodbits_horse_armor, [], ne_faction],

["charger_black", "Black Charger", [("warhorse_08y",0)], itp_type_horse, 0, 2811, abundance(40)|hit_points(200)|body_armor(70)|difficulty(4)|horse_speed(39)|horse_maneuver(44)|horse_charge(35)|horse_scale(112), imodbits_horse_armor, [], ne_faction],

["vaegir_warhorse", "warhorse", [("lamellar_charger_a",0)], itp_type_horse|itp_merchandise, 0, 1824, abundance(50)|hit_points(170)|body_armor(50)|difficulty(4)|horse_speed(45)|horse_maneuver(50)|horse_charge(35)|horse_scale(100), imodbits_horse_armor, [], ee_faction],
["vaegir_charger","Charger", [("mongols_charger3",0)], itp_merchandise|itp_type_horse, 0, 2511,abundance(40)|hit_points(170)|body_armor(60)|difficulty(5)|horse_speed(47)|horse_maneuver(49)|horse_charge(40)|horse_scale(100),imodbits_horse_armor, [], ee_faction],
["vaegir_charger_2","Charger", [("lamellar_charger_b",0)], itp_merchandise|itp_type_horse, 0, 2511,abundance(40)|hit_points(170)|body_armor(60)|difficulty(5)|horse_speed(47)|horse_maneuver(49)|horse_charge(40)|horse_scale(100),imodbits_horse_armor, [], ee_faction],

["warhorse_steppe","Steppe Charger", [("easterling_warhorse01",0)], itp_merchandise|itp_type_horse, 0, 2000,abundance(45)|hit_points(175)|body_armor(60)|difficulty(4)|horse_speed(40)|horse_maneuver(50)|horse_charge(28)|horse_scale(112),imodbits_horse_armor, [], ee_faction],
["khergit_charger", "khergit Charger", [("easterling_warhorse01",0)], itp_type_horse|itp_merchandise, 0, 1850, abundance(45)|hit_points(180)|body_armor(60)|difficulty(4)|horse_speed(43)|horse_maneuver(44)|horse_charge(35)|horse_scale(110), imodbits_horse_armor , [], tatar_faction],
["khergit_war_horse", "khergit war horse", [("dragonhorse",0)], itp_type_horse|itp_merchandise, 0, 2500, abundance(45)|hit_points(220)|body_armor(60)|difficulty(5)|horse_speed(43)|horse_maneuver(44)|horse_charge(35)|horse_scale(110), imodbits_horse_armor , [], tatar_faction],

["lamellar_warhorse","War Horse", [("3lamellar_charger",0)], itp_merchandise|itp_type_horse, 0, 1824,abundance(50)|hit_points(170)|body_armor(30)|difficulty(4)|horse_speed(42)|horse_maneuver(52)|horse_charge(20)|horse_scale(110),imodbits_horse_armor , [], arab_factions],
["lamellar_warhorse_2","War Horse", [("lamellar_charger_y",0)], itp_merchandise|itp_type_horse, 0, 2000,abundance(50)|hit_points(180)|body_armor(55)|difficulty(4)|horse_speed(40)|horse_maneuver(50)|horse_charge(28)|horse_scale(110),imodbits_horse_armor, [], arab_factions],
["lamellar_charger", "Lamellar Charger", [("lamellar_charger_x",0)], itp_type_horse|itp_merchandise, 0, 2511, abundance(40)|hit_points(190)|body_armor(60)|difficulty(4)|horse_speed(40)|horse_maneuver(44)|horse_charge(35)|horse_scale(112), imodbits_horse_armor , [], arab_factions],
["warhorse_sarranid","Sarranian War Horse", [("warhorse_sarranid",0)], itp_merchandise|itp_type_horse, 0, 2811,abundance(40)|hit_points(200)|body_armor(80)|difficulty(5)|horse_speed(40)|horse_maneuver(40)|horse_charge(42)|horse_scale(112),imodbits_horse_armor, [], arab_factions],
["lorien_warhorse", "Lothlorien_Warhorse", [("loth_warhorse01", 0)], itp_merchandise|itp_type_horse, 0, 5973, difficulty(5)|abundance(10)|hit_points(180)|body_armor(52)|horse_charge(32)|horse_maneuver(43)|horse_speed(40)|horse_scale(110), imodbits_horse_good , [], [fac_elf]],
["tzeentch_charger", "Tzeentch Charger", [("war_horse_b_tunde",0)], itp_merchandise|itp_type_horse, 0, 8000, abundance(30)|hit_points(300)|body_armor(80)|difficulty(7)|horse_speed(45)|horse_maneuver(52)|horse_charge(50)|horse_scale(112), imodbits_horse_armor, [], [fac_demon,fac_undeads_2]],




#whalebone crossbow, yew bow, war bow, arming sword
["arrows","Arrows", [("arrows_h1",0),("arrows_flying_h1",ixmesh_flying_ammo),("arrows_quiver_h1", ixmesh_carry),("arrows_quiver_h1", ixmesh_inventory)], itp_type_arrows|itp_merchandise|itp_default_ammo, itcf_carry_quiver_back, 
 72,weight(3)|abundance(90)|weapon_length(95)|thrust_damage(25,cut)|max_ammo(30),
 imodbits_missile, missile_distance_trigger, bow_factions
 ],


["khergit_arrows","Khergit Arrows", [("tatar_arrows_h2",0),("tatar_arrows_flying_h2",ixmesh_flying_ammo),("tatar_arrows_quiver_h2", ixmesh_carry),("tatar_arrows_quiver_h2", ixmesh_inventory)], itp_type_arrows, itcf_carry_quiver_back_right, 
  1230,weight(3.5)|abundance(50)|weapon_length(95)|thrust_damage(35,cut)|max_ammo(30),
  imodbits_missile,missile_distance_trigger, arab_factions+ee_faction
 ],
["barbed_arrows","Barbed Arrows", [("barbed_arrow",0),("flying_barbed_arrow",ixmesh_flying_ammo),("barbed_arrows_quiver_h2", ixmesh_carry),("barbed_arrows_quiver_h2", ixmesh_inventory)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 
 350,weight(3)|abundance(70)|weapon_length(95)|thrust_damage(30,cut)|max_ammo(30),
 imodbits_missile,missile_distance_trigger, bow_factions
 ],
["bodkin_arrows","Bodkin Arrows", [("bodkin_arrows_h2",0),("bodkin_arrows_flying_h2",ixmesh_flying_ammo),("bodkin_arrows_quiver_h2", ixmesh_carry),("bodkin_arrows_quiver_h2", ixmesh_inventory)], itp_type_arrows|itp_merchandise|itp_can_penetrate_shield, itcf_carry_quiver_back, 
 900,weight(3)|abundance(50)|weapon_length(91)|thrust_damage(30,pierce)|max_ammo(30),
 imodbits_missile,missile_distance_trigger, 
 bow_factions
 ],
  #NEW
["flat_headed_arrows","Flat Headed Arrows", [("flat_headed_arrow",0),("flying_flat_headed_arrow",ixmesh_flying_ammo),("flat_headed_arrow_quiver", ixmesh_carry),("flat_headed_arrow_quiver", ixmesh_inventory)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back, 
 1230,weight(6)|abundance(20)|weapon_length(90)|thrust_damage(40,cut)|max_ammo(30),
 imodbits_missile,missile_distance_trigger, ee_faction
 ],
["bamboo_arrows","Bamboo Arrows", [("bamboo_arrow",0),("flying_bamboo_arrow",ixmesh_flying_ammo),("bamboo_arrow_quiver", ixmesh_carry),("bamboo_arrow_quiver", ixmesh_inventory)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 
 150,weight(2.5)|abundance(40)|weapon_length(95)|thrust_damage(27,cut)|max_ammo(30),
 imodbits_missile,missile_distance_trigger, arab_factions
 ],
["piercing_arrows","Piercing Arrows", [("piercing_arrow_2",0),("flying_piercing_arrow_2",ixmesh_flying_ammo),("piercing_arrow_2_quiver", ixmesh_carry),("piercing_arrow_2_quiver", ixmesh_inventory)], itp_type_arrows|itp_can_penetrate_shield|itp_extra_penetration, itcf_carry_quiver_back,
 900,weight(4)|abundance(10)|weapon_length(91)|thrust_damage(35,pierce)|max_ammo(30),
 imodbits_missile,missile_distance_trigger, bow_factions
 ],
  #NEW
["woodelf_arrows", "Woodelf_Arrows", [("mirkwood_arrow", 0), ("mirkwood_arrow_flying", ixmesh_flying_ammo), ("mirkwood_quiver_new", ixmesh_carry),("mirkwood_quiver_new", ixmesh_inventory)], itp_merchandise|itp_type_arrows, itcf_carry_quiver_back, 
 1230, weight(1)|weapon_length(91)|abundance(10)|thrust_damage(30, pierce)|max_ammo(30), imodbits_missile,missile_distance_trigger, [fac_elf, fac_forest_ranger] ],
 
["elven_arrows", "Elven_Arrows", [("white_elf_arrow", 0), ("white_elf_arrow_flying", ixmesh_flying_ammo), ("lothlorien_quiver", ixmesh_carry),("lothlorien_quiver", ixmesh_inventory)], itp_merchandise|itp_type_arrows, itcf_carry_quiver_back, 1200, weight(3)|weapon_length(91)|abundance(10)|thrust_damage(36, pierce)|max_ammo(30), imodbits_missile ,missile_distance_trigger, [fac_elf, fac_forest_ranger]],
  #NEW
  
["iron_arrow","Iron Arrows", [("ironarrow",0),("flying_ironarrow",ixmesh_flying_ammo),("ironarrow_quiver", ixmesh_carry),("ironarrow_quiver", ixmesh_inventory)], itp_type_arrows|itp_merchandise|itp_default_ammo, itcf_carry_quiver_back, 
 150,weight(3)|abundance(90)|weapon_length(95)|thrust_damage(30,cut)|max_ammo(20),
 imodbits_missile, missile_distance_trigger, bow_factions
 ],
["steel_arrow","Steel Arrows", [("steelarrow",0),("flying_steelarrow",ixmesh_flying_ammo),("steelarrow_quiver", ixmesh_carry),("steelarrow_quiver", ixmesh_inventory)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 
 350,weight(3)|abundance(70)|weapon_length(95)|thrust_damage(36,cut)|max_ammo(20),
 imodbits_missile,missile_distance_trigger, bow_factions
 ],
["undead_arrow","Nordhero Arrows", [("nordheroarrow",0),("flying_nordheroarrow",ixmesh_flying_ammo),("nordheroarrow_quiver", ixmesh_carry),("nordheroarrow_quiver", ixmesh_inventory)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 
 350,weight(2.5)|abundance(70)|weapon_length(95)|thrust_damage(36,cut)|max_ammo(20),
 imodbits_missile,missile_distance_trigger, [fac_kingdom_5, fac_kingdom_10],
 ],
["nordic_arrow","Nordic Arrows", [("nordicarrow",0),("flying_nordicarrow",ixmesh_flying_ammo),("nordicarrow_quiver", ixmesh_carry),("nordicarrow_quiver", ixmesh_inventory)], itp_type_arrows|itp_can_penetrate_shield|itp_extra_penetration|itp_merchandise, itcf_carry_quiver_back,
 700,weight(4)|abundance(10)|weapon_length(91)|thrust_damage(42,cut)|max_ammo(20),
 imodbits_missile,missile_distance_trigger, [fac_elf, fac_kingdom_10, fac_scotland],
 ],
["elven_arrow","Elven Arrows", [("elvenarrow",0),("flying_elvenarrow",ixmesh_flying_ammo),("elvenarrow_quiver", ixmesh_carry),("elvenarrow_quiver", ixmesh_inventory)], itp_type_arrows|itp_merchandise|itp_can_penetrate_shield, itcf_carry_quiver_back, 
 1230,weight(1)|abundance(50)|weapon_length(91)|thrust_damage(30,pierce)|max_ammo(30),
 imodbits_missile,missile_distance_trigger,  [fac_elf, fac_forest_ranger, fac_kingdom_4],
 ],

["glass_arrow","Glass Arrows", [("glassarrow",0),("flying_glassarrow",ixmesh_flying_ammo),("glassarrow_quiver", ixmesh_carry),("glassarrow_quiver", ixmesh_inventory)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back, 
 1200,weight(1.5)|abundance(20)|weapon_length(90)|thrust_damage(36,pierce)|max_ammo(20),
 imodbits_missile,missile_distance_trigger, [fac_elf, fac_kingdom_4,fac_culture_4],
 ],
["stahlrim_arrow","stahlrim_arrow", [("stahlrimarrow",0),("flying_stahlrimarrow",ixmesh_flying_ammo),("stahlrimarrow_quiver", ixmesh_carry),("stahlrimarrow_quiver", ixmesh_inventory)], itp_can_penetrate_shield|itp_extra_penetration|itp_type_arrows, itcf_carry_quiver_back_right, 
 4500,weight(5)|abundance(5)|weapon_length(91)|max_ammo(20)|thrust_damage(54,pierce),
 imodbits_missile,missile_ice_trigger+missile_distance_trigger, [fac_elf, fac_kingdom_10, fac_scotland],
],
["ebony_arrow","ebony_arrow", [("ebonyarrow",0),("flying_ebonyarrow",ixmesh_flying_ammo),("ebonyarrow_quiver", ixmesh_carry),("ebonyarrow_quiver", ixmesh_inventory)], itp_can_penetrate_shield|itp_extra_penetration|itp_type_arrows, itcf_carry_quiver_back, 
 5000,weight(5)|abundance(5)|weapon_length(91)|max_ammo(20)|thrust_damage(60,pierce),
 imodbits_missile,missile_distance_trigger, 
 [fac_elf, fac_kingdom_5, fac_kingdom_7, fac_kingdom_3, fac_kingdom_10, fac_kingdom_8],
],
  #NEW
  
  
  
["flame_arrows","flame_arrows", [("arrows_h4",0),("huojian_fly",ixmesh_flying_ammo),("w_qui", ixmesh_carry),("w_qui", ixmesh_inventory)], itp_type_arrows, itcf_carry_quiver_back_right, 
 1500,weight(1.5)|weapon_length(91)|max_ammo(20)|thrust_damage(30,cut),
 imodbits_missile,missile_fire_trigger+missile_distance_trigger, arab_factions+ee_faction
],
["poison_arrows","flame_arrows", [("orcisharrow",0),("flying_orcisharrow",ixmesh_flying_ammo),("orcisharrow_quiver", ixmesh_carry),("orcisharrow_quiver", ixmesh_inventory)], itp_type_arrows, itcf_carry_quiver_back, 
 1500,weight(1.5)|weapon_length(91)|max_ammo(20)|thrust_damage(32,cut),
 imodbits_missile,missile_weak_poison_trigger+missile_distance_trigger, ee_faction
],


["evil_arrow_1","evil_arrows", [("nordheroarrow",0),("flying_nordheroarrow",ixmesh_flying_ammo),("nordicarrow_quiver", ixmesh_carry),("nordicarrow_quiver", ixmesh_inventory)], itp_type_arrows, itcf_carry_quiver_back_right, 
 124,weight(3)|abundance(70)|weapon_length(95)|thrust_damage(10,cut)|max_ammo(24),
 imodbits_missile,missile_distance_trigger, bow_factions
 ],

["holy_arrow","holy_arrows", [("elvenarrow",0),("flying_elvenarrow",ixmesh_flying_ammo),("elvenarrow_quiver", ixmesh_carry),("elvenarrow_quiver", ixmesh_inventory)], itp_type_arrows, itcf_carry_quiver_back_right, 
 124,weight(3)|abundance(70)|weapon_length(95)|thrust_damage(10,cut)|max_ammo(24),
 imodbits_missile,missile_distance_trigger, bow_factions
 ],


["evil_arrow_2","evil_arrows", [("poison_arrow_2",0),("poison_arrow_2_fl",ixmesh_flying_ammo)], itp_type_arrows|itp_is_magic_staff, 0, 
 10000,weight(1.5)|weapon_length(91)|max_ammo(20)|thrust_damage(35,cut),
 imodbits_missile,cast_magic_curse+missile_distance_trigger, bow_factions
],
["orcish_mutil_arrow","Orcish Mutil Arrows", [("orcisharrow",0),("flying_orcisharrow",ixmesh_flying_ammo),("orcisharrow_quiver", ixmesh_carry),("orcisharrow_quiver", ixmesh_inventory)], itp_type_arrows|itp_is_magic_staff, itcf_carry_quiver_back_right, 
  5000,weight(3.5)|abundance(50)|weapon_length(95)|thrust_damage(25,cut)|max_ammo(30),
  imodbits_missile,missile_distance_trigger, arab_factions+ee_faction
 ],
["stahlrim_mutil_arrow","Stahlrim Mutil_Arrow", [("stahlrimarrow",0),("flying_stahlrimarrow",ixmesh_flying_ammo),("stahlrimarrow_quiver", ixmesh_carry),("stahlrimarrow_quiver", ixmesh_inventory)], itp_can_penetrate_shield|itp_extra_penetration|itp_type_arrows|itp_is_magic_staff, itcf_carry_quiver_back_right, 
 15000,weight(5)|abundance(20)|weapon_length(91)|max_ammo(20)|thrust_damage(45,pierce),
 imodbits_missile,missile_ice_trigger+missile_distance_trigger, [fac_elf, fac_kingdom_10, fac_scotland],
],
["ebony_mutil_arrow","Ebony Mutil_Arrow", [("ebonyarrow",0),("flying_ebonyarrow",ixmesh_flying_ammo),("ebonyarrow_quiver", ixmesh_carry),("ebonyarrow_quiver", ixmesh_inventory)], itp_can_penetrate_shield|itp_extra_penetration|itp_type_arrows|itp_is_magic_staff, itcf_carry_quiver_back, 
 15000,weight(5)|abundance(20)|weapon_length(91)|max_ammo(20)|thrust_damage(50,pierce),
 imodbits_missile,missile_distance_trigger, 
 [fac_elf, fac_kingdom_5, fac_kingdom_7, fac_kingdom_3, fac_kingdom_10, fac_kingdom_8],
],
 
["mutil_arrow","mutil_arrow", [("elvenarrow",0),("flying_elvenarrow",ixmesh_flying_ammo),("elvenarrow_quiver", ixmesh_carry),("elvenarrow_quiver", ixmesh_inventory)], itp_type_arrows|itp_is_magic_staff, 0, 
 5000,weight(3)|abundance(70)|weapon_length(95)|thrust_damage(30,pierce)|max_ammo(24),
 imodbits_missile,missile_distance_trigger, [fac_elf, fac_forest_ranger, fac_kingdom_4]
 ],
  
["mutil_arrow_2","mutil_arrow", [("nordheroarrow",0),("flying_nordheroarrow",ixmesh_flying_ammo),("nordheroarrow_quiver", ixmesh_carry),("nordheroarrow_quiver", ixmesh_inventory)], itp_type_arrows|itp_is_magic_staff, 0, 
 5000,weight(3)|abundance(70)|weapon_length(95)|thrust_damage(36,pierce)|max_ammo(24),
 imodbits_missile,missile_distance_trigger, bow_factions
 ],
  
["woodelf_mutil_arrows", "Woodelf_mutil_Arrows", [("glassarrow", 0), ("flying_glassarrow", ixmesh_flying_ammo), ("glassarrow_quiver", ixmesh_carry),("glassarrow_quiver", ixmesh_inventory)], itp_merchandise|itp_type_arrows|itp_is_magic_staff, itcf_carry_quiver_back, 6000, weight(3)|weapon_length(91)|abundance(10)|thrust_damage(36, pierce)|max_ammo(30), imodbits_missile,missile_distance_trigger, [fac_kingdom_1,fac_kingdom_4] ],

["elven_arrows_fire", "Elven_Arrows", [("elvenarrow", 0), ("huojian_fly", ixmesh_flying_ammo), ("elvenarrow_quiver", ixmesh_carry),("elvenarrow_quiver", ixmesh_inventory)], itp_merchandise|itp_type_arrows|itp_is_magic_staff, itcf_carry_quiver_back, 8000, weight(3)|weapon_length(91)|abundance(10)|thrust_damage(36, pierce)|max_ammo(30), imodbits_missile ,missile_fire_2_trigger+missile_distance_trigger, [fac_elf, fac_forest_ranger]],

["woodelf_arrows_poison", "Woodelf_Arrows", [("ilithien_arrow", 0), ("ilithien_arrow_flying", ixmesh_flying_ammo), ("ithilien_quiver", ixmesh_carry),("ithilien_quiver", ixmesh_inventory)], itp_merchandise|itp_type_arrows|itp_is_magic_staff, itcf_carry_quiver_back_right, 6000, weight(3)|weapon_length(91)|abundance(10)|thrust_damage(38, pierce)|max_ammo(60), imodbits_missile,missile_poison_trigger+missile_distance_trigger, [fac_elf, fac_forest_ranger] ],

["woodelf_arrows_poison_2", "Woodelf_Arrows", [("glassarrow", 0), ("huojian_fly_green", ixmesh_flying_ammo), ("glassarrow_quiver", ixmesh_carry),("glassarrow_quiver", ixmesh_inventory)], itp_merchandise|itp_type_arrows|itp_is_magic_staff, itcf_carry_quiver_back_right, 10000, weight(3)|weapon_length(91)|abundance(10)|thrust_damage(38, pierce)|max_ammo(40), imodbits_missile,missile_power_poison_trigger+missile_distance_trigger, [fac_kingdom_8] ],

["elven_arrows_explove", "Elven_Arrows", [("elvenarrow", 0), ("flying_elvenarrow", ixmesh_flying_ammo), ("elvenarrow_quiver", ixmesh_carry),("elvenarrow_quiver", ixmesh_inventory)], itp_merchandise|itp_type_arrows|itp_is_magic_staff, itcf_carry_quiver_back_right, 12000, weight(3)|weapon_length(91)|abundance(10)|thrust_damage(25, pierce)|max_ammo(20), imodbits_missile ,missile_force_trigger+missile_distance_trigger, [fac_elf, fac_forest_ranger]],


["woodelf_arrows_freezing", "Woodelf_Arrows", [("stahlrimarrow", 0), ("guangjian_fly2", ixmesh_flying_ammo), ("stahlrimarrow_quiver", ixmesh_carry),("stahlrimarrow_quiver", ixmesh_inventory)], itp_merchandise|itp_type_arrows|itp_is_magic_staff, itcf_carry_quiver_back_right, 10000, weight(3)|weapon_length(91)|abundance(10)|thrust_damage(38, pierce)|max_ammo(25), imodbits_missile,missile_freezing_trigger+missile_distance_trigger, [fac_kingdom_10,fac_kingdom_1] ],
["sldequiver", "sldequiver", [("arrow",0),("huojian_fly",ixmesh_flying_ammo),("sldequiver",ixmesh_carry),("sldequiver", ixmesh_inventory)], itp_type_arrows|itp_can_penetrate_shield|itp_penalty_with_shield|itp_is_magic_staff, itcf_carry_quiver_back, 50000, weight(3)|abundance(160)|weapon_length(95)|thrust_damage(40,pierce)|max_ammo(1000), imodbits_missile,cast_magic_demon_arrow+missile_distance_trigger, [fac_kingdom_4,fac_kingdom_10]],
["demon_arrow","flame arrow", [("ebonyarrow",0),("guangjian_fly3",ixmesh_flying_ammo),("ebonyarrow_quiver",ixmesh_carry),("ebonyarrow_quiver", ixmesh_inventory)], itp_type_arrows|itp_is_magic_staff, itcf_carry_quiver_back, 
 15000,weight(1.5)|weapon_length(91)|max_ammo(20)|thrust_damage(60,pierce),
 imodbits_missile,cast_magic_demon_arrow+missile_distance_trigger, bow_factions],

 ["bolts", "Bolts", [("bolt",0),("flying_bolt",ixmesh_flying_ammo),("bolt_bag",ixmesh_carry),("bolt_bag", ixmesh_inventory)], itp_type_bolts|itp_default_ammo|itp_merchandise|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 
  64, weight(2.25)|abundance(90)|weapon_length(55)|thrust_damage(30,pierce)|max_ammo(20), 
  imodbits_missile,missile_distance_trigger , crossbow_factions
 ],
 ["steel_bolts", "Steel Bolts", [("bolt",0),("flying_bolt",ixmesh_flying_ammo),("bolt_bag_c",ixmesh_carry),("bolt_bag_c", ixmesh_inventory)], itp_type_bolts|itp_merchandise|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 
  210, weight(2.5)|abundance(20)|weapon_length(55)|thrust_damage(35,pierce)|max_ammo(20), 
  imodbits_missile,missile_distance_trigger , crossbow_factions
 ],
  ["swadian_steel_bolts", "Steel Bolts", [("bolt",0),("flying_bolt",ixmesh_flying_ammo),("bolt_bag_b",ixmesh_carry),("bolt_bag_b", ixmesh_inventory)], itp_type_bolts|itp_merchandise|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 
  210, weight(2.5)|abundance(20)|weapon_length(55)|thrust_damage(40,pierce)|max_ammo(20), 
  imodbits_missile,missile_distance_trigger , crossbow_factions
  ], 
  
 ["cartridges", "Cartridges", [("cartridge_a",0),("huojian_fly2",ixmesh_flying_ammo),("bag_ppb1",ixmesh_carry),("cartridge", ixmesh_inventory)], itp_type_bullets|itp_default_ammo|itp_merchandise|itp_covers_legs, itcf_carry_bow_back,
  150, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(60,cut)|max_ammo(30),
  imodbits_missile, missile_distance_trigger+bullet_dust_trigger , firearm_factions
 ],
 ["cartridges_2", "Cartridges", [("cartridge_a",0),("huojian_fly2",ixmesh_flying_ammo),("bag_c",ixmesh_carry),("cartridges", ixmesh_inventory)], itp_type_bullets|itp_merchandise|itp_covers_legs, itcf_carry_kite_shield,
  275, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(60,cut)|max_ammo(60),
  imodbits_missile, missile_distance_trigger+bullet_dust_trigger , firearm_factions
 ],
 
 ["cartridges_cannon", "Cartridges", [("minie_ball",0),("musket_balls",ixmesh_flying_ammo),("bag_ppa1",ixmesh_carry)], itp_type_bullets|itp_merchandise|itp_can_penetrate_shield|itp_bonus_against_shield|itp_covers_legs, itcf_carry_bow_back,
  20000, weight(2.25)|abundance(30)|weapon_length(3)|thrust_damage(100,pierce)|max_ammo(20), 
  imodbits_missile, powergun_trigger3+missile_distance_trigger , firearm_factions
 ],
 
 ["cartridges_cannon_1", "Cartridges", [("minie_ball",0),("musket_balls",ixmesh_flying_ammo),("bag_ppa1",ixmesh_carry)], itp_type_bullets|itp_merchandise|itp_can_penetrate_shield|itp_bonus_against_shield|itp_covers_legs, itcf_carry_bow_back,
  25000, weight(2.25)|abundance(30)|weapon_length(3)|thrust_damage(150,pierce)|max_ammo(15), 
  imodbits_missile, powergun_trigger2+missile_distance_trigger , firearm_factions
 ],
 ["cartridges_cannon_2", "Cartridges", [("minie_ball",0),("musket_balls",ixmesh_flying_ammo),("bag_ppa1",ixmesh_carry)], itp_type_bullets|itp_merchandise|itp_can_penetrate_shield|itp_bonus_against_shield|itp_covers_legs, itcf_carry_bow_back,
  25000, weight(2.25)|abundance(30)|weapon_length(3)|thrust_damage(100,pierce)|max_ammo(10), 
  imodbits_missile, powergun_trigger+missile_distance_trigger , firearm_factions
 ],
 
 ["cartridges_thrust", "Cartridges", [("bullet_2",0),("huojian_fly2",ixmesh_flying_ammo),("bag_a",ixmesh_carry)], itp_type_bullets|itp_merchandise|itp_can_penetrate_shield|itp_bonus_against_shield|itp_covers_legs, itcf_carry_quiver_back,
  150, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(80,pierce)|max_ammo(30), 
  imodbits_missile, missile_distance_trigger+bullet_dust_trigger , firearm_factions
 ],
 ["cartridges_burst", "Cartridges", [("musket_balls",0),("huojian_fly2",ixmesh_flying_ammo),("bag_a",ixmesh_carry),("cartridges", ixmesh_inventory)], itp_type_bullets|itp_merchandise|itp_covers_legs, itcf_carry_quiver_back, 
  275, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(40,cut)|max_ammo(15), 
  imodbits_missile, missile_distance_trigger+bullet_dust_trigger , firearm_factions
 ],

 ["cartridges_dummy", "Cartridges", [("cartridge_a",0),("huojian_fly2",ixmesh_flying_ammo)], itp_type_bullets|itp_no_pick_up_from_ground, itcf_carry_quiver_front_right,
  0, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(30,cut)|max_ammo(1),
  imodbits_missile, bullet_dust_trigger , firearm_factions
 ],

["pilgrim_disguise", "Pilgrim Disguise", [("raylin_pilgrim",0)], 0| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 25 , weight(2)|abundance(100)|head_armor(0)|body_armor(19)|leg_armor(8)|difficulty(0) ,imodbits_cloth , [], euro_factions],
["pilgrim_hood", "Pilgrim Hood", [("raylin_pilgrim_hood",0)], 0| itp_type_head_armor|itp_civilian  ,0, 35 , weight(1.25)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth , [], euro_factions],

# ARMOR
#handwear

["leather_gloves","Leather Gloves", [("glove4_L",0)], itp_merchandise|itp_type_hand_armor|itp_civilian,0, 
 50, weight(0.25)|abundance(120)|body_armor(2)|difficulty(0),imodbits_cloth, 
 [], all_factions],
["mail_mittens","Mail Mittens", [("glove3_L",0)], itp_merchandise|itp_type_hand_armor,0, 
 370, weight(0.5)|abundance(100)|body_armor(6)|difficulty(0),imodbits_armor, 
 [], euro_factions],
["scale_gauntlets","Scale Gauntlets", [("glove5_L",0)], itp_merchandise|itp_type_hand_armor,0, 
 820, weight(1)|abundance(100)|body_armor(9)|difficulty(0),imodbits_armor, 
 [], ee_faction+arab_factions],
["lamellar_gauntlets","Lamellar Gauntlets", [("glove6_L",0)], itp_merchandise|itp_type_hand_armor,0, 
 1010, weight(1.75)|abundance(100)|body_armor(10)|difficulty(0),imodbits_armor, 
 [], ee_faction+arab_factions],
["gauntlets","Gauntlets", [("gauntlets_L",0)], itp_merchandise|itp_type_hand_armor,0, 
 1010, weight(1.25)|abundance(100)|body_armor(10)|difficulty(0),imodbits_armor, 
 [] , [fac_kingdom_13]],
["bnw_gauntlets","Gauntlets", [("bnw_gauntlet_L",0)], itp_merchandise|itp_type_hand_armor,0, 
 1010, weight(1.25)|abundance(100)|body_armor(10)|difficulty(0),imodbits_armor, 
 [] , [fac_kingdom_7,fac_kingdom_1,fac_kingdom_11]],

["wisby_gauntlets_black","Gauntlets", [("wisby_gauntlets_black_L",0)], itp_merchandise|itp_type_hand_armor,0, 
 820, weight(1)|abundance(100)|body_armor(9)|difficulty(0),imodbits_armor, 
 [] , we_faction+se_faction],
["plate_mittens","Gauntlets", [("plate_mittens_L",0)], itp_merchandise|itp_type_hand_armor,0, 
 1010, weight(1.25)|abundance(100)|body_armor(10)|difficulty(0),imodbits_armor, 
 [], ne_faction],

["milanese_gauntlets","Gauntlets", [("milanese_gauntlet_L",0)], itp_merchandise|itp_type_hand_armor,0, 
 1010, weight(1.25)|abundance(100)|body_armor(10)|difficulty(0),imodbits_armor, 
 [] , se_faction],
["hourglass_gauntlets","Gauntlets", [("hourglass_gauntlets_L",0)], itp_merchandise|itp_type_hand_armor,0,
 1010, weight(1.25)|abundance(100)|body_armor(10)|difficulty(0),imodbits_armor, 
 [] , we_faction+se_faction],
["hourglass_gauntlets_ornate","Gauntlets", [("hourglass_gauntlets_ornate_L",0)], itp_merchandise|itp_type_hand_armor,0, 
 1450, weight(1.25)|abundance(100)|body_armor(12)|difficulty(0),imodbits_armor, 
 [] , we_faction],
["gondor_gauntlets","gondor Gauntlets", [("gondor_gloves2_L",0)], itp_merchandise|itp_type_hand_armor,0, 
 1010, weight(1.25)|abundance(100)|body_armor(10)|difficulty(0),imodbits_armor, 
 [] , [fac_kingdom_1,fac_hospitalier_knights]],
["maximilian_gauntlets","Maximilian Gauntlets", [("glove1_L",0)], itp_merchandise|itp_type_hand_armor,0, 
 1450, weight(1.25)|abundance(100)|body_armor(13)|difficulty(0),imodbits_armor, 
 [], [fac_kingdom_7]],

#footwear
["wrapping_boots", "Wrapping Boots", [("wrapping_boots_a",0)], itp_merchandise| itp_type_foot_armor|itp_civilian| itp_attach_armature ,0, 
 216 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(3)|difficulty(0) ,imodbits_cloth , 
 [], [fac_kingdom_4,fac_kingdom_13,fac_kingdom_6,fac_kingdom_8]],
["woolen_hose", "Woolen Hose", [("boot14_r",0)], itp_merchandise| itp_type_foot_armor|itp_civilian| itp_attach_armature ,0, 
 140 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(2)|difficulty(0) ,imodbits_cloth, 
 [], [fac_kingdom_4,fac_kingdom_5,fac_kingdom_7,fac_kingdom_8,fac_kingdom_10,fac_kingdom_11,fac_kingdom_13,fac_kingdom_1,fac_kingdom_2,fac_kingdom_3]],
["blue_hose", "Blue Hose", [("boot14",0)], itp_merchandise| itp_type_foot_armor|itp_civilian| itp_attach_armature ,0, 
 140 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(2)|difficulty(0) ,imodbits_cloth , 
 [], [fac_kingdom_4,fac_kingdom_5,fac_kingdom_7,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_13,fac_kingdom_1]],
["hunter_boots", "Hunter Boots", [("boot18",0)], itp_merchandise| itp_type_foot_armor|itp_civilian| itp_attach_armature,0, 
 648 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(9)|difficulty(0) ,imodbits_cloth, 
 [], [fac_kingdom_8]],
["hide_boots", "Hide Boots", [("boot6",0)], itp_merchandise| itp_type_foot_armor|itp_civilian| itp_attach_armature,0, 
 576 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth,
 [], [fac_kingdom_5,fac_kingdom_8,fac_kingdom_9,fac_kingdom_10,fac_kingdom_1,fac_kingdom_2,fac_kingdom_3]],
["ankle_boots", "Ankle Boots", [("boot15",0)], itp_merchandise| itp_type_foot_armor|itp_civilian| itp_attach_armature,0, 
 432 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth , 
 [], [fac_kingdom_4,fac_kingdom_5,fac_kingdom_7,fac_kingdom_8,fac_kingdom_13,fac_kingdom_1,fac_kingdom_2]],
["nomad_boots", "Nomad Boots", [("boot17",0)], itp_merchandise| itp_type_foot_armor|itp_civilian| itp_attach_armature,0, 
 576 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth , 
 [], [fac_kingdom_4,fac_kingdom_5,fac_kingdom_6,fac_kingdom_8,fac_kingdom_9,fac_kingdom_10,fac_kingdom_11,fac_kingdom_12,fac_kingdom_13,fac_kingdom_2,fac_kingdom_3]],
["leather_boots", "Leather Boots", [("boot7",0)], itp_merchandise| itp_type_foot_armor|itp_civilian| itp_attach_armature,0, 
 750 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth , 
 [], all_factions],
["splinted_leather_greaves", "Splinted Leather Greaves", [("boot4",0)], itp_merchandise| itp_type_foot_armor| itp_attach_armature,0, 
 1728 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(24)|difficulty(0) ,imodbits_armor , 
 [], all_factions],
["mail_chausses", "Mail Chausses", [("boot16",0)], itp_merchandise| itp_type_foot_armor| itp_attach_armature  ,0, 
 1872 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(26)|difficulty(0) ,imodbits_armor ,
 [], euro_factions],
["mail_boots", "Mail Boots", [("boot9",0)], itp_merchandise| itp_type_foot_armor| itp_attach_armature  ,0, 
 2016 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(7) ,imodbits_armor, 
 [], euro_factions],

["rus_shoes", "Rus Ankle Boots", [("rus_shoes",0)], itp_merchandise| itp_type_foot_armor|itp_civilian| itp_attach_armature,0, 
 936 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(13)|difficulty(0) ,imodbits_cloth, 
 [], ee_faction],
["rus_cav_boots", "Rus Cavalry Boots", [("rus_cav_boots",0)], itp_merchandise| itp_type_foot_armor|itp_civilian| itp_attach_armature ,0, 
 2376 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(0) ,imodbits_cloth, 
 [], ee_faction],

["rus_splint_greaves", "Splinted Greaves", [("rus_splint_greaves",0)], itp_merchandise| itp_type_foot_armor| itp_attach_armature,0, 
 2592 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(36)|difficulty(8) ,imodbits_plate , 
 [], ee_faction],

["cav_boots", "Rus Cavalry Boots", [("high_boots_cav",0)], itp_merchandise| itp_type_foot_armor|itp_civilian| itp_attach_armature ,0, 
 2016 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(0) ,imodbits_cloth, 
 [], we_faction],
["splinted_greaves", "Splinted Greaves", [("boot11",0)], itp_merchandise| itp_type_foot_armor| itp_attach_armature,0, 
 2520 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(35)|difficulty(7) ,imodbits_armor , 
 [], we_faction],
["bnw_splinted_greaves", "Splinted Greaves", [("splinted_greaves_nospurs",0)], itp_merchandise| itp_type_foot_armor| itp_attach_armature,0, 
 2520 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(35)|difficulty(7) ,imodbits_armor , 
 [], [fac_kingdom_7,fac_kingdom_1,fac_kingdom_11]],

["iron_greaves", "Iron Greaves", [("boot12",0)], itp_merchandise| itp_type_foot_armor| itp_attach_armature,0, 
 2664 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(37)|difficulty(9) ,imodbits_armor , 
 [], euro_factions],
["iron_greaves2", "Iron Greaves", [("boot10",0)], itp_merchandise| itp_type_foot_armor| itp_attach_armature,0, 
 2664 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(37)|difficulty(9) ,imodbits_armor , 
 [], euro_factions],
["steel_greaves", "Plate Boots", [("boot3",0)], itp_merchandise| itp_type_foot_armor| itp_attach_armature,0,
 2664 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(37)|difficulty(9) ,imodbits_armor , 
 [], euro_factions],
["plate_boots", "Plate Boots", [("boot1",0)], itp_merchandise| itp_type_foot_armor| itp_attach_armature,0, 
 2664 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(37)|difficulty(9) ,imodbits_armor , 
 [], euro_factions],

["maximilian_greaves", "Maximilian Greaves", [("boot5",0)], itp_type_foot_armor|itp_attach_armature, 0, 
 2880, weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(40)|difficulty(9), imodbits_good_plate,
 [], [fac_kingdom_7]],

["black_greaves", "Black Greaves", [("black_greaves",0)], itp_type_foot_armor|itp_attach_armature, 0, 
 2880, weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(40)|difficulty(9), imodbits_good_plate
 ],
["black_greaves2", "Black Greaves", [("hm_boo_masW",0)], itp_type_foot_armor|itp_attach_armature, 0, 
 2880, weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(40)|difficulty(9), imodbits_good_plate, [], [fac_demon_hunters, fac_hospitalier_knights] ],
 
["narf_hose", "Woolen Hose", [("narf_hose",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 140 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth ,
 [], euro_factions],
["hose_kneecops_red", "Woolen Hose with Kneecops", [("hose_kneecops_red",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 1650 , weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(6) ,imodbits_cloth ,
 [], euro_factions],
["hose_kneecops_green", "Woolen Hose with Kneecops", [("hose_kneecops_green",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 1650 , weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(6) ,imodbits_cloth ,
 [], euro_factions], 
 
["khergit_leather_boots", "Khergit Leather Boots", [("boot8",0)], itp_merchandise| itp_type_foot_armor|itp_civilian| itp_attach_armature ,0, 
 1008 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(14)|difficulty(0) ,imodbits_cloth , 
 [], tatar_faction],
["sarranid_boots_a", "Sarranid Shoes", [("boot13",0)], itp_type_foot_armor|itp_civilian| itp_attach_armature ,0, 
 576 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth,
  [], arab_factions],
["sarranid_boots_b", "Sarranid Leather Boots", [("sarranid_boots",0)], itp_merchandise| itp_type_foot_armor|itp_civilian| itp_attach_armature ,0,
 1008 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(14)|difficulty(0) ,imodbits_cloth, 
 [], arab_factions],
["sarranid_boots_c", "Plated Boots", [("sarranid_camel_boots",0)], itp_merchandise| itp_type_foot_armor|itp_civilian| itp_attach_armature ,0,
 1728 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(24)|difficulty(0) ,imodbits_plate, 
 [], arab_factions],
["sarranid_boots_d", "Sarranid Mail Boots", [("sarranid_mail_chausses",0)], itp_merchandise|itp_type_foot_armor|itp_civilian|itp_attach_armature ,0, 
 2520 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(35)|difficulty(0) ,imodbits_armor, 
[], arab_factions],


["sarranid_head_cloth", "Lady Head Cloth", [("tulbent",0)],  itp_type_head_armor| itp_doesnt_cover_hair|itp_civilian|itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth],
["sarranid_head_cloth_b", "Lady Head Cloth", [("tulbent_b",0)],  itp_type_head_armor| itp_doesnt_cover_hair|itp_civilian|itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["sarranid_felt_head_cloth", "Head Cloth", [("common_tulbent",0)],  itp_type_head_armor|itp_civilian|itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["sarranid_felt_head_cloth_b", "Head Cloth", [("common_tulbent_b",0)],  itp_type_head_armor|itp_civilian|itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth],


#bodywear
["lady_dress_ruby", "Lady Dress", [("lady_dress_r",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 100,cloth_tier_1,imodbits_cloth],
["lady_dress_green", "Lady Dress", [("lady_dress_g",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 100,cloth_tier_1,imodbits_cloth],
["lady_dress_blue", "Lady Dress", [("lady_dress_b",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 100,cloth_tier_1,imodbits_cloth],
["red_dress", "Red Dress", [("red_dress",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 100,cloth_tier_1,imodbits_cloth],
["brown_dress", "Brown Dress", [("brown_dress",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 100,cloth_tier_1,imodbits_cloth],
["green_dress", "Green Dress", [("green_dress",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 100,cloth_tier_1,imodbits_cloth],
["khergit_lady_dress", "Khergit Lady Dress", [("khergit_lady_dress",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 100,cloth_tier_1,imodbits_cloth],
["khergit_lady_dress_b", "Khergit Leather Lady Dress", [("khergit_lady_dress_b",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 100,cloth_tier_1,imodbits_cloth],
["sarranid_lady_dress", "Sarranid Lady Dress", [("sarranid_lady_dress",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 100,cloth_tier_1,imodbits_cloth],
["sarranid_lady_dress_b", "Sarranid Lady Dress", [("sarranid_lady_dress_b",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 100,cloth_tier_1,imodbits_cloth],
["sarranid_common_dress", "Sarranid Dress", [("sarranid_common_dress",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 100,cloth_tier_1,imodbits_cloth],
["sarranid_common_dress_b", "Sarranid Dress", [("sarranid_common_dress_b",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 100,cloth_tier_1,imodbits_cloth],
["courtly_outfit", "Courtly Outfit", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 100,cloth_tier_1,imodbits_cloth],
["nobleman_outfit", "Nobleman Outfit", [("nobleman_outfit_b_new",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 100,cloth_tier_4,imodbits_cloth ],


["nomad_armor", "Nomad Armor", [("nomad_armor_new",0)], itp_type_body_armor|itp_covers_legs   ,0, 100,cloth_tier_1,imodbits_cloth, [], [fac_kingdom_8]],
["khergit_armor", "Khergit Armor", [("khergit_armor_new",0)], itp_type_body_armor|itp_covers_legs ,0, 100,cloth_tier_1,imodbits_cloth, [], [fac_kingdom_3]],
["leather_jacket", "Leather Jacket", [("leather_jacket_new",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 100,cloth_tier_1,imodbits_cloth ],
#NEW:
["rawhide_coat", "Rawhide Coat", [("thick_coat_a",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 100,cloth_tier_1,imodbits_cloth , [], [fac_kingdom_8,fac_kingdom_5]],
#NEW: was lthr_armor_a
["leather_armor", "Leather Armor", [("tattered_leather_armor_a",0)], itp_type_body_armor|itp_covers_legs  ,0, 100,cloth_tier_1,imodbits_cloth , [], [fac_kingdom_1,fac_kingdom_5]],
["fur_coat", "Fur Coat", [("fur_coat",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 100,cloth_tier_1,imodbits_cloth],



#for future:
#["coat", "Coat", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 100,cloth_tier_1,imodbits_cloth],
#["leather_coat", "Leather Coat", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 100,cloth_tier_1,imodbits_cloth],
#["mail_coat", "Coat of Mail", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 100,cloth_tier_1,imodbits_cloth],
#["long_mail_coat", "Long Coat of Mail", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 100,cloth_tier_1,imodbits_cloth],
#["mail_with_tunic_red", "Mail with Tunic", [("arena_armorR_new",0)], itp_type_body_armor|itp_covers_legs ,0, 795 , weight(17)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(25)|difficulty(7) ,imodbits_armor],
#["mail_with_tunic_green", "Mail with Tunic", [("arena_armorG_new",0)], itp_type_body_armor|itp_covers_legs ,0, 795 , weight(17)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(25)|difficulty(7) ,imodbits_armor],
#["hide_coat", "Hide Coat", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 100,cloth_tier_1,imodbits_cloth],
#["merchant_outfit", "Merchant Outfit", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 100,cloth_tier_1,imodbits_cloth],
#["homespun_dress", "Homespun Dress", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 100,cloth_tier_1,imodbits_cloth],
#["thick_coat", "Thick Coat", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 100,cloth_tier_1,imodbits_cloth],
#["coat_with_cape", "Coat with Cape", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 100,cloth_tier_1,imodbits_cloth],
#["steppe_outfit", "Steppe Outfit", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 100,cloth_tier_1,imodbits_cloth],
#["nordic_outfit", "Nordic Outfit", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 100,cloth_tier_1,imodbits_cloth],
#["nordic_armor", "Nordic Armor", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 100,cloth_tier_1,imodbits_cloth],
#["hide_armor", "Hide Armor", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 100,cloth_tier_1,imodbits_cloth],
#["cloaked_tunic", "Cloaked Tunic", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 100,cloth_tier_1,imodbits_cloth],
#["sleeveless_tunic", "Sleeveless Tunic", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 100,cloth_tier_1,imodbits_cloth],
#["sleeveless_leather_tunic", "Sleeveless Leather Tunic", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 100,cloth_tier_1,imodbits_cloth],
#["linen_shirt", "Linen Shirt", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 100,cloth_tier_1,imodbits_cloth],
#["wool_coat", "Wool Coat", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 100,cloth_tier_1,imodbits_cloth],
#end

["dress", "Dress", [("dress",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 50,cloth_tier_0,imodbits_cloth ],
["blue_dress", "Blue Dress", [("blue_dress_new",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 50,cloth_tier_0,imodbits_cloth ],
["peasant_dress", "Peasant Dress", [("peasant_dress_b_new",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 50,cloth_tier_0,imodbits_cloth],
["woolen_dress", "Woolen Dress", [("woolen_dress",0)], itp_merchandise| itp_type_body_armor|itp_civilian|itp_covers_legs ,0, 50,cloth_tier_0,imodbits_cloth ],
["shirt", "Shirt", [("shirt",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 50,cloth_tier_0,imodbits_cloth ],
#NEW: was "linen_tunic"
["linen_tunic", "Linen Tunic", [("shirt_a",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 50,cloth_tier_0,imodbits_cloth, [], [fac_kingdom_2]],
#NEW was cvl_costume_a
["short_tunic", "Red Tunic", [("rich_tunic_a",0)], itp_type_body_armor|itp_civilian|itp_covers_legs ,0, 50,cloth_tier_0,imodbits_cloth ],
#TODO:
["red_shirt", "Red Shirt", [("rich_tunic_a",0)], merc_body_armor|itp_civilian ,0, 50,cloth_tier_0,imodbits_cloth, [], [fac_kingdom_1]],
["red_tunic", "Red Tunic", [("arena_tunicR_new",0)], merc_body_armor|itp_civilian ,0, 50,cloth_tier_0,imodbits_cloth, [], [fac_kingdom_1]],

["green_tunic", "Green Tunic", [("arena_tunicG_new",0)], merc_body_armor|itp_civilian ,0, 50,cloth_tier_0,imodbits_cloth , [], [fac_kingdom_5]],
["blue_tunic", "Blue Tunic", [("arena_tunicB_new",0)], merc_body_armor|itp_civilian ,0, 50,cloth_tier_0,imodbits_cloth, [], [fac_kingdom_10,fac_kingdom_4]],
["robe", "Robe", [("robe",0)], merc_body_armor|itp_civilian,0, 100,cloth_tier_1,imodbits_cloth],


["coarse_tunic", "Tunic with vest", [("coarse_tunic_a",0)], merc_body_armor|itp_civilian ,0, 100,cloth_tier_1,imodbits_cloth , [], [fac_kingdom_10]],
["leather_apron", "Leather Apron", [("leather_apron",0)], merc_body_armor|itp_civilian ,0, 100,cloth_tier_1,imodbits_cloth],
#NEW: was tabard_a
["tabard", "Tabard", [("tabard_b",0)], merc_body_armor|itp_civilian,0, 100,cloth_tier_1,imodbits_cloth ],
#NEW: was leather_vest

["leather_vest", "Leather Vest", [("leather_vest_a",0)], merc_body_armor|itp_civilian ,0, 100,cloth_tier_1,imodbits_cloth, [], [fac_kingdom_8,fac_kingdom_3]],
["steppe_armor", "Steppe Armor", [("lamellar_leather",0)], merc_body_armor ,0, 300,cloth_tier_2,imodbits_cloth, [], tatar_faction],
["gambeson", "Gambeson", [("white_gambeson_kovas",0)], merc_body_armor|itp_civilian,0, 300,cloth_tier_2,imodbits_cloth, [], [fac_kingdom_1]],
["blue_gambeson", "Blue Gambeson", [("gondor_noble_cloak",0)], merc_body_armor|itp_civilian,0, 300,cloth_tier_2,imodbits_cloth, [], [fac_kingdom_1]],
#NEW: was red_gambeson
["red_gambeson", "Red Gambeson", [("red_gambeson_a",0)], merc_body_armor|itp_civilian,0, 300,cloth_tier_2,imodbits_cloth, [], [fac_kingdom_4,fac_kingdom_8]],

["yellow_gambeson", "German Gambeson", [("german_gambeson_a",0)], merc_body_armor|itp_civilian,0, 300,cloth_tier_2,imodbits_cloth, [], [fac_kingdom_7]],
["green_gambeson", "German Gambeson", [("green_gambeson_a",0)], merc_body_armor|itp_civilian,0, 300,cloth_tier_2,imodbits_cloth, [], [fac_kingdom_5]],


#NEW: was aketon_a
["padded_cloth", "gondor_jerkin", [("gondor_jerkin",0)], merc_body_armor ,0, 940,cloth_tier_3,imodbits_cloth, [], [fac_kingdom_1]],
["teu_padded_cloth", "Aketon", [("dol_padded_coat",0)], merc_body_armor ,0, 940,cloth_tier_3,imodbits_cloth, [], [fac_kingdom_1]],

#NEW:
["aketon_green", "Padded Cloth", [("padded_cloth_b",0)], merc_body_armor ,0, 940,cloth_tier_3,imodbits_cloth, [], [fac_kingdom_5]],
#NEW: was "leather_jerkin"
["leather_jerkin", "Leather Jerkin", [("armor15",0)], merc_body_armor|itp_civilian ,0, 300,cloth_tier_2,imodbits_cloth , [], [fac_kingdom_1]],
["nomad_vest", "Nomad Vest", [("nomad_vest_new",0)], merc_body_armor|itp_civilian ,0, 300,cloth_tier_2,imodbits_cloth , [], [fac_kingdom_4]],
["ragged_outfit_high", "Ragged Outfit", [("ragged_outfit_highc",0)], merc_body_armor|itp_civilian ,0, 100,cloth_tier_1,imodbits_cloth , [], [fac_kingdom_4]],
["ragged_outfit", "Ragged Outfit", [("ragged_outfit_a_new",0)], merc_body_armor|itp_civilian ,0, 300,cloth_tier_2,imodbits_cloth , [], [fac_kingdom_5]],
["ragged_outfit_high2", "Ragged Outfit", [("ragged_outfit_b",0)], merc_body_armor|itp_civilian ,0, 940,cloth_tier_3,imodbits_cloth],
#NEW: was padded_leather
#["padded_leather", "Padded Leather", [("leather_armor_b",0)], merc_body_armor|itp_civilian,0, 940,cloth_tier_3,imodbits_cloth, [], [fac_kingdom_4]],
["padded_leather", "Padded Leather", [("armor22",0)], merc_body_armor|itp_civilian,0, 2704,mail_armor_tier_2,imodbits_cloth, [], [fac_kingdom_4]],

["tribal_warrior_outfit", "Tribal Warrior Outfit", [("tribal_warrior_outfit_a_new",0)], merc_body_armor|itp_civilian ,0, 1722,cloth_tier_4,imodbits_cloth, [], [fac_kingdom_3]],
["nomad_robe", "Nomad Robe", [("nomad_robe_a",0)], merc_body_armor|itp_civilian,0, 1722,cloth_tier_4,imodbits_cloth, [], [fac_kingdom_3]],

["pelt_coat", "Pelt Coat", [("coat_of_plates_b",0)],  merc_body_armor ,0, 1722,cloth_tier_4,imodbits_cloth , [], [fac_kingdom_8]],

#NEW: was "std_lthr_coat"
#["studded_leather_coat", "Studded Leather Coat", [("leather_armor_a",0)], merc_body_armor ,0, 1722,mail_armor_tier_1,imodbits_armor , [], [fac_kingdom_4]],
["studded_leather_coat", "Studded Leather Coat", [("armor21",0)], merc_body_armor ,0, 5256,mail_armor_tier_4,imodbits_armor , [], [fac_kingdom_4]],



["rus_robe", "Robe", [("Pol_svitka_pure_b",0)], merc_body_armor|itp_civilian,0, 100,cloth_tier_1,imodbits_cloth, [], [fac_kingdom_8]],
["rus_robe_2", "Robe", [("Pol_svitka_rich_a",0)], merc_body_armor|itp_civilian,0, 300,cloth_tier_2,imodbits_cloth, [], [fac_kingdom_8]],

["kaftan", "kaftan", [("drz_kaftan",0)], merc_body_armor|itp_civilian,0, 940,cloth_tier_3,imodbits_cloth, [], [fac_kingdom_8]],
["kaftan_over_mail", "Kaftan_over_Mail", [("kaftan_over_mail", 0)], merc_body_armor, 0, 2704,mail_armor_tier_2, imodbits_armor, [], [fac_kingdom_8]],


["red_pikiner_uniform", "Hajduk Uniform", [("mosk_streletz_spear",0)], merc_body_armor ,0, 1722,mail_armor_tier_1 ,imodbits_cloth, [], [fac_kingdom_8]],
["red_pikiner_uniform_2", "Hajduk Uniform", [("mosk_new_line_pikeman",0)], merc_body_armor ,0, 2704,mail_armor_tier_2 ,imodbits_cloth, [], [fac_kingdom_8]],
["poland_dragoon_coat", "Studded Leather Coat", [("poland_dragoon",0)], merc_body_armor ,0, 4035,mail_armor_tier_3,imodbits_armor , [], [fac_kingdom_8]],
["breastplate_polish", "breastplate", [("moskow_reytar",0)], merc_body_armor,0, 5738,breastplate_tier_3,imodbits_plate , [], [fac_kingdom_8]],

["heraldic_gambeson", "heraldic_gambeson", [("heraldic_armor_new_c",0)], merc_body_armor, 0, 1722,mail_armor_tier_1,imodbits_armor,  [(ti_on_init_item,[(store_trigger_param_1,":agent_no"),(store_trigger_param_2,":troop_no"),(call_script,"script_shield_item_set_banner","tableau_heraldic_armor_c",":agent_no",":troop_no")])] ],

["aketon", "Aketon", [("aketon",0)], merc_body_armor|itp_civilian,0, 940 , cloth_tier_3 ,imodbits_cloth , [], euro_factions],

["light_brigandine_red", "Brigandine", [("brigandine_red",0)], merc_body_armor,0, 2704,mail_armor_tier_2 ,imodbits_armor, [], [fac_kingdom_4]],
["light_brigandine_green", "Brigandine", [("brigandine_green",0)], merc_body_armor,0, 2704,mail_armor_tier_2 ,imodbits_armor, [], [fac_kingdom_5]],
["light_brigandine_blue", "Brigandine", [("brigandine_blue",0)], merc_body_armor,0, 2704,mail_armor_tier_2 ,imodbits_armor, [], [fac_kingdom_1,fac_kingdom_10]],
["light_brigandine_yellow", "Brigandine", [("brigandine_yellow",0)], merc_body_armor,0, 2704,mail_armor_tier_2 ,imodbits_armor, [], [fac_kingdom_7]],
["light_brigandine_black", "Brigandine", [("brigandine_black",0)], merc_body_armor,0, 2704,mail_armor_tier_2 ,imodbits_armor, [], [fac_kingdom_1]],

["mail_shirt", "Mail Shirt", [("mail_shirt_a1",0)], merc_body_armor ,0, 2704,mail_armor_tier_2,imodbits_armor , [], ne_faction],
["mail_with_tunic_red", "Mail with Tunic", [("arena_armorR_new",0)], merc_body_armor ,0, 2704,mail_armor_tier_2,imodbits_armor],
["mail_with_tunic_green", "Mail with Tunic", [("arena_armorG_new",0)], merc_body_armor ,0, 2704,mail_armor_tier_2,imodbits_armor],
["gon_footman", "Gondor_Mail_Shirt", [("gondor_footman",0)],merc_body_armor ,0, 2704,mail_armor_tier_2,imodbits_armor, [], [fac_kingdom_1]],
["gon_squire", "Gondor_Mail_with_Cloak", [("gondor_squire",0)], merc_body_armor ,0, 2704,mail_armor_tier_2,imodbits_armor, [], [fac_kingdom_1]],

["ranger_armor1", "Ranger's_Traveller_Outfit", [("armor9", 0)], itp_type_body_armor|itp_covers_legs, 0, 1722,cloth_tier_4, imodbits_armor], 

["armor7", "Leather_Outfit", [("light_leather_new", 0)],merc_body_armor, 0, 940, weight(4)|abundance(50)|head_armor(0)|body_armor(25)|leg_armor(14)|difficulty(4),imodbits_armor , [], euro_factions], 
["armor8", "Assasin's_Outfit", [("armor8", 0)], merc_body_armor, 0, 1722,weight(4)|abundance(60)|head_armor(0)|body_armor(31)|leg_armor(14)|difficulty(5), imodbits_armor , [], euro_factions], 
["armor9", "ranger_leather_armor", [("armor31", 0)], merc_body_armor, 0, 2704, weight(8)|abundance(65)|head_armor(0)|body_armor(41)|leg_armor(17)|difficulty(8),imodbits_armor , [], euro_factions], 

#["mail_with_tunic_polish", "Mail with Tunic", [("polish_panzernik",0)], merc_body_armor ,0, 2704,mail_armor_tier_2,imodbits_armor, [], [fac_kingdom_2]],
#["teu_mail_with_tunic_1", "Mail with Tunic", [("teutonic_grey_mail",0)],merc_body_armor ,0, 2704,mail_armor_tier_2,imodbits_armor, [], [fac_kingdom_13]],
#["teu_mail_with_tunic_2", "Mail with Tunic", [("teutonic_white_mail",0)],merc_body_armor,0,2704,mail_armor_tier_2,imodbits_armor, [], [fac_kingdom_13]],




["heraldic_mail", "heraldic_mail", [("heraldic_armor_new_b",0)], merc_body_armor, 0, 2704,mail_armor_tier_2,imodbits_armor,  [(ti_on_init_item,[(store_trigger_param_1,":agent_no"),(store_trigger_param_2,":troop_no"),(call_script,"script_shield_item_set_banner","tableau_heraldic_armor_b",":agent_no",":troop_no")])] , [fac_kingdom_4]],

["byrnie", "Byrnie", [("byrnie_a_new",0)], merc_body_armor ,0, 2704,mail_armor_tier_2,imodbits_armor, [], ne_faction],
["byrnie_1", "Byrnie", [("dejawolf_vikingbyrnie",0)], merc_body_armor ,0, 4035, mail_armor_tier_3,imodbits_armor, [], ne_faction],
["byrnie_2", "Byrnie", [("dejawolf_vikingbyrnie_h1",0)], merc_body_armor ,0, 4035, mail_armor_tier_3,imodbits_armor, [], ne_faction],
["byrnie_3", "Byrnie", [("dejawolf_vikingbyrnie_h3",0)], merc_body_armor ,0, 4035, mail_armor_tier_3,imodbits_armor, [], ne_faction],


#["mail_with_surcoat", "Mail with Surcoat", [("mail_long_surcoat_new",0)], merc_body_armor ,0, 4035,mail_armor_tier_3,imodbits_armor, [], [fac_kingdom_4,fac_kingdom_1]],

#["mail_with_surcoat_black", "Mail with Surcoat", [("mail_long_surcoat_new_e",0)], merc_body_armor ,0, 4035,mail_armor_tier_3,imodbits_armor ],
#["surcoat_over_mail", "Surcoat over Mail", [("surcoat_over_mail_new",0)], merc_body_armor ,0, 4035,mail_armor_tier_3,imodbits_armor ],



["teu_surcoat_over_mail_1", "Surcoat over Mail", [("gondor_steward_guard",0)], merc_body_armor ,0, 4035,mail_armor_tier_3,imodbits_armor, [], [fac_kingdom_1]],
["teu_surcoat_over_mail_2", "Surcoat over Mail", [("gon_tower_knight",0)], merc_body_armor ,0, 4035,mail_armor_tier_3,imodbits_armor, [], [fac_kingdom_1,fac_hospitalier_knights]],
#["teu_surcoat_over_mail_3", "Surcoat over Mail", [("teu_mail_long_surcoat_c",0)], merc_body_armor ,0, 4035,mail_armor_tier_3,imodbits_armor, [], [fac_kingdom_13]],
#["teu_surcoat_over_mail_4", "Surcoat over Mail", [("teu_black_surcoat",0)], merc_body_armor ,0, 4035,mail_armor_tier_3,imodbits_armor, [], [fac_kingdom_13]],



["ragged_outfit_mail", "ragged_outfit_high2", [("ragged_outfit_c",0)], merc_body_armor ,0, 4035,mail_armor_tier_3,imodbits_armor ],

["heraldic_mail_with_surcoat", "Heraldic Mail with Surcoat", [("heraldic_armor_new_a",0)], merc_body_armor ,0, 4035,mail_armor_tier_3,imodbits_armor, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_a", ":agent_no", ":troop_no")])], [fac_kingdom_8,fac_kingdom_11]],

["mail_hauberk", "Mail Hauberk", [("hauberk_a_new1",0)], merc_body_armor ,0, 5256,mail_armor_tier_4,imodbits_armor , [], ne_faction],

["haubergeon", "Haubergeon", [("haubergeon_c",0)], merc_body_armor ,0, 4035,mail_armor_tier_3,imodbits_armor, [], [fac_kingdom_10]],

["ee_mail_hauberk_1", "Mail Hauberk", [("zimke_hauberk_b",0)], merc_body_armor ,0, 4035,mail_armor_tier_3,imodbits_armor , [], ee_faction],
["ee_mail_hauberk_2", "Mail Hauberk", [("boyar_puzo",0)], merc_body_armor ,0, 5256,mail_armor_tier_4,imodbits_armor , [], ee_faction],

["ee_armor_3", "Light Mail and Plate", [("zimke_jawshan_one",0)], merc_body_armor,0, 5256,mail_armor_tier_4,imodbits_armor, [], ee_faction],
["ee_armor_4", "Mail and Plate", [("zimke_yushman",0)], merc_body_armor,0, 6683,mail_armor_tier_5,imodbits_armor, [], ee_faction],

["mail_hauberk_1", "Mail Hauberk", [("denmark_huscarl_b",0)], merc_body_armor ,0, 5256,mail_armor_tier_4,imodbits_armor , [], ne_faction],
["mail_hauberk_2", "Mail Hauberk", [("denmark_huscarl_ab",0)], merc_body_armor ,0, 5256,mail_armor_tier_4,imodbits_armor , [], ne_faction],
["mail_hauberk_3", "Mail Hauberk", [("denmark_huscarl_bc",0)], merc_body_armor ,0, 5256,mail_armor_tier_4,imodbits_armor , [], ne_faction],


["light_brigandine_red_mail", "Brigandine", [("brigandine_red_mail",0)], merc_body_armor,0, 4035,mail_armor_tier_3 ,imodbits_armor, [], [fac_kingdom_4]],
["light_brigandine_green_mail", "Brigandine", [("brigandine_green_mail",0)], merc_body_armor,0, 4035,mail_armor_tier_3 ,imodbits_armor, [], [fac_kingdom_5]],
["light_brigandine_blue_mail", "Brigandine", [("brigandine_blue_mail",0)], merc_body_armor,0, 4035,mail_armor_tier_3 ,imodbits_armor, [], [fac_kingdom_1]],
["light_brigandine_yellow_mail", "Brigandine", [("brigandine_yellow_mail",0)], merc_body_armor,0, 4035,mail_armor_tier_3 ,imodbits_armor, [], [fac_kingdom_7,fac_kingdom_10]],
["light_brigandine_black_mail", "Brigandine", [("brigandine_black_mail",0)], merc_body_armor,0, 4035,mail_armor_tier_3 ,imodbits_armor, [], [fac_kingdom_1]],

["brigandine_red", "Brigandine", [("brigandine_b",0)], merc_body_armor,0, 5256,mail_armor_tier_4,imodbits_plate, [], [fac_kingdom_4]],
["brigandine_blue", "Brigandine", [("brigandine_c",0)], merc_body_armor,0, 5256,mail_armor_tier_4,imodbits_plate, [], [fac_kingdom_1]],
["brigandine_black", "Brigandine", [("swareb_brigandine_b",0)], merc_body_armor,0, 5256,mail_armor_tier_4,imodbits_plate, [], [fac_kingdom_7]],
["brigandine_green", "Brigandine", [("brigandine_g",0)], merc_body_armor,0, 5256,mail_armor_tier_4,imodbits_plate, [], [fac_kingdom_5]],

["brigandine_heraldic", "Heraldic Brigandine", [("brigandine_heraldic",0)], merc_body_armor,0, 5256,mail_armor_tier_4,imodbits_plate, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_brigandine_new", ":agent_no", ":troop_no")])],],



["heraldic_mail_with_tabard", "Heraldic Mail with Tabard", [("heraldic_armor_new_d",0)], merc_body_armor ,0, 5256,mail_armor_tier_4,imodbits_armor,  [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_d", ":agent_no", ":troop_no")])], [fac_kingdom_4,fac_kingdom_10,fac_kingdom_11]],

["banded_armor", "Banded Armor", [("banded_armor_a1",0)], merc_body_armor ,0, 6683,mail_armor_tier_5,imodbits_armor, [], ne_faction],
["cuir_bouilli", "Cuir Bouilli", [("cuir_bouilli_a",0)], merc_body_armor ,0, 5256,mail_armor_tier_4,imodbits_armor, [], ne_faction],

["dol_hauberk", "Dol_Amroth_Hauberk", [("dol_hauberk",0)], merc_body_armor ,0, 5256,mail_armor_tier_4,imodbits_armor, [], [fac_kingdom_1]],

["gon_regular", "Gondor_Heavy_Mail", [("gondor_regular",0)], merc_body_armor ,0, 6683,mail_armor_tier_5,imodbits_armor, [], [fac_kingdom_1]],
["gon_knight", "Gondor_Heavy_Mail_and_Cloak", [("gondor_knight",0)], merc_body_armor ,0, 6683,mail_armor_tier_5,imodbits_armor, [], [fac_kingdom_1]],

["gondor_armor_low", "gondor_armor", [("gondor_armor_low",0)], merc_body_armor ,0, 7310,full_plate_armor_tier_1,imodbits_plate, [], [fac_kingdom_1]],
["gondor_armor_med", "gondor_armor", [("gondor_armor_med",0)], merc_body_armor ,0, 9216,full_plate_armor_tier_2,imodbits_plate, [], [fac_kingdom_1]],


["brigandine_plate_red", "Brigandine with Plate", [("brigandine_red_plate",0)], merc_body_armor,0, 6683,mail_armor_tier_5,imodbits_plate, [], [fac_kingdom_4]],
["brigandine_plate_green", "Brigandine with Plate", [("brigandine_green_plate",0)], merc_body_armor,0, 6683,mail_armor_tier_5,imodbits_plate, [], [fac_kingdom_5]],



["heraldic_mail_with_tunic", "Heraldic Mail", [("heraldic_armor_new_b",0)], merc_body_armor ,0, 5256,mail_armor_tier_4,imodbits_armor,  [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_b", ":agent_no", ":troop_no")])]],

["heraldic_mail_with_tunic_b", "Heraldic Mail", [("heraldic_armor_new_c",0)], merc_body_armor ,0, 5256,mail_armor_tier_4,imodbits_armor,  [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_c", ":agent_no", ":troop_no")])]],










["breastplate_red", "cuirass", [("red_cuirass",0)], merc_body_armor,0, 3933,breastplate_tier_1,imodbits_plate, [], [fac_kingdom_4,fac_kingdom_8]],
["breastplate_german", "cuirass", [("german_cuirass",0)], merc_body_armor,0, 3933,breastplate_tier_1,imodbits_plate , [], [fac_kingdom_7,fac_kingdom_11]],
["breastplate_blue", "cuirass", [("blue_cuirass",0)], merc_body_armor,0, 3933,breastplate_tier_1,imodbits_plate, [], [fac_kingdom_1]],
["breastplate_green", "cuirass", [("green_cuirass",0)], merc_body_armor,0, 3933,breastplate_tier_1,imodbits_plate, [], [fac_kingdom_5]],
#["breastplate_teu", "cuirass", [("black_cuirass",0)], merc_body_armor,0, 3933,breastplate_tier_1,imodbits_plate , [], [fac_kingdom_13]],
#["breastplate_plain", "cuirass", [("white_cuirass",0)], merc_body_armor,0, 3933,breastplate_tier_1,imodbits_plate , [], [fac_kingdom_10]],



#["breastplate_dir", "breastplate", [("half_plate_dir",0)], merc_body_armor,0, 4489,breastplate_tier_2,imodbits_plate , [], [fac_kingdom_8]],



["red_armour_1", "Red_Outfit", [("german_armour_T1_2",0)], merc_body_armor,0, 1722,breastplate_tier_0,imodbits_plate, [], [fac_kingdom_7]],
["blue_armour_1", "Black_Outfit", [("german_armour_T1_1",0)], merc_body_armor, 0, 1722,breastplate_tier_0,imodbits_armor, [], [fac_kingdom_7]],
["german_armour_1", "Gray_Shooter_Outfit", [("german_armour_T1",0)], merc_body_armor, 0, 1722,breastplate_tier_0,imodbits_armor, [], [fac_kingdom_7]],

["red_armour_2", "Imperial_Plate_Armor", [("german_armour_T2_2",0)], merc_body_armor,0, 4489,breastplate_tier_2,imodbits_plate, [], [fac_kingdom_8,fac_kingdom_7]],
["blue_armour_2", "Imperial_Plate_Armor", [("german_armour_T2_1",0)], merc_body_armor,0, 4489,breastplate_tier_2,imodbits_plate, [], [fac_kingdom_7]],
["german_armour_2", "Imperial_Plate_Armor", [("german_armour_T2",0)], merc_body_armor,0, 4489,breastplate_tier_2,imodbits_plate, [], [fac_kingdom_7]],

["red_armour_3", "Imperial_Plate_Armor", [("german_armour_T3_2",0)], merc_body_armor,0, 5738,breastplate_tier_3,imodbits_plate, [], [fac_kingdom_8,fac_kingdom_7]],
["blue_armour_3", "Imperial_Plate_Armor", [("german_armour_T3_1",0)], merc_body_armor,0, 5738,breastplate_tier_3,imodbits_plate, [], [fac_kingdom_7]],
["german_armour_3", "Imperial_Plate_Armor", [("german_armour_T3",0)], merc_body_armor,0, 5738,breastplate_tier_3,imodbits_plate, [], [fac_kingdom_7]],

["red_armour_4", "Imperial_Plate_Armor", [("german_armour_T4_1",0)], merc_body_armor,0, 6768,breastplate_tier_4,imodbits_plate, [], [fac_kingdom_8,fac_kingdom_7]],
["blue_armour_4", "uniform_with_breastplate", [("german_armour_T4",0)], merc_body_armor,0, 5738,breastplate_tier_3,imodbits_plate, [], [fac_kingdom_7]],
["german_armour_4", "Imperial_Plate_Armor", [("german_armour_T4_2",0)], merc_body_armor,0, 6768,breastplate_tier_4,imodbits_plate, [], [fac_kingdom_7]],

["red_armour_5", "Imperial_Plate_Armor", [("german_armour_T5",0)], merc_body_armor,0, 8100,breastplate_tier_5,imodbits_plate, [], [fac_kingdom_7]],
["blue_armour_5", "Imperial_Plate_Armor", [("german_armour_T5_2",0)], merc_body_armor,0, 10868,full_plate_armor_tier_3,imodbits_plate, [], [fac_kingdom_7]],
["german_armour_5", "Imperial_Plate_Armor", [("german_armour_T5_1",0)], merc_body_armor,0, 12769,full_plate_armor_tier_4,imodbits_plate, [], [fac_kingdom_7]],

["german_armour_6", "Imperial_Plate_Armor", [("german_armour_T6",0)], merc_body_armor,0, 12769,full_plate_armor_tier_4,imodbits_plate, [], [fac_kingdom_7]],

["reiksguard_armour", "Reiksguard_Armour", [("reiksguard_armour", 0)], merc_body_armor, 0, 12769,full_plate_armor_tier_4,imodbits_plate , [], [fac_kingdom_7]],

["light_mail_and_plate", "Light Mail and Plate", [("armor1",0)], itp_type_body_armor|itp_covers_legs   ,0, 5256,mail_armor_tier_4,imodbits_armor],
["mail_and_plate",       "Dol_Amroth_Heavy_Mail",       [("dol_heavy_mail",0)], itp_type_body_armor|itp_covers_legs   ,0,  7310,full_plate_armor_tier_1,imodbits_armor],

["early_transitional_e1", "Heavy Mail and Plate", [("armor17",0)], merc_body_armor ,0, 5256,mail_armor_tier_4,imodbits_armor, [], [fac_kingdom_4]],
["early_transitional_f1", "Heavy Mail and Plate", [("armor16",0)], merc_body_armor ,0, 5256,mail_armor_tier_4,imodbits_armor, [], [fac_kingdom_4]],

["early_transitional_hre", "Heavy Mail and Plate", [("armor33",0)], merc_body_armor ,0, 5256,mail_armor_tier_4,imodbits_armor, [], [fac_kingdom_7]],
#["early_transitional_teu", "Heavy Mail and Plate", [("early_transitional_teu",0)], merc_body_armor ,0, 5256,mail_armor_tier_4,imodbits_armor, [], [fac_kingdom_1]],
["early_transitional_heraldic", "Heavy Mail and Plate", [("early_transitional_heraldic",0)], merc_body_armor ,0, 5256,mail_armor_tier_4,imodbits_armor ,[(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_early_transitional_heraldic", ":agent_no", ":troop_no")])], [fac_kingdom_10]],
["knight_armor1", "Plate_Armor_With_Surcoat", [("armor13", 0)], merc_body_armor, 0, 7310,full_plate_armor_tier_1, imodbits_armor , [], euro_factions], 
["knight_armor2", "Plate_Armor_With_Surcoat", [("armor_frenchplate", 0)], merc_body_armor, 0, 7310,full_plate_armor_tier_1, imodbits_armor , [], euro_factions], 
["knight_armor3", "Plate_Armor_With_Surcoat", [("armor14", 0)], merc_body_armor, 0, 7310,full_plate_armor_tier_1, imodbits_armor , [], euro_factions], 
["knight_armor4", "Plate_Armor_With_Surcoat", [("armor2", 0)], merc_body_armor, 0, 7310,full_plate_armor_tier_1, imodbits_armor , [], euro_factions], 
["knight_armor5", "Plate_Armor_With_Surcoat", [("armor3", 0)], merc_body_armor, 0, 7310,full_plate_armor_tier_1, imodbits_armor , [], euro_factions], 
["knight_armor6", "Plate_Armor_With_Surcoat", [("armor_polishplate", 0)], merc_body_armor, 0, 7310,full_plate_armor_tier_1, imodbits_armor , [], euro_factions], 
["ranger_armor4", "Gothic_Mixed_Armor", [("armor23", 0)], itp_type_body_armor|itp_covers_legs, 0, 7310,full_plate_armor_tier_1, imodbits_armor], 

["corrazina_red", "corrazina", [("corrazina_red",0)], merc_body_armor, 0, 7310,full_plate_armor_tier_1,imodbits_plate, [], [fac_kingdom_4]],
["corrazina_blue", "corrazina", [("corrazina_blue",0)], merc_body_armor, 0, 7310,full_plate_armor_tier_1,imodbits_plate, [], [fac_kingdom_10]],
["corrazina_yellow", "corrazina", [("corrazina_yellow",0)], merc_body_armor, 0, 7310,full_plate_armor_tier_1,imodbits_plate , [], [fac_kingdom_7]],
["corrazina_green", "corrazina", [("corrazina_green",0)], merc_body_armor, 0, 7310,full_plate_armor_tier_1,imodbits_plate, [], [fac_kingdom_5]],



["half_plates", "churburg_13_mail", [("churburg_13_mail",0)], merc_body_armor, 0, 9216,full_plate_armor_tier_2,imodbits_plate, [], [fac_kingdom_8,fac_kingdom_1,fac_kingdom_10]],
["half_plates_red", "churburg_13_brass", [("churburg_13_e",0)], merc_body_armor, 0, 9216,full_plate_armor_tier_2,imodbits_plate, [], [fac_kingdom_4]],
["half_plates_blue", "churburg_13_brass", [("churburg_13",0)], merc_body_armor, 0, 9216,full_plate_armor_tier_2,imodbits_plate, [], [fac_kingdom_10,fac_kingdom_1]],
["half_plates_green", "churburg_13_brass", [("churburg_green",0)], merc_body_armor, 0, 9216,full_plate_armor_tier_2,imodbits_plate, [], [fac_kingdom_5]],
["half_plates_yello", "churburg_13_brass", [("churburg_yello",0)], merc_body_armor, 0, 9216,full_plate_armor_tier_2,imodbits_plate, [], [fac_kingdom_7]],

["half_plates_red_2", "churburg_13_brass", [("churburg_13_brass",0)], merc_body_armor, 0, 10868,full_plate_armor_tier_3,imodbits_plate, [], [fac_kingdom_4]],
["dol_very_heavy_mail", "churburg_13_brass", [("dol_very_heavy_mail",0)], merc_body_armor, 0, 10868,full_plate_armor_tier_3,imodbits_plate, [], [fac_kingdom_1]],

["gondor_fountain_armor", "gondor_fountain_armor", [("gondor_fountain_armor",0)], merc_body_armor, 0, 18000, weight(25)|abundance(20)|head_armor(0)|body_armor(90)|leg_armor(50)|difficulty(18), imodbits_good_plate, [], [fac_kingdom_1]],





["polish_hussar_armor", "Black Armor", [("pol_krilatiy_gusar_b",0)], merc_body_armor, 0, 8100,breastplate_tier_5,imodbits_plate, [], [fac_kingdom_8]],
["polish_hussar_armor_wing", "Black Armor", [("pol_krilatiy_gusar",0)], merc_body_armor, 0, 8100,breastplate_tier_5,imodbits_plate, [], [fac_kingdom_8]],

["bnw_armour", "Black and White Armour", [("bnw_armour_stripes",0)], merc_body_armor ,0, 8100,breastplate_tier_5,imodbits_plate, [], we_faction+se_faction],
["bnw_armour_red", "Black and White Armour", [("bnw_armour_slashed",0)], merc_body_armor ,0, 8100,breastplate_tier_5,imodbits_plate, [], we_faction+se_faction],
["bnw_armour_green", "Black and White Armour", [("bnw_armour_slashed_green",0)], merc_body_armor ,0, 8100,breastplate_tier_5,imodbits_plate, [], we_faction+se_faction],
["bnw_armour_german", "Black and White Armour", [("bnw_armour_stripes_german",0)], merc_body_armor ,0, 8100,breastplate_tier_5,imodbits_plate, [], [fac_kingdom_7]],

["plate_armor", "Plate Armor", [("2full_plate_armor",0)], merc_body_armor ,0, 10868,full_plate_armor_tier_3,imodbits_good_plate , [], [fac_kingdom_10]],

["plate_armor_2", "Platemail", [("plate_harness_03",0)], merc_body_armor ,0, 10868,full_plate_armor_tier_3,imodbits_good_plate , [], [fac_kingdom_4]],
#["plate_armor_3", "Platemail", [("platemail_harness_02",0)], merc_body_armor ,0, 10868,full_plate_armor_tier_3,imodbits_good_plate , [], [fac_kingdom_1]],
["plate_armor_3", "gondor_armor", [("gondor_armor",0)], merc_body_armor ,0, 10868,full_plate_armor_tier_3,imodbits_good_plate , [], [fac_kingdom_1]],
["plate_armor_4", "Platemail", [("platemail_harness_03",0)], merc_body_armor ,0, 10868,full_plate_armor_tier_3,imodbits_good_plate , [], [fac_kingdom_8]],
["plate_armor_5", "Platemail with Cloak", [("platemail_harness_05",0)], merc_body_armor ,0, 10868,full_plate_armor_tier_3,imodbits_good_plate , [], [fac_kingdom_10]],
["heraldic_plate", "Heraldic Platemail", [("platemail_harness_heraldic",0)], merc_body_armor, 0, 10868,full_plate_armor_tier_3,imodbits_good_plate , 
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_platemail_harness_heraldic", ":agent_no", ":troop_no")])], [fac_kingdom_2,fac_kingdom_10]],
["heraldic_plate_2", "Heraldic Platemail with Cloak", [("platemail_heraldic_03",0)], merc_body_armor, 0, 10868,full_plate_armor_tier_3,imodbits_good_plate , 
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_platemail_harness_heraldic", ":agent_no", ":troop_no")])], [fac_kingdom_2,fac_kingdom_10]],

["knight_plate", "Plate Armor", [("plate_harness_02",0)], merc_body_armor, 0, 12769,full_plate_armor_tier_4 ,imodbits_good_plate , [], [fac_kingdom_8,fac_kingdom_10,fac_kingdom_1,fac_kingdom_4]],
["knight_plate_2", "Plate Armor", [("plate_harness_06",0)], merc_body_armor, 0, 12769,full_plate_armor_tier_4 ,imodbits_good_plate , [], [fac_kingdom_4]],
["knight_plate_3", "gondor_lord_armor_cloaked", [("gondor_lord_armor_cloaked",0)], merc_body_armor, 0, 12769,full_plate_armor_tier_4 ,imodbits_good_plate, [], [fac_kingdom_1]],
["knight_plate_4", "gondor_citadel_armor", [("gondor_citadel_armor",0)], merc_body_armor, 0, 12769,full_plate_armor_tier_4 ,imodbits_good_plate, [], [fac_kingdom_1,fac_hospitalier_knights]],
["knight_plate_5", "Plate Armor", [("platemail_harness_02",0)], merc_body_armor, 0, 12769,full_plate_armor_tier_4 ,imodbits_good_plate, [], [fac_kingdom_8]],

["heraldic_harness", "Heraldic_Plate_Armor", [("plate_heraldic",0)], merc_body_armor, 0, 12769,full_plate_armor_tier_4 ,imodbits_good_plate , [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_plate_harness_heraldic", ":agent_no", ":troop_no")])], [fac_kingdom_5]],

#["16th_plate", "Plate_Armor", [("full_plate",0)], merc_body_armor, 0, 18000, weight(20)|abundance(20)|head_armor(0)|body_armor(85)|leg_armor(45)|difficulty(18), imodbits_good_plate , [], [fac_kingdom_7]],
["white_twiligh_armor", "white_twiligh_armor", [("white_twiligh_armor",0)], merc_body_armor, 0, 18000, weight(25)|abundance(20)|head_armor(15)|body_armor(85)|leg_armor(45)|difficulty(18), imodbits_good_plate , [], [fac_kingdom_1]],

["gondor_lord_armor", "gondor_lord_armor_cloaked", [("imrahil_armour",0)], merc_body_armor, 0, 18000, weight(20)|abundance(20)|head_armor(0)|body_armor(85)|leg_armor(45)|difficulty(18), imodbits_good_plate , [], [fac_kingdom_1]],

["swan_milanese_plate", "swan milanese_plate", [("dol_armour_plate",0)], merc_body_armor, 0, 20000, weight(30)|abundance(20)|head_armor(0)|body_armor(90)|leg_armor(50)|difficulty(18), imodbits_good_plate , [], [fac_kingdom_1]],

["black_plate_armor", "black_plate_armor", [("plate_harness_05",0)], itp_type_body_armor|itp_covers_legs, 0, 18000, weight(30)|abundance(20)|head_armor(0)|body_armor(86)|leg_armor(45)|difficulty(18), imodbits_plate],

["vampire_armor_1", "vampire_armor", [("Vampire_armor_low",0)], merc_body_armor ,0, 7310,full_plate_armor_tier_1,imodbits_plate, [], [fac_kingdom_5,fac_kingdom_3,fac_undeads_2]],
["vampire_armor_2", "vampire_armor", [("Vampire_armor_med",0)], merc_body_armor ,0, 9216,full_plate_armor_tier_2,imodbits_plate, [], [fac_kingdom_5,fac_kingdom_3,fac_undeads_2]],
["vampire_armor_3", "vampire_armor", [("Vampire_armor",0)], merc_body_armor ,0, 10868,full_plate_armor_tier_3,imodbits_good_plate , [], [fac_kingdom_3]],
["vampire_armor_4", "vampire_armor", [("Vampire_citadel_armor",0)], merc_body_armor, 0, 18000, weight(30)|abundance(20)|head_armor(0)|body_armor(86)|leg_armor(45)|difficulty(18) ,imodbits_good_plate, [], [fac_kingdom_3]],



["black_plate_armor_1", "Black Armor", [("dark_full_plate_armor1",0)], merc_body_armor, 0, 10868,full_plate_armor_tier_3, imodbits_good_plate, [], [fac_undeads_2]],
["black_plate_armor_2", "Black Armor", [("dark_full_plate_armor2",0)], merc_body_armor, 0, 12769,full_plate_armor_tier_4, imodbits_good_plate, [], [fac_undeads_2]],

["gothic_plate_nobevor", "gothic_plate", [("armor11",0)], merc_body_armor, 0, 12769,weight(25)|abundance(20)|head_armor(0)|body_armor(85)|leg_armor(50)|difficulty(18), imodbits_good_plate , [], [fac_kingdom_7]],
["gothic_plate", "gothic_plate", [("armor12",0)], merc_body_armor, 0, 18000, weight(25)|abundance(20)|head_armor(0)|body_armor(90)|leg_armor(50)|difficulty(18), imodbits_good_plate , [], [fac_kingdom_8,fac_kingdom_4,fac_kingdom_7]],
["gothic_plate_2", "gothic_plate", [("armor11_pelt",0)], merc_body_armor, 0, 18000, weight(25)|abundance(20)|head_armor(0)|body_armor(90)|leg_armor(50)|difficulty(18), imodbits_good_plate , [], [fac_kingdom_10]],

["maximilian_plate", "Maximilian_plate", [("armor20",0)], merc_body_armor, 0, 20000, weight(20)|abundance(20)|head_armor(0)|body_armor(95)|leg_armor(55)|difficulty(18), imodbits_good_plate,  [], [fac_kingdom_7]],


["milanese_plate", "milanese_plate", [("milanese_plate",0)], merc_body_armor, 0, 20000, weight(30)|abundance(20)|head_armor(0)|body_armor(90)|leg_armor(50)|difficulty(18), imodbits_good_plate, [], [fac_kingdom_5]],
["black_armor2", "Black Armor", [("hm_arm_masW",0)], itp_type_body_armor|itp_covers_legs, 0, 20000, weight(30)|abundance(20)|head_armor(0)|body_armor(90)|leg_armor(50)|difficulty(18), imodbits_good_plate, [], [fac_demon_hunters,fac_hospitalier_knights]],


["lamellar_vest", "Lamellar Vest", [("lamellar_vest_a",0)], merc_body_armor|itp_civilian ,0, 3451,lamellar_armor_tier_1,imodbits_cloth , [], ee_faction],
["lamellar_vest_khergit", "Lamellar Vest", [("lamellar_vest_b",0)], merc_body_armor|itp_civilian ,0, 3451,lamellar_armor_tier_1,imodbits_cloth, [], ee_faction],
["lamellar_vest_blue", "Lamellar Vest", [("lamellar_vest_a5",0)], merc_body_armor|itp_civilian ,0, 3451,lamellar_armor_tier_1,imodbits_cloth, [], ee_faction],
["lamellar_vest_black", "Lamellar Vest", [("lamellar_vest_a7",0)], merc_body_armor|itp_civilian ,0, 3451,lamellar_armor_tier_1,imodbits_cloth, [], ee_faction],



["kuyak", "Kuyak", [("kuyak_a",0)], merc_body_armor ,0, 3270 , weight(20)|abundance(50)|head_armor(0)|body_armor(57)|leg_armor(30)|difficulty(10) ,imodbits_armor, [], ee_faction],
["kuyak_2", "Kuyak", [("kuyak_b",0)], merc_body_armor ,0, 3270 , weight(20)|abundance(50)|head_armor(0)|body_armor(57)|leg_armor(30)|difficulty(10) ,imodbits_armor, [], ee_faction],

["lamellar_armor", "Lamellar Armor", [("lamellar_armor_b",0)], merc_body_armor ,0, 6360,lamellar_armor_tier_2,imodbits_armor , [], ee_faction],
["rus_lamellar_a", "Rus lamellar", [("rus_lamellar_a",0)], merc_body_armor ,0, 6360,lamellar_armor_tier_2,imodbits_armor, [], ee_faction],
["rus_lamellar_b", "Rus lamellar", [("rus_lamellar_b",0)],     merc_body_armor ,0, 6360,lamellar_armor_tier_2,imodbits_armor, [], ee_faction],

["rus_lamellar_c", "Rus lamellar", [("drz_lamellar_armor",0)], merc_body_armor ,0, 6360,lamellar_armor_tier_2,imodbits_armor, [], ee_faction],
["rus_scale", "Rus Scale", [("rus_scale",0)], merc_body_armor ,0, 7876,lamellar_armor_tier_3,imodbits_armor, [], ee_faction],
["scale_armor", "Scale Armor", [("lamellar_armor_e",0)], merc_body_armor ,0, 7876,lamellar_armor_tier_3,imodbits_armor, [], ee_faction],

["huscarl_armor", "huscarl Armor", [("huscarl_armour",0)], merc_body_armor ,0, 6683,mail_armor_tier_5,imodbits_armor, [], ne_faction],
["huscarl_armor_2", "huscarl Armor", [("huscarl_armour_pelt",0)], merc_body_armor ,0, 7876,lamellar_armor_tier_3,imodbits_armor, [], ne_faction],
["huscarl_armor_3", "coat_of_plates", [("nord_coat_of_plates",0)], merc_body_armor ,0, 7876,full_plate_armor_tier_1,imodbits_armor, [], ne_faction],
["huscarl_armor_4", "coat_of_plates", [("nord_coat_of_plates_pelt",0)], merc_body_armor ,0, 9216,full_plate_armor_tier_2,imodbits_armor, [], ne_faction],


#["harad_skirmisher","Light_Harad_Garb",[("harad_skirmisher",0)],itp_type_body_armor|itp_covers_legs|itp_merchandise,0,1722,cloth_tier_4,imodbits_cloth,],
["black_nomad_robe", "Nomad Robe", [("harad_skirmisher",0)], merc_body_armor|itp_civilian,0, 1722,cloth_tier_4,imodbits_cloth, [], tatar_faction],

#["harad_padded","Harondor_Padded_Armor",[("harad_padded",0)],itp_type_body_armor|itp_covers_legs|itp_merchandise,0,940,cloth_tier_3,imodbits_cloth,],
["black_khergit_armor", "Khergit Armor", [("harad_padded",0)], merc_body_armor ,0, 300,cloth_tier_2,imodbits_cloth, [], tatar_faction],

#["harad_tunic","Harad_Tunic",[("harad_tunic",0)],itp_type_body_armor|itp_covers_legs|itp_merchandise,0,300,cloth_tier_2,imodbits_cloth,],
["black_steppe_armor", "Steppe Armor", [("harad_tunic",0)], merc_body_armor ,0, 940,cloth_tier_3,imodbits_cloth, [], tatar_faction],

["harad_hauberk","Harondor_Hauberk",[("harad_hauberk",0)],itp_type_body_armor|itp_covers_legs|itp_merchandise,0,2704,mail_armor_tier_2,imodbits_armor, [], tatar_faction],

#["harad_archer","Harad_Archer_Armor",[("harad_archer",0)],itp_type_body_armor|itp_covers_legs|itp_merchandise,0,3451,lamellar_armor_tier_1,imodbits_armor,],
["black_tribal_warrior_outfit", "Tribal Warrior Outfit", [("harad_archer",0)], merc_body_armor|itp_civilian ,0, 1722,cloth_tier_4,imodbits_cloth, [], tatar_faction],

#["harad_lamellar","Harasjala_Armor",[("harad_lamellar",0)],itp_type_body_armor|itp_covers_legs|itp_merchandise,0,6360,lamellar_armor_tier_2,imodbits_armor,],
["lamellar_armor_black", "Lamellar Armor", [("harad_lamellar",0)], merc_body_armor ,0, 6360,lamellar_armor_tier_2,imodbits_armor , [], tatar_faction],

#["harad_heavy","Harad_Swordsman_Armor",[("harad_heavy",0)],itp_type_body_armor|itp_covers_legs|itp_merchandise,0,7876,lamellar_armor_tier_3,imodbits_armor,],
["khergit_lamellar_armor", "Khergit lamellar_armor", [("harad_heavy",0)], merc_body_armor, 0, 7876,lamellar_armor_tier_3,imodbits_armor, [], tatar_faction],

["khergit_elite_armor", "Khergit Elite Armor", [("harad_lion_scale",0)], merc_body_armor|itp_civilian ,0, 9216,lamellar_armor_tier_4,imodbits_armor, [], tatar_faction],
["black_snake_armor", "Maranka_Armor", [("black_snake_armor",0)], merc_body_armor|itp_civilian ,0, 9216,lamellar_armor_tier_4,imodbits_armor, [], tatar_faction],

["khergit_guard_armor", "Khergit Guard Armor", [("harad_scale",0)], merc_body_armor, 0, 12769,full_plate_armor_tier_4,imodbits_plate, [], tatar_faction],

["khergit_guard_boots",  "Khergit Guard Boots", [("harad_scale_greaves",0)], itp_type_foot_armor| itp_attach_armature,0, 254 , weight(1)|abundance(50)|head_armor(0)|body_armor(0)|leg_armor(35)|difficulty(0) ,imodbits_cloth, [], tatar_faction],


["vaegir_elite_armor", "Vaegir Elite Armor", [("drz_elite_lamellar_armor",0)], merc_body_armor|itp_civilian ,0, 9216,lamellar_armor_tier_4,imodbits_armor, [], ee_faction],

["sarranid_elite_armor", "Sarranid Elite Armor", [("tunic_armor_a",0)], merc_body_armor|itp_civilian ,0, 9216,lamellar_armor_tier_4,imodbits_armor, [], arab_factions],

#["studded_leather_coat_2", "Studded Leather Coat", [("leather_armor_padded1",0)], merc_body_armor ,0, 2704,mail_armor_tier_2,imodbits_armor , [], arab_factions],


#["moor_cloth_robe", "Worn Robe", [("wei_xiadi_kher_kaftan",0)], merc_body_armor ,0, 300,cloth_tier_2,imodbits_cloth, [], arab_factions],


#["moor_skirmisher_armor", "Skirmisher Armor", [("wei_xiadi_kher_ragged_outfit",0)], merc_body_armor|itp_civilian ,0, 1722,cloth_tier_4,imodbits_cloth, [], arab_factions],
#["moor_archers_vest", "Archer's Padded Vest", [("wei_xiadi_archers_vest01",0)], merc_body_armor ,0, 940,cloth_tier_3,imodbits_cloth, [], arab_factions],



#["moor_sarranid_leather_armor", "Sarranid Leather Armor", [("sarranid_studded_leather",0)], merc_body_armor ,0, 2704,mail_armor_tier_2,imodbits_armor, [], arab_factions],
#["moor_lamellar_vest", "Lamellar Vest", [("wei_xiadi_kher_lamellar_vest01",0)], merc_body_armor ,0,3451,lamellar_armor_tier_1,imodbits_cloth, [], arab_factions],



 #["moor_elite_armor", "Sarranid Elite Armor", [("wei_xiadi_samurai_armor01",0)], merc_body_armor|itp_civilian ,0, 9216,lamellar_armor_tier_4,imodbits_armor, [], arab_factions],

 #["archers_vest_2", "Archer's Padded Vest", [("wei_xiadi_archers_vest02",0)], merc_body_armor ,0, 940,cloth_tier_3,imodbits_cloth, [], arab_factions],
 

 ["sarranid_cloth_robe", "Worn Robe", [("sar_robe",0)], merc_body_armor ,0, 100,cloth_tier_1,imodbits_cloth , [], arab_factions],
 ["sarranid_cloth_robe_b", "Worn Robe", [("sar_robe_b",0)], merc_body_armor ,0, 300,cloth_tier_2,imodbits_cloth , [], arab_factions],
 ["skirmisher_armor", "Skirmisher Armor", [("skirmisher_armor",0)], merc_body_armor ,0, 940,cloth_tier_3,imodbits_cloth , [], arab_factions],

 #["sarranid_tunic", "Worn Robe", [("wei_xiadi_rich_tunic02",0)], merc_body_armor ,0,50,cloth_tier_0,imodbits_cloth, [], arab_factions],
 
 ["archers_vest", "Archer's Padded Vest", [("archers_vest",0)], merc_body_armor ,0, 940,cloth_tier_3,imodbits_cloth, [], arab_factions],

["sarranid_leather_armor", "Sarranid Leather Armor", [("sarranid_leather_armor",0)], merc_body_armor ,0, 2704,mail_armor_tier_2,imodbits_armor, [], arab_factions],
["sarranid_cavalry_robe", "Cavalry Robe", [("arabian_armor_a",0)], merc_body_armor|itp_civilian,0, 4035,mail_armor_tier_3,imodbits_armor, [], arab_factions],
["arabian_armor_b", "Sarranid Guard Armor", [("arabian_armor_b",0)], merc_body_armor ,0, 4035,mail_armor_tier_3,imodbits_armor, [], arab_factions],
["sarranid_mail_shirt", "Sarranid Mail Shirt", [("sarranian_mail_shirt",0)], merc_body_armor|itp_civilian ,0, 5256,mail_armor_tier_4,imodbits_armor, [], arab_factions],

["sarranid_mail_shirt_2", "kazaghand", [("zimke_kazaghand",0)], merc_body_armor|itp_civilian ,0, 5256,mail_armor_tier_4,imodbits_armor, [], tatar_faction + arab_factions],
["sarranid_mail_shirt_3", "kazaghand", [("zimke_kazaghand_b",0)], merc_body_armor|itp_civilian ,0, 6683,mail_armor_tier_5,imodbits_armor, [], tatar_faction + arab_factions],
["mamluke_mail", "Mamluke Mail", [("sarranid_elite_cavalary",0)], merc_body_armor|itp_civilian  ,0, 6683,mail_armor_tier_5,imodbits_armor, [], arab_factions],
#["studded_leather_coat_sarr", "Studded Leather Coat", [("wei_xiadi_sar_leather_chain",0)], merc_body_armor ,0, 2704,mail_armor_tier_2,imodbits_armor , [], arab_factions],
 

#["mamluke_lamellar", "Mamluke Lamellar armor", [("wei_xiadi_sarranid_mamluk_armor",0)], merc_body_armor ,0, 7876,lamellar_armor_tier_3,imodbits_armor , [], arab_factions],

["mamluke_mail_heavy", "Mamluke Mail Shirt", [("sipahi_jawshan",0)], merc_body_armor|itp_civilian  ,0,9216,full_plate_armor_tier_2,imodbits_plate, [], [fac_kingdom_9]],

#["turk_boots", "turk Boots", [("ottobott",0)], itp_merchandise| itp_type_foot_armor|itp_civilian| itp_attach_armature ,0, 576 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth, [], arab_factions],

#["turk_cloth_robe", "Worn Robe", [("bakak",0)], merc_body_armor ,0, 300,cloth_tier_2 ,imodbits_cloth , [], [fac_kingdom_9]],
#["janissary_cloth", "Worn Robe", [("cuppe",0)], merc_body_armor ,0, 940,cloth_tier_3 ,imodbits_cloth , [], [fac_kingdom_9]],

["turk_leather_armor", "deli Leather Armor", [("deli_robe",0)], merc_body_armor ,0, 2704,mail_armor_tier_2,imodbits_armor, [], [fac_kingdom_9]],

["turk_armor",            "sipahi_armor", [("heavy_yawshan",0)], merc_body_armor ,0, 7876,full_plate_armor_tier_1,imodbits_armor, [], [fac_kingdom_9]],
["turk_mail_heavy",   "janissary Mail Shirt", [("sipahi_jawshan",0)], merc_body_armor ,0,9216,full_plate_armor_tier_2,imodbits_armor, [], [fac_kingdom_9]],



["janissary_vest", "janissary Shirt", [("janichareteksiz",0)], merc_body_armor|itp_civilian ,0, 1722,cloth_tier_4 ,imodbits_cloth , [], [fac_kingdom_9]],
#["janissary_vest_2", "janissary Shirt", [("janichareteksiz",0)], merc_body_armor|itp_civilian ,0, 1722,cloth_tier_4 ,imodbits_cloth , [], [fac_kingdom_9]],
#["janissary_mail", "janissary Mail With Shirt", [("janichareteksiz_mail",0)], merc_body_armor|itp_civilian ,0, 4035,mail_armor_tier_3,imodbits_armor, [], [fac_kingdom_9]],
#["janissary_mail_musket", "janissary Mail With Shirt", [("ttr_seymen",0)], merc_body_armor|itp_civilian ,0, 5256,mail_armor_tier_4,imodbits_armor, [], [fac_kingdom_9]],
#["janissary_mail_heavy", "janissary Mail Shirt", [("ttr_mega-yushman",0)], merc_body_armor|itp_civilian  ,0,7310,full_plate_armor_tier_1,imodbits_armor, [], [fac_kingdom_9]],

#["sipahi_armor_a", "sipahi_armor", [("ttr_kolcha",0)], merc_body_armor|itp_civilian ,0, 4035,mail_armor_tier_3,imodbits_armor, [], [fac_kingdom_9]],
#["sipahi_armor_b", "sipahi_armor", [("tasarim",0)], merc_body_armor|itp_civilian ,0, 5256,mail_armor_tier_4,imodbits_armor , [], [fac_kingdom_9]],
#["sipahi_armor_c", "sipahi_armor", [("ola",0)], merc_body_armor|itp_civilian  ,0, 7876,lamellar_armor_tier_3,imodbits_armor, [], [fac_kingdom_9]],
#["sipahi_armor_d", "sipahi_armor", [("goldsipahi",0)], merc_body_armor|itp_civilian ,0, 9216,full_plate_armor_tier_2,imodbits_plate, [], [fac_kingdom_9]],

#["turk_turban", "Turban", [("turban2",0)], itp_merchandise| itp_type_head_armor   ,0,  170 , weight(1)|abundance(100)|head_armor(16)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_cloth,  [], [fac_kingdom_9]],
#["turk_turban_2", "Turban", [("turban1",0)], itp_merchandise| itp_type_head_armor   ,0,  170 , weight(1)|abundance(100)|head_armor(16)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_cloth,  [], [fac_kingdom_9]],
#["janissary_helmet", "janissary_helmet", [("kulah",0)], itp_type_head_armor,0,  266, weight(2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_cloth,  [], [fac_kingdom_9]],
#["janissary_helmet_2", "janissary_helmet", [("bork1",0)], itp_type_head_armor,0, 1066, weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0), imodbits_cloth,  [], [fac_kingdom_9]],
["janissary_helmet_3", "janissary_helmet", [("solak_helmet_C",0)], itp_type_head_armor,0, 
 1350, weight(2)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0), imodbits_cloth, 
 [], [fac_kingdom_9]],
["janissary_helmet_4", "janissary_helmet", [("janissary_boerk_B",0)], itp_type_head_armor,0, 
 1666, weight(2)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0), imodbits_cloth, 
 [], [fac_kingdom_9]],
["janissary_helmet_5", "janissary_helmet", [("janissary_boerk_C",0)], itp_type_head_armor,0, 
 2400, weight(2)|abundance(100)|head_armor(60)|body_armor(0)|leg_armor(0), imodbits_cloth, 
 [], [fac_kingdom_9]],

#["chichak1", "chichak", [("chichak2",0)], itp_merchandise| itp_type_head_armor ,0,  2400 , weight(3)|abundance(100)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,  [], arab_factions],
#["chichak2", "chichak", [("chichak1",0)], itp_merchandise| itp_type_head_armor| itp_covers_beard  ,0,  3266 , weight(3.5)|abundance(100)|head_armor(70)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,  [], arab_factions],
#["chichak3", "chichak", [("chichak3",0)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0,  3750, weight(3.5)|abundance(100)|head_armor(75)|body_armor(0)|leg_armor(0)|difficulty(7), imodbits_plate,  [], arab_factions],


["sarranid_dress_a", "Dress", [("sarranid_common_dress",0)], merc_body_armor ,0, 100,cloth_tier_1,imodbits_cloth ],
["sarranid_dress_b", "Dress", [("sarranid_common_dress_b",0)], merc_body_armor ,0, 100,cloth_tier_1,imodbits_cloth ],
##armors_d
##armors_e

#Quest-specific - perhaps can be used for prisoners,
["burlap_tunic", "Burlap Tunic", [("shirt",0)], itp_type_body_armor|itp_covers_legs ,0, 100,cloth_tier_1,imodbits_cloth ],



["strange_armor", "Strange Armor", [("samurai_armor",0)], itp_type_body_armor|itp_covers_legs, 0, 3451,lamellar_armor_tier_1,imodbits_armor ],
["strange_boots", "Strange Boots", [("samurai_boots",0)], itp_type_foot_armor|itp_attach_armature, 0, 2465, weight(1)|abundance(50)|head_armor(0)|body_armor(0)|leg_armor(21)|difficulty(0), imodbits_cloth ],
["strange_helmet", "Strange Helmet", [("samurai_helmet",0)], itp_type_head_armor, 0, 2824, weight(2)|abundance(50)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(7), imodbits_plate ],
["turret_hat_ruby", "Turret Hat", [("turret_hat_r",0)], itp_type_head_armor|itp_civilian|itp_fit_to_head ,0, 70 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth],
["turret_hat_blue", "Turret Hat", [("turret_hat_b",0)], itp_type_head_armor|itp_civilian|itp_fit_to_head ,0, 80 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["turret_hat_green", "Barbette", [("barbette_new",0)],itp_type_head_armor|itp_civilian|itp_fit_to_head,0,70, weight(0.5)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["head_wrappings","Head Wrapping",[("head_wrapping",0)],itp_type_head_armor|itp_fit_to_head,0,16, weight(0.25)|head_armor(3),imodbits_cloth],
["court_hat", "Turret Hat", [("court_hat",0)], itp_type_head_armor|itp_civilian|itp_fit_to_head ,0, 80 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["wimple_a", "Wimple", [("wimple_a_new",0)],itp_type_head_armor|itp_civilian|itp_fit_to_head,0,10, weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["wimple_with_veil", "Wimple with Veil", [("wimple_b_new",0)],itp_type_head_armor|itp_civilian|itp_fit_to_head,0,10, weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["straw_hat", "Straw Hat", [("straw_hat_new",0)],itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["drow_hood", "Hood", [("drow_hood_b",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,900, weight(1)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth , [], [fac_beast]],
["drow_hood_high", "Hood", [("drow_hood",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,1200, weight(1)|abundance(100)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth , [], [fac_beast]],
["hood_c", "Hood", [("hood_newgrn",0)],itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["drow_hood_elite", "Hood", [("drow_elite_helmet",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,1800, weight(1)|abundance(100)|head_armor(70)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth , [], [fac_beast]],
["headcloth", "Headcloth", [("headcloth_a_new",0)],  itp_type_head_armor|itp_civilian ,0, 1 , weight(0.5)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["woolen_hood", "Woolen Hood", [("woolen_hood",0)],  itp_type_head_armor|itp_civilian  ,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["arming_cap", "Arming Cap", [("Helmet_A2_01",0)],  itp_type_head_armor|itp_civilian ,0, 500 , weight(1)|abundance(100)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth],

["fur_hat", "Fur Hat", [("fur_hat_a_new",0)],  itp_type_head_armor|itp_civilian  ,0, 4 , weight(0.5)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth],
["nomad_cap", "Nomad Cap", [("nomad_cap_a_new",0)],  itp_type_head_armor|itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["nomad_cap_b", "Nomad Cap", [("nomad_cap_b_new",0)],  itp_type_head_armor|itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth],
["steppe_cap", "Steppe Cap", [("steppe_cap_a_new",0)],  itp_type_head_armor|itp_civilian ,0, 14 , weight(1)|abundance(100)|head_armor(16)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["padded_coif", "Padded Coif", [("padded_coif_a_new",0)],  itp_type_head_armor   ,0, 6 , weight(1)|abundance(100)|head_armor(16)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["woolen_cap", "Woolen Cap", [("woolen_cap_new",0)],  itp_type_head_armor|itp_civilian ,0, 2 , weight(1)|abundance(100)|head_armor(9)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["felt_hat", "Felt Hat", [("felt_hat_a_new",0)],  itp_type_head_armor|itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
#["felt_hat_b", "Felt Hat", [("felt_hat_b_newc",0)],  itp_type_head_armor|itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth],


["leather_cap", "Leather Cap", [("leather_cap_a_new",0)],  itp_type_head_armor|itp_civilian ,0, 8, weight(1)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["female_hood", "Lady's Hood", [("ladys_hood_new",0)],  itp_type_head_armor|itp_civilian  ,0, 9 , weight(1)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["leather_steppe_cap_a", "Steppe Cap", [("leather_steppe_cap_a_new",0)], itp_type_head_armor   ,0,24 , weight(1)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0) ,imodbits_cloth, [], ee_faction+tatar_faction],
["leather_steppe_cap_b", "Steppe Cap ", [("tattered_steppe_cap_b_new",0)], itp_type_head_armor   ,0,36 , weight(1)|abundance(100)|head_armor(21)|body_armor(0)|leg_armor(0) ,imodbits_cloth , [], ee_faction+tatar_faction],
["leather_steppe_cap_c", "Steppe Cap", [("steppe_cap_a_new",0)], itp_type_head_armor   ,0, 51 , weight(1)|abundance(100)|head_armor(24)|body_armor(0)|leg_armor(0) ,imodbits_cloth , [], ee_faction+tatar_faction],
["leather_warrior_cap", "Leather Warrior Cap", [("skull_cap_new_b",0)],  itp_type_head_armor|itp_civilian ,0, 14 , weight(1)|abundance(100)|head_armor(24)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], tatar_faction],


#iron_headwear_begin

["skullcap", "Skullcap", [("skull_cap_new_a",0)], itp_type_head_armor   ,0, 
 600 , weight(1.0)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate , 
 [], ne_faction],
 
#["helmet_with_neckguard", "Helmet with Neckguard", [("neckguard_helm_new",0)], itp_type_head_armor   ,0,
# 2016 , weight(1.5)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,  
# [], se_faction],

#["flat_topped_helmet", "Flat Topped Helmet", [("flattop_helmet_new",0)], itp_type_head_armor   ,0,
# 2400 , weight(1.75)|abundance(100)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate , 
# [], [fac_kingdom_1,fac_kingdom_2]],
 
["mail_coif", "Mail Coif", [("mail_coif_new",0)], itp_merchandise| itp_type_head_armor   ,0, 
 1350 , weight(1.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_armor , 
 [], euro_factions],
["footman_helmet", "Footman's Helmet", [("skull_cap_new",0)], itp_type_head_armor   ,0, 
 1066 , weight(1.5)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate , 
 [], [fac_kingdom_1]],
#missing...
["nasal_helmet", "Nasal Helmet", [("nasal_helmet_b",0)], itp_type_head_armor   ,0, 
 816 , weight(1.25)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, 
 [], ne_faction],
#["segmented_helmet", "Segmented Helmet", [("segmented_helm_new",0)], itp_type_head_armor   ,0, 
# 1066 , weight(1.25)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate , 
# [], ne_faction],
#["norman_helmet", "Helmet with Cap", [("norman_helmet_a",0)], itp_type_head_armor|itp_fit_to_head ,0,  1666 , weight(1.25)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,  [], ne_faction],

 
["kettle_hat", "Kettle Hat", [("kettle_hat_new",0)], itp_merchandise| itp_type_head_armor,0,
 1666 , weight(1.75)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate , 
 [], se_faction],
#["kettle_hat_2", "Kettle Hat", [("prato_chapel-de-fer",0)], itp_merchandise| itp_type_head_armor,0, 2400 , weight(1.75)|abundance(100)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,  [], euro_factions],


["kettle_hat_cloth1", "Kettle Hat", [("chapel-de-fer_cloth1",0), ("inv_chapel-de-fer_cloth1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 1666 , weight(1.75)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate , [], [fac_kingdom_4,fac_kingdom_7]],
["kettle_hat_cloth2", "Kettle Hat", [("chapel-de-fer_cloth2",0), ("inv_chapel-de-fer_cloth2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 1666 , weight(1.75)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate , [], [fac_kingdom_1,fac_kingdom_4]],
["kettle_hat_cloth3", "Kettle Hat", [("chapel-de-fer_cloth3",0), ("inv_chapel-de-fer_cloth3",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 1666 , weight(1.75)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate , [], [fac_kingdom_4,fac_kingdom_7]],
  
["kettle_hat_mail1", "Kettle Hat", [("chapel-de-fer_mail1",0), ("inv_chapel-de-fer_mail1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 2400 , weight(1.75)|abundance(100)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_4]],
["kettle_hat_mail2", "Kettle Hat", [("chapel-de-fer_mail2",0), ("inv_chapel-de-fer_mail2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 2400 , weight(1.75)|abundance(100)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_4,fac_kingdom_5]],
["kettle_hat_mail3", "Kettle Hat", [("chapel-de-fer_mail3",0), ("inv_chapel-de-fer_mail3",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 2400 , weight(1.75)|abundance(100)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_1,fac_kingdom_4]],

["khergit_lady_hat", "Khergit Lady Hat", [("khergit_lady_hat",0)],  itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair| itp_fit_to_head,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["khergit_lady_hat_b", "Khergit Lady Leather Hat", [("khergit_lady_hat_b",0)], itp_type_head_armor| itp_doesnt_cover_hair| itp_fit_to_head|itp_civilian ,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["sarranid_felt_hat", "Sarranid Felt Hat", [("sar_helmet3",0)], itp_merchandise| itp_type_head_armor   ,0, 16 , weight(2)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_cloth, [], arab_factions],

["turban", "Turban", [("tuareg_open",0)], itp_merchandise| itp_type_head_armor   ,0, 
 170 , weight(1)|abundance(100)|head_armor(16)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_cloth, 
 [], arab_factions],
["desert_turban", "Desert Turban", [("tuareg",0)], itp_merchandise| itp_type_head_armor| itp_covers_beard ,0, 
 294 , weight(1)|abundance(100)|head_armor(21)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_cloth, 
 [], arab_factions],
["sarranid_warrior_cap", "Sarranid Warrior Cap", [("tuareg_helmet",0)], itp_merchandise| itp_type_head_armor| itp_covers_beard  ,0, 
 600 , weight(2)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, 
 [], arab_factions],
["sarranid_horseman_helmet", "Horseman Helmet", [("sar_helmet2",0)], itp_merchandise| itp_type_head_armor   ,0, 
 1066 , weight(2.5)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, 
 [], arab_factions],
["sarranid_helmet1", "Sarranid Keffiyeh Helmet", [("sar_helmet1",0)], itp_merchandise| itp_type_head_armor   ,0, 
 1666 , weight(2.5)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, 
 [], arab_factions],
["sarranid_mail_coif", "Sarranid Mail Coif", [("tuareg_helmet2",0)], itp_merchandise| itp_type_head_armor ,0, 
 2400 , weight(3)|abundance(100)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, 
 [], arab_factions],
["sarranid_veiled_helmet", "Sarranid Veiled Helmet", [("turban_helmet_b_inv",0)], itp_merchandise| itp_type_head_armor| itp_covers_beard  ,0, 
 3266 , weight(3.5)|abundance(100)|head_armor(70)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,  [], arab_factions],
["sarranid_veiled_helmet2", "Sarranid Veiled Helmet", [("turban_helmet_new_inv",0)], itp_merchandise| itp_type_head_armor| itp_covers_beard  ,0, 
 3750 , weight(3.5)|abundance(100)|head_armor(75)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,  [], arab_factions],
["chichak1", "Chichak", [("ottoman_chichak",0)], itp_merchandise| itp_type_head_armor| itp_covers_beard  ,0, 
 3266 , weight(3.5)|abundance(100)|head_armor(70)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,  [], arab_factions],
["chichak2", "Elite_Cavalry_Chichak", [("ottoman_elite_cavalry_chichak",0)], itp_merchandise| itp_type_head_armor| itp_covers_beard  ,0, 
 3750 , weight(3.5)|abundance(100)|head_armor(75)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,  [], arab_factions],



["nordic_archer_helmet", "Nordic Leather Helmet", [("Helmet_A_vs2",0)], itp_merchandise| itp_type_head_armor    ,0, 
 600 , weight(2)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, 
 [], ne_faction],
["nordic_veteran_archer_helmet", "Nordic Leather Helmet", [("Helmet_A",0)], itp_merchandise| itp_type_head_armor,0, 
 1066 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, 
 [], ne_faction],
["nordic_footman_helmet", "Nordic Footman Helmet", [("Helmet_B_vs2",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0, 
 1350 , weight(1.75)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, 
 [], ne_faction],
["nordic_fighter_helmet", "Nordic Fighter Helmet", [("Helmet_B",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0, 
 1734 , weight(2)|abundance(100)|head_armor(51)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, 
 [], ne_faction],
["nordic_helmet", "Nordic Helmet", [("helmet_w_eyeguard_new",0)], itp_merchandise| itp_type_head_armor   ,0, 
 2410 , weight(2)|abundance(100)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, 
 [], ne_faction],
["nordic_huscarl_helmet", "Nordic Huscarl's Helmet", [("nordhelm_horn",0)], itp_merchandise| itp_type_head_armor   ,0, 
 2410 , weight(2)|abundance(100)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, 
 [], ne_faction],
["nordic_warlord_helmet", "Nordic Warlord Helmet", [("helm24",0)], itp_merchandise| itp_type_head_armor ,0, 
 2816 , weight(2.25)|abundance(100)|head_armor(65)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, 
 [], ne_faction],
["nord_norman_helmet", "Norman_Helmet", [("Helmet_Weathered_Berserker_C_01",0)], itp_type_head_armor|itp_merchandise, 0, 
 3266 , weight(2.25)|abundance(100)|head_armor(70)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, 
 [], ne_faction],
["nord_norman_mask", "norman_mask", [("Helmet_Weathered_Berserker_A_01",0)], itp_type_head_armor|itp_merchandise, 0, 
 3750 , weight(2.25)|abundance(100)|head_armor(75)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,
 [], ne_faction],
 
["nord_berserker_helmet", "berserker_mask", [("Helmet_Elite_Berserker_A_01",0)], itp_type_head_armor|itp_merchandise, 0, 
 4266 , weight(2.75)|abundance(100)|head_armor(80)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, 
 [], ne_faction],
["nord_berserker_mask", "berserker_mask", [("Helmet_Elite_Berserker_B_01",0)], itp_type_head_armor|itp_merchandise, 0, 
 5400,weight(3.0)|abundance(25)|head_armor(90)|body_armor(0)|leg_armor(0)|difficulty(10),imodbits_plate,
 [], ne_faction],

["vaegir_fur_cap", "Cap with Fur", [("vaeg_helmet3",0)], itp_merchandise| itp_type_head_armor   ,0, 
 600 , weight(1)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, 
 [], ee_faction],
["vaegir_fur_helmet", "Vaegir Helmet", [("vaeg_helmet2",0)], itp_merchandise| itp_type_head_armor   ,0, 
 1066 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, 
 [], ee_faction],
["vaegir_lamellar_helmet", "Helmet with Lamellar Guard", [("vaeg_helmet4",0)], itp_merchandise| itp_type_head_armor ,0, 
 1350 , weight(2.75)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, 
 [], ee_faction],
 
["vaegir_spiked_helmet", "Spiked Cap", [("inv_rus_helm",0), ("inv_rus_helm",ixmesh_inventory)], itp_merchandise| itp_type_head_armor   ,0, 
 1350 , weight(2.75)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, 
 [], ee_faction],
 
["spiked_helmet", "Spiked Helmet", [("vaeg_helmet1",0)], itp_merchandise| itp_type_head_armor   ,0, 
 1666 , weight(2.5)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, 
 [], ee_faction],
 
["tagancha_helm_a", "Tagancha helm", [("tagancha_helm_a",0), ("inv_tagancha_helm_a",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|  itp_attach_armature|itp_covers_beard,0, 
 2400 , weight(2.5)|abundance(100)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, 
 [], ee_faction],
["vaegir_noble_helmet", "Vaegir Nobleman Helmet", [("vaeg_helmet7",0)], itp_merchandise| itp_type_head_armor   ,0, 
 2816, weight(2.75)|abundance(100)|head_armor(65)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, 
 [], ee_faction],
["gnezdovo_helm", "Gnezdovo helm", [("gnezdovo_helm_a",0), ("inv_gnezdovo_helm_a",ixmesh_inventory)], itp_merchandise| itp_type_head_armor| itp_attach_armature|itp_covers_beard,0, 
 2816, weight(2.75)|abundance(100)|head_armor(65)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, 
 [], ee_faction],
 
["vaegir_war_helmet", "Vaegir War Helmet", [("vaegir_tourney",0)], itp_merchandise| itp_type_head_armor ,0, 
 3266 , weight(3)|abundance(100)|head_armor(70)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, 
 [], ee_faction],
["novogrod_helm", "Novogrod helm", [("novogrod_helm",0), ("inv_novogrod_helm",ixmesh_inventory)], itp_merchandise| itp_type_head_armor| itp_attach_armature|itp_covers_beard,0, 
 3266 , weight(3)|abundance(100)|head_armor(70)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, 
 [], ee_faction],
["tagancha_helm_b", "Tagancha helm", [("tagancha_helm_b",0), ("inv_tagancha_helm_b",ixmesh_inventory)], itp_merchandise| itp_type_head_armor| itp_attach_armature|itp_covers_beard,0, 
 3266 , weight(3)|abundance(100)|head_armor(70)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, 
 [], ee_faction],

["nikolskoe_helm", "Nikolskoe helm", [("nikolskoe_helm",0), ("inv_nikolskoe_helm",ixmesh_inventory)],itp_merchandise|itp_type_head_armor| itp_attach_armature|itp_covers_beard,0,
 3750 , weight(3.5)|abundance(100)|head_armor(75)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, 
 [], ee_faction],
["litchina_helm", "litchina helm", [("litchina_helm",0),("inv_litchina_helm",ixmesh_inventory)],itp_merchandise|itp_type_head_armor|itp_covers_beard| itp_attach_armature,0, 
 3750 , weight(3.5)|abundance(100)|head_armor(75)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, 
 [], ee_faction],


#TODO:
#["skullcap_b", "Skullcap_b", [("skull_cap_new_b",0)], itp_merchandise| itp_type_head_armor   ,0, 71 , weight(1.5)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ],

#new_hat


#["shlapa_black_1", "shlapa_black", [("shlapa_black_b",0)],  itp_type_head_armor|itp_civilian ,0, 100 , weight(1)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth],
#["shlapa_black_2", "shlapa_black", [("shlapa_black_c",0)],  itp_type_head_armor|itp_civilian ,0, 250 , weight(1)|abundance(100)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth],
#["shlapa_black_3", "shlapa_black", [("shlapa_black_c",0)],  itp_type_head_armor|itp_civilian ,0, 500 , weight(1)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth],

#["shlapa_blue_1", "shlapa_blue", [("shlapa_blue_b",0)],  itp_type_head_armor|itp_civilian ,0, 100 , weight(1)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth],
#["shlapa_blue_2", "shlapa_blue", [("shlapa_blue_a",0)],  itp_type_head_armor|itp_civilian ,0, 250 , weight(1)|abundance(100)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth],

#["shlapa_red", "shlapa_blue", [("shlapa_blue_c",0)],  itp_type_head_armor|itp_civilian ,0, 500 , weight(1)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth],

#["shlapa_brown_1", "shlapa_brown", [("shlapa_brown_a",0)],  itp_type_head_armor|itp_civilian ,0, 50 , weight(1)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth],
#["shlapa_brown_2", "shlapa_brown", [("shlapa_brown_b",0)],  itp_type_head_armor|itp_civilian ,0, 250 , weight(1)|abundance(100)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth],


["landsknecht_hat_yellow", "Hat", [("Helmet_A1_01",0)],  itp_type_head_armor|itp_civilian ,0, 1300 , weight(1)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth],


#new_hat

["hussar_hat", "hussar Cap", [("ukr_shapka_serduka",0)], itp_type_head_armor|itp_civilian ,0,
 800 , weight(1)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["cossack_hat_a", "Cossack Cap", [("ukr_shapka_s_perom_b",0)], itp_type_head_armor|itp_civilian ,0,
 250 , weight(1)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["cossack_hat_b", "Cossack Cap", [("ukr_kozak_shapka_b",0)], itp_type_head_armor|itp_civilian ,0,
 500 , weight(1)|abundance(100)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
 
["cossack_hat_c", "Cossack Cap", [("ukr_shapka_s_perom_a",0)], itp_type_head_armor|itp_civilian ,0,
 600 , weight(1)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

 


["beret_plain_red", "beret", [("beret_plain_red",0)],  itp_type_head_armor| itp_doesnt_cover_hair|itp_civilian ,0, 1300 , weight(1)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth],

["beret_plain_brown", "beret", [("beret_plain_brown",0)],  itp_type_head_armor| itp_doesnt_cover_hair|itp_civilian ,0, 1300 , weight(1)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth],

["beret_plumes_red", "beret", [("beret_plumes_red",0)],  itp_type_head_armor| itp_doesnt_cover_hair|itp_civilian ,0, 1300 , weight(1)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth],

["beret_plumes_brown", "beret", [("beret_plumes_brown",0)],  itp_type_head_armor| itp_doesnt_cover_hair|itp_civilian ,0, 1300 , weight(1)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth],




 

 
  
  
["reytar_helmet", "Reiter Helmet", [("mosk_reytar_helm",0)], itp_merchandise| itp_type_head_armor   ,0,
 2016 , weight(2.0)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,  
 [], ee_faction],
  
["boyar_helmet", "Boyar Militia Helmet", [("mosk_boyar_sholom",0)], itp_merchandise| itp_type_head_armor,0, 
 2816 , weight(2.5)|abundance(100)|head_armor(65)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate,
 [], ee_faction],
 
["polish_husar_helmet", "Winged Hussar Helmet", [("husar_sholom",0)], itp_merchandise| itp_type_head_armor,0, 
 3266 , weight(2.5)|abundance(100)|head_armor(70)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate,
 [], ee_faction],

 
#["sarg_helm", "sarg_helm", [("sturmhaube_1",0)], itp_merchandise|itp_type_head_armor   ,0, 
# 2016 , weight(1.5)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,  
# [], [fac_kingdom_4,fac_kingdom_7,fac_kingdom_1,fac_kingdom_11]],

#["footman_burgonet", "footmenburgonet", [("sturmhaube_6",0)], itp_merchandise|itp_type_head_armor   ,0, 
# 2016 , weight(2.0)|abundance(100)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,  
# [], [fac_kingdom_4,fac_kingdom_7,fac_kingdom_1,fac_kingdom_11]],
 
["sturmhaube_w1", "footmenburgonet", [("sturmhaube_1",0)], itp_merchandise|itp_type_head_armor   ,0, 
 2016 , weight(1.5)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,  
 [], [fac_kingdom_7,fac_kingdom_5,fac_kingdom_11]],
["sturmhaube_w2", "footmenburgonet", [("sturmhaube_6",0)], itp_merchandise|itp_type_head_armor   ,0, 
 2016 , weight(2.0)|abundance(100)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,  
 [], [fac_kingdom_7,fac_kingdom_5,fac_kingdom_11]],
["sturmhaube_w3", "footmenburgonet", [("sturmhaube_4",0)], itp_merchandise|itp_type_head_armor   ,0, 
 2816 , weight(2.0)|abundance(100)|head_armor(65)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,  
 [], [fac_kingdom_7,fac_kingdom_5,fac_kingdom_11]],
["sturmhaube_w4", "footmenburgonet", [("sturmhaube_5",0)], itp_merchandise|itp_type_head_armor   ,0, 
 3750 , weight(2.5)|abundance(100)|head_armor(70)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate,
 [], [fac_kingdom_7]],
 



 
["sturmhaube_bnw1", "footmenburgonet", [("sturmhaube_1BW",0)], itp_merchandise|itp_type_head_armor   ,0, 
 2016 , weight(1.5)|abundance(100)|head_armor(54)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,  
 [], [fac_kingdom_7,fac_kingdom_5,fac_kingdom_11]],
["sturmhaube_bnw2", "footmenburgonet", [("sturmhaube_2BW",0)], itp_merchandise|itp_type_head_armor   ,0, 
 2016 , weight(2.0)|abundance(100)|head_armor(64)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,  
 [], [fac_kingdom_7,fac_kingdom_5,fac_kingdom_11]],
["sturmhaube_bnw3", "footmenburgonet", [("sturmhaube_4BW",0)], itp_merchandise|itp_type_head_armor   ,0, 
 2816 , weight(2.0)|abundance(100)|head_armor(69)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,  
 [], [fac_kingdom_7,fac_kingdom_5,fac_kingdom_11]],
["sturmhaube_bnw4", "footmenburgonet", [("sturmhaube_5BW",0)], itp_merchandise|itp_type_head_armor   ,0, 
 3750 , weight(2.5)|abundance(100)|head_armor(74)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate,
 [], [fac_kingdom_7,fac_kingdom_5,fac_kingdom_11]],
 
#["burgonet", "Full Helm", [("burgonet",0)],itp_merchandise| itp_type_head_armor|itp_covers_head ,0, 
# 3750 , weight(2.5)|abundance(100)|head_armor(70)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate,
# [], [fac_kingdom_7]],
#["burgonet_trim", "Full Helm", [("burgonet_trim",0)],itp_merchandise| itp_type_head_armor|itp_covers_head ,0, 
# 3750 , weight(2.5)|abundance(100)|head_armor(75)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate,
# [], [fac_kingdom_7]],

["knight_helmet1", "Goat_Tourney_Mask", [("helm7",0)], itp_merchandise| itp_type_head_armor,0, 
 4266 , weight(2.75)|abundance(100)|head_armor(80)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, 
 [], euro_factions],
["knight_helmet2", "Eagle_Helmet", [("helm15",0)], itp_merchandise| itp_type_head_armor,0, 
 4266 , weight(2.75)|abundance(100)|head_armor(80)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, 
 [], euro_factions],
["knight_helmet3", "Horse_Great_Helm", [("helm23",0)], itp_merchandise| itp_type_head_armor,0, 
 4266 , weight(2.75)|abundance(100)|head_armor(80)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, 
 [], euro_factions],
 

["assasin_hood_1", "Assasin's_Hood", [("helm10", 0)], itp_type_head_armor|itp_civilian, 0, 1300, weight(0)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_cloth, [], euro_factions], 
["assasin_hood_2", "Assasin's_Hood", [("helm10_l", 0)], itp_type_head_armor|itp_civilian, 0, 1300, weight(0)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_cloth, [], euro_factions], 

["assasin_hood_3", "Assasin's_Hood", [("helm11", 0)], itp_type_head_armor|itp_civilian, 0, 2020, weight(0)|abundance(100)|head_armor(60)|body_armor(30)|leg_armor(0), imodbits_cloth, [], euro_factions], 
["assasin_hood_4", "Assasin's_Hood", [("helm11_l", 0)], itp_type_head_armor|itp_civilian, 0, 2020, weight(0)|abundance(100)|head_armor(60)|body_armor(30)|leg_armor(0), imodbits_cloth, [], euro_factions], 

["guard_helmet", "Guard Helmet", [("reinf_helmet_new",0)], itp_type_head_armor|itp_merchandise, 0, 
 1666 , weight(2)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, 
 [], [fac_kingdom_4,fac_kingdom_5,fac_kingdom_11,fac_kingdom_10,fac_kingdom_3]],
["bascinet", "Bascinet", [("bascinet_avt_new",0)], itp_merchandise|itp_type_head_armor   ,0,
 1666 , weight(2)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, 
 [], [fac_kingdom_4,fac_kingdom_7,fac_kingdom_1]],
  
["bascinet_2", "Bascinet with Aventail", [("onion-top_bascinet",0)], itp_merchandise|itp_type_head_armor   ,0, 
 2400 , weight(1.75)|abundance(100)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, 
 [], [fac_kingdom_5,fac_kingdom_1]],
#["bascinet_3", "Bascinet with Nose Guard", [("bascinet_new_b",0)], itp_merchandise|itp_type_head_armor   ,0, 2400 , weight(1.75)|abundance(100)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_5,fac_kingdom_1]],


["bascinet_coif", "bascinet_coif", [("bascinet_coif_01",0)], itp_merchandise|itp_type_head_armor ,0,
 2016 , weight(2)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate
, [], [fac_kingdom_10,fac_kingdom_7,fac_kingdom_1,fac_kingdom_4,fac_kingdom_5]],
 
["zitta_bascinet_novisor", "Bascinet", [("zitta_bascinet_novisor",0)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 2400 , weight(2)|abundance(100)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate 
, [], [fac_kingdom_10,fac_kingdom_7,fac_kingdom_1,fac_kingdom_4,fac_kingdom_5]],

["zitta_bascinet", "Klappvisier Bascinet", [("zitta_bascinet",0)], itp_merchandise| itp_type_head_armor|itp_covers_head | itp_attach_armature,0, 3750 , weight(2.5)|abundance(100)|head_armor(75)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate 
, [], [fac_kingdom_10,fac_kingdom_7,fac_kingdom_1,fac_kingdom_4,fac_kingdom_5]],
  
["barbutte", "barbutte", [("barbutte_01",0)], itp_type_head_armor, 0, 
 3266 , weight(3)|abundance(100)|head_armor(70)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate 
 , [], se_faction],
["barbutte_coif", "barbutte", [("barbutte_coif_01",0)], itp_type_head_armor, 0, 
 3750 , weight(3.5)|abundance(100)|head_armor(75)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate
 , [], se_faction],
 
["visored_bascinet_1", "Full Helm", [("visored_bascinet_01",0)], itp_merchandise| itp_type_head_armor|itp_covers_head ,0, 
 4266 , weight(2.75)|abundance(100)|head_armor(80)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate 
 , [], se_faction],
["visored_bascinet_2", "Full Helm", [("visored_bascinet_02",0)], itp_type_head_armor|itp_covers_head ,0, 
 4266 , weight(2.75)|abundance(100)|head_armor(90)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate 
 , [], se_faction],
 
 
["kettle_hat_3", "Kettle Hat", [("Helmet_E1_01",0)], itp_merchandise| itp_type_head_armor,0,
 1350 , weight(1.5)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate , 
 [], [fac_kingdom_7]],
["combed_morion_blued", "Blued Combed Morion", [("Helmet_E2_01",0)],  itp_type_head_armor   ,0, 
 1666 , weight(1.5)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,  
 [], [fac_kingdom_7]],
["combed_morion", "Combed Morion", [("combed_morion",0)], itp_merchandise| itp_type_head_armor   ,0, 
 2016 , weight(1.5)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,  
 [], [fac_kingdom_7]],
["combed_morion_2", "Combed Morion", [("Helmet_E3_01", 0)], itp_type_head_armor|itp_merchandise, 0, 
 2400 , weight(1.75)|abundance(100)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate , 
 [], [fac_kingdom_7]],
["combed_morion_3", "Combed Morion", [("Helmet_E4_01", 0)], itp_type_head_armor|itp_merchandise, 0, 
 3750 , weight(2.5)|abundance(100)|head_armor(75)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate,
 [], [fac_kingdom_7]],
 
 
["open_sallet", "open_sallet", [("open_sallet",0)], itp_type_head_armor|itp_merchandise, 0, 
 1666 , weight(2)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, 
 [], euro_factions],
["sallet", "sallet", [("visored_salet",0)], itp_type_head_armor|itp_merchandise, 0, 
 2400 , weight(2)|abundance(100)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, 
 [], euro_factions],
 
["open_sallet_coif", "sallet_coif", [("open_sallet_coif",0)], itp_type_head_armor|itp_merchandise, 0, 
 2816 , weight(2.5)|abundance(100)|head_armor(65)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate,
 [], euro_factions],
 
["sallet_coif", "sallet_coif", [("visored_sallet_coif",0)], itp_type_head_armor|itp_merchandise, 0, 
 3750 , weight(2.5)|abundance(100)|head_armor(75)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate,
 [], euro_factions],
["sallet_coif_ger", "sallet_coif", [("sallet_03",0)], itp_type_head_armor|itp_merchandise, 0, 
 3750 , weight(2.5)|abundance(100)|head_armor(75)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate,
 [], euro_factions],
 
["new_sallet", "new_sallet", [("new_sallet",0)], itp_type_head_armor|itp_merchandise|itp_covers_head, 0, 
 5400 , weight(2.75)|abundance(100)|head_armor(90)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, 
 [], euro_factions],
["new_sallet_2", "new_sallet", [("tournament_helmG",0)], itp_type_head_armor|itp_merchandise|itp_covers_head, 0, 
 5400 , weight(2.75)|abundance(100)|head_armor(90)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, 
 [], euro_factions],

["new_sallet_red", "new_sallet", [("sallet_sarleon_01",0)], itp_type_head_armor|itp_merchandise|itp_covers_head, 0, 
 5400 , weight(2.75)|abundance(100)|head_armor(90)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, 
 [], euro_factions],

["sallet_beret_plain_brown", "sallet_beret_plain_brown", [("sallet_beret_plain_brown",0)], itp_type_head_armor|itp_merchandise, 0, 
 1666 , weight(2)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, 
 [], [fac_kingdom_7]],
["sallet_beret_plain_red", "sallet_beret_plain_red", [("sallet_beret_plain_red",0)], itp_type_head_armor|itp_merchandise, 0, 
 1666 , weight(2)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, 
 [], [fac_kingdom_7]],
 
["sallet_beret_plumes_brown", "sallet_beret_plumes_brown", [("sallet_beret_plumes_brown",0)], itp_type_head_armor|itp_merchandise, 0, 
 2816 , weight(2.5)|abundance(100)|head_armor(70)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate,
 [], [fac_kingdom_7]],
["sallet_beret_plumes_red", "sallet_beret_plumes_red", [("sallet_beret_plumes_red",0)], itp_type_head_armor|itp_merchandise, 0, 
 2816 , weight(2.5)|abundance(100)|head_armor(70)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate,
 [], [fac_kingdom_7]],

["maximilian_sallet", "maximilian_sallet", [("helm19",0)], itp_type_head_armor|itp_merchandise|itp_covers_head, 0, 
 5400 , weight(2.75)|abundance(100)|head_armor(90)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, 
[], [fac_kingdom_7]],

["maximilian_sallet_2", "maximilian_sallet", [("helm20",0)], itp_type_head_armor|itp_merchandise|itp_covers_head, 0, 
 5400 , weight(2.75)|abundance(100)|head_armor(90)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, 
 [], [fac_kingdom_7]],

["black_helmet", "Black Helmet", [("black_helm",0)], itp_type_head_armor, 0, 
 3750 , weight(2.5)|abundance(100)|head_armor(75)|body_armor(0)|leg_armor(0)|difficulty(9), imodbits_good_plate
 , [], euro_factions],
  
#["full_helm", "Full Helm", [("2bascinet_new",0)], itp_merchandise| itp_type_head_armor|itp_covers_head ,0, 
# 3750 , weight(2.5)|abundance(100)|head_armor(75)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate,
# ],
 
## CC

["gondor_light_helm","Gondorian_Footman_Helm",[("gondor_footman_helm",0)],itp_type_head_armor|itp_merchandise,0,
 1666 , weight(1.5)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,[],[fac_kingdom_1,fac_hospitalier_knights]],
["gondor_infantry_helm","Gondor_Infantry_Helm",[("gondor_regular_helm",0)],itp_type_head_armor|itp_merchandise,0,
 2400 , weight(1.75)|abundance(100)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,[],[fac_kingdom_1,fac_hospitalier_knights]],
["tower_archer_helm","Tower_Archer_Helm",[("gondor_tower_archer_helm",0)],itp_type_head_armor|itp_merchandise,0,
 2016 , weight(1.5)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,[],[fac_kingdom_1,fac_hospitalier_knights]],

["gondor_knight_helm","Gondor_Knight_Helm",[("gondor_knight_helm",0)],itp_type_head_armor|itp_merchandise,0, 
 4266 , weight(2.75)|abundance(100)|head_armor(80)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate,[],[fac_kingdom_1,fac_hospitalier_knights]],
["gondor_guard_helm","Gondor_Guard_Helm",[("gondor_guard_helm",0)],itp_type_head_armor|itp_merchandise,0, 
  5400 , weight(2.75)|abundance(100)|head_armor(90)|body_armor(0)|leg_armor(0)|difficulty(10),imodbits_plate,[],[fac_kingdom_1,fac_hospitalier_knights]],

["gondor_dolamroth_helm","Dol_Amroth_Helm",[("gondor_dolamroth_helm",0)],itp_type_head_armor|itp_merchandise,0,
 1300,weight(2.5)|head_armor(35)|difficulty(0),imodbits_plate,[],[fac_kingdom_1,fac_hospitalier_knights]],
["gondor_dolamroth_helm_2","Dol_Amroth_Helm",[("dol_helmet",0)],itp_type_head_armor|itp_merchandise|itp_attach_armature,0,
 1300,weight(2.5)|head_armor(35)|difficulty(0),imodbits_plate,[],[fac_kingdom_1,fac_hospitalier_knights]],
["swan_knight_helm","Swan_Knight_Helm",[("gondor_dolamroth_knight_helm",0)],itp_type_head_armor|itp_merchandise,0,
 1500,weight(3)|head_armor(39)|difficulty(0),imodbits_plate,[],[fac_kingdom_1,fac_hospitalier_knights]],

["french_helm_closed", "Armet", [("flemish_armet",0)], itp_type_head_armor|itp_merchandise, 0, 
 4266 , weight(2.75)|abundance(100)|head_armor(80)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, 
 [], euro_factions],
["french_helm_2", "Armet", [("gondor_fountain_helmet",0)], itp_type_head_armor|itp_merchandise, 0, 
 4266 , weight(2.75)|abundance(100)|head_armor(100)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, 
 [], [fac_kingdom_1,fac_hospitalier_knights]],
["french_helm_3", "Armet", [("gondor_lord_helmet",0)], itp_type_head_armor|itp_merchandise|itp_attach_armature, 0, 
 5400 , weight(2.75)|abundance(100)|head_armor(90)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, 
 [], [fac_kingdom_1,fac_hospitalier_knights]],
 
["classichelm_plume", "classichelm_plume", [("classichelm_plume",0)], itp_type_head_armor|itp_merchandise|itp_covers_head, 0, 
 5400 , weight(2.75)|abundance(100)|head_armor(90)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, 
 [], euro_factions],
 
["black_helmet_2", "Black Helmet", [("hm_hlf_s01Y_combined",0)], itp_type_head_armor|itp_covers_head, 0, 
 5400, weight(2.75)|abundance(100)|head_armor(90)|body_armor(0)|leg_armor(0)|difficulty(9), imodbits_good_plate  , [], [fac_demon_hunters, fac_hospitalier_knights]],
 
["great_helmet", "Great Helmet", [("helm6",0)], itp_merchandise| itp_type_head_armor,0, 
 4266 , weight(2.75)|abundance(100)|head_armor(80)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, 
 [], euro_factions],

["great_helmet3", "Great Helmet", [("nordplatehelm",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 
 4266 , weight(2.75)|abundance(100)|head_armor(80)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, 
 [], [fac_kingdom_7,fac_kingdom_4,fac_kingdom_10]],
 
["horned_great_helmet", "horned_great_helmet", [("helmhorn2",0)], itp_type_head_armor|itp_merchandise|itp_covers_head, 0, 
 4266 , weight(2.75)|abundance(100)|head_armor(80)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, 
 [], [fac_kingdom_4,fac_kingdom_13,fac_kingdom_10]],
["horned_great_helmet_2", "horned_great_helmet", [("imrahil_helmet",0)], itp_type_head_armor|itp_merchandise|itp_attach_armature, 0, 
 4266 , weight(2.75)|abundance(100)|head_armor(80)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, 
  [], [fac_kingdom_1]],
  
["empire_helmet1", "Armet", [("empire_helmet1",0)], itp_type_head_armor|itp_merchandise, 0, 
 4266 , weight(2.75)|abundance(100)|head_armor(80)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, 
 [], [fac_kingdom_5,fac_kingdom_8,fac_kingdom_1,fac_kingdom_7]],
["empire_helmet2", "Armet", [("empire_helmet2",0)], itp_type_head_armor|itp_merchandise, 0, 
 4266 , weight(2.75)|abundance(100)|head_armor(80)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, 
 [], [fac_kingdom_5,fac_kingdom_8,fac_kingdom_1,fac_kingdom_7]],
["empire_helmet3", "Armet", [("empire_helmet4",0)], itp_type_head_armor|itp_merchandise, 0, 
 4266 , weight(2.75)|abundance(100)|head_armor(80)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, 
 [], [fac_kingdom_5,fac_kingdom_8,fac_kingdom_1,fac_kingdom_7]],
  
  
["winged_great_helmet", "Winged Great Helmet", [("maciejowski_helmet_new",0)], itp_merchandise|itp_type_head_armor|itp_covers_head,0, 
 5400 , weight(2.75)|abundance(100)|head_armor(90)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, 
 [], euro_factions],
  
["winged_great_helmet_teu", "Winged Great Helmet", [("dol_helmet_knight",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature,0, 
 5400 , weight(2.75)|abundance(100)|head_armor(90)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, 
 [], [fac_kingdom_1,fac_hospitalier_knights]],
["winged_great_helmet_blue", "Winged Great Helmet", [("gondor_captain_helmet_mail",0)], itp_merchandise|itp_type_head_armor,0, 
 5400 , weight(2.75)|abundance(100)|head_armor(90)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, 
 [], [fac_kingdom_1,fac_hospitalier_knights]],
["winged_great_helmet_ger", "Winged Great Helmet", [("great_winged_helm_3",0)], itp_merchandise|itp_type_head_armor|itp_covers_head,0, 
 5400 , weight(2.75)|abundance(100)|head_armor(90)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, 
 [], [fac_kingdom_4,fac_kingdom_13,fac_kingdom_7,fac_kingdom_10]],
  
  
["hounskull", "hounskull", [("hounskull",0)], itp_type_head_armor|itp_merchandise|itp_covers_head, 0, 
 4266 , weight(2.75)|abundance(100)|head_armor(80)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, 
  [], [fac_kingdom_4,fac_kingdom_5,fac_kingdom_7,fac_kingdom_11,fac_kingdom_13,fac_kingdom_1]],
["hounskull_2", "hounskull", [("hounskull_bascinet_01",0)], itp_type_head_armor|itp_merchandise|itp_covers_head, 0, 
 4266 , weight(2.75)|abundance(100)|head_armor(80)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, 
  [], [fac_kingdom_4,fac_kingdom_5,fac_kingdom_7,fac_kingdom_11,fac_kingdom_13,fac_kingdom_1]],
["hounskull_3", "hounskull", [("hounskull_bascinet_02",0)], itp_type_head_armor|itp_merchandise|itp_covers_head, 0, 
 4266 , weight(2.75)|abundance(100)|head_armor(80)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, 
  [], [fac_kingdom_4,fac_kingdom_5,fac_kingdom_7,fac_kingdom_11,fac_kingdom_13,fac_kingdom_1]],

["black_helmet2", "black_helm", [("hm_hlf_s01Y",0)], itp_type_head_armor|itp_covers_head, 0, 
 5400, weight(2.75)|abundance(100)|head_armor(90)|body_armor(0)|leg_armor(0)|difficulty(9), imodbits_good_plate , [], [fac_demon_hunters, fac_hospitalier_knights]],
 
["milanese_sallet", "milanese_sallet", [("milanese_sallet",0)], itp_type_head_armor|itp_merchandise|itp_covers_head, 0, 
 5400 , weight(2.75)|abundance(100)|head_armor(90)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, 
 [], [fac_kingdom_5,fac_kingdom_1,fac_kingdom_11]],
  


 
["deli_turban", "Desert Turban", [("deli_cap",0)], itp_merchandise| itp_type_head_armor| itp_covers_beard ,0, 
 294 , weight(1)|abundance(100)|head_armor(21)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_cloth, 
 [], [fac_kingdom_9]],

 
["black_snake_helm","Maranka_Helm",[("black_snake_helm",0)],itp_type_head_armor|itp_merchandise,0,1400,weight(2)|head_armor(70)|difficulty(0),imodbits_armor, [], tatar_faction],
["harad_heavy_inf_helm","Great_Harad_Helmet",[("harad_heavy_inf_helm",0)],itp_type_head_armor|itp_merchandise,0,1000,weight(2.5)|head_armor(55)|difficulty(0),imodbits_armor, [], tatar_faction],
["harad_eaglehelm","Eagle_Guard_Helm",[("eagle_guard_helmet",0)],itp_type_head_armor|itp_merchandise,0,1400,weight(3)|head_armor(60)|difficulty(0),imodbits_armor, [], tatar_faction],
["lion_helm","Lion_Guard_Helm",[("lion_helm",0)],itp_type_head_armor|itp_merchandise,0,1400,weight(3)|head_armor(50)|difficulty(0),imodbits_armor, [], tatar_faction],

["khergit_helmet", "Khergit Helmet", [("harad_cav_helm_a",0)], itp_type_head_armor|itp_merchandise, 0, 500, weight(2)|abundance(50)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_cloth , [], tatar_faction],
["khergit_war_helmet", "Khergit War Helmet", [("harad_cav_helm_b",0)], itp_type_head_armor|itp_merchandise, 0, 800, weight(2)|abundance(50)|head_armor(40)|body_armor(0)|leg_armor(0), imodbits_cloth, [], tatar_faction],
["khergit_guard_helmet", "Khergit Guard Helmet", [("harad_dragon_helm",0)], itp_type_head_armor|itp_merchandise   ,0, 433 , weight(2)|abundance(50)|head_armor(60)|body_armor(0)|leg_armor(0) ,imodbits_cloth, [], tatar_faction],
["khergit_cavalry_helmet", "Khergit Cavalry Helmet", [("harad_wavy_helm",0)], itp_type_head_armor| itp_merchandise   ,0, 333 , weight(2)|abundance(50)|head_armor(50)|body_armor(0)|leg_armor(0) ,imodbits_cloth, [], tatar_faction],
["khergit_mask", "Khergit War mask", [("harad_finhelm",0)], itp_type_head_armor|itp_merchandise, 0, 2000, weight(2)|abundance(50)|head_armor(70)|body_armor(0)|leg_armor(0), imodbits_cloth, [], tatar_faction],


#WEAPONS
["wooden_stick",         "Wooden Stick", [("wooden_stick",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,50 , weight(2.5)|difficulty(0)|spd_rtng(99)| weapon_length(63)|swing_damage(14 , blunt)| thrust_damage(0 ,  pierce),imodbits_none ],
["cudgel",         "Cudgel", [("club",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 50 , weight(2.5)|difficulty(0)|spd_rtng(99)| weapon_length(69)|swing_damage(15 , blunt)| thrust_damage(0 ,  pierce),imodbits_none, [], [fac_kingdom_13]],
["hammer",         "Hammer", [("iron_hammer_new",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar,50 , weight(2)|difficulty(0)|spd_rtng(100)| weapon_length(58)|swing_damage(20 , blunt)| thrust_damage(0 ,  pierce),imodbits_mace , [], [fac_kingdom_13]],
["club",         "Club", [("club",0)], itp_type_one_handed_wpn|itp_merchandise| itp_can_knock_down|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,50 , weight(2.5)|difficulty(0)|spd_rtng(95)| weapon_length(70)|swing_damage(16 , blunt)| thrust_damage(0 ,  pierce),imodbits_none , [], [fac_kingdom_9,fac_kingdom_3]],
["winged_mace",         "Flanged Mace", [("winged_mace_swup",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,244 , weight(3.5)|difficulty(0)|spd_rtng(90)| weapon_length(71)|swing_damage(33 , blunt)| thrust_damage(0 ,  pierce),imodbits_mace , [], [fac_kingdom_8,fac_kingdom_3,fac_kingdom_5]],
["spiked_mace",         "Spiked Mace", [("spiked_mace_new",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,360 , weight(3.5)|difficulty(0)|spd_rtng(88)| weapon_length(74)|swing_damage(34 , blunt)| thrust_damage(0 ,  pierce),imodbits_pick, [], ee_faction],
["military_hammer", "Military Hammer", [("military_hammer",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,634 , weight(4)|difficulty(0)|spd_rtng(89)| weapon_length(60)|swing_damage(37 , blunt)| thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_kingdom_1,fac_kingdom_5]],

["pickaxe",         "Pickaxe", [("fighting_pick_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,56 , weight(3)|difficulty(0)|spd_rtng(96)| weapon_length(68)|swing_damage(24 , pierce)| thrust_damage(0 ,  pierce),imodbits_pick, [], [fac_kingdom_9]],
["spiked_club",         "Spiked Club", [("spiked_club",0)], itp_type_one_handed_wpn|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,166 , weight(3)|difficulty(0)|spd_rtng(97)| weapon_length(70)|swing_damage(16 , pierce)| thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_kingdom_6]],
["fighting_pick", "Fighting Pick", [("fighting_pick_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,216 , weight(3.5)|difficulty(0)|spd_rtng(94)| weapon_length(70)|swing_damage(25 , pierce)| thrust_damage(0 ,  pierce),imodbits_pick , [], [fac_kingdom_1,fac_kingdom_5,fac_kingdom_7]],
["military_pick", "Military Pick", [("steel_pick_swup",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,560 , weight(4)|difficulty(0)|spd_rtng(90)| weapon_length(65)|swing_damage(26 , pierce)| thrust_damage(0 ,  pierce),imodbits_pick , [], [fac_kingdom_1,fac_kingdom_4,fac_kingdom_5]],


["morningstar",         "Morningstar", [("mace_morningstar_new",0)], itp_can_knock_down|itp_crush_through|itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry|itp_unbalanced, itc_scimitar|itcf_carry_mace_left_hip,610 , weight(5.5)|difficulty(13)|spd_rtng(90)| weapon_length(85)|swing_damage(32 , pierce)| thrust_damage(0 ,  pierce),imodbits_mace , [], [fac_kingdom_1,fac_kingdom_5,fac_kingdom_7]],
["morningstar2",         "Morningstar", [("mace_new",0)], itp_can_knock_down|itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry|itp_unbalanced, itc_morningstar|itcf_carry_mace_left_hip,820 , weight(4.5)|difficulty(10)|spd_rtng(95)| weapon_length(100)|swing_damage(38 , pierce)| thrust_damage(0 ,  pierce),imodbits_mace , [], [fac_kingdom_1,fac_kingdom_11]],


["sickle",         "Sickle", [("sickle",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry|itp_wooden_parry, itc_cleaver,9 , weight(1.5)|difficulty(0)|spd_rtng(99)| weapon_length(54)|swing_damage(22 , cut)| thrust_damage(0 ,  pierce),imodbits_none , [], [fac_kingdom_13]],
["cleaver",         "Cleaver", [("cleaver_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry|itp_wooden_parry, itc_cleaver,14 , weight(1.5)|difficulty(0)|spd_rtng(103)| weapon_length(35)|swing_damage(24 , cut)| thrust_damage(0 ,  pierce),imodbits_none , [], [fac_kingdom_13]],
["knife",         "Knife", [("peasant_knife_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itcf_thrust_onehanded| itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_carry_dagger_front_left,18 , weight(1)|difficulty(0)|spd_rtng(110)| weapon_length(44)|swing_damage(22 , cut)| thrust_damage(20 ,  pierce),imodbits_sword ],
["butchering_knife", "Butchering Knife", [("khyber_knife_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itcf_thrust_onehanded| itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_carry_dagger_front_right,23 , weight(1)|difficulty(0)|spd_rtng(108)| weapon_length(60)|swing_damage(25 , cut)| thrust_damage(30 ,  pierce),imodbits_sword , [], [fac_kingdom_13]],
["dagger",         "Dagger", [("dagger_b",0),("dagger_b_scabbard",ixmesh_carry),("dagger_b",imodbits_good),("dagger_b_scabbard",ixmesh_carry|imodbits_good)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itcf_thrust_onehanded| itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn,37 , weight(1.25)|difficulty(0)|spd_rtng(112)| weapon_length(47)|swing_damage(22 , cut)| thrust_damage(35 ,  pierce),imodbits_sword_high],

["falchion",         "Falchion", [("falchion_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip,368 , weight(2.5)|difficulty(8)|spd_rtng(96)| weapon_length(73)|swing_damage(36 , cut)| thrust_damage(0 ,  pierce),imodbits_sword, [], [fac_kingdom_10,fac_kingdom_5]],

#["grosse_messer", "Military Falchion", [("grosse_messer_b",0),("grosse_messer_b_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise| itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 630 , weight(2.5)|difficulty(9)|spd_rtng(98)| weapon_length(92)|swing_damage(38 , cut)| thrust_damage(24 ,  cut),imodbits_sword_high, [], [fac_kingdom_5]],


["scimitar",         "Scimitar", [("scimitar_a",0),("scab_scimeter_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,1141 , weight(1.5)|difficulty(0)|spd_rtng(104)| weapon_length(97)|swing_damage(35, cut)| thrust_damage(0 ,  pierce),imodbits_sword_high , [], ee_faction+arab_factions],
["scimitar_b",         "Elite Scimitar", [("scimitar_b",0),("scab_scimeter_b", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,1282 , weight(1.5)|difficulty(0)|spd_rtng(104)| weapon_length(100)|swing_damage(37 , cut)| thrust_damage(0 ,  pierce),imodbits_sword_high , [], ee_faction+arab_factions],
["scimitar_long", "Scimitar", [("lui_cimeterre",0),("scab_scimeter",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_extra_penetration, itc_morningstar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1460, weight(2.0)|difficulty(0)|spd_rtng(104)|weapon_length(120)|swing_damage(39,cut)|thrust_damage(0,pierce), imodbit_balanced|imodbit_tempered|imodbit_masterwork| imodbit_deadly| imodbit_sharp, [], ee_faction+arab_factions],
["scimitar_sulatn",         "Damascus_Scimitar", [("damascus_scimitar",0),("scab_damascus_scimitar", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_extra_penetration, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1397 , weight(1.5)|difficulty(0)|spd_rtng(104)| weapon_length(103)|swing_damage(38 , cut)| thrust_damage(0 ,  pierce),imodbits_sword_high , [], ee_faction+arab_factions],


["arabian_sword_a",         "Sarranid Sword", [("arabian_sword_a",0),("scab_arabian_sword_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_extra_penetration, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,963 , weight(1.5)|difficulty(0)|spd_rtng(99)| weapon_length(97)|swing_damage(31 , cut)| thrust_damage(19 ,  pierce),imodbits_sword_high, [], arab_factions],
["arabian_sword_b",         "Sarranid Arming Sword", [("arabian_sword_b",0),("scab_arabian_sword_b", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_extra_penetration, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,931 , weight(1.5)|difficulty(0)|spd_rtng(99)| weapon_length(97)|swing_damage(30 , cut)| thrust_damage(25 ,  pierce),imodbits_sword_high, [], arab_factions],
["sarranid_cavalry_sword",         "Sarranid Cavalry Sword", [("arabian_sword_c",0),("scab_arabian_sword_c", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_extra_penetration, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,1050 , weight(1.75)|difficulty(0)|spd_rtng(98)| weapon_length(105)|swing_damage(34 , cut)| thrust_damage(9 ,  pierce),imodbits_sword_high, [], arab_factions],
["arabian_sword_d",         "Sarranid Guard Sword", [("arabian_sword_d",0),("scab_arabian_sword_d", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_extra_penetration, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,1149 , weight(1.5)|difficulty(0)|spd_rtng(99)| weapon_length(97)|swing_damage(37 , cut)| thrust_damage(20 ,  pierce),imodbit_balanced|imodbit_tempered|imodbit_masterwork| imodbit_deadly| imodbit_sharp, [], arab_factions],


["hatchet",         "Hatchet", [("hatchet",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,50 , weight(2)|difficulty(0)|spd_rtng(87)| weapon_length(48)|swing_damage(21 , pierce)| thrust_damage(0 ,  pierce),imodbits_axe , [], euro_factions],
["hand_axe",         "Hand Axe", [("hatchet",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,50 , weight(2)|difficulty(7)|spd_rtng(85)| weapon_length(50)|swing_damage(23 , pierce)| thrust_damage(0 ,  pierce),imodbits_axe, [], euro_factions],
["fighting_axe", "Fighting Axe", [("fighting_ax",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_extra_penetration|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,150 , weight(2.5)|difficulty(9)|spd_rtng(75)| weapon_length(90)|swing_damage(25 , pierce)| thrust_damage(0 ,  pierce),imodbits_axe , [], euro_factions],
["axe",                 "Axe", [("iron_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,338 , weight(4)|difficulty(8)|spd_rtng(80)| weapon_length(108)|swing_damage(29 , pierce)| thrust_damage(0 ,  pierce),imodbits_axe , [], euro_factions],
["voulge",         "Voulge", [("voulge",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,450 , weight(4.5)|difficulty(8)|spd_rtng(75)| weapon_length(119)|swing_damage(39 , pierce)| thrust_damage(0 ,  pierce),imodbits_axe , [], euro_factions],
["battle_axe",         "Battle Axe", [("battle_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_extra_penetration|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,341 , weight(5)|difficulty(9)|spd_rtng(75)| weapon_length(108)|swing_damage(37 , pierce)| thrust_damage(0 ,  pierce),imodbits_axe , [], euro_factions],
["war_axe",         "War Axe", [("war_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_extra_penetration|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,322 , weight(5)|difficulty(10)|spd_rtng(70)| weapon_length(110)|swing_damage(39 , pierce)| thrust_damage(0 ,  pierce),imodbits_axe , [], euro_factions],




["two_handed_cleaver", "War Cleaver", [("military_cleaver_a",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back,
 1096 , weight(2.75)|difficulty(10)|spd_rtng(93)| weapon_length(120)|swing_damage(45 , cut)| thrust_damage(0 ,  cut),imodbits_sword_high , [], [fac_kingdom_5,fac_kingdom_11]],
["military_cleaver_b", "Soldier's Cleaver", [("military_cleaver_b",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip,
 895 , weight(1.5)|difficulty(0)|spd_rtng(96)| weapon_length(95)|swing_damage(31 , cut)| thrust_damage(0 ,  pierce),imodbits_sword_high ],
["military_cleaver_c", "Military Cleaver", [("military_cleaver_c",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip,
 1011 , weight(1.5)|difficulty(0)|spd_rtng(96)| weapon_length(95)|swing_damage(35 , cut)| thrust_damage(0 ,  pierce),imodbits_sword_high ],

["sword_two_handed_b",         "Two Handed Sword", [("Faradon_twohanded2",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 836 , weight(2.75)|difficulty(10)|spd_rtng(95)| weapon_length(110)|swing_damage(40 , cut)| thrust_damage(37 ,  cut),imodbits_sword_high , [], euro_factions],
#["sword_of_war", "Sword of War", [("b_bastard_sword",0),("scab_bastardsw_b", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn, 524 , weight(3)|difficulty(8)|spd_rtng(93)| weapon_length(125)|swing_damage(53 , cut)| thrust_damage(39 ,  cut),imodbits_sword_high ],

["undead_sword_1", "Long Sword", [("dragonbone_sword1", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 1000 , weight(1.5)|difficulty(0)|spd_rtng(99)| weapon_length(100)|swing_damage(30 , cut)| thrust_damage(25 ,  pierce),imodbits_sword_high, [], [fac_kingdom_5]],

["undead_sword_2", "Longsword", [("dragonbonesword", 0)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 2550 , weight(1.5)|difficulty(0)|spd_rtng(96)| weapon_length(105)|swing_damage(35 , cut)| thrust_damage(25 ,  pierce),imodbits_sword , [], [fac_kingdom_5]],
["undead_scimitar",    "Scimitar", [("dragonbonekatana",0)], itp_merchandise|itp_type_one_handed_wpn|itp_primary, itc_scimitar|itcf_carry_katana, 1500 , weight(1.75)|difficulty(0)|spd_rtng(104)| weapon_length(110)|swing_damage(40 , cut)| thrust_damage(0 ,  pierce),imodbit_balanced|imodbit_tempered|imodbit_masterwork| imodbit_deadly| imodbit_sharp , [], [fac_kingdom_5]],

["undead_sword_two_handed_1", "Two Handed Sword", [("dragonbone_greatsword1",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 836 , weight(2.75)|difficulty(10)|spd_rtng(95)| weapon_length(110)|swing_damage(40 , cut)| thrust_damage(37 ,  cut),imodbits_sword_high , [], [fac_kingdom_5]],
["undead_sword_two_handed_2", "Great Sword", [("dragonbonegreatsword",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 1123 , weight(2.75)|difficulty(10)|spd_rtng(92)| weapon_length(120)|swing_damage(45 , cut)| thrust_damage(39 ,  cut),imodbits_sword_high , [], [fac_kingdom_5]],

["undead_sword_two_handed_3", "Two Handed Sabre", [("dragonbonedaikatana",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back, 1521 , weight(2.75)|difficulty(12)|spd_rtng(100)| weapon_length(116)|swing_damage(44 , cut)| thrust_damage(0 ,  pierce),imodbits_sword_high, [], ee_faction+tatar_faction],
["undead_sword_two_handed_4", "Two Handed Sabre", [("dragonbonenodachi",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back, 1590 , weight(2.75)|difficulty(12)|spd_rtng(95)| weapon_length(145)|swing_damage(46 , cut)| thrust_damage(0 ,  pierce),imodbits_sword_high , [], ee_faction+tatar_faction],


["undead_axe", "Fighting Axe", [("dragonbonewaraxe",0)], itp_merchandise|itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,700 , weight(2.5)|difficulty(9)|spd_rtng(75)| weapon_length(90)|swing_damage(35 , pierce)| thrust_damage(0 ,  pierce),imodbits_axe , [], [fac_kingdom_5] ],

["nordhero_long_axe",      "Nord Hero Great Long Axe", [("nordherobattleaxe",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_extra_penetration|itp_wooden_parry|itp_crush_through|itp_cant_use_on_horseback, itc_nodachi|itcf_carry_axe_back, 8800 , weight(3.8)|difficulty(10)|spd_rtng(98)| weapon_length(127)|swing_damage(50 , pierce)| thrust_damage(0 ,  pierce),imodbits_axe, [], ne_faction],
["nordhero_long_axe_2",      "Nord Hero Great Long Axe", [("rune_nordherobattleaxe",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_extra_penetration|itp_wooden_parry|itp_crush_through|itp_cant_use_on_horseback, itc_nodachi|itcf_carry_axe_back, 6600 , weight(3.8)|difficulty(10)|spd_rtng(100)| weapon_length(127)|swing_damage(55 , pierce)| thrust_damage(0 ,  pierce),imodbits_axe, [], ne_faction],


["nordhero_sword", "Nord Hero War Sword", [("hero_sword_sml",0)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield|itp_extra_penetration|itp_crush_through, itc_longsword|itcf_carry_sword_left_hip, 2000 , weight(1.25)|difficulty(0)|spd_rtng(100)| weapon_length(86)|swing_damage(35 , pierce)| thrust_damage(37, cut),imodbits_sword_high , [], ne_faction] ,
["nordhero_sword_long", "Long Nord Hero War Sword", [("NordHeroSword",0)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield|itp_extra_penetration|itp_crush_through, itc_longsword|itcf_carry_sword_left_hip, 5000 , weight(1.5)|difficulty(0)|spd_rtng(100)| weapon_length(102)|swing_damage(40 , pierce)| thrust_damage(27, pierce),imodbits_sword_high , [], ne_faction] ,

["nordhero_axe_1", "One Handed Battle Axe", [("nordheroaxe",0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield|itp_extra_penetration, itc_scimitar|itcf_carry_axe_left_hip, 2000, weight(2.0)|difficulty(9)|spd_rtng(80)|weapon_length(60)|swing_damage(37,pierce)|thrust_damage(0,pierce), imodbits_axe|imodbit_masterwork , [], ne_faction],
["nordhero_axe_2", "One Handed Battle Axe", [("rune_nordheroaxe",0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield|itp_extra_penetration, itc_scimitar|itcf_carry_axe_left_hip, 5000, weight(2.0)|difficulty(9)|spd_rtng(95)|weapon_length(60)|swing_damage(42,pierce)|thrust_damage(0,pierce), imodbits_axe|imodbit_masterwork , [], ne_faction],


["nordhero_greatsword", "Nord Hero Greatsword", [("NordHeroGreatsword",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through, itc_greatsword|itcf_carry_sword_back, 4000 , weight(2.75)|difficulty(10)|spd_rtng(100)| weapon_length(125)|swing_damage(48 , pierce)| thrust_damage(39 ,  pierce),imodbits_sword_high, [], ne_faction],
["nordhero_greatsword_2", "Nord Hero Greatsword", [("hero_sword_large",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through, itc_greatsword|itcf_carry_sword_back, 5000 , weight(2.75)|difficulty(10)|spd_rtng(100)| weapon_length(125)|swing_damage(53 , pierce)| thrust_damage(44 ,  pierce),imodbits_sword_high, [], ne_faction],

["danish_greatsword", "Danish Greatsword", [("Faradon_twohanded2",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 953 , weight(2.75)|difficulty(10)|spd_rtng(96)| weapon_length(114)|swing_damage(42 , cut)| thrust_damage(33 ,  pierce),imodbits_sword_high, [], ne_faction],

["sword_two_handed_a",         "Great Sword", [("Faradon_twohanded1",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 1123 , weight(2.75)|difficulty(10)|spd_rtng(92)| weapon_length(120)|swing_damage(45 , cut)| thrust_damage(39 ,  cut),imodbits_sword_high , [], euro_factions],
["great_sword",         "Great Sword", [("lui_zweilander",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_crush_through|itp_can_knock_down, itc_claymore, 1479 , weight(2.75)|difficulty(10)|spd_rtng(87)| weapon_length(138)|swing_damage(48 , cut)| thrust_damage(28 ,  pierce),imodbits_sword_high, [], we_faction],

["bastard_sword_a", "Bastard Sword", [("bastard_sword_a",0),("bastard_sword_a_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 937 , weight(2.0)|difficulty(9)|spd_rtng(95)| weapon_length(100)|swing_damage(39 , cut)| thrust_damage(26 ,  pierce),imodbits_sword_high , [], we_faction+ne_faction],
["bastard_sword_b", "Heavy Bastard Sword", [("Faradon_handandahalf",0),("Faradon_handandahalf_scab", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 957 , weight(2.25)|difficulty(9)|spd_rtng(93)| weapon_length(110)|swing_damage(42 , cut)| thrust_damage(27 ,  pierce),imodbits_sword_high , [], we_faction+ne_faction],

["bastard_sword_e", "english_longsword", [("Sword_Empire_I_01",0),("Sword_Empire_I_Scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_back|itcf_show_holster_when_drawn,
 1400 , weight(2.0)|difficulty(9)|spd_rtng(101)| weapon_length(106)|swing_damage(34, pierce)| thrust_damage(30 ,  pierce),imodbits_sword_high , [], ne_faction],
 
["bastard_sword_f", "german_bastard_sword", [("Sword_Empire_H_01", 0), ("Sword_Empire_H_Scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 1387 , weight(1.75)|difficulty(10)|spd_rtng(96)| weapon_length(106)|swing_damage(30 , pierce)| thrust_damage(33 ,  pierce),imodbits_sword_high, [], [fac_kingdom_13,fac_kingdom_7,fac_kingdom_2,fac_kingdom_10,fac_kingdom_1]],

["bastard_sword_c", "Heavy Bastard Sword", [("holy_sword",0)], itp_type_two_handed_wpn|itp_primary|itp_can_penetrate_shield|itp_bonus_against_shield|itp_extra_penetration, itc_bastardsword, 50000 , weight(2.25)|difficulty(15)|spd_rtng(105)| weapon_length(145)|swing_damage(45 , pierce)| thrust_damage(50 ,  pierce),imodbit_balanced|imodbit_tempered|imodbit_masterwork| imodbit_deadly| imodbit_sharp,holy_weapon_trigger, [fac_kingdom_1]],
["bastard_sword_d", "Heavy Bastard Sword", [("sword_repent",0),("sword_repent_scab", ixmesh_carry)], itp_type_two_handed_wpn| itp_primary, itc_bastardsword|itcf_carry_sword_back|itcf_show_holster_when_drawn, 5540 , weight(2.25)|difficulty(15)|spd_rtng(100)| weapon_length(113)|swing_damage(48 , cut)| thrust_damage(35 ,  pierce),imodbit_balanced|imodbit_tempered|imodbit_masterwork| imodbit_deadly| imodbit_sharp, [], [fac_kingdom_5,fac_kingdom_13]],


["skycutter", "Skycutter", [("skycutter",0)], itp_crush_through|itp_type_one_handed_wpn|itp_unique|itp_primary, itc_longsword|itcf_carry_sword_back, 20000 , weight(2.0)|difficulty(9)|spd_rtng(101)| weapon_length(125)|swing_damage(45, pierce)| thrust_damage(32 ,  pierce),imodbits_sword_high],


["bastard_sword_d_fire", "Heavy Bastard Sword", [("sword_blind",0),("spak_book", ixmesh_carry)], itp_type_two_handed_wpn| itp_primary|itp_unique, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 50000 , weight(2.25)|difficulty(10)|spd_rtng(100)| weapon_length(120)|swing_damage(50 , pierce)| thrust_damage(35 ,  pierce),imodbit_balanced|imodbit_tempered|imodbit_masterwork| imodbit_deadly| imodbit_sharp, [(ti_on_init_item, [
(try_begin),
(eq, "$g_weapon_fire_particle", 0),
(set_current_color,600,510,400),(set_position_delta,0,50,0),
(store_trigger_param_2, ":troop_no"),
(troop_is_hero, ":troop_no"),
(particle_system_add_new, "psys_items_fire_white"),(add_point_light, 10, 30),
(try_end),
])]],

["sword_claymore_01",         "Claymore", [("lowlander_sword",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_can_penetrate_shield, itc_claymore,4000 , weight(6)|difficulty(19)|spd_rtng(92)| weapon_length(132)|swing_damage(46 , cut)| thrust_damage(29 ,  pierce),imodbit_balanced|imodbit_tempered|imodbit_masterwork| imodbit_deadly| imodbit_sharp, [], [fac_kingdom_4]],
["sword_claymore_02",         "Claymore", [("scottish_claymore",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_can_penetrate_shield, itc_claymore,4500 , weight(6)|difficulty(19)|spd_rtng(89)| weapon_length(139)|swing_damage(48 , cut)| thrust_damage(22 ,  pierce),imodbit_balanced|imodbit_tempered|imodbit_masterwork| imodbit_deadly| imodbit_sharp, [], [fac_kingdom_4]],



["scottish_claymore",         "scottish_claymore", [("ssdj23",0)], itp_type_two_handed_wpn|itp_primary|itp_can_penetrate_shield|itp_bonus_against_shield|itp_extra_penetration, itc_bastardsword|itcf_carry_sword_back, 50000 , weight(2.5)|difficulty(18)|spd_rtng(100)| weapon_length(150)|swing_damage(46 , pierce)| thrust_damage(50 ,  pierce),imodbits_sword_high , dragon_weapon_trigger, [fac_kingdom_8]],


["sword_two_handed_c", "Great Sword", [("lui_greatswordc",0)], itp_crush_through|itp_type_polearm|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_can_penetrate_shield|itp_next_item_as_melee, itc_staff|itcf_carry_sword_back|itcf_horseback_slash_polearm, 1743, weight(2.75)|difficulty(12)|spd_rtng(85)|weapon_length(135)|swing_damage(45,cut)|thrust_damage(30,pierce), imodbit_balanced|imodbit_tempered|imodbit_masterwork| imodbit_deadly| imodbit_sharp, [], [fac_kingdom_7]],
["sword_two_handed_c_alt", "Great Sword", [("lui_greatswordc",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_can_penetrate_shield, itc_nodachi|itcf_carry_sword_back, 1743, weight(2.75)|difficulty(12)|spd_rtng(80)|weapon_length(125)|swing_damage(45,pierce)|thrust_damage(0,pierce), imodbit_balanced|imodbit_tempered|imodbit_masterwork| imodbit_deadly| imodbit_sharp, [], [fac_kingdom_7]],

["flamberge",         "Flamberge Zweihander", [("flamberge",0)], itp_crush_through|itp_type_polearm|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_can_penetrate_shield|itp_next_item_as_melee|itp_can_knock_down, itc_staff|itcf_carry_sword_back, 2445 , weight(3.75)|difficulty(15)|spd_rtng(82)| weapon_length(150)|swing_damage(53, cut)| thrust_damage(28 ,  pierce),imodbit_balanced|imodbit_tempered|imodbit_masterwork| imodbit_deadly| imodbit_sharp, [], [fac_kingdom_7]],
["flamberge_alt",         "Flamberge Zweihander", [("flamberge",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_crush_through|itp_can_knock_down|itp_cant_use_on_horseback|itp_can_penetrate_shield, itc_nodachi|itcf_carry_sword_back, 2445 , weight(3.75)|difficulty(15)|spd_rtng(82)| weapon_length(150)|swing_damage(53, pierce)| thrust_damage(0 ,  pierce),imodbit_balanced|imodbit_tempered|imodbit_masterwork| imodbit_deadly| imodbit_sharp, [], [fac_kingdom_13,fac_kingdom_7]],


["one_handed_war_axe_a", "One Handed Axe", [("one_handed_war_axe_a",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 309 , weight(1.5)|difficulty(9)|spd_rtng(83)| weapon_length(60)|swing_damage(31 , pierce)| thrust_damage(0 ,  pierce),imodbits_axe , [], ne_faction],
["one_handed_battle_axe_a", "One Handed Battle Axe", [("one_handed_battle_axe_a",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 332 , weight(1.5)|difficulty(9)|spd_rtng(81)| weapon_length(62)|swing_damage(32 , pierce)| thrust_damage(0 ,  pierce),imodbits_axe, [], ne_faction],
["one_handed_war_axe_b", "One Handed War Axe", [("one_handed_war_axe_b",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_extra_penetration|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 376 , weight(1.5)|difficulty(9)|spd_rtng(81)| weapon_length(65)|swing_damage(33 , pierce)| thrust_damage(0 ,  pierce),imodbits_axe , [], ne_faction],
["one_handed_battle_axe_b", "One Handed Battle Axe", [("one_handed_battle_axe_b",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_extra_penetration|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 332 , weight(1.75)|difficulty(9)|spd_rtng(81)| weapon_length(61)|swing_damage(33 , pierce)| thrust_damage(0 ,  pierce),imodbits_axe, [], ne_faction],
["one_handed_battle_axe_c", "One Handed Battle Axe", [("one_handed_battle_axe_c",0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield|itp_extra_penetration, itc_scimitar|itcf_carry_axe_left_hip, 550, weight(2.0)|difficulty(9)|spd_rtng(80)|weapon_length(60)|swing_damage(34,pierce)|thrust_damage(0,pierce), imodbits_axe|imodbit_masterwork , [], ne_faction],
["knightaxe", "knightaxe", [("euro_axe_01",0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield|itp_extra_penetration, itc_scimitar|itcf_carry_axe_left_hip, 477, weight(2.5)|difficulty(12)|spd_rtng(82)|weapon_length(90)|swing_damage(35,pierce)|thrust_damage(0,pierce), imodbits_axe|imodbit_masterwork , [], ne_faction],
["burning_axe", "The Burning Axe of Sankis", [("two_handed_dwarf_axe_1", 0)], itp_type_one_handed_wpn|itp_unique|itp_wooden_parry|itp_primary|itp_bonus_against_shield, itc_scimitar|itcf_carry_axe_left_hip, 20000, weight(4)|abundance(100)|difficulty(9)|weapon_length(107)|spd_rtng(90)|swing_damage(45, pierce)|thrust_damage(0, pierce), imodbits_axe, []], 
["slaughter_axe", "Axe of Slaughter", [("orc_dualbattleaxe",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unique|itp_can_knock_down|itp_crush_through|itp_extra_penetration, itc_nodachi|itcf_carry_axe_left_hip, 20000 , weight(18)|difficulty(12)|spd_rtng(90) | weapon_length(125)|swing_damage(50 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],

["dwarf_spanner", "Dwarven_Runic_Spanner", [("dw_spanner", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield, itc_nodachi|itcf_carry_axe_back, 825, weight(9.)|abundance(100)|difficulty(12)|weapon_length(99)|spd_rtng(90)|swing_damage(38, blunt)|thrust_damage(0, pierce), imodbits_axe, [], [fac_kingdom_10]], 
  
["dwarf_axe", "Dwarven_Axe", [("one_handed_dwarf_axe_1", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield, itc_scimitar|itcf_carry_axe_left_hip, 51, weight(2.)|abundance(100)|difficulty(7)|weapon_length(54)|spd_rtng(94)|swing_damage(32, pierce)|thrust_damage(0, pierce), imodbits_axe, [], [fac_kingdom_10]], 
["dwarf_hand_axe", "Dwarven_One_Handed_Axe", [("one_handed_dwarf_axe_2", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield, itc_scimitar|itcf_carry_axe_left_hip, 77, weight(2.500000)|abundance(100)|difficulty(7)|weapon_length(58)|spd_rtng(93)|swing_damage(35, pierce)|thrust_damage(0, pierce), imodbits_axe, [], [fac_kingdom_10]], 
["dwarf_fighting_axe", "Dwarven_Fighting_Axe", [("one_handed_dwarf_axe_3", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield, itc_scimitar|itcf_carry_axe_left_hip, 150, weight(2.500000)|abundance(100)|difficulty(9)|weapon_length(63)|spd_rtng(95)|swing_damage(33, pierce)|thrust_damage(0, pierce), imodbits_axe, [], [fac_kingdom_10]], 


["dwarf_battle_axe", "Dwarven_Battle_Axe", [("one_handed_dwarf_axe_5", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield, itc_scimitar|itcf_carry_axe_left_hip, 610, weight(2.500000)|abundance(100)|difficulty(11)|weapon_length(60)|spd_rtng(95)|swing_damage(38, pierce)|thrust_damage(0, pierce), imodbits_axe, [], [fac_kingdom_10]], 
["dwarf_runic_axe", "Dwarven_Runic_Axe", [("one_handed_dwarf_axe_4", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield, itc_scimitar|itcf_carry_axe_left_hip, 570, weight(2.500000)|abundance(100)|difficulty(9)|weapon_length(57)|spd_rtng(95)|swing_damage(37, pierce)|thrust_damage(0, pierce), imodbits_axe, [], [fac_kingdom_10]], 
["dwarf_iron_axe", "Dwarven_Iron_Axe", [("one_handed_dwarf_axe_6", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield, itc_scimitar|itcf_carry_axe_left_hip, 560, weight(1.750000)|abundance(100)|difficulty(10)|weapon_length(62)|spd_rtng(102)|swing_damage(36, pierce)|thrust_damage(0, pierce), imodbits_axe, [], [fac_kingdom_10]], 
["dwarf_lordrunic_axe", "Dwarven_Lord_Runic_Axe", [("one_handed_dwarf_axe_7", 0)], itp_type_one_handed_wpn|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield, itc_scimitar|itcf_carry_axe_left_hip, 760, weight(1.750000)|abundance(100)|difficulty(13)|weapon_length(62)|spd_rtng(105)|swing_damage(54, pierce)|thrust_damage(0, pierce), imodbits_axe, [], [fac_kingdom_10]], 
  
["dwarf_long_axe", "Dwarven_Two_Handed_Axe", [("two_handed_dwarf_axe_1", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 455, weight(4.)|abundance(100)|difficulty(10)|weapon_length(107)|spd_rtng(88)|swing_damage(45, pierce)|thrust_damage(0, pierce), imodbits_axe, [], [fac_kingdom_10]], 
["dwarf_long_axe_2", "Dwarven_Lord_Great_Axe", [("two_handed_dwarf_axe_2", 0)], itp_type_two_handed_wpn|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield, itc_nodachi|itcf_carry_axe_back, 950, weight(4.500000)|abundance(100)|difficulty(12)|weapon_length(115)|spd_rtng(90)|swing_damage(51, pierce)|thrust_damage(0, pierce), imodbits_axe, [], [fac_kingdom_2]], 
["dwarf_long_axe_3", "Dwarven_Slayer_Axe", [("two_handed_dwarf_axe_4", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield, itc_nodachi|itcf_carry_axe_back, 690, weight(4.)|abundance(100)|difficulty(12)|weapon_length(90)|spd_rtng(86)|swing_damage(55, pierce)|thrust_damage(0, pierce), imodbits_axe, [], [fac_kingdom_10]], 
["dwarf_long_axe_4", "Dwarven_Dragon_Axe", [("two_handed_dwarf_axe_3", 0)], itp_type_two_handed_wpn|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield, itc_nodachi|itcf_carry_axe_back, 30000, weight(4.500000)|abundance(100)|difficulty(13)|weapon_length(98)|spd_rtng(86)|swing_damage(60, pierce)|thrust_damage(0, pierce), imodbits_axe], 

["two_handed_axe",         "Two Handed Axe", [("two_handed_battle_axe_a",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 429 , weight(2.7)|difficulty(10)|spd_rtng(75)| weapon_length(90)|swing_damage(38 , pierce)| thrust_damage(0 ,  pierce),imodbits_axe , [], ne_faction],
["two_handed_battle_axe_2",         "Two Handed War Axe", [("two_handed_battle_axe_b",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 454 , weight(2.75)|difficulty(10)|spd_rtng(74)| weapon_length(92)|swing_damage(40 , pierce)| thrust_damage(0 ,  pierce),imodbits_axe, [], ne_faction],
["shortened_voulge",         "Shortened Voulge", [("two_handed_battle_axe_c",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_extra_penetration|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 533 , weight(3)|difficulty(10)|spd_rtng(68)| weapon_length(100)|swing_damage(47 , pierce)| thrust_damage(0 ,  pierce),imodbits_axe , [], euro_factions],
["great_axe",         "Great Axe", [("two_handed_battle_axe_e",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_extra_penetration|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 564 , weight(2.9)|difficulty(10)|spd_rtng(71)| weapon_length(96)|swing_damage(48 , pierce)| thrust_damage(0 ,  pierce),imodbits_axe, [], ne_faction],
["long_axe", "Long Axe", [("long_axe_a",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_next_item_as_melee, itc_staff|itcf_carry_axe_back, 390, weight(3.6)|difficulty(10)|spd_rtng(80)|weapon_length(120)|swing_damage(53,cut)|thrust_damage(21,pierce), imodbits_axe, [], ne_faction],
["long_axe_alt",         "Long Axe", [("long_axe_a",0)],itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced|itp_crush_through, itc_nodachi|itcf_carry_axe_back, 390 , weight(3.6)|difficulty(10)|spd_rtng(68)| weapon_length(120)|swing_damage(50 , pierce)| thrust_damage(0 ,  pierce),imodbits_axe, [], ne_faction],
["long_axe_b", "Long War Axe", [("long_axe_b",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_extra_penetration|itp_next_item_as_melee, itc_staff|itcf_carry_axe_back, 510, weight(3.75)|difficulty(10)|spd_rtng(80)|weapon_length(125)|swing_damage(57,cut)|thrust_damage(23,pierce), imodbits_axe, [], ne_faction],
["long_axe_b_alt",         "Long War Axe", [("long_axe_b",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_extra_penetration|itp_wooden_parry|itp_unbalanced|itp_crush_through, itc_nodachi|itcf_carry_axe_back, 510 , weight(3.75)|difficulty(10)|spd_rtng(65)| weapon_length(125)|swing_damage(53 , pierce)| thrust_damage(0 ,  pierce),imodbits_axe, [], ne_faction],
["long_axe_c", "Great Long Axe", [("long_axe_c",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_extra_penetration|itp_next_item_as_melee, itc_staff|itcf_carry_axe_back, 660, weight(3.8)|difficulty(10)|spd_rtng(80)|weapon_length(127)|swing_damage(60,cut)|thrust_damage(21,pierce), imodbits_axe|imodbit_masterwork, [], ne_faction],
["long_axe_c_alt",      "Great Long Axe", [("long_axe_c",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_extra_penetration|itp_wooden_parry|itp_unbalanced|itp_crush_through, itc_nodachi|itcf_carry_axe_back, 660 , weight(3.8)|difficulty(10)|spd_rtng(65)| weapon_length(127)|swing_damage(55 , pierce)| thrust_damage(0 ,  pierce),imodbits_axe, [], ne_faction],

["greataxe_adjudgment", "Great_Axe:Adjudgment", [("greataxe_adjudgment",0)], itp_type_two_handed_wpn|itp_primary|itp_two_handed|itp_bonus_against_shield|itp_extra_penetration|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 2000 , weight(7)|difficulty(15)|spd_rtng(88)| weapon_length(122)|swing_damage(50 , pierce)| thrust_damage(0 ,  pierce),imodbits_axe|imodbit_masterwork ],

["long_axe_d", "Great Long Axe", [("greataxe_adjudgment",0)], itp_type_polearm|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_next_item_as_melee|itp_can_penetrate_shield|itp_can_knock_down|itp_crush_through|itp_extra_penetration|itp_unique, itc_staff|itcf_carry_axe_back, 50000, weight(4)|difficulty(10)|spd_rtng(86)|weapon_length(120)|swing_damage(57,cut)|thrust_damage(34,pierce), imodbits_axe|imodbit_masterwork],
["long_axe_d_alt",      "Great Long Axe", [("greataxe_adjudgment",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced|itp_can_penetrate_shield|itp_can_knock_down|itp_crush_through|itp_extra_penetration|itp_unique, itc_nodachi|itcf_carry_axe_back, 50000 , weight(4)|difficulty(10)|spd_rtng(86)| weapon_length(120)|swing_damage(57 , cut)| thrust_damage(0 ,  pierce),imodbits_axe ],


["chaos_axe", "Chaos Axe", [("lod_WAoRChaosAxeC",0),("lod_WAoRChaosAxeC", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield|itp_extra_penetration|itp_unique,  itc_scimitar|itcf_carry_axe_left_hip,  50000, weight(2.0)|difficulty(9)|spd_rtng(95)|weapon_length(85)|swing_damage(45,pierce)|thrust_damage(0,pierce), imodbits_axe|imodbit_masterwork ,[(ti_on_init_item, [
(try_begin),
(eq, "$g_weapon_fire_particle", 0),
(set_position_delta,0,60,0),
(store_trigger_param_2, ":troop_no"),
(troop_is_hero, ":troop_no"),
(particle_system_add_new, "psys_item_blood_Drop"),
(try_end),
])]],
["double_axe", "Double Axe", [("d_axe",0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_can_knock_down|itp_crush_through|itp_unbalanced|itp_extra_penetration, itc_nodachi|itcf_carry_axe_back, 959, weight(12)|difficulty(22)|spd_rtng(90)|weapon_length(97)|swing_damage(55,pierce)|thrust_damage(20,pierce), imodbits_axe|imodbit_masterwork, [], ne_faction],

["bardiche", "Bardiche", [("two_handed_battle_axe_d",0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_two_handed|itp_bonus_against_shield|itp_unbalanced|itp_crush_through, itc_morningstar|itcf_carry_axe_back, 291, weight(4.75)|difficulty(10)|spd_rtng(72)|weapon_length(102)|swing_damage(47,pierce)|thrust_damage(0,pierce), imodbits_axe|imodbit_masterwork, [], ee_faction],
["great_bardiche", "Great Bardiche", [("two_handed_battle_axe_f",0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_extra_penetration|itp_can_penetrate_shield|itp_unbalanced|itp_crush_through, itc_morningstar|itcf_carry_axe_back, 617, weight(5.0)|difficulty(10)|spd_rtng(65)|weapon_length(116)|swing_damage(49,pierce)|thrust_damage(0,pierce), imodbits_axe|imodbit_masterwork , [], ee_faction],

["cav_axe", "Cavalry_axe", [("euro_axe_01", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_bonus_against_shield|itp_crush_through, itc_morningstar|itcf_carry_axe_back, 500, weight(2.5)|weapon_length(80)|difficulty(12)|spd_rtng(83)|swing_damage(43, pierce)|thrust_damage(0, pierce), imodbits_axe|imodbit_masterwork, [], ee_faction],
["cav_bardiche", "Cavalry_Bardiche", [("euro_axe_02", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_bonus_against_shield|itp_crush_through, itc_morningstar|itcf_carry_axe_back, 500, weight(3)|weapon_length(90)|difficulty(12)|spd_rtng(80)|swing_damage(45, pierce)|thrust_damage(0, pierce), imodbits_axe|imodbit_masterwork, [], ee_faction],

["long_bardiche", "Long Bardiche", [("two_handed_battle_long_axe_b",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_can_knock_down|itp_crush_through|itp_cant_use_on_horseback, itc_staff|itcf_carry_axe_back, 390, weight(4.5)|difficulty(8)|spd_rtng(77)|weapon_length(140)|swing_damage(48,pierce)|thrust_damage(20,pierce), imodbits_axe|imodbit_masterwork, [], ee_faction],
["great_long_bardiche", "Great Long Bardiche", [("two_handed_battle_long_axe_c",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_extra_penetration|itp_can_penetrate_shield|itp_can_knock_down|itp_can_penetrate_shield|itp_crush_through|itp_cant_use_on_horseback, itc_staff|itcf_carry_axe_back, 660, weight(5.0)|difficulty(10)|spd_rtng(70)|weapon_length(155)|swing_damage(50,pierce)|thrust_damage(20,pierce), imodbits_axe|imodbit_masterwork, [], ee_faction],

["hafted_blade_b", "Hafted Blade", [("khergit_pike_b",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield, itc_guandao|itcf_carry_spear, 185, weight(2.75)|difficulty(10)|spd_rtng(83)|weapon_length(130)|swing_damage(51,cut)|thrust_damage(20,pierce), imodbits_polearm|imodbit_masterwork, [], tatar_faction],
["hafted_blade_a", "Hafted Blade", [("khergit_pike_a",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield, itc_guandao|itcf_carry_spear, 350, weight(3.25)|difficulty(10)|spd_rtng(75)|weapon_length(153)|swing_damage(54,cut)|thrust_damage(19,pierce), imodbits_polearm|imodbit_masterwork, [], tatar_faction],

["hafted_blade_c", "Hafted Blade", [("lui_khegitnagita",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield, itc_cutting_spear|itcf_carry_spear, 10000, weight(3.25)|difficulty(15)|spd_rtng(85)|weapon_length(187)|swing_damage(59,pierce)|thrust_damage(23,pierce), imodbits_polearm|imodbit_masterwork, [], tatar_faction],

["serpent_sword", "Serpent Sword", [("SerpentSword",0),("SerpentSword", ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_can_penetrate_shield|itp_unique, itc_claymore,50000 , weight(2.5)|difficulty(12)|spd_rtng(110)| weapon_length(140)|swing_damage(45 , pierce)| thrust_damage(28 ,  pierce),imodbit_balanced|imodbit_masterwork, ],
["natalya_slayer", "Natalya's Slayer", [("quick_crossbow",0)], itp_unique|itp_type_crossbow|itp_primary|itp_is_magic_staff, itcf_shoot_crossbow, 20000, weight(3)|spd_rtng(50)|shoot_speed(100)|thrust_damage(65,pierce)|max_ammo(6), imodbits_crossbow , [], [fac_beast]],


["death_grip", "Death of grip", [("barf_skeleton_handL",0)], itp_type_hand_armor|itp_unique, 0, 20000, weight(1.25)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(0)|difficulty(15), imodbits_armor ],
["death_finger", "Montes finger", [("draugr_handL",0)], itp_type_hand_armor|itp_unique, 0, 20000, weight(0.25)|abundance(100)|head_armor(10)|body_armor(10)|leg_armor(10)|difficulty(12), imodbits_armor ],
["drakons_lesson","Drakon's Lesson", [("sigma_zuoshou1_L",0)], itp_type_hand_armor|itp_unique,0,  20000, weight(2.25)|abundance(100)|body_armor(15)|difficulty(12),imodbits_armor, ],
["giant_gauntlets","Gauntlets of Giant Strength", [("amade_steel_gauntlet_L",0)], itp_type_hand_armor|itp_unique,0,  20000, weight(2.25)|abundance(100)|body_armor(15)|difficulty(12),imodbits_armor, ],
["marksman_gloves","marksman Gloves", [("glove4_L",0)], itp_type_hand_armor|itp_unique,0,  20000, weight(0.25)|abundance(120)|body_armor(2)|difficulty(12),imodbits_cloth, ],
["armlet_mordiggian", "Armlet of Mordiggian", [("knight_of_molag_bal_hand_L",0)], itp_type_hand_armor|itp_unique, 0, 20000, weight(0.25)|abundance(100)|head_armor(10)|body_armor(10)|leg_armor(10)|difficulty(0), imodbits_armor ],
["satanic_hand","satanic", [("Glove_Khorne_L",0)], itp_unique|itp_type_hand_armor,0,  20000, weight(1)|abundance(100)|body_armor(10)|difficulty(0),imodbits_armor, [], [fac_kingdom_9,fac_demon]],

["barrier_leg", "BARRIER_leg", [("Boots_Khorne",0)], itp_unique|itp_type_foot_armor|itp_attach_armature ,0,  20000 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(50)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_9,fac_demon]],



["fast_travel_boot", "Fast travel boots", [("boot4",0)], itp_unique| itp_type_foot_armor|itp_civilian| itp_attach_armature ,0, 
 20000 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(24)|difficulty(9) ,imodbits_cloth ], 
["guard_kneecops", "guard's Kneecops", [("hose_kneecops_red",0)], itp_unique| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 20000 , weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(12) ,imodbits_cloth],
["rider_boots", "Rus Cavalry Boots", [("high_boots_cav",0)], itp_unique| itp_type_foot_armor|itp_civilian| itp_attach_armature ,0, 
 20000 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(12) ,imodbits_cloth ],
["nilfurs_boast", "Nilfur's Boast", [("twilight_boots",0)],  itp_unique|itp_type_foot_armor| itp_attach_armature,0, 
 20000 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(40)|difficulty(12) ,imodbits_plate ],

["vanguard_shield", "Vanguard_shield", [("Black_d",0)], itp_type_shield|itp_unique, itcf_carry_kite_shield,  50000 , weight(2)|shield_hit_points(5000)|body_armor(125)|spd_rtng(100)|shield_width(150)|difficulty(5),imodbits_shield],

["akarats_awakening","Akarat's Awakening",[("denethor_shield",0)],itp_unique|itp_type_shield|itp_wooden_parry,itcf_carry_kite_shield,50000,weight(2.5)|hit_points(20000)|body_armor(92)|spd_rtng(82)|shield_width(40)|shield_height(90),imodbits_shield, Akarat_hit_trigger, []],
["hellskull", "Hellskull", [("Shield_Khorne", 0)], itp_unique|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 20000, weight(4.)|abundance(100)|difficulty(0)|hit_points(20000)|body_armor(100)|spd_rtng(85)|shield_width(90), imodbits_shield, Hellskull_hit_trigger, []], 
["freeze_shield", "Freeze of Deflection", [("glass_shield",0)], itp_unique|itp_type_shield, itcf_carry_round_shield,  20000 , weight(1)|difficulty(5)|shield_hit_points(20000)|body_armor(90)|spd_rtng(120)|shield_width(50)|shield_height(60),imodbits_shield , freeze_shield_hit_trigger, [fac_elf, fac_kingdom_4,fac_forest_ranger]],
["dragon_shield_2", "Dragon Shield", [("fix_EOS_knight_shield",0)], itp_type_shield|itp_unique, itcf_carry_kite_shield,  20000 , weight(2)|shield_hit_points(5000)|body_armor(125)|spd_rtng(100)|shield_width(40)|shield_height(60)|difficulty(6),imodbits_shield , dragon_shield_2_hit_trigger, []],

["tynan_dagger", "Tynan's Dagger", [("fix_copy_sword17_a",0)], itp_type_shield|itp_unique|itp_force_attach_left_hand, 0, 20000 , weight(1)|hit_points(5000)|body_armor(100)|spd_rtng(150)|shield_width(50)|shield_height(100)|difficulty(3),imodbits_shield,tynan_dagger_trigger ],
["frostfang", "Frost fang", [("Frostfang",0),("Frostfang_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_unique, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 50000 , weight(1.5)|difficulty(9)|spd_rtng(96)| weapon_length(105)|swing_damage(40 , pierce)| thrust_damage(25 ,  pierce),imodbits_sword_high , [(ti_on_init_item, [
(try_begin),
(eq, "$g_weapon_fire_particle", 0),
(set_position_delta,0,50,0),
(store_trigger_param_2, ":troop_no"),
(troop_is_hero, ":troop_no"),
(particle_system_add_new, "psys_frostfang_snowflake"),
(particle_system_add_new, "psys_frostfang_smoke"),
(try_end),
])]],
["kwan_dao", "Kwan Dao", [("wushuang_weapon_qinlongdao",0)], itp_type_polearm|itp_unique|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield, itc_guandao|itcf_carry_spear, 20000, weight(2.75)|difficulty(12)|spd_rtng(100)|weapon_length(170)|swing_damage(50,pierce)|thrust_damage(20,pierce), imodbits_polearm|imodbit_masterwork, [], tatar_faction],
["avalon_halberd", "Avalon_Halberd", [("glassHalberd",0)], itp_unique|itp_type_polearm|itp_wooden_parry|itp_two_handed|itp_primary|itp_crush_through|itp_extra_penetration|itp_couchable|itp_crush_through|itp_bonus_against_shield, itc_guandao, 20000, weight(2.5)|difficulty(20)|spd_rtng(120)|weapon_length(180)|swing_damage(50,pierce)|thrust_damage(50,pierce), imodbits_polearm|imodbit_masterwork , [], [fac_forest_ranger,fac_kingdom_4,fac_culture_4]],

["golem_crusher", "Golem Crusher", [("stahlrimwarhammer",0)], itp_can_knock_down|itp_crush_through|itp_type_two_handed_wpn|itp_unique|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear,20000 , weight(9)|difficulty(12)|spd_rtng(100)| weapon_length(70)|swing_damage(80 , blunt)| thrust_damage(0 ,  pierce),imodbits_mace],

["blinding_sand", "Blinding Sand", [("ygrayne",0)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_crush_through|itp_can_knock_down|itp_can_penetrate_shield, itc_scimitar|itcf_carry_sword_left_hip, 20000 , weight(1.75)|difficulty(12)|spd_rtng(115)| weapon_length(115)|swing_damage(45 , pierce),imodbits_sword_high ],
["soul_stealer", "Soul Stealer", [("ebony_longsword",0)], itp_unique|itp_type_one_handed_wpn|itp_primary|itp_crush_through|itp_extra_penetration|itp_can_penetrate_shield, itc_longsword|itcf_carry_sword_back, 20000 , weight(2)|difficulty(9)|spd_rtng(100)| weapon_length(113)|swing_damage(45 , pierce)| thrust_damage(32 ,  pierce),imodbits_sword_high, [], [fac_undeads_2,fac_beast]],
["morrigan", "Morrigan Blade", [("Morrigan",0)], itp_type_one_handed_wpn|itp_primary|itp_unique, itc_longsword, 50000 , weight(1.5)|difficulty(12)|spd_rtng(100)| weapon_length(120)|swing_damage(40 , pierce)| thrust_damage(25 ,  pierce),imodbits_sword_high , [], ne_faction],
["gwilith", "Gwilith", [("gwilith_1h", 0), ("gwilith_1h_sheath", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield|itp_unique|itp_next_item_as_melee, itc_scimitar|itcf_show_holster_when_drawn|itcf_carry_wakizashi, 50000, weight(2)|weapon_length(118)|difficulty(12)|spd_rtng(115)|abundance(100)|swing_damage(40, pierce), imodbits_sword_high ,[
 (ti_on_weapon_attack, 
  [
   (store_trigger_param_1, ":shooter"),
   (call_script,"script_cf_agent_cleave",":shooter", 1, 0),
  ]),
 (ti_on_init_item, 
  [
  (eq, "$g_weapon_fire_particle", 0),
  (set_position_delta,0,55,0),
  (store_trigger_param_2, ":troop_no"),
  (troop_is_hero, ":troop_no"),
  (particle_system_add_new, "psys_frostfang_smoke"),
 ])
]],
["gwilith_2", "Gwilith", [("gwilith_1h", 0), ("gwilith_1h_sheath", ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unique, itc_morningstar|itcf_show_holster_when_drawn|itcf_carry_wakizashi, 50000, weight(2)|weapon_length(140)|difficulty(12)|spd_rtng(120)|abundance(100)|swing_damage(50, pierce), imodbits_sword_high ,[
 (ti_on_weapon_attack, 
  [
   (store_trigger_param_1, ":shooter"),
   (call_script,"script_cf_agent_cleave",":shooter", 1, 0),
  ]),
 (ti_on_init_item, 
  [
  (eq, "$g_weapon_fire_particle", 0),
  (set_position_delta,0,55,0),
  (store_trigger_param_2, ":troop_no"),
  (troop_is_hero, ":troop_no"),
  (particle_system_add_new, "psys_frostfang_smoke"),
 ])
]],

["frankenstein_head","The skull of Frankenstein",[("draugr_head",0)],itp_unique|itp_type_fullhelm,0,20000,weight(2)|head_armor(30)|difficulty(0),imodbits_plate,],

["stone_mask","Stone mask",[("ribun_maskm_0",0)],itp_unique|itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair|itp_fit_to_head,0,50000,weight(2)|head_armor(90)|difficulty(15),imodbits_plate,],
["mages_shade", "Dark Mage's Shade", [("wizard_black_hat",0)],  itp_unique|itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair ,0, 20000 , weight(1)|abundance(100)|head_armor(31)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_cloth],

["sword_medieval_a", "medieval Sword", [("sword_medieval_b",0),("sword_medieval_b_scabbard", ixmesh_carry),("sword_rusty_a",imodbit_rusty),("sword_rusty_a_scabbard", ixmesh_carry|imodbit_rusty)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 893 , weight(1.5)|difficulty(0)|spd_rtng(99)| weapon_length(95)|swing_damage(30 , cut)| thrust_damage(22 ,  pierce),imodbits_sword_high , [], euro_factions],

["sword_medieval_b", "Espada Eslavona", [("Sword_Empire_L_01",0),("Sword_Empire_L_Scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 907 , weight(1)|difficulty(0)|spd_rtng(104)| weapon_length(95)|swing_damage(33 ,  cut)| thrust_damage(25 ,  pierce),imodbits_sword_high , [], [fac_kingdom_1,fac_kingdom_7]],

["sword_medieval_b_small", "Highlander Sword", [("Sword_Empire_B_01",0),("Sword_Empire_B_Scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 874 , weight(1.5)|difficulty(0)|spd_rtng(108)| weapon_length(81)|swing_damage(37, cut)| thrust_damage(26, pierce),imodbits_sword_high , [], [fac_kingdom_1,fac_kingdom_4]],

["sword_medieval_c", "Arming Sword", [("Sword_Empire_G_01",0),("Sword_Empire_G_Scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 953 , weight(1.5)|difficulty(0)|spd_rtng(99)| weapon_length(95)|swing_damage(35 , cut)| thrust_damage(27 ,  pierce),imodbits_sword_high, [], [fac_kingdom_5,fac_kingdom_7]],

["sword_medieval_c_small", "Short Arming Sword", [("Sword_Empire_K_01",0),("Sword_Empire_K_Scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 806 , weight(1.5)|difficulty(0)|spd_rtng(103)| weapon_length(80)|swing_damage(50, cut)| thrust_damage(30, pierce),imodbits_sword_high, [], [fac_kingdom_5,fac_kingdom_7]],

["sword_medieval_c_long", "Long Sword", [("Sword_Empire_E_01", 0), ("Sword_Empire_E_Scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1000 , weight(1.5)|difficulty(0)|spd_rtng(99)| weapon_length(100)|swing_damage(44 , cut)| thrust_damage(25 ,  pierce),imodbits_sword_high, [], [fac_kingdom_4]],

["sword_medieval_d_long", "Crusader's Longsword", [("Sword_Empire_F_01", 0), ("Sword_Empire_F_Scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 2550 , weight(1.5)|difficulty(0)|spd_rtng(96)| weapon_length(105)|swing_damage(40 , cut)| thrust_damage(25 ,  pierce),imodbits_sword , [], [fac_kingdom_13,fac_kingdom_1]],


["amroth_sword_a","Dol_Amroth_Sword",[("DA_sword_a",0),("scab_DA_sword_a",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_crush_through,itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,3000,weight(1.25)|difficulty(0)|spd_rtng(105)|weapon_length(88)|swing_damage(35,pierce)|thrust_damage(21,pierce),imodbits_sword, [], [fac_kingdom_1,fac_hospitalier_knights]],
["amroth_sword_b","Dol_Amroth_Knight_Sword",[("DA_sword_b",0),("scab_DA_sword_b",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_crush_through|itp_bonus_against_shield,itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,4000,weight(2)|difficulty(0)|spd_rtng(99)|weapon_length(100)|swing_damage(40,pierce)|thrust_damage(26,pierce),imodbits_sword_high, [], [fac_kingdom_1,fac_hospitalier_knights]],
["amroth_sword_c","Dol_Amroth_Heavy_Sword",[("DA_bastard",0),("scab_DA_bastard",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_crush_through|itp_bonus_against_shield,itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,7000,weight(2.25)|difficulty(0)|spd_rtng(96)|weapon_length(105)|swing_damage(45,pierce)|thrust_damage(26,pierce),imodbits_sword_high, [], [fac_kingdom_1,fac_hospitalier_knights]],
["gondor_ranger_sword","Gondor_Ranger_Sword",[("gondor_bastard",0),("scab_gondor_citadel",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary,itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,2550,weight(2)|difficulty(0)|spd_rtng(100)|weapon_length(105)|swing_damage(40,cut)|thrust_damage(26,pierce),imodbits_sword, [], [fac_kingdom_1,fac_hospitalier_knights]],
["gondor_citadel_sword","Gondor_Citadel_Sword",[("gondor_citadel",0),("scab_gondor_citadel",ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_crush_through|itp_bonus_against_shield,itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,6000,weight(1.25)|difficulty(0)|spd_rtng(100)|weapon_length(100)|swing_damage(36,pierce)|thrust_damage(30,pierce),imodbits_sword_high, [], [fac_kingdom_1,fac_hospitalier_knights]],

["longbowman_sword", "Archer's Sword", [("Sword_Empire_A_01", 0), ("Sword_Empire_A_Scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,955 , weight(1.0)|difficulty(0)|spd_rtng(99)| weapon_length(88)|swing_damage(28 , cut)| thrust_damage(21 ,  pierce),imodbits_sword_high , [], euro_factions],

["longsword", "Nordland_Sword", [("Sword_Empire_C_01", 0), ("Sword_Empire_C_Scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise| itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 758 , weight(2.0)|difficulty(9)|spd_rtng(97)| weapon_length(80)|swing_damage(45 , cut)| thrust_damage(29 ,  pierce),imodbits_sword_high , [], euro_factions],



["espada_eslavona_b", "Espada Eslavona", [("Reitschwert_Pistolier_B_01", 0), ("Reitschwert_Scabbard_Pistolier_B_01", ixmesh_carry)], itp_type_one_handed_wpn|itp_secondary|itp_primary|itp_extra_penetration|itp_crush_through, itc_longsword|itcf_carry_sword_left_hip, 2500 , weight(1.5)|difficulty(0)|spd_rtng(115)| weapon_length(108)|swing_damage(35 , pierce)| thrust_damage(40 ,  pierce),imodbits_sword_high , [], [fac_kingdom_1,fac_kingdom_11]],
["side_sword", "Side-sword", [("Reitschwert_Pistolier_C_01", 0), ("Reitschwert_Scabbard_Pistolier_C_01", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_secondary|itp_primary|itp_extra_penetration|itp_crush_through, itc_side_sword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,1010 , weight(1.5)|difficulty(0)|spd_rtng(98)| weapon_length(100)|swing_damage(40 , cut)| thrust_damage(33 ,  pierce),imodbits_sword_high , [], se_faction],
["rapierd", "Rapierd", [("Reitschwert_Pistolier_D_01", 0), ("Reitschwert_Scabbard_Pistolier_D_01", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_secondary|itp_primary|itp_extra_penetration|itp_crush_through, itc_side_sword|itcf_carry_sword_left_hip,1201, weight(1.5)|difficulty(0)|spd_rtng(99)|weapon_length(105)|swing_damage(35,cut)|thrust_damage(40,pierce), imodbit_balanced|imodbit_tempered|imodbit_masterwork| imodbit_deadly| imodbit_sharp, [], se_faction],



["sword_viking_1", "Nordic Sword", [("sword_viking_c",0),("sword_viking_c_scabbard ", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 993 , weight(1.5)|difficulty(0)|spd_rtng(98)| weapon_length(96)|swing_damage(33 , cut)| thrust_damage(21, pierce),imodbits_sword_high , [], ne_faction] ,
["sword_viking_2", "Nordic Sword", [("sword_viking_b",0),("sword_viking_b_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 972 , weight(1.5)|difficulty(0)|spd_rtng(95)| weapon_length(95)|swing_damage(33 , cut)| thrust_damage(24, pierce),imodbits_sword_high , [], ne_faction] ,
["sword_viking_2_small", "Nordic Short Sword", [("sword_viking_b_small",0),("sword_viking_b_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1500 , weight(1.25)|difficulty(0)|spd_rtng(100)| weapon_length(85)|swing_damage(36, pierce)| thrust_damage(35 , cut),imodbits_sword_high, [], ne_faction] ,
["sword_viking_3", "Nordic War Sword", [("sword_viking_a",0),("sword_viking_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1057 , weight(1.5)|difficulty(0)|spd_rtng(95)| weapon_length(95)|swing_damage(39 , cut)| thrust_damage(27, pierce),imodbits_sword_high , [], ne_faction] ,
["sword_viking_3_small", "Nordic Short War Sword", [("sword_viking_a_small",0),("sword_viking_a_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 2000 , weight(1.25)|difficulty(0)|spd_rtng(100)| weapon_length(86)|swing_damage(30 , pierce)| thrust_damage(37, cut),imodbits_sword_high , [], ne_faction] ,
["sword_viking_3_long", "Long Nordic War Sword", [("sword_viking_a_long",0),("sword_viking_a_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 5000 , weight(1.5)|difficulty(0)|spd_rtng(93)| weapon_length(102)|swing_damage(37 , pierce)| thrust_damage(27, pierce),imodbits_sword_high , [], ne_faction] ,

#["sword_viking_c_long", "sword_viking_c_long", [("sword_viking_c_long",0),("sword_viking_c_long_scabbard ", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
# 142 , weight(1.5)|difficulty(0)|spd_rtng(95)| weapon_length(105)|swing_damage(27 , cut)| thrust_damage(19 ,  pierce),imodbits_sword ] ,

["sword_khergit_1", "Nomad Sabre", [("khergit_sword_b",0),("khergit_sword_b_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 961 , weight(1.25)|difficulty(0)|spd_rtng(100)| weapon_length(86)|swing_damage(39 , cut),imodbits_sword_high , [], ee_faction+tatar_faction],
["sword_khergit_2", "Sabre", [("khergit_sword_c",0),("khergit_sword_c_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1022 , weight(1.5)|difficulty(0)|spd_rtng(99)| weapon_length(88)|swing_damage(40 , cut),imodbits_sword_high , [], ee_faction+tatar_faction],
["sword_khergit_3", "Sabre", [("khergit_sword_a",0),("khergit_sword_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1024 , weight(1.5)|difficulty(0)|spd_rtng(99)| weapon_length(87)|swing_damage(41 , cut),imodbits_sword_high , [], ee_faction+tatar_faction],
["sword_khergit_4", "Heavy Sabre", [("khergit_sword_d",0),("khergit_sword_d_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1138 , weight(1.75)|difficulty(0)|spd_rtng(98)| weapon_length(88)|swing_damage(42 , cut),imodbits_sword_high , [], ee_faction+tatar_faction],
["sword_khergit_5", "Harad_Scimitar", [("horandor_a",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 961 , weight(1.25)|difficulty(0)|spd_rtng(100)| weapon_length(100)|swing_damage(30 , pierce),imodbits_sword_high , [], tatar_faction],
["sword_khergit_6", "Harad_Heavy_Falchion", [("black_snake_sword",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 1024 , weight(1.5)|difficulty(0)|spd_rtng(99)| weapon_length(87)|swing_damage(32 , pierce),imodbits_sword_high , [], tatar_faction],
["sword_khergit_7", "Harad_Heavy_Sabre", [("harad_heavy_sword",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 1138 , weight(1.75)|difficulty(0)|spd_rtng(98)| weapon_length(98)|swing_damage(35 , pierce),imodbits_sword_high , [], tatar_faction],

["khergit_sword_two_handed_a",         "Two Handed Sabre", [("khergit_sword_two_handed_a",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back, 1521 , weight(2.75)|difficulty(12)|spd_rtng(96)| weapon_length(120)|swing_damage(44 , cut)| thrust_damage(0 ,  pierce),imodbits_sword_high, [], ee_faction+tatar_faction],
["khergit_sword_two_handed_b",         "Two Handed Sabre", [("khergit_sword_two_handed_b",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back, 1590 , weight(2.75)|difficulty(12)|spd_rtng(96)| weapon_length(120)|swing_damage(46 , cut)| thrust_damage(0 ,  pierce),imodbits_sword_high , [], ee_faction+tatar_faction],

["strange_sword", "Strange Sword", [("katana",0),("katana_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_primary, itc_morningstar|itcf_carry_katana|itcf_show_holster_when_drawn, 1679, weight(2.0)|difficulty(9)|spd_rtng(115)|weapon_length(95)|swing_damage(41,cut), imodbit_balanced|imodbit_tempered|imodbit_masterwork| imodbit_deadly| imodbit_sharp ],
["strange_great_sword", "Strange Great Sword", [("no_dachi",0),("no_dachi_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back|itcf_show_holster_when_drawn, 1920, weight(3.5)|difficulty(12)|spd_rtng(100)|weapon_length(125)|swing_damage(51,cut)|thrust_damage(0,pierce), imodbit_balanced|imodbit_tempered|imodbit_masterwork| imodbit_deadly| imodbit_sharp ],
["strange_short_sword", "Strange Short Sword", [("wakizashi",0),("wakizashi_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_wakizashi|itcf_show_holster_when_drawn, 1321, weight(1.25)|difficulty(0)|spd_rtng(115)|weapon_length(65)|swing_damage(35,cut), imodbit_balanced|imodbit_tempered|imodbit_masterwork| imodbit_deadly| imodbit_sharp ],

["mace_1",         "Spiked Club", [("mace_d",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 455 , weight(1.5)|difficulty(0)|spd_rtng(96)| weapon_length(70)|swing_damage(29 , pierce)| thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_kingdom_7]],
["mace_2",         "Knobbed_Mace", [("mace_a",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 498 , weight(2.5)|difficulty(0)|spd_rtng(98)| weapon_length(70)|swing_damage(31 , blunt)| thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_kingdom_5,fac_kingdom_7]],
["mace_3",         "Spiked Mace", [("mace_c",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 528 , weight(2.5)|difficulty(0)|spd_rtng(98)| weapon_length(70)|swing_damage(33 , blunt)| thrust_damage(0 ,  pierce),imodbits_mace , [], [fac_kingdom_8,fac_kingdom_9]],
["mace_4",         "Winged_Mace", [("mace_b",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 544 , weight(2.5)|difficulty(0)|spd_rtng(98)| weapon_length(70)|swing_damage(35 , blunt)| thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_kingdom_8,fac_kingdom_9]],
["mace_redhandle", "Mace", [("rrr_mace1",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 516 , weight(2)|difficulty(10)|spd_rtng(96)| weapon_length(79)|swing_damage(37 , blunt)| thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_kingdom_8,fac_kingdom_5]],
["mace_knobbedlong", "Mace", [("AN_whammer01",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 536 , weight(3)|difficulty(0)|spd_rtng(95)| weapon_length(80)|swing_damage(39 , blunt)| thrust_damage(0 ,  pierce),imodbits_mace , [], [fac_kingdom_5,fac_kingdom_7]],
["mace_woodenhandle", "Mace", [("rrr_mace4",0)], itp_type_one_handed_wpn|itp_merchandise|itp_can_knock_down| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 460 , weight(2)|difficulty(10)|spd_rtng(96)| weapon_length(73)|swing_damage(41 , blunt)| thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_kingdom_9,fac_kingdom_3,fac_kingdom_5]],

["empire_warhammer", "Warhammer", [("rrr_mace3",0)], itp_type_one_handed_wpn|itp_can_knock_down| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 653 , weight(2)|difficulty(10)|spd_rtng(92)| weapon_length(90)|swing_damage(40 , blunt)| thrust_damage(0 ,  pierce),imodbits_mace],

["great_mace", "Great Mace", [("war_mace_2",0)], itp_can_knock_down|itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_crush_through|itp_unbalanced, itc_morningstar|itcf_carry_axe_back, 382, weight(6)|difficulty(13)|spd_rtng(90)|weapon_length(105)|swing_damage(37,blunt)|thrust_damage(0,pierce), imodbits_mace , [], [fac_kingdom_5]],
["maul",         "Maul", [("maul_b",0)], itp_can_knock_down|itp_crush_through|itp_type_two_handed_wpn|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear,97 , weight(6)|difficulty(8)|spd_rtng(87)| weapon_length(69)|swing_damage(41 , blunt)| thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_kingdom_5]],
["sledgehammer", "Sledgehammer", [("maul_c",0)], itp_can_knock_down|itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear,101 , weight(7)|difficulty(10)|spd_rtng(86)| weapon_length(67)|swing_damage(46, blunt)| thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_kingdom_5]],

["warhammer",         "Great Hammer", [("maul_d",0)], itp_can_knock_down|itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear,290 , weight(9)|difficulty(14)|spd_rtng(83)| weapon_length(68)|swing_damage(50 , blunt)| thrust_damage(0 ,  pierce),imodbits_mace],
# Goedendag
["club_with_spike_head",  "Spiked Staff", [("mace_e",0)],  itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_wooden_parry, itc_bastardsword|itcf_carry_axe_back, 200 , weight(2.5)|difficulty(9)|spd_rtng(72)| weapon_length(117)|swing_damage(26 , blunt)| thrust_damage(24 ,  pierce),imodbits_mace , [], [fac_kingdom_5]],








["pitch_fork",         "Pitch Fork", [("pitch_fork",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear, 19 , weight(1.5)|difficulty(0)|spd_rtng(87)| weapon_length(154)|swing_damage(0 , cut)| thrust_damage(23 ,  pierce),imodbits_polearm, [], all_factions],
["military_fork", "Military Fork", [("military_fork",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_spear, 153 , weight(2)|difficulty(0)|spd_rtng(95)| weapon_length(135)|swing_damage(0 , cut)| thrust_damage(28 ,  pierce),imodbits_polearm, [], all_factions],
["battle_fork",         "Battle Fork", [("battle_fork",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_spear, 282 , weight(2.2)|difficulty(0)|spd_rtng(90)| weapon_length(144)|swing_damage(0, cut)| thrust_damage(35 ,  pierce),imodbits_polearm , [], all_factions],
["boar_spear",         "Boar Spear", [("spear",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_shortened_spear|itcf_carry_spear,76 , weight(1.5)|difficulty(0)|spd_rtng(90)| weapon_length(157)|swing_damage(26 , cut)| thrust_damage(23 ,  pierce),imodbits_polearm, [], all_factions],

["shortened_spear",         "Shortened Spear", [("spear_g_1-9m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_spear|itcf_carry_spear,
 200 , weight(2.0)|difficulty(0)|spd_rtng(102)| weapon_length(120)|swing_damage(19 , blunt)| thrust_damage(40 ,  pierce),imodbits_polearm, [], [fac_kingdom_10,fac_kingdom_4,fac_kingdom_7]],
["spear",         "Spear", [("spear_h_2-15m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_spear|itcf_carry_spear,
 200 , weight(2.25)|difficulty(0)|spd_rtng(98)| weapon_length(135)|swing_damage(20 , blunt)| thrust_damage(35 ,  pierce),imodbits_polearm , [], [fac_kingdom_1,fac_kingdom_3,fac_kingdom_4,fac_kingdom_5,fac_kingdom_9,fac_kingdom_10]],
["war_spear",         "War Spear", [("spear_i_2-3m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_spear|itcf_carry_spear, 200 , weight(2.5)|difficulty(0)|spd_rtng(95)| weapon_length(150)|swing_damage(20 , blunt)| thrust_damage(32 ,  pierce),imodbits_polearm, [], [fac_kingdom_9,fac_kingdom_1,fac_kingdom_4,fac_kingdom_5]],



["bamboo_spear",         "Bamboo Spear", [("arabian_spear_a_3m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear|itcf_carry_spear, 80 , weight(2.0)|difficulty(0)|spd_rtng(88)| weapon_length(200)|swing_damage(15 , blunt)| thrust_damage(30 ,  pierce),imodbits_polearm, [], [fac_kingdom_9]],

["double_sided_lance", "Double Sided Lance", [("lance_dblhead",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_glaive, 261 , weight(4.0)|difficulty(0)|spd_rtng(95)| weapon_length(128)|swing_damage(25, cut)| thrust_damage(41 ,  pierce),imodbits_polearm ],

["light_lance",         "Light Lance", [("spear_b_2-75m",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 180 , weight(4.5)|difficulty(0)|spd_rtng(85)| weapon_length(175)|swing_damage(16 , cut)| thrust_damage(28 ,  pierce),imodbits_polearm , [], all_factions],
["lance",         "Lance", [("spear_d_2-8m",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 270 , weight(4.75)|difficulty(0)|spd_rtng(80)| weapon_length(180)|swing_damage(16 , cut)| thrust_damage(30 ,  pierce),imodbits_polearm , [], all_factions],
["heavy_lance",         "Heavy Lance", [("spear_f_2-9m",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_pike, 360 , weight(5)|difficulty(8)|spd_rtng(75)| weapon_length(190)|swing_damage(16 , cut)| thrust_damage(33 ,  pierce),imodbits_polearm , [], all_factions],
["gondor_tower_spear","Gondorian_Tower_Spear",[("gondor_tower_spear",0)],itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_penalty_with_shield|itp_wooden_parry,itc_staff,600,weight(2.35)|difficulty(0)|spd_rtng(99)|weapon_length(180)|swing_damage(25,cut)|thrust_damage(37,pierce),imodbits_polearm, [], [fac_kingdom_1]],
["gondor_lance","Gondor_Lance",[("amroth_lance",0)],itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_penalty_with_shield|itp_wooden_parry,itc_pike,400,weight(2.35)|difficulty(8)|spd_rtng(89)|weapon_length(204)|swing_damage(20,blunt)|thrust_damage(40,pierce),imodbits_polearm, [], [fac_kingdom_1]],
["double_sided_lance_long", "Long Double Sided Lance", [("lance_dblhead_long",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff, 461 , weight(4.0)|difficulty(12)|spd_rtng(95)| weapon_length(175)|swing_damage(25, cut)| thrust_damage(41 ,  pierce),imodbits_polearm , [], [fac_kingdom_8]],


["sipah_lance",         "sipah Lance", [("spear_f_2-9m",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_pike, 360 , weight(5)|difficulty(8)|spd_rtng(75)| weapon_length(195)|swing_damage(16 , cut)| thrust_damage(43 ,  pierce),imodbits_polearm , [], arab_factions],

["khergit_lance", "khergit lance", [("lui_khergitpike",0)], itp_type_polearm|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield|itp_offset_lance|itp_couchable|itp_crush_through, itc_staff|itcf_horseback_slash_polearm, 2450, weight(2.75)|difficulty(15)|spd_rtng(83)|weapon_length(235)|swing_damage(52,cut)|thrust_damage(40,pierce), imodbits_polearm , [], arab_factions+tatar_faction],

["great_lance", "Great Lance", [("heavy_lance_swup",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_couchable|itp_crush_through, itc_greatlance, 2000, weight(5)|difficulty(10)|spd_rtng(55)|weapon_length(240)|swing_damage(0,cut)|thrust_damage(41,pierce), imodbits_polearm , [], we_faction+se_faction+ne_faction],
["jousting_lance", "Jousting Lance", [("joust_of_peace",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_couchable|itp_crush_through, itc_greatlance, 2000 , weight(5)|difficulty(0)|spd_rtng(60)| weapon_length(240)|swing_damage(0 , cut)| thrust_damage(30 ,  cut)|abundance(10),imodbits_polearm , [], we_faction+se_faction+ne_faction],
["gothic_lance", "gothic_lance", [("lance",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_couchable|itp_crush_through|itp_bonus_against_shield, itc_greatlance, 3000, weight(5)|difficulty(10)|spd_rtng(80)|weapon_length(240)|swing_damage(0,cut)|thrust_damage(45,pierce)|abundance(30), imodbits_polearm , [], we_faction+se_faction+ne_faction],
["great_lance_dark", "Great Lance", [("KTSR220",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_couchable|itp_crush_through, itc_greatlance, 3000, weight(5)|difficulty(12)|spd_rtng(55)|weapon_length(320)|swing_damage(0,cut)|thrust_damage(40,pierce)|abundance(30), imodbits_polearm , [], we_faction+ne_faction],
["great_lance2", "Great Lance", [("KTS444F",0)], itp_type_polearm|itp_unique|itp_primary|itp_bonus_against_shield|itp_penalty_with_shield|itp_couchable|itp_crush_through, itc_greatlance, 50000, weight(7)|difficulty(14)|spd_rtng(90)|weapon_length(380)|swing_damage(0,cut)|thrust_damage(100,pierce)|abundance(30), imodbits_polearm, [], ee_faction],

["hussar_lance_short", "Great Lance", [("pol_gusar_lansa_c",0)], itp_type_polearm|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_penalty_with_shield|itp_couchable|itp_crush_through, itc_greatlance, 3000, weight(8)|difficulty(7)|spd_rtng(60)|weapon_length(280)|swing_damage(0,cut)|thrust_damage(31,pierce)|abundance(50), imodbits_polearm, [], [fac_kingdom_8]],

["hussar_lance", "Great Lance", [("pol_gusar_lansa_b",0)], itp_type_polearm|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_penalty_with_shield|itp_couchable|itp_crush_through, itc_greatlance, 2000, weight(15)|difficulty(7)|spd_rtng(60)|weapon_length(320)|swing_damage(0,cut)|thrust_damage(35,pierce)|abundance(30), imodbits_polearm, [], [fac_kingdom_8]],
["hussar_lance_2", "Great Lance", [("pol_gusar_lansa_a",0)], itp_type_polearm|itp_primary|itp_bonus_against_shield|itp_penalty_with_shield|itp_couchable|itp_crush_through, itc_greatlance, 4000, weight(7)|difficulty(18)|spd_rtng(50)|weapon_length(400)|swing_damage(0,cut)|thrust_damage(35,pierce)|abundance(30), imodbits_polearm, [], [fac_kingdom_2]],

["pike",         "Pike", [("spear_a_3m",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_is_pike|itp_extra_penetration, itc_pike, 500 , weight(4)|difficulty(0)|spd_rtng(75)| weapon_length(245)|swing_damage(0 , cut)| thrust_damage(35 ,  pierce),imodbits_polearm , [], [fac_kingdom_8,fac_kingdom_10,fac_kingdom_1,fac_kingdom_7]],
["pike_2",         "Pike", [("spear_a_3-50m",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_is_pike|itp_extra_penetration, itc_pike, 500 , weight(5)|difficulty(0)|spd_rtng(75)| weapon_length(310)|swing_damage(0 , cut)| thrust_damage(33 ,  pierce),imodbits_polearm , [], [fac_kingdom_8,fac_kingdom_10,fac_kingdom_1,fac_kingdom_7]],
["long_pike", "long_pike", [("spear_a_4m",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield|itp_cant_use_on_horseback|itp_is_pike|itp_extra_penetration, itc_pike, 500, weight(7)|difficulty(0)|spd_rtng(75)|weapon_length(400)|swing_damage(0,cut)|thrust_damage(30,pierce), imodbits_polearm , [], [fac_kingdom_8,fac_kingdom_7]],
["long_pike_2", "long_pike", [("300spear",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield|itp_cant_use_on_horseback|itp_is_pike|itp_extra_penetration, itc_pike, 500, weight(9)|difficulty(0)|spd_rtng(75)|weapon_length(500)|swing_damage(0,cut)|thrust_damage(28,pierce), imodbits_polearm , [], [fac_kingdom_7]],

#["pike",         "Pike", [("spear_a_3m",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_greatlance, 500 , weight(4)|difficulty(0)|spd_rtng(80)| weapon_length(245)|swing_damage(0 , cut)| thrust_damage(35 ,  pierce),imodbits_polearm , [], [fac_kingdom_8,fac_kingdom_10,fac_kingdom_1,fac_kingdom_7]],
#["pike_2",         "Pike", [("spear_a_3-50m",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_greatlance, 500 , weight(5)|difficulty(0)|spd_rtng(75)| weapon_length(310)|swing_damage(0 , cut)| thrust_damage(35 ,  pierce),imodbits_polearm , [], [fac_kingdom_8,fac_kingdom_10,fac_kingdom_1,fac_kingdom_7]],
#["long_pike", "long_pike", [("spear_a_4m",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield|itp_cant_use_on_horseback, itc_greatlance, 500, weight(7)|difficulty(0)|spd_rtng(70)|weapon_length(400)|swing_damage(0,cut)|thrust_damage(35,pierce), imodbits_polearm , [], [fac_kingdom_8,fac_kingdom_7]],
#["long_pike_2", "long_pike", [("asd3",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield|itp_cant_use_on_horseback, itc_greatlance, 500, weight(9)|difficulty(0)|spd_rtng(65)|weapon_length(500)|swing_damage(0,cut)|thrust_damage(35,pierce), imodbits_polearm , [], [fac_kingdom_7]],

["ashwood_pike", "Ashwood Pike", [("pike",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry|itp_is_pike, itc_pike, 205 , weight(3.5)|difficulty(8)|spd_rtng(81)| weapon_length(170)|swing_damage(19,blunt)|thrust_damage(29, pierce),imodbits_polearm , [], all_factions],
["awlpike",    "Awlpike", [("awl_pike_b",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear|itcf_carry_spear, 345 , weight(2)|difficulty(0)|spd_rtng(95)| weapon_length(165)|swing_damage(20 , blunt)| thrust_damage(33 ,  pierce),imodbits_polearm, [], [fac_kingdom_7]],
["awlpike_long",  "Long Awlpike", [("awl_pike_a",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike, itc_spear|itcf_carry_spear, 385 , weight(2)|difficulty(0)|spd_rtng(92)| weapon_length(185)|swing_damage(20 , blunt)| thrust_damage(32 ,  pierce),imodbits_polearm, [], [fac_kingdom_7]],


["staff",         "Staff", [("wooden_staff",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_long_glaive|itcf_carry_sword_back, 36 , weight(1.5)|difficulty(0)|spd_rtng(100)| weapon_length(130)|swing_damage(18 , blunt)| thrust_damage(19 ,  blunt),imodbits_polearm , [], [fac_kingdom_13]],
["quarter_staff", "Quarter Staff", [("quarter_staff",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_long_glaive|itcf_carry_sword_back, 60 , weight(2)|difficulty(0)|spd_rtng(104)| weapon_length(140)|swing_damage(20 , blunt)| thrust_damage(20 ,  blunt),imodbits_polearm],
["iron_staff",         "Iron Staff", [("iron_staff",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield, itc_long_glaive|itcf_carry_sword_back, 202 , weight(2)|difficulty(0)|spd_rtng(97)| weapon_length(140)|swing_damage(25 , blunt)| thrust_damage(26 ,  blunt),imodbits_polearm, [], [fac_kingdom_13]],

["scythe",         "Scythe", [("scythe_swup",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_long_glaive|itcf_carry_spear, 172 , weight(2)|difficulty(0)|spd_rtng(97)| weapon_length(182)|swing_damage(30 , cut)| thrust_damage(25 ,  cut),imodbits_polearm , [], ee_faction],
["military_scythe",         "Military Scythe", [("spear_e_2-5m",0),("spear_c_2-5m",imodbits_bad)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_long_glaive|itcf_carry_spear, 620 , weight(2.5)|difficulty(0)|spd_rtng(80)| weapon_length(155)|swing_damage(41 , cut)| thrust_damage(28 ,  pierce),imodbits_polearm, [], ee_faction],


["glaive", "Glaive", [("glaive_b",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed|itp_is_glaive, itc_glaive|itcf_carry_spear, 1408, weight(4.5)|difficulty(0)|spd_rtng(79)|weapon_length(157)|swing_damage(41,cut)|thrust_damage(21,pierce), imodbits_polearm|imodbit_masterwork , [], [fac_kingdom_8,fac_kingdom_1]],
["glaive_a",  "Glaive", [("Halberd_Light_B_01",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed|itp_is_glaive, itc_glaive|itcf_carry_spear, 1380 , weight(4.5)|difficulty(9)|spd_rtng(82)| weapon_length(168)|swing_damage(39, cut)| thrust_damage(28 ,  pierce),imodbits_polearm, [], [fac_kingdom_10]],
["glaive_b",  "Glaive", [("Halberd_Light_D_01",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed|itp_is_glaive, itc_glaive|itcf_carry_spear, 1380 , weight(4.5)|difficulty(12)|spd_rtng(82)| weapon_length(190)|swing_damage(39, cut)| thrust_damage(28 ,  pierce),imodbits_polearm, [], [fac_kingdom_10]],
["poleaxe",         "Poleaxe", [("halbert_hypocritical",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed|itp_is_glaive, itc_glaive|itcf_carry_spear, 1536 , weight(4)|difficulty(12)|spd_rtng(90)| weapon_length(130)|swing_damage(37 , pierce)| thrust_damage(21 ,  pierce),imodbits_polearm, [], ne_faction],



["guisarme",         "guisarme", [("Halberd_Light_C_01",0)], itp_type_polearm|itp_crush_through|itp_merchandise| itp_primary|itp_wooden_parry|itp_is_glaive, itc_guisarme, 2283 , weight(6.5)|difficulty(10)|spd_rtng(70)| weapon_length(170)|swing_damage(32 , pierce)| thrust_damage(32 ,  pierce),imodbits_polearm, [], [fac_kingdom_9,fac_kingdom_4]],
["guisarme_2",         "guisarme", [("Halberd_Light_A_01",0)], itp_type_polearm|itp_crush_through|itp_merchandise| itp_primary|itp_wooden_parry|itp_is_glaive, itc_guisarme, 1959 , weight(6.5)|difficulty(10)|spd_rtng(70)| weapon_length(150)|swing_damage(34 , pierce)| thrust_damage(32 ,  pierce),imodbits_polearm, [], [fac_kingdom_9,fac_kingdom_4]],
["english_bill", "Bill", [("english_bill",0)], itp_type_polearm|itp_merchandise|itp_can_knock_down|itp_crush_through|itp_primary|itp_two_handed|itp_wooden_parry|itp_is_glaive, itc_cutting_spear, 2724 , weight(6.0)|difficulty(10)|spd_rtng(75)| weapon_length(200)|swing_damage(28 , pierce)| thrust_damage(28 ,  pierce),imodbits_axe, [], [fac_kingdom_4]], 



["german_poleaxe", "german_poleaxe", [("Halberd_Medium_B_01",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_crush_through|itp_cant_use_on_horseback|itp_bonus_against_shield|itp_extra_penetration, itc_glaive|itcf_carry_spear, 3265, weight(4)|difficulty(0)|spd_rtng(78)|weapon_length(131)|swing_damage(40,pierce)|thrust_damage(35,pierce), imodbits_polearm|imodbit_masterwork, [], [fac_kingdom_10,fac_kingdom_1,fac_kingdom_4]],


["german_poleaxe_1", "Imperial_Helmbarte", [("Halberd_Medium_A_01", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_crush_through|itp_cant_use_on_horseback|itp_bonus_against_shield|itp_extra_penetration, itc_glaive|itcf_carry_spear, 1200, weight(4)|abundance(100)|difficulty(12)|weapon_length(145)|spd_rtng(67)|swing_damage(29, pierce)|thrust_damage(24, pierce), imodbits_polearm|imodbit_masterwork, [], [fac_kingdom_10,fac_kingdom_1,fac_kingdom_4]],
["german_poleaxe_2", "Imperial_Helmbarte", [("Halberd_Medium_C_01", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_crush_through|itp_cant_use_on_horseback|itp_bonus_against_shield|itp_extra_penetration, itc_glaive|itcf_carry_spear, 1680, weight(5)|abundance(100)|difficulty(12)|weapon_length(146)|spd_rtng(71)|swing_damage(31, pierce)|thrust_damage(24, pierce), imodbits_polearm|imodbit_masterwork, [], [fac_kingdom_10]],
["german_poleaxe_3", "Imperial_Helmbarte", [("Halberd_Medium_D_01", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_crush_through|itp_cant_use_on_horseback|itp_bonus_against_shield|itp_extra_penetration, itc_glaive|itcf_carry_spear, 1800, weight(5.5)|abundance(100)|difficulty(12)|weapon_length(145)|spd_rtng(66)|swing_damage(39, pierce)|thrust_damage(24, pierce), imodbits_polearm|imodbit_masterwork, [], [fac_kingdom_10]],
["german_poleaxe_4", "Imperial_Helmbarte", [("Halberd_Medium_B_01", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_crush_through|itp_cant_use_on_horseback|itp_bonus_against_shield|itp_extra_penetration, itc_glaive|itcf_carry_spear, 1460, weight(4.5)|abundance(100)|difficulty(12)|weapon_length(142)|spd_rtng(70)|swing_damage(43,pierce)|thrust_damage(35,pierce), imodbits_polearm|imodbit_masterwork, [], [fac_kingdom_10]],

["polehammer",         "Polehammer", [("pole_hammer",0)], itp_type_polearm| itp_primary|itp_two_handed|itp_wooden_parry, itc_poleaxe, 2535 , weight(7)|difficulty(14)|spd_rtng(50)| weapon_length(130)|swing_damage(50 , blunt)| thrust_damage(30 ,  blunt),imodbits_polearm ],

["swiss_halberd_short", "swiss_halberd", [("halbert_2",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_extra_penetration|itp_cant_use_on_horseback, itc_poleaxe, 3852, weight(4)|difficulty(0)|spd_rtng(70)|weapon_length(150)|swing_damage(33,pierce)|thrust_damage(27,pierce), imodbits_polearm|imodbit_masterwork, [], se_faction],


["long_voulge", "Long Voulge", [("two_handed_battle_long_axe_a",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_is_pike|itp_extra_penetration|itp_cant_use_on_horseback|itp_is_glaive, itc_poleaxe|itcf_carry_spear, 1959, weight(3.0)|difficulty(10)|spd_rtng(70)|weapon_length(175)|swing_damage(35,pierce)|thrust_damage(18,pierce), imodbits_axe|imodbit_masterwork, [], [fac_kingdom_1]],
["swiss_halberd", "swiss_halberd", [("halbert_1",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_is_pike|itp_extra_penetration|itp_cant_use_on_horseback|itp_is_glaive, itc_poleaxe, 3852, weight(5)|difficulty(0)|spd_rtng(70)|weapon_length(185)|swing_damage(33,pierce)|thrust_damage(28,pierce), imodbits_polearm|imodbit_masterwork, [], se_faction],


["nord_poleaxe", "nord_poleaxe", [("Halberd_Heavy_D_01",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_offset_lance|itp_cant_use_on_horseback|itp_is_pike|itp_extra_penetration|itp_is_glaive, itc_cutting_spear, 3170, weight(4)|difficulty(10)|spd_rtng(65)|weapon_length(200)|swing_damage(35,pierce)|thrust_damage(31,pierce), imodbits_polearm|imodbit_masterwork, [], ne_faction],

["nord_poleaxe_1", "nord_poleaxe", [("Halberd_Heavy_A_01",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_offset_lance|itp_cant_use_on_horseback|itp_is_pike|itp_extra_penetration|itp_is_glaive, itc_poleaxe, 3170, weight(5)|difficulty(10)|spd_rtng(70)|weapon_length(183)|swing_damage(35,pierce)|thrust_damage(31,pierce), imodbits_polearm|imodbit_masterwork, [], ne_faction],
["nord_poleaxe_2", "nord_poleaxe", [("Halberd_Heavy_B_01",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_offset_lance|itp_cant_use_on_horseback|itp_is_pike|itp_extra_penetration|itp_is_glaive, itc_poleaxe, 3170, weight(6)|difficulty(10)|spd_rtng(70)|weapon_length(180)|swing_damage(40,pierce)|thrust_damage(31,pierce), imodbits_polearm|imodbit_masterwork, [], ne_faction],
["nord_poleaxe_3", "nord_poleaxe", [("Halberd_Heavy_C_01",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_offset_lance|itp_cant_use_on_horseback|itp_is_pike|itp_extra_penetration|itp_is_glaive, itc_cutting_spear, 3170, weight(7)|difficulty(10)|spd_rtng(70)|weapon_length(201)|swing_damage(40,pierce)|thrust_damage(31,pierce), imodbits_polearm|imodbit_masterwork, [], ne_faction],
["nord_poleaxe_4", "nord_poleaxe", [("Halberd_Heavy_D_01",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_offset_lance|itp_cant_use_on_horseback|itp_is_pike|itp_extra_penetration|itp_is_glaive, itc_cutting_spear, 3170, weight(4)|difficulty(10)|spd_rtng(75)|weapon_length(200)|swing_damage(45,pierce)|thrust_damage(31,pierce), imodbits_polearm|imodbit_masterwork, [], ne_faction],


["long_glaive", "nord_poleaxe", [("rrr_halberd6",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_offset_lance|itp_cant_use_on_horseback|itp_is_pike|itp_extra_penetration|itp_is_glaive, itc_cutting_spear, 3170, weight(4)|difficulty(10)|spd_rtng(65)|weapon_length(200)|swing_damage(35,cut)|thrust_damage(31,pierce), imodbits_polearm|imodbit_masterwork , [], se_faction],


["bec_de_corbin_a",  "War Hammer", [("bec_de_corbin_a",0)], itp_type_polearm|itp_merchandise|itp_primary|itp_crush_through|itp_wooden_parry|itp_two_handed|itp_bonus_against_shield|itp_cant_use_on_horseback, itc_glaive|itcf_carry_spear, 2956 , weight(3.0)|difficulty(0)|spd_rtng(81)| weapon_length(120)|swing_damage(45, pierce)| thrust_damage(38 ,  pierce),imodbits_polearm , [], [fac_kingdom_1]],
["polehammer_threeprong",         "Pole_Hammer", [("pole_hammar2",0)], itp_type_polearm|itp_merchandise|itp_primary|itp_crush_through|itp_wooden_parry|itp_two_handed|itp_bonus_against_shield|itp_cant_use_on_horseback, itc_glaive|itcf_carry_spear,3832 , weight(5)|difficulty(5)|spd_rtng(79)| weapon_length(155)|swing_damage(42 , pierce)| thrust_damage(30 ,  pierce),imodbits_polearm, [], [fac_kingdom_5,fac_kingdom_1]],
["polehammer_manhunter",         "Polehammer", [("rrr_polehammer3",0)], itp_type_polearm|itp_merchandise|itp_primary|itp_crush_through|itp_wooden_parry|itp_two_handed|itp_bonus_against_shield|itp_cant_use_on_horseback, itc_glaive|itcf_carry_spear, 3860 , weight(3)|difficulty(6)|spd_rtng(75)| weapon_length(160)|swing_damage(42 , pierce)| thrust_damage(44 ,  pierce),imodbits_polearm , [], [fac_kingdom_5]],



# SHIELDS

["wooden_shield", "Wooden Shield", [("shield_round_a",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  126 , weight(2)|shield_hit_points(180)|body_armor(60)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["nordic_shield", "Nordic Shield", [("shield_round_b",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  285 , weight(2)|shield_hit_points(220)|body_armor(60)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["fur_covered_shield",  "Fur Covered Shield", [("shield_kite_m",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  681 , weight(3.5)|shield_hit_points(120)|body_armor(60)|spd_rtng(76)|shield_width(81),imodbits_shield],
["steel_shield", "Steel Shield", [("shield_dragon",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,  2091 , weight(4)|shield_hit_points(300)|body_armor(100)|spd_rtng(61)|shield_width(40),imodbits_shield , [], [fac_kingdom_10,fac_kingdom_7]],

["dec_steel_shield", "Steel Shield", [("dec_steel_shield",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,  2091 , weight(4)|shield_hit_points(450)|body_armor(100)|spd_rtng(61)|shield_width(40),imodbits_shield , [], [fac_kingdom_9,fac_kingdom_3]],


["plate_covered_round_shield", "Plate Covered Round Shield", [("shield_round_e",0)], itp_type_shield, itcf_carry_round_shield,  420 , weight(4)|shield_hit_points(165)|body_armor(100)|spd_rtng(90)|shield_width(40),imodbits_shield],
["leather_covered_round_shield", "Leather Covered Round Shield", [("shield_round_d",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  240 , weight(2.5)|shield_hit_points(155)|body_armor(76)|spd_rtng(96)|shield_width(40),imodbits_shield ],
["hide_covered_round_shield", "Hide Covered Round Shield", [("shield_round_f",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  120 , weight(2)|shield_hit_points(130)|body_armor(66)|spd_rtng(100)|shield_width(40),imodbits_shield],


["shield_heater_a", "Heater Shield", [("shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  996 , weight(4)|shield_hit_points(410)|body_armor(78)|spd_rtng(87)|shield_width(36)|shield_height(70),imodbits_shield , [], [fac_kingdom_13]],
["shield_heater_b", "Heater Shield", [("shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  996 , weight(4)|shield_hit_points(410)|body_armor(78)|spd_rtng(87)|shield_width(36)|shield_height(70),imodbits_shield , [], euro_factions],
["shield_heater_c", "Heater Shield", [("shield_1",0)], itp_merchandise|itp_type_shield, itcf_carry_kite_shield,  2091 , weight(4)|shield_hit_points(520)|body_armor(100)|spd_rtng(80)|shield_width(36)|shield_height(70),imodbits_shield , [], euro_factions],


#["norman_shield_1",         "Kite Shield", [("norman_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|shield_hit_points(96)|body_armor(60)|spd_rtng(82)|shield_width(90),imodbits_shield],
#["norman_shield_2",         "Kite Shield", [("norman_shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|shield_hit_points(96)|body_armor(60)|spd_rtng(82)|shield_width(90),imodbits_shield],
#["norman_shield_3",         "Kite Shield", [("norman_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|shield_hit_points(96)|body_armor(60)|spd_rtng(82)|shield_width(90),imodbits_shield],
#["norman_shield_4",         "Kite Shield", [("norman_shield_4",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|shield_hit_points(96)|body_armor(60)|spd_rtng(82)|shield_width(90),imodbits_shield],
#["norman_shield_5",         "Kite Shield", [("norman_shield_5",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|shield_hit_points(96)|body_armor(60)|spd_rtng(82)|shield_width(90),imodbits_shield ],
#["norman_shield_6",         "Kite Shield", [("norman_shield_6",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|shield_hit_points(96)|body_armor(60)|spd_rtng(82)|shield_width(90),imodbits_shield ],
#["norman_shield_7",         "Kite Shield", [("norman_shield_7",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|shield_hit_points(96)|body_armor(60)|spd_rtng(82)|shield_width(90),imodbits_shield ],
#["norman_shield_8",         "Kite Shield", [("norman_shield_8",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|shield_hit_points(96)|body_armor(60)|spd_rtng(82)|shield_width(90),imodbits_shield ],

["tab_shield_round_a", "Old Round Shield", [("tableau_shield_round_5",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,78 , weight(2.5)|shield_hit_points(98)|body_armor(60)|spd_rtng(93)|shield_width(50),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_5", ":agent_no", ":troop_no")])], [fac_kingdom_10,fac_kingdom_4]],
["tab_shield_round_b", "Plain Round Shield", [("tableau_shield_round_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,195 , weight(3)|shield_hit_points(130)|body_armor(64)|spd_rtng(90)|shield_width(50),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_3", ":agent_no", ":troop_no")])], [fac_kingdom_10]],
["tab_shield_round_c", "Round Shield", [("tableau_shield_round_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,315 , weight(3.5)|shield_hit_points(155)|body_armor(68)|spd_rtng(87)|shield_width(50),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_round_shield_2", ":agent_no", ":troop_no")])], [fac_kingdom_10]],
["tab_shield_round_d", "Heavy Round Shield", [("tableau_shield_round_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,630 , weight(4)|shield_hit_points(175)|body_armor(72)|spd_rtng(84)|shield_width(50),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_1", ":agent_no", ":troop_no")])], [fac_kingdom_10]],
["tab_shield_round_e", "Huscarl's Round Shield", [("tableau_shield_round_4",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,1290 , weight(4.5)|shield_hit_points(220)|body_armor(76)|spd_rtng(81)|shield_width(50),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_4", ":agent_no", ":troop_no")])], [fac_kingdom_10]],



["tab_shield_kite_a", "Old Kite Shield",   [("tableau_shield_kite_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,99 , weight(2)|shield_hit_points(82)|body_armor(60)|spd_rtng(96)|shield_width(36)|shield_height(70),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_1", ":agent_no", ":troop_no")])], [fac_kingdom_8,fac_kingdom_4]],
["tab_shield_kite_b", "Plain Kite Shield",   [("tableau_shield_kite_3" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,210 , weight(2.5)|shield_hit_points(107)|body_armor(64)|spd_rtng(93)|shield_width(36)|shield_height(70),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_3", ":agent_no", ":troop_no")])], [fac_kingdom_8,fac_kingdom_9,fac_kingdom_4,fac_kingdom_5]],
["tab_shield_kite_c", "Kite Shield",   [("tableau_shield_kite_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,468 , weight(3)|shield_hit_points(132)|body_armor(70)|spd_rtng(90)|shield_width(36)|shield_height(70),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_2", ":agent_no", ":troop_no")])], [fac_kingdom_8,fac_kingdom_9,fac_kingdom_10,fac_kingdom_4,fac_kingdom_7]],
["tab_shield_kite_d", "Heavy Kite Shield",   [("tableau_shield_kite_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,960 , weight(3.5)|shield_hit_points(155)|body_armor(76)|spd_rtng(87)|shield_width(36)|shield_height(70),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_2", ":agent_no", ":troop_no")])], [fac_kingdom_8,fac_kingdom_10,fac_kingdom_4]],


["tab_shield_kite_cav_a", "Horseman's Kite Shield",   [("tableau_shield_kite_4" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,615 , weight(2)|shield_hit_points(84)|body_armor(70)|spd_rtng(103)|shield_width(30)|shield_height(50),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_4", ":agent_no", ":troop_no")])], [fac_kingdom_8,fac_kingdom_10]],
["tab_shield_kite_cav_b", "Knightly Kite Shield",   [("tableau_shield_kite_4" ,0)], itp_merchandise|itp_type_shield, itcf_carry_kite_shield,1080 , weight(2.5)|shield_hit_points(115)|body_armor(86)|spd_rtng(100)|shield_width(30)|shield_height(50),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_4", ":agent_no", ":troop_no")])], [fac_kingdom_8,fac_kingdom_10,fac_kingdom_4]],


["tab_shield_heater_a", "Old Heater Shield",   [("tableau_shield_heater_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,108 , weight(2)|shield_hit_points(80)|body_armor(60)|spd_rtng(96)|shield_width(36)|shield_height(70),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])], [fac_kingdom_1,fac_kingdom_4,fac_kingdom_5,fac_kingdom_7]],
["tab_shield_heater_b", "Plain Heater Shield",   [("tableau_shield_heater_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,222 , weight(2.5)|shield_hit_points(105)|body_armor(66)|spd_rtng(93)|shield_width(36)|shield_height(70),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])], [fac_kingdom_1]],
["tab_shield_heater_c", "Heater Shield",   [("tableau_shield_heater_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,480 , weight(3)|shield_hit_points(130)|body_armor(72)|spd_rtng(90)|shield_width(36)|shield_height(70),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])], [fac_kingdom_1,fac_kingdom_4,fac_kingdom_7]],
["tab_shield_heater_d", "Heavy Heater Shield",   [("tableau_shield_heater_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,996 , weight(3.5)|shield_hit_points(152)|body_armor(78)|spd_rtng(87)|shield_width(36)|shield_height(70),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])], [fac_kingdom_4,fac_kingdom_5,fac_kingdom_7]],


["tab_shield_heater_cav_a", "Horseman's Heater Shield",   [("tableau_shield_heater_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,687 , weight(2)|shield_hit_points(80)|body_armor(84)|spd_rtng(103)|shield_width(30)|shield_height(50),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_2", ":agent_no", ":troop_no")])], [fac_kingdom_4,fac_kingdom_5,fac_kingdom_7]],
["tab_shield_heater_cav_b", "Knightly Heater Shield",   [("tableau_shield_heater_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,1170 , weight(2.5)|shield_hit_points(110)|body_armor(90)|spd_rtng(100)|shield_width(30)|shield_height(50),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_2", ":agent_no", ":troop_no")])], [fac_kingdom_1,fac_kingdom_7]],


["tab_shield_pavise_a", "Old Board Shield",   [("tableau_shield_pavise_2" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,180 , weight(3.5)|shield_hit_points(140)|body_armor(55)|spd_rtng(89)|shield_width(43)|shield_height(100),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_2", ":agent_no", ":troop_no")])], [fac_kingdom_5,fac_kingdom_7]],
["tab_shield_pavise_b", "Plain Board Shield",   [("tableau_shield_pavise_2" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,342 , weight(4)|shield_hit_points(180)|body_armor(62)|spd_rtng(85)|shield_width(43)|shield_height(100),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_2", ":agent_no", ":troop_no")])], [fac_kingdom_5,fac_kingdom_7]],
["tab_shield_pavise_c", "Board Shield",   [("tableau_shield_pavise_1" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,630 , weight(4.5)|shield_hit_points(220)|body_armor(64)|spd_rtng(81)|shield_width(43)|shield_height(100),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_1", ":agent_no", ":troop_no")])], [fac_kingdom_1,fac_kingdom_5]],
["tab_shield_pavise_d", "Heavy Board Shield", [("tableau_shield_pavise_1",0)], itp_type_shield|itp_merchandise|itp_wooden_parry|itp_cant_use_on_horseback, itcf_carry_board_shield, 1110, weight(5)|shield_hit_points(280)|body_armor(66)|spd_rtng(78)|shield_width(43)|shield_height(100), imodbits_shield, [(ti_on_init_item,[(store_trigger_param_1,":agent_no"),(store_trigger_param_2,":troop_no"),(call_script,"script_shield_item_set_banner","tableau_pavise_shield_1",":agent_no",":troop_no")])] , [fac_kingdom_5]],

["tab_shield_pavise_cav", "Cavalry Board Shield", [("cavalry_shield_pavise_15", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_board_shield, 1260, weight(3.5)|abundance(90)|shield_hit_points(215)|body_armor(90)|spd_rtng(90)|shield_width(50)|shield_height(60), imodbits_shield, [(ti_on_init_item,[(store_trigger_param_1,":agent_no"),(store_trigger_param_2,":troop_no"),(call_script,"script_shield_item_set_banner","tableau_pavise_shield_1",":agent_no",":troop_no")])] ],

["tab_shield_small_round_a", "Plain Cavalry Shield", [("tableau_shield_small_round_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,288 , weight(2)|shield_hit_points(80)|body_armor(66)|spd_rtng(105)|shield_width(40),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_3", ":agent_no", ":troop_no")])], [fac_kingdom_9,fac_kingdom_3,fac_kingdom_4]],
["tab_shield_small_round_b", "Round Cavalry Shield", [("tableau_shield_small_round_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,585 , weight(2.5)|shield_hit_points(100)|body_armor(78)|spd_rtng(103)|shield_width(40),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_1", ":agent_no", ":troop_no")])], [fac_kingdom_9,fac_kingdom_3,fac_kingdom_4,fac_kingdom_7]],
["tab_shield_small_round_c", "Elite Cavalry Shield", [("tableau_shield_small_round_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,1110 , weight(3)|shield_hit_points(125)|body_armor(88)|spd_rtng(100)|shield_width(40),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_2", ":agent_no", ":troop_no")])], [fac_kingdom_9,fac_kingdom_3,fac_kingdom_4,fac_kingdom_7]],



["shield_otto1", "Turkish_Shield", [("tableau_shield_otto1", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 600, weight(2)|shield_width(30)|shield_height(50)|abundance(100)|shield_hit_points(90)|body_armor(70)|spd_rtng(92), imodbits_shield, [(ti_on_init_item,[(store_trigger_param_1,":agent_no"),(store_trigger_param_2,":troop_no"),(call_script,"script_shield_item_set_banner","tableau_shield_otto1",":agent_no",":troop_no")])] , [fac_kingdom_8,fac_kingdom_9]],
["shield_otto2", "Turkish_Shield", [("tableau_shield_otto2", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 1200, weight(2)|shield_width(30)|shield_height(50)|abundance(100)|shield_hit_points(110)|body_armor(70)|spd_rtng(90), imodbits_shield, [(ti_on_init_item,[(store_trigger_param_1,":agent_no"),(store_trigger_param_2,":troop_no"),(call_script,"script_shield_item_set_banner","tableau_shield_otto3",":agent_no",":troop_no")])] , [fac_kingdom_8,fac_kingdom_9]],
["shield_otto_wing", "Turkish_Shield", [("tableau_shield_otto3", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 1200, weight(2)|shield_width(30)|shield_height(50)|abundance(100)|shield_hit_points(135)|body_armor(75)|spd_rtng(90), imodbits_shield, [(ti_on_init_item,[(store_trigger_param_1,":agent_no"),(store_trigger_param_2,":troop_no"),(call_script,"script_shield_item_set_banner","tableau_shield_otto2",":agent_no",":troop_no")])] , [fac_kingdom_8,fac_kingdom_9]],




["gondor_shield_a","Gondor_Square_Shield",[("gondor_square_shield",0)],itp_type_shield|itp_wooden_parry|itp_merchandise|itp_cant_use_on_horseback,itcf_carry_kite_shield,600,weight(3)|hit_points(3360)|body_armor(56)|spd_rtng(82)|shield_width(90)|shield_height(90),imodbits_shield, [], [fac_kingdom_1]],
["gondor_shield_b","Gondor_Kite_Shield",[("gondor_point_shield",0)],itp_type_shield|itp_wooden_parry|itp_merchandise,itcf_carry_kite_shield,400,weight(2.5)|hit_points(150)|body_armor(65)|spd_rtng(100)|shield_width(30)|shield_height(50),imodbits_shield, [], [fac_kingdom_1]],
["gondor_shield_c","Gondor_Tower_Shield",[("gondor_tower_shield",0)],itp_type_shield|itp_wooden_parry|itp_merchandise|itp_cant_use_on_horseback,itcf_carry_kite_shield,1110,weight(3)|hit_points(210)|body_armor(70)|spd_rtng(75)|shield_width(43)|shield_height(100),imodbits_shield, [], [fac_kingdom_1]],
["gondor_shield_d","Gondor_Kite_Shield",[("gondorian_kite_shield",0)],itp_type_shield|itp_wooden_parry|itp_merchandise,itcf_carry_kite_shield, 1080,weight(2.5)|hit_points(260)|body_armor(80)|spd_rtng(100)|shield_width(30)|shield_height(50),imodbits_shield, [], [fac_kingdom_1]],
["gondor_shield_e","Gondor_Royal_Shield",[("denethor_shield",0)],itp_type_shield|itp_wooden_parry,itcf_carry_kite_shield,1200,weight(2.5)|hit_points(305)|body_armor(92)|spd_rtng(82)|shield_width(40)|shield_height(90),imodbits_shield, [], [fac_kingdom_1,fac_hospitalier_knights]],




["dol_shield_a","DA_shield_kite",[("DA_shield_kite",0)],itp_type_shield|itp_wooden_parry|itp_merchandise,itcf_carry_kite_shield,1080,weight(2.5)|hit_points(160)|body_armor(80)|spd_rtng(100)|shield_width(30)|shield_height(50),imodbits_shield, [], [fac_kingdom_1]],
["dol_shield_b","shield_dolamroth",[("shield_dolamroth",0)],itp_type_shield|itp_wooden_parry,itcf_carry_kite_shield,1200,weight(2.5)|hit_points(2220)|body_armor(92)|spd_rtng(82)|shield_width(40)|shield_height(90),imodbits_shield, [], [fac_kingdom_1,fac_hospitalier_knights]],
#RANGED


#TODO:
["darts",         "Darts", [("dart_b",0),("dart_b_bag", ixmesh_carry),("dart_b_bag", ixmesh_inventory)], itp_type_thrown|itp_merchandise|itp_primary ,itcf_throw_javelin|itcf_carry_quiver_right_vertical|itcf_show_holster_when_drawn,155 , weight(5)|difficulty(1)|spd_rtng(93)| shoot_speed(28)| thrust_damage(36 ,  cut)|max_ammo(7)|weapon_length(32),imodbits_thrown,missile_distance_trigger, throw_factions],
["war_darts",         "War Darts", [("dart_a",0),("dart_a_bag", ixmesh_carry),("dart_a_bag", ixmesh_inventory)], itp_type_thrown|itp_merchandise|itp_primary ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,285 , weight(5)|difficulty(1)|spd_rtng(95)| shoot_speed(27)| thrust_damage(38 ,  cut)|max_ammo(7)|weapon_length(45),imodbits_thrown,missile_distance_trigger, throw_factions],

["javelin",         "Javelins", [("javelin",0),("javelins_quiver_new", ixmesh_carry),("javelins_quiver_new", ixmesh_inventory)], itp_type_thrown|itp_merchandise|itp_primary ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,300, weight(5)|difficulty(1)|spd_rtng(91)| shoot_speed(25)| thrust_damage(53 ,  cut)|max_ammo(5)|weapon_length(75),imodbits_thrown,missile_distance_trigger, throw_factions],
["javelin_melee",         "Javelin", [("javelin",0)], itp_type_polearm|itp_primary|itp_wooden_parry , itc_shortened_spear,300, weight(1)|difficulty(0)|spd_rtng(95)|swing_damage(12, cut)| thrust_damage(14,  pierce)|weapon_length(75),imodbits_polearm ],

["jarid",         "Jarids", [("jarid_new",0),("jarid_quiver", ixmesh_carry),("jarid_quiver", ixmesh_inventory)], itp_type_thrown|itp_merchandise|itp_primary ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,560 , weight(4)|difficulty(2)|spd_rtng(89)| shoot_speed(24)| thrust_damage(48 ,  cut)|max_ammo(4)|weapon_length(65),imodbits_thrown,missile_distance_trigger, throw_factions],
["jarid_melee",         "Jarid", [("jarid_new",0),("jarid_quiver", ixmesh_carry)], itp_type_polearm|itp_primary|itp_wooden_parry , itc_shortened_spear,560 , weight(1)|difficulty(2)|spd_rtng(93)| swing_damage(16, cut)| thrust_damage(20 ,  pierce)|weapon_length(65),imodbits_thrown ],
["throwing_spears",         "Throwing Spears", [("jarid_new_b",0),("jarid_new_b_bag", ixmesh_carry),("jarid_new_b_bag", ixmesh_inventory)], itp_type_thrown|itp_merchandise|itp_primary ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,525 , weight(4)|difficulty(2)|spd_rtng(87)| shoot_speed(22)| thrust_damage(67 ,  cut)|max_ammo(4)|weapon_length(65),imodbits_thrown,missile_distance_trigger, [fac_kingdom_10]],
["throwing_spear_melee",         "Throwing Spear", [("jarid_new_b",0),("javelins_quiver", ixmesh_carry)],itp_type_polearm|itp_primary|itp_wooden_parry , itc_shortened_spear,525 , weight(1)|difficulty(1)|spd_rtng(91)| swing_damage(18, cut)| thrust_damage(23 ,  pierce)|weapon_length(75),imodbits_thrown ],


["throwing_pike",         "Throwing Pikes", [("ylyq_zaoyun_qiang",0),("ylyq_zaoyun_qiang_fly",ixmesh_flying_ammo)], itp_type_thrown|itp_primary|itp_can_penetrate_shield|itp_bonus_against_shield|itp_unique|itp_next_item_as_melee, itcf_throw_javelin|itcf_carry_spear, 50000 , weight(3.0)|difficulty(4)|spd_rtng(81)| weapon_length(140)| thrust_damage(60 ,pierce)| shoot_speed(40)|max_ammo(15),imodbits_thrown , [(ti_on_weapon_attack,[
(store_trigger_param_1,":shooter"),#Get the attacker Agent for add_missile'
(try_for_range, ":unused", 1, 11),
  (copy_position, pos2, pos1),
    (agent_get_horse,":horse",":shooter"),
    (agent_get_look_position,pos3,":shooter"),
    (agent_get_position,pos4,":shooter"),
    (position_copy_rotation,pos4,pos3),
    (try_begin), 
      (gt, ":horse", -1),
      (position_move_z,pos4,270),
    (else_try),
      (neg|gt, ":horse", -1),
      (position_move_z,pos4,170),
    (try_end),
  (set_fixed_point_multiplier, 100),
  (store_random_in_range, ":z_offset", -300, 301),#Random Rotation of Z
  (position_rotate_x_floating, pos4, 9000), # change axis by rotating 90 degrees
  (position_rotate_y_floating, pos4, ":z_offset"), # rotate z floating
  (position_rotate_x_floating, pos4, -9000), # change axis back
  (store_random_in_range, ":x_offset", -300, 301),#Random Rotation of X
  (position_rotate_x_floating, pos4, ":x_offset"), # Final adjustment of X
  (add_missile, ":shooter", pos4, 4000, "itm_throwing_spears", 0, "itm_throwing_spears", 0),
(try_end),

]),]+missile_distance_trigger],
["throwing_pike_melee",         "Throwing Pike", [("ylyq_zaoyun_qiang",0)], itp_type_polearm|itp_primary|itp_can_penetrate_shield|itp_bonus_against_shield|itp_unique, itc_spear|itcf_carry_spear, 50000 , weight(3.0)|difficulty(0)|spd_rtng(120)| weapon_length(160)|swing_damage(30 , blunt)| thrust_damage(100 ,  pierce),imodbits_thrown ],

#TODO:
#TODO: Heavy throwing Spear
["stones",         "Stones", [("throwing_stone",0)], itp_type_thrown|itp_crush_through|itp_primary ,itcf_throw_stone, 1 , weight(4)|difficulty(0)|spd_rtng(97)| shoot_speed(10)| thrust_damage(11 ,  blunt)|max_ammo(18)|weapon_length(8),imodbits_thrown_2,missile_distance_trigger],
["nahptha_bomb", "nahptha_bomb", [("naphtha",0)], itp_type_thrown|itp_crush_through|itp_merchandise|itp_primary ,itcf_throw_stone, 2000 , weight(4)|difficulty(0)|spd_rtng(97)| shoot_speed(24)| thrust_damage(50 ,  pierce)|max_ammo(10)|weapon_length(8)|difficulty(3),imodbits_thrown_2,missile_distance_trigger+nahptha_fire_trigger, tatar_faction+arab_factions],

["throwing_knives", "Throwing Knives", [("mirkwood_white_knife",0)], itp_type_thrown|itp_crush_through|itp_merchandise|itp_primary ,itcf_throw_knife, 76 , weight(3.5)|difficulty(0)|spd_rtng(121)| shoot_speed(32)| thrust_damage(32 ,  pierce)|max_ammo(14)|weapon_length(0),imodbits_thrown,missile_distance_trigger, [fac_forest_ranger]],
["throwing_daggers", "Throwing Daggers", [("SerpentDagger",0)], itp_type_thrown|itp_crush_through|itp_merchandise|itp_primary ,itcf_throw_knife, 50000 , weight(3.5)|difficulty(0)|spd_rtng(110)| shoot_speed(100)| thrust_damage(100 ,  pierce)|max_ammo(12)|weapon_length(0),imodbits_thrown,missile_distance_trigger, [fac_beast]],
["throwing_scimitar", "Throwing scimitar", [("harad_heavy_sword",0)], itp_type_thrown|itp_crush_through|itp_merchandise|itp_primary|itp_next_item_as_melee ,itcf_throw_stone, 193 , weight(3.5)|difficulty(0)|spd_rtng(110)| shoot_speed(24)| thrust_damage(40 ,  cut)|max_ammo(20)|weapon_length(60),imodbits_thrown,missile_distance_trigger, throw_factions],
["throwing_scimitar_alt", "Elite Scimitar", [("harad_heavy_sword",0),("scab_scimeter_b", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,290 , weight(1.5)|difficulty(0)|spd_rtng(104)| weapon_length(100)|swing_damage(39 , cut)| thrust_damage(0 ,  pierce),imodbits_sword_high ],


["gondor_javelin","Gondor_Javelin",[("gondor_javelin",0),("jarid_quiver",ixmesh_carry)],itp_type_thrown|itp_crush_through|itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,600,weight(10)|difficulty(2)|shoot_speed(25)|spd_rtng(91)|weapon_length(75)|thrust_damage(50,pierce)|max_ammo(8),imodbits_thrown,missile_distance_trigger, [fac_kingdom_1,fac_hospitalier_knights]],

["glass_javelin","Glass Javelin",[("GlassJavelin",0),("jarid_quiver",ixmesh_carry)],itp_type_thrown|itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,600,weight(10)|difficulty(2)|shoot_speed(25)|spd_rtng(91)|weapon_length(75)|thrust_damage(55,pierce)|max_ammo(8),imodbits_thrown,missile_distance_trigger, [fac_kingdom_4]],
["ebony_javelin","Ebony Javelin",[("EbonyJavelin",0),("jarid_quiver",ixmesh_carry)],itp_type_thrown|itp_crush_through|itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,600,weight(10)|difficulty(2)|shoot_speed(25)|spd_rtng(91)|weapon_length(75)|thrust_damage(53,pierce)|max_ammo(16),imodbits_thrown,missile_distance_trigger, [fac_undeads_2,fac_beast]],



["nord_javelin",         "Javelins", [("javelin",0),("javelins_quiver_new", ixmesh_carry),("javelins_quiver_new", ixmesh_inventory)], itp_type_thrown|itp_merchandise|itp_primary ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,600, weight(10)|difficulty(1)|spd_rtng(91)| shoot_speed(25)| thrust_damage(53 ,  cut)|max_ammo(15)|weapon_length(75),imodbits_thrown,missile_distance_trigger, [fac_kingdom_10,fac_kingdom_4]],
["nord_throwing_spears",         "Throwing Spears", [("NordHeroJavelin",0)], itp_type_thrown|itp_crush_through|itp_merchandise|itp_primary ,itcf_throw_javelin|itcf_carry_quiver_back,1050 , weight(8)|difficulty(2)|spd_rtng(87)| shoot_speed(22)| thrust_damage(58 ,  cut)|max_ammo(10)|weapon_length(65),imodbits_thrown,
[(ti_on_weapon_attack,[
(store_trigger_param_1,":shooter"),#Get the attacker Agent for add_missile'
(try_for_range, ":unused", 0, 1),
  (copy_position, pos2, pos1),
  (agent_get_look_position,pos3,":shooter"),
  (position_copy_rotation,pos2,pos3),
  (set_fixed_point_multiplier, 100),
  (store_random_in_range, ":z_offset", -300, 301),#Random Rotation of Z
  (position_rotate_x_floating, pos2, 9000), # change axis by rotating 90 degrees
  (position_rotate_y_floating, pos2, ":z_offset"), # rotate z floating
  (position_rotate_x_floating, pos2, -9000), # change axis back
  (store_random_in_range, ":x_offset", -300, 301),#Random Rotation of X
  (position_rotate_x_floating, pos2, ":x_offset"), # Final adjustment of X
        
  (add_missile, ":shooter", pos2, 2300, "itm_nord_throwing_spears", 0, "itm_nord_throwing_spears", 0),
(try_end),
]),]+missile_distance_trigger, [fac_scotland,fac_kingdom_10]],
["nord_jarid",         "Jarids", [("NordHeroJavelin2",0)], itp_type_thrown|itp_crush_through|itp_merchandise|itp_primary ,itcf_throw_javelin|itcf_carry_quiver_back,1120 , weight(8)|difficulty(2)|spd_rtng(89)| shoot_speed(24)| thrust_damage(62 ,  cut)|max_ammo(10)|weapon_length(75),imodbits_thrown,
[(ti_on_weapon_attack,[
(store_trigger_param_1,":shooter"),#Get the attacker Agent for add_missile'
(try_for_range, ":unused", 0, 2),
  (copy_position, pos2, pos1),
  (agent_get_look_position,pos3,":shooter"),
  (position_copy_rotation,pos2,pos3),
  (set_fixed_point_multiplier, 100),
  (store_random_in_range, ":z_offset", -300, 301),#Random Rotation of Z
  (position_rotate_x_floating, pos2, 9000), # change axis by rotating 90 degrees
  (position_rotate_y_floating, pos2, ":z_offset"), # rotate z floating
  (position_rotate_x_floating, pos2, -9000), # change axis back
  (store_random_in_range, ":x_offset", -300, 301),#Random Rotation of X
  (position_rotate_x_floating, pos2, ":x_offset"), # Final adjustment of X
        
  (add_missile, ":shooter", pos2, 2700, "itm_nord_jarid", 0, "itm_nord_jarid", 0),
(try_end),
]),]+missile_distance_trigger, [fac_scotland,fac_kingdom_10]],


#TODO: Light Trowing axe, Heavy Throwing Axe
#["vk_axe", "vk_axe", [("vk_axe",0)], itp_type_thrown|itp_primary|itp_can_penetrate_shield|itp_bonus_against_shield, itcf_throw_axe|itcf_throw_stone, 50000, weight(5)|difficulty(3)|spd_rtng(98)|shoot_speed(25)|thrust_damage(60,pierce)|max_ammo(99)|weapon_length(33)|difficulty(5), imodbits_thrown_minus_heavy,
#[(ti_on_missile_hit, [
#      (store_trigger_param_1, ":shooter_agent"),
#      (try_begin),
#        (eq, "$given_vk_axe", 1),
#        (agent_refill_ammo,":shooter_agent"),
#      (try_end),
#    ])]+missile_distance_trigger],
    
["vk_axe", "vk_axe", [("nordheroaxe",0)], itp_type_thrown|itp_crush_through|itp_primary|itp_can_penetrate_shield|itp_bonus_against_shield, itcf_throw_axe|itcf_throw_stone, 50000, weight(5)|difficulty(3)|spd_rtng(98)|shoot_speed(25)|thrust_damage(60,pierce)|max_ammo(5)|weapon_length(33)|difficulty(5), imodbits_thrown_minus_heavy,
[(ti_on_weapon_attack,[
(store_trigger_param_1,":shooter"),#Get the attacker Agent for add_missile'
(try_for_range, ":unused", 1, 4),

  (copy_position, pos2, pos1),
       
    (agent_get_horse,":horse",":shooter"),
    (agent_get_look_position,pos3,":shooter"),
    (agent_get_position,pos4,":shooter"),
    (position_copy_rotation,pos4,pos3),
    (try_begin), 
      (gt, ":horse", -1),
      (position_move_z,pos4,270),
    (else_try),
      (neg|gt, ":horse", -1),
      (position_move_z,pos4,170),
    (try_end),
                        
  #Shotgun script
  #Rifle Version
  (set_fixed_point_multiplier, 100),
  (store_random_in_range, ":z_offset", -300, 301),#Random Rotation of Z
  (position_rotate_x_floating, pos4, 9000), # change axis by rotating 90 degrees
  (position_rotate_y_floating, pos4, ":z_offset"), # rotate z floating
  (position_rotate_x_floating, pos4, -9000), # change axis back
  (store_random_in_range, ":x_offset", -300, 301),#Random Rotation of X
  (position_rotate_x_floating, pos4, ":x_offset"), # Final adjustment of X
        
  (add_missile, ":shooter", pos4, 3000, "itm_vk_axe", 0, "itm_vk_axe", 0),
(try_end),

]),]+missile_distance_trigger, ne_faction],
    
    
["throwing_star_a", "throwing_star_a", [("new_throwing_star_b",0)], itp_type_thrown|itp_primary|itp_unique, itcf_throw_knife, 50000, weight(3.5)|difficulty(0)|spd_rtng(200)|shoot_speed(50)|thrust_damage(25,cut)|max_ammo(30)|weapon_length(3)|difficulty(2), imodbits_thrown,
 [(ti_on_missile_hit,
    [   (try_begin),
      (store_trigger_param_1, ":shooter"),#store the value of the agent who weave
      (assign,":c",-1),
      (try_begin),
         (eq, "$g_use_special_item", 1),
         (assign,":c",1),
      (else_try),
         (agent_is_non_player, ":shooter"),
         (assign,":c",1),
      (try_end),
      (eq,":c",1),
      (try_begin),
        (assign,":distance",99999),
        (try_begin),
          (agent_get_look_position, pos2, ":shooter"),
          (get_distance_between_positions,":dist",pos1,pos2),
          (lt,":dist",":distance"),
          (assign,":distance",":dist"),
        (end_try),
        (agent_get_look_position, pos2, ":shooter"),
        (particle_system_burst, "psys_pistol_smoke", pos2, 15),
        (get_distance_between_positions,":dist",pos1,pos2),
        (try_begin),
          (gt,":dist",5000),
          (position_move_y,pos2,5000),
            (position_set_z_to_ground_level, pos2),
            (particle_system_burst, "psys_pistol_smoke", pos2, 15),
            (agent_set_position,":shooter",pos2),
                (else_try),
        (position_set_z_to_ground_level, pos1),
        (particle_system_burst, "psys_pistol_smoke", pos1, 15),
        (agent_set_position,":shooter",pos1),
        (try_end),
      (try_end),
      
            (agent_set_hit_points,":shooter",100,0),
        (try_end),
    ]),
]+missile_distance_trigger],

["throwing_star_b", "throwing_star_b", [("throwing_star_a",0)], itp_type_thrown|itp_primary|itp_unique, itcf_throw_knife, 50000, weight(3.5)|difficulty(0)|spd_rtng(200)|shoot_speed(50)|thrust_damage(25,cut)|max_ammo(30)|weapon_length(3), imodbits_thrown,
 [(ti_on_weapon_attack,[
(store_trigger_param_1,":shooter"),#Get the attacker Agent for add_missile'
(try_for_range, ":unused", 1, 11),
  (copy_position, pos2, pos1),
    (agent_get_horse,":horse",":shooter"),
    (agent_get_look_position,pos3,":shooter"),
    (agent_get_position,pos4,":shooter"),
    (position_copy_rotation,pos4,pos3),
    (try_begin), 
      (gt, ":horse", -1),
      (position_move_z,pos4,270),
    (else_try),
      (neg|gt, ":horse", -1),
      (position_move_z,pos4,170),
    (try_end),
  #Shotgun script
  #Rifle Version
  (set_fixed_point_multiplier, 100),
  (store_random_in_range, ":z_offset", -500, 501),#Random Rotation of Z
  (position_rotate_x_floating, pos4, 9000), # change axis by rotating 90 degrees
  (position_rotate_y_floating, pos4, ":z_offset"), # rotate z floating
  (position_rotate_x_floating, pos4, -9000), # change axis back
  (store_random_in_range, ":x_offset", -500, 501),#Random Rotation of X
  (position_rotate_x_floating, pos4, ":x_offset"), # Final adjustment of X
  #(add_missile, ":shooter", pos4, 3000, "itm_nord_throwing_spears", 0, "itm_nord_throwing_spears", 0),
  (add_missile, ":shooter", pos4, 5000, "itm_throwing_star_dummy", 0, "itm_throwing_star_dummy", 0),
(try_end),

]),]],
   
["throwing_star_dummy", "throwing_star_dummy", [("new_throwing_star_b",0)], itp_type_thrown|itp_primary|itp_unique|itp_no_pick_up_from_ground, itcf_throw_knife, 50000, weight(3.5)|difficulty(0)|spd_rtng(200)|shoot_speed(50)|thrust_damage(30,pierce)|max_ammo(1)|weapon_length(3)|difficulty(0), imodbits_thrown],
["throwing_star_dummy_2", "throwing_star_dummy", [("throwing_star_a",0)], itp_type_thrown|itp_primary|itp_unique|itp_no_pick_up_from_ground, itcf_throw_knife, 50000, weight(3.5)|difficulty(0)|spd_rtng(200)|shoot_speed(50)|thrust_damage(60,cut)|max_ammo(1)|weapon_length(3)|difficulty(0), imodbits_thrown],



["granata", "Large_Grenade", [("bombaaa", 0)], itp_type_thrown|itp_crush_through|itp_merchandise|itp_primary, itcf_throw_stone, 5400, weight(4)|weapon_length(30)|difficulty(1)|spd_rtng(65)|shoot_speed(17)|abundance(33)|thrust_damage(175, blunt)|max_ammo(3), imodbits_none,[(ti_on_missile_hit, [(store_trigger_param_1, ":shooter"),(copy_position,pos51,pos1),(call_script, "script_magic_deliver_area_damage", ":shooter", 600, 7, 15),]),]+missile_distance_trigger,firearm_factions],
["granata_medium", "Medium_Grenade", [("bombaaa_m", 0)], itp_type_thrown|itp_crush_through|itp_merchandise|itp_primary, itcf_throw_stone, 4500, weight(4)|weapon_length(25)|difficulty(2)|spd_rtng(67)|shoot_speed(18)|abundance(33)|thrust_damage(140, blunt)|max_ammo(5), imodbits_none,[(ti_on_missile_hit, [(store_trigger_param_1, ":shooter"),(copy_position,pos51,pos1),(call_script, "script_magic_deliver_area_damage", ":shooter", 400, 5, 15),]),]+missile_distance_trigger,firearm_factions],
["granata_small", "Small_Grenade", [("bombaaa_s", 0)], itp_type_thrown|itp_crush_through|itp_merchandise|itp_primary, itcf_throw_stone, 4000, weight(4)|weapon_length(20)|difficulty(3)|spd_rtng(70)|shoot_speed(20)|abundance(33)|thrust_damage(100, blunt)|max_ammo(7), imodbits_none,[(ti_on_missile_hit, [(store_trigger_param_1, ":shooter"),(copy_position,pos51,pos1),(call_script, "script_magic_deliver_area_damage", ":shooter", 200, 4, 15),]),]+missile_distance_trigger,firearm_factions],

["light_throwing_axes", "Light Throwing Axes", [("francisca",0),("francisca_quiver", ixmesh_carry)], itp_type_thrown|itp_crush_through|itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_throw_axe,360, weight(5)|difficulty(2)|spd_rtng(88)| shoot_speed(18)| thrust_damage(55,pierce)|max_ammo(4)|weapon_length(33),imodbits_thrown_minus_heavy,missile_distance_trigger, ne_faction],
["light_throwing_axes_melee", "Light Throwing Axe", [("francisca",0)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield,itc_scimitar,360, weight(1)|difficulty(2)|spd_rtng(99)|weapon_length(53)| swing_damage(26,pierce),imodbits_thrown_minus_heavy ],
["throwing_axes", "Throwing Axes", [("throwing_axe_a",0),("throwing_axe_a_quiver", ixmesh_carry)], itp_type_thrown|itp_crush_through|itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_throw_axe,490, weight(5)|difficulty(3)|spd_rtng(88)| shoot_speed(11)| thrust_damage(60,pierce)|max_ammo(4)|weapon_length(33),imodbits_thrown_minus_heavy,missile_distance_trigger, ne_faction],
["throwing_axes_melee", "Throwing Axe", [("throwing_axe_a",0)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield,itc_scimitar,490, weight(1)|difficulty(3)|spd_rtng(98)| swing_damage(29,pierce)|weapon_length(53),imodbits_thrown_minus_heavy ],
["heavy_throwing_axes", "Heavy Throwing Axes", [("throwing_axe_b",0),("throwing_axe_b_quiver", ixmesh_carry)], itp_type_thrown|itp_crush_through|itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_throw_axe,620, weight(5)|difficulty(4)|spd_rtng(88)| shoot_speed(11)| thrust_damage(65,pierce)|max_ammo(4)|weapon_length(33),imodbits_thrown_minus_heavy,missile_distance_trigger, ne_faction],
["heavy_throwing_axes_melee", "Heavy Throwing Axe", [("throwing_axe_b",0)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield,itc_scimitar,620, weight(1)|difficulty(4)|spd_rtng(97)| swing_damage(32,pierce)|weapon_length(53),imodbits_thrown_minus_heavy ],


["hunting_bow",         "Hunting Bow", [("hunting_bow",0),("hunting_bow_carry",ixmesh_carry)],itp_type_bow|itp_merchandise|itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back,17 , weight(1)|difficulty(0)|accuracy(97)|spd_rtng(85)| shoot_speed(45)| thrust_damage(15 ,  cut),imodbits_bow , [], bow_factions],
["short_bow",         "Short Bow", [("short_bow",0),("short_bow_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_primary ,itcf_shoot_bow|itcf_carry_bow_back,58 , weight(1)|difficulty(1)|accuracy(95)|spd_rtng(100)| shoot_speed(68)| thrust_damage(18 ,  cut),imodbits_bow , [], bow_factions],
["nomad_bow",         "Nomad Bow", [("nomad_bow_h3",0),("nomad_bow_scabbard_h3", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_primary ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn,164 , weight(1.25)|difficulty(3)|accuracy(94)|spd_rtng(72)| shoot_speed(75)| thrust_damage(23 ,  cut),imodbits_bow , [], arab_factions+ee_faction+tatar_faction],
["long_bow",         "Long Bow", [("long_bow",0),("long_bow_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_primary|itp_two_handed|itp_cant_use_on_horseback ,itcf_shoot_bow|itcf_carry_bow_back,145 , weight(1.75)|difficulty(3)|accuracy(91)|spd_rtng(60)| shoot_speed(82)| thrust_damage(28 ,  cut),imodbits_bow , [], ne_faction],
["strong_bow",         "Strong Bow", [("horn_bow_h3",0),("horn_bow_scabbard_h3", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_primary ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn,437 , weight(1.25)|difficulty(2)|accuracy(95)|spd_rtng(60)| shoot_speed(70)| thrust_damage(21 ,cut),imodbits_bow , [], arab_factions+ee_faction],
["khergit_bow",         "Khergit Bow", [("tatar_bow_h3",0),("tatar_bow_scabbard_h3", ixmesh_carry)], itp_type_bow|itp_primary|itp_merchandise,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn,269 , weight(1.25)|difficulty(4)|accuracy(93)|spd_rtng(67)| shoot_speed(79)| thrust_damage(16 ,pierce),imodbits_bow , [], ee_faction+tatar_faction],
["war_bow",         "War Bow", [("rus_bow_h4",0),("rus_bow_carry_h4",ixmesh_carry)],itp_type_bow|itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back,728 , weight(1.5)|difficulty(4)|accuracy(95)|spd_rtng(70)| shoot_speed(70)| thrust_damage(28 ,cut),imodbits_bow , [], ee_faction+tatar_faction],
["long_bow_2",         "Long Bow", [("long_bow5",0),("long_bow5_carry",ixmesh_carry)], itp_type_bow|itp_primary|itp_two_handed|itp_cant_use_on_horseback ,itcf_shoot_bow|itcf_carry_bow_back,925 , weight(1.75)|difficulty(4)|accuracy(91)|spd_rtng(65)| shoot_speed(95)| thrust_damage(20 ,  pierce),imodbits_bow , [], ne_faction],

["yumi", "Yumi_Bow", [("yumi_h3", 0), ("yumi_carry_h3", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back, 500, weight(1.750000)|abundance(100)|difficulty(3)|accuracy(85)|spd_rtng(97)|shoot_speed(55)|max_ammo(0)|thrust_damage(16, pierce)|weapon_length(0), imodbits_bow], 
["yumi2", "Yumi_Bow", [("yumi_h4", 0), ("yumi_carry_h4", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back, 700, weight(1.750000)|abundance(100)|difficulty(4)|accuracy(90)|spd_rtng(84)|shoot_speed(59)|max_ammo(0)|thrust_damage(23, pierce)|weapon_length(0), imodbits_bow, [], [fac_elf,fac_forest_ranger]], 

["imperial_bow", "Imperial War Bow", [("imperial_bow", 0), ("imperial_bow_case", ixmesh_carry)], itp_type_bow|itp_two_handed|itp_primary|itp_merchandise|itp_is_magic_staff, itcf_show_holster_when_drawn|itcf_shoot_bow|itcf_carry_bowcase_left, 2000, weight(1.5)|difficulty(5)|accuracy(95)|spd_rtng(80)|shoot_speed(75)|thrust_damage(19,pierce), imodbits_bow , magic_bow_trigger, [fac_kingdom_8]],
["long_bow_3",         "Long Bow", [("glassbow",0)], itp_type_bow|itp_primary|itp_two_handed|itp_is_magic_staff|itp_merchandise ,itcf_shoot_bow|itcf_carry_bow_back,2500 , weight(3)|difficulty(5)|accuracy(90)|spd_rtng(70)| shoot_speed(95)| thrust_damage(28 ,  pierce),imodbits_bow , magic_bow_trigger, [fac_kingdom_4]],

["khergit_long_bow",         "Turkish_Bow", [("dedal_bow_tatar_c",0),("dedal_bowcase_tatar_c", ixmesh_carry), ("dedal_bow_tatar_c_icon", ixmesh_inventory)], itp_type_bow|itp_primary|itp_is_magic_staff|itp_merchandise,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_carry_bowcase_left,1000 , weight(1.25)|difficulty(5)|accuracy(93)|spd_rtng(55)| shoot_speed(88)| thrust_damage(20 ,pierce),imodbits_bow , magic_bow_trigger, [fac_kingdom_9,fac_kingdom_3]],
["skeletonbow", "Long Bow", [("skeletonbow",0)], itp_type_bow|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back,925 , weight(1.25)|difficulty(4)|accuracy(91)|spd_rtng(70)| shoot_speed(95)| thrust_damage(15 ,  pierce),imodbits_bow , [], [fac_elf,fac_undeads_2,fac_demon,fac_kingdom_3,fac_kingdom_5]],

["black_bow", "Black Bow", [("skeletonbowskull",0)], itp_type_bow|itp_two_handed|itp_primary|itp_is_magic_staff|itp_merchandise, itcf_shoot_bow|itcf_carry_bow_back, 5000, weight(1.25)|difficulty(6)|accuracy(90)|spd_rtng(70)|shoot_speed(95)|thrust_damage(23,pierce), imodbits_bow, magic_bow_trigger, [fac_kingdom_5] ],

["nord_bow_1", "nord Long Bow", [("nordherobow",0)], itp_merchandise|itp_type_bow|itp_primary|itp_two_handed|itp_cant_use_on_horseback ,itcf_shoot_bow|itcf_carry_bow_back,925 , weight(2)|difficulty(4)|accuracy(91)|spd_rtng(65)| shoot_speed(95)| thrust_damage(20 ,  pierce),imodbits_bow , [], [fac_kingdom_10]],
["nord_bow_2", "nord hero Bow", [("bow_nordic",0)], itp_merchandise|itp_type_bow|itp_primary|itp_two_handed|itp_cant_use_on_horseback|itp_is_magic_staff ,itcf_shoot_bow|itcf_carry_bow_back,2000 , weight(3)|difficulty(5)|accuracy(94)|spd_rtng(63)| shoot_speed(100)| thrust_damage(24 ,  pierce),imodbits_bow , magic_bow_trigger, [fac_kingdom_10]],
["nord_bow_3", "stahlrim Long Bow", [("stahlrimbow",0)], itp_merchandise|itp_type_bow|itp_primary|itp_two_handed|itp_cant_use_on_horseback|itp_is_magic_staff|itp_merchandise ,itcf_shoot_bow|itcf_carry_bow_back,4500 , weight(3.25)|difficulty(6)|accuracy(99)|spd_rtng(60)| shoot_speed(105)| thrust_damage(32 ,  pierce),imodbits_bow , magic_bow_trigger, [fac_kingdom_10,fac_kingdom_1]],

["ebony_bow", "Ebony Bow", [("ebonybow",0)], itp_type_bow|itp_primary|itp_two_handed|itp_merchandise|itp_bonus_against_shield|itp_crush_through|itp_can_penetrate_shield ,itcf_shoot_bow|itcf_carry_bow_back,6000 , weight(3.5)|difficulty(6)|accuracy(99)|spd_rtng(50)| shoot_speed(105)| thrust_damage(45 ,  pierce),imodbits_bow , magic_bow_trigger, [fac_kingdom_8,fac_kingdom_10]],


["dragon_bone_bow", "Dragon Bone Bow", [("dragonbonebow",0)], itp_type_bow|itp_two_handed|itp_primary|itp_is_magic_staff, itcf_shoot_bow|itcf_carry_bow_back, 7500, weight(1.25)|difficulty(7)|spd_rtng(80)|shoot_speed(80)|thrust_damage(32,pierce), imodbits_bow, magic_bow_trigger, [fac_elf,fac_forest_ranger] ],
["karztev_bow", "Black_Bow", [("dwarvenbowkarztev",0)], itp_type_bow|itp_primary|itp_is_magic_staff,itcf_shoot_bow|itcf_carry_bow_back, 20000 , weight(1.25)|difficulty(6)|accuracy(99)|spd_rtng(65)| shoot_speed(70)| thrust_damage(21 ,pierce),imodbits_bow , magic_bow_trigger, [fac_elf,fac_forest_ranger]],
["auriels_bow", "Auriels_Bow", [("aurielsbow", 0)], itp_type_bow|itp_two_handed|itp_primary|itp_is_magic_staff, itcf_shoot_bow|itcf_carry_bow_back, 50000, weight(1.4)|difficulty(7)|accuracy(99)|spd_rtng(88)|shoot_speed(75)|thrust_damage(34, pierce), imodbits_bow ],

["hurricane_bow", "Hurricane_Bow", [("lonely", 0), ("lonely_carry", ixmesh_carry)], itp_type_bow|itp_two_handed|itp_primary|itp_is_magic_staff, itcf_shoot_bow|itcf_carry_bow_back, 50000, weight(1)|difficulty(7)|accuracy(99)|spd_rtng(92)|shoot_speed(60)|thrust_damage(28, pierce)|max_ammo(0), imodbits_bow , magic_bow_trigger],

["elven_bow",         "elven_bow", [("elven_bow", 0)],itp_type_bow|itp_primary|itp_two_handed|itp_is_magic_staff ,itcf_shoot_bow,50000 , 
weight(1.75)|difficulty(7)|accuracy(99)|spd_rtng(85)|shoot_speed(91)|thrust_damage(40,pierce),imodbits_bow, magic_bow_trigger, ne_faction],

["mirkwood_bow", "Mirkwood_Bow", [("mirkwood_bow", 0), ("mirkwood_bow_carry", ixmesh_carry)], itp_merchandise|itp_type_bow|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_is_magic_staff, itcf_shoot_bow|itcf_carry_bow_back, 3616, weight(1.75)|difficulty(5)|accuracy(100)|spd_rtng(100)|shoot_speed(82)|thrust_damage(15, pierce)|abundance(10)|max_ammo(0), imodbits_bow, magic_bow_trigger, [fac_elf,fac_forest_ranger] ],
["lorien_bow", "Galadhrim_Bow", [("Elfbow", 0), ("Elfbow_carry", ixmesh_carry)], itp_merchandise|itp_type_bow|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_is_magic_staff, itcf_shoot_bow|itcf_carry_bow_back, 2000, weight(1.5)|difficulty(5)|accuracy(100)|spd_rtng(100)|shoot_speed(85)|thrust_damage(15,pierce), imodbits_bow, magic_bow_trigger, [fac_elf] ],
["lorien_bow_2", "Galadhrim_Bow", [("elven_bow", 0)], itp_merchandise|itp_type_bow|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_is_magic_staff, itcf_shoot_bow|itcf_carry_bow_back, 3616, weight(1.5)|difficulty(6)|accuracy(100)|spd_rtng(110)|shoot_speed(90)|thrust_damage(20, pierce)|abundance(10)|max_ammo(0), imodbits_bow , magic_bow_trigger, [fac_kingdom_1]],
["mirkwood_bow_2", "Sharpshooter_Bow", [("latticed_flatbow",0),("latticed_flatbow_carry",ixmesh_carry)], itp_merchandise|itp_type_bow|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_is_magic_staff, itcf_shoot_bow|itcf_carry_bow_back, 3616, weight(1)|difficulty(6)|accuracy(100)|spd_rtng(90)|shoot_speed(95)|thrust_damage(23, pierce)|abundance(10)|max_ammo(0), imodbits_bow, magic_bow_trigger, [fac_elf,fac_forest_ranger] ],

["hunting_crossbow", "Hunting Crossbow", [("crossbow_b",0)], itp_type_crossbow|itp_merchandise|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 150, weight(2.25)|difficulty(0)|spd_rtng(45)|shoot_speed(45)|thrust_damage(35,pierce)|max_ammo(1), imodbits_crossbow , [], crossbow_factions],
["light_crossbow", "Light Crossbow", [("quick_crossbow",0)], itp_type_crossbow|itp_merchandise|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 300, weight(2.5)|difficulty(8)|spd_rtng(40)|shoot_speed(52)|thrust_damage(45,pierce)|max_ammo(1),imodbits_crossbow , [], crossbow_factions],
["crossbow", "Crossbow", [("heavy_crossbow_h1",0)], itp_type_crossbow|itp_merchandise|itp_cant_reload_on_horseback|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 600, weight(3)|spd_rtng(40)|shoot_speed(75)|thrust_damage(45,pierce)|max_ammo(1), imodbits_crossbow , [], crossbow_factions],
["heavy_crossbow", "Heavy Crossbow", [("crossbow_c",0)], itp_type_crossbow|itp_merchandise|itp_cant_reload_on_horseback|itp_two_handed|itp_primary|itp_bonus_against_shield, itcf_shoot_crossbow|itcf_carry_crossbow_back, 1200, weight(3.5)|difficulty(9)|spd_rtng(30)|shoot_speed(80)|thrust_damage(55,pierce)|max_ammo(1), imodbits_crossbow , [], crossbow_factions],
 
["sniper_crossbow", "Siege Crossbow", [("arbalest_h2",0)], itp_type_crossbow|itp_merchandise|itp_cant_reload_on_horseback|itp_two_handed|itp_primary|itp_bonus_against_shield, itcf_shoot_crossbow|itcf_carry_crossbow_back, 2400, weight(3.75)|difficulty(10)|spd_rtng(25)|shoot_speed(90)|thrust_damage(65,pierce)|max_ammo(1), imodbits_crossbow , [], se_faction],

["arbalest_1", "arbalest", [("spak_crsb01",0)], itp_type_crossbow|itp_merchandise|itp_cant_reload_on_horseback|itp_two_handed|itp_primary|itp_bonus_against_shield, itcf_shoot_crossbow|itcf_carry_crossbow_back, 4800, weight(3.75)|difficulty(10)|spd_rtng(20)|shoot_speed(90)|thrust_damage(75,pierce)|max_ammo(1), imodbits_crossbow , [], se_faction],
["arbalest_2", "arbalest", [("spak_crsb02",0)], itp_type_crossbow|itp_merchandise|itp_cant_reload_on_horseback|itp_two_handed|itp_primary|itp_bonus_against_shield, itcf_shoot_crossbow|itcf_carry_crossbow_back|itcf_reload_pistol, 9600, weight(3.75)|difficulty(10)|spd_rtng(25)|shoot_speed(100)|thrust_damage(85,pierce)|max_ammo(1), imodbits_crossbow , [], se_faction],
 
["rhod_crossbow", "Crossbow", [("heavy_crossbow_h2",0)], itp_type_crossbow|itp_cant_reload_on_horseback|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 1200, weight(3)|spd_rtng(25)|shoot_speed(80)|thrust_damage(45,pierce)|max_ammo(1), imodbits_crossbow , [], se_faction],
["rhod_sniper_crossbow", "Siege Crossbow", [("arbalest_h3",0)], itp_type_crossbow|itp_cant_reload_on_horseback|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 3600, weight(3.75)|difficulty(10)|spd_rtng(20)|shoot_speed(90)|thrust_damage(60,pierce)|max_ammo(1),imodbits_crossbow, [], se_faction], 

["van_helsing_crossbow_bolt", "Van Helsing Crossbow Bolt", [("van_helsing_crossbow_bolt",0),("van_helsing_crossbow_bolt_copy",ixmesh_flying_ammo),("van_helsing_crossbow_bolt_bag",ixmesh_carry),("van_helsing_crossbow_bolt_bag", ixmesh_inventory)], itp_type_bolts|itp_can_penetrate_shield|itp_bonus_against_shield, itcf_carry_quiver_right_vertical, 5000, weight(2.5)|abundance(20)|weapon_length(63)|thrust_damage(40,pierce)|max_ammo(60), imodbits_missile,missile_holy_fire_trigger+missile_holy_fire_trigger_1+missile_distance_trigger ],

["van_helsing_crossbow", "Van Helsing Crossbow", [("van_helsing_crossbow_01",0),("van_helsing_crossbow_01_scabbard",ixmesh_carry),("van_helsing_crossbow_01_scabbard",ixmesh_inventory)], itp_type_crossbow|itp_two_handed|itp_primary|itp_next_item_as_melee, itcf_shoot_crossbow|itcf_carry_crossbow_back, 50000, weight(3.75)|difficulty(10)|spd_rtng(45)|shoot_speed(100)|thrust_damage(60,pierce)|max_ammo(10), imodbits_crossbow ,[(ti_on_weapon_attack,[
(store_trigger_param_1,":shooter"),#Get the attacker Agent for add_missile'
(try_for_range, ":unused", 1, 3),
#(try_for_range, ":unused", 1, 1),
    (agent_get_wielded_item,":agent_cur_weapon",":shooter"),
    (gt,":agent_cur_weapon",0),
    
     (assign,":cur_weapon_slot",-1),
     (assign,":item_slot_num",4),
     (try_for_range,":cur_item_slot",0,":item_slot_num"),
        (eq,":cur_weapon_slot",-1),
        (agent_get_item_slot, ":item_no", ":shooter", ":cur_item_slot"),
        (eq,":item_no",":agent_cur_weapon"),
        (assign,":cur_weapon_slot",":cur_item_slot"),
     (try_end),
                    #match the right ammmo type
     (assign,":cur_ammo_id","itm_van_helsing_crossbow_bolt"),#as default
     (assign,":item_slot_num",4),
     (try_for_range,":cur_item_slot",0,":item_slot_num"),
        (agent_get_item_slot, ":item_no", ":shooter", ":cur_item_slot"),
        (gt,":item_no",-1),
        (item_get_type, ":item_type", ":item_no"),
        (eq,":item_type",itp_type_bolts),
        (agent_get_item_cur_ammo, ":cur_ammo_2", ":shooter", ":cur_item_slot"),
        (gt,":cur_ammo_2",0),
        (assign,":cur_ammo_id",":item_no"),
        (assign,":item_slot_num",0),#break
     (try_end),
  
    (agent_get_horse,":horse",":shooter"),
    (agent_get_look_position,pos3,":shooter"),
    (agent_get_position,pos4,":shooter"),
    (position_copy_rotation,pos4,pos3),
    (try_begin), 
      (gt, ":horse", -1),
      (position_move_z,pos4,270),
    (else_try),
      (neg|gt, ":horse", -1),
      (position_move_z,pos4,170),
    (try_end),
                      
    #Shotgun script
    #Rifle Version
    (add_missile, ":shooter", pos4, 200, "itm_van_helsing_crossbow", 0, ":cur_ammo_id", 0),
    
(try_end),
]),]],
["van_helsing_crossbow_auto", "Van Helsing Crossbow", [("van_helsing_crossbow_01",0),("van_helsing_crossbow_01_scabbard",ixmesh_carry)], itp_type_crossbow|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 20000, weight(3.75)|difficulty(10)|spd_rtng(100)|shoot_speed(120)|thrust_damage(80,pierce)|max_ammo(30), imodbits_crossbow ],

["crossbow_cannon", "Buriza-Do Kyanon", [("spak_crsb02",0)], itp_type_crossbow|itp_unique|itp_two_handed|itp_primary|itp_bonus_against_shield, itcf_shoot_crossbow|itcf_carry_crossbow_back|itcf_reload_pistol, 20000, weight(3.75)|spd_rtng(50)|shoot_speed(100)|thrust_damage(100,pierce)|max_ammo(2), imodbits_crossbow ],
["charm_bow", "Cupid's bow", [("imperial_bow", 0), ("imperial_bow_case", ixmesh_carry)], itp_type_bow|itp_two_handed|itp_primary|itp_unique|itp_is_magic_staff, itcf_show_holster_when_drawn|itcf_shoot_bow|itcf_carry_bowcase_left, 20000, weight(1.5)|difficulty(5)|accuracy(95)|spd_rtng(80)|shoot_speed(75)|thrust_damage(25,pierce), imodbits_bow , magic_bow_trigger],
["sloth_crossbow", "Valder's Bow of Sloth", [("skeleton_crossbow",0)], itp_type_crossbow|itp_unique|itp_primary|itp_is_magic_staff, itcf_shoot_crossbow|itcf_carry_crossbow_back, 20000, weight(2.5)|difficulty(8)|spd_rtng(80)|shoot_speed(70)|thrust_damage(45,pierce)|max_ammo(1),imodbits_crossbow , magic_bow_trigger],


["bonecrossbow", "bonecrossbow", [("arbalest_h4",0)], itp_type_crossbow|itp_primary|itp_next_item_as_melee, itcf_shoot_crossbow|itcf_carry_crossbow_back, 5000, weight(3.75)|difficulty(9)|spd_rtng(50)|shoot_speed(100)|thrust_damage(55,pierce)|max_ammo(6), imodbits_crossbow ,[(ti_on_weapon_attack,[
(store_trigger_param_1,":shooter"),#Get the attacker Agent for add_missile'
(try_for_range, ":unused", 1, 3),
#(try_for_range, ":unused", 1, 1),
    (agent_get_wielded_item,":agent_cur_weapon",":shooter"),
    (gt,":agent_cur_weapon",0),
    
     (assign,":cur_weapon_slot",-1),
     (assign,":item_slot_num",4),
     (try_for_range,":cur_item_slot",0,":item_slot_num"),
        (eq,":cur_weapon_slot",-1),
        (agent_get_item_slot, ":item_no", ":shooter", ":cur_item_slot"),
        (eq,":item_no",":agent_cur_weapon"),
        (assign,":cur_weapon_slot",":cur_item_slot"),
     (try_end),
        
  #  (agent_get_item_cur_ammo, ":cur_ammo", ":shooter",":cur_weapon_slot"),
  #  (gt,":cur_ammo",0),
  #  (val_sub,":cur_ammo",1),
  #  (agent_set_ammo,":shooter",":agent_cur_weapon",":cur_ammo"),
                        
                    #match the right ammmo type
     (assign,":cur_ammo_id","itm_bolts"),#as default
     (assign,":item_slot_num",4),
     (try_for_range,":cur_item_slot",0,":item_slot_num"),
        (agent_get_item_slot, ":item_no", ":shooter", ":cur_item_slot"),
        (gt,":item_no",-1),
        (item_get_type, ":item_type", ":item_no"),
        (eq,":item_type",itp_type_bolts),
        (agent_get_item_cur_ammo, ":cur_ammo_2", ":shooter", ":cur_item_slot"),
        (gt,":cur_ammo_2",0),
        (assign,":cur_ammo_id",":item_no"),
        (assign,":item_slot_num",0),#break
     (try_end),
  
    (agent_get_horse,":horse",":shooter"),
    (agent_get_look_position,pos3,":shooter"),
    (agent_get_position,pos4,":shooter"),
    (position_copy_rotation,pos4,pos3),
    (try_begin), 
      (gt, ":horse", -1),
      (position_move_z,pos4,270),
    (else_try),
      (neg|gt, ":horse", -1),
      (position_move_z,pos4,170),
    (try_end),
                      
  #Shotgun script
  #Rifle Version
  (set_fixed_point_multiplier, 100),
  (store_random_in_range, ":z_offset", -300, 301),#Random Rotation of Z
  (position_rotate_x_floating, pos4, 9000), # change axis by rotating 90 degrees
  (position_rotate_y_floating, pos4, ":z_offset"), # rotate z floating
  (position_rotate_x_floating, pos4, -9000), # change axis back
  (store_random_in_range, ":x_offset", -300, 301),#Random Rotation of X
  (position_rotate_x_floating, pos4, ":x_offset"), # Final adjustment of X
        
  (add_missile, ":shooter", pos4, 10000, "itm_hunting_crossbow", 0, ":cur_ammo_id", 0),
  
(try_end),
]),]],
["bonecrossbow_auto", "bonecrossbow", [("arbalest_h4",0)], itp_type_crossbow|itp_primary|itp_is_magic_staff, itcf_shoot_crossbow|itcf_carry_crossbow_back, 5000, weight(3.75)|difficulty(9)|spd_rtng(50)|shoot_speed(100)|thrust_damage(90,pierce)|max_ammo(6), imodbits_crossbow ],



["flintlock_pistol", "Flintlock Pistol", [("flintlock_pistol",0)], itp_type_pistol|itp_merchandise|itp_primary ,itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_pistol_front_left, 
 600 , weight(2.0)|difficulty(0)|spd_rtng(45) | shoot_speed(100) | thrust_damage(48 ,pierce)|max_ammo(1)|accuracy(66),imodbits_gun, pistol_trigger , firearm_factions ],
["flintlock_pistol_2", "Pistol", [("flintlock_pistol",0)], itp_type_pistol|itp_merchandise|itp_primary ,itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_pistol_front_left,
 600 , weight(2.25)|difficulty(0)|spd_rtng(47) | shoot_speed(95) | thrust_damage(66 ,pierce)|max_ammo(1)|accuracy(67),imodbits_gun, pistol_trigger , firearm_factions ],
["flintlock_pistol_veteran", "Flintlock Pistol", [("pistol_pure_a",0)], itp_type_pistol|itp_merchandise|itp_primary ,itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_pistol_front_left, 
 3100 , weight(2.0)|difficulty(0)|spd_rtng(60) | shoot_speed(100) | thrust_damage(67 ,pierce)|max_ammo(1)|accuracy(70),imodbits_gun, pistol_trigger , firearm_factions ],
["flintlock_pistol_veteran_2", "Good Pistol", [("pistol_pure_b",0)], itp_type_pistol|itp_merchandise|itp_primary ,itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_pistol_front_left,
 3600 , weight(2.5)|difficulty(0)|spd_rtng(59) | shoot_speed(110) | thrust_damage(71 ,pierce)|max_ammo(1)|accuracy(75),imodbits_gun, pistol_trigger , firearm_factions ],
["flintlock_pistol_veteran_3", "Good Pistol", [("pistol_pure_c",0)], itp_type_pistol|itp_merchandise|itp_primary ,itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_pistol_front_left,
 3400 , weight(2.25)|difficulty(0)|spd_rtng(61) | shoot_speed(105) | thrust_damage(69 ,pierce)|max_ammo(1)|accuracy(73),imodbits_gun, pistol_trigger , firearm_factions ],
["flintlock_pistol_4s", "Flintlock Pistol", [("pistol_2stwol",0)], itp_type_pistol|itp_merchandise|itp_primary, itcf_shoot_pistol|itcf_carry_revolver_right|itcf_reload_pistol, 
 3600, weight(2.5)|difficulty(0)|spd_rtng(47)|shoot_speed(98)|thrust_damage(55,pierce)|max_ammo(4)|accuracy(68), imodbits_gun, pistol_trigger , firearm_factions],
["flintlock_pistol_2s", "Flintlock Pistol", [("pistol_2stwolB",0)], itp_type_pistol|itp_merchandise|itp_primary, itcf_shoot_pistol|itcf_carry_revolver_right|itcf_reload_pistol, 
 6800, weight(2.5)|difficulty(0)|spd_rtng(61)|shoot_speed(105)|thrust_damage(66,pierce)|max_ammo(2)|accuracy(75), imodbits_gun, pistol_trigger , firearm_factions],
 
["zlmg", "zlmg", [("zlmg",0)], itp_type_pistol|itp_crush_through|itp_primary|itp_unique, itcf_shoot_pistol|itcf_carry_pistol_front_left|itcf_reload_musket, 
 50000, weight(1.5)|difficulty(0)|spd_rtng(45)|shoot_speed(160)|thrust_damage(90,pierce)|max_ammo(6)|accuracy(99), imodbits_gun, 
 [(ti_on_weapon_attack,
  [(store_trigger_param_1, ":shooter"),(agent_set_ammo,":shooter","itm_zlmg",6),])]+pistol_trigger 
 ],

["flintlock_pistol_elite", "Flintlock Pistol", [("pistol_rich_a",0)], itp_type_pistol|itp_primary|itp_merchandise, itcf_shoot_pistol|itcf_carry_pistol_front_left|itcf_reload_musket, 
 5000, weight(2.0)|difficulty(0)|spd_rtng(62)|shoot_speed(105)|thrust_damage(70,blunt)|max_ammo(1)|accuracy(84), imodbits_gun, pistol_trigger , [fac_dwarf]],
["flintlock_pistol_elite_1", "Hand-crafted Pistol", [("pistol_rich_b",0)], itp_type_pistol|itp_merchandise|itp_primary ,itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_pistol_front_left,
 6000 , weight(2.0)|difficulty(0)|spd_rtng(64) | shoot_speed(115) | thrust_damage(78 ,pierce)|max_ammo(1)|accuracy(79),imodbits_gun, pistol_trigger , [fac_dwarf] ], 
["flintlock_pistol_elite_2", "Dutch Pistol", [("pistol_rich_c",0)], itp_type_pistol|itp_merchandise|itp_primary ,itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_pistol_front_left,
 7000 , weight(2.25)|difficulty(0)|spd_rtng(63) | shoot_speed(125) | thrust_damage(81 ,pierce)|max_ammo(1)|accuracy(82),imodbits_gun, pistol_trigger , [fac_dwarf] ], 

["pistol_2stwol", "Double-barreled Miquelet Pistol", [("pistol_2stwol",0)], itp_type_pistol|itp_crush_through|itp_merchandise|itp_primary ,itcf_reload_musket|itcf_shoot_pistol|itcf_carry_pistol_front_left,
 5000 , weight(3.25)|difficulty(0)|spd_rtng(44) | shoot_speed(125) | thrust_damage(80 ,pierce)|max_ammo(2)|accuracy(82),imodbits_gun, pistol_trigger , [fac_dwarf] ], 
["pistol_2stwolB", "Double-barreled Dutch Pistol", [("pistol_2stwolB",0)], itp_type_pistol|itp_crush_through|itp_merchandise|itp_primary ,itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_pistol_front_left,
 6000 , weight(3.25)|difficulty(0)|spd_rtng(46) | shoot_speed(145) | thrust_damage(85 ,pierce)|max_ammo(2)|accuracy(85),imodbits_gun, pistol_trigger , [fac_dwarf] ], 
["reitern_pistol_4s", "Flintlock Pistol", [("pistol_2stwolB",0)], itp_type_pistol|itp_crush_through|itp_primary, itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_pistol_front_left, 
 10000, weight(3.25)|difficulty(0)|spd_rtng(48)|shoot_speed(145)|thrust_damage(85,pierce)|max_ammo(2)|accuracy(85), imodbits_gun, pistol_trigger , [fac_dwarf]],

["musket_hand_gun", "Musket", [("Gun_Empire_Medium_Muscket_D_P1_01",0)], itp_type_musket|itp_crush_through|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 20000, weight(4)|difficulty(0)|spd_rtng(30)|shoot_speed(240)|thrust_damage(95,pierce)|max_ammo(1)|accuracy(75), imodbits_gun, hand_cannon_trigger , firearm_factions],

  
#["musket", "Musket", [("rifle_musketoonpel",0)], itp_type_musket|itp_crush_through|itp_merchandise|itp_cant_reload_on_horseback|itp_two_handed|itp_primary, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 1160, weight(7.5)|difficulty(0)|spd_rtng(25)|shoot_speed(120)|abundance(38)|thrust_damage(80 ,cut)|max_ammo(1)|accuracy(67), imodbits_gun, musket_trigger , firearm_factions], 
#["musket_2s", "Musket", [("rifle_2barrel_star",0),("rifle_2barrel_star_copy",ixmesh_carry)], itp_type_musket|itp_crush_through|itp_merchandise|itp_two_handed|itp_primary,  itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 3800, weight(5.25)|difficulty(0)|spd_rtng(20)|shoot_speed(120)|abundance(30)|thrust_damage(70 ,cut)|max_ammo(2)|accuracy(79), imodbits_gun, musket_trigger , firearm_factions],
  
#["musket_veteran", "Musket", [("rifle_musket",0),("rifle_musket_copy",ixmesh_carry)], itp_type_musket|itp_crush_through|itp_merchandise|itp_cant_reload_on_horseback|itp_two_handed|itp_primary|itp_bonus_against_shield,  itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 2100, weight(6.5)|difficulty(0)|spd_rtng(29)|shoot_speed(140)|thrust_damage(73,pierce)|max_ammo(1)|accuracy(82), imodbits_gun, musket_trigger , firearm_factions],

["musket_cavalry", "Musket", [("french_dragoon_musket",0)], itp_type_musket|itp_crush_through|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield,  itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 15000, weight(4.25)|difficulty(0)|spd_rtng(29)|shoot_speed(142)|thrust_damage(80,pierce)|max_ammo(1)|accuracy(90), imodbits_gun,musket_trigger , [fac_kingdom_8]],
    
["musket_noble", "Musket", [("french_charleville",0)], itp_type_musket|itp_crush_through|itp_two_handed|itp_primary|itp_bonus_against_shield,  itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 28000, weight(5.75)|difficulty(0)|spd_rtng(40)|shoot_speed(165)|abundance(40)|thrust_damage(93,pierce)|max_ammo(1)|accuracy(95), imodbits_gun,musket_trigger , [fac_dwarf]],


 
["musket_rifle", "Musket", [("french_versailles",0)], itp_type_musket|itp_crush_through|itp_cant_reload_on_horseback|itp_two_handed|itp_primary|itp_next_item_as_melee|itp_bonus_against_shield,  itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 15000, weight(3.75)|difficulty(0)|spd_rtng(35)|shoot_speed(160)|thrust_damage(130,pierce)|max_ammo(1)|accuracy(100), imodbits_gun, musket_trigger , [fac_dwarf]], 
["musket_rifle_melee", "Jarid", [("french_versailles",0)], itp_type_polearm|itp_two_handed|itp_offset_lance|itp_primary|itp_wooden_parry|itp_no_blur, itc_cutting_spear|itcf_carry_crossbow_back, 345, weight(2.25)|difficulty(0)|spd_rtng(92)|weapon_length(165)|swing_damage(20,cut)|thrust_damage(33,pierce), imodbits_polearm ],

["light_muscket_1", "Linear_Hackenbuchse", [("Gun_Empire_Light_Muscket_B_P1_01",0)], itp_type_musket|itp_crush_through|itp_merchandise|itp_two_handed|itp_primary|itp_cant_reload_on_horseback, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 3600, weight(3)|difficulty(0)|spd_rtng(35)|shoot_speed(230)|thrust_damage(70,pierce)|max_ammo(1)|accuracy(80), imodbits_gun
, musket_trigger, firearm_factions],
["light_muscket_2", "Hunting_Hackenbuchse", [("Gun_Empire_Light_Muscket_A_P1_01", 0)], itp_type_musket|itp_crush_through|itp_merchandise|itp_two_handed|itp_primary|itp_cant_reload_on_horseback, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 3600, weight(3)|difficulty(0)|spd_rtng(33)|shoot_speed(220)|thrust_damage(75,pierce)|max_ammo(1)|accuracy(83), imodbits_gun
, musket_trigger, firearm_factions],
["light_muscket_3", "Hunting_Hackenbuchse", [("Gun_Empire_Light_Muscket_C_P1_01", 0)], itp_type_musket|itp_crush_through|itp_merchandise|itp_two_handed|itp_primary|itp_cant_reload_on_horseback, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 5400, weight(3)|difficulty(0)|spd_rtng(31)|shoot_speed(220)|thrust_damage(82,pierce)|max_ammo(1)|accuracy(90), imodbits_gun
, musket_trigger, firearm_factions],
["light_muscket_4", "Hunting_Hackenbuchse", [("Gun_Empire_Light_Muscket_D_P1_01", 0)], itp_type_musket|itp_crush_through|itp_merchandise|itp_two_handed|itp_primary|itp_cant_reload_on_horseback, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 5400, weight(3)|difficulty(0)|spd_rtng(28)|shoot_speed(220)|thrust_damage(90,pierce)|max_ammo(1)|accuracy(97), imodbits_gun
, musket_trigger, firearm_factions],

["medium_muscket_1", "Linear_Hackenbuchse", [("Gun_Empire_Medium_Muscket_D_P1_01", 0)], itp_type_musket|itp_crush_through|itp_merchandise|itp_two_handed|itp_primary|itp_cant_reload_on_horseback, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 7000, weight(4)|difficulty(0)|spd_rtng(30)|shoot_speed(240)|thrust_damage(90,pierce)|max_ammo(1)|accuracy(80), imodbits_gun, musket_trigger, firearm_factions],
["medium_muscket_2", "Doppelaufbuchse", [("Gun_Empire_Medium_Muscket_E_P1_01", 0)], itp_type_musket|itp_crush_through|itp_merchandise|itp_two_handed|itp_primary|itp_cant_reload_on_horseback, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 7000, weight(6)|difficulty(0)|spd_rtng(25)|shoot_speed(240)|thrust_damage(80,pierce)|max_ammo(2)|accuracy(75), imodbits_gun, musket_trigger, firearm_factions],
["medium_muscket_3", "Sniper_Hackenbuchse", [("Gun_Empire_Medium_Muscket_F_P1_01", 0)], itp_type_musket|itp_crush_through|itp_merchandise|itp_two_handed|itp_primary|itp_cant_reload_on_horseback, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 7000, weight(5)|difficulty(0)|spd_rtng(27)|shoot_speed(240)|thrust_damage(100,pierce)|max_ammo(1)|accuracy(90), imodbits_gun, musket_trigger, firearm_factions],

["heavy_muscket_1", "Trench_Hackenbuchse", [("Gun_Empire_Heavy_Muscket_A_P1_01", 0)], itp_type_musket|itp_crush_through|itp_merchandise|itp_two_handed|itp_primary|itp_cant_reload_on_horseback, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 10000, weight(4)|difficulty(0)|spd_rtng(30)|shoot_speed(250)|thrust_damage(110,pierce)|max_ammo(1)|accuracy(75), imodbits_gun, musket_trigger, firearm_factions],
["heavy_muscket_2", "Nuln_Bockgewehre", [("Gun_Empire_Heavy_Muscket_B_P1_01", 0)], itp_type_musket|itp_crush_through|itp_merchandise|itp_two_handed|itp_primary|itp_cant_reload_on_horseback, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 10000, weight(6)|difficulty(0)|spd_rtng(30)|shoot_speed(250)|thrust_damage(100,pierce)|max_ammo(2)|accuracy(75), imodbits_gun, musket_trigger, firearm_factions],
["heavy_muscket_3", "Sniper_Hackenbuchse", [("Gun_Empire_Heavy_Muscket_E_P1_01", 0)], itp_type_musket|itp_crush_through|itp_merchandise|itp_two_handed|itp_primary|itp_cant_reload_on_horseback, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 10000, weight(5)|difficulty(0)|spd_rtng(30)|shoot_speed(250)|thrust_damage(150,pierce)|max_ammo(1)|accuracy(90), imodbits_gun, musket_trigger, firearm_factions],
["heavy_muscket_4", "Ostland_Edel_Doppelaufbuchse", [("Gun_Empire_Heavy_Muscket_F_P1_01", 0)], itp_type_musket|itp_crush_through|itp_merchandise|itp_two_handed|itp_primary|itp_cant_reload_on_horseback, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 10000, weight(8)|difficulty(0)|spd_rtng(30)|shoot_speed(250)|thrust_damage(120,pierce)|max_ammo(2)|accuracy(90), imodbits_gun, musket_trigger, firearm_factions],


["hand_cannon", "Hand Cannon", [("cannon2",0)], itp_type_musket|itp_crush_through|itp_unique|itp_primary|itp_two_handed|itp_bonus_against_shield|itp_cant_reload_while_moving ,itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 50000 , weight(30.0)|abundance(5)|difficulty(0)|spd_rtng(15)| shoot_speed(100)| thrust_damage(150 ,pierce)|max_ammo(1)|accuracy(60),imodbits_gun,  hand_cannon_trigger , [fac_dwarf]],
["hand_cannon_2", "Hand Cannon", [("cannon2",0)], itp_type_musket|itp_crush_through|itp_unique|itp_primary|itp_two_handed|itp_bonus_against_shield|itp_cant_reload_while_moving ,itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 50000 , weight(30.0)|abundance(5)|difficulty(0)|spd_rtng(25)| shoot_speed(120)| thrust_damage(180 ,pierce)|max_ammo(1)|accuracy(65),imodbits_gun,  hand_cannon_trigger , [fac_dwarf]],
["hand_cannon_3", "Hand Cannon", [("Gun_Empire_Heavy_gunner",0)], itp_type_musket|itp_crush_through|itp_unique|itp_primary|itp_two_handed|itp_bonus_against_shield|itp_cant_reload_while_moving ,itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 50000 , weight(30.0)|abundance(5)|difficulty(0)|spd_rtng(35)| shoot_speed(140)| thrust_damage(210 ,pierce)|max_ammo(1)|accuracy(70),imodbits_gun,  hand_cannon_trigger , [fac_dwarf]],
["hand_cannon_4", "Hand Cannon", [("Gun_Empire_Heavy_gunner",0)], itp_type_musket|itp_crush_through|itp_unique|itp_primary|itp_two_handed|itp_bonus_against_shield|itp_cant_reload_while_moving ,itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 50000 , weight(30.0)|abundance(5)|difficulty(0)|spd_rtng(40)| shoot_speed(160)| thrust_damage(240 ,pierce)|max_ammo(1)|accuracy(75),imodbits_gun,  hand_cannon_trigger , [fac_dwarf]],

["samopal", "Handmade_Firearm", [("samopal_a",0)], itp_type_musket|itp_crush_through|itp_merchandise|itp_primary, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 450, weight(6)|difficulty(0)|spd_rtng(23)|shoot_speed(112)|thrust_damage(56,pierce)|max_ammo(1)|accuracy(70), imodbits_gun, musket_trigger, firearm_factions],

["old_musket", "old_musket", [("mushket_old_a",0)], itp_type_musket|itp_crush_through|itp_merchandise|itp_two_handed|itp_primary|itp_cant_reload_on_horseback, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 640, weight(7)|difficulty(0)|spd_rtng(25)|shoot_speed(130)|thrust_damage(69,pierce)|max_ammo(1)|accuracy(78), imodbits_gun
, musket_trigger, firearm_factions],
["good_musket", "Wheellock_Musket", [("mushket_b", 0)], itp_type_musket|itp_crush_through|itp_merchandise|itp_two_handed|itp_primary|itp_cant_reload_on_horseback, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 3600, weight(6.25)|difficulty(0)|spd_rtng(31)|shoot_speed(152)|thrust_damage(75,pierce)|max_ammo(1)|accuracy(83), imodbits_gun
, musket_trigger, firearm_factions],
["mushket_udarniy", "Miquelet_Musket", [("evr_musket_udarniy_b", 0)], itp_type_musket|itp_crush_through|itp_merchandise|itp_two_handed|itp_primary|itp_cant_reload_on_horseback, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 7000, weight(5.75)|difficulty(0)|spd_rtng(27)|shoot_speed(160)|thrust_damage(82,pierce)|max_ammo(1)|accuracy(90), imodbits_gun
, musket_trigger, firearm_factions],
["eoro_musket", "European_Musket", [("evr_musket_udarniy_a", 0)], itp_type_musket|itp_crush_through|itp_merchandise|itp_two_handed|itp_primary|itp_cant_reload_on_horseback, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 10000, weight(5.75)|difficulty(0)|spd_rtng(30)|shoot_speed(165)|thrust_damage(90,pierce)|max_ammo(1)|accuracy(97), imodbits_gun
, musket_trigger, firearm_factions],

["turk_musket_fitil", "turk_Matchlock_Musket", [("musket_turk_fitil_pure", 0)], itp_type_musket|itp_crush_through|itp_merchandise|itp_two_handed|itp_primary|itp_cant_reload_on_horseback, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 1160, weight(7.75)|difficulty(0)|spd_rtng(18)|shoot_speed(139)|thrust_damage(73,pierce)|max_ammo(1)|accuracy(75), imodbits_gun
, musket_trigger, arab_factions],
["turk_musket_koleso", "turk_Wheellock_Musket", [("musket_turk_koleso", 0)], itp_type_musket|itp_crush_through|itp_merchandise|itp_two_handed|itp_primary|itp_cant_reload_on_horseback, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 3000, weight(7.75)|difficulty(0)|spd_rtng(21)|shoot_speed(150)|thrust_damage(78,pierce)|max_ammo(1)|accuracy(80), imodbits_gun
, musket_trigger, arab_factions],
["turk_musket", "turk_Miquelet_Musket", [("musket_turk_udarniy_b", 0)], itp_type_musket|itp_crush_through|itp_merchandise|itp_two_handed|itp_primary|itp_cant_reload_on_horseback, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 5000, weight(6)|difficulty(0)|spd_rtng(24)|shoot_speed(153)|thrust_damage(85,pierce)|max_ammo(1)|accuracy(88), imodbits_gun
, musket_trigger, arab_factions],
["turk_musket_good", "Turkish_Musket", [("musket_turk_udarniy_b", 0)], itp_type_musket|itp_crush_through|itp_merchandise|itp_two_handed|itp_primary|itp_cant_reload_on_horseback, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 15000, weight(6)|difficulty(0)|spd_rtng(26)|shoot_speed(163)|thrust_damage(93,pierce)|max_ammo(1)|accuracy(92), imodbits_gun
, musket_trigger, arab_factions],

["carbine_old", "Matchlock_Carbine", [("karabin_old_a", 0)], itp_type_musket|itp_crush_through|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 960, weight(5.0)|difficulty(0)|spd_rtng(35)|shoot_speed(120)|thrust_damage(62,pierce)|max_ammo(1)|accuracy(72), imodbits_gun
, musket_trigger, firearm_factions],
["carbine", "Wheellock_Carbine", [("karabin_b", 0)], itp_type_musket|itp_crush_through|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 3400, weight(4.25)|difficulty(0)|spd_rtng(40)|shoot_speed(125)|thrust_damage(68,pierce)|max_ammo(1)|accuracy(78), imodbits_gun
, musket_trigger, firearm_factions],
["carbine_batarey", "Miquelet_Carbine", [("karabin_batarey", 0)], itp_type_musket|itp_crush_through|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 4800, weight(4.25)|difficulty(0)|spd_rtng(43)|shoot_speed(130)|thrust_damage(72,pierce)|max_ammo(1)|accuracy(80), imodbits_gun
, musket_trigger, firearm_factions],
["carbine_batarey_2shot", "barreled_Wheellock_Carbine", [("karabin_2stwolB", 0)], itp_type_musket|itp_crush_through|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 9600, weight(3.25)|difficulty(0)|spd_rtng(25)|shoot_speed(131)|thrust_damage(70,pierce)|max_ammo(2)|accuracy(80), imodbits_gun
, musket_trigger, firearm_factions],
["carbine_batarey_good", "crafted_Carbine", [("karabin_batarey_good", 0)], itp_type_musket|itp_crush_through|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 5500, weight(4.25)|difficulty(0)|spd_rtng(44)|shoot_speed(132)|thrust_damage(75,pierce)|max_ammo(1)|accuracy(81), imodbits_gun
, musket_trigger, firearm_factions],



["torch",         "Torch", [("club",0)], itp_type_one_handed_wpn|itp_primary, itc_scimitar, 11 , weight(2.5)|difficulty(0)|spd_rtng(95)| weapon_length(95)|swing_damage(11 , blunt)| thrust_damage(0 ,  pierce),imodbits_none, [(ti_on_init_item, [(set_position_delta,0,60,0),(particle_system_add_new, "psys_torch_fire"),(particle_system_add_new, "psys_torch_smoke"),(set_current_color,150, 130, 70),(add_point_light, 10, 30),])]],

["lyre",         "Lyre", [("lyre",0)], itp_type_shield|itp_wooden_parry|itp_civilian, itcf_carry_bow_back,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),0 ],
["lute",         "Lute", [("lute",0)], itp_type_shield|itp_wooden_parry|itp_civilian, itcf_carry_bow_back,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),0 ],


["court_dress", "Court Dress", [("court_dress",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(4)|difficulty(0) ,imodbits_cloth],
["rich_outfit", "Rich Outfit", [("merchant_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
#["leather_steppe_cap_c", "Leather Steppe Cap", [("leather_steppe_cap_c",0)], itp_type_head_armor   ,0, 51 , weight(2)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
#["felt_steppe_cap", "Felt Steppe Cap", [("felt_steppe_cap",0)], itp_type_head_armor   ,0, 237 , weight(2)|abundance(100)|head_armor(16)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],

["black_hood", "Black Hood", [("hood_black",0)], itp_type_head_armor|itp_merchandise   ,0, 193 , weight(2)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0) ,imodbits_cloth],
["black_hood_mask", "Black Hood", [("shadow_mask",0)], itp_type_head_armor|itp_unique   ,0, 10000 , weight(2)|abundance(1)|head_armor(60)|body_armor(40)|leg_armor(30) ,imodbits_cloth],
["ninjia_armor", "Assassin's Armor", [("shadow_outfit_c",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 9216,lamellar_armor_tier_4,imodbits_plate],



["light_leather", "Light Leather", [("nightswatch",0)], merc_body_armor   ,0, 940, weight(11)|abundance(60)|head_armor(0)|body_armor(32)|leg_armor(15)|difficulty(5),imodbits_cloth , [], [fac_beast]],
["light_leather_boots",  "Light Leather Boots", [("light_leather_boots",0)], itp_type_foot_armor|itp_merchandise| itp_attach_armature,0, 91 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(15)|difficulty(0) ,imodbits_cloth],


["tunic_with_green_cape", "Tunic with Green Cape", [("peasant_man_a",0)], merc_body_armor|itp_civilian ,0, 50,cloth_tier_2,imodbits_cloth , [], [fac_kingdom_5]],
["keys", "Ring of Keys", [("throwing_axe_a",0)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield,itc_scimitar,240, weight(5)|spd_rtng(98)| swing_damage(29,cut)|max_ammo(5)|weapon_length(53),imodbits_thrown ],
["bride_dress", "Bride Dress", [("bride_dress",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 100,cloth_tier_1,imodbits_cloth],
["bride_crown", "Crown of Flowers", [("bride_crown",0)],  itp_type_head_armor| itp_doesnt_cover_hair|itp_civilian|itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bride_shoes", "Bride Shoes", [("bride_shoes",0)], itp_type_foot_armor|itp_civilian| itp_attach_armature ,0, 30 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],

["practice_bow_2","Practice Bow", [("hunting_bow",0), ("hunting_bow_carry",ixmesh_carry)], itp_type_bow|itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back, 0, weight(1.5)|spd_rtng(90)| shoot_speed(40)| thrust_damage(16, blunt),imodbits_bow ],
["practice_arrows_2","Practice Arrows", [("arena_arrow",0),("flying_arrow",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(80)| thrust_damage(5, blunt),imodbits_missile],



["drow_leather_boots", "drow_leather_boots", [("drow_leather_boots", 0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 2945, weight(1)|abundance(10)|head_armor(0)|body_armor(0)|leg_armor(20), imodbits_cloth , [], [fac_beast]],
["drow_elite_boots", "drow_elite_boots", [("drow_elite_boots", 0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 4047, weight(1)|abundance(10)|head_armor(0)|body_armor(0)|leg_armor(30), imodbits_armor , [], [fac_beast]],


["felguard_body", "FelGuard_body", [("FelGuard_body",0)], itp_type_body_armor|itp_covers_legs|itp_unique, 0, 50000, weight(24)|abundance(100)|head_armor(0)|body_armor(80)|leg_armor(30)|difficulty(20), imodbits_armor ],
["felguard_calf", "FelGuard_calf", [("FelGuard_calf",0)], itp_type_foot_armor|itp_attach_armature|itp_unique, 0, 50000, weight(3.5)|abundance(100)|head_armor(40)|body_armor(40)|leg_armor(40)|difficulty(20), imodbits_armor ],

["toumingtou", "toumingtou", [("toumingtou",0)], itp_type_head_armor|itp_civilian| itp_doesnt_cover_hair|itp_unique, 0, 4500, weight(2.75)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(9), imodbits_plate],

["toumingdun", "toumingdun", [("toumingshen",0)], itp_type_shield|itp_unique,itcf_carry_round_shield, 1597, weight(4)|shield_hit_points(500)|body_armor(0)|spd_rtng(61)|shield_width(30), imodbits_shield ],

["assassin_dagger",         "Dagger", [("dagger_b",0),("dagger_b_scabbard",ixmesh_carry),("dagger",imodbits_good),("dagger_b_scabbard",ixmesh_carry|imodbits_good)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry, itcf_thrust_onehanded| itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn,5000 , weight(0.75)|difficulty(13)|spd_rtng(150)| weapon_length(50)|swing_damage(25 , cut)| thrust_damage(75 ,  pierce),imodbit_balanced|imodbit_tempered|imodbit_masterwork| imodbit_deadly| imodbit_sharp ],

#["duelrapier", "Duel Rapier", [("lui_duelrapier_copy",0)], itp_type_shield|itp_merchandise, 0, 370, weight(3)|hit_points(500)|body_armor(15)|spd_rtng(99)|shield_width(10)|shield_height(105),imodbits_none],
#["dueling_scimitar", "Dueling scimitar", [("lui_duelscimitar_copy",0)], itp_type_shield, 0, 195 , weight(2)|hit_points(1000)|body_armor(17)|spd_rtng(100)|shield_width(5)|shield_height(100),imodbits_none],
#["dueling_saber", "Dueling Saber", [("lui_duelsaber_copy",0)], itp_type_shield, itcf_carry_sword_left_hip, 195 , weight(2)|hit_points(1000)|body_armor(17)|spd_rtng(100)|shield_width(5)|shield_height(100),imodbits_none],
["dueling_dagger", "Dueling Dagger", [("dueldagger",0)], itp_merchandise|itp_type_shield, 0, 195 , weight(1)|hit_points(500)|body_armor(22)|spd_rtng(47)|shield_width(5)|shield_height(40),imodbits_none , [], [fac_neutral,fac_commoners,fac_beast]],
#["dueling_axe", "Dueling axe", [("lui_knightaxeonehb_copy",0)], itp_merchandise|itp_type_shield, 0, 195 , weight(1)|hit_points(1000)|body_armor(38)|spd_rtng(100)|shield_width(5)|shield_height(93),imodbits_none],
#["dueling_sword", "Dueling sword", [("sword_medieval_d_long_copy",0)], itp_merchandise|itp_type_shield, 0, 195 , weight(1)|hit_points(1000)|body_armor(17)|spd_rtng(100)|shield_width(35)|shield_height(105),imodbits_none],





["assassin_mail_coif", "assassin Mail Coif", [("assassin_helmet2",0)], itp_merchandise| itp_type_head_armor ,0, 2730 , weight(2)|abundance(100)|head_armor(90)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_6]],

#special_item

["khorne_axe", "Drink blood", [("thrud_axe",0)], itp_type_two_handed_wpn|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_can_knock_down|itp_crush_through|itp_extra_penetration, itc_nodachi, 30000, weight(6.5)|difficulty(24)|spd_rtng(130)|weapon_length(150)|swing_damage(55,pierce)|thrust_damage(0,pierce), imodbits_axe|imodbit_masterwork,],


["ebony_blade", "Ebony Blade", [("ebonyblade",0)], itp_unique|itp_two_handed|itp_type_two_handed_wpn|itp_primary|itp_extra_penetration|itp_can_penetrate_shield, itc_nodachi|itcf_carry_sword_back, 
50000 , weight(1.75)|difficulty(30)|spd_rtng(130)| weapon_length(150)|swing_damage(60 , pierce)| thrust_damage(0 ,  pierce),imodbits_sword_high , [
 (ti_on_weapon_attack, 
  [
   (store_trigger_param_1, ":shooter"),
   (call_script,"script_cf_agent_cleave",":shooter", 1, 0),
  ]),
],],
["dawnbreaker_1", "Dawnbreaker Staff", [("tianshijian1", 0)], itp_merchandise|itp_type_pistol|itp_primary|itp_next_item_as_melee|itp_is_magic_staff ,itcf_reload_pistol|itcf_shoot_pistol|itcf_carry_sword_back,
 50000 , weight(3.25)|difficulty(0)|spd_rtng(90) | shoot_speed(150) | thrust_damage(80 ,pierce)|max_ammo(3)|accuracy(99),imodbits_magic_staff, magic_cast_trigger , [fac_elf] ], 
["dawnbreaker", "Dawnbreaker", [("tianshijian1",0)], itp_unique|itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_crush_through|itp_is_magic_staff, itc_greatsword|itcf_carry_sword_back, 
50000 , weight(2)|difficulty(18)|spd_rtng(120)| weapon_length(190)|swing_damage(55 , pierce)| thrust_damage(40 ,  pierce),imodbits_sword_high, ],

["swiftness_sword", "Sword of Swiftness", [("ElvenSword",0)], itp_crush_through|itp_type_one_handed_wpn|itp_unique|itp_primary, itc_longsword|itcf_carry_sword_back,
 50000 , weight(2.0)|difficulty(15)|spd_rtng(100)| weapon_length(125)|swing_damage(45, pierce)| thrust_damage(32 ,  pierce),imodbits_sword_high],
 
["flamberge_fire",         "Flamberge Zweihander", [("ssdj34",0),("ssdj34", ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_crush_through|itp_can_knock_down|itp_can_penetrate_shield|itp_unique|itp_cant_use_on_horseback, itc_greatsword, 50000 , weight(3.75)|difficulty(18)|spd_rtng(95)| weapon_length(150)|swing_damage(60, pierce)| thrust_damage(36 ,  pierce),imodbit_balanced|imodbit_tempered|imodbit_masterwork| imodbit_deadly| imodbit_sharp, [(ti_on_init_item, [
(try_begin),
(eq, "$g_weapon_fire_particle", 0),
(set_current_color,600,510,400),(set_position_delta,0,75,0),
(store_trigger_param_2, ":troop_no"),
(troop_is_hero, ":troop_no"),
(particle_system_add_new, "psys_items_fire_blue"),
(try_end),
])]],

["trgba", "trgba", [("glassbattleaxe_2",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_can_penetrate_shield|itp_extra_penetration|itp_crush_through|itp_unique, itc_nodachi|itcf_carry_axe_back, 50000, weight(3.0)|difficulty(18)|spd_rtng(100)|weapon_length(120)|swing_damage(60,pierce)|thrust_damage(0,pierce), imodbits_axe|imodbit_masterwork, [], ne_faction],
            
["frostmourne", "Frostmourne", [("DemonSword01",0),("DemonSword01", ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_can_penetrate_shield|itp_bonus_against_shield|itp_extra_penetration|itp_unique, itc_bastardsword|itc_claymore|itcf_carry_sword_back,20000 , weight(2.25)|difficulty(10)|spd_rtng(88)| weapon_length(140)|swing_damage(45 , pierce)| thrust_damage(50 ,  pierce),imodbit_balanced|imodbit_tempered|imodbit_masterwork| imodbit_deadly| imodbit_sharp,[(ti_on_init_item, [
(try_begin),
 (eq, "$g_weapon_fire_particle", 0),
 (set_position_delta,0,50,0),
 (store_trigger_param_2, ":troop_no"),
 (troop_is_hero, ":troop_no"),
 (particle_system_add_new, "psys_frostfang_snowflake"),
 (particle_system_add_new, "psys_frostfang_smoke"),
(try_end),
])]],

["grief_1", "The Grief",  [("Reitschwert_Pistolier_D_01", 0), ("Reitschwert_Scabbard_Pistolier_D_01", ixmesh_carry)], itp_unique|itp_type_pistol|itp_crush_through|itp_primary|itp_next_item_as_melee|itp_is_magic_staff ,itcf_reload_pistol|itcf_shoot_pistol|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 30000 , weight(3.25)|difficulty(0)|spd_rtng(40) | shoot_speed(140) | thrust_damage(75 ,pierce)|max_ammo(2)|accuracy(82),imodbit_balanced|imodbit_tempered|imodbit_masterwork| imodbit_deadly| imodbit_sharp, [(ti_on_init_item, [
(try_begin),
(eq, "$g_weapon_fire_particle", 0),
(set_position_delta,0,50,0),
(store_trigger_param_2, ":troop_no"),
(troop_is_hero, ":troop_no"),
(particle_system_add_new, "psys_frostfang_snowflake"),
(particle_system_add_new, "psys_frostfang_smoke"),
(try_end),
])]+magic_cast_trigger], 
["grief_2", "The Grief", [("Reitschwert_Pistolier_D_01", 0), ("Reitschwert_Scabbard_Pistolier_D_01", ixmesh_carry)], itp_type_one_handed_wpn|itp_secondary|itp_primary|itp_extra_penetration|itp_crush_through, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,30000, weight(1.5)|difficulty(0)|spd_rtng(150)|weapon_length(125)|swing_damage(45,pierce)|thrust_damage(100,pierce), imodbit_balanced|imodbit_tempered|imodbit_masterwork| imodbit_deadly| imodbit_sharp,[(ti_on_init_item, [
(try_begin),
(eq, "$g_weapon_fire_particle", 0),
(set_position_delta,0,50,0),
(store_trigger_param_2, ":troop_no"),
(troop_is_hero, ":troop_no"),
(particle_system_add_new, "psys_frostfang_snowflake"),
(particle_system_add_new, "psys_frostfang_smoke"),
(try_end),
])]],

["plague_staff_1", "Plague Scythe", [("Scythe_Crusher_A_01",0)], itp_type_pistol|itp_crush_through|itp_next_item_as_melee|itp_primary|itp_is_magic_staff ,itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_spear,
 20000 , weight(3.25)|difficulty(0)|spd_rtng(45) | shoot_speed(200) | thrust_damage(85 ,pierce)|max_ammo(1)|accuracy(85),imodbits_magic_staff, magic_cast_trigger , [fac_undeads_2] ], 
["plague_staff", "Plague Scythe", [("Scythe_Crusher_A_01",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_can_knock_down|itp_crush_through|itp_is_glaive, itc_nodachi|itcf_carry_spear, 5000, weight(1.5)|weapon_length(167)|difficulty(0)|spd_rtng(110)|abundance(10)|swing_damage(45, pierce)|thrust_damage(0, pierce), imodbits_axe|imodbit_masterwork ],




["mjolnir",         "mjolnir", [("Mjolnir",0),("Mjolnir", ixmesh_carry)], itp_type_thrown|itp_crush_through|itp_primary|itp_next_item_as_melee|itp_unique ,itcf_throw_stone,50000, weight(5)|difficulty(4)|spd_rtng(91)| shoot_speed(70)| thrust_damage(50 ,  blunt)|max_ammo(2)|weapon_length(75),imodbits_thrown,thunder_weapon_trigger+mjolnir_trigger+missile_distance_trigger],

["mjolnir_melee",         "mjolnir", [("Mjolnir",0),("Mjolnir", ixmesh_carry)], itp_type_one_handed_wpn|itp_can_knock_down|itp_crush_through| itp_primary|itp_two_handed|itp_unbalanced|itp_unique, itc_nodachi|itcf_carry_spear,50000 , weight(6)|difficulty(25)|spd_rtng(83)| weapon_length(75)|swing_damage(50 , blunt)| thrust_damage(0 ,  pierce),imodbits_mace, thunder_weapon_trigger_2+mjolnir_trigger],

["angelic_alliance", "Heaven Alliance", [("retribution1h",0),("spak_book", ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed| itp_primary|itp_crush_through|itp_can_knock_down|itp_can_penetrate_shield|itp_unique, itc_greatsword|itcf_carry_sword_back, 50000 , weight(2.25)|difficulty(21)|spd_rtng(97)| weapon_length(155)|swing_damage(50 , pierce)| thrust_damage(35 ,  pierce),imodbit_balanced|imodbit_tempered|imodbit_masterwork| imodbit_deadly| imodbit_sharp, [(ti_on_init_item, [
(try_begin),
(eq, "$g_weapon_fire_particle", 0),
(set_current_color,600,510,400),(set_position_delta,0,75,0),
(store_trigger_param_2, ":troop_no"),
(troop_is_hero, ":troop_no"),
(particle_system_add_new, "psys_items_fire_white"),(add_point_light, 10, 30),
(try_end),
])]],
["zamorak", "zamorak", [("zamorak",0)], itp_unique|itp_type_two_handed_wpn|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_can_knock_down|itp_crush_through|itp_extra_penetration, itc_greatsword, 50000, weight(6.5)|difficulty(21)|spd_rtng(130)|weapon_length(150)|swing_damage(55,pierce)|thrust_damage(0,pierce), imodbits_axe|imodbit_masterwork,],

["calibur",  "Calibur", [("scottish_claymore",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_can_penetrate_shield|itp_bonus_against_shield|itp_extra_penetration|itp_unique, itc_claymore|itcf_carry_sword_back, 50000 , weight(2.5)|difficulty(18)|spd_rtng(100)| weapon_length(120)|swing_damage(40 , pierce)| thrust_damage(50 ,  pierce),imodbits_sword_high , [], [fac_kingdom_4]],

["excalibur_1", "Excalibur", [("henrysword",0),("henrysword_scabbard_02", ixmesh_carry)], itp_type_two_handed_wpn|itp_primary|itp_can_penetrate_shield|itp_bonus_against_shield|itp_extra_penetration|itp_unique, itc_bastardsword|itc_claymore|itcf_show_holster_when_drawn|itcf_carry_sword_back,50000 , weight(2.25)|difficulty(12)|spd_rtng(115)| weapon_length(145)|swing_damage(65 , pierce)| thrust_damage(50 ,  pierce),imodbit_balanced|imodbit_tempered|imodbit_masterwork| imodbit_deadly| imodbit_sharp, ],
["excalibur_2", "Excalibur without scabbard", [("henrysword",0)], itp_type_two_handed_wpn|itp_primary|itp_can_penetrate_shield|itp_bonus_against_shield|itp_extra_penetration|itp_unique, itc_bastardsword|itc_claymore|itcf_carry_sword_back,50000 , weight(2.25)|difficulty(15)|spd_rtng(115)| weapon_length(145)|swing_damage(65 , pierce)| thrust_damage(50 ,  pierce),imodbit_balanced|imodbit_tempered|imodbit_masterwork| imodbit_deadly| imodbit_sharp, ],

["angel_blade", "angel_blade", [("SigmarsSword1",0),("spak_book", ixmesh_carry)], itp_type_two_handed_wpn| itp_primary|itp_crush_through|itp_can_knock_down|itp_can_penetrate_shield|itp_unique, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 50000 , weight(2.25)|difficulty(18)|spd_rtng(97)| weapon_length(155)|swing_damage(50 , pierce)| thrust_damage(35 ,  pierce),imodbit_balanced|imodbit_tempered|imodbit_masterwork| imodbit_deadly| imodbit_sharp,holy_weapon_trigger],


["flame_blade", "flame_blade", [("jianhong",0),("jianhong", ixmesh_carry)], itp_type_two_handed_wpn| itp_primary|itp_crush_through|itp_can_knock_down|itp_can_penetrate_shield|itp_unique, itc_bastardsword|itcf_carry_sword_back, 50000 , weight(2.25)|difficulty(15)|spd_rtng(97)| weapon_length(155)|swing_damage(55 , pierce)| thrust_damage(35 ,  pierce),imodbit_balanced|imodbit_tempered|imodbit_masterwork| imodbit_deadly| imodbit_sharp,[(ti_on_init_item, [
(try_begin),
(eq, "$g_weapon_fire_particle", 0),
(set_position_delta,0,75,0),
(store_trigger_param_2, ":troop_no"),
(troop_is_hero, ":troop_no"),
(particle_system_add_new, "psys_items_fire_red"),
(try_end),
])]],


["aurora_blade", "Aurora blade", [("WAoRSwordA",0),("WAoRSwordA", ixmesh_carry)], itp_type_one_handed_wpn| itp_primary|itp_crush_through|itp_can_knock_down|itp_unique, itc_longsword|itcf_carry_sword_left_hip, 50000 , weight(2.25)|difficulty(15)|spd_rtng(97)| weapon_length(140)|swing_damage(50 , pierce)| thrust_damage(35 ,  pierce),imodbit_balanced|imodbit_tempered|imodbit_masterwork| imodbit_deadly| imodbit_sharp,[(ti_on_init_item, [
(try_begin),
(eq, "$g_weapon_fire_particle", 0),
(set_position_delta,0,70,0),
(store_trigger_param_2, ":troop_no"),
(troop_is_hero, ":troop_no"),
(particle_system_add_new, "psys_aurora_blade_lightning"),
(try_end),
])]],

 
["jingubang", "jingubang", [("txz_weapon_a02_06",0)], itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_offset_lance|itp_couchable|itp_crush_through|itp_unbalanced|itp_unique, itc_long_glaive|itcf_carry_sword_back, 50000, weight(20)|difficulty(24)|spd_rtng(65)|weapon_length(220)|swing_damage(150,blunt)|thrust_damage(150,blunt), imodbits_polearm ],
 
["serpent_dagger", "Serpent Dagger", [("SerpentDagger",0),("SerpentDagger", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry|itp_unique|itp_crush_through, itcf_thrust_onehanded| itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_carry_dagger_front_left,50000 , weight(0.75)|difficulty(9)|spd_rtng(150)| weapon_length(60)|swing_damage(25 , cut)| thrust_damage(150 ,  pierce),imodbit_balanced|imodbit_masterwork, ],
 
 
["charonscall", "Charons Call", [("CharonsCall",0),("CharonsCall", ixmesh_carry)], itp_type_two_handed_wpn|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_can_knock_down|itp_crush_through|itp_unbalanced|itp_extra_penetration, itc_nodachi|itcf_carry_axe_back, 50000, weight(6.5)|difficulty(15)|spd_rtng(110)|weapon_length(95)|swing_damage(55,pierce)|thrust_damage(0,pierce), imodbits_axe|imodbit_masterwork, [(ti_on_init_item, [
(try_begin),
(eq, "$g_weapon_fire_particle", 0),
(set_position_delta,0,75,0),
(store_trigger_param_2, ":troop_no"),
(troop_is_hero, ":troop_no"),
(particle_system_add_new, "psys_item_blood_Drop"),
(try_end),
])]],

["throwing_gungnir",         "Throwing Gungnir", [("gungnir",0), ("copy_gungnir", ixmesh_flying_ammo)], itp_type_thrown|itp_crush_through|itp_primary|itp_next_item_as_melee|itp_unique ,itcf_throw_javelin|itcf_carry_quiver_back,50000 , weight(5)|difficulty(4)|spd_rtng(87)| shoot_speed(40)| thrust_damage(50 ,  pierce)|max_ammo(2)|weapon_length(80),imodbits_thrown,[
    (ti_on_missile_hit, [
        (store_trigger_param_1, ":shooter"),
        (copy_position,pos51,pos1),
        (call_script, "script_magic_deliver_area_damage", ":shooter", 300, 7, 0),
    ]),
    ]+gungnir_trigger+missile_distance_trigger, [fac_kingdom_12]],
["gungnir", "Gungnir", [("gungnir", 0)], itp_type_polearm|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_cant_use_on_horseback|itp_unique, itc_spear|itcf_carry_spear, 50000, weight(2.5)|weapon_length(150)|difficulty(12)|spd_rtng(95)|abundance(1)|swing_damage(30, pierce)|thrust_damage(200, pierce), imodbits_polearm, gungnir_trigger ],
 
 
 
 
["holy_granata", "Holy_Grenade", [("hhg", 0)], itp_type_thrown|itp_crush_through|itp_unique|itp_primary, itcf_throw_stone, 20000, weight(4)|weapon_length(30)|difficulty(0)|spd_rtng(100)|shoot_speed(30)|abundance(33)|thrust_damage(100, blunt)|max_ammo(30), imodbits_none,[(ti_on_missile_hit, [(store_trigger_param_1, ":shooter"),(copy_position,pos51,pos1),(call_script, "script_magic_deliver_area_damage", ":shooter", 600, 10, 14),]),]+missile_distance_trigger,firearm_factions],
 
["mandolin"," Aiffe's Mandolin", [("lute",0)], itp_type_shield|itp_unique|itp_wooden_parry|itp_civilian, itcf_carry_bow_back,  
 50000 , weight(1.5)|shield_hit_points(10000)|body_armor(40)|spd_rtng(97)|shield_width(50)|shield_height(180)|difficulty(2), imodbits_shield ],
["lordaeron", "lordaeron", [("fix_shield20_a_combined",0)], itp_type_shield|itp_unique, itcf_carry_kite_shield, 50000, weight(3.5)|shield_hit_points(10000)|body_armor(20)|spd_rtng(87)|shield_width(50)|shield_height(80)|difficulty(5), imodbits_shield ],

["death_skull", "Death head", [("helmet_orc_skull",0)], itp_type_fullhelm|itp_unique|itp_fit_to_head, 0, 20000, weight(1.0)|abundance(100)|head_armor(120)|body_armor(0)|leg_armor(0)|difficulty(12), imodbits_plate],


["command_helm", "The Helm of Command", [("gondor_captain_helmet_mail",0)], itp_unique|itp_type_head_armor,0,  20000 , weight(2.75)|abundance(100)|head_armor(90)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate, ],

["caesar_mask","Caesar mask",[("dragonhelm_1",0)],itp_unique|itp_type_fullhelm,0,50000,weight(4)|abundance(15)|head_armor(85)|difficulty(15),imodbits_armor],

["mask_of_blades","maskofblades",[("maskofbladesmale",0)],itp_unique|itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair|itp_fit_to_head,0,20000,weight(2)|head_armor(40)|difficulty(0),imodbits_plate,],

["crimson_guard_plate", "Crimson guard plate", [("Armor_Elite_Khorne",0)], itp_unique|itp_type_body_armor|itp_covers_legs, 0, 50000, weight(30)|abundance(20)|head_armor(13)|body_armor(95)|leg_armor(45)|difficulty(18), imodbits_good_plate, [], [fac_kingdom_9,fac_demon]],
["black_hole_plate", "Ebony mail plate", [("ebonyarmorbody",0)], itp_unique|itp_type_body_armor|itp_covers_legs, 0, 50000, weight(30)|abundance(20)|head_armor(13)|body_armor(85)|leg_armor(45)|difficulty(18), imodbits_good_plate, [], [fac_kingdom_8,fac_undeads_2,fac_beast]],
["enchanter_robe", "Enchanter_Robe", [("wizard_robe_3",0)], itp_unique|itp_type_body_armor|itp_covers_legs ,0, 50000,weight(11)|abundance(30)|head_armor(10)|body_armor(80)|leg_armor(45)|difficulty(6),imodbits_cloth , [], [fac_dark_knights,fac_commoners]],
["undead_scythe", "Death scythe", [("dragonbonescythe",0)], itp_unique|itp_type_two_handed_wpn|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_can_knock_down|itp_crush_through|itp_extra_penetration, itc_guandao, 50000, weight(6.5)|difficulty(30)|spd_rtng(130)|weapon_length(150)|swing_damage(55,pierce)|thrust_damage(0,pierce), imodbits_axe|imodbit_masterwork,],
["black_king_bar", "Black King Bar", [("ebony_long_mace",0)], itp_can_knock_down|itp_crush_through|itp_type_one_handed_wpn|itp_unique|itp_primary, itc_scimitar|itcf_carry_mace_left_hip,50000 , weight(2.5)|difficulty(10)|spd_rtng(100)| weapon_length(100)|swing_damage(50 , pierce)| thrust_damage(0 ,  pierce),imodbits_mace , [], [fac_undeads_2,fac_beast]],
["antimage_shield", "Antimage_Shield", [("fix_lorien_kite", 0)], itp_unique|itp_type_shield|itp_cant_use_on_horseback, itcf_carry_kite_shield, 50000, weight(2)|shield_width(70)|shield_height(70)|abundance(10)|hit_points(5000)|body_armor(200)|spd_rtng(82), imodbits_shield, [], [fac_elf] ],
["black_hole_sword", "black_hole Sword", [("ebonyPersonGreatsword",0)], itp_unique|itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_crush_through|itp_can_knock_down|itp_can_penetrate_shield, itc_greatsword|itcf_carry_sword_back, 50000 , weight(2.75)|difficulty(15)|spd_rtng(130)| weapon_length(150)|swing_damage(55, pierce)| thrust_damage(50,pierce),imodbits_sword_high, [], [fac_undeads_2,fac_beast]],


["khorne_helm", "Chaos Knight Helm", [("Helm_Khorne",0)], itp_unique|itp_type_fullhelm, 0, 
 20000 , weight(2.75)|abundance(100)|head_armor(95)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_good_plate],

["midas_hand","Midas's hand", [("golem_gold_handL",0)], itp_type_hand_armor|itp_unique,0,  50000, weight(2.25)|abundance(100)|body_armor(15)|difficulty(12),imodbits_armor, ],

["ramun_jacket", "Ramun's Leather Jacket", [("leather_jacket_new",0)], itp_unique|itp_type_body_armor|itp_covers_legs ,0, 20000, weight(5)|abundance(30)|head_armor(0)|body_armor(65)|leg_armor(30)|difficulty(1),imodbits_cloth ],

["spellbreak_armor", "spellbreak_armor", [("elf_twiligh_armor",0)], itp_unique|itp_type_body_armor|itp_covers_legs, 0, 20000, weight(28)|abundance(100)|head_armor(20)|body_armor(90)|leg_armor(40)|difficulty(24), imodbits_good_plate],
["dragon_heart_plate", "Dragon Heart_plate", [("longqishi_body",0)], itp_type_body_armor|itp_covers_legs|itp_unique, 0, 50000, weight(30)|abundance(20)|head_armor(13)|body_armor(85)|leg_armor(45)|difficulty(24), imodbits_good_plate, [], [fac_kingdom_8,fac_kingdom_4]],
["assault_plate", "Assault Cuirass", [("Black_Knight",0)], itp_type_body_armor|itp_covers_legs|itp_unique, 0, 50000, weight(30)|abundance(20)|head_armor(13)|body_armor(95)|leg_armor(45)|difficulty(24), imodbits_good_plate],
["shadow_robes", "Cloak of Death`s Shadow", [("nazgul_tvs",0)], itp_type_body_armor|itp_covers_legs|itp_unique, 0, 50000, weight(5)|abundance(20)|head_armor(13)|head_armor(6)|body_armor(70)|leg_armor(18)|difficulty(18), imodbits_armor, [], [fac_kingdom_3]],
["shivas_guard", "Shiva's Guard", [("plate_falcon_armor_silver",0)], itp_type_body_armor|itp_covers_legs|itp_unique, 0, 50000, weight(30)|abundance(20)|head_armor(15)|body_armor(80)|leg_armor(45)|difficulty(21), imodbits_good_plate],
 
["curse_armor", "Armor of the Damned", [("knight_of_molag_bal_armor",0)], itp_type_body_armor|itp_covers_legs|itp_unique, 0, 50000, weight(40)|abundance(20)|head_armor(13)|body_armor(90)|leg_armor(45)|difficulty(21), imodbits_good_plate, [], [fac_undeads_2]],
 
["saint_robe", "Saint Ranan's Robe", [("priest_2",0)],  itp_unique|itp_type_body_armor  |itp_civilian ,0,
  20000,weight(5)|abundance(30)|head_armor(0)|body_armor(65)|leg_armor(30)|difficulty(12),imodbits_cloth ],
["dwarf_crown", "new_sallet", [("DwarfHelmKingCrown",0)], itp_unique|itp_type_head_armor|itp_covers_beard, 0, 
 20000 , weight(2.75)|abundance(100)|head_armor(90)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate,[], [fac_dwarf] ],
 
["sanguine_rose", "Sanguine Rose", [("sanguinerose",0),("sanguinerose",ixmesh_flying_ammo)], itp_unique|itp_type_thrown|itp_is_magic_staff|itp_primary, itcf_throw_stone,
  20000, weight(4)|abundance(90)|spd_rtng(65)|shoot_speed(50)|weapon_length(3)|thrust_damage(100,pierce)|max_ammo(6),imodbits_none, 
  [(ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_troop_id,":troop_id", ":shooter"),
      (eq, "$g_mt_mode", 0),
      (troop_is_hero,":troop_id"),
      
      (assign,":cur_ammo_id","itm_cartridges"),#as default
      (assign,":item_slot_num",4),
      (try_for_range,":cur_item_slot",0,":item_slot_num"),
        (agent_get_item_slot, ":item_no", ":shooter", ":cur_item_slot"),
        (gt,":item_no",-1),
        (eq,":item_no","itm_sanguine_rose"),
        (agent_get_item_cur_ammo, ":cur_ammo", ":shooter", ":cur_item_slot"),
        (gt,":cur_ammo",0),
        (assign,":cur_ammo_id",":item_no"),
        (assign,":item_slot_num",0),#break
      (try_end),
      (agent_get_wielded_item, ":weapon", ":shooter", 0),
      (eq, ":weapon", "itm_sanguine_rose"),
      (eq, ":cur_ammo_id", ":weapon"),
      (assign,":spawn_troop_id",0),
      
      (try_for_range,":unused",0,1),
        (store_random_in_range, ":ran", 0, 7),
        (try_begin),
          (eq,":ran",0),
          (assign,":spawn_troop_id","trp_huge_inferno"),
        (else_try),  
          (eq,":ran",1),
          (assign,":spawn_troop_id","trp_demon_5"),
        (else_try),  
          (eq,":ran",2),
          (assign,":spawn_troop_id","trp_mummy_4"),
        (else_try),  
          (eq,":ran",3),
          (assign,":spawn_troop_id","trp_demon_6"),
        (else_try),  
          (eq,":ran",4),
          (assign,":spawn_troop_id","trp_demon_8"),
        (else_try),  
          (eq,":ran",5),
          (assign,":spawn_troop_id","trp_demon_human_5_2"),
        (else_try),  
          (eq,":ran",6),
          (assign,":spawn_troop_id","trp_demon_4_3"),
          
          
        (try_end),  
        (copy_position, pos51, pos5),
        (call_script,"script_cf_agent_spawn_agent_to_pos51", ":shooter", ":spawn_troop_id", 1),
      (try_end),
    ])],
],
  
["natalya_mark","Natalya's Mark", [("toumingtou",0),("van_helsing_crossbow_bolt_copy",ixmesh_flying_ammo),("van_helsing_crossbow_bolt_bag", ixmesh_carry),("van_helsing_crossbow_bolt_bag", ixmesh_inventory)], itp_unique|itp_type_bolts|itp_can_penetrate_shield|itp_bonus_against_shield|itp_is_magic_staff, itcf_carry_quiver_right_vertical, 20000,weight(2.25)|abundance(35)|weapon_length(55)|thrust_damage(40,pierce)|max_ammo(30),imodbits_missile,natalyas_mark+missile_distance_trigger],
 
["colt1855", "colt1855", [("colt1855",0)], itp_type_musket|itp_crush_through|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_is_magic_staff, itcf_shoot_musket|itc_parry_polearm|itcf_reload_musket|itcf_carry_crossbow_back, 
 50000, weight(2.0)|difficulty(0)|spd_rtng(80)|shoot_speed(180)|thrust_damage(90,pierce)|max_ammo(6)|accuracy(99), imodbits_magic_staff,  musket_trigger+magic_cast_trigger  ],

["trophy_a","Battle Trophy", [("Gold2",0)], itp_type_goods, 0, 2000,weight(3)|abundance(90),imodbits_none],
["trophy_b","War Trophy", [("gems",0)], itp_type_goods, 0, 10000,weight(5)|abundance(60),imodbits_none],
["trophy_c","Epic Trophy", [("jewelchest_high_poly",0)], itp_type_goods|itp_unique, 0, 50000,weight(7)|abundance(30),imodbits_none],

["chest_1","chest", [("chest_gothic",0)], itp_type_goods, 0, 30000,weight(10)|abundance(50),imodbits_none],
["chest_2","chest", [("chest_b",0)], itp_type_goods, 0, 30000,weight(10)|abundance(50),imodbits_none],
["chest_3","chest", [("chest_c",0)], itp_type_goods, 0, 30000,weight(10)|abundance(50),imodbits_none],
["chest_4","chest", [("player_chest",0)], itp_type_goods, 0, 30000,weight(10)|abundance(50),imodbits_none],

#["chest_5","chest", [("package",0)], itp_type_goods, 0, 30000,weight(10)|abundance(50),imodbits_none],
["dragon_knight_lance", "Dragon knight Lance", [("lance22_a",0)], itp_type_polearm|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_couchable|itp_crush_through, itc_greatlance, 30000, weight(5)|difficulty(12)|spd_rtng(75)|weapon_length(280)|swing_damage(0,cut)|thrust_damage(40,pierce)|abundance(30), imodbits_polearm , dragon_weapon_trigger, [fac_kingdom_8,fac_beast]],
["dragon_knight_shield", "Dragon Knight_shield", [("fix_shield22_a_combined",0)], itp_type_shield, itcf_carry_kite_shield,  2091 , weight(4)|difficulty(10)|shield_hit_points(300)|body_armor(125)|spd_rtng(100)|shield_width(50)|shield_height(70),imodbits_shield,  [], [fac_kingdom_8,fac_beast]],


["dragon_plate", "Dragon Knight_plate", [("longqishi_body",0)], merc_body_armor, 0, 20000, weight(30)|abundance(20)|head_armor(13)|body_armor(85)|leg_armor(45)|difficulty(18), imodbits_good_plate, [], [fac_kingdom_8,fac_kingdom_4]],
["dragon_foot", "Dragon Knight Boots", [("longqishitui",0)], itp_merchandise| itp_type_foot_armor| itp_attach_armature,0,
 2664 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(40)|difficulty(9) ,imodbits_good_plate,  [], [fac_kingdom_8,fac_beast]],
["dragon_head", "Dragon Knight Helm", [("longqishitoukui",0)], itp_type_head_armor|itp_merchandise, 0, 
 5400 , weight(2.75)|abundance(100)|head_armor(90)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_good_plate,   [],  [fac_kingdom_8,fac_beast]],
["dragon_knight_hand","Dragon Knight_hand", [("rabbi_hand_L",0)], itp_merchandise|itp_type_hand_armor,0,  820, weight(1)|abundance(30)|body_armor(10)|difficulty(0),imodbits_armor , [], [fac_kingdom_8,fac_kingdom_4]],
["grey_knight_staff", "grey_knight Staff", [("halbert_of_grey_knight",0)], itp_merchandise|itp_type_pistol|itp_crush_through|itp_primary|itp_next_item_as_melee|itp_is_magic_staff ,itcf_reload_pistol|itcf_shoot_pistol|itcf_carry_spear,
 25000 , weight(3.25)|difficulty(0)|spd_rtng(40) | shoot_speed(170) | thrust_damage(80 ,pierce)|max_ammo(1)|accuracy(99),imodbits_magic_staff, magic_cast_trigger , [fac_demon_hunters, fac_hospitalier_knights] ], 
["grey_knight_poleaxe", "grey_knight_poleaxe", [("halbert_of_grey_knight",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_crush_through|itp_extra_penetration, itc_glaive|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_carry_spear|itcf_horseback_slash_polearm, 5000, weight(4)|difficulty(0)|spd_rtng(120)|weapon_length(165)|swing_damage(55,pierce)|thrust_damage(55,pierce), imodbits_polearm|imodbit_masterwork],

["grey_knight_sword", "grey_knight_sword", [("greatsword_of_grey_knight",0)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_crush_through|itp_can_knock_down|itp_can_penetrate_shield, itc_longsword|itcf_carry_sword_back,
 5000 , weight(2.0)|difficulty(18)|spd_rtng(101)| weapon_length(125)|swing_damage(45, pierce)| thrust_damage(32 ,  pierce),imodbits_sword_high, [],[fac_demon_hunters, fac_hospitalier_knights]],

["grey_knight_plate", "Grey Knight_plate", [("hm_arm_masV",0)], merc_body_armor, 0, 20000, weight(30)|abundance(70)|head_armor(13)|body_armor(95)|leg_armor(45)|difficulty(18), imodbits_good_plate, [], [fac_kingdom_7]],
["grey_knight_foot", "Grey Knight Boots", [("hm_boo_masV",0)], itp_merchandise| itp_type_foot_armor| itp_attach_armature,0,
 2664 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(45)|difficulty(9) ,imodbits_good_plate,  [], [fac_demon_hunters, fac_hospitalier_knights]],
["grey_knight_head", "Grey Knight Helm", [("imphelmf",0)], itp_type_head_armor|itp_merchandise, 0, 
 5400 , weight(2.75)|abundance(100)|head_armor(100)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_good_plate,   [], [fac_demon_hunters, fac_hospitalier_knights]],
["grey_knight_hand","Grey Knight_hand", [("hm_glv_masV_L",0)], itp_merchandise|itp_type_hand_armor,0,  820, weight(1)|abundance(100)|body_armor(10)|difficulty(0),imodbits_armor,  [], [fac_kingdom_7]],
["grey_knight_shield", "Grey Knight_shield", [("shield_of_grey_knight",0)], itp_type_shield, itcf_carry_kite_shield,  2091 , weight(4)|difficulty(10)|shield_hit_points(300)|body_armor(125)|spd_rtng(100)|shield_width(50)|shield_height(70),imodbits_shield,  [], [fac_demon_hunters, fac_hospitalier_knights]],

["bane_blade_plate", "Bane Blade_plate", [("hm_arm_masX",0)], merc_body_armor, 0, 20000, weight(30)|abundance(20)|head_armor(13)|body_armor(95)|leg_armor(45)|difficulty(18), imodbits_good_plate, [], [fac_kingdom_7]],
["bane_blade_foot", "Bane Blade Boots", [("hm_boo_masX",0)], itp_merchandise| itp_type_foot_armor| itp_attach_armature,0,
 2664 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(45)|difficulty(9) ,imodbits_good_plate,  [], [fac_kingdom_7]],
["bane_blade_hand","Bane Blade_hand", [("hm_glv_masX_L",0)], itp_merchandise|itp_type_hand_armor,0,  820, weight(1)|abundance(30)|body_armor(10)|difficulty(0),imodbits_armor,  [], [fac_kingdom_7]],
["bane_blade_head", "sallet_beret_plumes_red", [("imphelmf",0)], itp_type_head_armor|itp_merchandise, 0,  4000 , weight(2.5)|abundance(100)|head_armor(80)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_7]],

["sigma_knight_plate", "sigma Knight_plate", [("sigma_zhongjia_1",0)], merc_body_armor, 0, 18000, weight(25)|abundance(20)|head_armor(0)|body_armor(90)|leg_armor(50)|difficulty(18), imodbits_good_plate , [], [fac_kingdom_7]],
["sigma_knight_foot", "sigma Knight Boots", [("sigma_xie1",0)], itp_merchandise| itp_type_foot_armor| itp_attach_armature,0,
 2664 , weight(3.5)|abundance(10)|head_armor(0)|body_armor(0)|leg_armor(40)|difficulty(9) ,imodbits_good_plate,  [], [fac_kingdom_7]],
["sigma_knight_head", "sigma Knight Helm", [("hm_hlf_s02U",0)], itp_type_fullhelm, 0, 
 5400 , weight(2.75)|abundance(10)|head_armor(90)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_good_plate,   [], [fac_kingdom_7]],
["sigma_knight_hand","sigma Knight_hand", [("sigma_zuoshou1_L",0)], itp_merchandise|itp_type_hand_armor,0,  820, weight(1)|abundance(10)|body_armor(10)|difficulty(0),imodbits_armor,  [], [fac_kingdom_7]],

["dawnguard_armor", "Dawnguard_Paladin_Armour", [("dawnguardbody", 0)], merc_body_armor, 0, 10868,full_plate_armor_tier_4, imodbits_plate, [], [fac_kingdom_10]], 
["dawnguard_helmet", "Dawnguard_Paladin_Helm", [("dawnguardHelmet",0)], itp_merchandise| itp_type_head_armor,0, 
 4266 , weight(2.75)|abundance(100)|head_armor(90)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate,  [], [fac_kingdom_10,fac_demon_hunters, fac_hospitalier_knights]], 
["dawnguard_shield", "Dawnguard Paladin_shield", [("fix_dawnguardShield",0)], itp_type_shield, itcf_carry_kite_shield,  2091 , weight(4)|difficulty(4)|shield_hit_points(300)|body_armor(125)|spd_rtng(70)|shield_width(50),imodbits_shield,  [], [fac_kingdom_10,fac_demon_hunters, fac_hospitalier_knights]], 

["dawnguard_sword", "Dawnguard Sword", [("dawnguardSword",0)], itp_merchandise|itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_back, 
3040 , weight(2)|difficulty(8)|spd_rtng(115)| weapon_length(100)|swing_damage(30 , pierce)| thrust_damage(32 ,  pierce),imodbits_sword_high, holy_weapon_trigger, [fac_kingdom_10,fac_demon_hunters, fac_hospitalier_knights]], 
["dawnguard_greatsword", "Dawnguard Great Sword", [("dawnguardgreatsword",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_crush_through, itc_greatsword|itcf_carry_sword_back, 
3540 , weight(3)|difficulty(8)|spd_rtng(115)| weapon_length(140)|swing_damage(40 , pierce)| thrust_damage(35 ,  pierce),imodbits_sword_high, holy_weapon_trigger, [fac_kingdom_10,fac_demon_hunters, fac_hospitalier_knights]], 
["dawnguard_hammer", "Dawnguard Hammer", [("dawnguardhammer",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary, itc_scimitar|itcf_carry_mace_left_hip,2000 , weight(3)|difficulty(0)|spd_rtng(100)| weapon_length(70)|swing_damage(37 , blunt)| thrust_damage(0 ,  pierce),imodbits_mace, holy_weapon_trigger, [fac_kingdom_10,fac_kingdom_7]], 
["dawnguard_javelin","Dawnguard Javelin",[("dawnguardshortspear",0),("jarid_quiver",ixmesh_carry)],itp_type_thrown|itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,3000,abundance(20)|weight(10)|difficulty(3)|shoot_speed(30)|spd_rtng(91)|weapon_length(75)|thrust_damage(53,pierce)|max_ammo(10),imodbits_thrown,
[(ti_on_weapon_attack,[
(store_trigger_param_1,":shooter"),#Get the attacker Agent for add_missile'
(try_for_range, ":unused", 0, 4),
  (copy_position, pos2, pos1),
  (agent_get_look_position,pos3,":shooter"),
  (position_copy_rotation,pos2,pos3),
  #Shotgun script
  #Rifle Version
  (set_fixed_point_multiplier, 100),
  (store_random_in_range, ":z_offset", -300, 301),#Random Rotation of Z
  (position_rotate_x_floating, pos2, 9000), # change axis by rotating 90 degrees
  (position_rotate_y_floating, pos2, ":z_offset"), # rotate z floating
  (position_rotate_x_floating, pos2, -9000), # change axis back
  (store_random_in_range, ":x_offset", -300, 301),#Random Rotation of X
  (position_rotate_x_floating, pos2, ":x_offset"), # Final adjustment of X
        
  (add_missile, ":shooter", pos2, 3000, "itm_dawnguard_javelin", 0, "itm_dawnguard_javelin", 0),
(try_end),
]),]+missile_holy_fire_trigger+missile_holy_fire_trigger_2, [fac_kingdom_10,fac_demon_hunters, fac_hospitalier_knights]], 



#["dragonpriest_helm_0","dragon priest_Helm",[("dragonhelm_0",0)],itp_type_fullhelm,0,3000,weight(4)|head_armor(85)|difficulty(0),imodbits_armor],
["dragonpriest_helm_1","dragon priest_Helm",[("dragonhelm_0",0)],itp_unique|itp_type_fullhelm,0,3000,weight(4)|abundance(15)|head_armor(85)|difficulty(0),imodbits_armor],

["dragonpriest_staff_1", "dragon priest Staff", [("dragonprieststaff",0)], itp_unique|itp_type_pistol|itp_crush_through|itp_primary|itp_is_magic_staff ,itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_spear,
 30000 , weight(3.25)|abundance(15)|difficulty(0)|spd_rtng(45) | shoot_speed(200) | thrust_damage(85 ,pierce)|max_ammo(2)|accuracy(85),imodbits_magic_staff, magic_cast_trigger , [fac_undeads_2] ], 

["dragonpriest_armor", "dragon priest_armor", [("draugr_priest",0)], itp_type_body_armor|itp_covers_legs, 0, 20000, weight(28)|abundance(100)|head_armor(0)|body_armor(100)|leg_armor(60)|difficulty(20), imodbits_good_plate,[], [fac_undeads_2] ],

["nord_knight_plate", "Plate Armor", [("nordcuirass",0)], merc_body_armor, 0, 12769,full_plate_armor_tier_4 ,imodbits_good_plate , [], [fac_kingdom_8,fac_kingdom_10]],
["nord_plate_boots", "Plate Boots", [("nordbootsm",0)], itp_merchandise| itp_type_foot_armor| itp_attach_armature,0,  2664 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(37)|difficulty(9) ,imodbits_armor ,  [], [fac_kingdom_8,fac_kingdom_10]],


["black_knight_sword", "Black_knight_sword", [("ebonyPersonGreatsword",0)], itp_merchandise|itp_type_one_handed_wpn|itp_unique|itp_primary|itp_crush_through|itp_extra_penetration|itp_can_penetrate_shield, itc_longsword|itcf_carry_sword_back,
 2700 , weight(2.0)|abundance(10)|difficulty(12)|spd_rtng(101)| weapon_length(150)|swing_damage(50, pierce)| thrust_damage(30 ,  pierce),imodbits_sword_high, [],[fac_undeads_2,fac_kingdom_3]],
 
  
["black_knight_shield", "Black Knight_shield", [("Black_d",0)], itp_type_shield, itcf_carry_kite_shield,  2091 , weight(4)|abundance(10)|difficulty(10)|shield_hit_points(300)|body_armor(125)|spd_rtng(100)|shield_width(50)|shield_height(50),imodbits_shield,  [], [fac_undeads_2,fac_kingdom_3]],

["black_knight_plate", "Black Knight_plate", [("Black_Knight",0)], merc_body_armor, 0, 20000, weight(30)|abundance(20)|head_armor(13)|body_armor(95)|leg_armor(45)|difficulty(18), imodbits_good_plate, [], [fac_undeads_2,fac_kingdom_3]],
["black_knight_foot", "Black Knight Boots", [("Black_Knightt",0)], itp_merchandise| itp_type_foot_armor| itp_attach_armature,0,
 2664 , weight(3.5)|abundance(10)|head_armor(0)|body_armor(0)|leg_armor(45)|difficulty(9) ,imodbits_good_plate,  [], [fac_undeads_2,fac_kingdom_3]],
["black_knight_head", "Black Knight Helm", [("Black_Knighth",0)], itp_type_fullhelm, 0, 
 5400 , weight(2.75)|abundance(10)|head_armor(100)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_good_plate,   [], [fac_undeads_2,fac_kingdom_3]],
["black_knight_hand","Black Knight_hand", [("Black_Knight-L",0)], itp_merchandise|itp_type_hand_armor,0,  820, weight(1)|abundance(10)|body_armor(10)|difficulty(0),imodbits_armor,  [], [fac_kingdom_3]],

["nazgul_robes", "nazgul_robes", [("nazgul_tvs",0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 20000, weight(5)|abundance(20)|head_armor(13)|body_armor(100)|leg_armor(60)|difficulty(18), imodbits_armor, [], [fac_kingdom_3]],
["nazgul_hood_1", "nazgul_hood", [("nazgul_hood_tvs",0)], itp_type_fullhelm|itp_attach_armature, 0, 
 10000 , weight(2)|abundance(10)|head_armor(90)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_armor,   [], [fac_kingdom_3]],
["nazgul_hood_2", "nazgul_hood", [("witchking_outfit.1",0)], itp_type_fullhelm|itp_attach_armature, 0, 
 10000 , weight(2)|abundance(10)|head_armor(100)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_armor,   [], [fac_kingdom_3]],

["valkyrie_armor_1","Valkyrie Light Plate",[("aribeth_armor",0)],itp_type_body_armor|itp_covers_legs,0,5256,mail_armor_tier_4,imodbits_plate, [], [fac_commoners,fac_kingdom_10]],
["valkyrie_armor_2","Valkyrie Light Plate",[("aribeth_armor_dark",0)],itp_type_body_armor|itp_covers_legs,0,7310,full_plate_armor_tier_1,imodbits_plate, [], [fac_kingdom_10]],
["valkyrie_armor_3","Valkyrie Armor",[("aribeth_armor_dark_chainmail",0)],itp_type_body_armor|itp_covers_legs,0,9216,full_plate_armor_tier_2,imodbits_plate, [], [fac_kingdom_10]],

["valkyrie_helm_1","Valkyrie_helm_iron",[("Valkyrie_helm_iron",0)],itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair,0, 3266 , weight(1)|abundance(25)|head_armor(50)|body_armor(10)|leg_armor(10),imodbits_plate, [], [fac_commoners,fac_kingdom_10]],
["valkyrie_helm_2","Valkyrie_helm_Silver",[("Valkyrie_helm_Silver",0)],itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair,0,4266 , weight(1)|abundance(25)|head_armor(70)|body_armor(10)|leg_armor(10),imodbits_plate, [], [fac_kingdom_10]],
["valkyrie_helm_3","Valkyrie_helm_gold",[("Valkyrie_helm_gold",0)],itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair,0,5400 , weight(1)|abundance(25)|head_armor(90)|body_armor(10)|leg_armor(10),imodbits_plate, [], [fac_kingdom_10]],

["drow_plate", "dark elf_plate", [("plate_falcon_armor_black",0)], merc_body_armor, 0, 20000, weight(30)|abundance(20)|head_armor(15)|body_armor(85)|leg_armor(45)|difficulty(18), imodbits_good_plate, [], [fac_kingdom_8,fac_beast]],
["drow_plate_foot", "dark elf Boots", [("plate_falcon_boots_black",0)], itp_merchandise| itp_type_foot_armor| itp_attach_armature,0,
 2664 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(40)|difficulty(9) ,imodbits_good_plate,  [], [fac_kingdom_8,fac_beast]],
["drow_plate_hand","dark elf_hand", [("plate_falcon_black_gloves_L",0)], itp_merchandise|itp_type_hand_armor,0,  820, weight(1)|abundance(30)|body_armor(10)|difficulty(0),imodbits_armor,  [], [fac_kingdom_8,fac_beast]],

["elf_plate", "elf_plate", [("plate_falcon_armor_silver",0)], merc_body_armor, 0, 18000, weight(30)|abundance(20)|head_armor(15)|body_armor(80)|leg_armor(45)|difficulty(18), imodbits_good_plate, [], [fac_elf]],
["elf_foot", "elf Boots", [("plate_falcon_boots_silver",0)], itp_merchandise| itp_type_foot_armor| itp_attach_armature,0,
 2664 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(40)|difficulty(9) ,imodbits_good_plate, [], [fac_elf]],
["elf_hand","elf_hand", [("plate_falcon_silver_gloves_L",0)], itp_merchandise|itp_type_hand_armor,0,  820, weight(1)|abundance(30)|body_armor(10)|difficulty(0),imodbits_armor, [], [fac_elf]],


["gold_elf_plate", "gold elf_plate", [("plate_falcon_armor_gold",0)], merc_body_armor, 0, 20000, weight(30)|abundance(20)|head_armor(15)|body_armor(85)|leg_armor(45)|difficulty(18), imodbits_good_plate, [], [fac_elf]],
["gold_elf_foot", "gold elf Boots", [("plate_falcon_boots_gold",0)], itp_merchandise| itp_type_foot_armor| itp_attach_armature,0,
 2664 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(45)|difficulty(9) ,imodbits_good_plate,  [], [fac_elf]],
["gold_elf_hand","gold elf_hand", [("plate_falcon_gold_gloves_L",0)], itp_merchandise|itp_type_hand_armor,0,  820, weight(1)|abundance(30)|body_armor(10)|difficulty(0),imodbits_armor, [], [fac_elf]],

#highlander pack

 ["highlander_armor4",  "highlander merchant costume", [("a_h4",0)], merc_body_armor ,0, 940,cloth_tier_3,imodbits_cloth , [], [fac_kingdom_10]],
 ["highlander_armor4_1",  "highlander merchant costume2", [("a_h4_1",0)], merc_body_armor ,0, 940,cloth_tier_3,imodbits_cloth , [], [fac_kingdom_10, fac_dwarf, fac_scotland]],

 ["highlander_armor1",  "highlander costume", [("a_h1",0)], merc_body_armor ,0, 1722,cloth_tier_4,imodbits_cloth , [], [fac_kingdom_10]],
 ["highlander_armor1_1",  "highlander costume2", [("a_h1_1",0)], merc_body_armor ,0, 1722,cloth_tier_4,imodbits_cloth  , [], [fac_kingdom_10, fac_dwarf, fac_scotland]],
 ["highlander_armor2",  "highlander armor", [("a_h2",0)], merc_body_armor ,0, 6360,lamellar_armor_tier_2,imodbits_armor  , [], [fac_kingdom_10]],
 ["highlander_armor2_1",  "highlander armor2", [("a_h2_1",0)], merc_body_armor ,0, 6360,lamellar_armor_tier_2,imodbits_armor  , [], [fac_kingdom_10]],
 ["highlander_armor3",  "elite highlander armor", [("a_h3",0)], merc_body_armor|itp_civilian ,0, 9216,lamellar_armor_tier_4,imodbits_armor , [], [fac_kingdom_10]],
 ["highlander_armor3_1",  "elite highlander armor2", [("a_h3_1",0)], merc_body_armor|itp_civilian ,0, 9216,lamellar_armor_tier_4,imodbits_armor , [], [fac_kingdom_10]],

 ["highlander_hat1", "Highlander beret", [("h_h1",0)], itp_type_head_armor| itp_attach_armature|itp_fit_to_head   ,0, 500 , weight(1)|abundance(100)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_10, fac_dwarf, fac_scotland]],
 ["highlander_hat1_1", "Highlander beret2", [("h_h1_1",0)], itp_type_head_armor | itp_attach_armature|itp_fit_to_head   ,0, 500 , weight(1)|abundance(100)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_10, fac_dwarf, fac_scotland]],
 ["highlander_hat2", "Highlander beret3", [("h_h2",0)], itp_type_head_armor | itp_attach_armature|itp_fit_to_head   ,0, 800 , weight(2)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0) ,imodbits_cloth , [], [fac_kingdom_10, fac_dwarf, fac_scotland]],
 ["highlander_hat2_1", "Highlander beret4", [("h_h2_1",0)], itp_type_head_armor | itp_attach_armature|itp_fit_to_head   ,0, 800 , weight(2)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0) ,imodbits_cloth , [], [fac_kingdom_10, fac_dwarf, fac_scotland]],
 
 ["highlander_boot1", "highlander boots", [("b_h1",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 750 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_10, fac_dwarf, fac_scotland]],
  ["highlander_boot1_1", "highlander boots2", [("b_h1_1",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 750 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_10, fac_dwarf, fac_scotland]],
 ["highlander_boot2", "highlander boots3", [("b_h2",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 2016 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_10, fac_dwarf, fac_scotland]],
  ["highlander_boot2_1", "highlander boots4", [("b_h2_1",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 2016 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_10, fac_dwarf, fac_scotland]],



 ["highlander_shield1", "Improved Highlander shield1", [("s_h1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield ,  450 , weight(3.5)|hit_points(100)|body_armor(60)|spd_rtng(100)|shield_width(50),imodbits_shield , [], [fac_kingdom_10]],
 ["highlander_shield2", "Improved Highlander shield2", [("s_h1_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield ,  900 , weight(3.5)|hit_points(150)|body_armor(70)|spd_rtng(100)|shield_width(50),imodbits_shield , [], [fac_kingdom_10]],
 ["highlander_shield3", "Improved Highlander shield3", [("s_h1_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield ,  1350 , weight(3.5)|hit_points(200)|body_armor(80)|spd_rtng(100)|shield_width(50),imodbits_shield  , [], [fac_kingdom_10]],
#higlanderpack end

["ogre_shield", "Ogre Shield", [("orc_shield",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(4.5)|shield_hit_points(400)|body_armor(50)|spd_rtng(78)|shield_width(70)|shield_height(70),imodbits_shield ],

["heavyogresword",         "Heavy Ogre Sword", [("heavyogresword",0)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_dagger_front_left,
 	500 , weight(20)|abundance(1)|difficulty(20)|spd_rtng(100) | weapon_length(150)|swing_damage(40 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_high ],

["ogre_axe", "Ogre Axe", [("orc_battleaxe",0)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 142 , weight(10)|abundance(1)|difficulty(15)|spd_rtng(90) | weapon_length(125)|swing_damage(45 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],
["ogre_axe_2", "Ogre Axe", [("orc_dualbattleaxe",0)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 142 , weight(10)|abundance(1)|difficulty(15)|spd_rtng(90) | weapon_length(125)|swing_damage(55 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],
["ogre_axe_3", "Glaive", [("orc_halberd",0)], itp_type_two_handed_wpn|itp_primary|itp_two_handed|itp_bonus_against_shield|itp_wooden_parry|itp_is_glaive, itc_poleaxe|itcf_carry_spear, 1408, weight(4.5)|difficulty(15)|spd_rtng(79)|weapon_length(160)|swing_damage(45,pierce)|thrust_damage(30,pierce), imodbits_polearm|imodbit_masterwork],
["ogre_axe_4", "Ogre Axe", [("orc_halberd1",0)], itp_type_two_handed_wpn|itp_primary|itp_two_handed|itp_bonus_against_shield|itp_wooden_parry|itp_is_glaive, itc_poleaxe|itcf_carry_spear, 142 , weight(10)|abundance(1)|difficulty(15)|spd_rtng(90) | weapon_length(170)|swing_damage(55 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],

["orc_handaxe", "Org's Axe", [("orc_handaxe",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 250 , weight(2.3)|difficulty(3)|spd_rtng(90) | weapon_length(80)|swing_damage(40,pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],
["orc_greatsword","Ogre Sword", [("orc_greatsword",0)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_dagger_front_left,
 500 , weight(20)|abundance(1)|difficulty(20)|spd_rtng(95) | weapon_length(125)|swing_damage(45 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_high ],


 
["ogre_boots_01", "Ogre Boots", [("ogre_calf",0)], itp_type_foot_armor |itp_civilian |itp_unique,0,
 19 , weight(10.25)|abundance(10)|head_armor(0)|body_armor(0)|leg_armor(50)|difficulty(0) ,imodbits_cloth ],
["ogre_boots_02", "Ogre Boots", [("barbar_boots",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature|itp_unique,0,
 19 , weight(10.25)|abundance(10)|head_armor(0)|body_armor(0)|leg_armor(60)|difficulty(0) ,imodbits_cloth ],

["ogre_armor1", "Orc Fur", [("orc_fur",0)], itp_unique|itp_type_body_armor|itp_force_show_body |itp_civilian ,0,
 100 , weight(1)|abundance(100)|head_armor(0)|body_armor(60)|leg_armor(10)|difficulty(6),imodbits_cloth],
["ogre_armor2", "Orc Fur With Shoulderpad", [("barbar_body",0)], itp_unique|itp_type_body_armor|itp_covers_legs |itp_civilian ,0,
 200 , weight(2)|abundance(100)|head_armor(0)|body_armor(70)|leg_armor(10)|difficulty(6),imodbits_cloth],
["ogre_armor3", "Orc Shoulderpads", [("orc_shoulderpads",0)], itp_unique|itp_type_body_armor|itp_force_show_body |itp_civilian ,0,
 300 , weight(2)|abundance(100)|head_armor(0)|body_armor(80)|leg_armor(10)|difficulty(6),imodbits_cloth],
["ogre_armor", "Orc Fur With Shoulderpads", [("orc_fur_with_shoulderpads",0)], itp_unique|itp_type_body_armor|itp_covers_legs |itp_civilian ,0,
 400 , weight(3)|abundance(100)|head_armor(0)|body_armor(90)|leg_armor(10)|difficulty(6),imodbits_cloth],

["ogre_bear_helmet", "bear_helme", [("ogre_Bear_helmet", 0)], itp_type_head_armor|itp_civilian|itp_unique, 0, 4000, weight(10)|abundance(100)|head_armor(50)|body_armor(20)|leg_armor(0), imodbits_cloth ],

["ogre_nemean_helm", "nemean_helm", [("ogre_head_combined", 0)], itp_type_fullhelm|itp_unique, 0, 4000, weight(10)|abundance(100)|head_armor(50)|body_armor(20)|leg_armor(0), imodbits_cloth ],
["ogre_barbar_helm", "bear_helme", [("barbar_helm", 0)], itp_type_head_armor|itp_civilian|itp_unique, 0, 4000, weight(10)|abundance(100)|head_armor(80)|body_armor(20)|leg_armor(0), imodbits_cloth ],


#dd Org Armours

["org_armour_5", "Org captain Armour", [("org_armour_5",0)], itp_unique|itp_type_body_armor  |itp_covers_legs ,0, 9216,full_plate_armor_tier_2 ,imodbits_plate ],
["org_armour_4", "Org mail Armour", [("org_armour_4",0)], itp_unique|itp_type_body_armor  |itp_covers_legs ,0, 6683,mail_armor_tier_5 ,imodbits_plate ],
["org_armour_3", "Org mail Armour", [("org_armour_3",0)], itp_unique|itp_type_body_armor  |itp_covers_legs ,0, 4035,mail_armor_tier_3 ,imodbits_plate ],
["org_armour_1", "Org Armour", [("org_armour_1",0)], itp_unique|itp_type_body_armor  |itp_covers_legs ,0, 1722,cloth_tier_4 ,imodbits_plate ],

["org_helmet_3", "Org captain Helmet", [("org_helmet_5",0)], itp_unique|itp_type_head_armor,0, 
  3266 , weight(3)|abundance(100)|head_armor(70)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["org_helmet_2", "Org Elite Helmet", [("org_helmet_3",0)], itp_unique|itp_type_head_armor ,0, 
  2400 , weight(2)|abundance(100)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["org_helmet_1", "Org Guard Helmet", [("org_helmet_2",0)], itp_unique|itp_type_head_armor ,0, 
  1666 , weight(2)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],

["org_boot_1", "Org Leather Boots", [("org_boots_2",0)], itp_unique|itp_type_foot_armor|itp_civilian|itp_attach_armature,0,
 1250 , weight(2.0)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(7) ,imodbits_armor ],
["org_boot_2", "Org Leather with Iron Boots", [("org_boots_3",0)], itp_unique|itp_type_foot_armor|itp_attach_armature,0,
 2520 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(35)|difficulty(7) ,imodbits_armor ],


["org_crossbow_1", "Org Crossbow", [("org-crossbow",0)], itp_type_crossbow |itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 400 , weight(4.5)|difficulty(3)|spd_rtng(50) | shoot_speed(75) | thrust_damage(35,pierce)|max_ammo(2),imodbits_crossbow ],
["org_crossbow_2", "Org Crossbow", [("org-crossbow",0)], itp_type_crossbow |itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 500 , weight(4.5)|difficulty(3)|spd_rtng(45) | shoot_speed(80) | thrust_damage(40,pierce)|max_ammo(3),imodbits_crossbow ],

["org_sword1", "Org's Sword", [("orgsword1",0)], itp_type_one_handed_wpn|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 105 , weight(2.5)|difficulty(6)|spd_rtng(106) | weapon_length(82)|swing_damage(25 , cut) | thrust_damage(0 ,  pierce),imodbits_sword ],
["org_sword2", "Org's Sword", [("orgsword2",0)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 400 , weight(1.0)|difficulty(0)|spd_rtng(104) |weapon_length(82)|swing_damage(31 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ],
["org_axe3", "Org's Axe", [("orgaxe6",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 190 , weight(2.0)|difficulty(3)|spd_rtng(80) | weapon_length(61)|swing_damage(30 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],
["org_axe4", "Org's Axe", [("orgaxe5",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 250 , weight(2.3)|difficulty(3)|spd_rtng(90) | weapon_length(70)|swing_damage(35,pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],
["org_twohanderaxe",  "Org's Two-handed Axe", [("orgaxe7",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 240 , weight(5)|difficulty(8)|spd_rtng(78) | weapon_length(110)|swing_damage(46 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],

["org_shield_1",         "Org's Shield", [("fix_org_shield_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  100 , weight(2.0)|hit_points(50)|body_armor(30)|spd_rtng(90)|shield_width(30)|shield_height(40),imodbits_shield ],
["org_shield_2",         "Org's Shield", [("fix_org_shield_2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  102 , weight(2.5)|hit_points(120)|body_armor(50)|spd_rtng(90)|shield_width(50)|shield_height(100),imodbits_shield ],
["org_shield_3",         "Org's Shield", [("org_shield_3",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(4.5)|hit_points(1000)|body_armor(50)|spd_rtng(100)|shield_width(40)|shield_height(40),imodbits_shield ],



["org_lance", "Org's Lance", [("Org-Spear3",0)], itp_couchable|itp_type_polearm| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_greatlance, 158 , weight(5)|difficulty(0)|spd_rtng(61) | weapon_length(205)|swing_damage(30 , cut) | thrust_damage(30 ,  pierce),imodbits_polearm ],


["org_spear_2", "Org's Spear", [("Org-Spear1",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff|itcf_carry_spear, 261 , weight(4.0)|difficulty(0)|spd_rtng(95) | weapon_length(131)|swing_damage(33 , cut) | thrust_damage(27 ,  pierce),imodbits_polearm ],
["org_spear_3", "Org's Spear", [("Org-Spear2",0)],itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff|itcf_carry_spear, 384 , weight(4.5)|difficulty(0)|spd_rtng(77) | weapon_length(170)|swing_damage(50 , cut) | thrust_damage(30 ,  pierce),imodbits_polearm ],

["org_throwing_spears_1",         "Org's Throwing Spears", [("Org-Spear1",0)], itp_type_thrown|itp_crush_through|itp_primary ,itcf_throw_javelin|itcf_carry_spear,560 , weight(4)|difficulty(2)|spd_rtng(89)| shoot_speed(24)| thrust_damage(48 ,  cut)|max_ammo(4)|weapon_length(80),imodbits_thrown,missile_distance_trigger, throw_factions],
["org_throwing_spears_2",         "Org's Throwing Spears", [("Org-Spear2",0)], itp_type_thrown|itp_crush_through|itp_primary ,itcf_throw_javelin|itcf_carry_spear,525 , weight(4)|difficulty(2)|spd_rtng(87)| shoot_speed(22)| thrust_damage(67 ,  cut)|max_ammo(4)|weapon_length(120),imodbits_thrown,missile_distance_trigger, throw_factions],


["orc_armour", "Orc_Shirt", [("orc_archer", 0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 940,cloth_tier_3, imodbits_cloth], 
["orc_armour2", "Orc_Armoured_Shirt", [("orc_archer2", 0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 1722,cloth_tier_4, imodbits_cloth], 
["orc_armour3", "Orc_Mail_Shirt", [("orc_archer3", 0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 2704,mail_armor_tier_2, imodbits_plate], 

["orc_medarmor", "Orc_Mail_Shirt", [("orc_boy1", 0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 2704,mail_armor_tier_2, imodbits_plate], 
["orc_medarmor2", "Orc_Mail_Shirt", [("orc_boy2", 0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 2704,mail_armor_tier_2, imodbits_plate], 
["orc_armorheav", "Orc_Armour", [("orc_boy_v1", 0)], itp_unique|itp_type_body_armor|itp_covers_legs, 536870912, 4035,mail_armor_tier_3, imodbits_plate], 
["orc_armorheav2", "Orc_Armour", [("orc_boy_v2", 0)], itp_unique|itp_type_body_armor|itp_covers_legs, 536870912, 4035,mail_armor_tier_3, imodbits_plate], 


["orc_bigun_armour", "Orc_Heavy_Armour", [("bigun_armour", 0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 5256,mail_armor_tier_4, imodbits_plate], 
["orc_bigun_armour2", "Orc_Heavy_Armour", [("bigun_armour2", 0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 5256,mail_armor_tier_4, imodbits_plate], 

["orc_boar_armour", "Orc_Boar_Armour", [("orc_boarboy", 0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 3451,lamellar_armor_tier_1, imodbits_plate], 
["orc_boar_armour_vet", "Orc_Heavy_Boar_Armour", [("orc_boarboy_v", 0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 6360,lamellar_armor_tier_2, imodbits_plate], 

["blackorc", "Black_Orc_Armour", [("black_armour", 0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 7310,full_plate_armor_tier_1, imodbits_plate], 
["blackorc_vet", "Black_Orc_Heavy_Armour", [("black_armour2", 0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 9216,full_plate_armor_tier_2, imodbits_plate], 
["blackorcboss_armour", "Black_Orc_Boss_Armour", [("blackboss_armour", 0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 10868,full_plate_armor_tier_3, imodbits_plate], 

["orcboss_armour", "Orc_Boss_Armour", [("bossorc2", 0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 10868,full_plate_armor_tier_3, imodbits_plate], 
["orcboss_armour2", "Orc_Boss_Armour", [("bossorc", 0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 10868,full_plate_armor_tier_3, imodbits_plate], 
["orcbigboss_armour", "Orc_BigBoss_Armour", [("bigbossorc", 0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 12769,full_plate_armor_tier_4, imodbits_plate], 

["orc_pot", "Orc_Pot_Helmet", [("orc_archerpot", 0)], itp_unique|itp_type_head_armor, 0, 300, weight(1.25)|abundance(100)|difficulty(0)|head_armor(33)|body_armor(0)|leg_armor(0), imodbits_plate], 
["orc_archerhelmet", "Orc_Light_Helmet", [("orc_archerhelmetspike", 0)], itp_unique|itp_type_head_armor, 0, 440, weight(1.00)|abundance(100)|difficulty(0)|head_armor(42)|body_armor(0)|leg_armor(0), imodbits_plate], 
["orc_archerhelmet2", "Orc_Light_Helmet", [("orc_archerhelmet", 0)], itp_unique|itp_type_head_armor, 0, 640, weight(1.00)|abundance(100)|difficulty(0)|head_armor(51)|body_armor(0)|leg_armor(0), imodbits_plate], 

["orcboy_helmet", "Orc_Helmet", [("orcboy_helmet", 0)], itp_unique|itp_type_head_armor, 0, 700, weight(2.00)|abundance(120)|difficulty(6)|head_armor(55)|body_armor(0)|leg_armor(0), imodbits_plate], 
["orcboy_helmet2", "Orc_Helmet", [("orcboy_helmet2", 0)], itp_unique|itp_type_head_armor, 0, 700, weight(2.00)|abundance(120)|difficulty(6)|head_armor(55)|body_armor(0)|leg_armor(0), imodbits_plate], 
["orcboy_helmet3", "Orc_Helmet", [("orcguard_hetmet", 0)], itp_unique|itp_type_head_armor, 0, 700, weight(2.00)|abundance(120)|difficulty(6)|head_armor(55)|body_armor(0)|leg_armor(0), imodbits_plate], 

["orcvet_helmet", "Orc_Helmet", [("orcboy_helmetv", 0)], itp_unique|itp_type_head_armor, 0, 860, weight(2.50)|abundance(120)|difficulty(6)|head_armor(60)|body_armor(0)|leg_armor(0), imodbits_plate], 
["orcvet_helmet2", "Orc_Helmet", [("orcboy_helmetv2", 0)], itp_unique|itp_type_head_armor, 0, 860, weight(2.50)|abundance(120)|difficulty(6)|head_armor(60)|body_armor(0)|leg_armor(0), imodbits_plate], 

["orcboar_helmet", "Orc_Boar_Helmet", [("orcboar_helmet", 0)], itp_unique|itp_type_head_armor, 0, 1460, weight(2.50)|abundance(120)|difficulty(7)|head_armor(67)|body_armor(0)|leg_armor(0), imodbits_plate], 
["orcboar_helmv", "Orc_Boar_Helm", [("orcboar_helmv", 0)], itp_unique|itp_type_head_armor, 0, 2300, weight(2.75)|abundance(100)|difficulty(10)|head_armor(75)|body_armor(0)|leg_armor(0), imodbits_plate], 

["orc_bigun_helm", "Bigun_Helm", [("orchelm", 0)], itp_unique|itp_type_head_armor, 0, 2100, weight(2.75)|abundance(100)|difficulty(9)|head_armor(72)|body_armor(0)|leg_armor(0), imodbits_plate], 
["orc_bigun_helm2", "Bigun_Helm", [("orchelm2", 0)], itp_unique|itp_type_head_armor, 0, 2100, weight(2.75)|abundance(100)|difficulty(9)|head_armor(72)|body_armor(0)|leg_armor(0), imodbits_plate], 

["blackorc_helm", "Black_Orc_Helm", [("orcfullhelm", 0)], itp_type_head_armor, 0, 2700, weight(2.75)|abundance(100)|difficulty(11)|head_armor(79)|body_armor(0)|leg_armor(0), imodbits_plate], 
["blackorc_helm_vet", "Black_Orc_Heavy_Helm", [("orcfullhelmv", 0)], itp_type_head_armor, 0, 3100, weight(2.75)|abundance(100)|difficulty(11)|head_armor(82)|body_armor(0)|leg_armor(0), imodbits_plate], 

["blackorcboss_helm", "Black_Orc_Boss_Helm", [("orcbosshelm5", 0)], itp_unique|itp_type_head_armor, 0, 4000, weight(3.00)|abundance(80)|difficulty(12)|head_armor(87)|body_armor(0)|leg_armor(0), imodbits_plate], 
["orcboss_helm1", "Orc_Boss_Lite_Helmet", [("orcbosshelm1", 0)], itp_unique|itp_type_head_armor, 0, 2700, weight(2.75)|abundance(100)|difficulty(11)|head_armor(79)|body_armor(0)|leg_armor(0), imodbits_plate], 
["orcboss_helm2", "Orc_Boss_Helmet", [("orcbosshelm2", 0)], itp_unique|itp_type_head_armor, 0, 3300, weight(2.75)|abundance(100)|difficulty(12)|head_armor(80)|body_armor(0)|leg_armor(0), imodbits_plate], 
["orcboss_helm3", "Orc_Boss_Helm", [("orcbosshelm3", 0)], itp_unique|itp_type_head_armor, 0, 4000, weight(3.00)|abundance(80)|difficulty(12)|head_armor(87)|body_armor(0)|leg_armor(0), imodbits_plate], 
["orcbigboss_helm", "Orc_Big_Boss_Helm", [("orcbosshelm4", 0)], itp_unique|itp_type_head_armor, 0, 6000, weight(3.00)|abundance(80)|difficulty(14)|head_armor(90)|body_armor(0)|leg_armor(0), imodbits_plate], 



["orc_boots", "Orc_Boots", [("orcboot1", 0)], itp_unique|itp_type_foot_armor|itp_civilian| itp_attach_armature, 0, 90, weight(1.00)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(15), imodbits_cloth, [], [fac_orc]], 
["orc_boots2", "Orc_Capped_Boots", [("orcboot2", 0)], itp_unique|itp_type_foot_armor|itp_civilian| itp_attach_armature, 0, 174, weight(1.25)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(20), imodbits_cloth, [], [fac_orc]], 
["orc_boots3", "Orc_Reinforced_Boots", [("orcboot3", 0)], itp_unique|itp_type_foot_armor|itp_civilian| itp_attach_armature, 0, 274, weight(1.25)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(25), imodbits_cloth, [], [fac_orc]], 
["orc_boots4", "Orc_Armoured_Boots", [("orcboot4", 0)], itp_unique|itp_type_foot_armor|itp_civilian| itp_attach_armature, 0, 530, weight(3.00)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(30), imodbits_armor, [], [fac_orc]], 
["orc_heavy_boots", "Orc_Heavy_Boots", [("orcboot5", 0)], itp_unique|itp_type_foot_armor|itp_civilian| itp_attach_armature, 0, 1250, weight(3.00)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(35), imodbits_armor, [], [fac_orc]], 


["orcaxe1", "Orc_Axe", [("GS_Axe_1H_TE_02", 0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield, itc_scimitar|itcf_carry_mace_left_hip, 150, weight(1.00)|abundance(100)|difficulty(0)|weapon_length(80)|spd_rtng(94)|swing_damage(30, cut)|thrust_damage(0, pierce), imodbits_axe, [], [fac_orc]], 
["orcaxe2", "Orc_Axe", [("GS_Axe_1H_T1_03", 0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield, itc_scimitar|itcf_carry_mace_left_hip, 295, weight(1.00)|abundance(100)|difficulty(0)|weapon_length(84)|spd_rtng(96)|swing_damage(38, cut)|thrust_damage(0, pierce), imodbits_axe, [], [fac_orc]], 
["orcaxe3", "Orc_Axe", [("GS_Axe_1H_T2_04", 0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield, itc_scimitar|itcf_carry_mace_left_hip, 225, weight(2.00)|abundance(100)|difficulty(10)|weapon_length(90)|spd_rtng(95)|swing_damage(34, pierce)|thrust_damage(0, pierce), imodbits_axe, [], [fac_orc]], 


["orcaxe4", "Mighty_Cleava", [("GS_Axe_2H_TE_02",0)], itp_type_two_handed_wpn|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_merchandise|itp_crush_through|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 821, weight(6.5)|difficulty(18)|spd_rtng(85)|weapon_length(145)|swing_damage(52,pierce)|thrust_damage(0,pierce), imodbits_axe, [], [fac_orc]], 
["orcaxe5", "Orc_Axe", [("GS_Axe_2H_T2_03",0)], itp_type_two_handed_wpn|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_merchandise|itp_crush_through|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 414, weight(6.5)|difficulty(18)|spd_rtng(89)|weapon_length(120)|swing_damage(45,pierce)|thrust_damage(0,pierce), imodbits_axe, [], [fac_orc]], 


["orc_spear", "Orc_Stabba", [("GS_Spear_TE_02",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_wooden_parry, itc_glaive|itcf_carry_spear, 261 , weight(2.0)|difficulty(0)|spd_rtng(90) | weapon_length(190)|swing_damage(33 , cut) | thrust_damage(27 ,  pierce),imodbits_polearm, [], [fac_orc]], 
["orc_spear2", "Orc_Stabba", [("GS_Spear_TE_01",0)],itp_type_polearm|itp_offset_lance| itp_primary|itp_wooden_parry, itc_glaive|itcf_carry_spear, 384 , weight(2.5)|difficulty(0)|spd_rtng(89) | weapon_length(198)|swing_damage(29 , cut) | thrust_damage(30 ,  pierce),imodbits_polearm, [], [fac_orc]], 
["orc_spear3", "Orc_Stabba", [("GS_Spear_2H_T3_01",0)],itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_wooden_parry, itc_glaive|itcf_carry_spear, 384 , weight(2.5)|difficulty(0)|spd_rtng(89) | weapon_length(208)|swing_damage(25 , cut) | thrust_damage(30 ,  pierce),imodbits_polearm, [], [fac_orc]], 

["orc_shield", "Black_Orc_Blocka", [("GS_Shield_T4_02",0)], itp_type_shield|itp_wooden_parry|itp_cant_use_on_horseback, itcf_carry_board_shield,  955 , weight(2.0)|hit_points(820)|body_armor(23)|spd_rtng(80)|shield_width(50)|shield_height(100),imodbits_shield, [], [fac_orc]], 
["orc_shield2", "Black_Orc_Blocka", [("GS_Shield_T4_01",0)], itp_type_shield|itp_wooden_parry|itp_cant_use_on_horseback, itcf_carry_board_shield,  885 , weight(2.5)|hit_points(770)|body_armor(21)|spd_rtng(80)|shield_width(60)|shield_height(100),imodbits_shield, [], [fac_orc]], 
["orc_shield3", "Orc_Blocka", [("GS_Shield_T3_02",0)], itp_type_shield|itp_wooden_parry|itp_cant_use_on_horseback, itcf_carry_board_shield,  381 , weight(4.5)|hit_points(350)|body_armor(16)|spd_rtng(85)|shield_width(50)|shield_height(100),imodbits_shield, [], [fac_orc]], 
["orc_shield4", "Orc_Blocka", [("GS_Shield_T3_01",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  95 , weight(4.5)|hit_points(300)|body_armor(10)|spd_rtng(100)|shield_width(50),imodbits_shield, [], [fac_orc]], 
["orc_shield5", "Orc_Blocka", [("GS_Shield_T2_01",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  425 , weight(4.5)|hit_points(315)|body_armor(19)|spd_rtng(100)|shield_width(60),imodbits_shield, [], [fac_orc]], 

["choppa1", "Orc_Choppa", [("orc_choppa4", 0)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield, itc_scimitar|itcf_carry_mace_left_hip, 220, weight(1.50)|abundance(100)|difficulty(7)|weapon_length(72)|spd_rtng(99)|swing_damage(28, cut)|thrust_damage(0, pierce), imodbits_axe, [], [fac_orc]], 
["choppa2", "Orc_Choppa", [("GS_Choppa_1H_T3_01", 0)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield, itc_scimitar|itcf_carry_mace_left_hip, 180, weight(1.50)|abundance(100)|difficulty(8)|weapon_length(73)|spd_rtng(99)|swing_damage(30, cut)|thrust_damage(0, pierce), imodbits_axe, [], [fac_orc]], 
["choppa3", "Orc_Heavy_Choppa", [("GS_Choppa_1H_T3_02", 0)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield, itc_scimitar|itcf_carry_mace_left_hip, 230, weight(2.00)|abundance(100)|difficulty(8)|weapon_length(70)|spd_rtng(99)|swing_damage(32, cut)|thrust_damage(0, pierce), imodbits_axe, [], [fac_orc]], 

["choppa4", "Black_Orc_Choppa", [("orc_choppa6", 0)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield, itc_scimitar|itcf_carry_mace_left_hip, 420, weight(2.00)|abundance(100)|difficulty(9)|weapon_length(104)|spd_rtng(96)|swing_damage(32, pierce)|thrust_damage(0, pierce), imodbits_axe, [], [fac_orc]], 
["choppa5", "Black_Orc_Choppa", [("GS_Choppa_1H_TE_03", 0)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield, itc_scimitar|itcf_carry_mace_left_hip, 2500, weight(2.00)|abundance(100)|difficulty(10)|weapon_length(102)|spd_rtng(97)|swing_damage(36, pierce)|thrust_damage(0, pierce), imodbits_axe, [], [fac_orc]], 
["choppa6", "Orc_War_Choppa", [("GS_Choppa_1H_T5_03", 0)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield, itc_scimitar|itcf_carry_mace_left_hip, 2750, weight(2.00)|abundance(100)|difficulty(11)|weapon_length(104)|spd_rtng(96)|swing_damage(40, pierce)|thrust_damage(0, pierce), imodbits_axe, [], [fac_orc]], 





["beastman_head", "Beastman_head", [("beastmen", 0)], itp_type_fullhelm, 0, 75, weight(2)|abundance(10)|head_armor(40)|body_armor(0)|leg_armor(0), imodbits_none , [], [fac_beast]],
["beastman_head2", "Beastman_head", [("beastmenss", 0)], itp_type_fullhelm, 0, 75, weight(2)|abundance(10)|head_armor(40)|body_armor(0)|leg_armor(0), imodbits_none , [], [fac_beast]],
["beastarmour_head", "Beastman_helmet", [("beastman", 0)], itp_type_fullhelm, 0, 200, weight(4)|abundance(10)|head_armor(60)|body_armor(0)|leg_armor(0), imodbits_none , [], [fac_beast]],
["beastlord_head", "Beastlord_head", [("beastlord", 0)], itp_type_fullhelm, 0, 400, weight(4)|abundance(10)|head_armor(70)|body_armor(0)|leg_armor(0), imodbits_none , [], [fac_beast]],


["beastman_body", "Beastman", [("beastman_bodys", 0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 210, weight(10)|abundance(10)|head_armor(0)|body_armor(30)|leg_armor(10), imodbits_armor , [], [fac_beast]],
["beastman_armour", "Beastman_armour", [("beastman_body", 0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 410, weight(11)|abundance(10)|head_armor(0)|body_armor(45)|leg_armor(10), imodbits_armor , [], [fac_beast]],
["beastman_heavyarmour", "Beastman_heavy_armour", [("beastman_arm", 0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 2100, weight(19)|abundance(10)|head_armor(0)|body_armor(60)|leg_armor(10), imodbits_armor , [], [fac_beast]],

["rathelm", "rat's_Head", [("SkavenHead", 0)], itp_type_fullhelm|itp_unique, 0, 75, weight(2)|abundance(10)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_none ],
["rathelm2", "rat's_Head", [("SkavenHead2", 0)], itp_type_fullhelm|itp_unique, 0, 75, weight(2)|abundance(10)|head_armor(50)|body_armor(0)|leg_armor(0), imodbits_none ],
["rathelm3", "rat's_Head", [("SkavenHead3", 0)], itp_type_fullhelm|itp_unique, 0, 75, weight(2)|abundance(10)|head_armor(70)|body_armor(0)|leg_armor(0), imodbits_none ],

####DUNLAND ITEMS##########
["rat_wolfboots","Wolfboots",[("rat_wolfboots",0)],itp_type_foot_armor|itp_attach_armature,0,300,weight(3)|leg_armor(10)|difficulty(0),imodbits_cloth, [], [fac_beast]],
##ARMORS########
["rat_armor_1","Rat_Fur_Armor",[("rat_fur_a",0)],itp_type_body_armor|itp_covers_legs,0,300,weight(14)|head_armor(1)|body_armor(20)|leg_armor(4)|difficulty(0),imodbits_cloth, [], [fac_beast]],
["rat_armor_2","Rat_Fur_Armor",[("rat_fur_b",0)],itp_type_body_armor|itp_covers_legs,0,400,weight(15)|head_armor(1)|body_armor(24)|leg_armor(8)|difficulty(0),imodbits_cloth, [], [fac_beast]],
["rat_armor_3","Rat_Fur_Armor",[("rat_fur_c",0)],itp_type_body_armor|itp_covers_legs,0,400,weight(15)|head_armor(1)|body_armor(24)|leg_armor(8)|difficulty(0),imodbits_cloth, [], [fac_beast]],

["rat_armor_4","Rat_Fur_Armor",[("rat_fur_d",0)],itp_type_body_armor|itp_covers_legs,0,350,weight(14)|head_armor(1)|body_armor(24)|leg_armor(4)|difficulty(0),imodbits_cloth, [], [fac_beast]],
["rat_armor_5","Rat_Fur_Armor",[("rat_fur_e",0)],itp_type_body_armor|itp_covers_legs,0,600,weight(15)|head_armor(1)|body_armor(28)|leg_armor(5)|difficulty(0),imodbits_cloth, [], [fac_beast]],
["rat_armor_6","Rat_Fur_Armor",[("rat_fur_f",0)],itp_type_body_armor|itp_covers_legs,0,700,weight(16)|head_armor(1)|body_armor(28)|leg_armor(8)|difficulty(0),imodbits_cloth, [], [fac_beast]],

["rat_armor_7","Dun_Long_Fur_Armor",[("rat_long_fur",0)],itp_type_body_armor|itp_covers_legs,0,900,weight(16)|head_armor(2)|body_armor(32)|leg_armor(9)|difficulty(0),imodbits_cloth,],
["rat_armor_8","Rat_Hauberk",[("rat_hauberk_a",0)],itp_type_body_armor|itp_covers_legs,0,1200,weight(23)|head_armor(2)|body_armor(44)|leg_armor(7)|difficulty(0),imodbits_armor, [], [fac_beast]],
["rat_armor_9","rat_Hauberk",[("rat_hauberk_b",0)],itp_type_body_armor|itp_covers_legs,0,1200,weight(23)|head_armor(2)|body_armor(44)|leg_armor(10)|difficulty(0),imodbits_armor, [], [fac_beast]],
["rat_armor_10","Dun_Chief_Armor",[("rat_chieftain",0)],itp_type_body_armor|itp_covers_legs,0,2000,weight(26)|head_armor(2)|body_armor(50)|leg_armor(13)|difficulty(0),imodbits_armor, [], [fac_beast]],
#######HELMS##########
#["dun_helm_a","Rat_Wolf_Cap",[("rat_wolfcap",0)],itp_type_head_armor,0,300,weight(2)|head_armor(25)|difficulty(0),imodbits_cloth],
#["dun_helm_b","Rat_Antler_Cap",[("rat_antlercap",0)],itp_type_head_armor,0,200,weight(2)|head_armor(21)|difficulty(0),imodbits_cloth],
#["dun_helm_c","Rat_Tall_Helm",[("rat_helm_a",0)],itp_type_head_armor,0,800,weight(2)|head_armor(30)|difficulty(0),imodbits_armor | imodbit_cracked],
#["dun_helm_d","Rat_Tall_Helm",[("rat_helm_c",0)],itp_type_head_armor,0,800,weight(2)|head_armor(30)|difficulty(0),imodbits_armor | imodbit_cracked],
#["dun_helm_e","Dun_Tall_War_Helm",[("rat_helm_b",0)],itp_type_head_armor,0,1200,weight(3)|head_armor(35)|difficulty(0),imodbits_armor],
#######SHIELDS##########

["granata_poison", "poison_Grenade", [("bombaaa_m", 0)], itp_type_thrown|itp_crush_through|itp_merchandise|itp_primary, itcf_throw_stone, 4500, weight(4)|weapon_length(25)|difficulty(2)|spd_rtng(67)|shoot_speed(18)|abundance(33)|thrust_damage(140, blunt)|max_ammo(6), imodbits_none,[(ti_on_missile_hit, [(store_trigger_param_1, ":shooter"),(copy_position,pos51,pos1),(call_script, "script_magic_deliver_area_damage", ":shooter", 120, 7, 11),]),]+missile_distance_trigger,firearm_factions],

["lizard_armour_1", "lizard Armour", [("lizard_body1",0)], itp_type_body_armor  |itp_covers_legs|itp_unique ,0, 100,cloth_tier_1 ,imodbits_plate , [], [fac_scotland]],
["lizard_armour_2", "lizard Leather Armour", [("lizleather1",0)], itp_type_body_armor  |itp_covers_legs|itp_unique ,0, 940,cloth_tier_3 ,imodbits_plate , [], [fac_scotland]],
["lizard_armour_3", "lizard Leather Armour", [("lizarmor1",0)], itp_type_body_armor  |itp_covers_legs|itp_unique ,0, 1722,mail_armor_tier_2 ,imodbits_plate , [], [fac_scotland]],
["lizard_armour_4", "lizard captain Armour", [("lizleatherarmor1",0)], itp_type_body_armor  |itp_covers_legs|itp_unique ,0, 4035, mail_armor_tier_3 ,imodbits_plate , [], [fac_scotland]],
["lizard_armour_5", "lizard captain Armour", [("lizplate1",0)], itp_type_body_armor  |itp_covers_legs|itp_unique ,0, 7876,lamellar_armor_tier_4 ,imodbits_plate , [], [fac_scotland]],
["lizard_armour_6", "lizard Armour", [("lizard_hero_armor1",0)], itp_type_body_armor  |itp_covers_legs|itp_unique ,0, 9216,full_plate_armor_tier_3 ,imodbits_plate , [], [fac_scotland]],

["lizard_shaman_1", "lizard mail Armour", [("lizardshaman2",0)], itp_type_body_armor  |itp_covers_legs|itp_unique ,0, 2704,mail_armor_tier_2 ,imodbits_plate , [], [fac_scotland]],
["lizard_shaman_2", "lizard captain Armour", [("lizardshaman3",0)], itp_type_body_armor  |itp_covers_legs|itp_unique ,0, 5256,mail_armor_tier_4 ,imodbits_plate , [], [fac_scotland]],

["lizard_boot_1", "lizard Legs", [("lizardlegs",0)], itp_type_foot_armor|itp_civilian|itp_attach_armature|itp_unique,0,
 1250 , weight(2.0)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(15)|difficulty(7) ,imodbits_armor , [], [fac_scotland]],
["lizard_boot_2", "lizard Leather Boots", [("lizardboots1",0)], itp_type_foot_armor|itp_attach_armature|itp_unique,0,
 2520 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(7) ,imodbits_armor , [], [fac_scotland]],
["lizard_boot_3", "lizard Leather Boots", [("lizardboots2",0)], itp_type_foot_armor|itp_civilian|itp_attach_armature|itp_unique,0,
 1250 , weight(2.0)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(7) ,imodbits_armor , [], [fac_scotland]],
["lizard_boot_4", "lizard Leather with Iron Boots", [("lizardboots3",0)], itp_type_foot_armor|itp_attach_armature|itp_unique,0,
 2520 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(40)|difficulty(7) ,imodbits_armor , [], [fac_scotland]],

["lizard_helmet_1", "lizard Helmet", [("lizardmanheadmulti2",0)], itp_unique|itp_type_fullhelm ,0, 
  1666 , weight(2)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate , [], [fac_scotland]],
["lizard_helmet_2", "lizard Helmet", [("lizardmanheadmulti5",0)], itp_unique|itp_type_fullhelm ,0, 
  2400 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate , [], [fac_scotland]],
["lizard_helmet_3", "lizard captain Helmet", [("lizardchainmaska",0)], itp_unique|itp_type_fullhelm,0, 
  3266 , weight(3)|abundance(100)|head_armor(70)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate , [], [fac_scotland]],
["lizard_shaman_helmet", "lizard shaman Helmet", [("lizheadcover1",0)], itp_unique|itp_type_fullhelm ,0, 
  2400 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate , [], [fac_scotland]],

["lizard_glove1","lizard_glove1", [("lizard_glove1_L",0)], itp_type_hand_armor|itp_unique,0, 
 820, weight(1)|abundance(100)|body_armor(10)|difficulty(0),imodbits_armor, [], [fac_scotland]],
["lizard_glove2","lizard_glove2", [("lizard_glove2_L",0)], itp_type_hand_armor|itp_unique,0, 
 820, weight(1)|abundance(100)|body_armor(15)|difficulty(0),imodbits_armor, [], [fac_scotland]],


#["wolfarmor", "Werewolf's_Paws", [("Werebody",0)], itp_type_full_body_armor ,0, 6360,weight(1)|abundance(60)|head_armor(0)|body_armor(45)|leg_armor(24)|difficulty(14),imodbits_armor ],
#["wolfboots", "Werewolf's_Paws", [("WolfBoot_L",0)], itp_type_foot_armor|itp_civilian|itp_unique ,0,  2376 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(0) ,imodbits_cloth,],
["wolfgloves","Werewolf's_Paws", [("wolfglove_L",0)], itp_type_hand_armor|itp_unique,0, 
 820, weight(1)|abundance(100)|body_armor(15)|difficulty(0),imodbits_armor, ],
["wolfhelm", "Werewolf's_Head", [("WerewolfHead", 0)], itp_type_fullhelm|itp_unique, 0, 75, weight(2)|abundance(10)|head_armor(80)|body_armor(0)|leg_armor(0), imodbits_none ],



["werewolfarmor", "Werewolf'armor", [("WhiteWerebody_1",0)], itp_unique|itp_type_full_body_armor ,0, 6360,weight(1)|abundance(60)|head_armor(70)|body_armor(70)|leg_armor(70)|difficulty(14),imodbits_armor ],
["werewolfarmor_w", "Werewolf'armor", [("Werebody_1",0)], itp_unique|itp_type_full_body_armor ,0, 6360,weight(1)|abundance(60)|head_armor(80)|body_armor(75)|leg_armor(75)|difficulty(14),imodbits_armor ],

["wolfclaw", "Werewolf's_Right_Claw", [("toumingshen",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_bonus_against_shield|itp_unique|itp_no_pick_up_from_ground, itc_gauntlet, 0 , weight(1.5)|difficulty(100)|spd_rtng(130)| weapon_length(120)|swing_damage(35 , cut)| thrust_damage(0 ,  pierce),imodbits_axe ],
["wolfclaw_w", "Werewolf's_Right_Claw", [("toumingshen",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_bonus_against_shield|itp_unique|itp_no_pick_up_from_ground, itc_gauntlet, 0 , weight(1.5)|difficulty(100)|spd_rtng(130)| weapon_length(120)|swing_damage(35 , pierce)| thrust_damage(0 ,  pierce),imodbits_axe ],

["werewolfclaw", "Werewolf's_Right_Claw", [("toumingshen",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_bonus_against_shield|itp_unique|itp_no_pick_up_from_ground, itc_gauntlet, 0 , weight(1.5)|difficulty(100)|spd_rtng(140)| weapon_length(120)|swing_damage(40 , pierce)| thrust_damage(0 ,  pierce),imodbits_axe ],
["werewolfclaw_w", "Werewolf's_Right_Claw", [("toumingshen",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_bonus_against_shield|itp_unique|itp_no_pick_up_from_ground, itc_gauntlet, 0 , weight(1.5)|difficulty(100)|spd_rtng(130)| weapon_length(120)|swing_damage(45 , pierce)| thrust_damage(0 ,  pierce),imodbits_axe ],

["hugewolfclaw", "Werewolf's_Right_Claw", [("toumingshen",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_can_knock_down|itp_crush_through|itp_bonus_against_shield|itp_unique|itp_no_pick_up_from_ground, itc_gauntlet, 0 , weight(1.5)|difficulty(100)|spd_rtng(140)| weapon_length(170)|swing_damage(40 , pierce)| thrust_damage(0 ,  pierce),imodbits_axe ],
["hugewolfclaw_w", "Werewolf's_Right_Claw", [("toumingshen",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_can_knock_down|itp_crush_through|itp_bonus_against_shield|itp_unique|itp_no_pick_up_from_ground, itc_gauntlet, 0 , weight(1.5)|difficulty(100)|spd_rtng(130)| weapon_length(150)|swing_damage(45 , pierce)| thrust_damage(0 ,  pierce),imodbits_axe ],

["tree_trunk_invis", "Tree_Trunk", [("toumingshou",0)], itp_can_knock_down|itp_crush_through|itp_type_one_handed_wpn|itp_primary|itp_wooden_parry|itp_wooden_attack|itp_unbalanced|itp_unique|itp_no_pick_up_from_ground, itc_gauntlet,101 , weight(250)|difficulty(20)|spd_rtng(87)| weapon_length(186)|swing_damage(50, blunt)| thrust_damage(50 ,  blunt),imodbits_mace, [], [fac_elf]],

["wolfclaw_dual", "Werewolf's_Left_Claw", [("toumingshen",0)], itp_type_shield|itp_unique, itcf_carry_round_shield,  2091 , weight(4)|difficulty(100)|shield_hit_points(999)|body_armor(125)|spd_rtng(61)|shield_width(60),imodbits_shield ],
["wolfclaw_dual_w", "Werewolf's_Left_Claw", [("toumingshen",0)], itp_type_shield|itp_unique, itcf_carry_round_shield,  2091 , weight(4)|difficulty(100)|shield_hit_points(999)|body_armor(125)|spd_rtng(61)|shield_width(60),imodbits_shield ,],

["werewolfclaw_dual", "Werewolf's_Left_Claw", [("toumingshen",0)], itp_type_shield|itp_unique, itcf_carry_round_shield,  2091 , weight(4)|difficulty(100)|shield_hit_points(999)|body_armor(125)|spd_rtng(61)|shield_width(60),imodbits_shield ],
["werewolfclaw_dual_w", "Werewolf's_Left_Claw", [("toumingshen",0)], itp_type_shield|itp_unique, itcf_carry_round_shield,  2091 , weight(4)|difficulty(100)|shield_hit_points(999)|body_armor(125)|spd_rtng(61)|shield_width(60),imodbits_shield ,],

#["wolfarmor_w", "Werewolf's_Paws", [("WhiteWerebody",0)], itp_type_full_body_armor ,0, 6360,weight(1)|abundance(60)|head_armor(0)|body_armor(60)|leg_armor(24)|difficulty(14),imodbits_armor ],
#["wolfboots_w", "Werewolf's_Paws", [("WhiteWolfBoot_L",0)], itp_type_foot_armor|itp_civilian|itp_unique ,0,  2376 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(0) ,imodbits_cloth,],
["wolfgloves_w","Werewolf's_Paws", [("whitewolfglove_L",0)], itp_type_hand_armor|itp_unique,0, 
 820, weight(1)|abundance(100)|body_armor(15)|difficulty(0),imodbits_armor, ],
["wolfhelm_w", "Werewolf's_Head", [("WhiteWerewolfHead", 0)], itp_type_fullhelm|itp_unique, 0, 75, weight(2)|abundance(10)|head_armor(80)|body_armor(0)|leg_armor(0), imodbits_none ],


["lorien_boots", "Lothlorien_Boots", [("lorien_boots", 0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 2945, weight(1)|abundance(10)|head_armor(0)|body_armor(0)|leg_armor(28), imodbits_cloth , [], [fac_elf,fac_hospitalier_knights]],

["lorien_archer", "Lorien_Archer_Armor", [("lorien_archer", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 1048, weight(8)|abundance(10)|head_armor(0)|body_armor(28)|leg_armor(10), imodbits_cloth , [], [fac_elf,fac_hospitalier_knights]],

["lorien_armor_e", "Lorien_Warden_Cloak", [("lorien_warden_cloak", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 4629, weight(10)|abundance(10)|difficulty(5)|head_armor(0)|body_armor(36)|leg_armor(20), imodbits_cloth , [], [fac_elf,fac_hospitalier_knights]],

["lorien_armor_c", "Lorien_Royal_Archer_Armor", [("lorien_royalarcher_01", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 7722, weight(18)|abundance(10)|difficulty(10)|head_armor(0)|body_armor(50)|leg_armor(20), imodbits_armor, [], [fac_elf,fac_hospitalier_knights] ],

["lorien_armor_a", "Lorien_Infantry_Armor", [("lorien_infantry_01", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 1233, weight(12)|abundance(10)|difficulty(6)|head_armor(0)|body_armor(30)|leg_armor(10), imodbits_armor , [], [fac_elf,fac_hospitalier_knights]],

["lorien_armor_b", "Lorien_Heavy_Infantry_Armor", [("lorien_vetinfantry_01", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 4765, weight(16)|abundance(10)|difficulty(8)|head_armor(0)|body_armor(40)|leg_armor(16), imodbits_armor, [], [fac_elf,fac_hospitalier_knights] ],

["lorien_armor_f", "Lorien_Elite_Armor", [("lorien_eliteinfantry_01", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 7693, weight(20)|abundance(10)|difficulty(10)|head_armor(0)|body_armor(56)|leg_armor(18), imodbits_armor, [], [fac_elf,fac_hospitalier_knights] ],

["lorien_armor_d", "Lorien_Royal_Swordsman_Armor", [("lorien_royalswordsman_01", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 15382, weight(22)|abundance(10)|difficulty(12)|head_armor(0)|body_armor(70)|leg_armor(24), imodbits_armor, [], [fac_elf,fac_hospitalier_knights] ],

["elf_twiligh_armor", "twiligh_armor", [("elf_twiligh_armor",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 20000, weight(28)|abundance(100)|head_armor(20)|body_armor(90)|leg_armor(40)|difficulty(20), imodbits_good_plate ,[], [fac_kingdom_1]],

["lorien_helm_a", "Lorien_Archer_Helm", [("lorienhelmetarcherlow", 0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head, 0, 6593, weight(1)|abundance(10)|difficulty(6)|head_armor(50)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac_elf] ],

["lorien_helm_b", "Lorien_Archer_Helm", [("lorienhelmetarcherhigh", 0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head, 0, 7037, weight(1)|abundance(10)|difficulty(6)|head_armor(70)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac_elf] ],

["lorien_helm_c", "Lorien_Infantry_Helm", [("lorienhelmetinf", 0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head, 0, 7286, weight(1)|abundance(10)|difficulty(6)|head_armor(60)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac_elf] ],

["lorien_helm_d", "Citadel_Knight_Helm", [("gondor_citadel_knight_helm", 0)], itp_merchandise|itp_type_head_armor, 0, 4900, weight(2.75)|abundance(10)|difficulty(10)|head_armor(70)|body_armor(0)|leg_armor(0), imodbits_armor ,[], [fac_kingdom_1] ],

["lorien_helm_e", "High_Helmet", [("gondor_leader_helm", 0)], itp_merchandise|itp_type_head_armor, 0, 8100, weight(2)|abundance(10)|difficulty(7)|head_armor(90)|body_armor(0)|leg_armor(0), imodbits_armor ,[], [fac_kingdom_1] ],

["lorien_helm_f", "Tower_Guard_Helm", [("gondor_tower_guard_helm", 0)], itp_merchandise|itp_type_head_armor, 0, 8100, weight(2.75)|abundance(10)|difficulty(10)|head_armor(120)|body_armor(0)|leg_armor(0), imodbits_armor ,[], [fac_elf,fac_hospitalier_knights] ],

#["tower_archer_helm", "Tower_Archer_Helm", [("gondor_tower_archer_helm", 0)], itp_type_head_armor, 0, 5625, weight(2)|abundance(10)|difficulty(7)|head_armor(112)|body_armor(0)|leg_armor(0), imodbits_armor ],


["lorien_sword_a", "Lorien_Longsword", [("lorien_sword_long", 0), ("scab_lorien_sword_long", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_show_holster_when_drawn|itcf_carry_sword_left_hip, 4856, weight(1.5)|weapon_length(87)|difficulty(2)|spd_rtng(105)|abundance(10)|swing_damage(34, cut)|thrust_damage(34, pierce), imodbits_sword_high, [], [fac_elf,fac_hospitalier_knights] ],

["lorien_sword_b", "Lorien_Shortsword", [("lorien_sword_short", 0), ("scab_lorien_sword_short", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_show_holster_when_drawn|itcf_carry_sword_left_hip, 3045, weight(1.5)|weapon_length(65)|difficulty(0)|spd_rtng(114)|abundance(10)|swing_damage(28, cut)|thrust_damage(34, pierce), imodbits_sword_high, [], [fac_elf,fac_hospitalier_knights] ],

["lorien_sword_c", "Lorien_War_Sword", [("lorien_sword_hand_and_half", 0), ("scab_lorien_sword_hand_and_half", ixmesh_carry)], itp_merchandise|itp_type_two_handed_wpn|itp_primary, itcf_thrust_onehanded|itcf_overswing_onehanded|itcf_slashright_onehanded|itcf_slashleft_onehanded|itc_claymore|itcf_show_holster_when_drawn|itcf_carry_sword_left_hip, 6493, weight(1.5)|weapon_length(92)|difficulty(3)|spd_rtng(100)|abundance(10)|swing_damage(41, cut)|thrust_damage(34, pierce), imodbits_sword_high, [], [fac_elf,fac_hospitalier_knights] ],


["lorien_shield_b", "Lorien_Tower_Shield", [("fix_lorien_kite", 0)], itp_merchandise|itp_type_shield|itp_wooden_parry|itp_cant_use_on_horseback, itcf_carry_kite_shield, 2156, weight(2)|shield_width(40)|shield_height(70)|abundance(10)|hit_points(1000)|body_armor(20)|spd_rtng(82), imodbits_shield, [], [fac_elf] ],

["lorien_shield_c", "Lorien_Kite_Shield", [("fix_lorien_kite_small", 0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 1983, weight(2)|shield_width(40)|shield_height(55)|abundance(10)|hit_points(800)|body_armor(18)|spd_rtng(92), imodbits_shield , [], [fac_elf]],

["lorien_round_shield", "Lorien_Round_Shield", [("lorien_round_shield", 0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 1685, weight(1)|shield_width(50)|abundance(10)|hit_points(700)|body_armor(14)|spd_rtng(96), imodbits_shield , [], [fac_elf]],


["mirkwood_boots", "Mirkwood_boots", [("mirkwood_boots", 0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 2520, weight(1)|abundance(10)|head_armor(0)|body_armor(0)|leg_armor(23), imodbits_cloth, [], [fac_forest_ranger,fac_kingdom_4] ],

["mirkwood_helm_a", "Mirkwood_Archer_Helm", [("mirkwood_helm", 0)], itp_merchandise|itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0, 6593, weight(1)|abundance(10)|head_armor(50)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac_forest_ranger,fac_kingdom_4] ],

["mirkwood_helm_d", "Mirkwood_Royal_Archer_Helm", [("mirkwoodroyalarcher", 0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head, 0, 7037, weight(1)|abundance(10)|head_armor(70)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac_forest_ranger,fac_kingdom_4] ],

["mirkwood_helm_b", "Mirkwood_Helm", [("mirkwoodnormalspearman", 0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head, 0, 6845, weight(1)|abundance(10)|difficulty(5)|head_armor(60)|body_armor(0)|leg_armor(0), imodbits_armor, [], [fac_forest_ranger,fac_kingdom_4] ],

["mirkwood_helm_c", "Mirkwood_Royal_Spearman_Helm", [("mirkwoodroyalspearman", 0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head, 0, 8252, weight(1)|abundance(10)|difficulty(6)|head_armor(80)|body_armor(0)|leg_armor(0), imodbits_good_plate , [], [fac_forest_ranger,fac_kingdom_4]],

["mirkwood_armor_a", "Light_Leather", [("mirkwood_leather", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 924, weight(10)|abundance(10)|difficulty(4)|head_armor(0)|body_armor(28)|leg_armor(12), imodbits_cloth, [], [fac_forest_ranger,fac_kingdom_4] ],

["mirkwood_armor_d", "Light_Quilted_Surcoat", [("mirkwood_quiltedsurcoat_01", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 3458, weight(13)|abundance(10)|difficulty(5)|head_armor(0)|body_armor(32)|leg_armor(14), imodbits_armor, [], [fac_forest_ranger,fac_kingdom_4] ],

["mirkwood_armor_e", "Light_Mail_and_Surcoat", [("mirkwood_maillewithsurcoat_01", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 6871, weight(15)|abundance(10)|difficulty(7)|head_armor(0)|body_armor(42)|leg_armor(18), imodbits_armor, [], [fac_forest_ranger,fac_kingdom_4] ],

["mirkwood_light_scale", "Light_Woodelf_Scale", [("mirkwood_light_scale", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 1424, weight(10)|abundance(10)|difficulty(6)|head_armor(0)|body_armor(30)|leg_armor(14), imodbits_armor, [], [fac_forest_ranger,fac_kingdom_4] ],

["mirkwood_armor_b", "Light_Quilted_and_Scale_Armor", [("mirkwood_scalequilted_01", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 4047, weight(12)|abundance(10)|difficulty(6)|head_armor(0)|body_armor(40)|leg_armor(18), imodbits_armor, [], [fac_forest_ranger,fac_kingdom_4] ],

["mirkwood_armor_c", "Light_Scale_over_Mail", [("mirkwood_scaleovermaille_01", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 7425, weight(16)|abundance(10)|difficulty(8)|head_armor(0)|body_armor(50)|leg_armor(20), imodbits_armor, [], [fac_forest_ranger,fac_kingdom_4] ],

["mirkwood_armor_f", "Royal_Woodelf_Armor", [("mirkwood_royal", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 14752, weight(20)|abundance(10)|difficulty(12)|head_armor(3)|body_armor(65)|leg_armor(16), imodbits_armor, [], [fac_forest_ranger,fac_kingdom_4] ],

["mirkwood_armor_g", "Royal_Woodelf_Armor", [("Shadow_striker", 0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 14752, weight(20)|abundance(10)|difficulty(12)|head_armor(3)|body_armor(60)|leg_armor(16), imodbits_armor, [], [fac_forest_ranger,fac_kingdom_4] ],





["mirkwood_knife", "Mirkwood_White_Knife", [("mirkwood_white_knife", 0), ("scab_mirkwood_white_knife", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_no_parry|itp_primary|itp_secondary, itcf_thrust_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_show_holster_when_drawn|itcf_carry_sword_left_hip, 2891, weight(0.75)|weapon_length(51)|difficulty(0)|spd_rtng(120)|abundance(10)|swing_damage(26, cut)|thrust_damage(32, pierce), imodbits_sword , [], [fac_forest_ranger,fac_kingdom_4]],

["mirkwood_sword", "Mirkwood_Sword", [("mirkwood_longsword", 0), ("scab_mirkwood_longsword", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_show_holster_when_drawn|itcf_carry_sword_left_hip, 5178, weight(1.25)|weapon_length(92)|difficulty(2)|spd_rtng(113)|abundance(10)|swing_damage(34, cut)|thrust_damage(32, pierce), imodbits_sword_high, [], [fac_forest_ranger,fac_kingdom_4] ],


["mirkwood_short_spear", "Mirkwood_Spear", [("mirkwood_short_spear", 0)], itp_merchandise|itp_type_polearm|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_cant_use_on_horseback, itc_spear|itcf_carry_spear, 2481, weight(2.5)|weapon_length(117)|difficulty(0)|spd_rtng(100)|abundance(10)|swing_damage(22, blunt)|thrust_damage(28, pierce), imodbits_polearm , [], [fac_forest_ranger,fac_kingdom_4]],

["mirkwood_war_spear", "Mirkwood_War_Spear", [("mirkwood_war_spear", 0)], itp_merchandise|itp_type_polearm|itp_default_ammo|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_cant_use_on_horseback, itc_spear|itcf_carry_spear, 3742, weight(2.5)|weapon_length(150)|difficulty(2)|spd_rtng(95)|abundance(10)|swing_damage(30, blunt)|thrust_damage(40, pierce), imodbits_polearm, [], [fac_forest_ranger,fac_kingdom_4] ],

["mirkwood_great_spear", "Mirkwood_Great_Spear", [("mirkwood_great_spear_large", 0)], itp_merchandise|itp_type_polearm|itp_default_ammo|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_is_pike, itc_pike|itcf_carry_spear, 5014, weight(3.5)|weapon_length(220)|difficulty(4)|spd_rtng(90)|abundance(10)|swing_damage(36, blunt)|thrust_damage(52, pierce),imodbits_polearm, [], [fac_forest_ranger,fac_kingdom_4] ],

["mirkwood_great_lance", "Mirkwood_Great_Lance", [("mirkwood_great_spear_large", 0)], itp_merchandise|itp_type_polearm|itp_couchable|itp_wooden_parry|itp_primary, itc_greatlance, 5014, weight(3.5)|weapon_length(220)|difficulty(4)|spd_rtng(90)|abundance(10)|swing_damage(32, blunt)|thrust_damage(48, pierce), imodbits_polearm, [], [fac_forest_ranger,fac_kingdom_4] ],

["mirkwood_spear_shield_a", "Mirkwood_Spearman_Shield", [("fix_mirkwood_spear_shield", 0)], itp_merchandise|itp_type_shield|itp_wooden_parry|itp_cant_use_on_horseback, itcf_carry_kite_shield, 2156, weight(3)|shield_width(40)|shield_height(70)|abundance(10)|hit_points(1000)|body_armor(20)|spd_rtng(82), imodbits_shield, [], [fac_forest_ranger,fac_kingdom_4] ],

["mirkwood_spear_shield_b", "Mirkwood_War_Shield", [("fix_mirkwood_med_shield", 0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 1923, weight(2)|shield_width(40)|shield_height(55)|abundance(10)|hit_points(800)|body_armor(15)|spd_rtng(90), imodbits_shield, [], [fac_forest_ranger] ],

["mirkwood_spear_shield_c", "Mirkwood_Swordsman_Shield", [("fix_mirkwood_royal_round", 0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 3445, weight(2)|shield_width(40)|shield_height(40)|abundance(10)|hit_points(1000)|body_armor(28)|spd_rtng(90), imodbits_shield, [], [fac_forest_ranger,fac_kingdom_4] ],



["scimitar_green", "Ranger_Scimitar", [("glass_longsword", 0)], itp_merchandise|itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_back, 6178, weight(1.25)|weapon_length(100)|difficulty(10)|spd_rtng(100)|abundance(10)|swing_damage(35, pierce)|thrust_damage(24, pierce), imodbits_sword_high,[], [fac_kingdom_4] ],

["sabre_hithlain", "Royal_Scimitar", [("sabre_hithlain", 0), ("sabre_hithlain_scab", ixmesh_carry)], itp_merchandise|itp_type_two_handed_wpn|itp_primary, itc_morningstar|itcf_show_holster_when_drawn|itcf_carry_katana, 2390, weight(2.25)|weapon_length(120)|difficulty(10)|spd_rtng(120)|abundance(10)|swing_damage(40, cut), imodbits_sword_high ,[], [fac_elf] ],

["courtblades_ivory_1", "Royal_Courtblade Staff", [("courtblades_ivory", 0), ("courtblades_ivory_scab", ixmesh_carry)], itp_merchandise|itp_type_pistol|itp_crush_through|itp_primary|itp_next_item_as_melee|itp_is_magic_staff ,itcf_reload_pistol|itcf_shoot_pistol|itcf_show_holster_when_drawn|itcf_carry_wakizashi,
 25000 , weight(3.25)|difficulty(0)|spd_rtng(80) | shoot_speed(150) | thrust_damage(80 ,pierce)|max_ammo(3)|accuracy(82),imodbits_magic_staff, magic_cast_trigger , [fac_elf] ], 
["courtblades_ivory", "Royal_Courtblade", [("courtblades_ivory", 0), ("courtblades_ivory_scab", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_show_holster_when_drawn|itcf_carry_wakizashi, 6513, weight(2.25)|weapon_length(100)|difficulty(10)|spd_rtng(120)|abundance(10)|swing_damage(40, cut)|thrust_damage(42, pierce), imodbits_sword_high  ,[], [fac_kingdom_1]],

["courtblades_green", "green_Courtblade", [("mirkwood_sword", 0), ("scab_mirkwood_sword", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_show_holster_when_drawn|itcf_carry_sword_left_hip, 6513, weight(2.25)|weapon_length(100)|difficulty(10)|spd_rtng(120)|abundance(10)|swing_damage(40, cut)|thrust_damage(40, pierce), imodbits_sword_high,[], [fac_forest_ranger,fac_culture_4] ],


["warblade_greensilver", "Glass Bastard Sword", [("glass_bastard",0)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_back, 8921, weight(1)|weapon_length(130)|difficulty(10)|spd_rtng(122)|abundance(10)|swing_damage(40, pierce), imodbits_sword_high,[], [fac_kingdom_4] ],
["warblade_ivorygold", "Royal_Warblade", [("warblade_ivorygold", 0), ("warblade_ivorygold_sheath", ixmesh_carry)], itp_merchandise|itp_type_two_handed_wpn|itp_primary, itc_morningstar|itcf_show_holster_when_drawn|itcf_carry_katana, 8921, weight(2)|weapon_length(110)|difficulty(10)|spd_rtng(110)|abundance(10)|swing_damage(47, cut), imodbits_sword_high ,[], [fac_elf] ],


["sabre_2h_green", "Greenwood_Sabre", [("glassbattleaxe", 0)], itp_merchandise|itp_type_two_handed_wpn|itp_primary|itp_bonus_against_shield|itp_extra_penetration|itp_two_handed, itc_nodachi|itcf_carry_axe_back, 12513, weight(1)|weapon_length(120)|difficulty(15)|spd_rtng(122)|abundance(10)|swing_damage(45, pierce), imodbits_axe|imodbit_masterwork,[], [fac_kingdom_4] ],


#["double_sided_sabre", "Double Sided Courtblade", [("dblhead_saber",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_next_item_as_melee, itc_staff|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded, 6513 , weight(4.5)|difficulty(10)|spd_rtng(120)| weapon_length(130)|swing_damage(40, cut)| thrust_damage(42 ,  pierce),imodbits_balanced|imodbits_tempered|imodbits_masterwork ],
#["double_sided_sabre_onehand", "Double Sided Courtblade", [("dblhead_saber",0)], itp_type_two_handed_wpn|itp_offset_lance| itp_primary, itc_bastardsword, 6513 , weight(4.5)|difficulty(10)|spd_rtng(120)| weapon_length(130)|swing_damage(40, cut)| thrust_damage(42 ,  pierce),imodbits_balanced|imodbits_tempered|imodbits_masterwork ],


["double_sided_sabre_2", "Double Sided Warblade", [("dblhead_saber_2",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_next_item_as_melee, itcf_overswing_polearm |itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm | itc_parry_polearm |itc_dagger | itcf_horseback_thrust_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded, 6513 , weight(4.5)|difficulty(10)|spd_rtng(120)| weapon_length(150)|swing_damage(40, pierce)| thrust_damage(42 ,  pierce),imodbits_sword_high ],
["double_sided_sabre_2_onehand", "Double Sided Warblade", [("dblhead_saber_2",0)], itp_type_two_handed_wpn|itp_offset_lance| itp_primary, itcf_overswing_polearm |itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm | itc_parry_polearm |itc_dagger | itcf_horseback_thrust_onehanded, 6513 , weight(4.5)|difficulty(10)|spd_rtng(120)| weapon_length(150)|swing_damage(40, pierce)| thrust_damage(42 ,  pierce),imodbits_sword_high ],


["ent_body","Ent_Body",[("ent_body",0)],itp_type_full_body_armor,0,1,weight(250)|head_armor(0)|body_armor(90)|leg_armor(0)|difficulty(70),0,],
["ent_head_helm","Ent_Head",[("ent_head1",0)],itp_type_fullhelm|itp_unique,0,1,weight(250)|head_armor(70)|body_armor(10)|difficulty(70),0],


["ent_feet_boots","Ent_Feet",[("ent_foot",0)],itp_type_foot_armor|itp_unique,0,1,weight(250)|head_armor(0)|body_armor(0)|leg_armor(70)|difficulty(70),0],
["ent_hands","Ent_Hands",[("ent_hand_L",0)],itp_type_hand_armor|itp_unique,0,1,weight(250)|body_armor(1)|difficulty(70),0],

["green_ent_body","Ent_Body",[("green_ent_body",0)],itp_type_full_body_armor,0,1,weight(250)|head_armor(0)|body_armor(65)|leg_armor(0)|difficulty(70),0,],
["green_ent_head_helm","Ent_Head",[("green_ent_head",0)],itp_type_fullhelm|itp_unique,0,1,weight(250)|head_armor(60)|body_armor(10)|difficulty(70),0],


["green_ent_feet_boots","Ent_Feet",[("green_ent_foot",0)],itp_type_foot_armor|itp_unique,0,1,weight(250)|head_armor(0)|body_armor(0)|leg_armor(60)|difficulty(70),0],
["green_ent_hands","Ent_Hands",[("green_ent_hand_L",0)],itp_type_hand_armor|itp_unique,0,1,weight(250)|body_armor(1)|difficulty(70),0],


["tree_trunk_invis", "Tree_Trunk", [("toumingshou",0)], itp_can_knock_down|itp_crush_through|itp_type_one_handed_wpn|itp_primary|itp_wooden_parry|itp_wooden_attack|itp_unbalanced|itp_unique|itp_no_pick_up_from_ground, itc_gauntlet,101 , weight(250)|difficulty(20)|spd_rtng(87)| weapon_length(186)|swing_damage(50, blunt)| thrust_damage(50 ,  blunt),imodbits_mace, [], [fac_elf]],
["tree_trunk_invis_2", "Tree_Trunk", [("toumingshou",0)], itp_can_knock_down|itp_crush_through|itp_type_one_handed_wpn|itp_primary|itp_wooden_parry|itp_wooden_attack|itp_unique|itp_no_pick_up_from_ground, itc_gauntlet,101 , weight(250)|difficulty(20)|spd_rtng(120)| weapon_length(186)|swing_damage(50, blunt)| thrust_damage(50 ,  blunt),imodbits_mace, [], [fac_elf]],

["troll_stones", "Stones", [("stone_ball",0)], itp_merchandise|itp_type_thrown|itp_crush_through|itp_primary ,itcf_throw_stone, 1 , weight(4)|difficulty(5)|spd_rtng(97)| shoot_speed(90)| thrust_damage(50 ,  blunt)|max_ammo(18)|weapon_length(25),imodbits_thrown_2,[(ti_on_missile_hit, [(store_trigger_param_1, ":shooter"),(copy_position,pos51,pos1),(call_script, "script_magic_deliver_area_damage", ":shooter", 210, 4, 2),]),]+missile_distance_trigger, [fac_orc]],

["troll_feet_boots", "Troll_Feet", [("troll_feet", 0)], itp_type_foot_armor|itp_unique|itp_civilian, 0, 4000, weight(58)|abundance(100)|head_armor(0)|body_armor(55)|leg_armor(55)|difficulty(70), imodbits_cloth ],

["troll_head_helm_1", "troll_Head", [("troll_head", 0)], itp_type_fullhelm|itp_unique, 0, 4000, weight(10)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(70), imodbits_cloth ],




["tree_trunk_club", "Tree_Trunk", [("troll_club",0)], itp_can_knock_down|itp_crush_through|itp_type_one_handed_wpn|itp_primary|itp_wooden_parry|itp_wooden_attack|itp_unbalanced|itp_unique|itp_no_pick_up_from_ground, itc_gauntlet,101 , weight(7)|difficulty(50)|spd_rtng(87)| weapon_length(186)|swing_damage(50, blunt)| thrust_damage(50 ,  blunt),imodbits_mace, [], [fac_orc]],


["olog_feet_boots", "Olog_Hai_Feet", [("olog_feet", 0)], itp_type_foot_armor|itp_unique|itp_civilian, 0, 4000, weight(30)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(100)|difficulty(70), imodbits_cloth ],

["olog_head_helm_1", "Olog_Hai_Head", [("olog_head", 0)], itp_type_fullhelm|itp_unique, 0, 4000, weight(30)|abundance(100)|head_armor(130)|body_armor(0)|leg_armor(0)|difficulty(70), imodbits_cloth ],



["olog_body_1", "Olog_Hai_Armor", [("olog_body", 0)], itp_type_body_armor|itp_unique|itp_covers_legs|itp_civilian, 0, 4000, weight(40)|abundance(100)|head_armor(0)|body_armor(100)|leg_armor(0)|difficulty(70), imodbits_cloth ],
["olog_body_2", "Olog_Hai_Armor", [("olog_body_b", 0)], itp_type_body_armor|itp_unique|itp_covers_legs|itp_civilian, 0, 4000, weight(40)|abundance(100)|head_armor(0)|body_armor(100)|leg_armor(0)|difficulty(70), imodbits_cloth ],

["olog_hands","Olog_Hai_Hands", [("olog_hand_L",0)], itp_type_hand_armor|itp_civilian|itp_unique,0, 
 50, weight(0)|abundance(100)|body_armor(10)|difficulty(70),imodbits_cloth, ],


["giant_hammer", "Giant_Hammer", [("giant_hammer",0)], itp_can_knock_down|itp_crush_through|itp_type_one_handed_wpn|itp_primary|itp_wooden_parry|itp_wooden_attack|itp_unbalanced|itp_unique|itp_no_pick_up_from_ground, itc_gauntlet,101 , weight(7)|difficulty(40)|spd_rtng(96)| weapon_length(150)|swing_damage(55, blunt)| thrust_damage(82 ,  blunt),imodbits_mace, [(ti_on_weapon_attack, [(store_trigger_param_1, ":shooter"),(agent_get_horse,":horse",":shooter"),(neg|gt,":horse",0),(copy_position,pos51,pos1),(call_script,"script_cf_agent_cleave",":shooter", 1, 0),])], [fac_orc]],

["giant_mace", "Giant_Mace", [("giant_mace",0)], itp_can_knock_down|itp_crush_through|itp_type_one_handed_wpn|itp_primary|itp_wooden_parry|itp_wooden_attack|itp_unbalanced|itp_unique|itp_no_pick_up_from_ground, itc_gauntlet,101 , weight(7)|difficulty(40)|spd_rtng(96)| weapon_length(150)|swing_damage(60, blunt)| thrust_damage(92 ,  blunt),imodbits_mace, [(ti_on_weapon_attack, [(store_trigger_param_1, ":shooter"),(agent_get_horse,":horse",":shooter"),(neg|gt,":horse",0),(copy_position,pos51,pos1),(call_script,"script_cf_agent_cleave",":shooter", 1, 0),])], [fac_orc]],

  
["dwarf_plate_armor", "Plate Armor", [("plate_and_kilt",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0, 10868,full_plate_armor_tier_3,imodbits_good_plate , [], [fac_kingdom_10]],

["dwarf_knight_plate", "Plate Armor", [("plate_and_kilt_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 12769,full_plate_armor_tier_4 ,imodbits_good_plate , [], [fac_kingdom_10]],

["dwarf_maul",         "Maul", [("stonemaul",0)], itp_merchandise|itp_type_one_handed_wpn|itp_can_knock_down|itp_crush_through| itp_primary|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_spear,97 , weight(6)|difficulty(8)|spd_rtng(83)| weapon_length(85)|swing_damage(40 , blunt)| thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_dwarf]],

["dwarf_maul_2",         "Great Hammer", [("DW_Hammer_2H_T4_01",0)], itp_merchandise|itp_type_one_handed_wpn|itp_can_knock_down|itp_crush_through| itp_primary|itp_unbalanced, itc_nodachi|itcf_carry_spear,97 , weight(6)|difficulty(8)|spd_rtng(83)| weapon_length(120)|swing_damage(45 , blunt)| thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_dwarf]],


["dwarf_maul_3",         "Flame Lord Great Hammer", [("dwtwo_hand_hammer",0)], itp_type_polearm|itp_two_handed|itp_can_knock_down|itp_bonus_against_shield|itp_crush_through| itp_primary|itp_unbalanced|itp_unique|itp_no_pick_up_from_ground, itc_gauntlet,97 , weight(6)|difficulty(12)|spd_rtng(92)| weapon_length(150)|swing_damage(60 , pierce)| thrust_damage(0 ,  pierce),imodbits_mace, [(ti_on_weapon_attack, [(store_trigger_param_1, ":shooter"),(agent_get_horse,":horse",":shooter"),(neg|gt,":horse",0),(copy_position,pos51,pos1),(call_script,"script_cf_agent_cleave",":shooter", 1, 0),])], [fac_dwarf]],


["thunder_staff", "thunder_staff", [("lod_WAoRStaffB",0),("lightning",ixmesh_flying_ammo),], itp_type_thrown|itp_crush_through|itp_primary|itp_next_item_as_melee ,itcf_throw_stone, 1 , weight(4)|difficulty(0)|spd_rtng(35)| shoot_speed(70)| thrust_damage(50 ,  pierce)|max_ammo(10)|weapon_length(25),imodbits_thrown_2,[(ti_on_missile_hit, [(store_trigger_param_1, ":shooter"),(copy_position,pos51,pos1),(call_script, "script_magic_deliver_area_damage", ":shooter", 170, 4, 5),]),]+missile_distance_trigger, [fac_dwarf]],
["thunder_spear",  "thunder_spear", [("lod_WAoRStaffB",0)], itp_type_polearm|itp_wooden_parry| itp_primary, itc_glaive|itcf_carry_spear, 202 , weight(2)|difficulty(0)|spd_rtng(100)| weapon_length(195)|swing_damage(45 , pierce)| thrust_damage(45 ,  pierce),imodbits_axe, [], [fac_commoners, fac_undeads_2]],

["dwarf_thunder_maul","mjolnir", [("Mjolnir",0)], itp_type_thrown|itp_crush_through|itp_primary|itp_next_item_as_melee|itp_unique ,itcf_throw_stone,30000, weight(5)|difficulty(6)|spd_rtng(91)| shoot_speed(70)| thrust_damage(50 ,  blunt)|max_ammo(10)|weapon_length(75),imodbits_thrown,thunder_weapon_trigger+missile_distance_trigger],
["dwarf_thunder_maul_melee","mjolnir", [("Mjolnir",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_crush_through| itp_primary|itp_unbalanced|itp_unique, itc_nodachi|itcf_carry_spear,97 , weight(6)|difficulty(25)|spd_rtng(83)| weapon_length(85)|swing_damage(50 , blunt)| thrust_damage(0 ,  pierce),imodbits_mace, thunder_weapon_trigger_2],



["dwarven_inf_helmet1", "dwarven_inf_helmet", [("dwarven_inf_helmet_t1",0)],  itp_type_head_armor|itp_unique   ,0, 
 5000 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, 
 [], [fac_dwarf]],
["dwarven_inf_helmet2", "dwarven_inf_helmet", [("dwarven_inf_helmet_t2",0)],  itp_type_head_armor|itp_unique ,0, 
 10000 , weight(2.25)|abundance(100)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(15) ,imodbits_plate, 
 [], [fac_dwarf]],
["dwarven_inf_helmet3", "dwarven_inf_helmet", [("dwarven_inf_helmet_t3",0)], itp_type_head_armor|itp_covers_beard|itp_unique, 0, 
 20000 , weight(2.25)|abundance(100)|head_armor(70)|body_armor(0)|leg_armor(0)|difficulty(15) ,imodbits_plate, 
 [], [fac_dwarf]],
["dwarven_inf_helmet4", "dwarven_inf_helmet", [("dwarven_inf_helmet_t4",0)], itp_type_head_armor|itp_covers_beard|itp_unique, 0, 
 20000 , weight(2.25)|abundance(100)|head_armor(90)|body_armor(0)|leg_armor(0)|difficulty(15) ,imodbits_plate,
 [], [fac_dwarf]],

["dwarf_war_pick", "Fighting Pick", [("dwarf_war_pick",0)], itp_type_one_handed_wpn|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,216 , weight(3.5)|difficulty(0)|spd_rtng(96)| weapon_length(75)|swing_damage(27 , pierce)| thrust_damage(0 ,  pierce),imodbits_pick, [], [fac_dwarf,fac_kingdom_10]], 
["dwarf_pick", "Military Pick", [("dwarf_adz",0)], itp_type_one_handed_wpn|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,560 , weight(4)|difficulty(0)|spd_rtng(92)| weapon_length(65)|swing_damage(28 , pierce)| thrust_damage(0 ,  pierce),imodbits_pick, [], [fac_dwarf,fac_kingdom_10]], 
["dwarf_great_pick", "Military Pick", [("dwarf_great_pick",0)], itp_type_two_handed_wpn|itp_primary|itp_wooden_parry, itc_morningstar|itcf_carry_mace_left_hip,890 , weight(4)|difficulty(0)|spd_rtng(90)| weapon_length(90)|swing_damage(33 , pierce)| thrust_damage(0 ,  pierce),imodbits_pick, [], [fac_dwarf,fac_kingdom_10]], 

["dwarf_one_handed_hammer", "Dwarven_One_Handed_Hammer", [("DW_Hammer_1H_T2_02", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_bonus_against_shield|itp_can_knock_down, itc_scimitar|itcf_carry_mace_left_hip, 87, weight(3)|abundance(100)|difficulty(0)|weapon_length(55)|spd_rtng(93)|swing_damage(35, blunt)|thrust_damage(0, pierce), imodbits_axe, [], [fac_dwarf,fac_kingdom_10]], 
["dwarf_one_handed_hammer2", "Dwarven_One_Handed_Hammer", [("DW_Hammer_1H_T4_01", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_bonus_against_shield|itp_can_knock_down, itc_scimitar|itcf_carry_mace_left_hip, 117, weight(3)|abundance(100)|difficulty(0)|weapon_length(60)|spd_rtng(92)|swing_damage(40, blunt)|thrust_damage(0, pierce), imodbits_axe, [], [fac_dwarf,fac_kingdom_10]], 
["dwarf_one_handed_hammer3", "Dwarven_One_Handed_Hammer", [("DW_Hammer_1H_TE_03", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_bonus_against_shield|itp_can_knock_down, itc_scimitar|itcf_carry_mace_left_hip, 137, weight(3.5)|abundance(100)|difficulty(0)|weapon_length(60)|spd_rtng(90)|swing_damage(45, blunt)|thrust_damage(0, pierce), imodbits_axe, [], [fac_dwarf,fac_kingdom_10]], 

["dwarf_warhammer", "Dwarven_Warhammer", [("stonemaul", 0)], itp_can_knock_down|itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear, 550, weight(10)|difficulty(14)|spd_rtng(83)|weapon_length(85)|swing_damage(46, blunt)|thrust_damage(0, pierce), imodbits_mace, [], [fac_dwarf,fac_kingdom_10]], 
["dwarf_warhammer2", "Dwarven_Warhammer", [("DW_Hammer_2H_T4_01", 0)], itp_can_knock_down|itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear, 550, weight(10)|difficulty(14)|spd_rtng(82)|weapon_length(98)|swing_damage(50, blunt)|thrust_damage(0, pierce), imodbits_mace, [], [fac_dwarf,fac_kingdom_10]], 
["dwarf_warhammer3", "Dwarven_Warhammer", [("dwtwo_hand_hammer", 0)], itp_can_knock_down|itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear, 550, weight(10)|difficulty(14)|spd_rtng(80)|weapon_length(93)|swing_damage(55, blunt)|thrust_damage(0, pierce), imodbits_mace, [], [fac_dwarf,fac_kingdom_10]], 
["dwarf_warhammer4", "Dwarven_Warhammer", [("dwtwo_hand_hammer", 0)], itp_can_knock_down|itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear, 30000, weight(10)|difficulty(14)|spd_rtng(80)|weapon_length(100)|swing_damage(60, blunt)|thrust_damage(0, pierce), imodbits_mace, [], [fac_dwarf,fac_kingdom_10]], 

["drawf_musket", "Musket", [("granatnik_a",0)], itp_merchandise|itp_type_musket|itp_crush_through|itp_cant_reload_on_horseback|itp_two_handed|itp_primary, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 1160, weight(7.5)|difficulty(0)|spd_rtng(29)|shoot_speed(150)|abundance(31)|thrust_damage(90 ,pierce)|max_ammo(1)|accuracy(90), imodbits_gun, musket_trigger , [fac_dwarf]], 


["dwarf_pistol_1", "Dwarf_Pistol", [("DW_Pistol_1H_T1_02",0)], itp_type_pistol|itp_merchandise|itp_primary ,itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_pistol_front_left, 
 2250 , weight(2.0)|difficulty(0)|spd_rtng(50) | shoot_speed(100) | thrust_damage(90 ,pierce)|max_ammo(1)|accuracy(80),imodbits_gun, pistol_trigger , [fac_dwarf] ],
 
["dwarf_pistol_2", "Dwarf_3_Barrel_Barrelled_Pistol", [("DW_Handgun_1H_TE_01",0)], itp_type_pistol|itp_merchandise|itp_primary ,itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_pistol_front_left,
 3600 , weight(2.5)|difficulty(0)|spd_rtng(35) | shoot_speed(110) | thrust_damage(85 ,pierce)|max_ammo(3)|accuracy(75),imodbits_gun, pistol_trigger , [fac_dwarf] ],
  
["dwarf_pistol_3", "Dwarf_Hand_Cannon", [("DW_handcannon",0)], itp_type_pistol|itp_merchandise|itp_primary ,itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_pistol_front_left,
 20000 , weight(2.25)|difficulty(0)|spd_rtng(30) | shoot_speed(80) | thrust_damage(90 ,pierce)|max_ammo(1)|accuracy(60),imodbits_gun, [(ti_on_weapon_attack, [
  (store_trigger_param_1,":agent_id"),
  (eq,":agent_id",":agent_id"),  
  (agent_get_wielded_item, ":weapon", ":agent_id", 0),
  (gt, ":weapon", 0),
    
  (copy_position,pos22,pos1),
  (position_move_y,pos22,110),
  (try_for_range,":unused",0,5), #3 extra bullets + 1 original = 5 bullets in one shot :D
  
    (copy_position,pos23,pos22),
    (store_random_in_range,":x_change",-15,16),
    (store_random_in_range,":z_change",-15,16),
    (position_rotate_x, pos23, ":x_change"),
    (position_rotate_z, pos23, ":z_change"),
    (set_fixed_point_multiplier,100),
    (store_random_in_range,":bullet_speed",8000,12000),
    (add_missile, ":agent_id", pos23, ":bullet_speed", ":weapon", 0, "itm_cartridges_dummy", 0),
  (try_end),])]+pistol_trigger , [fac_dwarf]],




["drawf_musket_1", "Dwarf_Musket", [("dw_rifle_t2_03",0)], itp_merchandise|itp_type_musket|itp_crush_through|itp_cant_reload_on_horseback|itp_two_handed|itp_primary, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 2325, weight(7.5)|difficulty(0)|spd_rtng(25)|shoot_speed(150)|abundance(31)|thrust_damage(100 ,pierce)|max_ammo(1)|accuracy(90), imodbits_gun, musket_trigger , [fac_kingdom_10]], 
["drawf_musket_2", "Dwarf_Musket", [("dwarfhandgun2h02",0)], itp_merchandise|itp_type_musket|itp_crush_through|itp_cant_reload_on_horseback|itp_two_handed|itp_primary, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 2325, weight(7.5)|difficulty(0)|spd_rtng(33)|shoot_speed(100)|abundance(31)|thrust_damage(120 ,pierce)|max_ammo(1)|accuracy(85), imodbits_gun, musket_trigger , [fac_kingdom_10]], 

["drawf_musket_3", "Dwarf_Musket", [("DW_Handgun_2H_T2_02",0)], itp_merchandise|itp_type_musket|itp_crush_through|itp_cant_reload_on_horseback|itp_two_handed|itp_primary, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 5000, weight(7.5)|difficulty(0)|spd_rtng(29)|shoot_speed(140)|abundance(31)|thrust_damage(90 ,pierce)|max_ammo(2)|accuracy(90), imodbits_gun, musket_trigger , [fac_dwarf]], 


["drawf_heavy_musket_1", "Rune_Musket_of_Reloading", [("DW_Rifle_2H_T3_01",0)], itp_type_musket|itp_two_handed|itp_crush_through|itp_primary|itp_bonus_against_shield|itp_cant_reload_on_horseback, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 10000, weight(7.5)|difficulty(0)|spd_rtng(25)|shoot_speed(150)|thrust_damage(150,pierce)|max_ammo(2)|accuracy(100), imodbits_gun, musket_trigger , [fac_dwarf]],
["drawf_heavy_musket_2", "Dwarven_Two_Barrel", [("DW_Handgun_2H_TE_03",0)], itp_type_musket|itp_two_handed|itp_crush_through|itp_primary|itp_bonus_against_shield|itp_cant_reload_on_horseback, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 14000, weight(7.5)|difficulty(0)|spd_rtng(25)|shoot_speed(130)|thrust_damage(120,pierce)|max_ammo(2)|accuracy(70), imodbits_gun, musket_trigger , [fac_dwarf]],
["drawf_heavy_musket_3", "Dwarven_Three_Barrel", [("DW_Handgun_2H_TE_02",0)], itp_type_musket|itp_two_handed|itp_crush_through|itp_primary|itp_bonus_against_shield|itp_cant_reload_on_horseback, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 21000, weight(7.5)|difficulty(0)|spd_rtng(25)|shoot_speed(130)|thrust_damage(120,pierce)|max_ammo(3)|accuracy(70), imodbits_gun, musket_trigger , [fac_dwarf]],


["drawf_musket", "Musket", [("granatnik_a",0)], itp_merchandise|itp_type_musket|itp_crush_through|itp_cant_reload_on_horseback|itp_two_handed|itp_primary, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 1160, weight(7.5)|difficulty(0)|spd_rtng(29)|shoot_speed(150)|abundance(31)|thrust_damage(90 ,pierce)|max_ammo(1)|accuracy(90), imodbits_gun, musket_trigger , [fac_dwarf]], 

["drawf_heavy_musket", "Musket", [("garlacz_a",0)], itp_merchandise|itp_type_musket|itp_crush_through|itp_primary|itp_cant_reload_on_horseback, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 2250, weight(7.5)|difficulty(0)|spd_rtng(25)|shoot_speed(100)|thrust_damage(120,pierce)|max_ammo(1)|accuracy(70), imodbits_gun, musket_trigger , [fac_dwarf]],

["drawf_flame_caster", "Musket", [("garlacz_a",0)], itp_merchandise|itp_type_musket|itp_crush_through|itp_primary|itp_cant_reload_on_horseback, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 2250, weight(7.5)|difficulty(0)|spd_rtng(45)|shoot_speed(70)|thrust_damage(100,pierce)|max_ammo(4)|accuracy(85), imodbits_gun, flame_cast_trigger , [fac_dwarf]],

 ["cartridges_flame", "Cartridges", [("minie_ball",0),("musket_balls",ixmesh_flying_ammo),("bag_ppa1",ixmesh_carry)], itp_type_bullets|itp_merchandise|itp_can_penetrate_shield|itp_bonus_against_shield|itp_covers_legs, itcf_carry_bow_back,
  20000, weight(2.25)|abundance(30)|weapon_length(3)|thrust_damage(55,pierce)|max_ammo(6), 
  imodbits_missile, missile_distance_trigger , [fac_dwarf]
 ],

["drawf_musket_8barrel1", "Musket", [("gatling",0)], itp_merchandise|itp_type_musket|itp_crush_through|itp_two_handed|itp_primary|itp_cant_reload_on_horseback, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 10000, weight(10)|difficulty(0)|spd_rtng(55)|shoot_speed(140)|thrust_damage(110,pierce)|max_ammo(30)|accuracy(90), imodbits_gun, musket_trigger , [fac_dwarf]],

#["drawf_musket_8barrel2", "Musket", [("rifle_8barrel",0)], itp_merchandise|itp_type_musket|itp_crush_through|itp_two_handed|itp_primary|itp_cant_reload_on_horseback, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 10000, weight(10)|difficulty(0)|spd_rtng(27)|shoot_speed(160)|thrust_damage(100,pierce)|max_ammo(7)|accuracy(95), imodbits_gun, musket_trigger , firearm_factions],




["drawf_musket_8barrel2", "Dwarf_Grenade_Launcher", [("DW_grenade_launcher",0)], itp_merchandise|itp_type_musket|itp_crush_through|itp_two_handed|itp_primary|itp_cant_reload_on_horseback, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 14000, weight(10)|difficulty(0)|spd_rtng(27)|shoot_speed(160)|thrust_damage(100,pierce)|max_ammo(1)|accuracy(90), imodbits_gun, [(ti_on_weapon_attack, [
  (store_trigger_param_1,":agent_id"),
  (eq,":agent_id",":agent_id"),  
  (agent_get_wielded_item, ":weapon", ":agent_id", 0),
  (gt, ":weapon", 0),
  
  (copy_position,pos22,pos1),
  (position_move_y,pos22,110),
  (try_for_range,":unused",0,10), #3 extra bullets + 1 original = 5 bullets in one shot :D
  
    (copy_position,pos23,pos22),
    (store_random_in_range,":x_change",-7,8),
    (store_random_in_range,":z_change",-10,11),
    (position_rotate_x, pos23, ":x_change"),
    (position_rotate_z, pos23, ":z_change"),
    (set_fixed_point_multiplier,100),
    (store_random_in_range,":bullet_speed",16000,24000),
    (add_missile, ":agent_id", pos23, ":bullet_speed", ":weapon", 0, "itm_cartridges_dummy", 0),
  (try_end),])]+musket_trigger , [fac_dwarf]],




["dwarf_miner_helm", "dwarf_miner_helm", [("DwarfHelmMiner",0)], itp_type_head_armor, 0, 
 600 , weight(2)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,[], [fac_dwarf] ],

["dwarf_mail_coif", "Mail Coif", [("DwarfHelmCoif",0)],  itp_type_head_armor   ,0, 
 1350 , weight(1.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_armor ,[], [fac_dwarf] ],
["dwarf_mail_coif_mask_1", "Footman's Helmet", [("DwarfHelmCoifMask",0)], itp_type_head_armor|itp_covers_beard   ,0, 
 1666 , weight(1.5)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ,[], [fac_dwarf] ],
["dwarf_mail_coif_mask_2", "Footman's Helmet", [("DwarfHelmCoifMask_B",0)], itp_type_head_armor|itp_covers_beard   ,0, 
 1666 , weight(1.5)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ,[], [fac_dwarf] ],

["dwarf_helm", "Guard Helmet", [("DwarfHelmFrisianChain",0)], itp_type_head_armor   ,0, 
 2016 , weight(1.5)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,[], [fac_dwarf]  ],
["dwarf_helm_mask_1", "Guard Helmet", [("DwarfHelmFrisianMask_A", 0)], itp_type_head_armor|itp_covers_beard, 0, 
 2400 , weight(1.75)|abundance(100)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[], [fac_dwarf] ],
["dwarf_helm_mask_2", "Guard Helmet", [("DwarfHelmFrisianMask_B", 0)], itp_type_head_armor|itp_covers_beard, 0, 
 2400 , weight(1.75)|abundance(100)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[], [fac_dwarf] ],

["dwarf_sallet_coif", "sallet_coif", [("DwarfHelmSalletChain",0)], itp_type_head_armor, 0, 
 2816 , weight(2.5)|abundance(100)|head_armor(65)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate,[], [fac_dwarf]],
 
["dwarf_sallet_coif_mask", "sallet_coif", [("DwarfHelmSalletSargeant",0)], itp_type_head_armor|itp_covers_beard, 0, 
 3750 , weight(2.5)|abundance(100)|head_armor(75)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate,[], [fac_dwarf]],

["dwarf_great_helmet_1", "Great Helmet", [("DwarfHelmIronheadFace",0)],  itp_type_head_armor|itp_covers_beard,0, 
 4266 , weight(2.75)|abundance(100)|head_armor(80)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate,[], [fac_dwarf] ],
["dwarf_great_helmet_2", "Great Helmet", [("DwarfHelmIronheadNasal",0)], itp_type_head_armor|itp_covers_beard,0, 
 4266 , weight(2.75)|abundance(100)|head_armor(80)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate,[], [fac_dwarf] ],

["dwarf_kingcrown", "new_sallet", [("DwarfHelmKingCrown",0)], itp_type_head_armor|itp_covers_beard, 0, 
 5400 , weight(2.75)|abundance(100)|head_armor(90)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate,[], [fac_dwarf] ],


["dwarf_padmail", "dwarf_padmail", [("dwarf_padmail",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 
3451,lamellar_armor_tier_1,imodbits_armor,[], [fac_dwarf]],
["dwarf_tunicmail", "dwarf_tunicmail", [("dwarf_tunicmailarcher",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian ,0,
6360,lamellar_armor_tier_2,imodbits_armor,[], [fac_dwarf]],
["dwarf_scalemail", "dwarven_scalemail", [("dwarf_scalemail",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 
10868,full_plate_armor_tier_4,imodbits_armor,[], [fac_dwarf]],

["dwarf_tunicmail_2", "dwarf_tunicmailarcher", [("dwarven_paddedlongcoat",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 
6360,lamellar_armor_tier_2,imodbits_armor,[], [fac_dwarf]],
["dwarven_tunicovermail", "dwarven_tunicovermail", [("annihilator_coat",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 
7876,lamellar_armor_tier_3,imodbits_armor,[], [fac_dwarf]],
["dwarven_scalemail", "dwarven_scalemail", [("dwarven_scalemail",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 
10868,full_plate_armor_tier_4,imodbits_armor,[], [fac_dwarf]],

["dwarf_chain_boots", "Mail Boots", [("dwarf_chain_boots",0)],  itp_type_foot_armor| itp_attach_armature  ,0, 
 2016 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(7) ,imodbits_armor,[], [fac_dwarf] ],
["dwarf_scale_boots", "scale Greaves", [("dwarf_scale_boots",0)],  itp_type_foot_armor| itp_attach_armature,0, 
 2592 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(36)|difficulty(8) ,imodbits_plate ,[], [fac_dwarf] ],




["skeleton_body_1", "skeleton", [("barf_skeleton",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_unique ,0, 950,weight(1)|abundance(50)|head_armor(0)|body_armor(25)|leg_armor(10)|difficulty(1),imodbits_armor ],
["skeleton_body_2", "skeleton", [("barf_skeleton_armor",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_unique ,0, 6360,mail_armor_tier_2,imodbits_armor ],
["skeleton_body_3", "skeleton", [("barf_skeleton_armor_1",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_unique ,0, 4035,mail_armor_tier_3,imodbits_armor ],
["skeleton_body_4", "skeleton", [("barf_skeleton_armor_2",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_unique ,0, 5256,mail_armor_tier_4,imodbits_armor ],
["skeleton_body_5", "skeleton", [("barf_skeleton_armor_3",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_unique ,0, 6360,mail_armor_tier_5,imodbits_armor ],


["mummy_body", "mummy_body", [("mummy_body",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_unique ,0, 6360,lamellar_armor_tier_2,imodbits_armor ],
["mummy_calf", "mummy_calf", [("mummy_calf_L",0)], itp_type_foot_armor|itp_civilian|itp_unique ,0, 
 2376 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(0) ,imodbits_cloth,],
["mummy_hand","mummy_hand", [("mummy_handL",0)], itp_type_hand_armor|itp_unique,0, 
 820, weight(1)|abundance(100)|body_armor(9)|difficulty(0),imodbits_armor, ],

["mummyhead", "mummyhead", [("mummyhead",0)],  itp_type_fullhelm|itp_unique  ,300, 
 600 , weight(2)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, ],
["tomb_knighthelm", "tomb_knighthelm", [("tomb_knighthelm",0)], itp_type_fullhelm|itp_unique   ,500, 
 1666 , weight(2.5)|abundance(100)|head_armor(50)|body_armor(20)|leg_armor(0)|difficulty(7) ,imodbits_plate, ],
["tomb_knightfull", "tomb_knightfull", [("tomb_knightfull",0)], itp_type_fullhelm|itp_unique ,800, 
 2400 , weight(3)|abundance(100)|head_armor(60)|body_armor(30)|leg_armor(0)|difficulty(7) ,imodbits_plate, ],
 
["tomb_king_helmet", "tomb_king_helmet", [("tomb_king_helmet",0)], itp_type_fullhelm|itp_unique  ,10000, 
 3266 , weight(3.5)|abundance(100)|head_armor(70)|body_armor(20)|leg_armor(0)|difficulty(7) ,imodbits_plate, ],

["tomb_shield", "tomb_shield", [("tomb_shieldthree",0)], itp_type_shield|itp_wooden_parry|itp_cant_use_on_horseback, itcf_carry_board_shield, 1110, weight(5)|shield_hit_points(196)|body_armor(66)|spd_rtng(78)|shield_width(43)|shield_height(100), imodbits_shield, ],

["tomb_sword", "tomb_sword", [("tombsword",0)], itp_type_one_handed_wpn| itp_primary, itc_bastardsword, 957 , weight(2.25)|difficulty(9)|spd_rtng(98)| weapon_length(105)|swing_damage(42 , cut)| thrust_damage(27 ,  pierce),imodbits_sword_high],

["dummy_weapon_2_hand",         "Maul", [("toumingshou",0)], itp_can_knock_down|itp_crush_through|itp_type_two_handed_wpn| itp_primary|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi,97 , weight(6)|difficulty(8)|spd_rtng(87)| weapon_length(45)|swing_damage(36 , blunt)| thrust_damage(0 ,  pierce),imodbits_mace],

["ushabti_body", "Anubis", [("ushabti", 0)], itp_type_body_armor|itp_unique|itp_covers_legs|itp_civilian|itp_covers_head, 0, 2000, weight(30.)|abundance(100)|difficulty(15)|head_armor(80)|body_armor(80)|leg_armor(80), imodbits_armor], 
["weak_ushabti_body", "Anubis_servant", [("ushabtiservant", 0)], itp_type_body_armor|itp_unique|itp_covers_legs|itp_civilian|itp_covers_head, 0, 2000, weight(30.)|abundance(100)|difficulty(15)|head_armor(80)|body_armor(65)|leg_armor(60), imodbits_armor], 

["ushabti_hands", "Anubis_Hands", [("ushabti_handL", 0)], itp_type_hand_armor|itp_unique|itp_civilian, 0, 900, weight(1.)|abundance(150)|difficulty(20)|head_armor(0)|body_armor(10)|leg_armor(0), imodbits_none], 

["tomb_axe", "Tomb_Axe", [("tombaxe1",0)], itp_type_two_handed_wpn| itp_primary|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield, itc_nodachi|itcf_carry_axe_back, 957 , weight(2.25)|difficulty(12)|spd_rtng(88)| weapon_length(96)|swing_damage(47 , pierce)| thrust_damage(0 ,  pierce),imodbits_sword_high],
["tomb_axe2", "Anubis_Axe", [("tombaxe2",0)], itp_type_two_handed_wpn| itp_primary|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield, itc_nodachi|itcf_carry_axe_back, 957 , weight(2.25)|difficulty(15)|spd_rtng(88)| weapon_length(159)|swing_damage(57 , pierce)| thrust_damage(0 ,  pierce),imodbits_sword_high],
["destroyer", "Destroyer_Of_Eternities", [("tombeternities", 0)], itp_type_two_handed_wpn|itp_unique|itp_primary, itc_greatsword|itcf_carry_sword_back, 50000, weight(2.50)|abundance(100)|difficulty(21)|weapon_length(130)|spd_rtng(96)|swing_damage(70, pierce)|thrust_damage(40, pierce), imodbits_sword_high], 



 ["magic_summon_neutral_near_ememy", "cast_magic_summon_neutral", [("bullet_1",0),("laser_bolt_green",ixmesh_flying_ammo),("icon_magic_summon_neutral", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  5000, weight(2.25)|abundance(15)|weapon_length(4)|thrust_damage(10,cut)|max_ammo(3),
  imodbits_none, cast_magic_summon_neutral+missile_distance_trigger , [fac_commoners, fac_demon_hunters, fac_hospitalier_knights , fac_undeads_2, fac_kingdom_1] ],

 ["magic_summon_demon", "summon_demon_Scroll", [("bullet_1",0),("laser_bolt_red",ixmesh_flying_ammo),("magic_3_icon", ixmesh_inventory)], itp_merchandise|itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  9000, weight(2.25)|abundance(10)|weapon_length(3)|thrust_damage(5,cut)|max_ammo(3),
  imodbits_none, missile_distance_trigger , [fac_undeads_2, fac_commoners] ],
 ["magic_summon_demon_near_ememy", "summon_demon_Scroll", [("bullet_1",0),("laser_bolt_red",ixmesh_flying_ammo),("magic_3_icon", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  9000, weight(2.25)|abundance(10)|weapon_length(3)|thrust_damage(10,cut)|max_ammo(2),
  imodbits_none, cast_magic_summon_demon , [fac_undeads_2, fac_commoners] ],

 ["magic_heal", "heal_Scroll", [("bullet_1",0),("laser_bolt_orange",ixmesh_flying_ammo),("magic_4_icon", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  1000, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(10,cut)|max_ammo(15),
  imodbits_none, cast_magic_heal+missile_distance_trigger , [fac_demon_hunters, fac_hospitalier_knights, fac_hospitalier_knights] ],

 ["magic_heal_near", "heal_Scroll", [("bullet_1",0),("laser_bolt_orange",ixmesh_flying_ammo),("magic_20_icon", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  1000, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(10,cut)|max_ammo(15),
  imodbits_none, missile_distance_trigger , [fac_demon_hunters, fac_hospitalier_knights] ],

 ["magic_summon_undead", "summon_undead_Scroll", [("bullet_1",0),("laser_bolt_green",ixmesh_flying_ammo),("icon_magic_summon_undead", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  6000, weight(2.25)|abundance(15)|weapon_length(3)|thrust_damage(5,cut)|max_ammo(6),
  imodbits_none, cast_magic_basic_curse+missile_distance_trigger , [fac_undeads_2] ],
 ["magic_summon_undead_near_ememy", "cast_magic_summon_undeadl", [("bullet_1",0),("laser_bolt_green",ixmesh_flying_ammo),("icon_magic_summon_undead", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  6000, weight(2.25)|abundance(15)|weapon_length(4)|thrust_damage(10,cut)|max_ammo(4),
  imodbits_none, cast_magic_basic_curse+cast_magic_summon_undead+missile_distance_trigger , [fac_undeads_2] ],

 ["magic_soulhunter", "Soulhunter", [("bullet_1",0),("laser_bolt_yellow",ixmesh_flying_ammo),("icon_magic_Soulhunter", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  15000, weight(2.25)|abundance(45)|weapon_length(3)|thrust_damage(5,cut)|max_ammo(2),
  imodbits_none, cast_magic_basic_curse+cast_magic_summon_Soulhunter+missile_distance_trigger , [fac_undeads_2] ],
 ["magic_zombie_lord", "Zombie_Lord", [("bullet_1",0),("laser_bolt_yellow",ixmesh_flying_ammo),("icon_magic_Zombie_Lord", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  15000, weight(2.25)|abundance(45)|weapon_length(3)|thrust_damage(5,cut)|max_ammo(2),
  imodbits_none, cast_magic_basic_curse+cast_magic_summon_Zombie_Lord+missile_distance_trigger , [fac_undeads_2] ],

 ["magic_curse", "curse_Scroll", [("bullet_1",0),("laser_bolt_red",ixmesh_flying_ammo),("icon_magic_curse", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  1500, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(10,cut)|max_ammo(30),
  imodbits_none, cast_magic_curse+missile_distance_trigger , [fac_commoners, fac_kingdom_5, fac_commoners] ],
 ["magic_slow", "slow_Scroll", [("bullet_1",0),("laser_bolt_red",ixmesh_flying_ammo),("icon_magic_Slow", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  1500, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(10,cut)|max_ammo(30),
  imodbits_none, cast_magic_Slow+missile_distance_trigger , [fac_commoners, fac_kingdom_5, fac_commoners] ],
 ["magic_weakness", "weakness_Scroll", [("bullet_1",0),("laser_bolt_red",ixmesh_flying_ammo),("icon_magic_Weakness", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  2500, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(10,cut)|max_ammo(20),
  imodbits_none, cast_magic_weakness+missile_distance_trigger , [fac_commoners, fac_kingdom_5, fac_commoners] ],

 ["magic_poison", "poison_Scroll", [("bullet_1",0),("laser_bolt_green",ixmesh_flying_ammo),("magic_7_icon", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  2500, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(20,cut)|max_ammo(20),
  imodbits_none, cast_magic_poison+missile_distance_trigger , [fac_commoners, fac_undeads_2] ],
 ["magic_death_cloud_dummy", "death_cloud Scroll", [("bullet_1",0),("magic_7_icon", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  5000, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(35,cut)|max_ammo(10),
  imodbits_none, cast_magic_death_cloud_2  , [fac_commoners, fac_undeads_2] ],
 ["magic_death_cloud", "death_cloud_Scroll", [("bullet_1",0),("laser_bolt_green",ixmesh_flying_ammo),("icon_magic_death_cloud", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  17500, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(70,cut)|max_ammo(4),
  imodbits_none, cast_magic_death_cloud+missile_distance_trigger , [fac_undeads_2] ],
 ["magic_soul_leech", "soul_Leech_Scroll", [("bullet_1",0),("laser_bolt_red",ixmesh_flying_ammo),("icon_magic_soul_Leech", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  17500, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(100,cut)|max_ammo(8),
  imodbits_none, cast_magic_soul_Leech+missile_distance_trigger , [fac_commoners, fac_kingdom_5, fac_commoners] ],

 ["magic_ice_ray", "ice_ray_Scroll", [("bullet_1",0),("guangjian_fly2",ixmesh_flying_ammo),("icon_magic_IceBolt", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  1500, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(25,cut)|max_ammo(30),
  imodbits_none, cast_magic_ice_ray+missile_distance_trigger , [fac_commoners, fac_kingdom_5] ],

 ["magic_deep_freeze", "deep_freeze_Scroll", [("bullet_1",0),("guangjian_fly2",ixmesh_flying_ammo),("magic_19_icon", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  2750, weight(2.25)|abundance(40)|weapon_length(3)|thrust_damage(80,cut)|max_ammo(6),
  imodbits_missile, cast_magic_deep_freeze+missile_distance_trigger , [fac_commoners] ],

 ["magic_frost_cloud", "deep_freeze_Scroll", [("bullet_1",0),("guangjian_fly2",ixmesh_flying_ammo),("icon_magic_Frost_cloudr", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  7500, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(70,cut)|max_ammo(4),
  imodbits_missile, cast_magic_Frost_cloud+missile_distance_trigger , [fac_commoners] ],
 ["magic_frost_cloud_dummy", "deep_freeze_Scroll", [("bullet_1",0),("guangjian_fly2",ixmesh_flying_ammo),("icon_magic_Frost_cloudr", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  2750, weight(2.25)|abundance(40)|weapon_length(3)|thrust_damage(70,cut)|max_ammo(15),
  imodbits_missile, cast_magic_Frost_cloudr+missile_distance_trigger , [fac_undeads_2, fac_commoners] ],

 ["magic_deadly_cold", "DEADLY_COLD_Scroll", [("bullet_1",0),("guangjian_fly2",ixmesh_flying_ammo),("icon_magic_DEADLY_COLD", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  15000, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(100,cut)|max_ammo(6),
  imodbits_none, cast_magic_DEADLY_COLD+missile_distance_trigger , [fac_undeads_2, fac_kingdom_7] ],

 ["magic_frozen_orb", "frozen_orb_Scroll", [("bullet_1",0),("guangjian_fly2",ixmesh_flying_ammo),("icon_magic_frozen_orb", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  15000, weight(2.25)|abundance(10)|weapon_length(3)|thrust_damage(100,cut)|max_ammo(5),
  imodbits_none, cast_magic_frozen_orb+missile_distance_trigger , [fac_undeads_2] ],
 ["magic_blizzard", "blizzard_Scroll", [("bullet_1",0),("guangjian_fly2",ixmesh_flying_ammo),("icon_magic_Blizzard", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  15000, weight(2.25)|abundance(30)|weapon_length(3)|thrust_damage(100,cut)|max_ammo(7),
  imodbits_none, cast_magic_blizzard+missile_distance_trigger , [ fac_undeads_2] ],
  
  


 ["magic_paralysis_cloud", "paralysis_cloud_Scroll", [("bullet_1",0),("laser_bolt_green",ixmesh_flying_ammo),("icon_magic_Petrification", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  7500, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(70,cut)|max_ammo(6),
  imodbits_none, cast_magic_Petrification+missile_distance_trigger , [fac_undeads_2] ],

 ["magic_arrow", "_magic_arrow_Scroll", [("bullet_1",0),("evil_arrow_fl",ixmesh_flying_ammo),("magic_12_icon", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  1000, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(15,cut)|max_ammo(30),
  imodbits_none, [] , [fac_commoners, fac_kingdom_5, fac_commoners] ],

 ["magic_entangling", "Entangling_Scroll", [("bullet_1",0),("laser_bolt_green",ixmesh_flying_ammo),("icon_magic_EntanglingRoots", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  4000, weight(2.25)|abundance(40)|weapon_length(3)|thrust_damage(80,cut)|max_ammo(8),
  imodbits_missile, cast_magic_Entangling+missile_distance_trigger , [fac_commoners] ],
 ["magic_web", "Arcane_web_Scroll", [("bullet_1",0),("flash_arcane_02",ixmesh_flying_ammo),("icon_magic_Web", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  4000, weight(2.25)|abundance(40)|weapon_length(3)|thrust_damage(80,cut)|max_ammo(8),
  imodbits_missile, cast_magic_web+missile_distance_trigger , [fac_commoners] ],
 ["magic_dispel_magic", "Dispel_Magic_Scroll", [("bullet_1",0),("flash_arcane_02",ixmesh_flying_ammo),("icon_magic_Dispel_Magic", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  4000, weight(2.25)|abundance(40)|weapon_length(3)|thrust_damage(80,cut)|max_ammo(8),
  imodbits_missile, cast_magic_Dispel_Magic+missile_distance_trigger , [fac_commoners] ],


 ["magic_spark", "spark_Scroll", [("bullet_1",0),("blitzball",ixmesh_flying_ammo),("icon_magic_thunder", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  1500, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(25,cut)|max_ammo(30),
  imodbits_none, cast_magic_LightningBolt+missile_distance_trigger , [fac_commoners, fac_kingdom_5] ],
 ["magic_lightning", "lightning_Scroll", [("bullet_1",0),("bullet_1",ixmesh_flying_ammo),("icon_magic_LightningBolt", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  2000, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(80,cut)|max_ammo(20),
  imodbits_none, cast_magic_lightning+missile_distance_trigger , [fac_commoners] ],
 ["magic_arcane_orb", "Arcane_Orb_Scroll", [("bullet_1",0),("flash_arcane_02",ixmesh_flying_ammo),("icon_magic_Arcane_Orb", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  4000, weight(2.25)|abundance(40)|weapon_length(3)|thrust_damage(80,cut)|max_ammo(15),
  imodbits_missile, cast_magic_Arcane_Orb+missile_distance_trigger , [fac_commoners] ],
  
 ["magic_black_hold", "Black_Hold_Scroll", [("bullet_1",0),("flash_arcane_02",ixmesh_flying_ammo),("magic_15_icon", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  10000, weight(2.25)|abundance(40)|weapon_length(3)|thrust_damage(90,cut)|max_ammo(4),
  imodbits_missile, cast_magic_black_hold_long+missile_distance_trigger , [fac_commoners] ],
  
 ["magic_black_hold_2", "Black_Hold_Scroll", [("bullet_1",0),("flash_arcane_02",ixmesh_flying_ammo),("magic_15_icon", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  10000, weight(2.25)|abundance(40)|weapon_length(3)|thrust_damage(90,cut)|max_ammo(10),
  imodbits_missile, cast_magic_black_hold+missile_distance_trigger , [fac_commoners] ],
  
 ["magic_lightning_burst", "Lightning Burst_Scroll", [("bullet_1",0),("blitzball",ixmesh_flying_ammo),("icon_magic_LightningBurst", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  7500, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(100,cut)|max_ammo(5),
  imodbits_none, cast_magic_lightning_burst+missile_distance_trigger , [fac_undeads_2, fac_commoners] ],
 ["magic_lightningball", "lightningball_Scroll", [("bullet_1",0),("bullet_1",ixmesh_flying_ammo),("icon_magic_LightningBurst", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  2000, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(35,cut)|max_ammo(10),
  imodbits_none, cast_magic_lightningball+missile_distance_trigger , [fac_commoners, fac_kingdom_5, fac_commoners] ],


 ["magic_shrapmetal", "shrapmetal_Scroll", [("bullet_1",0),("evil_arrow",ixmesh_flying_ammo),("magic_9_icon", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  1500, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(35,cut)|max_ammo(20),
  imodbits_none, missile_distance_trigger , [fac_commoners,fac_kingdom_5] ],
  
 ["magic_summon_blade", "summon_blade", [("bullet_1",0),("laser_bolt_yellow",ixmesh_flying_ammo),("magic_16_icon", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  15000, weight(2.25)|abundance(45)|weapon_length(3)|thrust_damage(5,cut)|max_ammo(2),
  imodbits_none, cast_magic_summon_blade+missile_distance_trigger , [fac_commoners] ],
 ["magic_fireball", "_fireball_Scroll", [("bullet_1",0),("guangjian_fly3",ixmesh_flying_ammo),("magic_11_icon", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  2000, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(35,cut)|max_ammo(10),
  imodbits_none, cast_magic_fire_ball+missile_distance_trigger , [fac_commoners, fac_kingdom_5, fac_commoners] ],
 ["magic_fireball_2", "power_fireball_Scroll", [("bullet_1",0),("guangjian_fly3",ixmesh_flying_ammo),("magic_11_icon", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  10000, weight(2.25)|abundance(40)|weapon_length(3)|thrust_damage(80,cut)|max_ammo(7),
  imodbits_none, cast_magic_fire_ball_2+missile_distance_trigger , [fac_undeads_2, fac_commoners] ],
  
 ["magic_pyroblast", "Pyroblast_Scroll", [("bullet_1",0),("guangjian_fly3",ixmesh_flying_ammo),("icon_magic_Pyroblast", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  20000, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(100,cut)|max_ammo(6),
  imodbits_none, cast_magic_Pyroblast+missile_distance_trigger , [fac_commoners, fac_kingdom_5, fac_commoners] ],
  
 ["magic_dragon_breath", "dragon_breath_Scroll", [("bullet_1",0),("bullet_1",ixmesh_flying_ammo),("icon_magic_dragon_breath", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  2000, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(35,cut)|max_ammo(12),
  imodbits_none, missile_distance_trigger , [fac_commoners, fac_commoners] ],
  
 ["magic_meteor_shower", "meteor_shower_Scroll", [("bullet_1",0),("laser_bolt_yellow",ixmesh_flying_ammo),("magic_6_icon", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  2500, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(100,cut)|max_ammo(7),
  imodbits_none, cast_magic_meteor_shower+missile_distance_trigger , [fac_commoners, fac_undeads_2, fac_commoners] ],

 ["magic_incediary_cloud", "incediary_cloud_Scroll", [("bullet_1",0),("laser_bolt_red",ixmesh_flying_ammo),("icon_magic_incediary_cloud", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  15000, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(100,cut)|max_ammo(3),
  imodbits_none, cast_magic_incediary_cloud+missile_distance_trigger , [fac_undeads_2, fac_commoners] ],
  
 ["magic_apocalypse", "apocalypse_Scroll", [("bullet_1",0),("guangjian_fly3",ixmesh_flying_ammo),("icon_magic_apocalypse", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  15000, weight(2.25)|abundance(30)|weapon_length(3)|thrust_damage(100,cut)|max_ammo(4),
  imodbits_none, cast_magic_apocalypse+missile_distance_trigger , [ fac_undeads_2, fac_commoners] ],
  
  
 ["magic_heaven_fist", "heaven_fist_Scroll", [("bullet_1",0),("bullet_1",ixmesh_flying_ammo),("magic_13_icon", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  2500, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(70,cut)|max_ammo(10),
  imodbits_none, cast_magic_heaven_fist+missile_distance_trigger, [fac_demon_hunters, fac_hospitalier_knights, fac_kingdom_1] ],
  
 ["magic_sun_ray", "sun_ray_Scroll", [("bullet_1",0),("laser_bolt_orange",ixmesh_flying_ammo),("icon_magic_sun_ray", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  1500, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(25,cut)|max_ammo(20),
  imodbits_none, cast_magic_sun_ray+missile_distance_trigger , [fac_demon_hunters, fac_hospitalier_knights, fac_kingdom_1] ],
 ["magic_column_of_fire", "column_of_fire_Scroll", [("bullet_1",0),("laser_bolt_orange",ixmesh_flying_ammo),("icon_magic_Sunburst", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  2500, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(70,cut)|max_ammo(6),
  imodbits_none, cast_magic_column_of_fire+missile_distance_trigger , [fac_demon_hunters, fac_hospitalier_knights] ],
 ["magic_teleport", "teleport_Scroll", [("bullet_1",0),("laser_bolt_blue",ixmesh_flying_ammo),("icon_magic_hurricane", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  4000, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(50,cut)|max_ammo(8),
  imodbits_none, cast_magic_teleport+missile_distance_trigger , [fac_demon_hunters, fac_hospitalier_knights]],
  
 ["magic_armageddon", "Armageddon_Scroll", [("bullet_1",0),("laser_bolt_red",ixmesh_flying_ammo),("magic_18_icon", ixmesh_inventory)], itp_type_bullets|itp_is_magic_staff, 0,
  50000, weight(2.25)|abundance(20)|weapon_length(3)|thrust_damage(100,cut)|max_ammo(2),
  imodbits_missile, cast_magic_armageddon+missile_distance_trigger , [fac_undeads_2] ],
 ["magic_armageddon_dummy", "Armageddon Scroll", [("bullet_1",0),("huge_infern",ixmesh_flying_ammo),("magic_18_icon", ixmesh_inventory)], itp_type_bullets|itp_is_magic_staff, 0,
  275, weight(2.25)|abundance(40)|weapon_length(3)|thrust_damage(5,cut)|max_ammo(5),
  imodbits_missile, cast_magic_armageddon_2 , [fac_commoners] ],

  
 ["magic_meteor_shower_dummy", "Stones", [("bullet_1",0),("flame_ball",ixmesh_flying_ammo),("magic_6_icon", ixmesh_inventory)], itp_type_bolts|itp_is_magic_staff ,0, 
 1 , weight(2.75)|abundance(90)|weapon_length(25)| thrust_damage(50 ,  blunt)|max_ammo(18),
 imodbits_none,[(ti_on_missile_hit, [(store_trigger_param_1, ":shooter"),(copy_position,pos51,pos1),(call_script, "script_magic_deliver_area_damage", ":shooter", 200, 7, 0),]),]],
    
 ["magic_heaven_fist_dummy", "heaven_fist Scroll", [("bullet_1",0),("iron_fist",ixmesh_flying_ammo),("magic_13_icon", ixmesh_inventory)], itp_type_bullets|itp_is_magic_staff, 0,
  1500, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(70,cut)|max_ammo(20),
  imodbits_none, cast_magic_heaven_fist_2],

 ["magic_incediary_cloud_dummy", "incediary_cloud Scroll", [("bullet_1",0),("magic_8_icon", ixmesh_inventory)], itp_type_bullets|itp_is_magic_staff, 0,
  2500, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(5,cut)|max_ammo(6),
  imodbits_none, cast_magic_incediary_cloud_2  ],

 ["magic_poison_dummy", "death_cloud Scroll", [("bullet_1",0),("flame_ball",ixmesh_flying_ammo),("magic_11_icon", ixmesh_inventory)], itp_type_bullets|itp_is_magic_staff, 0,
  275, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(70,cut)|max_ammo(1),
  imodbits_none, cast_magic_fire_ball_3,  ],


["wooden_staff_1", "wooden Staff", [("jorneyman_staff",0)], itp_merchandise|itp_type_pistol|itp_crush_through|itp_primary|itp_next_item_as_melee|itp_is_magic_staff ,itcf_reload_pistol|itcf_shoot_pistol|itcf_carry_spear,
 10000 , weight(3.25)|difficulty(0)|spd_rtng(20) | shoot_speed(80) | thrust_damage(50 ,pierce)|max_ammo(1)|accuracy(82),imodbits_magic_staff, magic_cast_trigger , [fac_commoners, fac_demon_hunters, fac_hospitalier_knights, fac_undeads_2, fac_kingdom_5, fac_kingdom_1] ], 
["wooden_staff",  "wooden Staff", [("jorneyman_staff",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_penalty_with_shield, itc_staff|itcf_carry_spear, 202 , weight(2)|spd_rtng(97)| weapon_length(180)|swing_damage(25 , blunt)| thrust_damage(26 ,  blunt),imodbits_polearm ],

["mage_staff_1", "mage_staff", [("duanzhui30",0)], itp_merchandise|itp_type_pistol|itp_crush_through|itp_primary|itp_next_item_as_melee|itp_is_magic_staff ,itcf_reload_pistol|itcf_shoot_pistol|itcf_carry_spear,
 15000 , weight(3.25)|difficulty(0)|spd_rtng(50) | shoot_speed(130) | thrust_damage(70 ,pierce)|max_ammo(1)|accuracy(82),imodbits_magic_staff, magic_cast_trigger , [fac_commoners] ], 
["mage_staff",  "mage_staff", [("duanzhui30",0)], itp_type_two_handed_wpn|itp_offset_lance| itp_primary|itp_penalty_with_shield, itc_glaive|itcf_carry_spear, 202 , weight(2)|difficulty(0)|spd_rtng(97)| weapon_length(130)|swing_damage(40 , blunt)| thrust_damage(26 ,  blunt),imodbits_polearm, [], [fac_commoners]],

["archmage_staff_1", "arch mage Staff", [("staffofmagnus",0)], itp_merchandise|itp_type_pistol|itp_crush_through|itp_primary|itp_next_item_as_melee|itp_is_magic_staff ,itcf_reload_pistol|itcf_shoot_pistol|itcf_carry_spear,
 20000 , weight(3.25)|difficulty(0)|spd_rtng(55) | shoot_speed(140) | thrust_damage(75 ,pierce)|max_ammo(1)|accuracy(82),imodbits_magic_staff, magic_cast_trigger , [fac_commoners] ], 
["archmage_staff",  "arch mage Staff", [("staffofmagnus",0)], itp_type_two_handed_wpn|itp_offset_lance| itp_primary|itp_penalty_with_shield, itc_staff|itcf_carry_spear, 202 , weight(2)|difficulty(0)|spd_rtng(97)| weapon_length(150)|swing_damage(45 , blunt)| thrust_damage(26 ,  blunt),imodbits_polearm, [], [fac_commoners]],

["sorcerer_staff_1", "Sorcerer_staff", [("sarustaff",0)], itp_merchandise|itp_type_pistol|itp_crush_through|itp_primary|itp_next_item_as_melee|itp_is_magic_staff ,itcf_reload_pistol|itcf_shoot_pistol|itcf_carry_spear,
 15000 , weight(3.25)|difficulty(0)|spd_rtng(30) | shoot_speed(110) | thrust_damage(60 ,pierce)|max_ammo(1)|accuracy(82),imodbits_magic_staff, magic_cast_trigger , [fac_commoners, fac_undeads_2, fac_commoners] ], 
["sorcerer_staff",  "Sorcerer_staff", [("sarustaff",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_penalty_with_shield, itc_glaive|itcf_carry_spear, 202 , weight(2)|difficulty(0)|spd_rtng(97)| weapon_length(150)|swing_damage(30 , cut)| thrust_damage(26 ,  blunt),imodbits_polearm, [], [fac_commoners, fac_undeads_2, fac_commoners]],

["demon_staff_1", "demon_staff", [("staff22_a",0)], itp_merchandise|itp_type_pistol|itp_crush_through|itp_primary|itp_next_item_as_melee|itp_is_magic_staff ,itcf_reload_pistol|itcf_shoot_pistol|itcf_carry_spear,
 25000 , weight(3.25)|difficulty(0)|spd_rtng(40) | shoot_speed(160) | thrust_damage(90 ,pierce)|max_ammo(1)|accuracy(82),imodbits_magic_staff, magic_cast_trigger , [fac_commoners, fac_commoners]],
["demon_staff",  "demon_staff", [("staff22_a",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_penalty_with_shield, itc_glaive|itcf_carry_spear, 202 , weight(2)|difficulty(0)|spd_rtng(97)| weapon_length(140)|swing_damage(40 , blunt)| thrust_damage(26 ,  blunt),imodbits_polearm, [], [fac_commoners, fac_commoners]],


["thunder_staff_1", "thunder Staff", [("lod_WAoRStaffB",0)], itp_merchandise|itp_type_pistol|itp_crush_through|itp_primary|itp_is_magic_staff ,itcf_reload_pistol|itcf_shoot_pistol|itcf_carry_spear,
 20000 , weight(3.25)|difficulty(0)|spd_rtng(35) | shoot_speed(140) | thrust_damage(75 ,pierce)|max_ammo(1)|accuracy(82),imodbits_magic_staff, magic_cast_trigger , [fac_commoners, fac_commoners] ], 
["thunder_staff_melee",  "thunder Staff", [("lod_WAoRStaffB",0)], itp_type_polearm|itp_couchable|itp_offset_lance| itp_primary|itp_penalty_with_shield, itc_greatlance|itcf_carry_spear, 2502 , weight(2)|difficulty(0)|spd_rtng(97)| weapon_length(195)|swing_damage(25 , cut)| thrust_damage(35 ,  pierce),imodbits_axe, [], [fac_commoners, fac_commoners,fac_kingdom_8,fac_beast]],

["shaman_staff_1", "shaman_staff", [("flame_staff",0)], itp_merchandise|itp_type_pistol|itp_crush_through|itp_primary|itp_next_item_as_melee|itp_is_magic_staff ,itcf_reload_pistol|itcf_shoot_pistol|itcf_carry_spear,
 20000 , weight(3.25)|difficulty(0)|spd_rtng(35) | shoot_speed(140) | thrust_damage(75 ,pierce)|max_ammo(1)|accuracy(82),imodbits_magic_staff, [(ti_on_init_item, [(set_position_delta,0,120,0),(particle_system_add_new, "psys_torch_fire"),(particle_system_add_new, "psys_torch_smoke"),(set_current_color,150, 130, 70),(add_point_light, 10, 30),])]+magic_cast_trigger , [fac_commoners, fac_undeads_2,fac_kingdom_10] ], 
  
["shaman_staff",  "shaman_staff", [("flame_staff",0)], itp_type_two_handed_wpn|itp_offset_lance| itp_primary|itp_penalty_with_shield, itc_glaive|itcf_carry_spear, 202 , weight(2)|difficulty(0)|spd_rtng(97)| weapon_length(175)|swing_damage(35 , cut)| thrust_damage(26 ,  blunt),imodbits_axe, [(ti_on_init_item, [(set_position_delta,0,120,0),(particle_system_add_new, "psys_torch_fire"),(particle_system_add_new, "psys_torch_smoke"),(set_current_color,150, 130, 70),(add_point_light, 10, 30),])], [fac_commoners, fac_undeads_2]],

["warlock_staff_1", "warlock Staff", [("lod_WAoRStaffA",0)], itp_merchandise|itp_type_pistol|itp_crush_through|itp_primary|itp_is_magic_staff ,itcf_reload_pistol|itcf_shoot_pistol|itcf_carry_spear,
 15000 , weight(3.25)|difficulty(0)|spd_rtng(30) | shoot_speed(110) | thrust_damage(60 ,pierce)|max_ammo(1)|accuracy(82),imodbits_magic_staff, magic_cast_trigger , [fac_commoners, fac_commoners] ], 
["drow_lance", "drow_lance", [("WAoRStaffC", 0)], itp_merchandise|itp_type_polearm|itp_couchable|itp_wooden_parry|itp_primary, itc_greatlance|itcf_carry_spear, 5014, weight(3.5)|weapon_length(220)|difficulty(4)|spd_rtng(90)|abundance(10)|swing_damage(32, blunt)|thrust_damage(50, pierce), imodbits_polearm, [],[fac_kingdom_8,fac_commoners,fac_beast]],

["skull_staff", "skull Staff", [("skull_staff",0)], itp_merchandise|itp_type_pistol|itp_crush_through|itp_primary|itp_next_item_as_melee|itp_is_magic_staff ,itcf_reload_pistol|itcf_shoot_pistol|itcf_carry_spear,
 20000 , weight(3.25)|difficulty(0)|spd_rtng(35) | shoot_speed(140) | thrust_damage(75 ,pierce)|max_ammo(1)|accuracy(82),imodbits_magic_staff, magic_cast_trigger , [fac_commoners, fac_undeads_2] ], 
["skull_staff_melee",  "skull Staff", [("skull_staff",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_penalty_with_shield, itc_staff|itcf_carry_spear, 202 , weight(2)|difficulty(0)|spd_rtng(97)| weapon_length(157)|swing_damage(25 , cut)| thrust_damage(26 ,  pierce),imodbits_axe, [], [fac_commoners, fac_undeads_2]],


["lich_staff_1", "lich Staff", [("mummy_staff",0)], itp_merchandise|itp_type_pistol|itp_crush_through|itp_primary|itp_next_item_as_melee|itp_is_magic_staff ,itcf_reload_pistol|itcf_shoot_pistol|itcf_carry_spear,
 25000 , weight(3.25)|difficulty(0)|spd_rtng(40) | shoot_speed(170) | thrust_damage(80 ,pierce)|max_ammo(1)|accuracy(82),imodbits_magic_staff, magic_cast_trigger , [fac_commoners,fac_undeads_2] ], 
["lich_staff",  "lich Staff", [("mummy_staff",0)], itp_type_two_handed_wpn|itp_offset_lance| itp_primary|itp_penalty_with_shield, itc_glaive|itcf_carry_spear, 202 , weight(2)|difficulty(0)|spd_rtng(97)| weapon_length(130)|swing_damage(35 , blunt)| thrust_damage(26 ,  blunt),imodbits_polearm, [], [fac_undeads_2]],

["archlich_staff_1", "lich Staff", [("dragonbonestaff",0),("dragonbonestaff_inv",ixmesh_inventory),("dragonbonestaff_inv",ixmesh_carry)], itp_type_pistol|itp_crush_through|itp_next_item_as_melee|itp_primary|itp_is_magic_staff ,itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_spear,
 30000 , weight(3.25)|difficulty(0)|spd_rtng(45) | shoot_speed(200) | thrust_damage(85 ,pierce)|max_ammo(1)|accuracy(85),imodbits_magic_staff, magic_cast_trigger , [fac_undeads_2,fac_kingdom_5,fac_commoners]],
["mummy_staff", "mummy Staff", [("dragonbonestaff",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_penalty_with_shield, itc_glaive|itcf_carry_spear, 60 , weight(2)|difficulty(0)|spd_rtng(104)| weapon_length(180)|swing_damage(20 , blunt)| thrust_damage(20 ,  blunt),imodbits_polearm],

["venom_staff_1", "Venom_Staff", [("tomestaff",0)], itp_merchandise|itp_type_pistol|itp_crush_through|itp_primary|itp_next_item_as_melee|itp_is_magic_staff ,itcf_reload_pistol|itcf_shoot_pistol|itcf_carry_spear,
 25000 , weight(3.25)|difficulty(0)|spd_rtng(40) | shoot_speed(160) | thrust_damage(80 ,pierce)|max_ammo(1)|accuracy(82),imodbits_magic_staff, magic_cast_trigger , [fac_undeads_2,fac_demon] ], 
["venom_staff",  "Venom_Staff", [("tomestaff",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_penalty_with_shield, itc_glaive|itcf_carry_spear, 202 , weight(2)|difficulty(0)|spd_rtng(97)| weapon_length(170)|swing_damage(35 , pierce)| thrust_damage(45 ,  pierce),imodbits_polearm, [], [fac_undeads_2]],

["mark_chaos_1", "Mark_Chaos Staff", [("lod_WAoRSwordA",0)], itp_merchandise|itp_type_pistol|itp_crush_through|itp_primary|itp_next_item_as_melee|itp_is_magic_staff ,itcf_reload_pistol|itcf_shoot_pistol|itcf_carry_sword_back,
 25000 , weight(3.25)|difficulty(0)|spd_rtng(40) | shoot_speed(150) | thrust_damage(80 ,pierce)|max_ammo(3)|accuracy(82),imodbits_magic_staff, magic_cast_trigger , [fac_commoners, fac_kingdom_9,fac_demon] ], 
["mark_chaos",  "Mark_Chaos Staff", [("lod_WAoRSwordA",0)], itp_type_one_handed_wpn| itp_primary|itp_crush_through|itp_unique|itp_can_knock_down|itp_bonus_against_shield, itc_longsword|itcf_carry_sword_back, 10000 , weight(2)|difficulty(0)|spd_rtng(90)| weapon_length(140)|swing_damage(40, pierce)| thrust_damage(0 ,  pierce),imodbits_polearm, [], [fac_commoners]],

["drow_staff_1", "drow Staff", [("WAoRStaffC",0)], itp_merchandise|itp_type_pistol|itp_crush_through|itp_primary|itp_is_magic_staff ,itcf_reload_pistol|itcf_shoot_pistol|itcf_carry_spear,
 25000 , weight(3.25)|difficulty(0)|spd_rtng(40) | shoot_speed(170) | thrust_damage(80 ,pierce)|max_ammo(1)|accuracy(82),imodbits_magic_staff, magic_cast_trigger , [fac_beast] ], 

["drow_staff_2", "drow Staff", [("WAoRStaffE",0)], itp_type_pistol|itp_crush_through|itp_next_item_as_melee|itp_primary|itp_is_magic_staff ,itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_spear,
 30000 , weight(3.25)|difficulty(0)|spd_rtng(45) | shoot_speed(200) | thrust_damage(85 ,pierce)|max_ammo(1)|accuracy(85),imodbits_magic_staff, magic_cast_trigger , [fac_kingdom_8,fac_beast] ], 
["drow_staff_2_melee", "drow Staff", [("WAoRStaffE",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_crush_through|itp_two_handed|itp_extra_penetration, itc_glaive|itcf_carry_spear, 202 , weight(2)|difficulty(0)|spd_rtng(97)| weapon_length(170)|swing_damage(36 , pierce)| thrust_damage(26 ,  blunt),imodbits_polearm, [], [fac_beast]],


["ogrehammer_cast", "Ogre's Hammer", [("ogrehammer",0)], itp_type_pistol|itp_crush_through|itp_primary|itp_next_item_as_melee|itp_is_magic_staff ,itcf_reload_pistol|itcf_shoot_pistol|itcf_carry_sword_left_hip,
50000 , weight(20)|abundance(1)|difficulty(0)|spd_rtng(40) | shoot_speed(90) | thrust_damage(60 ,pierce)|max_ammo(1)|accuracy(82),imodbits_magic_staff, magic_cast_trigger , [fac_commoners, fac_orc] ], 
["ogrehammer_melee", "Ogre's Hammer", [("ogrehammer",0)], itp_crush_through|itp_type_one_handed_wpn|itp_can_knock_down|itp_primary|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear, 
290 , weight(20)|abundance(1)|difficulty(14)|spd_rtng(70) | weapon_length(180)|swing_damage(60 , blunt) | thrust_damage(15 ,  pierce),imodbits_mace ],

["shaman_staff_2", "shaman Staff", [("shaman_staff_b",0)], itp_merchandise|itp_type_pistol|itp_crush_through|itp_primary|itp_next_item_as_melee|itp_is_magic_staff ,itcf_reload_pistol|itcf_shoot_pistol|itcf_carry_spear,
 20000 , weight(3.25)|difficulty(0)|spd_rtng(35) | shoot_speed(140) | thrust_damage(75 ,pierce)|max_ammo(1)|accuracy(82),imodbits_magic_staff, magic_cast_trigger , [fac_commoners, fac_scotland, fac_undeads_2] ], 
["shaman_staff_3",  "skull Staff", [("shaman_staff_b",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_penalty_with_shield, itc_staff|itcf_carry_spear, 202 , weight(2)|difficulty(0)|spd_rtng(97)| weapon_length(157)|swing_damage(25 , cut)| thrust_damage(26 ,  pierce),imodbits_axe, [], [fac_commoners, fac_undeads_2]],

["nec_robe", "nec_robe", [("demonrobe",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0, 1722,cloth_tier_4,imodbits_cloth, [], [fac_undeads_2, fac_commoners]],
["lich_armor", "lich_armor", [("lich_robe2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 8100,breastplate_tier_5,imodbits_plate, [], [fac_undeads_2]],
["archlich_armor", "twiligh_armor", [("archlich_armor",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 10868,full_plate_armor_tier_3, imodbits_good_plate , [], [fac_undeads_2,fac_kingdom_5,fac_commoners]],
["vampire_rapierd", "Rapierd", [("Reitschwert_Pistolier_A_01", 0), ("Reitschwert_scabbard", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary, itc_side_sword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,1201, weight(1.5)|difficulty(0)|spd_rtng(110)|weapon_length(115)|swing_damage(26,cut)|thrust_damage(39,pierce), imodbit_balanced|imodbit_tempered|imodbit_masterwork| imodbit_deadly| imodbit_sharp, [], [fac_undeads_2]],


["undead_double_axe", "Double Axe", [("AN_axe03b",0)], itp_merchandise|itp_type_two_handed_wpn|itp_cant_use_on_horseback|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_can_knock_down|itp_crush_through|itp_unbalanced|itp_extra_penetration, itc_nodachi|itcf_carry_axe_back, 2500, weight(6.5)|difficulty(8)|spd_rtng(110)|weapon_length(100)|swing_damage(55,pierce)|thrust_damage(0,pierce), imodbits_axe|imodbit_masterwork, [], [fac_undeads_2]],

["undead_shield_kite_cav", "Knightly Kite Shield",   [("undead_newsh" ,0)], itp_merchandise|itp_type_shield, itcf_carry_kite_shield,2160 , weight(3.5)|shield_hit_points(250)|body_armor(90)|spd_rtng(100)|shield_width(40)|shield_height(55),imodbits_shield, [], [fac_kingdom_3] ],

["skeleton_throwing_pike",  "Throwing Pikes", [("skeleton_pike",0)], itp_type_thrown| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry, itcf_throw_javelin, 500 , weight(3.0)|difficulty(4)|spd_rtng(81)| weapon_length(180)| thrust_damage(60 ,pierce)| shoot_speed(26)|max_ammo(3),imodbits_thrown , missile_distance_trigger, [fac_undeads_2]],
["skeleton_pike_melee",     "Throwing Pike", [("skeleton_pike",0)], itp_type_polearm| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_is_pike, itc_pike, 500 , weight(3.0)|difficulty(0)|spd_rtng(81)| weapon_length(245)|swing_damage(16 , blunt)| thrust_damage(26 ,  pierce),imodbits_thrown, [], [fac_undeads_2] ],

["vampire_tunic", "tunic_over_shirt", [("vampire_tunic_over_shirt",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 4035,mail_armor_tier_3,imodbits_cloth, [], [fac_undeads_2,fac_kingdom_5,fac_commoners]],



["death_knight_plate", "Dread Knight_plate", [("siwangkaijia",0)], merc_body_armor, 0, 20000, weight(30)|abundance(20)|head_armor(13)|body_armor(85)|leg_armor(45)|difficulty(18), imodbits_good_plate, [], [fac_undeads_2]],
["death_knight_foot", "Dread Knight Boots", [("siwangchangxue",0)], itp_merchandise| itp_type_foot_armor| itp_attach_armature,0,
 2664 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(40)|difficulty(9) ,imodbits_good_plate,  [], [fac_undeads_2]],
["death_knight_head", "Dread Knight Helm", [("siwangqishitou",0)], itp_merchandise|itp_type_fullhelm, 0, 
 5400 , weight(2.75)|abundance(100)|head_armor(90)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_good_plate,   [], [fac_undeads_2]],
["death_knight_hand","Dread Knight_hand", [("siwangshou_L",0)], itp_merchandise|itp_type_hand_armor,0,  820, weight(1)|abundance(30)|body_armor(10)|difficulty(0),imodbits_armor, [], [fac_undeads_2]],
["death_knight_shield", "Dread Knight_shield", [("fix_EOS_knight_shield",0)], itp_type_shield, itcf_carry_kite_shield,  2091 , weight(4)|difficulty(10)|shield_hit_points(300)|body_armor(125)|spd_rtng(100)|shield_width(40)|shield_height(60),imodbits_shield , [], [fac_undeads_2,fac_kingdom_5]],

["undead_great_helmet", "Great Helmet", [("2great_helmet_black",0)],  itp_merchandise|itp_type_fullhelm,0, 
 4266 , weight(2.75)|abundance(100)|head_armor(80)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, [], [fac_undeads_2] ],
["undead_winged_great_helmet", "Winged Great Helmet", [("maciejowski_helmet_black",0)], itp_merchandise|itp_type_fullhelm,0, 
 5400 , weight(2.75)|abundance(100)|head_armor(90)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, [], [fac_undeads_2] ],

#["vampiehelm_0", "vampieHelm", [("toumingshou",0)], itp_merchandise|itp_type_head_armor|itp_civilian| itp_doesnt_cover_hair, 0, 
# 2730 , weight(2.75)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate,[], [fac_undeads_2] ],
 
["vampiehelm_0", "vampieHelm", [("vampie_toutao",0)], itp_merchandise|itp_type_head_armor|itp_civilian, 0, 
 2730 , weight(2.75)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate,[], [fac_undeads_2] ],

 
["lich_helm", "lichhelm", [("nekromantahead3",0)], itp_merchandise|itp_type_head_armor|itp_civilian ,0, 5400 , weight(2)|abundance(100)|head_armor(90)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,[], [fac_undeads_2]],

["demon_hood", "demon_hood", [("demon_hood",0)], itp_merchandise|itp_type_head_armor|itp_civilian|itp_covers_head ,0, 2730 , weight(2)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,[], [fac_undeads_2]],
["scull_head", "scull_head", [("nekromantahead1",0)], itp_merchandise|itp_type_head_armor|itp_civilian ,0, 5400 , weight(2)|abundance(100)|head_armor(70)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,[], [fac_undeads_2]],
["crown", "crown", [("aqs_crown_new",0)], itp_type_head_armor|itp_civilian| itp_doesnt_cover_hair, 0, 
 20000 , weight(2.75)|abundance(100)|head_armor(100)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, [], [fac_undeads_2,fac_kingdom_5]],



["twiligh_armor", "twiligh_armor", [("twiligh_armor",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 20000, weight(28)|abundance(100)|head_armor(0)|body_armor(100)|leg_armor(60)|difficulty(20), imodbits_good_plate,[], [fac_undeads_2,fac_kingdom_3,fac_kingdom_5] ],
["twilight_boots", "twilight_boots", [("twilight_boots",0)],  itp_merchandise|itp_type_foot_armor| itp_attach_armature,0, 
 20000 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(40)|difficulty(8) ,imodbits_plate ,[], [fac_undeads_2] ],
["twilight_gloves","Gauntlets", [("twilight_gloves_L",0)], itp_merchandise|itp_type_hand_armor,0, 640, weight(1.25)|abundance(100)|body_armor(13)|difficulty(0),imodbits_armor,[], [fac_undeads_2,fac_kingdom_5,fac_commoners]],
["twilight_helm", "twilighthelm", [("twilighthelm",0)], itp_merchandise|itp_type_fullhelm|itp_covers_head ,0, 2730 , weight(2)|abundance(100)|head_armor(90)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,[], [fac_undeads_2,fac_kingdom_5,fac_commoners]],







 ["laser_bolt_blue", "Plasma_Gas_Cartridges", [("bullet_1",0),("laser_bolt_blue",ixmesh_flying_ammo),("spak_book",ixmesh_carry)], itp_type_bullets|itp_can_penetrate_shield|itp_bonus_against_shield|itp_covers_legs, itcf_carry_sword_left_hip,
  20000, weight(2.25)|abundance(30)|weapon_length(3)|thrust_damage(50,pierce)|max_ammo(120), 
  imodbits_missile, missile_distance_trigger , [fac_demon_hunters] ],
 ["laser_bolt_red", "Plasma_Gas_Cartridges", [("bullet_1",0),("laser_bolt_red",ixmesh_flying_ammo),("laser_bolt_red_cartridges_pistol", ixmesh_inventory)], itp_type_bullets, 0,
  275, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(200,cut)|max_ammo(60),
  imodbits_missile, missile_distance_trigger , [fac_dwarf] ],


["amade_bronze_gauntlets","Bronze Gauntlets", [("amade_bronze_gauntlet_L",0)], itp_type_hand_armor,0, 
 5000, weight(2.25)|abundance(100)|body_armor(15)|difficulty(0),imodbits_armor, 
 [] , [fac_kingdom_1,fac_dark_knights]],
["amade_steel_gauntlets","Steel Gauntlets", [("amade_steel_gauntlet_L",0)], itp_type_hand_armor,0, 
 5000, weight(2.25)|abundance(100)|body_armor(15)|difficulty(0),imodbits_armor, 
 [] , [fac_dark_knights]],

["amade_bronze_greaves", "Bronze Greaves", [("amade_bronze_greaves",0)],  itp_type_foot_armor| itp_attach_armature,0,
 4000 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(45)|difficulty(9) ,imodbits_armor , 
 [], [fac_kingdom_1,fac_dark_knights]],
["amade_steel_greaves", "Steel Greaves", [("amade_steel_greaves",0)],  itp_type_foot_armor| itp_attach_armature,0, 
 4000 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(45)|difficulty(9) ,imodbits_armor , 
 [], [fac_dark_knights]],

["amade_bronze_plate","Bronze Plate Armor",[("amade_bronze_plate",0)],itp_type_body_armor|itp_covers_legs,0,
 25000,weight(30)|abundance(30)|head_armor(0)|body_armor(95)|leg_armor(50)|difficulty(18),
 imodbits_good_plate, [], [fac_dark_knights]],
["amade_steel_plate","Steel Plate Armor",[("amade_steel_plate",0)],itp_type_body_armor|itp_covers_legs,0,
 25000,weight(30)|abundance(30)|head_armor(0)|body_armor(85)|leg_armor(50)|difficulty(18),
 imodbits_good_plate, [], [fac_dark_knights]],

["amade_bronze_winged_helm","Bronze Winged Helm",[("amade_bronze_winged_helm",0),("amade_bronze_winged_helm_store",ixmesh_inventory)],itp_type_head_armor|itp_civilian|itp_attach_armature,0,
 5400,weight(3.0)|abundance(25)|head_armor(90)|body_armor(0)|leg_armor(0)|difficulty(10),imodbits_plate, [], [fac_kingdom_10,fac_dark_knights]
],

#["amade_bronze_winged_helm_small","Bronze Winged Helm",[("amade_bronze_winged_helm_plain",0)],itp_type_head_armor|itp_civilian,0, 3266 , weight(3)|abundance(100)|head_armor(70)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_dark_knights] ],


["amade_steel_winged_helm","Steel Winged Helm",[("amade_steel_winged_helm",0),("amade_steel_winged_helm_store",ixmesh_inventory)],itp_type_head_armor|itp_civilian|itp_attach_armature,0,
 4266 , weight(3.0)|abundance(25)|head_armor(80)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, [], [fac_dark_knights] 
],

#["amade_steel_winged_helm_small","Steel Winged Helm",[("amade_steel_winged_helm_plain",0)],itp_type_head_armor|itp_civilian,0, 2400 , weight(2.0)|abundance(100)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_dark_knights]],
["drow_bolts","drow Bolts", [("toumingtou",0),("van_helsing_crossbow_bolt_copy",ixmesh_flying_ammo),("van_helsing_crossbow_bolt_bag", ixmesh_carry),("van_helsing_crossbow_bolt_bag", ixmesh_carry|imodbit_large_bag)], itp_type_bolts|itp_can_penetrate_shield|itp_bonus_against_shield|itp_is_magic_staff, itcf_carry_quiver_right_vertical, 5000,weight(2.25)|abundance(35)|weapon_length(55)|thrust_damage(40,pierce)|max_ammo(15),imodbits_missile,missile_poison_trigger+missile_distance_trigger, [], [fac_beast]],

["throwing_lightning",         "Throwing lightning", [("small_lightning_combined",0),("lightning", ixmesh_flying_ammo)], itp_type_thrown|itp_crush_through|itp_primary|itp_next_item_as_melee ,itcf_throw_stone,10000 , weight(4)|difficulty(4)|spd_rtng(60)| shoot_speed(100)| thrust_damage(67 ,  cut)|max_ammo(24)|weapon_length(65),imodbits_thrown,thunder_weapon_trigger+missile_distance_trigger, [fac_dark_knights]],

["throwing_lightning_melee",         "Throwing lightning", [("small_lightning_combined",0),("lightning", ixmesh_flying_ammo)],itp_type_polearm|itp_primary|itp_wooden_parry , itc_longsword,10000 , weight(1)|difficulty(4)|spd_rtng(91)| swing_damage(54, pierce)| thrust_damage(40 ,  pierce)|weapon_length(200),imodbits_thrown, thunder_weapon_trigger_2, [fac_dark_knights] ],



#["xenoargh_evil_helm","Evil Helm",[("xenoargh_evil_helm",0),("xenoargh_evil_helm_store",ixmesh_inventory)],itp_type_head_armor|itp_civilian|itp_covers_head,0,4266,weight(3.0)|abundance(25)|head_armor(80)|body_armor(0)|leg_armor(0)|difficulty(8),imodbits_plate],

#["xenoargh_evil_helm_yellow","Yellow Evil Helm",[("xenoargh_evil_helm_yellow",0),("xenoargh_evil_helm_yellow_store",ixmesh_inventory)],itp_type_head_armor|itp_civilian|itp_covers_head,0,4266,weight(3.0)|abundance(25)|head_armor(80)|body_armor(0)|leg_armor(0)|difficulty(8),imodbits_plate],

#["xenoargh_evil_helm_white","White Evil Helm",[("xenoargh_evil_helm_white",0),("xenoargh_evil_helm_white_store",ixmesh_inventory)],itp_type_head_armor|itp_civilian|itp_covers_head,0,4266,weight(3.0)|abundance(25)|head_armor(80)|body_armor(0)|leg_armor(0)|difficulty(8),imodbits_plate],

["xenoargh_mask_black","Black Mask",[("drow_elite_helmet1",0)],itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair|itp_fit_to_head,0,2400 , weight(3)|abundance(100)|head_armor(70)|body_armor(0)|leg_armor(0)|difficulty(7),imodbits_plate],

["xenoargh_hornmask_black","Sister's Mask",[("xenoargh_hornmask_black",0)],itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair|itp_fit_to_head,0,2400 , weight(3)|abundance(100)|head_armor(70)|body_armor(0)|leg_armor(0)|difficulty(7),imodbits_plate],

#["xenoargh_dark_armor02","Dark Armor",[("xenoargh_dark_armor02",0)],itp_type_body_armor|itp_covers_legs,0,20000,full_plate_armor_tier_4,imodbits_good_plate],

#["xenoargh_dark_armor","Spiked Armor",[("xenoargh_dark_armor",0)],itp_type_body_armor|itp_covers_legs,0,25000,weight(30)|abundance(20)|head_armor(0)|body_armor(90)|leg_armor(50)|difficulty(18),imodbits_good_plate],

#["aribeth_armor","Female Light Plate",[("aribeth_armor",0)],itp_type_body_armor|itp_covers_legs,0,7310,full_plate_armor_tier_1,imodbits_plate],
#["aribeth_armor_dark","Female Light Plate",[("aribeth_armor_dark",0)],itp_type_body_armor|itp_covers_legs,0,7310,full_plate_armor_tier_1,imodbits_plate],

#["aribeth_armor_dark_chainmail","Female Dark Armor",[("aribeth_armor_dark_chainmail",0)],itp_type_body_armor|itp_covers_legs,0,9216,full_plate_armor_tier_2,imodbits_plate],

["dthehun_new_battle_armor01","Female Plate Mail",[("dthehun_new_battle_armor05",0)],itp_type_body_armor|itp_covers_legs,0,10868,full_plate_armor_tier_3,imodbits_good_plate, [], [fac_demon_hunters, fac_hospitalier_knights]],
["sissofbattle_armor","Sister of battle armor",[("sissofbattle_armor",0)],itp_type_body_armor|itp_covers_legs,0,25000,weight(25)|abundance(100)|head_armor(0)|body_armor(100)|leg_armor(50)|difficulty(18), imodbits_good_plate, [], [fac_demon_hunters, fac_hospitalier_knights]],
["sissofbattle_armor_red","Sister of battle armor",[("red_sissofbattle_armor",0)],itp_type_body_armor|itp_covers_legs,0,23550,weight(25)|abundance(100)|head_armor(0)|body_armor(150)|leg_armor(60)|difficulty(16),imodbits_good_plate,[], [fac_demon_hunters, fac_hospitalier_knights]],
["sissofbattle_armor_fly","Sister of battle armor",[("fly_red_sissofbattle_armor",0)],itp_type_body_armor|itp_covers_legs,0,23550,weight(30)|abundance(100)|head_armor(0)|body_armor(150)|leg_armor(60)|difficulty(16),imodbits_good_plate,[], [fac_demon_hunters, fac_hospitalier_knights]],

["sissofbattle_sword",         "Sister of battle Zweihander", [("lod_WAoREELongSword",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_can_penetrate_shield|itp_next_item_as_melee, itc_staff|itcf_carry_sword_back, 2445 , weight(3.75)|difficulty(15)|spd_rtng(100)| weapon_length(150)|swing_damage(53, pierce)| thrust_damage(28 ,  pierce),imodbit_balanced|imodbit_tempered|imodbit_masterwork| imodbit_deadly| imodbit_sharp, holy_weapon_trigger,[fac_demon_hunters, fac_hospitalier_knights]],
["sissofbattle_sword_alt",         "Sister of battle Zweihander", [("lod_WAoREELongSword",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_unbalanced|itp_crush_through|itp_can_knock_down|itp_cant_use_on_horseback|itp_can_penetrate_shield, itc_nodachi|itcf_carry_sword_back, 2445 , weight(3.75)|difficulty(15)|spd_rtng(100)| weapon_length(150)|swing_damage(55, pierce)| thrust_damage(0 ,  pierce),imodbit_balanced|imodbit_tempered|imodbit_masterwork| imodbit_deadly| imodbit_sharp, holy_weapon_trigger,[fac_demon_hunters, fac_hospitalier_knights]],

["sissofbattle_sword_short",         "Sister of battle sword", [("smlj",0)], itp_type_one_handed_wpn|itp_primary|itp_crush_through|itp_can_knock_down|itp_can_penetrate_shield, itc_longsword|itcf_carry_sword_back, 2445 , weight(1.5)|difficulty(5)|spd_rtng(100)| weapon_length(115)|swing_damage(35, pierce)| thrust_damage(0 ,  pierce),imodbit_balanced|imodbit_tempered|imodbit_masterwork| imodbit_deadly| imodbit_sharp, holy_weapon_trigger,[fac_demon_hunters, fac_hospitalier_knights]],

["sissofbattle_e5", "e5", [("pistol_2stwolC",0)], itp_type_pistol|itp_crush_through|itp_primary ,itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_pistol_front_left, 
 50000 , weight(2.0)|difficulty(0)|spd_rtng(70) | shoot_speed(120) | thrust_damage(110 ,pierce)|max_ammo(2)|accuracy(90),imodbits_gun, flame_cast_trigger , [fac_demon_hunters, fac_hospitalier_knights] ],



["sissofbattle_A295", "A295", [("Gun_Empire_Heavy_Muscket_F_P1_01",0)], itp_type_musket|itp_crush_through|itp_two_handed|itp_primary|itp_bonus_against_shield,  itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 28000, weight(3.0)|difficulty(0)|spd_rtng(60)|shoot_speed(150)|thrust_damage(125,pierce)|max_ammo(8)|accuracy(95), imodbits_gun,flame_cast_trigger , [fac_demon_hunters, fac_hospitalier_knights]],

["sissofbattle_A295_heavy", "A295", [("Gun_Empire_Heavy_gunner",0)], itp_type_musket|itp_crush_through|itp_two_handed|itp_primary|itp_bonus_against_shield,  itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 28000, weight(3.0)|difficulty(0)|spd_rtng(60)|shoot_speed(200)|thrust_damage(190,pierce)|max_ammo(2)|accuracy(120), imodbits_gun,flame_cast_trigger , [fac_demon_hunters, fac_hospitalier_knights]],

["cartridges_sissofbattle_flame", "Cartridges", [("minie_ball",0),("musket_balls",ixmesh_flying_ammo),("spak_book",ixmesh_carry)], itp_type_bullets|itp_can_penetrate_shield|itp_bonus_against_shield|itp_covers_legs, itcf_carry_sword_left_hip,
  20000, weight(2.25)|abundance(30)|weapon_length(3)|thrust_damage(50,pierce)|max_ammo(6), 
  imodbits_missile, missile_distance_trigger , [fac_demon_hunters, fac_hospitalier_knights] ],

["cartridges_sissofbattle_flame_2", "Cartridges", [("minie_ball",0),("musket_balls",ixmesh_flying_ammo),("spak_book",ixmesh_carry)], itp_type_bullets|itp_can_penetrate_shield|itp_bonus_against_shield|itp_covers_legs, itcf_carry_sword_left_hip,
  20000, weight(2.25)|abundance(30)|weapon_length(3)|thrust_damage(50,pierce)|max_ammo(30), 
  imodbits_missile, missile_distance_trigger , [fac_demon_hunters, fac_hospitalier_knights] ],

["cartridges_sissofbattle_bolter", "Cartridges", [("minie_ball", 0),("huojian_fly2",ixmesh_flying_ammo),("spak_book",ixmesh_carry)],  itp_type_bullets|itp_can_penetrate_shield|itp_bonus_against_shield|itp_covers_legs, itcf_carry_sword_left_hip, 35000, weight(4)|weapon_length(30)|difficulty(0)|spd_rtng(65)|shoot_speed(17)|abundance(33)|thrust_damage(50, cut)|max_ammo(30), imodbits_none,[(ti_on_missile_hit, [(store_trigger_param_1, ":shooter"),(copy_position,pos51,pos1),(call_script, "script_magic_deliver_area_damage", ":shooter", 150, 4, 16),]),]+missile_distance_trigger,[fac_demon_hunters, fac_hospitalier_knights]],

["cartridges_sissofbattle_bolter_2", "Cartridges", [("minie_ball", 0),("prt__fly311",ixmesh_flying_ammo),("spak_book",ixmesh_carry)],  itp_type_bullets|itp_can_penetrate_shield|itp_bonus_against_shield|itp_covers_legs, itcf_carry_sword_left_hip, 35000, weight(4)|weapon_length(30)|difficulty(0)|spd_rtng(65)|shoot_speed(17)|abundance(33)|thrust_damage(50, cut)|max_ammo(30), imodbits_none,[(ti_on_missile_hit, [(store_trigger_param_1, ":shooter"),(copy_position,pos51,pos1),(call_script, "script_magic_deliver_area_damage", ":shooter", 100, 7, 14),]),]+missile_distance_trigger,[fac_demon_hunters, fac_hospitalier_knights]],


["siss_cap", "Cap", [("eyepiece_up",0)],  itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair ,0,
 8000,  weight(5)|abundance(100)|head_armor(100)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["priest_cap_1", "Cap", [("priest_2_coif_1",0)],  itp_merchandise|itp_type_head_armor  |itp_civilian ,0,
 250,  weight(1)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth , [], [fac_demon_hunters, fac_hospitalier_knights]],

["priest_cap_2", "Cap", [("priest_2_coif_2",0)],  itp_merchandise|itp_type_head_armor  |itp_civilian ,0,
 500,  weight(1)|abundance(100)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], [fac_demon_hunters, fac_hospitalier_knights] ],

["priest_robe_1", "Priest Robe", [("priest_1",0)],  itp_merchandise|itp_type_body_armor  |itp_civilian ,0,
  300,  cloth_tier_3 ,imodbits_cloth, [], [fac_demon_hunters, fac_hospitalier_knights] ],
["priest_robe_2", "Priest Robe", [("priest_2",0)],  itp_merchandise|itp_type_body_armor  |itp_civilian ,0,
  940,cloth_tier_4 ,imodbits_cloth ],
["priest_robe_3", "Priest Robe", [("priest_2_1",0)],  itp_merchandise|itp_type_body_armor  |itp_civilian ,0,
  940,cloth_tier_4 ,imodbits_cloth, [], [fac_demon_hunters, fac_hospitalier_knights] ],
  
["surgeon", "Surgeon Outfit", [("surgeon",0)],  itp_type_body_armor  |itp_civilian ,0,
  300,  cloth_tier_4 ,imodbits_cloth, [], [fac_demon_hunters, fac_hospitalier_knights] ],

["priest_1_boots", "Sandals", [("priest_1_boots",0)],  itp_merchandise|itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
  96,  weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(2)|difficulty(0) ,imodbits_cloth, [], [fac_demon_hunters, fac_hospitalier_knights] ],
["priest_2_boots", "Hose", [("priest_2_boots",0)],  itp_merchandise|itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
  96,  weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(2)|difficulty(0) ,imodbits_cloth, [], [fac_demon_hunters, fac_hospitalier_knights] ],

["bishop_great_helm", "Bishop Great_Helm", [("bishop_tophelm", 0)], itp_merchandise | itp_type_fullhelm, 0,
  4266,  weight(2.75)|head_armor(80)|difficulty(10), imodbits_plate,
  [], [fac_demon_hunters, fac_hospitalier_knights] ],
        
["bishop_armour", "Bishop Armour", [("bishop",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,  7310,full_plate_armor_tier_1 ,imodbits_armor, [], [fac_kingdom_1]],

["bishop_mitre", "Cap", [("bishop_mitre",0)],  itp_merchandise|itp_type_head_armor|itp_civilian|itp_fit_to_head ,0,
  6500,  weight(2)|abundance(100)|head_armor(85)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_cloth, [], [fac_demon_hunters, fac_hospitalier_knights] ],
  
["empire_priest", "Empire_Priest_Armour", [("empire_priest", 0)], merc_body_armor, 0, 10868,full_plate_armor_tier_3, imodbits_plate, [], [fac_kingdom_1]], 
  
["bishop_staff", "Bishop Staff", [("cleric_staff",0)], itp_merchandise|itp_type_pistol|itp_crush_through|itp_primary|itp_next_item_as_melee|itp_is_magic_staff ,itcf_reload_pistol|itcf_shoot_pistol|itcf_carry_spear,
 20000 , weight(3.25)|difficulty(0)|spd_rtng(20) | shoot_speed(80) | thrust_damage(50 ,pierce)|max_ammo(1)|accuracy(82),imodbits_magic_staff, magic_cast_trigger , [fac_demon_hunters, fac_hospitalier_knights] ], 
["bishop_staff_melee","Bishop Staff", [("cleric_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itc_parry_polearm|itcf_carry_sword_back,9, weight(2)|spd_rtng(120) | weapon_length(115)|swing_damage(30,blunt) | thrust_damage(30,blunt),imodbits_polearm, holy_weapon_trigger],

["war_clerics_warhammer_cast", "Warhammer", [("war_mace_2",0),("spak_book", ixmesh_carry)], itp_merchandise|itp_type_pistol|itp_crush_through|itp_primary|itp_next_item_as_melee|itp_is_magic_staff ,itcf_reload_pistol|itcf_shoot_pistol|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 25000 , weight(3.25)|difficulty(0)|spd_rtng(30) | shoot_speed(110) | thrust_damage(60 ,pierce)|max_ammo(1)|accuracy(82),imodbits_magic_staff, magic_cast_trigger , [fac_demon_hunters, fac_hospitalier_knights] ], 
 ["war_clerics_warhammer", "Warhammer", [("war_mace_2",0),("spak_book", ixmesh_carry)], itp_type_one_handed_wpn|itp_can_knock_down| itp_primary|itp_wooden_parry|itp_crush_through, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 653 , weight(4)|difficulty(18)|spd_rtng(100)| weapon_length(120)|swing_damage(45 , blunt),imodbits_mace, holy_weapon_trigger],

["war_clerics_warhammer_cast_2", "Great Hammer", [("smchui",0),("spak_book", ixmesh_carry)], itp_merchandise|itp_type_pistol|itp_crush_through|itp_primary|itp_next_item_as_melee|itp_is_magic_staff ,itcf_reload_pistol|itcf_shoot_pistol|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 25000 , weight(3.25)|difficulty(0)|spd_rtng(40) | shoot_speed(170) | thrust_damage(80 ,pierce)|max_ammo(1)|accuracy(82),imodbits_magic_staff, magic_cast_trigger , [fac_demon_hunters, fac_hospitalier_knights] ], 
["war_clerics_warhammer_2",         "Great Hammer", [("smchui",0),("spak_book", ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_can_knock_down|itp_crush_through| itp_primary|itp_cant_use_on_horseback, itc_nodachi|itcf_carry_spear,97 , weight(6)|difficulty(8)|spd_rtng(93)| weapon_length(120)|swing_damage(50 , blunt)| thrust_damage(0 ,  pierce),imodbits_mace, holy_weapon_trigger],

["bishop_staff_2", "Bishop Staff", [("duanzhui26",0)], itp_type_pistol|itp_crush_through|itp_next_item_as_melee|itp_primary|itp_is_magic_staff ,itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_spear,
 30000 , weight(3.25)|difficulty(0)|spd_rtng(50) | shoot_speed(200) | thrust_damage(85 ,pierce)|max_ammo(1)|accuracy(85),imodbits_magic_staff, magic_cast_trigger , [fac_demon_hunters, fac_hospitalier_knights] ], 
["bishop_staff_2_melee", "Bishop Staff", [("duanzhui26",0)], itp_type_two_handed_wpn|itp_offset_lance| itp_primary|itp_penalty_with_shield, itc_glaive|itcf_carry_spear, 60 , weight(2)|difficulty(0)|spd_rtng(104)| weapon_length(130)|swing_damage(35 , blunt)| thrust_damage(20 ,  blunt),imodbits_polearm, holy_weapon_trigger],

 ["magic_heaven_fist_throw_2", "heaven_fist_Scroll", [("throwable_cross",0),("throwable_cross",ixmesh_flying_ammo)], itp_merchandise|itp_type_thrown|itp_crush_through|itp_is_magic_staff|itp_primary, itcf_throw_stone,
  2500, weight(2.25)|abundance(90)|spd_rtng(65)|shoot_speed(50)|weapon_length(3)|thrust_damage(70,cut)|max_ammo(10),
  imodbits_none, cast_magic_heaven_fist_3+missile_distance_trigger, [fac_demon_hunters, fac_hospitalier_knights] ],
 ["magic_heaven_fist_throw_1", "heaven_fist Scroll", [("throwable_cross",0),("iron_fist",ixmesh_flying_ammo)], itp_type_thrown|itp_crush_through|itp_is_magic_staff|itp_primary, itcf_throw_stone,
  1500, weight(2.25)|abundance(90)|spd_rtng(65)|shoot_speed(70)|weapon_length(3)|thrust_damage(70,cut)|max_ammo(20),
  imodbits_none, cast_magic_heaven_fist_2, [fac_demon_hunters, fac_hospitalier_knights] ],
 ["crusader_sword_1", "Crusader_sword", [("ElvenSword",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback, itc_greatsword|itcf_carry_sword_back,
 2700 , weight(2.0)|difficulty(9)|spd_rtng(101)| weapon_length(125)|swing_damage(40, pierce)| thrust_damage(32 ,  pierce),imodbits_sword_high, [],[fac_demon_hunters, fac_hospitalier_knights]],
 ["crusader_sword_2", "Holy Avenger_sword", [("copy_ElvenSword",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback, itc_greatsword|itcf_carry_sword_back,
 5000 , weight(2.0)|difficulty(9)|spd_rtng(130)| weapon_length(125)|swing_damage(55, pierce)| thrust_damage(32 ,  pierce),imodbits_sword_high, [],[fac_demon_hunters, fac_hospitalier_knights]],


 

["bloodguard_body", "Scorpion_Boss", [("xiewang",0)], itp_type_half_body_armor, 0, 20000, weight(5)|abundance(65)|head_armor(20)|body_armor(80)|leg_armor(60)|difficulty(12), imodbits_armor ],

["succubus_body", "Succubus body", [("darkmoon",0)], itp_type_full_body_armor, 0, 20000, weight(5)|abundance(65)|head_armor(70)|body_armor(80)|leg_armor(60)|difficulty(12), imodbits_armor ],
 
["imp_head", "imp head", [("demon_head_01",0)], itp_type_fullhelm|itp_covers_beard|itp_unique|itp_fit_to_head, 0, 4500, weight(2.75)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(0)|difficulty(9), imodbits_plate],
["imp_foot", "imp foot", [("demon_legs",0)], itp_type_foot_armor|itp_attach_armature|itp_unique, 0, 2570 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(9), imodbits_armor ],
["imp_hand", "imp hand", [("demon_hand_L",0)], itp_type_hand_armor|itp_unique, 0, 540, weight(1.25)|abundance(100)|body_armor(10)|difficulty(0), imodbits_armor ],
["imp_body", "imp body", [("demon_body",0)], itp_type_full_body_armor, 0, 20000, weight(26)|abundance(65)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(12), imodbits_armor ],
 
["imp_fork","imp Fork", [("basic_demon_lance",0)], itp_type_thrown|itp_crush_through|itp_primary|itp_next_item_as_melee ,itcf_throw_javelin,560 , weight(4)|difficulty(2)|spd_rtng(89)| shoot_speed(24)| thrust_damage(48 ,  pierce)|max_ammo(45)|weapon_length(131),imodbits_thrown,missile_distance_trigger, throw_factions],
["imp_fork_melee","imp Fork", [("basic_demon_lance",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_wooden_parry, itc_staff|itcf_horseback_slash_polearm, 282 , weight(2.2)|difficulty(0)|spd_rtng(90)| weapon_length(200)|swing_damage(0, cut)| thrust_damage(40 ,  pierce),imodbits_polearm ],
 
["demon_lance","demon_lance", [("long_demon_lance",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_is_pike|itp_extra_penetration, itc_greatlance, 282 , weight(2.2)|difficulty(0)|spd_rtng(90)| weapon_length(250)|swing_damage(0, cut)| thrust_damage(35 ,  pierce),imodbits_polearm ],


["demon_fireball", "Large_Grenade", [("bombaaa_m", 0),("guangjian3",ixmesh_flying_ammo)], itp_type_thrown|itp_crush_through|itp_primary, itcf_throw_stone, 10000, weight(4)|weapon_length(30)|difficulty(0)|spd_rtng(100)|shoot_speed(70)|thrust_damage(35, pierce)|max_ammo(12), imodbits_none,[(ti_on_missile_hit, [(store_trigger_param_1, ":shooter"),(copy_position,pos51,pos1),(call_script, "script_magic_deliver_area_damage", ":shooter", 50, 5, 1),]),]+missile_distance_trigger,firearm_factions],
 
["imp_head_2", "imp head", [("red_demon_head_01",0)], itp_type_fullhelm|itp_covers_beard|itp_unique|itp_fit_to_head, 0, 4500, weight(2.75)|abundance(100)|head_armor(90)|body_armor(30)|leg_armor(0)|difficulty(9), imodbits_plate],
["imp_foot_2", "imp foot", [("red_demon_legs",0)], itp_type_foot_armor|itp_attach_armature|itp_unique, 0, 2570 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(65)|difficulty(9), imodbits_armor ],
["imp_hand_2", "imp hand", [("red_demon_hand_L",0)], itp_type_hand_armor|itp_unique, 0, 540, weight(1.25)|abundance(100)|body_armor(10)|difficulty(0), imodbits_armor ],
["imp_body_2", "imp body", [("red_demon_body",0)], itp_type_full_body_armor, 0, 20000, weight(26)|abundance(65)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(12), imodbits_armor ],
 
["arch_demon_axe_2", "Arch Demon scythe", [("CharonsCall",0)], itp_type_polearm|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_can_knock_down|itp_crush_through|itp_extra_penetration, itc_nodachi, 959, weight(6.5)|difficulty(8)|spd_rtng(75)|weapon_length(150)|swing_damage(100,pierce)|thrust_damage(0,pierce), imodbits_axe|imodbit_masterwork],
 
["demon_head", "toumingtou", [("toumingtou",0)], itp_type_fullhelm|itp_unique, 0, 4500, weight(2.75)|abundance(1)|head_armor(0)|body_armor(0)|leg_armor(0)|difficulty(9), imodbits_plate],
["demon_foot", "toumingtui", [("toumingtou",0)], itp_type_foot_armor|itp_attach_armature|itp_unique, 0, 2570 , weight(3.5)|abundance(1)|head_armor(0)|body_armor(0)|leg_armor(0)|difficulty(9), imodbits_armor ],
["demon_hand", "toumingshou", [("toumingtou",0)], itp_type_hand_armor|itp_unique, 0, 540, weight(1.25)|abundance(1)|body_armor(0)|difficulty(0), imodbits_armor ],

["horned_demon_body", "Horned Demon body", [("guaishou1",0)], itp_type_full_body_armor, 0, 20000, weight(26)|abundance(65)|head_armor(65)|body_armor(65)|leg_armor(65)|difficulty(12), imodbits_armor ],
#["horned_demon_sword", "Horned Demon_sword", [("toumingshen",0)], itp_can_knock_down|itp_crush_through|itp_type_one_handed_wpn|itp_primary|itp_unique, itc_gauntlet,610 , weight(5.5)|difficulty(13)|spd_rtng(120)| weapon_length(140)|swing_damage(35 , pierce)| thrust_damage(0 ,  pierce),imodbits_mace ],

["sandwraith_body", "Sandwraith", [("efreeti", 0)], itp_type_half_body_armor, 0, 2000, weight(30.)|abundance(100)|difficulty(15)|head_armor(0)|body_armor(70)|leg_armor(70), imodbits_armor], 
["sandwraith_hands", "Sandwraith_Hands", [("efreeti_handL", 0)], itp_type_hand_armor|itp_unique|itp_civilian, 0, 900, weight(1.)|abundance(150)|difficulty(20)|head_armor(0)|body_armor(10)|leg_armor(0), imodbits_none], 
["efreet_head", "efreet_head", [("efreetihead",0)], itp_type_fullhelm|itp_unique, 0, 4500, weight(2.75)|abundance(1)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(9), imodbits_plate],
["efreet_shield", "efreet__shield", [("toumingshen",0)], itp_type_shield|itp_unique,itcf_carry_round_shield, 1597, weight(4)|shield_hit_points(500)|body_armor(90)|spd_rtng(61)|shield_width(50), imodbits_shield ],
["efreet_sword", "efreet_sword", [("scimitar_return",0)], itp_type_one_handed_wpn|itp_primary|itp_unique, itc_scimitar,610 , weight(5.5)|difficulty(13)|spd_rtng(120)| weapon_length(100)|swing_damage(45 , pierce)| thrust_damage(0 ,  pierce),imodbits_sword_high ],

["arch_demon_body", "Arch Demon body", [("ArchDemon",0)], itp_type_full_body_armor, 0, 20000, weight(26)|abundance(65)|head_armor(120)|body_armor(120)|leg_armor(100)|difficulty(12), imodbits_armor ],
["arch_demon_axe", "Arch Demon Axe", [("thrud_axe",0)], itp_type_polearm|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_can_knock_down|itp_crush_through|itp_extra_penetration, itc_nodachi, 959, weight(6.5)|difficulty(8)|spd_rtng(125)|weapon_length(180)|swing_damage(60,pierce)|thrust_damage(0,pierce), imodbits_axe|imodbit_masterwork],
 
["balor_body", "Balor body", [("guaishou2",0)], itp_type_full_body_armor, 0, 20000, weight(26)|abundance(65)|head_armor(70)|body_armor(85)|leg_armor(70)|difficulty(12), imodbits_armor ],

["balor_sword", "Balor_sword", [("long_WAoRChaosAxeD",0)], itp_type_pistol|itp_crush_through|itp_primary|itp_next_item_as_melee|itp_is_magic_staff ,itcf_reload_pistol|itcf_shoot_pistol,
 25000 , weight(3.25)|difficulty(0)|spd_rtng(50) | shoot_speed(150) | thrust_damage(80 ,pierce)|max_ammo(3)|accuracy(100),imodbits_magic_staff,magic_cast_trigger , [fac_commoners] ], 
["balor_sword_melee", "Balor_sword", [("long_WAoRChaosAxeD",0)], itp_can_knock_down|itp_crush_through|itp_type_polearm|itp_primary|itp_unique|itp_bonus_against_shield, itc_nodachi|itcf_carry_sword_back,610 , weight(3.25)|difficulty(0)|spd_rtng(100)| weapon_length(180)|swing_damage(50 , pierce)| thrust_damage(50 , pierce),imodbits_mace ],
  
["pit_lord_sword", "pit_lord_sword", [("WAoRChaosAxeD",0),("WAoRChaosAxeD_inv",ixmesh_inventory),("WAoRChaosAxeD_inv",ixmesh_carry)], itp_type_pistol|itp_crush_through|itp_primary|itp_next_item_as_melee|itp_is_magic_staff ,itcf_reload_pistol|itcf_shoot_pistol,
 25000 , weight(3.25)|difficulty(0)|spd_rtng(50) | shoot_speed(100) | thrust_damage(80 ,pierce)|max_ammo(1)|accuracy(82),imodbits_magic_staff,magic_cast_trigger , [fac_commoners] ],  
["pit_lord_sword_melee", "pit_lord_sword", [("WAoRChaosAxeD",0)], itp_can_knock_down|itp_crush_through|itp_type_two_handed_wpn|itp_offset_lance|itp_primary|itp_unique, itc_nodachi|itcf_carry_spear,610 , weight(5.5)|difficulty(13)|spd_rtng(130)| weapon_length(140)|swing_damage(45 , pierce)| thrust_damage(45 , pierce),imodbits_mace ],
  
  
 ["magic_robe", "Apprentice_Robe", [("mage_robe_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0, 1000, weight(11)|abundance(40)|head_armor(0)|body_armor(21)|leg_armor(10)|difficulty(3),imodbits_cloth, [],[fac_commoners]],
 ["magic_robe_2_1", "RED Robe", [("wizard_robe_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0, 1000,weight(11)|abundance(50)|head_armor(0)|body_armor(31)|leg_armor(14)|difficulty(5),imodbits_cloth, [],[fac_commoners]],
 ["magic_robe_2_2", "black_Robe", [("robe_black",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0, 1000,weight(11)|abundance(50)|head_armor(0)|body_armor(31)|leg_armor(14)|difficulty(5),imodbits_cloth, [],[fac_neutral]],
 ["magic_robe_3", "Archmage_Robe", [("wizard_robe_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0, 1000,weight(11)|abundance(30)|head_armor(0)|body_armor(40)|leg_armor(18)|difficulty(6),imodbits_cloth, [],[fac_commoners]],
 
["wizard_hat", "Wizard Hat", [("wizard_red_hat",0)],  itp_merchandise|itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair ,0, 1000 , weight(1)|abundance(100)|head_armor(21)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [],[fac_commoners]],
["wizard_hat_2_1", "Wizard Hat", [("wizard_circelet_1",0)],  itp_merchandise|itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair ,0, 1300 , weight(1)|abundance(100)|head_armor(31)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [],[fac_commoners]],
["wizard_hat_2_2", "Wizard Hat", [("wizard_black_hat",0)],  itp_merchandise|itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair ,0, 1300 , weight(1)|abundance(100)|head_armor(31)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [],[fac_kingdom_8]],
["wizard_hat_3", "Wizard Hat", [("wizard_circelet_2",0)],  itp_merchandise|itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair ,0, 2020 , weight(1)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [],[fac_commoners]],


#["beholder", "beholder", [("beholder2",0)],  itp_type_head_armor|itp_civilian|itp_unique|itp_fit_to_head ,0, 1300 , weight(1)|abundance(100)|head_armor(50)|body_armor(50)|leg_armor(50)|difficulty(0) ,imodbits_cloth],
["beholder", "beholder", [("beholder2",0)], itp_type_body_armor|itp_covers_head|itp_covers_legs|itp_unique, 0, 20000, weight(26)|abundance(65)|head_armor(50)|body_armor(50)|leg_armor(50)|difficulty(0), imodbits_armor ],

["demon_body", "toumingshen", [("toumingtou",0)], itp_type_full_body_armor, 0, 20000, weight(26)|abundance(65)|head_armor(0)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_armor ],
["wizard_hood_2_2", "ranger hood", [("greehat1",0)],  itp_type_head_armor|itp_civilian ,0, 1300 , weight(1)|abundance(100)|head_armor(31)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth],
["wizard_hood_3", "ranger hood", [("greehat",0)],  itp_type_head_armor|itp_civilian ,0, 2020 , weight(1)|abundance(100)|head_armor(65)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth],
  
["death_scythe", "Death scythe", [("dk_ebony",0)], itp_type_polearm|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_can_knock_down|itp_crush_through|itp_extra_penetration, itc_nodachi, 95900, weight(6.5)|difficulty(21)|spd_rtng(100)|weapon_length(190)|swing_damage(55,pierce)|thrust_damage(0,pierce), imodbits_axe|imodbit_masterwork, [(ti_on_weapon_attack, [(store_trigger_param_1, ":shooter"),(agent_get_horse,":horse",":shooter"),(neg|gt,":horse",0),(copy_position,pos51,pos1),(call_script,"script_cf_agent_cleave",":shooter", 1, 0),])],],


["death_head", "Death head", [("barf_skull",0)], itp_type_fullhelm|itp_unique|itp_fit_to_head, 0, 4500, weight(2.75)|abundance(100)|head_armor(90)|body_armor(0)|leg_armor(0)|difficulty(9), imodbits_plate],
["death_hand", "Death hand", [("barf_skeleton_handL",0)], itp_type_hand_armor|itp_unique, 0, 540, weight(1.25)|abundance(100)|body_armor(15)|difficulty(0), imodbits_armor ],
["death_body", "Death body", [("death_body",0)], itp_type_body_armor|itp_covers_legs, 0, 20000, weight(3)|abundance(15)|head_armor(20)|body_armor(90)|leg_armor(65)|difficulty(0), imodbits_armor ],

["wight_body", "Wight body", [("xenoargh_remnant",0)], itp_type_full_body_armor, 0, 5000, weight(3)|abundance(15)|head_armor(40)|body_armor(40)|leg_armor(45)|difficulty(0), imodbits_armor ],
["wraith_body", "Wraith body", [("sishen_new",0)], itp_type_full_body_armor, 0, 20000, weight(3)|abundance(15)|head_armor(90)|body_armor(110)|leg_armor(65)|difficulty(0), imodbits_armor ],

["giant_greaves", "Steel Greaves", [("greaves_black",0)],  itp_type_foot_armor| itp_attach_armature,0, 
 4000 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(9) ,imodbits_armor , 
 [], euro_factions],
["giant_plate","Steel Plate Armor",[("cuirass_black",0)],itp_type_body_armor|itp_covers_legs,0,
 5738,breastplate_tier_3,imodbits_plate,],


["sg_human_small","Soul Gems_small", [("heaven_small",0)], itp_type_thrown|itp_primary|itp_no_pick_up_from_ground, itcf_throw_stone, 5000, weight(3)|difficulty(0)|abundance(120)|spd_rtng(97)| shoot_speed(70)| thrust_damage(100 ,  blunt)|max_ammo(1)|weapon_length(8),imodbits_none,
[(ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_troop_id,":troop_id", ":shooter"),
      
      (eq, "$g_mt_mode", 0),
      (troop_is_hero,":troop_id"),
      (assign,":spawn_troop_id",0),
      (store_random_in_range, ":number", 5, 8),
      (try_for_range,":unused",0,":number"),
        (store_random_in_range, ":spawn_troop_id", "trp_we_recruit", "trp_caravan_master"),
        (copy_position, pos51, pos5),
        (call_script,"script_cf_agent_spawn_agent_to_pos51", ":shooter", ":spawn_troop_id", 2),
      (try_end),
      (agent_unequip_item, ":shooter", "itm_sg_human_small"),
      (try_begin),
        (agent_get_troop_id,":troop_id", ":shooter"),
        (this_or_next|is_between, ":troop_id", companions_begin, companions_end),
        (eq, ":troop_id", 0),
        (troop_remove_item,":troop_id","itm_sg_human_small"),
      (try_end),
      
      
    ])],
],

["sg_purple_small","Demon's souls small", [("purple_small",0)], itp_type_thrown|itp_primary|itp_no_pick_up_from_ground, itcf_throw_stone, 5000, weight(3)|difficulty(0)|abundance(120)|spd_rtng(97)| shoot_speed(70)| thrust_damage(100 ,  blunt)|max_ammo(1)|weapon_length(8),imodbits_none,
[(ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_troop_id,":troop_id", ":shooter"),
      (eq, "$g_mt_mode", 0),
      (troop_is_hero,":troop_id"),
      (assign,":spawn_troop_id",0),
      
      (try_for_range,":unused",0,5),
        (store_random_in_range, ":ran", 0, 5),
        (try_begin),
          (eq,":ran",0),
          (assign,":spawn_troop_id","trp_demon_5"),
        (else_try),  
          (eq,":ran",1),
          (assign,":spawn_troop_id","trp_demon_5"),
        (else_try),  
          (eq,":ran",2),
          (assign,":spawn_troop_id","trp_demon_6"),
        (else_try),  
          (eq,":ran",3),
          (assign,":spawn_troop_id","trp_demon_6"),
        (else_try),  
          (eq,":ran",4),
          (assign,":spawn_troop_id","trp_demon_7"),
        (try_end),  
        (copy_position, pos51, pos5),
        (call_script,"script_cf_agent_spawn_agent_to_pos51", ":shooter", ":spawn_troop_id", 1),
      (try_end),
      (agent_unequip_item, ":shooter", "itm_sg_purple_small"),
      (try_begin),
        (agent_get_troop_id,":troop_id", ":shooter"),
        (this_or_next|is_between, ":troop_id", companions_begin, companions_end),
        (eq, ":troop_id", 0),
        (troop_remove_item,":troop_id","itm_sg_purple_small"),
      (try_end),
    ])],
],
["sg_black_small","Fallen soul_small", [("black_small",0)], itp_type_thrown|itp_primary|itp_no_pick_up_from_ground, itcf_throw_stone, 5000, weight(3)|difficulty(0)|abundance(120)|spd_rtng(97)| shoot_speed(70)| thrust_damage(100 ,  blunt)|max_ammo(1)|weapon_length(8),imodbits_none,
[(ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_troop_id,":troop_id", ":shooter"),
      (eq, "$g_mt_mode", 0),
      (troop_is_hero,":troop_id"),
      (assign,":spawn_troop_id",0),
      (try_for_range,":unused",0,5),
        (store_random_in_range, ":ran", 0, 5),
        (try_begin),
          (eq,":ran",0),
          (assign,":spawn_troop_id","trp_black_dragon"),
          (assign,":number",1),
        (else_try),  
          (eq,":ran",1),
          (assign,":spawn_troop_id","trp_death"),
          (assign,":number",1),
        (else_try),  
          (eq,":ran",2),
          (assign,":spawn_troop_id","trp_vampire_3"),
          (assign,":number",2),
        (else_try),  
          (eq,":ran",3),
          (assign,":spawn_troop_id","trp_lich_2"),
          (assign,":number",1),
        (else_try),  
          (eq,":ran",4),
          (assign,":spawn_troop_id","trp_death"),
          (assign,":number",1),
        (try_end),  
        (copy_position, pos51, pos5),
        (call_script,"script_cf_agent_spawn_agent_to_pos51", ":shooter", ":spawn_troop_id", ":number"),
      (try_end),
      (agent_unequip_item, ":shooter", "itm_sg_black_small"),
      (try_begin),
        (agent_get_troop_id,":troop_id", ":shooter"),
        (this_or_next|is_between, ":troop_id", companions_begin, companions_end),
        (eq, ":troop_id", 0),
        (troop_remove_item,":troop_id","itm_sg_black_small"),
      (try_end),
    ])],
],
["sg_green_small"," heart of nature small", [("green_small",0)], itp_type_thrown|itp_primary|itp_no_pick_up_from_ground, itcf_throw_stone, 5000, weight(3)|difficulty(0)|abundance(120)|spd_rtng(97)| shoot_speed(70)| thrust_damage(100 ,  blunt)|max_ammo(1)|weapon_length(8),imodbits_none,
[(ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_troop_id,":troop_id", ":shooter"),
      (eq, "$g_mt_mode", 0),
      (troop_is_hero,":troop_id"),
      (assign,":spawn_troop_id",0),
      (try_for_range,":unused",0,5),
        (store_random_in_range, ":ran", 0, 3),
        (try_begin),
          (eq,":ran",0),
          (assign,":spawn_troop_id","trp_ent_1"),
        (else_try),  
          (eq,":ran",1),
          (assign,":spawn_troop_id","trp_ent_2"),
        (else_try),  
          (eq,":ran",2),
          (assign,":spawn_troop_id","trp_green_dragon"),
        (else_try),  
          (eq,":ran",2),
          (assign,":spawn_troop_id","trp_green_dragon"),
        (try_end),  
        (copy_position, pos51, pos5),
        (call_script,"script_cf_agent_spawn_agent_to_pos51", ":shooter", ":spawn_troop_id", 1),
      (try_end),
      (agent_unequip_item, ":shooter", "itm_sg_green_small"),
      (try_begin),
        (agent_get_troop_id,":troop_id", ":shooter"),
        (this_or_next|is_between, ":troop_id", companions_begin, companions_end),
        (eq, ":troop_id", 0),
        (troop_remove_item,":troop_id","itm_sg_green_small"),
      (try_end),
    ])],
],
["sg_orange_small","wild heart_small", [("orange_small",0)], itp_type_thrown|itp_primary|itp_no_pick_up_from_ground, itcf_throw_stone, 5000, weight(3)|difficulty(0)|abundance(120)|spd_rtng(97)| shoot_speed(70)| thrust_damage(100 ,  blunt)|max_ammo(1)|weapon_length(8),imodbits_none,
[(ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_troop_id,":troop_id", ":shooter"),
      (eq, "$g_mt_mode", 0),
      (troop_is_hero,":troop_id"),
      (assign,":spawn_troop_id",0),
      (try_for_range,":unused",0,5),
        (store_random_in_range, ":ran", 0, 5),
        (assign,":number",1),
        (try_begin),
          (eq,":ran",0),
          (assign,":spawn_troop_id","trp_fire_dragon"),
        (else_try),  
          (eq,":ran",1),
          (assign,":spawn_troop_id","trp_cyclop"),
        (else_try),  
          (eq,":ran",2),
          (assign,":spawn_troop_id","trp_troll_2"),
        (else_try),  
          (eq,":ran",3),
          (assign,":spawn_troop_id","trp_troll_1"),
        (else_try),  
          (eq,":ran",4),
          (assign,":spawn_troop_id","trp_red_dragon"),
        (try_end),  
        (copy_position, pos51, pos5),
        (call_script,"script_cf_agent_spawn_agent_to_pos51", ":shooter", ":spawn_troop_id", ":number"),
      (try_end),
      (agent_unequip_item, ":shooter", "itm_sg_orange_small"),
      (try_begin),
        (agent_get_troop_id,":troop_id", ":shooter"),
        (this_or_next|is_between, ":troop_id", companions_begin, companions_end),
        (eq, ":troop_id", 0),
        (troop_remove_item,":troop_id","itm_sg_orange_small"),
      (try_end),
    ])],
],
["sg_yellow_small","Holy Spirit_small", [("yellow_small",0)], itp_type_thrown|itp_primary|itp_no_pick_up_from_ground, itcf_throw_stone, 5000, weight(3)|difficulty(0)|abundance(120)|spd_rtng(97)| shoot_speed(70)| thrust_damage(100 ,  blunt)|max_ammo(1)|weapon_length(8),imodbits_none,
[(ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_troop_id,":troop_id", ":shooter"),
      (eq, "$g_mt_mode", 0),
      (troop_is_hero,":troop_id"),
      (assign,":spawn_troop_id",0),
      (try_for_range,":unused",0,5),
        (store_random_in_range, ":ran", 0, 5),
        (try_begin),
          (eq,":ran",0),
          (assign,":spawn_troop_id","trp_ent_1"),
        (else_try),  
          (eq,":ran",1),
          (assign,":spawn_troop_id","trp_gold_dragon"),
        (else_try),  
          (eq,":ran",2),
          (assign,":spawn_troop_id","trp_angle"),
        (else_try),  
          (eq,":ran",3),
          (assign,":spawn_troop_id","trp_angle"),
        (else_try),  
          (eq,":ran",4),
          (assign,":spawn_troop_id","trp_archangle"),
        (try_end),  
        (copy_position, pos51, pos5),
        (call_script,"script_cf_agent_spawn_agent_to_pos51", ":shooter", ":spawn_troop_id", 1),
      (try_end),
      (agent_unequip_item, ":shooter", "itm_sg_yellow_small"),
      (try_begin),
        (agent_get_troop_id,":troop_id", ":shooter"),
        (this_or_next|is_between, ":troop_id", companions_begin, companions_end),
        (eq, ":troop_id", 0),
        (troop_remove_item,":troop_id","itm_sg_yellow_small"),
      (try_end),
    ])],
],
["sg_blue_small","storm jewel_small", [("blue_small",0)], itp_type_thrown|itp_primary|itp_no_pick_up_from_ground, itcf_throw_stone, 5000, weight(3)|difficulty(0)|abundance(120)|spd_rtng(97)| shoot_speed(70)| thrust_damage(100 ,  blunt)|max_ammo(1)|weapon_length(8),imodbits_none,
[(ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (agent_get_troop_id,":troop_id", ":shooter"),
      (eq, "$g_mt_mode", 0),
      (troop_is_hero,":troop_id"),
      (assign,":spawn_troop_id",0),
      (try_for_range,":unused",0,5),
        (store_random_in_range, ":ran", 0, 5),
        (assign,":number",1),
        (try_begin),
          (eq,":ran",0),
          (assign,":spawn_troop_id","trp_giant_2"),
          (assign,":number",3),
        (else_try),  
          (eq,":ran",1),
          (assign,":spawn_troop_id","trp_giant_3"),
          (assign,":number",3),
        (else_try),  
          (eq,":ran",2),
          (assign,":spawn_troop_id","trp_titan_2"),
        (else_try),  
          (eq,":ran",3),
          (assign,":spawn_troop_id","trp_lava_dragon"),
        (else_try),  
          (eq,":ran",4),
          (assign,":spawn_troop_id","trp_titan_1"),
          (assign,":number",2),
        (try_end),  
        (copy_position, pos51, pos5),
        (call_script,"script_cf_agent_spawn_agent_to_pos51", ":shooter", ":spawn_troop_id", ":number"),
      (try_end),
      (agent_unequip_item, ":shooter", "itm_sg_blue_small"),
      (try_begin),
        (agent_get_troop_id,":troop_id", ":shooter"),
        (this_or_next|is_between, ":troop_id", companions_begin, companions_end),
        (eq, ":troop_id", 0),
        (troop_remove_item,":troop_id","itm_sg_blue_small"),
      (try_end),
    ])],
],

["sg_human_big","Soul Gems_big", [("heaven_big",0)], itp_type_goods, 0, 15000,weight(3)|abundance(90),imodbits_none],
["sg_purple_big","Demon's souls small", [("purple_big",0)], itp_type_goods, 0, 15000,weight(3)|abundance(90),imodbits_none],
["sg_black_big","Fallen soul_big", [("black_big",0)], itp_type_goods, 0, 15000,weight(3)|abundance(90),imodbits_none],
["sg_green_big"," heart of nature small", [("green_big",0)], itp_type_goods, 0, 15000,weight(3)|abundance(90),imodbits_none],
["sg_orange_big","wild heart_big", [("orange_big",0)], itp_type_goods, 0, 15000,weight(3)|abundance(90),imodbits_none],
["sg_yellow_big","Holy Spirit_big", [("yellow_big",0)], itp_type_goods, 0, 15000,weight(3)|abundance(90),imodbits_none],
["sg_blue_big","storm jewel_big", [("blue_big",0)], itp_type_goods, 0, 15000,weight(3)|abundance(90),imodbits_none],

["sg_blood","Flame essence", [("blood_small",0)], itp_type_goods, 0, 10000,weight(3)|abundance(90),imodbits_none],


["sulfur", "Sulfur", [("wax", 0)], itp_type_goods|itp_merchandise, 0, 500, weight(10.)|abundance(100)|max_ammo(0)|food_quality(0), imodbits_none], 
["crystal", "Crystal", [("Crystal", 0)], itp_type_goods|itp_merchandise, 0, 500, weight(10.)|abundance(100)|max_ammo(0)|food_quality(0), imodbits_none], 
["mercury", "Mercury", [("mercury", 0)], itp_type_goods|itp_merchandise, 0, 500, weight(10.)|abundance(100)|max_ammo(0)|food_quality(0), imodbits_none], 
["silver", "Silver", [("Silver2", 0)], itp_type_goods|itp_merchandise, 0, 1000, weight(50.)|abundance(100)|max_ammo(0)|food_quality(0), imodbits_none], 
["diamonds", "Diamonds", [("Diamonds2", 0)], itp_type_goods, 0, 10000, weight(10.)|abundance(30)|max_ammo(0)|food_quality(0), imodbits_none], 
["clay", "Graveyard_Soil", [("Clay", 0)], itp_type_goods|itp_merchandise, 0, 100, weight(40.)|abundance(100)|max_ammo(0)|food_quality(0), imodbits_none], 
["skeleton", "Human_skeleton", [("skeleton_a", 0)], itp_type_goods, 0, 1, weight(55.)|abundance(100)|max_ammo(54)|food_quality(70), imodbits_none], 

["green_dragon_body", "green_dragon body", [("green_drake_body",0)], itp_type_full_body_armor, 0, 25000, weight(30)|abundance(30)|head_armor(0)|body_armor(80)|leg_armor(50)|difficulty(18), imodbits_plate ],
["green_dragon_shield", "green_dragon_shield", [("toumingshen",0)], itp_type_shield,itcf_carry_round_shield|itp_unique, 1597, weight(4)|shield_hit_points(500)|body_armor(90)|spd_rtng(61)|shield_width(50), imodbits_shield ],
["green_dragon_sword", "green_dragon_sword", [("toumingshen",0)], itp_type_pistol|itp_primary|itp_next_item_as_melee|itp_is_magic_staff|itp_unique|itp_no_pick_up_from_ground ,itcf_reload_pistol|itcf_shoot_pistol,
 25000 , weight(3.25)|difficulty(0)|spd_rtng(50) | shoot_speed(80) | thrust_damage(80 ,pierce)|max_ammo(1)|accuracy(82),imodbits_magic_staff,magic_cast_trigger , [fac_commoners] ],  
["green_dragon_sword_melee", "green_dragon_sword", [("toumingshen",0)], itp_can_knock_down|itp_crush_through|itp_type_one_handed_wpn|itp_primary|itp_unique|itp_no_pick_up_from_ground, itc_gauntlet|itcf_carry_mace_left_hip,610 , weight(5.5)|difficulty(13)|spd_rtng(100)| weapon_length(150)|swing_damage(45 , pierce)| thrust_damage(0 ,  pierce),imodbits_mace,dragon_weapon_trigger ],

["red_dragon_body", "red_dragon body", [("red_drake_body",0)], itp_type_full_body_armor, 0, 25000, weight(30)|abundance(30)|head_armor(0)|body_armor(90)|leg_armor(50)|difficulty(18), imodbits_plate ],

["red_dragon_sword", "red_dragon_sword", [("toumingshen",0)], itp_type_pistol|itp_primary|itp_next_item_as_melee|itp_is_magic_staff|itp_unique|itp_no_pick_up_from_ground ,itcf_reload_pistol|itcf_shoot_pistol,
 25000 , weight(3.25)|difficulty(0)|spd_rtng(50) | shoot_speed(90) | thrust_damage(80 ,pierce)|max_ammo(1)|accuracy(100),imodbits_magic_staff,magic_cast_trigger+flame_cast_trigger , [fac_commoners] ],  
["red_dragon_sword_melee", "red_dragon_sword", [("toumingshen",0)], itp_can_knock_down|itp_crush_through|itp_type_one_handed_wpn|itp_primary|itp_unique, itc_gauntlet|itcf_carry_mace_left_hip,610 , weight(5.5)|difficulty(13)|spd_rtng(90)| weapon_length(150)|swing_damage(50 , pierce)| thrust_damage(0 ,  pierce),imodbits_mace,dragon_weapon_trigger ],

["black_dragon_body", "black_dragon body", [("mutare_drake_body",0)], itp_type_full_body_armor, 0, 25000, weight(30)|abundance(30)|head_armor(0)|body_armor(100)|leg_armor(50)|difficulty(18), imodbits_plate ],

["black_dragon_sword", "black_dragon_sword", [("toumingshen",0)], itp_type_pistol|itp_primary|itp_next_item_as_melee|itp_is_magic_staff|itp_unique|itp_no_pick_up_from_ground ,itcf_reload_pistol|itcf_shoot_pistol,
 25000 , weight(3.25)|difficulty(0)|spd_rtng(70) | shoot_speed(90) | thrust_damage(80 ,pierce)|max_ammo(1)|accuracy(82),imodbits_magic_staff,magic_cast_trigger , [fac_commoners] ],  
["black_dragon_sword_melee", "black_dragon_sword", [("toumingshen",0)], itp_can_knock_down|itp_crush_through|itp_type_one_handed_wpn|itp_primary|itp_unique, itc_gauntlet|itcf_carry_mace_left_hip,610 , weight(5.5)|difficulty(13)|spd_rtng(100)| weapon_length(150)|swing_damage(55 , pierce)| thrust_damage(0 ,  pierce),imodbits_mace,dragon_weapon_trigger ],

["gold_dragon_body", "gold_dragon body", [("gold_drake_body",0)], itp_type_full_body_armor, 0, 25000, weight(30)|abundance(30)|head_armor(0)|body_armor(120)|leg_armor(50)|difficulty(18), imodbits_plate ],

["gold_dragon_sword", "gold_dragon_sword", [("toumingshen",0)], itp_type_pistol|itp_primary|itp_next_item_as_melee|itp_is_magic_staff|itp_unique|itp_no_pick_up_from_ground ,itcf_reload_pistol|itcf_shoot_pistol,
 25000 , weight(3.25)|difficulty(0)|spd_rtng(70) | shoot_speed(90) | thrust_damage(80 ,pierce)|max_ammo(3)|accuracy(99),imodbits_magic_staff,magic_cast_trigger+flame_cast_trigger , [fac_commoners] ],  
["gold_dragon_sword_melee", "gold_dragon_sword", [("toumingshen",0)], itp_can_knock_down|itp_type_one_handed_wpn|itp_primary|itp_unique, itc_gauntlet|itcf_carry_mace_left_hip,610 , weight(5.5)|difficulty(13)|spd_rtng(100)| weapon_length(120)|swing_damage(35 , pierce)| thrust_damage(0 ,  pierce),imodbits_mace,dragon_weapon_trigger ],

["fire_dragon_body", "fire_dragon body", [("fire_drake_body",0)], itp_type_full_body_armor, 0, 25000, weight(30)|abundance(30)|head_armor(0)|body_armor(90)|leg_armor(50)|difficulty(18), imodbits_plate ],

["fire_dragon_sword", "fire_dragon_sword", [("toumingshen",0)], itp_type_pistol|itp_primary|itp_next_item_as_melee|itp_is_magic_staff|itp_unique|itp_no_pick_up_from_ground ,itcf_reload_pistol|itcf_shoot_pistol,
 25000 , weight(3.25)|difficulty(0)|spd_rtng(50) | shoot_speed(90) | thrust_damage(80 ,pierce)|max_ammo(1)|accuracy(100),imodbits_magic_staff,magic_cast_trigger+flame_cast_trigger , [fac_commoners] ],  
["fire_dragon_sword_melee", "fire_dragon_sword", [("toumingshen",0)], itp_can_knock_down|itp_crush_through|itp_type_one_handed_wpn|itp_primary|itp_unique, itc_gauntlet|itcf_carry_mace_left_hip,610 , weight(5.5)|difficulty(13)|spd_rtng(90)| weapon_length(150)|swing_damage(60 , pierce)| thrust_damage(0 ,  pierce),imodbits_mace,dragon_weapon_trigger ],

["lava_dragon_body", "lava_dragon body", [("lava_drake_body",0)], itp_type_full_body_armor, 0, 25000, weight(30)|abundance(30)|head_armor(0)|body_armor(120)|leg_armor(60)|difficulty(18), imodbits_plate ],

["lava_dragon_sword", "lava_dragon_sword", [("toumingshen",0)], itp_type_pistol|itp_primary|itp_next_item_as_melee|itp_is_magic_staff|itp_unique|itp_no_pick_up_from_ground ,itcf_reload_pistol|itcf_shoot_pistol,
 25000 , weight(3.25)|difficulty(0)|spd_rtng(70) | shoot_speed(60) | thrust_damage(80 ,pierce)|max_ammo(1)|accuracy(82),imodbits_magic_staff,magic_cast_trigger+flame_cast_trigger , [fac_commoners] ],  
["lava_dragon_sword_melee", "lava_dragon_sword", [("toumingshen",0)], itp_can_knock_down|itp_crush_through|itp_type_one_handed_wpn|itp_primary|itp_unique, itc_gauntlet|itcf_carry_mace_left_hip,610 , weight(5.5)|difficulty(13)|spd_rtng(100)| weapon_length(150)|swing_damage(75 , pierce)| thrust_damage(0 ,  pierce),imodbits_mace,dragon_weapon_trigger ],

["bone_dragon_body", "bone_dragon body", [("bone_dragon",0)], itp_type_full_body_armor, 0, 25000, weight(30)|abundance(30)|head_armor(0)|body_armor(90)|leg_armor(50)|difficulty(18), imodbits_plate ],

["bone_dragon_sword_melee", "bone_dragon_sword", [("toumingshen",0)], itp_can_knock_down|itp_crush_through|itp_type_one_handed_wpn|itp_primary|itp_unique, itc_gauntlet|itcf_carry_mace_left_hip,610 , weight(5.5)|difficulty(13)|spd_rtng(90)| weapon_length(150)|swing_damage(50 , pierce)| thrust_damage(0 ,  pierce),imodbits_mace ],

["ghost_dragon_body", "ghost_dragon body", [("ghost_dragon",0)], itp_type_full_body_armor, 0, 25000, weight(30)|abundance(30)|head_armor(0)|body_armor(100)|leg_armor(50)|difficulty(18), imodbits_plate ],

["ghost_dragon_sword_melee", "ghost_dragon_sword", [("toumingshen",0)], itp_can_knock_down|itp_crush_through|itp_type_one_handed_wpn|itp_primary|itp_unique, itc_gauntlet|itcf_carry_mace_left_hip,610 , weight(5.5)|difficulty(13)|spd_rtng(150)| weapon_length(120)|swing_damage(55 , pierce)| thrust_damage(0 ,  pierce),imodbits_mace,[(ti_on_weapon_attack, [(store_trigger_param_1, ":shooter"),(agent_get_horse,":horse",":shooter"),(neg|gt,":horse",0),(copy_position,pos51,pos1),(call_script,"script_cf_agent_cleave",":shooter", 1, 0),])] ],

["lich_dragon_body", "lich_dragon body", [("lich_dragon",0)], itp_type_full_body_armor, 0, 25000, weight(30)|abundance(30)|head_armor(0)|body_armor(120)|leg_armor(50)|difficulty(18), imodbits_plate ],

["lich_dragon_sword", "lich_dragon_sword", [("toumingshen",0)], itp_type_pistol|itp_primary|itp_next_item_as_melee|itp_is_magic_staff|itp_unique|itp_no_pick_up_from_ground ,itcf_reload_pistol|itcf_shoot_pistol,
 25000 , weight(3.25)|difficulty(0)|spd_rtng(70) | shoot_speed(90) | thrust_damage(80 ,pierce)|max_ammo(3)|accuracy(99),imodbits_magic_staff,magic_cast_trigger+flame_cast_trigger , [fac_commoners] ],  
["lich_dragon_sword_melee", "lich_dragon_sword", [("toumingshen",0)], itp_can_knock_down|itp_type_one_handed_wpn|itp_primary|itp_unique, itc_gauntlet|itcf_carry_mace_left_hip,610 , weight(5.5)|difficulty(13)|spd_rtng(150)| weapon_length(120)|swing_damage(55 , pierce)| thrust_damage(0 ,  pierce),imodbits_mace,[(ti_on_weapon_attack, [(store_trigger_param_1, ":shooter"),(agent_get_horse,":horse",":shooter"),(neg|gt,":horse",0),(copy_position,pos51,pos1),(call_script,"script_cf_agent_cleave",":shooter", 1, 0),])] ],


 ["black_dragon_breath", "death_cloud Scroll", [("bullet_1",0),("huojian_fly_green",ixmesh_flying_ammo)], itp_type_bullets|itp_unique, 0,
  275, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(70,cut)|max_ammo(30),
  imodbits_missile, cast_magic_weakness+cast_magic_soul_Leech , firearm_factions ],
 ["green_dragon_breath", "death_cloud Scroll", [("bullet_1",0),("huojian_fly_green",ixmesh_flying_ammo)], itp_type_bullets|itp_unique, 0,
  275, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(70,cut)|max_ammo(30),
  imodbits_missile, cast_magic_poison , firearm_factions ],
 ["green_dragon_breath_2", "death_cloud Scroll", [("bullet_1",0),("huojian_fly_green",ixmesh_flying_ammo)], itp_type_bullets|itp_unique, 0,
  275, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(70,cut)|max_ammo(6),
  imodbits_missile, cast_magic_death_cloud , firearm_factions ],

 ["red_dragon_breath", "_fireball_Scroll", [("bullet_1",0),("guangjian_fly3",ixmesh_flying_ammo)], itp_type_bullets|itp_unique, 0,
  275, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(35,cut)|max_ammo(20),
  imodbits_missile, cast_magic_fire_ball+missile_distance_trigger , firearm_factions ],
 ["red_dragon_breath_2", "death_cloud Scroll", [("bullet_1",0),("guangjian_fly3",ixmesh_flying_ammo)], itp_type_bullets|itp_unique, 0,
  275, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(70,cut)|max_ammo(15),
  imodbits_missile, cast_magic_incediary_cloud_2 , firearm_factions ],
  
 ["gold_dragon_breath", "_fireball_Scroll", [("bullet_1",0),("guangjian_fly3",ixmesh_flying_ammo)], itp_type_bullets|itp_unique, 0,
  275, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(35,cut)|max_ammo(30),
  imodbits_missile, cast_magic_column_of_fire+cast_magic_fire_ball+missile_distance_trigger , firearm_factions ],

 ["fire_dragon_breath", "_fireball_Scroll", [("bullet_1",0),("guangjian_fly3",ixmesh_flying_ammo)], itp_type_bullets|itp_unique, 0,
  275, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(35,cut)|max_ammo(10),
  imodbits_missile, cast_magic_fire_ball_2+missile_distance_trigger , firearm_factions ],
 ["lava_dragon_breath", "death_cloud Scroll", [("bullet_1",0),("guangjian_fly3",ixmesh_flying_ammo)], itp_type_bullets|itp_unique, 0,
  275, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(70,cut)|max_ammo(5),
  imodbits_missile, cast_magic_incediary_cloud , firearm_factions ],

["behemoth_armor", "Behemoth'armor", [("rancor",0)], itp_type_full_body_armor ,0, 6360,weight(1)|abundance(60)|head_armor(60)|body_armor(60)|leg_armor(60)|difficulty(14),imodbits_armor ],

["angle_body", "angle_body", [("tt",0)], itp_type_full_body_armor, 0, 20000, weight(26)|abundance(65)|head_armor(70)|body_armor(90)|leg_armor(70)|difficulty(12), imodbits_armor ],
["angle_shield", "angle_shield", [("tianshijian2",0)], itp_type_shield,itcf_carry_round_shield, 1597, weight(4)|shield_hit_points(500)|body_armor(90)|spd_rtng(61)|abundance(60)|shield_width(60), imodbits_shield ],
["angle_sword", "angle_sword", [("tianshijian1",0)], itp_type_one_handed_wpn|itp_primary|itp_crush_through|itp_extra_penetration, itc_morningstar,610 , weight(5.5)|difficulty(13)|spd_rtng(95)|abundance(30)| weapon_length(160)|swing_damage(45 , pierce)| thrust_damage(100 ,  pierce),imodbits_mace ],

["archangle_body", "archangle_body", [("tts",0)], itp_type_full_body_armor, 0, 20000, weight(26)|abundance(65)|head_armor(90)|body_armor(120)|leg_armor(90)|difficulty(12), imodbits_armor ],
["archangle_shield", "archangle_shield", [("antianshijian2",0)], itp_type_shield,itcf_carry_round_shield, 1597, weight(4)|shield_hit_points(500)|body_armor(90)|spd_rtng(61)|abundance(60)|shield_width(80), imodbits_shield ],
["archangle_sword", "archangle_sword", [("antianshijian1",0)], itp_type_one_handed_wpn|itp_primary|itp_crush_through|itp_extra_penetration, itc_morningstar,610 , weight(5.5)|difficulty(13)|spd_rtng(100)|abundance(30)| weapon_length(160)|swing_damage(60 , pierce)| thrust_damage(100 ,  pierce),imodbits_mace ],

 ["angle_sword_2", "heaven_fist Scroll", [("tianshijian1",0),("tianshijian1",ixmesh_flying_ammo)], itp_type_thrown|itp_is_magic_staff|itp_primary, itcf_throw_stone,
  6000, weight(2.25)|abundance(60)|spd_rtng(65)|shoot_speed(50)|weapon_length(3)|thrust_damage(100,pierce)|max_ammo(10),
  imodbits_none, cast_magic_column_of_fire+cast_magic_heaven_fist_2, [fac_demon_hunters, fac_hospitalier_knights] ],
 ["archangle_sword_2", "heaven_fist_Scroll", [("antianshijian1",0),("antianshijian1",ixmesh_flying_ammo)], itp_merchandise|itp_type_thrown|itp_is_magic_staff|itp_primary, itcf_throw_stone,
  12000, weight(2.25)|abundance(30)|spd_rtng(65)|shoot_speed(70)|weapon_length(3)|thrust_damage(100,pierce)|max_ammo(10),
  imodbits_none, cast_magic_column_of_fire+cast_magic_heaven_fist_3, [fac_demon_hunters, fac_hospitalier_knights] ],

["infreno_armor", "infreno_Paws", [("shikuilei",0)], itp_type_full_body_armor ,0, 6360,lamellar_armor_tier_2,imodbits_armor ],
["infreno_right_claw", "infreno_Right_Claw", [("shiyoushou",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_unique|itp_bonus_against_shield|itp_no_pick_up_from_ground, itc_gauntlet, 0 , weight(1.5)|difficulty(100)|spd_rtng(100)| weapon_length(60)|swing_damage(40 , blunt)| thrust_damage(0 ,  blunt),imodbits_axe ],
["infreno_left_claw", "infreno_Left_Claw", [("shizuoshou",0)], itp_type_shield|itp_unique, itcf_carry_round_shield,  2091 , weight(4)|difficulty(100)|shield_hit_points(999)|body_armor(125)|spd_rtng(61)|shield_width(60),imodbits_shield ],

["huge_infreno_armor", "infreno_Paws", [("shikuilei",0)], itp_type_full_body_armor ,0, 12769,full_plate_armor_tier_4,imodbits_armor ],
["huge_infreno_right_claw", "infreno_Right_Claw", [("shiyoushou",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_unique|itp_bonus_against_shield|itp_no_pick_up_from_ground, itc_gauntlet, 0 , weight(1.5)|difficulty(100)|spd_rtng(95)| weapon_length(60)|swing_damage(50 , blunt)| thrust_damage(0 ,  blunt),imodbits_axe ],
["huge_infreno_left_claw", "infreno_Left_Claw", [("shizuoshou",0)], itp_type_shield|itp_unique, itcf_carry_round_shield,  2091 , weight(4)|difficulty(100)|shield_hit_points(999)|body_armor(125)|spd_rtng(61)|shield_width(60),imodbits_shield ],

["stone_golemarmor", "stone_golem_body", [("stone_golem_torso",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_unique ,0, 6360,weight(1)|abundance(60)|head_armor(0)|body_armor(60)|leg_armor(0)|difficulty(14),imodbits_armor ],
["stone_golemboots", "stone_golem_feet", [("stone_golem_feet",0)], itp_type_foot_armor|itp_civilian|itp_unique ,0, 
 2376 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(60)|difficulty(0) ,imodbits_cloth,],
["stone_golemgloves","stone_golem_hand", [("stone_golem_handL",0)], itp_type_hand_armor|itp_unique,0, 
 820, weight(1)|abundance(100)|body_armor(15)|difficulty(0),imodbits_armor, ],
["stone_golemhelm", "stone_golem_head", [("stone_golem_head", 0)], itp_type_fullhelm|itp_unique, 0, 75, weight(2)|abundance(10)|head_armor(60)|body_armor(0)|leg_armor(0), imodbits_none ],

["iron_golemarmor", "iron_golem_body", [("iron_golem_body",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_unique ,0, 6360,weight(1)|abundance(60)|head_armor(0)|body_armor(90)|leg_armor(0)|difficulty(14),imodbits_armor ],
["iron_golemboots", "silver_golem_feet", [("iron_golem_legs",0)], itp_type_foot_armor|itp_civilian|itp_unique ,0, 
 2376 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(90)|difficulty(0) ,imodbits_cloth,],
["iron_golemgloves","silver_golem_hand", [("iron_golem_hand_L",0)], itp_type_hand_armor|itp_unique,0, 
 820, weight(1)|abundance(100)|body_armor(15)|difficulty(0),imodbits_armor, ],
["iron_golemhelm", "silver_golem_head", [("iron_golem_head", 0)], itp_type_fullhelm|itp_unique, 0, 75, weight(2)|abundance(10)|head_armor(90)|body_armor(0)|leg_armor(0), imodbits_none ],

["silver_golemarmor", "silver_golem_body", [("silver_golem_body",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_unique ,0, 6360,weight(1)|abundance(60)|head_armor(0)|body_armor(70)|leg_armor(0)|difficulty(14),imodbits_armor ],
["silver_golemboots", "silver_golem_feet", [("silver_golem_feet",0)], itp_type_foot_armor|itp_civilian|itp_unique ,0, 
 2376 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(70)|difficulty(0) ,imodbits_cloth,],
["silver_golemgloves","silver_golem_hand", [("silver_golem_handL",0)], itp_type_hand_armor|itp_unique,0, 
 820, weight(1)|abundance(100)|body_armor(15)|difficulty(0),imodbits_armor, ],
["silver_golemhelm", "silver_golem_head", [("silver_golem_head", 0)], itp_type_fullhelm|itp_unique, 0, 75, weight(2)|abundance(10)|head_armor(70)|body_armor(0)|leg_armor(0), imodbits_none ],


["gargoyle_body", "gargoyle body", [("gargoyle",0)], itp_type_full_body_armor, 0, 50000, weight(3)|abundance(15)|head_armor(120)|body_armor(90)|leg_armor(90)|difficulty(0), imodbits_armor ],

["banshen_body", "banshen_body", [("banshen_body",0)], itp_type_full_body_armor ,0, 6360,weight(1)|abundance(60)|head_armor(80)|body_armor(80)|leg_armor(0)|difficulty(14),imodbits_armor ],
["banshen_leg", "banshen_leg", [("banshen_legL",0)], itp_type_foot_armor|itp_civilian|itp_unique ,0, 
 2376 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(60)|difficulty(0) ,imodbits_cloth,],
["banshen_hand","banshen_hand", [("banshen_handL",0)], itp_type_hand_armor|itp_unique,0, 
 820, weight(1)|abundance(100)|body_armor(10)|difficulty(0),imodbits_armor, ],
["banshen_axe", "banshen_axe", [("banshen_fu",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_bonus_against_shield, itc_morningstar, 0 , weight(1.5)|difficulty(100)|spd_rtng(100)| weapon_length(100)|swing_damage(60 , pierce)| thrust_damage(0 ,  blunt),imodbits_axe ],
["banshen_shield", "banshen_shield", [("fix_banshen_shield",0)], itp_type_shield, itcf_carry_kite_shield,  2091 , weight(4)|difficulty(10)|shield_hit_points(999)|body_armor(125)|spd_rtng(100)|shield_width(50)|shield_height(100),imodbits_shield ],

["rhun_armor_1","Demon_Light_Battlewear",[("RhunArmorLight1",0)],itp_type_body_armor|itp_covers_legs,0,300,cloth_tier_2,imodbits_cloth],
["rhun_armor_2","Demon_Light_Battlewear",[("RhunArmorLight4",0)],itp_type_body_armor|itp_covers_legs,0,940,cloth_tier_3,imodbits_cloth],

["rhun_armor_3","Demon_Medium_Battlewear",[("Armor_Chaos_1",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,2704,mail_armor_tier_2,imodbits_armor, [], [fac_kingdom_9,fac_demon]],
["rhun_armor_4","Demon_Medium_Battlewear",[("Armor_Chaos_2",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,4035,mail_armor_tier_3,imodbits_armor, [], [fac_kingdom_9]],

["rhun_armor_5","Demon_Heavy_Battlewear",[("Armor_Chaos_3",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,6360,lamellar_armor_tier_2,imodbits_armor, [], [fac_kingdom_9]],
["rhun_armor_6","Demon_Heavy_Battlewear",[("Armor_Chaos_4",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,7876,lamellar_armor_tier_3,imodbits_armor, [], [fac_kingdom_9]],

["rhun_armor_6_1","Chaos_Warrior_Armour",[("Armor_Crusher_1",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,9216,full_plate_armor_tier_2,imodbits_plate, [], [fac_kingdom_9]],
["rhun_armor_6_3","Chaos_Warrior_Armour",[("Armor_Chaos_Warrior",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,9216,full_plate_armor_tier_2e,imodbits_plate, [], [fac_kingdom_9]],
["rhun_armor_6_2", "Chaos_Warrior_Armour", [("Armor_Crusher_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 12769,full_plate_armor_tier_4,imodbits_plate, [], [fac_kingdom_9]],

["rhun_armor_7","Chaos_Warrior_Armour",[("Armor_Elite_Chaos_02",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,10868,full_plate_armor_tier_3,imodbits_plate, [], [fac_kingdom_9,fac_kingdom_10]],
["rhun_armor_8", "Chaos_Knight_Armour", [("Armor_Elite_Chaos_01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 12769,full_plate_armor_tier_4,imodbits_plate, [], [fac_kingdom_9,fac_kingdom_10]],
["rhun_armor_9","Chaos_Chosen_Armour",[("Armor_Elite_Chaos_03",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,18000, weight(30)|abundance(20)|head_armor(0)|body_armor(86)|leg_armor(45)|difficulty(18),imodbits_plate, [], [fac_kingdom_9]],

["chaos_gauntlets_1","Chaos_Gauntlets", [("Glove_Crusher_L",0)], itp_merchandise|itp_type_hand_armor,0,  820, weight(1)|abundance(100)|body_armor(10)|difficulty(0),imodbits_armor, [], [fac_kingdom_9]],
["chaos_gauntlets","Chaos_Gauntlets", [("Glove_Chaos_L",0)], itp_merchandise|itp_type_hand_armor,0,  820, weight(1)|abundance(100)|body_armor(10)|difficulty(0),imodbits_armor, [], [fac_kingdom_9,fac_kingdom_10]],

["rhun_helm_1","Demon_Round_Masked_Helm",[("RhunHelmRound1",0)],itp_merchandise|itp_type_head_armor,0,1400,weight(2)|head_armor(30)|difficulty(0),imodbits_armor, [], [fac_kingdom_9,fac_demon]],
["rhun_helm_2","Demon_Horned_Pot",[("RhunHelmConical1",0)],itp_merchandise|itp_type_head_armor,0,1500,weight(2.5)|head_armor(40)|difficulty(0),imodbits_armor, [], [fac_kingdom_9]],
["rhun_helm_3","Demon_Horned_Pot",[("RhunHelmPot3",0)],itp_merchandise|itp_type_head_armor,0,1600,weight(3)|head_armor(50)|difficulty(0),imodbits_armor, [], [fac_kingdom_9]],
["rhun_helm_4","Demon_Horde_Horned_Helm",[("RhunHelmHorde2",0)],itp_merchandise|itp_type_head_armor,0,1800,weight(2.5)|head_armor(60)|difficulty(0),imodbits_armor, [], [fac_undeads_2]],
["rhun_helm_5","Demon_Chieftain_Helm",[("RhunHelmDeathDealer1",0)],itp_merchandise|itp_type_head_armor,0,2500,weight(3.5)|head_armor(70)|difficulty(0),imodbits_armor, [], [fac_kingdom_5]],
["rhun_helm_6","Demon_Chieftain_Helm",[("helmetdragonplate",0)],itp_merchandise|itp_type_head_armor,0,3000,weight(4)|head_armor(75)|difficulty(0),imodbits_armor, [], [fac_undeads_2]],

["rhun_helm_7_2", "Chaos_Warrior_Helm", [("Helm_A_Elite_Crusher_B_01", 0)], itp_merchandise|itp_type_head_armor|itp_covers_head, 0, 4740, weight(2.75)|abundance(100)|difficulty(11)|head_armor(85)|body_armor(0)|leg_armor(0), imodbits_plate, [], [fac_kingdom_9]], 
["rhun_helm_7", "Chaos_Warrior_Helm", [("Helm_A_Elite_Crusher_A_01", 0)], itp_merchandise|itp_type_head_armor|itp_covers_head, 0, 4740, weight(2.75)|abundance(100)|difficulty(11)|head_armor(85)|body_armor(0)|leg_armor(0), imodbits_plate, [], [fac_kingdom_9]], 
["rhun_helm_8", "Chaos_Knight_Helm", [("Helm_A_Elite_Chaos_Warrior_B_01", 0)], itp_merchandise|itp_type_head_armor|itp_covers_head, 0, 4740, weight(2.75)|abundance(100)|difficulty(11)|head_armor(85)|body_armor(0)|leg_armor(0), imodbits_plate, [], [fac_kingdom_9]], 
["rhun_helm_9", "Chaos_Chosen_Helm", [("Helm_A_Elite_Chaos_Warrior_A_01", 0)], itp_merchandise|itp_type_head_armor|itp_covers_head, 0, 4740, weight(2.75)|abundance(100)|difficulty(11)|head_armor(85)|body_armor(0)|leg_armor(0), imodbits_plate, [], [fac_kingdom_9]], 

["chaos_leg_1", "Chaos Knight_leg", [("Boots_Chaos1",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature ,0,  2376 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(35)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_9]],
["chaos_leg_2", "Chaos Knight_leg", [("Boots_Chaos2",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature ,0,  2376 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(40)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_9,fac_kingdom_10]],
["chaos_leg_3", "Chaos Knight_leg", [("Boots_Chaos3",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature ,0,  2376 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(45)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_9]],



["demon_knight_plate", "Khorne Knight_plate", [("Armor_Elite_Khorne",0)], merc_body_armor, 0, 20000, weight(30)|abundance(20)|head_armor(13)|body_armor(95)|leg_armor(45)|difficulty(18), imodbits_good_plate, [], [fac_kingdom_9,fac_demon]],
["demon_knight_head", "Khorne Knight Helm", [("Helm_Khorne",0)], itp_merchandise|itp_type_fullhelm, 0, 
 5400 , weight(2.75)|abundance(100)|head_armor(95)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_good_plate, [], [fac_kingdom_9,fac_demon]],
["demon_knight_head_2", "Khorne Knight Helm", [("Helm_khorne3",0)], itp_merchandise|itp_type_fullhelm, 0, 
 5400 , weight(2.75)|abundance(100)|head_armor(95)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_good_plate, [], [fac_kingdom_9,fac_demon]],
["demon_knight_leg", "Khorne Knight_leg", [("Boots_Khorne",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature ,0,  2376 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(50)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_9,fac_demon]],
["demon_knight_hand","Khorne Knight_hand", [("Glove_Khorne_L",0)], itp_merchandise|itp_type_hand_armor,0,  820, weight(1)|abundance(100)|body_armor(10)|difficulty(0),imodbits_armor, [], [fac_kingdom_9,fac_demon]],

["nurgle_chosen_armor", "Nurgle Knight_plate", [("Armor_Elite_Nurgle",0)], merc_body_armor, 0, 20000, weight(30)|abundance(20)|head_armor(13)|body_armor(95)|leg_armor(45)|difficulty(18), imodbits_good_plate, [], [fac_kingdom_9,fac_demon]],
["nurgle_chosen_head_1", "Nurgle Knight Helm", [("Helm_Nurgle_1",0)], itp_merchandise|itp_type_fullhelm, 0, 
 5400 , weight(2.75)|abundance(100)|head_armor(95)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_good_plate, [], [fac_kingdom_9,fac_demon]],
["nurgle_chosen_head_2", "Nurgle Knight Helm", [("Helm_Nurgle_2",0)], itp_merchandise|itp_type_fullhelm, 0, 
 5400 , weight(2.75)|abundance(100)|head_armor(95)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_good_plate, [], [fac_kingdom_9,fac_demon]],
["nurgle_chosen_leg", "Nurgle Knight_leg", [("Boots_Nurgle",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature ,0,  2376 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(50)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_9,fac_demon]],
["nurgle_chosen_hand","Nurgle Knight_hand", [("Glove_Nurgle_L",0)], itp_merchandise|itp_type_hand_armor,0,  820, weight(1)|abundance(100)|body_armor(10)|difficulty(0),imodbits_armor, [], [fac_kingdom_9,fac_demon]],
["nurgle_shield_1", "Nurgle_Warrior_Shield", [("Shield_Nurgle_1", 0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 2025, weight(4.)|abundance(100)|difficulty(10)|hit_points(1000)|body_armor(100)|spd_rtng(85)|shield_width(90), imodbits_shield, [], [fac_kingdom_9,fac_demon,fac_commoners]], 
["nurgle_shield_2", "Nurgle_Warrior_Shield", [("Shield_Nurgle_2", 0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 2025, weight(4.)|abundance(100)|difficulty(10)|hit_points(1000)|body_armor(100)|spd_rtng(85)|shield_width(90), imodbits_shield, [], [fac_kingdom_9,fac_demon,fac_commoners]], 
["nurgle_mace", "Iron Mace", [("Greatmace_Elite_Crusher_B_01",0)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield|itp_crush_through|itp_can_knock_down, itc_scimitar|itcf_carry_axe_back, 20000, weight(4.5)|difficulty(12)|spd_rtng(100)|weapon_length(120)|swing_damage(45,blunt)|thrust_damage(0,blunt), imodbits_mace|imodbit_masterwork, [], [fac_kingdom_9]],


["chaos_warrior_shield", "Chaos_Warrior_Shield", [("Shield_Chaos", 0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 1010, weight(4.)|abundance(100)|difficulty(0)|hit_points(120)|body_armor(80)|spd_rtng(85)|shield_width(50)|shield_height(70), imodbits_shield, [], [fac_kingdom_9]], 
["chaos_knight_shield", "Chaos_Knight_shield", [("Shield_Elite_Chaos_01", 0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 1525, weight(4.)|abundance(100)|difficulty(0)|hit_points(160)|body_armor(90)|spd_rtng(85)|shield_width(50)|shield_height(70), imodbits_shield, [], [fac_kingdom_9]], 
["chaos_chosen_shield", "chaos_chosen_shield", [("Shield_Elite_Chaos_02", 0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 1525, weight(4.)|abundance(100)|difficulty(0)|hit_points(160)|body_armor(90)|spd_rtng(85)|shield_width(50)|shield_height(70), imodbits_shield, [], [fac_kingdom_9]],
["khorne_shield", "Khorne_Warrior_Shield", [("Shield_Khorne", 0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 2025, weight(4.)|abundance(100)|difficulty(0)|hit_points(200)|body_armor(100)|spd_rtng(85)|shield_width(90), imodbits_shield, [], [fac_kingdom_9,fac_demon,fac_commoners]], 
["khorne_shield2", "Khorne_Warrior_Shield", [("Shield_Khorne_2", 0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 2025, weight(4.)|abundance(100)|difficulty(0)|hit_points(200)|body_armor(100)|spd_rtng(85)|shield_width(90), imodbits_shield, [], [fac_kingdom_9,fac_demon,fac_commoners]], 

["demon_knight_shield", "tzeentch_Knight_shield", [("chaos_knight_shield", 0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 2025, weight(4.)|abundance(100)|difficulty(0)|hit_points(200)|body_armor(100)|spd_rtng(85)|shield_width(50)|shield_height(60), imodbits_shield, [], [fac_kingdom_9,fac_demon]], 

["demon_warrior_body", "Demon Warrior body", [("chaos_w",0)], itp_type_full_body_armor, 0, 20000, weight(3)|abundance(60)|head_armor(95)|body_armor(95)|leg_armor(95)|difficulty(0), imodbits_armor , [], [fac_kingdom_9,fac_demon]],


["imp_head_3", "imp head", [("bloodletter_head",0)], itp_type_fullhelm|itp_covers_beard|itp_unique|itp_covers_head, 0, 4500, weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(9), imodbits_plate],
["imp_foot_3", "imp foot", [("bloodletter_legs",0)], itp_type_foot_armor|itp_attach_armature|itp_unique, 0, 2570 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(9), imodbits_armor ],
["imp_hand_3", "imp hand", [("herald_handL",0)], itp_type_hand_armor|itp_unique, 0, 540, weight(1.25)|abundance(100)|body_armor(10)|difficulty(0), imodbits_armor ],
["imp_body_3", "imp body", [("bloodletter",0)], itp_type_full_body_armor, 0, 20000, weight(26)|abundance(65)|head_armor(10)|body_armor(50)|leg_armor(15)|difficulty(12), imodbits_armor ],

["demon_sword_3", "Fury_Sword", [("TH_CSword", 0)], itp_type_two_handed_wpn|itp_primary|itp_two_handed|itp_can_knock_down|itp_cant_use_on_horseback, itc_greatsword, 5000, weight(7)|weapon_length(150)|difficulty(8)|spd_rtng(80)|abundance(10)|swing_damage(50, pierce)|thrust_damage(50, pierce), imodbits_sword_high ],

["sarranid_two_handed_mace_1", "Iron Mace", [("BigMace_Crusher_A_01",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_wooden_parry|itp_crush_through|itp_can_knock_down|itp_cant_use_on_horseback, itc_greatsword|itcf_carry_axe_back, 470, weight(4.5)|difficulty(12)|spd_rtng(75)|weapon_length(120)|swing_damage(40,blunt)|thrust_damage(36,blunt), imodbits_mace|imodbit_masterwork, [], [fac_kingdom_9]],

["sarranid_two_handed_mace_2", "Iron Mace", [("Greatmace_Elite_Crusher_B_01",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_wooden_parry|itp_crush_through|itp_can_knock_down|itp_cant_use_on_horseback, itc_greatsword|itcf_carry_axe_back, 2000, weight(4.5)|difficulty(12)|spd_rtng(75)|weapon_length(120)|swing_damage(55,blunt)|thrust_damage(51,blunt), imodbits_mace|imodbit_masterwork, [], [fac_kingdom_9]],


["sarranid_mace_1", "Iron Mace", [("Mace_A_Chaos_Warrior_01",0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_can_knock_down, itc_scimitar|itcf_carry_mace_left_hip, 790, weight(2.0)|difficulty(10)|spd_rtng(85)|weapon_length(79)|swing_damage(35,blunt)|thrust_damage(0,pierce), imodbits_mace|imodbit_masterwork, [], [fac_kingdom_9]],
["sarranid_mace_2", "Iron Mace", [("Mace_B_Elite_Chaos_Warrior_01",0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_can_knock_down, itc_scimitar|itcf_carry_mace_left_hip, 1200, weight(2.0)|difficulty(10)|spd_rtng(80)|weapon_length(86)|swing_damage(40,blunt)|thrust_damage(0,pierce), imodbits_mace|imodbit_masterwork, [], [fac_kingdom_9]],


["sarranid_axe_a", "Iron Battle Axe", [("Axe_A_Chaos_Warrior_01",0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_crush_through|itp_bonus_against_shield, itc_scimitar|itcf_carry_axe_left_hip, 500, weight(1.75)|difficulty(9)|spd_rtng(88)|weapon_length(99)|swing_damage(32,pierce)|thrust_damage(0,pierce), imodbits_axe|imodbit_masterwork, [], [fac_kingdom_9]],
["sarranid_axe_b", "Iron War Axe", [("Axe_B_Chaos_Warrior_01",0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_crush_through|itp_bonus_against_shield, itc_scimitar|itcf_carry_axe_left_hip, 620, weight(1.75)|difficulty(9)|spd_rtng(90)|weapon_length(85)|swing_damage(40,pierce)|thrust_damage(0,pierce), imodbits_axe|imodbit_masterwork, [], [fac_kingdom_9]],

["sarranid_two_handed_axe_a", "Sarranid Battle Axe", [("Axe_A_Elite_Chaos_Warrior_01",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced|itp_cant_use_on_horseback, itc_nodachi|itcf_carry_axe_back, 1350, weight(3.0)|difficulty(12)|spd_rtng(83)|weapon_length(100)|swing_damage(49,pierce)|thrust_damage(0,pierce), imodbits_axe|imodbit_masterwork, [], [fac_kingdom_9]],
["sarranid_two_handed_axe_b", "Sarranid War Axe", [("Axe_B_Elite_Chaos_Warrior_01",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced|itp_cant_use_on_horseback, itc_nodachi|itcf_carry_axe_back, 1280, weight(3.0)|difficulty(12)|spd_rtng(87)|weapon_length(120)|swing_damage(60,pierce)|thrust_damage(0,pierce), imodbits_axe|imodbit_masterwork , [], [fac_kingdom_9]],

["sarranid_double_axe", "Sarranid Double-bladed Axe", [("GreatAxe_Elite_Crusher_B_01",0)], itp_type_two_handed_wpn|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced|itp_can_knock_down|itp_cant_use_on_horseback, itc_nodachi|itcf_carry_axe_back, 1280, weight(4.0)|difficulty(10)|spd_rtng(66)|weapon_length(130)|swing_damage(55,pierce)|thrust_damage(0,pierce), imodbits_axe|imodbit_masterwork , [], [fac_kingdom_9]],

["sarranid_long_double_axe",  "Double-bladed_Axe", [("GreatHalberd_Crusher_A_01",0)], itp_type_polearm|itp_merchandise|itp_primary|itp_crush_through|itp_wooden_parry|itp_two_handed|itp_bonus_against_shield|itp_extra_penetration|itp_cant_use_on_horseback, itc_cutting_spear|itcf_carry_spear, 2542 , weight(3.0)|difficulty(8)|spd_rtng(70)| weapon_length(150)|swing_damage(45, pierce)| thrust_damage(18 ,  pierce),imodbits_polearm , [], [fac_kingdom_9]],
["c_c_scythe", "Chaos_Crusher_Scythe", [("Scythe_Crusher_A_01",0)], itp_type_polearm|itp_merchandise|itp_can_knock_down|itp_crush_through|itp_primary|itp_two_handed|itp_wooden_parry|itp_cant_use_on_horseback|itp_is_glaive, itc_cutting_spear, 2724 , weight(6.0)|difficulty(10)|spd_rtng(70)| weapon_length(170)|swing_damage(60 , cut)| thrust_damage(34 ,  pierce),imodbits_polearm, [], [fac_kingdom_9]], 

["chaos_sword1", "Chaos_Sword", [("CSword1", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_crush_through|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 380, weight(1.500000)|abundance(100)|difficulty(7)|weapon_length(99)|spd_rtng(108)|swing_damage(30, pierce)|thrust_damage(21, pierce), imodbits_sword_high, [], [fac_kingdom_9]], 
["chaos_sword2", "Chaos_War_Sword", [("CSword2", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_crush_through|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 950, weight(1.750000)|abundance(100)|difficulty(9)|weapon_length(105)|spd_rtng(101)|swing_damage(33, pierce)|thrust_damage(20, pierce), imodbits_sword, [], [fac_kingdom_9]], 
["chaos_sword3", "Chaos_Knight_Sword", [("CSword3", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_crush_through|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 2500, weight(1.500000)|abundance(100)|difficulty(10)|weapon_length(105)|spd_rtng(98)|swing_damage(35, pierce)|thrust_damage(28, pierce), imodbits_sword_high, [], [fac_kingdom_9]], 
["chaos_sword4", "Chaos_Chosen_Sword", [("CSword4", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_crush_through|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 2623, weight(2.750000)|abundance(100)|difficulty(11)|weapon_length(114)|spd_rtng(95)|swing_damage(40, pierce)|thrust_damage(29, pierce), imodbits_sword_high, [], [fac_kingdom_9]], 
["chaos_sword5", "Chaos_Lord_Sword", [("DemonSword", 0)], itp_type_two_handed_wpn|itp_primary|itp_crush_through|itp_can_knock_down|itp_can_penetrate_shield, itc_bastardsword|itcf_carry_sword_back, 4550, weight(2.750000)|abundance(100)|difficulty(13)|weapon_length(130)|spd_rtng(95)|swing_damage(45, pierce)|thrust_damage(45, pierce), imodbits_sword_high, [], [fac_kingdom_9]], 


["demon_pickaxe_2", "Deadly_Hand", [("Scythe_Crusher_A_01", 0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_is_glaive, itc_nodachi, 5000, weight(1.5)|weapon_length(167)|difficulty(0)|spd_rtng(98)|abundance(10)|swing_damage(40, pierce)|thrust_damage(0, pierce), imodbits_axe|imodbit_masterwork , [], [fac_demon]],
["demon_axe", "Thrud_Axe", [("thrud_axe",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_unbalanced|itp_can_penetrate_shield, itc_nodachi|itcf_carry_sword_back, 10000 , weight(3.75)|difficulty(30)|spd_rtng(80)| weapon_length(130)|swing_damage(50, pierce)| thrust_damage(0 ,  pierce),imodbit_balanced|imodbit_tempered|imodbit_masterwork| imodbit_deadly| imodbit_sharp, [], [fac_kingdom_9,fac_demon]],

["chaos_throw1", "Chaos_Warrior_Throwing_Axe", [("Axe_A_Chaos_Warrior_01", 0)], itp_type_thrown|itp_crush_through|itp_merchandise|itp_primary|itp_bonus_against_shield, itcf_throw_axe, 300, weight(5)|abundance(100)|difficulty(5)|accuracy(0)|spd_rtng(80)|shoot_speed(18)|max_ammo(4)|thrust_damage(60, pierce)|weapon_length(50), imodbits_thrown_minus_heavy,missile_distance_trigger, [fac_kingdom_9]], 
["chaos_throw2", "Chaos_Warrior_Throwing_Axe", [("Axe_A_Elite_Chaos_Warrior_01", 0)], itp_type_thrown|itp_crush_through|itp_merchandise|itp_primary|itp_bonus_against_shield, itcf_throw_axe, 700, weight(5)|abundance(100)|difficulty(5)|accuracy(0)|spd_rtng(70)|shoot_speed(18)|max_ammo(4)|thrust_damage(70, pierce)|weapon_length(50), imodbits_thrown_minus_heavy,missile_distance_trigger, [fac_kingdom_9]], 
  
["chaos_lance_1","Chaos_Great_Naginata", [("GreatNaginata_Elite_Crusher_B_01",0)], itp_couchable|itp_type_polearm|itp_two_handed|itp_offset_lance|itp_merchandise| itp_primary|itp_offset_lance|itp_penalty_with_shield|itp_wooden_parry, itc_long_glaive, 360 , weight(5)|difficulty(8)|spd_rtng(75)| weapon_length(195)|swing_damage(65 , cut)| thrust_damage(43 ,  pierce),imodbits_polearm , [], [fac_kingdom_9]],
["chaos_lance_2", "Chaos_Naginata", [("Naginata_Elite_Crusher_B_01",0)], itp_type_polearm|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield|itp_offset_lance|itp_couchable|itp_crush_through, itc_long_glaive, 2450, weight(2.75)|difficulty(15)|spd_rtng(83)|weapon_length(235)|swing_damage(55,cut)|thrust_damage(40,pierce), imodbits_polearm , [], [fac_kingdom_9]],


["skeleton_armor_1", "Black Armor", [("spak_coat_of_plates_b",0)], itp_type_body_armor|itp_covers_legs, 0, 8100,breastplate_tier_5,imodbits_plate],
["skeleton_armor_2", "Black Armor", [("spak_coat_of_plates_e",0)], itp_type_body_armor|itp_covers_legs, 0, 8100,breastplate_tier_5,imodbits_plate],
["skeleton_armor_3", "Black Armor", [("spak_coat_of_plates_f",0)], itp_type_body_armor|itp_covers_legs, 0, 8100,breastplate_tier_5,imodbits_plate],
["undeadface_f", "Undead_head", [("undeadface_f", 0)], itp_type_fullhelm|itp_unique, 0, 1, weight(5.)|abundance(10)|difficulty(0)|head_armor(15)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["undead_body_f", "Undead_Body", [("undeadbody2_f", 0)], itp_type_body_armor|itp_unique|itp_covers_legs, 0, 1, mail_armor_tier_2, imodbits_cloth], 
["undead_foots_f", "Undead_Foots", [("undead_calf_f_L", 0)], itp_type_foot_armor|itp_unique, 0, 1, weight(10.)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(25), imodbits_cloth], 

["undeadface_gr", "Undead_head", [("undeadface_green", 0)], itp_type_fullhelm|itp_unique, 0, 1, weight(5.)|abundance(10)|difficulty(0)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["undead_body_gr", "Undead_Body", [("undeadbody2_g", 0)], itp_type_body_armor|itp_unique|itp_covers_legs, 0, 1, mail_armor_tier_3, imodbits_cloth], 
["undead_foots_gr", "Undead_Foots", [("undead_calf_green_L", 0)], itp_type_foot_armor|itp_unique, 0, 1, weight(10.)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(40), imodbits_cloth], 

["draugr_body_1","draugr_body",[("draugr",0)],itp_type_body_armor|itp_covers_legs,0,2000,weight(26)|head_armor(2)|body_armor(50)|leg_armor(13)|difficulty(0),imodbits_armor,],
["draugr_body_2","draugr_body",[("draugr1",0)],itp_type_body_armor|itp_covers_legs,0,2000,weight(26)|head_armor(2)|body_armor(50)|leg_armor(13)|difficulty(0),imodbits_armor,],
["draugr_body_3","draugr_body",[("draugr2",0)],itp_type_body_armor|itp_covers_legs,0,2000,weight(26)|head_armor(2)|body_armor(50)|leg_armor(13)|difficulty(0),imodbits_armor,],
["draugr_body_4","draugr_body",[("draugr3",0)],itp_type_body_armor|itp_covers_legs,0,2000,weight(26)|head_armor(2)|body_armor(50)|leg_armor(13)|difficulty(0),imodbits_armor,],
 
["draugr_head_0","draugr Helmet",[("draugr_head",0)],itp_type_fullhelm,0,600,weight(2)|head_armor(30)|difficulty(7),imodbits_plate,],
["draugr_head_1","draugr Helmet",[("draugr_Helmet_A_vs2",0)],itp_type_fullhelm,0,600,weight(2)|head_armor(30)|difficulty(7),imodbits_plate,],
["draugr_head_2","draugr Helmet",[("draugr_Helmet_B_vs2",0)],itp_type_fullhelm,0,1350,weight(2)|head_armor(45)|difficulty(7),imodbits_plate,],
["draugr_head_3","draugr Helmet",[("draugr_Helmet_C",0)],itp_type_fullhelm,0,2410,weight(2)|head_armor(60)|difficulty(7),imodbits_plate,],
["draugr_head_4","draugr Helm",[("draugrhelmetfemale_1",0)],itp_type_fullhelm,0,3000,weight(4)|head_armor(75)|difficulty(0),imodbits_armor],
["draugr_head_5","draugr Helm",[("draugrhelmetmale_1",0)],itp_type_fullhelm,0,3000,weight(4)|head_armor(75)|difficulty(0),imodbits_armor],
["draugr_hand", "{!}glove_animation", [("draugr_handL", 0)], itp_type_hand_armor, 0, 0, weight(1)|abundance(100), imodbits_none], 

["death_lord_helm","draugr overlord_Helm",[("death_yngolshelm",0)],itp_type_fullhelm,0,3000,weight(4)|head_armor(85)|difficulty(0),imodbits_armor],


#["dragon_sword", "dragon_sword", [("ssdj27",0)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_back, 937 , weight(2.0)|difficulty(9)|spd_rtng(101)| weapon_length(125)|swing_damage(35, pierce)| thrust_damage(32 ,  pierce),imodbits_sword_high , [], [fac_kingdom_4]],


["cyclop_body", "cyclop_body", [("kuangyeduyan",0)], itp_type_full_body_armor, 0, 20000, weight(26)|abundance(65)|head_armor(90)|body_armor(100)|leg_armor(90)|difficulty(12), imodbits_armor ],
["cyclop_weapon", "Giant_Mace", [("kuangyemubang",0)], itp_can_knock_down|itp_crush_through|itp_type_one_handed_wpn|itp_primary|itp_wooden_parry|itp_wooden_attack|itp_unique|itp_no_pick_up_from_ground, itc_gauntlet,101 , weight(7)|difficulty(40)|spd_rtng(75)| weapon_length(130)|swing_damage(67, blunt)| thrust_damage(92 ,  blunt),imodbits_mace, [], [fac_orc]],

["pixie_body", "Pixie body", [("Pixie",0)], itp_type_full_body_armor, 0, 4000, weight(3)|abundance(15)|head_armor(45)|body_armor(60)|leg_armor(45)|difficulty(0), imodbits_armor ],
["dryad_body", "Dryad body", [("Dryad",0)], itp_type_full_body_armor, 0, 5000, weight(3)|abundance(15)|head_armor(60)|body_armor(75)|leg_armor(60)|difficulty(0), imodbits_armor ],


#["herald_body", "Herald_of_Khorne", [("herald", 0)], itp_type_body_armor|itp_unique|itp_covers_legs|itp_civilian|itp_covers_head, 0, 2000, weight(30.)|abundance(100)|difficulty(15)|head_armor(80)|body_armor(80)|leg_armor(80), imodbits_armor], 





["dedal_kufel", "Kufel", [("dedal_kufelL", 0)], itp_type_hand_armor, 0, 0, weight(1.0)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(0), imodbits_none], 
["dedal_lutnia", "Lutnia", [("dedal_lutniaL", 0)], itp_type_hand_armor, 0, 0, weight(1.0)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(0), imodbits_none], 
["dedal_lira", "Lira", [("dedal_liraL", 0)], itp_type_hand_armor, 0, 0, weight(1.0)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(0), imodbits_none], 
["eating_ani", "{!}glove_animation", [("eatingL", 0)], itp_type_hand_armor, 0, 0, weight(1)|abundance(100), imodbits_none], 
["sharpening_1_ani", "{!}glove_animation", [("sharpening_1_L", 0)], itp_type_hand_armor|itp_force_show_left_hand|itp_force_show_right_hand, 0, 0, weight(1)|abundance(100), imodbits_none], 
["reading_ani", "{!}glove_animation", [("readingL", 0)], itp_type_hand_armor|itp_force_show_left_hand|itp_force_show_right_hand, 0, 0, weight(1)|abundance(100), imodbits_none], 

  

["wolfhelm_w2", "Werewolf's_Head", [("WhiteWerewolf", 0)], itp_type_fullhelm|itp_unique, 0, 75, weight(2)|abundance(10)|head_armor(80)|body_armor(20)|leg_armor(20), imodbits_none ],










["holy_cross","holy_cross", [("holy_cross",0), ("goods_cross_silver", ixmesh_inventory)], itp_type_goods, 0, 2500,weight(3)|abundance(90),imodbits_none],

 ["magic_ice_ray_dummy", "ice_ray_Scroll", [("guangjian_fly2",ixmesh_flying_ammo),("guangjian_fly2",0)], itp_type_bullets|itp_is_magic_staff, 0,
  1500, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(30,cut)|max_ammo(30),
  imodbits_none, cast_magic_ice_ray_dummy , [fac_commoners, fac_undeads_2] ],
 ["magic_sun_ray_dummy", "sun_ray_Scroll", [("bullet_1",0),("laser_bolt_orange",ixmesh_flying_ammo),("laser_bolt_orange", ixmesh_inventory)], itp_type_bullets|itp_is_magic_staff, 0,
  1500, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(150,cut)|max_ammo(20),imodbits_none ],
 ["magic_fire_ray_dummy", "fire_ray_Scroll", [("guangjian_fly3",ixmesh_flying_ammo),("guangjian_fly3",0)], itp_type_bullets|itp_is_magic_staff, 0,
  1500, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(30,cut)|max_ammo(30),
  imodbits_none, cast_magic_fire_ray_dummy , [fac_commoners, fac_undeads_2] ],
  ["cannon_dummy", "Small_Grenade", [("bombaaa_s", 0)], itp_type_bullets|itp_primary, 0, 
  4000, weight(4)|weapon_length(20)|abundance(70)|thrust_damage(100, blunt)|max_ammo(7), 
  imodbits_none,
  [(ti_on_missile_hit, 
   [
    (store_trigger_param_1, ":shooter"),
    (copy_position,pos51,pos1),
    (call_script, "script_magic_deliver_area_damage", ":shooter", 250, 6, 16),
  ]),],],

 ["granata_dummy", "granata_dummy", [("minie_ball",0),("minie_ball",ixmesh_flying_ammo)], itp_type_bullets|itp_no_pick_up_from_ground, itcf_carry_quiver_front_right,
  0, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(60,cut)|max_ammo(1), imodbits_missile,],

 ["wizard_hat_4", "Wizard Hat", [("wizard_hood_1",0)],  itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair ,0, 3266 , weight(1)|abundance(100)|head_armor(70)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], [fac_dark_knights,fac_commoners]],
 ["magic_robe_4", "Archmage_Robe", [("wizard_robe_3",0)], itp_type_body_armor|itp_covers_legs ,0, 9216,weight(11)|abundance(30)|head_armor(0)|body_armor(70)|leg_armor(35)|difficulty(6),imodbits_cloth , [], [fac_dark_knights,fac_commoners]],



["bingqishi", "ICE Knight_plate", [("dzin_armor",0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 12769,full_plate_armor_tier_4,imodbits_plate],
["bingqishitui", "ICE Knight Boots", [("toumingtou",0)],  itp_type_foot_armor| itp_attach_armature,0,
 2376 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(40)|difficulty(9) ,imodbits_plate, ],
["bingqishitoukui", "ICE Knight Helm", [("dzin_head2",0)], itp_type_fullhelm, 0, 
 5400 , weight(2.75)|abundance(100)|head_armor(80)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate,],
["bingqishishou","ICE Knight_hand", [("d_handL",0)], itp_type_hand_armor,0,  820, weight(1)|abundance(30)|body_armor(10)|difficulty(0),imodbits_plate, ],
["bingdun", "ICE Knight_shield", [("toumingtou",0)], itp_type_shield, itcf_carry_kite_shield,  2091 , weight(4)|difficulty(1)|shield_hit_points(30)|body_armor(20)|spd_rtng(100)|shield_width(100),imodbits_shield, ],
["bingjian", "ICE_knight_sword", [("toumingtou",0)], itp_type_two_handed_wpn|itp_unique|itp_primary, itc_bastardsword|itcf_carry_sword_back,
 2700 , weight(2.5)|difficulty(9)|spd_rtng(101)| weapon_length(160)|swing_damage(40, pierce)| thrust_damage(32 ,  pierce),imodbits_sword_high, 
 [
  (ti_on_weapon_attack, 
    [
      (store_trigger_param_1, ":shooter"),
      (copy_position,pos5,pos1),
      (copy_position,pos30,pos5),
      (position_move_z, pos30, 120),
      (particle_system_burst, "psys_lightning_attack", pos30, 10),
      (position_move_y, pos1, -60),
      (try_for_agents,":possable_agent"),
        (agent_is_alive,":possable_agent"),
        (this_or_next|agent_is_ally,":shooter"),
        (agent_is_ally,":possable_agent"),
        (this_or_next|neg|agent_is_ally,":possable_agent"),
        (neg|agent_is_ally,":shooter"),

        (agent_get_position,pos3,":possable_agent"),
        (get_distance_between_positions,":dist",pos5,pos3),
        (le,":dist",150),
        (assign,":agent",":possable_agent"),
        (get_distance_between_positions, ":var_4", pos1, pos3),
        (ge, ":var_4", ":dist"),
        (agent_deliver_damage_to_agent, ":shooter", ":agent", 40),
      (try_end),
    ]) ] 
],
 

["death_hood", "demon_hood", [("copy_demon_hood",0)], itp_type_fullhelm|itp_covers_head ,0, 2730 , weight(2)|abundance(100)|head_armor(90)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,[], [fac_undeads_2]],

["mirkwood_helm_e", "Mirkwood_Royal_Helm", [("glasshelmet", 0)], itp_merchandise|itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair, 0, 8252, weight(1)|abundance(10)|difficulty(6)|head_armor(90)|body_armor(0)|leg_armor(0), imodbits_good_plate , [], [fac_forest_ranger,fac_culture_4]],

["ebony_axe", "Ebony battle Axe", [("ebonybattleaxe",0)], itp_merchandise|itp_type_two_handed_wpn| itp_primary|itp_bonus_against_shield|itp_extra_penetration|itp_crush_through, itc_morningstar|itcf_carry_axe_back,12513 , weight(2.5)|difficulty(15)|spd_rtng(110)| weapon_length(100)|swing_damage(45 , pierce)| thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_kingdom_8,fac_kingdom_10]],

["ebony_double_axe", "Ebony Double Axe", [("ebonybattleaxe_2",0)], itp_merchandise|itp_type_two_handed_wpn|itp_cant_use_on_horseback|itp_crush_through|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_can_knock_down|itp_crush_through|itp_unbalanced|itp_extra_penetration, itc_nodachi|itcf_carry_axe_back, 2500, weight(5)|difficulty(8)|spd_rtng(100)|weapon_length(100)|swing_damage(55,pierce)|thrust_damage(0,pierce), imodbits_axe|imodbit_masterwork, [], [fac_undeads_2,fac_beast]],

["ebony_poleaxe", "ebony_poleaxe", [("ebony_halberd",0)], itp_type_polearm|itp_merchandise|itp_crush_through|itp_two_handed|itp_primary|itp_offset_lance|itp_cant_use_on_horseback|itp_extra_penetration, itc_guandao, 5000, weight(4)|difficulty(10)|spd_rtng(85)|weapon_length(200)|swing_damage(45,pierce)|thrust_damage(30,pierce), imodbits_polearm|imodbit_masterwork, [], [fac_kingdom_8,fac_kingdom_10]],

["ebony_long_mace", "ebony_long_mace", [("ebony_long_mace",0)], itp_can_knock_down|itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_morningstar|itcf_carry_mace_left_hip,2000 , weight(2.5)|difficulty(10)|spd_rtng(95)| weapon_length(100)|swing_damage(50 , pierce)| thrust_damage(0 ,  pierce),imodbits_mace , [], [fac_kingdom_8,fac_kingdom_3,fac_kingdom_7]],

["ebony_throwing_pike",  "ebony Throwing Pikes", [("ebonyspear",0)], itp_type_thrown|itp_crush_through| itp_cant_use_on_horseback|itp_primary|itp_wooden_parry, itcf_throw_javelin, 500 , weight(3.0)|difficulty(4)|spd_rtng(81)| weapon_length(200)| thrust_damage(60 ,pierce)| shoot_speed(26)|max_ammo(3),imodbits_thrown , missile_distance_trigger, [fac_undeads_2,fac_beast]],
["ebony_pike_melee",     "ebony Throwing Pike", [("ebonyspear",0)], itp_type_polearm| itp_cant_use_on_horseback|itp_primary|itp_wooden_parry|itp_two_handed|itp_is_pike, itc_pike, 500 , weight(3.0)|difficulty(0)|spd_rtng(100)| weapon_length(220)|swing_damage(35 , pierce)| thrust_damage(30 ,  pierce),imodbits_thrown, [], [fac_undeads_2,fac_beast] ],

["ebony_scimitar_1", "Scimitar", [("ebonysword",0)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_extra_penetration, itc_scimitar|itcf_carry_sword_back,
 2000 , weight(1.5)|difficulty(9)|spd_rtng(104)| weapon_length(100)|swing_damage(30 , pierce)| thrust_damage(0 ,  pierce),imodbits_sword_high , [], [fac_undeads_2,fac_beast]],
["ebony_scimitar_2", "Elite Scimitar", [("ebonySword_2",0)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_extra_penetration, itc_scimitar|itcf_carry_sword_back,
2500 , weight(1.5)|difficulty(9)|spd_rtng(104)| weapon_length(100)|swing_damage(33 , pierce)| thrust_damage(0 ,  pierce),imodbits_sword_high , [], [fac_undeads_2,fac_beast]],

["ebony_arming_sword", "Ebony Heavy Sword", [("ebonyPersonSword",0)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_extra_penetration|itp_bonus_against_shield, itc_longsword|itcf_carry_sword_back, 
2400 , weight(2.25)|difficulty(10)|spd_rtng(90)| weapon_length(100)|swing_damage(35, pierce)| thrust_damage(30 ,  pierce),imodbits_sword_high , [], [fac_undeads_2,fac_beast]],
["ebony_long_sword", "Ebony Long Sword", [("ebony_longsword",0)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_extra_penetration, itc_longsword|itcf_carry_sword_back, 
3040 , weight(2)|difficulty(9)|spd_rtng(100)| weapon_length(113)|swing_damage(32 , pierce)| thrust_damage(32 ,  pierce),imodbits_sword_high, [], [fac_undeads_2,fac_beast]],

["ebony_bastard_sword", "Ebony Bastard Sword", [("ebony_bastard",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_crush_through|itp_can_penetrate_shield|itp_cant_use_on_horseback, itc_greatsword|itcf_carry_sword_back, 
3540 , weight(2.25)|difficulty(12)|spd_rtng(100)| weapon_length(125)|swing_damage(40 , pierce)| thrust_damage(35 ,  pierce),imodbits_sword_high, [], [fac_undeads_2,fac_beast]],
["ebony_great_sword_2", "Ebony_Great Sword", [("ssdj24",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_crush_through|itp_can_knock_down|itp_cant_use_on_horseback|itp_can_penetrate_shield, itc_greatsword|itcf_carry_sword_back, 
5000, weight(2.75)|difficulty(12)|spd_rtng(95)|weapon_length(140)|swing_damage(45,pierce)|thrust_damage(30,pierce), imodbits_sword_high, [], [fac_undeads_2,fac_beast]],
["ebony_great_sword", "Ebony_Great Sword", [("ebonyPersonGreatsword",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_crush_through|itp_can_knock_down|itp_cant_use_on_horseback|itp_can_penetrate_shield, itc_greatsword|itcf_carry_sword_back, 
6000 , weight(3.75)|difficulty(15)|spd_rtng(90)| weapon_length(150)|swing_damage(50, pierce)| thrust_damage(30,pierce),imodbits_sword_high, [], [fac_undeads_2,fac_beast]],

["ebony_scimitar_long_1", "Ebony Two Handed Scimitar", [("ebonyGreatsword_2",0)], itp_merchandise|itp_two_handed|itp_type_two_handed_wpn|itp_primary|itp_extra_penetration|itp_can_penetrate_shield, itc_morningstar|itcf_carry_sword_back, 
2500 , weight(1.75)|difficulty(12)|spd_rtng(102)| weapon_length(115)|swing_damage(43 , pierce)| thrust_damage(0 ,  pierce),imodbits_sword_high , [], [fac_undeads_2,fac_beast]],
["ebony_scimitar_long_3", "Ebony Two Handed Scimitar", [("ebonygreatsword",0)], itp_merchandise|itp_two_handed|itp_type_two_handed_wpn|itp_primary|itp_extra_penetration|itp_can_penetrate_shield, itc_morningstar|itcf_carry_sword_back, 
3500 , weight(1.75)|difficulty(12)|spd_rtng(100)| weapon_length(130)|swing_damage(45 , pierce)| thrust_damage(0 ,  pierce),imodbits_sword_high , [], [fac_undeads_2,fac_beast]],

["ebony_scimitar_long_2", "Ebony cav Scimitar", [("AN_sword01",0)], itp_merchandise|itp_type_two_handed_wpn|itp_primary|itp_extra_penetration|itp_crush_through, itc_morningstar|itcf_carry_sword_back, 
3000, weight(1.75)|difficulty(10)|spd_rtng(100)|weapon_length(116)|swing_damage(40,pierce)|thrust_damage(0,pierce), imodbits_sword_high , [], [fac_undeads_2,fac_beast]],
["ebony_scimitar_long_4", "Ebony cav Scimitar", [("DreadweaveSword",0)], itp_merchandise|itp_type_two_handed_wpn|itp_wooden_parry|itp_primary|itp_extra_penetration|itp_can_penetrate_shield|itp_crush_through, itc_morningstar|itcf_carry_sword_back, 
4000, weight(2.0)|difficulty(10)|spd_rtng(96)|weapon_length(143)|swing_damage(43,pierce)|thrust_damage(0,pierce), imodbits_sword_high , [], [fac_undeads_2,fac_beast]],



["glass_sword_a", "Glass Sword", [("glass_sword", 0)], itp_merchandise|itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_back, 3000, weight(1.5)|weapon_length(100)|difficulty(0)|spd_rtng(122)|abundance(30)|swing_damage(30, pierce)|thrust_damage(34, pierce), imodbits_sword_high, [], [fac_kingdom_4] ],
["glass_sword_b", "Glass Long Sword", [("glass_long_sword", 0)], itp_merchandise|itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_back, 4500, weight(1.5)|weapon_length(120)|difficulty(0)|spd_rtng(114)|abundance(30)|swing_damage(35, pierce)|thrust_damage(34, pierce), imodbits_sword_high, [], [fac_kingdom_4] ],
["glass_sword_c", "Glass Great Sword", [("glassGreatsword", 0)], itp_merchandise|itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_claymore|itcf_carry_sword_back, 7500, weight(1.5)|weapon_length(145)|difficulty(15)|spd_rtng(110)|abundance(30)|swing_damage(40, pierce)|thrust_damage(34, pierce), imodbits_sword_high, [], [fac_kingdom_4] ],
["mirkwood_sword_reward", "Greenwood_Relic_Sword", [("glassclaymore", 0)], itp_merchandise|itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield, itc_claymore|itcf_carry_sword_back, 10000, weight(1.5)|weapon_length(130)|difficulty(15)|spd_rtng(122)|abundance(30)|swing_damage(50, pierce)|thrust_damage(50, pierce), imodbits_sword_high, [], [fac_kingdom_4] ],

["glass_halberd", "Glass_Halberd", [("glassHalberd",0)], itp_type_polearm|itp_wooden_parry|itp_two_handed|itp_primary|itp_crush_through|itp_cant_use_on_horseback|itp_extra_penetration, itc_guandao, 7500, weight(2.5)|difficulty(20)|spd_rtng(100)|weapon_length(180)|swing_damage(40,pierce)|thrust_damage(40,pierce), imodbits_polearm|imodbit_masterwork , [], [fac_forest_ranger,fac_kingdom_4,fac_culture_4]],
["glass_lance", "Glass_Lance", [("glass_spear", 0)], itp_merchandise|itp_type_polearm|itp_couchable|itp_wooden_parry|itp_primary, itc_greatlance, 5014, weight(3.5)|weapon_length(220)|difficulty(4)|spd_rtng(100)|abundance(10)|swing_damage(32, blunt)|thrust_damage(48, pierce), imodbits_polearm|imodbit_masterwork, [], [fac_kingdom_4] ],
["glass_lance_2", "Glass Great lance", [("glassspear",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_couchable|itp_crush_through|itp_bonus_against_shield, itc_greatlance, 3000, weight(5)|difficulty(10)|spd_rtng(80)|weapon_length(240)|swing_damage(0,cut)|thrust_damage(45,pierce)|abundance(30), imodbits_polearm , [], [fac_kingdom_4]],
["glass_mace", "Glass Mace", [("glass_mace",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,1500 , weight(1.5)|difficulty(0)|spd_rtng(90)| weapon_length(71)|swing_damage(38 , pierce)| thrust_damage(0 ,  pierce),imodbits_mace , [], [fac_kingdom_4]],
["glass_mace_2", "Glass Mace", [("glass_quadmace",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,1500 , weight(1.5)|difficulty(0)|spd_rtng(90)| weapon_length(71)|swing_damage(42 , pierce)| thrust_damage(0 ,  pierce),imodbits_mace , [], [fac_kingdom_4]],
["glass_long_mace", "glass_long_mace", [("glass_long_mace",0)], itp_can_knock_down|itp_crush_through|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_mace_left_hip,2000 , weight(2)|difficulty(10)|spd_rtng(99)| weapon_length(100)|swing_damage(38 , pierce)| thrust_damage(0 ,  pierce),imodbits_mace , [], [fac_kingdom_4]],

["stalhrim_sword", "Stalhrim Long Sword", [("StalhrimLongSword", 0)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_extra_penetration, itc_longsword|itcf_carry_sword_back, 3000, weight(1.5)|weapon_length(115)|difficulty(0)|spd_rtng(114)|abundance(30)|swing_damage(38, pierce)|thrust_damage(34, pierce), imodbits_sword_high, [], [fac_kingdom_10] ],
["stalhrim_greatsword", "Stalhrim Great Sword", [("StalhrimGreatSword", 0)], itp_merchandise|itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_extra_penetration|itp_cant_use_on_horseback, itc_greatsword, 5000, weight(1.5)|weapon_length(160)|difficulty(12)|spd_rtng(110)|abundance(30)|swing_damage(46, pierce)|thrust_damage(34, pierce), imodbits_sword_high, [], [fac_kingdom_10] ],
["stahlrim_axe", "Stalhrim axe", [("stahlrimwaraxe",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,1500 , weight(1.5)|difficulty(0)|abundance(30)|spd_rtng(90)| weapon_length(71)|swing_damage(42 , pierce)| thrust_damage(0 ,  pierce),imodbits_mace , [], [fac_kingdom_10]],
["stahlrim_battleaxe", "Stalhrim battleaxe", [("stahlrimbattleaxe",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_extra_penetration|itp_wooden_parry|itp_crush_through|itp_cant_use_on_horseback, itc_nodachi|itcf_carry_axe_back, 8000 , weight(3.8)|abundance(30)|difficulty(10)|spd_rtng(100)| weapon_length(130)|swing_damage(60 , pierce)| thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_kingdom_10, fac_scotland]],
["stalhrim_sword_short", "Stalhrim Sword", [("stahlrimsword", 0)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_extra_penetration, itc_longsword|itcf_carry_sword_back, 6000, weight(1.5)|weapon_length(90)|difficulty(0)|spd_rtng(114)|abundance(30)|swing_damage(43, pierce)|thrust_damage(34, pierce), imodbits_sword_high, [], [fac_kingdom_10, fac_scotland] ],

["black_shield", "Black Knight_shield", [("fix_EOS_knight_shield",0)], itp_type_shield, itcf_carry_kite_shield,  2091 , weight(4)|difficulty(5)|shield_hit_points(200)|body_armor(125)|spd_rtng(70)|shield_width(40)|shield_height(60),imodbits_shield,  [], [fac_kingdom_8,fac_undeads_2,fac_kingdom_10,fac_beast,fac_kingdom_4]],

 ["witch_robe_1", "witch_robe", [("witch_robe",0)], itp_type_body_armor|itp_covers_legs ,0, 1000,weight(11)|abundance(50)|head_armor(0)|body_armor(42)|leg_armor(14)|difficulty(5),imodbits_cloth , [], [fac_kingdom_8,fac_beast]],
 ["witch_robe_3", "witch_robe", [("chaosfemale_armour2",0)], itp_type_body_armor|itp_covers_legs ,0, 9216,weight(11)|abundance(30)|head_armor(0)|body_armor(70)|leg_armor(35)|difficulty(20),imodbits_cloth , [], [fac_kingdom_8]],
 ["witch_robe_4", "witch_robe", [("chaosfemale_armour",0)], itp_type_body_armor|itp_covers_legs ,0, 9216,weight(11)|abundance(30)|head_armor(0)|body_armor(70)|leg_armor(35)|difficulty(20),imodbits_cloth , [], [fac_kingdom_8]],
 ["daemonette_claws","Daemonette_claws", [("demonclaw_L",0)], itp_type_hand_armor|itp_unique|itp_civilian,0,  820, weight(1)|abundance(30)|body_armor(10)|difficulty(0),imodbits_plate, ],
 











["imp_head_4", "imp head", [("balroghead",0)], itp_type_fullhelm|itp_covers_beard|itp_unique|itp_covers_head, 0, 4500, weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(9), imodbits_plate],


["gold_golemarmor", "gold_golem_body", [("golem_gold_body",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_unique ,0, 6360,weight(1)|abundance(60)|head_armor(0)|body_armor(100)|leg_armor(0)|difficulty(14),imodbits_armor ],
["gold_golemboots", "gold_golem_feet", [("golem_gold_legs",0)], itp_type_foot_armor|itp_civilian|itp_unique ,0, 
 2376 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(100)|difficulty(0) ,imodbits_cloth,],
["gold_golemgloves","gold_golem_hand", [("golem_gold_handL",0)], itp_type_hand_armor|itp_unique,0, 
 820, weight(1)|abundance(100)|body_armor(10)|difficulty(0),imodbits_armor, ],
["gold_golemhelm", "gold_golem_head", [("golem_gold_head", 0)], itp_type_fullhelm|itp_unique, 0, 75, weight(2)|abundance(10)|head_armor(100)|body_armor(0)|leg_armor(0), imodbits_none ],


["air_elemental", "Air_Elemental_Body", [("airelemental", 0)], itp_type_full_body_armor, 0, 0, weight(1)|head_armor(0)|body_armor(40)|leg_armor(40), imodbits_plate], 
["air_elemental_head", "Air_Elemental_Head", [("airelemental_head", 0)], itp_type_head_armor|itp_covers_head|itp_unique, 0, 0, weight(1)|head_armor(40)|body_armor(0)|leg_armor(0), imodbits_plate], 
["air_elemental_hand", "Air_Elemental_Hands", [("airelemental_hand_L", 0)], itp_type_hand_armor|itp_unique, 0, 0, weight(0)|abundance(120)|difficulty(0)|head_armor(0)|body_armor(10)|leg_armor(0), imodbits_cloth], 

["water_elemental", "Water_Elemental_Body", [("waterelemental", 0)], itp_type_full_body_armor, 0, 0, weight(1)|head_armor(0)|body_armor(60)|leg_armor(60), imodbits_plate], 
["water_elemental_head", "Water_Elemental_Head", [("waterelemental_head", 0)], itp_type_head_armor|itp_covers_head|itp_unique, 0, 0, weight(1)|head_armor(60)|body_armor(0)|leg_armor(0), imodbits_plate], 

["fire_elemental_hand", "fire__Elemental_Hands", [("elemental_fire_handL", 0)], itp_type_hand_armor|itp_unique, 0, 0, weight(0)|abundance(120)|difficulty(0)|head_armor(0)|body_armor(10)|leg_armor(0), imodbits_cloth], 
["fire_elemental_body", "fire__Elemental_Body", [("elemental_fire", 0)], itp_type_full_body_armor, 0, 2000, weight(5)|head_armor(0)|body_armor(60)|leg_armor(0), imodbits_plate], 
["fire_elemental_head", "fire__Elemental_Head", [("elemental_fire_head", 0)], itp_type_head_armor|itp_covers_head|itp_unique, 0, 500, weight(5)|head_armor(70)|body_armor(0)|leg_armor(0), imodbits_plate], 
["fire_elemental_legs", "fire__Elemental_Legs", [("elemental_fire_boots", 0)], itp_type_foot_armor|itp_civilian|itp_unique, 0, 300, weight(5)|head_armor(0)|body_armor(0)|leg_armor(70), imodbits_plate], 


["earthelemental_body", "Earth_Elemental_Body", [("earthelemental_body", 0)], itp_type_full_body_armor, 0, 2000, weight(5)|head_armor(0)|body_armor(80)|leg_armor(0), imodbits_plate], 
["earthelemental_head", "Earth_Elemental_Head", [("earthelemental_head", 0)], itp_type_head_armor|itp_covers_head|itp_unique, 0, 500, weight(5)|head_armor(80)|body_armor(0)|leg_armor(0), imodbits_plate], 
["earthelemental_legs", "Earth_Elemental_Legs", [("earthelemental_legs", 0)], itp_type_foot_armor|itp_civilian|itp_unique, 0, 300, weight(5)|head_armor(0)|body_armor(0)|leg_armor(80), imodbits_plate], 

["meduza", "meduza_Body", [("meduza", 0)], itp_type_half_body_armor, 0, 0, weight(1.)|body_armor(50)|leg_armor(40), imodbits_plate], 
["meduza_head", "meduzahead", [("meduzahead", 0)], itp_type_head_armor|itp_covers_head|itp_unique, 0, 0, weight(1.)|head_armor(60)|body_armor(0)|leg_armor(0), imodbits_plate], 

["meduza_up", "meduza_Body", [("meduza_up", 0)], itp_type_half_body_armor, 0, 0, weight(1.)|body_armor(75)|leg_armor(60), imodbits_plate], 
["meduza_head2", "meduzahead2", [("meduzahead2", 0)], itp_type_head_armor|itp_covers_head|itp_unique, 0, 0, weight(1.)|head_armor(90)|body_armor(0)|leg_armor(0), imodbits_plate], 

["wight_body_low", "Wight body", [("wight_body",0)], itp_type_half_body_armor, 0, 5000, weight(3)|abundance(15)|head_armor(40)|body_armor(40)|leg_armor(45)|difficulty(0), imodbits_armor ],

["serpentfly", "serpentfly body", [("serpentfly",0)], itp_type_full_body_armor, 0, 5000, weight(3)|abundance(15)|head_armor(30)|body_armor(30)|leg_armor(40)|difficulty(0), imodbits_armor ],
["firefly", "firefly body", [("smoczawazka2",0)], itp_type_full_body_armor, 0, 5000, weight(3)|abundance(15)|head_armor(30)|body_armor(20)|leg_armor(40)|difficulty(0), imodbits_armor ],
["dragonfly", "dragonfly body", [("dragonfly",0)], itp_type_full_body_armor, 0, 4000, weight(3)|abundance(15)|head_armor(30)|body_armor(40)|leg_armor(40)|difficulty(0), imodbits_armor ],


["serpentfly_weapon", "Serpent_Fly_Poison", [("bullet_1", 0)], itp_secondary|itp_type_one_handed_wpn|itp_primary|itp_unique, 9223372036879941646, 0, weight(1.5)|weapon_length(40)|difficulty(0)|spd_rtng(120)|abundance(30)|swing_damage(25, cut)|thrust_damage(0, pierce), imodbits_axe,],

["firefly_fireball", "fireFly_Poison", [("bullet_1", 0),("guangjian3",ixmesh_flying_ammo)], itp_type_thrown|itp_crush_through|itp_primary|itp_unique, itcf_throw_stone, 0, weight(4)|weapon_length(0)|difficulty(0)|spd_rtng(120)|shoot_speed(70)|thrust_damage(35, cut)|max_ammo(30), imodbits_none],

["ghost_behemoth_armor", "Ghost Behemoth'armor", [("ghost_rancor",0)], itp_type_full_body_armor ,0, 6360,weight(1)|abundance(60)|head_armor(75)|body_armor(75)|leg_armor(75)|difficulty(14),imodbits_armor ],

["nurgling_armor", "nurgling armor", [("nurgling",0)], itp_type_full_body_armor ,0, 6360,weight(1)|abundance(60)|head_armor(50)|body_armor(45)|leg_armor(40)|difficulty(14),imodbits_armor ],
["plaguebearer_armor", "plaguebearer armor", [("plaguebearer",0)], itp_type_full_body_armor ,0, 6360,weight(1)|abundance(60)|head_armor(100)|body_armor(100)|leg_armor(100)|difficulty(14),imodbits_armor ],


["horned_demon_sword", "Horned Demon_sword", [("toumingshen",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_can_knock_down|itp_crush_through|itp_bonus_against_shield|itp_unique|itp_no_pick_up_from_ground, itc_gauntlet,0 , weight(0.5)|difficulty(100)|spd_rtng(170)| weapon_length(140)|swing_damage(40 , pierce)| thrust_damage(0 ,  pierce),imodbits_mace ],

 
#["demon_armor_1", "demon_armor", [("demon_armor_1",0)], itp_type_body_armor|itp_force_show_body |itp_civilian ,0, 100 , breastplate_tier_3,imodbits_cloth],
#["demon_armor_2", "demon_armor", [("demon_armor_2",0)], itp_type_body_armor|itp_covers_legs |itp_civilian ,0, 200 , breastplate_tier_4,imodbits_cloth],
#["demon_armor_3", "demon_armor", [("demon_armor_3",0)], itp_type_body_armor|itp_force_show_body |itp_civilian ,0, 300 , breastplate_tier_5,imodbits_cloth],
#["demon_armor_4", "demon_armor", [("archdevil_armor_1.",0)], itp_type_body_armor|itp_covers_legs |itp_civilian ,0, 400 , full_plate_armor_tier_4,imodbits_cloth],


["xenoargh_bola","Boleadora (bola)",[("minie_ball",0),("xenoargh_bola",ixmesh_flying_ammo),("xenoargh_bola_store",ixmesh_inventory)],itp_type_thrown|itp_crush_through|itp_no_pick_up_from_ground|itp_primary,itcf_throw_axe,2500,weight(5)|spd_rtng(120)|shoot_speed(30)|thrust_damage(55,blunt)|max_ammo(7)|weapon_length(100)|accuracy(100),imodbits_none,
[
(ti_on_missile_hit,
      [
      (store_trigger_param_1,":shooter"),   
      (try_begin),
        (copy_position, pos63, pos1),	
        (position_set_y, pos63, 0),	
        (try_for_agents,":agent"),
          (agent_is_active,":agent"),
          (agent_is_alive,":agent"),   
          (agent_get_position,pos62,":agent"),
          (position_set_y, pos62, 0),
          (get_distance_between_positions,":dist",pos63,pos62),
          (lt,":dist",150),            	
          (try_begin),
            (neg|agent_is_human, ":agent"),#stop if not human
            (agent_get_rider,":rider_agent",":agent"),
            (assign, ":continue", 0),
            (try_begin),
              (gt,":rider_agent",-1),
              (agent_is_ally, ":rider_agent"),
              (neg|agent_is_ally, ":shooter"),
              (assign, ":continue", 1),
            (else_try),
              (gt,":rider_agent",-1),
              (neg|agent_is_ally, ":rider_agent"),
              (agent_is_ally, ":shooter"),
              (assign, ":continue", 1),
            (else_try),
              (le,":rider_agent",-1),
              (assign, ":continue", 1),
            (try_end),
            (eq, ":continue", 1),
            (agent_get_rider,":rider_agent",":agent"),
            (try_begin),
              (gt,":rider_agent",-1),
              (agent_set_animation, ":rider_agent", "anim_bash_knocked"),  
              (agent_set_slot, ":rider_agent", slot_agent_special_ability_affect_type, entangle),
              (agent_set_slot, ":rider_agent", slot_agent_special_ability_affect_time, 3),
              (store_random_in_range,":random_no",350,750),
              (agent_deliver_damage_to_agent,":shooter",":agent",":random_no"),
            (else_try),
              (le,":rider_agent",-1),
              (agent_set_hit_points,":agent",0,0),
              (agent_deliver_damage_to_agent,":shooter",":agent"),
            (try_end),
          (else_try),
            (assign, ":continue", 0),
            (try_begin),
              (agent_is_ally, ":agent"),
              (neg|agent_is_ally, ":shooter"),
              (assign, ":continue", 1),
            (else_try),
              (neg|agent_is_ally, ":agent"),
              (agent_is_ally, ":shooter"),
              (assign, ":continue", 1),
            (try_end),
            (eq, ":continue", 1),
            (agent_is_human, ":agent"),
            (position_move_z, pos62, 200),
            (particle_system_burst,"psys_stun_effect",pos62,1),
            (agent_set_animation, ":agent", "anim_bash_knocked"),  
            (agent_set_slot, ":agent", slot_agent_special_ability_affect_type, entangle),
            (agent_set_slot, ":agent", slot_agent_special_ability_affect_time, 3),
        (try_end),
      (try_end),
]),
]],


["barrel_bomb", "barrel_bomb", [("ale_barrel",0)], itp_type_two_handed_wpn|itp_unique|itp_two_handed|itp_primary, itc_nodachi, 100 , weight(4)|spd_rtng(100)| weapon_length(100)|swing_damage(200 , pierce)| thrust_damage(200 ,  pierce),imodbits_sword_high,[
 (ti_on_weapon_attack, 
  [
      (store_trigger_param_1, ":shooter"),
      (agent_get_position, pos1, ":shooter"),
      (copy_position,pos51,pos1),
      (set_fixed_point_multiplier, 1),
      (play_sound_at_position, "snd_cannon_shot", pos51),
      (particle_system_burst, "psys_explosive_explosion_sparks_a", pos51, 35),
      (particle_system_burst, "psys_explosive_explosion_sparks_b", pos51, 35),
      (particle_system_burst, "psys_bomb_smoke", pos51, 5),
      (particle_system_burst, "psys_bomb_dust", pos51, 5),
        
      (try_for_agents,":possable_agent"),
        (agent_is_alive,":possable_agent"),
        (this_or_next|eq,":shooter",":possable_agent"),
        (this_or_next|agent_is_ally,":shooter"),
        (agent_is_ally,":possable_agent"),
        (this_or_next|eq,":shooter",":possable_agent"),
        (this_or_next|neg|agent_is_ally,":possable_agent"),
        (neg|agent_is_ally,":shooter"),
        (agent_get_position,pos3,":possable_agent"),
        (get_distance_between_positions,":dist",pos51,pos3),
        (le,":dist",600),
        (assign,":agent",":possable_agent"),
        (store_random_in_range, ":thrust_damage", 200, 300),  
        
         (store_agent_hit_points, ":hp", ":agent", 1),
         (val_sub, ":hp", ":thrust_damage"),
         (val_max, ":hp", 0),
         (agent_set_hit_points,":agent",":hp",1),
        
         (try_begin),
           (neg|agent_is_human,":agent"),
           (agent_set_animation,":agent","anim_horse_rear"), 
           (agent_deliver_damage_to_agent,":shooter",":agent"),
         (else_try),
           (agent_set_animation, ":agent", "anim_bash_out_2"),
           (agent_deliver_damage_to_agent, ":shooter", ":agent"),
         (try_end),
        (store_random_in_range, ":thrust_damage", 2000, 3000),  
        (call_script, "script_magic_deliver_damage_to_agent", ":shooter", ":agent", ":thrust_damage", burn, 3, 15),
      (try_end),
   
  ]),
  ],firearm_factions],





["druid_robe_1", "Druid_Robe", [("druid2",0)], itp_type_body_armor|itp_covers_legs ,0, 1000,weight(6)|abundance(30)|head_armor(0)|body_armor(40)|leg_armor(18)|difficulty(6),imodbits_cloth , [], [fac_forest_ranger,fac_culture_4]],
["druid_robe_2", "Druid_Robe", [("druid3",0)], itp_type_body_armor|itp_covers_legs ,0, 1000,weight(6)|abundance(30)|head_armor(0)|body_armor(70)|leg_armor(18)|difficulty(6),imodbits_cloth , [], [fac_forest_ranger,fac_culture_4]],
["druid_cap", "Druid_Wolf_Cap", [("rat_wolfcap",0)], itp_type_head_armor,0, 760 , weight(2.75)|abundance(100)|head_armor(70)|body_armor(0)|leg_armor(0), imodbits_plate , [], [fac_forest_ranger,fac_kingdom_4,fac_culture_4]],

["ebony_male_plate", "Ebony Male plate", [("ebonyarmorbody",0)], merc_body_armor, 0, 20000, weight(30)|abundance(20)|head_armor(13)|body_armor(85)|leg_armor(45)|difficulty(18), imodbits_good_plate, [], [fac_kingdom_8,fac_undeads_2,fac_beast]],
["ebony_male_foot", "Ebony Male Boots", [("ebonyarmorboots",0)], itp_merchandise| itp_type_foot_armor| itp_attach_armature,0,
 2664 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(40)|difficulty(9) ,imodbits_good_plate,  [], [fac_kingdom_8,fac_undeads_2,fac_beast]],
["ebony_male_head", "Ebony Male Helm", [("ebonyarmorhelmet",0)], itp_type_head_armor|itp_merchandise, 0, 
 5400 , weight(2.75)|abundance(100)|head_armor(90)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_good_plate,   [], [fac_kingdom_8,fac_undeads_2,fac_beast]],
["ebony_male_hand","Ebony Male_hand", [("ebonyarmorgloves_L",0)], itp_merchandise|itp_type_hand_armor,0,  820, weight(1)|abundance(30)|body_armor(10)|difficulty(0),imodbits_armor , [], [fac_kingdom_8,fac_undeads_2,fac_beast]],


["glass_female_plate", "Glass Female_plate", [("glasscuriass_f",0)], merc_body_armor, 0, 20000, weight(20)|abundance(20)|head_armor(0)|body_armor(80)|leg_armor(45)|difficulty(12), imodbits_good_plate, [], [fac_elf, fac_kingdom_4,fac_forest_ranger,fac_culture_4]],
["glass_male_plate", "Glass Male_plate", [("glasscuriass_m",0)], merc_body_armor, 0, 20000, weight(20)|abundance(20)|head_armor(13)|body_armor(85)|leg_armor(45)|difficulty(15), imodbits_good_plate, [], [fac_kingdom_4]],

["glass_foot", "Glass Boots", [("glassboots_m",0)], itp_merchandise| itp_type_foot_armor| itp_attach_armature,0,
 2664 , weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(40)|difficulty(9) ,imodbits_good_plate,  [], [fac_elf, fac_kingdom_4,fac_forest_ranger,fac_culture_4]],
["glass_hand","Glass_hand", [("glassgauntlet_m_L",0)], itp_merchandise|itp_type_hand_armor,0,  820, weight(1)|abundance(30)|body_armor(10)|difficulty(0),imodbits_armor , [], [fac_kingdom_4]],

["glass_head", "Glass_Helm", [("glasshelmet_m", 0)], itp_merchandise|itp_type_head_armor, 0, 8252, weight(1)|abundance(10)|difficulty(6)|head_armor(100)|body_armor(0)|leg_armor(0), imodbits_good_plate , [], [fac_kingdom_4]],

["rat_king_skin", "Rat_king Skin", [("rat_chieftain",0)], itp_unique|itp_type_body_armor|itp_covers_legs, 0, 40000,weight(2)|abundance(50)|head_armor(25)|body_armor(75)|leg_armor(25)|difficulty(15),imodbits_good_plate],

["glass_shield", "glass Shield", [("glass_shield",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,  4000 , weight(1)|difficulty(5)|shield_hit_points(400)|body_armor(90)|spd_rtng(120)|shield_width(50)|shield_height(60),imodbits_shield , [], [fac_kingdom_4]],


["cartridges_sissofbattle_holy", "Cartridges", [("bullet_2", 0),("huojian_fly2",ixmesh_flying_ammo),("spak_book",ixmesh_carry)],  itp_type_bullets|itp_can_penetrate_shield|itp_bonus_against_shield|itp_covers_legs, itcf_carry_sword_left_hip, 
 5000, weight(4)|weapon_length(3)|shoot_speed(17)|abundance(33)|thrust_damage(70, cut)|max_ammo(30), imodbits_none,[(ti_on_missile_hit, [(store_trigger_param_1, ":shooter"),(copy_position,pos51,pos1),(call_script, "script_magic_deliver_area_damage", ":shooter", 70, 3, 7),]),]+missile_distance_trigger+bullet_dust_trigger,[fac_demon_hunters]],


["sissofbattle_holy_granata", "Holy_Grenade", [("hhg", 0),("spak_book",ixmesh_carry)], itp_type_thrown|itp_crush_through|itp_unique|itp_primary, itcf_throw_stone, 20000, weight(4)|weapon_length(30)|difficulty(0)|spd_rtng(100)|shoot_speed(30)|abundance(33)|thrust_damage(100, blunt)|max_ammo(8), imodbits_none,[(ti_on_missile_hit, [(store_trigger_param_1, ":shooter"),(copy_position,pos51,pos1),(call_script, "script_magic_deliver_area_damage", ":shooter", 200, 7, 14),]),]+missile_distance_trigger,firearm_factions],

["cartridges_sissofbattle_flame_cannon", "Cartridges", [("minie_ball",0),("musket_balls",ixmesh_flying_ammo),("spak_book",ixmesh_carry)], itp_type_bullets|itp_can_penetrate_shield|itp_bonus_against_shield|itp_covers_legs, itcf_carry_sword_left_hip,
  20000, weight(2.25)|abundance(30)|weapon_length(3)|thrust_damage(50,pierce)|max_ammo(6), 
  imodbits_missile, powergun_flame_trigger+missile_distance_trigger , [fac_demon_hunters] ],

["glassdagger_1", "glassdagger Staff", [("glassdagger",0)], itp_merchandise|itp_type_pistol|itp_crush_through|itp_primary|itp_next_item_as_melee|itp_is_magic_staff ,itcf_reload_pistol|itcf_shoot_pistol|itcf_carry_dagger_front_left,
 25000 , weight(3.25)|difficulty(0)|spd_rtng(40) | shoot_speed(150) | thrust_damage(80 ,pierce)|max_ammo(1)|accuracy(82),imodbits_magic_staff, magic_cast_trigger , [fac_culture_4] ], 
["glassdagger",  "glass dagger", [("glassdagger",0)], itp_type_one_handed_wpn| itp_primary|itp_crush_through|itp_can_knock_down|itp_bonus_against_shield, itc_longsword|itcf_carry_dagger_front_left, 10000 , weight(2)|difficulty(0)|spd_rtng(110)| weapon_length(55)|swing_damage(70, pierce)| thrust_damage(0 ,  pierce),imodbits_polearm, [], [fac_culture_4]],



["rat_musket_8barrel", "Musket", [("gatling",0)], itp_merchandise|itp_type_musket|itp_crush_through|itp_two_handed|itp_primary|itp_cant_reload_on_horseback, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 10000, weight(10)|difficulty(0)|spd_rtng(70)|shoot_speed(140)|thrust_damage(70,pierce)|max_ammo(30)|accuracy(70), imodbits_gun, musket_trigger , [fac_dwarf]],


 ["cartridges_rar", "Cartridges", [("bullet_2",0),("huojian_fly2",ixmesh_flying_ammo),("gatlingbullet",ixmesh_carry),("gatlingbullet", ixmesh_inventory)], itp_type_bullets, itcf_carry_quiver_right_vertical,
  3000, weight(9)|abundance(5)|weapon_length(3)|thrust_damage(40,pierce)|max_ammo(120),
  imodbits_missile, missile_distance_trigger+bullet_dust_trigger , firearm_factions
 ],

["stahlrim_plate", "Stahlrim plate", [("geteshi",0)], merc_body_armor, 0, 20000, weight(10)|abundance(20)|head_armor(13)|body_armor(85)|leg_armor(45)|difficulty(18), imodbits_good_plate, [], [fac_kingdom_10]],
["stahlrim_foot", "Stahlrim Boots", [("geteshi_boot",0)], itp_merchandise| itp_type_foot_armor| itp_attach_armature,0,
 2664 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(40)|difficulty(9) ,imodbits_good_plate, [], [fac_kingdom_10, fac_scotland]],


["emp_wh_armor1", "Witch_Hunter_Outfit", [("BadAssLongCoat", 0)], merc_body_armor, 0, 5000, weight(10)|abundance(100)|difficulty(9)|head_armor(10)|body_armor(50)|leg_armor(40), imodbits_plate, [], [fac_kingdom_7]],
["emp_wh_helmet1", "Witch_Hunter_Hat", [("BadAssLongCoat_Hat", 0)], itp_type_head_armor|itp_merchandise, 0, 2500, weight(2)|abundance(100)|difficulty(0)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate, [], [fac_kingdom_7]],

#["double_axe_onehand", "Double Axe", [("d_axe",0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_bonus_against_shield|itp_can_knock_down|itp_crush_through|itp_unbalanced, itc_morningstar|itcf_carry_axe_back, 959, weight(12)|difficulty(22)|spd_rtng(90)|weapon_length(97)|swing_damage(50,pierce), imodbits_axe|imodbit_masterwork, [], ne_faction],

["blue_dragon_body", "blue dragon body", [("green_dragon",0)], itp_type_full_body_armor, 0, 25000, weight(30)|abundance(30)|head_armor(0)|body_armor(80)|leg_armor(50)|difficulty(18), imodbits_plate ],

["werewolf_head_1", "Cap with Fur", [("werewolf_head_1",0)], itp_type_fullhelm   ,0, 
 600 , weight(1)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, 
 [], ee_faction],
["werewolf_head_2", "Vaegir Helmet", [("werewolf_head_2",0)], itp_type_fullhelm   ,0, 
 1066 , weight(2)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, 
 [], ee_faction],
["werewolf_head_3", "Helmet with Lamellar Guard", [("werewolf_head_3",0)], itp_type_fullhelm ,0, 
 1350 , weight(2.75)|abundance(100)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, 
 [], ee_faction],
["werewolf_head_4", "Helmet with Lamellar Guard", [("werewolf_head_4",0)], itp_type_fullhelm ,0, 
 1350 , weight(2.75)|abundance(100)|head_armor(75)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, 
 [], ee_faction],

 
 
["goblin_barrel","goblin_in_barrel", [("ale_barrel",0)], itp_type_thrown|itp_primary|itp_no_pick_up_from_ground, itcf_throw_stone, 5000, weight(3)|difficulty(5)|abundance(120)|spd_rtng(97)| shoot_speed(80)| thrust_damage(100 ,  blunt)|max_ammo(8)|weapon_length(8),imodbits_thrown_2,[(ti_on_missile_hit, [(store_trigger_param_1, ":shooter"),(copy_position,pos51,pos1),(call_script, "script_magic_deliver_area_damage", ":shooter", 210, 4, 2),]),]+missile_distance_trigger+goblin_summon, [fac_orc]],



["dun_helm_a","Wolf_Cap",[("rat_wolfcap",0)],itp_type_head_armor,0,300,weight(2)|head_armor(50)|body_armor(50)|leg_armor(50)|difficulty(0),imodbits_cloth],

["air_elemental_2", "Air_Elemental_Body", [("airelemental", 0)], itp_type_full_body_armor, 0, 0, weight(1)|head_armor(30)|body_armor(70)|leg_armor(70), imodbits_plate], 
["water_elemental_2", "Water_Elemental_Body", [("waterelemental", 0)], itp_type_full_body_armor, 0, 0, weight(1)|head_armor(20)|body_armor(80)|leg_armor(80), imodbits_plate], 
["fire_elemental_body_2", "fire__Elemental_Body", [("elemental_fire", 0)], itp_type_full_body_armor, 0, 2000, weight(5)|head_armor(20)|body_armor(80)|leg_armor(20), imodbits_plate], 
["earthelemental_body_2", "Earth_Elemental_Body", [("earthelemental_body", 0)], itp_type_full_body_armor, 0, 2000, weight(5)|head_armor(10)|body_armor(90)|leg_armor(10), imodbits_plate], 


["air_elemental_3", "Air_Elemental_Body", [("airelemental", 0)], itp_type_full_body_armor, 0, 0, weight(1)|head_armor(40)|body_armor(90)|leg_armor(90), imodbits_plate], 
["water_elemental_3", "Water_Elemental_Body", [("waterelemental", 0)], itp_type_full_body_armor, 0, 0, weight(1)|head_armor(40)|body_armor(80)|leg_armor(90), imodbits_plate], 
["fire_elemental_body_3", "fire__Elemental_Body", [("elemental_fire", 0)], itp_type_full_body_armor, 0, 2000, weight(5)|head_armor(30)|body_armor(90)|leg_armor(30), imodbits_plate], 
["earthelemental_body_3", "Earth_Elemental_Body", [("earthelemental_body", 0)], itp_type_full_body_armor, 0, 2000, weight(5)|head_armor(30)|body_armor(110)|leg_armor(30), imodbits_plate], 

["tree_trunk_invis_3", "Tree_Trunk", [("toumingshou",0)], itp_can_knock_down|itp_crush_through|itp_type_one_handed_wpn|itp_primary|itp_wooden_parry|itp_wooden_attack|itp_unbalanced|itp_unique|itp_no_pick_up_from_ground, itc_gauntlet,101 , weight(250)|difficulty(20)|spd_rtng(87)| weapon_length(186)|swing_damage(50, blunt)| thrust_damage(50 ,  blunt),imodbits_mace, [(ti_on_weapon_attack, [(store_trigger_param_1, ":shooter"),(agent_get_horse,":horse",":shooter"),(neg|gt,":horse",0),(copy_position,pos51,pos1),(call_script,"script_cf_agent_cleave",":shooter", 1, 0),])], [fac_elf]],

["undeadface_mohrg", "Mohrg_head", [("Mohrg_head", 0)], itp_type_fullhelm|itp_unique, 0, 1, weight(5)|abundance(10)|difficulty(0)|head_armor(50)|body_armor(0)|leg_armor(0), imodbits_cloth], 
["undead_body_mohrg", "Mohrg_Body", [("Mohrg_body", 0)], itp_type_body_armor|itp_unique|itp_covers_legs, 0, 1, breastplate_tier_5, imodbits_cloth], 

["berserk_helm", "berserk_helm", [("berserk_helm", 0), ("berserk_helm_inventory", ixmesh_inventory)], itp_type_head_armor|itp_civilian|itp_attach_armature|itp_merchandise, 0, 4266, weight(4)|abundance(10)|difficulty(0)|head_armor(80)|body_armor(50)|leg_armor(50), imodbits_plate,  [], ne_faction],
["berserk_armor", "berserk_armor", [("berserk_armor", 0)], merc_body_armor, 0, 7876,full_plate_armor_tier_1, imodbits_armor, [], ne_faction],

 ["lich_dragon_breath", "death_cloud Scroll", [("bullet_1",0),("huojian_fly_green",ixmesh_flying_ammo)], itp_type_bullets|itp_unique, 0,
  275, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(70,cut)|max_ammo(15),
  imodbits_missile, cast_magic_summon_Zombie_Lord+cast_magic_soul_Leech , firearm_factions ],

#new epic




["enchanter_staff_1", "enchanter Staff", [("staffofmagnus",0)], itp_unique|itp_type_pistol|itp_crush_through|itp_primary|itp_next_item_as_melee|itp_is_magic_staff ,itcf_reload_pistol|itcf_shoot_pistol|itcf_carry_spear,
 20000 , weight(3.25)|difficulty(0)|spd_rtng(55) | shoot_speed(140) | thrust_damage(75 ,pierce)|max_ammo(3)|accuracy(82),imodbits_magic_staff, magic_cast_trigger , [fac_commoners] ], 
["enchanter_staff",  "enchanter Staff", [("staffofmagnus",0)], itp_type_two_handed_wpn|itp_offset_lance| itp_primary|itp_penalty_with_shield, itc_staff|itcf_carry_spear, 20000 , weight(2)|difficulty(0)|spd_rtng(97)| weapon_length(150)|swing_damage(45 , blunt)| thrust_damage(26 ,  blunt),imodbits_polearm, [], [fac_commoners]],
["dragon_shield", "Dragon Shield", [("fix_EOS_knight_shield",0)], itp_type_shield|itp_unique, itcf_carry_kite_shield,  20000 , weight(2)|shield_hit_points(5000)|body_armor(125)|spd_rtng(100)|shield_width(40)|shield_height(60)|difficulty(6),imodbits_shield],
["eggshield_2", "eggshield_2", [("sh_snake",0)], itp_type_shield|itp_unique, itcf_carry_kite_shield, 50000, weight(5)|shield_hit_points(7000)|body_armor(40)|spd_rtng(78)|shield_width(30)|shield_height(60)|difficulty(3), imodbits_shield,tynan_dagger_trigger ],

["magic_book_1", "Mirrorball", [("book_b",0)], 
 itp_type_shield|itp_merchandise, itcf_carry_sword_left_hip,  
 5000 , weight(2.0)|abundance(70)|hit_points(10000)|body_armor(20)|spd_rtng(80)|shield_width(10)|shield_height(10),imodbits_none, [], [fac_dark_knights,fac_commoners, fac_undeads_2]], 
["magic_book_2", "Triumvirate", [("church_book_a",0)], 
 itp_type_shield|itp_merchandise, itcf_carry_sword_left_hip,  
 50000 , weight(2.0)|abundance(10)|hit_points(10000)|body_armor(20)|spd_rtng(80)|shield_width(10)|shield_height(10),imodbits_none, [], [fac_dark_knights,fac_commoners, fac_undeads_2]], 
["magic_book_3", "Winter Flurry", [("church_book_d",0)], 
 itp_type_shield|itp_merchandise, itcf_carry_sword_left_hip,  
 50000 , weight(2.0)|abundance(10)|hit_points(10000)|body_armor(20)|spd_rtng(80)|shield_width(10)|shield_height(10),imodbits_none, [], [fac_dark_knights,fac_commoners, fac_undeads_2]], 
["magic_book_4", "Firebird's Eye", [("church_book_e",0)], 
 itp_type_shield|itp_merchandise, itcf_carry_sword_left_hip,  
 50000 , weight(2.0)|abundance(10)|hit_points(10000)|body_armor(20)|spd_rtng(80)|shield_width(10)|shield_height(10),imodbits_none, [], [fac_dark_knights,fac_commoners, fac_undeads_2]], 
 
 
["magic_book_5", "Tome of Elemental", [("church_book_b",0)], 
 itp_type_shield|itp_merchandise, itcf_carry_sword_left_hip,  
 5000 , weight(2.0)|abundance(70)|hit_points(10000)|body_armor(20)|spd_rtng(80)|shield_width(10)|shield_height(10),imodbits_none, [], [fac_dark_knights,fac_commoners, fac_undeads_2]], 
["magic_book_6", "Sandro Notebook", [("book_a",0)], 
 itp_type_shield|itp_merchandise, itcf_carry_sword_left_hip,  
 50000 , weight(2.0)|abundance(10)|hit_points(10000)|body_armor(20)|spd_rtng(80)|shield_width(10)|shield_height(10),imodbits_none, [], [fac_dark_knights,fac_commoners, fac_undeads_2]], 
["magic_book_7", "Demonary", [("church_book_f",0)], 
 itp_type_shield|itp_merchandise, itcf_carry_sword_left_hip,  
 50000 , weight(2.0)|abundance(10)|hit_points(10000)|body_armor(20)|spd_rtng(80)|shield_width(10)|shield_height(10),imodbits_none, [], [fac_dark_knights,fac_commoners, fac_undeads_2]], 
["magic_book_8", "Book of Bitterness", [("church_book_c",0)], 
 itp_type_shield|itp_merchandise, itcf_carry_sword_left_hip,  
 50000 , weight(2.0)|abundance(10)|hit_points(10000)|body_armor(20)|spd_rtng(80)|shield_width(10)|shield_height(10),imodbits_none, [], [fac_dark_knights,fac_commoners, fac_undeads_2]], 


 ["magic_arrow_power", "_magic_arrow_Scroll", [("bullet_1",0),("holy_arrow_fl",ixmesh_flying_ammo),("magic_12_icon", ixmesh_inventory)], itp_merchandise|itp_type_bullets|itp_is_magic_staff, 0,
  1000, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(150,cut)|max_ammo(30),
  imodbits_none, missile_ice_trigger , [fac_commoners, fac_kingdom_5, fac_commoners] ],
["molag_bal_boots", "molag_bal_boots", [("knight_of_molag_bal_boots",0)], itp_unique|itp_type_foot_armor|itp_attach_armature ,0,  20000 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(50)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_9,fac_demon]],

["rhongomiant", "Rhongomiant", [("blackqq", 0)], itp_type_polearm|itp_unique|itp_primary|itp_bonus_against_shield|itp_penalty_with_shield|itp_couchable|itp_crush_through|itp_extra_penetration, itc_greatlance, 50000, weight(2.5)|weapon_length(400)|difficulty(12)|spd_rtng(95)|abundance(1)|swing_damage(30, pierce)|thrust_damage(200, pierce), imodbits_polearm, gungnir_trigger ],
["aroundight", "Aroundight", [("Black_j",0)], itp_unique|itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_crush_through|itp_can_knock_down|itp_can_penetrate_shield, itc_greatsword|itcf_carry_sword_back, 50000 , weight(2.75)|difficulty(15)|spd_rtng(130)| weapon_length(180)|swing_damage(60, pierce)| thrust_damage(100,pierce),imodbits_sword_high],

["power_musket_8barrel", "Musket", [("gatling",0)], itp_unique|itp_type_musket|itp_crush_through|itp_two_handed|itp_primary, itcf_shoot_musket|itcf_reload_musket|itc_parry_polearm|itcf_carry_crossbow_back, 10000, weight(10)|difficulty(0)|spd_rtng(150)|shoot_speed(140)|thrust_damage(140,pierce)|max_ammo(300)|accuracy(70), imodbits_gun, musket_trigger , [fac_dwarf]],

["magic_book_9", "Anpu Neb-Ta", [("book_a",0)], 
 itp_type_shield|itp_unique, itcf_carry_sword_left_hip,  
 50000 , weight(2.0)|abundance(10)|hit_points(10000)|body_armor(20)|spd_rtng(80)|shield_width(10)|shield_height(10),imodbits_none, [], [fac_dark_knights,fac_commoners, fac_undeads_2]], 

["dawnbreaker_armor", "dawnbreaker_armor", [("elf_twiligh_armor",0)], itp_unique|itp_type_body_armor|itp_covers_legs, 0, 20000, weight(28)|abundance(100)|head_armor(20)|body_armor(90)|leg_armor(40)|difficulty(24), imodbits_good_plate],

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#Hunting Mod begin#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
 ["deer","Deer", [("deer",0)], itp_unique|itp_type_horse, 0, 1411,abundance(40)|hit_points(40)|body_armor(0)|difficulty(11)|horse_speed(50)|horse_maneuver(32)|horse_charge(20),imodbits_horse_basic],
 ["boar","Boar", [("boar",0)], itp_unique|itp_disable_agent_sounds|itp_type_horse|itp_is_pike, 0, 1411,abundance(40)|hit_points(150)|body_armor(50)|difficulty(11)|horse_speed(20)|horse_maneuver(50)|horse_charge(25),imodbits_horse_basic],
 ["wolf_wild","wolf_mount_white", [("warg1",0)],itp_unique|itp_type_horse|itp_disable_agent_sounds|itp_is_pike, 0, 1411,abundance(40)|hit_points(150)|body_armor(30)|difficulty(11)|horse_speed(50)|horse_maneuver(50)|horse_charge(25),imodbits_horse_adv, [], [fac_orc]],
 
 
 ["ogar_wild","ogar", [("ogar",0)],itp_unique|itp_type_horse|itp_disable_agent_sounds|itp_is_pike, 0, 1411,abundance(40)|hit_points(200)|body_armor(45)|difficulty(11)|horse_speed(50)|horse_maneuver(50)|horse_charge(25),imodbits_horse_adv, [], [fac_orc]],
 ["orthrus_wild","orthrus", [("orthrus",0)],itp_unique|itp_type_horse|itp_disable_agent_sounds|itp_is_pike, 0, 1411,abundance(40)|hit_points(300)|body_armor(45)|difficulty(11)|horse_speed(50)|horse_maneuver(50)|horse_charge(25),imodbits_horse_adv, [], [fac_orc]],
 ["cerber_wild","cerber", [("cerber",0)],itp_unique|itp_type_horse|itp_disable_agent_sounds|itp_is_pike, 0, 1411,abundance(40)|hit_points(450)|body_armor(45)|difficulty(11)|horse_speed(50)|horse_maneuver(50)|horse_charge(25),imodbits_horse_adv, [], [fac_orc]],
 
 
 
["gorgon_1_wild", "Gorgon", [("gorgonka", 0)], itp_type_horse|itp_merchandise|itp_disable_agent_sounds|itp_is_pike, 0, 8000, abundance(40)|difficulty(11)|hit_points(700)|body_armor(70)|horse_speed(35)|horse_maneuver(42)|horse_charge(40)|horse_scale(115), imodbits_horse_armor, [], [fac_scotland]], 
["gorgon_2_wild", "Mighty_Gorgon", [("upg_gorgonka", 0)], itp_type_horse|itp_merchandise|itp_disable_agent_sounds|itp_is_pike, 0, 10000, abundance(40)|difficulty(11)|hit_points(900)|body_armor(90)|horse_speed(42)|horse_maneuver(42)|horse_charge(45)|horse_scale(120), imodbits_horse_armor, [], [fac_scotland]], 
 ["griffin_wild", "griffin", [("griffin",0)], itp_merchandise|itp_type_horse|itp_disable_agent_sounds|itp_is_magic_staff|itp_is_pike, 0, 4000, abundance(40)|hit_points(600)|body_armor(60)|difficulty(11)|horse_speed(50)|horse_maneuver(33)|horse_charge(35)|horse_scale(120), imodbits_horse_armor, [], [fac_kingdom_1,fac_kingdom_7,fac_dwarf]],
["spider_wild","spider", [("spider",0)],itp_merchandise|itp_type_horse|itp_disable_agent_sounds|itp_is_pike, 0, 1411,abundance(40)|hit_points(400)|body_armor(50)|difficulty(11)|horse_speed(37)|horse_maneuver(70)|horse_charge(25),imodbits_horse_adv, [], [fac_orc,fac_beast]],

 ["unicorn_wild","Unicorn", [("unicorn",0)], itp_unique|itp_type_horse, 0, 4000,abundance(40)|hit_points(600)|body_armor(75)|difficulty(11)|horse_speed(50)|horse_maneuver(46)|horse_charge(100)|horse_scale(112), imodbits_horse_armor, [], [fac_forest_ranger,fac_elf]],
 
 ["deer_meat","Venison", [("raw_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 242,weight(30)|abundance(100)|food_quality(40)|max_ammo(30),imodbits_none],




 ["ogar","ogar", [("ogar",0)],itp_type_horse|itp_disable_agent_sounds|itp_is_pike, 0, 1411,abundance(40)|hit_points(150)|body_armor(30)|difficulty(11)|horse_speed(50)|horse_maneuver(50)|horse_charge(25),imodbits_horse_adv, [], [fac_orc]],
 ["orthrus","orthrus", [("orthrus",0)],itp_type_horse|itp_disable_agent_sounds|itp_is_pike, 0, 1411,abundance(40)|hit_points(200)|body_armor(30)|difficulty(11)|horse_speed(50)|horse_maneuver(50)|horse_charge(50),imodbits_horse_adv, [], [fac_orc]],
 ["cerber","cerber", [("cerber",0)],itp_type_horse|itp_disable_agent_sounds|itp_is_pike, 0, 1411,abundance(40)|hit_points(300)|body_armor(30)|difficulty(11)|horse_speed(50)|horse_maneuver(50)|horse_charge(75),imodbits_horse_adv, [], [fac_orc]],

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#Hunting Mod end#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

["items_end", "Items End", [("shield_round_a",0)], 0, 0, 1, 0, 0],
]
# modmerger_start version=201 type=2
try:
    component_name = "items"
    var_set = { "items" : items }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
