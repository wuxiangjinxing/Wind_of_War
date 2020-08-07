from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *

pmf_is_prisoner = 0x0001

####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See header_parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id. 
#    7.2) Minimum number of troops in the stack. 
#    7.3) Maximum number of troops in the stack. 
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################
highland_personality = aggressiveness_11 | courage_11

outsiders_personality = aggressiveness_7 | courage_4
native_personality = aggressiveness_8 | courage_9
dark_personality = aggressiveness_15 | courage_15 | banditness
robber_knight_personality   = aggressiveness_15 | courage_13 | banditness

#soldier_personality = aggressiveness_8 | courage_9
#merchant_personality = aggressiveness_0 | courage_7
#escorted_merchant_personality = aggressiveness_0 | courage_11
#bandit_personality   = aggressiveness_3 | courage_8 | banditness

party_templates = [
  ("none","none",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("rescued_prisoners","Rescued Prisoners",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("enemy","Enemy",icon_gray_knight,0,fac_undeads,merchant_personality,[]),
  ("hero_party","Hero Party",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
####################################################################################################################
# Party templates before this point are hard-wired into the game and should not be changed. 
####################################################################################################################
##  ("old_garrison","Old Garrison",icon_vaegir_knight,0,fac_neutral,merchant_personality,[]),
  ("village_defenders","Village Defenders",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,10,20),(trp_peasant_woman,0,4),(trp_watchman,2,5)]),

  ("cattle_herd","Cattle Herd",icon_cattle|carries_goods(0)|pf_always_visible,0,fac_neutral,merchant_personality,[(trp_cattle,80,120)]),

##  ("vaegir_nobleman","Vaegir Nobleman",icon_vaegir_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_vaegir_knight,2,6),(trp_vaegir_horseman,4,12)]),
##  ("swadian_nobleman","Swadian Nobleman",icon_gray_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_swadian_knight,2,6),(trp_swadian_man_at_arms,4,12)]),
# Ryan BEGIN
  ("looters", "Looters", icon_dunlander|carries_goods(8), 0, fac_outlaws, bandit_personality, [(trp_outlaw_leader,0,2),(trp_looter,8,40),(trp_bandit,0,8)] ),
  
  
# Ryan END
  ("adventurer", "adventurer", icon_gray_knight|carries_goods(8), 0,fac_manhunters,outsiders_personality, [(trp_adventurer,5,5),(trp_musket_hunter,13,25),(trp_mercenary_swordsman,10,20)] ),
  ("manhunters", "Manhunters", icon_gray_knight, 0, fac_manhunters, soldier_personality, [(trp_slaver_chief,1,5),(trp_manhunter,13,25),(trp_slave_hunter,10,20)] ),
  
  ("war_clerics", "war_clerics", icon_gray_knight, 0, fac_demon_hunters, soldier_personality, [(trp_teutonic_dis_knight,5,10),(trp_teutonic_sword,13,25),(trp_clerics,10,20),(trp_hospitaller_knight_2,1,5)] ),
  ("sissofbattle","sissofbattle",icon_gray_knight,0,fac_demon_hunters,soldier_personality,[(trp_sissofbattle,10,20),(trp_grey_knight_inquisitor,2,3),(trp_healer,5,5),(trp_sissofbattle_s,5,5),(trp_angle,2,5)]),
  ("sissofbattle_huge","sissofbattle",icon_huge_flagbearer,0,fac_demon_hunters,soldier_personality,[(trp_archangle,2,3),(trp_sissofbattle,20,40),(trp_grey_knight_terminator,2,5),(trp_healer,5,5),(trp_sissofbattle_r,10,20), (trp_angle,5,10)]),

  ("mercenary","mercenary",icon_gray_knight,0,fac_manhunters,soldier_personality,[(trp_mercenary_cavalry,1,5),(trp_caravan_guard,13,25),(trp_mercenary_horseman,10,20)] ),
  ("robber_knights_2","Roving Robber Knight",icon_gray_knight|carries_goods(8),0,fac_deserters,robber_knight_personality,[]),
  
  ("robber_knights","Roving Robber Knight",icon_gray_knight|carries_goods(8),0,fac_robber_knights,robber_knight_personality,[(trp_we_knight_3,1,4),(trp_we_knight_2,4,8), (trp_we_knight_1,9,18),(trp_raider,5,12),(trp_mountain_bandit,5,22),(trp_forest_bandit,8,25)]),
  
  ("robber_knights_huge","Roving Robber Knight",icon_gray_knight|carries_goods(8),0,fac_robber_knights,robber_knight_personality,[(trp_we_knight_3,5,10),(trp_we_knight_2,7,15), (trp_we_knight_1,10,20),(trp_raider,12,25)]),

  ("brigand_huge","brigand Band",icon_dunlander_x3|carries_goods(9),0,fac_outlaws,robber_knight_personality,[(trp_we_knight_3,5,15),(trp_we_knight_2,5,15),(trp_we_knight_1,5,15),(trp_raider,25,50),(trp_bandit,50,50)]),
  ("robber_knights_band","Roving Robber Knight Band",icon_dunlander_x3|carries_goods(9),0,fac_robber_knights,robber_knight_personality,[(trp_we_knight_2, 1, 5), (trp_raider,5,12),(trp_looter,50,50)]),
  ("brigand","brigand",icon_brigand|carries_goods(9),0,fac_outlaws,robber_knight_personality,[(trp_outlaw_leader,1,1),(trp_raider,1,10), (trp_brigand,2,17),(trp_bandit,4,34)]),
  ("looters_2", "Looters", icon_umbar_corsair_x3|carries_goods(9), 0, fac_outlaws, bandit_personality, [(trp_outlaw_leader,1,10),(trp_looter,50,100)] ),
    
  ("ninjia", "ninjia", icon_peasant|carries_goods(8), 0,fac_outlaws,outsiders_personality, [(trp_ninjia_adv,4,12),(trp_ninjia,8,15),(trp_strange_warrior,8,15)] ),

 # ("strange_warrior", "strange warrior", icon_axeman|carries_goods(8), 0,fac_outlaws,outsiders_personality, [(trp_strange_warrior_adv,1,5),(trp_strange_warrior,8,21),(trp_strange_spearman,14,21),(trp_ninjia,0,8)] ),
 # ("strange_cavalry", "strange warrior", icon_brigand|carries_goods(8), 0,fac_outlaws,outsiders_personality, [(trp_strange_cavalry_adv,5,10),(trp_strange_cavalry,10,20)] ),
  
#  ("gaelic_1",     "gaelic Warriors",     icon_peasant|carries_goods(2),0, fac_gaelic, soldier_personality, [(trp_gaelic_tribesman,7,14),(trp_gaelic_fighter,5,15),(trp_gaelic_warrior,1,4)]),
#  ("gaelic_2",     "gaelic Warband",      icon_peasant|carries_goods(2),0, fac_gaelic, soldier_personality, [(trp_gaelic_fighter,7,14),(trp_gaelic_warrior,8,16)]),
#  ("gaelic_huge",     "gaelic Warband",   icon_huge_peasant_3|carries_goods(2),0, fac_gaelic, soldier_personality, [(trp_gaelic_fighter,50,50),(trp_gaelic_warrior,50,50)]),

  ("dragonfly", "dragonfly", icon_axeman|carries_goods(8), 0, fac_outlaws, bandit_personality, [(trp_dragonfly,8,40),(trp_firefly,2,10)] ),
  ("scottish_1",   "scottish Warriors",  icon_axeman|carries_goods(2),0, fac_scotland, soldier_personality, [(trp_scottish_guard,1,5),(trp_scottish_jav,5,10),(trp_scottish_pikeman,7,14),(trp_scottish_axeman,2,4),(trp_dragonfly,5,10)]),
  ("scottish_2",   "scottish Warband",   icon_axeman|carries_goods(2),0, fac_scotland, soldier_personality, [(trp_scottish_guard,3,5),(trp_scottish_swordman,4,8),(trp_lizard_rider_1,7,15),(trp_scottish_pikeman_2,8,15),(trp_lizard_axeman_1,8,16),(trp_lizard_axeman_2,4,8)]),
  ("scottish_huge",   "scottish Warband",icon_huge_axeman|carries_goods(2),0, fac_scotland, soldier_personality, [(trp_lich_3,1,3),(trp_lizard_dragon,3,5),(trp_scottish_pikeman_3,15,20),(trp_lizard_rider_1,10,20),(trp_draugr_2,25,30),(trp_scottish_swordman,5,10)]),
  
  ("rus_1",   "rus cav",  icon_vaegir_knight|carries_goods(2),0, fac_cossack, soldier_personality, [(trp_rus_dvor_cavalry,4,10),(trp_rus_cossack_2,6,18),(trp_rus_cossack,6,18)]),
    
  ("rus_2",   "rus foot",   icon_vaegir_knight|carries_goods(2),0, fac_cossack, soldier_personality, [(trp_taiga_bandit_leader,5,8),(trp_taiga_brigand,5,18),(trp_balkan_archer_2,7,14),(trp_balkan_billman_3,4,10)]),
  
  ("rus_3",   "rus Warriors",  icon_vaegir_knight|carries_goods(2),0, fac_cossack, soldier_personality, [(trp_rus_cossack_3,7,14),(trp_taiga_bandit_leader,7,14),(trp_rus_dvor_cavalry,4,10),(trp_balkan_billman_2,5,10)]),
  ("rus_4",   "rus Warband",   icon_vaegir_knight|carries_goods(2),0, fac_cossack, soldier_personality, [(trp_rus_cossack,7,14),(trp_balkan_archer_3,7,14),(trp_rus_dvor_cavalry_2,4,10),(trp_balkan_billman_3,5,10)]),
    
  ("rus_deserters", "rus_deserters", icon_vaegir_knight|carries_goods(8), 0,fac_cossack,bandit_personality, [(trp_rus_boyar_2,4,8),(trp_balkan_billman_3,10,15),(trp_balkan_archer_3,10,15),(trp_rus_cossack_2,14,20),(trp_taiga_bandit_leader,10,15)]),
  ("rus_army", "rus_army", icon_huge_gray_knight|carries_goods(8), 0,fac_cossack,bandit_personality, [(trp_rus_palace_guard,5,8),(trp_rus_cossack_3,10,15),(trp_balkan_billman_3,10,15),(trp_taiga_bandit_leader,10,20),(trp_balkan_archer_3,10,20)] ),
    
  ("welsh",   "Welsh hunter",   icon_archer|carries_goods(2),0, fac_welsh, soldier_personality, [(trp_welsh_longbowm_1,7,14),(trp_welsh_longbowm_3,2,6),(trp_welsh_spearman_1,2,6)]),
  ("welsh_2",   "Welsh hunter",   icon_archer|carries_goods(2),0, fac_welsh, soldier_personality, [(trp_welsh_longbowm_2,7,14),(trp_welsh_spearman_1,5,11),(trp_welsh_longbowm_3,5,11),(trp_welsh_spearman_2,1,5)]),
  ("welsh_huge",   "Welsh hunter",   icon_huge_archer|carries_goods(2),0, fac_welsh, soldier_personality, [(trp_welsh_longbowm_3,25,51),(trp_welsh_spearman_1,25,31),(trp_welsh_spearman_2,5,11)]),
  
  ("swiss",   "swiss Patrol",   icon_axeman|carries_goods(2),0, fac_swiss, soldier_personality, [(trp_german_reitern_1,0,1),(trp_german_pikeman_1,10,15),(trp_german_twohander_2,5,5),(trp_iberian_town_footman_1,2,5),(trp_german_crossbow_2,2,5)]),
  ("swiss_2",   "swiss Patrol",   icon_axeman|carries_goods(2),0, fac_swiss, soldier_personality, [(trp_german_pikeman_2,15,20),(trp_german_twohander_2,5,10),(trp_iberian_knight_2,5,10),(trp_german_crossbow_3,5,10)]),
  ("swiss_huge",   "swiss Patrol",   icon_huge_axeman|carries_goods(2),0, fac_swiss, soldier_personality, [(trp_german_reitern_2,5,5),(trp_german_pikeman_3,20,20),(trp_german_crossbow_4,10,10),(trp_german_twohander_3,20,20),(trp_iberian_town_footman_2,10,10),(trp_german_crossbow_3,15,15)]),
  

  ("troll","Roving troll",icon_wild_troll|carries_goods(8),0,fac_orc,dark_personality,
  [(trp_troll_2,0,2),(trp_troll_1,2,8), (trp_goblin_skirmisher,2,10),(trp_goblin,8,10)]),
    
  ("ogre_tribe",     "ogre Warriors",     icon_orc_tribal|carries_goods(2),0, fac_orc, soldier_personality, 
  [(trp_ogre_war,1,4),(trp_ogre,5,15),(trp_ogre_young,7,14)]),
  ("ogre_warrior",     "ogre Warriors",      icon_uruk|carries_goods(2),0, fac_orc, soldier_personality, 
  [(trp_troll_1, 0, 1),(trp_ogre_mega, 0, 2),(trp_ogre_war,8,16),(trp_ogre,7,14)]),
  ("ogre_huge",     "ogre Warriors",      icon_uruk_x4|carries_goods(2),0, fac_orc, soldier_personality, 
  [(trp_troll_2, 1, 1),(trp_ogre_mega, 1, 2),(trp_ogre_war,8,16),(trp_ogre,8,16),(trp_ogre_young,8,16)]),

  ("goblin_looter", "goblin_looter", icon_orc_tribal|carries_goods(8), 0, fac_orc, bandit_personality, 
  [(trp_goblin_guard,0,2),(trp_goblin,8,20),(trp_goblin_horseman,1,4)] ),
  
  ("goblin_tribe", "goblin_tribe", icon_orc_tribal_x4|carries_goods(9), 0, fac_orc, bandit_personality, 
  [(trp_goblin_guard,1,10),(trp_goblin_knight,1,3),(trp_goblin_horseman,2,5),(trp_goblin_footman,10,15),(trp_goblin,50,100)] ),
  ("goblin_brigand","goblin_brigand",icon_orc|carries_goods(9),0,fac_orc,bandit_personality,
  [(trp_goblin_knight,1,1),(trp_goblin_horseman,3,5),(trp_goblin_infantry,5,5), (trp_goblin_skirmisher,2,17),(trp_goblin_footman,4,34),(trp_goblin_bomber,1,4)]),
  
  ("goblin_warrior",   "goblin_Warriors",  icon_orc|carries_goods(2),0, fac_orc, soldier_personality, 
  [(trp_troll_2,0,1),(trp_goblin_guard,2,4),(trp_goblin_infantry,7,14),(trp_goblin_crossbowman,5,10),(trp_goblin_bomber,4,4)]),
  
  ("goblin_huge","goblin_Warband",icon_orc_x4|carries_goods(9),0,fac_orc,soldier_personality, [(trp_cyclop,2,5),(trp_goblin_horseman,15,25),(trp_goblin_guard,5,15),(trp_goblin_crossbowman,15,25),(trp_goblin_infantry,15,25),(trp_goblin_bomber,5,10)]),

  ("goblin_raider",   "goblin_raiders",  icon_wargrider_run|carries_goods(2),0, fac_orc, soldier_personality, 
  [(trp_goblin_knight,2,4),(trp_goblin_horseman,7,14)]),

  ("orc_bandits","orc Bandits",icon_orc|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_orc_big,1,3),(trp_orc_boy,8,37),(trp_arrer_youngun,4,15)]),

  ("orc_raiders", "orc_raiders", icon_wild_troll|carries_goods(5), 0, fac_orc, soldier_personality, [(trp_troll_1,1,4),(trp_orc_blackorc_boss,4,10),(trp_goblin_infantry,6,15),(trp_orc_blackorc,6,15)] ),
    
  ("orc_warrior","orc_warrior",icon_orc|carries_goods(5),0,fac_orc,dark_personality,[(trp_orc_boar_big,1,1),(trp_orc_big,1,3),(trp_troll_1,1,1),(trp_orc_warrior,2,18),(trp_orc_boy,4,10),(trp_orc_arrer_boy,4,10)]),
  
  ("orc_warband", "blackorc_warband", icon_wild_troll|carries_goods(5), 0, fac_orc, soldier_personality, [(trp_troll_2,1,3),(trp_orc_blackorc_boss,3,8),(trp_orc_veterun_blackorc,2,5),(trp_orc_blackorc,4,10), (trp_goblin_crossbowman,4,10),(trp_goblin_infantry,10,20)] ),
  
  
  ("orc_huge_warband_1","orc_huge_warband",icon_wargrider_walk_x4|carries_goods(5),0,fac_orc,dark_personality,[(trp_demon_4_2,1,3),(trp_cyclop,2,3),(trp_ogre_war,10,30),(trp_ogre_mega,10,20),(trp_ogre_cannon,2,10),(trp_goblin_guard,15,20)]),
  
  ("orc_huge_warband_2","orc_huge_warband",icon_wild_troll|carries_goods(5),0,fac_orc,dark_personality,[(trp_orc_big_boss,1,3),(trp_troll_2,3,5),(trp_orc_veteran_boar,5,20),(trp_orc_veterun_blackorc,10,30),(trp_orc_blackorc_boss,1,10),(trp_orc_big,15,40)]),

  ("wood_elven_1","wood_elven tribe",icon_mirkwood_elf|carries_goods(2),0,fac_forest_ranger,dark_personality,
  [(trp_woodelf_druid_1,0,2),(trp_woodelf_sworddancer,1,3),(trp_dryad,1,3),(trp_woodelf_recruit,8,37),(trp_woodelf_scout,4,15),(trp_grandelf_recruit,0,5,pmf_is_prisoner)]),
  ("wood_elven_2","wood_elven scout",icon_mirkwood_elf|carries_goods(2),0,fac_forest_ranger,dark_personality,
  [(trp_woodelf_druid_1,1,5),(trp_woodelf_stinger,3,9),(trp_dryad,2,5),(trp_woodelf_scout,8,27),(trp_woodelf_watchman,4,15),(trp_grandelf_recruit,0,5,pmf_is_prisoner)]),
  ("wood_elven_3","wood_elven hunter",icon_mirkwood_elf_x3|carries_goods(2),0,fac_forest_ranger,dark_personality,
  [(trp_woodelf_druid_2,1,5),(trp_woodelf_m_hunter,5,15),(trp_woodelf_cavalry,2,5),(trp_woodelf_swordman,5,15),(trp_woodelf_hunter,8,16),(trp_woodelf_spearman,5,8)]),
  ("wood_elven_4","wood_elven Ranger",icon_mirkwood_elf_x3|carries_goods(2),0,fac_forest_ranger,dark_personality,
  [(trp_green_dragon,1,3),(trp_woodelf_druid_2,2,5),(trp_woodelf_sharpshooter,1,12),(trp_woodelf_sworddancer,3,9),(trp_woodelf_stinger,6,18),(trp_woodelf_swordman,6,18)]),

  ("grand_elven_1","grand_elven tribe",icon_lorien_elf_a|carries_goods(2),0,fac_elf,dark_personality,
  [(trp_ent_1,0,2),(trp_grandelf_arcane_guard,0,2),(trp_pixie,1,3),(trp_grandelf_recruit,8,37),(trp_grandelf_infantry,4,15),(trp_dwarf_miner,0,5,pmf_is_prisoner)]),
  ("grand_elven_2","grand_elven warden",icon_lorien_elf_b|carries_goods(2),0,fac_elf,dark_personality,
  [(trp_ent_1,1,5),(trp_grandelf_swordman_adv,3,9),(trp_pixie,2,5),(trp_grandelf_warden,8,27),(trp_grandelf_infantry,4,15),(trp_dwarf_miner,0,5,pmf_is_prisoner)]),
  ("grand_elven_3","grand_elven Warband",icon_lorien_elf_b_x3|carries_goods(2),0,fac_elf,dark_personality,
  [(trp_ent_1,1,5),(trp_grandelf_guard,5,15),(trp_grandelf_mage_1,2,5),(trp_grandelf_swordman_adv,5,15),(trp_grandelf_marksman,8,16),(trp_grandelf_arcane_archer,5,8)]),
  ("grand_elven_4","grand_elven Army",icon_lorien_elf_b_x3|carries_goods(2),0,fac_elf,dark_personality,
  [(trp_gold_dragon,1,2),(trp_grandelf_mage_2,2,5),(trp_grandelf_cavalry,1,12),(trp_grandelf_arcane_guard,3,9),(trp_grandelf_swordman,6,18),(trp_grandelf_marksman,6,18)]),

  ("dwarf_1","dwarf_miner",icon_dwarf|carries_goods(2),0,fac_dwarf,highland_personality,[(trp_giant_1,1,4),(trp_dwarf_warrior,4,8),(trp_dwarf_musketeer_1,2,8),(trp_dwarf_miner,9,18),(trp_woodelf_recruit,0,5,pmf_is_prisoner)]),
  
  ("giant_1",   "giant",  icon_axeman|carries_goods(2),0, fac_dwarf, highland_personality, [(trp_giant_1,4,25),(trp_giant_1_3,2,5)]),
  ("giant_2",   "giant",  icon_axeman|carries_goods(2),0, fac_dwarf, highland_personality, [(trp_giant_1,5,10),(trp_giant_1_2,7,14),(trp_giant_1_3,7,14)]),
  ("giant_1_huge",   "giant",  icon_huge_axeman|carries_goods(2),0, fac_dwarf, dark_personality, [(trp_giant_1,6,30),(trp_giant_3,4,10)]),
  ("giant_2_huge",   "giant",  icon_huge_axeman|carries_goods(2),0, fac_dwarf, dark_personality, [(trp_giant_1,5,20),(trp_giant_2,7,14),(trp_giant_1_3,7,14)]),
  
  ("dwarf_2_1",   "dwarf_Patrol",   icon_dwarf|carries_goods(2),0, fac_dwarf, dark_personality,
  [(trp_dwarf_bear_rider,5,10),(trp_dwarf_veteran,7,14),(trp_giant_2,2,5),(trp_woodelf_recruit,2,5,pmf_is_prisoner)]),
  ("dwarf_2_2",   "dwarf_Patrol",  icon_dwarf|carries_goods(2),0, fac_dwarf, dark_personality, 
  [(trp_dwarf_veteran,7,14),(trp_dwarf_musketeer_1,7,14),(trp_giant_3,2,5),(trp_woodelf_recruit,2,5,pmf_is_prisoner)]),
  ("dwarf_2_3",   "dwarf_Patrol",   icon_dwarf|carries_goods(2),0, fac_dwarf, dark_personality, 
  [(trp_giant_1,7,14),(trp_dwarf_musketeer_2_2,7,14),(trp_giant_2,2,5),(trp_woodelf_recruit,2,5,pmf_is_prisoner)]),

  ("dwarf_3", "dwarf_War Party", icon_dwarf|carries_goods(5), 0, fac_dwarf, dark_personality, [(trp_fire_dragon,1,1),(trp_dwarf_guard_3,2,5),(trp_dwarf_guard_1,4,10),(trp_dwarf_ironbreaker,5,10),(trp_dwarf_bear_rider,5,10),(trp_dwarf_musketeer_2_1,10,20)]),
  ("dwarf_4", "dwarf_Army", icon_dwarf_x3|carries_goods(5), 0, fac_dwarf, dark_personality, 
  [(trp_lava_dragon,1,3),(trp_dwarf_guard_3,2,5),(trp_dwarf_musketeer_3,15,20),(trp_dwarf_guard_2,15,20),(trp_dwarf_berserker,10,15),(trp_dwarf_ironbreaker,15,25)]),
  
  ("rat_tribe", "rat_tribe", icon_orc_tribal_x4|carries_goods(9), 0, fac_beast, bandit_personality, 
   [(trp_rat_3,1,10),(trp_minotaur_3,1,3),(trp_rat_2,10,15),(trp_rat_1,50,100)] ),

  ("rat_looter", "rat_looter", icon_orc_tribal|carries_goods(8), 0, fac_beast, bandit_personality, 
   [(trp_minotaur_2,0,2),(trp_rat_1,8,20),(trp_rat_2,0,4)] ),
  
  ("rat_brigand","rat_sout",icon_orc|carries_goods(9),0,fac_beast,bandit_personality,
   [(trp_minotaur_3,1,1),(trp_rat_4,3,10),(trp_rat_3,5,14), (trp_rat_2,10,25), (trp_rat_5_3,1,5),(trp_rat_bomber,4,4)]),
                          
  ("rat_huge","rat_Warband",icon_orc_x4|carries_goods(9),0,fac_beast,soldier_personality, 
   [(trp_minotaur_3,1,5),(trp_rat_5_1,10,15),(trp_rat_5_2,5,15),(trp_minotaur_2,10,15),(trp_rat_4,10,20),(trp_rat_5_3,5,5)]),

  ("minotaur","minotaur",icon_axeman|carries_goods(2),0,fac_beast,dark_personality,[(trp_minotaur_3,1,3),(trp_minotaur_1,8,27),(trp_minotaur_2,4,15),(trp_medusa_1,2,4)]),
  ("minotaur_2","minotaur",icon_axeman|carries_goods(2),0,fac_beast,dark_personality,[(trp_minotaur_2,8,18),(trp_medusa_2,1,3),(trp_minotaur_3,4,15),(trp_medusa_1,2,9),(trp_undead_magic_1,5,5),(trp_rat_bomber,4,4)]),
  
  ("minotaur_huge","minotaur",icon_drow_army|carries_goods(10),0,fac_beast,dark_personality,[(trp_minotaur_3,2,6),(trp_rat_4,6,15),(trp_minotaur_2,4,15),(trp_red_dragon,1,2),(trp_medusa_2,5,10),(trp_rat_bomber,4,4)]),
  
  ("drow_elven_1","drow_elven assassin",icon_drow_fighter|carries_goods(2),0,fac_beast,dark_personality,
  [(trp_drowelf_which_1,1,5),(trp_drowelf_assassin_2,3,9),(trp_minotaur_2,8,27),(trp_drowelf_assassin_1,4,15)]),
  ("drow_elven_2","drow_elven raider",icon_drow_fighter|carries_goods(2),0,fac_beast,dark_personality,
  [(trp_black_dragon,0,1),(trp_drowelf_which_1,1,5),(trp_minotaur_3,5,15),(trp_drowelf_raider_2,5,15),(trp_drowelf_raider_1,8,16),(trp_drowelf_assassin_3,5,5)]),
  ("drow_elven_3","drow_elven Army",icon_drow_army|carries_goods(10),0,fac_beast,dark_personality,
  [(trp_black_dragon,1,2),(trp_drowelf_which_2,2,5),(trp_drowelf_raider_2,4,12),(trp_rat_5_3,5,9),(trp_drowelf_infantry_2,6,18),(trp_drowelf_assassin_2,6,18)]),
    
  ("mage","mage",icon_axeman|carries_goods(2),0,fac_dark_knights,dark_personality,[(trp_human_magic_2,1,3),(trp_golem_1,5,15),(trp_golem_3,5,10),(trp_human_magic_1,4,7)]),
  ("mage_huge",   "mage",  icon_huge_axeman|carries_goods(2),0, fac_dark_knights, dark_personality, [(trp_human_magic_3,4,15),(trp_human_magic_2,5,10),(trp_golem_3,5,15),(trp_golem_4,1,5),(trp_gargoyle,1,2)]),
  ("titan","titan",icon_axeman|carries_goods(2),0,fac_dark_knights,dark_personality,[(trp_titan_1,1,3),(trp_golem_1,10,15),(trp_human_magic_2,5,10),(trp_titan_0,4,7)]),
  ("titan_huge",   "titan",  icon_huge_axeman|carries_goods(2),0, fac_dark_knights, dark_personality, [(trp_titan_0,4,15),(trp_human_magic_2,5,10),(trp_golem_3,10,15),(trp_titan_1,1,5),(trp_titan_2,1,2)]),
  
  ("mummy","mummy",icon_skeletons|carries_goods(2),0,fac_demon,dark_personality,[(trp_mummy_1,4,28),(trp_mummy_2,4,15),(trp_mummy_3,1,3)]),
  ("mummy_2","mummy",icon_skeletons|carries_goods(2),0,fac_demon,dark_personality,[(trp_mummy_2_1,4,28),(trp_werewolf_1,4,15),(trp_mummy_4,1,3)]),
  
  ("mummy_huge","mummy",icon_skeletons_x3|carries_goods(10),0,fac_demon,dark_personality,[(trp_mummy_4,1,3),(trp_mummy_2_1,5,10),(trp_mummy_2,4,10),(trp_werewolf_1,5,10),(trp_mummy_3,1,3)]),
  
  ("werewolf_1","werewolf",icon_axeman|carries_goods(2),0,fac_demon,dark_personality,[(trp_werewolf_1,6,30),(trp_werewolf_1_a,3,4)]),
  #("werewolf_2","White Werewolf",icon_axeman|carries_goods(2),0,fac_dark_knights,dark_personality,[(trp_werewolf_2,6,30)]),
  
  ("werewolf_1_huge","werewolf",icon_huge_axeman|carries_goods(10),0,fac_demon,dark_personality,[(trp_mummy_4,1,3),(trp_werewolf_1,6,30),(trp_werewolf_1_a,3,15)]),
  #("werewolf_2_huge","White Werewolf",icon_huge_axeman|carries_goods(10),0,fac_dark_knights,dark_personality,[(trp_werewolf_2,6,30),(trp_werewolf_2_a,6,15)]),
  
  ("undead_1","undead_Party",icon_skeletons|carries_goods(2),0,fac_undeads_2,bandit_personality,
  [(trp_lich_1,0,1),(trp_zombie_2,2,18),(trp_zombie_1,14,40),(trp_undead_magic_2,1,4)]),
  
  ("undead_1_2","undead_Party",icon_skeleton_archer|carries_goods(2),0,fac_undeads_2,bandit_personality,
  [(trp_undead_horse_2,0,1),(trp_skeleton_lord,3,9),(trp_se_pikeman_1,2,10),(trp_se_musketeer_1,2,13),(trp_se_billman_1,6,20)]),
  ("undead_1_3","undead_Party",icon_skeletons|carries_goods(2),0,fac_undeads_2,bandit_personality,
  [(trp_wraith,0,1),(trp_dullahan,2,6),(trp_wight,2,13),(trp_ghost,5,20)]),
  
  ("undead_2","undead_warband",icon_single_unholy_knight|carries_goods(2),0,fac_undeads_2,dark_personality,
  [(trp_undead_horse_3,1,2),(trp_undead_horse_2,2,6),(trp_undead_horse_1,3,12),(trp_skeleton_warrior,4,18),(trp_skeleton_archer,4,24)]),
  ("undead_3","undead_army",icon_skeleton_archer|carries_goods(2),0,fac_undeads_2,dark_personality,
  [(trp_lich_2,1,3),(trp_lich_1,2,6),(trp_undead_magic_2,2,12),(trp_skeleton_lord,8,16),(trp_ghost,8,10),(trp_wight,4,10)]),
  ("undead_2_huge","undead_warband",icon_unholy_knights|carries_goods(2),0,fac_undeads_2,dark_personality,
  [(trp_wraith,3,6),(trp_undead_horse_3,3,9),(trp_undead_horse_1,9,20),(trp_undead_horse_2,4,18),(trp_dullahan,4,24),(trp_skeleton_archer,4,24)]),
  ("undead_3_huge","undead_army",icon_undead_army|carries_goods(2),0,fac_undeads_2,dark_personality,
  [(trp_ghost_dragon,4,12),(trp_lich_2,4,9),(trp_lich_1,4,12),(trp_skeleton_lord,8,16),(trp_wight,12,20),(trp_undead_magic_2,2,12)]),
  
  ("undead_4","vampire_army",icon_shadows|carries_goods(20),0,fac_undeads_2,dark_personality,
  [(trp_vampire_3,1,6),(trp_undead_horse_1,2,6),(trp_vampire_2,3,12),(trp_vampire_assassin,6,24),(trp_peasant_woman,2,5,pmf_is_prisoner)]),
  ("undead_4_huge","vampire_army",icon_shadows|carries_goods(20),0,fac_undeads_2,dark_personality,
  [(trp_death,2,6),(trp_vampire_4,2,6),(trp_vampire_3,3,18),(trp_undead_horse_2,4,12),(trp_vampire_2,6,24),(trp_undead_magic_2,6,20)]),
  
  ("draugr_1","Draugr Thrall",icon_skeletons|carries_goods(2),0,fac_scotland,bandit_personality,
  [(trp_lich_3,0,1),(trp_draugr_lord,1,1),(trp_draugr_3,1,2),(trp_draugr_2,5,10), (trp_draugr_1,9,18)]),
  ("draugr_2", "Restless Dragon Priest", icon_undead_army|carries_goods(8), 0,fac_scotland,bandit_personality, 
  [(trp_lich_dragon,0,1),(trp_lich_3,1,1),(trp_draugr_lord,2,4),(trp_draugr_3,5,10), (trp_draugr_2,9,18)] ),
  
  
  ("demon_1_weak", "demon_Cultists", icon_axeman|carries_goods(8), 0, fac_demon, bandit_personality, 
   [(trp_demon_magic_2,0,2),(trp_ghazis_1,8,20),(trp_demon_human_2,4,8)] ),
  
  ("demon_2_weak", "demon_Cultists", icon_huge_axeman|carries_goods(9), 0, fac_demon, bandit_personality, 
   [(trp_demon_human_3,1,10),(trp_demon_magic_3,0,1),(trp_demon_human_2,10,15),(trp_ghazis_1,50,100)] ),
  
  ("demon_3_weak","demon_sout",icon_brigand|carries_goods(9),0,fac_demon,bandit_personality,
   [(trp_demon_magic_3,1,1),(trp_me_mercenary_swordsman_1,3,10),(trp_saracen_cav_1,5,14), (trp_ghazis_2,10,25), (trp_demon_human_4,1,5),(trp_demon_human_3,4,4)]),
                          
  ("demon_4_weak","demon_warband",icon_demon_x3|carries_goods(9),0,fac_demon,soldier_personality, 
   [(trp_demon_magic_3,1,5),(trp_demon_1,10,15),(trp_demon_human_3,5,15),(trp_saracen_cav_2,10,15),(trp_me_mercenary_swordsman_1,10,20),(trp_demon_1_2,5,5)]),
  
  
  ("demon_1","demon_Cultists",icon_demons|carries_goods(2),0,fac_demon,bandit_personality,
  [(trp_demon_2,3,5),(trp_demon_1_2,2,5),(trp_demon_human_3,2,5),(trp_demon_magic_1,4,6),(trp_demon_human_1,5,20)]),
  
  ("demon_2","demon_warband",icon_demons|carries_goods(2),0,fac_demon,dark_personality,
  [(trp_demon_human_5_2,1,2),(trp_demon_magic_3,1,3),(trp_demon_human_4,3,12),(trp_demon_magic_2,2,8),(trp_demon_1,4,24),(trp_demon_human_2,4,24)]),
  ("demon_2_huge","demon_warband",icon_demon_x3|carries_goods(2),0,fac_demon,dark_personality,
  [(trp_demon_6,1,2),(trp_demon_magic_3,3,6),(trp_demon_human_5_1,3,9),(trp_demon_human_4,9,18),(trp_demon_4,4,10),(trp_demon_magic_2,4,8)]),

  ("demon_3","demon_army",icon_demons|carries_goods(2),0,fac_demon,dark_personality,
  [(trp_demon_5,1,1),(trp_demon_4,2,4),(trp_demon_3,2,4),(trp_demon_1_2,4,16),(trp_demon_2,8,16)]),
  ("demon_3_huge","demon_army",icon_demon_x3|carries_goods(2),0,fac_demon,dark_personality,
  [(trp_demon_5,3,6),(trp_demon_3,2,12),(trp_demon_1_2,8,16),(trp_demon_2,8,16),(trp_demon_4,2,12)]),
  
    
  ("hospitalier_cultists", "Order of the hospitalier Cultists", icon_axeman|carries_goods(5), 0, fac_demon_hunters, soldier_personality, [(trp_teutonic_pilgrim,6,12),(trp_teutonic_spearman,3,8),(trp_teutonic_horse_1,2,4),(trp_monk,3,7)] ),
  
  ("hospitalier_knights","Order of the hospitalier",icon_gray_knight,0,fac_demon_hunters,soldier_personality,  [(trp_teutonic_horse_2, 6, 10),(trp_france_crossbow_2, 6, 10),(trp_teutonic_horse_1, 6, 10),(trp_teutonic_sword, 6, 10), (trp_france_horse_1,6,12)]),

  ("hospitalier_knights_2","Order of the hospitalier",icon_gray_knight,0,fac_demon_hunters,soldier_personality,  [(trp_teutonic_dis_knight,2,5), (trp_hospitaller_knight_2,2,5), (trp_clerics,5,10), (trp_hospitaller_knight,5,15), (trp_teutonic_dis_halbbruder,6,10), (trp_teutonic_spearman,10,20)]),

  ("hospitalier_knights_huge","Order of the hospitalier Legion",icon_huge_gray_knight,0,fac_demon_hunters,soldier_personality,  [(trp_hospitaller_knight_2,5,15), (trp_priest,7, 15), (trp_france_crossbow_3,7, 15), (trp_hospitaller_knight,7, 15), (trp_archangle,3, 6), (trp_teutonic_dis_knight,7, 15)]),
    
  #("dark_hunters","Dark Hunters",icon_gray_knight,0,fac_hospitalier_knights,soldier_personality,[(trp_dark_knight,4,42),(trp_dark_sniper,10,20),(trp_dark_hunter,13,25)]),

##  ("peasant","Peasant",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,1,6),(trp_peasant_woman,0,7)]),


  ("forest_bandits","Forest Bandits",icon_archer|carries_goods(2),0,fac_forest_ranger,bandit_personality,[(trp_welsh_spearman_2,1,3),(trp_forest_bandit,8,37),(trp_welsh_longbowm_1,4,15)]),
  ("taiga_bandits","Tundra Bandits",icon_axeman|carries_goods(2),0,fac_cossack,bandit_personality,[(trp_taiga_bandit,4,28),(trp_taiga_brigand,4,15),(trp_taiga_bandit_leader,1,3)]),
  ("steppe_bandits","Steppe Bandits",icon_khergit|carries_goods(2),0,fac_khergits,bandit_personality,[(trp_black_khergit_raidmaster,1,1),(trp_steppe_tribesman,8,31)]),
  ("sea_raiders","Sea Raiders",icon_axeman|carries_goods(2),0,fac_sea_raiders,bandit_personality,[(trp_nord_footman,7,14),(trp_mercenary_berserker,5,11),(trp_nord_warrior,4,11),(trp_nord_champion,5,10),(trp_nord_valkyrie_2,0,2)]),
  ("mountain_bandits","Mountain Bandits",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_mountain_bandit,5,32),(trp_mountain_bandit_leader,1,10)]),
  ("desert_bandits","Desert Bandits",icon_brigand|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_saracen_cav_2,4,10),(trp_desert_bandit,8,25)]),
  
  
  #("dark_cultists", "Dark_Cultists", icon_axeman|carries_goods(5), 0, fac_dark_knights, dark_personality, [(trp_teutonic_pilgrim,10,40),(trp_dark_warrior,4,10),(trp_dark_hunter,3,5),(trp_dark_fighter,8,13)] ),
  #("mountain_tribesman","mountain_tribesman",icon_axeman|carries_goods(2),0,fac_mountain_tribe,highland_personality,[(trp_mountain_warchief,1,3),(trp_mountain_headhunter,4,15),(trp_mountain_fighter,4,15),(trp_mountain_tribesman,8,30)]),
  ("norman", "norman", icon_huge_flagbearer|carries_goods(8), 0,fac_scotland,bandit_personality, [(trp_nord_valkyrie_2,1,5),(trp_nord_warrior,4,20),(trp_nord_mounted_scout_2,3,15),(trp_nord_raider,1,15)] ),
  ("camel_cavalry", "camel_cavalry", icon_vaegir_knight|carries_goods(8), 0,fac_outlaws,bandit_personality, [(trp_marinid_camel_3_1,3,15),(trp_marinid_camel_2,3,35)] ),
  ("cossack", "cossack", icon_vaegir_knight|carries_goods(8), 0, fac_cossack,bandit_personality, [(trp_rus_boyar_2,1,5),(trp_taiga_brigand,2,18),(trp_rus_cossack,6,24)] ),
  ("forest_brotherhood", "forest_Brotherhood", icon_archer|carries_goods(8),0,fac_forest_ranger,bandit_personality, [(trp_welsh_longbowm_3,1,4),(trp_welsh_longbowm_2,3,15),(trp_welsh_spearman_1,4,15),(trp_forest_bandit,4,32)] ),

  ("deserters","Deserters",icon_generic_knight_x3|carries_goods(3),0,fac_deserters,bandit_personality,[]),

  
  ("forest_hunter", "forest_hunter", icon_archer|carries_goods(8),0,fac_forest_ranger,bandit_personality, [(trp_welsh_longbowm_3,3,9),(trp_welsh_longbowm_2,5,20),(trp_welsh_spearman_2,12,25),(trp_sherwood_archer,10,17)] ),
  ("sherwood_warband", "sherwood_warband", icon_huge_archer|carries_goods(8),0,fac_forest_ranger,bandit_personality, [(trp_welsh_longbowm_3,12,20),(trp_sherwood_archer,11,31),(trp_welsh_longbowm_2,25,51),(trp_welsh_spearman_2,25,51)] ),

  #("dark_warriors", "Dark_warriors", icon_gray_knight|carries_goods(5), 0, fac_dark_knights, dark_personality, [(trp_dark_rider,3,5),(trp_dark_halberd,5,15),(trp_dark_sergeant,5,15),(trp_dark_warrior,8,21),(trp_dark_fighter,10,30)] ),
  #("dark_hunters", "Dark Hunters", icon_gray_knight|carries_goods(2), 0, fac_dark_knights, dark_personality, [(trp_dark_knight,5,20),(trp_dark_rider,4,21),(trp_dark_sergeant,10,20),(trp_dark_ranged,13,25)] ),
  #("dark_leader", "Dark leader", icon_gray_knight|carries_goods(2), 0, fac_dark_knights, soldier_personality, [(trp_dark_knight,25,42),(trp_dark_rider,13,25)] ),
  
  #("mountain_raiders", "mountain_raiders", icon_axeman|carries_goods(5), 0, fac_mountain_tribe, highland_personality, [(trp_mountain_warchief,6,10),(trp_mountain_warrior,8,20),(trp_mountain_headhunter,8,20),(trp_mountain_pikeman,8,20)] ),
  #("mountain_warband", "mountain_warband", icon_axeman|carries_goods(5), 0, fac_mountain_tribe, highland_personality, [(trp_mountain_warchief,12,20),(trp_mountain_swordman,12,20),(trp_mountain_axeman,12,20),(trp_mountain_headhunter,12,20),(trp_mountain_pikeman,16,40)] ),
  #("mountain_warchief", "mountain_warchief", icon_huge_axeman|carries_goods(5), 0, fac_mountain_tribe, highland_personality, [(trp_mountain_warchief,12,20),(trp_mountain_swordman,25,50),(trp_mountain_axeman,25,50),(trp_mountain_headhunter,25,50),(trp_mountain_pikeman,25,50)] ),
  
  ("black_khergit_raiders","Black Khergit Raiders",icon_khergit_horseman_b|carries_goods(5),0,fac_khergits,bandit_personality,[(trp_black_khergit_raidmaster,0,1),(trp_black_khergit_lancer,1,6),(trp_black_khergit_guard,2,18),(trp_black_khergit_horseman,6,24)]),
  ("black_khergit_marauders","Black Khergit Marauders",icon_easterling_horseman|carries_goods(5),0,fac_khergits,bandit_personality,[(trp_black_khergit_raidmaster,1,3),(trp_black_khergit_lancer,4,16),(trp_black_khergit_guard,5,15),(trp_black_khergit_horseman,12,24)]),
  ("black_khergit_warband","Black Khergit warband",icon_easterling_horseman_x3|carries_goods(5),0,fac_khergits,bandit_personality,[(trp_black_khergit_raidmaster,1,12),(trp_black_khergit_lancer,25,25),(trp_black_khergit_guard,25,25),(trp_black_khergit_horseman,50,50)]),
  
  #("nomad","Steppe nomad",icon_khergit|carries_goods(2),0,fac_khergits,bandit_personality,[(trp_khergit_skirmisher,4,30),(trp_khergit_horse_archer,2,15),(trp_khergit_nomad_horseman,2,15),(trp_khergit_nomad_leader,1,5)]),
  
  ("peasant_rebels", "Peasant Rebels", icon_huge_peasant_1,0,fac_deserters,bandit_personality,[(trp_farmer,100,300)]),
  
  ("merchant_caravan","Merchant Caravan",icon_mule|carries_goods(20)|pf_auto_remove_in_town|pf_quest_party,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_merchant_cavalry_militia,5,15)]),
  ("troublesome_bandits","Troublesome Bandits",icon_gray_knight|carries_goods(9)|pf_quest_party,0,fac_outlaws,bandit_personality,[(trp_we_knight_3,1,1),(trp_we_knight_2,1,5),(trp_raider,15,25)]),
      
  ("bandits_awaiting_ransom","Bandits Awaiting Ransom",icon_brigand|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_we_knight_3,1,1),(trp_slave_hunter,12,29),(trp_raider,12,29),(trp_kidnapped_girl,1,1,pmf_is_prisoner)]),
  ("kidnapped_girl","Kidnapped Girl",icon_woman|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_kidnapped_girl,1,1)]),

##  ("farmers","Farmers",icon_peasant,0,fac_innocents,merchant_personality,[(trp_farmer,11,22),(trp_peasant_woman,16,44)]),
  ("village_farmers","Village Farmers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_peasant_woman,3,8)]),
##  ("refugees","Refugees",icon_woman_b,0,fac_innocents,merchant_personality,[(trp_refugee,19,48)]),

  ("spy_partners", "Unremarkable Travellers", icon_gray_knight|carries_goods(10)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy_partner,1,1),(trp_caravan_guard,5,11)]),
  ("runaway_serfs","Runaway Serfs",icon_peasant|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_farmer,6,7), (trp_peasant_woman,3,3)]),
  ("spy", "Ordinary Townsman", icon_brigand|carries_goods(4)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy,1,1)]),
  ("sacrificed_messenger", "Sacrificed Messenger", icon_gray_knight|carries_goods(3)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[]),
##  ("conspirator", "Conspirators", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator,3,4)]),
##  ("conspirator_leader", "Conspirator Leader", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator_leader,1,1)]),
##  ("peasant_rebels", "Peasant Rebels", icon_peasant,0,fac_peasant_rebels,bandit_personality,[(trp_peasant_rebel,33,97)]),
##  ("noble_refugees", "Noble Refugees", icon_gray_knight|carries_goods(12)|pf_quest_party,0,fac_noble_refugees,merchant_personality,[(trp_noble_refugee,3,5),(trp_noble_refugee_woman,5,7)]),


  ("forager_party","Foraging Party",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("scout_party","Scouts",icon_gray_knight|carries_goods(1)|pf_show_faction,0,fac_commoners,bandit_personality,[]),
  ("patrol_party","Patrol",icon_gray_knight|carries_goods(2)|pf_show_faction,0,fac_commoners,soldier_personality,[]),
#  ("war_party", "War Party",icon_gray_knight|carries_goods(3),0,fac_commoners,soldier_personality,[]),
  ("messenger_party","Messenger",icon_gray_knight|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("raider_party","Raiders",icon_gray_knight|carries_goods(16)|pf_show_faction,0,fac_commoners,bandit_personality,[]),
  ("raider_captives","Raider Captives",0,0,fac_commoners,0,[(trp_peasant_woman,6,30,pmf_is_prisoner)]),
  ("kingdom_caravan_party","Caravan",icon_mule|carries_goods(25)|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_caravan_master,1,1),(trp_merchant_cavalry_militia,12,30)]),
  ("prisoner_train_party","Prisoner Train",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("default_prisoners","Default Prisoners",0,0,fac_commoners,0,[(trp_bandit,5,10,pmf_is_prisoner)]),

# Ozan BEGIN
  ("routed_warriors","Routed Enemies",icon_vaegir_knight,0,fac_commoners,soldier_personality,[]),
# Ozan END

# Caravans

  ("center_reinforcements","Reinforcements",icon_axeman|carries_goods(16),0,fac_commoners,soldier_personality,[(trp_townsman,5,30),(trp_watchman,4,20)]),
  
  #("kingdom_hero_party","{!}War Party",icon_flagbearer_a|pf_show_faction|pf_default_behavior,0,fac_commoners,soldier_personality,[]),
  ("kingdom_hero_party","{!}War Party",icon_flagbearer_2|pf_show_faction|pf_default_behavior,0,fac_commoners,soldier_personality,[]),
  ("adventurer_party","Adventurer Party",icon_flagbearer_2|pf_show_faction,0,fac_commoners,soldier_personality,[(trp_farmer,10,20),]),

# Reinforcements
#  ("default_reinforcements_a","default_reinforcements_a",0,0,1,0,[(trp_caravan_guard,1,10),(trp_watchman,3,16),(trp_farmer,9,24)]),
#  ("default_reinforcements_b","default_reinforcements_b",0,0,1,0,[(trp_mercenary,1,7),(trp_caravan_guard,3,10),(trp_watchman,3,15)]),
#  ("default_reinforcements_c","default_reinforcements_c",0,0,1,0,[(trp_hired_blade,1,7),(trp_mercenary,3,10),(trp_caravan_guard,3,15)]),
  ("player_faction_reinforcements_a", "{!}player_faction_reinforcements_a", 0, 0, 1, 0, [(trp_custom_infantry,2,6),(trp_custom_recruit,4,7)]),
  ("player_faction_reinforcements_b", "{!}player_faction_reinforcements_b", 0, 0, 1, 0, [(trp_custom_footman,2,4),(trp_custom_musket,2,4),(trp_custom_horseman,1,1)]),
  ("player_faction_reinforcements_c", "{!}player_faction_reinforcements_c", 0, 0, 1, 0, [(trp_custom_sergeant,2,3),(trp_custom_cavalry,2,3),(trp_custom_cannon_man,0,1)]),

  ("kingdom_1_reinforcements_a", "{!}_a", 0, 0, 1, 0, [(trp_teutonic_pilgrim,10,10),(trp_france_town_recruit,15,15),(trp_france_knight_1,5,5)]),
  ("kingdom_1_reinforcements_b", "{!}_b", 0, 0, 1, 0, [(trp_france_swordsman_1,2,6),(trp_france_crossbow_1,4,7)]),
  ("kingdom_1_reinforcements_c", "{!}_c", 0, 0, 1, 0, [(trp_france_knight_4,1,4),(trp_teutonic_horse_2,4,8),(trp_france_knight_1,2,8),(trp_france_crossbow_3, 9, 18)]), 

  ("kingdom_3_reinforcements_a", "{!}_a", 0, 0, 1, 0, [(trp_khergit_skirmisher,10,10),(trp_goblin,30,30),(trp_khergit_guard, 5, 5)]),
  ("kingdom_3_reinforcements_b", "{!}_b", 0, 0, 1, 0, [(trp_khergit_horse_archer,2,4),(trp_khergit_dis_guard,0,1),(trp_khergit_skirmisher,4,7)]),
  ("kingdom_3_reinforcements_c", "{!}_c", 0, 0, 1, 0, [(trp_troll_1,1,4),(trp_khergit_heavy,4,8),(trp_khergit_guard, 2, 8),(trp_khergit_dis_guard, 9, 18)]),

  ("kingdom_4_reinforcements_a", "{!}_a", 0, 0, 1, 0, [(trp_woodelf_recruit,5,5),(trp_england_town_recruit,20,20),(trp_england_knight_1,5,5)]),
  ("kingdom_4_reinforcements_b", "{!}_b", 0, 0, 1, 0, [(trp_woodelf_watchman,2,6),(trp_england_longbowm_1,4,7)]),
  ("kingdom_4_reinforcements_c", "{!}_c", 0, 0, 1, 0, [(trp_england_knight_3,1,4),(trp_england_swordsman_3,4,8),(trp_england_knight_1,2,8),(trp_england_longbowm_4, 9, 18)]), 

  ("kingdom_5_reinforcements_a", "{!}_a", 0, 0, 1, 0, [(trp_se_tribesman,15,15),(trp_italian_town_recruit,10,10),(trp_italian_horse_1,5,5)]),
  ("kingdom_5_reinforcements_b", "{!}_b", 0, 0, 1, 0, [(trp_italian_crossbow_2,2,6),(trp_se_musketeer_1,4,7)]),
  ("kingdom_5_reinforcements_c", "{!}_c", 0, 0, 1, 0, [(trp_italian_horse_4,1,4),(trp_italian_town_footman_3,4,8),(trp_italian_horse_2,2,8),(trp_italian_crossbow_3, 9, 18)]), 

  ("kingdom_7_reinforcements_a", "{!}_a", 0, 0, 1, 0, [(trp_iberian_town_militia,10,10),(trp_german_town_recruit,15,15),(trp_german_knight_1,5,5)]),
  ("kingdom_7_reinforcements_b", "{!}_b", 0, 0, 1, 0, [(trp_german_pikeman_1,2,6),(trp_german_crossbow_1,4,7)]),
  ("kingdom_7_reinforcements_c", "{!}_c", 0, 0, 1, 0, [(trp_german_knight_4,1,4),(trp_german_reitern_1,4,8),(trp_german_knight_1,2,8),(trp_german_twohander_3, 9, 18)]), 

  ("kingdom_8_reinforcements_a", "{!}_a", 0, 0, 1, 0, [(trp_balkan_vil_recruit,15,15),(trp_polish_town_recruit,10,10),(trp_polish_knight_1,5,5)]),
  ("kingdom_8_reinforcements_b", "{!}_b", 0, 0, 1, 0, [(trp_rus_cossack_2,2,6),(trp_polish_crossbow_2,3,5),(trp_balkan_archer_2,1,3)]),
  ("kingdom_8_reinforcements_c", "{!}_c", 0, 0, 1, 0, [(trp_polish_knight_3,1,4),(trp_rus_dvor_cavalry_2,4,8),(trp_polish_horse_4,2,8),(trp_polish_knight_1, 9, 18)]), 

  ("kingdom_9_reinforcements_a", "{!}_a", 0, 0, 1, 0, [(trp_turk_azap,15,15),(trp_mamluke_recruit,10,10),(trp_turk_sipahi, 5, 5)]),
  ("kingdom_9_reinforcements_b", "{!}_b", 0, 0, 1, 0, [(trp_janissary_archer,3,6),(trp_turk_azap,4,7)]),
  ("kingdom_9_reinforcements_c", "{!}_c", 0, 0, 1, 0, [(trp_turk_roy_sipahi,1,4),(trp_janissary_musketeer_2,4,8),(trp_turk_sipahi_lance, 2, 8),(trp_janissary_infantry_2, 9, 18)]),

  ("kingdom_10_reinforcements_a", "{!}_a", 0, 0, 1, 0, [(trp_nord_town_recruit, 10, 10),(trp_nord_knight_1,5,5),(trp_nord_recruit,15,15)]),
  ("kingdom_10_reinforcements_b", "{!}_b", 0, 0, 1, 0, [(trp_nord_crossbow_1,1,3),(trp_nord_skirmisher,3,5),(trp_nord_footman,2,5)]),
  ("kingdom_10_reinforcements_c", "{!}_c", 0, 0, 1, 0, [(trp_nord_knight_3,1,4),(trp_nord_knight_1,4,8),(trp_nord_champion,2,8),(trp_nord_axeman_2, 9, 18)]), 


  ("france_lance_t4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_france_knight_4, 1, 2),(trp_france_knight_3, 2, 4),(trp_angle, 1, 1),(trp_teutonic_dis_knight, 1, 2)]),
  
  
  ("france_lance_t3_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_grandelf_swordman_adv, 5, 5), (trp_france_swordsman_3, 10, 10)]),
  ("france_lance_t3_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_france_crossbow_4, 7, 7), (trp_france_archer_3, 7, 7)]),
  ("france_lance_t3_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_france_pikeman_4, 5, 5), (trp_france_pikeman_3, 10, 10)]),
  ("france_lance_t3_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_priest, 3, 5), (trp_teutonic_sword, 10, 10)]),
  ("france_lance_t3_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_france_knight_3, 3, 5), (trp_france_knight_2, 5, 5)]),
  
  ("france_lance_t2_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_france_swordsman_2, 5, 5), (trp_france_swordsman_1, 20, 20)]),
  ("france_lance_t2_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_france_archer_3, 5, 5), (trp_france_crossbow_2, 20, 20)]),
  ("france_lance_t2_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_france_pikeman_2, 5, 5), (trp_france_pikeman_1, 20, 20)]),
  ("france_lance_t2_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_clerics, 3, 5), (trp_teutonic_spearman, 10, 10)]),
  ("france_lance_t2_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_france_knight_2, 5, 5), (trp_france_knight_1, 10, 10)]),
  
  ("france_lance_t1_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_france_crossbow_2, 5, 5), (trp_france_crossbow_1, 20, 20)]),
  ("france_lance_t1_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_france_pikeman_1, 5, 5), (trp_france_militia, 20, 20)]),
  ("france_lance_t1_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_france_knight_1, 5, 5), (trp_france_town_recruit, 25, 25)]),
  ("france_lance_t1_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_monk, 5, 5), (trp_teutonic_pilgrim, 25, 25)]),
  ("france_lance_t1_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_france_knight_1, 5, 5), (trp_france_town_recruit, 25, 25)]),

  ("france_lance_end", "{!}Lance", 0, 0, fac_neutral, 0, []),

  ("order_lance_t4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_france_knight_4, 1, 1),(trp_sissofbattle_s, 1, 2),(trp_angle, 1, 2),(trp_france_knight_3, 2, 4),(trp_teutonic_horse_3, 2, 6)]),

  ("order_lance_t3_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_teutonic_horse_3, 5, 5), (trp_teutonic_horse_2, 10, 10)]),
  ("order_lance_t3_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_teutonic_dis_knight, 5, 5), (trp_teutonic_dis_halbbruder, 10, 10)]),
  ("order_lance_t3_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_healer, 1, 5), (trp_priest, 5, 5)]),
  ("order_lance_t3_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_france_swordsman_4, 7, 7), (trp_teutonic_horse_3, 5, 5)]),
  ("order_lance_t3_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_sissofbattle_c, 5, 5), (trp_france_archer_3, 10, 10)]),
  
  ("order_lance_t2_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_france_pikeman_3, 5, 5), (trp_france_pikeman_2, 15, 20)]),
  ("order_lance_t2_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_france_archer_3, 5, 5), (trp_france_crossbow_2, 15, 20)]),
  ("order_lance_t2_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_priest, 5, 5), (trp_clerics, 10, 10)]),
  ("order_lance_t2_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_teutonic_horse_1, 5, 5), (trp_teutonic_spearman, 15, 20)]),
  ("order_lance_t2_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_teutonic_sword, 5, 5), (trp_teutonic_spearman, 15, 20)]),
  
  ("order_lance_t1_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_france_pikeman_1, 5, 5), (trp_france_militia, 15, 20)]),
  ("order_lance_t1_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_teutonic_spearman, 10, 10), (trp_teutonic_pilgrim, 15, 15)]),
  ("order_lance_t1_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_clerics, 5, 5), (trp_monk, 10, 10)]),
  ("order_lance_t1_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_france_pikeman_1, 5, 5), (trp_france_militia, 15, 20)]),
  ("order_lance_t1_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_teutonic_spearman, 10, 10), (trp_teutonic_pilgrim, 15, 15)]),

  ("order_lance_end", "{!}Lance", 0, 0, fac_neutral, 0, []),


  ("khergit_lance_t4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_khergit_general, 1, 2),(trp_ogre_war, 2, 5),(trp_cyclop, 0, 1),(trp_khergit_guard, 2, 4)]),

  ("khergit_lance_t3_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_khergit_heavy, 5, 5), (trp_khergit_lancer, 10, 10)]),
  ("khergit_lance_t3_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_khergit_elite_horse_archer, 5, 5), (trp_khergit_veteran_horse_archer, 10, 10)]),
  ("khergit_lance_t3_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_ogre_cannon, 1, 2), (trp_ogre_war, 10, 10)]),
  ("khergit_lance_t3_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_troll_1, 1, 5), (trp_khergit_heavy_archer, 10, 10)]),
  ("khergit_lance_t3_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_ogre_mega, 5, 5), (trp_ogre_war, 10, 10)]),
  
  ("khergit_lance_t2_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_khergit_lancer, 5, 5), (trp_khergit_horseman, 20, 20)]),
  ("khergit_lance_t2_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_khergit_heavy, 5, 5), (trp_khergit_lancer, 10, 10)]),
  ("khergit_lance_t2_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_khergit_veteran_horse_archer, 5, 5), (trp_khergit_horse_archer, 20, 20)]),
  ("khergit_lance_t2_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_ogre_war, 5, 5), (trp_ogre, 15, 15)]),
  ("khergit_lance_t2_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_ogre_war, 5, 5), (trp_ogre, 20, 20)]),

  ("khergit_lance_t1_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_ogre, 5, 5), (trp_ogre_young, 20, 20)]),
  ("khergit_lance_t1_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_khergit_horseman, 5, 5), (trp_khergit_skirmisher, 20, 20)]),
  ("khergit_lance_t1_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_khergit_horseman, 5, 5), (trp_khergit_skirmisher, 20, 20)]),
  ("khergit_lance_t1_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_khergit_guard, 5, 5), (trp_khergit_skirmisher, 20, 20)]),
  ("khergit_lance_t1_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_ogre, 5, 5), (trp_ogre_young, 20, 20)]),
  
  ("khergit_lance_end", "{!}Lance", 0, 0, fac_neutral, 0, []),
  
  
  ("orc_lance_t4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_orc_blackorc_boss, 1, 3),(trp_troll_1, 1, 1),(trp_ogre_war, 2, 2),(trp_demon_4_2, 1, 1),(trp_orc_boar_big, 1, 2)]),

  ("orc_lance_t3_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_orc_veterun_blackorc, 5, 5), (trp_orc_blackorc, 10, 10)]),
  ("orc_lance_t3_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_orc_boar_big, 5, 5), (trp_orc_veteran_boar, 10, 10)]),
  ("orc_lance_t3_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_demon_4_3, 1, 5), (trp_demon_4_2, 5, 5)]),
  ("orc_lance_t3_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_orc_blackorc_boss, 1, 3), (trp_orc_veterun_blackorc, 10, 10)]),
  ("orc_lance_t3_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_troll_2, 0, 1), (trp_orc_veterun_arrer, 10, 10)]),
  
  ("orc_lance_t2_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_orc_big, 5, 5), (trp_orc_warrior, 15, 20)]),
  ("orc_lance_t2_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_orc_veteran_boar, 5, 5), (trp_orc_boar_boy, 15, 20)]),
  ("orc_lance_t2_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_goblin_knight, 5, 5), (trp_goblin_horseman, 15, 20)]),
  ("orc_lance_t2_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_orc_veterun_blackorc, 5, 5), (trp_orc_blackorc, 10, 10)]),
  ("orc_lance_t2_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_orc_arrer_boy, 5, 5), (trp_arrer_youngun, 15, 15)]),

  ("orc_lance_t1_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_goblin_horseman, 5, 5), (trp_orc_boy, 20, 20)]),
  ("orc_lance_t1_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_goblin_infantry, 10, 10), (trp_goblin_footman, 20, 20)]),
  ("orc_lance_t1_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_goblin_crossbowman, 10, 10), (trp_goblin_skirmisher, 20, 20)]),
  ("orc_lance_t1_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_arrer_youngun, 5, 5), (trp_orc, 20, 20)]),

  ("orc_lance_end", "{!}Lance", 0, 0, fac_neutral, 0, []),
  
  ("england_lance_t4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_england_knight_2, 1, 2),(trp_woodelf_swordman, 1, 3),(trp_england_knight_4, 1, 2),(trp_england_knight_1, 2, 3),(trp_england_swordsman_3, 1, 2)]),
  
  ("england_lance_t3_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_england_swordsman_3, 1, 2), (trp_england_swordsman_2, 10, 10)]),
  ("england_lance_t3_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_england_swordsman_3, 1, 2), (trp_england_billmen_2, 10, 10)]),
  ("england_lance_t3_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_woodelf_stinger, 1, 2), (trp_woodelf_m_hunter, 10, 10)]),
  ("england_lance_t3_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_england_knight_2, 1, 2), (trp_england_horse_2, 10, 10)]),
  ("england_lance_t3_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_woodelf_swordman, 1, 2), (trp_woodelf_spearman, 10, 10)]),
    
  ("england_lance_t2_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_england_swordsman_2, 5, 5), (trp_england_swordsman_1, 20, 20)]),
  ("england_lance_t2_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_england_swordsman_2, 5, 5), (trp_england_billmen_1, 20, 20)]),
  ("england_lance_t2_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_england_longbowm_4, 5, 5), (trp_england_longbowm_3, 20, 20)]),
  ("england_lance_t2_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_england_longbowm_3, 5, 5), (trp_england_longbowm_2, 20, 20)]),
  ("england_lance_t2_6", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_woodelf_hunter, 5, 5), (trp_woodelf_scout, 10, 10)]),

  ("england_lance_t1_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_england_swordsman_1, 5, 5), (trp_england_militia, 25, 25)]),
  ("england_lance_t1_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_england_longbowm_2, 5, 5), (trp_england_longbowm_1, 25, 25)]),
  ("england_lance_t1_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_woodelf_scout, 5, 5), (trp_woodelf_recruit, 20, 20)]),
  ("england_lance_t1_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_england_horse_1, 5, 5), (trp_england_town_recruit, 25, 25)]),
  ("england_lance_t1_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_england_knight_1, 2, 4), (trp_woodelf_recruit, 25, 25)]),

  ("england_lance_end", "{!}Lance", 0, 0, fac_neutral, 0, []),

  ("woodelf_lance_t4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_england_knight_2, 1, 2),(trp_woodelf_cavalry, 1, 3),(trp_england_knight_3, 1, 2),(trp_england_horse_3, 2, 3),(trp_ent_2, 1, 2)]),
  
  ("woodelf_lance_t3_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_england_billmen_3, 5, 5), (trp_england_billmen_2, 10, 10)]),
  ("woodelf_lance_t3_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_woodelf_stinger, 1, 5), (trp_woodelf_m_hunter, 10, 10)]),
  ("woodelf_lance_t3_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_woodelf_druid_1, 1, 1), (trp_woodelf_m_hunter, 10, 10)]),
  ("woodelf_lance_t3_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_england_horse_3, 1, 5), (trp_england_horse_2, 10, 10)]),
  ("woodelf_lance_t3_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_ent_2, 1, 5), (trp_woodelf_swordman, 10, 10)]),
    
  ("woodelf_lance_t2_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_england_billmen_2, 5, 5), (trp_england_billmen_1, 20, 20)]),
  ("woodelf_lance_t2_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_woodelf_m_hunter, 5, 5), (trp_woodelf_hunter, 20, 20)]),
  ("woodelf_lance_t2_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_england_longbowm_3, 5, 5), (trp_england_longbowm_2, 20, 20)]),
  ("woodelf_lance_t2_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_woodelf_spearman, 5, 5), (trp_woodelf_watchman, 10, 10)]),
  ("woodelf_lance_t2_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_woodelf_hunter, 5, 5), (trp_woodelf_scout, 10, 10)]),

  ("woodelf_lance_t1_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_dryad, 5, 5), (trp_england_town_recruit, 25, 25)]),
  ("woodelf_lance_t1_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_england_longbowm_2, 5, 5), (trp_england_longbowm_1, 25, 25)]),
  ("woodelf_lance_t1_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_woodelf_watchman, 5, 5), (trp_woodelf_recruit, 20, 20)]),
  ("woodelf_lance_t1_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_woodelf_scout, 5, 5), (trp_woodelf_recruit, 20, 20)]),
  ("woodelf_lance_t1_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_england_horse_1, 5, 5), (trp_england_town_recruit, 25, 25)]),

  ("woodelf_lance_end", "{!}Lance", 0, 0, fac_neutral, 0, []),

  ("italian_lance_t4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_bone_dragon, 1, 2),(trp_undead_horse_2, 1, 2),(trp_italian_horse_4, 2, 4),(trp_wight, 1, 2)]),
  
  ("italian_lance_t3_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_italian_town_footman_3, 5, 5), (trp_italian_town_footman_2, 10, 10)]),
  ("italian_lance_t3_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_italian_crossbow_3, 5, 5), (trp_italian_crossbow_2, 10, 10)]),
  ("italian_lance_t3_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_undead_horse_2, 1, 5), (trp_undead_horse_1, 10, 10)]),
  ("italian_lance_t3_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_cannon_man, 1, 2), (trp_italian_town_footman_3, 10, 10)]),
  ("italian_lance_t3_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_ghost_dragon, 1, 2), (trp_wight, 10, 10)]),
  
  ("italian_lance_t2_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_italian_horse_4, 5, 5), (trp_italian_horse_2, 20, 20)]),
  ("italian_lance_t2_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_italian_crossbow_2, 5, 5), (trp_italian_town_footman_2, 20, 20)]),
  ("italian_lance_t2_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_se_pikeman_3, 5, 5), (trp_se_pikeman_2, 20, 20)]),
  ("italian_lance_t2_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_italian_town_footman_2, 5, 5), (trp_italian_town_footman_1, 20, 20)]),
  ("italian_lance_t2_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_italian_crossbow_2, 5, 5), (trp_italian_crossbow_1, 20, 20)]),

  ("italian_lance_t1_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_se_pikeman_2, 5, 5), (trp_se_pikeman_1, 20, 20)]),
  ("italian_lance_t1_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_italian_crossbow_1, 5, 5), (trp_italian_town_recruit, 25, 25)]),
  ("italian_lance_t1_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_italian_horse_3, 5, 5), (trp_italian_horse_1, 25, 25)]),
  ("italian_lance_t1_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_italian_town_footman_1, 5, 5), (trp_italian_town_militia, 15, 15)]),
  ("italian_lance_t1_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_italian_crossbow_2, 5, 5), (trp_italian_crossbow_1, 15, 15)]),

  ("italian_lance_end", "{!}Lance", 0, 0, fac_neutral, 0, []),

  ("undead_lance_t4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_vampire_4, 1, 1),(trp_undead_horse_3, 0, 1),(trp_undead_horse_1, 2, 4),(trp_undead_horse_2, 2, 3)]),
  
  ("undead_lance_t3_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_vampire_3, 1, 5), (trp_vampire_2, 10, 10)]),
  ("undead_lance_t3_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_skeleton_lord, 10, 10), (trp_undead_horse_2, 5, 5)]),
  ("undead_lance_t3_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_lich_1, 5, 5), (trp_se_musketeer_2, 20, 20)]),
  ("undead_lance_t3_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_skeleton_spearman, 5, 5), (trp_se_pikeman_3, 20, 20)]),
  ("undead_lance_t3_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_vampire_2, 5, 5), (trp_se_pikeman_3, 20, 20)]),
  ("undead_lance_t3_6", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_bone_dragon, 3, 5), (trp_undead_horse_2, 10, 10)]),

  ("undead_lance_t2_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_se_musketeer_2, 5, 5), (trp_se_musketeer_1, 20, 20)]),
  ("undead_lance_t2_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_vampire_2, 1, 5), (trp_vampire_1, 10, 10)]),
  ("undead_lance_t2_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_undead_magic_2, 1, 5), (trp_vampire_assassin, 10, 10)]),
  ("undead_lance_t2_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_se_pikeman_3, 5, 5), (trp_se_pikeman_2, 20, 20)]),
  ("undead_lance_t2_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_se_billman_2, 5, 5), (trp_se_billman_1, 20, 20)]),

  ("undead_lance_t1_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_se_billman_1, 5, 5), (trp_se_pikeman_1, 20, 20)]),
  ("undead_lance_t1_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_italian_crossbow_1, 5, 5), (trp_zombie_2, 15, 15)]),
  ("undead_lance_t1_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_wight, 5, 5), (trp_ghost, 10, 10)]),
  ("undead_lance_t1_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_se_musketeer_1, 5, 5), (trp_se_skirmisher, 20, 20)]),
  ("undead_lance_t1_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_se_pikeman_2, 5, 5), (trp_se_pikeman_1, 20, 20)]),

  ("undead_lance_end", "{!}Lance", 0, 0, fac_neutral, 0, []),


  ("german_lance_t4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_german_knight_4, 1, 2),(trp_iberian_town_footman_3, 1, 3),(trp_german_knight_3, 1, 2),(trp_german_knight_1, 1, 3),(trp_german_reitern_2, 1, 2)]),
  
  ("german_lance_t3_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_german_twohander_3, 5, 5), (trp_german_twohander_2, 10, 10)]),
  ("german_lance_t3_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_german_crossbow_4, 5, 5), (trp_german_crossbow_3, 10, 10)]),
  ("german_lance_t3_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_gargoyle, 1, 5), (trp_human_magic_3, 3, 5)]),
  ("german_lance_t3_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_iberian_knight_3, 1, 5), (trp_iberian_town_footman_2, 10, 10)]),
  ("german_lance_t3_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_german_reitern_2, 1, 5), (trp_german_reitern_1, 10, 10)]),
  ("german_lance_t3_6", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_iberian_town_footman_3, 5, 5), (trp_german_pikeman_3, 10, 10)]),
  
  ("german_lance_t2_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_german_twohander_2, 5, 5), (trp_german_twohander_1, 20, 20)]),
  ("german_lance_t2_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_german_crossbow_3, 5, 5), (trp_german_crossbow_2, 20, 20)]),
  ("german_lance_t2_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_german_pikeman_3, 5, 5), (trp_german_pikeman_2, 10, 10)]),
  ("german_lance_t2_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_german_reitern_1, 5, 5), (trp_iberian_dragoon_1, 10, 10)]),
  ("german_lance_t2_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_iberian_town_footman_2, 5, 5), (trp_iberian_town_footman_1, 10, 10)]),
  ("german_lance_t2_6", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_human_magic_2, 5, 5), (trp_german_militia, 10, 10)]),

  ("german_lance_t1_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_german_crossbow_2, 5, 5), (trp_german_crossbow_1, 15, 15)]),
  ("german_lance_t1_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_german_militia, 5, 5), (trp_german_town_recruit, 25, 25)]),
  ("german_lance_t1_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_german_pikeman_2, 5, 5), (trp_german_pikeman_1, 15, 15)]),
  ("german_lance_t1_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_iberian_town_footman_1, 5, 5), (trp_iberian_town_militia, 15, 15)]),
  ("german_lance_t1_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_iberian_dragoon_1, 5, 5), (trp_german_town_recruit, 25, 25)]),
  ("german_lance_t1_6", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_german_knight_1, 2, 4), (trp_iberian_town_militia, 15, 15)]),

  ("german_lance_end", "{!}Lance", 0, 0, fac_neutral, 0, []),

  ("hungary_lance_t4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_polish_knight_2, 1, 2),(trp_polish_knight_3, 1, 3),(trp_balkan_billman_4, 1, 1),(trp_polish_knight_1, 2, 4),(trp_rus_dvor_cavalry_2, 1, 2)]),
  ("hungary_lance_t3_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_polish_crossbow_3_2, 1, 5), (trp_polish_crossbow_3_1, 10, 10)]),
  ("hungary_lance_t3_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_werewolf_huge, 1, 3), (trp_balkan_billman_3, 10, 10)]),
  ("hungary_lance_t3_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_balkan_billman_3, 5, 5), (trp_polish_pikeman_2, 10, 10)]),
  ("hungary_lance_t3_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_polish_knight_2, 1, 5), (trp_polish_horse_4, 10, 10)]),
  ("hungary_lance_t3_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_polish_which_2, 1, 5), (trp_polish_horse_4, 10, 10)]),
  ("hungary_lance_t3_6", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_polish_which_2, 1, 5),(trp_polish_which_1, 5, 10)]),
  
  ("hungary_lance_t2_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_polish_crossbow_3_1, 5, 5), (trp_polish_crossbow_2, 20, 20)]),
  ("hungary_lance_t2_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_polish_horse_4, 1, 5), (trp_polish_horse_3, 15, 15)]),
  ("hungary_lance_t2_2_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_rus_cossack_3, 5, 5), (trp_rus_cossack_2, 20, 20)]),
  ("hungary_lance_t2_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_balkan_billman_3, 5, 5), (trp_balkan_billman_2, 15, 15)]),
  ("hungary_lance_t2_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_polish_pikeman_2, 5, 5), (trp_polish_pikeman_1, 20, 20)]),
  ("hungary_lance_t2_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_balkan_archer_3, 5, 5), (trp_balkan_archer_2, 15, 15)]),

  ("hungary_lance_t1_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_polish_horse_2, 5, 5), (trp_polish_horse_1, 15, 15)]),
  ("hungary_lance_t1_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_polish_crossbow_1, 5, 5), (trp_polish_town_recruit, 25, 25)]),
  ("hungary_lance_t1_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_balkan_billman_2, 5, 5), (trp_balkan_footman_1, 20, 20)]),
  ("hungary_lance_t1_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_rus_cossack_1, 5, 5), (trp_balkan_vil_recruit, 25, 25)]),
  ("hungary_lance_t1_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_polish_knight_1, 5, 5), (trp_rus_cossack_1, 25, 25)]),

  ("hungary_lance_end", "{!}Lance", 0, 0, fac_neutral, 0, []),


  ("drowelf_lance_t4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_rus_boyar_2, 1, 2),(trp_minotaur_3, 1, 3),(trp_drowelf_which_1, 1, 1),(trp_rat_5_3, 2, 2),(trp_drowelf_raider_2, 1, 2)]),
  ("drowelf_lance_t3_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_drowelf_raider_2, 2, 5), (trp_drowelf_raider_1,10, 10)]),
  ("drowelf_lance_t3_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_drowelf_assassin_3, 2, 5), (trp_drowelf_assassin_3, 10, 10)]),
  ("drowelf_lance_t3_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_drowelf_infantry_2, 5, 5), (trp_drowelf_infantry_1, 10, 10)]),
  ("drowelf_lance_t3_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_minotaur_3, 2, 5), (trp_minotaur_3, 10, 10)]),
  ("drowelf_lance_t3_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_medusa_2, 5, 5), (trp_medusa_2, 10, 10)]),
  
  ("drowelf_lance_t2_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_drowelf_raider_1, 5, 5), (trp_drowelf_footman, 10, 10)]),
  ("drowelf_lance_t2_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_drowelf_assassin_3, 10, 10), (trp_drowelf_assassin_1, 15, 15)]),
  ("drowelf_lance_t2_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_minotaur_2, 5, 5), (trp_minotaur_2, 15, 15)]),
  ("drowelf_lance_t2_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_drowelf_infantry_1, 5, 5), (trp_minotaur_1, 15, 15)]),
  ("drowelf_lance_t2_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_medusa_1, 5, 5), (trp_medusa_1, 15, 15)]),

  ("drowelf_lance_t1_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_rat_2, 5, 5), (trp_rat_1, 25, 25)]),
  ("drowelf_lance_t1_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_undead_magic_1, 5, 5), (trp_rat_2, 20, 20)]),
  ("drowelf_lance_t1_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_minotaur_1, 5, 5), (trp_minotaur_1, 15, 15)]),
  ("drowelf_lance_t1_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_drowelf_footman, 1, 5), (trp_drowelf_recruit, 15, 15)]),
  ("drowelf_lance_t1_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_rat_3, 5, 5), (trp_rat_2, 20, 20)]),

  ("drowelf_lance_end", "{!}Lance", 0, 0, fac_neutral, 0, []),


  ("turk_lance_t4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_turk_roy_sipahi, 1, 2),(trp_mamluke_horseman_2, 1, 3),(trp_demon_human_5_1, 0, 1),(trp_turk_sipahi, 2, 4),(trp_sarranid_assasin, 1, 2)]),
  
  ("turk_lance_t3_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_janissary_infantry_2, 1, 2), (trp_janissary_infantry_2, 5, 10)]),
  ("turk_lance_t3_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_janissary_musketeer_2, 1, 2), (trp_janissary_musketeer_2, 5, 10)]),
  ("turk_lance_t3_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_mamluke_horseman_3, 1, 2), (trp_mamluke_horseman_2, 10, 10)]),
  ("turk_lance_t3_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_chaos_warrior_2, 1, 2), (trp_chaos_warrior_2, 5, 10)]),
  ("turk_lance_t3_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_demon_human_5_1, 1, 2), (trp_turk_cav_3, 10, 10)]),
  ("turk_lance_t3_6", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_janissary_musketeer_2, 1, 2), (trp_janissary_musketeer_1, 10, 10)]),
    
  ("turk_lance_t2_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_janissary_infantry_1, 5, 5), (trp_turk_footman, 20, 20)]),
  ("turk_lance_t2_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_janissary_musketeer_2, 5, 5), (trp_janissary_musketeer_1, 10, 15)]),
  ("turk_lance_t2_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_chaos_warrior_1, 5, 5), (trp_me_mercenary_swordsman_2, 20, 20)]),
  ("turk_lance_t2_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_turk_archer_2, 5, 5), (trp_turk_archer_1, 20, 20)]),
  ("turk_lance_t2_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_turk_cav_3, 5, 5), (trp_turk_cav_2, 20, 20)]),
  ("turk_lance_t2_5_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_mamluke_horseman_2, 5, 5), (trp_mamluke_horseman, 20, 20)]),

  ("turk_lance_t1_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_turk_azap, 5, 5), (trp_turk_village_rabble, 25, 25)]),
  ("turk_lance_t1_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_turk_cav_2, 5, 5), (trp_turk_cav_1, 25, 25)]),
  ("turk_lance_t1_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_turk_archer_2, 5, 5), (trp_mamluke_recruit, 25, 25)]),
  ("turk_lance_t1_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_chaos_warrior_1, 5, 5), (trp_mamluke_recruit, 25, 25)]),
  ("turk_lance_t1_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_janissary_infantry_1, 5, 5), (trp_janissary_retainer, 25, 25)]),

  ("turk_lance_end", "{!}Lance", 0, 0, fac_neutral, 0, []),

  ("nord_lance_t4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_nord_knight_3, 1, 1),(trp_nord_valkyrie_2, 1, 2),(trp_god_choosen_berserker, 1, 3),(trp_nord_halberd_2, 2, 4),(trp_nord_knight_2, 1, 2)]),
  
  ("nord_lance_t3_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_nord_halberd_2, 1, 5), (trp_nord_halberd_1, 10, 10)]),
  ("nord_lance_t3_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_nord_axeman_2, 1, 5), (trp_nord_axeman_1, 10, 10)]),
  ("nord_lance_t3_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_dwarf_guard_1, 5, 5), (trp_dwarf_ironbreaker, 10, 10)]),
  ("nord_lance_t3_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_fire_dragon, 0, 1), (trp_mercenary_berserker, 10, 10)]),
  ("nord_lance_t3_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_nord_gunner, 1, 5), (trp_nord_crossbow_2, 10, 10)]),
  ("nord_lance_t3_6", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_nord_valkyrie_3, 1, 2), (trp_nord_valkyrie_2, 10, 10)]),
  
  ("nord_lance_t2_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_nord_halberd_1, 5, 5), (trp_nord_swordsmen, 20, 20)]),
  ("nord_lance_t2_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_nord_axeman_1, 5, 5), (trp_nord_swordsmen, 20, 20)]),
  ("nord_lance_t2_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_nord_knight_1, 5, 5), (trp_nord_warrior, 20, 20)]),
  ("nord_lance_t2_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_nord_crossbow_2, 5, 5), (trp_nord_crossbow_1, 20, 20)]),
  ("nord_lance_t2_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_nord_veteran, 5, 5), (trp_nord_warrior, 20, 20)]),
  ("nord_lance_t2_6", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_nord_valkyrie_1, 5, 5), (trp_nord_mounted_scout, 20, 20)]),

  ("nord_lance_t1_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_nord_swordsmen, 5, 5), (trp_nord_town_militia, 25, 25)]),
  ("nord_lance_t1_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_nord_crossbow_1, 5, 5), (trp_nord_skirmisher, 20, 20)]),
  ("nord_lance_t1_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_giant_1, 5, 5), (trp_nord_town_militia, 20, 20)]),
  ("nord_lance_t1_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_nord_warrior, 5, 5), (trp_nord_recruit, 25, 25)]),
  ("nord_lance_t1_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_nord_warrior, 5, 5), (trp_nord_footman, 25, 25)]),

  ("nord_lance_end", "{!}Lance", 0, 0, fac_neutral, 0, []),
  
    ("faction_2_lance_t4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_ghost_dragon, 1, 1),(trp_death, 0, 1),(trp_lich_1, 2, 4),(trp_undead_horse_2, 2, 3)]),
  
  ("faction_2_lance_t3_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_vampire_3, 1, 5), (trp_vampire_2, 10, 10)]),
  ("faction_2_lance_t3_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_skeleton_lord, 10, 10), (trp_undead_horse_2, 5, 5)]),
  ("faction_2_lance_t3_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_skeleton_archer, 10, 10), (trp_undead_magic_2, 5, 5),(trp_lich_1, 1, 1),]),
  ("faction_2_lance_t3_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_skeleton_lord, 5, 5), (trp_skeleton_spearman, 20, 20)]),
  ("faction_2_lance_t3_6", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_bone_dragon, 2, 5), (trp_undead_horse_2, 10, 10)]),

  ("faction_2_lance_t2_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_se_musketeer_2, 5, 5), (trp_se_musketeer_1, 20, 20)]),
  ("faction_2_lance_t2_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_skeleton_warrior, 5, 5), (trp_undead_horse_1, 5, 10)]),
  ("faction_2_lance_t2_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_undead_magic_2, 1, 5), (trp_skeleton_halberd, 10, 10)]),
  ("faction_2_lance_t2_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_wight, 5, 5), (trp_wight, 20, 20)]),


  ("faction_2_lance_t1_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_skeleton_warrior, 5, 5), (trp_se_billman_1, 20, 20)]),
  ("faction_2_lance_t1_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_dullahan, 5, 5), (trp_zombie_2, 15, 15)]),
  ("faction_2_lance_t1_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_wight, 5, 5), (trp_ghost, 10, 10)]),
  ("faction_2_lance_t1_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_skeleton_archer, 5, 5), (trp_se_musketeer_1, 20, 20)]),
  ("faction_2_lance_t1_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_se_skirmisher, 15, 15), (trp_se_pikeman_1, 15, 15)]),

  ("faction_2_lance_end", "{!}Lance", 0, 0, fac_neutral, 0, []),


  ("faction_6_lance_t4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_orc_blackorc_boss, 1, 3),(trp_troll_2, 0, 1),(trp_ogre_war2, 0, 2),(trp_demon_4_2, 1, 1),(trp_ogre_mega, 1, 2)]),

  ("faction_6_lance_t3_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_orc_blackorc_boss, 5, 5), (trp_ogre_war, 5, 10)]),
  ("faction_6_lance_t3_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_orc_boar_big, 5, 5), (trp_orc_veteran_boar, 10, 10)]),
  ("faction_6_lance_t3_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_troll_3, 1, 5), (trp_demon_1, 5, 5)]),
  ("faction_6_lance_t3_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_orc_blackorc_boss, 1, 3), (trp_orc_veterun_blackorc, 10, 10)]),
  ("faction_6_lance_t3_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_ogre_cannon, 1, 1), (trp_ogre_war, 5, 10)]),
  
  ("faction_6_lance_t2_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_orc_big, 5, 5), (trp_orc_warrior, 15, 20)]),
  ("faction_6_lance_t2_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_orc_veteran_boar, 5, 5), (trp_orc_boar_boy, 15, 20)]),
  ("faction_6_lance_t2_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_ogre, 5, 5), (trp_ogre_young, 15, 20)]),
  ("faction_6_lance_t2_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_orc_veterun_blackorc, 5, 5), (trp_orc_blackorc, 10, 10)]),
  ("faction_6_lance_t2_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_orc_arrer_boy, 5, 5), (trp_arrer_youngun, 15, 15)]),

  ("faction_6_lance_t1_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_goblin_knight, 5, 10), (trp_goblin_horseman, 20, 20)]),
  ("faction_6_lance_t1_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_goblin_guard, 5, 10), (trp_goblin_infantry, 20, 20)]),
  ("faction_6_lance_t1_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_goblin_crossbowman, 15, 15), (trp_goblin_skirmisher, 15, 15)]),
  ("faction_6_lance_t1_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_goblin_footman, 15, 15), (trp_goblin_skirmisher, 15, 15)]),

  ("faction_6_lance_end", "{!}Lance", 0, 0, fac_neutral, 0, []),


  ("faction_11_lance_t4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_we_knight_3, 1, 2),(trp_musket_ranger, 1, 3),(trp_we_knight_1, 1, 2),(trp_mercenary_cavalry, 1, 3),(trp_cannon_man, 1, 1)]),
  
  ("faction_11_lance_t3_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_mercenary_elite_axeman, 5, 5), (trp_mercenary_axeman, 10, 10)]),
  ("faction_11_lance_t3_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_musket_line_infantry_2, 5, 5), (trp_musket_line_infantry, 10, 10)]),
  ("faction_11_lance_t3_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_assassin, 5, 10), (trp_human_magic_2, 5, 5)]),
  ("faction_11_lance_t3_6", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_musket_ranger, 5, 5), (trp_swiss_pikeman_2, 10, 10)]),
  
  ("faction_11_lance_t2_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_swiss_halberd_2, 5, 5), (trp_swiss_halberd, 20, 20)]),
  ("faction_11_lance_t2_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_musket_line_infantry, 5, 5), (trp_musket_man, 20, 20)]),
  ("faction_11_lance_t2_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_swiss_pikeman_2, 5, 5), (trp_swiss_pikeman, 10, 10)]),
  ("faction_11_lance_t2_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_hired_blade, 5, 5), (trp_mercenary_swordsman, 10, 10)]),

  ("faction_11_lance_t1_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_musket_man, 5, 5), (trp_musket_hunter, 15, 15)]),
  ("faction_11_lance_t1_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_caravan_guard, 15, 15), (trp_watchman, 15, 15)]),
  ("faction_11_lance_t1_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_swiss_pikeman, 5, 5), (trp_swiss_swordman, 15, 15)]),
  ("faction_11_lance_t1_6", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_we_knight_2, 2, 4), (trp_we_noble_lad, 15, 15)]),
  ("faction_11_lance_end", "{!}Lance", 0, 0, fac_neutral, 0, []),

  ("faction_12_lance_t4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_lich_3, 1, 1),(trp_lich_dragon, 0, 1),(trp_god_choosen_berserker, 1, 3),(trp_lizard_dragon, 2, 4),(trp_scottish_swordman, 1, 2)]),
  
  ("faction_12_lance_t3_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_draugr_lord, 5, 5), (trp_draugr_3, 15, 15)]),
  ("faction_12_lance_t3_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_god_choosen_berserker, 5, 5), (trp_mercenary_berserker, 10, 10)]),
  ("faction_12_lance_t3_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_lizard_dragon, 1, 2), (trp_scottish_guard, 1, 2)]),

  ("faction_12_lance_t3_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_draugr_lord, 1, 5), (trp_scottish_pikeman_3, 10, 10)]),

  
  ("faction_12_lance_t2_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_nord_champion, 1, 5), (trp_nord_veteran, 10, 20)]),
  ("faction_12_lance_t2_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_lizard_axeman_2, 5, 10), (trp_lizard_axeman_1, 10, 20)]),

  ("faction_12_lance_t2_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_draugr_3, 5, 5), (trp_draugr_2, 20, 20)]),
  ("faction_12_lance_t2_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_nord_veteran, 5, 5), (trp_nord_warrior, 20, 20)]),
  ("faction_12_lance_t2_6", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_lizard_rider_2, 10, 10), (trp_scottish_pikeman_2, 15, 15)]),

  ("faction_12_lance_t1_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_draugr_2, 5, 5), (trp_draugr_1, 25, 25)]),
  ("faction_12_lance_t1_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_nord_warrior, 5, 5), (trp_nord_footman, 20, 20)]),

  ("faction_12_lance_t1_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_lizard_rider_1, 5, 5), (trp_scottish_axeman, 20, 20)]),
  ("faction_12_lance_t1_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_firefly, 5, 10), (trp_scottish_pikeman, 10, 10)]),

  ("faction_12_lance_end", "{!}Lance", 0, 0, fac_neutral, 0, []),



  ("faction_13_lance_t4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_we_knight_2, 1, 2),(trp_green_dragon, 0, 1),(trp_we_knight_3, 2, 3),(trp_we_knight_1, 2, 3),(trp_ent_2, 1, 2)]),
  
  ("faction_13_lance_t3_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_woodelf_sharpshooter, 1, 2), (trp_woodelf_stinger, 5, 5)]),
  ("faction_13_lance_t3_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_woodelf_sworddancer, 1, 2), (trp_woodelf_swordman, 5, 5)]),
  ("faction_13_lance_t3_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_woodelf_stinger, 1, 2), (trp_woodelf_m_hunter, 10, 10)]),
  ("faction_13_lance_t3_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_we_knight_3, 5, 5), (trp_we_knight_2, 10, 10)]),
  ("faction_13_lance_t3_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_woodelf_swordman, 1, 2), (trp_woodelf_spearman, 10, 10)]),
    
  ("faction_13_lance_t2_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_welsh_longbowm_2, 5, 5), (trp_welsh_spearman_1, 20, 20)]),
  ("faction_13_lance_t2_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_dis_knight_2, 10, 10), (trp_dis_knight_1, 15, 15)]),
  ("faction_13_lance_t2_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_woodelf_stinger, 5, 5), (trp_welsh_longbowm_3, 20, 20)]),
  ("faction_13_lance_t2_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_welsh_longbowm_3, 5, 5), (trp_welsh_longbowm_2, 20, 20)]),
  ("faction_13_lance_t2_6", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_woodelf_hunter, 5, 5), (trp_woodelf_scout, 10, 10)]),

  ("faction_13_lance_t1_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_welsh_spearman_1, 5, 5), (trp_dryad, 15, 15)]),
  ("faction_13_lance_t1_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_welsh_longbowm_2, 5, 5), (trp_welsh_longbowm_1, 25, 25)]),
  ("faction_13_lance_t1_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_woodelf_scout, 5, 5), (trp_woodelf_recruit, 20, 20)]),
  ("faction_13_lance_t1_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_dryad, 5, 10), (trp_woodelf_scout, 10, 15)]),
  ("faction_13_lance_t1_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_we_knight_1, 5, 5), (trp_forest_bandit, 25, 25)]),
  ("faction_13_lance_end", "{!}Lance", 0, 0, fac_neutral, 0, []),


  ("faction_14_lance_t4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_red_dragon, 1, 1),(trp_minotaur_3, 2, 3),(trp_drowelf_which_1, 1, 1),(trp_rat_5_3, 2, 2),(trp_drowelf_raider_2, 1, 2)]),
  ("faction_14_lance_t3_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_drowelf_raider_2, 2, 5), (trp_drowelf_raider_1,10, 10)]),
  ("faction_14_lance_t3_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_drowelf_assassin_3, 2, 5), (trp_drowelf_assassin_3, 10, 10)]),
  ("faction_14_lance_t3_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_drowelf_infantry_2, 5, 5), (trp_drowelf_infantry_1, 10, 10)]),
  ("faction_14_lance_t3_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_minotaur_3, 2, 5), (trp_minotaur_3, 10, 10)]),
  ("faction_14_lance_t3_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_drowelf_which_1, 5, 5), (trp_medusa_2, 10, 10)]),
  
  
  
  ("faction_14_lance_t2_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_drowelf_raider_1, 5, 5), (trp_drowelf_footman, 10, 10)]),
  ("faction_14_lance_t2_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_rat_5_2, 10, 10), (trp_rat_5_3, 15, 15)]),
  ("faction_14_lance_t2_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_rat_5_1, 5, 5), (trp_minotaur_2, 15, 15)]),
  ("faction_14_lance_t2_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_drowelf_infantry_1, 5, 5), (trp_minotaur_1, 15, 15)]),
  ("faction_14_lance_t2_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_medusa_2, 5, 5), (trp_medusa_1, 15, 15)]),




  ("faction_14_lance_t1_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_minotaur_2, 5, 5), (trp_rat_1, 25, 25)]),
  ("faction_14_lance_t1_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_undead_magic_1, 5, 5), (trp_rat_2, 20, 20)]),
  ("faction_14_lance_t1_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_rat_1, 15, 15), (trp_minotaur_1, 5, 5)]),
  ("faction_14_lance_t1_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_drowelf_footman, 1, 5), (trp_drowelf_recruit, 15, 15)]),
  ("faction_14_lance_t1_5", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_rat_3, 15, 15), (trp_rat_2, 15, 15)]),

  ("faction_14_lance_end", "{!}Lance", 0, 0, fac_neutral, 0, []),

  
  ("scottish_merc", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_scottish_guard, 4, 7),(trp_scottish_axeman, 12, 15),(trp_dragonfly, 20, 30)]),
  ("scottish_merc_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_scottish_swordman, 3, 7),(trp_scottish_pikeman_2, 5, 7),(trp_scottish_pikeman, 12, 15),(trp_scottish_axeman, 6, 10)]),
  ("scottish_merc_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_scottish_guard, 1, 3),(trp_scottish_pikeman_2, 10, 15),(trp_scottish_pikeman, 12, 15)]),
  

  ("swiss_merc", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_swiss_halberd_2, 4, 7),(trp_swiss_pikeman, 12, 15),(trp_musket_hunter, 6, 10)]),
  ("swiss_merc_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_swiss_halberd_2, 4, 7),(trp_musket_man, 6, 10),(trp_swiss_halberd, 12, 15)]),
  ("swiss_merc_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_swiss_halberd_2, 3, 7),(trp_swiss_pikeman_2, 5, 7),(trp_swiss_pikeman, 12, 15),(trp_swiss_halberd, 6, 10)]),
  
  
  ("welsh_merc", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_welsh_longbowm_3, 1, 3),(trp_welsh_longbowm_2, 12, 15),(trp_welsh_spearman_1, 10, 15)]),

  ("cossack_merc", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_rus_cossack, 12, 18),(trp_rus_cossack_2, 10, 18)]),
  ("cossack_merc_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_rus_cossack_3, 1, 5),(trp_rus_cossack_2, 25, 32)]),

  ("cannon_merc", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_cannon_man, 5, 5)]),
  ("cannon_merc_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_cannon_man, 1, 5),(trp_musket_ranger, 3, 15)]),


  ("viking_merc_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_mercenary_elite_axeman, 3, 7), (trp_nord_raider, 5, 7), (trp_nord_veteran, 18, 25)]),
  ("viking_merc_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_werewolf_berserker, 3, 7), (trp_god_choosen_berserker, 5, 7), (trp_mercenary_berserker, 18, 25)]),
  ("viking_merc_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_dwarf_guard_3, 3, 7), (trp_nord_crossbow_2, 6, 10), (trp_nord_axeman_1, 5, 7), (trp_nord_swordsmen, 12, 15)]),
  ("viking_merc_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_lich_3, 0, 1),(trp_draugr_lord, 5, 7), (trp_draugr_2, 12, 20)]),

  ("german_merc_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_german_twohander_3, 4, 7), (trp_german_pikeman_1, 12, 15), (trp_german_crossbow_2, 6, 10)]),
  ("german_merc_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_german_reitern_2, 1, 5), (trp_german_reitern_1, 5, 5), (trp_iberian_dragoon_1, 15, 15)]),
  ("german_merc_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_iberian_knight_3, 3, 7), (trp_german_twohander_1, 5, 7), (trp_german_pikeman_1, 12, 15), (trp_german_crossbow_2, 6, 10)]),
  
  ("naffatun_merc", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_naffatun, 15, 20), (trp_me_hand_gunner, 5, 10)]),
  ("assasin_merc", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_sarranid_assasin, 20, 20)]),


  ("saracen_merc_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_me_mercenary_swordsman_3, 1, 5), (trp_me_mercenary_swordsman_1, 25, 32)]),
  ("saracen_merc_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_saracen_cav_2, 5, 5), (trp_saracen_cav_1, 13, 27)]),
  ("saracen_merc_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_me_mercenary_swordsman_3, 1, 5),(trp_saracen_cav_2, 10, 18),(trp_me_mercenary_swordsman_2, 12, 15)]),
  
  ("saracen_merc_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_turk_sipahi, 1, 5), (trp_turk_cav_2, 13, 27)]),
  
  ("bedouin_merc", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_marinid_camel_2, 10, 18),(trp_bedouin_camel_gunnner, 12, 18)]),
  
  ("balkan_cav_merc", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_mercenary_balkan_cav, 25, 32)]),
  ("balkan_merc", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_polish_knight_1, 1, 5),(trp_balkan_cav_3, 1, 5),(trp_balkan_archer_2, 12, 15),(trp_balkan_archer_3, 4, 7),(trp_balkan_billman_2, 6, 10),(trp_balkan_billman_3, 1, 5)]),

  #("spain_merc_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_iberian_town_footman_2, 4, 7), (trp_iberian_town_pikeman_2, 12, 15), (trp_iberian_musketeer_1, 6, 10)]),
  #("spain_merc_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_iberian_knight_2, 2, 5), (trp_iberian_town_footman_2, 4, 6), (trp_iberian_town_pikeman_2, 10, 13), (trp_iberian_musketeer_2, 5, 8), (trp_iberian_town_footman_1, 7, 12)]),
  #("spain_merc_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_iberian_dragoon_1, 3, 7), (trp_iberian_town_footman_1, 5, 7), (trp_iberian_town_pikeman_2, 12, 15), (trp_iberian_musketeer_2, 6, 10)]),
  
  ("longbowmen_merc", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_sherwood_archer, 5, 5), (trp_welsh_longbowm_2, 15, 20), (trp_champion_swordsman, 1, 1)]),

  ("war_clerics_merc", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_teutonic_dis_knight, 3, 5), (trp_teutonic_sword, 6, 10)]),
  ("ghazis_merc", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_ghazis_2, 15, 15), (trp_ghazis_1, 30, 30)]),
  
  ("france_merc", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_france_knight_3, 3, 7), (trp_france_swordsman_2, 5, 7), (trp_france_pikeman_1, 12, 15), (trp_france_crossbow_2, 6, 10)]),
  ("england_merc", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_england_horse_2, 3, 7), (trp_england_swordsman_2, 5, 7), (trp_england_longbowm_2, 12, 15), (trp_england_billmen_1, 6, 10)]),
    
  ("polish_merc", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_polish_knight_4, 0, 1), (trp_polish_horse_4, 2, 5), (trp_polish_pikeman_2, 4, 7), (trp_polish_pikeman_1, 12, 15), (trp_polish_crossbow_3_2, 2, 5), (trp_polish_crossbow_2, 6, 10)]),
  ("teutoni_merc", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_angle, 1, 3), (trp_teutonic_horse_3, 2, 3), (trp_teutonic_dis_halbbruder, 4, 7)]),
  ("teutoni_merc_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_teutonic_horse_2, 3, 7), (trp_teutonic_dis_knight, 5, 7), (trp_teutonic_spearman, 12, 15), (trp_teutonic_sword, 6, 10)]),

  
  ("italian_merc_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_italian_horse_4, 1, 3), (trp_italian_horse_3, 2, 3), (trp_italian_horse_2, 5, 8)]),
  ("italian_merc_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_italian_horse_3, 3, 7), (trp_italian_town_footman_1, 5, 7), (trp_se_pikeman_2, 12, 15), (trp_italian_crossbow_1, 6, 10)]),
  
  ("rus_merc_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_black_khergit_lancer, 1, 3), (trp_steppe_horseman_2, 2, 6), (trp_steppe_horse_archer_2, 3, 7), (trp_steppe_horse_archer_1, 6, 10), (trp_black_khergit_horseman, 4, 7), (trp_steppe_tribesman, 12, 15)]),
  ("rus_merc_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_black_khergit_raidmaster, 1, 3), (trp_black_khergit_lancer, 2, 3), (trp_black_khergit_guard, 5, 8)]),
  ("rus_merc_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_black_khergit_raidmaster, 1, 1), (trp_steppe_horseman_2, 2, 5), (trp_black_khergit_horseman, 8, 13), (trp_steppe_tribesman, 10, 14)]),


  ("rus_merc_4", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_rus_palace_guard, 3, 7),(trp_rus_dvor_cavalry_2,6,10), (trp_rus_boyar_2,5,7),(trp_rus_cossack_3,12,15),]),
    
  ("ghazis_merc_fan", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_demon_magic_2, 5, 5),(trp_demon_human_3, 5, 5), (trp_demon_human_2, 20, 20)]),
  ("scottish_merc_fan", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_scottish_swordman, 3, 5),(trp_scottish_guard, 2, 5),(trp_scottish_pikeman_2, 10, 20)]),
  ("cannon_merc_fan", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_cannon_man, 5, 15)]),
  ("assasin_merc_fan", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_sarranid_assasin_2, 5, 5), (trp_sarranid_assasin, 20, 20)]),
  ("swiss_merc_fan", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_swiss_pikeman_2, 14, 19),(trp_swiss_halberd_2, 8, 15)]),
  ("rus_merc_2_fan", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_black_khergit_raidmaster, 2, 6), (trp_black_khergit_lancer, 5, 12), (trp_black_khergit_guard, 3, 8)]),

  ("hospitalier_knight_merc_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_grey_knight_terminator, 1, 3), (trp_teutonic_dis_knight, 10, 15), (trp_hospitaller_knight, 3, 5)]),
  ("hospitalier_knight_merc_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_grey_knight_inquisitor, 1, 3), (trp_hospitaller_knight_2, 3, 5), (trp_france_horse_3, 5, 10)]),

  ("goblin_merc_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_cyclop, 1, 3),(trp_goblin_horseman, 15, 27),(trp_goblin_guard, 18, 30)]),
  ("goblin_merc_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_orc_big_boss,1,5),(trp_orc_blackorc_boss, 3, 5),(trp_orc_blackorc,6,10), (trp_orc_veteran_boar,5,7),(trp_orc_warrior,12,15),]),
  
  ("orc_warrior","orc_warrior",icon_orc|carries_goods(5),0,fac_orc,dark_personality,[(trp_orc_boar_big,1,1),(trp_orc_big,1,3),(trp_troll_1,1,1),(trp_orc_warrior,2,18),(trp_orc_boy,4,10),(trp_orc_arrer_boy,4,10)]),
  
  ("mage_merc", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_human_magic_3, 5, 5),(trp_golem_3, 10, 10),(trp_gargoyle, 1, 2)]),
  ("mage_merc_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_human_magic_3, 3, 7),(trp_human_magic_2, 4, 9),(trp_we_recruit, 3, 6)]),

  ("demon_merc_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_demon_5, 1, 3), (trp_demon_4_2, 3, 5), (trp_demon_3, 5, 8)]),
  ("demon_merc_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_demon_6, 1, 5), (trp_demon_1, 13, 27)]),
  
  
  ("undead_merc_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_undead_horse_3, 1, 3),(trp_vampire_1, 6, 18),(trp_undead_magic_2, 3, 5)]),
  ("undead_merc_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_lich_2, 1, 5), (trp_wight, 10, 10)]),
  ("undead_merc_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_skeleton_warrior, 10, 18),(trp_skeleton_archer, 12, 18),(trp_dullahan, 6, 6)]),

  ("werewolf_merc_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_werewolf_1, 6, 30),(trp_werewolf_1_a,3,15)]),
  #("werewolf_merc_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_werewolf_2, 4, 12),(trp_werewolf_2_a,2,6)]),

  ("mummy_merc", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_mummy_4, 0, 1),(trp_mummy_3, 1, 5), (trp_mummy_1, 13, 27)]),

  ("titan_merc_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_titan_1, 2, 5), (trp_titan_2, 1, 1)]),
  ("titan_merc_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_red_dragon, 1, 3), (trp_black_dragon, 1, 1)]),
  ("minotaur_merc", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_undead_magic_1, 2, 6), (trp_minotaur_1, 12, 13), (trp_minotaur_2, 5, 15)]),

  ("dwarf_merc_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_giant_2, 2, 6), (trp_dwarf_musketeer_2_2, 3, 6), (trp_dwarf_veteran, 18, 25)]),
  ("dwarf_merc_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_dwarf_berserker, 12, 25)]),
  ("dwarf_merc_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_giant_3, 2, 6), (trp_dwarf_musketeer_3, 3, 5), (trp_dwarf_guard_1, 5, 7), (trp_dwarf_ironbreaker, 12, 15)]),
  ("dwarf_merc_4","{!}dragon_altar",0,0,fac_neutral,0,[(trp_fire_dragon, 1, 2), (trp_dwarf_musketeer_2_2, 2, 4)]),

  ("drow_elven_merc_1","{!}labyrinth",0,0,fac_neutral,0,[(trp_drowelf_assassin_1,10,15), (trp_drowelf_infantry_1,5,8),(trp_drowelf_which_1, 1, 2)]),
  ("drow_elven_merc_2","{!}labyrinth",0,0,fac_neutral,0,[(trp_drowelf_raider_1,6,7), (trp_drowelf_infantry_2, 3, 5),(trp_drowelf_which_2, 2, 4)]),

  ("grand_elven_merc_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_grandelf_mage_1, 2, 6), (trp_grandelf_arcane_archer, 2, 4),(trp_grandelf_arcane_guard, 1, 2), (trp_grandelf_marksman, 5, 8)]),
  ("grand_elven_merc_2", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_grandelf_cavalry, 1, 2),(trp_grandelf_mage_2,1,2),(trp_grandelf_guard, 2, 3),(trp_grandelf_marksman, 4, 7),(trp_grandelf_infantry, 1, 5)]),

  ("wood_elven_merc_1", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_woodelf_sworddancer, 2, 4), (trp_woodelf_druid_1,1,3),(trp_woodelf_m_hunter, 6, 7), (trp_woodelf_swordman, 3, 5)]),
  ("wood_elven_merc_3", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_woodelf_sharpshooter, 2, 4), (trp_woodelf_druid_1, 2, 3), (trp_woodelf_spearman, 6, 8), (trp_woodelf_m_hunter, 3, 5)]),

  ("troll_merc", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_troll_2, 1, 3), (trp_troll_1, 4, 8)]),
  ("ogre_merc", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_demon_4_3, 1, 3),(trp_ogre_war, 5, 5), (trp_ogre, 15, 20), (trp_ogre_mega, 1, 1)]),
  
  ("witch_merc", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_polish_which_2, 1, 1), (trp_polish_which_1, 1, 3), (trp_werewolf_1, 4, 12)]),
  
  ("viking_merc_2_fan", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_nord_valkyrie_3, 1, 3), (trp_nord_valkyrie_2, 4, 7), (trp_nord_valkyrie_1, 5, 15)]),
  ("viking_merc_3_fan","{!}Lance",0,0,fac_neutral,0,[(trp_lich_3,1,2),(trp_draugr_3,3,5),(trp_draugr_2,12,15)]),

  ("sissofbattle_merc", "{!}Lance", 0, 0, fac_neutral, 0, [(trp_angle, 1, 3), (trp_sissofbattle_c, 2, 3), (trp_sissofbattle, 4, 7)]),

("steppe_bandit_lair" ,"Steppe Bandit Lair",icon_camp|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_khergits,bandit_personality,[(trp_steppe_tribesman,15,58)]),
("taiga_bandit_lair","Tundra Bandit Lair",icon_camp|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_cossack,bandit_personality,[(trp_taiga_bandit,15,58)]),
("desert_bandit_lair" ,"Desert Bandit Lair",icon_camp|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_outlaws,bandit_personality,[(trp_desert_bandit,15,58)]),
("forest_bandit_lair" ,"Forest Bandit Camp",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_outlaws,bandit_personality,[(trp_forest_bandit,15,58)]),
("mountain_bandit_lair" ,"Mountain Bandit Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|fac_outlaws,0,fac_neutral,bandit_personality,[(trp_mountain_bandit,15,58)]),
("sea_raider_lair","Sea Raider Landing",icon_ship_on_land|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_sea_raiders,bandit_personality,[(trp_nord_warrior,15,50)]),

("forest_ranger_lair" ,"Forest ranger Camp",icon_training_ground|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_welsh,bandit_personality,[(trp_welsh_longbowm_1,8,22),(trp_welsh_longbowm_2,5,10),(trp_welsh_longbowm_3,1,1),(trp_sherwood_archer,0,3)]),

#("mountain_tribes_lair" ,"mountain_tribes", icon_village_a|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_mountain_tribe,bandit_personality,[(trp_mountain_tribesman,10,30),(trp_mountain_fighter,8,22),(trp_mountain_warrior,5,10),(trp_mountain_warchief,1,4)]),

("dark_knight_lair", "Dark_castle", icon_castle_a|carries_goods(2)|pf_is_static|pf_hide_defenders, 0, fac_dark_knights, bandit_personality, [(trp_teutonic_spearman,10,30)] ),

("cossack_lair","Vodka Stash",icon_camp|carries_goods(3)|pf_is_static|pf_hide_defenders,0,fac_cossack,bandit_personality,[(trp_rus_cossack,5,52)]),  

("norman_cavalry_lair","Sea Raider Landing",icon_ship_on_land|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_sea_raiders,bandit_personality,[(trp_nord_raider,15,25)]),

("camel_cavalry_lair" ,"Desert Bandit Lair",icon_training_ground|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_outlaws,bandit_personality,[(trp_marinid_camel_2,3,35),(trp_marinid_camel_3_1,3,15)]),

("looter_lair","Kidnappers' Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_looter,15,25)]),

("farm","{!}farm",0,0,fac_neutral,0,[(trp_farmer,15,50)]),
("nomad_tent","{!}nomad_tent",icon_camp|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,0,[(trp_steppe_horseman_2, 8, 10), (trp_black_khergit_horseman,7,14),(trp_black_khergit_raidmaster, 1, 1), (trp_black_khergit_lancer, 5, 8)]),

("gobin_slum","{!}gobin_slum",icon_training_ground|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,0,[(trp_goblin_infantry, 14, 23),(trp_goblin,1,5),(trp_goblin_knight, 3, 7),(trp_goblin_crossbowman, 6, 18), (trp_troll_1, 2, 3)]),
("graveyard","{!}graveyard",0,0,fac_neutral,0,[(trp_zombie_2,2,7),(trp_undead_magic_2,1,3),(trp_wraith,0,1),(trp_se_pikeman_2,5,11),(trp_skeleton_archer,3,5)]),

("imp_cache","{!}imp_cache",0,0,fac_neutral,0,[(trp_demon_1,12,20), (trp_demon_1_2, 10, 18),(trp_demon_4, 0, 2)]),

("rogue_hideout","{!}rogue_hideout",0,0,fac_neutral,0,[(trp_assassin,5,30),(trp_bandit,15,20)]),
("longhouse","{!}longhouse",0,0,fac_neutral,0,[(trp_nord_warrior,18,25),(trp_nord_champion, 3, 7), (trp_mercenary_berserker,6,15)]),

("dwarf_cottage","{!}dwarf_cottage",0,0,fac_neutral,0,[(trp_dwarf_warrior,8,20),(trp_dwarf_musketeer_1, 5, 15), (trp_dwarf_guard_1, 1, 5),]),
("elf_homestead","{!}elf_homestead",0,0,fac_neutral,0,[(trp_woodelf_spearman, 6, 8),(trp_woodelf_scout,6,8), (trp_woodelf_sworddancer, 1, 3), (trp_woodelf_sharpshooter, 0, 2)]),

("monastery","{!}monastery",0,0,fac_neutral,0,[(trp_priest, 0, 2),(trp_clerics,2,5),(trp_monk,8,10)]),
("magic_guild","{!}magic_guild",0,0,fac_neutral,0,[(trp_golem_1, 10, 20),(trp_human_magic_1,6,8)]),

("keep","{!}keep",0,0,fac_neutral,0,[(trp_hired_blade,15,50)]),
("cathedral","{!}cathedral",0,0,fac_neutral,0,[(trp_sissofbattle,4,7),(trp_angle, 1, 2)]),
("demon_gate","{!}demon_gate",0,0,fac_neutral,0,[(trp_demon_3,5,8),(trp_demon_4, 3, 5),(trp_demon_5, 1, 3)]),
("clan_halls","{!}clan_halls",0,0,fac_neutral,0,[(trp_giant_1,7,14),(trp_giant_2, 2, 6), (trp_giant_3, 2, 6)]),
("vampire_estate","{!}vampire_estate",0,0,fac_neutral,0,[(trp_vampire_1,5,10),(trp_undead_horse_1,3,6),(trp_lich_1,0,1)]),

("ogre_fort","{!}ogre_fort",0,0,fac_neutral,0,[(trp_ogre,10,15),(trp_ogre_mega, 1, 5),(trp_ogre_war,8,10),]),

("wolf_pen","{!}wolf_pen",0,0,fac_neutral,0,[(trp_scottish_jav,4, 10),(trp_werewolf_1,2,5)]),
("labyrinth","{!}labyrinth",0,0,fac_neutral,0,[(trp_rat_3,12,15), (trp_minotaur_2, 5, 5),(trp_undead_magic_1, 2, 6)]),

("tomb_of_curses","{!}tomb_of_curses",0,0,fac_neutral,0,[(trp_mummy_2,4,15),(trp_mummy_1,4,28),(trp_mummy_3,1,3),(trp_mummy_4,0,1)]),
("treant_alcove","{!}treant_alcove",0,0,fac_neutral,0,[(trp_ent_2, 2, 6), (trp_woodelf_sharpshooter, 2, 4), (trp_woodelf_sworddancer, 6, 8), (trp_woodelf_m_hunter, 3, 5)]),

("knights_chapter","{!}knights_chapter",0,0,fac_neutral,0,[(trp_hired_blade,15,50)]),
("vampire_palace","{!}vampire_palace",0,0,fac_neutral,0,[(trp_undead_horse_3, 2, 5),(trp_vampire_3, 2, 5)]),
("cloud_temple","{!}cloud_temple",0,0,fac_neutral,0,[(trp_titan_1, 2, 5), (trp_titan_2, 1, 1)]),
("dragon_altar","{!}dragon_altar",0,0,fac_neutral,0,[(trp_green_dragon, 1, 3), (trp_gold_dragon, 1, 1)]),
("undead_magic_guild","{!}undead_magic_guild",0,0,fac_neutral,0,[(trp_lich_1, 1, 5), (trp_lich_2, 1, 2)]),
("troll_cave","{!}troll_cave",0,0,fac_neutral,0,[(trp_troll_2,1,1),(trp_troll_1,2,5)]),
("altar_of_light","{!}altar_of_light",0,0,fac_neutral,0,[(trp_archangle,1,1),(trp_angle, 2, 5)]),
("temple_of_the_fallen","{!}temple_of_the_fallen",0,0,fac_neutral,0,[(trp_demon_5,1,1),(trp_demon_6,2,5),]),
("forlorn_cathedral","{!}forlorn_cathedral",0,0,fac_neutral,0,[(trp_death,1,1), (trp_wraith, 2, 5)]),
("alchemist_lab","{!}alchemist_lab",0,0,fac_neutral,0,[(trp_ogre_cannon, 5, 15)]),


("bandit_lair_templates_end","{!}bandit_lair_templates_end",icon_axeman|carries_goods(2)|pf_is_static,0,fac_outlaws,bandit_personality,[(trp_looter,15,50)]),


#("dark_hoseman", "{!}dark_hoseman", 0, 0, fac_commoners, 0, [(trp_dark_hunter,13,24),(trp_dark_rider,9,15)]),
#("dark_archer", "{!}dark_archer", 0, 0, fac_commoners, 0, [(trp_dark_ranged,12,24),(trp_dark_fighter,12,26)]),
#("dark_footman", "{!}dark_footman", 0, 0, fac_commoners, 0, [(trp_dark_warrior,12,26),(trp_dark_sergeant,4,9),(trp_dark_halberd,4,9)]),
#("dark_new", "{!}dark_new", 0, 0, fac_commoners, 0, [(trp_teutonic_pilgrim,18,30),(trp_dark_fighter,8,18)]),

  ("leaded_looters","Band of robbers",icon_axeman|carries_goods(8)|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_looter_leader,1,1),(trp_looter,3,3)]),
 
   
   ##diplomacy begin
  ("dplmc_spouse","Your spouse",icon_woman|pf_civilian|pf_show_faction,0,fac_neutral,merchant_personality,[]),

  ("dplmc_gift_caravan","Your Caravan",icon_mule|carries_goods(25)|pf_show_faction,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_merchant_cavalry_militia,5,5)]),
#recruiter kit begin
   ("dplmc_recruiter","Recruiter",icon_gray_knight|pf_show_faction,0,fac_neutral,merchant_personality,[(trp_dplmc_recruiter,1,1)]),
#recruiter kit end
   ##diplomacy end
   
  ("morered_army","demon_army",icon_demons|carries_goods(2),0,fac_demon,dark_personality,
  [(trp_demon_5,1,3),(trp_turk_roy_sipahi,3,6),(trp_demon_1_2,8,16),(trp_janissary_infantry_2, 4, 8),(trp_mamluke_horseman_2,2,4),(trp_turk_sipahi,3,5)]),

  ("mira_army","demon_army",icon_demons|carries_goods(2),0,fac_demon,dark_personality,
  [(trp_demon_6,3,3),(trp_drowelf_which_2,3,6),(trp_drowelf_assassin_2,4,8),(trp_medusa_2, 4, 8),(trp_drowelf_raider_2,2,4),(trp_minotaur_3,10,15)]),
    
  ("kugath_army","demon_army",icon_demons|carries_goods(2),0,fac_demon,dark_personality,
  [(trp_demon_9,2,3),(trp_mamluke_horseman_2,3,6),(trp_demon_1_3,8,16),(trp_chaos_warrior_1, 4, 8),(trp_chaos_warrior_2,2,4),(trp_demon_magic_2,3,5)]),

  ("wax_gourd_army","Order of the hospitalier Legion",icon_huge_gray_knight,0,fac_demon_hunters,soldier_personality,  [(trp_hospitaller_knight_2,5,15), (trp_grey_knight_inquisitor,3, 5), (trp_france_horse_3,5, 10), (trp_hospitaller_knight,7, 15), (trp_archangle,3, 6), (trp_teutonic_dis_knight,7, 15)]),

  ("camp_1", "Camp", icon_camp_a|pf_is_static|pf_always_visible|pf_hide_defenders, 0, fac_neutral, bandit_personality, []),
  ("camp_2", "Camp", icon_camp_b|pf_is_static|pf_always_visible|pf_hide_defenders, 0, fac_neutral, bandit_personality, []),

  ("portal_1", "purple portal", icon_map_f_portal_1|pf_is_static|pf_always_visible|pf_hide_defenders, 0, fac_neutral, bandit_personality, []),
  ("portal_2", "red portal", icon_map_f_portal_2|pf_is_static|pf_always_visible|pf_hide_defenders, 0, fac_neutral, bandit_personality, []),
  ("portal_3", "green portal", icon_map_f_portal_3|pf_is_static|pf_always_visible|pf_hide_defenders, 0, fac_neutral, bandit_personality, []),
  ("portal_4", "blue portal", icon_map_f_portal_4|pf_is_static|pf_always_visible|pf_hide_defenders, 0, fac_neutral, bandit_personality, []),

  ("library_of_enlightenment", "Library of Enlightenment", icon_map_f_library_of_enlightenment|pf_is_static|pf_always_visible|pf_hide_defenders, 0, fac_neutral, bandit_personality, []),
  ("arena", "Arena", icon_map_f_arena|pf_is_static|pf_always_visible|pf_hide_defenders, 0, fac_neutral, bandit_personality, []),
  ("training_ground", "Mercenary Camp", icon_training_ground|pf_is_static|pf_always_visible|pf_hide_defenders, 0, fac_neutral, bandit_personality, []),
  ("school_of_magic", "School of Magic", icon_map_f_school_of_magic|pf_is_static|pf_always_visible|pf_hide_defenders, 0, fac_neutral, bandit_personality, []),
  ("witch_hut_1", "Witch Hut", icon_map_f_with_hut|pf_is_static|pf_always_visible|pf_hide_defenders, 0, fac_neutral, bandit_personality, []),
  
  ("tree_of_knowledge", "Tree of Knowledge", icon_map_tree|pf_is_static|pf_always_visible|pf_hide_defenders, 0, fac_neutral, bandit_personality, []),
  ("fountain", "Fountain", icon_fountain|pf_is_static|pf_always_visible|pf_hide_defenders, 0, fac_neutral, bandit_personality, []),
  ("temple", "Temple", icon_map_temple|pf_is_static|pf_always_visible|pf_hide_defenders, 0, fac_neutral, bandit_personality, []),
  ("prison", "prison", icon_map_prison|pf_is_static|pf_always_visible|pf_hide_defenders, 0, fac_neutral, bandit_personality, []),
  
  
  ("wind_mill", "wind_mill", icon_map_windmill|pf_is_static|pf_always_visible|pf_hide_defenders, 0, fac_neutral, bandit_personality, []),
  ("stables", "Stables", icon_map_messenger_post|pf_is_static|pf_always_visible|pf_hide_defenders, 0, fac_neutral, bandit_personality, []),
  ("tavern", "tavern", icon_map_tavern|pf_is_static|pf_always_visible|pf_hide_defenders, 0, fac_neutral, bandit_personality, []),
  ("watchtower", "watchtower", icon_map_watchtower|pf_is_static|pf_always_visible|pf_hide_defenders, 0, fac_neutral, bandit_personality, []),
  
  ("battlefield_1", "battlefield", icon_map_battlefield_1|pf_is_static|pf_always_visible|pf_hide_defenders, 0, fac_neutral, bandit_personality, []),
  ("battlefield_2", "battlefield", icon_map_battlefield_2|pf_is_static|pf_always_visible|pf_hide_defenders, 0, fac_neutral, bandit_personality, []),
  
  ("battlefield_3", "battlefield", icon_map_battlefield_3|pf_is_static|pf_always_visible|pf_hide_defenders, 0, fac_neutral, bandit_personality, []),
  ("battlefield_4", "battlefield", icon_map_battlefield_4|pf_is_static|pf_always_visible|pf_hide_defenders, 0, fac_neutral, bandit_personality, []),

  ("enhancement_end", "{!}Lance", 0, 0, fac_neutral, 0, []),
  
  ("experiance_stone", "Learning stone", icon_map_f_learning_stone|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_outlaw_leader,1,1),(trp_looter,8,40),(trp_bandit,0,8)]),
  
  ("camp_fire", "camp fire", icon_map_camp_fire|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_outlaw_leader,0,2),(trp_looter,8,40),(trp_bandit,0,8)]),
  ("gold_pile", "Gold Pile", icon_map_f_gold|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_outlaw_leader,0,2),(trp_looter,8,40),(trp_bandit,0,8)]),
  ("genie_lamp", "genie_lamp", icon_map_genie_lamp|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_we_recruit,1,3),]),
  ("genie_lamp_2", "genie_lamp", icon_map_genie_lamp|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_demon_4, 1, 3)]),
  ("treasure_chest_1", "treasure_chest", icon_map_treasure_chest|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_outlaw_leader,1,2),(trp_brigand,8,40),(trp_raider,0,8)]),
  ("treasure_chest_2", "treasure_chest", icon_map_f_treasure_chest|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_we_knight_1,2,2),(trp_mountain_bandit,4,20),(trp_forest_bandit,4,20),(trp_we_knight_1,0,8)]),
  ("treasure_chest_3", "treasure_chest", icon_map_f_artifact|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_we_knight_3,2,2),(trp_mountain_bandit,4,20),(trp_forest_bandit,4,20),(trp_we_knight_2,5,12)]),
    
  ("treasure_end", "{!}Lance", 0, 0, fac_neutral, 0, []),
  
  ("dragon_utopia", "Dragon Utopia", icon_map_f_dragon_utopia|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_lich_dragon, 1, 5),(trp_red_dragon, 5, 7),(trp_green_dragon, 5, 7),(trp_fire_dragon, 5, 7),(trp_bone_dragon, 8, 8)]),
  ("crypt", "Crypt", icon_map_f_crypt|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_zombie_1, 20, 20),(trp_se_tribesman, 20, 40),(trp_ghost, 5, 10),(trp_undead_magic_2, 5, 10),(trp_bone_dragon,0,1)]),
  ("pyramid", "Pyramid", icon_map_pyramid|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_mummy_2,4,15),(trp_mummy_1,4,28),(trp_mummy_3,1,3),(trp_mummy_4,0,1)]),
  ("imp_cache_2", "Imp Cache", icon_map_f_imp_cache|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_demon_1,10,20),(trp_demon_1_2,10,20),(trp_demon_1_3,10,20),(trp_demon_2,10,20),(trp_demon_3, 5, 10),(trp_demon_4, 5, 10)]),
  ("golem_factory", "Gargoyle Stonevault", icon_map_f_golem_factory|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_golem_1,10,20),(trp_golem_3,10,20),(trp_golem_2,6,12),(trp_golem_4, 9, 18),(trp_gargoyle, 0, 5)]),
  ("dragon_fly_hive", "Dragon Fly Hive", icon_map_f_dragon_fly_hive|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_dragonfly, 20, 60),(trp_firefly, 10, 30)]),
  ("dwarven_treasury", "Dwarven Treasury", icon_map_f_dwarven_treasury|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_dwarf_miner, 35, 70),(trp_dwarf_warrior, 10, 20),(trp_dwarf_musketeer_1, 5, 10)]),
  ("orc_tower", "Orc Tower", icon_orctower|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_goblin, 30, 70),(trp_orc_boy, 10, 50),(trp_orc_veterun_arrer, 10, 20),(trp_orc_blackorc, 5, 10),(trp_orc_big_boss, 0, 3)]),
  ("ivory_tower", "Ivory Tower", icon_map_f_school_of_magic|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_human_magic_1, 10, 20),(trp_golem_1, 8, 40),(trp_golem_4,2,10),(trp_gargoyle, 0, 2)]),
  ("evil_tower", "Black Tower", icon_evil_tower|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_demon_magic_1, 10, 20),(trp_demon_1, 8, 40),(trp_demon_4,2,10),(trp_demon_human_5_1, 0, 2)]),
  ("treetop_tower", "Treetop Tower", icon_map_f_treetop_tower|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_woodelf_sharpshooter,1,2),(trp_dryad,6,12),(trp_woodelf_hunter,5,10),(trp_woodelf_spearman,5,10),(trp_woodelf_recruit,10,20)]),
  ("subterranean_gate", "Subterranean_Gate", icon_cave|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_rat_2, 20, 50),(trp_minotaur_1, 10, 20),(trp_medusa_1, 10, 20),(trp_undead_magic_1, 10, 10)]),
  ("elemental_conservatory", "Elemental Conservatory", icon_map_f_elemental_conservatory|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_air_elemental, 20, 40),(trp_water_elemental, 20, 40),(trp_fire_elemental, 10, 20),(trp_earth_elemental, 10, 20)]),

  ("treant_thicket", "Treant Thicket", icon_grove|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_ent_1,1,2),(trp_grandelf_mage_1,3,6),(trp_grandelf_marksman,5,10),(trp_grandelf_swordman,5,10),(trp_grandelf_recruit,10,20)]),
  ("hall_of_shadows", "Hall_of_Shadows", icon_hill_fort_evil|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_drowelf_which_2,1,2),(trp_drowelf_assassin_2,3,6),(trp_drowelf_raider_1,5,10),(trp_drowelf_infantry_1,5,10),(trp_drowelf_recruit,10,20)]),
  
  ("keep_1", "Crusader Commandery", icon_hill_fort_good|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_angle,1,2),(trp_clerics,3,6),(trp_teutonic_horse_1,5,10),(trp_france_crossbow_2,5,10),(trp_teutonic_spearman,10,20)]),
  
  ("keep_2", "Mercenary Keep", icon_camp_2|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_german_town_recruit, 30, 70),(trp_german_pikeman_2, 10, 50),(trp_german_crossbow_2, 10, 20),(trp_german_reitern_1, 5, 10),(trp_german_reitern_3, 0, 3)]),
  
  ("keep_3", "hill_fort", icon_castle_hillfort|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_polish_town_recruit, 20, 70),(trp_polish_pikeman_1, 10, 20),(trp_polish_crossbow_2, 10, 20),(trp_polish_horse_3, 10, 30),(trp_polish_knight_1, 5, 13)]),
  
  ("keep_4", "hill_fort", icon_map_castle_nord|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_england_town_recruit, 30, 70),(trp_england_billmen_1, 10, 35),(trp_england_longbowm_2, 10, 35),(trp_england_knight_1, 5, 10),(trp_england_knight_4, 0, 3)]),
  
  ("keep_5", "hill_fort", icon_hill_fort_evil|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_turk_village_rabble, 20, 70),(trp_turk_spearman, 10, 25),(trp_turk_archer_1, 10, 25),(trp_turk_cav_2, 10, 20),(trp_turk_sipahi, 5, 13)]),
  
  ("keep_6","Sea Raider Landing",icon_ship_on_land|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_sea_raiders,bandit_personality,[(trp_nord_recruit, 30, 70),(trp_nord_warrior, 10, 50),(trp_nord_mounted_scout, 10, 20),(trp_mercenary_berserker, 5, 10),(trp_nord_valkyrie_3, 0, 3)]),
    
  ("ruins", "Haunted Ruins", icon_ruins|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_draugr_2,4,15),(trp_draugr_1,4,28),(trp_draugr_lord,4,15),(trp_lich_3,1,1),(trp_lich_dragon,0,1)]),

  ("derelict_ship_1", "Derelict Ship", icon_ship_on_land|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_farmer, 30, 75),(trp_musket_man, 10, 38),]),
  ("derelict_ship_2", "Derelict Ship", icon_ship_on_land|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_water_elemental, 20, 40),]),
  ("derelict_ship_3", "Derelict Ship", icon_ship_on_land|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_air_elemental, 20, 40),]),
  ("derelict_ship_4", "Derelict Ship", icon_ship_on_land|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_drowelf_assassin_3, 10, 20),(trp_drowelf_which_2, 5, 10),]),
  
  
  ("derelict_ship_5", "Ghost Ship", icon_ship_on_land|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_se_pikeman_1, 20, 60),]),
  ("derelict_ship_6", "Ghost Ship", icon_ship_on_land|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_draugr_1, 10, 50),]),
  ("derelict_ship_7", "Ghost Ship", icon_ship_on_land|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_ghost, 0, 22),(trp_wight, 0, 15),(trp_se_billman_1, 0, 21),(trp_zombie_1, 0, 17),]),
  ("derelict_ship_8", "Ghost Ship", icon_ship_on_land|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_ghost, 15, 15),(trp_wight, 15, 15),]),
  
  ("derelict_ship_9", "Ghost Ship", icon_ship_on_land|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_wight, 0, 25),(trp_skeleton_warrior, 0, 15),(trp_zombie_2, 0, 75),]),
  ("derelict_ship_10", "Ghost Ship", icon_ship_on_land|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_ghost, 15, 15),(trp_wight, 21, 21),(trp_wraith, 0, 4),(trp_death, 1, 2),]),

  ("bank_end", "{!}Lance", 0, 0, fac_neutral, 0, []),

  ("cloud_temple_2", "Cloud Temple", icon_map_f_cloud_temple|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_giant_1_3, 8, 12),(trp_giant_3, 2, 3)]),
  ("dragon_cave_5", "Lava Fissure", icon_volcano|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_giant_1_2, 8, 12),(trp_giant_2, 2, 3)]),

  ("portal_of_glory", "Portal of glory", icon_hill_fort_good|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_angle, 8, 12),(trp_archangle, 2, 3)]),
  ("portal_of_glory_2", "Portal of glory", icon_monastery|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_sissofbattle_s, 8, 12),(trp_sissofbattle_r, 2, 3)]),
  ("portal_of_glory_3", "Portal of glory", icon_monastery|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_nord_valkyrie_2, 8, 12),(trp_nord_valkyrie_3, 2, 3)]),
  
  ("cloud_temple_3", "Cloud Temple", icon_map_f_cloud_temple|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_titan_0, 8, 12),(trp_titan_1, 2, 3)]),
  ("cyclops_cave", "Cyclops Cave", icon_map_f_dwarven_treasury|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_cyclop, 8, 12),(trp_cyclop, 2, 3)]),
  ("troll_bridge","Troll Bridge",icon_bridge_a|pf_is_static|pf_hide_defenders, 0, fac_neutral,bandit_personality,[(trp_troll_1, 8, 12),(trp_troll_2, 2, 3)]),
  ("behemoth_cave", "Behemoth Lair", icon_bandit_lair|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_demon_4_2, 8, 12),(trp_demon_4_3, 2, 3)]),
  
  ("forsaken_palace_1", "Khorne Palace", icon_hill_fort_evil|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_demon_7, 8, 12),(trp_demon_5, 2, 3),(trp_demon_3, 8, 12),(trp_demon_1_2, 12, 12)]),
  ("forsaken_palace_2", "Tzeentch Palace", icon_evil_tower|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_demon_human_5_1, 8, 12),(trp_demon_6, 2, 3)]),
  ("forsaken_palace_3", "Nurgle Palace", icon_map_f_forsaken_palace|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_demon_8, 8, 12),(trp_demon_9, 2, 3),(trp_demon_1_3, 12, 12)]),
  ("forsaken_palace_4", "Slaanesh Palace", icon_map_prison|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_demon_human_5_2, 8, 12),(trp_demon_human_5_2, 2, 3)]),
    
  ("vampire_palace_1", "Scholomance", icon_evil_tower|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_lich_1, 8, 12),(trp_lich_2, 2, 3)]),
  ("vampire_palace_2", "vampire Palace", icon_map_prison|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_undead_horse_2, 8, 12),(trp_undead_horse_3, 2, 3)]),
  ("vampire_palace_3", "vampire Palace", icon_map_prison|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_vampire_3, 8, 12),(trp_vampire_4, 2, 3)]),
  
  ("witch_hut_2", "Witch Hut", icon_map_f_with_hut|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_polish_which_1, 8, 12),(trp_polish_which_2, 2, 3)]),
  ("school_of_magic_2", "School of Magic", icon_map_f_school_of_magic|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_human_magic_3, 8, 12),(trp_human_magic_4, 2, 3)]),
  ("pyramid_2", "Pyramid", icon_map_pyramid|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_mummy_3, 8, 12),(trp_mummy_4, 2, 3),(trp_werewolf_1_a, 6, 8),(trp_mummy_1, 18, 24)]),
  
  ("sepulcher", "Sepulcher", icon_map_f_obelisk|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_wraith, 8, 12),(trp_death, 2, 3),(trp_dullahan, 6, 8),(trp_ghost, 12, 16),]),
    
  ("dragon_vault", "Dragon Vault", icon_map_f_dragon_vault|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_bone_dragon, 8, 12),(trp_ghost_dragon, 2, 3)]),
  ("dragon_cave_1", "Dragon Cave", icon_cave_2|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_red_dragon, 8, 12),(trp_black_dragon, 2, 3)]),
  ("dragon_cave_2", "Dragon Vault", icon_map_f_dragon_cave|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_green_dragon, 8, 12),(trp_green_dragon, 2, 3)]),
  ("dragon_cave_3", "Lava Fissure", icon_volcano|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_fire_dragon, 8, 12),(trp_lava_dragon, 2, 3)]),
  ("dragon_cave_4", "Dragon Vault", icon_sacred_forest|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_gold_dragon, 6, 9)]),

  ("golem_factory_2", "Gargoyle Stonevault", icon_map_f_golem_factory|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_golem_3, 10, 15),(trp_golem_4, 7, 10)]),


  ("lair_end", "{!}Lance", 0, 0, fac_neutral, 0, []),
  
  ("obelisk_1", "obelisk", icon_map_f_obelisk|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_ghost_dragon, 1, 1),(trp_lich_3,1,1),(trp_draugr_lord, 6, 8),(trp_draugr_1, 12, 16),]),
  ("obelisk_2", "obelisk", icon_map_f_obelisk|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_ghost_dragon, 1, 1),(trp_lich_3,1,1),(trp_draugr_lord, 6, 8),(trp_draugr_1, 12, 16),]),
  ("obelisk_3", "obelisk", icon_map_f_obelisk|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_lich_dragon, 1, 1),(trp_lich_3,1,1),(trp_draugr_lord, 6, 8),(trp_draugr_1, 12, 16),]),
  
  ("obelisk_4", "obelisk", icon_map_f_obelisk|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_fire_dragon, 1, 1),(trp_lich_3,1,1),(trp_draugr_lord, 6, 8),(trp_draugr_1, 12, 16),]),
  ("obelisk_5", "obelisk", icon_map_f_obelisk|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_green_dragon, 1, 1),(trp_lich_3,1,1),(trp_draugr_lord, 6, 8),(trp_draugr_1, 12, 16),]),
  
  
  
  ("obelisk_6", "obelisk", icon_map_f_obelisk|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_red_dragon, 1, 1),(trp_lich_3,1,1),(trp_draugr_lord, 6, 8),(trp_draugr_1, 12, 16),]),
  ("obelisk_7", "obelisk", icon_map_f_obelisk|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_gold_dragon, 1, 1),(trp_lich_3,1,1),(trp_draugr_lord, 6, 8),(trp_draugr_1, 12, 16),]),

  ("obelisk_8", "obelisk", icon_map_f_obelisk|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_lich_dragon, 1, 1),(trp_lich_3,1,1),(trp_draugr_lord, 6, 8),(trp_draugr_1, 12, 16),]),
  ("obelisk_9", "obelisk", icon_map_f_obelisk|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_red_dragon, 1, 1),(trp_lich_3,1,1),(trp_draugr_lord, 6, 8),(trp_draugr_1, 12, 16),]),

  ("obelisk_10", "obelisk", icon_map_f_obelisk|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_red_dragon, 1, 1),(trp_lich_3,1,1),(trp_draugr_lord, 6, 8),(trp_draugr_1, 12, 16),]),
  ("obelisk_11", "obelisk", icon_map_f_obelisk|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_ghost_dragon, 1, 1),(trp_lich_3,1,1),(trp_draugr_lord, 6, 8),(trp_draugr_1, 12, 16),]),
  ("obelisk_12", "obelisk", icon_map_f_obelisk|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_ghost_dragon, 1, 1),(trp_lich_3,1,1),(trp_draugr_lord, 6, 8),(trp_draugr_1, 12, 16),]),

  ("obelisk_13", "obelisk", icon_map_f_obelisk|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_red_dragon, 1, 1),(trp_lich_3,1,1),(trp_draugr_lord, 6, 8),(trp_draugr_1, 12, 16),]),
  ("obelisk_14", "obelisk", icon_map_f_obelisk|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_gold_dragon, 1, 1),(trp_lich_3,1,1),(trp_draugr_lord, 6, 8),(trp_draugr_1, 12, 16),]),

  ("obelisk_15", "obelisk", icon_map_f_obelisk|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_ghost_dragon, 1, 1),(trp_lich_3,1,1),(trp_draugr_lord, 6, 8),(trp_draugr_1, 12, 16),]),
  ("obelisk_16", "obelisk", icon_map_f_obelisk|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_ghost_dragon, 1, 1),(trp_lich_3,1,1),(trp_draugr_lord, 6, 8),(trp_draugr_1, 12, 16),]),

  ("obelisk_17", "obelisk", icon_map_f_obelisk|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_black_dragon, 1, 1),(trp_lich_3,1,1),(trp_draugr_lord, 6, 8),(trp_draugr_1, 12, 16),]),
  ("obelisk_18", "obelisk", icon_map_f_obelisk|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_black_dragon, 1, 1),(trp_lich_3,1,1),(trp_draugr_lord, 6, 8),(trp_draugr_1, 12, 16),]),
  ("obelisk_19", "obelisk", icon_map_f_obelisk|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_black_dragon, 1, 1),(trp_lich_3,1,1),(trp_draugr_lord, 6, 8),(trp_draugr_1, 12, 16),]),
  
  
  ("obelisk_end", "{!}Lance", 0, 0, fac_neutral, 0, []),
]
# modmerger_start version=201 type=2
try:
    component_name = "party_templates"
    var_set = { "party_templates" : party_templates }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
