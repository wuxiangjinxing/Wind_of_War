# -*- coding: UTF-8 -*-
from header_common import *
from header_skills import *

####################################################################################################################
#  Each skill contains the following fields:
#  1) Skill id (string): used for referencing skills in other files. The prefix skl_ is automatically added before each skill-id .
#  2) Skill name (string).
#  3) Skill flags (int). See header_skills.py for a list of available flags
#  4) Maximum level of the skill (int).
#  5) Skill description (string): used in character window for explaining the skills.
# 
####################################################################################################################

#Hardcoded skills are {names (indexes, beginning with 0)}:
# Trade (1)
# Leadership (2)
# Prisoner Management (3)
# First Aid (9)
# Surgery (10)
# Wound Treatment (11)
# Inventory Management (12)
# Spotting (13)
# Pathfinding (14)
# Tactics (15)
# Tracking (16)
# Trainer (17)
# Engineer (18)
# Horse Archery (24)
# Riding (25)
# Athletics (26)
# Shield (27)
# Weapon Master (28)
# Power Draw (34)
# Power Throw (35)
# Power Strike (36)
# Ironflesh (37)
#
# The effects of these skills can only be removed if the skill is disabled with sf_inactive flag.
# If you want to add a new skill, use the reserved skills or use non-hardcoded skills.

skills = [
  ("trade","Trade",sf_base_att_cha|sf_effects_party,15,"Every level of this skill reduces your trade penalty by 5%%. (Party skill)  Max level: 10"),
  ("leadership","Leadership",sf_base_att_cha,15,"Every point increases maximum number of troops you can command by 10, increases your party morale and reduces troop wages by 5%%. (Leader skill)  Max level: 15"),
  ("prisoner_management", "Prisoner Management",sf_base_att_cha,15,"Every level of this skill increases maximum number of prisoners by 10. (Leader skill)  Max level: 15"), 
  ("magic_power","Magic_Power",sf_base_att_cha,15,"This_skill_represents_your_prowess_when_attacking_with_magic."), 
  ("magic_defence","Magic_Defense",sf_base_att_cha,10,"This_skill_represents_your_resistance_to_magical_attacks."), 
  ("paragon_knight","paragon_knight",sf_base_att_cha,10,"This is a reserved skill."), 
  ("persuasion","Persuasion", sf_base_att_cha,10, "This skill helps you make other people accept your point of view. (Personal skill)  Max level: 10"),
  ("engineer","Engineer",sf_base_att_int|sf_effects_party,10,"This skill allows you to construct siege equipment and fief improvements more efficiently. (Party skill)  Max level: 10"),
  ("undead_master","undead_master",sf_base_att_int,10,"This is a reserved skill."), 
  ("surgery","Surgery",sf_base_att_int|sf_effects_party|sf_inactive,10,"Each point to this skill gives a 5.5%% chance that a mortally struck party member will be wounded rather than killed. (Party skill)  Max level: 10"), 
  ("first_aid", "First Aid",sf_base_att_int|sf_effects_party,10,"Heroes regain 5%% per skill level of hit-points lost during mission. (Party skill)  Max level: 10"), 
  ("wound_treatment","Wound Treatment",sf_base_att_int|sf_effects_party,10,"Party healing speed is increased by 20%% per level of this skill. (Party skill)  Max level: 10"), 
  ("inventory_management","Inventory Management",sf_base_att_int,10,"Increases inventory capacity by +6 per skill level. (Leader skill)  Max level: 10"), 
  ("spotting","Spotting",sf_base_att_int|sf_effects_party,15,"Party seeing range is increased by 10%% per skill level. (Party skill)  Max level: 15"),
  ("pathfinding","Path-finding",sf_base_att_int|sf_effects_party,15,"Party map speed is increased by 6%% per skill level. (Party skill)  Max level: 15"), 
  ("tactics","Tactics",sf_base_att_int|sf_effects_party,15,"Every two levels of this skill increases starting battle advantage by 1. (Party skill)  Max level: 15"),
  ("tracking","Tracking",sf_base_att_int|sf_effects_party,15,"Tracks become more informative. (Party skill)  Max level: 15"),
  ("trainer","Trainer",sf_base_att_int,10,"Every day, each hero with this skill adds some experience to every other member of the party whose level is lower than his/hers. Experience gained goes as: {0,4,10,16,23,30,38,46,55,65,80}. (Personal skill)  Max level: 10"),
  ("necromancy","Necromancy",sf_base_att_int,10,"each skill can Improve Summon creatures Control time 1 min. After the battle, skill can Collecting souls of the dead, it Can be used to create undead, summon demons, or create medals"),   
  ("magic_skill","magic_skill",sf_base_att_int,15,"Each point to this skill increases ranged damage (excludes throwing and bow weapons) by 8%%. (Personal skill)  Max level: 15"), 
  ("archer_comman","archer_comman",sf_base_att_int,10,"This is a reserved skill."), 
  ("precise_shot","Precise Shot",sf_base_att_int,15,"Each point to this skill increases ranged damage (excludes throwing and bow weapons) by 8%%. (Personal skill)  Max level: 15"), 
  ("looting","Looting",sf_base_att_agi|sf_effects_party,15,"This skill increases the amount of loot obtained by 10%% per skill level. (Party skill)  Max level: 15"), 
  ("horse_archery","Horse Archery",sf_base_att_agi,10,"Reduces damage and accuracy penalties for archery and throwing from horseback. (Personal skill)  Max level: 10"),
  ("riding","Riding",sf_base_att_agi,10,"Enables you to ride horses of higher difficulty levels and increases your riding speed and manuever. (Personal skill)  Max level: 10"),
  ("athletics","Athletics",sf_base_att_agi|sf_inactive,10,"Improves your running speed. (Personal skill)  Max level: 10"),
  ("shield","Shield",sf_base_att_str,10,"Reduces damage to shields (by 8%% per skill level) and improves shield speed and coverage. (Personal skill)  Max level: 10"),
  ("weapon_master","Weapon Master",sf_base_att_agi,10,"Makes it easier to learn weapon proficiencies and increases the proficiency limits. Limits go as: 60, 100, 140, 180, 220, 260, 300, 340, 380, 420. (Personal skill)  Max level: 10"),
  ("stealth","Stealth",sf_base_att_agi,15,"This skill allows you to Causes_extra_damage.with_one_handed, crossbow ,pistol, thrown weapons"), 
  ("offense","Offense",sf_base_att_agi,15,"Each point to this skill increases the soldiers' damage by 5%%. (Leader skill) Max level: 15"), 
  ("reserved_11","Reserved Skill 11",sf_base_att_agi|sf_inactive,10,"This is a reserved skill."), 
  ("reserved_12","Reserved Skill 12",sf_base_att_agi|sf_inactive,10,"This is a reserved skill."), 
  ("reserved_13","Reserved Skill 13",sf_base_att_agi|sf_inactive,10,"This is a reserved skill."), 
  ("power_draw","Power Draw",sf_base_att_str,15,"Lets character use more powerful bows. Each point to this skill (up to four plus power-draw requirement of the bow) increases bow damage by 14%%. (Personal skill)  Max level: 12"),
  ("power_strike","Power Strike",sf_base_att_str,15,"Each point to this skill increases melee damage by 8%%. (Personal skill)  Max level: 15"),
  ("power_throw","Power Throw",sf_base_att_str|sf_inactive,15,"Each point to this skill increases throwing damage by 10%%. (Personal skill)  Max level: 15"),
  ("physique","Physique",sf_base_att_str,15,"Each point to this skill increases hit points. (Personal skill) Max level: 15"), 
  ("ironflesh","Ironflesh",sf_base_att_str,15,"Each point to this skill increases hit points, and improves your running speed greatly (by 3%% per skill level). (Personal skill) Max level: 15"), 
  ("tenacity","Armorer",sf_base_att_str,15,"Each point to this skill reduces damage to the soldiers from enemy by 3%%. (Leader skill) Max level: 15"), 
  #("reserved_15","Reserved Skill 15",sf_base_att_str|sf_inactive,10,"This is a reserved skill."), 
  ("reserved_16","Reserved Skill 16",sf_base_att_str|sf_inactive,10,"This is a reserved skill."), 
  ("reserved_17","Reserved Skill 17",sf_base_att_str|sf_inactive,10,"This is a reserved skill."), 
  ("reserved_18","Reserved Skill 18",sf_base_att_str|sf_inactive,10,"This is a reserved skill."), 
]
# modmerger_start version=201 type=2
try:
    component_name = "skills"
    var_set = { "skills" : skills }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
