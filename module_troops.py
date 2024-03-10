# -*- coding: UTF-8 -*-

import random

from header_common import *
from header_items import *
from header_troops import *
from header_skills import *
from ID_factions import *
from ID_items import *
from ID_scenes import *

####################################################################################################################
#  Each troop contains the following fields:
#  1) Troop id (string): used for referencing troops in other files. The prefix trp_ is automatically added before each troop-id .
#  2) Toop name (string).
#  3) Plural troop name (string).
#  4) Troop flags (int). See header_troops.py for a list of available flags
#  5) Scene (int) (only applicable to heroes) For example: scn_reyvadin_castle|entry(1) puts troop in reyvadin castle's first entry point
#  6) Reserved (int). Put constant "reserved" or 0.
#  7) Faction (int)
#  8) Inventory (list): Must be a list of items
#  9) Attributes (int): Example usage:
#           str_6|agi_6|int_4|cha_5|level(5)
# 10) Weapon proficiencies (int): Example usage:
#           wp_one_handed(55)|wp_two_handed(90)|wp_polearm(36)|wp_archery(80)|wp_crossbow(24)|wp_throwing(45)
#     The function wp(x) will create random weapon proficiencies close to value x.
#     To make an expert archer with other weapon proficiencies close to 60 you can use something like:
#           wp_archery(160) | wp(60)
# 11) Skills (int): See header_skills.py to see a list of skills. Example:
#           knows_ironflesh_3|knows_power_strike_2|knows_physique_2|knows_riding_2
# 12) Face code (int): You can obtain the face code by pressing ctrl+E in face generator screen
# 13) Face code (int)(2) (only applicable to regular troops, can be omitted for heroes):
#     The game will create random faces between Face code 1 and face code 2 for generated troops
# 14) Troop image (string): If this variable is set, the troop will use an image rather than its 3D visual during the conversations
#  town_1   Sargoth
#  town_2   Tihr
#  town_3   Veluca
#  town_4   Suno
#  town_5   Jelkala
#  town_6   Praven
#  town_7   Uxkhal
#  town_8   Reyvadin
#  town_9   Khudan
#  town_10  Tulga
#  town_11  Curaw
#  town_12  Wercheg
#  town_13  Rivacheg
#  town_14  Halmar
####################################################################################################################

# Some constant and function declarations to be used below...

def wp(x):
  n = 0
  r = 10 + int(x / 10)
  n |= wp_one_handed(x)
  n |= wp_two_handed(x)
  n |= wp_polearm(x)
  n |= wp_archery(x)
  n |= wp_crossbow(x)
  n |= wp_throwing(x)
  n |= wp_firearm(x)
  return n

def wpe(m,a,c,t):
   n = 0
   n |= wp_one_handed(m)
   n |= wp_two_handed(m)
   n |= wp_polearm(m)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n

def wpex(o,w,p,a,c,t):
   n = 0
   n |= wp_one_handed(o)
   n |= wp_two_handed(w)
   n |= wp_polearm(p)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   n |= wp_firearm(c)
   return n
   
def wp_melee(x):
  n = 0
  n |= wp_one_handed(x + 20)
  n |= wp_two_handed(x)
  n |= wp_polearm(x + 10)
  return n

def wp_missile(x):
  n = 0
  n |= wp_archery(x)
  n |= wp_crossbow(x)
  n |= wp_throwing(x)
  n |= wp_firearm(x)
  return n

#Skills
knows_common = knows_riding_1|knows_trade_2|knows_inventory_management_2|knows_prisoner_management_1
knows_leader = knows_riding_1|knows_leadership_3
knows_leader_low = knows_riding_1|knows_leadership_2
knows_knight_25 = knows_riding_4|knows_ironflesh_4|knows_shield_5|knows_power_strike_4|knows_physique_2

def_attrib = str_7 | agi_5 | int_4 | cha_4
def_attrib_multiplayer = str_14 | agi_14 | int_9 | cha_8
def_attrib_nobel_low = str_25|agi_25|int_18|cha_10
def_attrib_nobel = str_40|agi_28|int_21|cha_10

knows_knight_npc = knows_weapon_master_2|knows_ironflesh_4|knows_physique_2|knows_power_strike_4|knows_riding_4|knows_shield_2
knows_warrior_npc = knows_weapon_master_2|knows_ironflesh_1|knows_physique_1|knows_power_strike_2|knows_riding_2|knows_shield_1|knows_inventory_management_2
knows_merchant_npc = knows_riding_2|knows_trade_3|knows_inventory_management_3 #knows persuasion
knows_tracker_npc = knows_weapon_master_1|knows_physique_2|knows_spotting_2|knows_pathfinding_2|knows_tracking_2|knows_ironflesh_1|knows_inventory_management_2

gen_caravan_master_1 = tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_hero|tf_inactive|tf_is_merchant
gen_caravan_master_skills = knows_riding_1|knows_trade_2|knows_prisoner_management_1|knows_leadership_1|knows_riding_4|knows_ironflesh_3|knows_inventory_management_1

##chenwz
foot_attrib_1       = str_6|agi_6|int_5|cha_4             #|level(2)                        
foot_attrib_2       = str_9|agi_9|int_6|cha_5             #|level(6)                        
foot_attrib_3       = str_12|agi_9|int_6|cha_6            #|level(12)                      
foot_attrib_4       = str_15|agi_12|int_6|cha_6           #|level(18)                     
foot_attrib_5       = str_18|agi_16|int_9|cha_9           #|level(24)                     
foot_attrib_6       = str_21|agi_15|int_12|cha_12         #|level(30)                   

ranged_attrib_1     = str_9|agi_6|int_6|cha_6             #|level(2)                       
ranged_attrib_2     = str_11|agi_9|int_6|cha_6            #|level(5)                      
ranged_attrib_3     = str_13|agi_12|int_9|cha_9           #|level(11)                     
ranged_attrib_4     = str_15|agi_15|int_12|cha_12         #|level(17)                   
ranged_attrib_5     = str_17|agi_18|int_9|cha_12          #|level(23)                     
ranged_attrib_6     = str_19|agi_18|int_12|cha_12         #|level(29)                   

horse_attrib_1      = str_15|agi_15|int_6|cha_7           #|level(14)                     
horse_attrib_2      = str_18|agi_16|int_6|cha_9           #|level(22)                     
horse_attrib_3      = str_21|agi_18|int_9|cha_9           #|level(27)                     
horse_attrib_4      = str_25|agi_18|int_12|cha_12         #|level(30)                   
horse_attrib_5      = str_30|agi_22|int_12|cha_12         #|level(35)                   
horse_attrib_6      = str_35|agi_24|int_12|cha_12         #|level(40)                   
horse_attrib_7      = str_40|agi_28|int_12|cha_12         #|level(45)                   
horse_attrib_8      = str_45|agi_30|int_12|cha_12         #|level(50)                   
horse_attrib_9      = str_50|agi_32|int_12|cha_12         #|level(55)                   


knows_recruit            = knows_physique_1|knows_power_strike_1|knows_ironflesh_1
knows_militia            = knows_physique_1|knows_shield_1|knows_power_strike_1|knows_ironflesh_1|knows_reserved_18_10|knows_weapon_master_1

knows_infantry_1         = knows_physique_1|knows_shield_2|knows_power_strike_2|knows_ironflesh_2|knows_reserved_18_10|knows_weapon_master_1  #8
knows_infantry_2         = knows_physique_2|knows_shield_3|knows_power_strike_3|knows_ironflesh_3|knows_reserved_18_10|knows_weapon_master_1  #12
knows_infantry_3         = knows_physique_3|knows_shield_4|knows_power_strike_4|knows_ironflesh_4|knows_reserved_18_10|knows_weapon_master_2|knows_magic_defence_2 #18
knows_infantry_4         = knows_physique_4|knows_shield_5|knows_power_strike_5|knows_ironflesh_5|knows_reserved_18_10|knows_weapon_master_2|knows_magic_defence_2
knows_infantry_5         = knows_physique_5|knows_shield_6|knows_power_strike_6|knows_ironflesh_6|knows_reserved_18_10|knows_weapon_master_3|knows_magic_defence_3
knows_infantry_6         = knows_physique_6|knows_shield_7|knows_power_strike_7|knows_ironflesh_8|knows_reserved_18_10|knows_weapon_master_3|knows_magic_defence_3
knows_infantry_7         = knows_physique_7|knows_shield_8|knows_power_strike_8|knows_ironflesh_10|knows_reserved_18_10|knows_weapon_master_4|knows_magic_defence_4 #39
knows_infantry_8         = knows_physique_8|knows_shield_9|knows_power_strike_9|knows_ironflesh_12|knows_reserved_18_10|knows_weapon_master_4|knows_magic_defence_4 #43

knows_pikeman_1          = knows_physique_1|knows_shield_1|knows_power_strike_3|knows_ironflesh_2|knows_reserved_18_10|knows_weapon_master_1|knows_magic_defence_1
knows_pikeman_2          = knows_physique_1|knows_shield_2|knows_power_strike_4|knows_ironflesh_4|knows_reserved_18_10|knows_weapon_master_1|knows_magic_defence_2
knows_pikeman_3          = knows_physique_2|knows_shield_2|knows_power_strike_5|knows_ironflesh_6|knows_reserved_18_10|knows_weapon_master_2|knows_magic_defence_3
knows_pikeman_4          = knows_physique_2|knows_shield_3|knows_power_strike_6|knows_ironflesh_8|knows_reserved_18_10|knows_weapon_master_2|knows_magic_defence_4
knows_pikeman_5          = knows_physique_3|knows_shield_3|knows_power_strike_7|knows_ironflesh_10|knows_reserved_18_10|knows_weapon_master_3|knows_magic_defence_5
knows_pikeman_6          = knows_physique_3|knows_shield_4|knows_power_strike_8|knows_ironflesh_12|knows_reserved_18_10|knows_weapon_master_4|knows_magic_defence_6
knows_pikeman_7          = knows_physique_4|knows_shield_4|knows_power_strike_9|knows_ironflesh_14|knows_reserved_18_10|knows_weapon_master_5|knows_magic_defence_7
knows_pikeman_8          = knows_physique_4|knows_shield_5|knows_power_strike_10|knows_ironflesh_15|knows_reserved_18_10|knows_weapon_master_6|knows_magic_defence_8

knows_spearman_1         = knows_physique_1|knows_shield_3|knows_power_strike_3|knows_ironflesh_2|knows_reserved_18_10|knows_weapon_master_1
knows_spearman_2         = knows_physique_2|knows_shield_4|knows_power_strike_4|knows_ironflesh_3|knows_reserved_18_10|knows_weapon_master_1
knows_spearman_3         = knows_physique_3|knows_shield_5|knows_power_strike_6|knows_ironflesh_4|knows_reserved_18_10|knows_weapon_master_2
knows_spearman_4         = knows_physique_4|knows_shield_6|knows_power_strike_5|knows_ironflesh_5|knows_reserved_18_10|knows_weapon_master_2|knows_magic_defence_1
knows_spearman_5         = knows_physique_5|knows_shield_7|knows_power_strike_7|knows_ironflesh_6|knows_reserved_18_10|knows_weapon_master_3|knows_magic_defence_2
knows_spearman_6         = knows_physique_6|knows_shield_8|knows_power_strike_9|knows_ironflesh_8|knows_reserved_18_10|knows_weapon_master_3|knows_magic_defence_3
knows_spearman_7         = knows_physique_7|knows_shield_9|knows_power_strike_11|knows_ironflesh_10|knows_reserved_18_10|knows_weapon_master_4|knows_magic_defence_4
knows_spearman_8         = knows_physique_8|knows_shield_10|knows_power_strike_13|knows_ironflesh_12|knows_reserved_18_10|knows_weapon_master_4|knows_magic_defence_5

knows_swordman_1         = knows_physique_1|knows_shield_3|knows_power_strike_2|knows_ironflesh_2|knows_reserved_18_10|knows_weapon_master_1|knows_magic_defence_1
knows_swordman_2         = knows_physique_2|knows_shield_4|knows_power_strike_3|knows_ironflesh_4|knows_reserved_18_10|knows_weapon_master_1|knows_magic_defence_2
knows_swordman_3         = knows_physique_2|knows_shield_5|knows_power_strike_4|knows_ironflesh_6|knows_reserved_18_10|knows_weapon_master_1|knows_magic_defence_3
knows_swordman_4         = knows_physique_3|knows_shield_6|knows_power_strike_5|knows_ironflesh_8|knows_reserved_18_10|knows_weapon_master_2|knows_magic_defence_4
knows_swordman_5         = knows_physique_3|knows_shield_7|knows_power_strike_6|knows_ironflesh_9|knows_reserved_18_10|knows_weapon_master_2|knows_magic_defence_5
knows_swordman_6         = knows_physique_4|knows_shield_8|knows_power_strike_7|knows_ironflesh_11|knows_reserved_18_10|knows_weapon_master_3|knows_magic_defence_6
knows_swordman_7         = knows_physique_4|knows_shield_9|knows_power_strike_8|knows_ironflesh_13|knows_reserved_18_10|knows_weapon_master_4|knows_magic_defence_7
knows_swordman_8         = knows_physique_5|knows_shield_10|knows_power_strike_9|knows_ironflesh_15|knows_reserved_18_10|knows_weapon_master_4|knows_magic_defence_8

knows_light_swordman_1         = knows_stealth_1|knows_physique_1|knows_shield_1|knows_power_strike_2|knows_ironflesh_2|knows_reserved_18_10|knows_weapon_master_1
knows_light_swordman_2         = knows_stealth_2|knows_physique_2|knows_shield_2|knows_power_strike_3|knows_ironflesh_3|knows_reserved_18_10|knows_weapon_master_2
knows_light_swordman_3         = knows_stealth_3|knows_physique_3|knows_shield_3|knows_power_strike_4|knows_ironflesh_4|knows_reserved_18_10|knows_weapon_master_3
knows_light_swordman_4         = knows_stealth_4|knows_physique_4|knows_shield_4|knows_power_strike_5|knows_ironflesh_5|knows_reserved_18_10|knows_weapon_master_4|knows_magic_defence_1
knows_light_swordman_5         = knows_stealth_5|knows_physique_5|knows_shield_5|knows_power_strike_6|knows_ironflesh_6|knows_reserved_18_10|knows_weapon_master_5|knows_magic_defence_2
knows_light_swordman_6         = knows_stealth_6|knows_physique_6|knows_shield_6|knows_power_strike_7|knows_ironflesh_7|knows_reserved_18_10|knows_weapon_master_6|knows_magic_defence_3
knows_light_swordman_7         = knows_stealth_7|knows_physique_7|knows_shield_7|knows_power_strike_8|knows_ironflesh_8|knows_reserved_18_10|knows_weapon_master_7|knows_magic_defence_4
knows_light_swordman_8         = knows_stealth_8|knows_physique_8|knows_shield_8|knows_power_strike_9|knows_ironflesh_9|knows_reserved_18_10|knows_weapon_master_8|knows_magic_defence_5

knows_billman_1          = knows_physique_3|knows_shield_1|knows_power_strike_2|knows_ironflesh_2|knows_reserved_18_10|knows_weapon_master_1
knows_billman_2          = knows_physique_4|knows_shield_1|knows_power_strike_3|knows_ironflesh_3|knows_reserved_18_10|knows_weapon_master_1|knows_stealth_1
knows_billman_3          = knows_physique_5|knows_shield_2|knows_power_strike_5|knows_ironflesh_4|knows_reserved_18_10|knows_weapon_master_2|knows_stealth_1
knows_billman_4          = knows_physique_6|knows_shield_2|knows_power_strike_7|knows_ironflesh_5|knows_reserved_18_10|knows_weapon_master_2|knows_stealth_2|knows_magic_defence_1
knows_billman_5          = knows_physique_7|knows_shield_3|knows_power_strike_9|knows_ironflesh_6|knows_reserved_18_10|knows_weapon_master_3|knows_stealth_2|knows_magic_defence_2
knows_billman_6          = knows_physique_8|knows_shield_3|knows_power_strike_11|knows_ironflesh_7|knows_reserved_18_10|knows_weapon_master_3|knows_stealth_3|knows_magic_defence_3
knows_billman_7          = knows_physique_9|knows_shield_4|knows_power_strike_13|knows_ironflesh_8|knows_reserved_18_10|knows_weapon_master_4|knows_stealth_3|knows_magic_defence_4
knows_billman_8          = knows_physique_10|knows_shield_4|knows_power_strike_15|knows_ironflesh_9|knows_reserved_18_10|knows_weapon_master_4|knows_stealth_4|knows_magic_defence_5

knows_twohand_1          = knows_physique_1|knows_shield_2|knows_power_strike_3|knows_ironflesh_2|knows_reserved_18_10|knows_weapon_master_1
knows_twohand_2          = knows_physique_2|knows_shield_2|knows_power_strike_4|knows_ironflesh_3|knows_reserved_18_10|knows_weapon_master_2
knows_twohand_3          = knows_physique_3|knows_shield_3|knows_power_strike_5|knows_ironflesh_4|knows_reserved_18_10|knows_weapon_master_2|knows_stealth_1
knows_twohand_4          = knows_physique_4|knows_shield_3|knows_power_strike_6|knows_ironflesh_5|knows_reserved_18_10|knows_weapon_master_3|knows_stealth_1|knows_magic_defence_1
knows_twohand_5          = knows_physique_5|knows_shield_4|knows_power_strike_7|knows_ironflesh_6|knows_reserved_18_10|knows_weapon_master_3|knows_stealth_2|knows_magic_defence_2
knows_twohand_6          = knows_physique_6|knows_shield_4|knows_power_strike_9|knows_ironflesh_8|knows_reserved_18_10|knows_weapon_master_4|knows_stealth_2|knows_magic_defence_3
knows_twohand_7          = knows_physique_7|knows_shield_5|knows_power_strike_11|knows_ironflesh_10|knows_reserved_18_10|knows_weapon_master_4|knows_stealth_3|knows_magic_defence_4
knows_twohand_8          = knows_physique_8|knows_shield_5|knows_power_strike_13|knows_ironflesh_12|knows_reserved_18_10|knows_weapon_master_5|knows_stealth_3|knows_magic_defence_5
knows_twohand_9          = knows_physique_9|knows_shield_6|knows_power_strike_15|knows_ironflesh_15|knows_reserved_18_10|knows_weapon_master_6|knows_stealth_4|knows_magic_defence_6

knows_archer_1           = knows_physique_2|knows_shield_1|knows_power_strike_1|knows_ironflesh_1|knows_reserved_18_10|knows_weapon_master_1|knows_power_draw_2
knows_archer_2           = knows_physique_3|knows_shield_1|knows_power_strike_2|knows_ironflesh_2|knows_reserved_18_10|knows_weapon_master_1|knows_power_draw_3
knows_archer_3           = knows_physique_4|knows_shield_2|knows_power_strike_3|knows_ironflesh_3|knows_reserved_18_10|knows_weapon_master_2|knows_power_draw_4|knows_magic_defence_1
knows_archer_4           = knows_physique_5|knows_shield_2|knows_power_strike_4|knows_ironflesh_4|knows_reserved_18_10|knows_weapon_master_2|knows_power_draw_5|knows_magic_defence_1
knows_archer_5           = knows_physique_6|knows_shield_3|knows_power_strike_5|knows_ironflesh_5|knows_reserved_18_10|knows_weapon_master_3|knows_power_draw_6|knows_magic_defence_2
knows_archer_6           = knows_physique_6|knows_shield_3|knows_power_strike_6|knows_ironflesh_6|knows_reserved_18_10|knows_weapon_master_3|knows_power_draw_7|knows_magic_defence_2
knows_archer_7           = knows_physique_7|knows_shield_4|knows_power_strike_7|knows_ironflesh_7|knows_reserved_18_10|knows_weapon_master_4|knows_power_draw_8|knows_magic_defence_3
knows_archer_8           = knows_physique_8|knows_shield_4|knows_power_strike_8|knows_ironflesh_8|knows_reserved_18_10|knows_weapon_master_4|knows_power_draw_9|knows_magic_defence_3
knows_archer_9           = knows_physique_9|knows_shield_5|knows_power_strike_9|knows_ironflesh_9|knows_reserved_18_10|knows_weapon_master_5|knows_power_draw_10|knows_magic_defence_4

knows_nomad_1           = knows_physique_1|knows_shield_1|knows_power_strike_1|knows_ironflesh_1|knows_reserved_18_10|knows_weapon_master_1|knows_reserved_17_1|knows_power_draw_1|knows_stealth_1
knows_nomad_2           = knows_physique_1|knows_shield_2|knows_power_strike_1|knows_ironflesh_2|knows_reserved_18_10|knows_weapon_master_2|knows_reserved_17_2|knows_power_draw_2|knows_stealth_1
knows_nomad_3           = knows_physique_2|knows_shield_2|knows_power_strike_2|knows_ironflesh_2|knows_reserved_18_10|knows_weapon_master_3|knows_reserved_17_2|knows_power_draw_3|knows_stealth_1|knows_magic_defence_1
knows_nomad_4           = knows_physique_2|knows_shield_3|knows_power_strike_2|knows_ironflesh_3|knows_reserved_18_10|knows_weapon_master_4|knows_reserved_17_3|knows_power_draw_4|knows_stealth_2|knows_magic_defence_1
knows_nomad_5           = knows_physique_3|knows_shield_3|knows_power_strike_3|knows_ironflesh_3|knows_reserved_18_10|knows_weapon_master_5|knows_reserved_17_3|knows_power_draw_5|knows_stealth_2|knows_magic_defence_1
knows_nomad_6           = knows_physique_3|knows_shield_4|knows_power_strike_3|knows_ironflesh_4|knows_reserved_18_10|knows_weapon_master_6|knows_reserved_17_4|knows_power_draw_6|knows_stealth_2|knows_magic_defence_2
knows_nomad_7           = knows_physique_4|knows_shield_4|knows_power_strike_4|knows_ironflesh_5|knows_reserved_18_10|knows_weapon_master_7|knows_reserved_17_4|knows_power_draw_7|knows_stealth_3|knows_magic_defence_2
knows_nomad_8           = knows_physique_4|knows_shield_5|knows_power_strike_4|knows_ironflesh_6|knows_reserved_18_10|knows_weapon_master_8|knows_reserved_17_5|knows_power_draw_8|knows_stealth_3|knows_magic_defence_2
knows_nomad_9           = knows_physique_5|knows_shield_5|knows_power_strike_5|knows_ironflesh_7|knows_reserved_18_10|knows_weapon_master_9|knows_reserved_17_5|knows_power_draw_9|knows_stealth_3|knows_magic_defence_3

knows_ranger_1           = knows_physique_2|knows_stealth_1|knows_power_strike_1|knows_ironflesh_1|knows_reserved_18_10|knows_weapon_master_1|knows_power_draw_1
knows_ranger_2           = knows_physique_3|knows_stealth_1|knows_power_strike_2|knows_ironflesh_2|knows_reserved_18_10|knows_weapon_master_2|knows_power_draw_2
knows_ranger_3           = knows_physique_4|knows_stealth_2|knows_power_strike_3|knows_ironflesh_2|knows_reserved_18_10|knows_weapon_master_3|knows_power_draw_3|knows_magic_defence_1
knows_ranger_4           = knows_physique_5|knows_stealth_2|knows_power_strike_4|knows_ironflesh_3|knows_reserved_18_10|knows_weapon_master_4|knows_power_draw_4|knows_magic_defence_2
knows_ranger_5           = knows_physique_6|knows_stealth_3|knows_power_strike_5|knows_ironflesh_3|knows_reserved_18_10|knows_weapon_master_5|knows_power_draw_5|knows_magic_defence_3
knows_ranger_6           = knows_physique_6|knows_stealth_3|knows_power_strike_6|knows_ironflesh_4|knows_reserved_18_10|knows_weapon_master_6|knows_power_draw_6|knows_magic_defence_3
knows_ranger_7           = knows_physique_7|knows_stealth_4|knows_power_strike_7|knows_ironflesh_5|knows_reserved_18_10|knows_weapon_master_7|knows_power_draw_7|knows_magic_defence_4
knows_ranger_8           = knows_physique_8|knows_stealth_4|knows_power_strike_8|knows_ironflesh_6|knows_reserved_18_10|knows_weapon_master_8|knows_power_draw_8|knows_magic_defence_4
knows_ranger_9           = knows_physique_9|knows_stealth_5|knows_power_strike_9|knows_ironflesh_7|knows_reserved_18_10|knows_weapon_master_9|knows_power_draw_9|knows_magic_defence_5

knows_crossbowman_1      = knows_precise_shot_2|knows_physique_1|knows_shield_1|knows_power_strike_2|knows_ironflesh_1|knows_reserved_18_10|knows_weapon_master_1|knows_stealth_1
knows_crossbowman_2      = knows_precise_shot_3|knows_physique_2|knows_shield_2|knows_power_strike_3|knows_ironflesh_2|knows_reserved_18_10|knows_weapon_master_1|knows_stealth_2
knows_crossbowman_3      = knows_precise_shot_4|knows_physique_3|knows_shield_2|knows_power_strike_4|knows_ironflesh_3|knows_reserved_18_10|knows_weapon_master_2|knows_stealth_3|knows_magic_defence_1
knows_crossbowman_4      = knows_precise_shot_5|knows_physique_4|knows_shield_3|knows_power_strike_5|knows_ironflesh_4|knows_reserved_18_10|knows_weapon_master_2|knows_stealth_4|knows_magic_defence_1
knows_crossbowman_5      = knows_precise_shot_6|knows_physique_5|knows_shield_3|knows_power_strike_6|knows_ironflesh_5|knows_reserved_18_10|knows_weapon_master_3|knows_stealth_5|knows_magic_defence_2
knows_crossbowman_6      = knows_precise_shot_7|knows_physique_6|knows_shield_4|knows_power_strike_7|knows_ironflesh_6|knows_reserved_18_10|knows_weapon_master_3|knows_stealth_6|knows_magic_defence_3
knows_crossbowman_7      = knows_precise_shot_8|knows_physique_7|knows_shield_4|knows_power_strike_8|knows_ironflesh_7|knows_reserved_18_10|knows_weapon_master_4|knows_stealth_7|knows_magic_defence_4
knows_crossbowman_8      = knows_precise_shot_9|knows_physique_8|knows_shield_5|knows_power_strike_9|knows_ironflesh_8|knows_reserved_18_10|knows_weapon_master_4|knows_stealth_8|knows_magic_defence_5

knows_firearm_1          = knows_precise_shot_1|knows_physique_2|knows_shield_1|knows_power_strike_2|knows_ironflesh_2|knows_reserved_18_10|knows_weapon_master_1|knows_stealth_1
knows_firearm_2          = knows_precise_shot_2|knows_physique_3|knows_shield_1|knows_power_strike_3|knows_ironflesh_2|knows_reserved_18_10|knows_weapon_master_2|knows_stealth_2
knows_firearm_3          = knows_precise_shot_3|knows_physique_4|knows_shield_2|knows_power_strike_4|knows_ironflesh_3|knows_reserved_18_10|knows_weapon_master_3|knows_stealth_3|knows_magic_defence_1
knows_firearm_4          = knows_precise_shot_4|knows_physique_5|knows_shield_2|knows_power_strike_5|knows_ironflesh_3|knows_reserved_18_10|knows_weapon_master_4|knows_stealth_4|knows_magic_defence_1
knows_firearm_5          = knows_precise_shot_5|knows_physique_6|knows_shield_3|knows_power_strike_6|knows_ironflesh_4|knows_reserved_18_10|knows_weapon_master_5|knows_stealth_5|knows_magic_defence_2
knows_firearm_6          = knows_precise_shot_6|knows_physique_7|knows_shield_3|knows_power_strike_7|knows_ironflesh_4|knows_reserved_18_10|knows_weapon_master_6|knows_stealth_6|knows_magic_defence_2
knows_firearm_7          = knows_precise_shot_7|knows_physique_8|knows_shield_4|knows_power_strike_8|knows_ironflesh_5|knows_reserved_18_10|knows_weapon_master_7|knows_stealth_7|knows_magic_defence_3
knows_firearm_8          = knows_precise_shot_8|knows_physique_9|knows_shield_4|knows_power_strike_9|knows_ironflesh_5|knows_reserved_18_10|knows_weapon_master_8|knows_stealth_8|knows_magic_defence_4

knows_thrown_1           = knows_physique_2|knows_shield_1|knows_power_strike_2|knows_ironflesh_2|knows_reserved_18_10|knows_weapon_master_1|knows_reserved_17_2
knows_thrown_2           = knows_physique_3|knows_shield_2|knows_power_strike_3|knows_ironflesh_3|knows_reserved_18_10|knows_weapon_master_1|knows_reserved_17_3
knows_thrown_3           = knows_physique_4|knows_shield_2|knows_power_strike_4|knows_ironflesh_4|knows_reserved_18_10|knows_weapon_master_2|knows_reserved_17_4
knows_thrown_4           = knows_physique_5|knows_shield_3|knows_power_strike_5|knows_ironflesh_5|knows_reserved_18_10|knows_weapon_master_2|knows_reserved_17_5|knows_magic_defence_1
knows_thrown_5           = knows_physique_6|knows_shield_3|knows_power_strike_6|knows_ironflesh_6|knows_reserved_18_10|knows_weapon_master_3|knows_reserved_17_6|knows_magic_defence_1
knows_thrown_6           = knows_physique_7|knows_shield_4|knows_power_strike_7|knows_ironflesh_7|knows_reserved_18_10|knows_weapon_master_3|knows_reserved_17_7|knows_magic_defence_2
knows_thrown_7           = knows_physique_8|knows_shield_4|knows_power_strike_8|knows_ironflesh_8|knows_reserved_18_10|knows_weapon_master_4|knows_reserved_17_8|knows_magic_defence_2
knows_thrown_8           = knows_physique_9|knows_shield_5|knows_power_strike_9|knows_ironflesh_9|knows_reserved_18_10|knows_weapon_master_4|knows_reserved_17_9|knows_magic_defence_3
knows_thrown_9           = knows_physique_10|knows_shield_6|knows_power_strike_10|knows_ironflesh_10|knows_reserved_18_10|knows_weapon_master_5|knows_reserved_17_10|knows_magic_defence_4

knows_magic_1           = knows_physique_1|knows_shield_1|knows_power_strike_1|knows_ironflesh_1|knows_reserved_18_10|knows_weapon_master_1|knows_magic_power_1|knows_magic_defence_1|knows_necromancy_1|knows_magic_skill_1
knows_magic_2           = knows_physique_1|knows_shield_2|knows_power_strike_1|knows_ironflesh_1|knows_reserved_18_10|knows_weapon_master_1|knows_magic_power_2|knows_magic_defence_2|knows_necromancy_2|knows_magic_skill_2
knows_magic_3           = knows_physique_2|knows_shield_2|knows_power_strike_2|knows_ironflesh_2|knows_reserved_18_10|knows_weapon_master_2|knows_magic_power_3|knows_magic_defence_3|knows_necromancy_2|knows_magic_skill_3
knows_magic_4           = knows_physique_3|knows_shield_3|knows_power_strike_2|knows_ironflesh_2|knows_reserved_18_10|knows_weapon_master_2|knows_magic_power_4|knows_magic_defence_4|knows_necromancy_3|knows_magic_skill_4
knows_magic_5           = knows_physique_3|knows_shield_3|knows_power_strike_3|knows_ironflesh_3|knows_reserved_18_10|knows_weapon_master_3|knows_magic_power_5|knows_magic_defence_5|knows_necromancy_3|knows_magic_skill_5
knows_magic_6           = knows_physique_4|knows_shield_4|knows_power_strike_3|knows_ironflesh_3|knows_reserved_18_10|knows_weapon_master_3|knows_magic_power_6|knows_magic_defence_6|knows_necromancy_4|knows_magic_skill_6
knows_magic_7           = knows_physique_4|knows_shield_4|knows_power_strike_4|knows_ironflesh_4|knows_reserved_18_10|knows_weapon_master_4|knows_magic_power_7|knows_magic_defence_7|knows_necromancy_4|knows_magic_skill_7
knows_magic_8           = knows_physique_5|knows_shield_5|knows_power_strike_4|knows_ironflesh_4|knows_reserved_18_10|knows_weapon_master_4|knows_magic_power_8|knows_magic_defence_8|knows_necromancy_5|knows_magic_skill_8

knows_assasin_1         = knows_stealth_3|knows_physique_1|knows_power_strike_2|knows_ironflesh_2|knows_reserved_18_10|knows_weapon_master_3
knows_assasin_2         = knows_stealth_4|knows_physique_2|knows_power_strike_3|knows_ironflesh_2|knows_reserved_18_10|knows_weapon_master_4
knows_assasin_3         = knows_stealth_5|knows_physique_3|knows_power_strike_4|knows_ironflesh_3|knows_reserved_18_10|knows_weapon_master_5|knows_magic_defence_1
knows_assasin_4         = knows_stealth_6|knows_physique_4|knows_power_strike_5|knows_ironflesh_3|knows_reserved_18_10|knows_weapon_master_6|knows_magic_defence_2
knows_assasin_5         = knows_stealth_7|knows_physique_5|knows_power_strike_7|knows_ironflesh_4|knows_reserved_18_10|knows_weapon_master_7|knows_magic_defence_3
knows_assasin_6         = knows_stealth_8|knows_physique_6|knows_power_strike_9|knows_ironflesh_4|knows_reserved_18_10|knows_weapon_master_8|knows_magic_defence_4
knows_assasin_7         = knows_stealth_9|knows_physique_7|knows_power_strike_11|knows_ironflesh_5|knows_reserved_18_10|knows_weapon_master_9|knows_magic_defence_5
knows_assasin_8         = knows_stealth_10|knows_physique_8|knows_power_strike_13|knows_ironflesh_5|knows_reserved_18_10|knows_weapon_master_10|knows_magic_defence_6
knows_assasin_9         = knows_stealth_10|knows_physique_7|knows_power_strike_15|knows_ironflesh_5|knows_reserved_18_10|knows_weapon_master_10|knows_magic_defence_6

knows_vampire_1           = knows_ironflesh_1|knows_magic_defence_3
knows_vampire_2           = knows_ironflesh_2|knows_magic_defence_3
knows_vampire_3           = knows_ironflesh_3|knows_magic_defence_4
knows_vampire_4           = knows_ironflesh_4|knows_magic_defence_4
knows_vampire_5           = knows_ironflesh_5|knows_magic_defence_5
knows_vampire_6           = knows_ironflesh_6|knows_magic_defence_5
knows_vampire_7           = knows_ironflesh_7|knows_magic_defence_6

knows_knight_1           = knows_riding_2|knows_weapon_master_1|knows_magic_defence_2
knows_knight_2           = knows_riding_3|knows_weapon_master_1|knows_magic_defence_3
knows_knight_3           = knows_riding_4|knows_weapon_master_2|knows_magic_defence_3
knows_knight_4           = knows_riding_5|knows_weapon_master_2|knows_magic_defence_4
knows_knight_5           = knows_riding_6|knows_weapon_master_3|knows_magic_defence_4
knows_knight_6           = knows_riding_7|knows_weapon_master_3|knows_magic_defence_5
knows_knight_7           = knows_riding_8|knows_weapon_master_4|knows_magic_defence_5

knows_knight_east_1           = knows_riding_3|knows_weapon_master_1|knows_magic_defence_2
knows_knight_east_2           = knows_riding_4|knows_weapon_master_1|knows_magic_defence_3
knows_knight_east_3           = knows_riding_5|knows_weapon_master_2|knows_magic_defence_3
knows_knight_east_4           = knows_riding_6|knows_weapon_master_2|knows_magic_defence_4
knows_knight_east_5           = knows_riding_7|knows_weapon_master_3|knows_magic_defence_4
knows_knight_east_6           = knows_riding_8|knows_weapon_master_3|knows_magic_defence_5
knows_knight_east_7           = knows_riding_9|knows_weapon_master_4|knows_magic_defence_5

knows_knight_order_1           = knows_riding_2|knows_weapon_master_1|knows_magic_defence_3
knows_knight_order_2           = knows_riding_3|knows_weapon_master_1|knows_magic_defence_3
knows_knight_order_3           = knows_riding_4|knows_weapon_master_2|knows_magic_defence_4
knows_knight_order_4           = knows_riding_5|knows_weapon_master_2|knows_magic_defence_4
knows_knight_order_5           = knows_riding_6|knows_weapon_master_3|knows_magic_defence_5
knows_knight_order_6           = knows_riding_7|knows_weapon_master_3|knows_magic_defence_5
knows_knight_order_7           = knows_riding_8|knows_weapon_master_4|knows_magic_defence_6

knows_knight_foot_1           = knows_riding_2|knows_weapon_master_1|knows_magic_defence_1|knows_stealth_1
knows_knight_foot_2           = knows_riding_3|knows_weapon_master_1|knows_magic_defence_2|knows_stealth_1
knows_knight_foot_3           = knows_riding_4|knows_weapon_master_2|knows_magic_defence_2|knows_stealth_1
knows_knight_foot_4           = knows_riding_5|knows_weapon_master_2|knows_magic_defence_3|knows_stealth_2
knows_knight_foot_5           = knows_riding_6|knows_weapon_master_3|knows_magic_defence_3|knows_stealth_2
knows_knight_foot_6           = knows_riding_7|knows_weapon_master_3|knows_magic_defence_4|knows_stealth_2
knows_knight_foot_7           = knows_riding_8|knows_weapon_master_4|knows_magic_defence_4|knows_stealth_3

knows_horse_shoot_1      = knows_riding_1|knows_horse_archery_1
knows_horse_shoot_2      = knows_riding_2|knows_horse_archery_2
knows_horse_shoot_3      = knows_riding_3|knows_horse_archery_3
knows_horse_shoot_4      = knows_riding_4|knows_horse_archery_4
knows_horse_shoot_5      = knows_riding_5|knows_horse_archery_5
knows_horse_shoot_6      = knows_riding_6|knows_horse_archery_6
knows_horse_shoot_7      = knows_riding_7|knows_horse_archery_7
knows_horse_shoot_8      = knows_riding_8|knows_horse_archery_8
knows_horse_shoot_9      = knows_riding_9|knows_horse_archery_9
knows_horse_shoot_10      = knows_riding_10|knows_horse_archery_10
##chenwz

## CC
lord_attrib = str_60|agi_60|int_30|cha_20|level(38)
knows_lord_1 = knows_riding_3|knows_trade_3|knows_inventory_management_2|knows_tactics_4|knows_prisoner_management_4|knows_leadership_7|knows_pathfinding_5|knows_weapon_master_5

knight_attrib_1 = str_60|agi_40|int_12|cha_16|level(22)
knight_attrib_2 = str_55|agi_45|int_15|cha_18|level(26)
knight_attrib_3 = str_50|agi_50|int_18|cha_20|level(30)
knight_attrib_4 = str_45|agi_55|int_21|cha_22|level(35)
knight_attrib_5 = str_40|agi_60|int_24|cha_25|level(41)

king_attrib = str_100|agi_100|int_100|cha_25|level(60)
king_skills = knows_stealth_10|knows_riding_10|knows_ironflesh_15|knows_power_strike_15|knows_physique_10|knows_tactics_7|knows_prisoner_management_10|knows_leadership_15|knows_pathfinding_10|knows_trade_10|knows_weapon_master_10|knows_magic_defence_10|knows_horse_archery_10|knows_necromancy_5|knows_magic_power_5|knows_magic_skill_15


knight_skills_1 = knows_stealth_9|knows_riding_5|knows_ironflesh_13|knows_power_strike_13|knows_physique_13|knows_tactics_1|knows_prisoner_management_1|knows_leadership_5|knows_pathfinding_3|knows_trade_8|knows_weapon_master_2|knows_magic_defence_2|knows_magic_skill_5|knows_magic_power_1
knight_skills_2 = knows_stealth_7|knows_riding_5|knows_ironflesh_11|knows_power_strike_11|knows_physique_11|knows_tactics_2|knows_prisoner_management_2|knows_leadership_7|knows_pathfinding_5|knows_trade_7|knows_weapon_master_4|knows_magic_defence_4|knows_magic_skill_7|knows_magic_power_2
knight_skills_3 = knows_stealth_5|knows_riding_6|knows_ironflesh_9|knows_power_strike_9|knows_physique_9|knows_tactics_3|knows_prisoner_management_2|knows_leadership_9|knows_pathfinding_7|knows_trade_6|knows_weapon_master_6|knows_magic_defence_6|knows_magic_skill_9|knows_magic_power_3
knight_skills_4 = knows_stealth_5|knows_riding_6|knows_ironflesh_7|knows_power_strike_7|knows_physique_7|knows_tactics_6|knows_prisoner_management_3|knows_leadership_11|knows_pathfinding_9|knows_trade_5|knows_weapon_master_8|knows_magic_defence_8|knows_magic_skill_12|knows_magic_power_4
knight_skills_5 = knows_stealth_5|knows_riding_7|knows_ironflesh_7|knows_power_strike_5|knows_physique_5|knows_tactics_8|knows_prisoner_management_3|knows_leadership_13|knows_pathfinding_10|knows_trade_4|knows_weapon_master_10|knows_magic_defence_10|knows_magic_skill_14|knows_magic_power_5
## CC

tf_guarantee_all = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged
tf_guarantee_all_wo_ranged = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield

tf_guarantee_all_wo_horse = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged
tf_guarantee_all_footman = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield

tf_guarantee_all_pikeman = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_polearm
tf_guarantee_all_lancer = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_polearm|tf_guarantee_shield
tf_guarantee_all_nomad = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_polearm|tf_guarantee_ranged


#These face codes are generated by the in-game face generator.
#Enable edit mode and press ctrl+E in face generator screen to obtain face codes.


reserved = 0

no_scene = 0

swadian_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
swadian_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
swadian_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
swadian_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
swadian_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

swadian_face_younger_2 = 0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_young_2   = 0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_middle_2  = 0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_old_2     = 0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_older_2   = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000

west_euro_face_younger_1 = 0x0000000000002001355335371861249200000000001c96520000000000000000
west_euro_face_young_1   = 0x00000004400023c1355335371861249200000000001c96520000000000000000
west_euro_face_middle_1  = 0x00000008000023c1355335371861249200000000001c96520000000000000000
west_euro_face_old_1     = 0x0000000e000023c0355335371861249200000000001c96520000000000000000
west_euro_face_older_1   = 0x0000000fc00023c0355335371861249200000000001c96520000000000000000

west_euro_face_younger_2 = 0x000000003a0045c549fddefdffffffff00000000001e6db60000000000000000
west_euro_face_young_2   = 0x000000033a0045c549fddefdffffffff00000000001e6db60000000000000000
west_euro_face_middle_2  = 0x00000007ba0045c549fddefdffffffff00000000001e6db60000000000000000
west_euro_face_old_2     = 0x0000000e3b0045c549fddefdffffffff00000000001e6db60000000000000000
west_euro_face_older_2   = 0x0000000ffa0045c549fddefdffffffff00000000001e6db60000000000000000

east_euro_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
east_euro_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
east_euro_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
east_euro_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
east_euro_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

east_euro_face_younger_2 = 0x000000003f00230c4deeffffffffffff00000000001efff90000000000000000
east_euro_face_young_2   = 0x00000003bf00230c4deeffffffffffff00000000001efff90000000000000000
east_euro_face_middle_2  = 0x00000007bf00230c4deeffffffffffff00000000001efff90000000000000000
east_euro_face_old_2     = 0x0000000cbf00230c4deeffffffffffff00000000001efff90000000000000000
east_euro_face_older_2   = 0x0000000ff100230c4deeffffffffffff00000000001efff90000000000000000

vaegir_face_younger_1 = 0x000000001d001141044c21928821245200000000001d22190000000000000000
vaegir_face_young_1   = 0x000000029b001181044c21928821245200000000001d22190000000000000000
vaegir_face_middle_1  = 0x000000075f001181044c21928821245200000000001d22190000000000000000
vaegir_face_old_1     = 0x0000000e1f001181044c21928821245200000000001d22190000000000000000
vaegir_face_older_1   = 0x0000000fdf001180044c21928821245200000000001d22190000000000000000

vaegir_face_younger_2 = 0x0000000037002189497e97cb5fb27fff00000000001ff8370000000000000000
vaegir_face_young_2   = 0x0000000477002249497e97cb5fb27fff00000000001ff8370000000000000000
vaegir_face_middle_2  = 0x0000000877002349497e97cb5fb27fff00000000001ff8370000000000000000
vaegir_face_old_2     = 0x0000000e37002349497e97cb5fb27fff00000000001ff8370000000000000000
vaegir_face_older_2   = 0x0000000ff7002349497e97cb5fb27fff00000000001ff8370000000000000000

khergit_face_younger_1 = 0x00000000190830ca209d69b4100906da00000000001e10e30000000000000000
khergit_face_young_1   = 0x00000003590830ca209d69b4100906da00000000001e10e30000000000000000
khergit_face_middle_1  = 0x00000007d90830ca209d69b4100906da00000000001e10e30000000000000000
khergit_face_old_1     = 0x0000000e190830ca209d69b4100906da00000000001e10e30000000000000000
khergit_face_older_1   = 0x0000000fd90830ca209d69b4100906da00000000001e10e30000000000000000

khergit_face_younger_2 = 0x000000003f08514d49fff7d86cffffff00000000001ff97f0000000000000000
khergit_face_young_2   = 0x000000047f08514d49fff7d86cffffff00000000001ff97f0000000000000000
khergit_face_middle_2  = 0x00000007bf08514d49fff7d86cffffff00000000001ff97f0000000000000000
khergit_face_old_2     = 0x0000000e3f08518d49fff7d86cffffff00000000001ff97f0000000000000000
khergit_face_older_2   = 0x0000000fff0851cd49fff7d86cffffff00000000001ff97f0000000000000000

nord_face_younger_1 = 0x000000000000014104c200928801249200000000001d24100000000000000000
nord_face_young_1   = 0x000000044000014104c200928801249200000000001d24100000000000000000
nord_face_middle_1  = 0x000000084000014104c200928801249200000000001d24100000000000000000
nord_face_old_1     = 0x0000000e0000014104c200928801249200000000001d24100000000000000000
nord_face_older_1   = 0x0000000e0000014004c200928801249200000000001d24100000000000000000

nord_face_younger_2 = 0x000000002b00218a5bfcbdbb67b7ff7f00000000001eeb6f0000000000000000
nord_face_young_2   = 0x000000036b00234a5bfcbdbb67b7ff7f00000000001eeb6f0000000000000000
nord_face_middle_2  = 0x00000007eb00234a5bfcbdbb67b7ff7f00000000001eeb6f0000000000000000
nord_face_old_2     = 0x0000000deb00234a5bfcbdbb67b7ff7f00000000001eeb6f0000000000000000
nord_face_older_2   = 0x0000000feb0023465bfcbdbb67b7ff7f00000000001eeb6f0000000000000000

rhodok_face_younger_1 = 0x0000000009002003140000000000000000000000001c80400000000000000000
rhodok_face_young_1   = 0x0000000449002003140000000000000000000000001c80400000000000000000
rhodok_face_middle_1  = 0x0000000849002003140000000000000000000000001c80400000000000000000
rhodok_face_old_1     = 0x0000000cc9002003140000000000000000000000001c80400000000000000000
rhodok_face_older_1   = 0x0000000fc9002003140000000000000000000000001c80400000000000000000

rhodok_face_younger_2 = 0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_young_2   = 0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_middle_2  = 0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_old_2     = 0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_older_2   = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000

man_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
man_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
man_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
man_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
man_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

man_face_younger_2 = 0x000000003f0052064deeffffffffffff00000000001efff90000000000000000
man_face_young_2   = 0x00000003bf0052064deeffffffffffff00000000001efff90000000000000000
man_face_middle_2  = 0x00000007bf0052064deeffffffffffff00000000001efff90000000000000000
man_face_old_2     = 0x0000000bff0052064deeffffffffffff00000000001efff90000000000000000
man_face_older_2   = 0x0000000fff0052064deeffffffffffff00000000001efff90000000000000000

merchant_face_1    = man_face_young_1
merchant_face_2    = man_face_older_2

woman_face_1    = 0x0000000000000001000000000000000000000000001c00000000000000000000
woman_face_2    = 0x00000003bf0030067ff7fbffefff6dff00000000001f6dbf0000000000000000

european_woman_face_1	= 0x00000000000180014b5c0e2aa38d68d200000000001da7340000000000000000
european_woman_face_2	= 0x00000004bf0eb0073aa151d8dc792a9400000000001ee8e30000000000000000

swadian_woman_face_1 = 0x0000000180102006124925124928924900000000001c92890000000000000000
swadian_woman_face_2 = 0x00000001bf1000061db6d75db6b6dbad00000000001c92890000000000000000

khergit_woman_face_1 = 0x0000000180103006124925124928924900000000001c92890000000000000000
khergit_woman_face_2 = 0x00000001af1030025b6eb6dd6db6dd6d00000000001eedae0000000000000000

refugee_face1 = woman_face_1
refugee_face2 = woman_face_2
girl_face1    = woman_face_1
girl_face2    = woman_face_2

mercenary_face_1 = 0x0000000000000000000000000000000000000000001c00000000000000000000
mercenary_face_2 = 0x0000000cff00730b6db6db6db7fbffff00000000001efffe0000000000000000

vaegir_face1  = vaegir_face_young_1
vaegir_face2  = vaegir_face_older_2

bandit_face1  = man_face_young_1
bandit_face2  = man_face_older_2

undead_face1  = 0x00000000002000000000000000000000
undead_face2  = 0x000000000020010000001fffffffffff

arab_face_1 = 0x00000001ba04658646ed6fb6796a389a00000000001f681d0000000000000000
arab_face_2 = 0x000000018f00614a364b8ab5a3ae36d400000000001e3aa30000000000000000

arab_face_3 = 0x00000001ac0462483519af28b4b0d95300000000001ee3250000000000000000
arab_face_4 = 0x00000001bc006580365c15494dc646f100000000001db6530000000000000000

berber_face_1 = 0x000000000000710004820c24204c000200000000001d16100000000000000000
berber_face_2 = 0x00000007bf00728049fefe393fffc7ff00000000001ef96f0000000000000000

berber_face_3 = 0x000000040000710004820c24204c000200000000001d16100000000000000000
berber_face_4 = 0x0000000e3f00728049fefe393fffc7ff00000000001ef96f0000000000000000

euro_face_1 = 0x000000018d0c001058dca4bb5275b62300000000001dd8e60000000000000000
euro_face_2 = 0x000000018a08400966ee89d72584cb6100000000001cdaac0000000000000000

euro_face_3 = 0x000000019604001013597225acaf3b3400000000001ea79a0000000000000000
euro_face_4 = 0x00000001bf0c45c94add8a592445cb2400000000001e32b30000000000000000

latin_face_1 = 0x000000000000400a000000000000000000000000000000000000000000000000
latin_face_2 = 0x0000000cff00400b6db6db6db7fbffff00000000001efffe0000000000000000

west_euro_face_1  = west_euro_face_young_1
west_euro_face_2  = west_euro_face_older_2

swadian_face_face_1  = swadian_face_younger_1
swadian_face_face_2  = swadian_face_older_2

italian_face_1   = 0x0000000500003141355355370861008200000000001c96520000000000000000
italian_face_2  = 0x000000083e0040c649fc9e6f54b6dbbf00000000001d7b270000000000000000

lorien_elf_face_1      = 0x0000000ec0001007256d3159348da69300000000001d36b40000000000000000
lorien_elf_face_2      = 0x000000001400000836dd51589c88a69300000000001cd9340000000000000000
mirkwood_elf_face_1    = 0x000000000000014148ed6e47238dd70d00000000001d36f30000000000000000
mirkwood_elf_face_2    = 0x0000000df200314914ed6e45238e498e00000000001d38e10000000000000000
dwarf_face_1           = 0x00000001a3002083375c6eddad6db6db00000000001db7230000000000000000
dwarf_face_2           = 0x0000000aff005104069d91bd2c6dbada00000000001db6e90000000000000000
dwarf_face_3           = 0x0000000180001103375c6eddad6db6db00000000001db7230000000000000000
dwarf_face_4           = 0x00000005ea001183069b926d2c6dbada00000000001d29690000000000000000
dwarf_face_5           = 0x00000005ff002204069a936d2c6dbada00000000001d29510000000000000000
dwarf_face_6           = 0x0000000fff0020c3069a936d2c6dbada00000000001d29510000000000000000
dwarf_face_7           = 0x0000000fff002004069a936d2c6dbada00000000001d29510000000000000000

#NAMES:
#

troops = [
["player","Player","Player",tf_hero|tf_unmoveable_in_party_window,no_scene,reserved,fac_player_faction,[itm_mule],str_7|agi_5|int_4|cha_4,wp(15),0,0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
["multiplayer_profile_troop_male","multiplayer_profile_troop_male","multiplayer_profile_troop_male", tf_hero|tf_guarantee_all, 0, 0,fac_commoners,[itm_leather_jerkin,itm_leather_boots],0,0,0,0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
["multiplayer_profile_troop_female","multiplayer_profile_troop_female","multiplayer_profile_troop_female", tf_hero|tf_female|tf_guarantee_all, 0, 0,fac_commoners,[itm_tribal_warrior_outfit,itm_leather_boots],0,0,0,0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
["temp_troop","Temp Troop","Temp Troop",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
##  ["game","Game","Game",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
##  ["unarmed_troop","Unarmed Troop","Unarmed Troops",tf_hero,no_scene,reserved,fac_commoners,[itm_arrows,itm_short_bow],def_attrib|str_14,0,knows_common|knows_power_draw_2,0],

####################################################################################################################
# Troops before this point are hardwired into the game and their order should not be changed!
####################################################################################################################
["find_item_cheat","find_item_cheat","find_item_cheat",tf_hero|tf_is_merchant,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
["random_town_sequence","Random Town Sequence","Random Town Sequence",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
["tournament_participants","Tournament Participants","Tournament Participants",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
["tutorial_maceman","Maceman","Maceman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[itm_tutorial_club,itm_leather_jerkin,itm_hide_boots],str_6|agi_6|level(1),wp(50),knows_common,mercenary_face_1,mercenary_face_2],
["tutorial_archer","Archer","Archer",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,[itm_tutorial_short_bow,itm_tutorial_arrows,itm_linen_tunic,itm_hide_boots],str_6|agi_6|level(5),wp(100),knows_common|knows_power_draw_4,mercenary_face_1,mercenary_face_2],
["tutorial_swordsman","Swordsman","Swordsman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[itm_tutorial_sword,itm_leather_vest,itm_hide_boots],str_6|agi_6|level(5),wp(80),knows_common,mercenary_face_1,mercenary_face_2],

["novice_fighter","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[itm_hide_boots,itm_arena_tunic_red,itm_arena_tunic_blue,itm_arena_tunic_yellow],ranged_attrib_1|level(5),wp(60),knows_recruit,mercenary_face_1,mercenary_face_2],
["regular_fighter","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[itm_hide_boots,itm_mail_with_tunic_red,itm_mail_with_tunic_green],ranged_attrib_2|level(11),wp(90),knows_recruit|knows_ironflesh_1|knows_power_strike_1|knows_physique_1|knows_riding_1|knows_shield_2,mercenary_face_1,mercenary_face_2],
["veteran_fighter","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,0,fac_commoners,[itm_hide_boots,itm_mail_with_tunic_red,itm_mail_with_tunic_green],ranged_attrib_3|level(17),wp(110),knows_recruit|knows_ironflesh_3|knows_power_strike_2|knows_physique_2|knows_riding_2|knows_shield_3,mercenary_face_1,mercenary_face_2],
["champion_fighter","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[itm_hide_boots,itm_brigandine_red,itm_brigandine_blue,itm_brigandine_black,itm_brigandine_green],ranged_attrib_4|level(22),wp(140),knows_recruit|knows_ironflesh_4|knows_power_strike_3|knows_physique_3|knows_riding_3|knows_shield_4,mercenary_face_1,mercenary_face_2],

["arena_training_fighter_1","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[itm_hide_boots],foot_attrib_2|level(7),wp(100),knows_common|knows_ironflesh_1|knows_power_strike_1|knows_physique_1|knows_riding_1|knows_shield_2,mercenary_face_1,mercenary_face_2],
["arena_training_fighter_2", "Novice Fighter", "Novice Fighters", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_hide_boots], foot_attrib_2|level(9), wp(130), knows_common|knows_ironflesh_1|knows_horse_archery_1|knows_power_draw_1|knows_reserved_17_1|knows_physique_1|knows_riding_1, mercenary_face_1, mercenary_face_2 ],


["arena_training_fighter_3","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[itm_hide_boots],foot_attrib_3|level(11),wp(180),knows_billman_1|knows_horse_archery_2|knows_power_draw_2|knows_reserved_17_2|knows_riding_2, mercenary_face_1, mercenary_face_2 ],
["arena_training_fighter_4","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[itm_hide_boots],foot_attrib_3|level(13),wp(190),knows_pikeman_1|knows_horse_archery_5|knows_power_draw_2|knows_reserved_17_2|knows_riding_2, mercenary_face_1, mercenary_face_2 ],
["arena_training_fighter_5", "Regular Fighter", "Regular Fighters", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_hide_boots], foot_attrib_3|level(15), wp(200), knows_spearman_1|knows_horse_archery_2|knows_power_draw_2|knows_reserved_17_2|knows_riding_2, mercenary_face_1, mercenary_face_2 ],


["arena_training_fighter_6","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[itm_hide_boots],foot_attrib_4|level(17),wp(220),knows_billman_2|knows_horse_archery_3|knows_power_draw_3|knows_reserved_17_3|knows_riding_3,mercenary_face_1,mercenary_face_2],
["arena_training_fighter_7","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[itm_hide_boots],foot_attrib_4|level(19),wp(220),knows_spearman_2|knows_horse_archery_3|knows_power_draw_3|knows_reserved_17_3|knows_riding_3,mercenary_face_1,mercenary_face_2],
["arena_training_fighter_8","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[itm_hide_boots],foot_attrib_4|level(24),wp(250),knows_swordman_2|knows_horse_archery_3|knows_power_draw_3|knows_reserved_17_3|knows_riding_3,mercenary_face_1,mercenary_face_2],


["arena_training_fighter_9","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[itm_hide_boots],foot_attrib_5|level(28),wp(270),knows_swordman_3|knows_horse_archery_4|knows_power_draw_4|knows_reserved_17_4|knows_riding_5,mercenary_face_1,mercenary_face_2],
["arena_training_fighter_10","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[itm_hide_boots],foot_attrib_5|level(30),wp(300),knows_twohand_3|knows_horse_archery_4|knows_power_draw_4|knows_reserved_17_4|knows_riding_5,mercenary_face_1,mercenary_face_2],

["cattle","Cattle","Cattle",0,no_scene,reserved,fac_neutral, [], def_attrib|level(1),wp(60),0,mercenary_face_1, mercenary_face_2],


#soldiers:
#This troop is the troop marked as soldiers_begin
["farmer","Farmer","Farmers",tf_guarantee_armor,no_scene,reserved,fac_commoners,[itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots],def_attrib|level(4),wp(60),knows_common,man_face_middle_1,man_face_old_2],
  
["refugee","Refugee","Refugees",tf_female|tf_guarantee_armor,0,0,fac_commoners,[itm_knife,itm_pitch_fork,itm_sickle,itm_hatchet,itm_club,itm_dress,itm_robe,itm_woolen_dress,itm_headcloth,itm_woolen_hood,itm_wrapping_boots],def_attrib|level(1),wp(45),knows_common,refugee_face1,refugee_face2],
["peasant_woman","Peasant Woman","Peasant Women",tf_female|tf_guarantee_armor,0,0,fac_commoners,[itm_knife,itm_pitch_fork,itm_sickle,itm_hatchet,itm_club,itm_dress,itm_woolen_dress,itm_headcloth,itm_woolen_hood,itm_wrapping_boots],def_attrib|level(6),wp(40),knows_common,refugee_face1,refugee_face2],

["townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
  [
   itm_sword_medieval_a,itm_quarter_staff,itm_cartridges,itm_flintlock_pistol,itm_flintlock_pistol_2,
   itm_leather_cap,
   itm_gambeson,
   itm_woolen_hose,itm_nomad_boots,itm_blue_hose,itm_hide_boots,itm_ankle_boots,itm_leather_boots
  ],
  def_attrib|level(4),wp(60),knows_common,mercenary_face_1,mercenary_face_2],
  ["follower_woman","Camp Follower","Camp Follower",tf_female|tf_guarantee_all,0,0,fac_commoners,
   [itm_cartridges_burst,itm_carbine_old,itm_carbine,
    itm_nordic_shield,itm_hide_covered_round_shield,itm_hatchet,itm_hand_axe,itm_voulge,itm_fighting_pick,itm_club,itm_dress,itm_woolen_dress,itm_skullcap,itm_wrapping_boots],
   horse_attrib_1|level(12),wp(125)|wp_firearm(140),knows_common|knows_first_aid_2|knows_power_draw_2,refugee_face1,refugee_face2],
  ["hunter_woman","Huntress","Huntresses",tf_female|tf_guarantee_all,0,0,fac_commoners,
   [
    itm_cartridges_burst,itm_carbine_batarey,itm_carbine,
    itm_fur_covered_shield,itm_hide_covered_round_shield,
    itm_hatchet,itm_hand_axe,itm_voulge,itm_fighting_pick,itm_club,
    itm_leather_jerkin,itm_leather_vest,
    itm_skullcap,itm_leather_boots,
    itm_saddle_horse   
   ],
   horse_attrib_2|level(18),wp_melee(165)|wp_firearm(160),knows_horse_shoot_4|knows_first_aid_3|knows_crossbowman_2,refugee_face1,refugee_face2],
   
  ["fighter_woman","Camp Defender","Camp Defenders",tf_female|tf_mounted|tf_guarantee_all,0,0,fac_commoners,
   [
    itm_cartridges_burst,itm_carbine_batarey,itm_carbine_batarey_good,
    itm_plate_covered_round_shield,itm_tab_shield_small_round_c,
    itm_sword_khergit_2,itm_sword_khergit_3,
    itm_mail_with_tunic_green,itm_padded_leather,
    itm_guard_helmet,itm_bascinet_coif,
    itm_splinted_leather_greaves,
    itm_courser,itm_wisby_gauntlets_black
   ],
   horse_attrib_3|level(24),wp_melee(225)|wp_firearm(225),knows_horse_shoot_6|knows_first_aid_4|knows_crossbowman_4,refugee_face1,refugee_face2],
  ["sword_sister","Sword Sister","Sword Sisters",tf_female|tf_mounted|tf_guarantee_all,0,0,fac_commoners,
   [
    itm_cartridges_burst,itm_carbine_batarey_2shot,itm_carbine_batarey_good,
    #itm_sword_claymore_01,itm_sword_medieval_d_long,
    itm_sword_medieval_d_long,itm_steel_shield,
    itm_bnw_armour,itm_bnw_armour_green,itm_bnw_armour_german,
    itm_iron_greaves2,itm_steel_greaves,
    itm_sturmhaube_bnw1,
    itm_charger_old,
    itm_hourglass_gauntlets],
  horse_attrib_4|level(30),wp_melee(270)|wp_firearm(270),knows_horse_shoot_8|knows_first_aid_5|knows_crossbowman_6,refugee_face1,refugee_face2],

  ["watchman","Watchman","Watchmen",
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_culture_7,
   [
    itm_cartridges,
    itm_sword_medieval_a,itm_flintlock_pistol,itm_flintlock_pistol_2,
    itm_tab_shield_round_a,itm_tab_shield_round_b,
    itm_light_brigandine_red,itm_light_brigandine_black,itm_light_brigandine_blue,
    itm_mail_coif,itm_bascinet,
    itm_kettle_hat_3,itm_narf_hose
   ], 
  foot_attrib_2|level(12),wp(120), knows_light_swordman_1,mercenary_face_1,mercenary_face_2],
                      
           
  ["mercenary_swordsman","Mercenary Swordsman","Mercenary Swordsmen",
  tf_mounted|tf_guarantee_all_footman,0,0,fac_culture_7,
   [itm_bastard_sword_a,itm_bastard_sword_b,itm_sword_medieval_b,
    itm_tab_shield_heater_c,
    itm_light_brigandine_black_mail,itm_light_brigandine_red_mail,itm_light_brigandine_yellow_mail,itm_hose_kneecops_red,itm_mail_mittens,
    itm_zitta_bascinet,itm_zitta_bascinet_novisor,itm_kettle_hat_mail2,itm_kettle_hat_mail3],
   foot_attrib_4|level(18),wp(100),knows_light_swordman_2,mercenary_face_1, mercenary_face_2],
      
  ["hired_blade","Hired Blade","Hired Blades",
  tf_mounted|tf_guarantee_all_footman,0,0,fac_culture_7,
   [itm_bastard_sword_b,itm_bastard_sword_e,itm_bastard_sword_f,
    itm_tab_shield_heater_cav_a,itm_tab_shield_heater_d,
    itm_brigandine_plate_red,itm_corrazina_blue,itm_brigandine_plate_green,
    itm_corrazina_yellow,
    itm_iron_greaves,itm_plate_boots,
    itm_bascinet_coif,itm_visored_bascinet_1,itm_bascinet,itm_plate_mittens],
   foot_attrib_5|level(24),wp(130),knows_light_swordman_4,mercenary_face_1, mercenary_face_2],
            
  ["caravan_guard","Caravan Guard","Caravan Guards",
   tf_mounted|tf_guarantee_all_nomad,no_scene,0,fac_culture_7,
   [
    itm_light_lance,itm_cartridges,itm_flintlock_pistol,itm_flintlock_pistol_2,itm_flintlock_pistol_veteran,
    itm_fighting_pick,itm_sword_medieval_a,
    itm_tab_shield_round_b,itm_tab_shield_round_c,
    itm_light_brigandine_red,itm_light_brigandine_green,
    itm_light_brigandine_yellow,itm_light_brigandine_blue,itm_light_brigandine_black,
    itm_hose_kneecops_red,itm_padded_coif,itm_bascinet,itm_saddle_horse
   ],
   horse_attrib_1|level(15),wp(100),knows_swordman_1|knows_riding_2,mercenary_face_1,mercenary_face_2],
                              
  ["mercenary_horseman","Mercenary Horseman","Mercenary Horsemen",
   tf_mounted|tf_guarantee_all_lancer,0,0,fac_culture_7,
   [
    itm_lance,itm_heavy_lance,
    itm_bastard_sword_a,itm_sword_medieval_b,
    itm_tab_shield_heater_c,
    #itm_cuir_bouilli,itm_banded_armor,itm_coat_of_plates,
    
    itm_light_brigandine_red_mail,itm_light_brigandine_green_mail,
    itm_light_brigandine_yellow_mail,itm_light_brigandine_blue_mail,itm_light_brigandine_black_mail,
    itm_hose_kneecops_red,itm_hose_kneecops_green,
    #itm_splinted_leather_greaves,itm_splinted_greaves,
    itm_zitta_bascinet,itm_bascinet_coif,itm_zitta_bascinet_novisor,
    itm_hunter],
   horse_attrib_2|level(20),wp(120),knows_swordman_2|knows_riding_4,mercenary_face_1, mercenary_face_2],
   
  ["mercenary_cavalry","Mercenary Cavalry","Mercenary Cavalry",
   tf_mounted|tf_guarantee_all_lancer,0,0,fac_culture_7,
   [
    itm_heavy_lance,itm_great_lance,
    itm_bastard_sword_b,itm_sword_medieval_b,itm_tab_shield_heater_c,
    itm_knight_armor1,itm_knight_armor2,itm_knight_armor6,
    itm_knight_armor3,itm_knight_armor4,itm_knight_armor5,
    #itm_cuir_bouilli,itm_banded_armor,itm_coat_of_plates,itm_coat_of_plates_red,
    itm_plate_boots,itm_milanese_gauntlets,
    itm_knight_helmet1,itm_knight_helmet2,itm_knight_helmet3,
    itm_warhorse,itm_charger_old
   ],
   horse_attrib_3|level(25),wp(130),knows_swordman_4|knows_riding_5,mercenary_face_1, mercenary_face_2],
  ["musket_cavalry","Mercenary Cavalry","Mercenary Cavalry",
   tf_guarantee_all|tf_mounted,0,0,fac_culture_7,
   [
    itm_cartridges_burst,
    itm_flintlock_pistol_veteran_2,itm_flintlock_pistol_veteran_3,itm_flintlock_pistol_veteran,
    itm_bastard_sword_a,itm_tab_shield_heater_c,
    itm_red_armour_2,itm_blue_armour_2,itm_blue_armour_2,
    itm_red_armour_2,itm_german_armour_2,itm_german_armour_2,
    #itm_brigandine_black,
    itm_cav_boots,
    itm_sturmhaube_w1,itm_sturmhaube_w2,
    itm_hunter,itm_hunter
   ],
   horse_attrib_2|level(23),wp_one_handed(110)|wp_two_handed(110)|wp_firearm(150),knows_firearm_4|knows_horse_archery_6,mercenary_face_1,mercenary_face_2],
                                                            
  ["musket_hunter","musket_hunter","musket_hunter",
   tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_culture_7,
   [itm_cartridges,itm_samopal,itm_carbine_old,
    itm_sword_medieval_a,
    itm_red_gambeson,itm_green_gambeson,itm_yellow_gambeson,
    itm_ankle_boots,itm_leather_cap,itm_wrapping_boots],    
   def_attrib|level(12),wp(120)|wp_firearm(150),knows_firearm_1,mercenary_face_1,mercenary_face_2],
  ["musket_man","musket_man","musket_man",
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_culture_7,
   [
    itm_sword_medieval_a,itm_good_musket,itm_carbine_batarey,itm_good_musket,itm_cartridges_thrust,itm_cartridges,
    itm_beret_plain_brown,itm_beret_plain_red,
    itm_breastplate_red,itm_breastplate_blue,
    itm_breastplate_green,itm_breastplate_german,    

    itm_leather_boots,itm_splinted_leather_greaves
   ],
   foot_attrib_4|level(18),wp_one_handed (100) | wp_firearm (180) ,knows_firearm_2,mercenary_face_1,mercenary_face_2],
  ["musket_line_infantry", "musket_line_infantry", "musket_line_infantry", 
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves, 0, 0, fac_culture_7, 
   [
    itm_beret_plumes_brown,itm_beret_plumes_red,itm_combed_morion,
    
    itm_breastplate_red,itm_breastplate_blue,
    itm_breastplate_green,itm_breastplate_german,    
    itm_splinted_leather_greaves,itm_splinted_leather_greaves,
    itm_cartridges,itm_cartridges_thrust,itm_carbine_batarey_2shot,itm_mushket_udarniy,itm_rapierd
   ], 
   foot_attrib_4|level(24), wp_one_handed(140)|wp_firearm(250), knows_firearm_4,mercenary_face_1,mercenary_face_2 ],

  ["musket_line_infantry_2", "musket_adv_line_infantry", "musket_adv_line_infantry", 
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves, 0, 0, fac_culture_7, 
   [itm_cartridges,itm_cartridges_thrust,
    itm_red_armour_2,itm_german_armour_2,
    itm_blue_armour_2,
    itm_combed_morion,
    itm_splinted_leather_greaves,itm_splinted_leather_greaves,
    itm_eoro_musket,itm_rapierd], 
    foot_attrib_4|level(30), wp_one_handed(140)|wp_polearm(140)|wp_firearm(280), knows_firearm_5,mercenary_face_1,mercenary_face_2 ],


  ["saracen_cav_1","Saracen Cavalry","Saracen Cavalrys",
   tf_mounted|tf_guarantee_all, 0, 0, fac_kingdom_9,
  [
      itm_light_lance,itm_lance,
      itm_scimitar_b,itm_arabian_sword_b,
      itm_sarranid_cavalry_sword,
      itm_tab_shield_small_round_a,itm_tab_shield_small_round_b,
      itm_sarranid_mail_coif,
      itm_sarranid_leather_armor,itm_sarranid_cavalry_robe,
      itm_sarranid_boots_c,itm_sarranid_boots_b,
      itm_courser_steppe],
   horse_attrib_1|level(18),wp(120), knows_horse_shoot_5|knows_infantry_2,arab_face_1, arab_face_2],

  ["saracen_cav_2","Saracen Lancer","Saracen Lancers",
   tf_mounted|tf_guarantee_all, 0, 0, fac_kingdom_9,
   [
      itm_chaos_lance_1,itm_lance,
      itm_sarranid_cavalry_sword,itm_scimitar_b,
      itm_sarranid_mail_shirt_2,itm_sarranid_mail_shirt_3,
      itm_sarranid_horseman_helmet,itm_sarranid_boots_b,itm_sarranid_boots_c,itm_leather_gloves,
      itm_tab_shield_small_round_b,itm_tab_shield_small_round_c,
      itm_hunter_steppe],
   horse_attrib_2|level(24),wp_melee(150)|wp_throwing (110), knows_horse_shoot_7|knows_infantry_3,arab_face_1, arab_face_2],

  ["bedouin_camel_gunnner","Bedouin Camel gunnner","Bedouin Camel gunnners",
   tf_mounted|tf_guarantee_all, 0, 0, fac_culture_6,
   [itm_cartridges_burst,itm_samopal,itm_carbine_old,
    itm_arabian_sword_a,itm_arabian_sword_b,itm_scimitar_b,
    itm_leather_covered_round_shield,itm_leather_covered_round_shield,
    itm_skirmisher_armor,itm_arabian_armor_b,itm_arabian_armor_b,itm_sarranid_cavalry_robe,
    itm_sarranid_boots_a,itm_desert_turban,
    itm_camel,itm_camel2,itm_camel3], 
   horse_attrib_2|level(20), wp(100)|wp_firearm(150), knows_horse_shoot_5|knows_ranger_4, khergit_face_young_1,khergit_face_old_2],

  ["mercenary_balkan_cav","Albanian Cavalry","Albanian Cavalry",
   tf_mounted|tf_guarantee_all,0,0,fac_kingdom_8,
   [
    itm_double_sided_lance_long,itm_mace_redhandle,
    itm_hussar_hat,itm_hussar_hat,
    itm_red_pikiner_uniform_2,itm_red_pikiner_uniform,
    itm_khergit_leather_boots,itm_rus_cav_boots,
    itm_shield_otto1,itm_shield_otto2,
    itm_courser_steppe,itm_steppe_horse,itm_hunter_steppe
    ],
   horse_attrib_2|level(20),wp_melee(130),knows_riding_9|knows_light_swordman_4,swadian_face_young_1, swadian_face_old_2],
  ["we_noble_lad","West Euro Noble Lad","West Euro Noble Lads",
  tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_culture_1,
   [itm_lance,itm_fighting_pick,itm_bastard_sword_a,itm_sword_medieval_a,itm_tab_shield_heater_cav_a, itm_light_crossbow, itm_steel_bolts,
    itm_mail_with_tunic_red,itm_gon_squire,itm_light_brigandine_black,itm_byrnie,itm_haubergeon,itm_light_brigandine_green_mail,
    itm_ankle_boots,itm_mail_coif,itm_bascinet,itm_courser,itm_hunter],
   horse_attrib_1|level(13),wp_melee(80),knows_knight_1|knows_infantry_1,swadian_face_young_1, swadian_face_old_2],

  ["dis_knight_1","Mercenary halberd","Mercenary halberd",
  tf_mounted|tf_guarantee_all_wo_horse,0,0,fac_culture_1,
   [
    itm_german_poleaxe_2,itm_german_poleaxe_1,
    itm_heavy_crossbow,itm_steel_bolts,
    itm_early_transitional_e1,itm_light_mail_and_plate,
    itm_early_transitional_hre,itm_early_transitional_f1,
    itm_early_transitional_heraldic,
    itm_mail_boots,itm_mail_chausses,itm_mail_mittens,
    
    itm_bascinet_2,itm_bascinet_coif,itm_horned_great_helmet
   ],
   foot_attrib_4|level(18),wp(100),knows_precise_shot_2|knows_twohand_2,swadian_face_young_1, swadian_face_old_2],
                        
                                                
  ["dis_knight_2","Mercenary armor halberd","Mercenary armor halberd",
  tf_mounted|tf_guarantee_all_wo_horse,0,0,fac_culture_1,
   [itm_german_poleaxe_3,itm_bec_de_corbin_a,
    itm_sniper_crossbow,itm_steel_bolts,
    itm_half_plates,itm_half_plates_red_2,itm_half_plates_yello,
    itm_half_plates_green,itm_half_plates_blue,
    itm_iron_greaves,itm_plate_boots,
    itm_horned_great_helmet,itm_hounskull_3,itm_hounskull_2,itm_plate_mittens],
   foot_attrib_5|level(24),wp(130),knows_precise_shot_4|knows_twohand_4,swadian_face_young_1, swadian_face_old_2],


  ["mercenary_berserker", "mercenary Berserker", "mercenary Berserker", 
   tf_guarantee_all_footman, 0, 0, fac_kingdom_10, 
   [
    itm_tab_shield_round_d,
    itm_long_axe_alt,itm_long_axe_b_alt,itm_long_axe_c_alt,
    itm_throwing_spears,itm_throwing_spears,
    itm_byrnie_3,itm_mail_hauberk_3,itm_mail_hauberk_2,
    itm_splinted_leather_greaves,
    itm_nordic_warlord_helmet,
    itm_nordic_huscarl_helmet
   ], 
   foot_attrib_5|level(25), wp_melee(180)|wp_throwing(150), knows_billman_5|knows_power_throw_5|knows_physique_10, nord_face_middle_1, nord_face_older_2 ],

  ["god_choosen_berserker", "God_Choosen Berserker", "God_Choosen Berserker", 
   tf_guarantee_all_footman, 0, 0, fac_kingdom_10, 
   [
    itm_throwing_spears,itm_nord_javelin,itm_throwing_spears,
    itm_tab_shield_round_e,
    itm_greataxe_adjudgment,itm_double_axe,
    itm_huscarl_armor,itm_huscarl_armor_2,
    itm_iron_greaves,itm_plate_mittens,
    itm_nord_berserker_helmet,
    itm_nord_berserker_mask,
    itm_sg_orange_small
   ], 
   horse_attrib_6|level(35), wp_melee(240)|wp_throwing(250), knows_billman_7|knows_power_throw_6|knows_physique_10, nord_face_middle_1, nord_face_older_2 ],
                        
  ["mercenary_axeman", "mercenary Huscarl", "mercenary Huscarl", 
   tf_guarantee_all_footman, 0, 0, fac_kingdom_10, 
   [itm_throwing_spears,itm_tab_shield_round_e,itm_one_handed_battle_axe_c,itm_long_axe_c,itm_double_axe,
    itm_nordic_huscarl_helmet,itm_nordic_warlord_helmet,itm_banded_armor,itm_mail_boots,itm_mail_chausses,itm_mail_mittens],
   foot_attrib_5|level(28), wp_melee(170)|wp_throwing(180), knows_leader|knows_thrown_5, nord_face_middle_1, nord_face_older_2 ],

  ["hand_gunner","hand_gunner","hand_gunner",
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_culture_7,
   [
    itm_musket_hand_gun,itm_cartridges_burst,
    itm_tab_shield_pavise_d,
    itm_one_handed_battle_axe_b,
    itm_leather_gloves,itm_leather_boots,
    itm_bnw_armour,itm_bnw_armour_red,
    itm_open_sallet_coif,itm_sallet_coif
    ],
   foot_attrib_4|level(28),wp_melee (140)|wp_firearm (180),knows_swordman_3,mercenary_face_1,mercenary_face_2],

  ["me_hand_gunner","Greek Firethrower","Greek Firethrower",
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_culture_6,
   [
    itm_drawf_flame_caster,itm_drawf_flame_caster,
    itm_cartridges_flame,itm_cartridges_flame,
    itm_sword_khergit_3,itm_sword_khergit_2,
    itm_leather_gloves,itm_rus_splint_greaves,itm_rus_splint_greaves,
    itm_rus_lamellar_b,itm_rus_lamellar_c,itm_rus_lamellar_a,
    itm_tagancha_helm_a,itm_tagancha_helm_b
    ],
   foot_attrib_4|level(40),wp_melee (170)|wp_firearm (180),knows_spearman_4,mercenary_face_1,mercenary_face_2],


  ["merchant_cavalry_militia","Merchant Cavalry Militia","Merchant Cavalry Militia",
   tf_mounted|tf_guarantee_all,0,0,fac_culture_7,
   [itm_heavy_lance,itm_sword_medieval_c,itm_tab_shield_heater_d,
   
    itm_light_brigandine_red_mail,itm_light_brigandine_green_mail,itm_light_brigandine_blue_mail,
    itm_hose_kneecops_red,itm_hose_kneecops_green,itm_zitta_bascinet,
    #itm_half_plates,itm_iron_greaves2,itm_hounskull,
    itm_hourglass_gauntlets_ornate,itm_hunter,itm_courser,itm_hunter],
   def_attrib|level(20),wp(100),knows_riding_4|knows_infantry_4,mercenary_face_1,mercenary_face_2],
   
  ["musket_ranger", "musket_ranger", "musket_ranger", 
   tf_guarantee_all, 0, 0, fac_culture_7, 
   [itm_cartridges_thrust,
    itm_red_armour_3,itm_german_armour_3,itm_blue_armour_3,
    itm_combed_morion,itm_marksman_gloves,
    itm_splinted_leather_greaves,itm_splinted_leather_greaves,
     itm_musket_rifle,itm_rapierd], 
    horse_attrib_5|level(45), wp_one_handed(300)|wp_polearm(300)|wp_firearm(500), knows_precise_shot_10|knows_physique_9|knows_shield_4|knows_power_strike_9|knows_ironflesh_5|knows_weapon_master_8|knows_stealth_10|knows_magic_defence_4,mercenary_face_1,mercenary_face_2 ],
      
      
    
  ["monk","Monk","Monk",
   tf_guarantee_all_wo_horse,0,0,fac_culture_7,
   [itm_wooden_staff_1,itm_magic_burning_gaze,

    itm_priest_robe_1,itm_priest_1_boots,itm_black_hood,

   ],
    horse_attrib_1|level(20), wp_melee(20)|wp_polearm(200)|wp_firearm(200), knows_magic_1,nord_face_young_1, nord_face_old_2],
    
  ["clerics", "Clerics", "Clerics ", 
   tf_guarantee_all_wo_horse, 0, 0, fac_culture_7, 
   [
    itm_bishop_staff,itm_magic_burning_gaze,

    itm_priest_robe_2,itm_priest_robe_2,itm_priest_cap_1,
    itm_priest_2_boots,

   ], 
    horse_attrib_2|level(30), wp_melee(30)|wp_polearm(150)|wp_firearm(300), knows_magic_3,vaegir_face_young_1, vaegir_face_middle_2],
    
  ["priest", "Priest", "Priest ", 
   tf_guarantee_all, 0, 0, fac_culture_7, 
   [
    itm_bishop_staff_2,itm_magic_burning_gaze,
    itm_priest_robe_3,itm_priest_robe_3,itm_bishop_mitre,
    itm_priest_2_boots,itm_sg_yellow_small,itm_courser
   ], 
    horse_attrib_3|level(40), wp_melee(40)|wp_polearm(140)|wp_firearm(400), knows_magic_6|knows_horse_shoot_3,swadian_face_young_1,swadian_face_old_2],

  ["healer", "Healer", "Healer ", 
   tf_guarantee_all_wo_horse,0,0,fac_culture_7,
   [itm_bishop_staff_2,itm_magic_blinding_light,
    itm_war_clerics_warhammer_cast_2,
    itm_bishop_armour,itm_bishop_great_helm,itm_wisby_gauntlets_black,itm_mail_boots,
    itm_bishop_armour,itm_bishop_great_helm,itm_wisby_gauntlets_black,itm_mail_boots,
    #itm_surgeon,itm_priest_2_boots,
    itm_sg_yellow_small
   ],
    horse_attrib_5|level(50), wp_melee(250)|wp_polearm(200)|wp_firearm(400), knows_infantry_7|knows_magic_power_7|knows_magic_defence_9|knows_magic_skill_10,rhodok_face_young_1, rhodok_face_old_2],
      


 ["manhunter","Manhunter","Manhunters",
 tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_commoners,
   [itm_mace_3,itm_winged_mace,itm_nasal_helmet,
    itm_aketon,itm_light_brigandine_red_mail,itm_light_brigandine_blue_mail,
    itm_wooden_shield,itm_narf_hose,itm_narf_hose,itm_sumpter_horse],
 foot_attrib_2|level(10),wp(70),knows_light_swordman_1|knows_riding_1,bandit_face1,bandit_face2],
 
 ["slave_driver","Slave Driver","Slave Drivers",
 tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_commoners,
  [itm_club_with_spike_head,itm_mail_coif,itm_nordic_shield,itm_winged_mace,
   itm_leather_gloves,itm_hose_kneecops_red,itm_hose_kneecops_green,itm_steppe_horse,
   itm_light_brigandine_red,itm_light_brigandine_blue,itm_light_brigandine_yellow,itm_light_brigandine_green
  ],
   foot_attrib_3|level(15),wp(100),knows_riding_2|knows_light_swordman_1,bandit_face1, bandit_face2],
 
 ["slave_hunter","Slave Hunter","Slave Hunters",
  tf_mounted|tf_guarantee_all_wo_ranged ,0,0,fac_commoners,
  [
   itm_winged_mace,itm_maul,itm_sledgehammer,itm_spiked_mace,
   itm_bascinet_coif,itm_bascinet_2,itm_zitta_bascinet_novisor,
   itm_brigandine_red,itm_brigandine_blue,itm_brigandine_black,itm_brigandine_green,
  itm_tab_shield_round_c,itm_tab_shield_round_d,itm_mail_chausses,itm_splinted_leather_greaves,itm_leather_gloves,itm_courser,itm_hunter],
  horse_attrib_1|level(20),wp(130),knows_riding_4|knows_light_swordman_3,bandit_face1,bandit_face2],
 ["slaver_chief","Slaver Chief","Slaver Chiefs",
  tf_mounted|tf_guarantee_all,0,0,fac_commoners,
  [itm_military_hammer,itm_warhammer,
   itm_brigandine_plate_red,itm_corrazina_blue,itm_brigandine_plate_green,
   itm_steel_shield,itm_scale_gauntlets,itm_mail_mittens,itm_bascinet_coif,itm_plate_boots,itm_mail_boots,itm_warhorse,itm_cartridges,itm_flintlock_pistol_elite
  ],
  horse_attrib_3|level(25),wp(160),knows_precise_shot_4|knows_light_swordman_4|knows_riding_4,bandit_face1,bandit_face2],


#mercenary_leader
  ["slaver_captain","Slaver captain","Slaver captain",
   tf_mounted|tf_guarantee_all,0,0,fac_commoners,
  [itm_military_hammer,itm_warhammer,
   itm_plate_armor,itm_plate_armor_2,
   itm_steel_shield,itm_hourglass_gauntlets,itm_visored_bascinet_1,itm_steel_greaves,itm_warhorse,itm_cartridges_burst,itm_flintlock_pistol_elite],
  horse_attrib_4|level(30),wp(160),knows_precise_shot_6|knows_leader|knows_horse_shoot_6|knows_light_swordman_6,bandit_face1,bandit_face2],
  
  ["mercenary_lance","Mercenary Lance","Mercenary Lance",
 tf_mounted|tf_guarantee_all_lancer,0,0,fac_culture_7,
   [itm_sword_medieval_d_long,itm_gothic_lance,itm_great_lance,itm_morningstar,itm_morningstar2,itm_toumingdun,
    itm_knight_plate,itm_knight_plate,
    itm_plate_armor,itm_plate_armor_5,
    itm_plate_mittens,itm_milanese_gauntlets,itm_hourglass_gauntlets,
    itm_gothic_plate_nobevor,itm_plate_boots,itm_french_helm_closed,itm_classichelm_plume,itm_french_helm_closed,itm_charger_noble],
   horse_attrib_4|level(30),wp(160),knows_riding_6|knows_swordman_5,mercenary_face_1,mercenary_face_2],
          
  ["adventurer","adventurer","adventurers",tf_guarantee_all,0,0,fac_kingdom_1,
   [
    itm_arbalest_2,itm_swadian_steel_bolts,
    itm_bastard_sword_b,itm_espada_eslavona_b,itm_side_sword,
    itm_tab_shield_pavise_c,itm_tab_shield_heater_cav_b,
    itm_half_plates_blue,itm_half_plates_blue,
    itm_iron_greaves,itm_iron_greaves2,
    itm_sturmhaube_w1,itm_sturmhaube_w2,itm_sturmhaube_w3,itm_sturmhaube_w4,
    itm_wisby_gauntlets_black
   ],
   horse_attrib_5|level(40),wp_melee(300)|wp_crossbow(350),knows_crossbowman_8|knows_first_aid_4,mercenary_face_1,mercenary_face_2],
            
  ["dis_knight_3","Mercenary Champion halberd","Mercenary Champion halberd",
    tf_mounted|tf_guarantee_all_wo_horse,0,0,fac_culture_1,
   [
    itm_sword_two_handed_c,itm_bec_de_corbin_a,itm_polehammer_threeprong,
    itm_arbalest_1,itm_swadian_steel_bolts,
    itm_knight_plate,itm_knight_plate_5,itm_knight_plate,
    itm_plate_mittens,itm_milanese_gauntlets,
    itm_iron_greaves,itm_steel_greaves,
    itm_new_sallet,itm_new_sallet_2,itm_milanese_sallet
   ],
   foot_attrib_6|level(30),wp(160),knows_precise_shot_6|knows_twohand_6, swadian_face_young_1, swadian_face_old_2],
                  
  ["champion_swordsman","Mercenary Champion swordsman","Mercenary Champion swordsman",
    tf_mounted|tf_guarantee_all_footman,0,0,fac_culture_7,
   [
    itm_sword_medieval_d_long,itm_bastard_sword_b,itm_bastard_sword_e,itm_bastard_sword_f,
    itm_tab_shield_heater_cav_b,itm_tab_shield_heater_d,
    itm_plate_armor_4,itm_plate_armor,itm_plate_armor_5,
    itm_plate_mittens,itm_milanese_gauntlets,
    itm_plate_boots,itm_steel_greaves,
    itm_visored_bascinet_1,itm_visored_bascinet_2
   ],
   foot_attrib_6|level(30),wp(160),knows_light_swordman_7,mercenary_face_1,mercenary_face_2],
   
            
  ["pistol_cavalry","pistol_cavalry","pistol_cavalry",
    tf_mounted|tf_guarantee_all,0,0,fac_culture_7,
  [
   itm_flintlock_pistol_elite_1,itm_flintlock_pistol_elite_2,
   #itm_flintlock_pistol_4s,itm_flintlock_pistol_2s,
   itm_cartridges_burst,itm_bastard_sword_f,itm_cartridges_burst,
   itm_tab_shield_heater_d,
   
    itm_red_armour_5,itm_blue_armour_5,
    #itm_red_armour_5,itm_german_armour_5,
   
   itm_bnw_splinted_greaves,itm_bnw_gauntlets,
   itm_sturmhaube_w3,itm_sturmhaube_w4,
   itm_charger_old],
   horse_attrib_3|level(30),wp_melee(150)|wp_firearm(250),knows_firearm_5|knows_horse_archery_7,mercenary_face_1, mercenary_face_2],
            
  ["mercenary_pavise_crossbow_captain","Mercenary pavise_crossbow","Mercenary pavise_crossbow",
   tf_guarantee_all_wo_horse,0,0,fac_culture_2,
   [
    itm_bonecrossbow_auto,itm_swadian_steel_bolts,itm_swadian_steel_bolts,
    itm_ebony_long_sword,itm_ebony_long_mace,
    itm_tab_shield_pavise_d,itm_tab_shield_pavise_d,
    itm_heraldic_harness,
    itm_sallet_coif,itm_open_sallet_coif,itm_iron_greaves,itm_iron_greaves2,itm_marksman_gloves
   ],
   horse_attrib_5|level(50),wp_melee(300)|wp_crossbow(400),knows_precise_shot_10|knows_physique_8|knows_shield_10|knows_power_strike_9|knows_ironflesh_8|knows_weapon_master_8|knows_stealth_8|knows_magic_defence_5,italian_face_1,italian_face_2],
#mercenary_leader


  ["mercenary_elite_axeman", "mercenary Plate Armour Huscarl", "mercenary Plate Armour Huscarl", 
   tf_guarantee_all_footman, 0, 0, fac_kingdom_10, 
   [
    itm_nord_javelin,itm_nord_javelin,
    itm_stalhrim_sword,itm_nordhero_sword_long,itm_stahlrim_battleaxe,
    #itm_nordhero_greatsword_2,itm_nordhero_long_axe,
    #itm_stalhrim_greatsword,
    itm_black_shield,itm_black_shield,
    itm_nord_knight_plate,itm_nord_knight_plate,itm_gothic_plate_2,
    itm_nord_plate_boots,itm_plate_mittens,itm_great_helmet3,itm_great_helmet3,itm_trophy_b,itm_sg_orange_small,
   ], 
   str_70|agi_70|int_12|cha_12|level(45), wp_melee(350)|wp_throwing(350), knows_physique_10|knows_shield_6|knows_power_strike_10|knows_ironflesh_10|knows_weapon_master_8|knows_power_throw_10|knows_magic_defence_10|knows_magic_power_3, nord_face_middle_1, nord_face_older_2 ],

 ["naffatun", "Naffatun", "Naffatun",tf_guarantee_all,0,0,fac_culture_6,
  [itm_nahptha_bomb,itm_arabian_sword_b,itm_tab_shield_small_round_c,itm_arabian_armor_b,itm_sarranid_boots_c,itm_sarranid_boots_b,itm_sarranid_mail_coif],
  foot_attrib_5|level(24),wp_melee(100)|wp_throwing (200),knows_leader|knows_thrown_4,arab_face_3, arab_face_4],

  ["sarranid_assasin", "Battlefield Assasin", "Battlefield Assasins",tf_guarantee_all_footman, 0, 0, fac_culture_6, 
   [itm_sword_khergit_5,itm_tab_shield_small_round_c,itm_throwing_scimitar,
   #itm_throwing_star_a,
    itm_sarranid_boots_d,itm_sarranid_boots_c,
    itm_ninjia_armor,itm_assassin_mail_coif,
    itm_lamellar_gauntlets
    ], 
   horse_attrib_5|level(30), wp(200), knows_assasin_5|knows_power_throw_4, arab_face_3, arab_face_4 ],
  ["sarranid_assasin_2", " Armor Battlefield Assasin", "Armor Battlefield Assasins",tf_guarantee_all_wo_horse, 0, 0, fac_culture_6, 
   [itm_sword_khergit_7,itm_tab_shield_small_round_c,itm_granata_medium,
   #itm_throwing_star_a,
    #itm_werewolfclaw,itm_werewolfclaw_dual,
    itm_mask_of_blades,itm_mask_of_blades,
    itm_sarranid_boots_d,itm_lamellar_gauntlets,
    itm_armor8,itm_armor8,
    ], 
   horse_attrib_6|level(40), wp(350), knows_assasin_7|knows_power_throw_6, arab_face_3, arab_face_4 ],

  ["cannon_man", "cannon_man", "cannon_man", tf_guarantee_all_wo_horse, 0, 0, fac_culture_7, 
   [
     itm_cartridges_cannon,itm_cartridges_cannon_1,itm_sword_medieval_c,
     itm_hand_cannon,itm_hand_cannon,
     itm_hand_cannon_2,itm_hand_cannon_3,
     itm_bnw_armour_green,itm_bnw_armour,
     itm_sturmhaube_bnw2,itm_sturmhaube_bnw1,
     itm_bnw_splinted_greaves,itm_sg_human_big
    ],
   foot_attrib_5|level(40), wp_one_handed(140)|wp_firearm(200), knows_firearm_8,mercenary_face_1,mercenary_face_2 ],
        
   ["assassin", "assassin", "assassin", tf_guarantee_all_wo_horse, 0, 0, fac_commoners, 
    [itm_armor7,itm_armor7,itm_hide_boots,itm_hide_boots,itm_assasin_hood_2,itm_assasin_hood_4,
    itm_assassin_dagger,itm_dueling_dagger,itm_cartridges_thrust,itm_cartridges_thrust,itm_pistol_2stwol], 
    foot_attrib_4|str_20|agi_25|level(20), wp(180), knows_stealth_10|knows_ironflesh_8|knows_power_strike_10|knows_physique_10, bandit_face1, bandit_face2 ],


 ["ghazis_1","Ghazis","Ghazis",
  tf_guarantee_all_footman,0,0,fac_culture_6,
   [itm_battle_axe,itm_axe,
    itm_jarid,itm_arrows,itm_strong_bow,itm_nomad_bow,
    itm_tab_shield_small_round_a,
    itm_desert_turban,itm_sarranid_warrior_cap,
    itm_sarranid_leather_armor,itm_sarranid_boots_b
    ],
   foot_attrib_2|level(15),wp(100),knows_ranger_2|knows_power_throw_2,arab_face_1, arab_face_2],

 ["ghazis_2","Ghazis","Ghazis",
  tf_guarantee_all_wo_horse,0,0,fac_culture_6,
   [itm_battle_axe,itm_war_axe,
    itm_jarid,itm_bamboo_arrows,itm_strong_bow,itm_nomad_bow,
    itm_tab_shield_small_round_b,
    itm_sarranid_warrior_cap,itm_sarranid_warrior_cap,
    itm_sarranid_leather_armor,itm_sarranid_boots_b
    ],
   foot_attrib_3|level(20),wp(120),knows_ranger_3|knows_power_throw_2,arab_face_1, arab_face_2],

  ["me_mercenary_swordsman_1","Mercenary Saracen Swordsman","Mercenary Saracen Swordsmen",
  tf_guarantee_ranged|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_culture_6,
   [itm_arabian_sword_b,itm_arabian_sword_a,
    itm_tab_shield_small_round_c,
    itm_bamboo_arrows,itm_sword_khergit_3,itm_mace_4,itm_nomad_bow,itm_nomad_bow,itm_strong_bow,
    itm_arabian_armor_b,itm_sarranid_mail_shirt,itm_sarranid_mail_shirt_3,
    itm_mail_mittens,
    itm_sarranid_boots_c,itm_sarranid_boots_b, 
    itm_sarranid_horseman_helmet,itm_sarranid_mail_coif,itm_sarranid_helmet1],
   foot_attrib_4|level(24),wp(150),knows_ranger_3|knows_power_throw_4,mercenary_face_1, mercenary_face_2],

 ["turk_archer_3","Ottoman Infantry","Ottoman Infantry",
 tf_guarantee_ranged|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_9,
   [itm_bamboo_arrows,itm_one_handed_war_axe_b,itm_mace_woodenhandle,itm_khergit_long_bow,itm_tab_shield_small_round_c,
    itm_turk_mail_heavy,itm_sarranid_boots_c,itm_chichak1,itm_chichak2],
   foot_attrib_5|level(30),wp_melee(200)|wp_missile(200), knows_archer_6|knows_power_throw_6,euro_face_3, euro_face_4],
      

  ["mercenaries_end","mercenaries_end","mercenaries_end",
   tf_undead|tf_no_capture_alive|tf_guarantee_all_footman,0,0,fac_undeads_2,
   [
   
    itm_demon_head,itm_demon_foot,itm_demon_hand,itm_demon_body
   ],
   horse_attrib_4|level(30),wp(300),knows_ironflesh_6|knows_twohand_5|knows_magic_defence_10,mercenary_face_1,mercenary_face_2],
## CC

            

  ["france_prison_guard","Prison Guard","Prison Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_swiss_halberd,itm_pike,itm_bastard_sword_b,itm_morningstar,itm_sword_medieval_b,itm_tab_shield_heater_c,itm_half_plates_blue,itm_plate_boots,itm_hounskull,itm_milanese_sallet,itm_milanese_gauntlets],
   def_attrib|level(25),wp(130),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3|knows_magic_defence_10,west_euro_face_young_1, west_euro_face_old_2],
  ["france_castle_guard","Castle Guard","Castle Guards",tf_unmoveable_in_party_window|tf_allways_fall_dead|tf_guarantee_all_wo_horse,0,0,fac_kingdom_1,
   [itm_war_clerics_warhammer_cast_2,itm_magic_soul_quench,itm_magic_wind_blast,itm_magic_burning_gaze,itm_elf_twiligh_armor,itm_amade_bronze_greaves,itm_black_helmet_2,itm_amade_bronze_gauntlets],
   horse_attrib_4|level(35),wp(300),knows_spearman_6|knows_magic_power_5|knows_magic_defence_10|knows_magic_skill_10,west_euro_face_young_1, west_euro_face_old_2],
         
  ["khergit_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_sword_khergit_3,itm_tab_shield_small_round_b,itm_tab_shield_small_round_a,itm_lamellar_vest_khergit,itm_lamellar_armor,itm_khergit_leather_boots,itm_rus_splint_greaves,itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_leather_warrior_cap],
   def_attrib|level(24),wp(130),knows_physique_5|knows_shield_2|knows_ironflesh_5|knows_magic_defence_10,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_castle_guard","Castle Guard","Castle Guards", tf_unmoveable_in_party_window|tf_allways_fall_dead|tf_guarantee_all_wo_horse,0,0,fac_kingdom_3,
   [itm_ebony_bastard_sword,itm_ebony_scimitar_1,itm_ebony_long_mace,itm_undead_shield_kite_cav,
    itm_orcish_mutil_arrow,itm_orcish_mutil_arrow,itm_demon_arrow,itm_ebony_arrow_fireball_2,itm_karztev_bow,
   itm_vampire_armor_4,itm_black_knight_hand,itm_black_knight_foot,itm_black_helmet],
   horse_attrib_4|level(35),wp(300),knows_archer_7|knows_magic_power_7|knows_magic_defence_10,khergit_face_middle_1, khergit_face_older_2],
     
     
  ["england_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_ashwood_pike,itm_one_handed_war_axe_b,itm_fighting_axe,itm_one_handed_war_axe_b,itm_cuir_bouilli,itm_mail_chausses,itm_iron_greaves,itm_mail_coif,itm_nordic_helmet,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_physique_3|knows_shield_2|knows_ironflesh_3|knows_magic_defence_10,nord_face_middle_1, nord_face_older_2],
  ["england_castle_guard","Castle Guard","Castle Guards", tf_unmoveable_in_party_window|tf_allways_fall_dead|tf_guarantee_all_wo_horse,0,0,fac_kingdom_4,
   [itm_long_bow_3,itm_woodelf_mutil_arrows,itm_woodelf_arrows_amber_spear,itm_glass_arrow_paralysis_cloud,itm_warblade_greensilver,itm_black_shield,itm_dragon_plate,itm_dragon_foot,itm_dragon_head,itm_dragon_knight_hand],
   horse_attrib_6|level(35),wp(300),knows_archer_9|knows_magic_power_4|knows_magic_defence_10,nord_face_middle_1, nord_face_older_2],
     
  ["italian_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_swiss_halberd,itm_sword_medieval_c,itm_morningstar,itm_tab_shield_pavise_b,itm_open_sallet_coif,itm_corrazina_green,itm_mail_chausses,itm_iron_greaves,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_physique_3|knows_shield_2|knows_ironflesh_3|knows_magic_defence_10,italian_face_1, italian_face_2],
  ["italian_castle_guard","Castle Guard","Castle Guards", tf_undead|tf_unmoveable_in_party_window|tf_allways_fall_dead|tf_guarantee_all_wo_horse,0,0,fac_kingdom_5,
   [itm_undead_arrow_summon_undead,itm_undead_arrow_gaze_of_nagash,itm_black_bow,itm_mutil_arrow_2,itm_undead_sword_two_handed_2,itm_rhun_helm_5,itm_skeleton_armor_2,itm_black_greaves,itm_leather_gloves],
   horse_attrib_3|level(35),wp(300),knows_archer_5|knows_magic_power_5|knows_swordman_4|knows_magic_defence_10,italian_face_1, italian_face_2],

  ["german_prison_guard","Prison Guard","Prison Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_7,
   [itm_pike,itm_bastard_sword_f,itm_morningstar,itm_tab_shield_heater_c,itm_corrazina_yellow,itm_plate_boots,itm_new_sallet,itm_leather_gloves],
   def_attrib|level(25),wp(130),knows_common|knows_shield_3|knows_ironflesh_3|knows_magic_defence_10|knows_power_strike_3,swadian_face_face_1, swadian_face_face_2],
  ["german_castle_guard","Castle Guard","Castle Guards", tf_unmoveable_in_party_window|tf_allways_fall_dead|tf_guarantee_all_wo_horse,0,0,fac_kingdom_7,
   [itm_flamberge,itm_hand_cannon_3,itm_cartridges_burst,itm_cartridges_cannon_1,itm_bnw_armour_german,itm_bnw_splinted_greaves,itm_sturmhaube_bnw3,itm_bnw_gauntlets],
   horse_attrib_5|level(35),wp(300),knows_firearm_7|knows_knight_3|knows_magic_defence_10,swadian_face_face_1, swadian_face_face_2],
            
  ["vaegir_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_8,
   [itm_ashwood_pike,itm_battle_fork,itm_bardiche,itm_battle_axe,itm_fighting_axe,itm_tab_shield_kite_b,itm_ee_mail_hauberk_1,itm_ee_armor_4,itm_mail_chausses,itm_iron_greaves,itm_nordic_helmet,itm_nordic_helmet,itm_nordic_helmet,itm_spiked_helmet,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_physique_3|knows_shield_2|knows_ironflesh_3|knows_magic_defence_10,east_euro_face_middle_1, east_euro_face_older_2],
  ["vaegir_castle_guard","Castle Guard","Castle Guards", tf_unmoveable_in_party_window|tf_allways_fall_dead|tf_guarantee_all_wo_horse,0,0,fac_kingdom_8,
   [itm_cav_axe,itm_hand_cannon_4,itm_cartridges_cannon,itm_tab_shield_kite_d,itm_rus_scale,itm_mail_chausses,itm_iron_greaves,itm_beastarmour_head,itm_beastarmour_head,itm_leather_gloves],
   horse_attrib_4|level(35),wp(250),knows_billman_6|knows_magic_defence_10,east_euro_face_middle_1, east_euro_face_older_2],
      
  ["janissary_prison_guard","Prison Guard","Prison Guards", tf_demon_human|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_9,
   [itm_chaos_sword3,itm_sarranid_two_handed_axe_b,itm_chaos_warrior_shield,itm_rhun_armor_7,itm_chaos_gauntlets,itm_black_greaves,itm_rhun_helm_7],
   def_attrib|level(24),wp(130),knows_physique_5|knows_shield_2|knows_ironflesh_5|knows_magic_defence_10,khergit_face_middle_1, khergit_face_older_2],
      
  ["janissary_castle_guard","Castle Guard","Castle Guards", tf_demon_human|tf_unmoveable_in_party_window|tf_allways_fall_dead|tf_guarantee_all_wo_horse,0,0,fac_kingdom_9,
   [
    itm_sarranid_axe_b,itm_sarranid_mace_2,
    itm_karztev_bow,itm_karztev_bow,
    itm_demon_arrow,itm_ebony_mutil_arrow,itm_ebony_arrow_fireball_2,
    itm_rhun_armor_6_1,itm_rhun_armor_6_2,
    itm_imp_foot_2,itm_imp_head_4,itm_imp_hand_3
   ],
   horse_attrib_8|level(35),wp(300),knows_magic_power_5|knows_archer_9|knows_magic_defence_10,khergit_face_middle_1, khergit_face_older_2],
         
                  
  ["nord_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_10,
   [itm_ashwood_pike,itm_battle_fork,itm_long_axe_c_alt,itm_fighting_axe,itm_tab_shield_round_d,itm_half_plates_blue,itm_mail_chausses,itm_iron_greaves,itm_nordic_helmet,itm_nordic_helmet,itm_nordic_helmet,itm_spiked_helmet,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_physique_3|knows_shield_2|knows_ironflesh_3|knows_magic_defence_10,nord_face_middle_1, nord_face_older_2],
  ["nord_castle_guard","Castle Guard","Castle Guards", tf_unmoveable_in_party_window|tf_allways_fall_dead|tf_guarantee_all_wo_horse,0,0,fac_kingdom_10,
   [itm_nord_bow_3,itm_stahlrim_arrow_deadly_cold,itm_stahlrim_mutil_arrow,itm_stahlrim_arrow_frozen_orb,
    itm_stalhrim_greatsword,itm_stahlrim_battleaxe,
    itm_nord_knight_plate,itm_nord_knight_plate,
    itm_nord_plate_boots,itm_nord_plate_boots,
    itm_great_helmet3,itm_great_helmet3,
    itm_leather_gloves
    ],
   str_70|agi_70|int_12|cha_12|level(35),wp(300),knows_physique_10|knows_shield_6|knows_power_strike_10|knows_ironflesh_10|knows_weapon_master_8|knows_power_draw_8|knows_magic_power_6|knows_magic_defence_10,nord_face_middle_1, nord_face_older_2],
      
  ["we_recruit","frozen Knight","frozen Knights",
   tf_guarantee_all_wo_ranged,0,0,fac_dark_knights,
   [
    itm_bingqishi,itm_bingqishi,
    itm_bingqishitui,itm_bingqishitui,
    itm_bingqishitoukui,itm_bingqishitoukui,
    itm_bingqishishou,itm_bingqishishou,
    itm_bingdun,itm_bingjian,
   ],
  str_70|agi_70|int_12|cha_12|level(50), wp_melee(350), knows_light_swordman_8|knows_stealth_10|knows_weapon_master_10, swadian_face_face_1, swadian_face_face_2 ],
      
      
 ["human_magic_4","frozen_Arch_Mage","frozen_Arch_Mage",
  tf_guarantee_ranged|tf_no_capture_alive|tf_guarantee_all_footman,0,0,fac_dark_knights,
   [
    itm_enchanter_staff_1,
    
    itm_magic_fireball,itm_magic_fireball,

    itm_magic_robe_4,itm_leather_boots,itm_wizard_hat_4,itm_trophy_c,itm_sg_human_big],
   foot_attrib_5|level(55),wp_melee(250)|wp_firearm(300),knows_magic_8,euro_face_3, euro_face_4],




  ["drowelf_recruit","Drow Elf Recruit","Drow Elf Recruit",
  tf_female_elf|tf_guarantee_all_wo_horse,0,0,fac_beast,
   [
    itm_steel_bolts,itm_steel_bolts,itm_light_crossbow,
    itm_ebony_scimitar_1,itm_ebony_scimitar_1,itm_drow_shield,
    itm_drow_hood,itm_drow_armor,itm_drow_leather_boots,
   ],
   horse_attrib_4|level(30),wp_melee(300)|wp_crossbow(300),knows_precise_shot_2|knows_assasin_4|knows_magic_defence_4,mirkwood_elf_face_1,mirkwood_elf_face_2],

  ["drowelf_footman","Drow Elf Swordman","Drow Elf Swordman",
   tf_female_elf|tf_guarantee_all_footman,0,0,fac_beast,
   [
    itm_ebony_javelin,itm_ebony_scimitar_2,itm_ebony_scimitar_long_1,itm_drow_shield,
    itm_drow_hood_elite,itm_drow_elite_armor,itm_drow_elite_boots,itm_drow_elite_gloves,itm_trophy_a
   ],
   horse_attrib_5|level(35),wp_melee(350)|wp_throwing(350),knows_light_swordman_5|knows_magic_defence_4|knows_reserved_17_4,mirkwood_elf_face_1,mirkwood_elf_face_2],

  ["drowelf_assassin_1","Drow Elf Scout","Drow Elf Scout",
  tf_female_elf|tf_guarantee_all_wo_horse,0,0,fac_beast,
   [
    itm_tutorial_bolts,itm_tutorial_bolts,itm_drow_crossbow,
    itm_ebony_scimitar_1,itm_ebony_scimitar_1,itm_dueling_dagger,
    itm_drow_hood,itm_drow_armor,itm_drow_leather_boots,
   ],
   horse_attrib_4|level(35),wp_melee(300)|wp_crossbow(300),knows_precise_shot_2|knows_magic_power_1|knows_assasin_5|knows_magic_defence_4,mirkwood_elf_face_1,mirkwood_elf_face_2],
  ["drowelf_assassin_2","Drow Elf Assassin","Drow Elf Assassin",
   tf_female_elf|tf_guarantee_all_wo_horse,0,0,fac_beast,
   [
    itm_tutorial_bolts,itm_bonecrossbow_auto,itm_bolt_shadow_bolt,
    itm_assassin_dagger,itm_assassin_dagger,itm_dueling_dagger,
    itm_drow_hood_high,itm_drow_elite_armor,itm_drow_elite_boots,itm_drow_elite_gloves,itm_trophy_a
   ],
   horse_attrib_5|level(40),wp_melee(350)|wp_crossbow(350),knows_precise_shot_3|knows_magic_power_2|knows_assasin_7|knows_magic_defence_6,mirkwood_elf_face_1,mirkwood_elf_face_2],
  ["drowelf_assassin_3","Drow Elf Shade","Drow Elf Shade",
   tf_female_elf|tf_guarantee_all_wo_horse,0,0,fac_beast,
   [
    itm_bolt_shadow_bolt,itm_bonecrossbow_auto,itm_bolt_doom_bolt,
    itm_serpent_dagger,itm_serpent_dagger,itm_drow_round_shield,
    itm_drow_hood_elite,itm_drow_elite_armor_1,itm_drow_elite_boots,itm_drow_elite_gloves,itm_trophy_a
   ],
   horse_attrib_5|level(45),wp_melee(400)|wp_crossbow(350),knows_magic_power_4|knows_assasin_7|knows_magic_defence_6,mirkwood_elf_face_1,mirkwood_elf_face_2],

  ["drowelf_infantry_1","Drow Elf Black Guard","Drow Elf Black Guard",
   tf_female_elf|tf_guarantee_all_footman,0,0,fac_beast,
   [
    itm_drow_staff_2_melee,itm_drow_staff_2_melee,itm_ebony_poleaxe,
    itm_drow_hood_elite,itm_drow_elite_armor_2,itm_drow_plate_foot,itm_drow_plate_hand,itm_trophy_a
   ],
   horse_attrib_6|level(40),wp_melee(400),knows_light_swordman_6|knows_magic_defence_4,mirkwood_elf_face_1,mirkwood_elf_face_2],
   
  ["drowelf_infantry_2","Drow Elf Executioner","Drow Elf Executioner",
   tf_female_elf|tf_guarantee_all_footman,0,0,fac_beast,
   [
    itm_ebony_great_sword,itm_ebony_scimitar_long_3,itm_ebony_scimitar_2,itm_black_shield,
    #itm_xenoargh_mask_black,itm_drow_plate,itm_drow_plate_foot,itm_drow_plate_hand
    itm_ebony_male_head,itm_ebony_male_plate,itm_ebony_male_foot,itm_ebony_male_hand
   ],
   horse_attrib_7|level(45),wp_melee(450),knows_light_swordman_8|knows_magic_defence_6,mirkwood_elf_face_1,mirkwood_elf_face_2],


  ["drowelf_raider_1","Drow Elf Dark Raider","Drow Elf Dark Raider",
   tf_female_elf|tf_guarantee_all_lancer|tf_mounted,0,0,fac_beast,
   [
    itm_thunder_staff_melee,itm_ebony_scimitar_1,itm_drow_shield,
    itm_drow_basilisk,
    itm_drow_hood_elite,itm_drow_elite_armor_1,itm_drow_plate_foot,itm_drow_plate_hand,itm_trophy_a
   ],
   horse_attrib_6|level(40),wp_melee(400),knows_riding_10|knows_assasin_6|knows_magic_defence_4,mirkwood_elf_face_1,mirkwood_elf_face_2],
   
  ["drowelf_raider_2","Drow Elf Grim Raider","Drow Elf Grim Raider",
   tf_female_elf|tf_guarantee_all_lancer|tf_mounted,0,0,fac_beast,
   [
    itm_drow_lance,itm_ebony_scimitar_2,itm_drow_shield_rider,
    itm_drow_basilisk_2,
    #itm_xenoargh_mask_black,itm_grim_raider_armor_1,itm_drow_plate_foot,itm_drow_plate_hand
    itm_ebony_male_head,itm_drow_plate,itm_drow_plate_foot,itm_drow_plate_hand
   ],
   horse_attrib_7|level(45),wp_melee(450),knows_riding_10|knows_assasin_8|knows_magic_defence_6,mirkwood_elf_face_1,mirkwood_elf_face_2],

  ["drowelf_which_1","Drow Elf Shadow Witch","Drow Elf Shadow Witch",
   tf_female_elf|tf_guarantee_all_wo_horse,0,0,fac_beast,
   [
    itm_drow_staff_2,
    #itm_magic_summon_undead_near_ememy,
    itm_magic_oblivion,
    itm_serpent_dagger,
    itm_xenoargh_mask_black,itm_grim_raider_armor_2,
    itm_demon_foot,itm_drow_elite_gloves,itm_trophy_c,
   ],
   horse_attrib_8|level(45),wp_melee(300)|wp_firearm(300),knows_assasin_5|knows_magic_4,mirkwood_elf_face_1,mirkwood_elf_face_2],
  ["drowelf_which_2","Drow Elf Shadow Mistress","Drow Elf Shadow Mistress",
   tf_female_elf|tf_guarantee_all_wo_horse,0,0,fac_beast,
   [
    itm_drow_staff_3,itm_magic_word_of_pain,itm_magic_doom_bolt,
    
    #itm_magic_summon_demon_near_ememy,
    itm_serpent_dagger,
    itm_xenoargh_mask_black,itm_mistress_armor,
    itm_demon_foot,itm_drow_elite_gloves,itm_trophy_c,
   ],
   horse_attrib_9|level(50),wp_melee(350)|wp_firearm(350),knows_assasin_7|knows_magic_6,mirkwood_elf_face_1,mirkwood_elf_face_2],

   
  ["werewolf_berserker", "werewolf Berserker", "werewolf Berserker", 
   tf_guarantee_all_footman, 0, 0, fac_kingdom_10, 
   [
    #itm_nordhero_sword_long,itm_nordhero_greatsword_2,itm_stalhrim_greatsword,
    itm_stahlrim_battleaxe,itm_nordhero_long_axe,
    itm_stahlrim_plate,itm_stahlrim_plate,
    itm_stahlrim_foot,itm_wolfgloves_w,
    itm_wolfhelm_w2,itm_wolfhelm_w,
    itm_sg_orange_small
   ], 
   str_70|agi_70|int_12|cha_12|level(50), wp_melee(350)|wp_throwing(350),knows_power_throw_8|knows_physique_10|knows_shield_4|knows_power_strike_15|knows_ironflesh_10|knows_reserved_18_10|knows_weapon_master_10|knows_stealth_8|knows_magic_defence_6, nord_face_middle_1, nord_face_older_2 ],


  ["german_twohander_4", "Bane Blade", "Bane Blade", tf_guarantee_all_footman, 0, 0, fac_kingdom_7, 
  [itm_flamberge_fire,itm_trophy_c,
   itm_bane_blade_plate,itm_bane_blade_foot,itm_bane_blade_head,itm_bane_blade_hand,
   itm_bane_blade_plate,itm_bane_blade_foot,itm_bane_blade_head,itm_bane_blade_hand,
  ], 
  str_70|agi_70|int_12|cha_12|level(50), wp_melee(350), knows_physique_9|knows_shield_6|knows_power_strike_15|knows_ironflesh_15|knows_weapon_master_8|knows_stealth_8|knows_magic_defence_10, swadian_face_face_1, swadian_face_face_2 ],
            
  ["dryad","Dryad","Dryad",
   tf_female|tf_guarantee_all_footman,0,0,fac_forest_ranger,
   [
    itm_wolfclaw,itm_wolfclaw_dual,
    itm_demon_head,itm_demon_foot,itm_demon_hand,
    itm_dryad_body,itm_sg_green_small,itm_sg_green_small
   ], 
   horse_attrib_3|level(30),wp_melee(200),knows_assasin_5,berber_face_1, berber_face_2],
  ["pixie","Pixie","Pixie",
   tf_female|tf_guarantee_all_footman,0,0,fac_elf,
   [
    itm_wolfclaw_w,itm_wolfclaw_dual_w,
    itm_demon_head,itm_demon_foot,itm_demon_hand,
    itm_pixie_body,itm_sg_green_small
   ], 
   horse_attrib_3|level(30),wp_melee(200),knows_light_swordman_5,berber_face_1, berber_face_2],


 ["turk_village_rabble","turk Recruit","turk Recruits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_9,
   [
      itm_hatchet,itm_pickaxe,itm_club,
      itm_military_fork,itm_bamboo_spear,
      itm_hunting_bow,itm_barbed_arrows,
      itm_turban,itm_turban,
      itm_sarranid_boots_a,itm_sarranid_boots_a,
      itm_sarranid_cloth_robe,itm_sarranid_cloth_robe,itm_sarranid_cloth_robe_b
   ],
   foot_attrib_2|level(6),wp(50), knows_archer_1,euro_face_3, euro_face_4],
      
 ["turk_azap","turk Azap","turk Azap",
  tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_9,
   [
    itm_bamboo_spear,itm_war_spear,itm_spear,

    itm_jarid,itm_jarid,itm_jarid,itm_sword_khergit_2,
    itm_shield_otto1,
    itm_turban,itm_desert_turban,itm_desert_turban,
    itm_skirmisher_armor,itm_sarranid_boots_a
   ],
   foot_attrib_3|level(12), wp(75), knows_thrown_2,euro_face_3, euro_face_4],
      
      
            
  ["me_mercenary_swordsman_2","Mercenary Saracen Swordsman","Mercenary Saracen Swordsmen",
   tf_mounted|tf_guarantee_all_footman,0,0,fac_culture_6,
   [itm_sarranid_cavalry_sword,itm_arabian_sword_d,itm_scimitar,
    itm_dec_steel_shield,itm_jarid,itm_jarid,
    itm_mamluke_mail,itm_turk_armor,
    itm_sarranid_boots_d,itm_sarranid_boots_c,
    itm_sarranid_veiled_helmet,itm_chichak1,
    itm_scale_gauntlets],
   foot_attrib_5|level(24),wp(150),knows_swordman_3|knows_reserved_17_4,mercenary_face_1, mercenary_face_2],

  ["me_mercenary_swordsman_3","Mercenary Saracen Swordsman","Mercenary Saracen Swordsmen",
    tf_mounted|tf_guarantee_all_footman,0,0,fac_culture_6,
   [
    itm_sword_khergit_6,itm_sword_khergit_6,
    itm_jarid,itm_jarid,
    itm_dec_steel_shield,
    itm_sarranid_elite_armor,itm_turk_mail_heavy,
    itm_lamellar_gauntlets,
    itm_sarranid_boots_d,itm_sarranid_boots_c,
    itm_chichak2,itm_sarranid_veiled_helmet2
   ],
   horse_attrib_4|level(30),wp(200),knows_swordman_5|knows_reserved_17_6,mercenary_face_1,mercenary_face_2],
      
      
 ["turk_spearman","turk spearman","turk spearman",
  tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_kingdom_9,
   [
    itm_guisarme_2,itm_guisarme,
    itm_jarid,itm_jarid,
    itm_sarranid_mail_coif,
    itm_shield_otto2,itm_shield_otto1,
    itm_sarranid_boots_b,itm_sarranid_boots_c,
    itm_sarranid_leather_armor,itm_sarranid_mail_shirt
    ],
   foot_attrib_4|level(18), wp(100), knows_thrown_3,euro_face_3, euro_face_4],
      
 ["turk_footman","turk Voynik","turk Voynik",
  tf_guarantee_all_pikeman,0,0,fac_kingdom_9,
   [
    itm_sarranid_cavalry_sword,itm_arabian_sword_d,itm_sarranid_axe_a,
    itm_c_c_scythe,itm_sarranid_long_double_axe,
    itm_shield_otto2,
    itm_arabian_armor_b,itm_sarranid_mail_shirt,itm_sarranid_mail_shirt_3,itm_turk_mail_heavy,
    itm_mail_mittens,itm_scale_gauntlets,
    itm_sarranid_horseman_helmet,itm_sarranid_helmet1,itm_sarranid_warrior_cap,
    itm_sarranid_boots_c,itm_sarranid_boots_d
   ],
   foot_attrib_5|level(24), wp_melee(150),knows_twohand_4,euro_face_3, euro_face_4],
                                                       
   
                             
 ["turk_archer_1","turk Archer","turk Archers",
  tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_9,
   [itm_bamboo_arrows,itm_strong_bow,itm_strong_bow,itm_nomad_bow,itm_sword_khergit_2,itm_mace_3,itm_tab_shield_small_round_a,
   itm_archers_vest,itm_sarranid_boots_b,itm_turban,itm_desert_turban],
   foot_attrib_2|level(19), wp_melee(90)|wp_missile(110), knows_archer_3,euro_face_3, euro_face_4],
 ["turk_archer_2","turk Master Archer","turk Master Archers",
  tf_guarantee_ranged|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_9,
   [itm_bamboo_arrows,itm_sword_khergit_3,itm_mace_4,itm_nomad_bow,itm_nomad_bow,itm_strong_bow,
    itm_arabian_armor_b,itm_tab_shield_small_round_b,
    itm_sarranid_boots_c,itm_sarranid_boots_b,itm_sarranid_mail_coif],
   foot_attrib_3|level(24),wp_melee(100)|wp_missile(130), knows_archer_4|knows_thrown_1,euro_face_3, euro_face_4],
      

  ["turk_cav_1","Steppe Cavalry","Steppe Cavalrys",
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged|tf_mounted,0,0,fac_kingdom_9,
   [itm_arrows,itm_arabian_sword_a,itm_spear, itm_war_spear,
    itm_nomad_bow,itm_strong_bow,itm_jarid,itm_jarid,
    itm_desert_turban,itm_turban,
    itm_skirmisher_armor,
    itm_desert_turban,itm_sarranid_boots_a,
    itm_shield_otto1,itm_shield_otto_wing,
    itm_saddle_horse_steppe,itm_saddle_horse_steppe,itm_arabian_horse_a],
   horse_attrib_1|level(12),wp(100)|wp_missile(130),knows_horse_shoot_5|knows_ranger_2,arab_face_1, arab_face_2],
  ["turk_cav_2","turkoman Cavalry","turkoman Cavalrys",
   tf_guarantee_all_nomad|tf_mounted,0,0,fac_kingdom_9,
   [
    itm_bamboo_arrows,itm_arabian_sword_b,itm_sarranid_cavalry_sword,itm_light_lance,
    itm_khergit_bow,itm_nomad_bow,itm_nomad_bow,
    itm_deli_turban,
    itm_turk_leather_armor,itm_sarranid_cavalry_robe,itm_sarranid_leather_armor,
    itm_sarranid_boots_b,
    itm_shield_otto_wing,itm_shield_otto1,
    itm_courser_steppe,itm_arabian_horse_a
   ],
   horse_attrib_2|level(18),wp(120)|wp_missile(150),knows_horse_shoot_7|knows_ranger_3,arab_face_1, arab_face_2],
      
  ["turk_cav_3","Veteran turkoman Cavalry","Veteran turkoman Cavalry",
   tf_guarantee_all_nomad|tf_mounted,0,0,fac_kingdom_9,
   [
    itm_khergit_arrows,itm_sarranid_cavalry_sword,itm_scimitar_b,itm_lance,
    itm_khergit_bow,itm_khergit_bow,
    itm_sarranid_horseman_helmet,itm_sarranid_horseman_helmet,
    itm_sarranid_mail_shirt_3,itm_sarranid_mail_shirt_2,
    itm_sarranid_boots_c,
    itm_shield_otto2,itm_shield_otto_wing,
    itm_courser_steppe,itm_hunter_steppe,itm_arabian_horse_b
   ],
   horse_attrib_3|level(24),wp(140)|wp_missile(170),knows_horse_shoot_8|knows_ranger_4,arab_face_1, arab_face_2],  
   
  ["marinid_camel_1","marinid Desert Camel Cavalry","marinid Desert Camel Cavalry",
  tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_culture_6,
  [
    itm_arabian_sword_a,
    itm_winged_mace,
    itm_spear, itm_light_lance,
    itm_jarid,itm_jarid,
    itm_leather_covered_round_shield,itm_leather_covered_round_shield,
    itm_skirmisher_armor,itm_archers_vest,
    itm_sarranid_leather_armor, 
    itm_desert_turban, itm_turban,itm_leather_steppe_cap_b,
    itm_camel],
   foot_attrib_2|level(13),wp(100),knows_horse_shoot_5|knows_thrown_3,berber_face_1, berber_face_2],
   
  ["marinid_camel_2","marinid Camel Cavalry","marinid Camel Cavalry",
   tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_culture_6,
   [
      itm_sarranid_cavalry_sword,
      itm_sarranid_mace_1,
      itm_sarranid_axe_a,
      itm_sarranid_axe_b,
      itm_throwing_spears,itm_throwing_spears,
      itm_leather_covered_round_shield,itm_tab_shield_small_round_b,
      itm_desert_turban, itm_sarranid_warrior_cap,itm_sarranid_horseman_helmet,
      itm_arabian_armor_b,itm_lamellar_vest_khergit,
      itm_sarranid_boots_b,itm_leather_gloves,itm_tab_shield_small_round_b,itm_tab_shield_small_round_c,itm_camel2],
   horse_attrib_1|level(19),wp(120),knows_horse_shoot_6|knows_thrown_4,berber_face_1, berber_face_2],

  ["marinid_camel_3_1","marinid heavy Camel Cavalry","marinid heavy Camel Cavalry",
  tf_mounted|tf_guarantee_all,0,0,fac_culture_6,
   [
      itm_heavy_lance,
      itm_sarranid_cavalry_sword,
      itm_scimitar_b,
      itm_sarranid_two_handed_mace_1,
      itm_sarranid_mace_1,
      itm_sarranid_axe_a,
      itm_sarranid_axe_b,
      #itm_throwing_scimitar,itm_throwing_scimitar,
      itm_dec_steel_shield,itm_dec_steel_shield,
      
    itm_sarranid_mail_coif,itm_sarranid_veiled_helmet,itm_mamluke_mail,itm_sarranid_boots_d,itm_leather_gloves,itm_camel3],
   horse_attrib_2|level(25),wp_melee(150)|wp_throwing (110),knows_horse_shoot_7|knows_thrown_5,berber_face_1, berber_face_2],
      
  ["marinid_camel_3_2","marinid Camel Gunner","marinid Camel Gunners",
  tf_mounted|tf_guarantee_all,0,0,fac_culture_6,
   [
      itm_carbine_batarey,
      itm_carbine_batarey_2shot,
      itm_carbine,
      itm_cartridges,
      itm_cartridges_2,
      
      itm_sarranid_cavalry_sword,
      itm_sarranid_mace_1,
      itm_sarranid_axe_a,
      itm_sarranid_axe_b,
    
    itm_sarranid_horseman_helmet,itm_lamellar_vest_khergit,itm_sarranid_boots_b,itm_leather_gloves,itm_tab_shield_small_round_b,itm_tab_shield_small_round_c,itm_camel2],
   horse_attrib_2|level(25),wp(130)|wp_firearm(230) ,knows_horse_shoot_7|knows_firearm_5,berber_face_1, berber_face_2],

  ["marinid_camel_4_1","marinid Veteran heavy Camel Cavalry","marinid Veteran heavy Camel Cavalry",
  tf_mounted|tf_guarantee_all,0,0,fac_culture_6,
   [
      itm_morningstar,
      itm_sarranid_two_handed_mace_1,
      itm_sarranid_mace_1,
      itm_sarranid_axe_a,
      itm_sarranid_axe_b,
      #itm_throwing_scimitar,itm_throwing_scimitar,
      itm_dec_steel_shield,itm_dec_steel_shield,
      
     itm_sarranid_veiled_helmet,itm_sarranid_elite_armor,itm_mamluke_mail_heavy,itm_sarranid_boots_d,itm_leather_gloves,itm_camel3],
   horse_attrib_3|level(30),wp_melee(200)|wp_throwing (180),knows_horse_shoot_7|knows_thrown_6,berber_face_1, berber_face_2],
      
  ["marinid_camel_4_2","marinid Veteran Camel Gunner","marinid Veteran Camel Gunners",
  tf_mounted|tf_guarantee_all,0,0,fac_culture_6,
   [
      itm_carbine_batarey_good,
      itm_carbine_batarey_2shot,
      itm_cartridges_burst,
      
      itm_sarranid_cavalry_sword,
      itm_sarranid_mace_1,
      itm_sarranid_axe_a,
      itm_sarranid_axe_b,
    
    itm_sarranid_horseman_helmet,itm_mamluke_mail,itm_sarranid_boots_b,itm_leather_gloves,itm_tab_shield_small_round_b,itm_tab_shield_small_round_c,itm_camel3],
   horse_attrib_3|level(30),wp(130)|wp_firearm(330) ,knows_riding_7|knows_horse_archery_9|knows_firearm_7,berber_face_1, berber_face_2],

  ["welsh_longbowm_1","welsh hunter","welsh hunter",
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_forest_ranger,
   [itm_arrows,itm_bamboo_arrows,itm_long_bow,
    itm_longbowman_sword,itm_sword_medieval_b_small,

    itm_ranger_armor1,itm_tunic_with_green_cape,
    itm_hood_c,itm_hood_c,itm_leather_boots,itm_wrapping_boots],
   foot_attrib_2|level(16),wp_melee(100)|wp_archery (180),knows_ranger_2,nord_face_young_1, nord_face_old_2],
            
  ["welsh_longbowm_2","welsh longbowman","welsh longbowman",
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_forest_ranger,
   [itm_elven_arrow,itm_mutil_arrow,itm_long_bow_2,
    itm_scimitar_green,
    itm_leather_gloves,
    itm_leather_boots,
    itm_ranger_armor1,itm_padded_leather,
    itm_wizard_hood_2_2,
   ],
   foot_attrib_3|level(22),wp_melee(100)|wp_archery (240),knows_magic_power_3|knows_ranger_3,nord_face_young_1, nord_face_old_2],
      
  ["welsh_longbowm_3","welsh Veteran Longbowmen","welsh Veteran Longbowmen",
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_forest_ranger,
   [itm_mutil_arrow,itm_woodelf_mutil_arrows,itm_long_bow_3,
    itm_warblade_greensilver,
    itm_leather_gloves,
    itm_splinted_leather_greaves,
    itm_padded_leather,itm_wizard_hood_3],
   foot_attrib_4|level(28),wp_melee(100)|wp_archery(320),knows_magic_power_5|knows_ranger_5,nord_face_young_1, nord_face_old_2],


  ["welsh_spearman_1","welsh spearman","welsh spearman",
   tf_guarantee_all_pikeman,0,0,fac_forest_ranger,
   [  
      itm_shortened_spear,itm_war_spear,
      itm_military_scythe,itm_glaive,
      
      itm_tab_shield_small_round_b,
      itm_tab_shield_small_round_a,
      
      itm_padded_leather,itm_studded_leather_coat,
      itm_mail_coif,itm_bascinet,
      itm_leather_boots,itm_mail_mittens
   ],
   foot_attrib_4|level(20),wp_melee(180),knows_light_swordman_3,west_euro_face_younger_1, west_euro_face_older_2],
   
  ["welsh_spearman_2","welsh Veteran spearman","welsh Veteran spearman",
   tf_guarantee_shield|tf_guarantee_all_pikeman,0,0,fac_forest_ranger,
   [
      itm_long_voulge,itm_one_handed_war_axe_b,itm_glaive,
      
      itm_tab_shield_small_round_b,
      itm_tab_shield_small_round_c,
      itm_bascinet,itm_bascinet_coif,
      
      itm_ranger_armor4,
      itm_studded_leather_coat,      
      itm_splinted_greaves,itm_splinted_leather_greaves,itm_mail_mittens
   ],
   foot_attrib_5|level(24),wp_melee(200),knows_light_swordman_5,west_euro_face_younger_1, west_euro_face_older_2],

  ["dragonfly","dragonfly","dragonfly",tf_goblin|tf_guarantee_all_footman,0,0,fac_scotland,
   [
    itm_serpentfly_weapon,
    itm_demon_head,itm_demon_foot,itm_demon_hand,
    itm_serpentfly,itm_dragonfly,itm_serpentfly,
   ],
   horse_attrib_1|level(15),wp(80),knows_stealth_1,bandit_face1, bandit_face2],   

  ["firefly","firefly","firefly",tf_goblin|tf_guarantee_ranged|tf_guarantee_all_footman,0,0,fac_scotland,
   [
    itm_serpentfly_weapon,itm_firefly_fireball,
    itm_demon_head,itm_demon_foot,itm_demon_hand,
    itm_firefly
   ],
   horse_attrib_1|level(15),wp (80) | wp_throwing (150),knows_stealth_1|knows_thrown_3,bandit_face1, bandit_face2],

  ["scottish_jav","Lizard Skirmisher","Lizard Skirmisher",
   tf_ogre|tf_guarantee_all_footman,0,0,fac_scotland,
   [
      itm_sword_viking_2,itm_sword_viking_1,itm_spear,
      itm_javelin,itm_javelin,
      itm_lizard_armour_1,itm_lizard_boot_1,
      itm_lizard_helmet_1,itm_lizard_glove1,
   ],
   horse_attrib_2|level(14),wp(150),knows_thrown_3|knows_vampire_3,swadian_face_younger_1, swadian_face_older_2],

  ["scottish_axeman","Lizard Marauder","Lizard Marauder",
   tf_ogre|tf_guarantee_all_footman,0,0,fac_scotland,
   [
      itm_nordhero_sword, itm_nordhero_axe_1,itm_glaive,
      itm_throwing_spears,itm_throwing_spears,
      itm_highlander_shield3,itm_highlander_shield2,
      itm_lizard_armour_3,itm_lizard_boot_2,
      itm_lizard_helmet_2,itm_lizard_glove1,
   ],
   horse_attrib_3|level(21),wp_melee(200),knows_swordman_4|knows_vampire_5,swadian_face_younger_1, swadian_face_older_2],

  ["lizard_axeman_1","Lizard Veteran Marauder","Lizard Veteran Marauder",
   tf_ogre|tf_guarantee_all_footman,0,0,fac_scotland,
   [
      itm_nordhero_sword_long, itm_nordhero_axe_2,itm_nordhero_long_axe,
      itm_org_throwing_spears_1,itm_org_throwing_spears_1,
      itm_tab_shield_round_a,itm_tab_shield_round_b,
      itm_lizard_armour_4,itm_lizard_boot_3,
      itm_lizard_helmet_2,itm_lizard_glove2,
   ],
   horse_attrib_4|level(28),wp_melee(250),knows_swordman_5|knows_vampire_5,swadian_face_younger_1, swadian_face_older_2],

  ["lizard_rider_1","Lizard Coldone Rider","Lizard Coldone Rider",
   tf_ogre|tf_mounted|tf_guarantee_all_lancer,0,0,fac_scotland,
   [
      itm_nordhero_sword, itm_nordhero_greatsword,
      itm_lance,itm_lance,itm_lizard_basilisk,
      itm_tab_shield_round_c,itm_tab_shield_round_c,
      itm_lizard_armour_4,itm_lizard_boot_3,
      itm_lizard_helmet_2,itm_lizard_glove1,
   ],
   horse_attrib_4|level(28),wp_melee(250),knows_swordman_5|knows_vampire_5,swadian_face_younger_1, swadian_face_older_2],




  ["scottish_pikeman","Lizard Archer","Lizard Archer",
   tf_guarantee_all_wo_horse,0,0,fac_scotland,
   [
      itm_undead_arrow,itm_undead_arrow,
      itm_nord_bow_1,itm_nord_bow_1,
      itm_sword_khergit_3,itm_sword_khergit_2,
      
      itm_highlander_shield3,itm_highlander_shield2,
      itm_lizard_armour_2,itm_lizard_boot_2,
      itm_lizard_helmet_1,itm_lizard_glove1,
   ],
   horse_attrib_3|level(21),wp_melee(170)|wp_archery(200),knows_ranger_5|knows_vampire_4,swadian_face_younger_1, swadian_face_older_2],

  ["scottish_pikeman_2","Lizard Stalker","Lizard Stalker",
   tf_guarantee_all_wo_horse,0,0,fac_scotland,
   [
      itm_poison_arrows,itm_mutil_arrow_2,
      itm_nord_bow_2,itm_nord_bow_2,
      itm_nordhero_axe_1,itm_nordhero_axe_2,
      
      itm_highlander_shield3,itm_highlander_shield2,
      itm_lizard_armour_3,itm_lizard_boot_3,
      itm_lizard_helmet_2,itm_lizard_glove1,
   ],
   horse_attrib_4|level(28),wp_melee(200)|wp_archery(300),knows_ranger_7|knows_vampire_5|knows_magic_power_2,swadian_face_younger_1, swadian_face_older_2],
  
  ["lizard_axeman_2","Lizard Champion","Lizard Champion",
   tf_ogre|tf_guarantee_all_footman,0,0,fac_scotland,
   [
      itm_stalhrim_sword_short,itm_stahlrim_axe, itm_stahlrim_battleaxe,
      itm_throwing_spears,itm_throwing_spears,
      itm_tab_shield_round_d,itm_tab_shield_round_d,
      itm_lizard_armour_6,itm_lizard_boot_4,
      itm_lizard_helmet_3,itm_lizard_glove2,
   ],
   horse_attrib_5|level(35),wp_melee(300),knows_swordman_7|knows_vampire_5,swadian_face_younger_1, swadian_face_older_2],

  ["lizard_rider_2","Lizard Coldone Champion","Lizard Coldone Champion",
   tf_ogre|tf_mounted|tf_guarantee_all_lancer,0,0,fac_scotland,
   [
      itm_stalhrim_sword, itm_stalhrim_greatsword,
      itm_heavy_lance,itm_heavy_lance,itm_lizard_basilisk_2,
      itm_tab_shield_round_d,itm_tab_shield_round_d,
      itm_lizard_armour_5,itm_lizard_boot_4,
      itm_lizard_helmet_3,itm_lizard_glove2,
   ],
   horse_attrib_5|level(35),wp_melee(250),knows_swordman_6|knows_vampire_5,swadian_face_younger_1, swadian_face_older_2],
  
  ["scottish_pikeman_3","Lizard Warrior","Lizard Warrior",
   tf_guarantee_all_wo_horse,0,0,fac_scotland,
   [
      itm_woodelf_arrows_freezing,itm_stahlrim_arrow,
      itm_nord_bow_3,itm_nord_bow_3,
      itm_stahlrim_axe,
      
      itm_highlander_shield3,itm_highlander_shield2,
      itm_lizard_armour_3,itm_lizard_boot_3,
      itm_lizard_helmet_2,itm_lizard_glove1,
   ],
   horse_attrib_5|level(35),wp_melee(350)|wp_archery(400),knows_ranger_6|knows_vampire_6|knows_magic_power_4,swadian_face_younger_1, swadian_face_older_2],

  ["scottish_swordman","Lizard Beastmaster","Lizard Beastmaster",
   tf_ogre|tf_mounted|tf_guarantee_all,0,0,fac_scotland,
   [
      itm_stalhrim_sword,itm_stahlrim_axe,itm_tab_shield_round_d,itm_nord_jarid,
      
      
      itm_lizard_armour_6,itm_lizard_boot_4,
      itm_lizard_helmet_3,itm_lizard_glove2,
      itm_gorgon_1,itm_gorgon_2
   ],
   horse_attrib_7|level(42),wp_melee(300),knows_swordman_8|knows_vampire_7,swadian_face_younger_1, swadian_face_older_2],   

  ["scottish_guard","Lizard Shaman","Lizard Shaman",
   tf_guarantee_all_wo_horse,0,0,fac_scotland,
   [
      itm_magic_poison,
      itm_shaman_staff_2,
      itm_lizard_boot_1,itm_lizard_glove1,
      itm_lizard_shaman_helmet,itm_lizard_shaman_helmet,
      itm_lizard_shaman_1,itm_lizard_shaman_2
   ],
   horse_attrib_6|level(35),wp_melee(280)| wp_firearm (300),knows_magic_7|knows_vampire_7,swadian_face_younger_1, swadian_face_older_2],

  ["lizard_dragon", "lizard dragon", "lizard dragon", 
   tf_titan|tf_guarantee_all_wo_horse, 0, 0, fac_scotland, 
   [
    itm_black_dragon_sword_melee,itm_green_dragon_shield,
    #itm_green_dragon_breath_2,itm_green_dragon_breath,
    itm_demon_head,itm_demon_foot,itm_demon_hand,itm_trophy_b,itm_sg_blood,
    itm_blue_dragon_body,itm_sg_blue_big,itm_sg_blue_big
   ], 
   horse_attrib_5|str_80|level(45), wp(350), knows_physique_7|knows_shield_5|knows_power_strike_8|knows_ironflesh_12|knows_reserved_18_10|knows_weapon_master_7|knows_magic_power_6|knows_magic_defence_9|knows_magic_skill_15, swadian_face_young_1, swadian_face_young_1 ],

  ["swiss_swordman","swiss swordman","swiss swordman",
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_swiss,
   [
    #itm_sword_medieval_c_small,itm_side_sword,itm_steel_shield,
    itm_swiss_halberd_short,itm_glaive,itm_guisarme,itm_guisarme_2,
    itm_kettle_hat_cloth1,itm_kettle_hat_cloth2,itm_kettle_hat_cloth3,
    itm_light_brigandine_green,itm_light_brigandine_green,
    itm_narf_hose,itm_leather_gloves],
   foot_attrib_4|level(18),wp_melee(120) ,knows_physique_6|knows_light_swordman_3, latin_face_1, latin_face_2],

  ["swiss_pikeman","swiss Pikeman","swiss Pikeman",
   tf_guarantee_all_pikeman,0,0,fac_swiss,
   [itm_long_pike,itm_long_pike_2,itm_pike_2,itm_long_pike_2,
    itm_swiss_halberd,itm_long_voulge,itm_long_glaive,
    itm_side_sword,itm_steel_shield,
    itm_kettle_hat_mail1,itm_kettle_hat_mail2,itm_kettle_hat_mail3,
    itm_light_brigandine_green_mail,itm_light_brigandine_green_mail,
    itm_hose_kneecops_green,itm_leather_gloves],
   foot_attrib_5|level(24),wp_melee(120)|wp_polearm (190) ,knows_physique_6|knows_pikeman_4, latin_face_1, latin_face_2],

  ["swiss_pikeman_2","swiss Armor Pikeman","swiss Armor Pikeman",
  tf_guarantee_all_pikeman|tf_guarantee_shield,0,0,fac_swiss,
   [itm_pike_2,itm_long_pike,itm_pike,itm_long_pike,
    itm_side_sword,itm_steel_shield,
    itm_nord_poleaxe_1,itm_nord_poleaxe_2,itm_nord_poleaxe_3,itm_nord_poleaxe_4,
    itm_sturmhaube_bnw4,itm_sturmhaube_bnw3,itm_sturmhaube_bnw2,
    itm_bnw_armour,itm_bnw_armour,itm_bnw_splinted_greaves,itm_bnw_gauntlets],
   horse_attrib_5|level(40), wp_melee(150)|wp_polearm (250) ,knows_physique_6|knows_pikeman_8,latin_face_1, latin_face_2],

  ["swiss_halberd","swiss halberd","swiss halberd",
   tf_guarantee_all_pikeman|tf_guarantee_shield,0,0,fac_swiss,
   [
    itm_glaive_a,itm_glaive_b,itm_glaive,itm_guisarme,itm_guisarme_2,
    itm_swiss_halberd_short,

    itm_zitta_bascinet_novisor,itm_kettle_hat_mail2,itm_kettle_hat_mail3,
    itm_light_brigandine_green_mail,itm_light_brigandine_green_mail,
    itm_hose_kneecops_green,itm_leather_gloves],
   foot_attrib_4|level(24),wp_melee(150), knows_pikeman_4,latin_face_1, latin_face_2],
  ["swiss_halberd_2","swiss guard","swiss guard",
   tf_guarantee_all_pikeman|tf_guarantee_shield,0,0,fac_swiss,
   [
    itm_german_poleaxe_1,itm_german_poleaxe_2,itm_german_poleaxe_3,itm_german_poleaxe_4,
    itm_poleaxe,itm_bec_de_corbin_a,itm_polehammer_threeprong,itm_polehammer_manhunter,
    itm_combed_morion_3,
    itm_half_plates,itm_half_plates_green,itm_brigandine_plate_green,
    itm_iron_greaves2,itm_milanese_gauntlets],
   horse_attrib_5|level(40),wp_melee(250), knows_pikeman_8,latin_face_1, latin_face_2],

  ["goblin","goblin","goblin",
   tf_goblin|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_orc,
   [
    itm_org_sword1,itm_stones,itm_org_shield_1, itm_org_shield_1,
    itm_woolen_cap,itm_woolen_cap,
   ],
   ranged_attrib_2|level(6),wp(60),knows_militia, bandit_face1, bandit_face2],

  ["goblin_footman","goblin Footman","goblin Footmen",
   tf_goblin|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor,0,0,fac_orc,
   [
    itm_org_axe3,itm_org_sword2,
    itm_org_throwing_spears_1,itm_org_throwing_spears_1,
    itm_org_shield_2,itm_org_shield_1,
    itm_org_armour_1,itm_org_armour_1,itm_org_boot_1
   ],
   ranged_attrib_3|level(13),wp(75),knows_thrown_2, bandit_face1, bandit_face2],
  ["goblin_skirmisher","goblin Skirmisher","goblin Skirmishers",tf_goblin|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_orc,
   [
    itm_arrows,
    itm_org_spear_2,
    itm_short_bow,itm_short_bow,itm_hunting_bow,
    itm_org_armour_1,itm_org_armour_1,
    itm_org_boot_1
   ],
   ranged_attrib_3|level(12),wp(60),knows_ranger_2,bandit_face1, bandit_face2],   

  ["goblin_crossbowman","goblin Crossbowman","goblin Crossbowmen",tf_goblin|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_orc,
   [itm_bolts,
    itm_org_spear_3,
    itm_org_crossbow_1,itm_org_crossbow_1,itm_org_crossbow_2,
    itm_org_armour_3,
    itm_org_boot_1,
    itm_org_helmet_1
   ],
   ranged_attrib_4|level(18),wp (70) | wp_crossbow (150),knows_crossbowman_3,bandit_face1, bandit_face2],
  ["goblin_infantry","goblin Infantry","goblin Infantries",tf_goblin|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_orc,
   [itm_org_axe3,itm_org_shield_2,itm_xenoargh_bola,itm_xenoargh_bola,
    itm_org_armour_4,itm_org_armour_4,
    itm_org_boot_2,itm_org_helmet_1,itm_org_helmet_1,itm_org_helmet_1],
   ranged_attrib_5|level(19),wp(150),knows_light_swordman_3,bandit_face1, bandit_face2],
  ["goblin_horseman","goblin Wolf_Rider","goblin Wolf_Rider",tf_goblin|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_orc,
   [
    itm_org_axe3,itm_org_spear_3,itm_org_shield_3,itm_xenoargh_bola,itm_xenoargh_bola,
    itm_org_armour_4,itm_org_armour_3,
    itm_org_boot_2,
    itm_org_helmet_2,itm_org_helmet_2,itm_org_helmet_2,
    itm_wolf_mount_white,itm_wolf_mount_black,itm_furs
   ],
   ranged_attrib_5|level(20),wp(150),knows_riding_3|knows_light_swordman_4|knows_horse_archery_10,bandit_face1, bandit_face2],
   
   
  ["goblin_guard","goblin Guard","goblin Guards",tf_goblin|tf_mounted|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_orc,
   [#itm_org_throwing_spears_2,
    itm_org_twohanderaxe,itm_org_axe4,itm_org_shield_3,
    itm_org_armour_5,itm_org_boot_2,itm_org_helmet_3],
   foot_attrib_5|level(30),wp_melee(200),knows_light_swordman_5,bandit_face1, bandit_face2],
  ["goblin_knight","goblin captain","goblin captain",tf_goblin|tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_orc,
   [itm_org_axe4,
    itm_org_lance,itm_org_lance,
    itm_org_shield_3,
    itm_org_armour_5,itm_org_armour_5,
    itm_org_boot_2,
    itm_org_helmet_3,itm_org_helmet_3,
    itm_spider,itm_spider,itm_spider,itm_furs,itm_pork
    ],
   foot_attrib_6|level(30),wp(200),knows_riding_6|knows_light_swordman_6,bandit_face1, bandit_face2],

  ["goblin_bomber","goblin Bomber","goblin Bomber",
   tf_goblin|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_orc,
   [itm_barrel_bomb,
    itm_org_armour_4,itm_org_armour_4,
    itm_org_boot_2,itm_org_helmet_1,itm_org_helmet_1,itm_org_helmet_1],
   ranged_attrib_5|level(19),wp(150),knows_physique_10|knows_power_strike_4|knows_ironflesh_10|knows_reserved_18_10|knows_weapon_master_10|knows_magic_defence_1,bandit_face1, bandit_face2],

  ["rat_bomber", "rat Bomber", "rat Bomber", 
   tf_goblin|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_beast,
   [
    itm_barrel_bomb,
    itm_rat_armor_8,itm_rat_armor_9,itm_rat_armor_10,
    itm_rus_shoes,
    itm_rathelm2,itm_wolfgloves,itm_cheese
   ],
   ranged_attrib_4|level(20),wp(180),knows_physique_10|knows_power_strike_4|knows_ironflesh_10|knows_reserved_18_10|knows_weapon_master_10|knows_magic_defence_1,bandit_face1, bandit_face2],

 ["ogre_young","Ogre","Ogre",
  tf_ogre|tf_no_capture_alive|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_shield,0,0,fac_orc,
  [
   itm_ogre_axe_3,itm_orc_handaxe,
   itm_org_shield_1,itm_org_throwing_spears_1,
   itm_ogre_armor1,itm_ogre_boots_01,itm_dried_meat
  ],
   horse_attrib_2|str_30|level(20),wp(200),knows_physique_6|knows_shield_2|knows_power_strike_7|knows_ironflesh_5|knows_reserved_18_10|knows_weapon_master_3|knows_stealth_2|knows_magic_defence_3|knows_power_throw_4, vaegir_face_young_1, vaegir_face_middle_2],

 ["ogre","Ogre Fighter","Ogre Fighter",
  tf_ogre|tf_no_capture_alive|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_shield,0,0,fac_orc,
  [
    itm_ogre_shield,itm_ogre_axe,
    itm_ogre_bear_helmet,
    itm_orc_greatsword,itm_ogre_axe_3,itm_org_throwing_spears_2,
    itm_ogre_armor3,itm_org_throwing_spears_1,itm_ogre_boots_01,
    itm_dried_meat,itm_pork
   ],
   horse_attrib_3|str_50|level(30),wp(250),knows_physique_8|knows_shield_3|knows_power_strike_11|knows_ironflesh_8|knows_reserved_18_10|knows_weapon_master_5|knows_stealth_3|knows_magic_defence_5|knows_power_throw_6, vaegir_face_young_1, vaegir_face_middle_2],

 ["ogre_gunner","Ogre gunner","Ogre gunner",
  tf_ogre|tf_no_capture_alive|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_shield,0,0,fac_orc,
  [
    itm_ogre_shield,itm_ogre_axe,
    itm_ogre_bear_helmet,
    itm_orc_greatsword,itm_ogre_axe_3,
    itm_flintlock_pistol_elite_1,itm_flintlock_pistol_elite_2,
    itm_cartridges_burst,itm_cartridges_burst,
    itm_ogre_armor3,itm_ogre_boots_01,
    itm_dried_meat,itm_pork
   ],
   horse_attrib_3|str_50|level(30),wp(250),knows_physique_8|knows_shield_3|knows_power_strike_11|knows_ironflesh_8|knows_reserved_18_10|knows_weapon_master_2|knows_stealth_7|knows_magic_defence_5|knows_power_throw_6, vaegir_face_young_1, vaegir_face_middle_2],

 ["ogre_gunner2","Ogre gunner 2","Ogre gunner 2",
  tf_ogre|tf_no_capture_alive|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_shield,0,0,fac_orc,
  [
    itm_ogre_shield,itm_ogre_axe_2,
    itm_ogre_bear_helmet,
    itm_reitern_pistol_4s,itm_musket_hand_gun,
    itm_cartridges_cannon_1,itm_cartridges_burst,
    
    itm_ogre_barbar_helm,itm_vanguard_shield,itm_ogre_boots_02,itm_ogre_armor,
    itm_dried_meat,itm_dried_meat,itm_sausages,itm_trophy_b,itm_sg_orange_small
   ],
   horse_attrib_3|str_50|level(30),wp(250),knows_physique_8|knows_shield_3|knows_power_strike_11|knows_ironflesh_8|knows_reserved_18_10|knows_weapon_master_2|knows_stealth_7|knows_magic_defence_5|knows_power_throw_6, vaegir_face_young_1, vaegir_face_middle_2],

 ["ogre_war","war Ogre","war Ogre",
  tf_ogre|tf_no_capture_alive|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_shield,0,0,fac_orc,
   [
    itm_ogre_axe_4,itm_ogre_axe_2,itm_nord_javelin,
    itm_ogre_barbar_helm,itm_vanguard_shield,itm_ogre_boots_02,itm_ogre_armor,
    itm_dried_meat,itm_dried_meat,itm_sausages,itm_trophy_b,itm_sg_orange_small
   ],
   horse_attrib_5|str_70|level(40),wp(300),knows_physique_10|knows_shield_10|knows_power_strike_15|knows_ironflesh_15|knows_reserved_18_10|knows_weapon_master_7|knows_stealth_4|knows_magic_defence_10|knows_power_throw_8, vaegir_face_young_1, vaegir_face_middle_2],


 ["ogre_war2","Ogre Executioner","Ogre Executioner",
  tf_ogre|tf_no_capture_alive|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_shield,0,0,fac_orc,
   [
    itm_slaughter_axe,itm_slaughter_axe,
    itm_ogre_barbar_helm,itm_ogre_boots_02,itm_ogre_armor3,
    itm_dried_meat,itm_dried_meat,itm_sausages,itm_trophy_b,itm_sg_orange_small
   ],
   str_50|agi_50|int_12|cha_12|level(40),wp(300),knows_physique_10|knows_shield_4|knows_power_strike_15|knows_ironflesh_12|knows_reserved_18_10|knows_weapon_master_9|knows_stealth_15|knows_magic_defence_9, vaegir_face_young_1, vaegir_face_middle_2],



 ["ogre_mega","Ogre Mage","Ogre Mage",
  tf_ogre|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_orc,
   [itm_ogrehammer_cast,itm_magic_fireball,itm_magic_pyroblast,itm_magic_fireball_2,itm_ogre_nemean_helm,itm_ogre_armor2,itm_ogre_boots_02,itm_sausages,itm_trophy_b,itm_sg_orange_big],
   horse_attrib_4|str_70|level(40),wp(250),knows_magic_power_4|knows_magic_defence_4|knows_billman_5|knows_magic_skill_10, vaegir_face_young_1, vaegir_face_middle_2],

 ["troll_1","Troll","Troll",tf_troll|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_orc,
  [itm_tree_trunk_club,itm_heavyogresword,itm_troll_stones,itm_troll_head_helm_1,itm_troll_feet_boots,itm_trophy_b,itm_sg_orange_big],
   str_80|agi_25|int_4|cha_4|level(40),wp(250),knows_thrown_6|knows_ironflesh_10, vaegir_face_young_1, vaegir_face_middle_2],
   
 ["troll_2","Armored_Troll","Armored_Troll",tf_troll|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_orc,
  [
   itm_giant_hammer,itm_giant_mace,
   itm_troll_stones,
   itm_olog_head_helm_1,itm_olog_body_1,itm_olog_body_2,itm_olog_hands,itm_olog_feet_boots,itm_trophy_c,itm_sg_orange_big],
   str_100|agi_255|int_4|cha_4|level(60),wp(350),knows_swordman_7|knows_power_throw_4, vaegir_face_young_1, vaegir_face_middle_2],

  ["cyclop","Cyclop","Cyclop",
   tf_titan|tf_guarantee_all_footman, 0, 0, fac_orc, 
  [
   itm_cyclop_weapon,
   itm_demon_head,itm_cyclop_body,itm_demon_foot,itm_demon_hand,itm_trophy_b,itm_trophy_c,itm_sg_orange_big],
   str_90|agi_20|int_4|cha_4|level(60),wp(300),knows_physique_9|knows_shield_4|knows_power_strike_13|knows_ironflesh_10|knows_reserved_18_10|knows_weapon_master_6|knows_stealth_3|knows_magic_defence_9|knows_power_throw_9, vaegir_face_young_1, vaegir_face_middle_2],

 ["troll_3","Troll Goblin Thrower","Troll Goblin Thrower",tf_troll|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_orc,
  [itm_giant_hammer,itm_goblin_barrel,itm_troll_head_helm_1,itm_troll_feet_boots,itm_trophy_b,itm_sg_orange_big],
   str_80|agi_25|int_4|cha_4|level(40),wp(250),knows_thrown_8|knows_ironflesh_12, vaegir_face_young_1, vaegir_face_middle_2],

 ["ogre_cannon","Ogre Leadbelchers","Ogre Leadbelchers",
  tf_ogre|tf_no_capture_alive|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_orc,
   [itm_orc_greatsword,itm_ogre_bear_helmet,itm_ogre_shield,itm_ogre_armor3,itm_ogre_boots_02,
    itm_hand_cannon_2,itm_cartridges_burst,itm_cartridges_burst,itm_cartridges_burst,
    itm_dried_meat,itm_dried_meat,itm_sausages,itm_trophy_b,itm_sg_orange_small
   ],
   def_attrib|str_40|level(40),wp(200),knows_billman_5, vaegir_face_young_1, vaegir_face_middle_2],

  ["harpy_1","harpy","harpy",
   tf_female|tf_guarantee_all_footman,0,0,fac_orc,
   [
    itm_sword_khergit_3,itm_fur_covered_shield,
    itm_harpy_head_1,itm_demon_foot,
    itm_harpy_body_1,itm_sg_orange_small
   ], 
   horse_attrib_3|level(30),wp_melee(200),knows_assasin_5,berber_face_1, berber_face_2],
  ["harpy_2","Harpy_Hag","Harpy_Hag",
   tf_female|tf_guarantee_all_footman,0,0,fac_orc,
   [
    itm_sword_khergit_4,itm_fur_covered_shield,
    itm_magic_spirit_leech,itm_gold_dragon_sword,
    itm_harpy_head_2,itm_demon_foot,
    itm_harpy_body_2,itm_sg_orange_small
   ], 
   horse_attrib_3|level(30),wp_melee(200),knows_light_swordman_5,berber_face_1, berber_face_2],

  ["orc", "Orc", "Orcz", tf_orc|tf_randomize_face|tf_guarantee_boots, 0, 0, fac_orc, 
    [itm_club, itm_hatchet, itm_orc_boots], 
    foot_attrib_1|level(5),wp(50),knows_billman_1,
    0x0000000009003109207000000000000000000000001C80470000000000000000, 0x0000000B3F0061CD6D7FFBDF9DF6EBEE00000000001FFB7F0000000000000000,],
    
  ["orc_boy", "Orc Boy", "Orc Boyz", 
   tf_orc|tf_randomize_face|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, 0, 0, fac_orc, 
    [itm_orc_medarmor, itm_orc_medarmor2, itm_orcaxe2,itm_orc_spear, itm_orc_shield4, itm_orc_boots2, itm_orc_archerhelmet, itm_orc_archerhelmet], 
    foot_attrib_2|level(10),wp(90),knows_billman_2,
    0x00000003C9003109207000000000000000000000001C80470000000000000000, 0x0000000FFF0061CD6D7FFBDF9DF6EBEE00000000001FFB7F0000000000000000,],
    
  ["orc_warrior", "Orc Warrior", "Orc Warriorz", 
   tf_orc|tf_randomize_face|tf_guarantee_all_footman, 0, 0, fac_orc, 
    [itm_orc_shield4,itm_orc_armorheav, itm_orc_armorheav2, itm_orc_armour3, itm_orc_boots3, itm_orc_spear2, itm_choppa1, itm_orc_archerhelmet2, itm_orc_archerhelmet2], 
    foot_attrib_3|level(15),wp(130),knows_billman_4,
    0x00000003C9003109207000000000000000000000001C80470000000000000000, 0x0000000FFF0061CD6D7FFBDF9DF6EBEE00000000001FFB7F0000000000000000,],    
    
  ["orc_big", "Orc Big'Un", "Orc Big'Unz", 
   tf_orc|tf_randomize_face|tf_guarantee_all_footman, 0, 0, fac_orc, 
    [itm_orc_shield3, itm_orcaxe3, itm_orc_boots3, itm_orc_bigun_armour, itm_orc_bigun_armour2, itm_choppa2, itm_orcvet_helmet, itm_orcvet_helmet], 
    foot_attrib_4|level(20),wp(170),knows_physique_7|knows_shield_3|knows_power_strike_9|knows_ironflesh_6|knows_reserved_18_10|knows_weapon_master_4|knows_stealth_2|knows_magic_defence_5|knows_power_throw_3,
    0x00000007C9003109207000000000000000000000001C80470000000000000000, 0x0000000FFF0061CD6D7FFBDF9DF6EBEE00000000001FFB7F0000000000000000,],

  ["orc_blackorc", "Black Orc", "Black Orcz", 
   tf_beastman|tf_randomize_face|tf_guarantee_all_footman, 0, 0, fac_orc, 
    [ itm_choppa5,itm_orc_shield2, itm_orc_boots4, itm_blackorc, itm_choppa4, itm_orc_heavy_helm], 
    horse_attrib_3|level(25),wp(210),knows_physique_7|knows_shield_4|knows_power_strike_9|knows_ironflesh_8|knows_reserved_18_10|knows_weapon_master_6|knows_stealth_2|knows_magic_defence_7|knows_power_throw_3,
    0x00000007C9003109207000000000000000000000001C80470000000000000000, 0x0000000FFF0061CD6D7FFBDF9DF6EBEE00000000001FFB7F0000000000000000,],

  ["orc_veterun_blackorc", "Veterun Black Orc", "Veterun Black Orcz", 
   tf_beastman|tf_randomize_face|tf_guarantee_all_footman, 0, 0, fac_orc, 
    [ itm_orcaxe4,itm_orc_shield, itm_orc_heavy_boots, itm_orc_heavy_helm, itm_choppa5, itm_blackorc_vet], 
    horse_attrib_4|level(33),wp(290),knows_physique_8|knows_shield_6|knows_power_strike_11|knows_ironflesh_10|knows_reserved_18_10|knows_weapon_master_7|knows_stealth_3|knows_magic_defence_9|knows_power_throw_4,
    0x00000007C9003109207000000000000000000000001C80470000000000000000, 0x0000000FFF0061CD6D7FFBDF9DF6EBEE00000000001FFB7F0000000000000000,],

  ["orc_blackorc_boss", "Black Orc Immortul", "Black Orc Immortul", 
   tf_beastman|tf_randomize_face|tf_guarantee_all_footman, 0, 0, fac_orc, 
    [itm_blackorcboss_armour,itm_blackorcboss_armour,itm_orcaxe5,itm_choppa6,itm_orc_heavy_helm2,itm_orc_heavy_helm2, itm_tab_shield_round_e,itm_orc_heavy_boots], 
    horse_attrib_5|level(40),wp(360),knows_physique_9|knows_shield_8|knows_power_strike_13|knows_ironflesh_12|knows_reserved_18_10|knows_weapon_master_8|knows_stealth_4|knows_magic_defence_10|knows_power_throw_5,
    0x00000007C9003109207000000000000000000000001C80470000000000000000, 0x0000000FFF0061CD6D7FFBDF9DF6EBEE00000000001FFB7F0000000000000000,],



  ["orc_boar_boy", "Orc Boar Boy", "Orc Boar Boyz", 
   tf_orc|tf_randomize_face|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse, 0, 0, fac_orc, 
    [itm_org_spear_3, itm_choppa3, itm_orcboy_helmet, itm_orc_boar_armour, itm_tab_shield_round_d, itm_orc_boots4, itm_boar_mount_charge], 
    horse_attrib_2|level(22),wp(210),knows_riding_4|knows_pikeman_6,
    0x00000007C9003109207000000000000000000000001C80470000000000000000, 0x0000000FFF0061CD6D7FFBDF9DF6EBEE00000000001FFB7F0000000000000000,],

  ["orc_veteran_boar", "Orc Veterun Boar Boy", "Orc Veterun Boar Boyz", 
   tf_orc|tf_randomize_face|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse, 0, 0, fac_orc, 
    [itm_org_lance, itm_choppa4, itm_orcvet_helmet, itm_orc_boar_armour_vet, itm_tab_shield_round_e, itm_orc_heavy_boots, itm_warboar], 
    horse_attrib_3|level(28),wp(240),knows_riding_5|knows_pikeman_7,
    0x00000007C9003109207000000000000000000000001C80470000000000000000, 0x0000000FFF0061CD6D7FFBDF9DF6EBEE00000000001FFB7F0000000000000000,],

  ["orc_boar_big", "Orc Boar Big'Un", "Orc Veterun Boar Big'Un", 
   tf_orc|tf_randomize_face|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse, 0, 0, fac_orc, 
    [itm_orc_spear3,itm_choppa5,itm_orc_heavy_helm,itm_orcboss_armour2,itm_tab_shield_round_e,itm_orc_heavy_boots,itm_warboar], 
    horse_attrib_4|level(33),wp(280),knows_riding_6|knows_pikeman_8,
    0x00000007C9003109207000000000000000000000001C80470000000000000000, 0x0000000FFF0061CD6D7FFBDF9DF6EBEE00000000001FFB7F0000000000000000,],

  ["arrer_youngun", "Orc Arrer Youngun", "Orc Arrer Youngunz", 
   tf_orc|tf_randomize_face|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, 0, 0, fac_orc, 
    [itm_iron_arrow, itm_orc_armour, itm_short_bow, itm_orcaxe1, itm_orc_boots, itm_orc_archerhelmet], 
    ranged_attrib_3|level(14),wp(120),knows_physique_3|knows_shield_1|knows_power_strike_2|knows_ironflesh_2|knows_reserved_18_10|knows_weapon_master_1|knows_power_draw_5,
    0x0000000009003109207000000000000000000000001C80470000000000000000, 0x0000000B3F0061CD6D7FFBDF9DF6EBEE00000000001FFB7F0000000000000000,],

  ["orc_arrer_boy", "Orc Arrer Boy", "Orc Arrer Boyz", 
   tf_orc|tf_randomize_face|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, 0, 0, fac_orc, 
    [itm_iron_arrow, itm_long_bow, itm_orcaxe2, itm_orc_boots2, itm_orc_armour2, itm_orc_archerhelmet2], 
    ranged_attrib_4|level(19),wp(180),knows_physique_4|knows_shield_2|knows_power_strike_3|knows_ironflesh_3|knows_reserved_18_10|knows_weapon_master_2|knows_power_draw_6|knows_magic_defence_1,
    0x0000000009003109207000000000000000000000001C80470000000000000000, 0x0000000B3F0061CD6D7FFBDF9DF6EBEE00000000001FFB7F0000000000000000,],

  ["orc_veterun_arrer", "Orc Veterun Arrer Boy", "Orc Veterun Arrer Boyz", 
   tf_orc|tf_randomize_face|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, 0, 0, fac_orc, 
    [itm_flat_headed_arrows, itm_war_bow, itm_orcaxe3, itm_orc_boots3, itm_orc_armour3, itm_orcboy_helmet], 
    ranged_attrib_5|level(24),wp(240),knows_physique_6|knows_shield_6|knows_power_strike_6|knows_ironflesh_5|knows_reserved_18_10|knows_weapon_master_4|knows_power_draw_8|knows_magic_defence_6|knows_power_throw_3,
    0x0000000009003109207000000000000000000000001C80470000000000000000, 0x0000000B3F0061CD6D7FFBDF9DF6EBEE00000000001FFB7F0000000000000000,],


  ["orc_big_boss", "Orc BigBoss", "Orc BigBoss", 
   tf_beastman|tf_randomize_face|tf_guarantee_all_footman, 0, 0, fac_orc, 
    [itm_orcbigboss_armour,itm_orcbigboss_armour, itm_vk_axe,itm_chaos_axe,itm_orc_heavy_helm2, itm_steel_shield, itm_orc_heavy_boots,itm_trophy_b,itm_sg_orange_big], 
    horse_attrib_6|level(50),wp(350),knows_physique_10|knows_shield_6|knows_power_strike_15|knows_ironflesh_15|knows_reserved_18_10|knows_weapon_master_9|knows_stealth_6|knows_magic_defence_10|knows_power_throw_7,
    0x00000007C9003109207000000000000000000000001C80470000000000000000, 0x0000000FFF0061CD6D7FFBDF9DF6EBEE00000000001FFB7F0000000000000000,],

  ["woodelf_recruit","Wood Elf_recruit","Wood Elf_recruit",
   tf_male_elf|tf_guarantee_all_wo_horse,0,0,fac_forest_ranger,
   [
     itm_woodelf_arrows,itm_mirkwood_knife,itm_mirkwood_short_spear,itm_hunting_bow,
     itm_wizard_hood_2_2,
     itm_mirkwood_clothes,itm_mirkwood_clothes,
     itm_mirkwood_boots,itm_raw_grapes
   ],
   foot_attrib_3|level(12),wp_melee(100)|wp_archery(150),knows_ranger_2,mirkwood_elf_face_1,mirkwood_elf_face_2],
  ["woodelf_scout","Wood Elf Scout","Wood Elf Scout",
   tf_male_elf|tf_guarantee_all_wo_horse,0,0,fac_forest_ranger,
   [
    itm_woodelf_arrows,itm_glass_arrow,
    itm_mirkwood_knife,itm_mirkwood_knife,
    itm_long_bow,itm_hunting_bow,
    
    itm_wizard_hood_2_2,itm_wizard_hood_3,
    itm_mirkwood_armor_a,
    itm_mirkwood_boots,itm_raw_grapes
   ],
   horse_attrib_1|level(20),wp_melee(120)|wp_archery(200),knows_ranger_3,mirkwood_elf_face_1,mirkwood_elf_face_2],
  ["woodelf_hunter","Wood Elf Hunter","Wood Elf Hunter",
   tf_male_elf|tf_guarantee_all_wo_horse,0,0,fac_forest_ranger,
   [
    itm_glass_arrow,itm_woodelf_mutil_arrows,
    itm_mirkwood_sword,itm_courtblades_green,itm_mirkwood_war_spear,
    itm_long_bow,itm_long_bow_2,itm_mirkwood_spear_shield_b,

    itm_wizard_hood_3,
    itm_mirkwood_hunter,
    itm_mirkwood_boots,itm_raw_grapes
   ],
   horse_attrib_2|level(28),wp_melee(160)|wp_archery(250),knows_magic_power_1|knows_ranger_4,mirkwood_elf_face_1,mirkwood_elf_face_2],
  ["woodelf_m_hunter","Wood Elf Master Hunter","Wood Elf Master Hunter",
  tf_male_elf|tf_guarantee_all_wo_horse,0,0,fac_forest_ranger,
   [
    itm_woodelf_mutil_arrows,itm_woodelf_mutil_arrows,itm_mirkwood_bow,
    itm_courtblades_green,itm_mirkwood_war_spear,itm_mirkwood_spear_shield_c,
    
    itm_mirkwood_helm_a,
    itm_mirkwood_veteran_hunter,
    itm_mirkwood_boots,itm_trophy_a,
    
   ],
   horse_attrib_3|level(34),wp_melee(200)|wp_archery(300),knows_ranger_5|knows_magic_power_2|knows_magic_defence_4,mirkwood_elf_face_1,mirkwood_elf_face_2],
  ["woodelf_stinger","Wood Elf_stinger","Wood Elf_stinger",
   tf_male_elf|tf_guarantee_all_wo_horse,0,0,fac_forest_ranger,
   [
    itm_glass_arrow_poison,itm_mirkwood_bow,itm_glass_arrow_paralysis_cloud,
    itm_glass_sword_b,
    
    itm_mirkwood_helm_d,
    itm_mirkwood_master_hunter,
    itm_mirkwood_boots,itm_trophy_a,itm_trophy_b
   ],
   horse_attrib_4|level(42),wp_melee(200)|wp_archery(350),knows_magic_power_3|knows_ranger_6|knows_magic_defence_6,mirkwood_elf_face_1,mirkwood_elf_face_2],

  ["woodelf_sharpshooter","Wood Elf_sharpshooter","Wood Elf_sharpshooter",
   tf_male_elf|tf_guarantee_all_wo_horse,0,0,fac_forest_ranger,
   [
    itm_woodelf_arrows_amber_spear,itm_woodelf_mutil_arrows,itm_woodelf_arrows_bray_scream,
    itm_mirkwood_bow_2,itm_mirkwood_bow_2,
    itm_glass_sword_c,
    #itm_mirkwood_sword_reward,
    
    itm_mirkwood_helm_e,
    itm_mirkwood_armor_f,
    itm_mirkwood_boots,itm_trophy_b,itm_sg_green_big
   ],
   horse_attrib_5|level(50),wp_melee(250)|wp_archery(400),knows_magic_power_6|knows_ranger_7|knows_magic_defence_8,mirkwood_elf_face_1,mirkwood_elf_face_2],

  ["woodelf_druid_1","Wood Elf Druid","Wood Elf Druid",
   tf_male_elf|tf_guarantee_all_wo_horse,0,0,fac_forest_ranger,
   [
    itm_druid_staff_1,
    #itm_magic_summon_undead_near_ememy,
    itm_magic_amber_spear,
    itm_glass_sword_c,
    itm_druid_cap,itm_druid_robe_1,
    itm_mirkwood_boots,itm_trophy_c,
   ],
   horse_attrib_8|level(45),wp_melee(300)|wp_firearm(300),knows_billman_6|knows_magic_power_5|knows_magic_defence_6|knows_necromancy_6|knows_magic_skill_6,mirkwood_elf_face_1,mirkwood_elf_face_2],
  ["woodelf_druid_2","Wood Elf Druid Elder","Wood Elf Druid Elder",
   tf_male_elf|tf_guarantee_all_wo_horse,0,0,fac_forest_ranger,
   [
    itm_druid_staff_2,itm_magic_amber_spear,
    #itm_magic_summon_demon_near_ememy,
    itm_sabre_2h_green,
    itm_mirkwood_helm_e,itm_druid_robe_2,
    itm_mirkwood_boots,itm_trophy_c,
   ],
   horse_attrib_9|level(50),wp_melee(350)|wp_firearm(350),knows_billman_7|knows_magic_power_6|knows_magic_defence_8|knows_necromancy_8|knows_magic_skill_8,mirkwood_elf_face_1,mirkwood_elf_face_2],
   
  ["woodelf_watchman","Wood Elf spearman","Wood Elf spearman",
   tf_male_elf|tf_guarantee_all_footman,0,0,fac_forest_ranger,
   [
    itm_mirkwood_great_spear,itm_mirkwood_sword,
    itm_mirkwood_spear_shield_b,
    #itm_mirkwood_knife,itm_mirkwood_knife,itm_mirkwood_sword,
    
    itm_mirkwood_helm_a,
    itm_mirkwood_armor_d,
    itm_mirkwood_boots,itm_raw_grapes,
   ],
   horse_attrib_1|level(20),wp_melee(200),knows_billman_3,mirkwood_elf_face_1,mirkwood_elf_face_2],
  ["woodelf_spearman","Wood Elf Wind Dancer","Wood Elf Wind Dancer",
   tf_male_elf|tf_guarantee_all_footman,0,0,fac_forest_ranger,
   [
    itm_mirkwood_sword,
    itm_mirkwood_spear_shield_a,

    itm_mirkwood_helm_b,
    itm_mirkwood_armor_b,
    itm_mirkwood_boots,itm_wine,itm_raw_grapes,
   ],
   horse_attrib_2|level(28),wp_melee(280),knows_billman_4|knows_magic_defence_4,mirkwood_elf_face_1,mirkwood_elf_face_2],
  ["woodelf_swordman","Wood Elf War Dancer","Wood Elf War Dancer",
  tf_male_elf|tf_guarantee_all_footman,0,0,fac_forest_ranger,
   [
    itm_glass_sword_c,itm_glass_sword_a,
    itm_mirkwood_shield_d,
        
    itm_mirkwood_helm_c,
    itm_mirkwood_armor_c,
    itm_mirkwood_boots,itm_wine,itm_apples,itm_trophy_a,
    
   ],
   horse_attrib_3|level(36),wp_melee(330),knows_billman_5|knows_magic_defence_6,mirkwood_elf_face_1,mirkwood_elf_face_2],
  ["woodelf_sworddancer","Wood Elf_sworddancer","Wood Elf_sworddancer",
   tf_male_elf|tf_guarantee_all_footman,0,0,fac_forest_ranger,
   [
    itm_mirkwood_sword_reward,itm_sabre_2h_green,
    itm_glass_shield,
    itm_courtblades_green,
    
    itm_glass_head,itm_mirkwood_helm_e,
    itm_glass_female_plate,
    itm_glass_foot,itm_glass_hand,
    itm_wine,itm_sg_green_small,itm_trophy_a,itm_sg_green_small,
   ],
   horse_attrib_5|level(42),wp_melee(350),knows_billman_7|knows_magic_defence_8,mirkwood_elf_face_1,mirkwood_elf_face_2],

  ["woodelf_cavalry","Wood Elf_cavalry","Wood Elf_cavalry",
   tf_male_elf|tf_guarantee_all|tf_mounted,0,0,fac_forest_ranger,
   [
    itm_glass_lance,
    itm_glass_sword_c,itm_glass_sword_a,
    itm_glass_shield,
    
    itm_glass_head,
    itm_glass_female_plate,
    itm_glass_foot,itm_glass_hand,
    itm_pegasus,itm_pegasus,
    itm_wine,itm_sg_green_small,itm_trophy_a,itm_sg_green_small,
   ],
   horse_attrib_5|level(42),wp_melee(380),knows_riding_8|knows_twohand_7,mirkwood_elf_face_1,mirkwood_elf_face_2],

  ["grandelf_recruit","Grand Elf_recruit","Grand Elf_recruit",
   tf_male_elf|tf_guarantee_all_wo_horse,0,0,fac_elf,
   [
    itm_elven_arrow,
    itm_lorien_sword_b,itm_lorien_round_shield,
    itm_war_bow,
    
    itm_lorien_archer,itm_lorien_archer,
    itm_lorien_boots,itm_raw_olives
   ],
   horse_attrib_1|level(18),wp(140),knows_archer_3,lorien_elf_face_1,lorien_elf_face_2],
  ["grandelf_warden","Grand Elf warden","Grand Elf warden",
   tf_male_elf|tf_guarantee_all_wo_horse,0,0,fac_elf,
   [
    itm_elven_arrows,
    itm_lorien_sword_b,itm_lorien_round_shield,
    itm_lorien_bow,

    itm_lorien_helm_a,
    itm_lorien_armor_e,itm_lorien_armor_e,
    itm_lorien_boots,itm_raw_olives
   ],
   horse_attrib_2|level(26),wp_melee(160)|wp_archery(200),knows_archer_4,lorien_elf_face_1,lorien_elf_face_2],
  ["grandelf_marksman","Grand Elf marksman","Grand Elf marksman",
   tf_male_elf|tf_guarantee_all_wo_horse,0,0,fac_elf,
   [
    itm_mutil_arrow,itm_elven_arrows_burning_gaze,itm_elven_arrows_wind_blast,
    itm_lorien_bow,itm_lorien_bow,
    itm_lorien_sword_b,itm_lorien_shield_c,
    
    itm_lorien_helm_b,
    itm_lorien_armor_c,itm_lorien_armor_c,
    itm_lorien_captain_greaves,itm_trophy_a,itm_wine
    
   ],
   horse_attrib_3|level(32),wp_melee(190)|wp_archery(250),knows_magic_power_3|knows_archer_6,lorien_elf_face_1,lorien_elf_face_2],
   
   
  ["grandelf_arcane_archer","Grand Elf_Arcane Archer","Grand Elf_Arcane Archer",
   tf_male_elf|tf_guarantee_all_wo_horse,0,0,fac_elf,
   [
    itm_elven_arrows_blinding_light,itm_woodelf_arrows_freezing,itm_elven_arrows_soul_quench,itm_lorien_bow_2,
    itm_sabre_hithlain,
    
    itm_lorien_helm_b,
    itm_lorien_armor_d,itm_elf_hand,
    itm_lorien_armor_d,itm_elf_hand,
    itm_lorien_royal_greaves,itm_honey,itm_trophy_b,itm_wine,itm_sg_green_big
   ],
   horse_attrib_4|level(40),wp_melee(220)|wp_archery(300),knows_magic_power_4|knows_archer_7,lorien_elf_face_1,lorien_elf_face_2],

  ["grandelf_arcane_guard","Grand Elf Arcane Guard","Grand Elf Arcane Guard",
   tf_male_elf|tf_guarantee_all_wo_horse,0,0,fac_elf,
   [
    itm_stahlrim_mutil_arrow,itm_elven_arrows_arcane_unforging,itm_elven_arrows_net_of_amyntok,itm_elven_arrows_lightning,
    itm_lorien_bow_2,
    itm_courtblades_ivory,
    #itm_lorien_shield_b,
    
    itm_lorien_royal_archer,
    itm_lorien_reward_armor,itm_gold_elf_hand,
    itm_lorien_reward_armor,itm_gold_elf_hand,
    itm_lorien_reward_greaves,itm_trophy_b,itm_sg_green_big,itm_sg_green_big,itm_wine
   ],
   horse_attrib_5|level(48),wp_melee(410)|wp_archery(410),knows_magic_power_6|knows_swordman_8|knows_power_draw_8|knows_magic_defence_10,lorien_elf_face_1,lorien_elf_face_2],


  ["grandelf_infantry","Grand Elf infantry","Grand Elf infantry",
   tf_male_elf|tf_guarantee_all_footman,0,0,fac_elf,
   [
    itm_lorien_sword_a,itm_lorien_sword_c,itm_lorien_sword_b,
    itm_lorien_shield_b,

    itm_lorien_helm_c,itm_lorien_helm_b,
    itm_lorien_armor_a,itm_lorien_armor_a,
    itm_lorien_captain_greaves,itm_raw_olives
   ],
   horse_attrib_2|level(26),wp_melee(210),knows_swordman_4|knows_magic_defence_4,lorien_elf_face_1,lorien_elf_face_2],
  ["grandelf_swordman","Grand Elf Swordman","Grand Elf Swordman",
   tf_male_elf|tf_guarantee_all_footman,0,0,fac_elf,
   [
    itm_sabre_hithlain,
    itm_lorien_sword_c,itm_courtblades_ivory,
    itm_lorien_shield_d,
    
    itm_lorien_captain_helmet,itm_lorien_captain_helmet,
    itm_lorien_armor_b,itm_lorien_armor_f,
    itm_lorien_captain_greaves,itm_wine,itm_raw_olives
    
   ],
   horse_attrib_3|level(32),wp_melee(290),knows_swordman_5|knows_magic_defence_6,lorien_elf_face_1,lorien_elf_face_2],
  ["grandelf_swordman_adv","Grand Elf Royal Swordman","Grand Elf Royal Swordman",
   tf_male_elf|tf_guarantee_all_footman,0,0,fac_elf,
   [
    #itm_lorien_sword_c,itm_lorien_sword_a,
    #itm_courtblades_ivory,
    itm_warblade_ivorygold,
    itm_lorien_shield_e,
    
    
    itm_lorien_palace_guard_helm,itm_lorien_palace_guard_helm,
    itm_elf_plate,itm_elf_hand,
    itm_elf_foot,itm_trophy_b,itm_sg_green_small,itm_wine
   ],
   horse_attrib_4|level(40),wp_melee(350),knows_swordman_7|knows_magic_defence_8,lorien_elf_face_1,lorien_elf_face_2],

  ["grandelf_guard","Grand Elf_guard","Grand Elf_guard",
   tf_male_elf|tf_guarantee_all_footman,0,0,fac_elf,
   [
    #itm_lorien_sword_c,
    #itm_elf_glaive_a,itm_elf_glaive_b,
    #itm_lorien_sword_a,
    #itm_double_sided_sabre_2,
    itm_double_sided_sabre_2_onehand,
    itm_antimage_shield,
    
    itm_lorien_royal_helmet,
    itm_lorien_reward_armor,itm_gold_elf_hand,
    itm_lorien_reward_armor,itm_gold_elf_hand,
    itm_lorien_reward_greaves,itm_trophy_b,itm_sg_green_small,itm_sg_green_big,itm_wine
   ],
   horse_attrib_5|level(48),wp_melee(410),knows_swordman_8|knows_magic_defence_10,lorien_elf_face_1,lorien_elf_face_2],

  ["grandelf_mage_1","Grand Elf spellswoed","Grand Elf spellswoed",
   tf_male_elf|tf_guarantee_all_wo_horse,0,0,fac_elf,
   [
    itm_courtblades_ivory_1,
    itm_lorien_shield_d,
    itm_magic_soul_quench,
    itm_lorien_palace_guard_helm,itm_lorien_palace_guard_helm,
    itm_gold_elf_plate,itm_gold_elf_hand,
    itm_gold_elf_foot,itm_trophy_b,itm_wine
   ],
   horse_attrib_5|level(45),wp_melee(350)|wp_firearm(300),knows_swordman_7|knows_magic_power_5|knows_magic_defence_9|knows_necromancy_3|knows_magic_skill_5,mirkwood_elf_face_1,mirkwood_elf_face_2],
  ["grandelf_mage_2","Grand Elf Dawn Blade","Grand Elf Dawn Blade",
   tf_male_elf|tf_guarantee_all_wo_horse,0,0,fac_elf,
   [
    itm_dawnbreaker_1,itm_magic_soul_quench,

    itm_lorien_royal_helmet,
    itm_elf_twiligh_armor,itm_gold_elf_hand,
    itm_gold_elf_foot,itm_trophy_b,itm_sg_green_big,itm_wine
   ],
   str_45|agi_30|int_20|cha_12|level(60),wp_melee(450)|wp_firearm(350),knows_swordman_8|knows_magic_power_8|knows_magic_defence_10|knows_necromancy_5|knows_magic_skill_10,mirkwood_elf_face_1,mirkwood_elf_face_2],

 ["ent_1","Ancient Treant","Ancient Treant",tf_troll|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_elf,
   [
    itm_tree_trunk_invis,
    itm_ent_body,itm_ent_hands,itm_ent_feet_boots,itm_trophy_c,
    itm_ent_head_helm,itm_apples,itm_apples,itm_sg_green_small,itm_sg_yellow_big
   ],
   str_100|agi_20|int_4|cha_4|level(60),wp(200),knows_swordman_7|knows_magic_defence_10, vaegir_face_young_1, vaegir_face_middle_2],
      
 ["ent_2","Savage Treant","Savage Treant",tf_troll|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_forest_ranger,
   [
    itm_tree_trunk_invis_2,
    itm_green_ent_body,itm_green_ent_hands,itm_green_ent_feet_boots,itm_trophy_c,
    itm_green_ent_head_helm,itm_honey,itm_honey,itm_sg_green_small,itm_sg_orange_big
   ],
   str_100|agi_50|int_4|cha_4|level(60),wp(200),knows_billman_8|knows_magic_defence_9, vaegir_face_young_1, vaegir_face_middle_2],

 ["ent_3","Leshy","Leshy",tf_titan|tf_no_capture_alive|tf_guarantee_all_wo_horse,0,0,fac_forest_ranger,
   [
    itm_leshen_weapon,itm_werewolfclaw_dual_w,itm_magic_amber_spear,
    itm_leshen_weapon,itm_werewolfclaw_dual_w,itm_magic_amber_spear,
    itm_leshen_body,
    itm_demon_head,itm_demon_foot,itm_demon_hand,
    itm_trophy_c,itm_honey,itm_sg_green_small,itm_sg_orange_big
   ],
   str_100|agi_50|int_30|cha_4|level(60),wp(300),knows_physique_9|knows_shield_6|knows_power_strike_15|knows_ironflesh_9|knows_reserved_18_10|knows_weapon_master_6|knows_stealth_4|knows_magic_defence_10|knows_magic_skill_15|knows_magic_power_6, vaegir_face_young_1, vaegir_face_middle_2],


  ["grandelf_cavalry","Grand Elf_cavalry","Grand Elf_cavalry",
   tf_male_elf|tf_guarantee_all|tf_mounted,0,0,fac_elf,
   [
    #itm_lorien_sword_c,
    itm_mirkwood_great_lance,
    itm_warblade_ivorygold,
    
    #itm_lorien_sword_a,itm_courtblades_ivory,
    itm_lorien_shield_d,
    
    itm_lorien_palace_guard_helm,
    itm_elf_plate,itm_elf_hand,
    itm_elf_foot,itm_unicorn,itm_unicorn,
    itm_honey,itm_trophy_c,itm_sg_green_big,itm_wine
   ],
   horse_attrib_6|level(49),wp_melee(440),knows_riding_10|knows_twohand_6|knows_magic_defence_10,lorien_elf_face_1,lorien_elf_face_2],


  ["dwarf_miner","Dwarf Miner","Dwarf Miner",
   tf_dwarf|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_dwarf,
   [
    itm_dwarf_war_pick,itm_dwarf_pick,itm_dwarf_great_pick,
    #itm_tab_shield_round_a,
    itm_tab_shield_round_a,itm_granata_small,
    #itm_arrows,itm_hunting_bow,
    itm_erebor_tunic_1,itm_erebor_tunic_2,
    itm_dwarf_miner_helm,itm_dwarf_miner_helm,
    itm_dwarf_boots,itm_dwarf_boots,itm_iron],
   foot_attrib_3|level(7),wp(60),knows_pikeman_1|knows_magic_defence_2,nord_face_younger_1, nord_face_old_2],

  ["dwarf_warrior","Dwarf Warrior","Dwarf Warriors",
   tf_dwarf|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_dwarf,
   [
    itm_dwarf_warhammer,itm_dwarf_great_pick,
    itm_dwarf_one_handed_hammer,itm_dwarf_war_pick,
    itm_dwarf_light_shield_1,itm_dwarf_light_shield_2,
    itm_javelin,itm_light_throwing_axes,
    itm_dwarf_light_helmet_2,itm_dwarf_light_helmet_2,
    itm_erebor_padmail,itm_erebor_padmail,
    itm_dwarf_chain_boots,itm_dwarf_chain_boots,
    itm_iron
   ],
   horse_attrib_1|level(15),wp(120),knows_pikeman_2|knows_magic_defence_3,nord_face_middle_1, nord_face_older_2],
   
  ["dwarf_veteran","Dwarf Veteran","Dwarf Veterans",
   tf_dwarf|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_dwarf,
   [
    itm_dwarf_warhammer2,
    itm_dwarf_one_handed_hammer2,
    itm_dwarf_light_shield_1,itm_dwarf_light_shield_2,
    itm_javelin,itm_throwing_axes,

    itm_dwarf_light_helmet_2,itm_dwarf_light_helmet_2,
    itm_erebor_scalemail,itm_erebor_scalemail,
    itm_dwarf_scale_boots,itm_ale
   ],
   horse_attrib_2|level(23),wp(180),knows_pikeman_4,nord_face_middle_1, nord_face_older_2],
      
  ["dwarf_ironbreaker","Dwarf Iron Breaker","Dwarf Iron Breaker",
   tf_dwarf|tf_guarantee_all_footman,0,0,fac_dwarf,
   [
    itm_dwarf_warhammer3,itm_dwarf_one_handed_hammer3,
    itm_dwarf_pistol_1,itm_cartridges_burst,itm_granata_medium,
    itm_erebor_shield,itm_erebor_shield,

    itm_dwarf_heavy_helmet_2,itm_dwarf_heavy_helmet_2,
    itm_erebor_scalemail,itm_erebor_heavy_armor,
    itm_erebor_heavy_greaves,itm_iron_greaves,itm_gauntlets,itm_ale,itm_iron
   ],
   horse_attrib_3|level(31),wp(240),knows_pikeman_5|knows_stealth_4,nord_face_middle_1, nord_face_older_2],
   
  ["dwarf_bear_rider","Dwarf Bear Rider","Dwarf Bear Rider",
   tf_dwarf|tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_dwarf,
   [
    itm_dwarf_one_handed_hammer3,itm_dwarf_one_handed_hammer2,
    itm_granata_medium,itm_granata,
    itm_erebor_shield,itm_erebor_shield,

    itm_dwarf_heavy_helmet_2,itm_dwarf_heavy_helmet_2,
    itm_erebor_heavy_armor,itm_erebor_heavy_armor,
    itm_erebor_heavy_greaves,itm_iron_greaves,itm_gauntlets,itm_bear,itm_bear
   ],
   horse_attrib_5|level(40),wp(250),knows_knight_foot_2|knows_pikeman_8|knows_magic_defence_6,nord_face_middle_1, nord_face_older_2],
   
   
  ["dwarf_berserker","Dwarf Berserker","Dwarf Berserker",
   tf_dwarf|tf_guarantee_all_footman,0,0,fac_dwarf,
   [
    #itm_heavy_throwing_axes,itm_heavy_throwing_axes,
    #itm_trgwa,itm_drawf_double_axe,
    #itm_dwarf_long_axe_3,itm_dwarf_long_axe_4,
    itm_pike_2,itm_long_pike_2,itm_nord_poleaxe_1,itm_nord_poleaxe_3,

    itm_dwarf_heavy_helmet_2,itm_dwarf_heavy_helmet_2,
    itm_erebor_heavy_armor,itm_erebor_scalemail,
    itm_erebor_heavy_greaves,itm_mail_mittens,itm_ale
   ],
   horse_attrib_4|level(32),wp(250),knows_pikeman_6|knows_magic_defence_5,nord_face_middle_1, nord_face_older_2],

  ["dwarf_guard_1","Dwarf Kings Guard","Dwarf Kings Guard",
   tf_dwarf|tf_guarantee_all_footman,0,0,fac_dwarf,
   [
    itm_dwarf_long_axe_4,itm_dwarf_warhammer4,
    itm_dwarf_pistol_2,itm_dwarf_pistol_3,itm_cartridges_burst,itm_granata,
    itm_dwarf_one_handed_hammer3,
    itm_erebor_guard_shield,itm_erebor_guard_shield,

    itm_dwarf_guard_helmet_2,itm_dwarf_guard_helmet_2,
    itm_erebor_guard_armor,itm_erebor_guard_armor,
    itm_erebor_guard_greaves,itm_dwarf_gauntlets,itm_ale,itm_tools,itm_sg_blue_small,itm_trophy_a,
   ],
   horse_attrib_5|level(40),wp(300),knows_twohand_8|knows_magic_defence_8|knows_stealth_6,nord_face_middle_1, nord_face_older_2],

  ["dwarf_guard_2","Dwarf Room Guard","Dwarf Room Guard",
   tf_dwarf|tf_guarantee_all_pikeman,0,0,fac_dwarf,
   [
    itm_pike_2,itm_long_pike,itm_nord_poleaxe_2,itm_nord_poleaxe_4,

    itm_dwarf_guard_helmet_2,itm_dwarf_guard_helmet_2,
    itm_erebor_guard_armor,itm_erebor_heavy_armor,
    itm_erebor_guard_greaves,itm_dwarf_gauntlets,itm_ale,itm_tools,itm_sg_green_small,itm_trophy_a,
   ],
   horse_attrib_5|level(40),wp(300),knows_pikeman_8|knows_magic_defence_8,nord_face_middle_1, nord_face_older_2],
      
  ["dwarf_guard_3","Dwarf Champion","Dwarf Champion",
   tf_dwarf|tf_guarantee_all_footman,0,0,fac_dwarf,
   [
    itm_banshen_axe,itm_thunder_staff,
    itm_erebor_guard_shield,
    itm_dwarf_black_helmet_3,
    itm_dwarf_black_armor,itm_dwarf_black_armor,
    itm_dwarf_black_greaves,itm_dwarf_gauntlets,itm_trophy_b,itm_trophy_b,itm_sg_blue_small,itm_trophy_c,
   ],
   str_100|agi_50|int_50|cha_12|level(50),wp(400),knows_magic_power_6|knows_physique_10|knows_shield_6|knows_power_strike_13|knows_ironflesh_12|knows_stealth_5|knows_weapon_master_5|knows_magic_defence_10,nord_face_middle_1, nord_face_older_2],

  ["dwarf_musketeer_1","Dwarf Musketeer","Dwarf Musketeer",
   tf_dwarf|tf_guarantee_all_wo_horse,0,0,fac_dwarf,
   [
    itm_dwarf_axe,itm_dwarf_hand_axe,
    itm_drawf_musket_3,itm_drawf_musket_3,
    itm_cartridges_burst,itm_cartridges_burst,
    
    itm_highlander_hat1,itm_highlander_hat1,
    itm_dwarf_padtunic_1,itm_dwarf_padtunic_1,
    itm_dwarf_boots,itm_dwarf_boots
    
   ],
   foot_attrib_4|level(18),wp_melee(100)|wp_firearm(200), knows_precise_shot_4|knows_physique_2|knows_shield_2|knows_power_strike_5|knows_ironflesh_6|knows_reserved_18_10|knows_weapon_master_3|knows_magic_defence_4,nord_face_middle_1, nord_face_older_2],
      
  ["dwarf_musketeer_2_1","Dwarf Thunderer","Dwarf Thunderer",
    tf_dwarf|tf_guarantee_all_wo_horse,0,0,fac_dwarf,
   [
    itm_dwarf_fighting_axe,itm_dwarf_hand_axe,
    itm_drawf_heavy_musket_2,itm_drawf_heavy_musket_3,
    itm_cartridges_burst,itm_cartridges_burst,
    itm_highlander_hat2,itm_highlander_hat2,
    itm_dwarf_padtunic_2,itm_dwarf_padtunic_2,
    itm_dwarf_boots,itm_dwarf_boots
   ],
   foot_attrib_5|level(26),wp_melee(200)|wp_firearm (300), knows_precise_shot_6|knows_physique_3|knows_shield_3|knows_power_strike_7|knows_ironflesh_10|knows_reserved_18_10|knows_weapon_master_5|knows_stealth_5|knows_magic_defence_6, nord_face_middle_1, nord_face_older_2],
      
#  ["dwarf_musketeer_2_2","Dwarf Flame Caster","Dwarf Flame Caster",
#    tf_dwarf|tf_guarantee_all_wo_horse,0,0,fac_dwarf,
#   [
#    itm_one_handed_battle_axe_b,itm_one_handed_battle_axe_a,
#    itm_drawf_flame_caster,itm_drawf_flame_caster,
#    itm_cartridges_flame,itm_cartridges_flame,
#    itm_dwarf_mail_coif,itm_dwarf_mail_coif_mask_1,itm_dwarf_mail_coif_mask_2,
#    itm_highlander_armor3,itm_highlander_armor3_1,
#    itm_highlander_boot2,itm_highlander_boot2_1,itm_ale,itm_oil,itm_oil
#   ],
#   foot_attrib_5|level(24),wp_melee(120)|wp_firearm (250), knows_pikeman_6|knows_magic_defence_4, nord_face_middle_1, nord_face_older_2],

  ["dwarf_musketeer_2_2","Dwarf Flame Caster","Dwarf Flame Caster",
    tf_dwarf|tf_guarantee_all_wo_horse,0,0,fac_dwarf,
   [
    #itm_one_handed_battle_axe_b,itm_one_handed_battle_axe_a,
    itm_shaman_staff_1,
    itm_magic_dragon_breath,
    #itm_magic_summon_demon,itm_magic_pyroblast,itm_magic_fireball_2,
    #itm_dwarf_mail_coif,itm_dwarf_mail_coif_mask_1,itm_dwarf_mail_coif_mask_2,
    itm_highlander_hat1,itm_highlander_hat1,
    itm_dwarf_padtunic_1,itm_dwarf_padtunic_1,
    itm_dwarf_boots,itm_dwarf_boots,itm_ale,itm_sg_blue_small,itm_trophy_b,
   ],
   foot_attrib_5|level(35),wp_melee(150)|wp_firearm (250), knows_pikeman_6|knows_magic_power_7, nord_face_middle_1, nord_face_older_2],


  ["dwarf_musketeer_3","Dwarf Forge Guardian","Dwarf Forge Guardian",
    tf_dwarf|tf_guarantee_all_wo_horse,0,0,fac_dwarf,
   [
    itm_dwarf_spanner,itm_dwarf_spanner,
    #itm_drawf_musket_8barrel2,itm_cartridges_thrust,itm_cartridges_thrust,
    itm_drawf_musket_8barrel1,itm_cartridges_rar,itm_cartridges_rar,
    itm_dwarf_light_helmet_2,itm_dwarf_heavy_helmet_2,itm_dwarf_heavy_helmet_2,
    itm_erebor_padmail,itm_erebor_scalemail,itm_dwarf_scale_boots,itm_tools,itm_ale,itm_sg_blue_small,itm_trophy_a,
   ],
   foot_attrib_6|level(34),wp_one_handed(250)|wp_polearm(250)|wp_firearm(400), knows_precise_shot_8|knows_physique_4|knows_shield_4|knows_power_strike_9|knows_ironflesh_14|knows_reserved_18_10|knows_weapon_master_5|knows_stealth_7|knows_magic_defence_9, nord_face_middle_1, nord_face_older_2],



  ["giant_1","Hill Giant","Hill Giant",
   tf_titan|tf_guarantee_all_footman,0,0,fac_dwarf,
   [
    itm_dwarf_maul,
    itm_dwarven_inf_helmet1,

    itm_dwarf_padmail,itm_dwarf_tunicmail,
    itm_dwarf_chain_boots
   ],
   horse_attrib_4|level(24),wp(150),knows_pikeman_4|knows_magic_defence_6,dwarf_face_1, dwarf_face_2],
      
  ["giant_1_2","Flame Giant","Flame Giant",
   tf_titan|tf_no_capture_alive|tf_guarantee_all_footman,0,0,fac_dwarf,
   [
    itm_dwarf_maul_2,
    #itm_tab_shield_round_d,itm_tab_shield_round_c,
    #itm_javelin,itm_throwing_axes,

    itm_dwarven_inf_helmet2,itm_dwarven_inf_helmet3,

    itm_dwarf_tunicmail_2,itm_dwarven_tunicovermail,
    itm_dwarf_chain_boots
   ],
   horse_attrib_6|level(35),wp(225),knows_pikeman_5|knows_magic_defence_6,dwarf_face_2, dwarf_face_3],
  ["giant_1_3","Thunder Giant","Thunder Giant",
   tf_titan|tf_no_capture_alive|tf_guarantee_all_footman|tf_guarantee_ranged,0,0,fac_dwarf,
   [
    itm_tab_shield_round_d,itm_tab_shield_round_c,
    itm_thunder_staff,itm_sword_viking_3_small,

    itm_dwarven_inf_helmet2,

    itm_dwarf_tunicmail,
    itm_dwarf_chain_boots
   ],
   horse_attrib_6|level(35),wp(200),knows_thrown_8|knows_magic_defence_6,dwarf_face_4, dwarf_face_5],

  ["giant_2","Flame Lord","Flame Lord",
   tf_titan|tf_no_capture_alive|tf_guarantee_all_footman,0,0,fac_dwarf,
   [
    itm_dwarf_maul_3,
    #itm_tab_shield_round_d,itm_tab_shield_round_c,

    itm_dwarven_inf_helmet3,itm_dwarven_inf_helmet4,
    itm_dwarven_tunicovermail,itm_dwarven_scalemail,
    itm_dwarf_scale_boots,itm_dwarf_chain_boots,itm_gauntlets,itm_sg_blue_small,itm_sg_green_big,itm_trophy_b,
   ],
   horse_attrib_9|level(45),wp(300),knows_pikeman_8|knows_magic_defence_6,dwarf_face_5, dwarf_face_6],
   
  ["giant_3","Thunder Thane","Thunder Thane",
   tf_titan|tf_no_capture_alive|tf_guarantee_all_footman|tf_guarantee_ranged,0,0,fac_dwarf,
   [
   
    itm_banshen_shield,itm_banshen_shield,
    itm_dwarf_thunder_maul,itm_dwarf_thunder_maul_melee,

    itm_dwarven_inf_helmet3,
    itm_dwarf_scalemail,
    itm_dwarf_scale_boots,itm_gauntlets,itm_sg_blue_big,itm_sg_blue_small,itm_trophy_b,
   ],
   horse_attrib_9|level(45),wp(250),knows_thrown_7|knows_magic_power_5|knows_magic_defence_6,dwarf_face_6, dwarf_face_7],

  ["se_tribesman","SE Tribesman","SE Tribesmen",tf_undead|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_undeads_2,
   [itm_sword_khergit_1,itm_hand_axe,itm_sword_medieval_a,itm_sword_medieval_c,itm_fur_covered_shield,itm_javelin,
    itm_skeleton_body_1,itm_wrapping_boots
   ],
   foot_attrib_2|level(6),wp(60),knows_thrown_1,latin_face_1, latin_face_2],
      
  ["se_skirmisher","SE Skirmisher","SE Skirmishers",
   tf_undead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_undeads_2,
   [itm_sword_medieval_c,itm_undead_sword_1,itm_fighting_axe,
    itm_javelin,itm_nord_javelin,
    itm_fur_covered_shield,itm_wooden_shield,
    itm_nordic_archer_helmet,itm_hood_c,
    itm_skeleton_body_1,
    itm_wrapping_boots
   ],
   foot_attrib_3|level(12),wp_melee(80)|wp_throwing(120),knows_thrown_2,latin_face_1, latin_face_2],
      
      
  ["se_musketeer_1","SE Musketeer","SE Musketeer",
   tf_undead|tf_guarantee_all_wo_horse,0,0,fac_undeads_2,
   [
    itm_sword_medieval_c,itm_undead_sword_1,
    itm_hunting_bow,itm_short_bow,itm_long_bow,itm_long_bow,
    itm_arrows,itm_undead_arrow,itm_combed_morion,
    itm_skeleton_body_1,itm_skeleton_body_2,itm_leather_boots
   ],
   foot_attrib_4|level(18),wp_melee(100)|wp_archery(180), knows_archer_3,latin_face_1, latin_face_2],
   
  ["se_musketeer_2","SE Veteran Musketeer","SE Veteran Musketeer",
    tf_undead|tf_guarantee_all_wo_horse,0,0,fac_undeads_2,
   [
    itm_undead_sword_1,itm_undead_axe,
    itm_undead_arrow,itm_undead_arrow,
    itm_skeletonbow,itm_skeletonbow,
    itm_combed_morion,
    itm_skeleton_body_2,itm_skeleton_body_3,itm_splinted_leather_greaves
   ],
   foot_attrib_5|level(24),wp_melee(120)|wp_archery (210), knows_archer_4, latin_face_1, latin_face_2],
   
  ["se_billman_1","SE billman","SE billman",
   tf_undead|tf_guarantee_all_footman,0,0,fac_undeads_2,
   [
    itm_undead_sword_2,itm_undead_sword_1,
    itm_nordic_shield,itm_nordic_shield,itm_nordic_shield,
    itm_undead_sword_two_handed_1,
    itm_kettle_hat_cloth3,itm_kettle_hat_mail3,itm_barbutte,
    itm_skeleton_body_3,itm_skeleton_body_3,
    itm_narf_hose,itm_hose_kneecops_green,itm_leather_gloves
   ],
   foot_attrib_4|level(18),wp_melee(120), knows_swordman_3, latin_face_1, latin_face_2],
   
  ["se_billman_2","SE Veteran billman","SE Veteran billman",
  tf_undead|tf_guarantee_all_footman,0,0,fac_undeads_2,
   [
    itm_undead_axe,itm_undead_sword_2,itm_undead_scimitar,
    itm_plate_covered_round_shield,itm_plate_covered_round_shield,itm_plate_covered_round_shield,
    itm_undead_sword_two_handed_2,
    itm_barbutte,itm_barbutte_coif,
    itm_skeleton_body_5,itm_skeleton_body_5,

    itm_splinted_leather_greaves,itm_splinted_greaves,itm_wisby_gauntlets_black],
    
   foot_attrib_5|level(24),wp_melee(150), knows_swordman_4, latin_face_1, latin_face_2],
   
  ["se_pikeman_1","SE spearman","SE spearman",
   tf_undead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_undeads_2,
   [
    itm_skeleton_pike_melee,itm_pike_2,itm_long_voulge,
    
    itm_kettle_hat_cloth2,itm_kettle_hat_cloth3,
    itm_skeleton_body_1,itm_skeleton_body_1,
    itm_narf_hose],
   foot_attrib_3|level(12),wp_melee(90),knows_spearman_2,latin_face_1, latin_face_2],
  ["se_pikeman_2","SE Pikeman","SE Pikeman",
   tf_undead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_undeads_2,
   [itm_long_pike,itm_pike_2,itm_swiss_halberd,itm_nord_poleaxe_1,
    itm_sword_medieval_c_small,
    itm_kettle_hat_cloth1,itm_kettle_hat_mail2,itm_kettle_hat_cloth3,
    itm_skeleton_body_2,itm_skeleton_body_4,
    itm_hose_kneecops_green,itm_narf_hose,itm_leather_gloves],
   foot_attrib_4|level(18),wp_melee(100)|wp_polearm (140), knows_pikeman_3, latin_face_1, latin_face_2],
  ["se_pikeman_3","SE Veteran Pikeman","SE Veteran Pikeman",
   tf_undead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_undeads_2,
   [itm_pike_2,itm_skeleton_pike_melee,itm_nord_poleaxe_2,itm_nord_poleaxe_3,
    itm_sword_medieval_c_small,
    itm_barbutte,itm_barbutte,itm_kettle_hat_mail3,
    itm_skeleton_body_4,itm_skeleton_body_4,
    itm_hose_kneecops_green,itm_leather_gloves],
   foot_attrib_5|level(24),wp_melee(120)|wp_polearm (190) ,knows_pikeman_4, latin_face_1, latin_face_2],

  ["zombie_1","Zombie","Zombie",
   tf_undead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_undeads_2,
   [
    itm_hatchet,itm_falchion,itm_stones,
    itm_spiked_mace,itm_sword_viking_1,itm_falchion,
    itm_undeadface_f, itm_undead_body_f, itm_undead_foots_f, itm_leather_gloves
   ],
   str_20|agi_10|int_3|cha_3|level(15),wp(50),knows_shield_10|knows_power_strike_2|knows_ironflesh_10|knows_weapon_master_2|knows_magic_defence_1,nord_face_middle_1, nord_face_older_2],

  ["zombie_2","Zombie","Zombie",
   tf_undead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_undeads_2,
   [
    itm_spiked_mace,itm_undead_sword_1,itm_sword_medieval_a,itm_undead_axe,
    itm_undeadface_gr, itm_undead_body_gr, itm_undead_foots_gr, itm_leather_gloves
   ],
   str_30|agi_10|int_3|cha_3|level(25),wp(100),knows_shield_10|knows_power_strike_3|knows_ironflesh_15|knows_weapon_master_4|knows_magic_defence_3,nord_face_middle_1, nord_face_older_2],

  ["zombie_3","Crypt Ghouls","Crypt Ghouls",
   tf_vampire|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_undeads_2,
   [
    itm_plate_covered_round_shield,itm_undead_sword_2,itm_undead_scimitar,itm_undead_axe,

    itm_undeadface_mohrg,itm_undead_body_mohrg,
    itm_undeadface_mohrg,itm_undead_body_mohrg,
    itm_leather_boots,itm_draugr_hand,
   ],
   str_50|agi_30|int_3|cha_3|level(35),wp(100),knows_shield_10|knows_power_strike_7|knows_ironflesh_10|knows_weapon_master_4|knows_magic_defence_5,nord_face_middle_1, nord_face_older_2],

  ["zombie_4","Zombie Warrior","Zombie Warrior",
   tf_undead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_undeads_2,
   [
    itm_plate_covered_round_shield,itm_undead_shield_kite_cav,
    itm_ebony_axe,itm_undead_axe,

    itm_draugr_body_3, itm_draugr_body_4, 
    itm_draugr_head_4,itm_draugr_head_5,
    itm_leather_boots,itm_draugr_hand,
   ],
   str_50|agi_30|int_3|cha_3|level(35),wp(200),knows_shield_10|knows_power_strike_3|knows_ironflesh_15|knows_weapon_master_4|knows_magic_defence_7,nord_face_middle_1, nord_face_older_2],

  ["zombie_5","Crypt Horrors","Crypt Horrors",
   tf_vampire|tf_guarantee_all_footman, 0, 0, fac_undeads_2, 
   [
    itm_werewolfclaw,itm_werewolfclaw_dual,
    itm_demon_zombie,itm_trophy_b,
    itm_demon_foot,itm_demon_head,itm_demon_hand,itm_sg_black_big,itm_sg_black_big
   ],
   horse_attrib_6|level(45),wp_melee(300),knows_physique_6|knows_power_strike_9|knows_ironflesh_15|knows_reserved_18_10|knows_weapon_master_4|knows_stealth_2|knows_magic_defence_8,nord_face_middle_1, nord_face_older_2],

  ["zombie_6","Vargheists","Vargheists",
   tf_vampire|tf_guarantee_all_footman, 0, 0, fac_undeads_2, 
   [
    itm_werewolfclaw,itm_werewolfclaw_dual,
    itm_lobo_body,itm_trophy_b,
    itm_demon_foot,itm_demon_head,itm_demon_hand,itm_sg_black_big,itm_sg_black_big
   ],
   horse_attrib_6|level(45),wp_melee(300),knows_physique_10|knows_power_strike_9|knows_ironflesh_10|knows_reserved_18_10|knows_stealth_8|knows_magic_defence_7,nord_face_middle_1, nord_face_older_2],

  ["skeleton_spearman","Grave_guard spearman","Grave_guard spearman",
   tf_undead|tf_mounted|tf_guarantee_all_wo_ranged|tf_guarantee_horse,0,0,fac_undeads_2,
   [
    itm_ebony_throwing_pike,itm_ebony_throwing_pike,
    itm_ebony_scimitar_2,itm_undead_shield_kite_cav,
    itm_rhun_helm_4,itm_rhun_helm_5,
    itm_skeleton_armor_1,itm_black_greaves,itm_leather_gloves,
    itm_undead_charger_2,itm_undead_charger_2
   ],
   horse_attrib_5|level(30),wp(300),knows_riding_4|knows_pikeman_7|knows_magic_defence_5|knows_power_throw_4,nord_face_middle_1, nord_face_older_2],


  ["skeleton_halberd","Grave_guard halberd","Grave_guard halberd",
   tf_undead|tf_guarantee_all_footman,0,0,fac_undeads_2,
   [
    itm_ebony_poleaxe,itm_ebony_poleaxe,
    itm_ebony_pike_melee,itm_ebony_pike_melee,
    itm_rhun_helm_4,itm_rhun_helm_5,
    itm_skeleton_armor_2,itm_black_greaves,itm_leather_gloves,
   ],
   horse_attrib_5|level(30),wp(280),knows_pikeman_7|knows_magic_defence_5,nord_face_middle_1, nord_face_older_2],
   
  ["skeleton_warrior","Grave_guard Warrior","Grave_guard Warriors",
   tf_undead|tf_guarantee_all_footman,0,0,fac_undeads_2,
   [
    itm_undead_axe,itm_undead_sword_two_handed_2,
    itm_undead_scimitar,itm_undead_sword_two_handed_3,
    itm_undead_shield_kite_cav,itm_undead_shield_kite_cav,

    itm_rhun_helm_5,itm_rhun_helm_4,
    itm_skeleton_armor_3,itm_black_greaves,itm_leather_gloves,
    #itm_skeleton_body_3
   ],
   horse_attrib_4|level(30),wp(280),knows_swordman_6|knows_magic_defence_7,nord_face_middle_1, nord_face_older_2],
   
  ["skeleton_archer","skeleton Archer","skeleton Archer",
   tf_undead|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_undeads_2,
   [
    itm_undead_scimitar,
    itm_mutil_arrow_2,itm_mutil_arrow_2,itm_evil_arrow_2,
    itm_black_bow,itm_black_bow,

    itm_rhun_helm_4,itm_rhun_helm_4,
    itm_skeleton_body_3,itm_skeleton_body_2,itm_skeleton_body_2,itm_leather_gloves,
   ],
   foot_attrib_5|level(30),wp_melee(200)|wp_archery(290), knows_magic_power_3|knows_archer_6|knows_magic_defence_5,nord_face_middle_1, nord_face_older_2],

  ["skeleton_lord","skeleton Lord","skeleton Lord",
   tf_undead|tf_no_capture_alive|tf_guarantee_all_footman,0,0,fac_undeads_2,
   [
    itm_undead_scimitar,itm_ebony_scimitar_long_3,
    itm_ebony_axe,itm_undead_double_axe,
    itm_black_shield,itm_ebony_javelin,itm_ebony_javelin,
    
    itm_rhun_helm_6,itm_rhun_helm_6,
    #itm_visored_bascinet_1,
    itm_black_plate_armor,itm_trophy_a,
    itm_black_greaves,itm_gauntlets],
   horse_attrib_6|level(40),wp(350),knows_swordman_8|knows_thrown_5|knows_magic_defence_9,nord_face_middle_1, nord_face_older_2],
   
  ["skeleton_cav","skeleton","skeleton",
   tf_undead|tf_mounted|tf_guarantee_all_wo_ranged|tf_guarantee_horse,0,0,fac_undeads_2,
   [
    itm_gothic_lance,itm_great_lance_dark,
    itm_ebony_scimitar_2,itm_death_knight_shield,
    itm_rhun_helm_6,itm_rhun_helm_6,
    itm_black_plate_armor_2,itm_black_greaves,itm_gauntlets,itm_trophy_a,
    itm_undead_charger_2,itm_undead_charger_2
   ],
   horse_attrib_6|level(40),wp(350),knows_riding_4|knows_physique_4|knows_shield_5|knows_power_strike_10|knows_ironflesh_15|knows_reserved_18_10|knows_weapon_master_6|knows_magic_defence_9,nord_face_middle_1, nord_face_older_2],

   
  ["draugr_1","Draugr","Draugr",
   tf_undead|tf_guarantee_all_footman,0,0,fac_kingdom_10,
   [
    itm_one_handed_war_axe_b,itm_sword_viking_2,itm_stones,
    itm_one_handed_battle_axe_a,itm_sword_viking_1,itm_falchion,
    
    itm_draugr_body_1, itm_draugr_body_2, 
    itm_draugr_head_0,itm_draugr_head_1,
    itm_leather_boots,itm_draugr_hand,
   ],
   str_15|agi_10|int_3|cha_3|level(15),wp(100),knows_thrown_4|knows_power_draw_3|knows_magic_defence_4,nord_face_middle_1, nord_face_older_2],


  ["draugr_2","Draugr Wight","Draugr Wight",
   tf_undead|tf_guarantee_all_footman,0,0,fac_kingdom_10,
   [
    itm_sword_viking_3,itm_nordhero_axe_1,itm_nordhero_long_axe,
    itm_tab_shield_round_e,itm_throwing_spears,itm_long_axe_b_alt,
    itm_undead_arrow,itm_nord_bow_1,
    itm_draugr_body_2, itm_draugr_body_3, 
    itm_draugr_head_2,itm_draugr_head_3,
    itm_splinted_leather_greaves, itm_draugr_hand,
   ],
   str_30|agi_10|int_3|cha_3|level(25),wp(175),knows_twohand_3|knows_power_draw_3|knows_magic_defence_6,nord_face_middle_1, nord_face_older_2],
      
  ["draugr_3","Draugr Scourge","Draugr Scourge",
   tf_undead|tf_guarantee_all_footman,0,0,fac_kingdom_10,
   [
    itm_nordhero_sword,itm_nordhero_axe_2,itm_nordhero_greatsword,itm_nordhero_long_axe,
    itm_tab_shield_round_d,itm_nord_throwing_spears,
    itm_mutil_arrow_2,itm_nord_bow_2,itm_nordic_arrow,
    itm_draugr_body_3, itm_draugr_body_4, 
    itm_draugr_head_4,itm_draugr_head_5,
    itm_mail_boots, itm_mail_mittens
   ],
   str_45|agi_18|int_3|cha_3|level(35),wp(250),knows_twohand_5|knows_thrown_6|knows_power_draw_5|knows_magic_power_2|knows_magic_defence_8,nord_face_middle_1, nord_face_older_2],

  ["draugr_lord","draugr death overlord","draugr death overlord",
   tf_undead|tf_guarantee_all_footman,0,0,fac_kingdom_10,
   [
    itm_nordhero_sword_long,itm_nordhero_greatsword_2,itm_nordhero_long_axe_2,
    itm_ebony_axe,itm_ebony_great_sword_2,
    itm_nord_bow_2,itm_ebony_bow,itm_mutil_arrow_2,itm_ebony_arrow,itm_undead_arrow_spirit_leech,
    itm_black_shield,
    
    itm_death_lord_helm,itm_death_lord_helm,
    itm_rhun_armor_7,itm_rhun_armor_8,itm_trophy_a,
    itm_chaos_leg_2,itm_chaos_gauntlets],
   str_60|agi_18|int_3|cha_3|level(45),wp(350),knows_twohand_7|knows_magic_power_3|knows_archer_5|knows_magic_defence_10,nord_face_middle_1, nord_face_older_2],

  ["dullahan", "Dullahan", "Dullahan", 
   tf_vampire|tf_no_capture_alive|tf_guarantee_all_footman, 0, 0, fac_undeads_2, 
   [
    itm_ebony_axe,itm_ebony_arming_sword,itm_ebony_great_sword_2,itm_ebony_great_sword,
    itm_undead_shield_kite_cav,itm_undead_shield_kite_cav,
    
    itm_black_plate_armor_2,itm_black_plate_armor_2,
    itm_demon_head,
    itm_black_greaves,itm_gauntlets,
    itm_velvet,itm_sg_black_small,itm_trophy_b,
   ], 
   horse_attrib_5|level(40), wp_melee(300), knows_knight_3|knows_twohand_6|knows_magic_defence_10, swadian_face_young_1, swadian_face_young_1 ],

  ["mummy_1","mummy","mummy",
   tf_undead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_demon,
   [
    itm_dummy_weapon_2_hand,
    itm_mummy_hand,itm_mummyhead,itm_mummy_body,itm_mummy_calf,itm_linen
   ],
   horse_attrib_3|level(15),wp(145),knows_physique_2|knows_shield_5|knows_power_strike_3|knows_ironflesh_6|knows_weapon_master_4|knows_magic_defence_4,nord_face_middle_1, nord_face_older_2],

  ["mummy_2","mummy Warrior","mummy Warrior",
   tf_undead|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_demon,
   [
    itm_tomb_sword,itm_tomb_shield,
    itm_tomb_knighthelm,itm_tomb_knightfull,
    itm_mummy_hand,itm_mummy_body,itm_mummy_calf,itm_linen,itm_velvet
   ],
   horse_attrib_4|level(25),wp(200),knows_physique_3|knows_shield_6|knows_power_strike_3|knows_ironflesh_8|knows_weapon_master_6|knows_magic_defence_6,nord_face_middle_1, nord_face_older_2],


  ["mummy_3","mummy King","mummy King",
   tf_undead|tf_no_capture_alive|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_demon,
   [itm_lich_staff_1,itm_tomb_axe2,
    #itm_magic_summon_undead_near_ememy,
    itm_magic_spirit_leech,
   
    #itm_mummy_staff,
    itm_tomb_king_helmet,itm_trophy_b,
    itm_mummy_hand,itm_bloodguard_body,itm_demon_foot,itm_linen,itm_spice,itm_velvet,itm_sg_black_small,itm_sg_black_small,
   ],
   horse_attrib_5|level(45),wp(250),knows_swordman_7|knows_magic_7|knows_magic_defence_8,nord_face_middle_1, nord_face_older_2],  
      
  ["mummy_2_1","Werewolf mummy","Werewolf mummy",
   tf_titan|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_demon,
   [
    itm_tomb_axe2,itm_tomb_sword,itm_tomb_shield,
    itm_weak_ushabti_body,
    itm_demon_head,itm_demon_foot,itm_ushabti_hands,itm_trophy_a,
    itm_furs,itm_spice
   ],
   horse_attrib_6|level(40),wp(300),knows_physique_8|knows_shield_5|knows_power_strike_13|knows_ironflesh_12|knows_reserved_18_10|knows_weapon_master_6|knows_stealth_3|knows_magic_defence_6,nord_face_middle_1, nord_face_older_2],

  ["mummy_2_2","Werewolf mummy","Werewolf mummy",
   tf_titan|tf_no_capture_alive|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_demon,
   [
    itm_tomb_axe,itm_ebony_bow,itm_demon_arrow,itm_ebony_arrow,
    itm_weak_ushabti_body,
    itm_demon_head,itm_demon_foot,itm_ushabti_hands,itm_trophy_a,
    itm_furs,itm_spice
   ],
   horse_attrib_6|level(40),wp(300),knows_physique_6|knows_power_strike_6|knows_ironflesh_8|knows_weapon_master_6|knows_magic_defence_6,nord_face_middle_1, nord_face_older_2],
  ["mummy_2_3", "Anubis", "Anubis", 
   tf_titan|tf_no_capture_alive|tf_guarantee_ranged|tf_guarantee_all_footman, 0, 0, fac_demon, 
   [
    itm_hurricane_bow,itm_destroyer,itm_demon_arrow,itm_demon_arrow,
    itm_demon_head,itm_demon_foot,itm_ushabti_hands,itm_trophy_c,
    itm_ushabti_body,itm_sg_black_big,itm_sg_black_big
   ], 
  horse_attrib_8|level(60), wp(300), knows_twohand_8|knows_magic_7|knows_magic_defence_10, nord_face_young_1, swadian_face_older_2 ],
      
  ["mummy_4", "Anubis", "Anubis", 
   tf_titan|tf_no_capture_alive|tf_guarantee_ranged|tf_guarantee_all_footman, 0, 0, fac_demon, 
   [
    itm_venom_staff_1,itm_destroyer,itm_magic_spirit_leech,
    itm_demon_head,itm_demon_foot,itm_ushabti_hands,itm_trophy_c,
    itm_ushabti_body,itm_sg_black_big,itm_sg_black_big
   ], 
  horse_attrib_8|level(60), wp(300), knows_twohand_8|knows_magic_7|knows_magic_defence_10, nord_face_young_1, swadian_face_older_2 ],
      
  ["lich_3", "Dragon Priest", "Dragon Priest", 
  tf_undead|tf_guarantee_ranged|tf_guarantee_all_footman,0,0,fac_kingdom_10,
   [itm_dragonpriest_staff_1,itm_stalhrim_greatsword,
    #itm_magic_summon_undead_near_ememy,
    itm_magic_lightning,

    itm_twilight_boots,itm_draugr_hand,
    itm_dragonpriest_armor,itm_dragonpriest_helm_1,
    itm_velvet,itm_trophy_c,itm_sg_black_big,], 
   horse_attrib_6|level(60), wp_melee(300)|wp_firearm(300), knows_twohand_7|knows_magic_8|knows_magic_defence_8, euro_face_3, euro_face_4 ],
                      
["vampire_assassin","Townsman","Townsmen",
  tf_vampire|tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_undeads_2,
  [
   itm_ebony_scimitar_1,itm_ebony_long_sword,
   itm_vampiehelm_0,itm_xenoargh_hornmask_black,
   itm_vampire_tunic,
   itm_undead_shield_kite_cav,itm_undead_shield_kite_cav,
   itm_leather_boots,
  ],
   horse_attrib_3|level(20), wp_melee(250), knows_vampire_1|knows_light_swordman_3, swadian_face_young_1, swadian_face_young_1 ],
      
 ["undead_magic_2","Necromancer","Necromancer",
  tf_vampire|tf_guarantee_ranged|tf_no_capture_alive|tf_guarantee_all_footman,0,0,fac_undeads_2,
   [
    itm_skull_staff,
    #itm_magic_summon_undead,
    itm_magic_spirit_leech,

    itm_vampire_tunic,itm_leather_boots,itm_leather_gloves,itm_vampiehelm_0,itm_vampiehelm_0],
   horse_attrib_4|level(30),wp_melee(120)|wp_firearm(200),knows_vampire_2|knows_magic_3,euro_face_3, euro_face_4],

 ["lich_1","Lich","Lich",
  tf_undead|tf_no_capture_alive|tf_guarantee_ranged|tf_guarantee_all_footman,0,0,fac_undeads_2,
   [itm_archlich_staff_1,
    itm_magic_spirit_leech,

    itm_lich_armor,itm_gauntlets,itm_iron_greaves,itm_scull_head,itm_demon_hood,itm_sg_black_big,itm_trophy_b,itm_demon_hood],
   foot_attrib_4|level(40),wp_melee(120)|wp_firearm(250),knows_vampire_3|knows_magic_5, euro_face_4],
  ["lich_2", "Archlich", "Archlich", 
  tf_undead|tf_no_capture_alive|tf_guarantee_ranged|tf_guarantee_all_footman,0,0,fac_undeads_2,
   [itm_archlich_staff_1,
    itm_magic_gaze_of_nagash,

    itm_twilight_boots,itm_twilight_gloves,itm_archlich_armor,itm_lich_helm,itm_crown,itm_velvet,itm_trophy_c,itm_sg_black_big,], 
   foot_attrib_5|level(50), wp_melee(140)|wp_firearm(300), knows_vampire_4|knows_magic_7, euro_face_3, euro_face_4 ],




  ["vampire_1", "vampire young", "vampire young", 
   tf_vampire|tf_no_capture_alive|tf_guarantee_all_footman, 0, 0, fac_undeads_2, 
   [
    itm_ebony_arming_sword,itm_ebony_bastard_sword,
    itm_black_shield,itm_black_shield,
    itm_vampire_armor_1,itm_vampire_armor_2,itm_vampire_armor_1,
    itm_iron_greaves,itm_black_helmet,itm_black_helmet,
    ], 
   horse_attrib_4|level(20), wp_melee(250), knows_vampire_4|knows_light_swordman_4, swadian_face_young_1, swadian_face_young_1 ],
   
   
   
  ["vampire_2", "vampire", "vampire", 
   tf_vampire|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet, 0, 0, fac_undeads_2, 
   [
    #itm_knightaxe,itm_bastard_sword_f,itm_morningstar,
    itm_ebony_bastard_sword,itm_ebony_scimitar_long_1,
    
    itm_twilight_boots,itm_twilight_gloves,itm_vampire_armor_3,itm_vampire_armor_3,itm_xenoargh_mask_black,
    itm_velvet,itm_sg_black_small,itm_trophy_a,
   ], 
   horse_attrib_5|level(30), wp_melee(300), knows_vampire_5|knows_light_swordman_5, swadian_face_young_1, swadian_face_young_1 ],
  ["vampire_3", "vampire Lord", "vampire Lord", 
   tf_vampire|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet, 0, 0, fac_undeads_2, 
   [
    itm_ebony_great_sword_2,itm_ebony_scimitar_long_3,
    itm_vampire_armor_4,itm_vampire_armor_4,itm_twilight_boots,itm_lich_helm,itm_twilight_gloves,
    itm_velvet,itm_sg_black_big,itm_trophy_b,
   ], 
  horse_attrib_7|level(40), wp_melee(350), knows_stealth_6|knows_physique_6|knows_shield_6|knows_power_strike_7|knows_ironflesh_10|knows_reserved_18_10|knows_weapon_master_6|knows_magic_defence_7, nord_face_young_1, swadian_face_older_2 ],
  
  
  ["vampire_4", "Vampire Prince", "vampire Prince", 
   tf_vampire|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet, 0, 0, fac_undeads_2, 
   [
    itm_ebony_great_sword,
    itm_twiligh_armor,itm_twilight_boots,itm_twilight_helm,itm_twilight_gloves,
    itm_velvet,itm_sg_black_big,itm_trophy_b,
   ], 
  horse_attrib_9|level(50), wp_melee(400), knows_stealth_8|knows_physique_8|knows_shield_8|knows_power_strike_9|knows_ironflesh_13|knows_reserved_18_10|knows_weapon_master_8|knows_magic_defence_9, nord_face_young_1, swadian_face_older_2 ],
  
  ["undead_horse_1", "Dark Knight", "Dark Knights", 
   tf_vampire|tf_mounted|tf_guarantee_all_wo_ranged|tf_guarantee_horse, 0, 0, fac_undeads_2, 
   [
    #itm_heavy_lance,
    itm_ebony_scimitar_2,itm_undead_shield_kite_cav,
    itm_ebony_scimitar_long_2,itm_ebony_bastard_sword,
    itm_black_plate_armor_1,itm_black_plate_armor_2,
    itm_gauntlets,itm_black_greaves,
    itm_undead_great_helmet,itm_undead_great_helmet,itm_undead_winged_great_helmet,
    itm_undead_charger_2,itm_undead_charger_2,itm_sg_black_small
   ], 
   horse_attrib_5|level(30), wp_melee(300), knows_riding_3|knows_vampire_5|knows_light_swordman_4, swadian_face_young_1, swadian_face_young_1 ],

  ["undead_horse_2", "Dread Knight", "Dread Knights", 
   tf_vampire|tf_mounted|tf_guarantee_all_wo_ranged|tf_guarantee_horse, 0, 0, fac_undeads_2, 
   [
    #itm_gothic_lance,
    itm_ebony_long_mace,itm_ebony_long_sword,
    itm_death_knight_shield,itm_death_knight_shield,

    itm_ebony_double_axe,itm_ebony_great_sword,
    itm_death_knight_plate,itm_death_knight_plate,
    itm_death_knight_head,itm_undead_winged_great_helmet,
    itm_death_knight_foot,itm_death_knight_hand,
    
    itm_trophy_b,
    itm_undead_charger_plate,itm_undead_charger_plate,itm_velvet,itm_sg_black_small,
   ], 
   horse_attrib_7|level(40), wp_melee(350), knows_riding_5|knows_stealth_6|knows_physique_6|knows_shield_6|knows_power_strike_10|knows_ironflesh_10|knows_reserved_18_10|knows_weapon_master_6|knows_magic_defence_7, swadian_face_young_1, swadian_face_young_1 ],
   
  ["undead_horse_3", "Dark Champion", "Dark Champion", 
   tf_vampire|tf_mounted|tf_guarantee_all_wo_ranged|tf_guarantee_horse, 0, 0, fac_undeads_2, 
   [#itm_great_lance_dark,
    itm_undead_scythe,
    #itm_undead_scimitar_long_2,itm_death_knight_shield,
    #itm_undead_scimitar_long_2,itm_death_knight_shield,
    #itm_undead_double_axe,
    itm_black_knight_plate,
    itm_black_knight_foot,
    itm_nazgul_hood_1,#itm_twilight_helm,
    itm_black_knight_hand,itm_trophy_c,
    itm_undead_charger,itm_undead_charger,itm_velvet,itm_sg_black_big], 
  horse_attrib_9|level(50), wp_melee(400), knows_riding_7|knows_stealth_8|knows_physique_7|knows_shield_7|knows_power_strike_12|knows_ironflesh_12|knows_reserved_18_10|knows_weapon_master_9|knows_magic_defence_9, nord_face_young_1, swadian_face_older_2 ],
  

  ["ghost", "ghost", "ghost", 
   tf_vampire|tf_guarantee_all_footman, 0, 0, fac_undeads_2, 
   [
    itm_werewolfclaw,itm_werewolfclaw_dual,
    itm_death_head,itm_demon_foot,itm_death_hand,
    itm_wight_body_low
   ], 
  horse_attrib_2|level(20), wp_melee(150), knows_assasin_3, nord_face_young_1, swadian_face_older_2 ],

  ["wight", "Wight", "Wight", 
   tf_vampire|tf_guarantee_all_footman, 0, 0, fac_undeads_2, 
   [
    itm_werewolfclaw_w,itm_werewolfclaw_dual_w,
    itm_demon_head,itm_demon_foot,itm_death_hand,
    itm_wight_body,itm_sg_black_small,itm_sg_black_small
   ], 
  horse_attrib_3|level(30), wp_melee(200), knows_assasin_5, nord_face_young_1, swadian_face_older_2 ],

  ["wraith", "Wraith", "Wraith", 
   tf_titan|tf_guarantee_all_footman, 0, 0, fac_undeads_2, 
   [
    itm_death_scythe,
    #itm_steel_shield,itm_steel_shield,
    itm_death_body,itm_trophy_b,
    itm_demon_foot,itm_death_head,itm_death_hand,itm_sg_black_big,itm_sg_black_big
   ], 
  horse_attrib_6|level(45), wp_melee(300), knows_physique_6|knows_shield_4|knows_power_strike_9|knows_ironflesh_8|knows_reserved_18_10|knows_weapon_master_4|knows_stealth_2|knows_magic_defence_6, nord_face_young_1, swadian_face_older_2 ],

  ["death", "Reaper", "Reaper", 
   tf_titan|tf_guarantee_all_footman, 0, 0, fac_undeads_2, 
   [
    itm_death_scythe,
    #itm_steel_shield,itm_steel_shield,
    itm_demon_head,itm_demon_foot,itm_death_grip,itm_trophy_c,
    itm_wraith_body,itm_sg_black_big,itm_sg_black_big
   ], 
  horse_attrib_7|level(60), wp_melee(400), knows_physique_8|knows_shield_5|knows_power_strike_13|knows_ironflesh_12|knows_reserved_18_10|knows_weapon_master_5|knows_stealth_5|knows_magic_defence_10, nord_face_young_1, swadian_face_older_2 ],


  ["rat_1","rat Slave","rat Slave",
   tf_goblin|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_armor,0,0,fac_beast,
   [
    itm_org_spear_2,itm_stones, itm_org_shield_1,
    itm_rat_armor_1,itm_rat_armor_2,itm_rat_armor_3,
    itm_rat_wolfboots,itm_rat_wolfboots,
    itm_rathelm,itm_wolfgloves,
   ],
   ranged_attrib_2|level(6),wp(60),knows_assasin_1, bandit_face1, bandit_face2],
  
  ["rat_2", "rat Skirmisher", "rat Skirmishers", 
   tf_goblin|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_beast,
   [
    itm_org_axe3,itm_org_sword2,itm_club_with_spike_head,itm_spiked_mace,itm_sledgehammer,
    itm_flintlock_pistol, itm_flintlock_pistol_2,itm_carbine,itm_samopal,itm_cartridges,
    itm_fur_covered_shield,itm_leather_covered_round_shield,
    itm_rat_armor_4,itm_rat_armor_5,itm_rat_armor_6,itm_rat_armor_7,
    itm_rat_wolfboots,itm_rat_wolfboots,
    itm_rathelm2,itm_wolfgloves,itm_cheese
   ],
   ranged_attrib_3|level(13),wp(120),knows_assasin_2, bandit_face1, bandit_face2],
    
  ["rat_3", "rat Jezzail", "rat Jezzails", 
   tf_goblin|tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_beast,
   [
    itm_hand_axe,itm_sword_viking_3,itm_org_shield_2,
    itm_war_axe,itm_warhammer,itm_voulge,
    itm_carbine_batarey_2shot,itm_good_musket,itm_flintlock_pistol_2s,itm_cartridges,
    itm_plate_covered_round_shield,itm_leather_covered_round_shield,
    itm_rat_armor_7,itm_rat_armor_8,itm_rat_armor_9,itm_rat_armor_10,
    itm_rus_shoes,
    itm_rathelm2,itm_wolfgloves,itm_cheese
   ],
   ranged_attrib_4|level(20),wp(180),knows_assasin_3,bandit_face1, bandit_face2],

  ["rat_4", "Rat Gunner", "Rat Gunners",
   tf_goblin|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_beast,
   [
    itm_drawf_musket,itm_drawf_heavy_musket,itm_musket_hand_gun,
    itm_cartridges_burst,
    #itm_rat_musket_8barrel,itm_cartridges_rar,
    itm_sword_viking_3,itm_war_axe,itm_one_handed_war_axe_b,itm_drow_round_shield,
    itm_breastplate_polish,itm_breastplate_polish,itm_breastplate_polish,
    itm_splinted_leather_greaves,itm_mail_chausses,
    itm_leather_gloves,
    itm_rathelm3,itm_wolfgloves,itm_cheese
    
    ],
   foot_attrib_5|level(26),wp(220),knows_assasin_4,bandit_face1, bandit_face2],

  ["rat_5_1", "Storm vermin", "storm vermins",
   tf_goblin|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_beast,
   [#itm_org_throwing_spears_2,
    itm_german_poleaxe_1,itm_swiss_halberd_short,itm_german_poleaxe_2,itm_bec_de_corbin_a,itm_polehammer_manhunter,
    #itm_reitern_pistol_4s,itm_cartridges_burst,
    itm_granata_poison,itm_granata_poison,
    
    itm_nordic_shield,itm_tab_shield_round_c,itm_tab_shield_heater_c,
    itm_polish_hussar_armor,itm_ee_armor_4,itm_ee_armor_3,
    itm_rus_splint_greaves,itm_rus_splint_greaves,
    itm_rathelm3,itm_wolfgloves,
   ],
   horse_attrib_4|level(35),wp(270),knows_assasin_5|knows_reserved_17_3,bandit_face1, bandit_face2],

  ["rat_5_2", "Death Sniper", "Death Snipers",
   tf_goblin|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_beast,
   [#itm_org_throwing_spears_2,
    itm_musket_rifle,itm_cartridges_thrust,
    itm_ebony_scimitar_1,
    itm_drow_round_shield,
    itm_rus_shoes,itm_breastplate_polish,
    itm_rathelm2,itm_wolfgloves,itm_cheese
   ],
   horse_attrib_4|level(35),wp(240)|wp_firearm(400),knows_stealth_3|knows_assasin_5,bandit_face1, bandit_face2],
   
  ["rat_5_3", "Ratling Gunner", "Ratling Gunners",
   tf_goblin|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_beast,
   [
    itm_rat_musket_8barrel,itm_cartridges_rar,
   
    itm_sword_viking_3,itm_war_axe,itm_one_handed_war_axe_b,itm_drow_round_shield,
    itm_polish_hussar_armor,itm_ee_armor_4,itm_ee_armor_3,
    itm_rus_splint_greaves,itm_rus_splint_greaves,
    itm_rathelm3,itm_wolfgloves,
    ],
   horse_attrib_4|level(35),wp(240)|wp_firearm(300),knows_stealth_3|knows_assasin_5,bandit_face1, bandit_face2],

  ["minotaur_1","Minotaur","Minotaur",
   tf_beastman|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_beast,
   [
    itm_two_handed_axe,itm_great_axe,
    itm_beastman_head,itm_beastman_head2,
    itm_beastman_body,itm_beastman_armour,itm_beast_leg,itm_cattle_meat,itm_cheese
   ],
   horse_attrib_3|level(25),wp_melee(250),knows_physique_4|knows_shield_3|knows_power_strike_6|knows_ironflesh_6|knows_weapon_master_3|knows_stealth_2|knows_magic_defence_1,nord_face_middle_1, nord_face_older_2],

  ["minotaur_2","Minotaur Guard","Minotaur Guard",
   tf_beastman|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_beast,
   [
    itm_ebony_axe,itm_trophy_a,
    itm_beastlord_head,itm_beastarmour_head,
    itm_beastman_plate,itm_beastman_plate,
    itm_beastman_heavyarmour,itm_beast_leg,itm_cattle_meat,itm_furs,itm_butter
   ],
   horse_attrib_5|level(35),wp_melee(350),knows_physique_6|knows_shield_4|knows_power_strike_12|knows_ironflesh_12|knows_weapon_master_4|knows_stealth_2|knows_magic_defence_5,nord_face_middle_1, nord_face_older_2],

  ["minotaur_3","Minotaur Lord","Minotaur Lord",
   tf_titan|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_beast,
   [
    itm_ebony_double_axe,itm_ebony_double_axe,itm_trophy_b,
    itm_beastlord_head,itm_ebony_male_plate,itm_ebony_male_foot,itm_ebony_male_hand,
    itm_sg_orange_small,itm_sg_orange_small
   ],
   horse_attrib_8|level(45),wp_melee(450),knows_physique_9|knows_shield_6|knows_power_strike_15|knows_ironflesh_15|knows_weapon_master_6|knows_stealth_4|knows_magic_defence_10 ,nord_face_middle_1, nord_face_older_2],


  ["red_dragon", "red_dragon", "red_dragon", 
   tf_titan|tf_guarantee_all_wo_horse, 0, 0, fac_beast, 
   [
    itm_red_dragon_sword,itm_green_dragon_shield,
    itm_red_dragon_breath,itm_red_dragon_breath_2,
    itm_demon_head,itm_demon_foot,itm_demon_hand,itm_trophy_b,itm_sg_blood,
    itm_red_dragon_body,itm_sg_orange_big,itm_sg_orange_big
   ], 
   horse_attrib_6|str_100|level(45), wp(300), knows_physique_7|knows_shield_7|knows_power_strike_6|knows_ironflesh_8|knows_reserved_18_10|knows_weapon_master_7|knows_magic_power_7|knows_magic_defence_7|knows_magic_skill_15, swadian_face_young_1, swadian_face_young_1 ],

  ["black_dragon", "black_dragon", "black_dragon", 
   tf_titan|tf_guarantee_all_wo_horse, 0, 0, fac_beast, 
   [
    itm_black_dragon_sword,itm_green_dragon_shield,
    itm_black_dragon_breath,itm_magic_death_cloud,
    itm_demon_head,itm_demon_foot,itm_demon_hand,itm_trophy_c,itm_sg_blood,itm_sg_blood,
    itm_black_dragon_body,itm_sg_black_big,itm_sg_black_big
   ], 
   horse_attrib_7|str_130|level(60), wp(400), knows_physique_10|knows_shield_9|knows_power_strike_10|knows_ironflesh_12|knows_reserved_18_10|knows_weapon_master_8|knows_magic_power_10|knows_magic_defence_10|knows_magic_skill_15, swadian_face_young_1, swadian_face_young_1 ],

  ["green_dragon", "green_dragon", "green_dragon", 
   tf_titan|tf_guarantee_all_wo_horse, 0, 0, fac_elf, 
   [
    itm_green_dragon_sword,itm_green_dragon_shield,
    itm_green_dragon_breath_2,itm_green_dragon_breath,
    itm_demon_head,itm_demon_foot,itm_demon_hand,itm_trophy_b,itm_sg_blood,
    itm_green_dragon_body,itm_sg_green_big,itm_sg_green_big
   ], 
   horse_attrib_5|str_80|level(40), wp(280), knows_physique_7|knows_shield_5|knows_power_strike_8|knows_ironflesh_6|knows_reserved_18_10|knows_weapon_master_7|knows_magic_power_6|knows_magic_defence_5|knows_magic_skill_15, swadian_face_young_1, swadian_face_young_1 ],
  ["gold_dragon", "gold_dragon", "gold_dragon", 
   tf_titan|tf_guarantee_all_wo_horse, 0, 0, fac_elf, 
   [
    itm_gold_dragon_sword,itm_green_dragon_shield,
    itm_gold_dragon_breath,
    itm_demon_head,itm_demon_foot,itm_demon_hand,itm_trophy_c,itm_sg_blood,itm_sg_blood,
    itm_gold_dragon_body,itm_sg_yellow_big,itm_sg_yellow_big
   ], 
   horse_attrib_7|str_120|level(60), wp(400), knows_physique_10|knows_shield_10|knows_power_strike_13|knows_ironflesh_15|knows_reserved_18_10|knows_weapon_master_8|knows_magic_power_8|knows_magic_defence_8|knows_magic_skill_15, swadian_face_young_1, swadian_face_young_1 ],

  ["fire_dragon", "fire_dragon", "fire_dragon", 
   tf_titan|tf_guarantee_all_wo_horse, 0, 0, fac_dwarf, 
   [
    itm_fire_dragon_sword,itm_green_dragon_shield,
    itm_fire_dragon_breath,itm_red_dragon_breath,
    itm_demon_head,itm_demon_foot,itm_demon_hand,itm_trophy_b,itm_sg_blood,
    itm_fire_dragon_body,itm_sg_orange_big,itm_sg_orange_big
   ], 
   horse_attrib_6|str_100|level(45), wp(400), knows_physique_3|knows_shield_7|knows_power_strike_10|knows_ironflesh_12|knows_reserved_18_10|knows_weapon_master_3|knows_magic_power_5|knows_magic_defence_7|knows_magic_skill_15, swadian_face_young_1, swadian_face_young_1 ],

  ["lava_dragon", "lava_dragon", "lava_dragon", 
   tf_titan|tf_guarantee_all_wo_horse, 0, 0, fac_dwarf, 
   [
    itm_lava_dragon_sword,itm_green_dragon_shield,
    itm_lava_dragon_breath,itm_red_dragon_breath_2,
    itm_demon_head,itm_demon_foot,itm_demon_hand,itm_trophy_c,itm_sg_blood,itm_sg_blood,
    itm_lava_dragon_body,itm_sg_orange_big,itm_sg_orange_big
   ], 
   horse_attrib_7|str_100|level(60), wp(500), knows_physique_5|knows_shield_9|knows_power_strike_15|knows_ironflesh_15|knows_reserved_18_10|knows_weapon_master_5|knows_magic_power_7|knows_magic_defence_9|knows_magic_skill_15, swadian_face_young_1, swadian_face_young_1 ],

  ["bone_dragon", "bone_dragon", "bone_dragon", 
   tf_titan|tf_guarantee_all_wo_horse, 0, 0, fac_undeads_2, 
   [
    itm_bone_dragon_sword_melee,itm_green_dragon_shield,
    itm_demon_head,itm_demon_foot,itm_demon_hand,itm_trophy_b,itm_sg_blood,
    itm_bone_dragon_body,itm_sg_orange_big,itm_sg_orange_big
   ], 
   horse_attrib_6|str_100|level(45), wp(300), knows_physique_7|knows_shield_10|knows_power_strike_6|knows_ironflesh_8|knows_reserved_18_10|knows_weapon_master_7|knows_magic_power_5|knows_magic_defence_7|knows_magic_skill_15, swadian_face_young_1, swadian_face_young_1 ],

  ["ghost_dragon", "ghost_dragon", "ghost_dragon", 
   tf_titan|tf_guarantee_all_wo_horse, 0, 0, fac_undeads_2, 
   [
    itm_ghost_dragon_sword_melee,itm_green_dragon_shield,
    itm_demon_head,itm_demon_foot,itm_demon_hand,itm_trophy_c,itm_sg_blood,itm_sg_blood,
    itm_ghost_dragon_body,itm_sg_black_big,itm_sg_black_big
   ], 
   horse_attrib_7|str_130|level(60), wp(400), knows_physique_10|knows_shield_10|knows_power_strike_10|knows_ironflesh_12|knows_reserved_18_10|knows_weapon_master_10|knows_magic_power_5|knows_magic_defence_7|knows_magic_skill_15, swadian_face_young_1, swadian_face_young_1 ],

  ["lich_dragon", "lich_dragon", "lich_dragon", 
   tf_titan|tf_guarantee_all_wo_horse, 0, 0, fac_undeads_2, 
   [
    itm_lich_dragon_sword,itm_green_dragon_shield,
    itm_lich_dragon_breath,itm_black_dragon_breath,
    itm_demon_head,itm_demon_foot,itm_demon_hand,itm_trophy_c,itm_sg_blood,itm_sg_blood,
    itm_lich_dragon_body,itm_sg_black_big,itm_sg_black_big
   ], 
   horse_attrib_7|str_130|level(60), wp(400), knows_physique_10|knows_shield_9|knows_power_strike_10|knows_ironflesh_12|knows_reserved_18_10|knows_weapon_master_8|knows_magic_power_10|knows_magic_defence_10|knows_magic_skill_15, swadian_face_young_1, swadian_face_young_1 ],


  ["werewolf_1","Werewolf","Werewolf",
   tf_ogre|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_demon,
   [
    itm_trophy_a,itm_furs,itm_raw_leather,itm_sg_orange_small,
    itm_wolfgloves,itm_wolfhelm,
    itm_hide_boots,itm_leather_boots,
    itm_wooden_shield,itm_nordic_shield,itm_fur_covered_shield,itm_hide_covered_round_shield,
    itm_morningstar,itm_war_axe,itm_military_cleaver_b,itm_sword_two_handed_b,itm_sword_two_handed_a,itm_bastard_sword_b,itm_one_handed_battle_axe_a,itm_great_mace,
    itm_mail_shirt,itm_byrnie,itm_ragged_outfit_mail,itm_highlander_armor2,itm_highlander_armor2_1,
    itm_mail_hauberk,itm_ee_mail_hauberk_1,itm_ee_mail_hauberk_2,itm_banded_armor,itm_cuir_bouilli,
    
   ],
   horse_attrib_5|level(35),wp(240),knows_billman_5,nord_face_middle_1, nord_face_older_2],
     



  ["werewolf_1_a","Power Werewolf","PowerWerewolf",
   tf_ogre|tf_no_capture_alive|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_demon,
   [
    itm_werewolfclaw,itm_werewolfclaw_dual,
    itm_demon_head,itm_demon_foot,itm_demon_hand,itm_trophy_b,itm_trophy_a,
    itm_werewolfarmor,itm_furs,itm_raw_leather,itm_sg_orange_big
   ],
   horse_attrib_6|level(50),wp(300),knows_billman_7|knows_magic_defence_8,nord_face_middle_1, nord_face_older_2],


  ["medusa_1","Medusas","Medusas",
   tf_female|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_beast,
   [
    itm_khergit_arrows,itm_khergit_arrows,itm_khergit_long_bow,itm_khergit_bow,
    itm_spiked_mace,itm_mace_4,itm_sword_khergit_3,itm_scimitar_b,
    itm_meduza_head,itm_demon_foot,
    itm_meduza
   ],
   horse_attrib_4|level(25),wp(145)|wp_archery (200),knows_billman_4|knows_archer_4,refugee_face1, refugee_face2],

  ["medusa_2","Medusa Queen","Medusa Queen",
   tf_female|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_beast,
   [itm_stahlrim_arrow,itm_ebony_arrow,
    itm_ebony_scimitar_1,itm_ebony_scimitar_1,
    itm_ebony_bow,itm_ebony_bow,
    itm_meduza_head2,itm_demon_foot,
    itm_meduza_up
   ],
   horse_attrib_5|level(35),wp(200)|wp_archery (250),knows_billman_5|knows_archer_7,refugee_face1, refugee_face2],


   
  ["air_elemental","Air Elemental","Air Elemental",
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_dark_knights,
   [
    itm_wolfclaw_w,itm_wolfclaw_dual_w,
    itm_air_elemental_head,itm_demon_foot,itm_air_elemental_hand,
    itm_air_elemental,
   ],
   horse_attrib_3|level(25),wp(200),knows_light_swordman_4,nord_face_middle_1, nord_face_older_2],
  ["water_elemental","Water Elemental","Water Elemental",
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_dark_knights,
   [
    itm_gold_dragon_sword,itm_magic_ice_ray_dummy,itm_magic_frost_cloud_dummy,
    itm_wolfclaw,itm_wolfclaw_dual,
    itm_water_elemental_head,itm_demon_foot,itm_air_elemental_hand,
    itm_water_elemental,
   ],
   horse_attrib_3|level(25),wp(150)|wp_firearm (200),knows_magic_4,nord_face_middle_1, nord_face_older_2],
      
  ["fire_elemental","Fire Elemental","Fire Elemental",
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_dark_knights,
   [
    itm_werewolfclaw_w,itm_werewolfclaw_dual_w,
    itm_fire_elemental_head,itm_fire_elemental_legs,itm_fire_elemental_hand,
    itm_fire_elemental_body,
   ],
   horse_attrib_4|level(30),wp(250),knows_twohand_6,nord_face_middle_1, nord_face_older_2],
  ["earth_elemental","Earth Elemental","Earth Elemental",
   tf_ogre|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_dark_knights,
   [
    itm_tree_trunk_invis,itm_werewolfclaw_dual_w,
    itm_earthelemental_head,itm_earthelemental_legs,itm_demon_hand,
    itm_earthelemental_body,
   ],
   horse_attrib_4|level(30),wp(200),knows_swordman_6|knows_magic_defence_5,nord_face_middle_1, nord_face_older_2],

  ["air_elemental_2","Air Elemental","Air Elemental",
   tf_ogre|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_dark_knights,
   [
    itm_werewolfclaw_w,itm_wolfclaw_dual_w,
    itm_air_elemental_head,itm_demon_foot,itm_air_elemental_hand,
    itm_air_elemental_2,
   ],
   horse_attrib_5|level(35),wp(250),knows_light_swordman_6,nord_face_middle_1, nord_face_older_2],
  ["water_elemental_2","Water Elemental","Water Elemental",
   tf_ogre|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_dark_knights,
   [
    itm_gold_dragon_sword,itm_magic_ice_ray,
    itm_werewolfclaw_w,itm_wolfclaw_dual,
    itm_water_elemental_head,itm_demon_foot,itm_air_elemental_hand,
    itm_water_elemental_2,
   ],
   horse_attrib_5|level(35),wp(250)|wp_firearm (300),knows_magic_6,nord_face_middle_1, nord_face_older_2],
      
  ["fire_elemental_2","Fire Elemental","Fire Elemental",
   tf_ogre|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_dark_knights,
   [
    itm_werewolfclaw_w,itm_werewolfclaw_dual_w,
    itm_fire_elemental_head,itm_fire_elemental_legs,itm_fire_elemental_hand,
    itm_fire_elemental_body_2,
   ],
   horse_attrib_6|level(40),wp(300),knows_twohand_8,nord_face_middle_1, nord_face_older_2],
  ["earth_elemental_2","Earth Elemental","Earth Elemental",
   tf_ogre|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_dark_knights,
   [
    itm_tree_trunk_invis,itm_werewolfclaw_dual_w,
    itm_earthelemental_head,itm_earthelemental_legs,itm_demon_hand,
    itm_earthelemental_body_2,itm_troll_stones,
   ],
   horse_attrib_6|level(40),wp(250),knows_swordman_8|knows_magic_defence_5,nord_face_middle_1, nord_face_older_2],
   
  ["air_elemental_3","Air Elemental","Air Elemental",
   tf_ogre|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_dark_knights,
   [
    itm_hugewolfclaw,itm_wolfclaw_dual_w,
    itm_air_elemental_head,itm_demon_foot,itm_air_elemental_hand,
    itm_air_elemental_3,
   ],
   horse_attrib_7|level(45),wp(250),knows_light_swordman_8|knows_magic_power_4,nord_face_middle_1, nord_face_older_2],
  ["water_elemental_3","Water Elemental","Water Elemental",
   tf_ogre|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_dark_knights,
   [
    itm_gold_dragon_sword,itm_magic_ice_ray,
    itm_water_elemental_head,itm_demon_foot,itm_air_elemental_hand,
    itm_water_elemental_3,
   ],
   horse_attrib_7|level(45),wp(250)|wp_firearm (300),knows_magic_8,nord_face_middle_1, nord_face_older_2],
      
  ["fire_elemental_3","Fire Elemental","Fire Elemental",
   tf_ogre|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_dark_knights,
   [
    itm_red_dragon_sword,itm_green_dragon_shield,
    itm_red_dragon_breath,itm_red_dragon_breath_2,
    itm_fire_elemental_head,itm_fire_elemental_legs,itm_fire_elemental_hand,
    itm_fire_elemental_body_3,
   ],
   str_50|agi_32|int_12|cha_12|level(50),wp(300),knows_physique_9|knows_shield_6|knows_power_strike_15|knows_ironflesh_15|knows_reserved_18_10|knows_weapon_master_6|knows_stealth_4|knows_magic_power_7|knows_magic_defence_7|knows_magic_skill_15,nord_face_middle_1, nord_face_older_2],
   
  ["earth_elemental_3","Earth Elemental","Earth Elemental",
   tf_ogre|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_dark_knights,
   [
    itm_tree_trunk_invis_3,
    itm_earthelemental_head,itm_earthelemental_legs,itm_demon_hand,
    itm_earthelemental_body_3,itm_troll_stones,
   ],
   str_50|agi_50|int_12|cha_12|level(50),wp(250),knows_physique_10|knows_shield_10|knows_power_strike_12|knows_ironflesh_15|knows_reserved_18_10|knows_weapon_master_8|knows_magic_defence_9|knows_power_throw_4,nord_face_middle_1, nord_face_older_2],



 ["human_magic_1","Apprentice","Apprentice",
  tf_guarantee_ranged|tf_guarantee_all_footman,0,0,fac_dark_knights,
   [
    itm_wooden_staff_1,
    itm_magic_searing_doom,
    
    itm_magic_robe,itm_leather_boots,itm_wizard_hat],
   foot_attrib_3|level(15),wp_melee(90)|wp_firearm (100),knows_magic_2,euro_face_3, euro_face_4],
   
 ["human_magic_2", "Mage", "Mage",
  tf_guarantee_ranged|tf_no_capture_alive|tf_guarantee_all_footman,0,0,fac_dark_knights,
   [itm_mage_staff_1,
    #itm_magic_summon_neutral_near_ememy,
    itm_magic_searing_doom,
    itm_horse_euro,
    itm_wizard_hat_2_1,
    itm_leather_boots,itm_magic_robe_2_1],
   foot_attrib_4|level(30),wp_melee (100)|wp_firearm (200),knows_magic_4,euro_face_3, euro_face_4],
      
 ["human_magic_3","Arch_Mage","Arch_Mage",
  tf_guarantee_ranged|tf_mounted|tf_no_capture_alive|tf_guarantee_all,0,0,fac_dark_knights,
   [
    itm_archmage_staff_1,
    
    #itm_magic_summon_neutral_near_ememy,
    itm_magic_searing_doom,
    itm_hunter,

    itm_magic_robe_3,itm_leather_boots,itm_wizard_hat_3,itm_trophy_b,itm_sg_human_big],
   foot_attrib_5|level(45),wp_melee(120)|wp_firearm(300),knows_magic_6|knows_horse_shoot_3,euro_face_3, euro_face_4],

  ["golem_1","stone golem","stone golem",
   tf_ogre|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_dark_knights,
   [
    itm_sledgehammer,itm_warhammer,
    itm_stone_golemgloves,itm_stone_golemhelm,itm_stone_golemarmor,itm_stone_golemboots,
   ],
   str_70|agi_5|int_4|cha_4|level(20),wp(145),knows_ironflesh_6|knows_twohand_4|knows_magic_defence_4,nord_face_middle_1, nord_face_older_2],
  ["golem_2","silver golem","silver golem",
   tf_ogre|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_dark_knights,
   [
    itm_cav_bardiche,itm_knightaxe,itm_hand_cannon_3,itm_hand_cannon_2,itm_cartridges_burst,itm_cartridges_cannon,
    itm_silver_golemgloves,itm_silver_golemhelm,itm_silver_golemarmor,itm_silver_golemboots,
   ],
   foot_attrib_4|level(30),wp(200),knows_ironflesh_10|knows_swordman_5|knows_magic_defence_9,nord_face_middle_1, nord_face_older_2],
  ["golem_3","iron golem","iron golem",
   tf_ogre|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_dark_knights,
   [
    itm_cav_bardiche,itm_knightaxe,itm_bastard_sword_e,itm_bastard_sword_f,itm_steel_shield,itm_steel_shield,
    itm_iron_golemgloves,itm_iron_golemhelm,itm_iron_golemarmor,itm_iron_golemboots,
   ],
   str_75|agi_5|int_4|cha_4|level(30),wp(200),knows_ironflesh_8|knows_twohand_5|knows_magic_defence_8,nord_face_middle_1, nord_face_older_2],  


  ["dendroid","Dendroid_Guard","Dendroid_Guard",
   tf_ogre|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_dark_knights,
   [
    itm_tree_trunk_invis,itm_werewolfclaw_dual_w,
    itm_dendroid_body,
   ],
   str_50|agi_50|int_4|cha_4|level(35),wp(200),knows_ironflesh_10|knows_twohand_7|knows_magic_defence_6,nord_face_middle_1, nord_face_older_2],  

  ["golem_4","gold golem","gold golem",
   tf_ogre|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_dark_knights,
   [
    itm_tree_trunk_invis,itm_werewolfclaw_dual_w,
    itm_gold_golemarmor,itm_gold_golemboots,itm_gold_golemgloves,itm_gold_golemhelm,
   ],
   str_100|agi_5|int_4|cha_4|level(35),wp(200),knows_ironflesh_10|knows_twohand_7|knows_magic_defence_10,nord_face_middle_1, nord_face_older_2],  

  ["sissofbattle","Sister of Battle","Sister of Battle",
   tf_female|tf_guarantee_all_wo_horse|tf_no_capture_alive,0,0,fac_kingdom_7,
   [
    itm_cartridges_sissofbattle_holy,
    itm_cartridges_sissofbattle_flame,
    itm_cartridges_sissofbattle_bolter_2,
    itm_sissofbattle_e5,itm_sissofbattle_a295,
    itm_sissofbattle_sword_short,
    itm_sissofbattle_armor,
    itm_toumingtou,
    itm_steel_greaves,
    itm_hourglass_gauntlets,itm_sg_yellow_small],
  horse_attrib_5|level(30),wp(200),knows_precise_shot_5|knows_twohand_5|knows_first_aid_5|knows_magic_defence_5,0x00000000000000120000000000000E0000000000000000000000000000000000,0x00000000000000120000000000000E0000000000000000000000000000000000],

  ["sissofbattle_c","Sister of Battle Celestion Squad","Sister of Battle Celestion Squad",
   tf_female|tf_guarantee_all_wo_horse|tf_no_capture_alive,0,0,fac_kingdom_7,
   [
    itm_cartridges_sissofbattle_flame_2,
    itm_cartridges_sissofbattle_bolter,
    itm_cartridges_sissofbattle_bolter_2,
    itm_sissofbattle_a295,itm_sissofbattle_a295,
    itm_sissofbattle_sword_short,
    itm_sissofbattle_armor,
    itm_toumingtou,itm_siss_cap,
    itm_steel_greaves,itm_trophy_b,
    itm_hourglass_gauntlets,itm_sg_yellow_small],
  horse_attrib_6|level(35),wp(300),knows_precise_shot_6|knows_twohand_6|knows_first_aid_5|knows_magic_defence_5,0x00000000000000120000000000000E0000000000000000000000000000000000,0x00000000000000120000000000000E0000000000000000000000000000000000],
  ["sissofbattle_s","Sister of Battle Seraphim Squad","Sister of Battle Seraphim Squad",
   tf_female|tf_guarantee_all_wo_horse|tf_no_capture_alive,0,0,fac_kingdom_7,
   [
    #itm_cartridges_sissofbattle_flame_2,itm_laser_bolt_red,
    #itm_sissofbattle_e5,itm_sissofbattle_e5,
    itm_sissofbattle_holy_granata,itm_sissofbattle_holy_granata,
    itm_sissofbattle_sword_alt,
    itm_sissofbattle_armor_fly,
    itm_toumingtou,
    itm_steel_greaves,itm_trophy_c,
    itm_hourglass_gauntlets,itm_sg_yellow_big],
  horse_attrib_8|level(40),wp(500),knows_precise_shot_8|knows_twohand_8|knows_first_aid_5|knows_magic_defence_5,0x00000000000000120000000000000E0000000000000000000000000000000000,0x00000000000000120000000000000E0000000000000000000000000000000000],

  ["sissofbattle_r","Sister of Battle Retributor Squad","Sister of Battle Retributor Squad",
   tf_female|tf_guarantee_all_wo_horse|tf_no_capture_alive,0,0,fac_kingdom_7,
   [
    itm_cartridges_sissofbattle_bolter_2,
    itm_cartridges_sissofbattle_flame_cannon,
    itm_cartridges_cannon,
    itm_cartridges_sissofbattle_flame,
    itm_sissofbattle_a295_heavy,itm_sissofbattle_a295_heavy,
    itm_sissofbattle_sword,
    itm_sissofbattle_armor_red,
    itm_siss_cap,itm_siss_cap,
    itm_steel_greaves,itm_trophy_c,
    itm_hourglass_gauntlets,itm_sg_yellow_big],
  horse_attrib_9|level(45),wp(400),knows_precise_shot_10|knows_twohand_9|knows_first_aid_5|knows_magic_defence_5,0x00000000000000120000000000000E0000000000000000000000000000000000,0x00000000000000120000000000000E0000000000000000000000000000000000],

  ["angle", "Angle", "Angle", 
   tf_female|tf_guarantee_all_wo_horse, 0, 0, fac_kingdom_7, 
   #tf_female|tf_mounted|tf_guarantee_all_wo_ranged|tf_guarantee_horse, 0, 0, fac_kingdom_7, 
   [
    itm_angle_sword,
    itm_angle_shield,
    #itm_angle_horse,
    itm_angle_sword_2,itm_angle_sword_2,
    itm_trophy_b,
    itm_demon_head,itm_demon_foot,itm_demon_hand,
    itm_angle_body,itm_sg_yellow_big,itm_sg_yellow_big
   ], 
   horse_attrib_5|str_50|level(45), wp(300), knows_knight_foot_4|knows_swordman_6|knows_magic_3|knows_magic_defence_7|knows_weapon_master_7, swadian_face_young_1, swadian_face_young_1 ],

  ["archangle", "Arch Angle", "Arch Angle", 
   tf_female|tf_guarantee_all_wo_horse, 0, 0, fac_kingdom_7, 
   #tf_female|tf_mounted|tf_guarantee_all_wo_ranged|tf_guarantee_horse, 0, 0, fac_kingdom_7, 
   [
    itm_archangle_sword,itm_archangle_shield,
    #itm_angle_horse,
    itm_archangle_sword_2,
    itm_trophy_c,
    itm_demon_head,itm_demon_foot,itm_demon_hand,
    itm_archangle_body,itm_sg_yellow_big,itm_sg_yellow_big
   ], 
   horse_attrib_6|str_75|level(60), wp(400), knows_knight_foot_5|knows_swordman_8|knows_magic_5|knows_magic_defence_9|knows_weapon_master_9, swadian_face_young_1, swadian_face_young_1 ],

  ["titan_0","Giant","Giant",
   tf_titan|tf_no_capture_alive|tf_guarantee_all_footman|tf_guarantee_ranged,0,0,fac_dark_knights,
   [
    itm_throwing_lightning_melee,

    itm_toumingtou,
    itm_giant_plate,
    itm_giant_greaves,itm_sg_blue_small
   ],
   horse_attrib_4|level(30),wp(300),knows_twohand_5,nord_face_middle_1, nord_face_older_2],

  ["titan_1","Titan","Titan",
   tf_titan|tf_no_capture_alive|tf_guarantee_all_footman|tf_guarantee_ranged,0,0,fac_dark_knights,
   [
    itm_throwing_lightning_melee,itm_throwing_lightning,

    itm_amade_steel_winged_helm,
    itm_amade_steel_plate,itm_trophy_b,
    itm_amade_steel_greaves,itm_amade_steel_gauntlets,itm_sg_blue_big
   ],
   horse_attrib_5|int_50|level(45),wp(350),knows_thrown_8|knows_magic_power_7|knows_magic_defence_5,nord_face_middle_1, nord_face_older_2],
  ["titan_2","Storm Titan","Storm Titan",
   tf_titan|tf_no_capture_alive|tf_guarantee_all_footman|tf_guarantee_ranged,0,0,fac_dark_knights,
   [
    itm_throwing_lightning_melee,itm_throwing_lightning,
    #itm_steel_shield,itm_steel_shield,
    itm_amade_bronze_winged_helm,
    itm_amade_bronze_plate,itm_trophy_c,
    itm_amade_bronze_greaves,itm_amade_bronze_gauntlets,itm_sg_blue_big,itm_sg_blue_big
   ],
   horse_attrib_6|int_70|level(60),wp(400),knows_thrown_9|knows_magic_power_7|knows_magic_defence_10,nord_face_middle_1, nord_face_older_2],
   
   
   
 ["gargoyle","Gargoyle","Gargoyle",
   tf_titan|tf_guarantee_all_footman,0,0,fac_dark_knights,
   [
    itm_hugewolfclaw_w,itm_werewolfclaw_dual_w,
    itm_demon_head,itm_demon_foot,itm_death_hand,
    itm_gargoyle_body,itm_sg_black_big,itm_sg_blue_big
   ],
   str_70|agi_50|int_4|cha_4|level(50),wp_melee(350),knows_ironflesh_15|knows_billman_8|knows_magic_defence_10,euro_face_3, euro_face_4],

 ["undead_magic_1", "Evil Eye", "Evil Eye",
  tf_guarantee_ranged|tf_no_capture_alive|tf_guarantee_all_footman,0,0,fac_beast,
   [
    #itm_magic_summon_neutral_near_ememy,itm_magic_summon_undead_near_ememy,
    itm_magic_spirit_leech,itm_magic_ice_ray,itm_magic_poison,
    itm_gold_dragon_sword,
    itm_beholder,itm_demon_foot,itm_demon_hand,itm_demon_head,
   ],
   horse_attrib_4|level(25),wp_melee (250)|wp_firearm (250),knows_magic_6|knows_magic_defence_10,euro_face_3, euro_face_4],

 ["demon_magic_1","Heretic Cultist","Heretic Cultist",
  tf_demon_human|tf_guarantee_ranged|tf_guarantee_all_footman,0,0,fac_demon,
   [
    itm_wooden_staff_1,itm_battle_axe,
    itm_magic_fire_ray_dummy,
    
    itm_rhun_armor_1, itm_rhun_armor_2,itm_rhun_helm_1,itm_rhun_helm_2,itm_leather_gloves,itm_sarranid_boots_a
   ],
   foot_attrib_3|level(15),wp_melee(90)|wp_firearm (100),knows_magic_3,euro_face_3, euro_face_4],
   
 ["demon_magic_2", "Heretic Sorcerer", "Heretic Sorcerer",
  tf_demon_human|tf_guarantee_ranged|tf_no_capture_alive|tf_guarantee_all_footman,0,0,fac_demon,
   [itm_sorcerer_staff_1,
    itm_magic_fire_ray_dummy,
    #itm_magic_summon_demon,

    itm_sarranid_boots_b,itm_wizard_hat_2_2,itm_wizard_hat_2_2,
    itm_leather_gloves,itm_magic_robe_2_2],
   foot_attrib_4|level(30),wp_melee (100)|wp_firearm (200),knows_magic_5,euro_face_3, euro_face_4],
            
 ["demon_magic_3","Heretic Demonologist","Heretic Demonologist",
  tf_demon_human|tf_guarantee_ranged|tf_no_capture_alive|tf_guarantee_all_footman,0,0,fac_demon,
   [
    itm_demon_staff_1,
    itm_magic_poison_dummy,
    #itm_magic_summon_demon_near_ememy,
    itm_trophy_b,
    itm_nec_robe,itm_sarranid_boots_b,itm_leather_gloves,itm_demon_hood],
   foot_attrib_5|level(45),wp_melee(120)|wp_firearm(300),knows_magic_7,euro_face_3, euro_face_4],
   
  ["demon_human_1","Heretic_Initiate","Heretic_Initiates",
   tf_demon_human|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet,0,0,fac_demon,
   [
    itm_voulge,itm_battle_axe,
    itm_rhun_armor_1,itm_rhun_armor_2,itm_sarranid_boots_a,itm_sarranid_boots_b,itm_rhun_helm_1,itm_rhun_helm_2
    
   ],
   horse_attrib_2|level(10),wp(100),knows_billman_2,swadian_face_younger_1,swadian_face_middle_2],
   
  ["demon_human_2","Heretic_Berserker","Heretic_Berserkers",
   tf_demon_human|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet,0,0,fac_demon,
   [
    itm_chaos_sword1,itm_sarranid_axe_a,
    itm_tab_shield_kite_b,itm_tab_shield_kite_c,
    itm_arrows,itm_strong_bow,itm_nomad_bow,
    itm_rhun_armor_4,itm_rhun_armor_3,
    itm_chaos_leg_1,itm_chaos_leg_1,
    itm_rhun_helm_3,itm_rhun_helm_2
   ],
   horse_attrib_3|level(20),wp(150),knows_billman_3|knows_power_draw_3|knows_reserved_17_3,swadian_face_younger_1,swadian_face_middle_2],
      
  ["demon_human_3", "Heretic_fallen_Warrior", "Heretic_fallen_Warrior", 
   tf_demon_human|tf_guarantee_all_footman, 0, 0, fac_demon, 
   [
    itm_sarranid_axe_a,itm_sarranid_mace_1,
    itm_sarranid_two_handed_axe_a,itm_sarranid_two_handed_mace_1,
    itm_chaos_warrior_shield,itm_chaos_warrior_shield,
    itm_chaos_leg_1,itm_chaos_leg_1,itm_chaos_gauntlets_1,
    itm_rhun_armor_5,itm_rhun_armor_6,
    itm_rhun_helm_7,itm_rhun_helm_7_2,
   ], 
   horse_attrib_4|level(30), wp(200), knows_billman_5, swadian_face_middle_1, swadian_face_middle_1 ],
                                             
  ["demon_human_4", "Heretic Possessed", "Heretic Possesseds", 
   tf_demon_human|tf_guarantee_all_footman, 0, 0, fac_demon, 
  [
    itm_sarranid_axe_a,itm_sarranid_mace_1,
    itm_sarranid_two_handed_axe_b,itm_sarranid_two_handed_mace_2,
   
   itm_chaos_knight_shield,itm_chaos_knight_shield,
   itm_rhun_armor_6_2,itm_rhun_armor_6_1,
   itm_imp_foot_2,itm_imp_foot_2,itm_imp_head_4,itm_imp_head_4,itm_rhun_helm_9,
   itm_imp_hand_3,itm_imp_hand_3,itm_chaos_gauntlets_1,
  ],
   horse_attrib_6|level(40), wp(300), knows_riding_3|knows_billman_7, swadian_face_middle_2, swadian_face_older_2 ],
      
      
  ["demon_human_5_1", "Heretic Demon Knight", "Heretic Demon Knights", 
   tf_demon_human|tf_guarantee_all, 0, 0, fac_demon, 
   [
    itm_magic_pink_fire_of_tzeentch,itm_magic_blue_fire_of_tzeentch,
    itm_demon_knight_shield,itm_demon_knight_shield,
    itm_mark_chaos_1,
    itm_tzeentch_chosen_head,itm_tzeentch_chosen_leg,itm_tzeentch_chosen_hand,itm_tzeentch_chosen_armor,
    itm_tzeentch_charger,itm_tzeentch_charger,
    #itm_nightmare,itm_nightmare
   ], 
   str_35|agi_24|int_30|cha_12|level(50), wp(300), knows_knight_foot_3|knows_physique_6|knows_shield_4|knows_power_strike_6|knows_ironflesh_6|knows_reserved_18_10|knows_weapon_master_4|knows_magic_defence_9|knows_magic_power_6|knows_necromancy_2, swadian_face_middle_2, swadian_face_older_2 ],


  ["slaanesh_witch_1", "slaanesh_witch", "slaanesh_witch", 
   tf_female|tf_guarantee_ranged|tf_guarantee_all_wo_horse, 0, 0, fac_demon, 
   [itm_flame_arrows,itm_khergit_bow,
    itm_flat_headed_arrows,itm_khergit_bow,
    itm_slaanesh_banshee_sword,itm_slaanesh_banshee_sword,
    itm_slaanesh_witch_armor,itm_slaanesh_witch_leg,itm_slaanesh_witch_head
   ], 
   horse_attrib_4|level(30), wp(200), knows_physique_7|knows_shield_3|knows_power_strike_9|knows_ironflesh_6|knows_reserved_18_10|knows_weapon_master_5|knows_stealth_6|knows_power_draw_4|knows_weapon_master_6|knows_magic_defence_5, swadian_face_middle_1, swadian_face_middle_1 ],
                   
      
  ["slaanesh_witch_2", "slaanesh_banshee", "slaanesh_banshee", 
   tf_female|tf_guarantee_ranged|tf_guarantee_all_wo_horse, 0, 0, fac_demon, 
   [itm_orcish_mutil_arrow,itm_banshee_bow,
    itm_demon_arrow,itm_slaanesh_witch_shield,
    itm_slaanesh_banshee_sword,itm_slaanesh_chosen_sword,
   
    itm_slaanesh_banshee_armor,itm_slaanesh_witch_leg,itm_slaanesh_banshee_head
  ],
   horse_attrib_6|level(40), wp(250), knows_physique_8|knows_shield_3|knows_power_strike_11|knows_ironflesh_7|knows_reserved_18_10|knows_weapon_master_8|knows_stealth_8|knows_power_draw_7|knows_magic_defence_6, swadian_face_middle_2, swadian_face_older_2 ],


  ["demon_human_5_2", "Heretic Demon Marksman", "Heretic Demon Marksmen", 
   tf_female|tf_guarantee_ranged|tf_guarantee_all_wo_horse, 0, 0, fac_demon, 
   [
    itm_black_bow,itm_black_bow,
    itm_demon_arrow,itm_orcish_mutil_arrow,itm_orcish_mutil_arrow,
    itm_slaanesh_chosen_sword,itm_efreet_shield,
    itm_demon_head,itm_demon_foot,itm_demon_hand,
    itm_succubus_body,itm_trophy_c,
   ], 
   horse_attrib_8|level(50), wp(300), knows_magic_power_5|knows_billman_7|knows_power_draw_7|knows_stealth_10|knows_weapon_master_10|knows_magic_defence_8, swadian_face_older_2, swadian_face_old_2 ],

  ["demon_1", "Imp", "Imps", 
   tf_dwarf|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged, 0, 0, fac_demon, 
   [
    itm_imp_fork,itm_flamer_sword,itm_magic_blue_fire_of_tzeentch_dummy,itm_magic_stream_of_corruption_dummy,itm_magic_lash_of_slaanesh_dummy,

    #itm_black_bow,itm_evil_arrow_2,
    itm_imp_head_2,itm_imp_hand_2,itm_imp_body_2,
    itm_demon_head,itm_demon_foot,itm_demon_hand,
    
    ], 
   horse_attrib_2|level(20), wp(120), knows_stealth_2|knows_thrown_3, swadian_face_young_1, swadian_face_young_1 ],
   
  ["demon_1_3", "Nurgling", "Nurgling", 
   tf_dwarf|tf_guarantee_all_footman, 0, 0, fac_demon, 
   [
    itm_wolfclaw_w,itm_werewolfclaw_dual_w,
    itm_demon_head,itm_demon_foot,itm_demon_hand,itm_trophy_b,itm_trophy_c,
    itm_nurgling_armor,
    itm_sg_green_big,itm_sg_purple_big
   ], 
   horse_attrib_3|level(30), wp(180), knows_pikeman_4|knows_ironflesh_10, swadian_face_middle_2, swadian_face_older_2 ],
   
  ["demon_1_2", "Bloodletter", "Bloodletter", 
   tf_demon_human|tf_guarantee_all_footman, 0, 0, fac_demon, 
   [
    itm_demon_sword_3,itm_demon_axe,
    itm_demon_head,itm_demon_foot,
    itm_imp_hand_3,itm_imp_body_3,
    ], 
   horse_attrib_3|level(30), wp_melee(200), knows_stealth_1|knows_twohand_4, swadian_face_young_1, swadian_face_young_1 ],
      
  ["demon_2", "Vrock", "Vrock", 
   tf_demon_human|tf_guarantee_all_footman|tf_guarantee_ranged, 0, 0, fac_demon, 
   [
    itm_demon_pickaxe_2,
    #itm_demon_fireball,itm_demon_fireball,
    #itm_bloodguard_head,itm_bloodguard_body,itm_bloodguard_calf,
    #itm_gauntlets,
    itm_imp_head,itm_imp_foot,
    itm_imp_hand,itm_imp_body,
    
   ], 
   horse_attrib_3|level(30), wp_melee(200), knows_stealth_7|knows_billman_4, swadian_face_young_1, swadian_face_young_1 ],
   
  ["demon_3", "Horned Demon", "Horned Demon", 
   tf_demon_human|tf_guarantee_all_footman, 0, 0, fac_demon, 
   [
    itm_horned_demon_sword,itm_werewolfclaw_dual_w,
    
    itm_demon_head,itm_demon_foot,itm_demon_hand,itm_trophy_a,
    itm_horned_demon_body,itm_sg_purple_small
   ], 
   horse_attrib_7|level(45), wp_melee(350), knows_twohand_6|knows_stealth_6|knows_magic_defence_8|knows_physique_8, swadian_face_young_1, swadian_face_young_1 ],
      
  ["demon_1_4", "Flamer of Tzeentch", "Flamer of Tzeentch", 
   tf_demon_human|tf_guarantee_all_footman, 0, 0, fac_demon, 
   [
    itm_efreet_sword,itm_demon_fireball,
    #itm_magic_fireball,itm_magic_meteor_shower,itm_magic_summon_demon,
    itm_efreet_head,itm_demon_foot,itm_sandwraith_hands,itm_trophy_b,itm_trophy_a,
    itm_sandwraith_body
    ], 
   horse_attrib_3|level(30), wp(200), knows_stealth_3|knows_thrown_5|knows_magic_defence_5, swadian_face_young_1, swadian_face_young_1 ],
      
  ["demon_4", "Efreet", "Efreet", 
   tf_demon_human|tf_guarantee_all_footman, 0, 0, fac_demon, 
   [
    itm_flamer_sword,
    itm_cartridges_flame,itm_cartridges_flame,
    
    itm_demon_head,itm_demon_foot,itm_demon_hand,
    itm_flamer,
    itm_sg_purple_small
   ], 
   horse_attrib_5|level(39), wp(330), knows_swordman_6|knows_magic_defence_5|knows_physique_10, swadian_face_young_1, swadian_face_young_1 ],
   
   
   
  ["demon_4_2", "Behemoth", "Behemoth", 
   tf_titan|tf_guarantee_all_footman, 0, 0, fac_orc, 
   [
    itm_hugewolfclaw,itm_werewolfclaw_dual_w,
    itm_demon_head,itm_demon_foot,itm_demon_hand,itm_trophy_b,itm_trophy_b,
    itm_behemoth_armor,itm_sg_purple_big
   ], 
   horse_attrib_6|level(45), wp_melee(350), knows_billman_6|knows_magic_defence_3, swadian_face_young_1, swadian_face_young_1 ],
      
  ["demon_4_3", "Ghost Behemoth", "Ghost Behemoth", 
   tf_titan|tf_guarantee_all_footman, 0, 0, fac_orc, 
   [
    itm_hugewolfclaw_w,itm_werewolfclaw_dual_w,
    itm_demon_head,itm_demon_foot,itm_demon_hand,itm_trophy_b,itm_trophy_b,
    itm_ghost_behemoth_armor,itm_sg_purple_big,itm_sg_purple_big
   ], 
   str_70|agi_70|int_30|cha_12|level(60), wp_melee(350), knows_billman_8|knows_magic_defence_5, swadian_face_young_1, swadian_face_young_1 ],
   
  ["demon_5", "Arch Demon", "Arch Demon", 
   tf_titan|tf_guarantee_all_footman, 0, 0, fac_demon, 
   [
    itm_arch_demon_axe,itm_arch_demon_axe_2,
    itm_trophy_c,itm_trophy_b,
    
    itm_demon_head,itm_demon_foot,itm_demon_hand,
    itm_arch_demon_body,itm_sg_purple_big
   ], 
   str_70|agi_70|int_30|cha_12|level(60), wp_melee(400), knows_physique_10|knows_shield_10|knows_power_strike_15|knows_ironflesh_15|knows_reserved_18_10|knows_weapon_master_10|knows_magic_defence_10, swadian_face_young_1, swadian_face_young_1 ],
      
      
  ["slaanesh_chosen", "Slaanesh Chosen", "Slaanesh Chosen", 
   tf_female|tf_guarantee_ranged|tf_guarantee_all_footman, 0, 0, fac_demon, 
   [
    itm_slaanesh_chosen_shield,itm_slaanesh_chosen_sword_1,
    itm_magic_shadow_bolt,itm_trophy_b,
    
    itm_slaanesh_chosen_head,itm_slaanesh_chosen_leg,itm_slaanesh_chosen_hand,
    itm_slaanesh_chosen_armor,itm_sg_purple_big
   ], 
   str_40|agi_40|int_30|cha_12|level(50), wp(300), knows_physique_10|knows_shield_6|knows_power_strike_10|knows_ironflesh_9|knows_reserved_18_10|knows_stealth_8|knows_weapon_master_8|knows_magic_defence_9|knows_magic_power_5|knows_necromancy_2, swadian_face_young_1, swadian_face_young_1 ],
      
  ["daemon_prince_slaanesh", "Daemon Prince of Slaanesh", "Daemon Prince of Slaanesh", 
   tf_titan|tf_guarantee_all_footman, 0, 0, fac_demon, 
   [
    itm_slaanesh_daemon_shield,itm_slaanesh_daemon_sword,itm_magic_lash_of_slaanesh,itm_gold_dragon_sword,
    itm_trophy_c,itm_trophy_b,
    
    itm_demon_head,itm_demon_foot,itm_demon_hand,
    itm_slaanesh_prince,itm_sg_purple_big
   ], 
   str_60|agi_80|int_30|cha_12|level(60), wp_melee(520), knows_physique_10|knows_shield_10|knows_power_strike_10|knows_ironflesh_10|knows_reserved_18_10|knows_stealth_10|knows_weapon_master_10|knows_magic_defence_10|knows_magic_power_5|knows_necromancy_2, swadian_face_young_1, swadian_face_young_1 ],
      
  ["daemon_prince_nurgle", "Daemon Prince of nurgle", "Daemon Prince of nurgle", 
   tf_titan|tf_guarantee_all_wo_horse, 0, 0, fac_demon, 
   [
    itm_undead_scythe,itm_gold_dragon_sword,itm_magic_stream_of_corruption,
    #itm_nurgle_shield_1,itm_nurgle_shield_2,itm_nurgle_mace,
    itm_trophy_c,itm_trophy_b,
    
    itm_demon_head,itm_demon_foot,itm_nurgle_hands,
    itm_nurgle_prince,itm_sg_purple_big
   ], 
   str_60|agi_80|int_30|cha_12|level(60), wp_melee(400)|wp_firearm(250), knows_stealth_3|knows_physique_10|knows_shield_10|knows_power_strike_13|knows_ironflesh_15|knows_reserved_18_10|knows_weapon_master_10|knows_magic_power_7|knows_necromancy_4|knows_magic_defence_10, swadian_face_young_1, swadian_face_young_1 ],
      
  ["demon_6", "Pit Fiend", "Pit Fiends", 
   tf_titan|tf_guarantee_all_wo_horse, 0, 0, fac_demon, 
   [
    itm_balor_sword,
    itm_magic_blue_fire_of_tzeentch,
    itm_trophy_c,itm_trophy_b,
    itm_demon_head,itm_demon_foot,itm_tzeentch_hands,
    itm_balor_body,itm_sg_purple_big
   ], 
   str_60|agi_60|int_50|cha_12|level(60), wp(400), knows_knight_foot_3|knows_physique_8|knows_shield_4|knows_power_strike_9|knows_ironflesh_6|knows_reserved_18_10|knows_magic_power_13|knows_magic_defence_10|knows_necromancy_4|knows_magic_skill_15, swadian_face_young_1, swadian_face_young_1 ],


  ["demon_7", "Heretic Demon Knight", "Heretic Demon Knights", 
   tf_demon_human|tf_mounted|tf_guarantee_all, 0, 0, fac_demon, 
   [
    itm_chaos_sword5,itm_khorne_shield,itm_chaos_axe2,
    itm_demon_knight_plate,itm_demon_knight_plate,
    itm_demon_knight_leg,itm_barrier_leg,
    itm_demon_knight_head,itm_demon_knight_head_2,itm_khorne_helm,
    itm_trophy_b,itm_trophy_c,
    itm_demon_knight_hand,itm_satanic_hand,
    itm_hell_nightmare,
    itm_sg_purple_big,
    #itm_nightmare,itm_nightmare
   ], 
   horse_attrib_9|level(50), wp(350), knows_knight_foot_4|knows_physique_8|knows_shield_10|knows_power_strike_13|knows_ironflesh_12|knows_reserved_18_10|knows_stealth_5|knows_weapon_master_8|knows_magic_defence_10, swadian_face_middle_2, swadian_face_older_2 ],


  ["demon_8", "Nurgle plaguebearer", "Nurgle plaguebearer", 
   tf_demon_human|tf_guarantee_all_footman, 0, 0, fac_demon, 
   [
    itm_werewolfclaw_w,itm_werewolfclaw_dual_w,
    itm_demon_head,itm_demon_foot,itm_demon_hand,itm_trophy_b,itm_trophy_c,
    itm_plaguebearer_armor,
    itm_sg_green_big,itm_sg_purple_big
   ], 
   horse_attrib_5|level(40), wp(280), knows_physique_3|knows_shield_4|knows_power_strike_8|knows_ironflesh_12|knows_reserved_18_10|knows_weapon_master_4|knows_magic_defence_6, swadian_face_middle_2, swadian_face_older_2 ],

  ["demon_9", "Nurgle Chosen", "Nurgle Chosen", 
   tf_demon_human|tf_guarantee_all_footman, 0, 0, fac_demon, 
   [
    itm_nurgle_shield_1,itm_nurgle_shield_2,
    itm_nurgle_chosen_armor,itm_nurgle_chosen_armor,
    itm_nurgle_chosen_leg,itm_nurgle_chosen_leg,
    itm_nurgle_chosen_head_1,itm_nurgle_chosen_head_2,itm_trophy_b,itm_trophy_c,
    itm_nurgle_chosen_hand,itm_nurgle_chosen_hand,
    itm_plague_staff,itm_nurgle_mace,itm_sg_purple_big,
   ], 
   horse_attrib_9|level(50), wp(400), knows_stealth_3|knows_physique_5|knows_shield_10|knows_power_strike_9|knows_ironflesh_15|knows_reserved_18_10|knows_weapon_master_10|knows_magic_defence_8, swadian_face_middle_2, swadian_face_older_2 ],

  ["great_demon_nurgle", "Great Unclean ones", "Great Unclean ones", 
   tf_titan|tf_guarantee_all_wo_horse, 0, 0, fac_demon, 
   [
    itm_green_dragon_sword,itm_magic_spirit_leech,
    itm_huge_infreno_left_claw,itm_huge_infreno_left_claw,
    itm_trophy_c,itm_trophy_b,
    
    itm_demon_head,itm_demon_foot,itm_demon_hand,
    itm_papanurg_body,itm_sg_purple_big
   ], 
   str_80|agi_80|int_30|cha_12|level(60), wp_melee(400)|wp_firearm(100), knows_physique_10|knows_shield_10|knows_power_strike_13|knows_ironflesh_15|knows_reserved_18_10|knows_weapon_master_10|knows_magic_power_5|knows_necromancy_4|knows_magic_defence_10, swadian_face_young_1, swadian_face_young_1 ],


  ["inferno","inferno","inferno",
   tf_dwarf|tf_no_capture_alive|tf_guarantee_all_footman,0,0,fac_demon,
   [
    itm_infreno_right_claw,itm_infreno_left_claw,
    itm_demon_head,itm_demon_foot,itm_demon_hand,
    itm_infreno_armor,itm_sg_purple_big
   ],
   horse_attrib_5|level(35),wp(200),knows_swordman_6|knows_magic_defence_5,nord_face_middle_1, nord_face_older_2],
  ["huge_inferno","huge_inferno","huge_inferno",
   tf_titan|tf_no_capture_alive|tf_guarantee_all_footman,0,0,fac_demon,
   [
    itm_huge_infreno_right_claw,itm_huge_infreno_left_claw,
    itm_demon_head,itm_demon_foot,itm_demon_hand,
    itm_huge_infreno_armor,itm_sg_purple_big,itm_sg_purple_big
   ],
   horse_attrib_6|str_100|level(50),wp(300),knows_swordman_8|knows_magic_defence_10,nord_face_middle_1, nord_face_older_2],



  ["france_town_recruit","France Townsman","France Townsman",
   tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_1,
   [
    itm_bolts,itm_hunting_crossbow,
    itm_spiked_club,itm_fighting_pick,itm_rapierd,
    itm_tab_shield_heater_a,
    itm_blue_gambeson,itm_arming_cap,itm_narf_hose
   ],
   foot_attrib_2|level(6),wp(80),knows_precise_shot_1|knows_militia,west_euro_face_1, west_euro_face_2],
      
   
  ["france_militia","France Militia","France Militia",
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_shield,0,0,fac_kingdom_1,
   [
    itm_spear,itm_war_spear,itm_ashwood_pike,
    itm_fighting_pick,itm_sword_medieval_b_small,itm_sword_medieval_a,
    itm_tab_shield_heater_b,
    itm_blue_gambeson,itm_padded_cloth,
    itm_arming_cap,itm_arming_cap,itm_gondor_light_helm,
    itm_narf_hose,itm_hose_kneecops_red
   ],
   foot_attrib_3|level(12),wp(95),knows_spearman_1,west_euro_face_1, west_euro_face_2],
         
  ["france_pikeman_1","France Pikeman","France Pikeman",
   tf_guarantee_all_pikeman,0,0,fac_kingdom_1,
   [
    itm_pike_2,itm_pike,
    itm_rapierd,
    itm_light_brigandine_black_mail,itm_light_brigandine_black,
    itm_hose_kneecops_red,itm_hose_kneecops_red,itm_leather_gloves,
    itm_gondor_light_helm,itm_gondor_light_helm,itm_gondor_light_helm
   ],
   foot_attrib_4|level(20),wp_melee(150),knows_pikeman_2,west_euro_face_1, west_euro_face_2],
  ["france_pikeman_2","France halberd","France halberd",
   tf_guarantee_all_pikeman,0,0,fac_kingdom_1,
   [
    itm_poleaxe,itm_pike,itm_pike_2,itm_swiss_halberd,
    
    itm_gondor_armor_low,
    itm_splinted_greaves,itm_splinted_leather_greaves,
    itm_gondor_infantry_helm,itm_gondor_infantry_helm,
    itm_wisby_gauntlets_black,itm_mail_mittens
    ],
   horse_attrib_3|level(24),wp_melee(200),knows_pikeman_4,west_euro_face_1, west_euro_face_2],
                  
  ["france_pikeman_3","France halberd Sergeant","France halberd Sergeant",
   tf_guarantee_all_pikeman,0,0,fac_kingdom_1,
   [
    itm_long_glaive,itm_long_voulge,itm_pike_2,
    itm_gondor_armor_med,itm_gondor_armor_low,
    itm_iron_greaves2,itm_iron_greaves,
    itm_gondor_guard_helm,itm_lorien_helm_d,itm_lorien_helm_d,
    itm_gondor_gauntlets,itm_gondor_gauntlets
   ],
   horse_attrib_5|level(35),wp_melee(250),knows_pikeman_6,west_euro_face_1, west_euro_face_2],
         
         
  ["france_swordsman_1","France Footman","France Footmen",
   tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_1,
   [
    itm_military_pick,itm_military_hammer,itm_bastard_sword_a,itm_bastard_sword_b,itm_longsword,
    
    itm_gon_footman,itm_gon_squire,itm_gon_regular,
    itm_gondor_shield_b,itm_gondor_shield_b,
    itm_mail_mittens,itm_leather_gloves,
    itm_mail_chausses,itm_mail_boots,
    itm_gondor_light_helm,itm_gondor_light_helm
   ],
   foot_attrib_4|level(18),wp_melee(155),knows_swordman_2,west_euro_face_1, west_euro_face_2],
            
  ["france_swordsman_2","France Infantry","France Infantry",
   tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_1,
   [
    itm_gondor_ranger_sword,itm_morningstar,itm_gondor_citadel_sword,
    
    itm_gondor_shield_a,itm_gondor_shield_a,
    itm_wisby_gauntlets_black,itm_gondor_gauntlets,
    itm_splinted_greaves,itm_iron_greaves,itm_iron_greaves2,
    itm_gon_knight,itm_gondor_armor_low,itm_gon_regular,
    itm_gondor_infantry_helm,itm_tower_archer_helm,itm_gondor_light_helm,
   ],
   horse_attrib_3|level(25),wp_melee(200),knows_swordman_4,west_euro_face_1, west_euro_face_2],
      
  ["france_swordsman_3","kingdom Armoured Swordsmen","Armoured Swordsmen Sergeants",
   tf_guarantee_all_footman,0,0,fac_kingdom_1,
   [
    itm_gondor_citadel_sword,
    itm_gondor_shield_c,
    itm_gondor_armor_med,itm_plate_armor_3,
    itm_iron_greaves2,itm_iron_greaves,
    itm_gondor_knight_helm,itm_gondor_guard_helm,itm_gondor_guard_helm,
    itm_gondor_gauntlets,
   ],
   horse_attrib_5|level(35),wp_melee(250),knows_swordman_6,west_euro_face_1, west_euro_face_2], 
   
  ["france_crossbow_1","France Peasant Archer","France Peasant Archer",
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves,0,0,fac_kingdom_1,
   [
    itm_arrows,itm_steel_arrow,itm_hunting_bow,itm_hunting_bow,itm_short_bow,
    itm_axe,itm_hatchet,itm_voulge,
    itm_gambeson,itm_padded_cloth,itm_ankle_boots,itm_arming_cap,itm_arming_cap
    ],
   ranged_attrib_3|level(14),wp(80),knows_archer_1,west_euro_face_1, west_euro_face_2],

  ["france_crossbow_2","France Skirmisher","France Skirmisher",
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_1,
   [
    itm_steel_arrow,itm_steel_arrow,itm_bolts,itm_steel_bolts,
    itm_long_bow,itm_rhod_crossbow,itm_crossbow,
    itm_battle_axe,itm_hand_axe,itm_longbowman_sword,
    itm_light_brigandine_black,
    itm_narf_hose,itm_kettle_hat_cloth2,itm_kettle_hat_cloth2
   ],
   ranged_attrib_4|level(20), wp_melee(90)|wp_archery(110)|wp_crossbow(130), knows_precise_shot_3|knows_archer_2|knows_crossbowman_1,west_euro_face_1, west_euro_face_2],
      
  ["france_archer_3","France Crossbowman","France Crossbowman",
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_1,
   [
    itm_steel_bolts,itm_steel_bolts,
    itm_sniper_crossbow,
    itm_gondor_shield_a,itm_gondor_shield_a,
    itm_bastard_sword_b,itm_military_pick,itm_military_hammer,
    itm_light_brigandine_black_mail,
    itm_hose_kneecops_red,itm_hose_kneecops_green,
    itm_kettle_hat_mail3,itm_zitta_bascinet_novisor,
    itm_wisby_gauntlets_black
    ],
   foot_attrib_5|level(25),wp(130)|wp_crossbow(180), knows_crossbowman_5,west_euro_face_1, west_euro_face_2],
      
  ["france_crossbow_3","France Arbalester","France Arbalester",
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_1,
   [
    itm_arbalest_1,itm_arbalest_2,itm_swadian_steel_bolts,
    itm_gondor_shield_c,itm_gondor_shield_c,    
    itm_bastard_sword_e,itm_side_sword,
    itm_gondor_armor_low,itm_iron_greaves,
    itm_zitta_bascinet,itm_zitta_bascinet_novisor,itm_gondor_gauntlets
    ],
   foot_attrib_5|level(28),wp(150)|wp_crossbow(220), knows_crossbowman_7,west_euro_face_1, west_euro_face_2],

  ["france_pikeman_4","France halberd Sergeant","France halberd Sergeant",
   tf_guarantee_all_pikeman,0,0,fac_kingdom_1,
   [
    itm_grey_knight_poleaxe,itm_grey_knight_poleaxe,
    
    itm_gondor_guard_helm,itm_gondor_guard_helm,

    itm_plate_armor_3,itm_knight_plate_3,
    itm_iron_greaves2,itm_iron_greaves,
    itm_gondor_gauntlets,
   ],
   horse_attrib_7|level(45),wp_melee(300),knows_physique_7|knows_shield_5|knows_power_strike_15|knows_ironflesh_12|knows_weapon_master_4|knows_stealth_10|knows_magic_defence_9,west_euro_face_1, west_euro_face_2],
         
  ["france_swordsman_4","kingdom Armoured Swordsmen","Armoured Swordsmen Sergeants",
   tf_guarantee_all_footman,0,0,fac_kingdom_1,
   [
    itm_amroth_sword_c,itm_dawnguard_javelin,
    itm_gondor_shield_d,
    itm_gondor_guard_helm,itm_gondor_guard_helm,
    itm_plate_armor_3,itm_knight_plate_3,
    itm_iron_greaves2,itm_iron_greaves,
    itm_gondor_gauntlets,
   ],
   horse_attrib_8|level(45),wp_melee(350),knows_physique_5|knows_shield_10|knows_power_strike_10|knows_ironflesh_15|knows_weapon_master_8|knows_magic_defence_10,west_euro_face_1, west_euro_face_2], 


  ["france_crossbow_4","France Arbalester","France Arbalester",
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_1,
   [
    itm_nord_bow_3,itm_nord_bow_3,itm_stahlrim_mutil_arrow,itm_stahlrim_arrow,
    itm_gondor_shield_d,itm_gondor_shield_d,    
    itm_amroth_sword_b,itm_amroth_sword_b,
    
    itm_gondor_guard_helm,itm_gondor_guard_helm,
    itm_plate_armor_3,itm_knight_plate_3,
    itm_iron_greaves2,itm_iron_greaves,
    itm_gondor_gauntlets,
    ],
   horse_attrib_6|level(45),wp(300), knows_physique_8|knows_shield_5|knows_power_strike_8|knows_ironflesh_10|knows_weapon_master_5|knows_stealth_5|knows_magic_power_5|knows_power_draw_10|knows_magic_defence_9,west_euro_face_1, west_euro_face_2],

  ["teutonic_pilgrim","Pilgrim","Pilgrims",
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, 0,0,fac_kingdom_1,
  [ 
    itm_wooden_staff_1,itm_magic_burning_gaze,itm_magic_earth_blood,
    itm_priest_robe_1,itm_priest_1_boots,itm_priest_cap_1,
    itm_pilgrim_hood,itm_teu_padded_cloth,

    ],
  horse_attrib_1|level(13),wp(100),knows_spearman_1|knows_magic_power_2|knows_magic_skill_4,west_euro_face_1, west_euro_face_2],

  ["teutonic_spearman","teutonic Squire","teutonic Squire",
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [
    itm_gondor_ranger_sword,itm_gondor_ranger_sword,
    itm_ashwood_pike,
    itm_gondor_shield_a,itm_gondor_shield_a,
    itm_dol_hauberk,
    #itm_teu_surcoat_over_mail_1,itm_teu_surcoat_over_mail_2,
    itm_mail_chausses,itm_mail_coif,itm_gondor_dolamroth_helm,itm_gondor_dolamroth_helm
    ],
   horse_attrib_2|level(20),wp_melee(130),knows_spearman_3|knows_magic_defence_4,west_euro_face_1, west_euro_face_2],

  ["teutonic_horse_1", "teutonic Knight", "teutonic Knight", 
   tf_mounted|tf_guarantee_all_lancer, 0, 0, fac_kingdom_1, 
   [
    itm_gondor_tower_spear,itm_amroth_sword_a,itm_amroth_sword_a,itm_gondor_shield_d,itm_gondor_shield_d,
    #itm_german_poleaxe_1,
    itm_wisby_gauntlets_black,
    itm_mail_and_plate,itm_iron_greaves,itm_gondor_dolamroth_helm_2,itm_barded_horse_teuton,itm_barded_horse_teuton
    ], 
   horse_attrib_3|level(27), wp_melee(200), knows_knight_foot_1|knows_twohand_4|knows_magic_defence_7, west_euro_face_1, west_euro_face_1 ],
  ["teutonic_horse_2", "teutonic Paladin", "teutonic Paladin", 
   tf_mounted|tf_guarantee_all_lancer, 0, 0, fac_kingdom_1, 
   [
    itm_gondor_lance,itm_amroth_sword_b,itm_amroth_sword_b,itm_amroth_sword_c,
    itm_dol_shield_a,itm_dol_shield_a,
    #itm_german_poleaxe_2,
    itm_dol_very_heavy_mail,itm_dol_very_heavy_mail,
    itm_swan_knight_helm,itm_iron_greaves,itm_wisby_gauntlets_black,itm_gondor_gauntlets,
    itm_warhorse_teuton,itm_warhorse_teuton,itm_sg_yellow_small
    ],
   horse_attrib_4|level(35), wp_melee(250), knows_knight_foot_3|knows_twohand_5|knows_magic_defence_10, west_euro_face_1, west_euro_face_1 ],
  ["teutonic_horse_3", "teutonic Defender Of Faith", "teutonic Defender Of Faith", 
   tf_mounted|tf_guarantee_all_lancer, 0, 0, fac_kingdom_1, 
   [
    itm_gothic_lance,itm_gothic_lance,
    #itm_sword_two_handed_c_alt,itm_german_poleaxe_3,
    itm_amroth_sword_c,itm_amroth_sword_c,itm_dol_shield_b,itm_dol_shield_b,
    itm_swan_milanese_plate,itm_swan_milanese_plate,itm_trophy_b,
    itm_iron_greaves,itm_winged_great_helmet_teu,itm_winged_great_helmet_teu,itm_gondor_gauntlets,
    itm_charger_teuton,itm_charger_teuton,itm_sg_yellow_small
   ],
  horse_attrib_6|level(40), wp_melee(300), knows_knight_foot_5|knows_twohand_7|knows_magic_defence_10, west_euro_face_1, west_euro_face_2 ],

  ["teutonic_sword","teutonic War Clerics","teutonic War Clerics",
   tf_guarantee_all_wo_horse, 0,0,fac_kingdom_1,
  [ 
   itm_tab_shield_heater_b,itm_shield_heater_c,
   itm_war_clerics_warhammer,itm_morningstar,
   #itm_magic_heaven_fist_throw_1,
   itm_bishop_armour,itm_bishop_great_helm,itm_wisby_gauntlets_black,
   itm_bishop_armour,itm_toumingtou,itm_wisby_gauntlets_black,
   itm_mail_boots,
  ],
  horse_attrib_1|level(27),wp(160),knows_spearman_4|knows_magic_defence_3|knows_magic_power_2|knows_magic_skill_5,west_euro_face_1, west_euro_face_2],
    
  ["teutonic_dis_halbbruder", "teutonic Inquisitor", "teutonic Inquisitor", 
  tf_guarantee_all_wo_horse, 0, 0, fac_kingdom_1, 
  [
   #itm_morningstar,
   #itm_magic_heaven_fist_throw_2,itm_magic_heaven_fist_throw_1,
   itm_shield_heater_c,itm_war_clerics_warhammer_2,
   itm_shield_heater_c,itm_war_clerics_warhammer_2,
   itm_empire_priest,itm_empire_priest,
   itm_trophy_a,
   itm_iron_greaves,itm_toumingtou,itm_gondor_gauntlets,itm_gondor_gauntlets,itm_sg_human_small
  ], 
  horse_attrib_3|level(35), wp(240), knows_spearman_6|knows_magic_defence_5|knows_magic_power_4|knows_magic_skill_6, west_euro_face_1, west_euro_face_2 ],
  ["teutonic_dis_knight","teutonic crusader","teutonic crusader", 
  tf_guarantee_all_wo_horse, 0, 0, fac_kingdom_1, 
  [
   #itm_magic_heaven_fist,itm_war_clerics_warhammer_2,
   #itm_steel_shield,itm_steel_shield,
   itm_crusader_sword_1,itm_crusader_sword_1,
   #itm_magic_heaven_fist_throw_2,itm_magic_heaven_fist_throw_1,
   itm_white_twiligh_armor,itm_steel_greaves,itm_gondor_gauntlets,itm_black_helmet2,
   itm_white_twiligh_armor,itm_steel_greaves,itm_gondor_gauntlets,itm_black_helmet2,
   itm_trophy_a,itm_sg_yellow_small
  ],
  horse_attrib_6|level(40),wp(280), knows_spearman_8|knows_magic_defence_7|knows_magic_power_5|knows_magic_skill_7, west_euro_face_1, west_euro_face_2 ],

  ["dunedain_ranger","dunedain_ranger","dunedain_ranger",
   tf_guarantee_all_wo_horse,0,0,fac_kingdom_1,
   [
    itm_woodelf_arrows_freezing,itm_woodelf_mutil_arrows,itm_lorien_bow_2,
    itm_courtblades_ivory,
    itm_armor9,itm_assasin_hood_4,itm_splinted_leather_greaves,
    itm_armor9,itm_assasin_hood_4,itm_splinted_leather_greaves,
   ], 
   horse_attrib_6|level(50),wp_melee(280)|wp_archery(350),knows_magic_power_7|knows_ranger_8,west_euro_face_1,west_euro_face_2],

  ["france_horse_1","France Militia_Cavalary","France Militia_Cavalary",
   tf_guarantee_all_pikeman, 0, 0, fac_hospitalier_knights, 
   [itm_gondor_shield_a,
   itm_pike_2,itm_long_pike,itm_pike,itm_gondor_ranger_sword,
   itm_teu_surcoat_over_mail_2,itm_mail_chausses,itm_kettle_hat
   ], 
  horse_attrib_2|level(24), wp(160), knows_pikeman_5,west_euro_face_1, west_euro_face_2],
      
  ["france_horse_2","teutonic Holy Avenger","teutonic Holy Avenger",
  tf_guarantee_all_wo_horse, 0, 0, fac_kingdom_1, 
   [
   itm_crusader_sword_2,itm_crusader_sword_2,
   itm_magic_heaven_fist_throw_2,itm_magic_heaven_fist_throw_2,
   itm_elf_twiligh_armor,itm_amade_bronze_greaves,itm_amade_bronze_gauntlets,itm_black_helmet_2,
   itm_elf_twiligh_armor,itm_amade_bronze_greaves,itm_amade_bronze_gauntlets,itm_black_helmet_2,
   itm_trophy_a,itm_sg_yellow_small
   ],
   horse_attrib_8|level(45),wp_melee(350)|wp_throwing(400),knows_physique_10|knows_shield_10|knows_power_strike_15|knows_ironflesh_15|knows_reserved_18_10|knows_weapon_master_10|knows_magic_defence_5|knows_magic_power_7|knows_magic_skill_1|knows_thrown_4,west_euro_face_1, west_euro_face_2],


  ["france_horse_3","France Man at Arms","France Men at Arms",tf_guarantee_all_wo_horse,0,0,fac_kingdom_1,
   [
    itm_grey_knight_poleaxe,itm_grey_knight_poleaxe,
    itm_bolt_burning_gaze,itm_crossbow_cannon,
    itm_gondor_fountain_armor,itm_gondor_fountain_armor,
    itm_french_helm_2,itm_french_helm_3,
    itm_steel_greaves,
    itm_trophy_a,
    itm_marksman_gloves],
   horse_attrib_8|level(45),wp(400),knows_precise_shot_8|knows_knight_3|knows_twohand_8|knows_magic_defence_10,west_euro_face_1, west_euro_face_2],

  ["france_horse_4","France Gendarme","France Gendarmes",
    tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
   [
    itm_mjolnir,itm_dwarf_thunder_maul,
    itm_amroth_sword_c,itm_amroth_sword_c,
    #itm_sword_two_handed_a,
    itm_gondor_shield_e,itm_gondor_shield_e,
    itm_white_twiligh_armor,itm_white_twiligh_armor,
    itm_steel_greaves,itm_steel_greaves,
    itm_black_helmet2,itm_black_helmet2,
    
    itm_armor_griffin,itm_armor_griffin,
    itm_trophy_b,
    itm_gondor_gauntlets,itm_hourglass_gauntlets_ornate
   ],
  horse_attrib_8|level(45),wp_melee(300)|wp_throwing(300),knows_knight_6|knows_spearman_8|knows_power_throw_6|knows_horse_archery_10|knows_magic_power_8,west_euro_face_1, west_euro_face_2],

  ["england_town_recruit","England Townsman","England Townsman",tf_guarantee_shield | tf_guarantee_armor | tf_guarantee_boots,0,0,fac_kingdom_4,
   [
    itm_boar_spear,itm_shortened_spear,itm_spear,itm_war_spear,
    itm_sword_medieval_c_long,
    itm_tab_shield_heater_a,
   
    itm_aketon,itm_aketon,itm_padded_coif,itm_padded_coif,itm_narf_hose],
   foot_attrib_2|level(6),wp(100),knows_spearman_1,nord_face_young_1, nord_face_old_2],
   
  ["england_militia","England Militia","England Militia",
   tf_guarantee_boots|tf_guarantee_armor | tf_guarantee_boots|tf_guarantee_shield,0,0,fac_kingdom_4,
   [itm_boar_spear,itm_shortened_spear,itm_spear,itm_war_spear,itm_ashwood_pike,
    itm_sword_medieval_c_long,itm_military_pick,
    itm_tab_shield_heater_a,
    itm_light_brigandine_red_mail,itm_light_brigandine_red,
    itm_nasal_helmet,itm_footman_helmet,itm_nasal_helmet,
    itm_narf_hose,itm_hose_kneecops_red,itm_narf_hose],
   foot_attrib_3|level(12),wp(140),knows_spearman_2,nord_face_young_1, nord_face_old_2],
      
  ["england_billmen_1","England billmen","England billmen",
   tf_guarantee_all_pikeman,0,0,fac_kingdom_4,
   [
    itm_english_bill,itm_guisarme_2,
    itm_leather_gloves,itm_mail_mittens,
    itm_narf_hose,itm_hose_kneecops_red,
    itm_brigandine_plate_red,itm_brigandine_red,itm_brigandine_red,
    itm_kettle_hat_mail3,itm_kettle_hat_cloth1,itm_kettle_hat_cloth3,
    itm_sallet_coif],
   foot_attrib_4|level(20),wp_melee(160),knows_physique_2|knows_billman_3,nord_face_young_1, nord_face_old_2],
   
  ["england_billmen_2","England Armoured billmen","England Armoured billmen",
   tf_guarantee_all_pikeman,0,0,fac_kingdom_4,
   [
    itm_english_bill,itm_guisarme,
    itm_mail_mittens,itm_plate_mittens,
    itm_mail_chausses,itm_mail_boots,
    itm_corrazina_red,itm_half_plates_red,
    itm_zitta_bascinet_novisor,itm_zitta_bascinet],
   foot_attrib_6|level(28),wp_melee(230),knows_physique_4|knows_billman_6,nord_face_young_1, nord_face_old_2],

  ["england_swordsman_1","England Man-at-Arm","England Man-at-Arm",
   tf_guarantee_all_footman,0,0,fac_kingdom_4,
   [
    itm_bastard_sword_b,itm_bastard_sword_e,
    #itm_sword_claymore_01,itm_sword_claymore_02,
    
    itm_tab_shield_kite_c,
    itm_tab_shield_heater_c,
    itm_leather_gloves,itm_mail_mittens,
    itm_leather_boots,itm_mail_chausses,
    itm_early_transitional_e1,itm_early_transitional_e1,
    itm_corrazina_red,
    itm_kettle_hat_mail1,itm_zitta_bascinet_novisor],
   foot_attrib_4|level(20),wp_melee(150),knows_physique_2|knows_shield_5|knows_power_strike_4|knows_ironflesh_6|knows_reserved_18_10|knows_weapon_master_1|knows_magic_defence_3,nord_face_young_1, nord_face_old_2],
      
  ["england_swordsman_2","England Armoured Swordsmen","England Armoured Swordsmen",
   tf_guarantee_all_footman,0,0,fac_kingdom_4,
   [
    #itm_bec_de_corbin_a,itm_polehammer_threeprong,
    itm_glass_sword_b,itm_scimitar_green,
    #itm_bec_de_corbin_a,itm_poleaxe,itm_german_poleaxe_1,
    
    itm_tab_shield_kite_d,
    itm_tab_shield_heater_d,
    itm_mail_mittens,itm_wisby_gauntlets_black,itm_plate_mittens,
    
    itm_half_plates_red,itm_half_plates_red,itm_half_plates_red_2,
    itm_splinted_greaves,itm_iron_greaves,itm_open_sallet,itm_mail_mittens,itm_plate_mittens],
   foot_attrib_6|level(30),wp_melee(200),knows_physique_3|knows_shield_7|knows_power_strike_6|knows_ironflesh_9|knows_reserved_18_10|knows_weapon_master_4|knows_magic_defence_5,nord_face_young_1, nord_face_old_2],
           
  ["england_billmen_3","England Armoured billmen","England Armoured billmen",
   tf_guarantee_all_pikeman,0,0,fac_kingdom_4,
   [
    itm_glass_halberd,itm_glass_halberd,
    itm_glass_head,itm_glass_head,
    itm_glass_male_plate,itm_glass_male_plate,
    itm_trophy_b,itm_trophy_a,
    itm_glass_foot,itm_glass_hand,
    itm_glass_foot,itm_glass_hand,
   ],
   str_60|agi_15|int_12|cha_12|level(45),wp_melee(280),knows_physique_9|knows_shield_4|knows_power_strike_12|knows_ironflesh_8|knows_reserved_18_10|knows_weapon_master_9|knows_magic_defence_9,nord_face_young_1, nord_face_old_2],
            
  ["england_swordsman_3","England Dismounted_Knight","England Dismounted_Knight",
   tf_guarantee_all_footman,0,0,fac_kingdom_4,
   [
    itm_glass_sword_a,
    itm_mirkwood_sword_reward,itm_glass_sword_c,
    itm_glass_shield,itm_glass_shield,
    #itm_dragon_plate,itm_dragon_plate,
    #itm_dragon_foot,itm_dragon_foot,
    itm_trophy_b,itm_trophy_a,
    #itm_dragon_head,itm_dragon_head,itm_dragon_knight_hand,
    
    itm_glass_head,itm_glass_head,
    itm_glass_male_plate,itm_glass_male_plate,
    itm_glass_foot,itm_glass_hand,
    itm_glass_foot,itm_glass_hand,
    ], 
   str_60|agi_15|int_12|cha_12|level(45),wp_melee(280),knows_physique_4|knows_shield_9|knows_power_strike_8|knows_ironflesh_13|knows_reserved_18_10|knows_weapon_master_9|knows_magic_defence_8,nord_face_young_1, nord_face_old_2],
                        
  ["england_longbowm_1","England yeoman","England yeoman",
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_arrows,itm_arrows,itm_long_bow,
    itm_longbowman_sword,itm_sword_medieval_b_small,
    itm_one_handed_war_axe_b,itm_one_handed_battle_axe_a,
    itm_tab_shield_small_round_a,
    itm_aketon,itm_light_brigandine_red,itm_footman_helmet,itm_nasal_helmet,itm_narf_hose,itm_narf_hose,itm_narf_hose],
   foot_attrib_2|level(12),wp_melee(135)|wp_archery (160),knows_physique_2|knows_archer_2,nord_face_young_1, nord_face_old_2],
            
  ["england_longbowm_2","England longbowman","England longbowman",
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_bodkin_arrows,itm_bodkin_arrows,itm_long_bow,
    itm_longbowman_sword,itm_sword_medieval_b_small,itm_one_handed_battle_axe_b,
    itm_tab_shield_small_round_b,
    itm_long_axe_b_alt,
    itm_leather_gloves,
    itm_hose_kneecops_red,itm_narf_hose,
    itm_light_brigandine_red_mail,itm_light_brigandine_red_mail,
    itm_kettle_hat_cloth1,itm_kettle_hat_cloth2,itm_kettle_hat_cloth3,
   ],
   foot_attrib_3|level(18),wp_melee(145)|wp_archery (180),knows_physique_2|knows_archer_4,nord_face_young_1, nord_face_old_2],

  ["england_longbowm_3","England Retinue Longbowmen","England Retinue Longbowmen",
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_piercing_arrows,itm_bodkin_arrows,itm_long_bow_2,
    itm_glass_mace,
    itm_tab_shield_small_round_c,
    itm_leather_gloves,
    itm_leather_boots,itm_splinted_leather_greaves,
    #itm_hose_kneecops_red,itm_hose_kneecops_red,
    itm_padded_leather,itm_studded_leather_coat,
    itm_kettle_hat_mail1,itm_kettle_hat_mail2,itm_kettle_hat_mail3,
    ],
   foot_attrib_5|level(26),wp_melee(180)| wp_archery (220),knows_physique_2|knows_archer_6,nord_face_young_1, nord_face_old_2],

  ["england_longbowm_4","England Retinue Longbowmen","England Retinue Longbowmen",
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_piercing_arrows,itm_piercing_arrows,itm_long_bow_3,
    #itm_long_axe_c,itm_long_axe_b,
    itm_glass_mace_2,
    itm_tab_shield_small_round_c,
    itm_leather_gloves,
    itm_splinted_leather_greaves,itm_trophy_a,
    itm_ranger_armor4,itm_open_sallet],
   horse_attrib_6|level(40),wp_melee(220)| wp_archery (350),knows_physique_4|knows_archer_9,nord_face_young_1, nord_face_old_2],

  ["england_horse_1", "England Hobilar", "England Hobilar",
    tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_nord_javelin,itm_tab_shield_kite_a,
    itm_one_handed_war_axe_a,itm_war_spear,

    itm_light_brigandine_red,itm_light_brigandine_red_mail,
    itm_kettle_hat_cloth2,itm_leather_gloves,itm_narf_hose,
    itm_nord_horse,itm_nord_horse],
   horse_attrib_2|level(20),wp(150),knows_thrown_3|knows_riding_4,nord_face_young_1, nord_face_old_2],

  ["england_horse_2", "England Border Horse", "England Border Horse",
    tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_tab_shield_kite_b,
    itm_one_handed_war_axe_b,itm_glass_javelin,
    itm_kettle_hat_mail2,itm_zitta_bascinet_novisor,
    itm_brigandine_red,itm_brigandine_plate_red,
    itm_cav_boots,itm_leather_gloves,
    itm_nord_courser,itm_nord_courser],
   horse_attrib_3|level(26),wp(180),knows_riding_5|knows_thrown_4,nord_face_young_1, nord_face_old_2],

  ["england_horse_3", "England Demi Lancers", "England Demi Lancers", 
   tf_mounted|tf_guarantee_all_lancer, no_scene, reserved, fac_kingdom_4, 
   [
    itm_bastard_sword_e,
    itm_tab_shield_kite_c,
    itm_nord_hunter,itm_nord_hunter,itm_glass_lance,itm_glass_lance_2,
    itm_sallet_coif,itm_open_sallet_coif,
    #itm_sturmhaube_w1,itm_sturmhaube_w2,
    itm_cav_boots,itm_leather_gloves,
    itm_corrazina_red,itm_half_plates_red,itm_half_plates_red_2,
   ], 
   horse_attrib_4|level(30),wp_melee(230),knows_riding_5|knows_spearman_5,nord_face_young_1, nord_face_old_2],

   
  ["german_town_recruit","German Townsman","German Townsman",
   tf_guarantee_shield | tf_guarantee_armor | tf_guarantee_boots,0,0,fac_kingdom_7,
   [
    itm_mace_1,itm_mace_2,itm_pitch_fork,itm_shortened_spear,itm_sword_medieval_b,
    itm_tab_shield_heater_a,itm_tab_shield_small_round_b,
    itm_aketon,itm_aketon,itm_yellow_gambeson,itm_arming_cap,itm_landsknecht_hat_yellow,itm_narf_hose],
   foot_attrib_2|level(6),wp(60),knows_militia,swadian_face_face_1, swadian_face_face_2],


  ["german_militia","German Militia","German Militia",
   tf_guarantee_boots|tf_guarantee_armor | tf_guarantee_boots|tf_guarantee_helmet,0,0,fac_kingdom_7,
   [itm_pike,itm_pike_2,itm_pike_2,itm_ashwood_pike,itm_ashwood_pike,
    itm_sword_medieval_b,itm_sword_medieval_c_small,
    #itm_light_brigandine_yellow,itm_light_brigandine_yellow_mail,itm_light_brigandine_yellow,
    itm_german_armour_1,itm_blue_armour_1,itm_red_armour_1,
    itm_landsknecht_hat_yellow,itm_kettle_hat_3,itm_arming_cap,itm_hose_kneecops_red],
   foot_attrib_3|level(12),wp(80),knows_spearman_2,swadian_face_face_1, swadian_face_face_2],
  
  ["german_pikeman_1","Landschneckt Pikeman","Landschneckt Pikeman",
   tf_guarantee_all_pikeman,0,0,fac_kingdom_7,
  [
   itm_long_pike_2,itm_pike_2,itm_long_pike,
   itm_sword_medieval_c_small,itm_sword_medieval_c,
   itm_beret_plain_brown,itm_beret_plumes_red,itm_kettle_hat_3,itm_open_sallet,
   itm_german_armour_2,itm_blue_armour_2,itm_red_armour_2,
   
   itm_splinted_greaves],
   horse_attrib_2|level(18),wp_melee(100)|wp_polearm (150), knows_pikeman_3,swadian_face_face_1, swadian_face_face_2],
  ["german_pikeman_2","Landschneckt Armoured Pikeman","Landschneckt Armoured Pikeman",
   tf_guarantee_all_pikeman,0,0,fac_kingdom_7,
  [
   itm_long_pike_2,itm_pike_2,itm_long_pike,
   itm_side_sword,itm_sword_medieval_c,
   itm_beret_plumes_brown,itm_beret_plumes_red,itm_kettle_hat_3,itm_open_sallet,
   itm_german_armour_3,itm_blue_armour_3,
   itm_splinted_greaves],
   horse_attrib_3|level(28),wp_melee(120)|wp_polearm (220), knows_pikeman_5,swadian_face_face_1, swadian_face_face_2],
     
  ["german_pikeman_3","Landschneckt Tercio Pikeman","Landschneckt Tercio Pikeman",
   tf_guarantee_all_pikeman,0,0,fac_kingdom_7,
   [
    itm_long_pike,itm_long_pike_2,
    itm_bastard_sword_f,itm_side_sword,itm_steel_shield,
    itm_splinted_leather_greaves,itm_leather_gloves,  
    itm_bnw_gauntlets,itm_bnw_splinted_greaves,
    itm_red_armour_4,itm_red_armour_4,
    itm_combed_morion_3,itm_combed_morion_2,itm_sallet_beret_plain_brown,itm_sallet_beret_plain_red,itm_sallet_beret_plumes_red
    ],
   horse_attrib_4|level(38),wp_melee(220)|wp_polearm (300), knows_pikeman_7,swadian_face_face_1, swadian_face_face_2],
  
  ["german_twohander_1", "Landschneckt Forlorn Hope", "Landschneckt Forlorn Hope", 
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, no_scene, reserved, fac_kingdom_7, 
  [itm_great_sword,itm_sword_two_handed_c_alt,
   itm_german_armour_4,itm_red_armour_5,itm_splinted_greaves,itm_combed_morion_3,itm_bnw_gauntlets
   ], 
  horse_attrib_2|level(20), wp_melee(150), knows_twohand_3, swadian_face_face_1, swadian_face_face_2 ],
  ["german_twohander_2", "Landschneckt Doppelsoeldner", "Landschneckt Doppelsoeldners", tf_guarantee_all_footman, no_scene, reserved, fac_kingdom_7, 
  [itm_flamberge,itm_flamberge_alt,itm_trophy_a,
   itm_german_armour_5,itm_red_armour_5,itm_blue_armour_5,
   itm_steel_greaves,itm_sallet_coif_ger,itm_hourglass_gauntlets_ornate,
   itm_steel_greaves,itm_sallet_beret_plumes_red,itm_hourglass_gauntlets_ornate,
  ], 
  horse_attrib_4|level(30), wp_melee(220), knows_twohand_6|knows_physique_3|knows_magic_defence_2|knows_weapon_master_2, swadian_face_face_1, swadian_face_face_2 ],
  
  ["german_twohander_3", "Landschneckt Champion", "German Champion", tf_guarantee_all_footman, no_scene, reserved, fac_kingdom_7, 
  [itm_ebony_great_sword,itm_trophy_b,
   itm_maximilian_plate,itm_maximilian_plate,
   itm_maximilian_greaves,itm_sallet_coif_ger,itm_hourglass_gauntlets_ornate,
   itm_maximilian_greaves,itm_sallet_beret_plumes_red,itm_hourglass_gauntlets_ornate,
  ], 
  horse_attrib_6|level(45), wp_melee(300), knows_twohand_8|knows_physique_3|knows_magic_defence_10|knows_weapon_master_10, swadian_face_face_1, swadian_face_face_2 ],

    
    
  ["german_crossbow_1","German Crossbow Militia","German Crossbow Militia",
  tf_guarantee_all_wo_horse,0,0,fac_kingdom_7,
   [
    itm_sword_medieval_a,itm_mace_2,itm_fighting_pick,
    itm_tab_shield_pavise_b,itm_tab_shield_pavise_a,
    itm_rhod_crossbow,itm_bolts,itm_steel_bolts,itm_swadian_steel_bolts,itm_cartridges,itm_samopal,
    itm_kettle_hat_cloth3,itm_kettle_hat_cloth1,itm_landsknecht_hat_yellow,
    itm_light_brigandine_yellow,itm_light_brigandine_yellow,itm_hose_kneecops_red
   ],
   foot_attrib_3|level(12),wp_melee(90)|wp_crossbow (135)|wp_firearm(150),knows_firearm_2,swadian_face_face_1, swadian_face_face_2],

  ["german_crossbow_2","Landschneckt Musketeer","Landschneckt Musketeer",
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_7,
   [
    itm_cartridges,
    itm_light_muscket_1,itm_light_muscket_2,itm_light_muscket_3,itm_light_muscket_4,
    itm_rapierd,itm_sword_medieval_b,itm_side_sword,
    itm_leather_gloves,itm_splinted_leather_greaves,itm_leather_boots,
    itm_blue_armour_1,itm_blue_armour_1,
    itm_beret_plumes_brown,itm_landsknecht_hat_yellow,itm_beret_plain_brown
    ],
   foot_attrib_4|level(20),wp_melee(110)|wp_firearm(200),knows_firearm_3,swadian_face_face_1, swadian_face_face_2],
   
  ["german_crossbow_3","Landschneckt Veteran Musketeer","Landschneckt Veteran Musketeer",
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_7,
   [itm_cartridges_thrust,    
    itm_medium_muscket_1,itm_medium_muscket_2,itm_medium_muscket_3,
    itm_rapierd,itm_sword_medieval_b,itm_side_sword,
    itm_leather_gloves,itm_splinted_leather_greaves,
    itm_blue_armour_2,itm_blue_armour_2,
    itm_combed_morion,itm_beret_plumes_brown,itm_sallet_beret_plain_brown
   ],
   foot_attrib_5|level(25),wp_melee(120)|wp_firearm(250),knows_firearm_5,swadian_face_face_1, swadian_face_face_2],

  ["german_crossbow_4","Landschneckt Tercio Musketeer","Landschneckt Tercio Musketeer",
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_7,
   [itm_cartridges_thrust,itm_cartridges_thrust,
    itm_heavy_muscket_1,itm_heavy_muscket_2,itm_heavy_muscket_3,
    itm_espada_eslavona_b,
    itm_leather_gloves,itm_splinted_greaves,
    itm_blue_armour_3,itm_blue_armour_3,
    itm_combed_morion,itm_sallet_beret_plain_brown],
   foot_attrib_6|level(30),wp_melee(200)|wp_firearm(350),knows_precise_shot_6|knows_light_swordman_8,swadian_face_face_1, swadian_face_face_2],

  ["german_crossbow_5","Landschneckt Tercio Musketeer","Landschneckt Tercio Musketeer",
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_7,
   [itm_cartridges_sissofbattle_bolter,itm_cartridges_sissofbattle_bolter,
    itm_heavy_muscket_4,
    itm_espada_eslavona_b,
    itm_marksman_gloves,itm_splinted_greaves,
    itm_blue_armour_4,itm_blue_armour_4,
    itm_sallet_beret_plain_brown,itm_sallet_beret_plain_brown],
   horse_attrib_5|level(40),wp_melee(350)|wp_firearm(400),knows_precise_shot_10|knows_light_swordman_8,swadian_face_face_1, swadian_face_face_2],



  ["witch_hunter","Witch Hunter","Witch Hunters",
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_7,
   [itm_cartridges_sissofbattle_bolter,itm_cartridges_sissofbattle_bolter_2,itm_cartridges_sissofbattle_holy,
      
    itm_sissofbattle_e5,
    itm_dawnguard_greatsword,itm_ebony_bastard_sword,
    itm_marksman_gloves,itm_splinted_greaves,
    itm_emp_wh_armor1,itm_emp_wh_armor1,
    itm_emp_wh_helmet1,itm_emp_wh_helmet1,itm_sg_yellow_small],
   horse_attrib_7|level(40),wp_melee(400)|wp_firearm(400),knows_precise_shot_10|knows_magic_defence_10|knows_stealth_10|knows_physique_8|knows_shield_6|knows_power_strike_10|knows_ironflesh_9|knows_reserved_18_10|knows_weapon_master_9,swadian_face_face_1, swadian_face_face_2],


  ["iberian_town_militia","iberian Town Militia","iberian Town Militia",
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_7,
   [
    itm_javelin,itm_darts,itm_war_darts,
    itm_ashwood_pike,
    itm_tab_shield_small_round_b,itm_tab_shield_small_round_c,
    itm_sword_medieval_a,itm_sword_medieval_b,
    itm_combed_morion_blued,itm_kettle_hat_3,itm_light_brigandine_yellow,
    #itm_light_brigandine_yellow,itm_light_brigandine_yellow_mail,
    itm_german_armour_2,itm_blue_armour_2,itm_red_armour_2,
   itm_german_armour_3,itm_blue_armour_3,itm_red_armour_3,
    itm_hose_kneecops_red],
   foot_attrib_3|level(12),wp(100),knows_light_swordman_2|knows_power_throw_1,swadian_face_face_1, swadian_face_face_2],

  ["iberian_town_footman_1","iberian Infantry","iberian Infantry",
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_7,
  [
   itm_side_sword,itm_sword_medieval_b,itm_plate_covered_round_shield,
   itm_flintlock_pistol_2,itm_flintlock_pistol,itm_cartridges,itm_granata_small,
   itm_sturmhaube_w1,itm_combed_morion_blued,itm_combed_morion,
   itm_german_armour_3,itm_blue_armour_3,itm_red_armour_3,
    itm_german_armour_4,itm_blue_armour_4,itm_red_armour_4,
   #itm_german_armour_3,itm_german_armour_2,itm_german_armour_4,
   itm_splinted_leather_greaves,itm_leather_gloves
  ],
  horse_attrib_3|level(20),wp(150),knows_precise_shot_2|knows_light_swordman_4|knows_power_throw_2,swadian_face_face_1,swadian_face_face_2],

  ["iberian_town_footman_2","iberian Sword_and_Buckler_Men","iberian Sword_and_Buckler_Men",
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_7,
   [
    itm_side_sword,itm_sword_medieval_b,itm_steel_shield,
    itm_espada_eslavona_b,
    itm_flintlock_pistol_veteran_2,itm_flintlock_pistol_veteran_3,
    itm_cartridges,itm_granata_small,
    itm_combed_morion_3,itm_combed_morion_2,itm_combed_morion_2,
    itm_german_armour_4,itm_blue_armour_4,itm_red_armour_4,
    itm_german_armour_6,itm_german_armour_6,
    itm_bnw_splinted_greaves,itm_bnw_gauntlets
   ],
   horse_attrib_4|level(30),wp(250)|wp_firearm(250),knows_precise_shot_4|knows_light_swordman_5|knows_power_throw_3,swadian_face_face_1, swadian_face_face_2],

  ["iberian_town_footman_3","iberian Conquistadore","iberian Conquistadores",
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_7,
   [
    itm_espada_eslavona_b,itm_dawnguard_hammer,itm_war_clerics_warhammer,itm_shield_heater_c,itm_shield_heater_c,
    itm_flintlock_pistol_elite_1,itm_flintlock_pistol_elite_2,itm_cartridges_burst,itm_cartridges,itm_granata_medium,
    itm_sigma_knight_plate,itm_sigma_knight_foot,itm_sigma_knight_head,itm_sigma_knight_hand,
    itm_german_armour_6,itm_steel_greaves,itm_sallet_beret_plumes_brown,itm_hourglass_gauntlets_ornate,
   ],
   horse_attrib_6|level(45),wp(350),knows_precise_shot_6|knows_light_swordman_8|knows_power_throw_4,swadian_face_face_1, swadian_face_face_2],

  ["iberian_dragoon_1","German Dragoon","German Dragoons",
    tf_mounted|tf_guarantee_all_nomad,0,0,fac_kingdom_7,
   [itm_carbine,itm_cartridges_burst,
    itm_side_sword,itm_lance,
    itm_kettle_hat_3,itm_sturmhaube_w1,itm_sturmhaube_w2,
    itm_blue_armour_2,itm_red_armour_3,
    itm_cav_boots,
    itm_courser,itm_courser,itm_hunter,itm_armored_horse_german],
  horse_attrib_2|level(20),wp_melee(110)|wp_firearm(200),knows_horse_shoot_5|knows_firearm_3,swadian_face_face_1, swadian_face_face_2],
  ["iberian_knight_2","German Demi Lancers","German Demi Lancers",
  tf_mounted|tf_guarantee_all_lancer,0,0,fac_kingdom_7,
   [
    itm_great_lance,itm_sword_medieval_b,itm_sword_medieval_b,itm_tab_shield_kite_c,itm_bastard_sword_b,
    
    itm_sturmhaube_bnw3,itm_sturmhaube_bnw2,itm_combed_morion_2,
    itm_blue_armour_3,itm_red_armour_4,
    itm_warhorse_german,itm_barded_horse_german,itm_barded_horse_german,
    itm_bnw_splinted_greaves,itm_bnw_gauntlets
   ],
   horse_attrib_4|level(30),wp(190),knows_riding_5|knows_light_swordman_5,swadian_face_face_1, swadian_face_face_2],

  ["iberian_knight_3","German Conquistadore","German Conquistadores",
  tf_mounted|tf_guarantee_all_lancer,0,0,fac_kingdom_7,
   [
    itm_great_lance_dark,itm_espada_eslavona_b,itm_steel_shield,itm_morningstar,
    #itm_sturmhaube_bnw4,itm_classichelm_plume,itm_classichelm_plume,
     itm_combed_morion_2,itm_combed_morion_2,itm_combed_morion_2,
    itm_charger_german,itm_charger_noble,itm_trophy_b,itm_sg_human_small,
    itm_german_armour_6,itm_german_armour_6,itm_iron_greaves2,itm_iron_greaves2,itm_hourglass_gauntlets_ornate
   ],
   horse_attrib_5|level(40),wp(300),knows_knight_order_6|knows_light_swordman_7,swadian_face_face_1, swadian_face_face_2],
      
  ["german_reitern_1","German Reiter","German Reiter",
  tf_mounted|tf_guarantee_all,0,0,fac_kingdom_7,
   [
    itm_pistol_2stwol,itm_cartridges_burst,
    itm_side_sword,
    itm_cartridges_burst,itm_tab_shield_heater_c,
    itm_german_armour_4,itm_splinted_greaves,itm_sturmhaube_w3,itm_sturmhaube_w4,
    itm_barded_horse_german,itm_barded_horse_german,itm_armored_horse_german
   ],
   horse_attrib_3|level(30),wp_melee(160)|wp_firearm(250),knows_knight_1|knows_firearm_4|knows_horse_archery_6,swadian_face_face_1, swadian_face_face_2],
  ["german_reitern_2","German Black_Reiter","German Black_Reiter",
  tf_mounted|tf_guarantee_all,0,0,fac_kingdom_7,
   [
    itm_reitern_pistol_4s,itm_cartridges_burst,
    itm_espada_eslavona_b,itm_bastard_sword_f,itm_trophy_a,
    itm_cartridges_burst,itm_tab_shield_heater_d,
    itm_bnw_armour_german,itm_bnw_splinted_greaves,itm_bnw_gauntlets,itm_sturmhaube_bnw4,
    itm_charger_german,itm_charger_german,itm_warhorse_german,itm_warhorse_german
   ],
   horse_attrib_5|level(38),wp_melee(200)|wp_firearm(320),knows_knight_3|knows_firearm_6|knows_horse_archery_8,swadian_face_face_1, swadian_face_face_2],

  ["german_reitern_3","German Black_Reiter","German Black_Reiter",
  tf_mounted|tf_guarantee_all,0,0,fac_kingdom_7,
   [
    itm_musket_hand_gun,itm_cartridges_cannon_1,itm_cartridges_burst,
    itm_bastard_sword_f,itm_trophy_a,

    itm_bnw_armour_german,itm_bnw_splinted_greaves,itm_bnw_gauntlets,itm_sturmhaube_bnw4,
    itm_charger_german,itm_charger_german,itm_warhorse_german,itm_warhorse_german
   ],
   horse_attrib_5|level(38),wp_melee(200)|wp_firearm(320),knows_knight_3|knows_firearm_6|knows_horse_archery_8,swadian_face_face_1, swadian_face_face_2],



  

  ["italian_town_recruit","Italian Townsman","Italian Townsman",tf_guarantee_shield | tf_guarantee_armor | tf_guarantee_boots,0,0,fac_kingdom_5,
   [
    itm_boar_spear,itm_war_spear,
    itm_mace_2,
    itm_sword_medieval_c,itm_sword_medieval_c_small,
    itm_bolts,itm_hunting_crossbow,
    itm_tab_shield_pavise_a,
    itm_light_brigandine_green,itm_light_brigandine_green_mail,
    itm_bascinet,itm_narf_hose],
   foot_attrib_1|level(6),wp(70),knows_precise_shot_2|knows_militia,italian_face_1, italian_face_2],

  ["italian_town_militia","Italian Town Militia","Italian Town Militia",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_5,
   [itm_ashwood_pike,itm_sword_medieval_c_small,
    #itm_war_darts,
    itm_tab_shield_pavise_b,itm_mace_redhandle,
    itm_bascinet_coif,itm_bascinet,
    itm_brigandine_green,itm_corrazina_green,
    itm_splinted_greaves,itm_splinted_leather_greaves,itm_leather_gloves],
   foot_attrib_2|level(12),wp_melee(100),knows_swordman_2,italian_face_1, italian_face_2],

  ["italian_town_footman_1","Italian Infantry","Italian Infantry",
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_5,
   [
    #itm_bec_de_corbin_a,itm_polehammer_threeprong,
    itm_tab_shield_pavise_c,
    itm_morningstar,itm_mace_knobbedlong,
    itm_barbutte_coif,itm_barbutte,
    itm_brigandine_plate_green,itm_half_plates_green,
    itm_iron_greaves2,itm_milanese_gauntlets],
   foot_attrib_3|level(24),wp_melee(150),knows_physique_3|knows_shield_7|knows_power_strike_6|knows_ironflesh_9|knows_reserved_18_10|knows_weapon_master_2|knows_magic_defence_7,italian_face_1, italian_face_2],
      
  ["italian_town_footman_2","Italian Heavy Infantry","Italian Heavy Infantry",
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_5,
   [
    #itm_swiss_halberd,itm_long_glaive,
    itm_bec_de_corbin_a,itm_polehammer_threeprong,
    itm_tab_shield_pavise_c,
    itm_empire_warhammer,itm_empire_warhammer,
    itm_visored_bascinet_1,itm_visored_bascinet_2,itm_open_sallet_coif,
    itm_half_plates_green,itm_brigandine_plate_green,
    itm_iron_greaves2,itm_milanese_gauntlets],
   horse_attrib_4|level(36),wp_melee(200),knows_physique_4|knows_shield_8|knows_power_strike_8|knows_ironflesh_11|knows_reserved_18_10|knows_weapon_master_3|knows_magic_defence_10,italian_face_1, italian_face_2],
         
         
  ["italian_town_footman_3","Italian Armor Infantry","Italian Armor Infantry",
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_5,
   [
    itm_ebony_long_mace,itm_ebony_poleaxe,
    itm_ebony_long_mace,itm_ebony_poleaxe,
    itm_tab_shield_pavise_d,
    itm_milanese_plate,itm_milanese_plate,
    itm_milanese_sallet,itm_milanese_sallet,
    itm_iron_greaves2,itm_hourglass_gauntlets],
   horse_attrib_6|level(45),wp_melee(300),knows_physique_5|knows_shield_10|knows_power_strike_12|knows_ironflesh_15|knows_reserved_18_10|knows_weapon_master_6|knows_magic_defence_10,italian_face_1, italian_face_2],
          
  ["italian_horse_1","Italian Militia Cavalary","Italian Militia Cavalary",
   tf_mounted|tf_guarantee_all_lancer,0,0,fac_kingdom_5,
   [
    itm_lance,   
    itm_sword_medieval_c,
    itm_tab_shield_kite_b,
    itm_courser,itm_hunter,
    itm_mail_boots,
    itm_breastplate_green,itm_breastplate_green,
    itm_barbutte,itm_bascinet,itm_guard_helmet,
    itm_leather_gloves    
    ],
   horse_attrib_1|level(14),wp_melee(80)|wp_polearm(100),knows_riding_3|knows_swordman_2,italian_face_1, italian_face_2],
      
  ["italian_horse_2","Italian Cavalary","Italian Cavalary",
   tf_mounted|tf_guarantee_all_lancer,0,0,fac_kingdom_5,
   [
   itm_great_lance,itm_heavy_lance,
   itm_sword_medieval_c,itm_tab_shield_heater_d,
   itm_half_plates_green,itm_iron_greaves2,
   itm_barbutte,itm_bascinet_coif,itm_barbutte_coif,
   itm_milanese_gauntlets,itm_hunter,itm_courser,itm_barded_horse_green],
   horse_attrib_2|level(22),wp_melee(100)|wp_polearm(133),knows_riding_4|knows_swordman_4,italian_face_1, italian_face_2],
   
  ["italian_horse_3","Italian Man at Arms","Italian Men at Arms",
   tf_mounted|tf_guarantee_all_lancer,0,0,fac_kingdom_5,
   [
    itm_gothic_lance,itm_great_lance,
    itm_tab_shield_heater_cav_a,itm_sword_medieval_c,itm_mace_knobbedlong,
    itm_heraldic_harness,itm_heraldic_harness,itm_iron_greaves2,
    itm_visored_bascinet_2,itm_visored_bascinet_1,
    itm_milanese_gauntlets,itm_hourglass_gauntlets_ornate,itm_trophy_a,
    itm_charger_old,itm_charger_old],
   horse_attrib_4|level(30),wp_melee(180)|wp_polearm(250),knows_riding_5|knows_swordman_6,italian_face_1, italian_face_2],
   
  ["italian_horse_4","Italian Broken Lance","Italian Broken Lances",
   tf_mounted|tf_guarantee_all_lancer,0,0,fac_kingdom_5,
   [
    itm_gothic_lance,itm_great_lance,
    itm_toumingdun,itm_morningstar,itm_great_mace,
    itm_milanese_plate,itm_iron_greaves2,
    itm_visored_bascinet_2,itm_milanese_sallet,itm_trophy_b,
    itm_milanese_gauntlets,itm_hourglass_gauntlets_ornate,
    itm_charger_noble],
   horse_attrib_5|level(38),wp_melee(240)|wp_polearm(350),knows_riding_6|knows_swordman_8,italian_face_1, italian_face_2],
   
  ["italian_crossbow_1","Italian Crossbow Militia","Italian Crossbow Militia",
  tf_guarantee_all_wo_horse,0,0,fac_kingdom_5,
   [
    itm_sword_medieval_c,itm_fighting_pick,
    itm_tab_shield_pavise_b,
    itm_heavy_crossbow,itm_bolts,itm_steel_bolts,itm_swadian_steel_bolts,
    itm_kettle_hat_mail2,itm_light_brigandine_green_mail,itm_hose_kneecops_green],
   foot_attrib_2|level(12),wp_melee (140) | wp_crossbow (180) ,knows_precise_shot_6|knows_crossbowman_2,italian_face_1, italian_face_2],
  ["italian_crossbow_2","Italian pavise Crossbowman","Italian pavise Crossbowmen",
  tf_guarantee_all_wo_horse,0,0,fac_kingdom_5,
   [
    itm_bastard_sword_b,itm_military_pick,itm_military_hammer,
    itm_tab_shield_pavise_c,
    itm_rhod_crossbow,itm_steel_bolts,
    itm_barbutte,itm_open_sallet,itm_breastplate_green,itm_corrazina_green,itm_splinted_leather_greaves],
   foot_attrib_4|level(24),wp_melee (200) | wp_crossbow (250) ,knows_precise_shot_8|knows_crossbowman_4, italian_face_1, italian_face_2],

  ["italian_crossbow_3","Italian Veteran pavise Crossbowman","Italian Veteran pavise Crossbowmen",
  tf_guarantee_all_wo_horse,0,0,fac_kingdom_5,
   [
    itm_morningstar,itm_great_mace,
    itm_tab_shield_pavise_d,
    itm_rhod_sniper_crossbow,itm_swadian_steel_bolts,itm_trophy_a,
    itm_open_sallet_coif,itm_barbutte,itm_barbutte_coif,itm_half_plates_green,itm_splinted_leather_greaves],
   horse_attrib_4|level(36),wp_melee (200) | wp_crossbow (350),knows_precise_shot_10|knows_crossbowman_7,italian_face_1, italian_face_2],

  ["italian_crossbow_4","Italian Crossbowman ","Italian Crossbowman ",
  tf_guarantee_all_wo_horse,0,0,fac_kingdom_5,
   [
    itm_morningstar,itm_great_mace,
    itm_marksman_gloves,
    itm_musket_rifle,itm_cartridges_thrust,itm_trophy_a,
    itm_open_sallet_coif,itm_barbutte,itm_barbutte_coif,itm_half_plates_green,itm_splinted_leather_greaves],
   horse_attrib_4|level(45), wp_one_handed(300)|wp_polearm(300)|wp_firearm(500),knows_precise_shot_10|knows_physique_9|knows_shield_4|knows_power_strike_9|knows_ironflesh_5|knows_weapon_master_8|knows_stealth_10|knows_magic_defence_4,italian_face_1, italian_face_2],




  ["nord_recruit","Nord Recruit","Nord Recruits",
   tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_10,
   [
    itm_axe,itm_hand_axe,itm_spear,itm_tab_shield_round_a,itm_tab_shield_round_a,
    itm_boar_spear,itm_shortened_spear,
    itm_arrows,itm_hunting_bow,
    itm_nordic_archer_helmet,itm_blue_tunic,itm_coarse_tunic,itm_hide_boots,itm_nomad_boots],
   foot_attrib_2|level(6),wp(60),knows_thrown_1,nord_face_younger_1, nord_face_old_2],
   
  ["nord_footman","Nord Footman","Nord Footmen",
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_10,
   [
    itm_one_handed_war_axe_b,
    itm_one_handed_war_axe_a,itm_spear,itm_shortened_spear,
    itm_iron_arrow,itm_hunting_bow,itm_short_bow,itm_short_bow,
    itm_tab_shield_round_b,
    itm_javelin,itm_throwing_axes,
    itm_nordic_footman_helmet,itm_nordic_veteran_archer_helmet,itm_mail_shirt,itm_byrnie,itm_leather_boots],
   foot_attrib_3|level(12),wp(80)|wp_throwing(120)|wp_archery (120),knows_thrown_2|knows_power_draw_2,nord_face_young_1, nord_face_old_2],
      
  ["nord_warrior","Nord Warrior","Nord Warriors",
   tf_guarantee_all_footman,0,0,fac_kingdom_10,
   [
    #itm_sword_viking_1,itm_sword_viking_2,
    itm_steel_arrow,itm_undead_arrow,itm_long_bow,itm_long_bow,
    itm_one_handed_war_axe_b,itm_one_handed_battle_axe_a,
    itm_tab_shield_round_c,itm_tab_shield_round_b,itm_tab_shield_round_c,
    itm_javelin,itm_throwing_axes,
    itm_long_axe_alt,itm_long_axe,
    itm_nordic_fighter_helmet,itm_byrnie_1,itm_byrnie_2,itm_mail_hauberk_1,itm_leather_boots],
   foot_attrib_4|level(19),wp(125)|wp_throwing(160)|wp_archery (160),knows_thrown_3|knows_power_draw_3,nord_face_young_1, nord_face_older_2],
   
  ["nord_valkyrie_1","Nord Sword Maiden","Nord Sword Maiden",
   tf_mounted|tf_female|tf_guarantee_all,0,0,fac_kingdom_10,
   [
    itm_valkyrie_armor_1,itm_valkyrie_armor_2,
    itm_nordhero_sword,itm_nordhero_sword_long,
    itm_tab_shield_round_c,
    itm_nord_throwing_spears,itm_nord_throwing_spears,
    itm_valkyrie_helm_1,itm_valkyrie_helm_1,
    itm_leather_gloves,itm_mail_mittens,itm_splinted_leather_greaves,
    itm_nord_hunter,itm_nord_hunter,
   ],
  horse_attrib_5|level(30),wp(300),knows_light_swordman_5|knows_power_throw_3|knows_riding_3|knows_magic_power_3,0x000000000008600a3837015ec100008400000000001c7e7c0000000000000000,0x000000000008600a3837015ec100008400000000001c7e7c0000000000000000],
  

  ["nord_valkyrie_2","Nord Valkyrie","Nord Valkerie",
   tf_mounted|tf_female|tf_guarantee_all,0,0,fac_kingdom_10,
   [
    itm_vk_axe,itm_nord_jarid,itm_nord_jarid,
    itm_valkyrie_armor_3,itm_dthehun_new_battle_armor01,itm_splinted_greaves,itm_iron_greaves,
    itm_nordhero_sword_long,itm_nordhero_greatsword,
    itm_tab_shield_round_d,
    itm_valkyrie_helm_2,itm_valkyrie_helm_2,
    itm_gauntlets,itm_mail_mittens,
    #itm_nord_warhorse,itm_nord_warhorse
   ],
  horse_attrib_6|level(40),wp(400),knows_light_swordman_6|knows_power_throw_4|knows_riding_6|knows_magic_power_6,0x000000000008600a3837015ec100008400000000001c7e7c0000000000000000,0x000000000008600a3837015ec100008400000000001c7e7c0000000000000000],
   
  ["nord_veteran","Nord Veteran","Nord Veterans",
   #tf_guarantee_all_footman,0,0,fac_kingdom_10,
   tf_guarantee_all,0,0,fac_kingdom_10,
   [
    itm_sword_viking_3,itm_one_handed_battle_axe_b,itm_one_handed_battle_axe_c,itm_spiked_mace,
    itm_tab_shield_round_e,
    itm_throwing_spears,itm_heavy_throwing_axes,
    itm_nordic_arrow,itm_nord_bow_1,itm_nordic_arrow,itm_nord_bow_2,
    itm_long_axe_b_alt,itm_long_axe_c_alt,
    itm_nordic_huscarl_helmet,
    itm_huscarl_armor,itm_mail_hauberk_2,itm_mail_hauberk_3,
    itm_splinted_leather_greaves,itm_mail_chausses,itm_leather_gloves],
   foot_attrib_5|level(24),wp_melee(160)|wp_throwing(200)|wp_archery (200),knows_twohand_4|knows_archer_3|knows_reserved_17_6,nord_face_young_1, nord_face_older_2],
   
  ["nord_valkyrie_3","Seeker of the Odin","Seekers of the Odin",
   tf_mounted|tf_female|tf_guarantee_all,0,0,fac_kingdom_10,
   [
    itm_stahlrim_plate,itm_stahlrim_plate,itm_stahlrim_foot,
    itm_frostfang,itm_vk_axe,
    itm_steel_shield,itm_steel_shield,
    itm_valkyrie_helm_3,itm_valkyrie_helm_3,
    itm_gauntlets,itm_gauntlets,
    #itm_charger_old,
   ],
  horse_attrib_8|level(50),wp(500),knows_light_swordman_8|knows_power_throw_8|knows_riding_8|knows_magic_power_4,0x000000000008600a3837015ec100008400000000001c7e7c0000000000000000,0x000000000008600a3837015ec100008400000000001c7e7c0000000000000000],

  ["nord_champion","Nord Huscarl","Nord Huscarls",
   #tf_guarantee_all_footman,0,0,fac_kingdom_10,
   tf_guarantee_all,0,0,fac_kingdom_10,
   [
    itm_nordhero_greatsword,itm_stalhrim_greatsword,
    itm_nordhero_sword,itm_stahlrim_axe,
    itm_tab_shield_round_e,
    itm_nord_javelin,itm_nord_javelin,
    itm_stahlrim_arrow,itm_nord_bow_3,itm_nord_bow_3,
    itm_nord_norman_mask,itm_nordic_warlord_helmet,
    itm_huscarl_armor_2,itm_huscarl_armor_4,itm_huscarl_armor_3,
    itm_iron_greaves,itm_mail_chausses,itm_mail_mittens],
   foot_attrib_6|level(35),wp_melee(200)|wp_throwing(240)|wp_archery (240),knows_twohand_6|knows_archer_4|knows_reserved_17_8,nord_face_middle_1, nord_face_older_2],

  ["nord_mounted_scout", "Nord mounted scout", "Nord mounted scout",
    tf_mounted|tf_guarantee_all,0,0,fac_kingdom_10,
   [itm_nord_javelin,itm_nord_javelin,
    itm_tab_shield_round_c,itm_light_lance,
    itm_sword_viking_1,itm_sword_viking_2,itm_one_handed_battle_axe_a,
    itm_nordic_footman_helmet,itm_nordic_fighter_helmet,
    itm_byrnie,itm_mail_shirt,
    itm_hunter_boots,itm_leather_boots,itm_leather_gloves,
    itm_nord_courser,itm_nord_horse],
  horse_attrib_3|level(20),wp_melee(145)|wp_throwing(190),knows_horse_shoot_5|knows_thrown_3,nord_face_young_1, nord_face_older_2],
  
  
  ["nord_mounted_scout_2", "Nord Veteran mounted scout", "Nord Veteran mounted scout",
    tf_mounted|tf_guarantee_all,0,0,fac_kingdom_10,
   [itm_nord_throwing_spears,itm_nord_throwing_spears,
    itm_sword_viking_3,itm_one_handed_battle_axe_b,itm_tab_shield_round_d,
    itm_courser,itm_nord_hunter,
    #itm_two_handed_battle_axe_2,itm_great_axe,
    itm_nord_norman_helmet,
    itm_mail_hauberk,itm_banded_armor,
    itm_mail_boots,itm_mail_chausses,itm_mail_mittens], 
   horse_attrib_4|level(26), wp(180)|wp_throwing(230), knows_horse_shoot_5|knows_thrown_4, nord_face_young_1, nord_face_older_2 ],

  ["nord_raider", "Nord Raider", "Nord Raider",
   tf_mounted|tf_guarantee_all, no_scene, reserved, fac_kingdom_10, 
  [
   itm_sword_viking_3_long,itm_one_handed_battle_axe_c,
   itm_long_axe_c_alt,itm_heavy_lance,itm_danish_greatsword,
   itm_tab_shield_kite_cav_b,itm_tab_shield_kite_d,
   itm_nord_norman_mask,
   itm_huscarl_armor,itm_huscarl_armor_3,
   itm_mail_boots,itm_mail_chausses,itm_mail_mittens,
   itm_nord_warhorse,itm_warhorse
  ],
  horse_attrib_5|level(30),wp(230),knows_riding_5|knows_billman_6,nord_face_young_1,nord_face_old_2],

  ["nord_town_recruit","NE Townsman","NE Townsman",
   tf_dwarf|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_10,
   [
    itm_dwarf_hand_axe,itm_dwarf_war_pick,
    itm_tab_shield_round_a,itm_tab_shield_round_a,itm_highlander_hat1,
    itm_ironhills_tunic_1,itm_ironhills_tunic_2,itm_dwarf_boots,itm_dwarf_boots
    ],
   horse_attrib_1|level(15),wp(100),knows_twohand_2|knows_magic_defence_3,nord_face_younger_1, nord_face_old_2],
   
  ["nord_town_militia","NE Militia","NE Militia",
   tf_dwarf|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_10,
   [#
    #
    itm_dwarf_hand_axe,itm_tab_shield_round_a,itm_tab_shield_round_b,
    itm_javelin,itm_light_throwing_axes,
    
    itm_dwarf_mail_coif,itm_dwarf_mail_coif_mask_1,itm_dwarf_light_helmet_1,
    itm_dwarf_gambeson_1,itm_dwarf_gambeson_2,itm_dwarf_padtunic_1,
    itm_dwarf_chain_boots
   ],
   horse_attrib_2|level(22),wp(150),knows_twohand_3|knows_magic_defence_4,nord_face_young_1, nord_face_old_2],

  ["nord_swordsmen","NE Swordsmen","NE Swordsmen",
   tf_dwarf|tf_guarantee_all_footman,0,0,fac_kingdom_10,
   [
    itm_dwarf_fighting_axe,
    #itm_long_axe,itm_long_axe_b,
    itm_dwarf_light_shield_1,itm_dwarf_light_shield_2,
    itm_javelin,itm_light_throwing_axes,
    itm_dwarf_padtunic_2,itm_ironhills_mail_1,itm_ironhills_mail_2,
    itm_dwarf_light_helmet_1,itm_dwarf_heavy_helmet_1,
    itm_leather_gloves,itm_erebor_heavy_greaves],
   horse_attrib_3|level(29),wp(200),knows_twohand_4|knows_thrown_1|knows_magic_defence_5,nord_face_young_1, nord_face_old_2],
                                                       
  ["nord_axeman_1","NE Axeman","NE Axeman",
   tf_dwarf|tf_guarantee_all_footman,0,0,fac_kingdom_10,
   [itm_dwarf_battle_axe,itm_dwarf_long_axe_2,itm_dwarf_long_axe_3,itm_ironhills_shield,itm_dwarf_long_axe,
    #itm_javelin,
    #itm_half_plates_blue,itm_corrazina_blue,
    itm_ironhills_mail_2,itm_ironhills_scalemail_1,itm_ironhills_scalemail_1,
    itm_nord_norman_helmet,itm_nord_norman_mask,
    itm_ironhills_heavy_greaves,itm_plate_mittens
   ],
   horse_attrib_4|level(36),wp(250),knows_swordman_6|knows_magic_defence_6,nord_face_young_1, nord_face_older_2],
      
  ["nord_axeman_2", "Nord Veteran Axeman", "Nord Veteran Axemen", 
   tf_dwarf|tf_guarantee_all_footman, 0, 0, fac_kingdom_10, 
  [itm_ironhills_shield,itm_dwarf_long_axe_3,itm_dwarf_long_axe_4,itm_dwarf_battle_axe,
   #itm_nord_jarid,
   #itm_plate_armor,itm_plate_armor_5,itm_knight_plate,
   itm_ironhills_scalemail_2,itm_ironhills_scalemail_2,itm_ironhills_guard_armor,
   itm_trophy_a,
   itm_nord_berserker_helmet,itm_nord_berserker_mask,
   itm_ironhills_guard_greaves,
   itm_plate_mittens
   ], 
   horse_attrib_6|level(41),wp(350),knows_swordman_8|knows_magic_defence_7,nord_face_middle_1, nord_face_older_2],


  ["nord_halberd_1","NE halberd","NE halberd",
   tf_dwarf|tf_guarantee_all_pikeman,0,0,fac_kingdom_10,
   [itm_poleaxe,itm_german_poleaxe_3,itm_german_poleaxe_4,itm_german_poleaxe_2,
    itm_plate_mittens,
    itm_dwarf_heavy_helmet_1,itm_dwarf_guard_helmet_1,
    itm_dwarf_runic_axe,itm_dwarf_battle_axe,
    itm_ironhills_shield,itm_ironhills_shield,
    itm_ironhills_heavy_armor,itm_ironhills_heavy_armor,
    itm_ironhills_heavy_greaves],
   horse_attrib_4|level(36),wp(250),knows_twohand_6|knows_magic_defence_6,nord_face_middle_1, nord_face_older_2],
  ["nord_halberd_2","Nord_Obtuasers","Nord_Obtuasers",
   tf_dwarf|tf_guarantee_all_pikeman,0,0,fac_kingdom_10,
   [
    itm_pike_2,itm_pike,itm_ebony_poleaxe,itm_nord_poleaxe_3,itm_nord_poleaxe_4,itm_nord_poleaxe_2,itm_nord_poleaxe_2,
    
    itm_dwarf_iron_axe,itm_dwarf_lordrunic_axe,
    itm_ironhills_shield,itm_ironhills_shield,
    itm_plate_mittens,
    itm_dwarf_guard_helmet_1,itm_dwarf_guard_helmet_1,itm_trophy_a,
    itm_ironhills_guard_armor,itm_ironhills_guard_armor,
    itm_ironhills_guard_greaves],
   horse_attrib_6|level(41),wp(300),knows_twohand_8|knows_magic_defence_7,nord_face_middle_1, nord_face_older_2],

            
  ["nord_skirmisher","NE Skirmisher","NE Skirmisher",
  tf_dwarf|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_10,
   [
      itm_dwarf_axe,itm_dwarf_hand_axe,
      itm_bolts,itm_steel_bolts,itm_sniper_crossbow,
      itm_highlander_shield1,itm_highlander_shield2,
      itm_ironhills_tunic_1,itm_ironhills_tunic_2,
      itm_dwarf_boots,itm_dwarf_boots,
   ],
   horse_attrib_1|level(20),wp(150),knows_crossbowman_3|knows_magic_defence_3,nord_face_young_1, nord_face_old_2],


  ["nord_crossbow_1","NE Crossbowman","NE Crossbowman",
  tf_dwarf|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_10,
   [
    itm_drawf_musket_1,itm_drawf_musket_2,itm_drawf_musket,
    itm_cartridges_thrust,itm_cartridges_thrust,
    itm_sword_viking_2,itm_dwarf_fighting_axe,
    itm_dwarf_padtunic_2,itm_dwarf_gambeson_1,itm_dwarf_boots,itm_dwarf_miner_helm,itm_dwarf_miner_helm],
   horse_attrib_2|level(27),wp_melee (150)| wp_firearm (200) ,knows_crossbowman_3|knows_magic_defence_3,nord_face_young_1, nord_face_old_2],
  ["nord_crossbow_2","NE Veteran Crossbowman","NE Veteran Crossbowman",
  tf_dwarf|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_10,
   [
    itm_drawf_heavy_musket_1,itm_cartridges_thrust,itm_cartridges_thrust,
    itm_dwarf_battle_axe,itm_dwarf_long_axe,
    itm_ironhills_mail_1,itm_ironhills_mail_2,itm_dwarf_padtunic_2,
    itm_dwarf_chain_boots,itm_dwarf_light_helmet_1,itm_dwarf_light_helmet_1],
   horse_attrib_3|level(34),wp_melee (180)|wp_firearm (250) ,knows_firearm_4|knows_magic_defence_4,nord_face_middle_1, nord_face_older_2],

  ["nord_gunner","NE Gunner","NE Gunners",
  tf_dwarf|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_10,
   [
    itm_dwarf_spanner,itm_dwarf_spanner,
    itm_tab_shield_round_c,
    #itm_medium_muscket_1,itm_medium_muscket_2,itm_medium_muscket_3,itm_cartridges_thrust,itm_cartridges_thrust,
    itm_drawf_musket_8barrel2,itm_cartridges_burst,itm_cartridges_cannon,
    itm_dwarf_heavy_helmet_1,
    itm_ironhills_scalemail_1,itm_ironhills_scalemail_2,itm_ironhills_scalemail_2,
    itm_dwarf_scale_boots
   ],
   horse_attrib_3|level(41),wp_melee (230)|wp_firearm (300) ,knows_firearm_6|knows_magic_defence_6,nord_face_middle_1, nord_face_older_2],

  ["polish_which_1","Polish Witch","Polish Witch",
   tf_female|tf_guarantee_all_wo_horse,0,0,fac_kingdom_8,
   [
    itm_skull_staff,
    itm_magic_shadow_bolt,
    itm_wizard_hat_2_2,itm_witch_robe_1,
    itm_leather_boots,itm_trophy_b,
   ],
   horse_attrib_7|level(45),wp_melee(300)|wp_firearm(300),knows_crossbowman_6|knows_magic_4,refugee_face1,refugee_face2],
  ["polish_which_2","Polish Hag","Polish Hag",
   tf_female|tf_guarantee_all_wo_horse,0,0,fac_kingdom_8,
   [
    itm_gold_dragon_sword,
    itm_magic_shadow_bolt,
    itm_toumingtou,
    itm_witch_robe_3,itm_witch_robe_4,itm_witch_robe_4,
    itm_imp_foot_2,itm_daemonette_claws,itm_trophy_c,
   ],
   horse_attrib_8|level(50),wp_melee(350)|wp_firearm(350),knows_crossbowman_8|knows_magic_6,refugee_face1,refugee_face2],

  ["balkan_vil_recruit","balkan Recruit","balkan Recruits",
  tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_8,
   [
    itm_wrapping_boots,itm_hunter_boots,itm_nomad_boots,
    itm_rawhide_coat,itm_leather_vest,itm_nomad_armor,
    itm_leather_cap,itm_fur_hat,itm_leather_steppe_cap_c,
    itm_hunting_bow,itm_barbed_arrows,
    itm_scythe,
    itm_scythe],
   foot_attrib_2|level(7),wp(65),knows_archer_1, east_euro_face_young_1, east_euro_face_old_2],
            
   ["balkan_footman_1","Minotaur Levies","Minotaur Levies",
   tf_ogre|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_8,
   [
     itm_fighting_axe,itm_long_axe,itm_long_axe_b,
     itm_tab_shield_kite_b,itm_javelin,
     itm_kuyak,itm_ee_mail_hauberk_1,
     itm_splinted_leather_greaves,itm_mail_chausses,itm_scale_gauntlets,
     itm_werewolf_head_1,itm_werewolf_head_1,
    ],
   horse_attrib_1|level(16),wp(150),knows_physique_4|knows_shield_1|knows_power_strike_3|knows_ironflesh_3|knows_weapon_master_1|knows_stealth_1|knows_magic_defence_1,east_euro_face_young_1,east_euro_face_old_2],
           
  ["balkan_billman_2","Minotaur Axeman","Minotaur Axeman",
   tf_ogre|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_8,
    [ 
     itm_long_axe_c,itm_long_bardiche,itm_cav_axe,itm_cav_axe,
     itm_throwing_axes,itm_throwing_axes,
     itm_tab_shield_kite_c,itm_tab_shield_kite_c,
     
     itm_rus_lamellar_a,itm_rus_scale,itm_rus_lamellar_c,
     itm_scale_gauntlets,itm_scale_gauntlets,itm_lamellar_gauntlets,
     itm_rus_splint_greaves,itm_rus_splint_greaves,
     itm_werewolf_head_2,itm_werewolf_head_2,
    ],
   horse_attrib_2|level(24),wp(220),knows_physique_6|knows_shield_2|knows_power_strike_6|knows_ironflesh_6|knows_weapon_master_2|knows_stealth_2|knows_magic_defence_3,east_euro_face_young_1, east_euro_face_old_2],
      
  ["balkan_billman_3","Minotaur Veteran Axeman","Minotaur Veteran Axeman",
   tf_ogre|tf_guarantee_all_pikeman,0,0,fac_kingdom_8,
    [
     itm_great_long_bardiche,itm_long_bardiche,itm_cav_bardiche,itm_cav_bardiche,
     itm_tab_shield_kite_d,
     itm_heavy_throwing_axes,itm_heavy_throwing_axes,

     itm_vaegir_elite_armor,itm_vaegir_elite_armor,
     itm_lamellar_gauntlets,itm_lamellar_gauntlets,
     itm_rus_splint_greaves,itm_rus_splint_greaves,
     itm_werewolf_head_3,itm_werewolf_head_3
    ],
   horse_attrib_4|level(32),wp(280),knows_physique_8|knows_shield_3|knows_power_strike_11|knows_ironflesh_9|knows_weapon_master_3|knows_stealth_3|knows_magic_defence_5,east_euro_face_young_1, east_euro_face_old_2],
      
  ["balkan_billman_4","Minotaur guard","Minotaur guard",
   tf_ogre|tf_guarantee_all_pikeman,0,0,fac_kingdom_8,
    [
     itm_ebony_poleaxe,itm_ebony_axe,itm_black_shield,
     itm_ebony_poleaxe,itm_ebony_axe,itm_black_shield,
     itm_heavy_throwing_axes,itm_heavy_throwing_axes,

     itm_nord_knight_plate,itm_nord_knight_plate,
     itm_gauntlets,itm_gauntlets,
     itm_nord_plate_boots,itm_nord_plate_boots,
     itm_werewolf_head_4,itm_werewolf_head_4
    ],
   horse_attrib_6|level(45),wp(350),knows_physique_9|knows_shield_4|knows_power_strike_14|knows_ironflesh_12|knows_weapon_master_6|knows_stealth_4|knows_magic_defence_9,east_euro_face_young_1, east_euro_face_old_2],
            
  ["werewolf_huge","Power Werewolf","PowerWerewolf",
   tf_titan|tf_guarantee_all_footman,0,0,fac_kingdom_8,
   [
    itm_hugewolfclaw_w,itm_werewolfclaw_dual_w,
    itm_demon_head,itm_demon_foot,itm_demon_hand,itm_trophy_b,itm_trophy_a,
    itm_werewolfarmor,itm_furs,itm_raw_leather,itm_sg_orange_big
   ],
   horse_attrib_8|level(50),wp(400),knows_physique_10|knows_shield_4|knows_power_strike_14|knows_ironflesh_15|knows_weapon_master_8|knows_stealth_8|knows_magic_defence_9,east_euro_face_young_1, east_euro_face_old_2],
            
  ["balkan_archer_2","balkan Archer","balkan Archers",
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_8,
   [
    itm_war_bow,itm_khergit_bow,itm_poison_arrows,itm_flame_arrows,
    itm_hunter_boots,itm_ankle_boots,itm_hide_boots,
    itm_kaftan_over_mail,itm_kaftan_over_mail,itm_kaftan,itm_ee_mail_hauberk_1,
    itm_vaegir_fur_cap,itm_vaegir_fur_helmet,itm_vaegir_spiked_helmet,
    itm_scimitar,itm_sword_khergit_2,itm_axe,itm_voulge,
   ],
   foot_attrib_4|level(21), wp_melee (140)|wp_archery (200) ,knows_billman_3|knows_archer_4, east_euro_face_young_1, east_euro_face_old_2],
  ["balkan_archer_3","balkan Marksmen","balkan Marksmen",
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_8,
    [
     itm_leather_boots,itm_leather_gloves,
     itm_war_bow,itm_khergit_long_bow,
     itm_flat_headed_arrows,itm_poison_arrows,
     itm_kuyak_2,itm_ee_mail_hauberk_2,
     itm_vaegir_noble_helmet,itm_spiked_helmet,itm_vaegir_lamellar_helmet,
     itm_scimitar_b,itm_scimitar_b,itm_bardiche,itm_long_bardiche,
    ],
   foot_attrib_6|level(31), wp_melee(180)|wp_archery (250),knows_billman_3|knows_archer_7,east_euro_face_young_1, east_euro_face_old_2],




  ["rus_cossack_1","Village cossack","Village cossack",
   tf_mounted|tf_guarantee_all_nomad,0,0,fac_kingdom_8,
   [
    itm_sword_khergit_2,itm_winged_mace,itm_scimitar,
    #itm_double_sided_lance,
    itm_nomad_bow,itm_khergit_bow,itm_nomad_bow,itm_barbed_arrows,itm_flame_arrows,
    itm_cossack_hat_a,itm_cossack_hat_b,
    itm_rus_robe,itm_rus_robe_2,itm_rus_shoes,
    
    itm_courser_steppe,itm_steppe_horse
   ],
  horse_attrib_1|level(15),wp_melee(150)|wp_firearm(170),knows_precise_shot_2|knows_horse_shoot_6|knows_light_swordman_2,vaegir_face_young_1,vaegir_face_old_2],
  
  ["rus_cossack_2","Don Cossack","Don Cossack",
   tf_mounted|tf_guarantee_all_nomad,0,0,fac_kingdom_8,
   [
    itm_sword_khergit_3,itm_scimitar_b,
    itm_flintlock_pistol_veteran_2,itm_flintlock_pistol_veteran_3,itm_cartridges,
    #itm_double_sided_lance,itm_double_sided_lance_long,
    itm_cossack_hat_c,itm_hussar_hat,
    itm_red_pikiner_uniform,itm_red_pikiner_uniform_2,
    itm_rus_cav_boots,itm_rus_shoes,

    itm_courser_steppe,itm_hunter_steppe
   ],
  horse_attrib_2|level(20),wp_melee(170)|wp_firearm(200),knows_precise_shot_4|knows_horse_shoot_7|knows_light_swordman_3,vaegir_face_young_1,vaegir_face_old_2],
  ["rus_cossack_3","Rank Cossack","Rank Cossack",
   tf_mounted|tf_guarantee_all_nomad,0,0,fac_kingdom_8,
   [
    itm_sword_khergit_4,itm_scimitar_b,
    #itm_double_sided_lance_long,itm_hussar_lance_short,
    itm_cartridges_thrust,
    itm_flintlock_pistol_veteran_2,itm_flintlock_pistol_veteran_3,

    itm_vaegir_spiked_helmet,itm_cossack_hat_c,
    
    itm_ee_mail_hauberk_1,itm_ee_mail_hauberk_2,itm_ee_armor_3,
    itm_rus_cav_boots,
    itm_hunter_steppe,itm_hunter_steppe_good
   ],
  horse_attrib_4|level(30),wp_melee(200)|wp_firearm(250),knows_precise_shot_6|knows_horse_shoot_8|knows_light_swordman_6,vaegir_face_young_1,vaegir_face_old_2],
         
  ["balkan_cav_3","balkan hussar","balkan hussars",
   tf_mounted|tf_guarantee_all_nomad,0,0,fac_kingdom_8,
   [
    itm_hussar_lance_short,itm_sword_khergit_6,itm_sword_khergit_7,
    itm_boyar_helmet,itm_reytar_helmet,
    itm_flintlock_pistol_elite_1,itm_flintlock_pistol_elite_2,itm_cartridges_thrust,
    itm_ee_armor_4,itm_ee_armor_4,
    itm_rus_splint_greaves,
    itm_hunter_steppe_good,itm_hunter_steppe_good
    ],
   horse_attrib_5|level(40),wp_melee(270)|wp_firearm(250),knows_precise_shot_8|knows_horse_shoot_10|knows_light_swordman_7,east_euro_face_young_1,east_euro_face_old_2],

  ["polish_town_recruit","Polish Townsman","Polish Townsman",
   tf_guarantee_shield | tf_guarantee_armor | tf_guarantee_boots,0,0,fac_kingdom_8,
   [
    itm_military_scythe,itm_military_scythe,
    itm_cartridges,itm_flintlock_pistol,itm_flintlock_pistol_2,    
    #itm_tab_shield_heater_a,
    itm_kaftan,itm_kaftan,itm_cossack_hat_a,itm_rus_shoes],
   foot_attrib_2|level(6),wp(60),knows_firearm_1,east_euro_face_young_1, east_euro_face_older_2],

  ["polish_crossbow_1","Polish crossbow Militia","Polish crossbow Militia",
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_8,
   [
    itm_cartridges,itm_samopal,itm_old_musket,
    itm_pike,itm_pike_2,itm_long_pike,
    itm_cossack_hat_b,itm_cossack_hat_c,
    itm_red_pikiner_uniform,itm_red_pikiner_uniform,
    itm_ankle_boots,itm_rus_shoes],
   foot_attrib_3|level(12),wp_melee(120)|wp_firearm (120),knows_precise_shot_2|knows_pikeman_2,east_euro_face_young_1, east_euro_face_older_2],

  ["polish_crossbow_2","Polish gunner","Polish gunner",
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_8,
   [
    itm_cartridges,itm_old_musket,itm_good_musket,
    itm_sword_khergit_2,
    itm_leather_gloves,itm_rus_shoes,
    itm_red_pikiner_uniform_2,
    itm_vaegir_spiked_helmet,itm_vaegir_spiked_helmet,itm_vaegir_lamellar_helmet
    ],
   foot_attrib_4|level(18),wp_melee (160) | wp_firearm (160),knows_precise_shot_3|knows_light_swordman_3,east_euro_face_young_1, east_euro_face_older_2],

  ["polish_crossbow_3_1","Polish Armor gunner","Polish Armor gunner",
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_8,
   [itm_cartridges_burst,    
    itm_mushket_udarniy,itm_eoro_musket,
    itm_bardiche,itm_great_bardiche,
    itm_leather_gloves,itm_rus_shoes,itm_splinted_leather_greaves,
    itm_red_armour_2,itm_beret_plumes_red],
   horse_attrib_3|level(24),wp_melee (190) | wp_firearm (190),knows_precise_shot_6|knows_light_swordman_5,east_euro_face_young_1, east_euro_face_older_2],
  ["polish_crossbow_3_2","Polish Musketeer","Polish Musketeer",
   tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_8,
   [itm_cartridges_burst,    
    itm_musket_noble,itm_musket_cavalry,
    itm_long_bardiche,itm_great_long_bardiche,
    itm_leather_gloves,itm_rus_shoes,itm_splinted_leather_greaves,
    itm_red_armour_3,itm_sallet_beret_plain_red],
   horse_attrib_5|level(34),wp_melee (260) | wp_firearm (260),knows_precise_shot_9|knows_light_swordman_7,east_euro_face_young_1, east_euro_face_older_2],


  ["polish_pikeman_1","Polish pikeman","Polish pikeman",
   tf_guarantee_all_pikeman,0,0,fac_kingdom_8,
   [
    itm_pike_2,itm_pike_2,
    itm_sword_khergit_2,itm_sword_khergit_3,
    itm_one_handed_battle_axe_a,itm_one_handed_battle_axe_b,
    itm_leather_gloves,itm_rus_shoes,
    itm_red_armour_2,itm_red_armour_3,
    itm_beret_plumes_red,itm_beret_plumes_red,itm_beret_plain_red
    ],
   horse_attrib_2|level(18),wp_melee (100)|wp_polearm (170),knows_pikeman_3,east_euro_face_young_1, east_euro_face_older_2],

  ["polish_pikeman_2","Polish Armor pikeman","Polish Armor pikeman",
   tf_guarantee_all_pikeman,0,0,fac_kingdom_8,
   [itm_long_pike,itm_pike_2,    
    itm_rapierd,itm_sword_khergit_4,
    itm_leather_gloves,itm_rus_cav_boots,
    itm_red_armour_4,itm_sallet_beret_plain_red],
   horse_attrib_3|level(24),wp_melee (120)|wp_polearm (250), knows_pikeman_5,east_euro_face_young_1, east_euro_face_older_2],

  ["polish_pikeman_3","Polish Armor pikeman","Polish Armor pikeman",
   tf_guarantee_all_pikeman,0,0,fac_kingdom_8,
   [itm_nord_poleaxe_3,itm_nord_poleaxe_4,    
    itm_rapierd,itm_sword_khergit_4,
    itm_leather_gloves,itm_rus_cav_boots,
    itm_boyar_helmet,itm_polish_hussar_armor,
    itm_boyar_helmet,itm_polish_hussar_armor,
    ],
   horse_attrib_5|level(35),wp_melee (260)|wp_polearm (280), knows_physique_4|knows_shield_4|knows_power_strike_9|knows_ironflesh_14|knows_reserved_18_10|knows_weapon_master_5|knows_magic_defence_7,east_euro_face_young_1, east_euro_face_older_2],



  ["polish_horse_1","polish Militia_Cavalary","polish Militia_Cavalary",
   tf_mounted|tf_guarantee_all_nomad,0,0,fac_kingdom_8,
   [
    itm_cartridges_burst,
    itm_flintlock_pistol_veteran,itm_flintlock_pistol,itm_flintlock_pistol_2,
    itm_sword_khergit_1,
    itm_lance,itm_heavy_lance,
    itm_tab_shield_kite_a,itm_tab_shield_kite_b,
    itm_courser_steppe,
    itm_rus_cav_boots,
    #itm_red_pikiner_uniform,
    itm_poland_dragoon_coat,itm_breastplate_polish,
    itm_cossack_hat_b,itm_cossack_hat_c,
    itm_leather_gloves    
    ],
   horse_attrib_1|level(14),wp_melee (150)|wp_firearm (150) ,knows_horse_shoot_4|knows_crossbowman_2,east_euro_face_young_1, east_euro_face_older_2],
   
  ["polish_horse_2","polish Horse_Strelets","polish Horse_Strelets",
   tf_mounted|tf_guarantee_all_nomad,0,0,fac_kingdom_8,
   [
    itm_hussar_lance_short,
    itm_flintlock_pistol_veteran_2,itm_flintlock_pistol_veteran_3,
    itm_sword_khergit_4,itm_sword_khergit_2,
    itm_one_handed_battle_axe_b,itm_cav_bardiche,itm_sword_khergit_4,
    itm_ee_armor_3,itm_ee_armor_4,
    itm_rus_cav_boots,itm_rus_splint_greaves,
    itm_boyar_helmet,itm_reytar_helmet,
    itm_tab_shield_kite_c,itm_tab_shield_kite_cav_a,
    itm_hunter_steppe],
   horse_attrib_2|level(25),wp_melee(180)|wp_firearm (200),knows_horse_shoot_7|knows_shield_4|knows_power_strike_8|knows_ironflesh_8|knows_reserved_18_10|knows_weapon_master_4|knows_magic_defence_4,east_euro_face_young_1, east_euro_face_older_2],
            
                        
  ["polish_horse_3","polish hussar","polish hussars",
   tf_mounted|tf_guarantee_all_lancer,0,0,fac_kingdom_8,
   [itm_sword_khergit_3,itm_sword_khergit_4, 
    itm_hussar_lance,
    itm_boyar_helmet,itm_boyar_helmet,
    itm_polish_husar_helmet,
    itm_polish_hussar_armor,
    itm_polish_hussar_armor_wing,
    itm_rus_splint_greaves,
    itm_shield_otto_wing,
    itm_hunter_steppe_good
    ],
   horse_attrib_4|level(35),wp_melee(230),knows_riding_10|knows_physique_7|knows_shield_9|knows_power_strike_11|knows_ironflesh_10|knows_reserved_18_10|knows_weapon_master_4|knows_magic_defence_8,east_euro_face_young_1,east_euro_face_older_2],


  ["polish_horse_4","polish Gryphon Legionnaire","polish Gryphon Legionnaire", 
  tf_mounted|tf_guarantee_all_lancer,0,0,fac_kingdom_8,
   [itm_sword_khergit_6,
    itm_hussar_lance_2,itm_hussar_lance, 
    itm_polish_husar_helmet,
    itm_polish_hussar_armor,
    itm_polish_hussar_armor_wing,
    itm_rus_splint_greaves,
    itm_shield_otto_wing,
    itm_griffin_wild
    ],
   horse_attrib_6|level(45),wp_melee(300),knows_riding_10|knows_physique_8|knows_shield_10|knows_power_strike_13|knows_ironflesh_12|knows_reserved_18_10|knows_weapon_master_6|knows_magic_defence_10,east_euro_face_young_1,east_euro_face_older_2],
         



 ["janissary_retainer","janissary retainer","janissary retainer",
  tf_demon_human|tf_guarantee_all_footman,0,0,fac_kingdom_9,
   [
    itm_jarid,itm_jarid,
    itm_chaos_sword1,itm_sarranid_mace_1,
    itm_tab_shield_kite_b,itm_tab_shield_kite_c,
    itm_rhun_armor_4,itm_rhun_armor_6,itm_rhun_armor_5,
    itm_sarranid_boots_d,itm_sarranid_boots_c,
    itm_rhun_helm_3,itm_rhun_helm_2
   ],
   horse_attrib_2|level(20),wp(150),knows_swordman_4|knows_reserved_17_4,euro_face_3, euro_face_4],
      
  ["chaos_warrior_1","Chaos Warrior","Chaos Warriors",
    tf_demon_human|tf_guarantee_all_footman,0,0,fac_kingdom_9,
   [
    itm_chaos_sword2,itm_sarranid_axe_a,itm_sarranid_mace_1,
    itm_chaos_throw1,itm_chaos_throw1,
    itm_chaos_warrior_shield,
    itm_rhun_armor_6_3,itm_rhun_armor_6_1,
    itm_chaos_gauntlets_1,
    itm_chaos_leg_1,itm_chaos_leg_1,
    itm_rhun_helm_7_2,itm_rhun_helm_7
   ],
   horse_attrib_4|level(30),wp(200),knows_swordman_5|knows_reserved_17_6,euro_face_3,euro_face_4],
  ["chaos_warrior_2","Elite Chaos Warrior","Elite Chaos Warriors",
    tf_demon_human|tf_guarantee_all_footman,0,0,fac_kingdom_9,
   [
    itm_chaos_sword4,itm_sarranid_axe_b,itm_sarranid_mace_2,
    itm_chaos_throw2,itm_chaos_throw2,
    itm_chaos_knight_shield,
    itm_rhun_armor_7,itm_rhun_armor_7,
    itm_chaos_gauntlets,
    itm_chaos_leg_2,itm_chaos_leg_2,
    itm_rhun_helm_8,itm_rhun_helm_9
   ],
   horse_attrib_6|level(40),wp(300),knows_swordman_7|knows_reserved_17_6,euro_face_3,euro_face_4],
   
 ["mamluke_recruit","mamluke Infantry","mamluke Veteran Infantries",
  tf_demon_human|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_9,
   [
    itm_chaos_sword1,itm_arabian_sword_a,itm_mace_3,
    itm_jarid,itm_jarid,itm_nomad_bow,itm_bamboo_arrows,itm_flat_headed_arrows,
    itm_tab_shield_small_round_b,itm_shield_otto1,
    itm_sarranid_mail_coif,itm_sarranid_helmet1,
    itm_arabian_armor_b,
    itm_sarranid_boots_c],
   foot_attrib_3|level(15),wp_melee (85)|wp_throwing (100),knows_thrown_2,arab_face_1, arab_face_2],
   
 ["mamluke_horseman","mamluke Horseman","mamluke Horsemen",
   tf_demon_human|tf_mounted|tf_guarantee_all_lancer,0,0,fac_kingdom_9,
   [itm_lance,
    itm_chaos_sword1,
    itm_tab_shield_small_round_b,
    itm_mamluke_mail,itm_turk_armor,
    itm_sarranid_boots_c,itm_sarranid_boots_b, 
    itm_sarranid_veiled_helmet,itm_sarranid_veiled_helmet2,itm_leather_gloves,itm_lamellar_warhorse,itm_lamellar_warhorse],
   horse_attrib_2|level(25),wp_melee(150),knows_knight_east_3|knows_thrown_3|knows_horse_archery_4,arab_face_1, arab_face_2],
   
   
 ["mamluke_horseman_2","mamluke Mamluke","mamluke Mamlukes",
  tf_demon_human|tf_mounted|tf_guarantee_all_lancer,0,0,fac_kingdom_9,
   [itm_chaos_lance_1,
    itm_sarranid_mace_1,
    itm_chaos_sword2,itm_chaos_sword3,
    itm_dec_steel_shield,
    itm_turk_mail_heavy,itm_turk_armor,
    itm_sarranid_boots_d,itm_sarranid_boots_c,
    itm_chichak1,itm_chichak2,
    itm_lamellar_charger,itm_warhorse_sarranid,
    itm_scale_gauntlets,itm_mail_mittens],
   horse_attrib_4|level(30),wp_melee(200) ,knows_knight_east_4|knows_twohand_5,arab_face_1, arab_face_2],

  ["mamluke_horseman_3", "mamluke Mamluke", "mamluke Mamlukes", 
   tf_demon_human|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse, 0, 0, fac_kingdom_9, 
  [
   itm_chaos_lance_2,
   itm_chaos_sword3,itm_sarranid_mace_2,
   itm_chaos_warrior_shield,itm_chaos_warrior_shield,
   itm_rhun_armor_6_2,
   itm_chaos_leg_1,itm_rhun_helm_7,itm_chaos_gauntlets_1,itm_nightmare,itm_sg_human_small
  ],
  horse_attrib_5|level(40), wp_melee(300), knows_knight_east_5|knows_twohand_7, arab_face_1, arab_face_2 ],

 ["janissary_archer", "janissary Archer", "janissary Archers",
  tf_demon_human|tf_guarantee_ranged|tf_guarantee_all_footman,0,0,fac_kingdom_9,
   [itm_flame_arrows,itm_khergit_bow,
    itm_flat_headed_arrows,itm_khergit_bow,

    itm_arabian_sword_a,itm_arabian_sword_b,
    itm_mace_3,itm_mace_4,itm_shield_otto1,
    itm_janissary_helmet_3,
    itm_sarranid_boots_b,itm_janissary_vest],
   horse_attrib_2|level(20),wp_melee (150)|wp_archery (150),knows_archer_4,euro_face_3, euro_face_4],

    
 ["janissary_infantry_1", "janissary Infantry","janissary Infantry",
  tf_demon_human|tf_guarantee_all_pikeman,0,0,fac_kingdom_9,
  [
   itm_chaos_sword2,itm_chaos_warrior_shield,
   itm_sarranid_two_handed_axe_a,itm_sarranid_two_handed_mace_1,
   
  itm_rhun_armor_6_1,itm_rhun_armor_6_1,
  itm_chaos_gauntlets_1,itm_chaos_leg_1,
  itm_rhun_helm_7,itm_rhun_helm_7
  ],
  horse_attrib_5|level(30),wp_melee(200),knows_twohand_6,euro_face_3, euro_face_4],
   
 ["janissary_infantry_2","janissary Infantry","janissary Infantry",
  tf_demon_human|tf_guarantee_all_pikeman,0,0,fac_kingdom_9,
   [
    itm_sarranid_two_handed_axe_b,itm_sarranid_double_axe,
    itm_sarranid_two_handed_mace_2,
    itm_chaos_sword3,itm_chaos_warrior_shield,
    itm_rhun_armor_8,itm_rhun_armor_8,
    itm_rhun_helm_8,itm_imp_head_4,itm_imp_head_4,
    itm_imp_foot_2,itm_chaos_leg_2,itm_imp_hand_3],
   horse_attrib_7|level(40),wp_melee (290),knows_twohand_8,euro_face_3, euro_face_4],
   
 ["janissary_musketeer_1","janissary Musketeers","janissary Musketeers",
  tf_demon_human|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_9,
   [itm_cartridges_burst,
    itm_turk_musket,itm_turk_musket_koleso,itm_turk_musket,
    itm_shield_otto2,
    itm_sarranid_cavalry_sword,itm_sword_khergit_4,
    itm_sarranid_mail_shirt,itm_sarranid_boots_c,itm_sarranid_boots_b,itm_janissary_helmet_4],
   horse_attrib_4|level(30),wp_melee(150)|wp_firearm(250),knows_firearm_6,euro_face_3, euro_face_4],
  ["janissary_musketeer_2", "janissary Musketeers", "janissary Musketeers", 
  tf_demon_human|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_9,
   [itm_cartridges_burst,itm_cartridges_thrust,
    itm_turk_musket_good,itm_turk_musket_good,
    itm_arabian_sword_d,itm_sword_khergit_5,
    itm_shield_otto2,
    itm_sarranid_boots_d,itm_sarranid_boots_b,itm_sarranid_mail_shirt,itm_janissary_helmet_5,itm_leather_gloves], 
   horse_attrib_6|level(40), wp_melee(200)|wp_firearm(350), knows_firearm_8, euro_face_3, euro_face_4 ],


["khergit_hunter","Khergit hunter","Khergit hunter",
  tf_guarantee_all_footman|tf_guarantee_ranged,0,0,fac_kingdom_3,
  [
   itm_khergit_arrows,itm_hunting_bow,itm_nomad_bow,
   itm_sword_khergit_2,itm_spear,
   itm_rhun_helm_k,
   itm_rhun_armor_a,itm_rhun_shoes
   ],
  foot_attrib_3|level(11),wp_melee(150)|wp_archery(200),knows_nomad_3,khergit_face_younger_1,khergit_face_old_2],

 ["khergit_foot_archer","Khergit Foot archers","Khergit Foot archers",
 tf_guarantee_all_footman|tf_guarantee_ranged,0,0,fac_kingdom_3,
  [itm_khergit_arrows,itm_nomad_bow,
  itm_sword_khergit_3,itm_winged_mace,
  itm_rhun_helm_m,itm_rhun_helm_m,itm_rhun_armor_j,itm_rhun_shoes,
  ],
  horse_attrib_1|level(16),wp_melee(200)|wp_archery(120)|wp_throwing(220),knows_archer_4,khergit_face_younger_1,khergit_face_old_2],
    
 ["khergit_footman","Khergit footman","Khergit footman",
 tf_guarantee_all_footman|tf_guarantee_ranged,0,0,fac_kingdom_3,
  [   itm_javelin,itm_javelin,itm_javelin,

  itm_sword_khergit_3,itm_winged_mace,
  itm_rhun_infantry_shield,itm_rhun_helm_m,itm_rhun_armor_j,itm_rhun_shoes,
  ],
  horse_attrib_1|level(16),wp_melee(200)|wp_throwing(250),knows_thrown_4|knows_swordman_4,khergit_face_younger_1,khergit_face_old_2],
    
 ["khergit_dismounted_lancer","Khergit Dismounted Lancer","Khergit Dismounted Lancer",
  tf_guarantee_all_footman,0,0,fac_kingdom_3,
  [
   itm_sword_khergit_7,itm_ebony_scimitar_2,itm_khergit_sword_two_handed_b,
   
   itm_rhun_dragon_shield,itm_rhun_dragon_shield,
   itm_javelin,itm_javelin,itm_javelin,
   itm_rhun_helm_a,itm_rhun_helm_a,itm_rhun_armor_h,itm_rhun_armor_h,itm_rhun_greaves,itm_lamellar_gauntlets
  ],
 horse_attrib_4|level(28),wp_melee(250)|wp_throwing(250),knows_thrown_6|knows_swordman_6,khergit_face_middle_1,khergit_face_older_2],
    
 ["khergit_heavy_infantry","Khergit_heavy_infantry","Khergit_heavy_infantry", 
  tf_guarantee_all_footman,0,0,fac_kingdom_3,
  [
   itm_sword_khergit_7,itm_ebony_scimitar_2,itm_khergit_sword_two_handed_b,
   
   itm_rhun_dragon_shield,itm_rhun_dragon_shield,
   itm_javelin,itm_javelin,itm_javelin,
   itm_rhun_helm_b,itm_rhun_helm_b,itm_rhun_armor_h,itm_rhun_armor_h,itm_rhun_greaves,itm_lamellar_gauntlets
  ],
 horse_attrib_4|level(36),wp_melee(300)|wp_throwing(350),knows_thrown_8|knows_swordman_8,khergit_face_middle_1,khergit_face_older_2],
    
 ["khergit_heavy_archer","Khergit heavy archer","Khergit heavy Archers",
 tf_guarantee_all_footman|tf_guarantee_ranged,0,0,fac_kingdom_3,
  [
   itm_sword_khergit_6,
   itm_orcish_mutil_arrow,itm_poison_arrows,itm_khergit_bow,
   itm_rhun_helm_c,itm_rhun_helm_c,
   itm_rhun_armor_g,itm_rhun_boots_balchoth
  ],
  horse_attrib_2|level(28),wp_melee(220)|wp_archery (240),knows_magic_power_5|knows_archer_5,khergit_face_middle_1,khergit_face_older_2],

 ["khergit_dis_guard","Khergit_dismounted_Guard","Khergit_dismounted_Guards", 
 tf_guarantee_all_footman|tf_guarantee_ranged,0,0,fac_kingdom_3,
  [
   itm_sword_khergit_6,
   itm_flame_arrows,itm_elven_arrows_fire,itm_khergit_long_bow,
   itm_rhun_helm_c,itm_rhun_helm_c,
   itm_rhun_armor_g,itm_rhun_boots_balchoth
  ],
  horse_attrib_2|level(36),wp_melee(260)|wp_archery (280),knows_magic_power_3|knows_archer_7,khergit_face_middle_1,khergit_face_older_2],

["khergit_tribesman","Khergit Tribesman","Khergit Tribesmen",
  tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_3,
  [
   #itm_khergit_arrows,itm_hunting_bow,
   itm_club,itm_spear,
   itm_steppe_cap,itm_nomad_cap_b,
   itm_rhun_cloth,itm_nomad_boots,itm_rhun_shoes
   ],
  foot_attrib_3|level(5),wp(100),knows_nomad_1,khergit_face_younger_1,khergit_face_old_2],

["khergit_skirmisher","Khergit nomad","Khergit nomad",
 tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_3,
 [ itm_khergit_arrows,itm_light_lance,itm_nomad_bow,
   itm_sword_khergit_1,itm_tab_shield_small_round_a,
   itm_rhun_helm_k,itm_rhun_armor_a,itm_rhun_shoes,
   itm_rhun_helm_k,itm_rhun_armor_a,itm_rhun_shoes,
   itm_steppe_horse,itm_saddle_horse_steppe
 ],
 horse_attrib_2|level(11),wp_melee(150)|wp_archery (180),knows_nomad_2|knows_riding_4|knows_horse_archery_10,khergit_face_younger_1,khergit_face_old_2],

["khergit_horseman","Khergit Horseman","Khergit Horsemen",
 tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_kingdom_3,
  [
    itm_light_lance,itm_sword_khergit_3,itm_tab_shield_small_round_b,
    itm_barbed_arrows,itm_light_lance,itm_nomad_bow,
    itm_rhun_helm_l,itm_rhun_armor_j,itm_rhun_shoes,
    itm_hunter_steppe,itm_steppe_horse
    ],
  horse_attrib_3|level(16),wp_melee(180)|wp_archery (200),knows_nomad_3|knows_riding_5|knows_horse_archery_10,khergit_face_young_1,khergit_face_older_2],


   ["khergit_horse_archer","Khergit nomad_horseman","Khergit nomad_horseman",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_kingdom_3,
   [
    itm_sword_khergit_2,itm_winged_mace,
    itm_nomad_bow,itm_barbed_arrows,itm_khergit_arrows,
    itm_tab_shield_small_round_a,itm_tab_shield_small_round_a,itm_tab_shield_small_round_b,
    itm_khergit_helmet,itm_khergit_helmet,itm_black_nomad_robe,itm_black_nomad_robe,itm_khergit_leather_boots,itm_steppe_horse
   ],
  horse_attrib_3|level(16),wp_melee(180)|wp_archery (200),knows_nomad_3|knows_riding_5|knows_horse_archery_10,khergit_face_young_1,khergit_face_older_2],

  ["khergit_lancer","Khergit Lancer","Khergit Lancers",tf_mounted|tf_guarantee_all_lancer,0,0,fac_kingdom_3,
   [
    itm_sword_khergit_4,itm_spiked_mace,itm_sword_khergit_5,itm_sipah_lance,
    itm_rhun_dragon_cavalry_shield,itm_javelin,
    itm_rhun_helm_i,itm_rhun_armor_p,itm_rhun_greaves,itm_leather_gloves,
    itm_rhun_helm_i,itm_rhun_armor_p,itm_rhun_greaves,itm_leather_gloves,
    itm_warhorse_steppe,itm_warhorse_steppe
   ],
   horse_attrib_4|level(28),wp_melee(250)|wp_throwing(300),knows_riding_7|knows_nomad_5|knows_horse_archery_10,khergit_face_middle_1,khergit_face_older_2],
   
  ["khergit_heavy","Khergit Heavy Lancer","Khergit Heavy Lancers",tf_mounted|tf_guarantee_all_lancer,0,0,fac_kingdom_3,
   [itm_mace_woodenhandle,itm_sword_khergit_7,itm_khergit_lance,itm_sword_khergit_5,        
    itm_rhun_dragon_cavalry_shield,itm_javelin,
    itm_rhun_helm_i,itm_rhun_armor_k,itm_rhun_greaves,itm_leather_gloves,
    itm_rhun_helm_i,itm_rhun_armor_k,itm_rhun_greaves,itm_leather_gloves,
    itm_khergit_war_horse,itm_khergit_war_horse],
   horse_attrib_6|level(36),wp_melee(300)|wp_throwing(300),knows_riding_7|knows_nomad_7|knows_horse_archery_10,khergit_face_middle_1,khergit_face_older_2],

  ["khergit_veteran_horse_archer","Khergit Veteran Horse Archer","Khergit Veteran Horse Archers",tf_guarantee_all,0,0,fac_kingdom_3,
    [itm_sword_khergit_4,itm_sword_khergit_3,itm_winged_mace,
     itm_khergit_bow,itm_khergit_bow,itm_khergit_arrows,itm_flame_arrows,
     itm_tab_shield_small_round_c,itm_tab_shield_small_round_c,
     itm_rhun_helm_e,itm_rhun_armor_o,itm_rhun_armor_o,itm_rhun_boots_balchoth,itm_leather_gloves,
     itm_huntera1,itm_huntera1
    ],
   horse_attrib_3|level(28),wp_melee(220)|wp_archery (240),knows_riding_7|knows_nomad_4|knows_horse_archery_10,khergit_face_middle_1,khergit_face_older_2],
  ["khergit_elite_horse_archer","Khergit Elite Horse Archer","Khergit Elite Horse Archers",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_6,itm_winged_mace,
   itm_khergit_bow,itm_poison_arrows,itm_flame_arrows,
    itm_tab_shield_small_round_b,itm_tab_shield_small_round_b,
    itm_rhun_helm_e,itm_rhun_armor_o,itm_rhun_armor_o,itm_rhun_boots_balchoth,itm_leather_gloves,
    itm_huntera2],
   horse_attrib_5|level(36),wp_melee(250)| wp_archery (280),knows_riding_8|knows_nomad_6|knows_horse_archery_10,khergit_face_middle_1,khergit_face_older_2],

  ["france_knight_1","France Squire","France Squire",
   tf_mounted|tf_guarantee_all_lancer,0,0,fac_kingdom_1,
   [
    itm_gondor_tower_spear,
    itm_one_handed_battle_axe_b,itm_one_handed_battle_axe_a,itm_bastard_sword_a,itm_longsword,
    itm_gondor_shield_b,
    itm_teu_surcoat_over_mail_1,itm_teu_surcoat_over_mail_1,
    itm_iron_greaves2,itm_wisby_gauntlets_black,
    itm_lorien_helm_d,itm_gondor_knight_helm,
    itm_courser,itm_hunter,itm_hunter
   ],
  horse_attrib_2|level(20),wp_melee(200),knows_knight_order_1|knows_swordman_2,west_euro_face_1,west_euro_face_2],
   
   
  ["france_knight_2","France Knight","France Knight",
   tf_mounted|tf_guarantee_all_lancer,0,0,fac_kingdom_1,
   [itm_gondor_lance,itm_gondor_lance,
    itm_longsword,itm_gondor_ranger_sword,
    itm_poleaxe,itm_bec_de_corbin_a,
    itm_gondor_shield_b,itm_gondor_shield_d,
    itm_gon_knight,itm_gon_knight,itm_iron_greaves2,itm_wisby_gauntlets_black,itm_wisby_gauntlets_black,
    itm_gondor_guard_helm,itm_lorien_helm_e,
    itm_warhorse_france,itm_warhorse_france,
   ],
 horse_attrib_3|level(27),wp_melee(250),knows_knight_order_2|knows_swordman_4,west_euro_face_1,west_euro_face_2],
 
  ["france_knight_3","France Noble Knight","France Noble Knight", 
   tf_mounted|tf_guarantee_all_lancer,0,0,fac_kingdom_1,
   [
    itm_gothic_lance,itm_great_lance_dark,
    itm_gondor_ranger_sword,itm_gondor_citadel_sword,
    itm_gondor_shield_d,
    itm_poleaxe,itm_bec_de_corbin_a,
    itm_plate_armor_3,itm_plate_armor_3,
    itm_iron_greaves2,itm_sg_human_small,itm_trophy_a,
    itm_french_helm_3,itm_french_helm_3,
    itm_charger_france,itm_charger_france,
    itm_gondor_gauntlets,itm_gondor_gauntlets
   ],
   horse_attrib_4|level(35),wp_melee(300),knows_knight_order_4|knows_swordman_6,west_euro_face_1,west_euro_face_2],

  ["france_knight_4","France Lancer","France Lancers", 
   tf_mounted|tf_guarantee_all_lancer,0,0,fac_kingdom_1,
   [
    itm_great_lance2,itm_great_lance2,
    itm_gondor_citadel_sword,itm_amroth_sword_b,
    itm_crusader_sword_2,
    itm_gondor_shield_e,itm_sg_human_small,itm_trophy_b,
    itm_gondor_lord_armor,
    itm_iron_greaves2,itm_iron_greaves2,
    itm_winged_great_helmet_blue,itm_winged_great_helmet_blue,
    itm_charger_france_2,itm_charger_france_2,
    itm_gondor_gauntlets,itm_gondor_gauntlets,itm_sg_human_small
   ],
  horse_attrib_7|level(45),wp_melee(350),knows_riding_7|knows_weapon_master_7|knows_magic_defence_9|knows_physique_5|knows_shield_10|knows_power_strike_9|knows_ironflesh_15|knows_reserved_18_10,west_euro_face_1,west_euro_face_2],




  ["hospitaller_knight", "Sun Crusader Knight", "Sun Crusader Knights", 
  tf_mounted|tf_guarantee_all_lancer, 0, 0,  fac_hospitalier_knights, 
   [
    itm_great_lance_dark,itm_great_lance_dark,itm_bastard_sword_c,
   itm_shield_heater_c,itm_dawnbreaker_armor,itm_amade_bronze_greaves,itm_amade_bronze_gauntlets,itm_black_helmet_2,itm_armor_demi_griffin,
   itm_shield_heater_c,itm_dawnbreaker_armor,itm_amade_bronze_greaves,itm_amade_bronze_gauntlets,itm_black_helmet_2,itm_armor_demi_griffin,
   itm_sg_human_big,itm_sg_yellow_small
   ], 
   horse_attrib_9|level(45), wp(450), knows_knight_order_4|knows_twohand_8, west_euro_face_1, west_euro_face_2 ],
   
      
  ["hospitaller_knight_2", "Dark Crusader Knight", "Dark Crusader Knights", 
   tf_mounted|tf_guarantee_all_lancer, 0, 0, fac_hospitalier_knights, 
   [
    itm_great_lance2,itm_great_lance2,itm_morrigan,itm_morrigan,
    itm_shield_heater_c,itm_black_armor2,itm_black_greaves2,itm_black_helmet2,itm_hourglass_gauntlets_ornate,itm_armor_demi_griffin,
    itm_shield_heater_c,itm_black_armor2,itm_black_greaves2,itm_black_helmet2,itm_hourglass_gauntlets_ornate,itm_armor_demi_griffin,itm_sg_human_big
   ], 
   horse_attrib_9|level(45), wp(450), knows_knight_order_4|knows_twohand_8|knows_magic_defence_10, west_euro_face_1, west_euro_face_2 ],

  ["england_knight_1","England Squire","England Squire",
   tf_mounted|tf_guarantee_all_lancer,0,0,fac_kingdom_4,
  [itm_heavy_lance,
    itm_tab_shield_heater_cav_a,itm_sword_claymore_01,
    itm_glass_mace,itm_bastard_sword_e,
    itm_early_transitional_e1,itm_knight_armor3,itm_half_plates_red,
    itm_early_transitional_f1,itm_knight_armor2,itm_half_plates_red,
    itm_iron_greaves2,itm_wisby_gauntlets_black,
    itm_great_helmet,itm_knight_helmet1,
    itm_barded_horse_red,itm_barded_horse_red],
  str_35|agi_16|int_6|cha_9|level(25),wp_melee(180),knows_knight_1|knows_twohand_4|knows_magic_defence_3,euro_face_1,euro_face_2],

  ["england_knight_2","England Norman Knight","England Norman Knight",
   tf_mounted|tf_guarantee_all_lancer,0,0,fac_kingdom_4,
   [itm_glass_mace_2,itm_warblade_greensilver,itm_great_lance,
    itm_sword_claymore_02,itm_poleaxe,
    itm_tab_shield_kite_cav_b,itm_tab_shield_kite_cav_b,
    itm_winged_great_helmet,itm_knight_helmet2,itm_knight_helmet3,
    itm_plate_armor_2,itm_knight_plate_2,itm_plate_armor_2,
    itm_iron_greaves2,itm_wisby_gauntlets_black,
    itm_warhorse_england,itm_warhorse_england_2],
   str_60|agi_18|int_12|cha_12|level(35),wp_melee(230),knows_knight_foot_3|knows_twohand_6|knows_magic_defence_3,euro_face_1,swadian_face_old_2],
  
  ["england_knight_3","England Knight","England Knight",
   tf_mounted|tf_guarantee_all_lancer,0,0,fac_kingdom_4,
   [
    itm_glass_sword_b,itm_glass_long_mace,
    itm_glass_lance_2,itm_glass_lance_2,
    itm_sabre_2h_green,itm_glass_sword_c,
    #itm_glass_halberd,
    itm_shield_heater_c,itm_shield_heater_c,
    itm_gothic_plate,itm_knight_plate_2,itm_knight_plate_2,
    itm_steel_greaves,itm_plate_mittens,itm_trophy_a,
    itm_visored_bascinet_1,itm_knight_helmet1,
    itm_charger_england,itm_warhorse_england_2,itm_sg_human_small],
   str_80|agi_22|int_12|cha_12|level(45),wp_melee(280),knows_knight_foot_5|knows_physique_7|knows_shield_5|knows_power_strike_11|knows_ironflesh_13|knows_reserved_18_10|knows_weapon_master_4|knows_stealth_3|knows_magic_defence_9,nord_face_young_1, nord_face_old_2],
    
  ["england_knight_4","England Pegasus Knight","England Pegasus Knight",
   tf_mounted|tf_guarantee_all_lancer,0,0,fac_kingdom_4,
   [

    itm_glass_lance_2,itm_glass_lance_2,
    itm_trgba,itm_trgba,

    itm_glass_head,itm_glass_head,
    itm_glass_male_plate,itm_glass_male_plate,
    itm_glass_foot,itm_glass_hand,
    itm_glass_foot,itm_glass_hand,
    itm_glass_shield,itm_glass_shield,
    
    itm_charger_pegasus,itm_charger_pegasus,itm_trophy_a,itm_sg_human_small],
   str_100|agi_22|int_12|cha_12|level(50),wp_melee(330),knows_knight_foot_5|knows_physique_9|knows_shield_6|knows_power_strike_13|knows_ironflesh_15|knows_reserved_18_10|knows_weapon_master_5|knows_stealth_4|knows_magic_defence_10,nord_face_young_1, nord_face_old_2],
    
    
  ["german_knight_1","German Squire","German Squire",
   tf_mounted|tf_guarantee_all,0,0,fac_kingdom_7,
  [ 
    #itm_lance,itm_longsword,itm_sword_two_handed_a,itm_tab_shield_heater_cav_a,
  
    #itm_knight_armor5,itm_half_plates_yello,
    #itm_knight_armor5,itm_half_plates_yello,
    itm_iron_greaves2,itm_wisby_gauntlets_black,
    #itm_hounskull_2,itm_knight_helmet2,itm_knight_helmet3,
    
    itm_pistol_2stwol,itm_cartridges_burst,itm_cartridges_burst,
    itm_side_sword,itm_sword_two_handed_a,itm_lance,
    itm_tab_shield_heater_cav_a,
    
    itm_german_armour_4,itm_half_plates_yello,
    itm_iron_greaves2,itm_wisby_gauntlets_black,
    itm_sturmhaube_w3,itm_sturmhaube_w4,
    
    itm_barded_horse_german,itm_armored_horse_german],
  horse_attrib_3|level(20),wp_melee(150)|wp_firearm(200),knows_knight_foot_1|knows_firearm_4|knows_horse_archery_4,swadian_face_face_1, swadian_face_face_2],
      
  ["german_knight_2","German Knight","German Knight",
   tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_7,
    [itm_heavy_lance,itm_great_lance,
     itm_great_sword,itm_ebony_arming_sword,itm_mace_knobbedlong,
     itm_tab_shield_heater_cav_a,
     itm_reiksguard_armour,itm_reiksguard_armour,itm_iron_greaves2,
     itm_empire_helmet1,itm_empire_helmet2,itm_empire_helmet3,
     itm_warhorse_german,itm_warhorse_german,
    itm_hourglass_gauntlets_ornate,itm_hourglass_gauntlets],
   horse_attrib_4|level(30), wp_melee(210), knows_knight_foot_2|knows_twohand_5, swadian_face_face_1, swadian_face_face_2 ],
    
  ["german_knight_3","German Imperial Knight","German Imperial Knight", 
  tf_mounted|tf_guarantee_all_lancer,0,0,fac_kingdom_7,
   [itm_gothic_lance,itm_ebony_long_sword,itm_empire_warhammer,itm_tab_shield_heater_cav_b,itm_flamberge,itm_trophy_a,
    itm_gothic_plate,itm_gothic_plate_nobevor,itm_steel_greaves,itm_steel_greaves,itm_new_sallet,itm_winged_great_helmet_ger,
    itm_charger_german,itm_hourglass_gauntlets,itm_hourglass_gauntlets,itm_sg_human_small],
   horse_attrib_5|level(40), wp_melee(270), knows_knight_foot_3|knows_twohand_7, swadian_face_face_1, swadian_face_face_2 ],
   
  ["german_knight_4","German_gothic_Knights","German_gothic_Knights", 
  tf_mounted|tf_guarantee_all_lancer,0,0,fac_kingdom_7,
   [itm_gothic_lance,itm_ebony_long_mace,itm_ebony_long_mace,
    itm_ebony_great_sword,itm_shield_heater_c,itm_shield_heater_c,itm_trophy_b,
    itm_maximilian_plate,itm_maximilian_greaves,itm_maximilian_greaves,itm_maximilian_sallet,itm_maximilian_sallet_2,
    itm_armor_demi_griffin,itm_armor_demi_griffin,itm_armor_demi_griffin,itm_maximilian_gauntlets,itm_maximilian_gauntlets,itm_sg_human_small],
   horse_attrib_7|level(50),wp_melee(330),knows_knight_foot_5|knows_twohand_9|knows_magic_defence_10|knows_weapon_master_10,swadian_face_face_1, swadian_face_face_2],

  ["grey_knight_inquisitor", "Grey Knight Inquisitor", "Grey Knight Inquisitor", 
  tf_guarantee_all, 0, 0, fac_kingdom_7, 
  [
   itm_grey_knight_staff,itm_grey_knight_staff,itm_magic_wind_blast,
   itm_grey_knight_plate,itm_grey_knight_plate,itm_trophy_b,
   itm_grey_knight_foot,itm_grey_knight_foot,
   itm_grey_knight_head,itm_grey_knight_head,
   itm_grey_knight_hand,itm_grey_knight_hand
  ], 
   horse_attrib_9|int_100|level(50), wp(300), knows_knight_foot_2|knows_billman_8|knows_magic_power_6|knows_magic_defence_10|knows_magic_skill_10, swadian_face_middle_1, swadian_face_older_2 ],
  ["grey_knight_terminator", "Grey Knight Terminator", "Grey Knight Terminator", 
   tf_guarantee_all_wo_ranged, 0, 0, fac_kingdom_7, 
   [itm_grey_knight_sword,itm_grey_knight_sword,
    itm_grey_knight_shield,itm_grey_knight_shield,itm_trophy_b,
    itm_grey_knight_plate,itm_grey_knight_plate,
    itm_grey_knight_foot,itm_grey_knight_foot,
    itm_grey_knight_head,itm_grey_knight_head,
    itm_grey_knight_hand,itm_grey_knight_hand
   ], 
   str_100|agi_32|int_12|cha_12|level(50), wp(400), knows_knight_foot_2|knows_swordman_8|knows_stealth_6|knows_weapon_master_8|knows_magic_defence_10, swadian_face_middle_1, swadian_face_old_2 ],

 # ["iberian_knight_1","iberian Squire","iberian Squire",
 #  tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_11,
 # [itm_heavy_lance,itm_military_pick,itm_bec_de_corbin_a,itm_tab_shield_heater_cav_a,
 #   itm_corrazina_yellow,
 #   itm_iron_greaves2,itm_wisby_gauntlets_black,
 #   itm_hounskull_2,
 #   itm_hunter,itm_barded_horse_yellow,itm_hunter],
 # horse_attrib_2|level(25),wp_melee(100),knows_knight_order_2|knows_infantry_3,swadian_face_face_1,swadian_face_face_2],


#  ["teutonic_halbbruder","teutonic Halbbruder","teutonic Halbbruder",
#   tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_13,
#   [itm_great_lance,itm_great_lance_dark,itm_sword_medieval_d_long,itm_morningstar,itm_tab_shield_heater_cav_b,itm_german_poleaxe_1,itm_trophy_a,
#    itm_gondor_armor_low,itm_plate_boots,itm_winged_great_helmet_teu,itm_warhorse_teuton,itm_charger_teuton,itm_gauntlets,itm_sg_human_small],
#    horse_attrib_5|level(35),wp_melee(230),knows_knight_foot_2|knows_twohand_5|knows_magic_defence_6,swadian_face_young_1,swadian_face_old_2],
  


  ["nord_knight_1","NE Squire","NE Squire",
   tf_mounted|tf_guarantee_all_lancer,0,0,fac_kingdom_10,
   [itm_lance,itm_lance,
    itm_one_handed_battle_axe_b,itm_sword_viking_3_long,itm_danish_greatsword,
    itm_tab_shield_kite_cav_a,itm_tab_shield_kite_c,
    itm_huscarl_armor,itm_banded_armor,
    itm_mail_boots,itm_mail_chausses,itm_mail_mittens,itm_nord_norman_helmet,
    itm_nord_hunter,itm_nord_hunter],
   str_35|agi_16|int_6|cha_9|level(25), wp_melee(200),knows_knight_foot_2|knows_twohand_4,nord_face_younger_1,nord_face_older_2],
      
  ["nord_knight_2","NE Mounted Huscarl","NE Mounted Huscarls",
   tf_mounted|tf_guarantee_all_lancer,0,0,fac_kingdom_10,
    [itm_heavy_lance,itm_heavy_lance,
     itm_nordhero_greatsword,itm_nordhero_greatsword_2,
     itm_stahlrim_axe,itm_nordhero_sword,
     itm_shield_heater_c,itm_shield_heater_c,
     itm_plate_armor_5,itm_plate_armor_5,itm_trophy_a,
     itm_nord_plate_boots,itm_nord_norman_mask,itm_mail_mittens,
     itm_nord_warhorse,itm_nord_warhorse],
  str_60|agi_18|int_12|cha_12|level(35),wp_melee(250),knows_knight_foot_3|knows_twohand_7,nord_face_younger_1,nord_face_older_2],
  
  ["nord_knight_3","NE Knight","NE Knight",
   tf_mounted|tf_guarantee_all_lancer,0,0,fac_kingdom_10,
   [
    itm_gothic_lance,
    itm_stalhrim_sword,itm_nordhero_sword_long,
    itm_nordhero_greatsword_2,itm_nordhero_long_axe,
    itm_stalhrim_greatsword,itm_stahlrim_battleaxe,
    itm_black_shield,itm_black_shield,
    itm_nord_knight_plate,itm_nord_knight_plate,itm_gothic_plate_2,
    itm_nord_plate_boots,itm_plate_mittens,itm_great_helmet3,itm_great_helmet3,itm_trophy_b,
    itm_charger_old,itm_sg_orange_small
   ],
   str_80|agi_22|int_12|cha_12|level(45),wp_melee(300),knows_knight_foot_4|knows_twohand_9|knows_magic_power_3|knows_magic_defence_10,nord_face_younger_1, nord_face_older_2],



  ["dawnguard_1", "Dawnguard Trainer", "Dawnguard Trainer", 
  tf_guarantee_all, 0, 0, fac_kingdom_10, 
  [
   itm_dawnguard_hammer,itm_van_helsing_crossbow_bolt,itm_van_helsing_crossbow_auto,itm_dawnguard_shield,
   itm_dawnguard_hammer,itm_van_helsing_crossbow_bolt,itm_van_helsing_crossbow_auto,itm_dawnguard_shield,
   itm_dawnguard_armor,itm_dawnguard_armor,itm_trophy_b,
   itm_black_greaves,itm_black_greaves,
   itm_dawnguard_helmet,itm_dawnguard_helmet,
   itm_hourglass_gauntlets,itm_hourglass_gauntlets
  ], 
   str_80|agi_22|int_12|cha_12|level(50), wp(300), knows_precise_shot_10|knows_knight_foot_2|knows_twohand_9|knows_stealth_3|knows_necromancy_5|knows_magic_power_3|knows_magic_defence_10, nord_face_younger_1, nord_face_older_2 ],
  ["dawnguard_2", "Dawnguard MAA", "Dawnguard MAA", 
   tf_guarantee_all_wo_ranged, 0, 0, fac_kingdom_10, 
   [
    itm_dawnguard_sword,itm_dawnguard_javelin,itm_dawnguard_greatsword,itm_dawnguard_shield,itm_trophy_b,
    itm_dawnguard_sword,itm_dawnguard_javelin,itm_dawnguard_greatsword,itm_dawnguard_shield,itm_trophy_b,
    itm_dawnguard_armor,itm_dawnguard_armor,
    itm_black_greaves,itm_black_greaves,
    itm_dawnguard_helmet,itm_dawnguard_helmet,
    itm_hourglass_gauntlets,itm_hourglass_gauntlets
   ], 
   str_100|agi_32|int_12|cha_12|level(50), wp(400), knows_knight_foot_2|knows_twohand_9|knows_stealth_3|knows_magic_power_3|knows_power_throw_5|knows_weapon_master_8|knows_magic_defence_10, nord_face_younger_1, nord_face_older_2 ],
 
      
      
  ["polish_knight_1","Polish Noble","Polish Nobles",
   tf_mounted|tf_guarantee_all_lancer,0,0,fac_kingdom_8,
  [ itm_heavy_lance,itm_fighting_axe,itm_cav_axe,itm_tab_shield_kite_c,
    itm_knight_armor5,itm_knight_armor6,itm_kuyak,itm_kuyak_2,
    itm_iron_greaves,itm_gauntlets,
    itm_vaegir_noble_helmet,itm_tagancha_helm_a,
    itm_hunter_steppe_good,itm_hunter_steppe_good],
  horse_attrib_2|level(20),wp(150),knows_knight_2|knows_spearman_3,east_euro_face_young_1, east_euro_face_older_2],
      
  ["rus_dvor_cavalry", "Rus_Dvor Cavalry", "Rus_Dvor Cavalry", 
   tf_mounted|tf_guarantee_all, no_scene, reserved, fac_kingdom_8, 
   [itm_tab_shield_kite_cav_a,itm_cav_axe,
    itm_war_bow,itm_flat_headed_arrows,itm_flame_arrows,
    itm_rus_lamellar_a,itm_rus_splint_greaves,itm_leather_gloves,
    itm_tagancha_helm_a,itm_tagancha_helm_b,
    itm_vaegir_warhorse,itm_vaegir_warhorse,
    ], 
   horse_attrib_3|level(30), wp_melee(200)|wp_archery(250), knows_knight_3|knows_horse_archery_6|knows_ranger_6, vaegir_face_middle_1, vaegir_face_older_2 ],
  ["rus_dvor_cavalry_2", "Rus_Veteran Dvor Cavalry", "Rus_Veteran Dvor Cavalry", 
   tf_mounted|tf_guarantee_all, no_scene, reserved, fac_kingdom_8,
  [itm_cav_bardiche,itm_tab_shield_kite_cav_b,
   itm_imperial_bow,itm_ebony_bow,itm_ebony_arrow,itm_woodelf_arrows_poison_2,
   itm_rus_scale,itm_rus_scale,itm_iron_greaves,itm_leather_gloves,
   itm_tagancha_helm_a,itm_tagancha_helm_b,
   itm_vaegir_charger_2,itm_vaegir_charger_2
   ],
  horse_attrib_5|level(40), wp_melee(250)|wp_archery(350), knows_knight_4|knows_horse_archery_7|knows_ranger_8, vaegir_face_middle_1, vaegir_face_older_2 ],
   
 
  ["polish_knight_2","Polish Retainer","Polish Retainers",
   tf_mounted|tf_guarantee_all_lancer,0,0,fac_kingdom_8,
    [
    itm_great_lance,itm_hussar_lance_short,
     itm_great_bardiche,itm_scimitar_sulatn,itm_knightaxe,
    #itm_war_bow,itm_flat_headed_arrows,itm_flame_arrows,
    itm_rus_lamellar_a,itm_rus_splint_greaves,itm_leather_gloves,
    itm_tagancha_helm_a,itm_tagancha_helm_b,
    itm_bear_light,itm_bear_1,
    itm_gauntlets],
   horse_attrib_4|level(30), wp_melee(250)|wp_archery(200), knows_knight_foot_2|knows_spearman_6|knows_horse_archery_4|knows_power_draw_4, swadian_face_face_1, swadian_face_face_2 ],
 
  ["polish_knight_3","polish Knight","polish Knight",
   tf_mounted|tf_guarantee_all_lancer,0,0,fac_kingdom_8,
   [
    itm_gothic_lance,itm_great_lance,itm_hussar_lance_short,
   
    #itm_imperial_bow,itm_ebony_bow,itm_ebony_arrow,itm_woodelf_arrows_poison_2,
    itm_ebony_long_mace,itm_ebony_arming_sword,itm_tab_shield_kite_cav_b,
    
    #itm_knight_plate_5,itm_knight_plate_5,itm_gothic_plate,
    #itm_iron_greaves,itm_iron_greaves2,
    #itm_new_sallet,itm_visored_bascinet_1,itm_visored_bascinet_2,
    #itm_hourglass_gauntlets,itm_hourglass_gauntlets_ornate,itm_hourglass_gauntlets,
     itm_rus_scale,itm_rus_scale,itm_iron_greaves,itm_leather_gloves,
     itm_tagancha_helm_a,itm_tagancha_helm_b,
     itm_rus_scale,itm_rus_scale,itm_iron_greaves,itm_leather_gloves,
     itm_tagancha_helm_a,itm_tagancha_helm_b,
    itm_bear_armored,itm_bear_light,
    itm_sg_human_small],
   str_60|agi_22|int_12|cha_12|level(40),wp_melee(350)|wp_archery(300),knows_knight_4|knows_spearman_8|knows_horse_archery_5|knows_power_draw_6,east_euro_face_young_1, east_euro_face_older_2],

  ["polish_knight_4","Polish Guard","Polish Guard",
   tf_mounted|tf_guarantee_all_lancer,0,0,fac_kingdom_8,
   [itm_dragon_knight_lance,itm_dragon_knight_lance,
    itm_nahptha_bomb,
    itm_scottish_claymore,itm_dragon_knight_shield,
    itm_dragon_plate,itm_dragon_plate,
    itm_dragon_foot,itm_dragon_foot,itm_trophy_a,
    itm_dragon_head,itm_dragon_head,itm_dragon_knight_hand,
    itm_black_dragon,itm_black_dragon,
    itm_sg_human_big],
   str_80|agi_22|int_12|cha_12|level(50),wp_melee(350),knows_knight_6|knows_physique_8|knows_shield_10|knows_power_strike_10|knows_ironflesh_12|knows_weapon_master_5|knows_weapon_master_7|knows_magic_defence_8,east_euro_face_young_1, east_euro_face_older_2],


  ["turk_sipahi","turk sipahi","turk sipahi",
  tf_demon_human|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_9,
  [
    #itm_chaos_warrior_shield,itm_chaos_sword3,itm_sarranid_mace_1,itm_sarranid_two_handed_axe_a,
    #itm_warhorse_sarranid,
    #itm_nightmare,
    #itm_chaos_gauntlets,itm_chaos_gauntlets,
    #itm_rhun_armor_7,itm_rhun_armor_7,itm_chaos_leg_1,itm_rhun_helm_7,itm_rhun_helm_7_2
    itm_chaos_lance_1,
    itm_sarranid_two_handed_mace_1,
    itm_chaos_sword2,itm_chaos_sword3,
    itm_dec_steel_shield,
    itm_turk_mail_heavy,itm_turk_armor,
    itm_sarranid_boots_d,itm_sarranid_boots_c,
    itm_chichak1,itm_chichak2,
    itm_lamellar_charger,itm_warhorse_sarranid,
    itm_scale_gauntlets,itm_mail_mittens
   ], 
  horse_attrib_5|level(30),wp_melee(200),knows_knight_east_4|knows_spearman_5,euro_face_3, euro_face_4],
  
  ["turk_sipahi_lance", "turk sipahi", "turk sipahi", 
  tf_demon_human|tf_mounted|tf_guarantee_all_wo_ranged, no_scene, reserved, fac_kingdom_9, 
   [
    itm_chaos_lance_1, itm_chaos_lance_2,
    itm_chaos_knight_shield,itm_chaos_sword4,itm_sarranid_mace_1,itm_sarranid_two_handed_axe_b,
    itm_chaos_gauntlets,itm_chaos_gauntlets,
    itm_rhun_armor_8,itm_rhun_armor_8,itm_chaos_leg_2,itm_rhun_helm_7,itm_rhun_helm_8,itm_rhun_helm_7_2,itm_rhun_helm_9,itm_nightmare,itm_nightmare
    ], 
   horse_attrib_6|level(35), wp_melee(270), knows_knight_east_5|knows_horse_shoot_7|knows_spearman_6, euro_face_3, euro_face_4 ],
  ["turk_roy_sipahi", "turk sipahi", "turk sipahi", 
   tf_demon_human|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse, no_scene, reserved, fac_kingdom_9, 
   [
    itm_chaos_lance_2,
    itm_chaos_sword4,itm_sarranid_mace_2,
    itm_demon_sword_3,itm_sarranid_double_axe,
    itm_chaos_chosen_shield,
    itm_chaos_gauntlets,itm_chaos_gauntlets,
    itm_rhun_armor_9,itm_rhun_armor_9,itm_chaos_leg_3,itm_rhun_helm_7,itm_rhun_helm_8,itm_rhun_helm_7_2,itm_rhun_helm_9,itm_nightmare_armor,itm_nightmare_armor,
    itm_sg_human_small],
   horse_attrib_7|level(40), wp_melee(350), knows_knight_east_6|knows_horse_shoot_8|knows_spearman_8, euro_face_3, euro_face_4 ],

  ["rus_boyar", "Rus_Boyar Son", "Rus_Boyar Sons", 
   tf_mounted|tf_guarantee_all, no_scene, reserved, fac_cossack, 
  [itm_scimitar_sulatn,itm_nord_javelin,itm_cav_axe,itm_great_bardiche,itm_tab_shield_kite_d,
    itm_rus_lamellar_b,itm_rus_lamellar_a,
    itm_rus_splint_greaves,
    itm_gnezdovo_helm,itm_tagancha_helm_a,
    itm_vaegir_warhorse,itm_vaegir_warhorse,
    itm_lamellar_gauntlets,itm_leather_gloves],
   horse_attrib_3|level(25), wp_melee(200)|wp_throwing(200), knows_horse_shoot_7|knows_knight_east_2|knows_light_swordman_4|knows_power_throw_6, vaegir_face_young_1, vaegir_face_young_2 ],
  ["rus_boyar_2", "Rus_Veteran Boyar Son", "Rus_Veteran Boyar Sons", 
   tf_mounted|tf_guarantee_all_lancer, no_scene, reserved, fac_cossack, 
  [itm_scimitar_sulatn,itm_hussar_lance_short,itm_cav_bardiche,itm_great_bardiche,itm_tab_shield_kite_d,
   itm_rus_scale,itm_rus_scale,
   itm_iron_greaves,
   itm_novogrod_helm,itm_litchina_helm,
   itm_gauntlets,itm_lamellar_gauntlets,itm_trophy_a,
   itm_vaegir_charger_2,itm_vaegir_charger_2,itm_sg_human_small],
   horse_attrib_4|level(30), wp_melee(270), knows_knight_east_4|knows_light_swordman_6|knows_power_throw_6, vaegir_face_young_1, vaegir_face_young_2 ],
  ["rus_palace_guard","Rus_Palace_Guards","Rus_Palace_Guards",
   tf_mounted|tf_guarantee_all_lancer,0,0,fac_cossack,
   [itm_hussar_lance_short,itm_hussar_lance_short,itm_cav_bardiche,itm_mace_redhandle,itm_tab_shield_kite_d,
    itm_vaegir_elite_armor,itm_vaegir_elite_armor,itm_iron_greaves,itm_novogrod_helm,itm_vaegir_charger,itm_gauntlets,itm_trophy_b,
    itm_iron_greaves,itm_novogrod_helm,itm_tagancha_helm_b,itm_litchina_helm,itm_vaegir_charger,itm_gauntlets,itm_sg_human_small],
   horse_attrib_5|level(40),wp_melee(320),knows_knight_east_5|knows_light_swordman_7|knows_power_throw_6,vaegir_face_young_1, vaegir_face_young_2],

  ["we_knight_1","West Euro Squire","West Euro Squire",
   tf_mounted|tf_guarantee_all_lancer,0,0,fac_culture_1,
  [ itm_heavy_lance,itm_military_pick,itm_bastard_sword_b,
    itm_longsword,itm_one_handed_battle_axe_a,
    itm_bastard_sword_e,itm_bastard_sword_f,
    itm_tab_shield_heater_cav_a,
    itm_early_transitional_f1,itm_early_transitional_e1,
    itm_early_transitional_hre,itm_light_mail_and_plate,itm_early_transitional_heraldic,
    itm_iron_greaves2,itm_wisby_gauntlets_black,
    itm_knight_helmet1,itm_knight_helmet2,itm_knight_helmet3,
    itm_barded_horse_red,itm_barded_horse_german,itm_barded_horse_green],
  horse_attrib_2|level(20),wp_melee(140),knows_knight_1|knows_infantry_3,swadian_face_younger_1,swadian_face_older_2],
   
  ["we_knight_2","West Euro Knight","West Euro Knight",
   tf_mounted|tf_guarantee_all_lancer,0,0,fac_culture_1,
    [itm_great_lance,
     itm_sword_two_handed_b,itm_sword_medieval_d_long,itm_morningstar,
     itm_great_sword,itm_bastard_sword_f,itm_morningstar,
     itm_tab_shield_heater_cav_a,
     itm_half_plates,
     itm_knight_armor1,itm_half_plates_blue,
     itm_knight_armor2,itm_half_plates_red,
     itm_knight_armor3,itm_half_plates_yello,
     itm_iron_greaves2,itm_hounskull,itm_horned_great_helmet,
     itm_great_helmet,itm_great_helmet3,itm_horned_great_helmet,itm_winged_great_helmet,
     itm_warhorse,itm_warhorse,itm_warhorse_england,itm_warhorse_england_2,itm_warhorse_france,itm_warhorse_german,
     itm_hourglass_gauntlets_ornate,itm_hourglass_gauntlets],
 horse_attrib_3|level(25),wp_melee(140),knows_knight_2|knows_infantry_4,swadian_face_younger_1,swadian_face_older_2],
  ["we_knight_3","West Euro Chivalric Knight","West Euro Chivalric Knight",
   tf_mounted|tf_guarantee_all_lancer,0,0,fac_culture_1,
   [itm_gothic_lance,itm_bastard_sword_f,itm_morningstar,itm_sword_two_handed_b,itm_tab_shield_heater_cav_b,
    itm_bastard_sword_e,itm_knightaxe,itm_great_lance_dark,
    itm_heraldic_harness,itm_heraldic_plate,
    itm_iron_greaves,itm_iron_greaves2,
    itm_french_helm_closed,itm_classichelm_plume,itm_french_helm_closed,
    itm_charger_old,itm_charger_england,itm_charger_german,itm_charger,itm_charger_france,
    itm_hourglass_gauntlets_ornate,itm_hourglass_gauntlets],
   horse_attrib_3|level(30),wp_melee(160),knows_knight_3|knows_infantry_6,swadian_face_younger_1, swadian_face_older_2],


  ["khergit_guard", "Khergit Guard", "Khergit Guard", 
   tf_vampire|tf_guarantee_all_wo_horse, 0, 0, fac_kingdom_3, 
   [
    itm_ebony_bastard_sword,itm_ebony_scimitar_2,itm_ebony_long_mace,itm_undead_shield_kite_cav,
    itm_poison_arrows,itm_orcish_mutil_arrow,itm_khergit_long_bow,
    itm_black_helmet,itm_black_knight_foot,itm_vampire_armor_3,itm_black_knight_hand,
    itm_black_helmet,itm_black_knight_foot,itm_vampire_armor_4,itm_black_knight_hand,   
    #itm_khergit_war_horse,itm_khergit_charger
   ],
   horse_attrib_4|level(30), wp_melee(200)|wp_archery(300), knows_physique_7|knows_shield_6|knows_stealth_4|knows_power_strike_7|knows_ironflesh_8|knows_reserved_18_10|knows_weapon_master_7|knows_magic_defence_2|knows_power_draw_7|knows_magic_power_3, khergit_face_middle_2, khergit_face_old_1 ],
   
   
["khergit_general", "Khergit general", "Khergit Generals", 
 tf_vampire|tf_guarantee_all|tf_mounted, 0, 0, fac_kingdom_3, 
  [
    itm_ebony_great_sword_2,itm_soul_stealer,itm_undead_shield_kite_cav,
    itm_death_body,itm_nazgul_hood_1,
    itm_black_knight_foot,
    itm_black_knight_hand,itm_trophy_b,
    itm_nightmare,itm_nightmare,itm_sg_black_big,itm_sg_human_big
  ],
  horse_attrib_6|level(40), wp_melee(300), knows_swordman_6|knows_riding_9|knows_power_strike_7|knows_vampire_6, khergit_face_old_2, khergit_face_older_2 ],

  ["nazgul", "nazgul", "nazgul", 
   tf_vampire|tf_mounted|tf_guarantee_all, 0, 0, fac_kingdom_3, 
   [
    #itm_ebony_great_sword,
    itm_black_knight_sword,itm_black_knight_shield,
    itm_nazgul_robes,itm_nazgul_hood_1,itm_nazgul_hood_2,
    itm_black_knight_foot,
    itm_black_knight_hand,itm_trophy_c,
    itm_nightmare,itm_nightmare,itm_sg_black_big,itm_sg_black_big
   ], 
  horse_attrib_8|level(50), wp_melee(400), knows_riding_10|knows_vampire_6|knows_swordman_8, nord_face_young_1, swadian_face_older_2 ],


  ["looter","Looter","Looters",tf_guarantee_armor,0,0,fac_outlaws,
   [
    itm_hatchet,itm_club,itm_butchering_knife,itm_falchion,itm_stones,
    itm_short_tunic,itm_linen_tunic,itm_coarse_tunic,itm_tabard,itm_leather_vest,itm_red_shirt,itm_robe,
    itm_woolen_cap,itm_woolen_cap,itm_fur_hat,itm_leather_cap,itm_pilgrim_disguise,itm_straw_hat,
    itm_nomad_boots,itm_blue_hose,itm_wrapping_boots
   ],
   def_attrib|level(8),wp(60),knows_common,bandit_face1, bandit_face2],

   
  ["bandit","Bandit","Bandits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_outlaws,
   [
    itm_arrows,itm_short_bow,
    itm_cartridges,itm_flintlock_pistol,
    itm_spiked_mace,itm_sword_viking_1,itm_falchion,
    itm_nordic_shield,itm_wooden_shield,
    itm_leather_cap,itm_turban,itm_pilgrim_disguise,itm_nobleman_outfit,
    itm_leather_jerkin,itm_nomad_armor,itm_leather_apron, 
    itm_nomad_boots,itm_wrapping_boots,
    itm_saddle_horse
   ],
   def_attrib|level(15),wp(100),knows_common|knows_power_draw_2,bandit_face1, bandit_face2],
   
   
  ["brigand","Brigand","Brigands",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_outlaws,
   [
    itm_spear,itm_war_spear,
    itm_carbine,itm_flintlock_pistol_2,itm_cartridges_burst,
    itm_spiked_mace,itm_sword_viking_2,itm_two_handed_axe,
    itm_wooden_shield,itm_hide_covered_round_shield,
    itm_nasal_helmet,itm_footman_helmet,
    itm_tribal_warrior_outfit,itm_pelt_coat,itm_leather_vest,
    itm_nomad_boots,itm_saddle_horse,itm_sumpter_horse
   ],
   def_attrib|level(20),wp(125),knows_riding_2|knows_swordman_1,bandit_face1, bandit_face2],
      
      
["raider","Raider","Raiders",tf_mounted|tf_guarantee_all_lancer,0, 0, fac_outlaws,
  [
   itm_boar_spear,itm_war_spear,
   itm_military_pick,itm_bastard_sword_a,itm_sword_medieval_a,
   itm_tab_shield_heater_cav_a,
   itm_early_transitional_e1,itm_early_transitional_f1,itm_early_transitional_hre,itm_light_mail_and_plate,
   itm_mail_chausses,itm_splinted_greaves,itm_leather_boots,
   itm_guard_helmet,itm_guard_helmet,itm_mail_coif,itm_bascinet_coif,itm_bascinet_coif,
   itm_saddle_horse,itm_courser,itm_hunter    
  ],
 foot_attrib_4|level(24),wp(140) ,knows_riding_4|knows_swordman_2,bandit_face1,bandit_face2],


 ["outlaw_leader","Notorious_Outlaw","Notorious_Outlaws", tf_mounted|tf_guarantee_all, 0,0,fac_outlaws,
  [
   itm_one_handed_battle_axe_b,itm_spiked_mace,
   itm_mail_hauberk,itm_haubergeon,
   itm_splinted_leather_greaves,itm_leather_boots,
   itm_leather_gloves,
   itm_hide_covered_round_shield,
   itm_mail_coif,itm_trophy_c,itm_trophy_a,
   itm_carbine_batarey,itm_cartridges_burst,itm_sword_medieval_a,itm_sword_medieval_b,
   itm_courser,itm_hunter
  ],
  foot_attrib_5|level(30),wp(220) ,knows_riding_6|knows_physique_4|knows_shield_5|knows_weapon_master_4|knows_reserved_17_5|knows_power_strike_5|knows_ironflesh_5,bandit_face1,bandit_face2],

## CC





  ["taiga_bandit","Taiga Bandit","Taiga Bandits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_cossack,
   [itm_arrows,itm_sword_khergit_1,itm_winged_mace,itm_spear, itm_light_lance,itm_nomad_bow,itm_nomad_bow,itm_short_bow,itm_jarid,itm_javelin,itm_vaegir_fur_cap,itm_vaegir_fur_cap,itm_nomad_armor,itm_leather_jerkin,itm_hide_boots,itm_nomad_boots,itm_leather_covered_round_shield,itm_leather_covered_round_shield],
   def_attrib|level(15),wp(110),knows_common|knows_power_draw_4|knows_reserved_17_3,east_euro_face_young_1, east_euro_face_old_2],
  ["steppe_bandit","Steppe Bandit","Steppe Bandits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged|tf_mounted,0,0,fac_kingdom_3,
   [itm_arrows,itm_sword_khergit_1,itm_winged_mace,itm_spear, itm_light_lance,itm_nomad_bow,itm_nomad_bow,itm_short_bow,itm_jarid,itm_leather_steppe_cap_a,itm_leather_steppe_cap_b,itm_nomad_cap,itm_nomad_cap_b,itm_khergit_armor,itm_steppe_armor,itm_leather_vest,itm_hide_boots,itm_nomad_boots,itm_leather_covered_round_shield,itm_leather_covered_round_shield,itm_saddle_horse,itm_steppe_horse,itm_steppe_horse],
   def_attrib|level(12),wp(100),knows_riding_4|knows_horse_archery_3|knows_power_draw_3,khergit_face_young_1, khergit_face_old_2],
  ["sea_raider","Sea Raider","Sea Raiders",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_4,
   [itm_arrows,itm_sword_viking_1,itm_sword_viking_2,itm_fighting_axe,itm_battle_axe,itm_spear,itm_nordic_shield,itm_nordic_shield,itm_nordic_shield,itm_wooden_shield,itm_long_bow,itm_javelin,itm_throwing_axes,
    itm_nordic_helmet,itm_nordic_helmet,itm_nasal_helmet,itm_nomad_vest,itm_byrnie,itm_mail_shirt,itm_leather_boots, itm_nomad_boots],
   def_attrib|level(16),wp(110),knows_ironflesh_2|knows_power_strike_2|knows_power_draw_3|knows_reserved_17_2|knows_riding_1|knows_physique_2,nord_face_young_1, nord_face_old_2],
  ["mountain_bandit","Mountain Bandit","Mountain Bandits",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_5,
   [itm_arrows,itm_sword_viking_1,itm_spear,itm_winged_mace,itm_maul,itm_falchion,itm_short_bow,itm_javelin,itm_fur_covered_shield,itm_hide_covered_round_shield,
    itm_felt_hat,itm_padded_coif,itm_skullcap,itm_ragged_outfit,itm_rawhide_coat,itm_leather_armor,itm_hide_boots,itm_nomad_boots,itm_wooden_shield,itm_nordic_shield],
   def_attrib|level(11),wp(90),knows_common|knows_power_draw_2,rhodok_face_young_1, rhodok_face_old_2],
  ["desert_bandit","Desert Bandit","Desert Bandits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted,0,0,fac_kingdom_6,
   [itm_arrows,itm_arabian_sword_a,itm_winged_mace,itm_spear, itm_light_lance,itm_jarid,itm_nomad_bow,itm_short_bow,itm_jarid,itm_sarranid_cloth_robe, itm_sarranid_cloth_robe, itm_skirmisher_armor, itm_desert_turban, itm_turban,itm_leather_steppe_cap_b,itm_leather_covered_round_shield,itm_leather_covered_round_shield,itm_saddle_horse,itm_arabian_horse_a],
   def_attrib|level(12),wp(100),knows_riding_4|knows_horse_archery_3|knows_power_draw_3,khergit_face_young_1, khergit_face_old_2],


  ["taiga_brigand","Taiga Bandit","Taiga brigand",
   tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_cossack,
   [
    itm_cartridges,itm_cartridges_burst,itm_sword_khergit_2,itm_spiked_mace,itm_boar_spear, 
    itm_flintlock_pistol,itm_flintlock_pistol_2,itm_flintlock_pistol_veteran,
    itm_carbine_batarey,itm_carbine,
    itm_jarid,
    #itm_vaegir_fur_helmet,itm_vaegir_spiked_helmet,
    itm_tribal_warrior_outfit,itm_red_pikiner_uniform,
    itm_cossack_hat_c,itm_hussar_hat,
    itm_rus_shoes,itm_nomad_boots,
    itm_tab_shield_kite_b,itm_tab_shield_round_b
   ],
   def_attrib|level(20),wp_melee(130)|wp_firearm(150)|wp_throwing(130),knows_billman_3|knows_reserved_17_3,east_euro_face_young_1, east_euro_face_old_2],
         
 ["taiga_bandit_leader","Taiga Bandit Leader","Taiga Bandit Leaders",
  tf_guarantee_all,0,0,fac_cossack,
  [
   itm_cartridges_thrust,
   itm_sword_khergit_4,itm_long_bardiche,itm_awlpike_long,
   itm_flintlock_pistol_2s,itm_flintlock_pistol_elite,
   itm_carbine_batarey_2shot,itm_carbine_batarey_good,
   itm_nord_javelin,itm_jarid,
   itm_vaegir_lamellar_helmet,itm_vaegir_spiked_helmet,
   itm_kuyak,itm_ee_armor_3,itm_ee_mail_hauberk_2,
   itm_rus_cav_boots,itm_rus_splint_greaves,
   itm_tab_shield_round_c,itm_tab_shield_round_b
  ],
   foot_attrib_5|level(28),wp_melee(150)|wp_firearm(180)|wp_throwing(150),knows_billman_4|knows_thrown_4,east_euro_face_young_1, east_euro_face_old_2],  

  ["rus_cossack","Rus_cossack","Rus_cossack",
   tf_guarantee_all|tf_mounted,0,0,fac_cossack,
   [itm_arrows,itm_flame_arrows,itm_sword_khergit_3,itm_winged_mace,itm_scimitar,
    itm_nomad_bow,itm_khergit_bow,itm_nomad_bow,
    itm_vaegir_fur_helmet,itm_vaegir_lamellar_helmet,
    itm_kuyak,itm_pelt_coat,
    itm_rus_cav_boots,itm_rus_shoes,
    itm_leather_covered_round_shield,itm_leather_covered_round_shield,
    itm_courser_steppe,itm_hunter_steppe,itm_hunter_steppe_good
   ],
  horse_attrib_2|level(20),wp_one_handed(120)|wp_archery(170),knows_horse_shoot_6|knows_archer_3,vaegir_face_young_1,vaegir_face_old_2],


  ["mountain_bandit_leader","Mountain Bandit Leader","Mountain Bandit Leaders",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_outlaws,
   [itm_iron_arrow,itm_sword_viking_3,itm_war_spear,itm_military_hammer,itm_warhammer,itm_fighting_axe,itm_long_bow,itm_jarid,itm_leather_covered_round_shield,itm_plate_covered_round_shield,itm_skullcap,itm_nasal_helmet,itm_bascinet_coif,itm_byrnie,itm_haubergeon,itm_splinted_leather_greaves,itm_mail_chausses,itm_shield_heater_c,itm_tab_shield_pavise_c],
   def_attrib_multiplayer|level(23),wp(120),knows_billman_2|knows_power_draw_3,rhodok_face_young_1, rhodok_face_old_2],  






#new bandit



  ["forest_bandit","Forest Bandit","Forest Bandits",
   tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_forest_ranger,
   [itm_arrows,itm_axe,itm_hatchet,itm_quarter_staff,itm_battle_axe,itm_hand_axe,itm_iron_staff,
    itm_long_bow,itm_hunting_bow,
    itm_hood_c,itm_wizard_hood_2_2,itm_shirt,itm_green_tunic,itm_leather_jerkin,itm_ragged_outfit,itm_hide_boots],
   foot_attrib_2|level(12),wp(100),knows_archer_1,swadian_face_young_1, swadian_face_old_2],
  ["forest_brigand","Forest brigand","Forest brigand",
   tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_forest_ranger,
   [itm_iron_arrow,itm_voulge,itm_hand_axe,itm_glaive,itm_long_bow,itm_long_bow,
    itm_wizard_hood_2_2,itm_ranger_armor1,itm_leather_boots],
   foot_attrib_3|level(18),wp(140),knows_archer_2,swadian_face_young_1, swadian_face_old_2],
  ["forest_hunter","forest hunter","forest hunter",
   tf_guarantee_all_footman|tf_guarantee_ranged,0,0,fac_forest_ranger,
   [itm_bodkin_arrows,itm_long_bow_2,itm_one_handed_war_axe_b,itm_glaive,itm_long_voulge,itm_mail_coif,itm_nasal_helmet,itm_padded_leather,itm_splinted_leather_greaves],
   foot_attrib_4|level(24),wp(120)|wp_archery(200),knows_archer_4,swadian_face_young_1,swadian_face_old_2],

   
  ["sherwood_archer", "sherwood_archer", "sherwood_archer", tf_guarantee_all, 0, 0, fac_forest_ranger, 
   [itm_woodelf_mutil_arrows,itm_woodelf_mutil_arrows,itm_long_bow_3,itm_longbowman_sword,itm_long_bow_2,itm_leather_gloves,itm_wizard_hood_2_2,itm_studded_leather_coat,itm_splinted_leather_greaves,itm_sg_human_big], 
   foot_attrib_5|level(34), wp(200)|wp_archery(320), knows_magic_power_8|knows_ranger_8, nord_face_young_1, nord_face_old_2 ],

   
## CC
  ["steppe_tribesman","Steppe Tribesman","Steppe Tribesmen",
   tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_khergits,
   [
    itm_sword_khergit_1,itm_winged_mace,itm_light_lance,
    itm_nomad_bow,itm_khergit_arrows,
    #itm_javelin,
    itm_tab_shield_small_round_a,
    itm_steppe_cap,itm_nomad_cap,itm_leather_steppe_cap_a,
    itm_khergit_armor,itm_nomad_cap_b,itm_leather_vest,itm_nomad_boots,
    itm_steppe_horse,itm_saddle_horse_steppe
   ],
   foot_attrib_3|level(12),wp(100)|wp_archery(120)|wp_throwing(80),knows_horse_shoot_4|knows_archer_2|knows_reserved_17_1,khergit_face_younger_1, khergit_face_old_2],

  ["steppe_horseman_1","Steppe Horseman","Steppe Horsemen",
   tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_khergits,
  [
   #itm_khergit_arrows,itm_nomad_bow,
   itm_light_lance,itm_sword_khergit_2,itm_light_lance,
   itm_tab_shield_small_round_a,itm_tab_shield_small_round_b,
   itm_leather_steppe_cap_a, itm_leather_steppe_cap_b,itm_nomad_robe,itm_nomad_vest,
   itm_nomad_boots,itm_khergit_leather_boots,itm_spiked_helmet,itm_nomad_cap,
   itm_steppe_horse,itm_hunter_steppe
  ],
   foot_attrib_4|level(18),wp(120),knows_horse_shoot_5|knows_pikeman_2,khergit_face_young_1, khergit_face_older_2],
   
  ["steppe_horse_archer_1","Steppe Horse Archer","Steppe Horse Archers",
   tf_mounted|tf_guarantee_all,0,0,fac_khergits,
   [
    itm_sword_khergit_2,itm_winged_mace,itm_light_lance,
    itm_khergit_bow,itm_nomad_bow,
    itm_bodkin_arrows,itm_flat_headed_arrows,
    #itm_javelin,
    itm_leather_steppe_cap_b,itm_leather_steppe_cap_c,
    itm_tribal_warrior_outfit,itm_nomad_robe,
    itm_khergit_leather_boots,
    itm_tab_shield_small_round_a,itm_tab_shield_small_round_b,
    itm_steppe_horse,itm_courser_steppe
   ],
   foot_attrib_4|level(18),wp(110)|wp_archery(150),knows_horse_shoot_5|knows_archer_3|knows_reserved_17_1,khergit_face_young_1, khergit_face_older_2],
  ["steppe_horse_archer_2","Steppe Veteran Horse Archer","Steppe Veteran Horse Archers",
   tf_mounted|tf_guarantee_all,0,0,fac_khergits,
   [
    itm_sword_khergit_3,itm_winged_mace,itm_light_lance,
    itm_khergit_bow,itm_flat_headed_arrows,
    #itm_javelin,
    itm_tab_shield_small_round_b,
    itm_tab_shield_small_round_c,
    itm_vaegir_lamellar_helmet,itm_sarranid_horseman_helmet,itm_leather_warrior_cap,
    itm_lamellar_vest,itm_tribal_warrior_outfit,
    itm_khergit_leather_boots,itm_leather_gloves,
    itm_hunter_steppe,itm_courser_steppe
   ],
   foot_attrib_5|level(24),wp(120)|wp_archery(200),knows_horse_shoot_7|knows_archer_4|knows_reserved_17_4,khergit_face_middle_1, khergit_face_older_2],
  ["steppe_horseman_2","Steppe Lancer","Steppe Lancers",
   tf_mounted|tf_guarantee_all_lancer,0,0,fac_khergits,
   [
    itm_one_handed_war_axe_b,itm_sword_khergit_4,itm_spiked_mace,
    itm_heavy_lance,itm_heavy_lance,itm_lance,
    #itm_khergit_bow,itm_nomad_bow,itm_nomad_bow,
    #itm_khergit_arrows,itm_khergit_arrows,
    itm_sarranid_horseman_helmet,itm_sarranid_veiled_helmet,itm_vaegir_lamellar_helmet,
    itm_lamellar_vest,itm_lamellar_armor,
    itm_khergit_leather_boots,itm_splinted_leather_greaves,
    itm_leather_gloves,itm_scale_gauntlets,
    itm_tab_shield_small_round_b,itm_tab_shield_small_round_c,
    itm_courser_steppe,itm_hunter_steppe_good
   ],
   foot_attrib_5|level(24),wp(150),knows_horse_shoot_8|knows_pikeman_3|knows_reserved_17_4,khergit_face_middle_1, khergit_face_older_2],

  ["black_khergit_horseman","Black Khergit Horseman","Black Khergit Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_khergits,
   [itm_khergit_arrows,itm_sword_khergit_2,itm_scimitar,itm_scimitar,itm_winged_mace,itm_lance,itm_khergit_bow,itm_khergit_bow,itm_nomad_bow,itm_nomad_bow,itm_khergit_war_helmet,itm_khergit_war_helmet,itm_lamellar_armor,itm_hide_boots,itm_plate_covered_round_shield,itm_trophy_a,itm_plate_covered_round_shield,itm_huntera2,itm_huntera1],
   horse_attrib_2|level(20),wp(140),knows_horse_shoot_5|knows_archer_2|knows_swordman_2,khergit_face_young_1, khergit_face_old_2],
  ["black_khergit_guard","Black Khergit Guard","Black Khergit Guard", tf_mounted|tf_guarantee_all,0,0,fac_khergits,
  [
   itm_flat_headed_arrows,itm_scimitar,itm_winged_mace,itm_khergit_bow,itm_khergit_bow,
   itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_khergit_guard_boots,itm_trophy_b,
   itm_khergit_guard_armor,itm_khergit_guard_boots,itm_khergit_guard_armor,itm_khergit_war_horse,itm_khergit_war_horse
  ],
  horse_attrib_4|level(30),wp(160)|wp_archery(250),knows_horse_shoot_7|knows_archer_4,khergit_face_middle_2, khergit_face_old_1],
  ["black_khergit_lancer","Black Khergit Lancer","Black Khergit Lancer", tf_mounted|tf_guarantee_all_lancer,0,0,fac_khergits,
   [
    itm_khergit_lance,itm_sword_khergit_4,itm_winged_mace,itm_steel_shield,
    itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_khergit_guard_boots,
    itm_khergit_guard_armor,itm_khergit_guard_boots,itm_khergit_guard_armor,itm_trophy_b,
    itm_khergit_war_horse,itm_khergit_war_horse
   ],
  horse_attrib_4|level(30),wp(200),knows_riding_6|knows_swordman_4,khergit_face_middle_1, khergit_face_old_1],

  ["black_khergit_raidmaster","Black Khergit Raid Leader","Black Khergit Raid Leaders",tf_mounted|tf_guarantee_all,0,0,fac_khergits,
   [
    itm_flat_headed_arrows,itm_sword_khergit_4,itm_khergit_lance,itm_war_bow,itm_khergit_bow,itm_war_bow,
    itm_khergit_guard_armor,itm_khergit_guard_armor,itm_khergit_guard_boots,itm_khergit_guard_helmet,itm_scale_gauntlets,
    itm_steel_shield,itm_trophy_c,
    itm_khergit_war_horse,itm_khergit_war_horse,itm_sg_human_big
   ],
   horse_attrib_6|level(40),wp_melee(250)|wp_archery(350),knows_horse_shoot_9|knows_swordman_5|knows_power_draw_8,khergit_face_old_1, khergit_face_older_2],

  ["ninjia", "ninjia", "ninjia", tf_guarantee_all, 0, 0, fac_outlaws, 
   [itm_black_hood_mask,itm_khergit_leather_boots,itm_khergit_leather_boots,itm_robe,itm_robe,
   #itm_throwing_star_a,
   itm_strange_short_sword,itm_toumingdun], 
  horse_attrib_6|level(20), wp(180), knows_ironflesh_5|knows_reserved_17_3|knows_stealth_3|knows_power_strike_5|knows_physique_5|knows_shield_8, bandit_face1, bandit_face2 ],
  ["ninjia_adv", "ninjia", "ninjia", tf_guarantee_all, 0, 0, fac_outlaws, 
   [itm_black_hood_mask,itm_khergit_leather_boots,itm_khergit_leather_boots,itm_ninjia_armor,itm_ninjia_armor,
   #itm_throwing_star_a,
   itm_throwing_star_b,itm_strange_great_sword], 
  horse_attrib_7|level(30), wp(240), knows_ironflesh_10|knows_reserved_17_5|knows_stealth_5|knows_power_strike_8|knows_physique_10, bandit_face1, bandit_face2 ],
  ["strange_warrior", "strange_warrior", "strange_warriors", tf_guarantee_all, 0,0,fac_outlaws, 
  [itm_strange_armor,itm_strange_armor,itm_strange_boots,itm_strange_boots,itm_strange_helmet,itm_strange_helmet,itm_strange_sword,itm_strange_great_sword,itm_strange_short_sword,itm_yumi,itm_yumi2,itm_flat_headed_arrows,itm_flat_headed_arrows], 
  foot_attrib_5|level(20), wp(180), knows_billman_4|knows_power_draw_4, mercenary_face_1, mercenary_face_2 ],
  

   
     

["caravan_master","Caravan Master","Caravan Masters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_commoners,[itm_reitern_pistol_4s,itm_cartridges_burst,itm_sword_medieval_c,itm_rich_outfit,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_rich_outfit,itm_leather_cap],def_attrib|level(9),wp(100)|wp_firearm(300),knows_common|knows_riding_4|knows_ironflesh_3|knows_leadership_5,mercenary_face_1,mercenary_face_2],

["kidnapped_girl","Kidnapped Girl","Kidnapped Girls",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_commoners,[itm_dress,itm_leather_boots],def_attrib|level(2),wp(50),knows_common|knows_riding_2,woman_face_1,woman_face_2],


## CC
## CC

#This troop is the troop marked as soldiers_end and town_walkers_begin
["town_walker_1","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_short_tunic,itm_linen_tunic,itm_fur_coat,itm_coarse_tunic,itm_tabard,itm_leather_vest,itm_arena_tunic_white,itm_leather_apron,itm_shirt,itm_arena_tunic_green,itm_arena_tunic_blue,itm_woolen_hose,itm_nomad_boots,itm_blue_hose,itm_hide_boots,itm_ankle_boots,itm_leather_boots,itm_fur_hat,itm_leather_cap,itm_straw_hat,itm_felt_hat],def_attrib|level(4),wp(60),knows_common,man_face_young_1,man_face_old_2],
["town_walker_2","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_blue_dress,itm_dress,itm_woolen_dress,itm_peasant_dress,itm_woolen_hose,itm_blue_hose,itm_wimple_a,itm_wimple_with_veil,itm_female_hood],def_attrib|level(2),wp(40),knows_common,european_woman_face_1,european_woman_face_2],


 ["drowelf_walker","Townswoman","Townswoman",
  tf_female_elf|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_beast,
   [
    itm_drow_hood,
    itm_drow_armor,itm_drow_elite_armor,itm_light_leather,itm_witch_robe_1,
    itm_drow_leather_boots,itm_light_leather_boots,
   ],
   def_attrib|level(4),wp(60),knows_common,mirkwood_elf_face_1,mirkwood_elf_face_2],

 ["woodelf_walker","Townswoman","Townswoman",
  tf_male_elf|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_forest_ranger,
   [
    itm_wizard_hood_2_2,itm_mirkwood_helm_e,
    itm_mirkwood_armor_a,itm_mirkwood_clothes,itm_mirkwood_light_scale,itm_mirkwood_hunter,
    itm_mirkwood_boots,itm_mirkwood_boots,
   ],
   def_attrib|level(4),wp(60),knows_common,mirkwood_elf_face_1,mirkwood_elf_face_2],
 ["grandelf_walker","Townswoman","Townswoman",
  tf_male_elf|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_forest_ranger,
   [
    #itm_wizard_hood_2_2,itm_mirkwood_helm_e,
    itm_lorien_archer,itm_lorien_armor_e,itm_lorien_armor_a,
    itm_lorien_palace_greaves,itm_lorien_palace_greaves,
   ],
   def_attrib|level(4),wp(60),knows_common,lorien_elf_face_1,lorien_elf_face_2],

  ["dwarf_walker","Dwarf Townswoman","Dwarf Townswoman",
   tf_dwarf|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_dwarf,
   [
    itm_erebor_tunic_1,itm_erebor_tunic_2,
    itm_ironhills_tunic_1,itm_ironhills_tunic_2,
    itm_dwarf_gambeson_1,itm_dwarf_gambeson_2,
    itm_highlander_hat1,itm_highlander_hat1_1,
    itm_highlander_hat2,itm_highlander_hat2_1,
    itm_dwarf_boots,itm_dwarf_boots,
    itm_dwarf_miner_helm,itm_dwarf_miner_helm],
   def_attrib|level(4),wp(60),knows_common,nord_face_younger_1,nord_face_old_2],

 ["vampire_walker","Townswoman","Townswoman",
  tf_vampire|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_undeads_2,
   [
    #itm_wizard_hood_2_2,itm_mirkwood_helm_e,
    itm_vampire_tunic,itm_linen_tunic,itm_tabard,itm_vampire_tunic,
    itm_leather_boots,itm_hide_boots,itm_splinted_leather_greaves,
   ],
   def_attrib|level(4),wp(60),knows_common,swadian_face_young_1, swadian_face_young_1],

 ["lich_walker","Lich","Lich",
  tf_undead|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_undeads_2,
   [
    itm_lich_helm,itm_crown,itm_scull_head,itm_demon_hood,
    itm_archlich_staff_1,itm_skull_staff,itm_magic_spirit_leech,itm_magic_summon_undead,
    itm_lich_armor,itm_archlich_armor,itm_tabard,itm_vampire_tunic,
    itm_iron_greaves,itm_twilight_boots,itm_splinted_leather_greaves,
   ],
   def_attrib|level(4),wp(60),knows_common,swadian_face_young_1, swadian_face_young_1],

 ["minotaur_walker","Minotaur","Minotaur",
  tf_beastman|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_beast,
   [
    itm_two_handed_axe,itm_great_axe,
    itm_beastman_head,itm_beastman_head2,itm_beastarmour_head,itm_beastlord_head,
    itm_beastman_body,itm_beastman_armour,itm_beastman_heavyarmour,
    itm_rawhide_coat,itm_leather_vest,itm_nomad_armor,itm_fur_coat,
    itm_beast_leg,itm_beast_leg,itm_beast_leg,
   ],
   def_attrib|level(4),wp(60),knows_common,swadian_face_young_1, swadian_face_young_1],

 ["demon_walker","Heretic Townsman","Heretic Townsman",
  tf_demon_human|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_demon,
   [
    itm_sarranid_felt_hat,itm_turban,
    itm_rhun_armor_1, itm_rhun_armor_2,
    itm_sarranid_cloth_robe,itm_sarranid_cloth_robe_b,
    itm_leather_gloves,itm_wrapping_boots,itm_sarranid_boots_a,
   ],
   foot_attrib_3|level(15),wp_melee(90)|wp_firearm (100),knows_magic_3,euro_face_3, euro_face_4],

 ["ogre_walker","Ogre","Ogre",
  tf_ogre|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_orc,
   [
    itm_ogre_bear_helmet,itm_ogre_nemean_helm,itm_ogre_barbar_helm,
    itm_ogre_armor1,itm_ogre_armor2,itm_ogre_armor3,itm_ogre_armor,
    itm_ogre_boots_01,itm_ogre_boots_02,
   ],
   def_attrib|level(4),wp(60),knows_common,swadian_face_young_1, swadian_face_young_1],

 ["goblin_walker","goblin","goblin",
   tf_goblin,0,0,fac_orc,
   [itm_bolts,itm_arrows,
    itm_org_armour_1,itm_org_armour_4,itm_org_armour_3,
    itm_org_boot_1,
    itm_short_bow, itm_org_shield_1,itm_org_spear_2,itm_org_crossbow_1,
    itm_woolen_cap,itm_woolen_cap,itm_org_helmet_1,
    itm_wolf_mount_white,itm_wolf_mount_black,
   ],
   def_attrib|level(4),wp(60),knows_common,swadian_face_young_1, swadian_face_young_1],

 ["khergit_townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_steppe_cap,itm_nomad_cap_b,itm_nomad_cap,itm_fur_hat,itm_leather_steppe_cap_a,itm_leather_steppe_cap_b,
    itm_nomad_boots,itm_khergit_leather_boots,itm_wrapping_boots,
    itm_leather_vest,itm_nomad_armor,itm_khergit_armor,itm_nomad_vest,itm_nomad_robe,itm_linen_tunic, itm_rawhide_coat,
    itm_sword_khergit_1,itm_steppe_horse,
   ],
   def_attrib|level(4),wp(60),knows_common,khergit_face_younger_1, khergit_face_middle_2],
 ["east_euro_townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_kaftan,itm_cossack_hat_a,itm_cossack_hat_b,itm_cossack_hat_c,itm_fur_hat,
    itm_wrapping_boots,itm_rus_shoes,itm_khergit_leather_boots,
    itm_leather_jacket,itm_fur_coat,itm_linen_tunic,itm_rus_robe, itm_rus_robe_2
   ],
   def_attrib|level(4),wp(60),knows_common,east_euro_face_younger_1, east_euro_face_middle_2],
#["khergit_townswoman","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_blue_dress,itm_dress,itm_woolen_dress,itm_peasant_dress,itm_woolen_hose,itm_blue_hose,itm_wimple_a,itm_wimple_with_veil,itm_female_hood],def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
["sarranid_townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,[itm_sarranid_felt_hat,itm_turban,itm_wrapping_boots,itm_sarranid_boots_a,itm_sarranid_cloth_robe,itm_sarranid_cloth_robe_b],def_attrib|level(4),wp(60),knows_common,arab_face_1,arab_face_2],
["sarranid_townswoman","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_sarranid_common_dress,itm_sarranid_common_dress_b,itm_woolen_hose,itm_sarranid_boots_a,itm_sarranid_felt_head_cloth,itm_sarranid_felt_head_cloth_b],def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],

#This troop is the troop marked as town_walkers_end and village_walkers_begin
["village_walker_1","Villager","Villagers",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_short_tunic,itm_linen_tunic,itm_coarse_tunic,itm_leather_vest,itm_leather_apron,itm_shirt,itm_woolen_hose,itm_nomad_boots,itm_blue_hose,itm_hide_boots,itm_ankle_boots,itm_leather_boots,itm_fur_hat,itm_leather_cap,itm_straw_hat,itm_felt_hat],def_attrib|level(4),wp(60),knows_common,man_face_younger_1,man_face_older_2],
["village_walker_2","Villager","Villagers",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_blue_dress,itm_dress,itm_woolen_dress,itm_peasant_dress,itm_woolen_hose,itm_blue_hose,itm_wimple_a,itm_wimple_with_veil,itm_female_hood],def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],

#This troop is the troop marked as village_walkers_end and spy_walkers_begin
["spy_walker_1","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,[itm_short_tunic,itm_linen_tunic,itm_coarse_tunic,itm_tabard,itm_leather_vest,itm_robe,itm_leather_apron,itm_shirt,itm_woolen_hose,itm_nomad_boots,itm_blue_hose,itm_hide_boots,itm_ankle_boots,itm_leather_boots,itm_fur_hat,itm_leather_cap,itm_straw_hat,itm_felt_hat],def_attrib|level(4),wp(60),knows_common,man_face_middle_1,man_face_old_2],
["spy_walker_2","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,[itm_blue_dress,itm_dress,itm_woolen_dress,itm_peasant_dress,itm_woolen_hose,itm_blue_hose,itm_wimple_a,itm_wimple_with_veil,itm_female_hood],def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
# Ryan END

#This troop is the troop marked as spy_walkers_end
# Zendar
  ["tournament_master","Tournament Master","Tournament Master",tf_hero, scn_zendar_center|entry(1),reserved,  fac_commoners,[itm_nomad_armor,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common,0x0000000eff004312345b6db6cb6db6db00000000001db6db0000000000000000],
  ["trainer","Trainer","Trainer",tf_hero, scn_zendar_center|entry(2),reserved,  fac_commoners,[itm_leather_jerkin,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000d7f00004836db6db6db6db6db00000000001db6db0000000000000000],
  ["Constable_Hareck","Constable Hareck","Constable Hareck",tf_hero, no_scene,reserved,  fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,0x00000000000c41c001fb15234eb6dd3f],

# Ryan BEGIN
["Ramun_the_slave_trader","Ramun, the slave trader","Ramun, the slave trader",tf_hero|tf_demon_human, no_scene,reserved, fac_commoners,[itm_ramun_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,0x0000000fd5105592385281c55b8e44eb00000000001d9b220000000000000000],

["guide","Quick Jimmy","Quick Jimmy",tf_hero, no_scene,0,  fac_commoners,[itm_coarse_tunic,itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c318301f24e38a36e38e3],
# Ryan END


#######################
# Custom Troops begin
# FORMAT:
# 1. Regular troop: this is the actual troop entry used for the troop. Ignore the equipment list, you can leave it blank.
# 2. Equip troop: shows what the troop will be carrying when the game first starts. This is later used for saving the troop's custom selection
# 3. Troop equipment selection: List of what is available to select during the customization phase. Can have up to around 80 items max, but recommended is maybe 50 max (to leave room so you can remove items from the current selection).

  ["custom_recruit","Personal Scout","Personal Scout",tf_female_elf|tf_guarantee_all,0,0,fac_neutral,[],horse_attrib_1|level(20),wp(120)|wp_archery(200)|wp_crossbow(200),knows_ranger_3|knows_reserved_17_2,mirkwood_elf_face_1, mirkwood_elf_face_2],
  ["custom_recruit_equip","{!}na","{!}na",tf_female_elf|tf_hero|tf_inactive,0,0,fac_neutral,
   [itm_arrows,itm_hunting_bow,itm_throwing_knives,itm_mirkwood_sword,itm_mirkwood_short_spear,
    itm_wizard_hood_2_2,itm_mirkwood_armor_a,itm_mirkwood_light_scale,itm_lorien_armor_a,itm_mirkwood_boots],
  def_attrib|level(1),wp(60),knows_recruit,0],
  ["custom_recruit_selection","{!}na","{!}na",tf_female_elf|tf_hero|tf_inactive,0,0,fac_neutral,
   [
    itm_arrows,itm_hunting_bow,itm_long_bow,
    #itm_bolts,itm_hunting_crossbow,itm_drow_sword,itm_drow_hood,itm_drow_leather_boots,itm_light_leather,
    itm_throwing_knives,
    itm_lorien_sword_a,itm_mirkwood_sword,
    itm_mirkwood_short_spear,
    itm_wizard_hood_2_2,
    itm_lorien_boots,itm_mirkwood_boots,
    itm_lorien_archer,itm_mirkwood_armor_a,itm_mirkwood_light_scale,itm_lorien_armor_a
  ],
  def_attrib|level(1),wp(60),knows_recruit|knows_inventory_management_10,0],
   
   
  ["custom_militia","Personal Scout","Personal Scout",tf_female_elf|tf_guarantee_all|tf_guarantee_polearm,0,0,fac_neutral,[],horse_attrib_3|level(30),wp(185)|wp_archery(270)|wp_crossbow(280),knows_ranger_5|knows_magic_power_2|knows_magic_defence_4|knows_reserved_17_3,mirkwood_elf_face_1, mirkwood_elf_face_2],
  ["custom_militia_equip","{!}na","{!}na",tf_female_elf|tf_hero|tf_inactive,0,0,fac_neutral,
   [itm_throwing_knives,itm_courtblades_green,itm_lorien_sword_c,itm_sabre_hithlain,itm_mirkwood_spear_shield_c,itm_mirkwood_spear_shield_a,itm_mirkwood_war_spear,
  itm_mirkwood_helm_a,itm_wizard_hood_3,itm_mirkwood_armor_e,itm_mirkwood_armor_b,itm_lorien_armor_b,itm_mirkwood_boots],
  def_attrib|level(1),wp(60),knows_recruit,0],
  ["custom_militia_selection","{!}na","{!}na",tf_female_elf|tf_hero|tf_inactive,0,0,fac_neutral,
   [
   # itm_drow_hood,itm_drow_hood_high,
    itm_mirkwood_helm_a,itm_lorien_helm_a,itm_wizard_hood_3,
    itm_woodelf_arrows,itm_woodelf_mutil_arrows,itm_long_bow_2,itm_lorien_bow,
   # itm_tutorial_bolts,itm_drow_crossbow,itm_crossbow,
    itm_mirkwood_spear_shield_c,itm_mirkwood_spear_shield_a,itm_lorien_round_shield,
   # itm_drow_round_shield,itm_dueling_dagger,
    itm_throwing_knives,
   # itm_drow_sword,itm_assassin_dagger,
    itm_sabre_hithlain,itm_lorien_sword_c,itm_courtblades_ivory,itm_lorien_shield_c,
    itm_courtblades_green,itm_mirkwood_war_spear,
    itm_mirkwood_armor_e,itm_mirkwood_armor_b,itm_lorien_armor_b,
    itm_mirkwood_boots,itm_leather_boots,itm_leather_gloves,itm_lorien_boots,
    itm_glaive,
    #itm_drow_leather_boots,itm_drow_armor,          

   ],
  def_attrib|level(1),wp(60),knows_recruit|knows_inventory_management_10,0],
   
  ["custom_sount","Personal Raider","Personal Raider",tf_female_elf|tf_mounted|tf_guarantee_all|tf_guarantee_polearm,0,0,fac_neutral,[],horse_attrib_5|level(40),wp(250)|wp_archery(350)|wp_crossbow(350),knows_riding_4|knows_magic_power_3|knows_ranger_6|knows_magic_defence_6|knows_horse_shoot_5|knows_reserved_17_3,mirkwood_elf_face_1, mirkwood_elf_face_2],
  ["custom_sount_equip","{!}na","{!}na",tf_female_elf|tf_hero|tf_inactive,0,0,fac_neutral,
   [itm_woodelf_mutil_arrows,itm_imperial_bow,itm_throwing_daggers,itm_warblade_ivorygold,itm_courtblades_ivory,itm_mirkwood_great_lance,itm_warblade_greensilver,itm_sabre_2h_green,itm_lorien_shield_c,itm_mirkwood_shield_d,
  itm_lorien_helm_b,itm_lorien_helm_c,itm_lorien_armor_b,itm_mirkwood_armor_f,itm_lorien_boots,itm_lorien_warhorse],
  def_attrib|level(1),wp(60),knows_recruit,0],
  ["custom_sount_selection","{!}na","{!}na",tf_female_elf|tf_hero|tf_inactive,0,0,fac_neutral,
   [
    #itm_drow_hood_elite,itm_drow_hood_high,
    itm_mirkwood_helm_b,itm_lorien_helm_b,itm_lorien_helm_c,itm_mirkwood_helm_d,
    itm_woodelf_arrows_poison,itm_woodelf_mutil_arrows,itm_mirkwood_bow,itm_lorien_bow_2,itm_elven_arrows_fire,itm_elven_arrows_explove,itm_imperial_bow,
    #itm_tutorial_bolts,itm_bonecrossbow_auto,itm_throwing_daggers,itm_drow_bolts,
    itm_mirkwood_shield_d,itm_mirkwood_spear_shield_a,itm_drow_round_shield,itm_dueling_dagger,
    itm_ebony_scimitar_2,itm_assassin_dagger,itm_thunder_staff_melee,itm_drow_shield,
    itm_warblade_ivorygold,itm_courtblades_ivory,itm_lorien_shield_c,itm_mirkwood_great_lance,
    itm_warblade_greensilver,itm_sabre_2h_green,itm_mirkwood_great_spear,itm_lorien_shield_b,
    itm_mirkwood_armor_c,itm_mirkwood_armor_f,itm_lorien_armor_b,itm_drow_elite_armor,
    itm_mirkwood_boots,itm_lorien_boots,
    #itm_drow_leather_boots,itm_drow_elite_boots,itm_drow_elite_gloves,
    itm_lorien_warhorse
   ],
  def_attrib|level(1),wp(60),knows_recruit|knows_inventory_management_10,0],

  ["custom_footman","Personal foodman","Personal foodman",tf_guarantee_all|tf_guarantee_polearm,0,0,fac_neutral,[],
   foot_attrib_4|level(20),wp(100),knows_precise_shot_2|knows_swordman_3|knows_reserved_17_2,mercenary_face_1, mercenary_face_2],
  ["custom_footman_equip","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_neutral,
  [itm_poleaxe,itm_military_cleaver_b,itm_sword_viking_2,itm_tab_shield_heater_c,
  itm_heraldic_mail_with_tabard,itm_brigandine_heraldic,itm_splinted_greaves,itm_bascinet_coif,itm_spiked_helmet,itm_mail_mittens],
def_attrib|level(1),wp(60),knows_recruit,0],
  ["custom_footman_selection","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_neutral,
   [
    itm_long_pike,itm_poleaxe,itm_sword_two_handed_a,itm_sword_viking_2,
    itm_war_axe,itm_one_handed_battle_axe_b,itm_awlpike_long,itm_military_pick,
    itm_javelin,itm_light_throwing_axes,
    itm_military_cleaver_b,
    itm_splinted_greaves,itm_mail_mittens,
    itm_bascinet_coif,itm_combed_morion,itm_sallet,itm_sturmhaube_w1,
    itm_tab_shield_kite_d,itm_tab_shield_kite_c,itm_tab_shield_heater_c, 
    itm_heavy_crossbow,itm_light_crossbow,itm_steel_bolts,
    #itm_lamellar_vest,
    #itm_heraldic_mail_with_surcoat,itm_surcoat_over_mail,itm_mail_with_surcoat,itm_haubergeon,
    itm_brigandine_heraldic,itm_heraldic_mail_with_tabard,itm_early_transitional_heraldic,itm_banded_armor,itm_cuir_bouilli,
  ],
  def_attrib|level(1),wp(60),knows_recruit|knows_inventory_management_10,0],


  ["custom_infantry","Personal infantry","Personal infantrys",tf_guarantee_all|tf_guarantee_polearm,0,0,fac_neutral,[],
   foot_attrib_5|level(25),wp(125),knows_precise_shot_4|knows_swordman_4|knows_reserved_17_3,mercenary_face_1, mercenary_face_2],
  ["custom_infantry_equip","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_neutral,
  [itm_bastard_sword_a,itm_military_pick,itm_sword_viking_2,itm_tab_shield_heater_cav_a,
  itm_half_plates_blue,itm_half_plates_red,itm_splinted_greaves,itm_combed_morion,itm_open_sallet_coif,itm_mail_mittens,itm_gauntlets],
def_attrib|level(1),wp(60),knows_recruit,0],
  ["custom_infantry_selection","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_neutral,
   [
    itm_pike_2,
    itm_bastard_sword_b,itm_morningstar,itm_sword_medieval_c_long,
    itm_german_poleaxe_1,itm_bec_de_corbin_a,itm_great_sword,itm_long_voulge,
    itm_combed_morion,itm_open_sallet_coif,
    itm_splinted_greaves,
    itm_lamellar_gauntlets,itm_gauntlets,itm_wisby_gauntlets_black,itm_plate_mittens,
    itm_guisarme,itm_one_handed_war_axe_b,itm_english_bill,
    itm_ashwood_pike,itm_long_axe_b_alt,
    itm_throwing_spears,itm_throwing_axes,
    itm_tab_shield_heater_cav_a,itm_tab_shield_kite_c,itm_tab_shield_round_c,itm_tab_shield_pavise_c, 
    itm_sniper_crossbow,itm_light_crossbow,itm_steel_bolts,
    #itm_green_armour_4,itm_corrazina_blue,
    #itm_coat_of_plates,itm_rus_lamellar_a,itm_lamellar_armor,
    
    itm_half_plates_red,itm_half_plates_blue,itm_half_plates_yello,
    itm_zitta_bascinet,itm_sallet_coif,itm_combed_morion_3,itm_barbutte_coif,itm_sturmhaube_bnw4,itm_litchina_helm,itm_nord_norman_mask,
    itm_khergit_elite_armor,itm_sarranid_elite_armor,itm_vaegir_elite_armor,
    itm_sarranid_boots_d,itm_rus_splint_greaves,
    #itm_hounskull,itm_footman_burgonet
   ],
  def_attrib|level(1),wp(60),knows_recruit|knows_inventory_management_10,0],

  ["custom_sergeant","Personal sergeant","Personal sergeants",tf_guarantee_all|tf_guarantee_polearm,0,0,fac_neutral,[],
   foot_attrib_6|level(30),wp(160),knows_precise_shot_6|knows_swordman_5|knows_reserved_17_4,mercenary_face_1, mercenary_face_2],
  ["custom_sergeant_equip","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_neutral,
  [itm_bastard_sword_b,itm_morningstar,itm_sword_medieval_c,itm_tab_shield_heater_cav_b,
  itm_knight_plate,itm_heraldic_harness,itm_steel_greaves,itm_sallet_coif,itm_barbutte_coif,itm_milanese_gauntlets,itm_hourglass_gauntlets],
  def_attrib|level(1),wp(60),knows_recruit,0],
  ["custom_sergeant_selection","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_neutral,
   [
    itm_milanese_gauntlets,itm_hourglass_gauntlets,
    itm_long_pike,itm_bastard_sword_f,itm_morningstar2,itm_sword_medieval_c,
    itm_german_poleaxe_2,itm_polehammer_threeprong,itm_one_handed_battle_axe_c,itm_nord_poleaxe_2,itm_sword_two_handed_c_alt,itm_long_axe_c_alt,
    itm_jarid,itm_heavy_throwing_axes,
    itm_tab_shield_round_d,itm_tab_shield_pavise_d,itm_tab_shield_heater_cav_b,
    itm_arbalest_1,itm_light_crossbow,itm_swadian_steel_bolts,
    itm_knight_plate,itm_knight_plate_2,itm_knight_plate_5,itm_heraldic_harness,
    
    itm_visored_bascinet_1,itm_french_helm_closed,itm_great_helmet,itm_horned_great_helmet,itm_hounskull,itm_hounskull_2,
    #itm_zitta_bascinet,itm_sallet_coif,itm_combed_morion_3,itm_barbutte_coif,itm_sturmhaube_bnw4,itm_litchina_helm,itm_nord_norman_mask,
    #itm_heraldic_plate,
    #itm_bnw_splinted_greaves,itm_bnw_gauntlets,
    #itm_khergit_elite_armor,itm_sarranid_elite_armor,itm_vaegir_elite_armor,
    itm_steel_greaves,
    #itm_milanese_sallet,itm_new_sallet,itm_winged_great_helmet
   ],
  def_attrib|level(1),wp(60),knows_recruit|knows_inventory_management_10,0],

["custom_musket","Personal musket","Personal muskets",tf_mounted|tf_guarantee_all,0,0,fac_neutral,[],ranged_attrib_4|level(20),wp_melee(100)|wp_firearm(180),knows_precise_shot_3|knows_horse_shoot_2|knows_firearm_1,mercenary_face_1,mercenary_face_2],
["custom_musket_equip","{!}na","{!}nas",tf_hero|tf_inactive,0,0,fac_neutral,[itm_sword_medieval_b,itm_flintlock_pistol_2s,itm_old_musket,itm_cartridges_2,itm_beret_plain_brown,itm_leather_armor,itm_leather_boots],def_attrib|level(1),wp(60),knows_common,0],
["custom_musket_selection", "{!}na","{!}nas", tf_hero|tf_inactive, 0, 0, fac_neutral, 
  [
    itm_breastplate_red,itm_breastplate_blue,
    itm_beret_plain_brown,itm_beret_plain_red,
   
   itm_leather_boots,itm_leather_gloves,
   itm_sword_medieval_c,itm_sword_medieval_c_small,
   itm_tab_shield_heater_a,itm_tab_shield_pavise_a,
   itm_steppe_horse,itm_saddle_horse,
   itm_flintlock_pistol_veteran,itm_flintlock_pistol_4s,itm_flintlock_pistol_2s,
   itm_old_musket,itm_turk_musket_fitil,itm_carbine_old,itm_granata_small,
   itm_cartridges_2,itm_cartridges,itm_cartridges_burst,itm_cartridges_thrust
  ], 
  def_attrib|level(1), wp(60), knows_common|knows_inventory_management_10, 0 ],

["custom_trained_musket","Personal Trained musket","Personal Trained muskets",tf_mounted|tf_guarantee_all,0,0,fac_neutral,[],ranged_attrib_5|level(25),wp_melee(100)|wp_firearm(210),knows_precise_shot_6|knows_horse_shoot_3|knows_firearm_3,mercenary_face_1,mercenary_face_2],
["custom_trained_musket_equip","{!}na","{!}nas",tf_hero|tf_inactive,0,0,fac_neutral,[itm_good_musket,itm_cartridges_2,itm_cartridges,itm_sword_medieval_c_small,itm_tab_shield_small_round_a,itm_tab_shield_small_round_b,itm_beret_plumes_red,itm_breastplate_red,itm_splinted_leather_greaves],def_attrib|level(1),wp(60),knows_common,0],
["custom_trained_musket_selection", "{!}na","{!}nas", tf_hero|tf_inactive, 0, 0, fac_neutral, 
  [ itm_sword_medieval_c,itm_sword_medieval_c_small,
  
    itm_beret_plumes_brown,itm_beret_plumes_red,
    itm_red_armour_2,itm_blue_armour_2,

    itm_open_sallet,itm_mail_coif,itm_kettle_hat,
    itm_tab_shield_heater_a,itm_tab_shield_pavise_a,
    itm_splinted_leather_greaves,
    itm_leather_gloves,
    itm_coursera1,itm_huntera1,itm_camel2,
    itm_flintlock_pistol_veteran,itm_flintlock_pistol_4s,itm_flintlock_pistol_2s,
    itm_turk_musket_koleso,itm_carbine,itm_good_musket,itm_granata_small,
    itm_cartridges_2,itm_cartridges_burst,itm_cartridges_thrust], 
  def_attrib|level(1), wp(60), knows_common|knows_inventory_management_10, 0 ],

["custom_veteran_musket","Personal Veteran musket","Personal Veteran muskets",tf_mounted|tf_guarantee_all,0,0,fac_neutral,[],ranged_attrib_5|level(30),wp_melee(100)|wp_firearm(240),knows_precise_shot_9|knows_horse_shoot_4|knows_firearm_4,mercenary_face_1,mercenary_face_2],
["custom_veteran_musket_equip","{!}na","{!}nas",tf_hero|tf_inactive,0,0,fac_neutral,[itm_mushket_udarniy,itm_musket_cavalry,itm_cartridges,itm_rapierd,itm_combed_morion,itm_red_armour_4,itm_splinted_leather_greaves],def_attrib|level(1),wp(60),knows_common,0],
["custom_veteran_musket_selection", "{!}na","{!}nas", tf_hero|tf_inactive, 0, 0, fac_neutral, 
  [itm_turk_musket,itm_mushket_udarniy,itm_reitern_pistol_4s,itm_carbine_batarey,itm_carbine_batarey_2shot,
   itm_cartridges_2,itm_cartridges_burst,itm_cartridges_thrust,
   itm_bastard_sword_a,itm_rapierd,itm_sword_medieval_c,itm_sword_medieval_c_small,
   itm_tab_shield_heater_c,itm_tab_shield_pavise_c,
   itm_splinted_leather_greaves,itm_musket_cavalry,
   itm_coursera2,itm_camel3,itm_hunter_steppe,itm_hunter_steppe_good,itm_hunter,itm_granata_small,
   itm_red_armour_4,itm_german_armour_4,
   itm_combed_morion,itm_open_sallet,itm_combed_morion,itm_bascinet_coif
  ],
   def_attrib|level(1), wp(60), knows_common|knows_inventory_management_10, 0 ],

  ["custom_horseman","Personal Woodsman","Personal Woodsmen",tf_mounted|tf_guarantee_all|tf_guarantee_polearm,0,0,fac_neutral,[],
   horse_attrib_1|level(20),wp(140),knows_recruit|knows_horse_shoot_6|knows_physique_2|knows_ironflesh_2|knows_shield_2|knows_reserved_17_2|knows_power_strike_2|knows_power_draw_2,mercenary_face_1, mercenary_face_2],
  ["custom_horseman_equip","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_neutral,
  [itm_light_lance,itm_axe,itm_fighting_pick,itm_sword_viking_1,itm_tab_shield_heater_c,
  itm_lamellar_vest,itm_mail_hauberk,itm_leather_boots,itm_bascinet_coif,itm_spiked_helmet,itm_leather_gloves],
def_attrib|level(1),wp(60),knows_recruit,0],
  ["custom_horseman_selection","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_neutral,
   [
    itm_lance,itm_axe,itm_fighting_pick,itm_sword_khergit_2,
    itm_lamellar_vest,itm_lamellar_vest_black,
    itm_mail_hauberk,itm_haubergeon,itm_heraldic_mail_with_surcoat,
    itm_breastplate_german,
    itm_sarranid_mail_shirt,itm_turk_mail_heavy,
    
    itm_leather_boots,itm_leather_gloves,
    itm_bascinet_coif,itm_spiked_helmet,itm_kettle_hat,
    
    itm_courser,itm_courser_steppe,itm_arabian_horse_a,itm_courser_steppe,
    itm_hunter,itm_hunter_steppe,itm_arabian_horse_b,itm_hunter_steppe,itm_camel2,
    
    itm_two_handed_battle_axe_2,itm_one_handed_battle_axe_a,itm_shortened_spear,itm_mace_3,itm_sledgehammer,
    itm_tab_shield_kite_c,itm_tab_shield_small_round_a, itm_tab_shield_heater_c,
    itm_arrows,itm_strong_bow,itm_nomad_bow,itm_long_bow,
    itm_sturmhaube_w1
   ],
  def_attrib|level(1),wp(60),knows_recruit|knows_inventory_management_10,0],

  ["custom_cavalry","Personal Warden","Personal Wardens",tf_mounted|tf_guarantee_all|tf_guarantee_polearm,0,0,fac_neutral,[],
   horse_attrib_2|level(25),wp(160),knows_recruit|knows_horse_shoot_7|knows_physique_3|knows_ironflesh_3|knows_shield_3|knows_reserved_17_3|knows_power_strike_3|knows_power_draw_3, mercenary_face_1, mercenary_face_2],
  ["custom_cavalry_equip","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_neutral,
  [itm_lance,itm_bastard_sword_a,itm_military_pick,itm_sword_khergit_3,itm_tab_shield_heater_cav_a,
  itm_banded_armor,itm_kuyak,itm_mail_chausses,itm_nordic_helmet,itm_bascinet,itm_mail_mittens,itm_scale_gauntlets],
def_attrib|level(1),wp(60),knows_recruit,0],
  ["custom_cavalry_selection","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_neutral,
   [
    itm_heavy_lance,itm_military_hammer,itm_warhammer,itm_military_pick,itm_sword_khergit_3,
    itm_banded_armor,itm_cuir_bouilli,itm_light_mail_and_plate,
    itm_early_transitional_heraldic,itm_heraldic_mail_with_tabard,itm_brigandine_heraldic,
    itm_kuyak,itm_lamellar_armor,
    
    itm_mail_chausses,itm_mail_boots,
    itm_nordic_helmet,itm_bascinet,itm_guard_helmet,itm_open_sallet,

    itm_mail_mittens,itm_scale_gauntlets,
    itm_hunter,itm_steppe_horse,itm_camel2,
    itm_huntera1,itm_coursera1,itm_arabian_horse_b,itm_hunter_steppe,itm_hunter_steppe,
    itm_pike,itm_pike_2,itm_long_pike,itm_long_pike_2,
    itm_one_handed_battle_axe_b,itm_bardiche,itm_awlpike,itm_sword_two_handed_b,
    itm_tab_shield_round_c,itm_tab_shield_small_round_b,itm_tab_shield_heater_cav_a, 
    itm_iron_arrow,itm_war_bow,itm_long_bow,itm_khergit_bow,
    
    itm_bascinet_coif
   ],
  def_attrib|level(1),wp(60),knows_recruit|knows_inventory_management_10,0],

  ["custom_cavalry_2","Personal Huntmaster","Personal Huntmasters",tf_mounted|tf_guarantee_all|tf_guarantee_polearm,0,0,fac_neutral,[],
   horse_attrib_3|level(30),wp(180),knows_recruit|knows_horse_shoot_8|knows_shield_4|knows_physique_4|knows_ironflesh_4|knows_reserved_17_4|knows_power_strike_5|knows_power_draw_4,mercenary_face_1, mercenary_face_2],
  ["custom_cavalry_2_equip","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_neutral,
  [itm_heavy_lance,itm_bastard_sword_b,itm_morningstar,itm_sword_khergit_4,itm_tab_shield_heater_cav_b,
  itm_rus_scale,itm_half_plates_blue,itm_mail_boots,itm_guard_helmet,itm_great_helmet,itm_mail_mittens,itm_gauntlets],
  def_attrib|level(1),wp(60),knows_recruit,0],
  ["custom_cavalry_2_selection","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_neutral,
   [
    itm_great_lance,itm_jousting_lance,itm_hussar_lance,
    itm_sarranid_two_handed_mace_1,itm_sarranid_mace_1,itm_morningstar,itm_sword_khergit_4,
    itm_huntera2,itm_coursera2,itm_camel3,itm_hunter_steppe,itm_hunter_steppe_good,
    #itm_warhorse,
    itm_glaive,itm_great_long_bardiche,itm_one_handed_battle_axe_c,itm_awlpike_long,itm_sword_two_handed_a,
    itm_pike,itm_pike_2,itm_long_pike,itm_long_pike_2,
    itm_tab_shield_round_d,itm_tab_shield_heater_cav_b,itm_tab_shield_small_round_c,
    itm_piercing_arrows,itm_long_bow_2,itm_khergit_bow,
    
    itm_rus_scale,itm_red_armour_5,itm_blue_armour_5,
    #itm_half_plates_green,
    itm_polish_hussar_armor,
    
    itm_nikolskoe_helm,itm_litchina_helm,
    itm_sarranid_boots_d,itm_rus_splint_greaves,
    
    itm_tagancha_helm_a,itm_khergit_mask,
    itm_sturmhaube_w1,itm_combed_morion,
    itm_rus_splint_greaves,itm_bnw_splinted_greaves,itm_iron_greaves,
    
    itm_gauntlets,itm_lamellar_gauntlets,
    itm_khergit_lamellar_armor
    ],
  def_attrib|level(1),wp(60),knows_recruit|knows_inventory_management_10,0],

["custom_knight_1","Personal Heavy Cavalry","Personal Heavy Cavalry",tf_mounted|tf_guarantee_all|tf_guarantee_polearm,0,0,fac_neutral,[],horse_attrib_2|level(25),wp_melee(150)|wp_throwing(150),knows_knight_2|knows_infantry_3|knows_reserved_17_4|knows_horse_archery_5,mercenary_face_1,mercenary_face_2],
["custom_knight_1_equip","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_neutral,[itm_heavy_lance,itm_bastard_sword_b,itm_morningstar,itm_sword_medieval_c,itm_tab_shield_heater_cav_b,itm_heraldic_mail_with_surcoat,itm_banded_armor,itm_mail_boots,itm_guard_helmet,itm_great_helmet,itm_hunter,itm_warhorse,itm_mail_mittens,itm_gauntlets],def_attrib|level(1),wp(60),knows_common,0],
["custom_knight_1_selection", "{!}na","{!}na", tf_hero|tf_inactive, 0, 0, fac_neutral, 
  [itm_khergit_lance,itm_heavy_lance,itm_bastard_sword_b,itm_military_pick,itm_longsword,
   itm_bec_de_corbin_a,itm_bardiche,
   itm_one_handed_battle_axe_c,itm_awlpike_long,itm_sword_two_handed_a,itm_nord_javelin,itm_long_axe_b_alt,
   itm_tab_shield_round_d,itm_tab_shield_heater_cav_b,
   
   itm_early_transitional_heraldic,itm_lamellar_armor,itm_rus_lamellar_b,
   itm_corrazina_blue,itm_corrazina_yellow,itm_corrazina_green,
   
   itm_hounskull,itm_horned_great_helmet,itm_great_helmet,itm_sturmhaube_w3,itm_zitta_bascinet,itm_sallet_coif,
   
   itm_vaegir_war_helmet,itm_novogrod_helm,itm_sarranid_veiled_helmet,itm_tagancha_helm_b,
   itm_sarranid_boots_d,itm_rus_splint_greaves,
   
   itm_iron_greaves2,itm_iron_greaves,itm_wisby_gauntlets_black,
   itm_lamellar_warhorse,itm_huntera2,itm_camel3,
   
   itm_warhorse,itm_nord_warhorse,itm_vaegir_warhorse,itm_lamellar_warhorse_2,itm_khergit_war_horse,itm_warhorse_german,itm_warhorse_england,
   
         
  ], def_attrib|level(1), wp(60), knows_common|knows_inventory_management_10, 0 ],
            
["custom_knight_2","Personal Heavy Cavalry","Personal Heavy Cavalry",tf_mounted|tf_guarantee_all|tf_guarantee_polearm,0,0,fac_neutral,[],horse_attrib_4|level(35),wp_melee(200)|wp_throwing(200),knows_knight_3|knows_infantry_5|knows_reserved_17_5|knows_horse_archery_5,mercenary_face_1,mercenary_face_2],
["custom_knight_2_equip","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_neutral,[itm_heavy_lance,itm_bastard_sword_b,itm_morningstar,itm_sword_medieval_c,itm_tab_shield_heater_cav_b,itm_heraldic_mail_with_surcoat,itm_banded_armor,itm_mail_boots,itm_guard_helmet,itm_great_helmet,itm_warhorse,itm_mail_mittens,itm_gauntlets],def_attrib|level(1),wp(60),knows_common,0],
["custom_knight_2_selection", "{!}na","{!}na", tf_hero|tf_inactive, 0, 0, fac_neutral, 
  [
   itm_great_lance,itm_practice_lance,
   itm_bastard_sword_e,itm_morningstar,itm_sword_medieval_d_long,itm_scimitar_b,
   itm_german_poleaxe_3,itm_polehammer_threeprong,itm_great_bardiche,itm_great_sword,itm_nord_javelin,
   itm_tab_shield_round_d,itm_tab_shield_pavise_d,itm_tab_shield_heater_cav_b,
   #itm_knight_plate,itm_knight_plate_2,itm_knight_plate_3,itm_knight_plate_4,itm_knight_plate_5,itm_heraldic_harness,
   
   itm_plate_armor,itm_plate_armor_2,itm_plate_armor_3,itm_plate_armor_4,itm_plate_armor_5,itm_heraldic_plate,itm_heraldic_plate_2,
   #itm_half_plates,
   #itm_zitta_bascinet,
   itm_hounskull,itm_hounskull_2,itm_hounskull_3,itm_french_helm_closed,
   
   itm_charger_old,itm_warhorse_england_2,itm_vaegir_charger,itm_lamellar_charger,itm_charger_france,itm_charger_german,itm_warhorse_steppe,
   
   itm_hourglass_gauntlets,itm_iron_greaves,
   itm_khergit_elite_armor,itm_vaegir_elite_armor,itm_sarranid_elite_armor,
   itm_nikolskoe_helm,itm_litchina_helm,
   itm_sarranid_boots_d,itm_rus_splint_greaves,
   itm_long_axe_c_alt,itm_heavy_throwing_axes,itm_one_handed_battle_axe_c,
   ], 
   def_attrib|level(1), wp(60), knows_common|knows_inventory_management_10, 0 ],
   
   
["custom_knight_3","Personal knight","Personal knight",tf_mounted|tf_guarantee_all|tf_guarantee_polearm,0,0,fac_neutral,[],horse_attrib_6|level(45),wp_melee(250)|wp_throwing(250),knows_knight_4|knows_infantry_7|knows_reserved_17_6,mercenary_face_1,mercenary_face_2],
["custom_knight_3_equip","{!}na","{!}na",tf_hero|tf_inactive,0,0,fac_neutral,[itm_great_lance,itm_sword_medieval_d_long,itm_morningstar,itm_sword_medieval_c,itm_tab_shield_heater_cav_b,itm_knight_plate_2,itm_plate_boots,itm_winged_great_helmet,itm_charger_old,itm_gauntlets],def_attrib|level(1),wp(60),knows_common,0],
["custom_knight_3_selection", "{!}na","{!}na", tf_hero|tf_inactive, 0, 0, fac_neutral, 
   [itm_polehammer_manhunter,itm_practice_lance,itm_hussar_lance_short,itm_gothic_lance,
    itm_morningstar,itm_morningstar2,itm_sword_medieval_d_long,itm_scimitar_sulatn,itm_bastard_sword_f,
    itm_tab_shield_heater_cav_b,
    itm_gothic_plate,itm_milanese_plate,itm_heraldic_harness,
    itm_khergit_guard_helmet,itm_khergit_guard_boots,itm_khergit_guard_armor,
    #itm_khergit_elite_armor,itm_sarranid_elite_armor,itm_vaegir_elite_armor,
    itm_french_helm_closed,itm_visored_bascinet_2,
    itm_french_helm_3,itm_milanese_sallet,itm_classichelm_plume,itm_winged_great_helmet,itm_new_sallet,
    itm_charger_noble,itm_charger_old,itm_charger_plate_german,
    itm_gauntlets,itm_milanese_gauntlets,itm_hourglass_gauntlets,
    itm_iron_greaves,itm_iron_greaves2,itm_plate_boots,itm_steel_greaves,
    itm_swiss_halberd,itm_great_bardiche,itm_nord_poleaxe_3,itm_sword_claymore_02,itm_flamberge,itm_double_axe,itm_knightaxe,
    itm_nord_jarid,itm_nord_javelin,
    itm_tab_shield_pavise_d,itm_steel_shield], 
   def_attrib|level(1), wp(60), knows_common|knows_inventory_management_10, 0 ],

["custom_cannon_man","Personal cannon_man","Personal cannon_men",tf_guarantee_all,0,0,fac_neutral,[],def_attrib_nobel_low|level(60),wp_one_handed(90)|wp_two_handed(90)|wp_polearm(90)|wp_firearm(220),knows_ironflesh_10|knows_physique_6|knows_power_strike_6|knows_magic_power_5|knows_magic_defence_5|knows_magic_skill_10,mercenary_face_1,mercenary_face_2],
["custom_cannon_man_equip","{!}na","{!}nas",tf_hero|tf_inactive,0,0,fac_neutral,[itm_cartridges_cannon,itm_hand_cannon,itm_bnw_armour_green,itm_sturmhaube_bnw1,itm_bnw_armour,itm_combed_morion,itm_splinted_leather_greaves,itm_sword_medieval_c],def_attrib|level(1),wp(60),knows_common,0],
["custom_cannon_man_selection", "{!}na","{!}nas", tf_hero|tf_inactive, no_scene, reserved, fac_neutral, 
 [itm_cartridges_thrust,itm_cartridges_cannon,itm_cartridges_burst,itm_hand_cannon,itm_bnw_armour_green,itm_sturmhaube_bnw1,itm_bnw_armour,itm_combed_morion,itm_splinted_leather_greaves,itm_sword_medieval_c,itm_half_plates_blue,itm_half_plates_red,itm_half_plates,itm_half_plates,itm_steel_greaves,itm_musket_rifle,itm_wooden_staff_1,itm_magic_robe,itm_horse_euro,itm_wizard_hat,itm_magic_ice_ray,itm_magic_burning_gaze,itm_magic_searing_doom], 
 def_attrib|level(1), wp(60), knows_common|knows_inventory_management_10, 0 ],


["custom_troops_end","{!}na","{!}na",0,0,0,fac_neutral,[itm_velvet],def_attrib|level(1),wp(60),knows_common|knows_inventory_management_10,swadian_face_middle_1, swadian_face_older_2],

["inventory_backup","{!}Inventory","{!}Inventory",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10,0],
# Custom Troops end
####################

## CC bandit heroes
  ["forest_bandit_hero","{!}Forest Bandit Hero","{!}Forest Bandits",tf_hero|tf_randomize_face,0,0,fac_outlaws,
   [itm_flame_arrows,itm_elven_bow,itm_one_handed_war_axe_b, itm_nasal_helmet,itm_mail_shirt,itm_leather_boots],
   knight_attrib_5|level(22),wp(180)|wp_archery(250),knows_archer_6|knows_leadership_4,swadian_face_young_1, swadian_face_old_2],
  #["forest_bandit_hero","{!}Forest Bandit Hero","{!}Forest Bandits",tf_hero|tf_randomize_face,0,0,fac_outlaws,
   #[itm_bodkin_arrows,itm_war_bow,itm_one_handed_war_axe_b, itm_nasal_helmet,itm_padded_leather,itm_ankle_boots],
   #knight_attrib_5|level(22),wp(180),knows_common|knows_power_strike_3|knows_power_draw_6|knows_tactics_4|knows_leadership_4,swadian_face_young_1, swadian_face_old_2],
  ["taiga_bandit_hero","{!}Taiga Bandit Hero","{!}Taiga Bandits",tf_hero|tf_randomize_face,0,0,fac_outlaws,
   [itm_bodkin_arrows,itm_strong_bow,itm_sword_khergit_4,itm_maul, itm_throwing_spears,itm_leather_warrior_cap,itm_lamellar_vest,itm_leather_boots,itm_leather_covered_round_shield],
   knight_attrib_5|level(30),wp(220),knows_common|knows_power_draw_8|knows_power_strike_4|knows_reserved_17_6|knows_tactics_6|knows_leadership_6,east_euro_face_young_1, east_euro_face_old_2],
  ["steppe_bandit_hero","{!}Steppe Bandit Hero","{!}Steppe Bandits",tf_hero|tf_randomize_face,0,0,fac_outlaws,
   [itm_flat_headed_arrows,itm_khergit_bow,itm_sword_khergit_4,itm_winged_mace, itm_heavy_lance,itm_khergit_guard_helmet,itm_khergit_guard_boots,itm_khergit_guard_armor,itm_leather_covered_round_shield,itm_khergit_war_horse],
   knight_attrib_5|level(24),wp(200),knows_riding_8|knows_power_strike_3|knows_ironflesh_4|knows_horse_archery_6|knows_power_draw_6|knows_tactics_5|knows_leadership_5,khergit_face_young_1, khergit_face_old_2],
  ["sea_raider_hero","{!}Sea Raider Hero","{!}Sea Raiders",tf_hero|tf_randomize_face,0,0,fac_outlaws,
   [itm_iron_arrow,itm_long_bow,itm_sword_viking_3,itm_long_axe_c,itm_tab_shield_round_d,itm_throwing_axes,
    itm_nordic_huscarl_helmet,itm_mail_hauberk,itm_mail_mittens],
   knight_attrib_5|level(32),wp(220),knows_ironflesh_4|knows_power_strike_4|knows_power_draw_6|knows_reserved_17_4|knows_riding_2|knows_physique_4|knows_tactics_6|knows_leadership_6,nord_face_young_1, nord_face_old_2],
  ["mountain_bandit_hero","{!}Mountain Bandit Hero","{!}Mountain Bandits",tf_hero|tf_randomize_face,0,0,fac_outlaws,
   [itm_iron_arrow,itm_strong_bow,itm_sword_viking_3,itm_plate_covered_round_shield,
    itm_leather_cap,itm_nomad_robe,itm_hide_boots],
   knight_attrib_5|level(22),wp(180),knows_common|knows_power_strike_2|knows_power_draw_4|knows_tactics_4|knows_leadership_4,rhodok_face_young_1, rhodok_face_old_2],
  ["desert_bandit_hero","{!}Desert Bandit Hero","{!}Desert Bandits",tf_hero|tf_randomize_face,0,0,fac_outlaws,
   [itm_throwing_scimitar,itm_throwing_scimitar,itm_sarranid_cavalry_sword,itm_winged_mace, itm_lance,itm_mamluke_mail, itm_sarranid_veiled_helmet,itm_sarranid_boots_b,itm_leather_covered_round_shield,itm_arabian_horse_b],
   knight_attrib_5|level(24),wp(200),knows_riding_8|knows_horse_archery_6|knows_power_strike_3|knows_reserved_17_6|knows_tactics_5|knows_leadership_5,khergit_face_young_1, khergit_face_old_2],
   
#["dark_knight_hero",  "dark_knight_hero",  "dark_knight_hero",  tf_unmoveable_in_party_window|tf_hero|tf_randomize_face, 0,reserved,  fac_dark_knights,[itm_charger_twilight,   itm_rich_outfit,        itm_blue_hose,                  itm_black_greaves,               itm_twiligh_armor, itm_twilight_gloves,    itm_bastard_sword_d_fire,      itm_lordaeron,  itm_gothic_lance,       itm_horned_great_helmet],          knight_attrib_5,wp(220),knight_skills_5|knows_trainer_5, swadian_face_young_1,swadian_face_older_2],

["forest_ranger_hero","Forest ranger Hero","{!}Forest Bandits",tf_unmoveable_in_party_window|tf_hero|tf_randomize_face,0,0,fac_welsh,[itm_flame_arrows,itm_bodkin_arrows,itm_elven_bow,itm_military_pick,itm_nasal_helmet,itm_mail_shirt,itm_leather_boots],knight_attrib_5|level(22),wp(180)|wp_archery(230),knows_common|knows_power_strike_3|knows_ironflesh_4|knows_power_draw_8|knows_tactics_4|knows_leadership_4,swadian_face_young_1,swadian_face_old_2],
  ["mountain_tribe_hero","Mountain tribe Hero","{!}Mountain tribe",
    tf_unmoveable_in_party_window|tf_hero|tf_randomize_face,0,0,fac_mountain_tribe,
  [itm_sword_claymore_01,itm_sword_viking_3,itm_plate_covered_round_shield,itm_nasal_helmet,itm_plate_armor,itm_plate_boots,itm_gauntlets],
  knight_attrib_5|level(35),wp(300),knows_twohand_5|knows_physique_8|knows_tactics_4|knows_leadership_4,rhodok_face_young_1,rhodok_face_old_2],
   
## CC


  ["Xerina","Xerina","Xerina",tf_unmoveable_in_party_window|tf_hero|tf_female, scn_the_happy_boar|entry(5),reserved,  fac_commoners,[itm_morningstar,itm_zlmg,itm_cartridges_thrust,itm_tab_shield_heater_cav_b,itm_cartridges_thrust,itm_leather_jerkin,itm_hide_boots,itm_half_plates,itm_hourglass_gauntlets,itm_combed_morion,itm_iron_greaves2,itm_barded_horse_green],def_attrib|str_15|agi_15|level(39),wp(312),knows_power_strike_5|knows_ironflesh_5|knows_riding_6|knows_power_draw_4|knows_physique_8|knows_shield_3,0x00000001ac0820074920561d0b51e6ed00000000001d40ed0000000000000000],
  ["Dranton","Dranton","Dranton",tf_unmoveable_in_party_window|tf_hero, scn_the_happy_boar|entry(2),reserved,  fac_commoners,[itm_gothic_lance,itm_great_mace,itm_mjolnir_melee,itm_leather_vest,itm_hide_boots,itm_tab_shield_heater_cav_b,itm_hounskull_3,itm_half_plates_red,itm_hourglass_gauntlets_ornate,itm_charger],def_attrib|str_15|agi_14|level(42),wp(324),knows_power_strike_5|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_physique_4|knows_shield_3,0x0000000a460c3002470c50f3502879f800000000001ce0a00000000000000000],
  ["Kradus","Kradus","Kradus",tf_unmoveable_in_party_window|tf_hero, scn_the_happy_boar|entry(3),reserved,  fac_commoners,[itm_padded_leather,itm_hide_boots,itm_scimitar_sulatn,itm_throwing_pike,itm_litchina_helm,itm_great_long_bardiche,itm_great_lance,itm_tab_shield_kite_cav_b,itm_gauntlets,itm_vaegir_elite_armor,itm_iron_greaves,itm_vaegir_charger],def_attrib|str_15|agi_14|level(43),wp(270),knows_power_strike_5|knows_ironflesh_7|knows_riding_6|knows_power_draw_4|knows_physique_4|knows_shield_3,0x0000000f5b1052c61ce1a9521db1375200000000001ed31b0000000000000000],


#Tutorial
["tutorial_trainer","Training Ground Master","Training Ground Master",tf_hero, 0, 0, fac_commoners,[itm_robe,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common,0x000000000008414401e28f534c8a2d09],
["tutorial_student_1","{!}tutorial_student_1","{!}tutorial_student_1",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,[itm_practice_sword,itm_practice_shield,itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],def_attrib|level(2),wp(20),knows_common,swadian_face_young_1,swadian_face_old_2],
["tutorial_student_2","{!}tutorial_student_2","{!}tutorial_student_2",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,[itm_practice_sword,itm_practice_shield,itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],def_attrib|level(2),wp(20),knows_common,swadian_face_young_1,swadian_face_old_2],
["tutorial_student_3","{!}tutorial_student_3","{!}tutorial_student_3",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,[itm_practice_staff,itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],def_attrib|level(2),wp(20),knows_common,swadian_face_young_1,swadian_face_old_2],
["tutorial_student_4","{!}tutorial_student_4","{!}tutorial_student_4",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,[itm_practice_staff,itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],def_attrib|level(2),wp(20),knows_common,swadian_face_young_1,swadian_face_old_2],

#Sargoth
#halkard, hardawk. lord_taucard lord_caupard. lord_paugard

#Salt mine
["Galeas","Galeas","Galeas",tf_hero, 0, reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,0x000000000004718201c073191a9bb10c],

#Dhorak keep

["farmer_from_bandit_village","Farmer","Farmers",tf_guarantee_armor,no_scene,reserved,fac_commoners,[itm_linen_tunic,itm_coarse_tunic,itm_shirt,itm_nomad_boots,itm_wrapping_boots],def_attrib|level(4),wp(60),knows_common,man_face_middle_1,man_face_older_2],
["bookcase_spell","{!}Bookcase","{!}Bookcase",tf_hero,0,reserved,fac_neutral,[],def_attrib,0,knows_inventory_management_10,0],
["bookcase_voice","{!}Bookcase","{!}Bookcase",tf_hero,0,reserved,fac_neutral,[],def_attrib,0,knows_inventory_management_10,0],
["bookcase_special_ability","{!}Bookcase","{!}Bookcase",tf_hero,0,reserved,fac_neutral,[],def_attrib,0,knows_inventory_management_10,0],
["Bookcase_special_ability_extra","{!}Bookcase","{!}Bookcase",tf_hero,0,reserved,fac_neutral,[],def_attrib,0,knows_inventory_management_10,0],
["Bookcase_special_ability_passive","{!}Bookcase","{!}Bookcase",tf_hero,0,reserved,fac_neutral,[],def_attrib,0,knows_inventory_management_10,0],
["Bookcase_bash","{!}Bookcase","{!}Bookcase",tf_hero,0,reserved,fac_neutral,[],def_attrib,0,knows_inventory_management_10,0],
["Bookcase_drink","{!}Bookcase","{!}Bookcase",tf_hero,0,reserved,fac_neutral,[],def_attrib,0,knows_inventory_management_10,0],




["trainer_1","Trainer","Trainer",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_1,0],

["trainer_2","Trainer","Trainer",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_4,0],

["trainer_3","Trainer","Trainer",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_7,0],

["trainer_4","Trainer","Trainer",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10,0],

["trainer_5","Trainer","Trainer",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10,0],


# Ransom brokers.
["ransom_broker_1","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_blue_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["ransom_broker_2","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_tabard,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["ransom_broker_3","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["ransom_broker_4","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_short_tunic,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["ransom_broker_5","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_green_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["ransom_broker_6","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["ransom_broker_7","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_red_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["ransom_broker_8","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["ransom_broker_9","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_yellow_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["ransom_broker_10","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_padded_leather,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],

# Tavern traveler.
  ["tavern_traveler_1","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_pilgrim_disguise, itm_pilgrim_hood, itm_hide_boots],horse_attrib_2|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_2","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_ranger_armor1,itm_hood_c,itm_bamboo_arrows,itm_long_bow,itm_wrapping_boots],horse_attrib_2|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_3","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_wizard_hat,itm_wooden_staff_1,itm_magic_searing_doom,itm_magic_robe,itm_leather_boots],horse_attrib_2|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
        
  ["tavern_traveler_4","Traveller","Traveller",tf_male_elf|tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_war_bow,itm_elven_arrows,itm_lorien_armor_a,itm_lorien_boots],horse_attrib_2|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  
  
  ["tavern_traveler_5","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_highlander_hat1_1,itm_highlander_armor4_1,itm_highlander_boot1_1],horse_attrib_2|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_6","Traveller","Traveller",tf_female|tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_lady_dress_blue,itm_hide_boots],horse_attrib_2|level(5),wp(20),knows_common,refugee_face1,refugee_face2],
  ["tavern_traveler_7","Traveller","Traveller",tf_vampire|tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_skull_staff,itm_magic_spirit_leech,itm_vampire_tunic,itm_hide_boots],horse_attrib_2|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_8","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_armor7,itm_assasin_hood_2,itm_hide_boots],horse_attrib_2|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_9","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_kaftan,itm_cossack_hat_c,itm_rus_shoes],horse_attrib_2|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_10","Traveller","Traveller",tf_female|tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_valkyrie_helm_1,itm_valkyrie_armor_1,itm_tab_shield_round_c,itm_nordhero_sword_long,itm_nord_throwing_spears,itm_hide_boots],horse_attrib_2|level(5),wp(20),knows_common,refugee_face1,refugee_face2],

# Tavern traveler.
["tavern_bookseller_1","Book_Merchant","Book_Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_reading_ani,itm_fur_coat,itm_hide_boots,itm_book_tactics,itm_book_persuasion,itm_book_spotting_reference,itm_book_leadership,itm_book_intelligence,itm_book_training_reference,itm_book_surgery_reference],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["tavern_bookseller_2","Book_Merchant","Book_Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_reading_ani,itm_fur_coat,itm_hide_boots,itm_book_wound_treatment_reference,itm_book_prisoner_management,itm_book_first_aid_reference,itm_book_trade,itm_book_engineering,itm_book_weapon_mastery,itm_book_pathfinding_reference],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],

# Tavern minstrel.
["tavern_minstrel_1","Wandering Minstrel","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_leather_jacket, itm_hide_boots, itm_dedal_lira, itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["tavern_minstrel_2","Wandering Bard","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_tunic_with_green_cape, itm_hide_boots, itm_dedal_lutnia, itm_lyre],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["tavern_minstrel_3","Wandering Ashik","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_nomad_robe, itm_hide_boots, itm_dedal_lira, itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["tavern_minstrel_4","Wandering Skald","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_fur_coat, itm_hide_boots, itm_dedal_lutnia, itm_lyre],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["tavern_minstrel_5","Wandering Troubadour","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_short_tunic, itm_hide_boots, itm_dedal_lira, itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],


## CC
["mystic_merchant_1","Mystic Merchant","Mystic Merchant",tf_hero|tf_is_merchant|tf_randomize_face|tf_demon_human, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,merchant_face_1,merchant_face_2],
["mystic_merchant_2","Mystic Merchant","Mystic Merchant",tf_hero|tf_is_merchant|tf_randomize_face|tf_male_elf, 0, reserved, fac_commoners,[itm_mirkwood_helm_a,itm_mirkwood_armor_d,itm_mirkwood_boots],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,mirkwood_elf_face_1,mirkwood_elf_face_2],
["mystic_merchant_3","Mystic Merchant","Mystic Merchant",tf_hero|tf_is_merchant|tf_randomize_face|tf_male_elf, 0, reserved, fac_commoners,[itm_lorien_helm_a,itm_lorien_archer,itm_lorien_boots],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,lorien_elf_face_1,lorien_elf_face_2],
["mystic_merchant_4","Mystic Merchant","Mystic Merchant",tf_hero|tf_is_merchant|tf_randomize_face|tf_goblin, 0, reserved, fac_commoners,[itm_org_armour_5,itm_org_boot_2,itm_org_helmet_3],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,merchant_face_1,merchant_face_2],
["mystic_merchant_5","Mystic Merchant","Mystic Merchant",tf_hero|tf_is_merchant|tf_randomize_face|tf_undead, 0, reserved, fac_commoners,[itm_death_body],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,merchant_face_1,merchant_face_2],
["mystic_merchant_6","Mystic Merchant","Mystic Merchant",tf_hero|tf_is_merchant|tf_randomize_face|tf_beastman, 0, reserved, fac_commoners,[itm_beastlord_head,itm_beastman_heavyarmour,itm_beast_leg],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,merchant_face_1,merchant_face_2],
["mystic_merchant_7","Mystic Merchant","Mystic Merchant",tf_hero|tf_is_merchant|tf_randomize_face|tf_dwarf, 0, reserved, fac_commoners,[itm_dwarf_miner_helm,itm_hide_boots,itm_highlander_armor4],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,merchant_face_1,merchant_face_2],
["mystic_merchant_8","Mystic Merchant","Mystic Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_magic_robe,itm_leather_boots,itm_wizard_hat],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,merchant_face_1,merchant_face_2],
["mystic_merchant_9","Mystic Merchant","Mystic Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_priest_robe_1,itm_priest_1_boots,itm_black_hood],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,merchant_face_1,merchant_face_2],

## CC

#NPC system changes begin
#Companions
["kingdom_heroes_including_player_begin",  "kingdom_heroes_including_player_begin",  "kingdom_heroes_including_player_begin",  tf_hero, 0,reserved,  fac_kingdom_1,[],          lord_attrib,wp(220),knows_lord_1, 0x000000000010918a01f248377289467d],



["npc1","Borcha","Borcha",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_khergit_armor,itm_nomad_cap,itm_nomad_boots,itm_sword_khergit_1],def_attrib_multiplayer|int_12|cha_7|level(3),wp(60),knows_tracker_npc|knows_ironflesh_1|knows_stealth_5|knows_pathfinding_3|knows_physique_2|knows_tracking_1|knows_riding_3|knows_weapon_master_3,0x00000004bf086143259d061a9046e23500000000001db52c0000000000000000],

["npc2","Marnid","Marnid", tf_hero|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,[itm_leather_jacket,itm_leather_boots,itm_leather_gloves,itm_club,itm_nord_horse],def_attrib_multiplayer|int_11|cha_6|level(1),wp(40)|wp_firearm(140),knows_merchant_npc|knows_trade_7|knows_weapon_master_3|knows_ironflesh_3|knows_power_strike_3|knows_physique_2|knows_first_aid_1|knows_leadership_1,0x000000019d004001570b893712c8d28d00000000001dc8990000000000000000],
["npc3","Ymira","Ymira",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_dress,itm_woolen_hose,itm_knife,itm_hunting_crossbow,itm_bolts,itm_horse_euro],def_attrib_multiplayer|int_11|cha_9|level(1),wp(20)|wp_firearm(120),knows_merchant_npc|knows_precise_shot_3|knows_magic_power_3|knows_magic_defence_2|knows_wound_treatment_1|knows_trade_1|knows_first_aid_3|knows_undead_master_1|knows_physique_1|knows_riding_1,0x00000001800000190000000000000e0000000000000000000000000000000000],
["npc4","Rolf","Rolf",tf_demon_human|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_leather_jerkin,itm_nomad_boots, itm_sword_medieval_b,itm_javelin,itm_javelin,itm_mail_hauberk],horse_attrib_3|level(5),wp(200),knows_knight_npc|knows_weapon_master_2|knows_power_strike_3|knows_riding_2|knows_physique_4|knows_reserved_17_4|knows_stealth_4|knows_undead_master_1|knows_tactics_2|knows_leadership_2|knows_looting_10,0x000000057f1074002c75c6a8a58ad72e00000000001e1a890000000000000000],

["npc5","Baheshtur","Baheshtur",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_lamellar_vest,itm_khergit_leather_boots,itm_hunter_steppe_good,itm_sword_khergit_3,itm_khergit_arrows,itm_khergit_bow,itm_tab_shield_small_round_c,itm_leather_steppe_cap_b],horse_attrib_2|level(11),wp(150)|wp_archery(500),knows_knight_npc|knows_horse_shoot_10|knows_archer_4|knows_swordman_2|knows_leadership_2|knows_weapon_master_1,0x000000088910318b5c6f972328324a6200000000001cd3310000000000000000],

["npc6","Firentis","Firentis",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_tabard,itm_nomad_boots,itm_bastard_sword_a,itm_lance,itm_tab_shield_heater_cav_a,itm_saddle_horse],def_attrib_multiplayer|level(8),wp(120),knows_knight_npc|knows_riding_2|knows_weapon_master_2|knows_power_strike_5|knows_physique_3|knows_trainer_1|knows_leadership_1|knows_magic_power_2,0x00000002050052036a1895d0748f3ca30000000000000f0b0000000000000000],
["npc7","Deshavi","Deshavi",tf_female_elf|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_ragged_outfit,itm_wrapping_boots, itm_hunting_bow, itm_arrows, itm_quarter_staff,itm_javelin,itm_fur_covered_shield],def_attrib_multiplayer|agi_12|int_10|level(4),wp(100),knows_tracker_npc|knows_stealth_3|knows_physique_2|knows_spotting_1|knows_pathfinding_1|knows_power_draw_4,0x00000001fc08400533a15297634d44f400000000001e02db0000000000000000],
["npc8","Matheld","Matheld",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_tribal_warrior_outfit,itm_hunter_boots, itm_valkyrie_helm_1,itm_nordhero_sword,itm_nord_throwing_spears,itm_tab_shield_round_c,itm_mail_shirt],def_attrib_multiplayer|level(8),wp(250),knows_stealth_5|knows_physique_5|knows_shield_3|knows_power_strike_5|knows_ironflesh_4|knows_reserved_18_10|knows_weapon_master_5|knows_reserved_17_3|knows_riding_4|knows_leadership_4|knows_tactics_1,0x00000001800000170000000000000e0000000000000000000000000000000000],


["npc9","Alayen","Alayen",tf_male_elf|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_tabard,itm_lorien_boots, itm_courtblades_ivory_1,itm_lorien_shield_c,itm_lorien_archer,itm_magic_lightning],def_attrib_multiplayer|level(3),wp(150)|wp_firearm(250),knows_riding_4|knows_leadership_1|knows_tactics_1|knows_physique_4|knows_shield_2|knows_power_strike_4|knows_ironflesh_4|knows_weapon_master_4|knows_magic_power_5|knows_magic_defence_1|knows_magic_defence_9|knows_necromancy_3|knows_magic_skill_5,0x000000018000100a38db6db6db6db6db00000000001db6eb0000000000000000],

["npc10","Bunduk","Bunduk",tf_male_elf|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_long_bow,itm_arrows,itm_mirkwood_knife,itm_mirkwood_spear_shield_c,itm_wizard_hood_2_2,itm_mirkwood_armor_a,itm_leather_gloves,itm_mirkwood_boots],horse_attrib_1|level(8),wp(200),knows_leadership_1|knows_trainer_2|knows_physique_5|knows_stealth_4|knows_power_strike_4|knows_ironflesh_3|knows_weapon_master_4|knows_power_draw_9|knows_magic_defence_4|knows_riding_2|knows_inventory_management_2|knows_magic_power_3,0x0000000fc00030023fc36db75b6ab6db00000000001d36db0000000000000000],

["npc11","Katrin","Katrin",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_leather_apron, itm_falchion, itm_wrapping_boots,itm_hunting_crossbow,itm_bolts,itm_nord_horse],str_8|agi_11|int_10|cha_10|level(3),wp(70)|wp_firearm(170),knows_merchant_npc|knows_weapon_master_1|knows_first_aid_3|knows_wound_treatment_2|knows_ironflesh_3|knows_inventory_management_5,0x00000003400030000000000000000e0000000000000000000000000000000000],

["npc12","Jeremus","Jeremus",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_pilgrim_hood,itm_pilgrim_disguise,itm_nomad_boots,itm_ebony_long_sword],def_attrib_multiplayer|int_13|cha_7|level(4),wp(100),knows_merchant_npc|knows_magic_4|knows_undead_master_4|knows_magic_power_4|knows_wound_treatment_7|knows_first_aid_3|knows_magic_skill_15,0x00000001800000110000000000000e0000000000000000000000000000000000],

["npc13","Nizar","Nizar",tf_female_elf|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_light_leather,itm_drow_leather_boots, itm_scimitar, itm_courser],horse_attrib_2|level(8),wp(200),knows_precise_shot_8|knows_weapon_master_5|knows_ironflesh_5|knows_physique_5|knows_power_strike_4|knows_riding_5|knows_shield_2|knows_stealth_8,0x00000004bf0475c85f4e9592de4e574c00000000001e369c0000000000000000],

["npc14","Lezalit","Lezalit",tf_dwarf|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_dwarf_fighting_axe, itm_haubergeon, itm_iron_greaves, itm_dwarf_mail_coif,itm_leather_gloves,itm_nobleman_outfit,itm_highlander_boot1, itm_dwarf_long_axe_2,itm_tab_shield_round_e],horse_attrib_3|level(8),wp(200),knows_knight_npc|knows_trainer_6|knows_physique_4|knows_shield_6|knows_power_strike_6|knows_ironflesh_8|knows_reserved_18_10|knows_weapon_master_6|knows_magic_defence_5,0x00000001a410259144d5d1d6eb55e96a00000000001db0db0000000000000000],


["npc15","Artimenner","Artimenner",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_rich_outfit,itm_nomad_boots, itm_sword_medieval_b_small,itm_wooden_staff_1,itm_magic_lightning],str_9|agi_9|int_12|cha_8|level(7),wp(80)|wp_firearm(180),knows_magic_power_4|knows_magic_defence_4|knows_necromancy_3|knows_warrior_npc|knows_tactics_2|knows_engineer_4|knows_trade_3|knows_tracking_1|knows_spotting_1|knows_magic_skill_5,0x0000000f2e1021862b4b9123594eab5300000000001d55360000000000000000],
["npc16","Klethi","Klethi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_peasant_dress,itm_nomad_boots, itm_dagger, itm_throwing_knives, itm_throwing_knives],str_9|agi_12|int_8|cha_7|level(2),wp(150),knows_knight_npc|knows_reserved_17_4|knows_assasin_3,0x000000034f0800090000000000000e0000000000000000000000000000000000],
["npc17","Balbanes","Balbanes",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_gothic_plate, itm_new_sallet, itm_hourglass_gauntlets, itm_iron_greaves2, itm_swiftness_sword, itm_charger, itm_gothic_lance, itm_vanguard_shield],str_30|agi_20|int_25|cha_30|level(50),wp(300),knows_warrior_npc|knows_riding_8|knows_leadership_10|knows_tactics_7|knows_trainer_5|knows_prisoner_management_4|knows_pathfinding_6|knows_magic_power_6|knows_physique_6|knows_shield_10|knows_power_strike_9|knows_ironflesh_15|knows_reserved_18_10|knows_weapon_master_8|knows_magic_defence_9,0x0000000f000015c836db6db6db6db6db00000000001db6db0000000000000000],


["npc18","Porziano","Porziano",tf_beastman|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_beastman_plate, itm_slaughter_axe, itm_gauntlets, itm_beast_leg, itm_arbalest_2, itm_empire_warhammer, itm_steel_bolts],str_20|agi_20|int_15|cha_25|level(40),wp(400),knight_skills_5|knows_stealth_8|knows_riding_7|knows_billman_7|knows_leadership_9|knows_tactics_6|knows_ironflesh_6|knows_prisoner_management_3,0x00000008400051c036db6db6db6db6db00000000001db6db0000000000000000],

["npc19","Boadicea, Battle Maiden","Boadicea",tf_female_elf|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_drow_elite_armor, itm_drow_hood_elite, itm_drow_elite_gloves, itm_drow_elite_boots, itm_soul_stealer, itm_drow_basilisk, itm_drow_lance, itm_drow_shield],str_21|agi_20|int_15|cha_25|level(42),wp(400),knight_skills_5|knows_riding_7|knows_assasin_5|knows_leadership_9|knows_tactics_6|knows_power_strike_6|knows_ironflesh_6|knows_pathfinding_5|knows_prisoner_management_5|knows_magic_defence_8,0x000000072500000536db6db6db6db6db00000000001db6db0000000000000000],

["npc20","Karn, the Silver Knight","Karn",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_plate_armor, itm_gauntlets, itm_iron_greaves, itm_great_lance,itm_sword_medieval_d_long, itm_dawnbreaker,itm_warhorse_teuton],horse_attrib_4|level(30),wp(250),knight_skills_3|knows_twohand_6|knows_magic_defence_10,0x00000001bf002008399d6db6db4996da00000000001d54d30000000000000000],
["npc21","Ostanes","Ostanes",tf_undead|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_mages_shade,itm_pilgrim_disguise, itm_leather_boots, itm_lich_staff_1,itm_magic_spirit_leech],str_16|agi_4|int_30|cha_30|level(50),wp(150)|wp_firearm(250),   knows_tracker_npc|knows_magic_power_10|knows_magic_defence_10|knows_magic_7|knows_necromancy_8|knows_undead_master_10|knows_wound_treatment_10|knows_first_aid_10|knows_riding_3|knows_magic_skill_15,0x0000000fc00060074f8ba62a9cd5d36d00000000001e36250000000000000000],
["npc22","Agustina, Battle Maiden","Agustina",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_half_plates, itm_milanese_gauntlets,itm_combed_morion, itm_steel_greaves, itm_sword_medieval_d_long, itm_charger, itm_hand_cannon, itm_cartridges_cannon_2, itm_cartridges_cannon],str_20|agi_20|int_15|cha_25|level(41),wp(200)|wp_firearm(250),knight_skills_5|knows_ironflesh_6|knows_trainer_4|knows_stealth_4|knows_undead_master_5|knows_horse_archery_5,0x00000001800000150000000000000e0000000000000000000000000000000000],
["npc23","Joan, War Maiden","Joan",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_knight_plate, itm_french_helm_closed, itm_hourglass_gauntlets, itm_iron_greaves2,itm_great_lance2, itm_skycutter, itm_charger_noble, itm_steel_shield],str_30|agi_20|int_25|cha_30|level(50),wp(300),knight_skills_5|knows_magic_defence_10|knows_weapon_master_10|knows_riding_8|knows_physique_6|knows_leadership_10|knows_tactics_7|knows_power_strike_9|knows_ironflesh_9|knows_trainer_5|knows_prisoner_management_4|knows_pathfinding_3|knows_necromancy_6,0x00000001800000110000000000000e0000000000000000000000000000000000],
["npc24","Xin Tian","Xin Tian",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_robe, itm_leather_boots, itm_sword_viking_2_small, itm_thunder_staff_1, itm_magic_poison_dummy],str_16|agi_4|int_30|cha_4|level(50),wp(100)|wp_firearm(250),   knows_magic_power_9|knows_magic_defence_9|knows_tracker_npc|knows_ironflesh_5|knows_physique_1|knows_tactics_10|knows_engineer_10|knows_riding_3|knows_magic_skill_10,0x00000003ff001388241f8dca2bc596d400000000001e36fa0000000000000000],
#["npc25","Bhagwandas","Bhagwandas",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_rich_outfit, itm_leather_boots,],str_4|agi_4|int_30|cha_4|level(50),wp(30),   knows_merchant_npc|knows_ironflesh_1|knows_physique_1|knows_trade_10|knows_looting_10|knows_riding_3,0x000000048000759437df6dc8e378b6db00000000001db6c30000000000000000],


#NPC system changes end



#governers olgrel rasevas                                                                        Horse          Bodywear                Footwear_in                     Footwear_out                    Armor                       Weapon                  Shield                  Headwaer
["kingdom_1_lord",  "King Harlaus",  "Harlaus",  tf_hero, 0,reserved,  fac_kingdom_1,[itm_armor_griffin,   itm_rich_outfit,        itm_blue_hose,                  itm_iron_greaves2,               itm_gondor_lord_armor, itm_gondor_gauntlets,    itm_swiftness_sword,itm_great_lance2,      itm_lordaeron,       itm_horned_great_helmet_2],          king_attrib,wp(450),king_skills|knows_trainer_5, 0x0000000f45041105241acd2b5a66a86900000000001e98310000000000000000,0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000],
["kingdom_2_lord",  "King Yaroglek",  "Yaroglek",  tf_hero, 0,reserved,  fac_kingdom_2,[    itm_courtly_outfit,      itm_leather_boots,              itm_mages_shade,itm_archlich_armor,itm_twilight_gloves, itm_leather_boots, itm_archlich_staff_1,itm_magic_spirit_leech],    king_attrib,wp(450),king_skills|knows_trainer_4|knows_magic_power_10|knows_magic_defence_10|knows_magic_7|knows_necromancy_8|knows_undead_master_10|knows_wound_treatment_10|knows_first_aid_10|knows_magic_skill_15, 0x0000000fc00060074f8ba62a9cd5d36d00000000001e36250000000000000000, vaegir_face_old_2],




["kingdom_3_lord",  "Sanjar Khan",  "Sanjar",  tf_hero|tf_vampire, 0,reserved,  fac_kingdom_3,[itm_black_dragon,   itm_shadow_robes,             itm_khergit_leather_boots,              itm_black_knight_foot,           itm_black_knight_plate,  itm_black_knight_hand,      itm_serpent_sword, itm_soul_stealer,              itm_dragon_shield,       itm_nazgul_hood_2],      king_attrib,wp(450),king_skills|knows_magic_power_9|knows_trainer_6, 0x0000000cee0051cc44be2d14d370c65c00000000001ed6df0000000000000000,khergit_face_old_2],
["kingdom_4_lord",  "King Ragnar",  "Ragnar",  tf_hero, 0,reserved,  fac_kingdom_4,[itm_undead_charger,    itm_nobleman_outfit,    itm_leather_boots,              itm_ebony_male_foot,                 itm_ebony_male_plate,  itm_ebony_male_hand,    itm_excalibur_2, itm_rhongomiant,          itm_vanguard_shield,    itm_black_knight_head],            king_attrib,wp(450),king_skills|knows_trainer_7, 0x0000000e8600215438f487091d51669c00000000001d932c0000000000000000, nord_face_older_2],


## CC
["kingdom_5_lord",  "King Graveth",  "Graveth",  tf_hero|tf_vampire, 0,reserved,  fac_kingdom_5,[itm_charger_noble,  itm_vampire_tunic,             itm_leather_boots,              itm_twilight_boots,   itm_archlich_armor,  itm_twilight_gloves, itm_ebony_blade,         itm_magic_spirit_leech,itm_archlich_staff_1, itm_crown],         king_attrib,wp(450),knows_magic_power_9|king_skills|knows_trainer_5, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000, rhodok_face_old_2],

["kingdom_6_lord",  "Sultan Hakim",  "Hakim",  tf_ogre|tf_hero, 0,reserved,  fac_kingdom_6,[itm_gorgon_2,     itm_ogre_armor,          itm_ogre_boots_02,       itm_ogre_barbar_helm,        itm_slaughter_axe,itm_nord_javelin,    itm_vanguard_shield],         king_attrib,wp(450),king_skills|knows_trainer_5, 0x0000000a4b103354189c71d6d386e8ac00000000001e24eb0000000000000000, rhodok_face_old_2],





["kingdom_7_lord",  "King Harlaus",  "Harlaus",  tf_hero, 0,reserved,  fac_kingdom_7,[itm_armor_demi_griffin,   itm_rich_outfit,        itm_blue_hose,                  itm_maximilian_greaves,               itm_maximilian_plate, itm_maximilian_gauntlets,    itm_gothic_lance, itm_angel_blade,      itm_lordaeron,       itm_new_sallet],          king_attrib,wp(450),king_skills|knows_trainer_5, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000,swadian_face_older_2],
["kingdom_8_lord",  "King Yaroglek",  "Yaroglek",  tf_hero, 0,reserved,  fac_kingdom_8,[itm_vaegir_charger,    itm_courtly_outfit,      itm_leather_boots,              itm_drow_plate_foot,              itm_dragon_heart_plate, itm_drow_plate_hand,      itm_blinding_sand,itm_serpent_sword,      itm_dragon_shield,      itm_litchina_helm],    king_attrib,wp(450),king_skills|knows_trainer_4, 0x0000000ec50001400a2269f919dee11700000000001cc57d0000000000000000, 0x0000000cbf00230c4deeffffffffffff00000000001efff90000000000000000],
["kingdom_9_lord",  "Sanjar Khan",  "Sanjar",  tf_hero, 0,reserved,  fac_kingdom_9,[itm_hell_nightmare,   itm_nomad_robe,             itm_leather_boots,              itm_demon_knight_leg,           itm_demon_knight_plate,  itm_demon_knight_hand,     itm_zamorak,itm_balor_sword,itm_magic_poison_dummy,              itm_demon_knight_shield,       itm_demon_knight_head],      king_attrib,wp(450),king_skills|knows_trainer_6, 0x000000050b003004072d51c293a9a70b00000000001dd6a90000000000000000,khergit_face_old_2],

["kingdom_10_lord",  "King Ragnar",  "Ragnar",  tf_hero, 0,reserved,  fac_kingdom_10,[itm_nord_warhorse,    itm_nobleman_outfit,    itm_leather_boots,              itm_plate_boots,                 itm_gothic_plate_2,  itm_gauntlets,    itm_throwing_gungnir,itm_frostfang, itm_dragon_shield,    itm_winged_great_helmet_ger],            king_attrib,wp(450),king_skills|knows_trainer_7, 0x00000006f00026863bbd61d693e0758300000000001c6ce60000000000000000, nord_face_older_2],
## CC





["kingdom_11_lord",  "King Graveth",  "Graveth",  tf_hero, 0,reserved,  fac_kingdom_11,[itm_charger_noble,  itm_tabard,             itm_leather_boots,              itm_iron_greaves2,   itm_reiksguard_armour,  itm_hourglass_gauntlets_ornate,         itm_espada_eslavona_b,         itm_tab_shield_heater_cav_b,itm_hand_cannon_4,         itm_cartridges_cannon_2,        itm_classichelm_plume],         king_attrib,wp(450),king_skills|knows_trainer_10, 0x0000000d6408358536d358b6898da8a300000000001cbd830000000000000000, rhodok_face_old_2],
["kingdom_12_lord",  "Sultan Hakim",  "Hakim",  tf_vampire|tf_hero, 0,reserved,  fac_kingdom_12,[itm_nord_warhorse,    itm_nobleman_outfit,    itm_leather_boots,              itm_twilight_boots,                 itm_dragonpriest_armor,  itm_caesar_mask    ,itm_magic_ice_ray, itm_dragonpriest_staff_1,    itm_aurora_blade],         king_attrib,wp(450),king_skills|knows_trainer_10|knows_magic_8|knows_magic_defence_8, 0x0000000a4b103354189c71d6d386e8ac00000000001e24eb0000000000000000, rhodok_face_old_2],


["kingdom_13_lord",  "King Harlaus",  "Harlaus",  tf_male_elf|tf_hero, 0,reserved,  fac_kingdom_13,[ itm_unicorn,  itm_mirkwood_armor_a,        itm_mirkwood_boots,                  itm_glass_foot,               itm_glass_female_plate, itm_glass_hand,    itm_trgba,itm_woodelf_arrows_poison_2,itm_woodelf_mutil_arrows,      itm_elven_bow,       itm_glass_head],          king_attrib,wp(450),king_skills|knows_trainer_6|knows_magic_skill_10|knows_power_draw_15|knows_archer_comman_10|knows_horse_archery_10|knows_offense_10|knows_pathfinding_10|knows_tenacity_10, 0x0000000d000410104495b1a68944b70b00000000001eb6ab0000000000000000,swadian_face_older_2],


["kingdom_14_lord",  "King Yaroglek",  "Yaroglek",  tf_female_elf|tf_hero, 0,reserved,  fac_kingdom_14,[itm_drow_basilisk_2,    itm_courtly_outfit,      itm_drow_leather_boots,              itm_ebony_male_foot,              itm_black_hole_plate, itm_ebony_male_hand,      itm_black_hole_sword,itm_magic_lightning,      itm_drow_staff_3,      itm_ebony_male_head],    king_attrib,wp(450),king_skills|knows_trainer_4|knows_magic_defence_10|knows_necromancy_5|knows_magic_power_8|knows_magic_skill_10|knows_paragon_knight_10|knows_offense_10|knows_magic_skill_10, 0x000000048000538416dbccc88561fcfb00000000001ec6330000000000000000, vaegir_face_old_2],





   



## CC

#    Imbrea   Belinda Ruby Qaelmas Rose    Willow
#  Alin  Ganzo            Zelka Rabugti
#  Qlurzach Ruhbus Givea_alsev  Belanz        Bendina
# Dunga        Agatha     Dibus Crahask

#                                                                               Horse                   Bodywear                Armor                               Footwear_in                 Footwear_out                        Headwear                    Weapon               Shield
#Swadian civilian clothes: itm_courtly_outfit itm_gambeson itm_blue_gambeson itm_red_gambeson itm_nobleman_outfit itm_rich_outfit itm_short_tunic itm_tabard
#Older knights with higher skills moved to top
["knight_1_1", "Count Klargus", "Klargus", tf_hero, 0, reserved,  fac_kingdom_1, [itm_armor_demi_griffin,      itm_courtly_outfit,      itm_knight_plate_4,   itm_woolen_hose, itm_iron_greaves2,       itm_winged_great_helmet_blue,           itm_gondor_citadel_sword,itm_great_lance2,  itm_gondor_gauntlets,         itm_gondor_shield_e],   knight_attrib_5,wp(300),knight_skills_5|knows_trainer_1|knows_trainer_3, 0x0000000c3e08601414ab4dc6e39296b200000000001e231b0000000000000000, swadian_face_older_2],

["knight_1_2", "Count Delinard", "Delinard", tf_hero, 0, reserved,  fac_kingdom_1, [           itm_red_gambeson,      itm_empire_priest,               itm_woolen_hose,            itm_iron_greaves,                    itm_french_helm_3,  itm_gondor_gauntlets,        itm_war_clerics_warhammer_cast_2,itm_magic_earth_blood    ],       knight_attrib_5,wp(400),knight_skills_5|knows_magic_defence_5|knows_magic_power_4, 0x0000000c0f08000458739a9a1476199800000000001fb6f10000000000000000, swadian_face_young_2],

["knight_1_3", "Count Haringoth", "Haringoth", tf_hero, 0, reserved,  fac_kingdom_1, [itm_armor_griffin,          itm_nobleman_outfit,     itm_white_twiligh_armor,                 itm_leather_boots,          itm_steel_greaves,        itm_black_helmet2, itm_gondor_gauntlets, itm_mjolnir, itm_great_lance2,itm_gondor_shield_e,  ],  knight_attrib_5,wp(300),knight_skills_5|knows_trainer_3, 0x0000000c0610351048e325361d7236cd00000000001d532a0000000000000000, swadian_face_young_2],

["knight_1_4", "Count Clais", "Clais", tf_hero, 0, reserved,  fac_kingdom_1, [itm_armor_demi_griffin,      itm_short_tunic,       itm_knight_plate_3,           itm_leather_boots,          itm_iron_greaves2,                   itm_french_helm_3, itm_gondor_gauntlets,       itm_gondor_citadel_sword,  itm_toumingdun],    knight_attrib_5,wp(300),knight_skills_5|knows_trainer_4, 0x0000000c03104490280a8cb2a24196ab00000000001eb4dc0000000000000000, swadian_face_older_2],
["knight_1_5", "Count Deglan", "Deglan", tf_hero, 0, reserved,  fac_kingdom_1, [itm_charger_black,           itm_rich_outfit,        itm_black_armor2,itm_woolen_hose, itm_black_greaves2, itm_black_helmet2, itm_hourglass_gauntlets_ornate,         itm_bastard_sword_c,itm_great_lance_dark,itm_german_poleaxe_4,    itm_tab_shield_heater_cav_b],      knight_attrib_4,wp(400),knight_skills_4|knows_trainer_6|knows_weapon_master_4|knows_stealth_8|knows_magic_defence_10, 0x0000000c330855054aa9aa431a48d74600000000001ed5240000000000000000, swadian_face_older_2],

["knight_1_6", "Count Tredian", "Tredian", tf_hero, 0, reserved,  fac_kingdom_1, [            itm_tabard,      itm_gondor_fountain_armor,               itm_leather_boots,          itm_iron_greaves2,                      itm_french_helm_2, itm_gondor_gauntlets, itm_bastard_sword_d_fire,  itm_lordaeron], knight_attrib_5,wp(350),knight_skills_4|knows_trainer_4|knows_weapon_master_10|knows_stealth_10, 0x0000000c2a0805442b2c6cc98c8dbaac00000000001d389b0000000000000000, swadian_face_older_2],

["knight_1_7", "Count Grainwad", "Grainwad", tf_hero, 0, reserved,  fac_kingdom_1, [            itm_tabard,      itm_dawnbreaker_armor,               itm_leather_boots,          itm_amade_bronze_greaves,                      itm_black_helmet_2, itm_amade_bronze_gauntlets, itm_dawnbreaker_1,itm_angle_sword_2, itm_angle_sword_2], knight_attrib_5,wp(350),knight_skills_4|knows_trainer_4|knows_thrown_7|knows_weapon_master_5|knows_magic_power_6, 0x0000000c380c30c2392a8e5322a5392c00000000001e5c620000000000000000, swadian_face_young_2],

["knight_1_8", "Count Ryis", "Ryis", tf_hero, 0, reserved,  fac_kingdom_1, [          itm_nobleman_outfit,     itm_elf_plate,                 itm_leather_boots,          itm_elf_foot,        itm_winged_great_helmet_teu,  itm_elf_hand,itm_sabre_hithlain, itm_lorien_bow_2, itm_woodelf_mutil_arrows,itm_woodelf_arrows_freezing],  knight_attrib_4,wp(300),knight_skills_4, 0x0000000c3f10000532d45203954e192200000000001e47630000000000000000, swadian_face_older_2],

["knight_1_9", "Count Plais", "Plais", tf_hero, 0, reserved,  fac_kingdom_1, [          itm_nobleman_outfit,     itm_empire_priest,                 itm_leather_boots,          itm_iron_greaves,        itm_bishop_mitre,  itm_gondor_gauntlets,itm_bishop_staff_2, itm_magic_ice_ray],  knight_attrib_4,wp(300),knight_skills_4, 0x0000000c3f10000532d45203954e192200000000001e47630000000000000000, swadian_face_older_2],
["knight_1_10", "Count Mirchaud", "Mirchaud", tf_hero, 0, reserved,  fac_kingdom_1, [itm_charger_teuton,           itm_gambeson,        itm_swan_milanese_plate,                   itm_woolen_hose,            itm_iron_greaves,                   itm_winged_great_helmet_teu,    itm_gondor_gauntlets,    itm_amroth_sword_c,itm_gothic_lance,        itm_dol_shield_b],   knight_attrib_3,wp(300),knight_skills_3, 0x0000000c1e001500589dae4094aa291c00000000001e37a80000000000000000, swadian_face_older_2],
["knight_1_11", "Count Stamar", "Stamar", tf_hero, 0, reserved,  fac_kingdom_1, [itm_charger_teuton,           itm_red_gambeson,      itm_swan_milanese_plate,               itm_woolen_hose,            itm_iron_greaves,                    itm_winged_great_helmet_teu,   itm_gondor_gauntlets,       itm_amroth_sword_c,itm_gothic_lance,    itm_dol_shield_b],       knight_attrib_3,wp(300),knight_skills_3, 0x000000095108144657a1ba3ad456e8cb00000000001e325a0000000000000000, swadian_face_older_2],
["knight_1_12", "Count Meltor", "Meltor", tf_hero, 0, reserved,  fac_kingdom_1, [itm_charger_teuton,      itm_rich_outfit,        itm_swan_milanese_plate,                    itm_woolen_hose,            itm_iron_greaves,                      itm_winged_great_helmet_teu,   itm_gondor_gauntlets,         itm_amroth_sword_c,itm_gothic_lance,   itm_dol_shield_b],    knight_attrib_3,wp(300),knight_skills_3, 0x0000000c010c42c14d9d6918bdb336e200000000001dd6a30000000000000000, swadian_face_older_2],



["knight_1_13", "Count Beranz", "Beranz", tf_hero, 0, reserved,  fac_kingdom_1, [itm_armor_demi_griffin,      itm_ragged_outfit,      itm_dol_very_heavy_mail,           itm_woolen_hose,            itm_iron_greaves,                itm_swan_knight_helm,   itm_gondor_gauntlets,         itm_amroth_sword_b,  itm_war_clerics_warhammer_2,     itm_dol_shield_a],   knight_attrib_2,wp(300),knight_skills_2, 0x0000000c150045c6365d8565932a8d6400000000001ec6940000000000000000, swadian_face_older_2],
["knight_1_14", "Count Rafard", "Rafard", tf_hero, 0, reserved,  fac_kingdom_1, [itm_warhorse_teuton,      itm_short_tunic,       itm_dol_very_heavy_mail,           itm_leather_boots,          itm_iron_greaves,                   itm_swan_knight_helm,  itm_gondor_gauntlets,     itm_amroth_sword_c, itm_gondor_lance,   itm_dol_shield_a],    knight_attrib_2,wp(500),knight_skills_3|knows_trainer_6, 0x0000000c0f0c320627627238dcd6599400000000001c573d0000000000000000, swadian_face_older_2],


["knight_1_15", "Count Regas", "Regas", tf_hero, 0, reserved,  fac_kingdom_1, [itm_armor_demi_griffin,            itm_rich_outfit,        itm_knight_plate_4,                   itm_woolen_hose,            itm_iron_greaves2,                   itm_french_helm_3,   itm_gondor_gauntlets,       itm_gondor_citadel_sword, itm_great_lance_dark,  itm_gondor_shield_d],      knight_attrib_4,wp(300),knight_skills_2, 0x0000000cb700210214ce89db276aa2f400000000001d36730000000000000000, swadian_face_young_2],

["knight_1_16", "Count Devlian", "Devlian", tf_hero, 0, reserved,  fac_kingdom_1, [itm_warhorse_france,      itm_courtly_outfit,      itm_gon_knight,                     itm_woolen_hose,            itm_iron_greaves2,                itm_gondor_guard_helm,   itm_gondor_gauntlets,         itm_gondor_ranger_sword,itm_bec_de_corbin_a,    itm_gondor_lance,       itm_gondor_shield_b],   knight_attrib_1,wp(300),knight_skills_2, 0x00000008200012033d9b6d4a92ada53500000000001cc1180000000000000000, swadian_face_young_2],


["knight_1_17", "Count Rafarch", "Rafarch", tf_hero, 0, reserved,  fac_kingdom_1, [itm_warhorse_teuton,      itm_gambeson,     itm_dol_very_heavy_mail,                 itm_blue_hose,              itm_iron_greaves2,                      itm_swan_knight_helm,   itm_gondor_gauntlets,    itm_amroth_sword_b, itm_gondor_lance,  itm_tab_shield_heater_cav_b],    knight_attrib_2,wp(400),knows_stealth_3|knows_riding_5|knows_ironflesh_6|knows_power_strike_7|knows_physique_5|knows_tactics_2|knows_prisoner_management_1|knows_leadership_5|knows_pathfinding_3|knows_trade_8|knows_weapon_master_5|knows_magic_defence_2|knows_shield_4, 0x0000000c4d0840d24a9b2ab4ac2a332400000000001d34db0000000000000000, swadian_face_young_2],

["knight_1_18", "Count Rochabarth", "Rochabarth", tf_hero, 0, reserved,  fac_kingdom_1, [itm_armor_demi_griffin,           itm_gambeson,        itm_plate_armor_3,                   itm_woolen_hose,            itm_iron_greaves2,                   itm_french_helm_3,   itm_gondor_gauntlets,     itm_gondor_citadel_sword,itm_german_poleaxe_4,itm_gothic_lance,        itm_gondor_shield_d],   knight_attrib_3,wp(300),knight_skills_1, 0x0000000c370c1194546469ca6c4e450e00000000001ebac40000000000000000, swadian_face_young_2],

["knight_1_19", "Count Despin", "Despin", tf_hero, 0, reserved,  fac_kingdom_1, [      itm_rich_outfit,        itm_plate_armor_3,                    itm_woolen_hose,            itm_iron_greaves2,                      itm_gondor_guard_helm, itm_gondor_gauntlets,           itm_amroth_sword_b,  itm_hurricane_bow, itm_stahlrim_mutil_arrow, itm_woodelf_arrows_freezing],    knight_attrib_1,wp(300),knows_stealth_9|knows_riding_5|knows_ironflesh_13|knows_power_strike_13|knows_physique_13|knows_tactics_1|knows_prisoner_management_1|knows_leadership_5|knows_pathfinding_3|knows_trade_8|knows_weapon_master_2|knows_magic_defence_9|knows_magic_skill_5|knows_magic_power_5|knows_power_draw_10|knows_shield_5, 0x0000000c0c1064864ba34e2ae291992b00000000001da8720000000000000000, swadian_face_young_2],

["knight_1_20", "Count Montewar", "Montewar", tf_hero, 0, reserved,  fac_kingdom_1, [itm_warhorse_teuton,      itm_ragged_outfit,      itm_dol_very_heavy_mail,           itm_woolen_hose,            itm_iron_greaves2,                itm_swan_knight_helm, itm_gondor_gauntlets,           itm_amroth_sword_b,   itm_german_poleaxe_4,   itm_tab_shield_heater_cav_a],   knight_attrib_2,wp(300),knows_stealth_3|knows_riding_5|knows_ironflesh_6|knows_power_strike_7|knows_physique_5|knows_tactics_2|knows_prisoner_management_1|knows_leadership_5|knows_pathfinding_3|knows_trade_8|knows_weapon_master_5|knows_magic_defence_2|knows_shield_4, 0x0000000c0a08038736db74c6a396a8e500000000001db8eb0000000000000000, swadian_face_young_2],





#["knight_2_2", "Boyar Naldera", "Naldera", tf_hero, 0, reserved,  fac_kingdom_2, [itm_vaegir_charger,      itm_rich_outfit,        itm_polish_hussar_armor_wing,               itm_woolen_hose,            itm_iron_greaves,                   itm_polish_husar_helmet,  itm_lamellar_gauntlets,      itm_hussar_lance_2,  itm_scimitar_sulatn,   itm_tab_shield_kite_cav_a],    knight_attrib_2,wp(300),knight_skills_2, 0x0000000683085618269cad4ac5c1a4d800000000001edc6d0000000000000000, vaegir_face_old_2],
#["knight_2_3", "Boyar Meriga", "Meriga", tf_hero, 0, reserved,  fac_kingdom_2, [itm_vaegir_charger,            itm_short_tunic,        itm_polish_hussar_armor_wing,                   itm_woolen_hose,            itm_iron_greaves,                   itm_polish_husar_helmet, itm_lamellar_gauntlets,           itm_hussar_lance_2, itm_scimitar_sulatn,           itm_tab_shield_kite_cav_b],     knight_attrib_3,wp(300),knight_skills_3, 0x00000007df08240e06016db71a81f6d500000000001d99330000000000000000, vaegir_face_older_2],
#["knight_2_4", "Boyar Khavel", "Khavel", tf_hero, 0, reserved,  fac_kingdom_2, [itm_vaegir_charger,      itm_courtly_outfit,     itm_polish_hussar_armor_wing,               itm_rus_shoes,          itm_iron_greaves,                      itm_polish_husar_helmet, itm_lamellar_gauntlets,         itm_scimitar_long,   itm_tab_shield_kite_cav_b],    knight_attrib_4,wp(300),knight_skills_4, 0x00000006d010149937332656738ddcdb00000000001f49530000000000000000, vaegir_face_older_2],
#["knight_2_5", "Boyar Doru", "Doru", tf_hero, 0, reserved,  fac_kingdom_2, [itm_vaegir_charger,            itm_rich_outfit,        itm_polish_hussar_armor_wing,                     itm_rus_shoes,          itm_iron_greaves,                   itm_polish_husar_helmet, itm_scale_gauntlets,   itm_scimitar_long,   itm_tab_shield_kite_d],       knight_attrib_5,wp(300),knight_skills_5, 0x0000000abd00010f47348c46e949d69600000000001c36e20000000000000000, vaegir_face_older_2],
#["knight_2_6", "Boyar Belgaru", "Belgaru", tf_hero, 0, reserved,  fac_kingdom_2, [itm_vaegir_charger,      itm_nomad_vest,      itm_polish_hussar_armor_wing,                   itm_woolen_hose,            itm_iron_greaves,                   itm_polish_husar_helmet,  itm_lamellar_gauntlets,          itm_sword_viking_3,           itm_tab_shield_kite_c],   knight_attrib_1,wp(300),knight_skills_1|knows_trainer_3, 0x00000007ca0835503c6156105c47424c00000000001dc5130000000000000000, vaegir_face_middle_2],
#["knight_2_7", "Boyar Ralcha", "Ralcha", tf_hero, 0, reserved,  fac_kingdom_2, [itm_vaegir_charger,      itm_leather_jacket,     itm_polish_hussar_armor_wing,                   itm_rus_shoes,          itm_iron_greaves,                      itm_polish_husar_helmet,  itm_lamellar_gauntlets,          itm_hussar_lance_2,itm_scimitar_long, itm_scimitar_sulatn,    itm_tab_shield_kite_cav_a],     knight_attrib_2,wp(300),knight_skills_2|knows_trainer_4, 0x00000006ab08361b4c92b1d31b4d2a6c00000000001cd99d0000000000000000, vaegir_face_old_2],
#["knight_2_8", "Boyar Vlan", "Vlan", tf_hero, 0, reserved,  fac_kingdom_2, [itm_vaegir_charger,            itm_nomad_robe,             itm_polish_hussar_armor_wing,                     itm_woolen_hose,            itm_iron_greaves,                   itm_polish_husar_helmet, itm_lamellar_gauntlets,       itm_hussar_lance_2,itm_scimitar_long,    itm_tab_shield_kite_d],    knight_attrib_3,wp(300),knight_skills_3|knows_trainer_5, 0x000000090000035536fa766753a5f04f00000000001d02150000000000000000, vaegir_face_older_2],
#["knight_2_9", "Boyar Mleza", "Mleza", tf_hero, 0, reserved,  fac_kingdom_2, [itm_vaegir_charger,      itm_rich_outfit,        itm_polish_hussar_armor_wing,                     itm_rus_shoes,          itm_iron_greaves,                   itm_polish_husar_helmet,  itm_lamellar_gauntlets,        itm_hussar_lance_2, itm_scimitar_sulatn,   itm_tab_shield_kite_d],    knight_attrib_4,wp(300),knight_skills_4, 0x00000002ff1005491ca24e5dde41571f00000000001c97f80000000000000000, vaegir_face_older_2],
#["knight_2_10", "Boyar Nelag", "Nelag", tf_hero, 0, reserved,  fac_kingdom_2, [itm_vaegir_charger,          itm_kuyak,        itm_polish_hussar_armor_wing,               itm_woolen_hose,            itm_iron_greaves,                      itm_polish_husar_helmet,  itm_scale_gauntlets,      itm_morningstar,itm_hussar_lance_2,   itm_tab_shield_kite_cav_b],      knight_attrib_5,wp(300),knight_skills_5|knows_trainer_6, 0x00000004e91003ce336565b4e7576ca600000000001ea4f30000000000000000, vaegir_face_older_2],
#["knight_2_11", "Boyar Crahask", "Crahask", tf_hero, 0, reserved,  fac_kingdom_2, [itm_vaegir_charger,      itm_leather_jacket,     itm_polish_hussar_armor_wing,                   itm_nomad_boots,            itm_iron_greaves,        itm_polish_husar_helmet, itm_scale_gauntlets,           itm_sword_viking_3,itm_hussar_lance_2,           itm_tab_shield_kite_cav_a],    knight_attrib_1,wp(300),knight_skills_1, 0x00000004d900450e450dc9beda6542d600000000001d86a30000000000000000, vaegir_face_middle_2],
#["knight_2_12", "Boyar Bracha", "Bracha", tf_hero, 0, reserved,  fac_kingdom_2, [itm_vaegir_charger,      itm_rich_outfit,        itm_polish_hussar_armor_wing,               itm_woolen_hose,            itm_iron_greaves,                   itm_polish_husar_helmet,  itm_lamellar_gauntlets,      itm_hussar_lance_2, itm_scimitar_sulatn,    itm_tab_shield_kite_cav_a],    knight_attrib_2,wp(300),knight_skills_2, 0x00000002c51024865d7a765fdfe07ad700000000001c36a80000000000000000, vaegir_face_old_2],
#["knight_2_13", "Boyar Druli", "Druli", tf_hero, 0, reserved,  fac_kingdom_2, [itm_vaegir_charger,            itm_short_tunic,        itm_polish_hussar_armor_wing,                   itm_woolen_hose,            itm_iron_greaves,                   itm_polish_husar_helmet,  itm_lamellar_gauntlets,          itm_hussar_lance_2, itm_scimitar_sulatn,           itm_tab_shield_kite_cav_b],     knight_attrib_3,wp(300),knight_skills_3, 0x00000006f904349768826dac9ca9dc2100000000001dd89e0000000000000000, vaegir_face_older_2],
#["knight_2_14", "Boyar Marmun", "Marmun", tf_hero, 0, reserved,  fac_kingdom_2, [itm_vaegir_charger,      itm_courtly_outfit,     itm_polish_hussar_armor_wing,               itm_rus_shoes,          itm_iron_greaves,                      itm_polish_husar_helmet,  itm_lamellar_gauntlets,        itm_hussar_lance_2, itm_scimitar_long,  itm_tab_shield_kite_cav_b],    knight_attrib_4,wp(300),knight_skills_4|knows_trainer_6, 0x00000003cb0843d7575b6a2920b1f92500000000001fbafb0000000000000000, vaegir_face_older_2],
#["knight_2_15", "Boyar Gastya", "Gastya", tf_hero, 0, reserved,  fac_kingdom_2, [itm_vaegir_charger,            itm_rich_outfit,        itm_polish_hussar_armor_wing,                     itm_rus_shoes,          itm_iron_greaves,                   itm_polish_husar_helmet, itm_lamellar_gauntlets,   itm_scimitar_long,  itm_hussar_lance_2, itm_tab_shield_kite_cav_b],       knight_attrib_5,wp(300),knight_skills_5, 0x0000000ec010035c09334c2bd46150cc00000000001d02bc0000000000000000, vaegir_face_older_2],
#["knight_2_16", "Boyar Harish", "Harish", tf_hero, 0, reserved,  fac_kingdom_2, [itm_vaegir_charger,      itm_nomad_vest,      itm_polish_hussar_armor_wing,                   itm_woolen_hose,            itm_iron_greaves,                   itm_polish_husar_helmet,  itm_lamellar_gauntlets,          itm_hussar_lance_2, itm_scimitar_sulatn,           itm_tab_shield_kite_c],   knight_attrib_1,wp(300),knight_skills_1, 0x0000000cc000138a26f36ded0d20389d00000000001d26230000000000000000, vaegir_face_middle_2],
#["knight_2_17", "Boyar Taisa", "Taisa", tf_hero, 0, reserved,  fac_kingdom_2, [itm_vaegir_charger,      itm_leather_jacket,     itm_polish_hussar_armor_wing,                   itm_rus_shoes,          itm_iron_greaves,                      itm_polish_husar_helmet,   itm_scale_gauntlets,         itm_hussar_lance_2, itm_scimitar_sulatn,    itm_tab_shield_kite_cav_a],     knight_attrib_2,wp(300),knight_skills_2, 0x0000000f1b00354d4ae23238de8a590d00000000001ea1240000000000000000, vaegir_face_old_2],
#["knight_2_18", "Boyar Valishin", "Valishin", tf_hero, 0, reserved,  fac_kingdom_2, [itm_vaegir_charger,            itm_nomad_robe,             itm_polish_hussar_armor_wing,                     itm_woolen_hose,            itm_iron_greaves,                   itm_polish_husar_helmet,  itm_lamellar_gauntlets,      itm_hussar_lance_2, itm_scimitar_sulatn,    itm_tab_shield_kite_cav_a],    knight_attrib_3,wp(300),knight_skills_3, 0x0000000f4000041536db6db6db6db6db00000000001db6db0000000000000000, vaegir_face_older_2],
#["knight_2_19", "Boyar Rudin", "Rudin", tf_hero, 0, reserved,  fac_kingdom_2, [itm_vaegir_charger,      itm_rich_outfit,        itm_polish_hussar_armor_wing,                     itm_rus_shoes,          itm_iron_greaves,                   itm_polish_husar_helmet, itm_scale_gauntlets,         itm_morningstar,  itm_hussar_lance_2, itm_tab_shield_kite_d],    knight_attrib_4,wp(300),knight_skills_4|knows_trainer_4, 0x0000000252103690166b90ad9da8b6ab00000000001cd2ac0000000000000000, vaegir_face_older_2],
#["knight_2_20", "Boyar Kumipa", "Kumipa", tf_hero, 0, reserved,  fac_kingdom_2, [itm_vaegir_charger,          itm_kuyak,        itm_polish_hussar_armor_wing,               itm_woolen_hose,            itm_iron_greaves,                      itm_polish_husar_helmet,  itm_lamellar_gauntlets,      itm_hussar_lance_2, itm_scimitar_sulatn,   itm_tab_shield_kite_cav_b],      knight_attrib_5,wp(300),knight_skills_5|knows_trainer_5, 0x0000000897043510366cb5c5536d78da00000000001dc4a90000000000000000, vaegir_face_older_2],

#khergit civilian clothes: itm_leather_vest, itm_nomad_vest, itm_nomad_robe, itm_lamellar_vest,itm_tribal_warrior_outfit
["knight_3_1", "Alagur Noyan", "Alagur", tf_hero|tf_vampire, 0, reserved,  fac_kingdom_3, [itm_nightmare, itm_nazgul_robes,itm_khergit_leather_boots,  itm_black_knight_foot, itm_nazgul_hood_1, itm_black_knight_hand, itm_leather_gloves,  itm_ebony_arming_sword, itm_drow_shield_rider ],  knight_attrib_4,wp(300),knight_skills_5|knows_trainer_3|knows_trainer_6, 0x000000043000318b54b246b7094dc39c00000000001d31270000000000000000, khergit_face_middle_2],
["knight_3_2", "Tonju Noyan",  "Tonju", tf_hero|tf_vampire, 0, reserved,  fac_kingdom_3, [itm_nightmare, itm_nazgul_robes, itm_khergit_leather_boots,  itm_black_knight_foot, itm_nazgul_hood_1, itm_black_knight_hand,  itm_drow_shield_rider,  itm_ebony_axe], knight_attrib_4,wp(300),knight_skills_5|knows_trainer_6, 0x0000000c280461004929b334ad632aa200000000001e05120000000000000000, khergit_face_old_2],
["knight_3_3", "Belir Noyan",  "Belir", tf_hero|tf_vampire, 0, reserved,  fac_kingdom_3, [itm_nightmare_armor, itm_nazgul_robes, itm_black_knight_plate,itm_khergit_leather_boots,  itm_black_knight_foot,  itm_nazgul_hood_2, itm_black_knight_hand, itm_ebony_great_sword, itm_ebony_arming_sword,  itm_drow_shield_rider,  ],  knight_attrib_4,wp(300),knight_skills_5|knows_trainer_5|knows_magic_power_4|knows_necromancy_4, 0x0000000e880062c53b0a6e4994ae272a00000000001db4e10000000000000000, khergit_face_older_2],
["knight_3_4", "Asugan Noyan", "Asugan", tf_hero, 0, reserved,  fac_kingdom_3, [itm_khergit_charger, itm_rhun_armor_k,  itm_khergit_elite_armor, itm_hide_boots,  itm_rhun_greaves,   itm_rhun_helm_n, itm_lamellar_gauntlets, itm_sword_khergit_7, itm_khergit_lance,  itm_dec_steel_shield],  knight_attrib_4,wp(300),knight_skills_4|knows_power_draw_4, 0x0000000c23085386391b5ac72a96d95c00000000001e37230000000000000000, khergit_face_older_2],
["knight_3_5", "Brula Noyan",  "Brula", tf_orc|tf_hero, 0, reserved,  fac_kingdom_3, 
 [itm_warboar,  itm_orcbigboss_armour,  itm_orc_heavy_boots, itm_orc_heavy_helm2, itm_chaos_axe, itm_steel_shield],  
 knight_attrib_5,wp(360),knight_skills_5|knows_weapon_master_4, 
 0x000000052900200F16E1ADC71C85A73B00000000001D199D0000000000000000, khergit_face_older_2],

 ["knight_3_6", "Imirza Noyan", "Imirza", tf_orc|tf_hero, 0, reserved,  fac_kingdom_3, 
  [itm_orcboss_armour2, itm_orc_heavy_helm2, itm_tab_shield_round_e, itm_orc_heavy_boots, itm_choppa5, itm_warboar], 
   knight_attrib_1,wp(300),knight_skills_1|knows_power_draw_4, 
  0x00000001AB00000001E325A723CA653500000000000000000000000000000000, khergit_face_middle_2],

["knight_3_7", "Urumuda Noyan","Urumuda", tf_orc|tf_hero, 0, reserved,  fac_kingdom_3, 
  [itm_orcboss_armour, itm_orc_heavy_helm2, itm_tab_shield_round_e, itm_orc_heavy_boots, itm_choppa4, itm_warboar], 
  knight_attrib_2,wp(300),knight_skills_2, 
  0x00000001BC00000001ED64B28D96566D00000000000000000000000000000000, khergit_face_old_2],

["knight_3_8", "Kramuk Noyan", "Kramuk", tf_troll|tf_hero, 0, reserved,  fac_kingdom_3,  
 [itm_olog_body_2, itm_olog_head_helm_1, itm_tab_shield_round_e, itm_olog_hands,itm_olog_feet_boots, itm_giant_hammer], 
 str_93|knight_attrib_5,wp(400),knight_skills_3|knows_reserved_17_4, 
 0x00000001BC00000001ED64B28D96566D00000000000000000000000000000000, khergit_face_older_2],

["knight_3_9", "Chaurka Noyan","Chaurka", tf_goblin|tf_hero, 0, reserved,  fac_kingdom_3, 
 [itm_org_armour_5, itm_org_helmet_3, itm_tab_shield_round_e, itm_org_boot_2, itm_org_lance,itm_org_axe4,itm_spider], 
 knight_attrib_4,wp(300),knight_skills_4, 
 0x000000019200000001DCDA68AD70BC9C00000000000000000000000000000000, khergit_face_older_2],


["knight_3_10", "Sebula Noyan","Sebula", tf_orc|tf_hero, 0, reserved,  fac_kingdom_3, 
  [itm_blackorcboss_armour, itm_orc_heavy_helm2, itm_tab_shield_round_e, itm_orc_heavy_boots,itm_heavy_throwing_axes,itm_choppa6], 
  knight_attrib_5,wp(300),knight_skills_5|knows_trainer_6|knows_reserved_17_5, 
  0x0000000a3b00418c5b36c686d920a76100000000001c436f0000000000000000, khergit_face_older_2],
["knight_3_11", "Tulug Noyan", "Tulug", tf_hero|tf_vampire, 0, reserved,  fac_kingdom_3, [itm_nightmare, itm_nazgul_robes, itm_khergit_leather_boots, itm_black_knight_foot,  itm_nazgul_hood_1,  itm_black_knight_hand, itm_ebony_long_sword,  itm_drow_shield_rider,  ],  knight_attrib_4,wp(300),knight_skills_5|knows_trainer_6, 0x00000007d100534b44962d14d370c65c00000000001ed6df0000000000000000, khergit_face_middle_2],
["knight_3_12", "Nasugei Noyan", "Nasugei", tf_hero|tf_vampire, 0, reserved,  fac_kingdom_3, [itm_nightmare, itm_nazgul_robes, itm_khergit_leather_boots, itm_black_knight_foot,  itm_nazgul_hood_1,  itm_black_knight_hand, itm_ebony_long_mace,  itm_drow_shield_rider], knight_attrib_4,wp(300),knight_skills_5|knows_trainer_6, 0x0000000bf400610c5b33d3c9258edb6c00000000001eb96d0000000000000000, khergit_face_old_2],
["knight_3_13", "Urubay Noyan","Urubay", tf_hero, 0, reserved,  fac_kingdom_3, [itm_khergit_charger, itm_nomad_robe,  itm_rhun_armor_p, itm_nomad_boots, itm_rhun_greaves,  itm_rhun_helm_n, itm_lamellar_gauntlets, itm_sword_khergit_4,  itm_dec_steel_shield, itm_khergit_bow, itm_flat_headed_arrows],  knight_attrib_3,wp(300),knight_skills_3|knows_trainer_3|knows_power_draw_4, 0x0000000bfd0061c65b6eb33b25d2591d00000000001f58eb0000000000000000, khergit_face_older_2],
["knight_3_14", "Hugu Noyan",  "Hugu", tf_hero, 0, reserved,  fac_kingdom_3, [itm_khergit_charger,  itm_rhun_armor_k, itm_hide_boots, itm_rhun_greaves, itm_rhun_helm_n, itm_lamellar_gauntlets, itm_sword_khergit_7,  itm_dec_steel_shield, itm_khergit_long_bow, itm_demon_arrow],  knight_attrib_4,wp(300),knight_skills_4|knows_trainer_6|knows_power_draw_8, 0x0000000b6900514144be2d14d370c65c00000000001ed6df0000000000000000, khergit_face_older_2],
["knight_3_15", "Tansugai Noyan", "Tansugai", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse_steppe,   itm_ragged_outfit, itm_rhun_armor_k, itm_hide_boots, itm_rhun_greaves,  itm_rhun_helm_i, itm_sword_khergit_4, itm_khergit_sword_two_handed_b, itm_tab_shield_small_round_c],  knight_attrib_5,wp(300),knight_skills_5|knows_trainer_4|knows_power_draw_4, 0x0000000c360c524b6454465b59b9d93500000000001ea4860000000000000000, khergit_face_older_2],

["knight_3_16", "Tirida Noyan","Tirida", tf_hero|tf_vampire, 0, reserved,  fac_kingdom_3, [itm_nightmare_armor, itm_nazgul_robes,  itm_death_body,  itm_khergit_leather_boots,  itm_black_knight_foot,  itm_nazgul_hood_2, itm_black_knight_hand, itm_ebony_long_mace,  itm_drow_shield_rider,  itm_black_bow,  itm_flame_arrows],  knight_attrib_4,wp(300),knight_skills_5|knows_magic_power_4|knows_power_draw_4, 0x0000000c350c418438ab85b75c61b8d300000000001d21530000000000000000, khergit_face_middle_2],
["knight_3_17", "Ulusamai Noyan", "Ulusamai", tf_hero|tf_vampire, 0, reserved,  fac_kingdom_3, [itm_nightmare_armor,  itm_nazgul_robes, itm_twiligh_armor, itm_khergit_leather_boots, itm_black_knight_foot, itm_nazgul_hood_2, itm_black_knight_hand,   itm_ebony_axe, itm_archlich_staff_1,itm_magic_spirit_leech],  knight_attrib_4,wp(300),knight_skills_5|knows_magic_power_4|knows_necromancy_4, 0x0000000c3c0821c647264ab6e68dc4d500000000001e42590000000000000000, khergit_face_old_2],
["knight_3_18", "Karaban Noyan", "Karaban", tf_hero|tf_vampire, 0, reserved,  fac_kingdom_3, [itm_nightmare_armor,   itm_nazgul_robes, itm_death_body, itm_khergit_leather_boots, itm_black_knight_foot,  itm_nazgul_hood_2, itm_black_knight_hand,   itm_ebony_scimitar_2,itm_ebony_scimitar_long_3, itm_drow_shield_rider, itm_khergit_lance,  ],   knight_attrib_4,wp(300),knight_skills_5|knows_trainer_4|knows_riding_4, 0x0000000c0810500347ae7acd0d3ad74a00000000001e289a0000000000000000, khergit_face_older_2],
["knight_3_19", "Akadan Noyan","Akadan", tf_hero, 0, reserved,  fac_kingdom_3, [itm_khergit_war_horse,   itm_nomad_robe, itm_rhun_armor_k, itm_leather_boots, itm_rhun_greaves,  itm_rhun_helm_n, itm_lamellar_gauntlets, itm_khergit_lance, itm_sword_khergit_7, itm_dec_steel_shield],  knight_attrib_4,wp(300),knight_skills_4|knows_trainer_5|knows_power_draw_4, 0x0000000c1500510528f50d52d20b152300000000001d66db0000000000000000, khergit_face_older_2],
["knight_3_20", "Dundush Noyan","Dundush", tf_hero, 0, reserved,  fac_kingdom_3, [itm_khergit_war_horse, itm_lamellar_vest, itm_rhun_armor_k, itm_hide_boots, itm_rhun_greaves, itm_rhun_helm_n, itm_scale_gauntlets, itm_khergit_sword_two_handed_a,  itm_khergit_lance, itm_khergit_long_bow, itm_demon_arrow],  knight_attrib_5,wp(300),knight_skills_5|knows_power_draw_8, 0x0000000f7800620d66b76edd5cd5eb6e00000000001f691e0000000000000000, khergit_face_older_2],


["knight_4_1","Henry_Beaufort","Henry_Beaufort", tf_hero, no_scene,reserved,fac_kingdom_4,
[itm_rich_outfit,  itm_glass_male_plate,   itm_woolen_hose,  itm_glass_foot,  itm_glass_head, itm_glass_hand, itm_woodelf_arrows_poison_2,itm_long_bow_3, itm_glass_long_mace,itm_freeze_shield], knight_attrib_1,wp(300),knows_magic_power_4|knight_skills_1|knows_power_draw_5, 0x000000072804030264fc6e46a568bd5900000000001db51c0000000000000000, nord_face_middle_2],
["knight_4_2","Humphrey_Stafford","Humphrey_Stafford", tf_hero, no_scene,reserved,fac_kingdom_4,
 [itm_warhorse_england, itm_short_tunic,  itm_knight_plate_2, itm_blue_hose,  itm_iron_greaves2,  itm_winged_great_helmet, itm_plate_mittens, itm_glass_long_mace,  itm_tab_shield_kite_cav_b],  knight_attrib_2,wp(300),knight_skills_2|knows_trainer_3, 0x00000007190804c334e86d2853654694000000000005445b0000000000000000, nord_face_old_2],

["knight_4_3","Henry_Holland","Henry_Holland", tf_hero, no_scene,reserved,fac_kingdom_4,
 [itm_charger_england, itm_rich_outfit,  itm_gothic_plate_nobevor,   itm_nomad_boots,  itm_iron_greaves2, itm_plate_mittens,   itm_hounskull,   itm_sword_claymore_01, itm_shield_heater_c],  knight_attrib_3,wp(300),knight_skills_3, 0x000000070a00039128dc2d29117496d40000000000119d210000000000000000, nord_face_older_2],
["knight_4_4","Thomas_Percy","Thomas_Percy", tf_male_elf|tf_hero, no_scene,reserved,fac_kingdom_4,
 [   itm_courtly_outfit,   itm_half_plates_red_2,   itm_woolen_hose,  itm_iron_greaves2, itm_plate_mittens,  itm_open_sallet, itm_glass_long_mace, itm_woodelf_mutil_arrows,itm_long_bow_3,itm_shield_heater_c],  knight_attrib_4,wp(300),knows_magic_power_10|knight_skills_4|knows_power_draw_5, 0x00000007280844c648a38ca6ac79daa500000000001d58da0000000000000000, nord_face_older_2],
["knight_4_5","Jean_de_Foix","Jean_de_Foix", tf_male_elf|tf_hero, no_scene,reserved,fac_kingdom_4,
 [itm_pegasus,  itm_rich_outfit,   itm_glass_male_plate,   itm_mirkwood_boots,  itm_glass_foot,  itm_glass_hand, itm_glass_head, itm_glass_sword_c, itm_freeze_shield, itm_glass_lance], knight_attrib_5,wp(380),knight_skills_5, 0x000000009f0c000a74e445ad61b5a84b00000000001d42de0000000000000000, nord_face_older_2],


["knight_4_6","John_Talbot","John_Talbot", tf_hero, no_scene,reserved,fac_kingdom_4,
 [itm_warhorse_england,   itm_rich_outfit,   itm_corrazina_red,  itm_woolen_hose,  itm_iron_greaves2,   itm_great_helmet, itm_plate_mittens,   itm_knightaxe,itm_sword_claymore_01, itm_shield_heater_c],   knight_attrib_1,wp(300),knight_skills_1, 0x00000007290415c94b136cc6e5b2465900000000001d38ee0000000000000000, nord_face_middle_2],
["knight_4_7","Jasper_Tudor","Jasper_Tudor", tf_hero, no_scene,reserved,fac_kingdom_4,
 [itm_warhorse_england_2,  itm_rich_outfit,   itm_plate_armor_2,   itm_blue_hose,  itm_iron_greaves2,  itm_winged_great_helmet, itm_wisby_gauntlets_black,   itm_bastard_sword_e, itm_glass_lance_2,  itm_tab_shield_kite_cav_b],   knight_attrib_2,wp(300),knight_skills_2|knows_trainer_4, 0x000000071d0835876cd474b8dab750ad0000000000054aae0000000000000000, nord_face_old_2],
["knight_4_8","Richard_Woodville","Richard_Woodville", tf_hero, no_scene,reserved,fac_kingdom_4,
 [itm_charger_england, itm_rich_outfit,  itm_half_plates_red_2,   itm_woolen_hose,  itm_iron_greaves2,   itm_sturmhaube_w3, itm_plate_mittens, itm_knightaxe,itm_sword_claymore_01,  itm_shield_heater_c],   knight_attrib_3,wp(300),knight_skills_3, 0x000000071f0043c82a939938dbae65290000000000166b640000000000000000, nord_face_older_2],
  
["knight_4_9","Richard_Neville","Richard_Neville", tf_male_elf|tf_hero, no_scene,reserved,fac_kingdom_4,
 [itm_charger_england, itm_rich_outfit,   itm_glass_male_plate, itm_mirkwood_boots,  itm_glass_foot,  itm_glass_hand,itm_glass_head, itm_sldequiver, itm_elven_bow,   itm_sabre_2h_green],  knight_attrib_4,wp(300),knight_skills_4|knows_trainer_5|knows_power_draw_7, 0x00000003f20810095cea6d2d5b8e32da00000000001db74b0000000000000000, nord_face_older_2],
["knight_4_10","Richard_Warwick","Richard_Warwick", tf_male_elf|tf_hero, no_scene,reserved,fac_kingdom_4,
 [itm_charger_england,   itm_courtly_outfit,   itm_glass_male_plate,   itm_mirkwood_boots,  itm_glass_foot,  itm_glass_hand,itm_glass_head,itm_courtblades_green, itm_mirkwood_sword_reward,itm_freeze_shield],  knight_attrib_5,wp(300),knight_skills_5|knows_trainer_6, 0x00000005500000095968ae66ce96db8e00000000001db45b0000000000000000, nord_face_older_2],


["knight_4_11","William_Neville","William_Neville", tf_male_elf|tf_hero, no_scene,reserved,fac_kingdom_4,
 [itm_warhorse_england_2, itm_rich_outfit,  itm_glass_male_plate,   itm_woolen_hose,  itm_glass_foot,  itm_glass_head,  itm_glass_hand,  itm_warblade_greensilver,itm_glass_halberd, itm_shield_heater_c], knight_attrib_1,wp(300),knight_skills_1, 0x00000003110400084b9d3119646a44a400000000001c96db0000000000000000, nord_face_middle_2],
["knight_4_12","Thomas_Scalles","Thomas_Scalles", tf_male_elf|tf_hero, no_scene,reserved,fac_kingdom_4,
 [itm_warhorse_england, itm_short_tunic,  itm_glass_male_plate, itm_blue_hose,  itm_glass_foot,  itm_glass_head,  itm_glass_hand,  itm_glass_sword_a,itm_glass_sword_c,itm_glass_lance_2,  itm_freeze_shield],  knight_attrib_2,wp(300),knight_skills_2, 0x000000029c082003176c89d79c791ea300000000000736e60000000000000000, nord_face_old_2],
["knight_4_13","John_Clifford","John_Clifford", tf_male_elf|tf_hero, no_scene,reserved,fac_kingdom_4,
 [itm_charger_england, itm_rich_outfit,  itm_glass_male_plate,   itm_nomad_boots,  itm_glass_foot, itm_glass_head,   itm_glass_hand,   itm_knightaxe,itm_sabre_2h_green, itm_freeze_shield],  knight_attrib_3,wp(300),knight_skills_3|knows_trainer_3, 0x00000007330420c96b2c4e57149ac26100000000001d35880000000000000000, nord_face_older_2],
 
 
["knight_4_14","Henry_Bourchier","Henry_Bourchier", tf_hero, no_scene,reserved,fac_kingdom_4,
 [itm_charger_england,  itm_courtly_outfit,   itm_gothic_plate_nobevor,   itm_woolen_hose,  itm_iron_greaves2,  itm_new_sallet_red, itm_plate_mittens, itm_glass_sword_c,itm_bastard_sword_e, itm_shield_heater_c],  knight_attrib_4,wp(300),knight_skills_4, 0x000000071c0824c3471c79b56da5590400000000001d99a30000000000000000, nord_face_older_2],
["knight_4_15","John_Montagu","John_Montagu", tf_male_elf|tf_hero, no_scene,reserved,fac_kingdom_4,
 [itm_leather_jacket,   itm_glass_male_plate,   itm_mirkwood_boots,  itm_glass_foot,  itm_glass_hand,itm_druid_cap, itm_magic_book_3, itm_magic_ice_ray,itm_shaman_staff_2,itm_magic_ice_ray], knight_attrib_5,wp(300),knight_skills_5|knows_trainer_6|knows_magic_power_10|knows_magic_defence_10|knows_necromancy_10, 0x00000005b9101004252b68ad1d45322d00000000001dd71d0000000000000000, nord_face_older_2],


["knight_4_16","Thomas_Kyriell","Thomas_Kyriell", tf_hero, no_scene,reserved,fac_kingdom_4,
 [itm_barded_horse_red,   itm_rich_outfit,   itm_half_plates_red,  itm_woolen_hose,  itm_iron_greaves2,   itm_hounskull, itm_plate_mittens,   itm_knightaxe, itm_shield_heater_c],   knight_attrib_1,wp(300),knight_skills_1, 0x000000099700124239233512e287391d00000000001db7200000000000000000, nord_face_middle_2],
 
["knight_4_17","John_de_Mowbray","John_de_Mowbray", tf_hero, no_scene,reserved,fac_kingdom_4,
 [itm_warhorse_england_2,  itm_rich_outfit,   itm_plate_armor_2,   itm_blue_hose,  itm_iron_greaves2,  itm_new_sallet_red, itm_plate_mittens,   itm_longsword,itm_poleaxe,  itm_tab_shield_kite_cav_b],   knight_attrib_2,wp(300),knight_skills_2|knows_trainer_4, 0x0000000a400822d214db71685d66346300000000001da6a50000000000000000, nord_face_old_2],
 
["knight_4_18","John_Surrey","John_Surrey", tf_hero, no_scene,reserved,fac_kingdom_4,
 [itm_charger_england, itm_rich_outfit,  itm_half_plates_red_2,   itm_woolen_hose,  itm_iron_greaves2,   itm_sturmhaube_bnw2, itm_plate_mittens, itm_bastard_sword_e, itm_glass_lance_2,  itm_tab_shield_kite_c],   knight_attrib_3,wp(300),knight_skills_3, 0x00000006cd00918866e22e3d9735a72600000000001eacad0000000000000000, nord_face_older_2],
  
  
["knight_4_19","William_FitzAlan","William_FitzAlan", tf_hero, no_scene,reserved,fac_kingdom_4,
 [ itm_rich_outfit,   itm_half_plates_red_2, itm_blue_hose,  itm_iron_greaves2,  itm_open_sallet, itm_plate_mittens,   itm_woodelf_mutil_arrows,itm_long_bow_3,  itm_long_axe_c,itm_shield_heater_c],  knight_attrib_4,wp(300),knows_magic_power_10|knight_skills_4|knows_power_draw_5, 0x000000070308601024e26d4a6295965a00000000001d23e40000000000000000, nord_face_older_2],
 
["knight_4_20","William_Bonville","William_Bonville", tf_male_elf|tf_hero, no_scene,reserved,fac_kingdom_4,
 [   itm_courtly_outfit,   itm_black_hole_plate,   itm_nomad_boots,  itm_ebony_male_foot, itm_ebony_male_hand,  itm_lancelothelmet,itm_aroundight, itm_power_musket_8barrel,itm_cartridges_rar,itm_cartridges_rar],  knight_attrib_5,wp(500),knows_stealth_10|knows_riding_10|knows_ironflesh_15|knows_power_strike_15|knows_physique_15|knows_tactics_10|knows_prisoner_management_3|knows_leadership_13|knows_pathfinding_10|knows_trade_4|knows_weapon_master_10|knows_magic_defence_10|knows_magic_skill_14|knows_precise_shot_10, 0x00000002000c90095d256556e435cbac00000000001ed7330000000000000000, nord_face_older_2],


["knight_5_1", "Count Matheas", "Matheas", tf_hero|tf_undead, 0, reserved,  fac_kingdom_5, [itm_nightmare,   itm_tabard,   itm_black_plate_armor,       itm_leather_boots,    itm_iron_greaves2,    itm_open_sallet_coif, itm_milanese_gauntlets,     itm_undead_axe,itm_steel_shield,itm_ebony_throwing_pike,   itm_heavy_lance],     knight_attrib_1,wp(300),knight_skills_1|knows_trainer_3, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
["knight_5_2", "Count Gutlans", "Gutlans", tf_hero, 0, reserved,  fac_kingdom_5, [itm_charger_noble,    itm_red_gambeson,       itm_milanese_plate,    itm_leather_boots,    itm_iron_greaves2,    itm_visored_bascinet_2, itm_milanese_gauntlets,      itm_undead_axe,  itm_sword_two_handed_a,   itm_toumingdun],     knight_attrib_2,wp(300),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
["knight_5_3", "Count Laruqen", "Laruqen", tf_hero, 0, reserved,  fac_kingdom_5, [itm_charger_noble,     itm_short_tunic,  itm_milanese_plate,     itm_nomad_boots,      itm_iron_greaves2,  itm_visored_bascinet_2, itm_milanese_gauntlets, itm_two_handed_cleaver,itm_carbine_batarey_good,itm_cartridges_thrust,  itm_toumingdun],    knight_attrib_3,wp(300),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
["knight_5_4", "Count Raichs", "Raichs", tf_hero|tf_vampire, 0, reserved,  fac_kingdom_5,  [itm_undead_charger_2,     itm_vampire_tunic,     itm_black_plate_armor_2,       itm_leather_boots,      itm_black_greaves,    itm_undead_winged_great_helmet, itm_gauntlets, itm_ebony_scimitar_long_4,    itm_undead_shield_kite_cav],    knight_attrib_4,wp(300),knight_skills_4, 0x0000000a7f002002345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
["knight_5_5", "Count Reland", "Reland", tf_hero|tf_vampire, 0, reserved,  fac_kingdom_5, [itm_undead_charger_plate,     itm_vampire_tunic,  itm_twiligh_armor,     itm_leather_boots,    itm_twilight_boots,    itm_twilight_helm, itm_twilight_gloves, itm_undead_double_axe,itm_great_lance_dark,itm_ebony_scimitar_long_4,  itm_undead_shield_kite_cav], knight_attrib_5,wp(300),knight_skills_5, 0x0000000f8604000154826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
["knight_5_6", "Count Tarchias", "Tarchias", tf_hero|tf_undead, 0, reserved,  fac_kingdom_5, [itm_nightmare,    itm_ragged_outfit,      itm_black_plate_armor,       itm_woolen_hose,      itm_iron_greaves2, itm_milanese_gauntlets,   itm_open_sallet_coif,     itm_undead_sword_two_handed_4,itm_steel_shield,itm_ebony_throwing_pike,   itm_heavy_lance],    knight_attrib_1,wp(300),knight_skills_1, 0x000000001100000648d24d36cd964b1d00000000001e2dac0000000000000000, rhodok_face_middle_2],
["knight_5_7", "Count Gharmall", "Gharmall", tf_hero, 0, reserved,  fac_kingdom_5, [itm_charger_noble,     itm_coarse_tunic,       itm_milanese_plate,   itm_leather_boots,    itm_mail_chausses,  itm_milanese_gauntlets,      itm_visored_bascinet_2,       itm_bastard_sword_a,itm_carbine_batarey_good,itm_cartridges_thrust,    itm_toumingdun],     knight_attrib_2,wp(300),knight_skills_2, 0x0000000c3a0455c443d46e4c8b91291a00000000001ca51b0000000000000000, rhodok_face_old_2],
["knight_5_8", "Count Talbar", "Talbar", tf_hero, 0, reserved,  fac_kingdom_5, [itm_charger_noble, itm_vampire_tunic,     itm_milanese_plate,    itm_woolen_hose,      itm_iron_greaves2,    itm_visored_bascinet_2,  itm_milanese_gauntlets,      itm_undead_axe, itm_sword_two_handed_b,  itm_toumingdun],    knight_attrib_3,wp(300),knight_skills_3|knows_trainer_3, 0x0000000c2c0844d42914d19b2369b4ea00000000001e331b0000000000000000, rhodok_face_older_2],
["knight_5_9", "Count Rimusk", "Rimusk", tf_hero|tf_vampire, 0, reserved,  fac_kingdom_5,  [itm_undead_charger_2,     itm_vampire_tunic,     itm_black_plate_armor_2,       itm_leather_boots,      itm_black_greaves,    itm_undead_winged_great_helmet, itm_gauntlets, itm_undead_double_axe,    itm_great_lance],   knight_attrib_4,wp(300),knight_skills_4|knows_trainer_6, 0x0000000fc00410032331b5551c4724a100000000001e39a40000000000000000, rhodok_face_older_2],
["knight_5_10", "Count Falsevor", "Falsevor", tf_hero|tf_vampire, 0, reserved,  fac_kingdom_5, [itm_undead_charger_plate,     itm_vampire_tunic,  itm_twiligh_armor,     itm_leather_boots,    itm_twilight_boots,    itm_twilight_helm, itm_twilight_gloves, itm_undead_double_axe,itm_great_lance_dark,itm_ebony_scimitar_long_4,  itm_undead_shield_kite_cav],  knight_attrib_5,wp(300),knight_skills_5|knows_trainer_4, 0x0000000fff0010063d9b6d4a92ada53500000000001cc1180000000000000000, rhodok_face_older_2],
["knight_5_11", "Count Etrosq", "Etrosq", tf_hero|tf_undead, 0, reserved,  fac_kingdom_5, [itm_nightmare,     itm_tabard,       itm_black_plate_armor,       itm_leather_boots,    itm_iron_greaves2,    itm_open_sallet_coif,  itm_milanese_gauntlets,    itm_undead_axe,itm_steel_shield,itm_ebony_throwing_pike,   itm_heavy_lance],     knight_attrib_1,wp(300),knight_skills_1, 0x0000000c170c14874752adb6eb3228d500000000001c955c0000000000000000, rhodok_face_middle_2],
["knight_5_12", "Count Kurnias", "Kurnias", tf_hero, 0, reserved,  fac_kingdom_5, [itm_charger_noble,    itm_red_gambeson,       itm_milanese_plate,    itm_leather_boots,    itm_iron_greaves2,    itm_visored_bascinet_1,  itm_milanese_gauntlets,      itm_undead_axe,itm_carbine_batarey_good,itm_cartridges_thrust,   itm_toumingdun],     knight_attrib_2,wp(300),knight_skills_2|knows_trainer_5, 0x0000000c080c13d056ec8da85e3126ed00000000001d4ce60000000000000000, rhodok_face_old_2],
["knight_5_13", "Count Tellrog", "Tellrog", tf_hero, 0, reserved,  fac_kingdom_5, [itm_charger_noble,     itm_short_tunic,  itm_milanese_plate,     itm_nomad_boots,      itm_iron_greaves2,  itm_visored_bascinet_1, itm_milanese_gauntlets,       itm_sword_two_handed_a,  itm_toumingdun],    knight_attrib_3,wp(300),knight_skills_3, 0x0000000cbf10100562a4954ae731588a00000000001d6b530000000000000000, rhodok_face_older_2],
["knight_5_14", "Count Tribidan", "Tribidan", tf_hero|tf_vampire, 0, reserved,  fac_kingdom_5, [itm_undead_charger_2,     itm_vampire_tunic,     itm_black_plate_armor_2,       itm_leather_boots,      itm_black_greaves,    itm_undead_winged_great_helmet, itm_gauntlets, itm_undead_scimitar,    itm_undead_shield_kite_cav],    knight_attrib_4,wp(300),knight_skills_4, 0x0000000c330805823baa77556c4e331a00000000001cb9110000000000000000, rhodok_face_older_2],
["knight_5_15", "Count Gerluchs", "Gerluchs", tf_hero|tf_vampire, 0, reserved,  fac_kingdom_5, [itm_undead_charger_plate,     itm_vampire_tunic,  itm_twiligh_armor,     itm_leather_boots,    itm_twilight_boots,    itm_twilight_helm, itm_twilight_gloves, itm_undead_double_axe,itm_great_lance_dark,itm_ebony_scimitar_long_4,  itm_undead_shield_kite_cav], knight_attrib_5,wp(300),knight_skills_5, 0x0000000fff000006370c4d4732b536de00000000001db9280000000000000000, rhodok_face_older_2],
["knight_5_16", "Count Fudreim", "Fudreim", tf_hero|tf_undead, 0, reserved,  fac_kingdom_5, [itm_nightmare,    itm_ragged_outfit,      itm_black_plate_armor,       itm_woolen_hose,      itm_iron_greaves2,    itm_open_sallet_coif, itm_milanese_gauntlets,     itm_undead_axe,itm_steel_shield,itm_ebony_throwing_pike,   itm_heavy_lance],    knight_attrib_1,wp(300),knight_skills_1, 0x0000000c06046151435b5122a37756a400000000001c46e50000000000000000, rhodok_face_middle_2],
["knight_5_17", "Count Nealcha", "Nealcha", tf_hero, 0, reserved,  fac_kingdom_5, [itm_charger_noble,     itm_coarse_tunic,       itm_milanese_plate,   itm_leather_boots,    itm_mail_chausses,       itm_visored_bascinet_1,  itm_milanese_gauntlets,      itm_bastard_sword_a,itm_carbine_batarey_good,itm_cartridges_thrust,    itm_toumingdun],     knight_attrib_2,wp(300),knight_skills_2, 0x0000000c081001d3465c89a6a452356300000000001cda550000000000000000, rhodok_face_old_2],
["knight_5_18", "Count Fraichin", "Fraichin", tf_hero, 0, reserved,  fac_kingdom_5, [itm_charger_noble, itm_vampire_tunic,     itm_milanese_plate,    itm_woolen_hose,      itm_iron_greaves2,    itm_visored_bascinet_2, itm_milanese_gauntlets,       itm_undead_axe,   itm_toumingdun],    knight_attrib_3,wp(300),knight_skills_3, 0x0000000a3d0c13c3452aa967276dc95c00000000001dad350000000000000000, rhodok_face_older_2],
["knight_5_19", "Count Trimbau", "Trimbau", tf_hero|tf_vampire, 0, reserved,  fac_kingdom_5,  [itm_undead_charger_2,     itm_vampire_tunic,     itm_black_plate_armor_2,       itm_leather_boots,      itm_black_greaves,    itm_undead_winged_great_helmet, itm_gauntlets, itm_ebony_scimitar_long_4,    itm_undead_shield_kite_cav],   knight_attrib_4,wp(300),knight_skills_4|knows_trainer_5, 0x0000000ff30800113baa77556c4e331a00000000001cb9110000000000000000, rhodok_face_older_2],
["knight_5_20", "Count Reichsin", "Reichsin", tf_hero|tf_vampire, 0, reserved,  fac_kingdom_5, [itm_undead_charger_plate,     itm_vampire_tunic,  itm_twiligh_armor,     itm_leather_boots,    itm_twilight_boots,    itm_twilight_helm, itm_twilight_gloves, itm_undead_double_axe,itm_great_lance_dark,itm_ebony_scimitar_long_4,  itm_undead_shield_kite_cav],  knight_attrib_5,wp(300),knight_skills_5|knows_trainer_6, 0x000000003600420515a865b45c64d64c00000000001d544b0000000000000000, rhodok_face_older_2],


#["knight_6_2", "Emir Hamezan", "Hamezan", tf_hero, 0, reserved,  fac_kingdom_6, [itm_warhorse_sarranid,    itm_sarranid_elite_armor,       itm_sarranid_boots_c,    itm_sarranid_boots_d,    itm_sarranid_warrior_cap, itm_leather_gloves,   itm_khergit_lance,   itm_morningstar,  itm_sword_two_handed_a,   itm_tab_shield_small_round_c],     knight_attrib_2,wp(300),knight_skills_2|knows_trainer_4, 0x00000001380825d444cb68b92b8d3b1d00000000001dd71e0000000000000000, rhodok_face_old_2],
#["knight_6_3", "Emir Atis", "Atis", tf_hero, 0, reserved,  fac_kingdom_6, [itm_lamellar_warhorse,     itm_mamluke_mail_heavy,       itm_nomad_boots,      itm_sarranid_warrior_cap,  itm_sarranid_two_handed_axe_a, itm_lamellar_gauntlets,  itm_tab_shield_small_round_c],    knight_attrib_3,wp(300),knight_skills_3, 0x000000002208428579723147247ad4e500000000001f14d40000000000000000, rhodok_face_older_2],
#["knight_6_4", "Emir Nuwas", "Nuwas", tf_hero, 0, reserved,  fac_kingdom_6, [itm_lamellar_warhorse,     itm_sarranid_elite_armor,            itm_sarranid_boots_c,          itm_sarranid_mail_coif,  itm_sarranid_cavalry_sword, itm_lamellar_gauntlets, itm_khergit_lance,   itm_tab_shield_small_round_c],    knight_attrib_4,wp(300),knight_skills_4, 0x00000009bf084285050caa7d285be51a00000000001d11010000000000000000, rhodok_face_older_2],
#["knight_6_5", "Emir Mundhalir", "Mundhalir", tf_hero, 0, reserved,  fac_kingdom_6, [itm_warhorse_sarranid,     itm_mamluke_mail,       itm_sarranid_boots_c,    itm_sarranid_veiled_helmet,  itm_sarranid_two_handed_axe_a,  itm_tab_shield_small_round_c], knight_attrib_5,wp(300),knight_skills_5, 0x000000002a084003330175aae175da9c00000000001e02150000000000000000, rhodok_face_older_2],
#["knight_6_6", "Emir Ghanawa", "Ghanawa", tf_hero, 0, reserved,  fac_kingdom_6, [itm_lamellar_warhorse,    itm_sarranid_elite_armor,            itm_sarranid_boots_c,      itm_splinted_greaves,    itm_sarranid_helmet1, itm_khergit_lance,      itm_sarranid_cavalry_sword,   itm_tab_shield_small_round_c],    knight_attrib_1,wp(300),knight_skills_1, 0x00000001830043834733294c89b128e200000000001259510000000000000000, rhodok_face_middle_2],
#["knight_6_7", "Emir Nuam", "Nuam", tf_hero, 0, reserved,  fac_kingdom_6, [itm_warhorse_sarranid,     itm_sarranid_elite_armor,          itm_sarranid_boots_c,          itm_sarranid_mail_coif,       itm_sarranid_cavalry_sword,  itm_lamellar_gauntlets,  itm_tab_shield_small_round_c],     knight_attrib_2,wp(300),knight_skills_2, 0x0000000cbf10434020504bbbda9135d500000000001f62380000000000000000, rhodok_face_old_2],
#["knight_6_8", "Emir Dhiyul", "Dhiyul", tf_hero, 0, reserved,  fac_kingdom_6, [itm_lamellar_warhorse, itm_mamluke_mail_heavy,         itm_sarranid_boots_c,      itm_sarranid_boots_d,    itm_sarranid_helmet1,        itm_morningstar, itm_khergit_lance,  itm_sarranid_cavalry_sword,  itm_tab_shield_small_round_c],    knight_attrib_3,wp(300),knight_skills_3|knows_trainer_3, 0x0000000190044003336dcd3ca2cacae300000000001f47640000000000000000, rhodok_face_older_2],
#["knight_6_9", "Emir Lakhem", "Lakhem", tf_hero, 0, reserved,  fac_kingdom_6, [itm_lamellar_charger,     itm_sarranid_elite_armor,        itm_sarranid_boots_c,    itm_sarranid_helmet1, itm_lamellar_gauntlets,   itm_khergit_lance, itm_tab_shield_small_round_c],   knight_attrib_4,wp(300),knight_skills_4|knows_trainer_6, 0x0000000dde0040c4549dd5ca6f4dd56500000000001e291b0000000000000000, rhodok_face_older_2],
#["knight_6_10", "Emir Ghulassen", "Ghulassen", tf_hero, 0, reserved,  fac_kingdom_6, [itm_lamellar_charger,     itm_mamluke_mail,       itm_sarranid_boots_c,  itm_sarranid_boots_c,       itm_sarranid_helmet1, itm_lamellar_gauntlets,   itm_khergit_lance,     itm_sarranid_cavalry_sword,   itm_tab_shield_small_round_c],  knight_attrib_5,wp(300),knight_skills_5|knows_trainer_4, 0x00000001a60441c66ce99256b4ad4b3300000000001d392c0000000000000000, rhodok_face_older_2],
#["knight_6_11", "Emir Azadun", "Azadun", tf_hero, 0, reserved,  fac_kingdom_6, [itm_lamellar_warhorse,     itm_sarranid_elite_armor,              itm_sarranid_boots_c,    itm_sarranid_boots_c,    itm_sarranid_mail_coif,  itm_leather_gloves,    itm_military_pick2,   itm_tab_shield_small_round_c],     knight_attrib_1,wp(300),knight_skills_1, 0x0000000fff08134726c28af8dc96e4da00000000001e541d0000000000000000, rhodok_face_middle_2],
#["knight_6_12", "Emir Quryas", "Quryas", tf_hero, 0, reserved,  fac_kingdom_6, [itm_lamellar_charger,    itm_mamluke_mail_heavy,           itm_sarranid_boots_c,    itm_sarranid_boots_d,    itm_sarranid_helmet1, itm_khergit_lance,    itm_morningstar,   itm_tab_shield_small_round_c],     knight_attrib_2,wp(300),knight_skills_2|knows_trainer_5, 0x0000000035104084635b74ba5491a7a400000000001e46d60000000000000000, rhodok_face_old_2],
#["knight_6_13", "Emir Amdar", "Amdar", tf_hero, 0, reserved,  fac_kingdom_6, [itm_warhorse_sarranid,     itm_sarranid_elite_armor,       itm_sarranid_boots_c,      itm_sarranid_boots_c,  itm_sarranid_helmet1,   itm_lamellar_gauntlets,     itm_sword_two_handed_a,  itm_tab_shield_small_round_c],    knight_attrib_3,wp(300),knight_skills_3, 0x00000000001021435b734d4ad94eba9400000000001eb8eb0000000000000000, rhodok_face_older_2],
#["knight_6_14", "Emir Hiwan", "Hiwan", tf_hero, 0, reserved,  fac_kingdom_6, [itm_warhorse_sarranid,     itm_sarranid_elite_armor,       itm_sarranid_boots_c,      itm_sarranid_boots_c,    itm_sarranid_mail_coif, itm_khergit_lance,  itm_sarranid_cavalry_sword,    itm_tab_shield_small_round_c],    knight_attrib_4,wp(300),knight_skills_4, 0x000000000c0c45c63a5b921ac22db8e200000000001cca530000000000000000, rhodok_face_older_2],
#["knight_6_15", "Emir Muhnir", "Muhnir", tf_hero, 0, reserved,  fac_kingdom_6, [itm_lamellar_charger,     itm_sarranid_elite_armor,       itm_sarranid_boots_c,    itm_sarranid_boots_d,    itm_sarranid_helmet1,  itm_sword_two_handed_a,  itm_tab_shield_small_round_c], knight_attrib_5,wp(300),knight_skills_5, 0x000000001b0c4185369a6938cecde95600000000001f25210000000000000000, rhodok_face_older_2],

#["knight_6_16", "Emir Ayyam", "Ayyam", tf_hero, 0, reserved,  fac_kingdom_6, [itm_lamellar_warhorse,    itm_mamluke_mail_heavy,             itm_sarranid_boots_c,      itm_sarranid_boots_c,    itm_sarranid_mail_coif, itm_leather_gloves,  itm_khergit_lance,    itm_military_pick2,   itm_tab_shield_small_round_c],    knight_attrib_1,wp(300),knight_skills_1, 0x00000007770841c80a01e1c5eb51ffff00000000001f12d80000000000000000, rhodok_face_middle_2],
#["knight_6_17", "Emir Raddoun", "Raddoun", tf_hero, 0, reserved,  fac_kingdom_6, [itm_lamellar_charger,     itm_sarranid_elite_armor,          itm_sarranid_boots_c,    itm_sarranid_boots_c,       itm_sarranid_mail_coif,  itm_leather_gloves,      itm_sarranid_cavalry_sword,    itm_tab_shield_small_round_c],     knight_attrib_2,wp(300),knight_skills_2, 0x000000007f0462c32419f47a1aba8bcf00000000001e7e090000000000000000, rhodok_face_old_2],
#["knight_6_18", "Emir Tilimsan", "Tilimsan", tf_hero, 0, reserved,  fac_kingdom_6, [itm_lamellar_warhorse,  itm_sarranid_elite_armor,     itm_sarranid_boots_c,      itm_sarranid_boots_d,    itm_sarranid_helmet1,  itm_khergit_lance,       itm_morningstar,   itm_tab_shield_small_round_c],    knight_attrib_3,wp(300),knight_skills_3, 0x000000003410410070d975caac91aca500000000001c27530000000000000000, rhodok_face_older_2],
#["knight_6_19", "Emir Dhashwal", "Dhashwal", tf_hero, 0, reserved,  fac_kingdom_6, [itm_warhorse_sarranid,     itm_sarranid_elite_armor,        itm_sarranid_boots_c,    itm_sarranid_boots_c,       itm_sarranid_mail_coif, itm_lamellar_gauntlets,   itm_military_pick2,  itm_sword_two_handed_a, itm_tab_shield_small_round_c],   knight_attrib_4,wp(300),knight_skills_4|knows_trainer_5, 0x000000018a08618016ac36bc8b6e4a9900000000001dd45d0000000000000000, rhodok_face_older_2],
#["knight_6_20", "Emir Biliya", "Biliya", tf_hero, 0, reserved,  fac_kingdom_6, [itm_warhorse_sarranid,     itm_mamluke_mail,       itm_sarranid_boots_c,  itm_sarranid_boots_c,       itm_sarranid_veiled_helmet,   itm_khergit_lance,      itm_sarranid_cavalry_sword,   itm_tab_shield_small_round_c],  knight_attrib_5,wp(300),knight_skills_5|knows_trainer_6, 0x00000001bd0040c0281a899ac956b94b00000000001ec8910000000000000000, rhodok_face_older_2],

["knight_7_1", "Count Friedrich", "Friedrich", tf_hero, 0, reserved, fac_kingdom_7, 
  [itm_armor_demi_griffin, itm_courtly_outfit, itm_gothic_plate_nobevor, itm_woolen_hose, itm_maximilian_greaves, itm_new_sallet, itm_bastard_sword_f,itm_morningstar2,itm_gothic_lance, itm_maximilian_gauntlets, itm_toumingdun], 
 knight_attrib_5,wp(300),knight_skills_5|knows_trainer_1|knows_trainer_3, 
  0x0000000c3e08601414ab4dc6e39296b200000000001e231b0000000000000000, swadian_face_older_2],
  
 ["knight_7_2", "Count Athalwolf", "Athalwolf", tf_hero, 0, reserved, fac_kingdom_7, 
 [itm_armor_demi_griffin, itm_red_gambeson, itm_enchanter_robe, itm_woolen_hose, itm_leather_boots, itm_wizard_hat_4, itm_hourglass_gauntlets, itm_magic_searing_doom,itm_enchanter_staff_1,itm_magic_searing_doom,], 
 knight_attrib_5,wp(300),knight_skills_5|knows_magic_power_8|knows_magic_defence_6|knows_necromancy_4, 
 0x0000000c0f0c320627627238dcd6599400000000001c573d0000000000000000, swadian_face_young_2],
 
 ["knight_7_3", "Count Herrmann", "Herrmann", tf_hero, 0, reserved, fac_kingdom_7, 
[ itm_nobleman_outfit, itm_grey_knight_plate, itm_leather_boots, itm_grey_knight_foot, itm_grey_knight_head, itm_grey_knight_hand, itm_grey_knight_poleaxe,itm_grey_knight_sword, itm_grey_knight_shield], knight_attrib_5|knows_weapon_master_8|knows_magic_power_8|knows_magic_defence_10,wp(300),knight_skills_5|knows_trainer_3, 0x0000000cb700210214ce89db276aa2f400000000001d36730000000000000000, swadian_face_young_2],
        
 ["knight_7_4", "Count Gottfied", "Gottfied", tf_hero, 0, reserved, fac_kingdom_7, 
[itm_armor_demi_griffin, itm_short_tunic, itm_empire_priest, itm_leather_boots, itm_iron_greaves, itm_bishop_mitre, itm_hourglass_gauntlets, itm_war_clerics_warhammer_cast_2, itm_war_clerics_warhammer_2, itm_magic_burning_gaze, itm_magic_burning_gaze], knight_attrib_5,wp(300),knight_skills_5|knows_trainer_4|knows_magic_power_6|knows_magic_defence_10|knows_necromancy_4, 0x0000000c370c1194546469ca6c4e450e00000000001ebac40000000000000000, swadian_face_older_2],
    
 ["knight_7_5", "Count Sigismund", "Sigismund", tf_hero, 0, reserved, fac_kingdom_7, 
[itm_armor_demi_griffin, itm_rich_outfit, itm_bane_blade_plate,itm_woolen_hose, itm_bane_blade_foot, itm_sallet_beret_plumes_red, itm_bane_blade_hand, itm_flamberge_fire,itm_morningstar2,itm_gothic_lance, itm_grey_knight_shield], knight_attrib_4,wp(300),knight_skills_4|knows_trainer_6, 0x0000000c0c1064864ba34e2ae291992b00000000001da8720000000000000000, swadian_face_older_2],
    
 ["knight_7_6", "Count Tredian", "Tredian", tf_hero, 0, reserved, fac_kingdom_7, 
[itm_armor_demi_griffin, itm_tabard, itm_gothic_plate_nobevor, itm_leather_boots, itm_maximilian_greaves, itm_new_sallet, itm_maximilian_gauntlets, itm_bastard_sword_b, itm_great_sword,itm_gothic_lance, itm_toumingdun], knight_attrib_5,wp(300),knight_skills_4|knows_trainer_4, 0x0000000c0a08038736db74c6a396a8e500000000001db8eb0000000000000000, swadian_face_older_2],
  
 ["knight_7_7", "Count Grainwad", "Grainwad", tf_hero, 0, reserved, fac_kingdom_7, 
[itm_armor_demi_griffin, itm_tabard, itm_grey_knight_plate, itm_leather_boots, itm_grey_knight_foot, itm_grey_knight_head, itm_grey_knight_hand, itm_grey_knight_sword, itm_grey_knight_poleaxe,itm_gothic_lance, itm_grey_knight_shield], str_100|agi_32|int_12|cha_12|level(50),wp(300),knight_skills_4|knows_trainer_4|knows_swordman_8|knows_stealth_6|knows_weapon_master_8|knows_magic_defence_10, 0x0000000c1e001500589dae4094aa291c00000000001e37a80000000000000000, swadian_face_young_2],
    
 ["knight_7_8", "Count Ryis", "Ryis", tf_hero, 0, reserved, fac_kingdom_7, 
[itm_armor_demi_griffin, itm_nobleman_outfit, itm_maximilian_plate, itm_leather_boots, itm_maximilian_greaves, itm_maximilian_sallet, itm_maximilian_gauntlets,itm_empire_warhammer, itm_ebony_great_sword, itm_gothic_lance, itm_toumingdun], knight_attrib_4,wp(300),knight_skills_4, 0x0000000c330855054aa9aa431a48d74600000000001ed5240000000000000000, swadian_face_older_2],

 ["knight_7_9", "Count Ludwig", "Ludwig", tf_hero, 0, reserved, fac_kingdom_7, 
[itm_charger_german, itm_gambeson, itm_knight_plate_5, itm_blue_hose, itm_maximilian_greaves, itm_hounskull_2, itm_maximilian_gauntlets, itm_morningstar,itm_great_lance, itm_tab_shield_heater_c], knight_attrib_3,wp(300),knight_skills_3, 0x0000000c0f08000458739a9a1476199800000000001fb6f10000000000000000, swadian_face_old_2],
  
 ["knight_7_10", "Count Heinrich", "Heinrich", tf_hero, 0, reserved, fac_kingdom_7, 
[itm_charger_german, itm_gambeson, itm_knight_plate_5, itm_woolen_hose, itm_maximilian_greaves, itm_winged_great_helmet_ger, itm_maximilian_gauntlets, itm_sword_two_handed_b,itm_great_lance, itm_tab_shield_heater_cav_b], knight_attrib_3,wp(300),knight_skills_3, 0x0000000c0610351048e325361d7236cd00000000001d532a0000000000000000, swadian_face_older_2],
  
 ["knight_7_11", "Count Bernhard", "Bernhard", tf_hero, 0, reserved, fac_kingdom_7, 
[itm_charger_german, itm_red_gambeson, itm_knight_plate_5, itm_woolen_hose, itm_iron_greaves, itm_winged_great_helmet_ger, itm_hourglass_gauntlets, itm_bastard_sword_a,itm_great_lance, itm_tab_shield_heater_cav_b], knight_attrib_3,wp(300),knight_skills_3, 0x0000000c03104490280a8cb2a24196ab00000000001eb4dc0000000000000000, swadian_face_older_2],
  
 ["knight_7_12", "Count Ulrich", "Ulrich", tf_hero, 0, reserved, fac_kingdom_7, 
[itm_charger_german, itm_rich_outfit, itm_empire_priest, itm_woolen_hose, itm_iron_greaves, itm_bishop_great_helm, itm_hourglass_gauntlets, itm_war_clerics_warhammer_cast_2,itm_magic_burning_gaze,itm_magic_burning_gaze, itm_shield_heater_c], knight_attrib_3|knows_magic_power_5,wp(300),knight_skills_3, 0x0000000c2a0805442b2c6cc98c8dbaac00000000001d389b0000000000000000, swadian_face_older_2],
    
 ["knight_7_13", "Count Hugo", "Hugo", tf_hero, 0, reserved, fac_kingdom_7, 
[itm_warhorse_german, itm_ragged_outfit, itm_bnw_armour_german, itm_woolen_hose, itm_bnw_gauntlets, itm_sturmhaube_bnw4, itm_bnw_splinted_greaves, itm_bastard_sword_f, itm_gothic_lance, itm_reitern_pistol_4s,itm_cartridges_burst], knight_attrib_2,wp(300),knight_skills_2|knows_horse_archery_8|knows_stealth_6, 0x0000000c380c30c2392a8e5322a5392c00000000001e5c620000000000000000, swadian_face_older_2],
    
 ["knight_7_14", "Count Rudolf", "Rudolf", tf_hero, 0, reserved, fac_kingdom_7, 
[itm_warhorse_german, itm_short_tunic, itm_bnw_armour_german, itm_leather_boots, itm_bnw_gauntlets, itm_sturmhaube_bnw4, itm_bnw_splinted_greaves, itm_bastard_sword_a, itm_reitern_pistol_4s,itm_cartridges_burst, itm_tab_shield_heater_d], knight_attrib_2,wp(300),knight_skills_3|knows_horse_archery_8|knows_stealth_6, 0x00000001bf08258956de95b64d4e56dc00000000001eb92d0000000000000000, swadian_face_older_2],
        
    
 ["knight_7_15", "Count Adolf", "Adolf", tf_hero, 0, reserved, fac_kingdom_7, 
[itm_charger_german, itm_rich_outfit, itm_maximilian_plate, itm_woolen_hose, itm_maximilian_greaves, itm_maximilian_sallet, itm_maximilian_gauntlets, itm_ebony_long_mace, itm_ebony_great_sword, itm_tab_shield_heater_d], knight_attrib_4,wp(300),knight_skills_2, 0x00000005bf1025d41d15105c936e1cdb00000000001e1d940000000000000000, swadian_face_young_2],
    
 ["knight_7_16", "Count Johann", "Johann", tf_hero, 0, reserved, fac_kingdom_7, 
[itm_griffin, itm_courtly_outfit, itm_enchanter_robe, itm_woolen_hose, itm_cav_boots, itm_wizard_hat_4, itm_magic_ice_ray, itm_enchanter_staff_1, itm_magic_ice_ray,itm_tab_shield_heater_c], knight_attrib_1|knows_magic_power_5|knows_magic_defence_3|knows_necromancy_7,wp(300),knight_skills_2, 0x000000004008b50657a1ba3ad44068cb00000000001e325a0000000000000000, swadian_face_young_2],
    
 ["knight_7_17", "Count Philipp", "Philipp", tf_hero, 0, reserved, fac_kingdom_7, 
[itm_charger_german, itm_gambeson, itm_bnw_armour_german, itm_blue_hose, itm_bnw_gauntlets, itm_sturmhaube_bnw4, itm_bnw_splinted_greaves, itm_morningstar, itm_reitern_pistol_4s,itm_cartridges_burst, itm_tab_shield_heater_cav_b], knight_attrib_2,wp(300),knight_skills_1|knows_trainer_4|knows_horse_archery_8|knows_stealth_6, 0x0000000a460c300148ed5e1727ea16500000000001e57a200000000000000000, swadian_face_young_2],

 ["knight_7_18", "Count Ludwig", "Ludwig", tf_hero, 0, reserved, fac_kingdom_7, 
[itm_warhorse_german, itm_gambeson, itm_knight_plate_5, itm_woolen_hose, itm_iron_greaves2, itm_winged_great_helmet_ger, itm_hourglass_gauntlets, itm_great_sword,itm_great_lance, itm_tab_shield_heater_cav_a], knight_attrib_3,wp(300),knight_skills_1, 0x00000000550055c6365d8565932a8d6400000000001ec6940000000000000000, swadian_face_young_2],

 ["knight_7_19", "Count Albrecht_Achilles", "Albrecht_Achilles", tf_hero, 0, reserved, fac_kingdom_7, 
[itm_griffin, itm_rich_outfit, itm_enchanter_robe, itm_woolen_hose, itm_cav_boots, itm_wizard_hat_4, itm_enchanter_staff_1,itm_magic_ice_ray], knight_attrib_1|knows_magic_power_7|knows_magic_defence_5|knows_necromancy_3,wp(300),knight_skills_1, 0x0000000e850801534cb531e99b78c52c00000000001dd4dd0000000000000000, swadian_face_young_2],
        
 ["knight_7_20", "Count Otto", "Otto", tf_hero, 0, reserved, fac_kingdom_7, 
[itm_charger_german, itm_ragged_outfit, itm_bnw_armour_german, itm_woolen_hose, itm_bnw_gauntlets, itm_sturmhaube_bnw4, itm_bnw_splinted_greaves, itm_espada_eslavona_b, itm_reitern_pistol_4s,itm_cartridges_burst, itm_tab_shield_heater_cav_a], knight_attrib_2|knows_horse_archery_8|knows_stealth_6,wp(300),knight_skills_1, 0x00000001a410259144d5d1d6eb55e96a00000000001db0db0000000000000000, swadian_face_young_2],




["knight_8_1", "Boyar Vuldrat", "Vuldrat", tf_hero, 0, reserved,  fac_kingdom_8, [itm_bear_armored,      itm_kuyak,     itm_vaegir_elite_armor,                   itm_nomad_boots,            itm_iron_greaves,        itm_vaegir_noble_helmet,    itm_lamellar_gauntlets,       itm_ebony_arming_sword,           itm_tab_shield_kite_c],    knight_attrib_1,wp(300),knight_skills_1|knows_trainer_3, 0x00000005590011c33d9b6d4a92ada53500000000001cc1180000000000000000, vaegir_face_middle_2],
["knight_8_2", "Boyar Naldera", "Naldera", tf_hero, 0, reserved,  fac_kingdom_8, [itm_bear_armored,      itm_rich_outfit,        itm_vaegir_elite_armor,               itm_woolen_hose,            itm_iron_greaves,                   itm_vaegir_noble_helmet,  itm_lamellar_gauntlets,      itm_great_bardiche, itm_ebony_scimitar_2,   itm_tab_shield_kite_cav_a],    knight_attrib_2,wp(300),knight_skills_2, 0x0000000c2a0015d249b68b46a98e176400000000001d95a40000000000000000, vaegir_face_old_2],
["knight_8_3", "Boyar Meriga", "Meriga", tf_hero, 0, reserved,  fac_kingdom_8, [itm_vaegir_charger,            itm_short_tunic,        itm_vaegir_elite_armor,                   itm_woolen_hose,            itm_iron_greaves,                   itm_litchina_helm, itm_lamellar_gauntlets,           itm_great_bardiche, itm_ebony_scimitar_2,           itm_tab_shield_kite_cav_b],     knight_attrib_3,wp(300),knight_skills_3, 0x0000000c131031c546a38a2765b4c86000000000001e58d30000000000000000, vaegir_face_older_2],
["knight_8_4", "Boyar Khavel", "Khavel", tf_hero, 0, reserved,  fac_kingdom_8, [itm_vaegir_charger,      itm_courtly_outfit,     itm_vaegir_elite_armor,               itm_rus_shoes,          itm_iron_greaves,                      itm_vaegir_noble_helmet, itm_lamellar_gauntlets,         itm_scimitar_long,   itm_tab_shield_kite_cav_b],    knight_attrib_4,wp(300),knight_skills_4, 0x0000000c2f0832c748f272540d8ab65900000000001d34e60000000000000000, vaegir_face_older_2],
["knight_8_5", "Boyar Doru", "Doru", tf_female_elf|tf_hero, 0, reserved,  fac_kingdom_8, [itm_drow_basilisk_2,            itm_rich_outfit,        itm_ebony_male_plate,                     itm_rus_shoes,          itm_ebony_male_foot,                   itm_ebony_male_head, itm_ebony_male_hand,   itm_drow_lance,itm_ebony_scimitar_2,itm_drow_shield_rider],       knight_attrib_5,wp(300),knight_skills_5|knows_trainer_10|knows_stealth_10|knows_weapon_master_10|knows_magic_defence_10, 0x0000000fb504000a66cec5e994456914000000000011a90b0000000000000000,mirkwood_elf_face_2],



["knight_8_6", "Boyar Belgaru", "Belgaru", tf_hero, 0, reserved,  fac_kingdom_8, [itm_bear_armored,      itm_nomad_vest,      itm_vaegir_elite_armor,                   itm_woolen_hose,            itm_iron_greaves,                   itm_litchina_helm,  itm_lamellar_gauntlets,          itm_ebony_arming_sword,           itm_tab_shield_kite_c],   knight_attrib_1,wp(300),knight_skills_1|knows_trainer_3, 0x0000000a0100421038da7157aa4e430a00000000001da8bc0000000000000000, vaegir_face_middle_2],
["knight_8_7", "Boyar Ralcha", "Ralcha", tf_hero, 0, reserved,  fac_kingdom_8, [itm_bear_armored,      itm_leather_jacket,     itm_vaegir_elite_armor,                   itm_rus_shoes,          itm_iron_greaves,                      itm_vaegir_noble_helmet,  itm_lamellar_gauntlets,          itm_great_bardiche, itm_ebony_scimitar_2,    itm_tab_shield_kite_cav_a],     knight_attrib_2,wp(300),knight_skills_2|knows_trainer_4, 0x0000000c04100153335ba9390b2d277500000000001d89120000000000000000, vaegir_face_old_2],
["knight_8_8", "Boyar Vlan", "Vlan", tf_hero, 0, reserved,  fac_kingdom_8, [itm_vaegir_charger,            itm_nomad_robe,             itm_vaegir_elite_armor,                     itm_woolen_hose,            itm_iron_greaves,                   itm_vaegir_noble_helmet, itm_lamellar_gauntlets,       itm_ebony_scimitar_long_2,    itm_tab_shield_kite_d],    knight_attrib_3,wp(300),knight_skills_3|knows_trainer_5, 0x0000000c00046581234e8da2cdd248db00000000001f569c0000000000000000, vaegir_face_older_2],
["knight_8_9", "Boyar Mleza", "Mleza", tf_hero, 0, reserved,  fac_kingdom_8, [itm_vaegir_charger,      itm_rich_outfit,        itm_vaegir_elite_armor,                     itm_rus_shoes,          itm_iron_greaves,                   itm_litchina_helm,  itm_lamellar_gauntlets,        itm_ebony_scimitar_long_3, itm_ebony_scimitar_2,   itm_tab_shield_kite_d],    knight_attrib_4,wp(300),knight_skills_4, 0x0000000c160451d2136469c4d9b159ad00000000001e28f10000000000000000, vaegir_face_older_2],
["knight_8_10", "Boyar Nelag", "Nelag", tf_beastman|tf_hero, 0, reserved,  fac_kingdom_8, [           itm_kuyak,        itm_ebony_male_plate,               itm_beast_leg,            itm_ebony_male_foot,                      itm_beastlord_head,  itm_ebony_male_hand,      (itm_ebony_double_axe,imod_masterwork),   itm_ebony_scimitar_2,itm_dragon_shield_2,],      knight_attrib_5,wp(300),knight_skills_5|knows_trainer_6|knows_power_strike_15|knows_ironflesh_15|knows_magic_defence_10|knows_magic_skill_15, 0x0000000f7c00520e66b76edd5cd5eb6e00000000001f691e0000000000000000, vaegir_face_older_2],

["knight_8_11", "Boyar Crahask", "Crahask", tf_female_elf|tf_hero, 0, reserved,  fac_kingdom_8, [itm_drow_basilisk,      itm_leather_jacket,     itm_ebony_male_plate,                   itm_nomad_boots,            itm_ebony_male_foot,        itm_ebony_male_head, itm_ebony_male_hand,           itm_ebony_great_sword,itm_thunder_staff_melee,itm_ebony_scimitar_2,itm_black_shield,],    horse_attrib_7|level(45),wp(400),knows_light_swordman_8|knows_magic_defence_6|knight_skills_1, 0x00000006ee04000b36f265e7543a377b00000000000f34220000000000000000,mirkwood_elf_face_2],

  


["knight_8_12", "Boyar Bracha", "Bracha", tf_hero, 0, reserved,  fac_kingdom_8, [itm_bear_armored,      itm_rich_outfit,        itm_vaegir_elite_armor,               itm_woolen_hose,            itm_iron_greaves,                   itm_vaegir_noble_helmet,  itm_lamellar_gauntlets,      itm_ebony_scimitar_long_1, itm_ebony_scimitar_2,    itm_tab_shield_kite_cav_a],    knight_attrib_2,wp(300),knight_skills_2, 0x0000000c0f04024b2509d5d53944c6a300000000001d5b320000000000000000, vaegir_face_old_2],
["knight_8_13", "Boyar Druli", "Druli", tf_hero, 0, reserved,  fac_kingdom_8, [itm_bear_armored,            itm_short_tunic,        itm_vaegir_elite_armor,                   itm_woolen_hose,            itm_iron_greaves,                   itm_litchina_helm,  itm_lamellar_gauntlets,          itm_great_bardiche, itm_ebony_scimitar_2,           itm_tab_shield_kite_cav_b],     knight_attrib_3,wp(300),knight_skills_3, 0x0000000c680432d3392230cb926d56ca00000000001da69b0000000000000000, vaegir_face_older_2],
["knight_8_14", "Boyar Marmun", "Marmun", tf_female_elf|tf_hero, 0, reserved,  fac_kingdom_8, [      itm_courtly_outfit,     itm_ebony_male_plate,               itm_rus_shoes,          itm_ebony_male_foot,                      itm_ebony_male_head,  itm_ebony_male_hand,        itm_serpent_dagger,   itm_tynan_dagger],    knight_attrib_4,wp(300),knight_skills_4|knows_trainer_6|knows_stealth_10|knows_power_strike_15|knows_weapon_master_10|knows_magic_defence_10,0x000000039c080009459471b95c76395b00000000000d2acc0000000000000000,mirkwood_elf_face_2],


["knight_8_15", "Boyar Gastya", "Gastya", tf_beastman|tf_hero, 0, reserved,  fac_kingdom_8, [            itm_rich_outfit,        itm_ebony_male_plate,                     itm_beast_leg,          itm_ebony_male_foot,                   itm_beastlord_head, itm_ebony_male_hand,    itm_ebony_axe, itm_vanguard_shield],       knight_attrib_5,wp(450),knight_skills_5|knows_power_strike_15|knows_ironflesh_15|knows_magic_defence_10|knows_magic_skill_15, 0x0000000de50052123b6bb36de5d6eb7400000000001dd72c0000000000000000, vaegir_face_older_2],

["knight_8_16", "Boyar Harish", "Harish", tf_beastman|tf_hero, 0, reserved,  fac_kingdom_8, [itm_vaegir_charger,      itm_nomad_vest,      itm_vaegir_elite_armor,                   itm_beast_leg,            itm_iron_greaves,                   itm_vaegir_noble_helmet,  itm_lamellar_gauntlets,          itm_ebony_scimitar_long_4, itm_ebony_scimitar_2,           itm_tab_shield_kite_c],   knight_attrib_1,wp(300),knight_skills_1, 0x000000085f00000539233512e287391d00000000001db7200000000000000000, vaegir_face_middle_2],


["knight_8_17", "Boyar Taisa", "Taisa", tf_female_elf|tf_hero, 0, reserved,  fac_kingdom_8, [itm_drow_basilisk_2,      itm_leather_jacket,     itm_ebony_male_plate,                   itm_rus_shoes,          itm_drow_plate_foot,                      itm_ebony_male_head,   itm_drow_plate_hand,         itm_drow_lance, itm_ebony_scimitar_2,   itm_drow_shield_rider],     knight_attrib_3,wp(450),knight_skills_2, 0x00000000f70000024ca330e4d2c18b2500000000000f579a0000000000000000,mirkwood_elf_face_2],

["knight_8_18", "Boyar Valishin", "Valishin", tf_female_elf|tf_hero, 0, reserved,  fac_kingdom_8, [itm_drow_basilisk_2,            itm_nomad_robe,             itm_ebony_male_plate,                     itm_woolen_hose,            itm_drow_plate_foot,                   itm_ebony_male_head,  itm_drow_plate_hand,      itm_drow_lance, itm_ebony_scimitar_2,   itm_drow_shield_rider],    knight_attrib_3,wp(450),knight_skills_3, 0x0000000fff0800042a6972b923522b1300000000001d67260000000000000000,mirkwood_elf_face_2],


["knight_8_19", "Boyar Rudin", "Rudin", tf_female_elf|tf_hero, 0, reserved,  fac_kingdom_8, [itm_drow_basilisk,      itm_rich_outfit,        itm_mistress_armor,                     itm_rus_shoes,          itm_demon_foot,                   itm_xenoargh_mask_black, itm_drow_elite_gloves,         itm_drow_staff_3,  itm_serpent_dagger,itm_magic_poison_dummy, itm_magic_fire_ray_dummy],    knight_attrib_4,wp(300),knight_skills_4|knows_trainer_10|knows_magic_power_15|knows_magic_defence_8|knows_necromancy_10|knows_magic_skill_10, 0x000000020200000126ed6e47238dc94d00000000001d36eb0000000000000000,mirkwood_elf_face_2],


["knight_8_20", "Boyar Kumipa", "Kumipa", tf_female_elf|tf_hero, 0, reserved,  fac_kingdom_8, [itm_drow_basilisk_2,          itm_kuyak,        itm_drow_plate,               itm_woolen_hose,            itm_drow_plate_foot,                      itm_ebony_male_head,  itm_drow_plate_hand,      itm_drow_lance, itm_ebony_scimitar_2,   itm_drow_shield_rider],      knight_attrib_5,wp(450),knight_skills_5|knows_trainer_10|knows_magic_defence_10, 0x000000009610000d6a9aad47286e74a90000000000125a8b0000000000000000,mirkwood_elf_face_2],



#khergit civilian clothes: itm_leather_vest, itm_nomad_vest, itm_nomad_robe, itm_lamellar_vest,itm_tribal_warrior_outfit
["knight_9_1", "Emir Uqais", "Uqais", tf_hero, 0, reserved,  fac_kingdom_9, [itm_lamellar_warhorse,   itm_rhun_armor_7,          itm_sarranid_boots_c,    itm_chaos_leg_2,    itm_rhun_helm_7, itm_leather_gloves,    itm_chaos_lance_1, itm_chaos_sword4,   itm_chaos_warrior_shield],     knight_attrib_1,wp(300),knight_skills_1|knows_trainer_3, 0x00000000600c2084486195383349eae500000000001d16a30000000000000000, rhodok_face_middle_2],
["knight_9_2", "Emir Hamezan", "Hamezan", tf_hero, 0, reserved,  fac_kingdom_9, [itm_warhorse_sarranid,    itm_rhun_armor_8,       itm_chaos_leg_2,    itm_chaos_leg_2,    itm_rhun_helm_8, itm_chaos_gauntlets,      itm_chaos_sword4,  itm_demon_sword_3,   itm_chaos_warrior_shield],     knight_attrib_2,wp(300),knight_skills_2|knows_trainer_4, 0x00000001380825d444cb68b92b8d3b1d00000000001dd71e0000000000000000, rhodok_face_old_2],
["knight_9_3", "Emir Atis", "Atis", tf_hero, 0, reserved,  fac_kingdom_9, [itm_lamellar_warhorse,     itm_rhun_armor_9,       itm_nomad_boots,itm_chaos_leg_3,      itm_rhun_helm_9,  itm_chaos_sword4,itm_demon_axe, itm_chaos_gauntlets,  itm_chaos_chosen_shield],    knight_attrib_3,wp(300),knight_skills_3, 
0x000000002208428579723147247ad4e500000000001f14d40000000000000000, rhodok_face_older_2],

["knight_9_5", "Emir Mundhalir", "Mundhalir", tf_demon_human|tf_hero, 0, reserved,  fac_kingdom_9, [itm_hell_nightmare,     itm_demon_knight_plate,       itm_demon_knight_hand,itm_demon_knight_leg,    itm_demon_knight_head,  itm_chaos_sword5,  itm_khorne_shield], knight_attrib_5,wp(300),knight_skills_5, 0x000000002a084003330175aae175da9c00000000001e02150000000000000000, rhodok_face_older_2],

["knight_9_4", "Emir Nuwas", "Nuwas", tf_demon_human|tf_hero, 0, reserved,  fac_kingdom_9, [itm_nightmare,     itm_rhun_armor_7,            itm_sarranid_boots_c,          itm_rhun_helm_7,  itm_chaos_sword4, itm_lamellar_gauntlets, itm_khergit_lance,   itm_chaos_warrior_shield],    knight_attrib_4,wp(300),knight_skills_4, 0x00000009bf084285050caa7d285be51a00000000001d11010000000000000000, rhodok_face_older_2],
["knight_9_6", "Emir Ghanawa", "Ghanawa", tf_hero, 0, reserved,  fac_kingdom_9, [itm_lamellar_warhorse,    itm_rhun_armor_9,            itm_sarranid_boots_c,      itm_chaos_leg_2,    itm_rhun_helm_9, itm_khergit_lance,      itm_chaos_sword4,   itm_chaos_chosen_shield],    knight_attrib_1,wp(300),knight_skills_1, 0x00000001830043834733294c89b128e200000000001259510000000000000000, rhodok_face_middle_2],
["knight_9_7", "Emir Nuam", "Nuam", tf_hero, 0, reserved,  fac_kingdom_9, [itm_warhorse_sarranid,     itm_rhun_armor_8,          itm_sarranid_boots_c,itm_chaos_leg_2,          itm_rhun_helm_8,       itm_chaos_sword4,  itm_lamellar_gauntlets,  itm_chaos_warrior_shield],     knight_attrib_2,wp(300),knight_skills_2, 0x0000000cbf10434020504bbbda9135d500000000001f62380000000000000000, rhodok_face_old_2],
["knight_9_8", "Emir Dhiyul", "Dhiyul", tf_hero, 0, reserved,  fac_kingdom_9, [itm_lamellar_warhorse, itm_rhun_armor_7,         itm_sarranid_boots_c,      itm_chaos_leg_3,    itm_rhun_helm_7,        itm_chaos_sword4, itm_khergit_lance,  itm_chaos_sword4,  itm_chaos_warrior_shield],    knight_attrib_3,wp(300),knight_skills_3|knows_trainer_3, 0x0000000190044003336dcd3ca2cacae300000000001f47640000000000000000, rhodok_face_older_2],
["knight_9_9", "Emir Lakhem", "Lakhem", tf_hero, 0, reserved,  fac_kingdom_9, [     itm_ninjia_armor,        itm_light_leather_boots,    itm_black_hood_mask, itm_lamellar_gauntlets,   itm_granata_medium,     itm_chaos_sword4, itm_tab_shield_small_round_c],   knight_attrib_4,wp(300),knight_skills_4|knows_reserved_17_6, 0x0000000dde0040c4549dd5ca6f4dd56500000000001e291b0000000000000000, rhodok_face_older_2],

["knight_9_10", "Emir Ghulassen", "Ghulassen", tf_demon_human|tf_hero, 0, reserved,  fac_kingdom_9, [itm_hell_nightmare,     itm_demon_knight_plate,       itm_sarranid_boots_c,  itm_demon_knight_leg,       itm_demon_knight_head, itm_demon_knight_hand,        itm_chaos_sword5,   itm_khorne_shield],  knight_attrib_5,wp(300),knight_skills_5|knows_trainer_4, 0x00000001a60441c66ce99256b4ad4b3300000000001d392c0000000000000000, rhodok_face_older_2],



["knight_9_11", "Emir Azadun", "Azadun", tf_demon_human|tf_hero, 0, reserved,  fac_kingdom_9, [itm_lamellar_warhorse,     itm_rhun_armor_9,              itm_sarranid_boots_c,    itm_chaos_leg_2,    itm_rhun_helm_9,  itm_leather_gloves,    itm_chaos_sword4,itm_chaos_lance_1,   itm_chaos_chosen_shield],     knight_attrib_1,wp(300),knight_skills_1, 0x0000000fff08134726c28af8dc96e4da00000000001e541d0000000000000000, rhodok_face_middle_2],
["knight_9_12", "Emir Quryas", "Quryas", tf_hero, 0, reserved,  fac_kingdom_9, [itm_coursera2,    itm_rhun_armor_8,           itm_sarranid_boots_c,    itm_chaos_leg_2,    itm_rhun_helm_8, itm_khergit_lance,    itm_chaos_sword4,   itm_chaos_warrior_shield],     knight_attrib_2,wp(300),knight_skills_2|knows_trainer_5, 0x0000000035104084635b74ba5491a7a400000000001e46d60000000000000000, rhodok_face_old_2],
["knight_9_13", "Emir Amdar", "Amdar", tf_demon_human|tf_hero, 0, reserved,  fac_kingdom_9, [itm_nightmare,     itm_rhun_armor_9,       itm_chaos_leg_3,      itm_sarranid_boots_c,  itm_rhun_helm_9,   itm_chaos_gauntlets,     itm_demon_sword_3,itm_chaos_sword4,  itm_chaos_chosen_shield],    knight_attrib_3,wp(300),knight_skills_3, 0x00000000001021435b734d4ad94eba9400000000001eb8eb0000000000000000, rhodok_face_older_2],
["knight_9_14", "Emir Hiwan", "Hiwan", tf_hero, 0, reserved,  fac_kingdom_9, [itm_warhorse_sarranid,     itm_rhun_armor_9,       itm_sarranid_boots_c,      itm_chaos_leg_3,    itm_rhun_helm_9, itm_mark_chaos,  itm_chaos_sword4,    itm_chaos_chosen_shield],    knight_attrib_4,wp(300),knight_skills_4, 0x000000000c0c45c63a5b921ac22db8e200000000001cca530000000000000000, rhodok_face_older_2],

["knight_9_15", "Emir Muhnir", "Muhnir", tf_demon_human|tf_hero, 0, reserved,  fac_kingdom_9, [itm_nightmare,     itm_demon_knight_plate,       itm_sarranid_boots_c,    itm_demon_knight_hand, itm_demon_knight_leg,    itm_demon_knight_head,  itm_balor_sword,itm_magic_poison_dummy,itm_magic_fire_ray_dummy,  itm_demon_knight_shield], knight_attrib_5,wp(300),knight_skills_5, 0x000000001b0c4185369a6938cecde95600000000001f25210000000000000000, rhodok_face_older_2],

["knight_9_16", "Emir Ayyam", "Ayyam", tf_hero, 0, reserved,  fac_kingdom_9, [itm_arabian_horse_a,    itm_rhun_armor_7,             itm_sarranid_boots_c,      itm_chaos_leg_2,    itm_rhun_helm_7, itm_leather_gloves,  itm_khergit_lance,    itm_chaos_sword4,   itm_chaos_warrior_shield],    knight_attrib_1,wp(300),knight_skills_1, 0x00000007770841c80a01e1c5eb51ffff00000000001f12d80000000000000000, rhodok_face_middle_2],
["knight_9_17", "Emir Raddoun", "Raddoun", tf_hero, 0, reserved,  fac_kingdom_9, [itm_arabian_horse_b,     itm_rhun_armor_9,          itm_sarranid_boots_c,    itm_chaos_leg_2,       itm_rhun_helm_9,  itm_leather_gloves,      itm_chaos_sword4,itm_chaos_lance_1,    itm_chaos_chosen_shield],     knight_attrib_2,wp(300),knight_skills_2, 0x000000007f0462c32419f47a1aba8bcf00000000001e7e090000000000000000, rhodok_face_old_2],
["knight_9_18", "Emir Tilimsan", "Tilimsan", tf_hero, 0, reserved,  fac_kingdom_9, [itm_arabian_horse_a,  itm_rhun_armor_9,     itm_sarranid_boots_c,      itm_chaos_leg_3,    itm_rhun_helm_9,  itm_khergit_lance,       itm_chaos_sword4,   itm_chaos_chosen_shield],    knight_attrib_3,wp(300),knight_skills_3, 0x000000003410410070d975caac91aca500000000001c27530000000000000000, rhodok_face_older_2],
["knight_9_19", "Emir Dhashwal", "Dhashwal", tf_demon_human|tf_hero, 0, reserved,  fac_kingdom_9, [itm_hell_nightmare,     itm_demon_knight_plate,        itm_demon_knight_leg,    itm_demon_knight_leg,       itm_demon_knight_head, itm_demon_knight_hand,   itm_chaos_sword5,   itm_khorne_shield],   knight_attrib_4,wp(300),knight_skills_4|knows_trainer_5, 0x000000018a08618016ac36bc8b6e4a9900000000001dd45d0000000000000000, rhodok_face_older_2],


["knight_9_20", "Emir Biliya", "Biliya", tf_demon_human|tf_hero, 0, reserved,  fac_kingdom_9, [itm_tzeentch_charger,     itm_tzeentch_chosen_armor,       itm_sarranid_boots_c,  itm_tzeentch_chosen_leg,       itm_tzeentch_chosen_head,itm_tzeentch_chosen_hand,   itm_mark_chaos_1,      itm_magic_lightning],  knight_attrib_5,wp(300),knight_skills_5|knows_magic_power_6|knows_necromancy_6, 0x00000001bd0040c0281a899ac956b94b00000000001ec8910000000000000000, rhodok_face_older_2],

["knight_10_1", "Jarl Aedin", "Aedin", tf_hero, 0, reserved,  fac_kingdom_10, [itm_rich_outfit,  itm_berserk_armor,   itm_woolen_hose,  itm_iron_greaves2,  itm_berserk_helm, itm_plate_mittens, itm_ebony_double_axe, itm_tab_shield_round_d, itm_throwing_pike], knight_attrib_1,wp(300),knight_skills_1, 0x0000000c13002254340eb1d91159392d00000000001eb75a0000000000000000, nord_face_middle_2],
["knight_10_2", "Jarl Irya", "Irya", tf_hero, 0, reserved,  fac_kingdom_10, [ itm_short_tunic,  itm_berserk_armor, itm_blue_hose,  itm_iron_greaves2,  itm_berserk_helm, itm_plate_mittens, itm_ebony_axe,  itm_tab_shield_round_d, itm_vk_axe],  knight_attrib_2,wp(300),knight_skills_2|knows_trainer_3, 0x0000000c1610218368e29744e9a5985b00000000001db2a10000000000000000, nord_face_old_2],
["knight_10_3", "Jarl Olaf", "Olaf", tf_hero, 0, reserved,  fac_kingdom_10, [itm_nord_warhorse, itm_rich_outfit,  itm_berserk_armor,   itm_nomad_boots,  itm_iron_greaves2, itm_plate_mittens,   itm_berserk_helm,   itm_ebony_double_axe, itm_tab_shield_round_e],  knight_attrib_3,wp(300),knight_skills_3, 0x0000000c03040289245a314b744b30a400000000001eb2a90000000000000000, nord_face_older_2],

["knight_10_4", "Jarl Reamald", "Reamald", tf_hero, 0, reserved,  fac_kingdom_10, [   itm_leather_vest,   itm_dawnguard_armor,   itm_woolen_hose,  itm_black_greaves, itm_plate_mittens,  itm_dawnguard_helmet, itm_dawnguard_hammer, itm_van_helsing_crossbow_bolt,itm_van_helsing_crossbow_auto,itm_dawnguard_shield],  knight_attrib_4,wp(300),knight_skills_4, 0x0000000c3f1001ca3d6955b26a8939a300000000001e39b60000000000000000, nord_face_older_2],
["knight_10_5", "Jarl Turya", "Turya", tf_hero, 0, reserved,  fac_kingdom_10, [  itm_highlander_armor3,   itm_berserk_armor,   itm_highlander_boot2,  itm_iron_greaves2,  itm_plate_mittens, itm_berserk_helm, itm_shaman_staff_1,itm_magic_poison_dummy, itm_magic_fire_ray_dummy], knight_attrib_5,wp(300),knight_skills_5|knows_magic_power_7|knows_magic_defence_7|knows_necromancy_4, 0x0000000ff508330546dc4a59422d450c00000000001e51340000000000000000, nord_face_older_2],

["knight_10_6", "Jarl Gundur", "Gundur", tf_hero, 0, reserved,  fac_kingdom_10, [   itm_nomad_robe,   itm_huscarl_armor,  itm_nomad_boots,  itm_iron_greaves2,   itm_nord_berserker_mask, itm_plate_mittens,   itm_knightaxe,itm_ebony_double_axe, itm_tab_shield_round_d, itm_throwing_pike],   knight_attrib_1,wp(300),knight_skills_1, 0x00000005b00011813d9b6d4a92ada53500000000001cc1180000000000000000, nord_face_middle_2],
["knight_10_7", "Jarl Harald", "Harald", tf_hero, 0, reserved,  fac_kingdom_10, [  itm_fur_coat,   itm_huscarl_armor_2,   itm_nomad_boots,  itm_iron_greaves2,  itm_nord_berserker_mask, itm_plate_mittens,   itm_longsword, itm_long_axe_c_alt,  itm_tab_shield_round_d, itm_vk_axe],   knight_attrib_2,wp(300),knight_skills_2|knows_trainer_4, 0x00000006690002873d9b6d4a92ada53500000000001cc1180000000000000000, nord_face_old_2],
["knight_10_8", "Jarl Knudarr", "Knudarr", tf_hero, 0, reserved,  fac_kingdom_10, [ itm_rich_outfit,  itm_huscarl_armor_3,   itm_woolen_hose,  itm_iron_greaves2,   itm_nord_berserker_mask, itm_plate_mittens, itm_knightaxe,itm_ebony_double_axe,  itm_tab_shield_round_e, itm_throwing_pike],   knight_attrib_3,wp(300),knight_skills_3, 0x0000000f830051c53b026e4994ae272a00000000001db4e10000000000000000, nord_face_older_2],

["knight_10_9", "Jarl Haeda", "Haeda", tf_hero, 0, reserved,  fac_kingdom_10, [ itm_nomad_robe,   itm_plate_armor, itm_blue_hose,  itm_iron_greaves2,  itm_wolfhelm_w2, itm_wolfgloves_w, itm_charonscall,   ],  knight_attrib_4,wp(300),knight_skills_4|knows_weapon_master_10|knows_stealth_5, 0x00000000080c54c1345bd21349b1b67300000000001c90c80000000000000000, nord_face_older_2],
["knight_10_10", "Jarl Turegor", "Turegor", tf_hero, 0, reserved,  fac_kingdom_10, [   itm_courtly_outfit,   itm_dawnguard_armor,   itm_nomad_boots,  itm_black_greaves, itm_plate_mittens,  itm_dawnguard_helmet,itm_dawnguard_greatsword, itm_dawnguard_sword,itm_dawnguard_javelin,itm_dawnguard_shield],  str_100|agi_32|int_21|cha_25|level(50),wp(300),knight_skills_5|knows_trainer_6|knows_stealth_3|knows_magic_power_3|knows_reserved_17_5|knows_weapon_master_8|knows_magic_defence_10, 0x000000084b0002063d9b6d4a92ada53500000000001cc1180000000000000000, nord_face_older_2],





["knight_10_11", "Jarl Logarson", "Logarson", tf_hero, 0, reserved,  fac_kingdom_10, [ itm_rich_outfit,  itm_huscarl_armor,   itm_woolen_hose,  itm_iron_greaves2,  itm_nord_norman_helmet,  itm_plate_mittens,  itm_great_bardiche, itm_tab_shield_round_d, itm_vk_axe], knight_attrib_1,wp(300),knight_skills_1, 0x000000002d100005471d4ae69ccacb1d00000000001dca550000000000000000, nord_face_middle_2],
["knight_10_12", "Jarl Aeric", "Aeric", tf_hero, 0, reserved,  fac_kingdom_10, [ itm_short_tunic,  itm_huscarl_armor_2, itm_blue_hose,  itm_iron_greaves2,  itm_nord_berserker_mask,  itm_plate_mittens,  itm_ebony_axe,  itm_tab_shield_round_d, itm_vk_axe],  knight_attrib_2,wp(300),knight_skills_2, 0x0000000b9500020824936cc51cb5bb2500000000001dd4d80000000000000000, nord_face_old_2],
["knight_10_13", "Jarl Faarn", "Faarn", tf_hero, 0, reserved,  fac_kingdom_10, [itm_nord_warhorse, itm_rich_outfit,  itm_gothic_plate_2,   itm_nomad_boots,  itm_iron_greaves2, itm_plate_mittens,   itm_nord_norman_mask,   itm_knightaxe,itm_ebony_double_axe, itm_tab_shield_round_e],  knight_attrib_3,wp(300),knight_skills_3|knows_trainer_3, 0x0000000a300012c439233512e287391d00000000001db7200000000000000000, nord_face_older_2],
["knight_10_14", "Jarl Bulba", "Bulba", tf_hero, 0, reserved,  fac_kingdom_10, [  itm_leather_vest,   itm_twiligh_armor,   itm_woolen_hose,  itm_twilight_boots,  itm_dragonpriest_helm_1, itm_twilight_gloves, itm_dragonpriest_staff_1, itm_magic_ice_ray, itm_stalhrim_greatsword],  knight_attrib_4,wp(300),knight_skills_4|knows_magic_8|knows_magic_defence_8, 0x0000000c0700414f2cb6aa36ea50a69d00000000001dc55c0000000000000000, nord_face_older_2],


["knight_10_15", "Jarl Rayeck", "Rayeck", tf_hero, 0, reserved,  fac_kingdom_10, [itm_charger_old,   itm_leather_jacket,   itm_gothic_plate_2,   itm_leather_boots, itm_plate_mittens,  itm_steel_greaves,  itm_amade_bronze_winged_helm, itm_frostfang, itm_throwing_gungnir,itm_steel_shield], knight_attrib_5|knows_reserved_17_8,wp(300),knight_skills_5|knows_trainer_6, 0x0000000d920801831715d1aa9221372300000000001ec6630000000000000000, nord_face_older_2],

["knight_10_16", "Jarl Dirigun", "Dirigun", tf_hero, 0, reserved,  fac_kingdom_10, [   itm_nomad_robe,   itm_huscarl_armor,  itm_nomad_boots,  itm_iron_greaves2,   itm_nord_berserker_mask, itm_plate_mittens,   itm_knightaxe, itm_tab_shield_round_d, itm_vk_axe],   knight_attrib_1,wp(300),knight_skills_1, 0x000000099700124239233512e287391d00000000001db7200000000000000000, nord_face_middle_2],
["knight_10_17", "Jarl Marayirr", "Marayirr", tf_hero, 0, reserved,  fac_kingdom_10, [  itm_fur_coat,   itm_huscarl_armor_2,   itm_nomad_boots,  itm_iron_greaves2,  itm_nord_berserker_mask, itm_plate_mittens,   itm_ebony_axe,  itm_tab_shield_round_d, itm_vk_axe],   knight_attrib_2,wp(300),knight_skills_2|knows_trainer_4, 0x0000000c2f0442036d232a2324b5b81400000000001e55630000000000000000, nord_face_old_2],
["knight_10_18", "Jarl Gearth", "Gearth", tf_hero, 0, reserved,  fac_kingdom_10, [ itm_rich_outfit,  itm_huscarl_armor_3,   itm_woolen_hose,  itm_iron_greaves2,   itm_nord_berserker_mask, itm_plate_mittens, itm_longsword, itm_long_axe_c_alt,  itm_tab_shield_round_d, itm_throwing_pike],   knight_attrib_3,wp(300),knight_skills_3, 0x0000000c0d00118866e22e3d9735a72600000000001eacad0000000000000000, nord_face_older_2],

["knight_10_19", "Jarl Surdun", "Surdun", tf_hero, 0, reserved,  fac_kingdom_10, [itm_nord_warhorse, itm_nomad_robe,   itm_banshen_body, itm_blue_hose,  itm_banshen_leg,  itm_demon_head, itm_banshen_hand,   itm_banshen_axe,  itm_great_lance_dark,itm_banshen_shield],  knight_attrib_4,wp(300),knight_skills_4|knows_trainer_5, 0x0000000c0308225124e26d4a6295965a00000000001d23e40000000000000000, nord_face_older_2],
["knight_10_20", "Jarl Gerlad", "Gerlad", tf_hero, 0, reserved,  fac_kingdom_10, [itm_charger_old,   itm_courtly_outfit,   itm_gothic_plate_2,   itm_nomad_boots,  itm_iron_greaves2, itm_plate_mittens,  itm_guard_helmet,itm_ebony_axe, itm_sldequiver, itm_elven_bow,itm_tab_shield_round_e],  knight_attrib_5,wp(300),knight_skills_5|knows_magic_power_5|knows_power_draw_7, 0x0000000f630052813b6bb36de5d6eb7400000000001dd72c0000000000000000, nord_face_older_2],


#["knight_11_2", "Count Gutlans", "Gutlans", tf_hero, 0, reserved,  fac_kingdom_11, [itm_charger_noble,    itm_red_gambeson,       itm_milanese_plate,    itm_leather_boots,    itm_iron_greaves2,    itm_milanese_sallet, itm_milanese_gauntlets,      itm_morningstar,  itm_sword_two_handed_a,   itm_toumingdun],     knight_attrib_2,wp(300),knight_skills_2|knows_trainer_4, 0x00000007670832103c5a6e275c92c52300000000001dbad50000000000000000, rhodok_face_old_2],
#["knight_11_3", "Count Laruqen", "Laruqen", tf_hero, 0, reserved,  fac_kingdom_11, [itm_charger_noble,     itm_short_tunic,  itm_milanese_plate,     itm_nomad_boots,      itm_iron_greaves2,  itm_milanese_sallet, itm_milanese_gauntlets, itm_two_handed_cleaver,itm_carbine_batarey_good,itm_cartridges_thrust,  itm_toumingdun],    knight_attrib_3,wp(300),knight_skills_3, 0x00000007790832496915792873f295a900000000001756da0000000000000000, rhodok_face_older_2],
#["knight_11_4", "Count Raichs", "Raichs", tf_hero, 0, reserved,  fac_kingdom_11, [itm_charger_noble,     itm_leather_jacket,     itm_milanese_plate,       itm_woolen_hose,      itm_iron_greaves2,    itm_milanese_sallet, itm_milanese_gauntlets, itm_bastard_sword_a,    itm_toumingdun],    knight_attrib_4,wp(300),knight_skills_4, 0x0000000765044405372c25a94b86b6cd00000000000dd84a0000000000000000, rhodok_face_older_2],
#["knight_11_5", "Count Reland", "Reland", tf_hero, 0, reserved,  fac_kingdom_11, [itm_charger_noble,     itm_rich_outfit,  itm_milanese_plate,     itm_leather_boots,    itm_iron_greaves2,    itm_milanese_sallet, itm_milanese_gauntlets, itm_two_handed_cleaver,  itm_toumingdun], knight_attrib_5,wp(300),knight_skills_5, 0x000000074f083144372d91a96549c4db00000000000db5890000000000000000, rhodok_face_older_2],
#["knight_11_6", "Count Tarchias", "Tarchias", tf_hero, 0, reserved,  fac_kingdom_11, [itm_charger_noble,    itm_ragged_outfit,      itm_milanese_plate,       itm_woolen_hose,      itm_iron_greaves2, itm_milanese_gauntlets,   itm_milanese_sallet,     itm_sword_two_handed_b,itm_carbine_batarey_good,itm_cartridges_thrust,   itm_toumingdun],    knight_attrib_1,wp(300),knight_skills_1, 0x00000007621001431adb9754d26ed70a00000000001e0cd50000000000000000, rhodok_face_middle_2],
#["knight_11_7", "Count Gharmall", "Gharmall", tf_hero, 0, reserved,  fac_kingdom_11, [itm_charger_noble,     itm_coarse_tunic,       itm_milanese_plate,   itm_leather_boots,    itm_mail_chausses,  itm_milanese_gauntlets,      itm_milanese_sallet,       itm_bastard_sword_a,itm_carbine_batarey_good,itm_cartridges_thrust,    itm_toumingdun],     knight_attrib_2,wp(300),knight_skills_2, 0x00000007621001431adb9754d26ed70a00000000001e0cd50000000000000000, rhodok_face_old_2],
#["knight_11_8", "Count Talbar", "Talbar", tf_hero, 0, reserved,  fac_kingdom_11, [itm_charger_noble, itm_courtly_outfit,     itm_milanese_plate,    itm_woolen_hose,      itm_iron_greaves2,    itm_milanese_sallet,  itm_milanese_gauntlets,      itm_morningstar, itm_sword_two_handed_b,  itm_toumingdun],    knight_attrib_3,wp(300),knight_skills_3|knows_trainer_3, 0x00000007641045c939b135b5528eb71c00000000001d49a20000000000000000, rhodok_face_older_2],
#["knight_11_9", "Count Rimusk", "Rimusk", tf_hero, 0, reserved,  fac_kingdom_11, [itm_charger_noble,     itm_leather_jacket,     itm_milanese_plate,   itm_leather_boots,    itm_iron_greaves2,       itm_milanese_sallet, itm_milanese_gauntlets,   itm_great_bardiche,   itm_toumingdun],   knight_attrib_4,wp(300),knight_skills_4|knows_trainer_6, 0x000000076a0c43ce5b6cb614d385491d00000000001128cf0000000000000000, rhodok_face_older_2],
#["knight_11_10", "Count Falsevor", "Falsevor", tf_hero, 0, reserved,  fac_kingdom_11, [itm_charger_noble,     itm_rich_outfit,  itm_milanese_plate,     itm_blue_hose,  itm_mail_chausses,       itm_milanese_sallet, itm_milanese_gauntlets,       itm_bastard_sword_a,   itm_toumingdun],  knight_attrib_5,wp(300),knight_skills_5|knows_trainer_4, 0x00000008e20011063d9b6d4a92ada53500000000001cc1180000000000000000, rhodok_face_older_2],
#["knight_11_11", "Count Etrosq", "Etrosq", tf_hero, 0, reserved,  fac_kingdom_11, [itm_charger_noble,     itm_tabard,       itm_milanese_plate,       itm_leather_boots,    itm_iron_greaves2,    itm_milanese_sallet,  itm_milanese_gauntlets,    itm_morningstar,itm_carbine_batarey_good,itm_cartridges_thrust,   itm_toumingdun],     knight_attrib_1,wp(300),knight_skills_1, 0x0000000c170c14874752adb6eb3228d500000000001c955c0000000000000000, rhodok_face_middle_2],
#["knight_11_12", "Count Kurnias", "Kurnias", tf_hero, 0, reserved,  fac_kingdom_11, [itm_charger_noble,    itm_red_gambeson,       itm_milanese_plate,    itm_leather_boots,    itm_iron_greaves2,    itm_milanese_sallet,  itm_milanese_gauntlets,      itm_morningstar,itm_carbine_batarey_good,itm_cartridges_thrust,   itm_toumingdun],     knight_attrib_2,wp(300),knight_skills_2|knows_trainer_5, 0x0000000c080c13d056ec8da85e3126ed00000000001d4ce60000000000000000, rhodok_face_old_2],
#["knight_11_13", "Count Tellrog", "Tellrog", tf_hero, 0, reserved,  fac_kingdom_11, [itm_charger_noble,     itm_short_tunic,  itm_milanese_plate,     itm_nomad_boots,      itm_iron_greaves2,  itm_milanese_sallet, itm_milanese_gauntlets,       itm_sword_two_handed_a,  itm_toumingdun],    knight_attrib_3,wp(300),knight_skills_3, 0x0000000cbf10100562a4954ae731588a00000000001d6b530000000000000000, rhodok_face_older_2],
#["knight_11_14", "Count Tribidan", "Tribidan", tf_hero, 0, reserved,  fac_kingdom_11, [itm_charger_noble,     itm_leather_jacket,     itm_milanese_plate,       itm_woolen_hose,      itm_iron_greaves2,    itm_milanese_sallet, itm_milanese_gauntlets, itm_bastard_sword_a,    itm_toumingdun],    knight_attrib_4,wp(300),knight_skills_4, 0x0000000c330805823baa77556c4e331a00000000001cb9110000000000000000, rhodok_face_older_2],
#["knight_11_15", "Count Gerluchs", "Gerluchs", tf_hero, 0, reserved,  fac_kingdom_11, [itm_charger_noble,     itm_rich_outfit,  itm_milanese_plate,     itm_leather_boots,    itm_iron_greaves2,    itm_milanese_sallet, itm_milanese_gauntlets,       itm_sword_two_handed_a,  itm_toumingdun], knight_attrib_5,wp(300),knight_skills_5, 0x0000000d51000106370c4d4732b536de00000000001db9280000000000000000, rhodok_face_older_2],
#["knight_11_16", "Count Fudreim", "Fudreim", tf_hero, 0, reserved,  fac_kingdom_11, [itm_charger_noble,    itm_ragged_outfit,      itm_milanese_plate,       itm_woolen_hose,      itm_iron_greaves2,    itm_guard_helmet, itm_milanese_gauntlets,     itm_morningstar,itm_carbine_batarey_good,itm_cartridges_thrust,   itm_toumingdun],    knight_attrib_1,wp(300),knight_skills_1, 0x0000000c06046151435b5122a37756a400000000001c46e50000000000000000, rhodok_face_middle_2],
#["knight_11_17", "Count Nealcha", "Nealcha", tf_hero, 0, reserved,  fac_kingdom_11, [itm_charger_noble,     itm_coarse_tunic,       itm_milanese_plate,   itm_leather_boots,    itm_mail_chausses,       itm_milanese_sallet,  itm_milanese_gauntlets,      itm_bastard_sword_a,itm_carbine_batarey_good,itm_cartridges_thrust,    itm_toumingdun],     knight_attrib_2,wp(300),knight_skills_2, 0x0000000c081001d3465c89a6a452356300000000001cda550000000000000000, rhodok_face_old_2],
#["knight_11_18", "Count Fraichin", "Fraichin", tf_hero, 0, reserved,  fac_kingdom_11, [itm_charger_noble, itm_courtly_outfit,     itm_milanese_plate,    itm_woolen_hose,      itm_iron_greaves2,    itm_milanese_sallet, itm_milanese_gauntlets,       itm_morningstar,   itm_toumingdun],    knight_attrib_3,wp(300),knight_skills_3, 0x0000000a3d0c13c3452aa967276dc95c00000000001dad350000000000000000, rhodok_face_older_2],
#["knight_11_19", "Count Trimbau", "Trimbau", tf_hero, 0, reserved,  fac_kingdom_11, [itm_charger_noble,     itm_leather_jacket,     itm_milanese_plate,   itm_leather_boots,    itm_iron_greaves2,       itm_milanese_sallet, itm_milanese_gauntlets,   itm_morningstar,  itm_sword_two_handed_a, itm_toumingdun],   knight_attrib_4,wp(300),knight_skills_4|knows_trainer_5, 0x0000000038043194092ab4b2d9adb44c00000000001e072c0000000000000000, rhodok_face_older_2],
#["knight_11_20", "Count Reichsin", "Reichsin", tf_hero, 0, reserved,  fac_kingdom_11, [itm_charger_noble,     itm_rich_outfit,  itm_milanese_plate,     itm_blue_hose,  itm_iron_greaves2,       itm_milanese_sallet, itm_milanese_gauntlets,       itm_bastard_sword_b,   itm_toumingdun],  knight_attrib_5,wp(300),knight_skills_5|knows_trainer_6, 0x000000003600420515a865b45c64d64c00000000001d544b0000000000000000, rhodok_face_older_2],

#["knight_13_2", "Knight Rutger", "Rutger", tf_hero, 0, reserved,  fac_kingdom_13, [itm_charger_old,           itm_red_gambeson,      itm_gothic_plate_nobevor,               itm_woolen_hose,            itm_iron_greaves,                    itm_new_sallet,  itm_hourglass_gauntlets,        itm_bastard_sword_a,itm_gothic_lance,    itm_toumingdun],       knight_attrib_5,wp(300),knight_skills_5, 0x0000000c351020c642548ea69b44971100000000001dbaa20000000000000000, swadian_face_young_2],
#["knight_13_3", "Knight Dietrich", "Dietrich", tf_hero, 0, reserved,  fac_kingdom_13, [itm_charger_teuton,          itm_nobleman_outfit,     itm_gothic_plate_nobevor,                 itm_leather_boots,          itm_iron_greaves2,        itm_new_sallet, itm_hourglass_gauntlets, itm_bastard_sword_b,itm_morningstar2,   itm_toumingdun],  knight_attrib_5,wp(300),knight_skills_5|knows_trainer_3, 0x00000002ff0443c43451a6284a69371c00000000001e1b320000000000000000, swadian_face_young_2],
#["knight_13_4", "Knight Poppo", "Poppo", tf_hero, 0, reserved,  fac_kingdom_13, [itm_charger_old,      itm_short_tunic,       itm_gothic_plate_nobevor,           itm_leather_boots,          itm_iron_greaves2,                   itm_new_sallet, itm_hourglass_gauntlets,       itm_bastard_sword_a,  itm_morningstar2,  itm_toumingdun],    knight_attrib_5,wp(300),knight_skills_5|knows_trainer_4, 0x00000002e2105505361c0db4d841272400000000001dc8910000000000000000, swadian_face_older_2],
#["knight_13_5", "Knight Andreas", "Andreas", tf_hero, 0, reserved,  fac_kingdom_13, [itm_charger_old,            itm_rich_outfit,        itm_gothic_plate_nobevor,itm_woolen_hose, itm_steel_greaves, itm_new_sallet, itm_hourglass_gauntlets,         itm_sword_medieval_d_long,itm_morningstar2,itm_gothic_lance,    itm_toumingdun],      knight_attrib_4,wp(300),knight_skills_4|knows_trainer_6, 0x000000087f0005d45463c53ac3cca6e400000000001dab6c0000000000000000, swadian_face_older_2],
#["knight_13_6", "Knight Hermann", "Hermann", tf_hero, 0, reserved,  fac_kingdom_13, [itm_charger_old,            itm_tabard,      itm_gothic_plate_nobevor,               itm_leather_boots,          itm_iron_greaves2,                      itm_new_sallet, itm_hourglass_gauntlets, itm_bastard_sword_b, itm_great_sword,itm_gothic_lance,  itm_toumingdun], knight_attrib_5,wp(300),knight_skills_4|knows_trainer_4, 0x000000094200159056d4aec2dca86d5400000000001ebaee0000000000000000, swadian_face_older_2],
#["knight_13_7", "Knight Birger", "Birger", tf_hero, 0, reserved,  fac_kingdom_13, [itm_charger_old,            itm_tabard,      itm_gothic_plate_nobevor,               itm_leather_boots,          itm_steel_greaves,                      itm_new_sallet, itm_hourglass_gauntlets, itm_bastard_sword_b,   itm_great_sword,itm_gothic_lance, itm_toumingdun], knight_attrib_5,wp(300),knight_skills_4|knows_trainer_4, 0x00000001ee0075cf265a6e290c91551300000000001dc8a20000000000000000, swadian_face_young_2],
#["knight_13_8", "Knight Ulf", "Ulf", tf_hero, 0, reserved,  fac_kingdom_13, [itm_charger_old,          itm_nobleman_outfit,     itm_gothic_plate_nobevor,                 itm_leather_boots,          itm_iron_greaves2,        itm_new_sallet,  itm_hourglass_gauntlets,itm_bastard_sword_b,  itm_great_sword, itm_gothic_lance, itm_toumingdun],  knight_attrib_4,wp(300),knight_skills_4, 0x000000098009f1922493a5b2d3a4b91b00000000001ea8f90000000000000000, swadian_face_older_2],

#Swadian younger knights

#Swadian younger knights
#["knight_13_9", "Knight Knut", "Knut", tf_hero, 0, reserved,  fac_kingdom_13, [itm_charger_teuton,      itm_gambeson,     itm_gondor_armor_med,                 itm_blue_hose,              itm_iron_greaves2,                      itm_hounskull_3,  itm_hourglass_gauntlets,     itm_morningstar,itm_great_lance,   itm_tab_shield_heater_c],    knight_attrib_3,wp(300),knight_skills_3, 0x00000004850493072714694b408cb7a000000000001dcaf40000000000000000, swadian_face_old_2],
#["knight_13_10", "Knight Mirchaud", "Mirchaud", tf_hero, 0, reserved,  fac_kingdom_13, [itm_charger_teuton,           itm_gambeson,        itm_gondor_armor_med,                   itm_woolen_hose,            itm_iron_greaves2,                   itm_winged_great_helmet_teu,    itm_hourglass_gauntlets,    itm_sword_two_handed_b,itm_great_lance,        itm_tab_shield_heater_cav_b],   knight_attrib_3,wp(300),knight_skills_3, 0x0000000101142103331fa9c90444272300000000001d28da0000000000000000, swadian_face_older_2],
#["knight_13_11", "Knight Abel", "Abel", tf_hero, 0, reserved,  fac_kingdom_13, [itm_charger_teuton,           itm_red_gambeson,      itm_gondor_armor_med,               itm_woolen_hose,            itm_iron_greaves,                    itm_winged_great_helmet_teu,   itm_hourglass_gauntlets,       itm_bastard_sword_a,itm_great_lance,    itm_tab_shield_heater_cav_b],       knight_attrib_3,wp(300),knight_skills_3, 0x000000026b05308f20d4ea38ca8cb71b00000000001db8a20000000000000000, swadian_face_older_2],
#["knight_13_12", "Knight Berlewin", "Berlewin", tf_hero, 0, reserved,  fac_kingdom_13, [itm_charger_teuton,      itm_rich_outfit,        itm_gondor_armor_med,                    itm_woolen_hose,            itm_iron_greaves2,                      itm_winged_great_helmet_teu,   itm_hourglass_gauntlets,         itm_morningstar,itm_great_lance,   itm_tab_shield_heater_c],    knight_attrib_3,wp(300),knight_skills_3, 0x000000059b0440d4371a8dc8db48189200000000001e48ac0000000000000000, swadian_face_older_2],


#["knight_13_13", "Knight Beranz", "Beranz", tf_hero, 0, reserved,  fac_kingdom_13, [itm_charger_teuton,      itm_ragged_outfit,      itm_half_plates,           itm_woolen_hose,            itm_iron_greaves2,                itm_hounskull_3,   itm_hourglass_gauntlets,         itm_sword_medieval_d_long,  itm_sword_two_handed_a,     itm_tab_shield_heater_c],   knight_attrib_2,wp(300),knight_skills_2, 0x0000000bff09601018a48e28c390c8b400000000001ecceb0000000000000000, swadian_face_older_2],
#["knight_13_14", "Knight Rafard", "Henricus", tf_hero, 0, reserved,  fac_kingdom_13, [itm_charger_teuton,      itm_short_tunic,       itm_half_plates,           itm_leather_boots,          itm_iron_greaves2,                   itm_hounskull_3,  itm_hourglass_gauntlets,     itm_bastard_sword_a, itm_great_lance_dark,   itm_tab_shield_heater_cav_a],    knight_attrib_2,wp(300),knight_skills_3|knows_trainer_6, 0x0000000e4a152504469e31b90564c3a300000000001e4b220000000000000000, swadian_face_older_2],
#["knight_13_15", "Knight Rudolf", "Rudolf", tf_hero, 0, reserved,  fac_kingdom_13, [itm_charger_teuton,            itm_rich_outfit,        itm_half_plates,                   itm_woolen_hose,            itm_iron_greaves2,                   itm_great_helmet,   itm_hourglass_gauntlets,       itm_sword_viking_3, itm_sword_two_handed_a,  itm_tab_shield_heater_d],      knight_attrib_4,wp(300),knight_skills_2, 0x00000008b90035d244a02b36912cb79500000000001ec9530000000000000000, swadian_face_young_2],
#["knight_13_16", "Knight Rembold", "Rembold", tf_hero, 0, reserved,  fac_kingdom_13, [itm_charger_teuton,      itm_courtly_outfit,      itm_half_plates,                     itm_woolen_hose,            itm_iron_greaves2,                itm_great_helmet,   itm_hourglass_gauntlets,         itm_sword_medieval_d_long,    itm_great_lance_dark,       itm_tab_shield_heater_c],   knight_attrib_1,wp(300),knight_skills_2, 0x00000005bf0054c545648b36902cb70a00000000001ec95b0000000000000000, swadian_face_young_2],
#["knight_13_17", "Knight Rafarch", "Rafarch", tf_hero, 0, reserved,  fac_kingdom_13, [itm_charger_teuton,      itm_gambeson,     itm_half_plates,                 itm_blue_hose,              itm_iron_greaves2,                      itm_hounskull_3,   itm_hourglass_gauntlets,    itm_morningstar, itm_great_lance_dark,  itm_tab_shield_heater_cav_b],    knight_attrib_2,wp(300),knight_skills_1|knows_trainer_4, 0x0000000900081086173c893d1050b72100000000001d48f30000000000000000, swadian_face_young_2],

#["knight_13_18", "Knight Rochabarth", "Rochabarth", tf_hero, 0, reserved,  fac_kingdom_13, [itm_charger_teuton,           itm_gambeson,        itm_gondor_armor_med,                   itm_woolen_hose,            itm_iron_greaves2,                   itm_winged_great_helmet_teu,   itm_hourglass_gauntlets,     itm_sword_two_handed_a,itm_great_lance,        itm_tab_shield_heater_cav_a],   knight_attrib_3,wp(300),knight_skills_1, 0x00000004ff08a00e2ad225648c2cbacb00000000001e26d90000000000000000, swadian_face_young_2],

#["knight_13_19", "Knight Gerburg", "Gerburg", tf_hero, 0, reserved,  fac_kingdom_13, [itm_charger_teuton,      itm_rich_outfit,        itm_half_plates,                    itm_woolen_hose,            itm_iron_greaves2,                      itm_great_helmet, itm_hourglass_gauntlets,           itm_morningstar,  itm_sword_two_handed_a, itm_tab_shield_heater_cav_a],    knight_attrib_1,wp(300),knight_skills_1, 0x0000000dbf10218527244a370a49baa300000000001f18ea0000000000000000, swadian_face_young_2],
#["knight_13_20", "Knight Montewar", "Heinrich", tf_hero, 0, reserved,  fac_kingdom_13, [itm_charger_teuton,      itm_ragged_outfit,      itm_half_plates,           itm_woolen_hose,            itm_iron_greaves2,                itm_hounskull_3, itm_hourglass_gauntlets,           itm_sword_medieval_d_long,   itm_sword_two_handed_a,   itm_tab_shield_heater_cav_a],   knight_attrib_2,wp(300),knight_skills_1, 0x00000006f61135c6425ba5c71b48b52200000000001f3aa40000000000000000, swadian_face_young_2],



#["knight_14_2", "Boyar Ivan", "Ivan", tf_hero, 0, reserved,  fac_kingdom_14, [itm_vaegir_charger,      itm_rich_outfit,        itm_vaegir_elite_armor,               itm_woolen_hose,            itm_iron_greaves,                   itm_vaegir_noble_helmet,  itm_lamellar_gauntlets,      itm_great_bardiche, itm_scimitar_sulatn,   itm_tab_shield_kite_cav_a],    knight_attrib_2,wp(300),knight_skills_2, 0x0000000a1c0c218524e288999b69b75400000000001cd4ec0000000000000000, vaegir_face_old_2],
#["knight_14_3", "Boyar Miloslav", "Miloslav", tf_hero, 0, reserved,  fac_kingdom_14, [itm_vaegir_charger,            itm_short_tunic,        itm_vaegir_elite_armor,                   itm_woolen_hose,            itm_iron_greaves,                   itm_litchina_helm, itm_lamellar_gauntlets,           itm_great_bardiche, itm_scimitar_sulatn,           itm_tab_shield_kite_cav_b],     knight_attrib_3,wp(300),knight_skills_3, 0x0000000a7500535066d3939d46e0b6c400000000001fd61f0000000000000000, vaegir_face_older_2],
#["knight_14_4", "Boyar Yuri", "Yuri", tf_hero, 0, reserved,  fac_kingdom_14, [itm_vaegir_charger,      itm_courtly_outfit,     itm_vaegir_elite_armor,               itm_rus_shoes,          itm_iron_greaves,                      itm_vaegir_noble_helmet, itm_lamellar_gauntlets,         itm_scimitar_long,   itm_tab_shield_kite_cav_b],    knight_attrib_4,wp(300),knight_skills_4, 0x0000000c2f0832c748f272540d8ab65900000000001d34e60000000000000000, vaegir_face_older_2],
#["knight_14_5", "Boyar Alekseev", "Alekseev", tf_hero, 0, reserved,  fac_kingdom_14, [itm_vaegir_charger,            itm_rich_outfit,        itm_vaegir_elite_armor,                     itm_rus_shoes,          itm_iron_greaves,                   itm_vaegir_noble_helmet, itm_scale_gauntlets,   itm_scimitar_long,   itm_tab_shield_kite_d],       knight_attrib_5,wp(300),knight_skills_5, 0x0000000c7f006350471b889ecf49fadf00000000001d99bb0000000000000000, vaegir_face_older_2],
#["knight_14_6", "Boyar Buiakov", "Buiakov", tf_hero, 0, reserved,  fac_kingdom_14, [itm_vaegir_charger,      itm_nomad_vest,      itm_vaegir_elite_armor,                   itm_woolen_hose,            itm_iron_greaves,                   itm_litchina_helm,  itm_lamellar_gauntlets,          itm_sword_viking_3,           itm_tab_shield_kite_c],   knight_attrib_1,wp(300),knight_skills_1|knows_trainer_3, 0x000000099408534e14a421c9526ecd2200000000001c98dc0000000000000000, vaegir_face_middle_2],
#["knight_14_7", "Boyar Domazhirov", "Domazhirov", tf_hero, 0, reserved,  fac_kingdom_14, [itm_vaegir_charger,      itm_leather_jacket,     itm_vaegir_elite_armor,                   itm_rus_shoes,          itm_iron_greaves,                      itm_vaegir_noble_helmet,  itm_lamellar_gauntlets,          itm_great_bardiche, itm_scimitar_sulatn,    itm_tab_shield_kite_cav_a],     knight_attrib_2,wp(300),knight_skills_2|knows_trainer_4, 0x0000000a750c23502f1372d152952d1b00000000001db0a40000000000000000, vaegir_face_old_2],
#["knight_14_8", "Boyar Ivanov", "Ivanov", tf_hero, 0, reserved,  fac_kingdom_14, [itm_vaegir_charger,            itm_nomad_robe,             itm_vaegir_elite_armor,                     itm_woolen_hose,            itm_iron_greaves,                   itm_vaegir_noble_helmet, itm_lamellar_gauntlets,       itm_great_bardiche,    itm_tab_shield_kite_d],    knight_attrib_3,wp(300),knight_skills_3|knows_trainer_5, 0x0000000f450c135b254b512853d578dd00000000001ea2f40000000000000000, vaegir_face_older_2],
#["knight_14_9", "Boyar Kozlov", "Kozlov", tf_hero, 0, reserved,  fac_kingdom_14, [itm_vaegir_charger,      itm_rich_outfit,        itm_vaegir_elite_armor,                     itm_rus_shoes,          itm_iron_greaves,                   itm_litchina_helm,  itm_lamellar_gauntlets,        itm_great_bardiche, itm_scimitar_sulatn,   itm_tab_shield_kite_d],    knight_attrib_4,wp(300),knight_skills_4, 0x00000006c40c418e569a91b9052cbefb00000000001f46230000000000000000, vaegir_face_older_2],
#["knight_14_10", "Boyar Maksimov", "Maksimov", tf_hero, 0, reserved,  fac_kingdom_14, [itm_vaegir_charger,          itm_kuyak,        itm_vaegir_elite_armor,               itm_woolen_hose,            itm_iron_greaves,                      itm_vaegir_noble_helmet,  itm_scale_gauntlets,      itm_morningstar,   itm_tab_shield_kite_cav_b],      knight_attrib_5,wp(300),knight_skills_5|knows_trainer_6, 0x0000000ed000039a565e6a3dd94c592400000000001db7ac0000000000000000, vaegir_face_older_2],
#["knight_14_11", "Boyar Malov", "Malov", tf_hero, 0, reserved,  fac_kingdom_14, [itm_vaegir_charger,      itm_leather_jacket,     itm_vaegir_elite_armor,                   itm_nomad_boots,            itm_iron_greaves,        itm_vaegir_noble_helmet, itm_scale_gauntlets,           itm_sword_viking_3,           itm_tab_shield_kite_cav_a],    knight_attrib_1,wp(300),knight_skills_1, 0x0000000f7c00534a55324a249a864ae500000000001ecda90000000000000000, vaegir_face_middle_2],
#["knight_14_12", "Boyar Chernekov", "Chernekov", tf_hero, 0, reserved,  fac_kingdom_14, [itm_vaegir_charger,      itm_rich_outfit,        itm_vaegir_elite_armor,               itm_woolen_hose,            itm_iron_greaves,                   itm_vaegir_noble_helmet,  itm_lamellar_gauntlets,      itm_great_bardiche, itm_scimitar_sulatn,    itm_tab_shield_kite_cav_a],    knight_attrib_2,wp(300),knight_skills_2, 0x00000004d400029b37dba53b4541be3f00000000001e95730000000000000000, vaegir_face_old_2],
#["knight_14_13", "Boyar Malov", "Malov", tf_hero, 0, reserved,  fac_kingdom_14, [itm_vaegir_charger,            itm_short_tunic,        itm_vaegir_elite_armor,                   itm_woolen_hose,            itm_iron_greaves,                   itm_litchina_helm,  itm_lamellar_gauntlets,          itm_great_bardiche, itm_scimitar_sulatn,           itm_tab_shield_kite_cav_b],     knight_attrib_3,wp(300),knight_skills_3, 0x000000011d00431d16956eb692f1486c00000000001e42a40000000000000000, vaegir_face_older_2],
#["knight_14_14", "Boyar Shchuka", "Shchuka", tf_hero, 0, reserved,  fac_kingdom_14, [itm_vaegir_charger,      itm_courtly_outfit,     itm_vaegir_elite_armor,               itm_rus_shoes,          itm_iron_greaves,                      itm_vaegir_noble_helmet,  itm_lamellar_gauntlets,        itm_great_bardiche,   itm_tab_shield_kite_cav_b],    knight_attrib_4,wp(300),knight_skills_4|knows_trainer_6, 0x0000000f3b0c328e4a898895854e22b300000000001cd6ad0000000000000000, vaegir_face_older_2],
#["knight_14_15", "Boyar Nezhkov", "Nezhkov", tf_hero, 0, reserved,  fac_kingdom_14, [itm_vaegir_charger,            itm_rich_outfit,        itm_vaegir_elite_armor,                     itm_rus_shoes,          itm_iron_greaves,                   itm_litchina_helm, itm_lamellar_gauntlets,   itm_scimitar_long,  itm_great_bardiche, itm_tab_shield_kite_cav_b],       knight_attrib_5,wp(300),knight_skills_5, 0x00000008540c058646b4acc512c2f66d00000000001f174d0000000000000000, vaegir_face_older_2],
#["knight_14_16", "Boyar Sidorov", "Sidorov", tf_hero, 0, reserved,  fac_kingdom_14, [itm_vaegir_charger,      itm_nomad_vest,      itm_vaegir_elite_armor,                   itm_woolen_hose,            itm_iron_greaves,                   itm_vaegir_noble_helmet,  itm_lamellar_gauntlets,          itm_great_bardiche, itm_scimitar_sulatn,           itm_tab_shield_kite_c],   knight_attrib_1,wp(300),knight_skills_1, 0x000000035400130e36dc6db71ba1831b00000000001d862b0000000000000000, vaegir_face_middle_2],
#["knight_14_17", "Boyar Vasilievich", "Vasilievich", tf_hero, 0, reserved,  fac_kingdom_14, [itm_vaegir_charger,      itm_leather_jacket,     itm_vaegir_elite_armor,                   itm_rus_shoes,          itm_iron_greaves,                      itm_vaegir_noble_helmet,   itm_scale_gauntlets,         itm_great_bardiche, itm_scimitar_sulatn,    itm_tab_shield_kite_cav_a],     knight_attrib_2,wp(300),knight_skills_2, 0x00000003ff0012d83742a93ddcc6b4ce00000000001e922f0000000000000000, vaegir_face_old_2],
#["knight_14_18", "Boyar Orekhov", "Orekhov", tf_hero, 0, reserved,  fac_kingdom_14, [itm_vaegir_charger,            itm_nomad_robe,             itm_nomad_vest,                     itm_woolen_hose,            itm_iron_greaves,                   itm_litchina_helm,  itm_lamellar_gauntlets,      itm_great_bardiche, itm_scimitar_sulatn,    itm_tab_shield_kite_cav_a],    knight_attrib_3,wp(300),knight_skills_3, 0x0000000b670012c23d9b6d4a92ada53500000000001cc1180000000000000000, vaegir_face_older_2],
#["knight_14_19", "Boyar Zubov", "Zubov", tf_hero, 0, reserved,  fac_kingdom_14, [itm_vaegir_charger,      itm_rich_outfit,        itm_vaegir_elite_armor,                     itm_rus_shoes,          itm_iron_greaves,                   itm_vaegir_noble_helmet, itm_scale_gauntlets,         itm_morningstar,  itm_great_bardiche, itm_tab_shield_kite_d],    knight_attrib_4,wp(300),knight_skills_4|knows_trainer_4, 0x000000096a08135016a38edca3adccf300000000001dc96b0000000000000000, vaegir_face_older_2],
#["knight_14_20", "Boyar Zavid", "Zavid", tf_hero, 0, reserved,  fac_kingdom_14, [itm_vaegir_charger,          itm_kuyak,        itm_vaegir_elite_armor,               itm_woolen_hose,            itm_iron_greaves,                      itm_litchina_helm,  itm_lamellar_gauntlets,      itm_great_bardiche, itm_scimitar_sulatn,   itm_tab_shield_kite_cav_b],      knight_attrib_5,wp(300),knight_skills_5|knows_trainer_5, 0x0000000b8c00034e77da74df4f04375b00000000001cdbae0000000000000000, vaegir_face_older_2],

["kingdom_1_pretender",  "Lady Isolla of Suno",       "Isolla",  tf_hero|tf_female|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_1,[itm_charger,   itm_rich_outfit,  itm_blue_hose,      itm_iron_greaves,         itm_mail_shirt,      itm_bastard_sword_b,      itm_tab_shield_small_round_c,       itm_bascinet],          lord_attrib,wp(300),knight_skills_5, 0x00000000ef00000237dc71b90c31631200000000001e371b0000000000000000],
#claims pre-salic descent

["kingdom_2_pretender",  "Prince Valdym the Bastard", "Valdym",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_2,[itm_hunter,    itm_courtly_outfit,      itm_leather_boots,              itm_mail_chausses,              itm_lamellar_armor,       itm_military_pick,      itm_tab_shield_heater_b,      itm_bascinet_coif],    lord_attrib,wp(300),knight_skills_5, 0x00000000200412142452ed631b30365c00000000001c94e80000000000000000, vaegir_face_middle_2],
#had his patrimony falsified

["kingdom_3_pretender",  "Dustum Khan",               "Dustum",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_3,[itm_courser,   itm_nomad_robe,             itm_leather_boots,              itm_splinted_greaves,           itm_khergit_guard_armor,         itm_sword_khergit_2,              itm_tab_shield_small_round_c,       itm_sarranid_horseman_helmet],      lord_attrib,wp(300),knight_skills_5, 0x000000065504310b30d556b51238f66100000000001c256d0000000000000000, khergit_face_middle_2],
#of the family

["kingdom_4_pretender",  "Lethwin Far-Seeker",   "Lethwin",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_4,[itm_hunter,    itm_tabard,    itm_leather_boots,              itm_mail_boots,                 itm_brigandine_blue,           itm_bastard_sword_e,           itm_tab_shield_heater_cav_a,    itm_kettle_hat],            lord_attrib,wp(300),knight_skills_5, 0x00000004340c01841d89949529a6776a00000000001c910a0000000000000000, nord_face_young_2],
#dispossessed and wronged

["kingdom_5_pretender",  "Lord Kastor of Veluca",  "Kastor",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_5,[itm_warhorse,  itm_nobleman_outfit,             itm_leather_boots,              itm_splinted_leather_greaves,   itm_heraldic_mail_with_surcoat,           itm_bastard_sword_a,         itm_tab_shield_heater_d,        itm_spiked_helmet],         lord_attrib,wp(300),knight_skills_5, 0x0000000bed1031051da9abc49ecce25e00000000001e98680000000000000000, rhodok_face_old_2],
#republican

["kingdom_6_pretender",  "Arwa the Pearled One",       "Arwa",  tf_hero|tf_female|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_6,[itm_arabian_horse_b, itm_sarranid_mail_shirt, itm_sarranid_boots_c, itm_sarranid_cavalry_sword,      itm_tab_shield_small_round_c],          lord_attrib,wp(300),knight_skills_5, 0x000000050b003004072d51c293a9a70b00000000001dd6a90000000000000000],

["adventurer_troop_1","White evil","White evil", tf_vampire|tf_hero|tf_unmoveable_in_party_window,0,0,fac_commoners,
 [
  itm_gwilith,itm_werewolfclaw_dual_w,itm_magic_spirit_leech,itm_gold_dragon_sword,
  itm_wight_body,itm_demon_foot,itm_demon_head,itm_death_hand
 ],
 horse_attrib_5|level(35),wp(450),knows_knight_2|knows_assasin_7|knows_magic_defence_10,
 0x0000000fc000938936db6db6db6db6db00000000001db6db0000000000000000,swadian_face_old_2
],

["adventurer_troop_2","rat the Invincible","rat the Invincible", tf_hero|tf_unmoveable_in_party_window,0,0,fac_commoners,
 [
  itm_rat_king_skin, itm_rus_splint_greaves,itm_rathelm3, itm_wolfgloves, 
  itm_frostmourne, itm_gungnir,itm_pegasus, itm_van_helsing_crossbow_bolt, itm_van_helsing_crossbow,
 ],
 str_30|agi_30|int_3|cha_3|level(35),wp(250),knows_knight_4|knows_horse_shoot_10|knows_crossbowman_8|knows_magic_power_4|knows_magic_defence_4,
 0x0000000fc000938936db6db6db6db6db00000000001db6db0000000000000000
],

["adventurer_troop_3","The duke of wax gourd","The duke of wax gourd", tf_hero|tf_unmoveable_in_party_window,0,0,fac_commoners,[itm_great_lance2,itm_excalibur_2,itm_dragon_shield_2,itm_vk_axe,itm_armor_demi_griffin,itm_command_helm,itm_dragon_heart_plate,itm_dragon_foot,itm_drakons_lesson],str_50|agi_50|int_12|cha_12|level(40),wp(300),knows_knight_foot_5|knows_twohand_7|knows_reserved_17_5|knows_shield_6,0x000000043f0084c036db6db6db6db6db00000000001db6db0000000000000000],

["adventurer_troop_4","Caesar the Dragon Emperor", "Caesar the Dragon Emperor", tf_vampire|tf_hero|tf_unmoveable_in_party_window,0,0,fac_commoners,
 [
    itm_aurora_blade, itm_dragonpriest_staff_1,itm_magic_ice_ray, 
    itm_twilight_boots,itm_draugr_hand,
    itm_dragonpriest_armor,itm_dragonpriest_helm_1,
 ],
 str_35|agi_24|int_50|cha_4|level(45),wp_melee(300)|wp_firearm(300),knows_knight_4|knows_twohand_7|knows_magic_8|knows_magic_defence_10,
 0x000000018000324428db8a431491472400000000001e44a90000000000000000
],

["adventurer_troop_5","Terry the Wiseman","Terry the Wiseman", tf_ogre|tf_hero|tf_unmoveable_in_party_window,0,0,fac_commoners,
 [
  #itm_shaman_staff_1, itm_magic_pyroblast,itm_magic_apocalypse, itm_burning_axe, 
  itm_shaman_staff_1, itm_magic_book_5,itm_magic_poison_dummy, itm_burning_axe, 
  itm_ogre_barbar_helm, itm_ogre_boots_02, itm_ogre_armor,
 ],
 str_21|agi_21|int_100|cha_3|level(45),wp(250),knows_knight_4|knows_horse_shoot_10|knows_crossbowman_8|knows_magic_power_4|knows_magic_defence_4|knows_magic_skill_8,
 0x0000000fff00030736db6db6db6db6d000000000001db6c70000000000000000
],

["adventurer_troop_6","Darus Blanke","Darus Blanke", tf_hero|tf_unmoveable_in_party_window,0,0,fac_commoners,[itm_great_lance2,itm_skycutter,itm_vanguard_shield,itm_charger_noble,itm_winged_great_helmet_blue,itm_knight_plate_4,itm_iron_greaves2,itm_gondor_gauntlets],str_50|agi_50|int_20|cha_21|level(45),wp(300),knows_knight_foot_5|knows_twohand_7|knows_trade_5|knows_looting_5|knows_shield_6,0x000000000000c00736db6db6db6db6db00000000001db6f00000000000000000,swadian_face_old_2],

["adventurer_troop_7","Sugar the Minotaur","Sugar the Minotaur", tf_hero|tf_unmoveable_in_party_window,0,0,fac_commoners,
 [
  itm_throwing_gungnir,itm_lordaeron, itm_charonscall, 
  itm_nord_berserker_mask, itm_fast_travel_boot, itm_dawnguard_armor,itm_giant_gauntlets,
 ],
 str_40|agi_60|int_10|cha_10|level(45),wp_melee(500)|wp_throwing(450),knows_knight_foot_2|knows_twohand_9|knows_stealth_7|knows_magic_power_5|knows_reserved_17_7|knows_weapon_master_8|knows_magic_defence_10, nord_face_younger_1,
 0x00000001bd00215436db6db6db6db6db00000000001db6db0000000000000000
],

["adventurer_troop_8","Dawn the Trial","Terry the Trial", tf_hero|tf_unmoveable_in_party_window,0,0,fac_commoners,
 [
  itm_war_clerics_warhammer_cast_2, itm_magic_burning_gaze,itm_magic_burning_gaze, itm_dawnbreaker, 
  itm_toumingtou, itm_iron_greaves, itm_dawnguard_armor,itm_hourglass_gauntlets,
 ],
 str_50|agi_50|int_50|cha_10|level(30),wp(300),knows_knight_4|knows_twohand_8|knows_magic_power_7|knows_necromancy_5|knows_magic_defence_10|knows_magic_skill_10,
 0x0000000f45041105241acd2b5a66a86900000000001e98310000000000000000
],
   
["adventurer_troop_9","Cain the murderer","Cain the murderer", tf_vampire|tf_hero|tf_unmoveable_in_party_window,0,0,fac_commoners,
 [
  itm_great_lance2, itm_ebony_blade,itm_dragon_shield_2, itm_soul_stealer, 
  itm_twilight_helm, itm_black_knight_foot, itm_black_knight_plate,itm_black_knight_hand,itm_undead_charger,
 ],
 str_60|agi_60|int_10|cha_10|level(50),wp_melee(400),knows_knight_foot_7|knows_twohand_9|knows_vampire_7|knows_stealth_10|knows_necromancy_10|knows_weapon_master_10|knows_magic_defence_10, nord_face_younger_1,
 0x00000001bd00215436db6db6db6db6db00000000001db6db0000000000000000
],

["adventurer_troop_10","Hawkeye the Ranger","Hawkeye the Ranger", tf_male_elf|tf_hero|tf_unmoveable_in_party_window,0,0,fac_commoners,
 [
  itm_woodelf_mutil_arrows,itm_auriels_bow,itm_swiftness_sword,itm_woodelf_arrows_freezing,
  itm_lorien_royal_archer,itm_spellbreak_armor,itm_gold_elf_hand,itm_fast_travel_boot
 ],
 str_60|agi_60|int_10|cha_10|level(45),wp_melee(350)|wp_archery(500),knows_magic_power_6|knows_horse_archery_5|knows_knight_3|knows_ranger_8|knows_power_draw_10|knows_magic_defence_10,
 0x00000007280844c648a38ca6ac79daa500000000001d58da0000000000000000,mirkwood_elf_face_2
],

["adventurer_troop_11","morered the Chosen of Khorne","morered the Chosen of Khorne", tf_demon_human|tf_hero|tf_unmoveable_in_party_window,0,0,fac_commoners,
 [
  itm_khorne_axe,itm_hellskull, itm_chaos_sword5, 
  itm_crimson_guard_plate, itm_barrier_leg, itm_khorne_helm,itm_satanic_hand,itm_hell_nightmare,
 ],
 str_80|agi_40|int_12|cha_12|level(60),wp(500)|wp_throwing(450),knows_knight_foot_4|knows_twohand_9|knows_magic_power_3|knight_skills_5, 0x00000001bd00215436db6db6db6db6db00000000001db6db0000000000000000,
],

["adventurer_troop_12","mira the Darkness Sword Song","mira the Darkness Sword Song", tf_female_elf|tf_hero|tf_unmoveable_in_party_window,0,0,fac_commoners,
 [
    itm_grief_1,itm_magic_ice_ray,
    itm_xenoargh_mask_black,itm_grim_raider_armor_2,
    itm_demon_foot,itm_drow_elite_gloves,
 ],
 str_40|agi_50|int_40|cha_20|level(60),wp_melee(400)|wp_firearm(450),knows_knight_foot_4|knows_assasin_9|knows_magic_power_10|knows_riding_7|knows_prisoner_management_3|knows_leadership_13|knows_pathfinding_5|knows_trade_4|knows_magic_defence_10|knows_magic_skill_10, mirkwood_elf_face_1,mirkwood_elf_face_2],

["adventurer_troop_13", "gitilla the hunter","gitilla the hunter", tf_orc|tf_hero, 0, reserved,  fac_commoners, 
  [itm_orcbigboss_armour, itm_orc_heavy_helm2, itm_steel_shield, itm_orc_heavy_boots,itm_vk_axe,itm_burning_axe], 
  horse_attrib_6|level(50),wp(400),knows_riding_7|knows_prisoner_management_3|knows_leadership_13|knows_pathfinding_5|knows_trade_4|knows_magic_defence_10|knows_trainer_6|knows_twohand_8|knows_reserved_17_5|knows_weapon_master_3, 
    0x00000007C9003109207000000000000000000000001C80470000000000000000, 0x0000000FFF0061CD6D7FFBDF9DF6EBEE00000000001FFB7F0000000000000000,],


["adventurer_troop_14","Ripper Gog Fargo","Ripper Gog Fargo", tf_ogre|tf_hero|tf_unmoveable_in_party_window,0,0,fac_commoners,
 [
  itm_slaughter_axe,itm_vanguard_shield, itm_orc_greatsword, 
  itm_ogre_barbar_helm, itm_ogre_boots_02, itm_ogre_armor,
 ],
 str_100|agi_50|int_5|cha_3|level(50),wp(500),knows_knight_4|knows_twohand_9|knows_weapon_master_10|knows_magic_defence_10,
 0x0000000fff00030736db6db6db6db6d000000000001db6c70000000000000000
],

["adventurer_troop_15","kugath the Plague Father","kugath the Plague Father", tf_demon_human|tf_hero|tf_unmoveable_in_party_window,0,0,fac_commoners,
 [
  itm_plague_staff_1,itm_magic_stream_of_corruption, itm_magic_spirit_leech, itm_magic_spirit_leech, 
  itm_shadow_robes, itm_black_knight_foot, itm_frankenstein_head,itm_death_finger,
 ],
 str_80|agi_40|int_60|cha_12|level(60),wp(500)|wp_firearm(450),knows_knight_foot_4|knows_twohand_9|knight_skills_5|knows_magic_power_10|knows_necromancy_9|knows_magic_skill_10, 0x0000000c3c0821c647264ab6e68dc4d500000000001e42590000000000000000,
],

["adventurer_troop_16","Terry the Lazywolf","Terry the Lazywolf", tf_hero|tf_unmoveable_in_party_window,0,0,fac_commoners,
 [
  itm_natalya_slayer,itm_natalya_mark, itm_sissofbattle_holy_granata, itm_blinding_sand, 
  itm_emp_wh_armor1, itm_nilfurs_boast, itm_siss_cap,itm_marksman_gloves,itm_wolf_mount_black,
 ],
 str_30|agi_30|int_10|cha_30|level(25),wp(200)|wp_crossbow(300)|wp_firearm(300),knows_precise_shot_10|knows_magic_defence_10|knows_stealth_5|knows_physique_2|knows_power_strike_8|knows_ironflesh_3|knows_horse_archery_5|knows_reserved_18_10|knows_weapon_master_5|knows_magic_power_8|knows_necromancy_5|knows_magic_skill_5|knows_undead_master_5|knows_pathfinding_5, 0x000000003f0080144adb9d38db2db4cb00000000001cb92b0000000000000000,
],

["adventurer_troop_17","Darus Blanke","Darus Blanke", tf_hero|tf_unmoveable_in_party_window,0,0,fac_commoners,
 [
  itm_gothic_lance,itm_morrigan,itm_vanguard_shield,itm_charger_noble,
  itm_winged_great_helmet_blue,itm_gothic_plate,itm_steel_greaves,itm_hourglass_gauntlets
 ],
 str_50|agi_30|int_20|cha_20|level(40),wp(300),knows_knight_foot_5|knows_twohand_7|knows_magic_defence_10|knows_shield_6,0x000000000000c00736db6db6db6db6db00000000001db6f00000000000000000,swadian_face_old_2],

["adventurer_troop_18","Rogue the Siren","Rogue the Siren", tf_female_elf|tf_hero|tf_unmoveable_in_party_window,0,0,fac_commoners,
 [
    itm_slaanesh_chosen_sword_1,itm_magic_lash_of_slaanesh,itm_slaanesh_chosen_shield,
    itm_slaanesh_banshee_head,itm_slaanesh_banshee_armor,
    itm_slaanesh_witch_leg,itm_drow_elite_gloves,
 ],
 str_20|agi_35|int_40|cha_60|level(35),wp_melee(252)|wp_firearm(350),knows_physique_15|knows_shield_4|knows_power_strike_5|knows_ironflesh_5|knows_weapon_master_5|knows_stealth_10|knows_magic_defence_10|knows_assasin_9|knows_magic_power_7|knows_riding_3|knows_prisoner_management_3|knows_leadership_13|knows_pathfinding_5|knows_trade_4|knows_magic_skill_5, mirkwood_elf_face_1,mirkwood_elf_face_2],

["knight_2_1", "Boyar Vuldrat", "Vuldrat", tf_hero|tf_unmoveable_in_party_window, 0, 0,  fac_kingdom_2,
 [itm_black_dragon,      itm_kuyak,     itm_dragon_heart_plate,                   itm_nomad_boots,            itm_dragon_foot,        itm_dragon_head,    itm_dragon_knight_hand,       itm_scottish_claymore,itm_dragon_knight_lance,            itm_dragon_shield],    
 str_80|agi_22|int_12|cha_12|level(50),wp(350)|wp_melee(350),knight_skills_1|knows_knight_6|knows_spearman_8|knows_magic_power_2|knows_weapon_master_3|knows_magic_defence_5, 
 vaegir_face_middle_1, vaegir_face_middle_2
],
["knight_6_1", "Emir Uqais", "Uqais", tf_hero|tf_female, 0, reserved,  fac_kingdom_6, [itm_lamellar_warhorse,   itm_death_body,          itm_sarranid_boots_c,   itm_leather_gloves,    itm_venom_staff_1, itm_magic_book_9,   itm_magic_spirit_leech,itm_magic_spirit_leech],     knight_attrib_1,wp(300),knight_skills_5|knows_necromancy_10|knows_magic_power_5|knows_magic_defence_9, 0x000000050b003004072d51c293a9a70b00000000001dd6a90000000000000000, rhodok_face_middle_2],




["knight_11_1", "Count Matheas", "Matheas", tf_dwarf|tf_hero, 0, reserved,  fac_kingdom_10, [   itm_tabard,   itm_ironhills_guard_armor,       itm_leather_boots,    itm_guard_kneecops,    itm_dwarf_guard_helmet_1, itm_giant_gauntlets,     itm_frostfang,itm_power_musket_8barrel,   itm_cartridges_flame,itm_cartridges_rar],     str_80|knight_attrib_4,wp(300),knows_precise_shot_10|knight_skills_1|knows_trainer_3|knows_stealth_3|knows_necromancy_5|knows_magic_power_3|knows_magic_defence_10, 0x000000076104018e38dea648946da9e000000000001f345d0000000000000000, rhodok_face_middle_2],

["knight_13_1", "Knight Dietrich", "Dietrich", tf_male_elf|tf_hero, 0, reserved,  fac_elf, [itm_charger_england,      itm_courtly_outfit,      itm_glass_male_plate,   itm_woolen_hose, itm_glass_foot,       itm_glass_head,           itm_glass_long_mace,itm_trgba,itm_avalon_halberd,  itm_glass_hand,         itm_freeze_shield],   str_80|knight_attrib_5,wp(300),knight_skills_5|knows_trainer_1|knows_trainer_3|knows_weapon_master_6|knows_magic_defence_3, 0x0000000a4000b40556d5adc90950b92400000000001eb72a0000000000000000, swadian_face_older_2],

["knight_14_1", "Boyar Aleksei", "Aleksei", tf_hero, 0, reserved,  fac_kingdom_14, [      itm_ragged_outfit,     itm_berserk_armor,                               itm_fast_travel_boot,        itm_berserk_helm,    itm_death_finger,     itm_throwing_pike_melee,  itm_morrigan,itm_throwing_pike,           itm_dragon_shield_2],    knight_attrib_5,wp(300),knight_skills_5|knows_trainer_3|knows_reserved_17_5, 0x000000098b08538f46cca9aa7b6dd65d00000000001e670c0000000000000000, vaegir_face_middle_2],


#["adventurer_troop_4","Konrad","Konrad", tf_hero|tf_unmoveable_in_party_window,0,0,fac_commoners,[itm_excalibur_1,itm_mjolnir,itm_tab_shield_kite_d,itm_sallet_beret_plumes_red,itm_bane_blade_plate,itm_bane_blade_hand,itm_bane_blade_foot],str_70|agi_70|int_12|cha_12|level(50),wp(350),knows_knight_2|knows_twohand_8|knows_reserved_17_10,0x000000081700205434db6df4636db8e400000000001db6e30000000000000000,swadian_face_old_2],


#["adventurer_troop_5","Sverre","Sverre", tf_hero|tf_unmoveable_in_party_window,0,0,fac_commoners,[itm_long_axe_d,itm_frostfang,itm_throwing_pike,itm_tab_shield_round_d,itm_nordic_warlord_helmet,itm_plate_armor,itm_plate_mittens,itm_iron_greaves],horse_attrib_4|level(30),wp(200),knows_knight_2|knows_billman_6|knows_reserved_17_10,0x000000048a00024723134e24cb51c91b00000000001dc6aa0000000000000000,swadian_face_old_2],




["quick_battle_troop_1","Rodrigo de Braganca","Rodrigo de Braganca", tf_hero|tf_unmoveable_in_party_window,0,0,fac_commoners,[itm_gwilith,itm_throwing_star_b,itm_ebony_blade,itm_throwing_star_a,itm_black_hood_mask,itm_ninjia_armor,itm_light_leather_boots,itm_leather_gloves],str_40|agi_40|int_21|cha_10|level(30),wp(250),knows_knight_2|knows_assasin_6|knows_reserved_17_3,0x0000000e240070cd598bb02b9556428c00000000001eabce0000000000000000,swadian_face_old_2],

#["quick_battle_troop_2","Agustina","Agustina", tf_hero|tf_unmoveable_in_party_window|tf_female,0,0,fac_commoners,[itm_bnw_armour, itm_milanese_gauntlets,itm_combed_morion, itm_steel_greaves, itm_angel_blade, itm_charger, itm_hand_cannon_4, itm_cartridges_cannon_2, itm_cartridges_burst],horse_attrib_4|level(30),wp(200)|wp_firearm(250),knows_knight_4|knows_horse_shoot_5|knows_firearm_6|knows_necromancy_10,0x00000001800000170000000000000e0000000000000000000000000000000000],

["quick_battle_troop_2","Agustina, Battle Maiden","Agustina",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[(itm_sissofbattle_armor_red,imod_thick), (itm_satanic_hand,imod_well_made),(itm_mask_of_blades,imod_superb), (itm_guard_kneecops,imod_superb), (itm_flamberge_fire,imod_tempered), itm_lordaeron, itm_dawnguard_javelin,itm_dawnguard_javelin,
#itm_sanguine_rose, itm_sissofbattle_holy_granata
],str_50|agi_50|int_10|cha_10|level(60),wp(500),knows_stealth_12|knows_shield_10|knows_ironflesh_15|knows_power_strike_12|knows_physique_10|knows_tactics_5|knows_prisoner_management_3|knows_leadership_13|knows_trade_4|knows_weapon_master_10|knows_magic_defence_10|knows_magic_skill_14|knows_magic_power_2|knows_trainer_4,0x000000018000100900000000000006db00000000000000000000000000000000],

["quick_battle_troop_3","Hegen","Hegen", tf_hero|tf_unmoveable_in_party_window,0,0,fac_commoners,[itm_great_lance2,itm_excalibur_2,itm_amroth_sword_c,itm_akarats_awakening,itm_charger_noble,itm_winged_great_helmet_teu,itm_swan_milanese_plate,itm_iron_greaves2,itm_gondor_gauntlets],horse_attrib_6|level(40),wp(300),knows_knight_foot_5|knows_twohand_7|knows_magic_defence_10,0x000000018000324428db8a431491472400000000001e44a90000000000000000,swadian_face_old_2],

["quick_battle_troop_4","Konrad","Konrad", tf_hero|tf_unmoveable_in_party_window,0,0,fac_commoners,[itm_black_hole_sword,itm_ebony_bow,itm_ebony_mutil_arrow,itm_demon_arrow,itm_ebony_male_hand,itm_black_hole_plate,itm_ebony_male_head,itm_ebony_male_foot],str_70|agi_70|int_12|cha_30|level(81),wp(450),knows_physique_12|knows_shield_10|knows_power_strike_12|knows_ironflesh_15|knows_reserved_18_10|knows_weapon_master_8|knows_stealth_4|knows_magic_defence_10|knows_necromancy_5|knows_magic_power_8|knows_magic_skill_10|knows_power_draw_10,0x000000081700205434db6df4636db8e400000000001db6e30000000000000000,swadian_face_old_2],

["quick_battle_troop_5","Sverre","Sverre", tf_hero|tf_unmoveable_in_party_window,0,0,fac_commoners,[itm_long_axe_d,itm_frostfang,itm_throwing_pike,itm_tab_shield_round_d,itm_nordic_warlord_helmet,itm_plate_armor,itm_plate_mittens,itm_iron_greaves],horse_attrib_4|level(30),wp(200),knows_knight_2|knows_billman_6|knows_reserved_17_10,0x000000048a00024723134e24cb51c91b00000000001dc6aa0000000000000000,swadian_face_old_2],

["quick_battle_troop_6","Borislav","Borislav", tf_hero|tf_unmoveable_in_party_window,0,0,fac_commoners,[itm_woodelf_mutil_arrows,itm_elven_bow,itm_trgba,itm_sldequiver,itm_mirkwood_helm_d,itm_mirkwood_armor_f,itm_leather_gloves,itm_mirkwood_boots],horse_attrib_4|level(30),wp_melee(250)|wp_archery(400),knows_magic_power_6|knows_horse_archery_2|knows_knight_1|knows_ranger_8|knows_power_draw_10,0x0000000fc00030023fc36db75b6ab6db00000000001d36db0000000000000000,mirkwood_elf_face_2],

["quick_battle_troop_7","Stavros","Stavros", tf_male_elf|tf_hero|tf_unmoveable_in_party_window,0,0,fac_commoners,[itm_cartridges_cannon_1,itm_angel_blade,itm_hand_cannon_4,itm_cartridges_cannon_1,itm_coursera2,itm_ramun_jacket,itm_splinted_leather_greaves,itm_dwarf_crown,itm_marksman_gloves],str_25|agi_45|int_15|cha_10|level(50),wp(300),knows_ironflesh_15|knows_physique_15|knows_power_strike_4|knows_stealth_15|knows_archer_comman_10|knows_magic_defence_10|knows_precise_shot_15|knows_magic_power_15|knows_weapon_master_10|knows_pathfinding_5|knows_necromancy_4|knows_horse_shoot_5,0x00000007c0000002548c3fc49842154900000000001c92d10000000000000000,swadian_face_old_2],

["quick_battle_troop_8","Gamara","Gamara", tf_hero|tf_unmoveable_in_party_window|tf_female_elf,0,0,fac_commoners,[itm_dwarf_thunder_maul,itm_frostfang,itm_drow_shield_rider,itm_xenoargh_mask_black,itm_drow_plate,itm_drow_plate_foot,itm_giant_gauntlets],def_attrib_nobel|level(30),wp(250),knows_horse_archery_2|knows_knight_1|knows_thrown_8|knows_magic_8,0x000000015400300118d36636db6dc8e400000000001db6db0000000000000000,swadian_face_old_2],

["quick_battle_troop_9","Aethrod","Aethrod", tf_hero|tf_unmoveable_in_party_window,0,0,fac_commoners,[itm_hurricane_bow,itm_woodelf_arrows_freezing,itm_woodelf_mutil_arrows,itm_jingubang,itm_iron_greaves,itm_vaegir_elite_armor,itm_vaegir_charger_2,itm_tagancha_helm_a],def_attrib_nobel|level(30),wp(250),knows_knight_4|knows_horse_shoot_7|knows_nomad_9|knows_magic_power_6,0x000000000000210536db6db6db6db6db00000000001db6db0000000000000000,swadian_face_old_2],

["quick_battle_troop_10","Zaira","Zaira", tf_hero|tf_unmoveable_in_party_window|tf_female,0,0,fac_commoners,[itm_great_lance_dark,itm_charonscall,itm_morrigan,itm_ebony_male_hand,itm_steel_shield,itm_demon_head,itm_ebony_male_plate,itm_ebony_male_foot,itm_undead_charger_plate],def_attrib_nobel|level(30),wp(250),knows_knight_6|knows_twohand_8|knows_magic_power_5|knows_necromancy_10,0x000000034f0800110000000000000e0000000000000000000000000000000000,swadian_face_old_2],


["quick_battle_troop_11","Argo Sendnar","Argo Sendnar", tf_hero|tf_unmoveable_in_party_window,0,0,fac_commoners,[itm_holy_granata,itm_zlmg,itm_swiftness_sword,itm_cartridges_burst,itm_warhorse_german,itm_bnw_gauntlets,itm_sturmhaube_bnw4,itm_bnw_splinted_greaves,itm_bnw_armour_german],def_attrib_nobel|level(30),wp(250)|wp_firearm(300),knows_knight_3|knows_horse_archery_8|knows_firearm_8|knows_reserved_17_5|knows_necromancy_10,0x0000000e800015125adb702de3459a9c00000000001ea6d00000000000000000,swadian_face_old_2],

["quick_battle_troop_12","Argo Sendnar","Argo Sendnar", tf_hero|tf_unmoveable_in_party_window,0,0,fac_commoners,[itm_archlich_staff_1,itm_ebony_blade,itm_magic_ice_ray,itm_magic_ice_ray,itm_tzeentch_charger,itm_twilight_gloves,itm_dragonpriest_helm_1,itm_nilfurs_boast,itm_archlich_armor],def_attrib_nobel_low|level(30),wp(250)|wp_firearm(300),knows_knight_6|knows_horse_archery_8|knows_magic_8|knows_magic_skill_10,0x0000000e800015125adb702de3459a9c00000000001ea6d00000000000000000,swadian_face_old_2],

#["quick_battle_troop_12","Argo Sendnar","Argo Sendnar", tf_hero|tf_unmoveable_in_party_window,0,0,fac_commoners,[itm_archlich_staff_1,itm_magic_black_hold,itm_magic_zombie_lord,itm_magic_paralysis_cloud,itm_tzeentch_charger,itm_twilight_gloves,itm_dragonpriest_helm_1,itm_nilfurs_boast,itm_archlich_armor],def_attrib_nobel_low|level(30),wp(250)|wp_firearm(300),knows_knight_6|knows_horse_archery_8|knows_magic_8|knows_magic_skill_10,0x0000000e800015125adb702de3459a9c00000000001ea6d00000000000000000,swadian_face_old_2],

#Royal family members

["knight_1_1_wife","Error - knight_1_1_wife should not appear in game","knight_1_1_wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_commoners, [itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],

#Swadian ladies - eight mothers, eight daughters, four sisters
["kingdom_1_lady_1","Lady Anna","Anna",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [          itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
["kingdom_1_lady_2","Lady Nelda","Nelda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
["knight_1_lady_3","Lady Bela","Bela",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
["knight_1_lady_4","Lady Elina","Elina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
["kingdom_l_lady_5","Lady Constanis","Constanis",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
["kingdom_1_lady_6","Lady Vera","Vera",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
["kingdom_1_lady_7","Lady Auberina","Auberina",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
["kingdom_1_lady_8","Lady Tibal","Tibal",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
["kingdom_1_lady_9","Lady Magar","Magar",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
["kingdom_1_lady_10","Lady Thedosa","Thedosa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
["kingdom_1_lady_11","Lady Melisar","Melisar",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
["kingdom_1_lady_12","Lady Irena","Irena",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
["kingdom_l_lady_13","Lady Philenna","Philenna",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
["kingdom_1_lady_14","Lady Sonadel","Sonadel",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
["kingdom_1_lady_15","Lady Boadila","Boadila",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
["kingdom_1_lady_16","Lady Elys","Elys",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
["kingdom_1_lady_17","Lady Johana","Johana",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
["kingdom_1_lady_18","Lady Bernatys","Bernatys",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
["kingdom_1_lady_19","Lady Enricata","Enricata",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
["kingdom_1_lady_20","Lady Gaeta","Gaeta",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],

#Vaegir ladies
["kingdom_2_lady_1","Lady Junitha","Junitha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
#["kingdom_2_lady_2","Lady Katia","Katia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
#["kingdom_2_lady_3","Lady Seomis","Seomis",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
#["kingdom_2_lady_4","Lady Drina","Drina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
#["kingdom_2_lady_5","Lady Nesha","Nesha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
#["kingdom_2_lady_6","Lady Tabath","Tabath",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
#["kingdom_2_lady_7","Lady Pelaeka","Pelaeka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
#["kingdom_2_lady_8","Lady Haris","Haris",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
#["kingdom_2_lady_9","Lady Vayen","Vayen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
#["kingdom_2_lady_10","Lady Joaka","Joaka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
#["kingdom_2_lady_11","Lady Tejina","Tejina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
#["kingdom_2_lady_12","Lady Olekseia","Olekseia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [      itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
#["kingdom_2_lady_13","Lady Myntha","Myntha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
#["kingdom_2_lady_14","Lady Akilina","Akilina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
#["kingdom_2_lady_15","Lady Sepana","Sepana",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
#["kingdom_2_lady_16","Lady Iarina","Iarina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,[       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
#["kingdom_2_lady_17","Lady Sihavan","Sihavan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
#["kingdom_2_lady_18","Lady Erenchina","Erenchina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [  itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
#["kingdom_2_lady_19","Lady Tamar","Tamar",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,[  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
#["kingdom_2_lady_20","Lady Valka","Valka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,[itm_green_dress,   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],


["kingdom_3_lady_1","Lady Borge","Borge",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_1],
["kingdom_3_lady_2","Lady Tuan","Tuan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
["kingdom_3_lady_3","Lady Mahraz","Mahraz",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [itm_red_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_2],
["kingdom_3_lady_4","Lady Ayasu","Ayasu",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_red_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
["kingdom_3_lady_5","Lady Ravin","Ravin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
["kingdom_3_lady_6","Lady Ruha","Ruha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
["kingdom_3_lady_7","Lady Chedina","Chedina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
["kingdom_3_lady_8","Lady Kefra","Kefra",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
["kingdom_3_lady_9","Lady Nirvaz","Nirvaz",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001940c3006019c925165d1129b00000000001d13240000000000000000],
["kingdom_3_lady_10","Lady Dulua","Dulua",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
["kingdom_3_lady_11","Lady Selik","Selik",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000019b083005389591941379b8d100000000001e63150000000000000000],
["kingdom_3_lady_12","Lady Thalatha","Thalatha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
["kingdom_3_lady_13","Lady Yasreen","Yasreen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
["kingdom_3_lady_14","Lady Nadha","Nadha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_1],
["kingdom_3_lady_15","Lady Zenur","Zenur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_2],
#["kingdom_3_lady_16","Lady Arjis","Zenur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001ad003001628c54b05d2e48b200000000001d56e60000000000000000],
#["kingdom_3_lady_17","Lady Atjahan", "Atjahan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001a700300265cb6db15d6db6da00000000001f82180000000000000000],
#["kingdom_3_lady_18","Lady Qutala","Qutala",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
#["kingdom_3_lady_19","Lady Hindal","Hindal",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
#["kingdom_3_lady_20","Lady Mechet","Mechet",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],



["kingdom_4_lady_1","Lady Jadeth","Jadeth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
["kingdom_4_lady_2","Lady Miar","Miar",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
["kingdom_4_lady_3","Lady Dria","Dria",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress, itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
["kingdom_4_lady_4","Lady Glunde","Glunde",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
["kingdom_4_lady_5","Lady Loeka","Loeka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
["kingdom_4_lady_6","Lady Bryn","Bryn",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
["kingdom_4_lady_7","Lady Eir","Eir",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
["knight_4_2b_daughter_1","Lady Thera","Thera",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
["kingdom_4_lady_9","Lady Hild","Hild",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,  itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
["knight_4_2c_wife_1","Lady Endegrid","Endegrid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
["kingdom_4_lady_11","Lady Herjasa","Herjasa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
["knight_4_2c_daughter","Lady Svipul","Svipul",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
["knight_4_1b_wife","Lady Ingunn","Ingunn",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
["kingdom_4_lady_14","Lady Kaeteli","Kaeteli",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
["knight_4_1b_daughter","Lady Eilif","Eilif",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
["knight_4_2b_daughter_2","Lady Gudrun","Gudrun",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,[    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
["kingdom_4_lady_17","Lady Bergit","Bergit",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
["knight_4_2c_wife_2","Lady Aesa","Aesa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
["knight_4_1c_daughter","Lady Alfrun","Alfrun",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,[    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
["kingdom_4_lady_20","Lady Afrid","Afrid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,[    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],


["kingdom_5_lady_1","Lady Brina","Brina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
["kingdom_5_lady_2","Lady Aliena","Aliena",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
["kingdom_5_lady_3","Lady Aneth","Aneth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
["kingdom_5_lady_4","Lady Reada","Reada",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
["kingdom_5_5_wife","Lady Saraten","Saraten",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
["kingdom_5_2b_wife_1","Lady Baotheia","Baotheia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [itm_lady_dress_green,     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000bf0400035913aa236b4d975a00000000001eb69c0000000000000000],
["kingdom_5_1c_daughter_1","Lady Eleandra","Eleandra",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
["kingdom_5_2c_daughter_1","Lady Meraced","Meraced",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
["kingdom_5_1c_wife_1","Lady Adelisa","Adelisa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
["kingdom_5_2c_wife_1","Lady Calantina","Calantina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
["kingdom_5_1c_daughter_2","Lady Forbesa","Forbesa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
["kingdom_5_2c_daughter_2","Lady Claudora","Claudora",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
["kingdom_5_1b_wife","Lady Anais","Anais",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
["kingdom_5_2b_wife_2","Lady Miraeia","Miraeia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
["kingdom_5_1c_daughter_3","Lady Agasia","Agasia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
["kingdom_5_lady_16","Lady Geneiava","Geneiava",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,[ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
["kingdom_5_1c_wife_2","Lady Gwenael","Gwenael",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
["kingdom_5_2c_wife_2","Lady Ysueth","Ysueth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
["kingdom_5_1c_daughter_4","Lady Ellian","Ellian",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,[ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
["kingdom_5_lady_20","Lady Timethi","Timethi",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,[ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],

#Sarranid ladies
["kingdom_6_lady_1","Lady Rayma","Rayma",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,  itm_sarranid_head_cloth,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
#["kingdom_6_lady_2","Lady Thanaikha","Thanaikha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
#["kingdom_6_lady_3","Lady Sulaha","Sulaha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,  [itm_sarranid_lady_dress,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
#["kingdom_6_lady_4","Lady Shatha","Shatha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,  [itm_sarranid_lady_dress,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
#["kingdom_6_lady_5","Lady Bawthan","Bawthan",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
#["kingdom_6_lady_6","Lady Mahayl","Mahayl",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
#["kingdom_6_lady_7","Lady Isna","Isna",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
#["kingdom_6_lady_8","Lady Siyafan","Siyafan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
#["kingdom_6_lady_9","Lady Ifar","Ifar",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
#["kingdom_6_lady_10","Lady Yasmin","Yasmin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
#["kingdom_6_lady_11","Lady Dula","Dula",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
#["kingdom_6_lady_12","Lady Ruwa","Ruwa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
#["kingdom_6_lady_13","Lady Luqa","Luqa",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
#["kingdom_6_lady_14","Lady Zandina","Zandina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
#["kingdom_6_lady_15","Lady Lulya","Lulya",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
#["kingdom_6_lady_16","Lady Zahara","Zahara",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
#["kingdom_6_lady_17","Lady Safiya","Safiya",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
#["kingdom_6_lady_18","Lady Khalisa","Khalisa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
#["kingdom_6_lady_19","Lady Janab","Janab",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
#["kingdom_6_lady_20","Lady Sur","Sur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],

["kingdom_7_lady_1", "Doamna Elena", "Elena", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_7, [itm_sarranid_head_cloth,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000 ],
["kingdom_7_lady_2", "Doamna Sorina", "Sorina", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_7, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000 ],
["kingdom_7_lady_3", "Doamna Ruxandra", "Ruxandra", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_7, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000 ],
["kingdom_7_lady_4", "Doamna Mihaela", "Mihaela", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_7, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000 ],
["kingdom_7_lady_5", "Doamna Zoita", "Zoita", tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_7, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2 ],
["kingdom_7_lady_6", "Doamna Anca", "Anca", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_7, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000 ],
["kingdom_7_lady_7", "Doamna Adela", "Adela", tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_7, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2 ],
["kingdom_7_lady_8", "Doamna Teodora", "Teodora", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_7, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000 ],
["kingdom_7_lady_9", "Doamna Maria", "Maria", tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_7, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2 ],
["kingdom_7_lady_10", "Doamna Nedeia", "Nedeia", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_7, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000 ],
["kingdom_7_lady_11", "Doamna Rodica", "Rodica", tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_7, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2 ],
["kingdom_7_lady_12", "Doamna Sanziana", "Sanziana", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_7, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000 ],
["kingdom_7_lady_13", "Doamna Brandusa", "Brandusa", tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_7, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2 ],
["kingdom_7_lady_14", "Doamna Roxana", "Roxana", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_7, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000 ],
["kingdom_7_lady_15", "Doamna Zina", "Zina", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_7, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2 ],
["kingdom_7_lady_16", "Doamna Iulia", "Iulia", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_7, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000 ],
["kingdom_7_lady_17", "Doamna Adelina", "Adelina", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_7, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000018000000f0000000000000e0000000000000000000000000000000000 ],
["kingdom_7_lady_18", "Doamna Corina", "Corina", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_7, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000 ],
["kingdom_7_lady_19", "Doamna Tincuta", "Tincuta", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_7, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_1 ],
["kingdom_7_lady_20", "Doamna Alexandra", "Alexandra", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_7, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_2 ],

["kingdom_8_lady_1","Lady Junitha","Junitha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
["kingdom_8_lady_2","Lady Katia","Katia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
["kingdom_8_lady_3","Lady Seomis","Seomis",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,  [   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
["kingdom_8_lady_4","Lady Drina","Drina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,  [    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
["kingdom_8_lady_5","Lady Nesha","Nesha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
["kingdom_8_lady_6","Lady Tabath","Tabath",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
["kingdom_8_lady_7","Lady Pelaeka","Pelaeka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,  [     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
["kingdom_8_lady_8","Lady Haris","Haris",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,  [    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
["kingdom_8_lady_9","Lady Vayen","Vayen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
["kingdom_8_lady_10","Lady Joaka","Joaka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
["kingdom_8_lady_11","Lady Tejina","Tejina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,  [    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
["kingdom_8_lady_12","Lady Olekseia","Olekseia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,  [      itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
["kingdom_8_lady_13","Lady Myntha","Myntha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
["kingdom_8_lady_14","Lady Akilina","Akilina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
["kingdom_8_lady_15","Lady Sepana","Sepana",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,  [     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
["kingdom_8_lady_16","Lady Iarina","Iarina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,[       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
["kingdom_8_lady_17","Lady Sihavan","Sihavan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
["kingdom_8_lady_18","Lady Erenchina","Erenchina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [  itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
["kingdom_8_lady_19","Lady Tamar","Tamar",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,[  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
["kingdom_8_lady_20","Lady Valka","Valka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,[itm_green_dress,   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],

["kingdom_9_lady_1","Lady Rayma","Rayma",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_sarranid_lady_dress,  itm_sarranid_head_cloth,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
["kingdom_9_lady_2","Lady Thanaikha","Thanaikha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
["kingdom_9_lady_3","Lady Sulaha","Sulaha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9,  [itm_sarranid_lady_dress,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
["kingdom_9_lady_4","Lady Shatha","Shatha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9,  [itm_sarranid_lady_dress,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
["kingdom_9_lady_5","Lady Bawthan","Bawthan",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
["kingdom_9_lady_6","Lady Mahayl","Mahayl",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
["kingdom_9_lady_7","Lady Isna","Isna",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
["kingdom_9_lady_8","Lady Siyafan","Siyafan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_sarranid_lady_dress_b,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
["kingdom_9_lady_9","Lady Ifar","Ifar",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
["kingdom_9_lady_10","Lady Yasmin","Yasmin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_sarranid_lady_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
["kingdom_9_lady_11","Lady Dula","Dula",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
["kingdom_9_lady_12","Lady Ruwa","Ruwa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_sarranid_lady_dress_b,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
["kingdom_9_lady_13","Lady Luqa","Luqa",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_sarranid_lady_dress_b,     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
["kingdom_9_lady_14","Lady Zandina","Zandina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
["kingdom_9_lady_15","Lady Lulya","Lulya",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_sarranid_lady_dress_b,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
["kingdom_9_lady_16","Lady Zahara","Zahara",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
["kingdom_9_lady_17","Lady Safiya","Safiya",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
["kingdom_9_lady_18","Lady Khalisa","Khalisa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
["kingdom_9_lady_19","Lady Janab","Janab",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
["kingdom_9_lady_20","Lady Sur","Sur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],

["kingdom_10_lady_1", "Hatun Guzalia", "Guzalia", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_10, [itm_sarranid_lady_dress,itm_sarranid_head_cloth,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000 ],
["kingdom_10_lady_2", "Hatun Culpan", "Culpan", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_10, [itm_sarranid_lady_dress_b,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000 ],
["kingdom_10_lady_3", "Hatun Tansilu", "Tansilu", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_10, [itm_sarranid_lady_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000 ],
["kingdom_10_lady_4", "Hatun Farida", "Farida", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_10, [itm_sarranid_lady_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000 ],
["kingdom_10_lady_5", "Hatun Darida", "Darida", tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_10, [itm_sarranid_lady_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2 ],
["kingdom_10_lady_6", "Hatun Zohra", "Zohra", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_10, [itm_sarranid_lady_dress_b,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000 ],
["kingdom_10_lady_7", "Hatun Alfia", "Alfia", tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_10, [itm_sarranid_lady_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2 ],
["kingdom_10_lady_8", "Hatun Golnaz", "Golnaz", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_10, [itm_sarranid_lady_dress_b,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000 ],
["kingdom_10_lady_9", "Hatun Lale", "Lale", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_10, [itm_brown_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000001940c3006019c925165d1129b00000000001d13240000000000000000 ],
["kingdom_10_lady_10", "Hatun Irem", "Irem", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_10, [itm_brown_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000 ],
["kingdom_10_lady_11", "Hatun Ipek", "Ipek", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_10, [itm_brown_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000019b083005389591941379b8d100000000001e63150000000000000000 ],
["kingdom_10_lady_12", "Hatun Hanife", "Hanife", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_10, [itm_brown_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000 ],
["kingdom_10_lady_13", "Hatun Gul", "Gul", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_10, [itm_brown_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000 ],
["kingdom_10_lady_14", "Hatun Emel", "Emel", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_10, [itm_brown_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, khergit_woman_face_1 ],
["kingdom_10_lady_15", "Hatun Elif", "Elif", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_10, [itm_brown_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, khergit_woman_face_2 ],
["kingdom_10_lady_16", "Hatun Dilara", "Dilara", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_10, [itm_brown_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000001ad003001628c54b05d2e48b200000000001d56e60000000000000000 ],
["kingdom_10_lady_17", "Hatun Muge", "Muge", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_10, [itm_brown_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000001a700300265cb6db15d6db6da00000000001f82180000000000000000 ],
["kingdom_10_lady_18", "Hatun Sevim", "Sevim", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_10, [itm_brown_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000 ],
["kingdom_10_lady_19", "Hatun Ozlem", "Ozlem", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_10, [itm_brown_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000 ],
["kingdom_10_lady_20", "Hatun Rafat", "Rafat", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_10, [itm_brown_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000 ],

["kingdom_11_lady_1", "Senora Adelita", "Adelita", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_11, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000 ],
#["kingdom_11_lady_2", "Senora Alma", "Alma", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_11, [itm_leather_boots,itm_lady_dress_ruby], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000 ],
#["kingdom_11_lady_3", "Senora Carmen", "Carmen", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_11, [itm_leather_boots,itm_red_dress], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000 ],
#["kingdom_11_lady_4", "Senora Amarantha", "Amarantha", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_11, [itm_leather_boots,itm_brown_dress], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000 ],
#["kingdom_11_lady_5", "Senora Antonia", "Antonia", tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_11, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2 ],
#["kingdom_11_lady_6", "Senora Azuccena", "Azuccena", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_11, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000 ],
#["kingdom_11_lady_7", "Senora Blanca", "Blanca", tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_11, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2 ],
#["kingdom_11_lady_8", "Senora Camilla", "Camilla", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_11, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000 ],
#["kingdom_11_lady_9", "Senora Carolina", "Carolina", tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_11, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2 ],
#["kingdom_11_lady_10", "Senora Dolores", "Dolores", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_11, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000 ],
#["kingdom_11_lady_11", "Senora Eliana", "Eliana", tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_11, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2 ],
#["kingdom_11_lady_12", "Senora Ernestina", "Ernestina", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_11, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000 ],
#["kingdom_11_lady_13", "Senora Eva", "Eva", tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_11, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2 ],
#["kingdom_11_lady_14", "Senora Felicia", "Felicia", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_11, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000 ],
#["kingdom_11_lady_15", "Senora Gabriela", "Gabriela", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_11, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2 ],
#["kingdom_11_lady_16", "Senora Gloria", "Gloria", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_11, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000 ],
#["kingdom_11_lady_17", "Senora Jacinta", "Jacinta", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_11, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000 ],
#["kingdom_11_lady_18", "Senora Laura", "Laura", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_11, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000 ],
#["kingdom_11_lady_19", "Senora Margarita", "Margarita", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_11, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_1 ],
#["kingdom_11_lady_20", "Senora Perlita", "Perlita", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_11, [itm_blue_hose], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_2 ],

["kingdom_13_lady_1", "Kniazhina Tamara", "Tamara", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_13, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000 ],
#["kingdom_13_lady_2", "Kniazhina Natasha", "Natasha", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_13, [itm_leather_boots,itm_lady_dress_ruby], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000 ],
#["kingdom_13_lady_3", "Kniazhina Raisa", "Raisa", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_13, [itm_leather_boots,itm_red_dress], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000 ],
#["kingdom_13_lady_4", "Kniazhina Ruslana", "Ruslana", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_13, [itm_leather_boots,itm_brown_dress], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000 ],
#["kingdom_13_lady_5", "Kniazhina Alyona", "Alyona", tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_13, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2 ],
#["kingdom_13_lady_6", "Kniazhina Anichka", "Anichka", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_13, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000 ],
#["kingdom_13_lady_7", "Kniazhina Bohdana", "Bohdana", tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_13, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2 ],
#["kingdom_13_lady_8", "Kniazhina Ludmilla", "Ludmilla", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_13, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000 ],
#["kingdom_13_lady_9", "Kniazhina Tanya", "Tanya", tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_13, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2 ],
#["kingdom_13_lady_10", "Kniazhina Viktorya", "Viktorya", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_13, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000 ],
#["kingdom_13_lady_11", "Kniazhina Lilia", "Lilia", tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_13, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2 ],
#["kingdom_13_lady_12", "Kniazhina Katerina", "Katerina", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_13, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000 ],
#["kingdom_13_lady_13", "Kniazhina Larissa", "Larissa", tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_13, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2 ],
#["kingdom_13_lady_14", "Kniazhina Oskana", "Oskana", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_13, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000 ],
#["kingdom_13_lady_15", "Kniazhina Ira", "Ira", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_13, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2 ],
#["kingdom_13_lady_16", "Kniazhina Alexandrina", "Alexandrina", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_13, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000 ],
#["kingdom_13_lady_17", "Kniazhina Natalia", "Natalia", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_13, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000 ],
#["kingdom_13_lady_18", "Kniazhina Svetlana", "Svetlana", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_13, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000 ],
#["kingdom_13_lady_19", "Kniazhina Mikayla", "Mikayla", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_13, [itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_1 ],
#["kingdom_13_lady_20", "Kniazhina Zhanna ", "Zhanna", tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_kingdom_13, [itm_blue_hose], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_2 ],

["kingdom_14_lady_1","Lady Agashka","Agashka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_14, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
#["kingdom_14_lady_2","Lady Aleksandra","Aleksandra",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_14, [    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
#["kingdom_14_lady_3","Lady Belukha","Belukha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_14,[   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
#["kingdom_14_lady_4","Lady Cecislava","Cecislava",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_14,[    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
#["kingdom_14_lady_5","Lady Deda","Deda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_14, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
#["kingdom_14_lady_6","Lady Dekava","Dekava",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_14, [     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
#["kingdom_14_lady_7","Lady Feklitsa","Feklitsa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_14,[     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
#["kingdom_14_lady_8","Lady Gandaza","Gandaza",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_14,[    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
#["kingdom_14_lady_9","Lady Alyona","Alyona",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_14, [    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
#["kingdom_14_lady_10","Lady Galina","Galina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_14, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
#["kingdom_14_lady_11","Lady Irina","Irina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_14,[    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
#["kingdom_14_lady_12","Lady Larissa","Larissa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_14,[      itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
#["kingdom_14_lady_13","Lady Natasha","Natasha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_14, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
#["kingdom_14_lady_14","Lady Svetlana","Svetlana",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_14, [     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
#["kingdom_14_lady_15","Lady Tatyana","Tatyana",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_14,[     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
#["kingdom_14_lady_16","Lady Iarina","Iarina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_14,[       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
#["kingdom_14_lady_17","Lady Sihavan","Sihavan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_14, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
#["kingdom_14_lady_18","Lady Erenchina","Erenchina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_14, [  itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
#["kingdom_14_lady_19","Lady Tamar","Tamar",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_14,[  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
#["kingdom_14_lady_20","Lady Valka","Valka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_14,[itm_green_dress,   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],


["heroes_end", "{!}heroes end", "{!}heroes end", tf_hero, 0,reserved,  fac_neutral,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000008318101f390c515555594],
#Merchants                                                                              AT                      SILAH                   ZIRH                        BOT                         Head_wear

  ["caravan_master_01","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_02","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_03","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_04","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_05","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_06","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_07","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_08","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_09","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_10","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_11","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_12","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_13","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_14","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_15","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_16","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_17","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_18","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_19","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_20","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_31","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_32","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_33","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_34","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_35","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_36","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_37","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_38","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_39","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_40","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_41","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_42","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_43","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_44","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_45","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_46","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_47","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_48","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_49","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],
  ["caravan_master_50","Caravan Master","Caravan Masters",gen_caravan_master_1,0,0, fac_commoners,[itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse, itm_leather_jacket, itm_leather_cap], def_attrib|level(9), wp(100), gen_caravan_master_skills, mercenary_face_1, mercenary_face_2],

  ["caravan_masters_end","caravan_masters_end","caravan_masters_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],


#Seneschals
["town_1_seneschal", "{!}Town 1 Seneschal", "{!}Town 1 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["town_2_seneschal", "{!}Town 2 Seneschal", "{!}Town 2 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_padded_leather,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["town_3_seneschal", "{!}Town 3 Seneschal", "{!}Town 3 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["town_4_seneschal", "{!}Town 4 Seneschal", "{!}Town 4 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["town_5_seneschal", "{!}Town 5 Seneschal", "{!}Town 5 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["town_6_seneschal", "{!}Town 6 Seneschal", "{!}Town 6 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["town_7_seneschal", "{!}Town 7 Seneschal", "{!}Town7 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_armor7,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["town_8_seneschal", "{!}Town 8 Seneschal", "{!}Town 8 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["town_9_seneschal", "{!}Town 9 Seneschal", "{!}Town 9 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["town_10_seneschal", "{!}Town 10 Seneschal", "{!}Town 10 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["town_11_seneschal", "{!}Town 11 Seneschal", "{!}Town 11 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jacket,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["town_12_seneschal", "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["town_13_seneschal", "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_armor7,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["town_14_seneschal", "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["town_15_seneschal", "{!}Town 15 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["town_16_seneschal", "{!}Town 16 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["town_17_seneschal", "{!}Town17 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["town_18_seneschal", "{!}Town 18 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["town_19_seneschal", "{!}Town 19 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["town_20_seneschal", "{!}Town 20 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["town_21_seneschal", "{!}Town 21 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["town_22_seneschal", "{!}Town 22 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["town_23_seneschal", "{!}Town 23 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0, reserved, fac_neutral, [itm_gambeson,itm_blue_hose], def_attrib|level(2), wp(20), knows_common, man_face_middle_1, man_face_older_2 ],
["town_24_seneschal", "{!}Town 24 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0, reserved, fac_neutral, [itm_gambeson,itm_blue_hose], def_attrib|level(2), wp(20), knows_common, man_face_middle_1, man_face_older_2 ],
["town_25_seneschal", "{!}Town 25 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0, reserved, fac_neutral, [itm_gambeson,itm_blue_hose], def_attrib|level(2), wp(20), knows_common, man_face_middle_1, man_face_older_2 ],

["castle_1_seneschal", "{!}Castle 1 Seneschal", "{!}Castle 1 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_2_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_3_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_4_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_5_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_armor7,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_6_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_7_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_8_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_9_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_10_seneschal", "{!}Castle 10 Seneschal", "{!}Castle 10 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_11_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_12_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_13_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_14_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_15_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_16_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_17_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_18_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_19_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_20_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_21_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_22_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_23_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_24_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_25_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_armor7,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_26_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_27_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_28_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_29_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_30_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_31_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_32_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_33_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_34_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_35_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_36_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_37_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_38_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_39_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_40_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_41_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_42_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_43_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_44_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_45_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_46_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_47_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_48_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_49_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_50_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_51_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_52_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_53_seneschal", "{!}Castle 1 Seneschal", "{!}Castle 1 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_54_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_55_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_56_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_57_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_armor7,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_58_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_59_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_60_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_61_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_62_seneschal", "{!}Castle 10 Seneschal", "{!}Castle 10 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_63_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_64_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_65_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_66_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_67_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_68_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_69_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_70_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_71_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_72_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_73_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_74_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
["castle_75_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],




#Arena Masters
["town_1_arena_master", "{!}Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_1_arena|entry(52),reserved,   fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib_nobel|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["town_2_arena_master", "{!}Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_2_arena|entry(52),reserved,   fac_commoners,[itm_linen_tunic,       itm_nomad_boots],   def_attrib_nobel|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["town_3_arena_master", "{!}Tournament Master","Tournament Master",tf_hero|tf_randomize_face|tf_male_elf, scn_town_3_arena|entry(52),reserved,   fac_commoners,[itm_mirkwood_armor_d,       itm_mirkwood_boots],    def_attrib_nobel|level(2),wp(20),knows_common,mirkwood_elf_face_1, mirkwood_elf_face_2],
["town_4_arena_master", "{!}Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_4_arena|entry(52),reserved,   fac_commoners,[itm_german_armour_4,itm_wisby_gauntlets_black,itm_iron_greaves2],    def_attrib_nobel|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["town_5_arena_master", "{!}Tournament Master","Tournament Master",tf_undead|tf_hero|tf_randomize_face, scn_town_5_arena|entry(52),reserved,   fac_commoners,[itm_lich_helm,itm_lich_armor,itm_skull_staff,itm_twilight_boots],   def_attrib_nobel|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["town_6_arena_master", "{!}Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_6_arena|entry(52),reserved,   fac_commoners,[itm_kaftan,    itm_leather_boots], def_attrib_nobel|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["town_7_arena_master", "{!}Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_7_arena|entry(52),reserved,   fac_commoners,[itm_padded_leather,    itm_nomad_boots],   def_attrib_nobel|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["town_8_arena_master", "{!}Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_8_arena|entry(52),reserved,   fac_commoners,[itm_linen_tunic,       itm_hide_boots],    def_attrib_nobel|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["town_9_arena_master", "{!}Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_9_arena|entry(52),reserved,   fac_commoners,[itm_padded_leather,    itm_leather_boots], def_attrib_nobel|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["town_10_arena_master","Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_10_arena|entry(52),reserved,  fac_commoners,[itm_nomad_armor,       itm_nomad_boots],   def_attrib_nobel|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["town_11_arena_master","Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_11_arena|entry(52),reserved,  fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib_nobel|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["town_12_arena_master","Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_12_arena|entry(52),reserved,  fac_commoners,[itm_kaftan,    itm_hide_boots],    def_attrib_nobel|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["town_13_arena_master","Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_13_arena|entry(52),reserved,  fac_commoners,[itm_coarse_tunic,      itm_nomad_boots],   def_attrib_nobel|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["town_14_arena_master","Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_14_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib_nobel|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["town_15_arena_master","Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_15_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib_nobel|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["town_16_arena_master","Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_16_arena|entry(52),reserved,  fac_commoners,[itm_fur_coat,    itm_hide_boots],    def_attrib_nobel|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["town_17_arena_master","Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_17_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib_nobel|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["town_18_arena_master","Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_18_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib_nobel|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["town_19_arena_master","Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_19_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib_nobel|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["town_20_arena_master","Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_20_arena|entry(52),reserved,  fac_commoners,[itm_fur_coat,    itm_hide_boots],    def_attrib_nobel|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["town_21_arena_master","Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_21_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib_nobel|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["town_22_arena_master","Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_22_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib_nobel|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["town_23_arena_master","Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_23_arena|entry(52),reserved,  fac_commoners,[itm_fur_coat,    itm_hide_boots],    def_attrib_nobel|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["town_24_arena_master", "{!}Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_24_arena|entry(52),reserved,   fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib_nobel|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["town_25_arena_master", "{!}Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_25_arena|entry(52),reserved,   fac_commoners,[itm_linen_tunic,       itm_nomad_boots],   def_attrib_nobel|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
# Underground

##  ["town_1_crook","Town 1 Crook","Town 1 Crook",tf_hero,                0,0, fac_neutral,[itm_linen_tunic,        itm_leather_boots       ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x000000000004428401f46e44a27144e3],
##  ["town_2_crook","Town 2 Crook","Town 2 Crook",tf_hero|tf_female,      0,0, fac_neutral,[itm_lady_dress_ruby,    itm_turret_hat_ruby     ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x000000000004300101c36db6db6db6db],
##  ["town_3_crook","Town 3 Crook","Town 3 Crook",tf_hero,                0,0, fac_neutral,[itm_leather_apron,      itm_hide_boots          ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c530701f17944a25164e1],
##  ["town_4_crook","Town 4 Crook","Town 4 Crook",tf_hero,                0,0, fac_neutral,[itm_coarse_tunic,       itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c840501f36db6db7134db],
##  ["town_5_crook","Town 5 Crook","Town 5 Crook",tf_hero,                0,0, fac_neutral,[itm_red_gambeson,       itm_blue_hose           ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c000601f36db6db7134db],
##  ["town_6_crook","Town 6 Crook","Town 6 Crook",tf_hero,                0,0, fac_neutral,[itm_coarse_tunic,       itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c10c801db6db6dd7598aa],
##  ["town_7_crook","Town 7 Crook","Town 7 Crook",tf_hero|tf_female,      0,0, fac_neutral,[itm_woolen_dress,       itm_woolen_hood         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000010214101de2f64db6db58d],
##
##  ["town_8_crook","Town 8 Crook","Town 8 Crook",tf_hero,                0,0, fac_neutral,[itm_leather_jacket,     itm_leather_boots       ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000010318401c96db4db6db58d],
##  ["town_9_crook","Town 9 Crook","Town 9 Crook",tf_hero,                0,0, fac_neutral,[itm_linen_tunic,        itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008520501f16db4db6db58d],
##  ["town_10_crook","Town 10 Crook","Town 10 Crook",tf_hero,             0,0, fac_neutral,[itm_coarse_tunic,      itm_nomad_boots         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008600701f35144db6db8a2],
##  ["town_11_crook","Town 11 Crook","Town 11 Crook",tf_hero|tf_female,   0,0, fac_neutral,[itm_blue_dress,        itm_wimple_with_veil    ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008408101f386c4db4dd514],
##  ["town_12_crook","Town 12 Crook","Town 12 Crook",tf_hero,             0,0, fac_neutral,[itm_coarse_tunic,      itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000870c501f386c4f34dbaa1],
##  ["town_13_crook","Town 13 Crook","Town 13 Crook",tf_hero,             0,0, fac_neutral,[itm_gambeson,     itm_nomad_boots         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c114901f245caf34dbaa1],
##  ["town_14_crook","Town 14 Crook","Town 14 Crook",tf_hero|tf_female,   0,0, fac_neutral,[itm_woolen_dress,      itm_turret_hat_ruby     ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000001021c001f545a49b6eb2bc],

# Armor Merchants
#arena_masters_end = zendar_armorer

["town_1_armorer","{!}Armorer",  "Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,           itm_leather_boots   ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_2_armorer","{!}Armorer",  "Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,          itm_straw_hat       ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
["town_3_armorer","{!}Armorer",  "Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_red,        itm_hide_boots      ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_4_armorer","{!}Armorer",  "Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_red_gambeson,         itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_5_armorer","{!}Armorer",  "Armorer",  tf_vampire|tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,          itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_6_armorer","{!}Armorer",  "Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,       itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_7_armorer","{!}Armorer",  "Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_kaftan,       itm_blue_hose       ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_8_armorer","{!}Armorer",  "Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_leather,       itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_9_armorer","{!}Armorer",  "Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_gambeson,        itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_10_armorer","{!}Armorer", "Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_kaftan,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_11_armorer","{!}Armorer", "Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,        itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_12_armorer","{!}Armorer", "Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_red_gambeson,         itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_13_armorer","{!}Armorer", "Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_14_armorer","{!}Armorer", "Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,         itm_headcloth       ],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
["town_15_armorer","{!}Armorer", "Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_gambeson,        itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_16_armorer","{!}Armorer", "Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,         itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_17_armorer","{!}Armorer", "Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_18_armorer","{!}Armorer", "Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,         itm_headcloth       ],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
["town_19_armorer","{!}Armorer", "Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_gambeson,        itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_20_armorer","{!}Armorer", "Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,         itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_21_armorer","{!}Armorer", "Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_22_armorer","{!}Armorer", "Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_sarranid_common_dress,         itm_sarranid_head_cloth       ],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
["town_23_armorer","{!}Armorer", "Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_24_armorer","{!}Armorer", "Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_sarranid_common_dress,         itm_sarranid_head_cloth       ],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
["town_25_armorer","{!}Armorer", "Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_sarranid_common_dress,         itm_sarranid_head_cloth       ],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
# Weapon merchants

["town_1_weaponsmith", "{!}Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,      itm_hide_boots,itm_straw_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
["town_2_weaponsmith", "{!}Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,     itm_nomad_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_3_weaponsmith", "{!}Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,   itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_4_weaponsmith", "{!}Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,            itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_5_weaponsmith", "{!}Weaponsmith","Weaponsmith",tf_vampire|tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_kaftan,   itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_6_weaponsmith", "{!}Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,      itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_7_weaponsmith", "{!}Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,            itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_8_weaponsmith", "{!}Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,     itm_wrapping_boots,itm_straw_hat],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
["town_9_weaponsmith", "{!}Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_kaftan,   itm_leather_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_10_weaponsmith", "{!}Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_11_weaponsmith", "{!}Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,  itm_woolen_hose],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_12_weaponsmith", "{!}Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,           itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_13_weaponsmith", "{!}Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_red,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_14_weaponsmith", "{!}Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_blue,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_15_weaponsmith", "{!}Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,  itm_woolen_hose],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_16_weaponsmith", "{!}Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,           itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_17_weaponsmith", "{!}Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_ranger_armor1,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_18_weaponsmith", "{!}Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_19_weaponsmith", "{!}Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,  itm_sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_20_weaponsmith", "{!}Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,           itm_sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_21_weaponsmith", "{!}Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_ranger_armor1,     itm_sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_22_weaponsmith", "{!}Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     itm_sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_23_weaponsmith", "{!}Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_green,     itm_sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_24_weaponsmith", "{!}Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     itm_sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_25_weaponsmith", "{!}Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     itm_sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],

#Tavern keepers

["town_1_tavernkeeper", "{!}Tavern_Keeper","Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_1_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
["town_2_tavernkeeper", "{!}Tavern_Keeper","Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_2_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
["town_3_tavernkeeper", "{!}Tavern_Keeper","Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_3_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_hide_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
["town_4_tavernkeeper", "{!}Tavern_Keeper","Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_4_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
["town_5_tavernkeeper", "{!}Tavern_Keeper","Tavern_Keeper",tf_vampire|tf_hero|tf_randomize_face,           scn_town_5_tavern|entry(9),0,   fac_commoners,[itm_vampire_tunic,       itm_hide_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
["town_6_tavernkeeper", "{!}Tavern_Keeper","Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_6_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_hide_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
["town_7_tavernkeeper", "{!}Tavern_Keeper","Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_7_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_leather_boots,      itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
["town_8_tavernkeeper", "{!}Tavern_Keeper","Tavern_Keeper",tf_dwarf|tf_hero|tf_randomize_face,           scn_town_8_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,      itm_leather_boots],def_attrib|level(2),wp(20),knows_common, nord_face_middle_1, nord_face_middle_2],


["town_9_tavernkeeper", "{!}Tavern_Keeper","Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_9_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
["town_10_tavernkeeper", "{!}Tavern_Keeper","Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_10_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_hide_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
["town_11_tavernkeeper", "{!}Tavern_Keeper","Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_11_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
["town_12_tavernkeeper", "{!}Tavern_Keeper","Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_12_tavern|entry(9),0,  fac_commoners,[itm_leather_apron,       itm_hide_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
["town_13_tavernkeeper", "{!}Tavern_Keeper","Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_13_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_hide_boots,     itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
["town_14_tavernkeeper", "{!}Tavern_Keeper","Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_14_tavern|entry(9),0,  fac_commoners,[itm_shirt,               itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
["town_15_tavernkeeper", "{!}Tavern_Keeper","Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_15_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
["town_16_tavernkeeper", "{!}Tavern_Keeper","Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_16_tavern|entry(9),0,  fac_commoners,[itm_leather_apron,       itm_hide_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
["town_17_tavernkeeper", "{!}Tavern_Keeper","Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_17_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_hide_boots,     itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
["town_18_tavernkeeper", "{!}Tavern_Keeper","Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_18_tavern|entry(9),0,  fac_commoners,[itm_shirt,               itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
["town_19_tavernkeeper", "{!}Tavern_Keeper","Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_19_tavern|entry(9),0,  fac_commoners,[itm_sarranid_dress_a,        itm_sarranid_boots_a],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
["town_20_tavernkeeper", "{!}Tavern_Keeper","Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_20_tavern|entry(9),0,  fac_commoners,[itm_sarranid_cloth_robe,       itm_sarranid_boots_a],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
["town_21_tavernkeeper", "{!}Tavern_Keeper","Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_21_tavern|entry(9),0,  fac_commoners,[itm_sarranid_common_dress,        itm_sarranid_boots_a,     itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
["town_22_tavernkeeper", "{!}Tavern_Keeper","Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_22_tavern|entry(9),0,  fac_commoners,[itm_sarranid_cloth_robe_b,               itm_sarranid_boots_a],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
["town_23_tavernkeeper", "{!}Tavern_Keeper","Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_23_tavern|entry(9),0,  fac_commoners,[itm_sarranid_common_dress,        itm_sarranid_boots_a,     itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
["town_24_tavernkeeper", "{!}Tavern_Keeper","Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_24_tavern|entry(9),0,  fac_commoners,[itm_sarranid_cloth_robe_b,               itm_sarranid_boots_a],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
["town_25_tavernkeeper", "{!}Tavern_Keeper","Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_25_tavern|entry(9),0,  fac_commoners,[itm_sarranid_cloth_robe_b,               itm_sarranid_boots_a],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
#Goods Merchants

["town_1_merchant", "{!}Merchant","Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_1_store|entry(9),0, fac_commoners,     [itm_coarse_tunic,  itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_2_merchant", "{!}Merchant","Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_2_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_3_merchant", "{!}Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_3_store|entry(9),0, fac_commoners,     [itm_dress,         itm_leather_boots,  itm_straw_hat   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
["town_4_merchant", "{!}Merchant","Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_4_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_5_merchant", "{!}Merchant","Merchant",          tf_vampire|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_5_store|entry(9),0, fac_commoners,     [itm_vampire_tunic,   itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_6_merchant", "{!}Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_6_store|entry(9),0, fac_commoners,     [itm_woolen_dress,  itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_7_merchant", "{!}Merchant","Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_7_store|entry(9),0, fac_commoners,     [itm_kaftan,itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_8_merchant", "{!}Merchant","Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_8_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_9_merchant", "{!}Merchant","Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_9_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_10_merchant", "{!}Merchant","Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_10_store|entry(9),0, fac_commoners,    [itm_kaftan,itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_11_merchant", "{!}Merchant","Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_11_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_12_merchant", "{!}Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_12_store|entry(9),0, fac_commoners,    [itm_woolen_dress,  itm_leather_boots,  itm_female_hood ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
["town_13_merchant", "{!}Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_13_store|entry(9),0, fac_commoners,    [itm_dress,         itm_leather_boots,  itm_straw_hat   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
["town_14_merchant", "{!}Merchant","Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_14_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_15_merchant", "{!}Merchant","Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_15_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_16_merchant", "{!}Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_16_store|entry(9),0, fac_commoners,    [itm_woolen_dress,  itm_leather_boots,  itm_female_hood ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
["town_17_merchant", "{!}Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_17_store|entry(9),0, fac_commoners,    [itm_dress,         itm_leather_boots,  itm_straw_hat   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
["town_18_merchant", "{!}Merchant","Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_18_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_19_merchant", "{!}Merchant","Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_19_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_20_merchant", "{!}Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_20_store|entry(9),0, fac_commoners,    [itm_sarranid_common_dress_b,  itm_sarranid_boots_a, itm_sarranid_felt_head_cloth_b  ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
["town_21_merchant", "{!}Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_21_store|entry(9),0, fac_commoners,    [itm_sarranid_dress_a,         itm_sarranid_boots_a,  itm_sarranid_felt_head_cloth  ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
["town_22_merchant", "{!}Merchant","Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_22_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_23_merchant", "{!}Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_23_store|entry(9),0, fac_commoners,    [itm_sarranid_dress_a,         itm_sarranid_boots_a,  itm_sarranid_felt_head_cloth  ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
["town_24_merchant", "{!}Merchant","Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_24_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_25_merchant", "{!}Merchant","Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_25_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["salt_mine_merchant","Barezan","Barezan",              tf_hero|tf_randomize_face|tf_is_merchant, scn_salt_mine|entry(1),0, fac_commoners,        [itm_leather_jacket, itm_leather_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, merchant_face_1, merchant_face_2],

# Horse Merchants

["town_1_horse_merchant","{!}Horse Merchant","Town 1 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_blue_dress,           itm_blue_hose,      itm_female_hood],   def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
["town_2_horse_merchant","{!}Horse Merchant","Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_linen_tunic,          itm_nomad_boots,],                      def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_3_horse_merchant","{!}Horse Merchant","Town 3 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_nomad_armor,          itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_4_horse_merchant","{!}Horse Merchant","Town 4 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_kaftan,       itm_nomad_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_5_horse_merchant","{!}Horse Merchant","Town 5 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_dress,                itm_woolen_hose,    itm_woolen_hood],   def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
["town_6_horse_merchant","{!}Horse Merchant","Town 6 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_7_horse_merchant","{!}Horse Merchant","Town 7 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_8_horse_merchant","{!}Horse Merchant","Town 8 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_9_horse_merchant","{!}Horse Merchant","Town 9 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_kaftan,       itm_woolen_hose],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_10_horse_merchant","{!}Horse Merchant","Town 10 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_blue_dress,          itm_blue_hose,      itm_straw_hat],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
["town_11_horse_merchant","{!}Horse Merchant","Town 11 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_nomad_armor,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_12_horse_merchant","{!}Horse Merchant","Town 12 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_leather_jacket,      itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_13_horse_merchant","{!}Horse Merchant","Town 13 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_coarse_tunic,        itm_nomad_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_14_horse_merchant","{!}Horse Merchant","Town 14 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_peasant_dress,       itm_blue_hose,      itm_headcloth],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
["town_15_horse_merchant","{!}Horse Merchant","Town 15 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_nomad_armor,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_16_horse_merchant","{!}Horse Merchant","Town 16 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_leather_jacket,      itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_17_horse_merchant","{!}Horse Merchant","Town 17 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_coarse_tunic,        itm_nomad_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_18_horse_merchant","{!}Horse Merchant","Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_peasant_dress,       itm_blue_hose,      itm_headcloth],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
["town_19_horse_merchant","{!}Horse Merchant","Town 15 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_nomad_armor,         itm_sarranid_boots_a],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_20_horse_merchant","{!}Horse Merchant","Town 16 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_sarranid_cloth_robe,      itm_sarranid_boots_a],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_21_horse_merchant","{!}Horse Merchant","Town 17 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_sarranid_cloth_robe_b,        itm_sarranid_boots_a],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_22_horse_merchant","{!}Horse Merchant","Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_sarranid_common_dress_b,       itm_blue_hose,      itm_sarranid_felt_head_cloth_b],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
["town_23_horse_merchant","{!}Horse Merchant","Town 17 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_sarranid_cloth_robe_b,        itm_sarranid_boots_a],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_24_horse_merchant","{!}Horse Merchant","Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_sarranid_common_dress_b,       itm_blue_hose,      itm_sarranid_felt_head_cloth_b],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
["town_25_horse_merchant","{!}Horse Merchant","Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_sarranid_common_dress_b,       itm_blue_hose,      itm_sarranid_felt_head_cloth_b],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
#Town Mayors    #itm_courtly_outfit itm_gambeson itm_gambeson itm_red_gambeson itm_nobleman_outfit itm_rich_outfit
["town_1_mayor", "{!}Guild_Master", "Guild_Master", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_courtly_outfit, itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
["town_2_mayor", "{!}Guild_Master", "Guild_Master", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_gambeson,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
["town_3_mayor", "{!}Guild_Master", "Guild_Master", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_gambeson,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
["town_4_mayor", "{!}Guild_Master", "Guild_Master", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_fur_coat,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
["town_5_mayor", "{!}Guild_Master", "Guild_Master", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_nobleman_outfit,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
["town_6_mayor", "{!}Guild_Master", "Guild_Master", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
["town_7_mayor", "{!}Guild_Master", "Guild_Master", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_rich_outfit,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
["town_8_mayor", "{!}Guild_Master", "Guild_Master", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
["town_9_mayor", "{!}Guild_Master", "Guild_Master", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_courtly_outfit,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
["town_10_mayor", "{!}Guild_Master", "Guild_Master", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_kaftan,     itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
["town_11_mayor", "{!}Guild_Master", "Guild_Master", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jacket,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
["town_12_mayor", "{!}Guild_Master", "Guild_Master", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_red_gambeson,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
["town_13_mayor", "{!}Guild_Master", "Guild_Master", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_nobleman_outfit,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
["town_14_mayor", "{!}Guild_Master", "Guild_Master", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
["town_15_mayor", "{!}Guild_Master", "Guild_Master", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jacket,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
["town_16_mayor", "{!}Guild_Master", "Guild_Master", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_fur_coat,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
["town_17_mayor", "{!}Guild_Master", "Guild_Master", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_nobleman_outfit,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
["town_18_mayor", "{!}Guild_Master", "Guild_Master", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
["town_19_mayor", "{!}Guild_Master", "Guild_Master", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,     itm_sarranid_boots_a],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
["town_20_mayor", "{!}Guild_Master", "Guild_Master", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,       itm_sarranid_boots_a], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
["town_21_mayor", "{!}Guild_Master", "Guild_Master", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,    itm_sarranid_boots_a],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
["town_22_mayor", "{!}Guild_Master", "Guild_Master", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,      itm_sarranid_boots_a],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
["town_23_mayor", "{!}Guild_Master", "Guild_Master", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,    itm_sarranid_boots_a],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
["town_24_mayor", "{!}Guild_Master", "Guild_Master", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,      itm_sarranid_boots_a],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
["town_25_mayor", "{!}Guild_Master", "Guild_Master", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,      itm_sarranid_boots_a],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
#Village stores
["village_1_elder", "{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
["village_2_elder", "{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_3_elder", "{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_4_elder", "{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
["village_5_elder", "{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
["village_6_elder", "{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["village_7_elder", "{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_8_elder", "{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
["village_9_elder", "{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,         man_face_old_1, man_face_older_2],
["village_10_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_11_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_12_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_13_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_14_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_15_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
["village_16_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_17_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_18_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_19_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots, itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
["village_20_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_21_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_22_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_23_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
["village_24_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_25_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
["village_26_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_27_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
["village_28_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_29_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["village_30_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_31_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_32_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_33_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_34_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_35_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_36_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["village_37_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_38_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["village_39_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_40_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_41_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_42_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_43_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_44_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_45_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_46_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["village_47_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_48_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["village_49_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_50_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_51_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_52_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_53_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
["village_54_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_55_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_56_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_57_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_58_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_59_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_60_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_61_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_62_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_63_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_64_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_65_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_66_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_67_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_68_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_69_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_70_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_71_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_72_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_73_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_74_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_75_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_76_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_77_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_78_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_79_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_80_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_81_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_82_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_83_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_84_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_85_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_86_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["village_87_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_88_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["village_89_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_90_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_91_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_92_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_93_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_94_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_95_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_96_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["village_97_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_98_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["village_99_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_100_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_101_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_102_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_103_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_104_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_105_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_106_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["village_107_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_108_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["village_109_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_110_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_111_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_112_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_113_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_114_elder","{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_115_elder", "{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
["village_116_elder", "{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_117_elder", "{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_118_elder", "{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
["village_119_elder", "{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
["village_120_elder", "{!}Village_Elder", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
# Place extra merchants before this point
["merchants_end","merchants_end","merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],

#Used for player enterprises
["town_1_master_craftsman", "{!}Town 1 Craftsman", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
["town_2_master_craftsman", "{!}Town 2 Craftsman", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_padded_leather,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x0000000f010811c92d3295e46a96c72300000000001f5a980000000000000000],
["town_3_master_craftsman", "{!}Town 3 Craftsman", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000001b083203151d2ad5648e52b400000000001b172e0000000000000000],
["town_4_master_craftsman", "{!}Town 4 Craftsman", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000001a10114f091b2c259cd4c92300000000000228dd0000000000000000],
["town_5_master_craftsman", "{!}Town 5 Craftsman", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_kaftan,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000d1044c578598cd92b5256db00000000001f23340000000000000000],
["town_6_master_craftsman", "{!}Town 6 Craftsman", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000001f046285493eaf1b048abcdb00000000001a8aad0000000000000000],
["town_7_master_craftsman", "{!}Town 7 Craftsman", "{!}Town 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_kaftan,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000002b0052c34c549225619356d400000000001cc6e60000000000000000],
["town_8_master_craftsman", "{!}Town 8 Craftsman", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x0000000fdb0c20465b6e51e8a12c82d400000000001e148c0000000000000000],
["town_9_master_craftsman", "{!}Town 9 Craftsman", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000009f7005246071db236e296a45300000000001a8b0a0000000000000000],
["town_10_master_craftsman", "{!}Town 10 Craftsman", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_kaftan,     itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000009f71012c2456a921aa379321a000000000012c6d90000000000000000],
["town_11_master_craftsman", "{!}Town 11 Craftsman", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000009f308514428db71b9ad70b72400000000001dc9140000000000000000],
["town_12_master_craftsman", "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000009e90825863853a5b91cd71a5b00000000000598db0000000000000000],
["town_13_master_craftsman", "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_kaftan,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000009fa0c708f274c8eb4c64e271300000000001eb69a0000000000000000],
["town_14_master_craftsman", "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000007590c3206155c8b475a4e439a00000000001f489a0000000000000000],
["town_15_master_craftsman", "{!}Town 15 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000007440022d04b2c6cb7d3723d5a00000000001dc90a0000000000000000],
["town_16_master_craftsman", "{!}Town 16 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000007680c3586054b8e372e4db65c00000000001db7230000000000000000],
["town_17_master_craftsman", "{!}Town 17 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x0000000766046186591b564cec85d2e200000000001e4cea0000000000000000],
["town_18_master_craftsman", "{!}Town 18 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x0000000e7e0075523a6aa9b6da61e8dd00000000001d96d30000000000000000],
["town_19_master_craftsman", "{!}Town 19 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000002408314852a432e88aaa42e100000000001e284e0000000000000000],
["town_20_master_craftsman", "{!}Town 20 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe_b,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000001104449136e44cbd1c9352bc000000000005e8d10000000000000000],
["town_21_master_craftsman", "{!}Town 21 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000000131032d3351c6e43226ec96c000000000005b5240000000000000000],
["town_22_master_craftsman", "{!}Town 22 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe_b,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000000200c658a5723b1a3148dc455000000000015ab920000000000000000],
["town_23_master_craftsman", "{!}Town 21 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000000131032d3351c6e43226ec96c000000000005b5240000000000000000],
["town_24_master_craftsman", "{!}Town 22 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe_b,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000000200c658a5723b1a3148dc455000000000015ab920000000000000000],
["town_25_master_craftsman", "{!}Town 22 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe_b,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000000200c658a5723b1a3148dc455000000000015ab920000000000000000],
# Chests
["zendar_chest","{!}Zendar Chest","{!}Zendar Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_ebony_male_head,itm_ebony_male_plate,itm_ebony_male_foot,itm_ebony_male_hand],def_attrib|level(18),wp(60),knows_common,0],
["tutorial_chest_1","{!}Melee Weapons Chest","{!}Melee Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_tutorial_sword, itm_tutorial_axe, itm_tutorial_spear, itm_tutorial_club, itm_tutorial_battle_axe],def_attrib|level(18),wp(60),knows_common, 0],
["tutorial_chest_2","{!}Ranged Weapons Chest","{!}Ranged Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_tutorial_short_bow, itm_tutorial_arrows, itm_tutorial_crossbow, itm_tutorial_bolts, itm_tutorial_throwing_daggers],def_attrib|level(18),wp(60),knows_common, 0],
## CC
["bonus_chest_1","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_glass_female_plate,itm_glass_male_plate,itm_glass_foot,itm_glass_hand,itm_glass_shield],def_attrib|level(18),wp(60),knows_common, 0],



["bonus_chest_2","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_imperial_bow,itm_black_helmet,itm_holy_cross,itm_toumingdun,itm_strange_sword,itm_nahptha_bomb,itm_bonecrossbow,itm_musket_hand_gun,itm_van_helsing_crossbow_bolt],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_chest_3","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_mage_staff_1,itm_white_twiligh_armor,itm_strange_armor,itm_assassin_dagger,itm_strange_great_sword,itm_rat_musket_8barrel,itm_gondor_lance],def_attrib|level(18),wp(60),knows_common, 0],
## CC

["household_possessions","{!}household_possessions","{!}household_possessions",tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],

["freelancer_equip_troop","{!}freelancer_equip_troop","{!}freelancer_equip_troop",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],

# These are used as arrays in the scripts.
## CC
  ["temp_array_a","{!}temp_array_a","{!}temp_array_a",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
  ["temp_array_b","{!}temp_array_b","{!}temp_array_b",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
  ["temp_array_c","{!}temp_array_c","{!}temp_array_c",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
  ["temp_array_d","{!}temp_array_d","{!}temp_array_d",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
  ["temp_array_e","{!}temp_array_e","{!}temp_array_e",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
  ["temp_array_f","{!}temp_array_f","{!}temp_array_f",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
  ["temp_array_g","{!}temp_array_g","{!}temp_array_g",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
  ["temp_array_h","{!}temp_array_h","{!}temp_array_h",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
  ["temp_array_i","{!}temp_array_i","{!}temp_array_i",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
  ["temp_array_j","{!}temp_array_j","{!}temp_array_j",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
## CC

["stack_selection_amounts","{!}stack_selection_amounts","{!}stack_selection_amounts",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_inventory_management_10,0],
["stack_selection_ids","{!}stack_selection_ids","{!}stack_selection_ids",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_inventory_management_10,0],

["notification_menu_types","{!}notification_menu_types","{!}notification_menu_types",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_inventory_management_10,0],
["notification_menu_var1","{!}notification_menu_var1","{!}notification_menu_var1",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_inventory_management_10,0],
["notification_menu_var2","{!}notification_menu_var2","{!}notification_menu_var2",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_inventory_management_10,0],

["banner_background_color_array","{!}banner_background_color_array","{!}banner_background_color_array",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_inventory_management_10,0],

["multiplayer_data","{!}multiplayer_data","{!}multiplayer_data",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_inventory_management_10,0],

##  ["black_khergit_guard","Black Khergit Guard","Black Khergit Guard",tf_mounted|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_khergits,
##   [itm_arrows,itm_nomad_sabre,itm_scimitar,itm_winged_mace,itm_lance,itm_khergit_bow,itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_khergit_guard_boots,itm_khergit_guard_armor,itm_nomad_shield,itm_steppe_horse,itm_warhorse],
##   def_attrib|level(28),wp(140),knows_riding_6|knows_ironflesh_4|knows_horse_archery_6|knows_power_draw_6,khergit_face1, khergit_face2],

## CC
["book_read","{!}na","{!}na",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
["book_reading_progress","{!}na","{!}na",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
["bookcase","{!}Bookcase","{!}Bookcase",tf_hero,0,reserved,fac_neutral,[],def_attrib,0,knows_inventory_management_10,0],
["temp_troop_2","{!}Temp Troop","{!}Temp Troop",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
## CC
# Add Extra Quest NPCs below this point

["local_merchant","Local Merchant","Local Merchants",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
["tax_rebel","Peasant Rebel","Peasant Rebels",tf_guarantee_armor,0,reserved,fac_commoners,[itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots],def_attrib|level(4),wp(60),knows_common,vaegir_face1,vaegir_face2],
["trainee_peasant","Peasant","Peasants",tf_guarantee_armor,0,reserved,fac_commoners,[itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots],def_attrib|horse_attrib_3|level(15),wp(120),knows_spearman_2,vaegir_face1,vaegir_face2],
["fugitive","Nervous Man","Nervous Men",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_short_tunic,itm_linen_tunic,itm_coarse_tunic,itm_tabard,itm_leather_vest,itm_woolen_hose,itm_nomad_boots,itm_blue_hose,itm_wrapping_boots,itm_fur_hat,itm_leather_cap,itm_sword_medieval_b,itm_throwing_daggers],def_attrib|str_24|agi_25|level(26),wp(180),knows_common|knows_reserved_17_6|knows_power_strike_6|knows_ironflesh_9,man_face_middle_1,man_face_old_2],

["belligerent_drunk","Belligerent Drunk","Belligerent Drunks",tf_vampire|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_light_brigandine_black_mail, itm_light_brigandine_red_mail, itm_light_brigandine_yellow_mail, itm_hose_kneecops_red, itm_mail_mittens, itm_zitta_bascinet, itm_zitta_bascinet_novisor, itm_kettle_hat_mail2, itm_kettle_hat_mail3,itm_ebony_long_sword],def_attrib|horse_attrib_6|level(15),wp(180),knows_spearman_3|knows_power_strike_2|knows_ironflesh_9,man_face_young_1,man_face_middle_2],


["hired_assassin","Hired Assassin","Hired Assassin",tf_vampire|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners, [itm_armor7,itm_armor8,itm_armor9,itm_woolen_hose,itm_blue_hose,itm_wrapping_boots,itm_xenoargh_hornmask_black,itm_xenoargh_hornmask_black,itm_assassin_dagger],def_attrib|horse_attrib_8|level(20),wp(250),knows_spearman_3|knows_power_strike_10|knows_ironflesh_10,man_face_young_1,man_face_middle_2],

["fight_promoter","Rough-Looking Character","Rough-Looking Character",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_short_tunic,itm_linen_tunic,itm_coarse_tunic,itm_tabard,itm_leather_vest,itm_woolen_hose,itm_nomad_boots,itm_blue_hose,itm_wrapping_boots,itm_fur_hat,itm_leather_cap,itm_sword_viking_1],def_attrib|str_20|agi_16|level(20),wp(180),knows_common|knows_power_strike_5|knows_ironflesh_3,bandit_face1,bandit_face2],



["spy","Ordinary Townsman","Ordinary Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,[itm_sword_viking_1,itm_armor7,itm_leather_boots,itm_courser,itm_leather_gloves],def_attrib|agi_11|level(20),wp(130),knows_common,man_face_middle_1,man_face_older_2],

["spy_partner","Unremarkable Townsman","Unremarkable Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,[itm_sword_medieval_b,itm_armor7,itm_leather_boots,itm_courser,itm_leather_gloves],def_attrib|agi_11|level(10),wp(130),knows_common,vaegir_face1,vaegir_face2],

["nurse_for_lady","Nurse","Nurse",tf_female|tf_guarantee_armor,0,reserved,fac_commoners,[itm_robe,itm_black_hood,itm_wrapping_boots],def_attrib|level(4),wp(60),knows_common,woman_face_1,woman_face_2],
["temporary_minister","Minister","Minister",tf_guarantee_armor|tf_guarantee_boots,0,reserved,fac_commoners,[itm_rich_outfit,itm_wrapping_boots],def_attrib|level(4),wp(60),knows_common,man_face_middle_1,man_face_older_2],




["quick_battle_6_player", "{!}quick_battle_6_player", "{!}quick_battle_6_player", tf_hero, 0, reserved,  fac_player_faction, [itm_padded_cloth,itm_nomad_boots, itm_splinted_leather_greaves, itm_skullcap, itm_sword_medieval_b,  itm_crossbow, itm_bolts, itm_plate_covered_round_shield],    knight_attrib_1,wp(130),knight_skills_1, 0x000000000008010b01f041a9249f65fd],

#Multiplayer ai troops
["swadian_crossbowman_multiplayer_ai","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,[itm_bolts,itm_crossbow,itm_sword_medieval_a,itm_tab_shield_heater_b,itm_leather_jerkin,itm_leather_armor,itm_ankle_boots,itm_footman_helmet],def_attrib|level(19),wp_melee(90)|wp_crossbow(100),knows_common|knows_ironflesh_4|knows_physique_6|knows_shield_5|knows_power_strike_3,swadian_face_young_1,swadian_face_old_2],



#Multiplayer troops (they must have the base items only, nothing else)
["swadian_crossbowman_multiplayer","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,[itm_bolts,itm_crossbow,itm_sword_medieval_a,itm_tab_shield_heater_a,itm_red_shirt,itm_ankle_boots],def_attrib_multiplayer|level(19),wpe(90,60,180,90),knows_common|knows_ironflesh_2|knows_physique_5|knows_shield_5|knows_power_strike_2|knows_riding_1,swadian_face_young_1,swadian_face_old_2],
["swadian_infantry_multiplayer","Swadian Infantry","Swadian Infantry",tf_guarantee_all,0,0,fac_kingdom_1,[itm_sword_medieval_a,itm_tab_shield_heater_a,itm_red_tunic,itm_ankle_boots],def_attrib_multiplayer|level(20),wpex(105,130,110,40,60,110),knows_common|knows_ironflesh_5|knows_shield_4|knows_power_strike_4|knows_reserved_17_2|knows_physique_6|knows_riding_1,swadian_face_middle_1,swadian_face_old_2],
["swadian_man_at_arms_multiplayer","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,[itm_lance,itm_sword_medieval_a,itm_tab_shield_heater_a,itm_red_tunic,itm_ankle_boots,itm_saddle_horse],def_attrib_multiplayer|level(20),wp_melee(110),knows_common|knows_riding_5|knows_ironflesh_3|knows_shield_2|knows_reserved_17_2|knows_power_strike_3|knows_physique_3,swadian_face_young_1,swadian_face_old_2],
#  ["swadian_mounted_crossbowman_multiplayer","Swadian Mounted Crossbowman","Swadian Mounted Crossbowmen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
#   [itm_bolts,itm_light_crossbow,itm_tab_shield_heater_cav_a,itm_bastard_sword_a,
#    itm_red_shirt,itm_hide_boots,itm_saddle_horse],
#   def_attrib_multiplayer|level(20),wp_melee(100)|wp_crossbow(120),knows_common|knows_riding_4|knows_shield_3|knows_ironflesh_3|knows_horse_archery_2|knows_power_strike_3|knows_physique_2|knows_shield_2,swadian_face_young_1, swadian_face_old_2],
["vaegir_archer_multiplayer","Vaegir Archer","Vaegir Archers",tf_guarantee_all,0,0,fac_kingdom_2,[itm_arrows,itm_scimitar,itm_nomad_bow,itm_linen_tunic,itm_hide_boots],def_attrib_multiplayer|str_12|level(19),wpe(80,150,60,80),knows_ironflesh_2|knows_power_draw_6|knows_physique_4|knows_shield_2|knows_riding_1,vaegir_face_young_1,vaegir_face_older_2],
["vaegir_spearman_multiplayer","Vaegir Spearman","Vaegir spearman",tf_guarantee_ranged|tf_guarantee_all_wo_horse,0,0,fac_kingdom_2,[itm_spear,itm_tab_shield_kite_a,itm_mace_1,itm_linen_tunic,itm_hide_boots],def_attrib_multiplayer|str_12|level(19),wpex(110,100,130,30,50,120),knows_ironflesh_4|knows_shield_2|knows_reserved_17_3|knows_power_strike_3|knows_physique_6|knows_riding_1,vaegir_face_young_1,vaegir_face_older_2],
["vaegir_horseman_multiplayer","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_2,[itm_scimitar,itm_lance,itm_tab_shield_kite_cav_a,itm_linen_tunic,itm_hide_boots,itm_saddle_horse],def_attrib_multiplayer|level(19),wpe(110,90,60,110),knows_riding_5|knows_ironflesh_3|knows_power_strike_2|knows_shield_3|knows_reserved_17_2,vaegir_face_young_1,vaegir_face_older_2],
["khergit_veteran_horse_archer_multiplayer","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,[itm_sword_khergit_1,itm_nomad_bow,itm_arrows,itm_tab_shield_small_round_a,itm_khergit_armor,itm_leather_steppe_cap_a,itm_hide_boots,itm_steppe_horse],def_attrib_multiplayer|level(21),wpe(80,150,60,100),knows_riding_6|knows_power_draw_5|knows_shield_2|knows_horse_archery_5|knows_physique_3,khergit_face_middle_1,khergit_face_older_2],
["khergit_lancer_multiplayer","Khergit Lancer","Khergit Lancers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,[itm_sword_khergit_1,itm_lance,itm_tab_shield_small_round_a,itm_khergit_armor,itm_leather_steppe_cap_a,itm_hide_boots,itm_steppe_horse],def_attrib_multiplayer|level(21),wp(115),knows_riding_6|knows_ironflesh_3|knows_reserved_17_3|knows_shield_2|knows_horse_archery_1|knows_power_strike_2|knows_physique_5,khergit_face_middle_1,khergit_face_older_2],
["nord_archer_multiplayer","Nord Archer","Nord Archers",tf_guarantee_all,0,0,fac_kingdom_4,[itm_arrows,itm_sword_viking_2_small,itm_short_bow,itm_blue_tunic,itm_leather_boots],def_attrib_multiplayer|str_11|level(15),wpe(90,150,60,80),knows_ironflesh_2|knows_power_strike_2|knows_shield_2|knows_power_draw_5|knows_physique_4|knows_riding_1,nord_face_young_1,nord_face_old_2],
["nord_veteran_multiplayer","Nord Huscarl","Nord Huscarls",tf_guarantee_all,0,0,fac_kingdom_4,[itm_sword_viking_1,itm_one_handed_war_axe_a,itm_tab_shield_round_a,itm_blue_tunic,itm_leather_boots],def_attrib_multiplayer|level(24),wpex(110,135,100,40,60,140),knows_ironflesh_4|knows_power_strike_5|knows_reserved_17_4|knows_physique_6|knows_shield_3|knows_riding_1,nord_face_young_1,nord_face_older_2],
["nord_scout_multiplayer","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,[itm_javelin,itm_sword_viking_1,itm_spear,itm_tab_shield_small_round_a,itm_blue_tunic,itm_leather_boots,itm_saddle_horse],def_attrib_multiplayer|level(19),wp(105),knows_riding_6|knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_horse_archery_2|knows_reserved_17_3|knows_physique_3,vaegir_face_young_1,vaegir_face_older_2],
["rhodok_veteran_crossbowman_multiplayer","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,[itm_crossbow,itm_bolts,itm_fighting_pick,itm_tab_shield_pavise_a,itm_tunic_with_green_cape,itm_ankle_boots],def_attrib_multiplayer|level(20),wpe(100,60,180,90),knows_common|knows_ironflesh_2|knows_shield_2|knows_power_strike_2|knows_physique_5|knows_riding_1,rhodok_face_middle_1,rhodok_face_older_2],
["rhodok_sergeant_multiplayer","Rhodok Sergeant","Rhodok Sergeants",tf_guarantee_all,0,0,fac_kingdom_5,[itm_fighting_pick,itm_tab_shield_pavise_a,itm_spear,itm_green_tunic,itm_ankle_boots],def_attrib_multiplayer|level(20),wpex(110,100,140,30,50,110),knows_common|knows_ironflesh_4|knows_shield_5|knows_power_strike_4|knows_reserved_17_1|knows_physique_6|knows_riding_1,rhodok_face_middle_1,rhodok_face_older_2],
["rhodok_horseman_multiplayer","Rhodok Horseman","Rhodok Horsemen",tf_guarantee_all,0,0,fac_kingdom_5,[itm_sword_medieval_a,itm_tab_shield_heater_cav_a,itm_light_lance,itm_green_tunic,itm_ankle_boots,itm_saddle_horse],def_attrib_multiplayer|level(20),wp(100),knows_riding_4|knows_ironflesh_3|knows_shield_2|knows_power_strike_2|knows_reserved_17_1|knows_physique_3,rhodok_face_middle_1,rhodok_face_older_2],
["sarranid_archer_multiplayer","Sarranid Archer","Sarranid Archers",tf_guarantee_all,0,0,fac_kingdom_6,[itm_arrows,itm_arabian_sword_a,itm_nomad_bow,itm_sarranid_cloth_robe,itm_sarranid_boots_b],def_attrib_multiplayer|str_12|level(19),wpe(80,150,60,80),knows_ironflesh_2|knows_power_draw_5|knows_physique_5|knows_shield_2|knows_riding_1,vaegir_face_young_1,vaegir_face_older_2],
["sarranid_footman_multiplayer","Sarranid Footman","Sarranid footman",tf_guarantee_all,0,0,fac_kingdom_6,[itm_bamboo_spear,itm_tab_shield_kite_a,itm_arabian_sword_a,itm_sarranid_cloth_robe,itm_sarranid_boots_b],def_attrib_multiplayer|str_12|level(19),wpex(110,100,130,30,50,120),knows_ironflesh_4|knows_shield_2|knows_reserved_17_3|knows_power_strike_3|knows_physique_6|knows_riding_1,vaegir_face_young_1,vaegir_face_older_2],
["sarranid_mamluke_multiplayer","Sarranid Mamluke","Sarranid Mamluke",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_6,[itm_arabian_sword_a,itm_lance,itm_tab_shield_small_round_a,itm_sarranid_cloth_robe,itm_sarranid_boots_b,itm_saddle_horse],def_attrib_multiplayer|level(19),wpe(110,90,60,110),knows_riding_5|knows_ironflesh_3|knows_power_strike_2|knows_shield_3|knows_reserved_17_2,vaegir_face_young_1,vaegir_face_older_2],

["multiplayer_end","{!}multiplayer_end","{!}multiplayer_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],

#replacable troop, not used
["nurse","Nurse","{!}nurse",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
#erase later added to avoid errors

#Player history array
["log_array_entry_type",            "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
["log_array_entry_time",            "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
["log_array_actor",                 "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
["log_array_center_object",         "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
["log_array_center_object_lord",    "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
["log_array_center_object_faction", "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
["log_array_troop_object",          "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
["log_array_troop_object_faction",  "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
["log_array_faction_object",        "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],


["tutorial_fighter_1","Novice Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,[itm_linen_tunic,itm_nomad_boots],def_attrib|level(1),wp_melee(10),knows_physique_1|knows_ironflesh_2|knows_shield_2,0x000000088c1073144252b1929a85569300000000000496a50000000000000000,vaegir_face_older_2],
["tutorial_fighter_2","Novice Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,[itm_green_tunic,itm_nomad_boots],def_attrib|level(1),wp_melee(10),knows_physique_1|knows_ironflesh_2|knows_shield_2,0x000000088b08049056ab56566135c46500000000001dda1b0000000000000000,vaegir_face_older_2],
["tutorial_fighter_3","Regular Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,[itm_green_tunic,itm_nomad_boots],def_attrib|level(9),wp_melee(50),knows_physique_1|knows_ironflesh_2|knows_shield_2,0x00000008bc00400654914a3b0d0de74d00000000001d584e0000000000000000,vaegir_face_older_2],
["tutorial_fighter_4","Veteran Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,[itm_linen_tunic,itm_nomad_boots],def_attrib|level(16),wp_melee(110),knows_physique_1|knows_ironflesh_3|knows_power_strike_2|knows_shield_2,0x000000089910324a495175324949671800000000001cd8ab0000000000000000,vaegir_face_older_2],
["tutorial_archer_1","Archer","Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,[itm_leather_jerkin,itm_leather_vest,itm_nomad_boots,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet,itm_vaegir_fur_cap,itm_nomad_cap],def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_physique_2|knows_reserved_17_1,vaegir_face_young_1,vaegir_face_older_2],
["tutorial_master_archer","Archery Trainer","Archery Trainer",tf_hero,0,0,fac_kingdom_2,[itm_linen_tunic,itm_nomad_boots],def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_physique_2|knows_reserved_17_1,0x0000000ea508540642f34d461d2d54a300000000001d5d9a0000000000000000,vaegir_face_older_2],
["tutorial_rider_1","Rider","{!}Vaegir Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_2,[itm_green_tunic,itm_hunter,itm_saddle_horse,itm_leather_gloves],def_attrib|level(24),wp(130),knows_riding_4|knows_shield_2|knows_ironflesh_3|knows_power_strike_2,vaegir_face_middle_1,vaegir_face_older_2],
["tutorial_rider_2","Horse archer","{!}Khergit Horse Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_kingdom_3,[itm_tribal_warrior_outfit,itm_nomad_robe,itm_hide_boots,itm_tab_shield_small_round_a,itm_steppe_horse],def_attrib|level(14),wp(80)|wp_archery(110),knows_riding_5|knows_power_draw_3|knows_ironflesh_1|knows_horse_archery_4|knows_reserved_17_1,khergit_face_young_1,khergit_face_older_2],
["tutorial_master_horseman","Riding Trainer","Riding Trainer",tf_hero,0,0,fac_kingdom_2,[itm_leather_vest,itm_nomad_boots],def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_physique_2|knows_reserved_17_1,0x0000000ea0084140478a692894ba185500000000001d4af30000000000000000,vaegir_face_older_2],

["swadian_merchant", "Merchant of Praven", "{!}Prominent", tf_hero|tf_randomize_face|tf_guarantee_all_wo_ranged, 0, reserved, fac_kingdom_1, [itm_sword_medieval_d_long, itm_courtly_outfit, itm_leather_boots], def_attrib_nobel|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
["vaegir_merchant", "Merchant of Reyvadin", "{!}Prominent", tf_hero|tf_randomize_face|tf_guarantee_all_wo_ranged, 0, reserved, fac_kingdom_2, [itm_knightaxe, itm_kaftan, itm_woolen_hose], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
["khergit_merchant", "Merchant of Tulga", "{!}Prominent", tf_hero|tf_randomize_face|tf_guarantee_all_wo_ranged, 0, reserved, fac_kingdom_3, [itm_sword_khergit_4, itm_red_gambeson, itm_nomad_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
["nord_merchant", "Merchant of Sargoth", "{!}Prominent", tf_hero|tf_randomize_face|tf_guarantee_all_wo_ranged, 0, reserved, fac_kingdom_4, [itm_trgba, itm_red_gambeson, itm_nomad_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
["rhodok_merchant", "Merchant of Jelkala", "{!}Prominent", tf_hero|tf_randomize_face|tf_guarantee_all_wo_ranged, 0, reserved, fac_kingdom_5, [itm_sword_medieval_d_long, itm_leather_jerkin, itm_blue_hose], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
["sarranid_merchant", "Merchant of Shariz", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_6, [itm_scimitar_sulatn, itm_sarranid_cloth_robe, itm_sarranid_boots_a], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
["startup_merchants_end","startup_merchants_end","startup_merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],

["sea_raider_leader","Sea Raider Captain","Sea Raiders",tf_hero|tf_guarantee_all_wo_ranged,0,0,fac_outlaws,[itm_arrows,itm_sword_viking_1,itm_sword_viking_2,itm_fighting_axe,itm_battle_axe,itm_spear,itm_nordic_shield,itm_nordic_shield,itm_nordic_shield,itm_wooden_shield,itm_long_bow,itm_javelin,itm_throwing_axes,itm_nordic_helmet,itm_nordic_helmet,itm_nasal_helmet,itm_mail_shirt,itm_byrnie,itm_mail_hauberk,itm_leather_boots,itm_nomad_boots],def_attrib|level(24),wp(110),knows_ironflesh_2|knows_power_strike_2|knows_power_draw_3|knows_reserved_17_2|knows_riding_1|knows_physique_2,nord_face_young_1,nord_face_old_2],

["looter_leader","Robber","Looters",tf_hero,0,0,fac_outlaws,[itm_hatchet,itm_club,itm_butchering_knife,itm_falchion,itm_rawhide_coat,itm_stones,itm_nomad_armor,itm_nomad_armor,itm_woolen_cap,itm_woolen_cap,itm_nomad_boots,itm_wrapping_boots],def_attrib|level(4),wp(20),knows_common,0x00000001b80032473ac49738206626b200000000001da7660000000000000000,bandit_face2],

["bandit_leaders_end","bandit_leaders_end","bandit_leaders_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],

["relative_of_merchant", "Merchant's Brother", "{!}Prominent",tf_hero,0,0,fac_kingdom_2,[itm_linen_tunic,itm_nomad_boots],def_attrib|level(1),wp_melee(10),knows_physique_1|knows_ironflesh_2|knows_shield_2,0x00000000320410022d2595495491afa400000000001d9ae30000000000000000,mercenary_face_2],

["relative_of_merchants_end","relative_of_merchants_end","relative_of_merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],

##diplomacy begin
["dplmc_chamberlain","Chamberlain Aubrey de Vere", "Chamberlains",tf_hero|tf_male,0,0,fac_commoners,[itm_tabard, itm_leather_boots], def_attrib|level(10), wp(40),knows_inventory_management_10,0x0000000dfc0c238838e571c8d469c91b00000000001e39230000000000000000],

["dplmc_constable","Constable Miles de Gloucester","Constables",tf_hero|tf_male,0,0,fac_commoners,[itm_bnw_armour, itm_leather_boots],knight_attrib_4,wp_melee(200),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_4|knows_physique_4,0x0000000b4b1015054b1b4d591cba28d300000000001e472b0000000000000000],

["dplmc_chancellor","Chancellor Herfast","Chancellors",tf_hero|tf_male,0,0,fac_commoners,[itm_nobleman_outfit, itm_leather_boots],def_attrib|level(10), wp(40),knows_inventory_management_10, 0x00000009a20c21cf491bad28a28628d400000000001e371a0000000000000000],

["dplmc_messenger","Messenger","Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_neutral,[itm_sword_medieval_b,itm_armor7,itm_leather_boots,itm_courser,itm_leather_gloves,itm_light_crossbow,itm_bolts],def_attrib|agi_21|int_30|cha_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_leadership_7,man_face_young_1,man_face_old_2],

["dplmc_scout","Scout","Scouts",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_neutral,[itm_sword_medieval_b,itm_armor7,itm_leather_boots,itm_courser,itm_leather_gloves,itm_light_crossbow,itm_bolts],def_attrib|agi_21|int_30|cha_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_leadership_7,man_face_young_1,man_face_old_2],
# recruiter kit begin
["dplmc_recruiter","Recruiter","Recruiter",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_neutral,[itm_sword_medieval_b,itm_armor7,itm_leather_boots,itm_courser,itm_leather_gloves,itm_light_crossbow,itm_bolts],def_attrib|agi_21|int_30|cha_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_leadership_7,swadian_face_young_1,swadian_face_old_2],
# recruiter kit end
##diplomacy end

   
["cheat_man", "cheat_man", "cheat_man", tf_guarantee_all_wo_ranged, 0, 0, fac_neutral, [itm_flamberge_fire,itm_golem_crusher,itm_ebony_blade,itm_khorne_axe,itm_angel_blade,itm_flame_blade,itm_aurora_blade,itm_serpent_sword,itm_dawnbreaker,itm_destroyer,itm_skycutter,itm_frostmourne,itm_zamorak,itm_excalibur_2,
itm_felguard_body,itm_felguard_calf,itm_khorne_helm], def_attrib|level(80), wp(500), knows_light_swordman_8|knows_physique_10|knows_ironflesh_8|knows_power_strike_10, swadian_face_middle_2, swadian_face_older_2 ],

["quartermaster", "Quartermaster","{!}Quartermaster",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,            itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],

["kingdom_1_reward", "{!}reward","{!}reward",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_kingdom_1,
  [itm_armored_horse_france,itm_charger_france,itm_charger_france_2,itm_charger_teuton,itm_griffin, 
   itm_swadian_steel_bolts,
   itm_gondor_gauntlets,itm_iron_greaves,itm_elf_foot,itm_elf_hand,
   itm_elf_plate,itm_swan_milanese_plate,itm_gondor_fountain_armor,itm_white_twiligh_armor,itm_dol_very_heavy_mail,itm_empire_priest,
   itm_black_helmet_2,itm_winged_great_helmet_teu,itm_horned_great_helmet_2,itm_black_helmet2,itm_winged_great_helmet_blue,itm_french_helm_2,itm_french_helm_3,
   itm_amroth_sword_c,itm_crusader_sword_1,itm_gondor_ranger_sword,itm_sword_medieval_d_long,itm_crusader_sword_2,
   itm_crossbow_cannon,itm_gothic_lance,itm_great_lance_dark,
   itm_gondor_shield_d,itm_gondor_shield_e,itm_dol_shield_b,
   itm_van_helsing_crossbow,itm_bastard_sword_c,itm_bastard_sword_d,
   itm_trophy_a,itm_trophy_b,itm_bastard_sword_d_fire,itm_war_clerics_warhammer_2,
  ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  
["kingdom_2_reward", "{!}reward","{!}reward",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_kingdom_2,
  [itm_hunter_steppe,itm_hunter_steppe_good,itm_vaegir_warhorse,itm_charger_noble,itm_charger,
   itm_lamellar_gauntlets,itm_rus_splint_greaves,
   itm_breastplate_polish,itm_polish_hussar_armor,itm_polish_hussar_armor_wing,itm_lamellar_armor,itm_rus_scale,itm_gothic_plate,
   itm_hounskull,itm_french_helm_closed,itm_polish_husar_helmet,itm_litchina_helm,
   itm_scimitar_long,itm_gwilith,itm_scimitar_b,itm_scimitar,itm_knightaxe,itm_rapierd,itm_sword_khergit_4,itm_sword_khergit_3,
   itm_gothic_lance,itm_great_lance_dark,itm_great_lance2,itm_hussar_lance,itm_hussar_lance_2,
   itm_tab_shield_kite_d,itm_tab_shield_kite_c,itm_tab_shield_kite_cav_b,
   itm_war_bow,itm_mushket_udarniy,itm_flintlock_pistol_elite_2,itm_trophy_b,itm_felguard_body
  ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["kingdom_3_reward", "{!}reward","{!}reward",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_kingdom_3,
  [itm_coursera1,itm_coursera2,itm_huntera1,itm_huntera2,itm_warhorse_steppe,itm_khergit_charger,itm_khergit_war_horse,
   itm_flame_arrows,itm_khergit_mask,itm_rus_splint_greaves,itm_khergit_lamellar_armor,itm_lamellar_gauntlets,itm_khergit_guard_helmet,itm_khergit_guard_boots,itm_khergit_guard_armor,itm_lamellar_armor_black,itm_khergit_elite_armor,itm_lamellar_vest_black,itm_litchina_helm,
   itm_scimitar_b,itm_blinding_sand,itm_one_handed_battle_axe_c,itm_kwan_dao,itm_hafted_blade_a,itm_sword_khergit_4,itm_sword_khergit_3,itm_khergit_sword_two_handed_a,itm_khergit_sword_two_handed_b,itm_strange_sword,itm_strange_great_sword,itm_khergit_lance,itm_dec_steel_shield,
   itm_nahptha_bomb,itm_khergit_bow,itm_trophy_a,itm_trophy_b,itm_nomad_bow,itm_throwing_star_a,itm_slaughter_axe,itm_jingubang,itm_gwilith
  ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["kingdom_4_reward", "{!}reward","{!}reward",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_kingdom_4,
  [itm_warhorse_england,itm_warhorse_england_2,itm_charger_england,itm_pegasus,
   itm_hourglass_gauntlets_ornate,itm_steel_greaves,
   itm_mirkwood_armor_e,itm_mirkwood_helm_d,itm_woodelf_mutil_arrows,itm_woodelf_arrows_poison,itm_sabre_2h_green,itm_dragon_foot,
   itm_mirkwood_armor_f,itm_dragon_plate,itm_dragon_knight_hand,itm_half_plates_red_2,itm_half_plates_red,itm_plate_armor_2,itm_gothic_plate_nobevor,itm_gothic_plate,
   itm_dragon_head,itm_winged_great_helmet,itm_mirkwood_helm_e,itm_fast_travel_boot,itm_open_sallet_coif,
   itm_bastard_sword_e,itm_glass_halberd,itm_charm_bow,itm_mirkwood_sword_reward,
   itm_glass_mace,itm_one_handed_battle_axe_b,itm_glass_long_mace,itm_glass_sword_a,
   itm_glass_lance,itm_glass_lance_2,
   itm_long_bow_2,itm_sldequiver,itm_elven_bow,itm_black_bow,itm_trophy_a,itm_trophy_b,itm_mirkwood_bow,itm_piercing_arrows,itm_scottish_claymore
 ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],


["kingdom_5_reward", "{!}reward","{!}reward",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_kingdom_5,
  [itm_charger_noble,itm_undead_charger_plate,itm_undead_charger_2,
   itm_charger_old,itm_skull_staff,
   itm_undead_shield_kite_cav,itm_death_knight_shield,itm_black_greaves,
   itm_milanese_gauntlets,itm_steel_greaves,itm_black_plate_armor_1,itm_black_plate_armor_2,itm_corrazina_green,itm_half_plates_green,
   itm_twilight_boots,itm_twiligh_armor,itm_knight_plate,itm_heraldic_harness,itm_milanese_plate,
   itm_twilight_helm,itm_milanese_sallet,itm_twilight_gloves,itm_frankenstein_head,itm_zitta_bascinet_novisor,itm_death_skull,
   itm_morningstar,itm_ebony_long_mace,itm_sword_medieval_c_small,itm_ebony_arming_sword,itm_ebony_long_sword,itm_great_mace,itm_ebony_great_sword,itm_gothic_lance,
   itm_ebony_throwing_pike,itm_ebony_poleaxe,itm_rhod_crossbow,itm_van_helsing_crossbow,itm_rhod_sniper_crossbow,itm_black_bow,itm_soul_stealer,itm_trophy_a,itm_trophy_b
  ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  
["kingdom_6_reward", "{!}reward","{!}reward",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_kingdom_6,
 [itm_hunter_steppe,itm_arabian_horse_b,itm_lamellar_warhorse,itm_lamellar_warhorse_2,itm_lamellar_charger,itm_warhorse_sarranid,
  itm_flame_arrows,itm_lamellar_gauntlets,itm_rus_splint_greaves,itm_sarranid_boots_d,itm_sarranid_elite_armor,itm_mamluke_mail,itm_arabian_armor_b,itm_sarranid_veiled_helmet,
   itm_scimitar_sulatn,itm_scimitar_b,itm_sarranid_cavalry_sword,itm_arabian_sword_d,itm_sword_khergit_4,itm_sarranid_two_handed_mace_1,itm_sarranid_mace_1,itm_sarranid_axe_a,itm_sarranid_axe_b,itm_sarranid_two_handed_axe_a,itm_sarranid_two_handed_axe_b,itm_khergit_lance,itm_dec_steel_shield,
   itm_nahptha_bomb,itm_war_bow,itm_trophy_a,itm_trophy_b,itm_flame_blade,itm_trophy_c,itm_flamberge_fire
  ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["kingdom_7_reward", "{!}reward","{!}reward",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_kingdom_7,
 [itm_armor_demi_griffin,itm_warhorse_german,itm_charger_german,itm_charger_plate_german,
  itm_hourglass_gauntlets_ornate,itm_steel_greaves,itm_pistol_2stwol,
  itm_red_armour_4,itm_blue_armour_5,itm_maximilian_plate,itm_half_plates_yello,itm_german_armour_5,itm_german_armour_6,itm_bane_blade_plate,itm_knight_plate_5,itm_gothic_plate,itm_gothic_plate_nobevor,
  itm_bane_blade_head,itm_new_sallet,itm_winged_great_helmet_ger,itm_bane_blade_hand,itm_sallet_coif,itm_bane_blade_foot,
  itm_empire_warhammer,itm_ebony_long_mace,itm_aurora_blade,itm_ebony_great_sword,itm_sword_two_handed_c,itm_sword_two_handed_c_alt,itm_flamberge,itm_flamberge_alt,itm_ebony_arming_sword,itm_rapierd,itm_great_mace,itm_great_lance,itm_gothic_lance,
  itm_zlmg,itm_flintlock_pistol_4s,itm_heavy_muscket_4,itm_trophy_a,itm_trophy_b,itm_morrigan
 ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
 
 
["kingdom_8_reward", "{!}reward","{!}reward",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_kingdom_8,
 [itm_vaegir_warhorse,itm_drow_basilisk,itm_hunter_steppe_good,itm_vaegir_charger,itm_vaegir_charger_2,itm_drow_basilisk_2,
 itm_dragon_knight_hand,itm_steel_greaves,
 itm_plate_armor,itm_lamellar_vest_khergit,itm_kuyak,itm_lamellar_armor,itm_rus_lamellar_a,itm_rus_lamellar_b,itm_rus_scale,
 itm_dragon_foot,itm_dragon_head,itm_drow_lance,
 itm_morningstar,itm_ebony_scimitar_2,itm_ebony_scimitar_1,itm_ebony_scimitar_long_1,
 itm_sword_khergit_5,itm_sword_khergit_6,itm_dragon_plate,itm_charonscall,
 itm_ebony_scimitar_long_3,itm_drow_plate,itm_drow_plate_foot,itm_drow_plate_hand,itm_flintlock_pistol_elite_1,
 itm_trophy_a,itm_trophy_b,itm_serpent_dagger,itm_granata_small,itm_lordaeron
 ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
 
 
["kingdom_9_reward", "{!}reward","{!}reward",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_kingdom_9,
  [itm_nightmare,itm_arabian_horse_b,itm_lamellar_warhorse,itm_nightmare_armor,itm_lamellar_charger,itm_warhorse_sarranid,
   itm_flame_arrows,
   itm_tzeentch_charger,itm_rus_splint_greaves,itm_turk_mail_heavy,itm_turk_armor,
   itm_sarranid_veiled_helmet,itm_chichak1,itm_chichak2,
   itm_chaos_warrior_shield,itm_chaos_knight_shield,itm_chaos_chosen_shield,itm_khorne_shield,itm_dec_steel_shield,itm_demon_knight_shield,
   itm_chaos_sword3,itm_chaos_sword4,itm_chaos_sword5,
   itm_rhun_armor_7,itm_rhun_armor_8,itm_rhun_armor_9,itm_demon_knight_plate,
   itm_chaos_leg_2,itm_chaos_leg_1,itm_chaos_leg_3,itm_demon_knight_leg,
   itm_rhun_helm_7,itm_rhun_helm_8,itm_rhun_helm_7_2,itm_rhun_helm_9,itm_demon_knight_head,itm_demon_knight_hand,
   itm_sarranid_mace_2,itm_sarranid_double_axe,itm_sarranid_cavalry_sword,itm_arabian_sword_d,
   itm_sarranid_two_handed_mace_1,itm_morrigan,itm_burning_axe,itm_sarranid_axe_b,itm_sarranid_two_handed_axe_a,itm_sarranid_two_handed_axe_b,itm_khergit_lance,

   itm_nahptha_bomb,itm_turk_musket_good,itm_turk_musket,itm_trophy_a,itm_trophy_b,itm_serpent_sword,itm_assassin_dagger,itm_sloth_crossbow,itm_felguard_calf],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
   
 ["kingdom_10_reward","{!}reward","{!}reward",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_kingdom_10,
  [itm_warhorse,itm_nord_warhorse,
  itm_plate_mittens,itm_nord_plate_boots,itm_gothic_plate_2,itm_huscarl_armor,
  itm_huscarl_armor_2,itm_dawnguard_armor,itm_cuir_bouilli,itm_huscarl_armor_3,itm_huscarl_armor_4,itm_plate_armor,itm_nord_knight_plate,
  itm_nordic_huscarl_helmet,itm_nordic_warlord_helmet,itm_nord_berserker_mask,itm_nord_norman_mask,itm_horned_great_helmet,itm_dawnguard_helmet,itm_great_helmet3,itm_open_sallet_coif,
  itm_dawnguard_greatsword,itm_frostfang,itm_ebony_double_axe,itm_dragon_shield_2,itm_one_handed_battle_axe_b,itm_stahlrim_axe,itm_nordhero_long_axe,itm_thunder_staff,itm_long_axe_c,itm_double_axe,itm_stalhrim_sword,itm_nordhero_sword_long,itm_nordhero_greatsword_2,itm_great_lance_dark,itm_dawnguard_shield,itm_tab_shield_round_e,itm_long_axe_d,
  itm_trophy_a,itm_trophy_b,itm_throwing_gungnir,itm_nord_throwing_spears,itm_vk_axe,itm_throwing_pike
  ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["kingdom_11_reward","{!}reward","{!}reward",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_kingdom_11,
  [
   itm_hourglass_gauntlets_ornate,itm_steel_greaves,itm_brigandine_black,
   itm_cartridges_cannon,
   itm_half_plates_yello,itm_half_plates_yello,itm_knight_plate,itm_heraldic_plate,itm_combed_morion_3,itm_combed_morion,itm_combed_morion_2,itm_classichelm_plume,itm_winged_great_helmet,itm_sallet_coif,itm_sturmhaube_bnw3,
   itm_morningstar,itm_morningstar2,itm_sword_two_handed_a,itm_sword_medieval_b,itm_espada_eslavona_b,itm_side_sword,
   itm_great_lance,itm_gothic_lance,itm_great_lance_dark,
   itm_steel_shield,itm_tab_shield_pavise_cav,itm_eoro_musket,itm_mushket_udarniy,itm_carbine_batarey_2shot,itm_carbine_batarey_good,
   itm_trophy_a,itm_trophy_b,itm_nord_jarid,itm_colt1855,itm_nord_javelin,itm_hand_cannon
  ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["kingdom_12_reward","{!}reward","{!}reward",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_kingdom_12,
  [itm_camel3,itm_camel2,itm_hunter_steppe,itm_arabian_horse_b,itm_lamellar_warhorse,itm_warhorse_sarranid,
   itm_flame_arrows,itm_lamellar_gauntlets,itm_rus_splint_greaves,itm_sarranid_boots_d,itm_mamluke_mail,itm_lamellar_vest_khergit,itm_sarranid_veiled_helmet,
   itm_scimitar_b,itm_sarranid_cavalry_sword,itm_arabian_sword_d,itm_sarranid_two_handed_mace_1,itm_sarranid_mace_1,itm_sarranid_axe_a,itm_sarranid_axe_b,itm_sarranid_two_handed_axe_a,itm_sarranid_two_handed_axe_b,itm_dec_steel_shield,itm_carbine_batarey_2shot,itm_carbine_batarey_good,
   itm_trophy_a,itm_trophy_b,itm_nomad_bow,itm_nord_jarid,itm_nord_throwing_spears,itm_nord_javelin,itm_granata_small,itm_chaos_axe
 ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["kingdom_13_reward","{!}reward","{!}reward",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_kingdom_13,
 [itm_warhorse_teuton,itm_charger_teuton,itm_charger_teuton,itm_charger_old,
  itm_hourglass_gauntlets_ornate,itm_steel_greaves,itm_angel_blade,itm_sg_yellow_big,itm_teu_surcoat_over_mail_1,itm_dol_hauberk,itm_gondor_armor_low,itm_gondor_armor_med,itm_teu_surcoat_over_mail_2,itm_gothic_plate,itm_gothic_plate_nobevor,
  itm_horned_great_helmet,itm_horned_great_helmet_2,itm_winged_great_helmet_teu,itm_sallet_coif,itm_open_sallet_coif,itm_morningstar,itm_morningstar2,itm_bastard_sword_f,itm_sword_two_handed_a,itm_flamberge,itm_flamberge_alt,itm_knightaxe,itm_sword_medieval_d_long,
  itm_great_lance,itm_gothic_lance,itm_great_lance_dark,itm_steel_shield,itm_sniper_crossbow,itm_eoro_musket,
  itm_trophy_a,itm_trophy_b,itm_eggshield_2
 ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["kingdom_14_reward", "{!}reward","{!}reward",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_kingdom_14,
  [itm_hunter_steppe,itm_hunter_steppe_good,itm_warhorse_steppe,itm_vaegir_warhorse,itm_vaegir_charger_2,
   itm_lamellar_gauntlets,itm_rus_splint_greaves,
   itm_rus_lamellar_b,itm_rus_lamellar_a,itm_lamellar_armor,itm_rus_scale,itm_vaegir_elite_armor,
   itm_hounskull,itm_french_helm_closed,itm_polish_husar_helmet,itm_litchina_helm,
   itm_scimitar_long,itm_scimitar_sulatn,itm_scimitar_b,itm_scimitar,itm_knightaxe,itm_cav_bardiche,itm_sword_khergit_3,
   itm_hussar_lance_short,itm_hussar_lance,
   itm_tab_shield_kite_d,itm_tab_shield_kite_c,itm_tab_shield_kite_cav_b,
   itm_war_bow,itm_flintlock_pistol_elite_1,itm_flintlock_pistol_elite_2,itm_trophy_b,itm_frostfang
  ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],

["musican_male","Musican","Musican",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_short_tunic, itm_linen_tunic, itm_tabard, itm_woolen_hose, itm_blue_hose],def_attrib|level(4),wp(60),knows_common,man_face_young_1,man_face_old_2],
["musican_female","Musican","Musican",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_blue_dress,itm_dress,itm_woolen_dress,itm_peasant_dress,itm_woolen_hose,itm_blue_hose,itm_wimple_a,itm_wimple_with_veil,itm_female_hood],def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
["musicans_end","Madame","Madame",tf_female|tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_commoners,[itm_lady_dress_blue,itm_lady_dress_green,itm_lady_dress_ruby,itm_leather_boots],def_attrib|level(5),wp(20),knows_common,0x0000000199041002736b7b6b14cab89b00000000001a390d0000000000000000,0x0000000480000005450b0f48dd2568d600000000001deb740000000000000000],

["nameless", "Nameless Enchanter","Nameless Enchanter",tf_hero, 0, 0, fac_commoners,[itm_zamorak,itm_ebony_blade,itm_tzeentch_charger,itm_twilight_gloves,itm_caesar_mask,itm_nilfurs_boast,itm_archlich_armor],
str_100|agi_100|int_18|cha_10|level(30),wp(300)|wp_firearm(300),knows_knight_6|knows_horse_archery_8|knows_magic_8, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],

  ["goblin_bomber2","goblin Bomber","goblin Bomber",
   tf_goblin|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_orc,
   [itm_barrel_bomb,
    itm_org_armour_4,itm_org_armour_4,
    itm_org_boot_2,itm_org_helmet_1,itm_org_helmet_1,itm_org_helmet_1],
   ranged_attrib_5|level(19),wp(150),knows_physique_10|knows_power_strike_4|knows_ironflesh_10|knows_reserved_18_10|knows_weapon_master_10|knows_magic_defence_1,bandit_face1, bandit_face2],

  ["rat_bomber2", "rat Bomber", "rat Bomber", 
   tf_goblin|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_beast,
   [
    itm_barrel_bomb,
    itm_rat_armor_8,itm_rat_armor_9,itm_rat_armor_10,
    itm_rus_shoes,
    itm_rathelm2,itm_wolfgloves,itm_cheese
   ],
   ranged_attrib_4|level(20),wp(180),knows_physique_10|knows_power_strike_4|knows_ironflesh_10|knows_reserved_18_10|knows_weapon_master_10|knows_magic_defence_1,bandit_face1, bandit_face2],


]


#Troop upgrade declarations

upgrade(troops,"farmer","watchman")
upgrade2(troops,"townsman","caravan_guard","manhunter")



#upgrade2(troops,"watchman","mercenary_swordsman","mercenary_crossbowman")
#upgrade2(troops,"mercenary_swordsman","hired_blade","hired_twohander")




upgrade2(troops,"we_noble_lad","dis_knight_1","we_knight_1")
upgrade(troops,"dis_knight_1","dis_knight_2")
upgrade(troops,"dis_knight_2","dis_knight_3")

upgrade(troops, "we_knight_1", "we_knight_2"),
upgrade(troops, "we_knight_2", "we_knight_3"),


#upgrade(troops,"mercenary_crossbowman","mercenary_sharpshooter")


#upgrade(troops,"mercenary_spearman","mercenary_pikeman")
#upgrade(troops,"mercenary_pikeman","mercenary_halberd")


upgrade(troops,"mercenary_axeman","mercenary_elite_axeman")

upgrade(troops,"mercenary_balkan_cav","polish_horse_3")
upgrade(troops, "hand_gunner", "cannon_man")

upgrade(troops,"manhunter","slave_driver")
upgrade(troops,"slave_driver","slave_hunter")
upgrade(troops,"slave_hunter","slaver_chief")
upgrade(troops,"slaver_chief","slaver_captain")



upgrade2(troops,"watchman","mercenary_swordsman","musket_man")
upgrade(troops,"mercenary_swordsman","hired_blade")
upgrade(troops,"hired_blade","champion_swordsman")

upgrade(troops,"musket_hunter","musket_man")
upgrade(troops,"musket_man","musket_line_infantry")
upgrade(troops,"musket_line_infantry","musket_line_infantry_2")
#upgrade(troops,"musket_line_infantry_2","musket_ranger")

upgrade2(troops,"caravan_guard","mercenary_horseman","merchant_cavalry_militia")
upgrade(troops,"mercenary_horseman","mercenary_cavalry")
upgrade(troops,"mercenary_cavalry","mercenary_lance")

upgrade2(troops,"swiss_swordman","swiss_pikeman","swiss_halberd")
upgrade(troops,"swiss_pikeman","swiss_pikeman_2")
upgrade(troops,"swiss_halberd","swiss_halberd_2")

#upgrade2(troops,"mercenary_horseman","mercenary_cavalry","musket_cavalry")
upgrade(troops,"musket_cavalry","pistol_cavalry")

#upgrade2(troops,"watchman","caravan_guard","musket_hunter")
#upgrade2(troops,"caravan_guard","mercenary_swordsman","mercenary_horseman")
#upgrade(troops,"mercenary_cavalry","mercenary_lance")
#upgrade(troops,"mercenary_sharpshooter","mercenary_sniper")

upgrade(troops,"refugee","follower_woman")

upgrade(troops,"peasant_woman","follower_woman")
upgrade(troops,"follower_woman","hunter_woman")
upgrade(troops,"hunter_woman","fighter_woman")
upgrade(troops,"fighter_woman","sword_sister")


upgrade2(troops,"france_town_recruit", "france_militia", "france_crossbow_1")
upgrade2(troops, "france_militia", "france_pikeman_1", "france_swordsman_1"),
upgrade(troops, "france_pikeman_1", "france_pikeman_2"),
upgrade(troops, "france_pikeman_2", "france_pikeman_3"),
upgrade(troops, "france_swordsman_1", "france_swordsman_2"),
upgrade(troops, "france_swordsman_2", "france_swordsman_3"),

upgrade(troops, "france_pikeman_3", "france_pikeman_4"),
upgrade(troops, "france_swordsman_3", "france_swordsman_4"),
upgrade(troops, "france_crossbow_3", "france_crossbow_4"),

upgrade(troops, "france_crossbow_1", "france_crossbow_2"),
upgrade(troops, "france_crossbow_2", "france_archer_3"),
upgrade(troops, "france_archer_3", "france_crossbow_3"),

upgrade2(troops,"teutonic_pilgrim", "teutonic_spearman", "monk")
upgrade2(troops, "teutonic_spearman", "teutonic_sword", "teutonic_horse_1"),
upgrade(troops, "teutonic_sword", "teutonic_dis_halbbruder"),
upgrade(troops, "teutonic_dis_halbbruder", "teutonic_dis_knight"),

upgrade(troops, "teutonic_horse_1", "teutonic_horse_2"),
upgrade(troops, "teutonic_horse_2", "teutonic_horse_3"),

upgrade(troops, "france_knight_1", "france_knight_2"),
upgrade(troops, "france_knight_2", "france_knight_3"),
upgrade(troops, "france_knight_3", "france_knight_4"),

#upgrade(troops, "hospitaller_knight", "hospitaller_knight_2"),

upgrade2(troops,"england_town_recruit", "england_militia", "england_longbowm_1")
upgrade2(troops, "england_militia", "england_billmen_1", "england_swordsman_1"),
upgrade(troops, "england_billmen_1", "england_billmen_2"),
upgrade(troops, "england_swordsman_1", "england_swordsman_2"),
upgrade(troops, "england_billmen_2", "england_billmen_3"),
upgrade(troops, "england_swordsman_2", "england_swordsman_3"),

upgrade(troops, "england_horse_1", "england_horse_2"),
upgrade(troops, "england_horse_2", "england_horse_3"),

upgrade2(troops, "england_longbowm_1", "england_longbowm_2", "england_horse_1"),
upgrade(troops, "england_longbowm_2", "england_longbowm_3"),
upgrade(troops, "england_longbowm_3", "england_longbowm_4"),

upgrade(troops, "england_knight_1", "england_knight_2"),
upgrade(troops, "england_knight_2", "england_knight_3"),
upgrade(troops, "england_knight_3", "england_knight_4"),

upgrade2(troops,"german_town_recruit", "german_militia", "german_crossbow_1")
upgrade2(troops, "german_militia", "german_pikeman_1", "german_twohander_1"),
upgrade(troops, "german_pikeman_1", "german_pikeman_2"),
upgrade(troops, "german_pikeman_2", "german_pikeman_3"),
upgrade(troops, "german_twohander_1", "german_twohander_2"),
upgrade(troops, "german_twohander_2", "german_twohander_3"),
   
upgrade(troops, "german_crossbow_1", "german_crossbow_2"),
upgrade(troops, "german_crossbow_2", "german_crossbow_3"),
upgrade(troops, "german_crossbow_3", "german_crossbow_4"),

upgrade2(troops, "iberian_town_militia", "iberian_town_footman_1", "iberian_dragoon_1"),
#upgrade2(troops, "iberian_town_footman_1", "iberian_town_footman_2", "human_magic_1"),
upgrade(troops, "iberian_town_footman_1", "iberian_town_footman_2"),
upgrade(troops, "iberian_town_footman_2", "iberian_town_footman_3"),

#upgrade2(troops, "iberian_dragoon_1", "iberian_knight_2", "german_reitern_1"),
upgrade(troops, "iberian_dragoon_1", "german_reitern_1"),
upgrade(troops, "german_reitern_1", "german_reitern_2"),

upgrade(troops, "iberian_knight_2", "iberian_knight_3"),

upgrade2(troops, "german_knight_1", "german_knight_2", "human_magic_1"),
upgrade(troops, "german_knight_2", "german_knight_3"),
upgrade(troops, "german_knight_3", "german_knight_4"),

upgrade2(troops,"se_tribesman", "se_pikeman_1", "se_skirmisher")
upgrade2(troops, "se_pikeman_1", "se_pikeman_2", "se_billman_1"),
upgrade(troops, "se_pikeman_2", "se_pikeman_3"),
upgrade(troops, "se_billman_1", "se_billman_2"),
upgrade(troops, "se_skirmisher", "se_musketeer_1"),
upgrade(troops, "se_musketeer_1", "se_musketeer_2"),

upgrade2(troops, "se_billman_2", "skeleton_warrior", "skeleton_spearman"),
upgrade(troops, "se_pikeman_3", "skeleton_halberd"),
upgrade(troops, "se_musketeer_2", "skeleton_archer"),
#upgrade2(troops,"skeleton", "se_pikeman_1", "se_skirmisher")
#upgrade(troops,"skeleton","skeleton_spearman")
#upgrade2(troops,"skeleton_spearman","skeleton_halberd","skeleton_archer")
#upgrade(troops,"skeleton_halberd","skeleton_warrior")
upgrade(troops,"skeleton_warrior","skeleton_lord")
upgrade(troops,"skeleton_spearman","skeleton_cav")


upgrade2(troops,"italian_town_recruit", "italian_town_militia", "italian_crossbow_1")
upgrade(troops, "italian_town_militia", "italian_town_footman_1"),
upgrade(troops, "italian_town_footman_1", "italian_town_footman_2"),
upgrade(troops, "italian_town_footman_2", "italian_town_footman_3"),

upgrade(troops, "italian_crossbow_1", "italian_crossbow_2"),
upgrade(troops, "italian_crossbow_2", "italian_crossbow_3"),
upgrade(troops, "italian_crossbow_3", "italian_crossbow_4"),

upgrade(troops, "italian_horse_1", "italian_horse_2"),
upgrade(troops, "italian_horse_2", "italian_horse_3"),
upgrade(troops, "italian_horse_3", "italian_horse_4"),

upgrade(troops, "mercenary_berserker", "god_choosen_berserker"),

upgrade(troops, "nord_recruit", "nord_footman")
upgrade2(troops, "nord_footman", "nord_warrior","nord_mounted_scout")
upgrade2(troops, "nord_warrior", "nord_veteran", "mercenary_berserker")
upgrade(troops, "nord_veteran", "nord_champion")
#upgrade(troops,"nord_champion","mercenary_elite_axeman")

upgrade(troops, "nord_valkyrie_1", "nord_valkyrie_2")
upgrade(troops, "nord_valkyrie_2", "nord_valkyrie_3")


upgrade2(troops, "nord_town_recruit", "nord_town_militia", "nord_skirmisher")
upgrade(troops, "nord_town_militia", "nord_swordsmen")
upgrade2(troops, "nord_swordsmen", "nord_axeman_1", "nord_halberd_1")
upgrade(troops, "nord_axeman_1", "nord_axeman_2")
upgrade(troops, "nord_halberd_1", "nord_halberd_2")

upgrade(troops, "nord_skirmisher", "nord_crossbow_1")
#upgrade2(troops, "nord_crossbow_1", "nord_crossbow_2", "nord_gunner")
upgrade(troops, "nord_crossbow_1", "nord_crossbow_2")
upgrade(troops, "nord_crossbow_2", "nord_gunner")


upgrade(troops, "nord_mounted_scout", "nord_mounted_scout_2"),
upgrade(troops, "nord_mounted_scout_2", "nord_raider"),

upgrade(troops, "nord_knight_1", "nord_knight_2")
upgrade(troops, "nord_knight_2", "nord_knight_3")


upgrade(troops, "draugr_1", "draugr_2")
upgrade(troops, "draugr_2", "draugr_3")
upgrade(troops, "draugr_3", "draugr_lord")

upgrade(troops, "polish_which_1", "polish_which_2")

upgrade2(troops,"balkan_vil_recruit", "polish_pikeman_1", "rus_cossack_1")

upgrade2(troops, "rus_cossack_1", "rus_cossack_2", "balkan_archer_2")
upgrade(troops, "rus_cossack_2", "rus_cossack_3")
upgrade(troops, "rus_cossack_3", "balkan_cav_3")

upgrade(troops, "polish_pikeman_1", "polish_pikeman_2"),
upgrade(troops, "polish_pikeman_2", "polish_pikeman_3"),

upgrade(troops,"balkan_archer_2", "balkan_archer_3")

upgrade2(troops,"polish_town_recruit", "balkan_footman_1", "polish_crossbow_1")

upgrade2(troops, "polish_crossbow_1", "polish_crossbow_2", "polish_horse_2")

upgrade(troops, "polish_crossbow_2", "polish_crossbow_3_1"),
upgrade(troops, "polish_crossbow_3_1", "polish_crossbow_3_2"),

upgrade(troops,"balkan_footman_1", "balkan_billman_2")
upgrade(troops,"balkan_billman_2", "balkan_billman_3")
upgrade(troops,"balkan_billman_3", "balkan_billman_4")

upgrade(troops, "polish_horse_1", "polish_horse_2")
upgrade(troops, "polish_horse_2", "polish_horse_3")
upgrade(troops, "polish_horse_3", "polish_horse_4")

upgrade(troops, "polish_knight_1", "polish_knight_2")
upgrade(troops,"rus_dvor_cavalry","rus_dvor_cavalry_2")
upgrade(troops, "polish_knight_2", "polish_knight_3")
#upgrade(troops, "polish_knight_3", "polish_knight_4"),

upgrade(troops,"rus_boyar","rus_boyar_2")
upgrade(troops,"rus_boyar_2","rus_palace_guard")

#upgrade(troops,"me_mercenary_swordsman_1","me_mercenary_swordsman_2")
upgrade2(troops,"me_mercenary_swordsman_2","chaos_warrior_1","sarranid_assasin")

upgrade(troops,"sarranid_assasin","sarranid_assasin_2")


upgrade2(troops, "ghazis_1", "ghazis_2","desert_bandit")
upgrade(troops, "ghazis_2", "me_mercenary_swordsman_1")
upgrade2(troops, "me_mercenary_swordsman_1", "turk_archer_3","chaos_warrior_1")

upgrade2(troops,"desert_bandit","saracen_cav_1","turk_cav_2")

upgrade2(troops, "marinid_camel_1", "marinid_camel_2","bedouin_camel_gunnner")
upgrade(troops, "marinid_camel_2", "marinid_camel_3_1")
upgrade(troops, "marinid_camel_3_1", "marinid_camel_4_1")

upgrade(troops,"bedouin_camel_gunnner","marinid_camel_3_2")
upgrade(troops, "marinid_camel_3_2", "marinid_camel_4_2")



upgrade(troops,"saracen_cav_1","saracen_cav_2")
upgrade(troops,"saracen_cav_2","mamluke_horseman")

upgrade(troops, "naffatun", "me_hand_gunner")

upgrade2(troops, "turk_village_rabble", "turk_azap", "turk_cav_1")
upgrade2(troops, "turk_azap", "turk_spearman", "turk_archer_1")

upgrade2(troops, "turk_spearman", "me_mercenary_swordsman_2", "turk_footman")

upgrade(troops, "turk_footman", "janissary_infantry_1")


upgrade(troops, "turk_archer_1", "turk_archer_2")
#upgrade(troops, "turk_archer_2", "turk_archer_3")

upgrade(troops, "turk_archer_2", "janissary_musketeer_1")

upgrade(troops, "turk_cav_1", "turk_cav_2")
upgrade(troops, "turk_cav_2", "turk_cav_3")

upgrade(troops,"turk_cav_3","mamluke_horseman_2")

upgrade(troops, "turk_sipahi", "turk_sipahi_lance")
upgrade(troops, "turk_sipahi_lance", "turk_roy_sipahi")

upgrade(troops, "mamluke_horseman", "mamluke_horseman_2")

upgrade2(troops, "mamluke_recruit", "janissary_archer", "janissary_retainer")

upgrade2(troops, "janissary_retainer", "chaos_warrior_1", "mamluke_horseman_2")
upgrade(troops, "chaos_warrior_1", "chaos_warrior_2")
upgrade(troops, "janissary_infantry_1", "janissary_infantry_2")
upgrade(troops, "mamluke_horseman_2", "mamluke_horseman_3")

upgrade2(troops, "janissary_archer", "janissary_infantry_1", "janissary_musketeer_1")
upgrade(troops, "janissary_musketeer_1", "janissary_musketeer_2")



upgrade2(troops,"khergit_tribesman","khergit_skirmisher","khergit_hunter")
#upgrade(troops,"khergit_skirmisher","khergit_horse_archer")
#upgrade(troops,"khergit_horse_archer","khergit_nomad_horseman")
#upgrade(troops,"khergit_tribesman","khergit_foot_archer")

upgrade2(troops,"khergit_hunter","khergit_footman","khergit_foot_archer")
upgrade(troops,"khergit_footman","khergit_dismounted_lancer")
upgrade(troops,"khergit_dismounted_lancer","khergit_heavy_infantry")
upgrade(troops,"khergit_foot_archer","khergit_heavy_archer")
upgrade(troops,"khergit_heavy_archer","khergit_dis_guard")

upgrade2(troops,"khergit_skirmisher","khergit_horseman","khergit_horse_archer")
upgrade(troops,"khergit_horseman","khergit_lancer")
upgrade(troops,"khergit_horse_archer","khergit_veteran_horse_archer")
upgrade(troops,"khergit_lancer","khergit_heavy")
upgrade(troops,"khergit_veteran_horse_archer","khergit_elite_horse_archer")

upgrade(troops,"khergit_guard","khergit_general")
upgrade(troops,"khergit_general","nazgul")


upgrade(troops,"looter","bandit")
upgrade2(troops,"bandit","brigand","mountain_bandit")
upgrade(troops,"brigand","raider")
upgrade(troops,"mountain_bandit","mountain_bandit_leader")


upgrade(troops,"forest_bandit","forest_brigand")
upgrade(troops,"forest_brigand","forest_hunter")


upgrade2(troops,"taiga_bandit","rus_cossack","taiga_brigand")
#upgrade(troops,"taiga_bandit","taiga_brigand")
upgrade(troops,"taiga_brigand","taiga_bandit_leader")

upgrade2(troops,"steppe_bandit","steppe_horseman_1","steppe_horse_archer_1")
upgrade2(troops,"steppe_tribesman","steppe_horseman_1","steppe_horse_archer_1")
upgrade(troops,"steppe_horseman_1","steppe_horseman_2")
upgrade(troops,"steppe_horse_archer_1","steppe_horse_archer_2")

upgrade(troops,"steppe_horseman_2","black_khergit_lancer")
upgrade(troops,"steppe_horse_archer_2","black_khergit_guard")

upgrade2(troops,"black_khergit_horseman","black_khergit_lancer","black_khergit_guard")
#upgrade(troops,"black_khergit_guard","black_khergit_raidmaster")


#upgrade2(troops,"polish_town_recruit", "polish_horse_1", "polish_crossbow_1")
#upgrade2(troops, "polish_crossbow_1", "polish_crossbow_2", "polish_pikeman_1")
#upgrade(troops, "polish_crossbow_2", "polish_crossbow_3_1"),
#upgrade(troops, "polish_crossbow_3_1", "polish_crossbow_3_2"),
#upgrade(troops, "polish_pikeman_1", "polish_pikeman_2"),
#upgrade(troops, "polish_horse_1", "polish_horse_2")
#upgrade(troops, "polish_horse_2", "polish_horse_3")
#upgrade(troops, "polish_horse_3", "polish_horse_4")
#upgrade(troops, "polish_knight_1", "polish_knight_2")
#upgrade(troops, "polish_knight_2", "polish_knight_3")
#upgrade(troops, "polish_knight_3", "polish_knight_4"),

#upgrade2(troops,"rus_town_recruit", "rus_musketeer_1", "rus_cossack_1")

#upgrade2(troops, "rus_musketeer_1", "rus_musketeer_2", "rus_pikeman_2")
#upgrade2(troops, "rus_musketeer_2", "rus_musketeer_3", "rus_musketeer_3_2"),

#upgrade(troops, "rus_pikeman_2", "rus_pikeman_3"),

#upgrade(troops, "rus_cossack_1", "rus_cossack_2")
#upgrade(troops, "rus_cossack_2", "rus_cossack_3")

#upgrade2(troops, "rus_noble", "rus_boyar", "rus_dvor_cavalry")

#upgrade(troops,"rus_cossack","rus_dvor_cavalry")
#upgrade(troops,"rus_dvor_cavalry","rus_dvor_cavalry_2")
#upgrade(troops,"rus_boyar","rus_boyar_2")
#upgrade(troops,"rus_boyar_2","rus_palace_guard")

#upgrade2(troops,"balkan_vil_recruit", "balkan_footman_1", "balkan_cav_1")
#upgrade(troops,"balkan_cav_1", "balkan_cav_2")
#upgrade(troops,"balkan_cav_2", "balkan_cav_3")

#upgrade2(troops,"balkan_footman_1", "balkan_billman_2", "balkan_archer_2")
#upgrade(troops,"balkan_billman_2", "balkan_billman_3")
#upgrade(troops,"balkan_archer_2", "balkan_archer_3")

#upgrade2(troops,"hungary_town_recruit", "hungary_horseman_1", "hungary_crossbow_1")
#upgrade2(troops,"hungary_horseman_1", "hungary_horseman_2", "hungary_town_pikeman_2")
#upgrade(troops,"hungary_horseman_2", "hungary_horseman_3")
#upgrade(troops,"hungary_town_pikeman_2", "hungary_town_pikeman_3")

#upgrade2(troops,"hungary_crossbow_1", "hungary_crossbow_2_1","hungary_crossbow_2_2")
#upgrade(troops,"hungary_crossbow_2_2", "hungary_crossbow_3_2")

#upgrade(troops, "hungary_knight_1", "hungary_knight_2")
#upgrade(troops, "hungary_knight_2", "hungary_knight_3")

#new bandit
#upgrade(troops,"forest_bandit","forest_brigand")
#upgrade2(troops,"steppe_bandit","black_khergit_horseman","steppe_brigand")
#upgrade2(troops,"sea_raider","sea_raider_viking","sea_raider_veteran")
#upgrade(troops,"desert_bandit","desert_brigand")

#new bandit ended


#upgrade(troops,"sea_raider_viking","norman_cavalry")
#upgrade(troops,"camel_cavalry","camel_mamluke")



upgrade2(troops,"scottish_jav","scottish_axeman","scottish_pikeman")
upgrade2(troops,"scottish_axeman","lizard_axeman_1","lizard_rider_1")
upgrade(troops,"lizard_axeman_1","lizard_axeman_2")
upgrade(troops,"lizard_rider_1","lizard_rider_2")

upgrade(troops,"scottish_pikeman","scottish_pikeman_2")
upgrade(troops,"scottish_pikeman_2","scottish_pikeman_3")

upgrade2(troops,"welsh_longbowm_1","welsh_longbowm_2","welsh_spearman_1")
upgrade(troops,"welsh_longbowm_2","welsh_longbowm_3")
upgrade(troops,"welsh_spearman_1","welsh_spearman_2")

#upgrade2(troops,"dark_hunter","dark_sniper","dark_knight")

upgrade(troops,"ninjia","ninjia_adv")
## CC

upgrade2(troops,"goblin","goblin_footman","goblin_skirmisher")

upgrade2(troops,"goblin_footman","goblin_infantry","goblin_horseman")
upgrade(troops,"goblin_skirmisher","goblin_crossbowman")

upgrade(troops,"goblin_infantry","goblin_guard")
upgrade(troops,"goblin_horseman","goblin_knight")

upgrade2(troops,"ogre_young","ogre","ogre_gunner")
upgrade(troops,"ogre","ogre_war")
upgrade(troops,"ogre_gunner","ogre_gunner2")

upgrade2(troops,"orc","orc_boy","arrer_youngun")
upgrade(troops,"orc_boy","orc_warrior")
upgrade2(troops,"orc_warrior","orc_big","orc_boar_boy")
upgrade(troops,"orc_big","orc_blackorc")
upgrade(troops,"orc_blackorc","orc_veterun_blackorc")
upgrade(troops,"orc_veterun_blackorc","orc_blackorc_boss")
upgrade(troops,"orc_boar_boy","orc_veteran_boar")
upgrade(troops,"orc_veteran_boar","orc_boar_big")
upgrade(troops,"arrer_youngun","orc_arrer_boy")
upgrade(troops,"orc_arrer_boy","orc_veterun_arrer")
upgrade(troops,"harpy_1","harpy_2")


upgrade2(troops,"woodelf_recruit","woodelf_watchman","woodelf_scout")


upgrade(troops,"woodelf_druid_1","woodelf_druid_2")

upgrade(troops,"woodelf_scout","woodelf_hunter")
upgrade(troops,"woodelf_hunter","woodelf_m_hunter")
upgrade(troops,"woodelf_m_hunter","woodelf_stinger")
upgrade(troops,"woodelf_stinger","woodelf_sharpshooter")

upgrade(troops,"woodelf_watchman","woodelf_spearman")
upgrade(troops,"woodelf_spearman","woodelf_swordman")
upgrade(troops,"woodelf_swordman","woodelf_sworddancer")

upgrade2(troops,"grandelf_recruit","grandelf_infantry","grandelf_warden")

upgrade(troops,"grandelf_warden","grandelf_marksman")
upgrade(troops,"grandelf_marksman","grandelf_arcane_archer")
upgrade(troops,"grandelf_arcane_archer","grandelf_arcane_guard")

upgrade(troops,"grandelf_mage_1","grandelf_mage_2")

upgrade(troops,"grandelf_infantry","grandelf_swordman")
upgrade(troops,"grandelf_swordman","grandelf_swordman_adv")
upgrade2(troops,"grandelf_swordman_adv","grandelf_guard","grandelf_cavalry")

upgrade(troops,"dwarf_miner","dwarf_warrior")
upgrade2(troops,"dwarf_warrior","dwarf_veteran","dwarf_musketeer_1")
upgrade2(troops,"dwarf_veteran","dwarf_ironbreaker","dwarf_berserker")

#upgrade2(troops,"dwarf_ironbreaker","dwarf_guard_1","dwarf_guard_2")
upgrade(troops,"dwarf_ironbreaker","dwarf_guard_1")
upgrade(troops,"dwarf_berserker","dwarf_guard_2")

upgrade(troops,"dwarf_musketeer_1", "dwarf_musketeer_2_1")
#upgrade2(troops,"dwarf_musketeer_1", "dwarf_musketeer_2_1", "dwarf_musketeer_2_2")
upgrade(troops,"dwarf_musketeer_2_1","dwarf_musketeer_3")

upgrade2(troops,"giant_1","giant_1_2","giant_1_3")
upgrade(troops,"giant_1_2","giant_2")
upgrade(troops,"giant_1_3","giant_3")

upgrade(troops,"mummy_1","mummy_2")
#upgrade(troops,"mummy_2","mummy_3")

upgrade(troops,"mummy_2_1","mummy_4")
upgrade(troops,"mummy_2_2","mummy_2_3")


#upgrade(troops,"undead_magic_1","undead_magic_2")

upgrade2(troops,"vampire_assassin","undead_magic_2","vampire_1")
upgrade(troops,"undead_magic_2","lich_1")
upgrade(troops,"lich_1","lich_2")
upgrade2(troops,"vampire_1","vampire_2","undead_horse_1")
upgrade(troops,"vampire_2","vampire_3")
upgrade(troops,"vampire_3","vampire_4")

upgrade(troops,"undead_horse_1","undead_horse_2")
upgrade(troops,"undead_horse_2","undead_horse_3")

upgrade(troops,"ghost","wight")

upgrade(troops,"wraith","death")
upgrade(troops,"zombie_1","zombie_2")
upgrade2(troops,"zombie_2","zombie_3","zombie_4")
upgrade(troops,"zombie_4","dullahan")
upgrade(troops,"zombie_3","zombie_5")
#upgrade2(troops,"zombie_3","zombie_5","zombie_6")

upgrade(troops,"rat_1","rat_2")
upgrade(troops,"rat_2","rat_3")
upgrade(troops,"rat_3","rat_4")
#upgrade2(troops,"rat_3","rat_4","")
upgrade2(troops,"rat_4","rat_5_1","rat_5_2")
#upgrade(troops,"rat_assassin_1","rat_assassin_2")

upgrade(troops,"minotaur_1","minotaur_2")
upgrade(troops,"minotaur_2","minotaur_3")

upgrade(troops,"red_dragon","black_dragon")
upgrade(troops,"fire_dragon","lava_dragon")

upgrade(troops,"bone_dragon","ghost_dragon")


upgrade2(troops,"drowelf_recruit","drowelf_footman","drowelf_assassin_1")
upgrade2(troops,"drowelf_footman","drowelf_infantry_1","drowelf_raider_1")
upgrade(troops,"drowelf_infantry_1","drowelf_infantry_2")
upgrade(troops,"drowelf_assassin_1","drowelf_assassin_2")
upgrade(troops,"drowelf_assassin_2","drowelf_assassin_3")
upgrade(troops,"drowelf_raider_1","drowelf_raider_2")
upgrade(troops,"drowelf_which_1","drowelf_which_2")

upgrade(troops,"werewolf_1","werewolf_1_a")
#upgrade(troops,"werewolf_2","werewolf_2_a")

upgrade(troops, "titan_0", "titan_1")
upgrade(troops, "titan_1", "titan_2"),

upgrade(troops, "human_magic_1", "human_magic_2")
upgrade(troops, "human_magic_2", "human_magic_3"),

upgrade2(troops, "demon_human_1", "demon_human_2","demon_magic_1"),
upgrade(troops, "demon_magic_1", "demon_magic_2"),
upgrade(troops, "demon_magic_2", "demon_magic_3"),
upgrade(troops, "demon_human_2", "demon_human_3"),
upgrade(troops, "demon_human_3", "demon_human_4"),
#upgrade(troops, "demon_human_4", "demon_human_5_1"),
#pgrade2(troops, "demon_human_4", "demon_human_5_1","demon_human_5_2"),
upgrade(troops, "demon_4_2", "demon_4_3"),
upgrade2(troops, "demon_1", "demon_1_3","demon_1_2"),
upgrade(troops, "demon_1_4", "demon_4"),


upgrade(troops, "slaanesh_witch_1", "slaanesh_witch_2"),
upgrade(troops, "slaanesh_witch_2", "demon_human_5_2"),

upgrade(troops, "slaanesh_chosen", "daemon_prince_slaanesh"),
upgrade(troops, "demon_human_5_1", "demon_6"),
upgrade(troops, "demon_7", "demon_5"),
upgrade2(troops, "demon_9", "daemon_prince_nurgle", "great_demon_nurgle"),
upgrade(troops, "angle", "archangle"),
upgrade(troops, "medusa_1", "medusa_2"),

#upgrade2(troops,"skeleton","skeleton_warrior","skeleton_archer")
#upgrade2(troops,"skeleton_warrior","skeleton_halberd","skeleton_spearman")



upgrade(troops, "monk", "clerics"),
upgrade(troops, "clerics", "priest"),
#upgrade(troops, "war_clerics_1", "war_clerics_2"),
upgrade(troops, "priest", "healer"),


upgrade2(troops, "sissofbattle", "sissofbattle_c", "sissofbattle_s"),
upgrade(troops, "sissofbattle_c", "sissofbattle_r"),

# Custom Troops Begin


upgrade(troops,"custom_recruit","custom_militia")
upgrade(troops,"custom_militia","custom_sount")

#upgrade(troops,"custom_militia","custom_footman")

upgrade(troops,"custom_footman","custom_infantry")
upgrade(troops,"custom_infantry","custom_sergeant")

#upgrade2(troops,"custom_sount","custom_horseman","custom_musket")

upgrade(troops,"custom_horseman","custom_cavalry")
upgrade(troops,"custom_cavalry","custom_cavalry_2")

upgrade(troops,"custom_musket","custom_trained_musket")
upgrade(troops,"custom_trained_musket","custom_veteran_musket")

#upgrade(troops,"custom_veteran_musket","custom_cannon_man")

upgrade(troops,"custom_knight_1","custom_knight_2")
upgrade(troops,"custom_knight_2","custom_knight_3")

# Custom Troops End

upgrade(troops,"air_elemental","air_elemental_2")
upgrade(troops,"air_elemental_2","air_elemental_3")

upgrade(troops,"water_elemental","water_elemental_2")
upgrade(troops,"water_elemental_2","water_elemental_3")

upgrade(troops,"fire_elemental","fire_elemental_2")
upgrade(troops,"fire_elemental_2","fire_elemental_3")

upgrade(troops,"earth_elemental","earth_elemental_2")
upgrade(troops,"earth_elemental_2","earth_elemental_3")



# modmerger_start version=201 type=2
try:
    component_name = "troops"
    var_set = { "troops" : troops }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
