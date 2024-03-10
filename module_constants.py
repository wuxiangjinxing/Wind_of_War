from ID_items import *
from ID_quests import *
from ID_factions import *
from header_triggers import *
##############################################################
# These constants are used in various files.
# If you need to define a value that will be used in those files,
# just define it here rather than copying it across each file, so
# that it will be easy to change it if you need to.
##############################################################
current_version = mod_version = 7526
 
lock_item = 100
 
lair_recruit_time_1 = 72
lair_recruit_time_2 = 168
lair_recruit_time_3 = 336
lair_recruit_time_4 = 672
battle_ratio_multiple = 200
########################################################
##  ITEM SLOTS             #############################
########################################################

slot_item_is_checked               = 0
slot_item_food_bonus               = 1
slot_item_book_reading_progress    = 2
slot_item_book_read                = 3
slot_item_intelligence_requirement = 4

slot_item_amount_available         = 7

slot_item_urban_demand             = 11 #consumer demand for a good in town, measured in abstract units. The more essential the item (ie, like grain) the higher the price
slot_item_rural_demand             = 12 #consumer demand in villages, measured in abstract units
slot_item_desert_demand            = 13 #consumer demand in villages, measured in abstract units

slot_item_production_slot          = 14 
slot_item_production_string        = 15 

slot_item_tied_to_good_price       = 20 #ie, weapons and metal armor to tools, padded to cloth, leather to leatherwork, etc

slot_item_num_positions            = 22
slot_item_positions_begin          = 23 #reserve around 5 slots after this


slot_item_multiplayer_faction_price_multipliers_begin = 30 #reserve around 10 slots after this

slot_item_primary_raw_material    		= 50
slot_item_is_raw_material_only_for      = 51
slot_item_input_number                  = 52 #ie, how many items of inputs consumed per run
slot_item_base_price                    = 53 #taken from module_items
#slot_item_production_site			    = 54 #a string replaced with function - Armagan
slot_item_output_per_run                = 55 #number of items produced per run
slot_item_overhead_per_run              = 56 #labor and overhead per run
slot_item_secondary_raw_material        = 57 #in this case, the amount used is only one
slot_item_enterprise_building_cost      = 58 #enterprise building cost


slot_item_multiplayer_item_class   = 60 #temporary, can be moved to higher values
slot_item_multiplayer_availability_linked_list_begin = 61 #temporary, can be moved to higher values
slot_item_temp_slot  = slot_item_multiplayer_item_class

########################################################
##  AGENT SLOTS            #############################
########################################################

slot_agent_target_entry_point     = 0
slot_agent_target_x_pos           = 1
slot_agent_target_y_pos           = 2
slot_agent_is_alive_before_retreat= 3
slot_agent_is_in_scripted_mode    = 4
slot_agent_is_not_reinforcement   = 5
slot_agent_tournament_point       = 6
slot_agent_arena_team_set         = 7
slot_agent_spawn_entry_point      = 8
slot_agent_target_prop_instance   = 9
slot_agent_map_overlay_id         = 10
slot_agent_target_entry_point     = 11
slot_agent_initial_ally_power     = 12
slot_agent_initial_enemy_power    = 13
slot_agent_enemy_threat           = 14
slot_agent_is_running_away        = 15
slot_agent_courage_score          = 16
slot_agent_is_respawn_as_bot      = 17
slot_agent_cur_animation          = 18
slot_agent_next_action_time       = 19
slot_agent_state                  = 20
slot_agent_in_duel_with           = 21
slot_agent_duel_start_time        = 22

slot_agent_walker_occupation      = 25
  
slot_player_charge_time  = slot_agent_next_action_time
slot_player_before_action  = slot_agent_cur_animation   
slot_agent_already_begg  = slot_agent_arena_team_set   


# agent slots
slot_agent_refill_ammo_times      = 26

slot_agent_player_target          = 27

slot_agent_is_skirmish            = 28
slot_agent_shoot_time_ticker      = 29

slot_agent_shield_bash_timer      = 30
slot_agent_hp_bar_overlay_id      = 31
slot_agent_hp_bar_bg_overlay_id   = 32
slot_agent_weapon_master_level    = 33
slot_agent_stealth_level          = 34  

slot_agent_athletics_level        = 21
slot_agent_riding_level           = 22

slot_agent_flamberge_attack_chance               = 36
slot_agent_extra_hp                              = 37
slot_agent_extra_shield                          = 74
slot_agent_backup_hp                             = 75

slot_agent_spawned                               = 38

slot_agent_two_handed_wp           = 39
slot_agent_one_handed_wp           = 40
slot_agent_spear_wp                = 41
slot_agent_pike_wp                 = 42
slot_agent_lance_wp                = 43
slot_agent_footbow                 = 44
slot_agent_horsebow                = 45
slot_agent_shield                  = 46
slot_agent_spear         = slot_agent_spear_wp

slot_agent_new_division  = 48
slot_agent_horse         = 49
slot_agent_horse_rider   = 50
slot_agent_volley_fire   = 51
slot_agent_spearwall     = 52
slot_agent_player_braced = 53

#Agent Slots
slot_agent_lance         = slot_agent_lance_wp
slot_agent_alt_div_check = 56

slot_agent_stamina                   = 47
slot_agent_horse_stamina          = 54
slot_agent_horse_is_charging      = 55

slot_agent_mana          = slot_agent_horse_stamina

slot_agent_cur_magic          = slot_agent_in_duel_with
slot_agent_max_mana               = slot_agent_duel_start_time
slot_agent_special_ability_extra_counter        = 23
slot_agent_special_ability_extra_cooldown       = 24
slot_agent_special_ability_cooldown              = 59
slot_agent_special_ability_counter               = 60
slot_agent_has_been_special_ability              = 61
slot_agent_special_ability_passiv_counter        = 62
slot_agent_special_ability_passiv_cooldown       = 63
slot_agent_special_damage_type                   = 64
slot_agent_special_damage_time                   = 65
slot_agent_special_damage_power                  = 66
slot_agent_spell_1_cooldown       = 79
slot_agent_spell_2_cooldown       = 80
slot_agent_spell_3_cooldown       = 81
slot_agent_spell_4_cooldown       = 82
slot_agent_spell_cast_time        = 83

slot_agent_special_ability_affect_type           = 57
slot_agent_special_ability_affect_time           = 58

slot_agent_buff_affect_type           = 87
slot_agent_buff_affect_time           = 88

slot_agent_debuff_affect_type           = 89
slot_agent_debuff_affect_time           = 90

slot_agent_forcefield_id                = 91
slot_agent_forcefield_instance_no       = 92

slot_agent_temp_slot       = 84

slot_agent_vc_wounded       = 85
slot_agent_vortice          = 86

slot_agent_charm_time                  = 69
slot_agent_old_team_set                = 70

slot_agent_paragon_knight_level        = 71
slot_agent_tenacity_level           = 72
slot_agent_is_fly           = 73
slot_agent_resilience           = 93

slot_agent_archer_state              = 76
slot_next_shoot_time                 = 77
slot_agent_next_release_time         = 78

burn  = 1
wound  = 2
poison  = 3 
severe_burn  = 4
ice  = 5 
freeze  = 6
holy_fire = 7
thunder = 8
curse = 9
power_jump = 10 
power_poison = 11 
marked_for_death = 12 
blinding = 13 


########################################################
##  FACTION SLOTS          #############################
########################################################
slot_faction_ai_state                   = 4
slot_faction_ai_object                  = 5
slot_faction_ai_rationale               = 6 #Currently unused, can be linked to strings generated from decision checklists

slot_faction_inactive_days              = 7

slot_faction_marshall                   = 8
slot_faction_ai_offensive_max_followers = 9

slot_faction_culture                    = 10
slot_faction_leader                     = 11

slot_faction_temp_slot                  = 12

##slot_faction_vassal_of            = 11
slot_faction_banner                     = 15

slot_faction_number_of_parties    = 20
slot_faction_state                = 21

slot_faction_adjective            = 22


slot_faction_player_alarm         		= 30
slot_faction_last_mercenary_offer_time 	= 31
slot_faction_recognized_player    		= 32

#overriding troop info for factions in quick start mode.
slot_faction_quick_battle_tier_1_infantry      = 41
slot_faction_quick_battle_tier_2_infantry      = 42
slot_faction_quick_battle_tier_3_infantry      = 43
slot_faction_quick_battle_tier_4_infantry      = 44
slot_faction_quick_battle_tier_5_infantry      = 45
slot_faction_quick_battle_tier_6_infantry      = 46

slot_faction_quick_battle_tier_1_archer        = 47
slot_faction_quick_battle_tier_2_archer        = 48
slot_faction_quick_battle_tier_3_archer        = 49
slot_faction_quick_battle_tier_4_archer        = 50
slot_faction_quick_battle_tier_5_archer        = 51
slot_faction_quick_battle_tier_6_archer        = 52

slot_faction_quick_battle_tier_1_cavalry       = 53
slot_faction_quick_battle_tier_2_cavalry       = 54
slot_faction_quick_battle_tier_3_cavalry       = 55
slot_faction_quick_battle_tier_4_cavalry       = 56
slot_faction_quick_battle_tier_5_cavalry       = 57
slot_faction_quick_battle_tier_6_cavalry       = 58

slot_faction_tier_1_troop         = 41
slot_faction_tier_2_troop         = 42
slot_faction_tier_3_troop         = 43
slot_faction_tier_4_troop         = 44
slot_faction_tier_5_troop         = 45
slot_faction_tier_6_troop         = 46
slot_faction_tier_1_castle_troop  = 46
slot_faction_tier_1_town_troop    = 47

slot_faction_deserter_troop       = 48
slot_faction_guard_troop          = 49
slot_faction_messenger_troop      = 50
slot_faction_prison_guard_troop   = 51
slot_faction_castle_guard_troop   = 52

slot_faction_town_walker_male_troop      = 53
slot_faction_town_walker_female_troop    = 54
slot_faction_village_walker_male_troop   = 55
slot_faction_village_walker_female_troop = 56
slot_faction_town_spy_male_troop         = 57
slot_faction_town_spy_female_troop       = 58

slot_faction_has_rebellion_chance = 60

slot_faction_instability          = 61 #last time measured


#UNIMPLEMENTED FEATURE ISSUES
slot_faction_war_damage_inflicted_when_marshal_appointed = 62 #Probably deprecate
slot_faction_war_damage_suffered_when_marshal_appointed  = 63 #Probably deprecate

slot_faction_political_issue 							 = 64 #Center or marshal appointment
slot_faction_political_issue_time 						 = 65 #Now is used

#Rebellion changes
#slot_faction_rebellion_target                     = 65
#slot_faction_inactive_leader_location         = 66
#slot_faction_support_base                     = 67
#Rebellion changes



#slot_faction_deserter_party_template       = 62

slot_faction_reinforcements_a        = 77
slot_faction_reinforcements_b        = 78
slot_faction_reinforcements_c        = 79

slot_faction_num_armies              = 80
slot_faction_num_castles             = 81
slot_faction_num_towns               = 82

slot_faction_invasion_town                 = 83
slot_faction_invasion_day                  = 84

slot_faction_last_attacked_center    = 85
slot_faction_last_attacked_hours     = 86
slot_faction_last_safe_hours         = 87

slot_faction_num_routed_agents       = 90

#useful for competitive consumption
slot_faction_biggest_feast_score      = 91
slot_faction_biggest_feast_time       = 92
slot_faction_biggest_feast_host       = 93


#Faction AI states
slot_faction_last_feast_concluded       = 94 #Set when a feast starts
slot_faction_last_feast_start_time      = 94 #this is a bit confusing


slot_faction_ai_last_offensive_time 	= 95 #Set when an offensive concludes
slot_faction_last_offensive_concluded 	= 95 #Set when an offensive concludes

slot_faction_ai_last_rest_time      	= 96 #the last time that the faction has had default or feast AI -- this determines lords' dissatisfaction with the campaign. Set during faction_ai script
slot_faction_ai_current_state_started   = 97 #

slot_faction_ai_last_decisive_event     = 98 #capture a fortress or declaration of war

slot_faction_morale_of_player_troops    = 99

slot_faction_infantry_1_number         = 66
slot_faction_infantry_2_number         = 67
slot_faction_infantry_3_number         = 68
slot_faction_infantry_4_number         = slot_faction_range_1_number            = 69
slot_faction_infantry_5_number         = slot_faction_range_2_number            = 70
slot_faction_infantry_6_number         = slot_faction_range_3_number            = 71
slot_faction_infantry_7_number         = slot_faction_cavalry_1_number             = 72
slot_faction_infantry_8_number         = slot_faction_cavalry_2_number             = 73
slot_faction_infantry_9_number         = slot_faction_cavalry_3_number             = 74
slot_faction_infantry_end_number       = 75

slot_faction_elite_cavalry_1_troop        = 116
slot_faction_elite_cavalry_2_troop        = 117
slot_faction_elite_cavalry_3_troop        = 118


slot_faction_infantry_1_troop             = 100
slot_faction_infantry_2_troop             = 101
slot_faction_infantry_3_troop             = 102 
slot_faction_infantry_4_troop             = slot_faction_range_1_troop                = 103
slot_faction_infantry_5_troop             = slot_faction_range_2_troop                = 104
slot_faction_infantry_6_troop             = slot_faction_range_3_troop                = 105  
slot_faction_infantry_7_troop             = slot_faction_cavalry_1_troop              = 106
slot_faction_infantry_8_troop             = slot_faction_cavalry_2_troop              = 107
slot_faction_infantry_9_troop             = slot_faction_cavalry_3_troop              = 108 
slot_faction_infantry_end_troop           = 109

slot_faction_religion                      = 109
religion_none = 0
religion_human = 1
religion_chaos = 2
religion_order = 3
religion_nature = 4
religion_death = 5

dplmc_slot_faction_policy_time                = 110 
dplmc_slot_faction_centralization             = 111        
dplmc_slot_faction_aristocracy                = 112        
dplmc_slot_faction_serfdom                    = 113 
dplmc_slot_faction_quality                    = 114 
dplmc_slot_faction_patrol_time                = 115

#diplomacy
slot_faction_truce_days_with_factions_begin 			= 120
slot_faction_provocation_days_with_factions_begin 		= 140
slot_faction_war_damage_inflicted_on_factions_begin 	= 160
slot_faction_sum_advice_about_factions_begin 			= 180
dplmc_slot_faction_attitude_begin             = 200
dplmc_slot_faction_attitude                   = 200

#revolts -- notes for self
#type 1 -- minor revolt, aimed at negotiating change without changing the ruler
#type 2 -- alternate ruler revolt (ie, pretender, chinese dynastic revolt -- keep the same polity but switch the ruler)
	#subtype -- pretender (keeps the same dynasty)
	#"mandate of heaven" -- same basic rules, but a different dynasty
	#alternate/religious
	#alternate/political
#type 3 -- separatist revolt
	# reGonalist/dynastic (based around an alternate ruling house
	# regionalist/republican
	# messianic (ie, Canudos)
	
########################################################
##  PARTY SLOTS            #############################
########################################################
slot_party_type                = 0  #spt_caravan, spt_town, spt_castle

#slot_party_type values
##spt_caravan            = 1
spt_castle             = 2
spt_town               = 3
spt_village            = 4
##spt_forager            = 5
spt_huge_party           = 5
spt_reinforcement      = 6
spt_patrol             = 7
spt_messenger          = 8
spt_raider             = 9
spt_scout              = 10
spt_kingdom_caravan    = 11
spt_prisoner_train     = 12
spt_kingdom_hero_party = 13
##spt_merchant_caravan   = 14
spt_village_farmer     = 15
spt_ship               = 16
spt_cattle_herd        = 17
spt_bandit_lair        = 18
#spt_deserter           = 20
dplmc_spt_spouse        = 19
dplmc_spt_recruiter     = 20
dplmc_spt_gift_caravan  = 21
spt_adventurer_party       = 22

spt_lair              = 23
spt_bank              = 24
spt_treasure          = 25

spt_portal_1            = 26
spt_portal_2            = 27
spt_portal_3            = 28
spt_portal_4            = 29
spt_enhancement              = 30
spt_obelisk              = 31


slot_party_retreat_flag        = 2
slot_party_ignore_player_until = 3
slot_party_ai_state            = 4
slot_party_ai_object           = 5
slot_party_ai_rationale        = 6 #Currently unused, but can be used to save a string explaining the lord's thinking

#slot_town_belongs_to_kingdom   = 6
slot_town_lord                 = 7
slot_party_ai_substate         = 8
slot_town_claimed_by_player    = 9

slot_cattle_driven_by_player = slot_town_lord #hack

slot_town_center        = 10
slot_town_castle        = 11
slot_town_prison        = 12
slot_town_tavern        = 13
slot_town_store         = 14
slot_town_arena         = 16
slot_town_alley         = 17
slot_town_walls         = 18
slot_center_culture     = 19

slot_town_seneschal     = 15
slot_town_tavernkeeper  = 20
slot_town_weaponsmith   = 21
slot_town_armorer       = 22
slot_town_merchant      = 23
slot_town_horse_merchant= 24
slot_town_elder         = 25
slot_center_player_relation = 26

slot_center_siege_with_belfry = 27
slot_center_last_taken_by_troop = 28

slot_town_mercs            = 29
slot_merc_parties_town            = slot_town_mercs


# party will follow this party if set:
slot_party_commander_party = 30 #default -1   #Deprecate
slot_party_following_player    = 31
slot_party_follow_player_until_time = 32
slot_party_dont_follow_player_until_time = 33

slot_village_raided_by        = 34
slot_village_state            = 35 #svs_normal, svs_being_raided, svs_looted, svs_recovering, svs_deserted
slot_village_raid_progress    = 36
slot_village_recover_progress = 37
slot_village_smoke_added      = 38

slot_village_infested_by_bandits   = 39

slot_center_last_visited_by_lord   = 41

slot_center_last_player_alarm_hour = 42

slot_village_player_can_not_steal_cattle = 46

slot_center_accumulated_rents      = 47 #collected automatically by NPC lords
slot_center_accumulated_tariffs    = 48 #collected automatically by NPC lords
slot_town_wealth        = 49 #total amount of accumulated wealth in the center, pays for the garrison
slot_town_prosperity    = 50 #affects the amount of wealth generated
slot_town_player_odds   = 51


slot_party_last_toll_paid_hours = 52
slot_party_food_store           = 53 #used for sieges
slot_center_is_besieged_by      = 54 #used for sieges
slot_center_last_spotted_enemy  = 55

slot_party_cached_strength        = 56
slot_party_nearby_friend_strength = 57
slot_party_nearby_enemy_strength  = 58
slot_party_follower_strength      = 59

slot_town_reinforcement_party_template = 60
slot_center_original_faction           = 61
slot_center_ex_faction                 = 62

## CC
slot_party_original_faction            = 61
## CC

slot_party_follow_me                   = 63
slot_center_siege_begin_hours          = 64 #used for sieges
slot_center_siege_hardness             = 65

slot_center_sortie_strength            = 66
slot_center_sortie_enemy_strength      = 67

slot_party_last_in_combat              = 68 #used for AI
slot_party_last_in_home_center         = 69 #used for AI
slot_party_leader_last_courted         = 70 #used for AI
slot_party_last_in_any_center          = 71 #used for AI



slot_castle_exterior    = slot_town_center

#slot_town_rebellion_contact   = 76
#trs_not_yet_approached  = 0
#trs_approached_before   = 1
#trs_approached_recently = 2

argument_none         = 0
argument_claim        = 1 #deprecate for legal
argument_legal        = 1

argument_ruler        = 2 #deprecate for commons
argument_commons      = 2

argument_benefit      = 3 #deprecate for reward
argument_reward       = 3 

argument_victory      = 4
argument_lords        = 5
argument_rivalries    = 6 #new - needs to be added

slot_town_village_product = 76

slot_town_rebellion_readiness = 77
#(readiness can be a negative number if the rebellion has been defeated)

slot_town_arena_melee_mission_tpl = 78
slot_town_arena_torny_mission_tpl = 79
slot_town_arena_melee_1_num_teams = 80
slot_town_arena_melee_1_team_size = 81
slot_town_arena_melee_2_num_teams = 82
slot_town_arena_melee_2_team_size = 83
slot_town_arena_melee_3_num_teams = 84
slot_town_arena_melee_3_team_size = 85
slot_town_arena_melee_cur_tier    = 86
slot_town_melee_fights_chance	  = 87
slot_town_volunteer_troop_type  = 88
slot_town_volunteer_troop_amount= 89
slot_center_mercenary_troop_type  = slot_town_volunteer_troop_type
slot_center_mercenary_troop_amount= slot_town_volunteer_troop_amount


slot_center_npc_volunteer_troop_type   = 90
slot_center_npc_volunteer_troop_amount = 91
slot_center_merc_lance_type_1  = 90
slot_center_merc_lance_type_2  = 91
slot_center_volunteer_troop_type  = 92
slot_center_volunteer_troop_amount= 93

#slot_center_companion_candidate   = 94
slot_center_ransom_broker         = 95
slot_center_tavern_traveler       = 96
slot_center_traveler_info_faction = 97
slot_center_tavern_bookseller     = 98
slot_center_tavern_minstrel       = 99
slot_party_blind_to_other_parties  = 101

num_party_loot_slots    = 5
slot_party_next_looted_item_slot  = 109
slot_party_looted_item_1          = 110
slot_party_looted_item_2          = 111
slot_party_looted_item_3          = 112
slot_party_looted_item_4          = 113
slot_party_looted_item_5          = 114
slot_party_looted_item_1_modifier = 115
slot_party_looted_item_2_modifier = 116
slot_party_looted_item_3_modifier = 117
slot_party_looted_item_4_modifier = 118
slot_party_looted_item_5_modifier = 119

slot_village_bound_center         = 120
slot_village_market_town          = 121
slot_village_farmer_party         = 122
slot_party_home_center            = 123 #Only use with caravans and villagers

slot_center_current_improvement   = 124
slot_center_improvement_end_hour  = 125

slot_party_last_traded_center     = 126 


slot_center_lair_build_type                        = 129  #Lair
slot_center_village_type                           = 130  #money
slot_center_advance_build_type                        = 131  #
slot_center_lair_build_cooldown                        = 132
slot_center_extra_build_cooldown                        = 133
slot_center_advance_build_cooldown                        = 134

slot_center_lair_attack_cooldown                       = 119

village_type_basic = 1
village_type_mine = 2
village_type_garden = 3
village_type_graveyard = 4

Alchemists_Lab = 1
Imp_Pit = 2
Crystal_Mine = 3
Ore_Pit = 4
Silver_Mine = 5
Gold_Mine = 6
Mine = 7
Gem_Mine = 8
Golem_Factory = 9
Elemental_Conflux = 10
Graveyard2 = 11
Mystical_Garden = 12
Ruins = 13
Den_of_Thieves = 14
Imp_Cache2 = 15
Refugee_Camp = 16
Necromancy_Amplifier = 17
Dream_Teacher = 18
Nord_Warrior_Tomb = 19
Subterranean_Gate = 20

Blood_Tank = 21
Sepulcher = 22
Hunters_Cabins = 23
Dragon_Cliffs = 24
Stone_Ring = 25
Dragon_Shrine = 26
Hall_of_Shadows = 27
Dragon_Spire = 28
Runic_Chapel = 29
Lava_Fissure = 30
Altar_of_Chaos = 31
Heart_of_Pit = 32

Mage_Housings = 33
Arcane_Forge = 34

Order_of_Paladins = 35
Transept_of_Heaven = 36

Warriors_Tents = 37
Behemoth_Crag = 38
Troll_Cave = 39

Monastery = 40




farm    = "pt_farm"
nomad_tent    = "pt_nomad_tent"
graveyard    = "pt_graveyard"
gobin_slum    = "pt_gobin_slum"
imp_cache    = "pt_imp_cache"
rogue_hideout    = "pt_rogue_hideout"
longhouse    = "pt_longhouse"

dwarf_cottage    = "pt_dwarf_cottage"
elf_homestead    = "pt_elf_homestead"
monastery    = "pt_monastery"
magic_guild    = "pt_magic_guild"

keep = "pt_keep"
cathedral    = "pt_cathedral"
demon_gate    = "pt_demon_gate"
clan_halls    = "pt_clan_halls"
vampire_estate    = "pt_vampire_estate"
ogre_fort    = "pt_ogre_fort"
wolf_pen    = "pt_wolf_pen"
labyrinth    = "pt_labyrinth"
tomb_of_curses    = "pt_tomb_of_curses"
treant_alcove    = "pt_treant_alcove"

knights_chapter    = "pt_knights_chapter"
vampire_palace    = "pt_vampire_palace"
cloud_temple    = "pt_cloud_temple"
dragon_altar    = "pt_dragon_altar"
undead_magic_guild    = "pt_undead_magic_guild"
troll_cave    = "pt_troll_cave"
altar_of_light    = "pt_altar_of_light"
temple_of_the_fallen    = "pt_temple_of_the_fallen"
forlorn_cathedral    = "pt_forlorn_cathedral"
alchemist_lab    = "pt_alchemist_lab"


slot_center_player_enterprise     				  = 137 #noted with the item produced
slot_center_player_enterprise_production_order    = 138
slot_center_player_enterprise_consumption_order   = 139 #not used
slot_center_player_enterprise_days_until_complete = 139 #Used instead

slot_center_player_enterprise_balance             = 140 #not used
slot_center_player_enterprise_input_price         = 141 #not used
slot_center_player_enterprise_output_price        = 142 #not used

slot_center_infantry_1_number            = 143
slot_center_infantry_2_number            = 144
slot_center_infantry_3_number            = 145
slot_center_infantry_4_number            = slot_center_range_1_number               = 146
slot_center_infantry_5_number            = slot_center_range_2_number               = 147
slot_center_infantry_6_number            = slot_center_range_3_number               = 148
slot_center_infantry_7_number            = slot_center_cavalry_1_number             = 149
slot_center_infantry_8_number            = slot_center_cavalry_2_number             = 150
slot_center_infantry_9_number            = slot_center_cavalry_3_number             = 151

slot_center_has_order                          = 152

slot_center_has_bandits                        = 155
slot_town_has_tournament                       = 156
slot_town_tournament_max_teams                 = 157
slot_town_tournament_max_team_size             = 158

slot_center_faction_when_oath_renounced        = 159

slot_center_walker_0_troop                   = 160
slot_center_walker_1_troop                   = 161
slot_center_walker_2_troop                   = 162
slot_center_walker_3_troop                   = 163
slot_center_walker_4_troop                   = 164
slot_center_walker_5_troop                   = 165
slot_center_walker_6_troop                   = 166
slot_center_walker_7_troop                   = 167
slot_center_walker_8_troop                   = 168
slot_center_walker_9_troop                   = 169

slot_center_walker_0_dna                     = 170
slot_center_walker_1_dna                     = 171
slot_center_walker_2_dna                     = 172
slot_center_walker_3_dna                     = 173
slot_center_walker_4_dna                     = 174
slot_center_walker_5_dna                     = 175
slot_center_walker_6_dna                     = 176
slot_center_walker_7_dna                     = 177
slot_center_walker_8_dna                     = 178
slot_center_walker_9_dna                     = 179

slot_center_walker_0_type                    = 180
slot_center_walker_1_type                    = 181
slot_center_walker_2_type                    = 182
slot_center_walker_3_type                    = 183
slot_center_walker_4_type                    = 184
slot_center_walker_5_type                    = 185
slot_center_walker_6_type                    = 186
slot_center_walker_7_type                    = 187
slot_center_walker_8_type                    = 188
slot_center_walker_9_type                    = 189

slot_town_trade_route_1           = 190
slot_town_trade_route_2           = 191
slot_town_trade_route_3           = 192
slot_town_trade_route_4           = 193
slot_town_trade_route_5           = 194
slot_town_trade_route_6           = 195
slot_town_trade_route_7           = 196
slot_town_trade_route_8           = 197
slot_town_trade_route_9           = 198
slot_town_trade_route_10          = 199
slot_town_trade_route_11          = 200
slot_town_trade_route_12          = 201
slot_town_trade_route_13          = 202
slot_town_trade_route_14          = 203
slot_town_trade_route_15          = 204
slot_town_trade_routes_begin = slot_town_trade_route_1
slot_town_trade_routes_end = slot_town_trade_route_15 + 1


num_trade_goods = itm_siege_supply - itm_spice
slot_town_trade_good_productions_begin       = 500 #a harmless number, until it can be deprecated

#These affect production but in some cases also demand, so it is perhaps easier to itemize them than to have separate 

slot_village_number_of_cattle            = 205
slot_center_head_cattle         = 205 #dried meat, cheese, hides, butter
slot_center_head_sheep			= 206 #sausages, wool
slot_center_head_horses		 	= 207 #horses can be a trade item used in tracking ,but which are never offered for sale

slot_center_acres_pasture       = 208
slot_production_sources_begin = 209
slot_center_acres_grain			= 209 #grain
slot_center_acres_olives        = 210 #nothing for now
slot_center_acres_vineyard		= 211 #fruit
slot_center_acres_flax          = 212 #flax - can be used for sailcloth
slot_center_acres_dates			= 213 #dates

slot_center_fishing_fleet		= 214 #smoked fish
slot_center_salt_pans		    = 215 #salt

slot_center_apiaries       		= 216 #honey
slot_center_silk_farms			= 217 #silk
slot_center_kirmiz_farms		= 218 #dyes

slot_center_iron_deposits       = 219 #iron
slot_center_fur_traps			= 220 #furs
#timber
#pitch

slot_center_mills				= 221 #bread
slot_center_breweries			= 222 #ale
slot_center_wine_presses		= 223 #wine
slot_center_olive_presses		= 224 #oil

slot_center_linen_looms			= 225 #linen
slot_center_silk_looms          = 226 #velvet
slot_center_wool_looms          = 227 #wool cloth

slot_center_pottery_kilns		= 228 #pottery
slot_center_smithies			= 229 #tools
slot_center_tanneries			= 230 #leatherwork
slot_center_shipyards			= 231 #naval stores - uses timber, pitch, and linen

slot_center_household_gardens   = 232 #cabbages
slot_production_sources_end = 233

#all spice comes overland to Tulga
#all dyes come by sea to Jelkala

#chicken and pork are perishable and non-tradeable, and based on grain production
#timber and pitch if we ever have a shipbuilding industry
#limestone and timber for mortar, if we allow building

slot_town_last_nearby_fire_time                         = 240

#slot_town_trade_good_prices_begin            = slot_town_trade_good_productions_begin + num_trade_goods + 1
slot_party_following_orders_of_troop        = 244
slot_party_orders_type				        = 245
slot_party_orders_object				    = 246
slot_party_orders_time				    	= 247

slot_party_temp_slot_1			            = 248 #right now used only within a single script, merchant_road_info_to_s42, to denote closed roads. Now also used in comparative scripts
slot_party_under_player_suggestion			= 249 #move this up a bit
slot_town_trade_good_prices_begin 			= 250

slot_center_last_reconnoitered_by_faction_time 				= 350
#slot_center_last_reconnoitered_by_faction_cached_strength 	= 360
#slot_center_last_reconnoitered_by_faction_friend_strength 	= 370







kingdom_party_types_begin = spt_reinforcement
kingdom_party_types_end = spt_kingdom_hero_party + 1

#slot_faction_state values
sfs_active                     = 0
sfs_defeated                   = 1
sfs_inactive                   = 2
sfs_inactive_rebellion         = 3
sfs_beginning_rebellion        = 4


#slot_faction_ai_state values
sfai_default                   		 = 0 #also defending
sfai_gathering_army            		 = 1
sfai_attacking_center          		 = 2
sfai_raiding_village           		 = 3
sfai_attacking_enemy_army      		 = 4
sfai_attacking_enemies_around_center = 5
sfai_feast             		 		 = 6 #can be feast, wedding, or major tournament
#Social events are a generic aristocratic gathering. Tournaments take place if they are in a town, and hunts take place if they are at a castle.
#Weddings will take place at social events between betrothed couples if they have been engaged for at least a month, if the lady's guardian is the town lord, and if both bride and groom are present


#Rebellion system changes begin
sfai_nascent_rebellion          = 7
#Rebellion system changes end

#slot_party_ai_state values
spai_undefined                  = -1
spai_besieging_center           = 1
spai_patrolling_around_center   = 4
spai_raiding_around_center      = 5
##spai_raiding_village            = 6
spai_holding_center             = 7
##spai_helping_town_against_siege = 9
spai_engaging_army              = 10
spai_accompanying_army          = 11
spai_screening_army             = 12
spai_trading_with_town          = 13
spai_retreating_to_center       = 14
##spai_trading_within_kingdom     = 15
spai_visiting_village           = 16 #same thing, I think. Recruiting differs from holding because NPC parties don't actually enter villages

#slot_village_state values
svs_normal                      = 0
svs_being_raided                = 1
svs_looted                      = 2
svs_recovering                  = 3
svs_deserted                    = 4
svs_under_siege                 = 5

#$g_player_icon_state values
pis_normal                      = 0
pis_camping                     = 1
pis_ship                        = 2


########################################################
##  SCENE SLOTS            #############################
########################################################
slot_scene_visited              = 0
slot_scene_belfry_props_begin   = 10



########################################################
##  TROOP SLOTS            #############################
########################################################
#slot_troop_role         = 0  # 10=Kingdom Lord

slot_troop_occupation          = 2  # 0 = free, 1 = merchant
#slot_troop_duty               = 3  # Kingdom duty, 0 = free
#slot_troop_homage_type         = 45
#homage_mercenary =             = 1 #Player is on a temporary contract
#homage_official =              = 2 #Player has a royal appointment
#homage_feudal   =              = 3 #


slot_troop_state               = 3  
slot_troop_last_talk_time      = 4
slot_troop_met                 = 5 #i also use this for the courtship state -- may become cumbersome
slot_troop_courtship_state     = 5 #2 professed admiration, 3 agreed to seek a marriage, 4 ended relationship

slot_troop_party_template      = 6
#slot_troop_kingdom_rank        = 7

slot_troop_renown              = 7

##slot_troop_is_prisoner         = 8  # important for heroes only
slot_troop_prisoner_of_party   = 8  # important for heroes only
#slot_troop_is_player_companion = 9  # important for heroes only:::USE  slot_troop_occupation = slto_player_companion

slot_troop_present_at_event    = 9

slot_troop_leaded_party         = 10 # important for kingdom heroes only
slot_troop_wealth               = 11 # important for kingdom heroes only
slot_troop_cur_center           = 12 # important for royal family members only (non-kingdom heroes)

slot_troop_banner_scene_prop    = 13 # important for kingdom heroes and player only

slot_troop_original_faction     = 14 # for pretenders
#slot_troop_loyalty              = 15 #deprecated - this is now derived from other figures
slot_troop_player_order_state   = 16 #Deprecated
slot_troop_player_order_object  = 17 #Deprecated

#troop_player order state are all deprecated in favor of party_order_state. This has two reasons -- 1) to reset AI if the party is eliminated, and 2) to allow the player at a later date to give orders to leaderless parties, if we want that


#Post 0907 changes begin
slot_troop_age                 =  18
slot_troop_age_appearance      =  19

#Post 0907 changes end

slot_troop_does_not_give_quest = 20
slot_troop_player_debt         = 21
slot_troop_player_relation     = 22
#slot_troop_player_favor        = 23
slot_troop_last_quest          = 24
slot_troop_last_quest_betrayed = 25
slot_troop_last_persuasion_time= 26
slot_troop_last_comment_time   = 27
slot_troop_spawned_before      = 28

#Post 0907 changes begin
slot_troop_last_comment_slot   = 29
#Post 0907 changes end

slot_troop_spouse              = 30
slot_troop_father              = 31
slot_troop_mother              = 32
slot_troop_guardian            = 33 #Usually siblings are identified by a common parent.This is used for brothers if the father is not an active npc. At some point we might introduce geneologies
slot_troop_betrothed           = 34 #Obviously superseded once slot_troop_spouse is filled
#other relations are derived from one's parents 
#slot_troop_daughter            = 33
#slot_troop_son                 = 34
#slot_troop_sibling             = 35
slot_troop_love_interest_1     = 35 #each unmarried lord has three love interests
slot_troop_love_interest_2     = 36
slot_troop_love_interest_3     = 37
slot_troop_love_interests_end  = 38
#ways to court -- discuss a book, commission/compose a poem, present a gift, recount your exploits, fulfil a specific quest, appear at a tournament
#preferences for women - (conventional - father's friends)
slot_lady_no_messages          				= 37
slot_lady_last_suitor          				= 38
slot_lord_granted_courtship_permission      = 38

slot_troop_betrothal_time                   = 39 #used in scheduling the wedding

slot_troop_trainer_met                       = 30
slot_troop_trainer_waiting_for_result        = 31
slot_troop_trainer_training_fight_won        = 32
slot_troop_trainer_num_opponents_to_beat     = 33
slot_troop_trainer_training_system_explained = 34
slot_troop_trainer_opponent_troop            = 35
slot_troop_trainer_training_difficulty       = 36
slot_troop_trainer_training_fight_won        = 37


slot_lady_used_tournament					= 40


slot_troop_current_rumor       = 45
slot_troop_temp_slot           = 46
slot_troop_promised_fief       = 47

slot_troop_set_decision_seed       = 48 #Does not change
slot_troop_temp_decision_seed      = 49 #Resets at recalculate_ai
slot_troop_recruitment_random      = 50 #used in a number of different places in the intrigue procedures to overcome intermediate hurdles, although not for the final calculation, might be replaced at some point by the global decision seed
#Decision seeds can be used so that some randomness can be added to NPC decisions, without allowing the player to spam the NPC with suggestions
#The temp decision seed is reset 24 to 48 hours after the NPC last spoke to the player, while the set seed only changes in special occasions
#The single seed is used with varying modula to give high/low outcomes on different issues, without using a separate slot for each issue

slot_troop_intrigue_impatience = 51
#recruitment changes end

#slot_troop_honorable          = 50
#slot_troop_merciful          = 51
slot_lord_reputation_type     		  = 52
slot_lord_recruitment_argument        = 53 #the last argument proposed by the player to the lord
slot_lord_recruitment_candidate       = 54 #the last candidate proposed by the player to the lord

slot_troop_change_to_faction          = 55

#slot_troop_readiness_to_join_army     = 57 #possibly deprecate
#slot_troop_readiness_to_follow_orders = 58 #possibly deprecate

# NPC-related constants

#NPC companion changes begin
slot_troop_first_encountered          = 59
slot_troop_home                       = 60

slot_troop_morality_state       = 61
tms_no_problem         = 0
tms_acknowledged       = 1
tms_dismissed          = 2

slot_troop_morality_type = 62
tmt_aristocratic = 1
tmt_egalitarian = 2
tmt_humanitarian = 3
tmt_honest = 4
tmt_pious = 5

slot_troop_morality_value = 63

slot_troop_2ary_morality_type  = 64
slot_troop_2ary_morality_state = 65
slot_troop_2ary_morality_value = 66

slot_troop_town_with_contacts  = 67
slot_troop_town_contact_type   = 68 #1 are nobles, 2 are commons

slot_troop_morality_penalties =  69 ### accumulated grievances from morality conflicts


slot_troop_personalityclash_object     = 71
#(0 - they have no problem, 1 - they have a problem)
slot_troop_personalityclash_state    = 72 #1 = pclash_penalty_to_self, 2 = pclash_penalty_to_other, 3 = pclash_penalty_to_other,
pclash_penalty_to_self  = 1
pclash_penalty_to_other = 2
pclash_penalty_to_both  = 3
#(a string)
slot_troop_personalityclash2_object   = 73
slot_troop_personalityclash2_state    = 74

slot_troop_personalitymatch_object   =  75
slot_troop_personalitymatch_state   =  76

slot_troop_personalityclash_penalties = 77 ### accumulated grievances from personality clash
slot_troop_personalityclash_penalties = 77 ### accumulated grievances from personality clash

slot_troop_home_speech_delivered = 78 #only for companions
slot_troop_discussed_rebellion   = 78 #only for pretenders

#courtship slots
slot_lady_courtship_heroic_recited 	    = 74
slot_lady_courtship_allegoric_recited 	= 75
slot_lady_courtship_comic_recited 		= 76
slot_lady_courtship_mystic_recited 		= 77
slot_lady_courtship_tragic_recited 		= 78



#NPC history slots
slot_troop_met_previously        = 80
slot_troop_turned_down_twice     = 81
slot_troop_playerparty_history   = 82

pp_history_scattered         = 1
pp_history_dismissed         = 2
pp_history_quit              = 3
pp_history_indeterminate     = 4

slot_troop_playerparty_history_string   = 83
slot_troop_return_renown        = 84

slot_troop_custom_banner_bg_color_1      = 85
slot_troop_custom_banner_bg_color_2      = 86
slot_troop_custom_banner_charge_color_1  = 87
slot_troop_custom_banner_charge_color_2  = 88
slot_troop_custom_banner_charge_color_3  = 89
slot_troop_custom_banner_charge_color_4  = 90
slot_troop_custom_banner_bg_type         = 91
slot_troop_custom_banner_charge_type_1   = 92
slot_troop_custom_banner_charge_type_2   = 93
slot_troop_custom_banner_charge_type_3   = 94
slot_troop_custom_banner_charge_type_4   = 95
slot_troop_custom_banner_flag_type       = 96
slot_troop_custom_banner_num_charges     = 97
slot_troop_custom_banner_positioning     = 98
slot_troop_custom_banner_map_flag_type   = 99

#conversation strings -- must be in this order!
slot_troop_intro 						= 101
slot_troop_intro_response_1 			= 102
slot_troop_intro_response_2 			= 103
slot_troop_backstory_a 					= 104
slot_troop_backstory_b 					= 105
slot_troop_backstory_c 					= 106
slot_troop_backstory_delayed 			= 107
slot_troop_backstory_response_1 		= 108
slot_troop_backstory_response_2 		= 109
slot_troop_signup   					= 110
slot_troop_signup_2 					= 111
slot_troop_signup_response_1 			= 112
slot_troop_signup_response_2 			= 113
slot_troop_mentions_payment 			= 114 #Not actually used
slot_troop_payment_response 			= 115 #Not actually used
slot_troop_morality_speech   			= 116
slot_troop_2ary_morality_speech 		= 117
slot_troop_personalityclash_speech 		= 118
slot_troop_personalityclash_speech_b 	= 119
slot_troop_personalityclash2_speech 	= 120
slot_troop_personalityclash2_speech_b 	= 121
slot_troop_personalitymatch_speech 		= 122
slot_troop_personalitymatch_speech_b 	= 123
slot_troop_retirement_speech 			= 124
slot_troop_rehire_speech 				= 125
slot_troop_home_intro           		= 126
slot_troop_home_description    			= 127
slot_troop_home_description_2 			= 128
slot_troop_home_recap         			= 129
slot_troop_honorific   					= 130
slot_troop_kingsupport_string_1			= 131
slot_troop_kingsupport_string_2			= 132
slot_troop_kingsupport_string_2a		= 133
slot_troop_kingsupport_string_2b		= 134
slot_troop_kingsupport_string_3			= 135
slot_troop_kingsupport_objection_string	= 136
slot_troop_intel_gathering_string	    = 137
slot_troop_fief_acceptance_string	    = 138
slot_troop_woman_to_woman_string	    = 139
slot_troop_turn_against_string	        = 140

slot_troop_strings_end 					= 141

slot_troop_payment_request 				= 141

#141, support base removed, slot now available

slot_troop_kingsupport_state			= 142
slot_troop_kingsupport_argument			= 143
slot_troop_kingsupport_opponent			= 144
slot_troop_kingsupport_objection_state  = 145 #0, default, 1, needs to voice, 2, has voiced

slot_troop_days_on_mission		        = 150
slot_troop_current_mission			    = 151
slot_troop_mission_object               = 152
npc_mission_kingsupport					= 1
npc_mission_gather_intel                = 2
npc_mission_peace_request               = 3
npc_mission_pledge_vassal               = 4
npc_mission_seek_recognition            = 5
npc_mission_test_waters                 = 6
npc_mission_non_aggression              = 7
npc_mission_rejoin_when_possible        = 8

#Number of routed agents after battle ends.
slot_troop_player_routed_agents                 = 146
slot_troop_ally_routed_agents                   = 147
slot_troop_enemy_routed_agents                  = 148

#Special quest slots
slot_troop_mission_participation        = 149
mp_unaware                              = 0 
mp_stay_out                             = 1 
mp_prison_break_fight                   = 2 
mp_prison_break_stand_back              = 3 
mp_prison_break_escaped                 = 4 
mp_prison_break_caught                  = 5 

#Below are some constants to expand the political system a bit. The idea is to make quarrels less random, but instead make them serve a rational purpose -- as a disincentive to lords to seek 

slot_troop_controversy                     = 150 #Determines whether or not a troop is likely to receive fief or marshalship
slot_troop_recent_offense_type 	           = 151 #failure to join army, failure to support colleague
slot_troop_recent_offense_object           = 152 #to whom it happened
slot_troop_recent_offense_time             = 153
slot_troop_stance_on_faction_issue         = 154 #when it happened

tro_failed_to_join_army                    = 1
tro_failed_to_support_colleague            = 2

#CONTROVERSY
#This is used to create a more "rational choice" model of faction politics, in which lords pick fights with other lords for gain, rather than simply because of clashing personalities
#It is intended to be a limiting factor for players and lords in their ability to intrigue against each other. It represents the embroilment of a lord in internal factional disputes. In contemporary media English, a lord with high "controversy" would be described as "embattled."
#The main effect of high controversy is that it disqualifies a lord from receiving a fief or an appointment
#It is a key political concept because it provides incentive for much of the political activity. For example, Lord Red Senior is worried that his rival, Lord Blue Senior, is going to get a fied which Lord Red wants. So, Lord Red turns to his protege, Lord Orange Junior, to attack Lord Blue in public. The fief goes to Lord Red instead of Lord Blue, and Lord Red helps Lord Orange at a later date.


slot_troop_will_join_prison_break      = 161


troop_slots_reserved_for_relations_start        = 165 #this is based on id_troops, and might change

slot_troop_relations_begin				= 0 #this creates an array for relations between troops
											#Right now, lords start at 165 and run to around 290, including pretenders
											
###################################################################################
# AutoLoot: Modified Constants
########################################################
##  PLAYER SLOTS           #############################
########################################################

slot_player_spawned_this_round                 = 0
slot_player_last_rounds_used_item_earnings     = 1
slot_player_selected_item_indices_begin        = 2
slot_player_selected_item_indices_end          = 11
slot_player_cur_selected_item_indices_begin    = slot_player_selected_item_indices_end
slot_player_cur_selected_item_indices_end      = slot_player_selected_item_indices_end + 9
slot_player_join_time                          = 21
slot_player_button_index                       = 22 #used for presentations
slot_player_can_answer_poll                    = 23
slot_player_first_spawn                        = 24
slot_player_spawned_at_siege_round             = 25
slot_player_poll_disabled_until_time           = 26
slot_player_total_equipment_value              = 27
slot_player_last_team_select_time              = 28
slot_player_death_pos_x                        = 29
slot_player_death_pos_y                        = 30
slot_player_death_pos_z                        = 31
slot_player_damage_given_to_target_1           = 32 #used only in destroy mod
slot_player_damage_given_to_target_2           = 33 #used only in destroy mod
slot_player_last_bot_count                     = 34
slot_player_bot_type_1_wanted                  = 35
slot_player_bot_type_2_wanted                  = 36
slot_player_bot_type_3_wanted                  = 37
slot_player_bot_type_4_wanted                  = 38
slot_player_spawn_count                        = 39


########################################################
##  TEAM SLOTS             #############################
########################################################

slot_team_flag_situation                       = 0

#"$character_gender"


#Rebellion changes end
# character backgrounds
#"$background_type"
cb_noble = 1
cb_merchant = 2
cb_guard = 3
cb_forester = 4
cb_nomad = 5
cb_thief = 6
cb_priest = 7
#"$background_answer_2"
cb2_page = 0
cb2_apprentice = 1
cb2_urchin  = 2
cb2_steppe_child = 3
cb2_merchants_helper = 4
#"$background_answer_3"
cb3_poacher = 3
cb3_craftsman = 4
cb3_peddler = 5
cb3_troubadour = 7
cb3_squire = 8
cb3_lady_in_waiting = 9
cb3_student = 10

cb4_revenge = 1
cb4_loss    = 2
cb4_wanderlust =  3
cb4_disown  = 5
cb4_greed  = 6

#NPC system changes end
#Encounter types
enctype_fighting_against_village_raid = 1
enctype_catched_during_village_raid   = 2


### Troop occupations slot_troop_occupation
slto_merchant           = 1
slto_inactive           = 0 #for companions at the beginning of the game
slto_wait_for_hire      = 11
slto_kingdom_hero       = 2

slto_player_companion   = 5 #This is specifically for companions in the employ of the player -- ie, in the party, or on a mission
slto_kingdom_lady       = 6 #Usually inactive (Calradia is a traditional place). However, can be made potentially active if active_npcs are expanded to include ladies
slto_kingdom_seneschal  = 7
slto_robber_knight      = 8
slto_inactive_pretender = 9
slto_adventurer         = 10 
slto_troop_follower     = 100
slto_troop_leader       = 101

stl_unassigned          = -1
stl_reserved_for_player = -2
stl_rejected_by_player  = -3

#NPC changes begin
slto_retirement      = 11
#slto_retirement_medium    = 12
#slto_retirement_short     = 13
#NPC changes end

########################################################
##  QUEST SLOTS            #############################
########################################################

slot_quest_target_center            = 1
slot_quest_target_troop             = 2
slot_quest_target_faction           = 3
slot_quest_object_troop             = 4
##slot_quest_target_troop_is_prisoner = 5
slot_quest_giver_troop              = 6
slot_quest_object_center            = 7
slot_quest_target_party             = 8
slot_quest_target_party_template    = 9
slot_quest_target_amount            = 10
slot_quest_current_state            = 11
slot_quest_giver_center             = 12
slot_quest_target_dna               = 13
slot_quest_target_item              = 14
slot_quest_object_faction           = 15

slot_quest_target_state             = 16
slot_quest_object_state             = 17

slot_quest_convince_value           = 19
slot_quest_importance               = 20
slot_quest_xp_reward                = 21
slot_quest_gold_reward              = 22
slot_quest_expiration_days          = 23
slot_quest_dont_give_again_period   = 24
slot_quest_dont_give_again_remaining_days = 25

slot_quest_failure_consequence      = 26
slot_quest_temp_slot      			= 27

########################################################
##  PARTY TEMPLATE SLOTS   #############################
########################################################

# Ryan BEGIN
slot_party_template_num_killed   = 1

slot_party_template_lair_type    	 	= 3
slot_party_template_lair_party    		= 4
slot_party_template_lair_spawnpoint     = 5

# party template slots
slot_party_template_has_hero            = 6
slot_party_template_spawn_point         = 7
slot_party_template_hero_id             = 8
slot_party_template_hero_name_begin     = 9
slot_party_template_hero_party_id       = 10
slot_party_template_hero_pre_name       = 11
slot_party_template_hero_pre_pre_name   = 12
slot_party_template_hero_next_spawn_time = 13
# Ryan END

slot_party_template_type   = 15

slot_party_template_basic_gold   = 16
slot_party_template_bonus_gold   = 17

slot_party_template_rewards_type   = 18
slot_party_template_rewards_num    = 19

slot_party_template_extra_troop   = 20
slot_party_template_extra_troop_num   = 21

slot_party_template_extra_rewards_type   = 22
slot_party_template_extra_rewards_num   = 23

lair              = 1
bank              = 2
treasure          = 3
enhancement       = 4
portal            = 5
experiance_stone  = 6
obelisk  = 7
other             = -1

Minor   = -2
Major   = -3
Relic   = -4

Book    = -5
Scroll  = -6

########################################################
##  SCENE PROP SLOTS       #############################
########################################################

scene_prop_open_or_close_slot       = 1
scene_prop_smoke_effect_done        = 2
scene_prop_number_of_agents_pushing = 3 #for belfries only
scene_prop_next_entry_point_id      = 4 #for belfries only
scene_prop_belfry_platform_moved    = 5 #for belfries only
scene_prop_slots_end                = 6

scene_prop_owner                = 10
scene_prop_owner_team           = 11
scene_prop_spell_id             = 12
scene_prop_spawn_time           = 13
scene_prop_attached_agent       = 14
scene_prop_scale                = 15
scene_prop_is_move              = 16

########################################################
rel_enemy   = 0
rel_neutral = 1
rel_ally    = 2


#Talk contexts
tc_town_talk                  = 0
tc_court_talk   	      	  = 1
tc_party_encounter            = 2
tc_castle_gate                = 3
tc_siege_commander            = 4
tc_join_battle_ally           = 5
tc_join_battle_enemy          = 6
tc_castle_commander           = 7
tc_hero_freed                 = 8
tc_hero_defeated              = 9
tc_entering_center_quest_talk = 10
tc_back_alley                 = 11
tc_siege_won_seneschal        = 12
tc_ally_thanks                = 13
tc_tavern_talk                = 14
tc_rebel_thanks               = 15
tc_garden            		  = 16
tc_courtship            	  = 16
tc_after_duel            	  = 17
tc_prison_break               = 18
tc_escape               	  = 19
tc_give_center_to_fief        = 20
tc_merchants_house            = 21


#Troop Commentaries begin
#Log entry types
#civilian
logent_village_raided            = 1
logent_village_extorted          = 2
logent_caravan_accosted          = 3
logent_traveller_attacked        = 3

logent_helped_peasants           = 4 

logent_party_traded              = 5

logent_castle_captured_by_player              = 10
logent_lord_defeated_by_player                = 11
logent_lord_captured_by_player                = 12
logent_lord_defeated_but_let_go_by_player     = 13
logent_player_defeated_by_lord                = 14
logent_player_retreated_from_lord             = 15
logent_player_retreated_from_lord_cowardly    = 16
logent_lord_helped_by_player                  = 17
logent_player_participated_in_siege           = 18
logent_player_participated_in_major_battle    = 19
logent_castle_given_to_lord_by_player         = 20

logent_pledged_allegiance          = 21
logent_liege_grants_fief_to_vassal = 22


logent_renounced_allegiance      = 23 

logent_player_claims_throne_1    		               = 24
logent_player_claims_throne_2    		               = 25


logent_troop_feels_cheated_by_troop_over_land		   = 26
logent_ruler_intervenes_in_quarrel                     = 27
logent_lords_quarrel_over_land                         = 28
logent_lords_quarrel_over_insult                       = 29
logent_marshal_vs_lord_quarrel                  	   = 30
logent_lords_quarrel_over_woman                        = 31

logent_lord_protests_marshall_appointment			   = 32
logent_lord_blames_defeat						   	   = 33

logent_player_suggestion_succeeded					   = 35
logent_player_suggestion_failed					       = 36

logent_liege_promises_fief_to_vassal				   = 37

logent_lord_insults_lord_for_cowardice                 = 38
logent_lord_insults_lord_for_rashness                  = 39
logent_lord_insults_lord_for_abandonment               = 40
logent_lord_insults_lord_for_indecision                = 41
logent_lord_insults_lord_for_cruelty                   = 42
logent_lord_insults_lord_for_dishonor                  = 43




logent_game_start                           = 45 
logent_poem_composed                        = 46 ##Not added
logent_tournament_distinguished             = 47 ##Not added
logent_tournament_won                       = 48 ##Not added

#logent courtship - lady is always actor, suitor is always troop object
logent_lady_favors_suitor                   = 51 #basically for gossip
logent_lady_betrothed_to_suitor_by_choice   = 52
logent_lady_betrothed_to_suitor_by_family   = 53
logent_lady_rejects_suitor                  = 54
logent_lady_father_rejects_suitor           = 55
logent_lady_marries_lord                    = 56
logent_lady_elopes_with_lord                = 57
logent_lady_rejected_by_suitor              = 58
logent_lady_betrothed_to_suitor_by_pressure = 59 #mostly for gossip

logent_lady_and_suitor_break_engagement		= 60
logent_lady_marries_suitor				    = 61

logent_lord_holds_lady_hostages             = 62
logent_challenger_defeats_lord_in_duel      = 63
logent_challenger_loses_to_lord_in_duel     = 64

logent_player_stole_cattles_from_village    = 66

logent_party_spots_wanted_bandits           = 70


logent_border_incident_cattle_stolen          = 72 #possibly add this to rumors for non-player faction
logent_border_incident_bride_abducted         = 73 #possibly add this to rumors for non-player faction
logent_border_incident_villagers_killed       = 74 #possibly add this to rumors for non-player faction
logent_border_incident_subjects_mistreated    = 75 #possibly add this to rumors for non-player faction

#These supplement caravans accosted and villages burnt, in that they create a provocation. So far, they only refer to the player
logent_border_incident_troop_attacks_neutral  = 76
logent_border_incident_troop_breaks_truce     = 77
logent_border_incident_troop_suborns_lord   = 78


logent_policy_ruler_attacks_without_provocation 			= 80
logent_policy_ruler_ignores_provocation         			= 81 #possibly add this to rumors for non-player factions
logent_policy_ruler_makes_peace_too_soon        			= 82
logent_policy_ruler_declares_war_with_justification         = 83
logent_policy_ruler_breaks_truce                            = 84
logent_policy_ruler_issues_indictment_just                  = 85 #possibly add this to rumors for non-player faction
logent_policy_ruler_issues_indictment_questionable          = 86 #possibly add this to rumors for non-player faction

logent_player_faction_declares_war						    = 90 #this doubles for declare war to extend power
logent_faction_declares_war_out_of_personal_enmity		    = 91
logent_faction_declares_war_to_regain_territory 		    = 92
logent_faction_declares_war_to_curb_power					= 93
logent_faction_declares_war_to_respond_to_provocation	    = 94

##diplomacy begin
logent_faction_declares_war_to_fulfil_pact	    = 95
logent_war_declaration_types_end							= 96
##diplomacy end

#logent_lady_breaks_betrothal_with_lord      = 58
#logent_lady_betrothal_broken_by_lord        = 59

#lord reputation type, for commentaries
#"Martial" will be twice as common as the other types
lrep_none           = 0 
lrep_martial        = 1 #chivalrous but not terribly empathetic or introspective, - eg Richard Lionheart, your average 14th century French baron
lrep_quarrelsome    = 2 #spiteful, cynical, a bit paranoid, possibly hotheaded - eg Robert Graves' Tiberius, some of Charles VI's uncles
lrep_selfrighteous  = 3 #coldblooded, moralizing, often cruel - eg William the Conqueror, Timur, Octavian, Aurangzeb (although he is arguably upstanding instead, particularly after his accession)
lrep_cunning        = 4 #coldblooded, pragmatic, amoral - eg Louis XI, Guiscard, Akbar Khan, Abd al-Aziz Ibn Saud
lrep_debauched      = 5 #spiteful, amoral, sadistic - eg Caligula, Tuchman's Charles of Navarre
lrep_goodnatured    = 6 #chivalrous, benevolent, perhaps a little too decent to be a good warlord - eg Hussein ibn Ali. Few well-known historical examples maybe. because many lack the drive to rise to faction leadership. Ranjit Singh has aspects
lrep_upstanding     = 7 #moralizing, benevolent, pragmatic, - eg Bernard Cornwell's Alfred, Charlemagne, Salah al-Din, Sher Shah Suri

lrep_roguish        = 8 #used for commons, specifically ex-companions. Tries to live life as a lord to the full
lrep_benefactor     = 9 #used for commons, specifically ex-companions. Tries to improve lot of folks on land
lrep_custodian      = 10 #used for commons, specifically ex-companions. Tries to maximize fief's earning potential

#lreps specific to dependent noblewomen
lrep_conventional    = 21 #Charlotte York in SATC seasons 1-2, probably most medieval aristocrats
lrep_adventurous     = 22 #Tomboyish. However, this basically means that she likes to travel and hunt, and perhaps yearn for wider adventures. However, medieval noblewomen who fight are rare, and those that attempt to live independently of a man are rarer still, and best represented by pre-scripted individuals like companions
lrep_otherworldly    = 23 #Prone to mysticism, romantic. 
lrep_ambitious       = 24 #Lady Macbeth
lrep_moralist        = 25 #Equivalent of upstanding or benefactor -- takes nobless oblige, and her traditional role as repository of morality, very seriously. Based loosely on Christine de Pisa 

#a more complicated system of reputation could include the following...

#successful vs unlucky -- basic gauge of success
#daring vs cautious -- maybe not necessary
#honorable/pious/ideological vs unscrupulous -- character's adherance to an external code of conduct. Fails to capture complexity of people like Aurangzeb, maybe, but good for NPCs
	#(visionary/altruist and orthodox/unorthodox could be a subset of the above, or the specific external code could be another tag)
#generous/loyal vs manipulative/exploitative -- character's sense of duty to specific individuals, based on their relationship. Affects loyalty of troops, etc
#merciful vs cruel/ruthless/sociopathic -- character's general sense of compassion. Sher Shah is example of unscrupulous and merciful (the latter to a degree).
#dignified vs unconventional -- character's adherance to social conventions. Very important, given the times


courtship_poem_tragic      = 1 #Emphasizes longing, Laila and Majnoon
courtship_poem_heroic      = 2 #Norse sagas with female heroines
courtship_poem_comic       = 3 #Emphasis on witty repartee -- Contrasto (Sicilian school satire) 
courtship_poem_mystic      = 4 #Sufi poetry. Song of Songs
courtship_poem_allegoric   = 5 #Idealizes woman as a civilizing force -- the Romance of the Rose, Siege of the Castle of Love

#courtship gifts currently deprecated


plain_village       = 1
snow_village        = 2
steppe_village      = 3
desert_village      = 4

plain_villages_begin = "scn_village_1"
plain_villages_end = "scn_village_16"

snow_villages_begin = "scn_village_16"
snow_villages_end = "scn_village_11"

steppe_villages_begin =  "scn_village_11"
steppe_villages_end =  "scn_village_91"

desert_villages_begin = "scn_village_91"
desert_villages_end =  "scn_village_35"

#Troop Commentaries end

tutorial_fighters_begin = "trp_tutorial_fighter_1"
tutorial_fighters_end   = "trp_tutorial_archer_1"

#Walker types: 
walkert_default            = 0
walkert_needs_money        = 1
walkert_needs_money_helped = 2
walkert_spy                = 3
num_town_walkers = 8
town_walker_entries_start = 32

# reinforcement_cost_easy = 600
# reinforcement_cost_moderate = 450
reinforcement_cost_easy = 2400
reinforcement_cost_moderate = 1800
reinforcement_cost_hard = 1200

merchant_toll_duration        = 72 #Tolls are valid for 72 hours

hero_escape_after_defeat_chance = 30


raid_distance = 4

surnames_begin = "str_surname_1"
surnames_end = "str_surnames_end"

merchant_surname_begin = "str_merchant_surname_1"
merchant_surname_end = "str_merchant_surname_end"

names_begin = "str_name_1"
names_end = surnames_begin
countersigns_begin = "str_countersign_1"
countersigns_end = names_begin
secret_signs_begin = "str_secret_sign_1"
secret_signs_end = countersigns_begin

kingdom_titles_male_begin = "str_faction_title_male_player"
kingdom_titles_female_begin = "str_faction_title_female_player"

kingdoms_begin = "fac_player_supporters_faction"
kingdoms_end = "fac_kingdoms_end"

commom_kingdoms_begin = "fac_kingdom_1"
commom_kingdoms_end = kingdoms_end

mod_heroes_kingdoms_begin = "fac_kingdom_2"
mod_heroes_kingdoms_end = kingdoms_end

bandit_kingdoms_begin = "fac_kingdom_2"
bandit_kingdoms_end = "fac_kingdom_1"

npc_kingdoms_begin = "fac_kingdom_1"
npc_kingdoms_end = kingdoms_end

quick_battle_kingdoms_end = npc_kingdoms_end

kingdom_ladies_begin = "trp_knight_1_1_wife"
kingdom_ladies_end = "trp_heroes_end"

#active NPCs in order: companions, kings, lords, pretenders

pretenders_begin = "trp_kingdom_1_pretender"
pretenders_end = "trp_adventurer_troop_1"

lords_begin = "trp_knight_1_1"
lords_end = pretenders_begin

kings_begin = "trp_kingdom_1_lord"
kings_end = lords_begin

companions_begin = "trp_npc1"
companions_end = kings_begin

active_npcs_begin = "trp_npc1"
active_npcs_end = kingdom_ladies_begin

companions_begin = "trp_npc1"
companions_end = kings_begin


adventurer_troops_begin = "trp_adventurer_troop_1"
adventurer_troops_end = "trp_knight_1_1_wife"

quick_battle_troops_begin = "trp_quick_battle_troop_1"
quick_battle_troops_end = "trp_kingdom_1_lady_1"

#"active_npcs_begin replaces kingdom_heroes_begin to allow for companions to become lords. Includes anyone who may at some point lead their own party: the original kingdom heroes, companions who may become kingdom heroes, and pretenders. (slto_kingdom_hero as an occupation means that you lead a party on the map. Pretenders have the occupation "slto_inactive_pretender", even if they are part of a player's party, until they have their own independent party)
#If you're a modder and you don't want to go through and switch every kingdom_heroes to active_npcs, simply define a constant: kingdom_heroes_begin = active_npcs_begin., and kingdom_heroes_end = active_npcs_end. I haven't tested for that, but I think it should work.

active_npcs_including_player_begin = "trp_kingdom_heroes_including_player_begin"
original_kingdom_heroes_begin = "trp_kingdom_1_lord"

heroes_begin = active_npcs_begin
heroes_end = kingdom_ladies_end

soldiers_begin = "trp_farmer"
soldiers_end = "trp_town_walker_1"



#Rebellion changes

##rebel_factions_begin = "fac_kingdom_1_rebels"
##rebel_factions_end =   "fac_kingdoms_end"

#Rebellion changes

## CC

mercenary_troops_begin = "trp_townsman"
mercenary_troops_end = "trp_mercenaries_end"

kingdom_troops_begin = "trp_france_prison_guard"
kingdom_troops_end = "trp_looter"

village_troops_begin =  "trp_we_recruit"
village_troops_end =  "trp_welsh_longbowm_1" 

town_troops_begin = "trp_france_town_recruit"
town_troops_end =  "trp_france_knight_1"

nobility_troops_begin = "trp_france_knight_1" 
nobility_troops_end = kingdom_troops_end

#army_troops_begin =  kingdom_troops_begin
#army_troops_end =  "trp_swadian_militia_leader" 

#militia_troops_begin = "trp_swadian_militia_leader"
#militia_troops_end =  "trp_we_knight_1"

#nobility_troops_begin = "trp_we_knight_1" 
#nobility_troops_end = kingdom_troops_end

mountain_troops_begin = "trp_mountain_tribesman" 
mountain_troops_end = "trp_forest_recruit"

forest_troops_begin = "trp_forest_recruit" 
forest_troops_end = "trp_steppe_tribesman"

dark_troops_begin = "trp_strange_warrior" 
dark_troops_end = "trp_caravan_master"

bandits_begin = "trp_bandit"
bandits_end = "trp_rus_cossack"

outlaws_troops_begin = "trp_looter"
outlaws_troops_end = "trp_rus_cossack"

bandit_party_template_begin = "pt_forest_bandits"
bandit_party_template_end   = "pt_deserters"

bandit_troops_begin = "trp_forest_bandit"
bandit_troops_end   = "trp_forest_brigand"

bandit_heroes_begin = "trp_forest_bandit_hero"
bandit_heroes_end   = "trp_Xerina"

mercenary_heroes_begin = "trp_Xerina"
mercenary_heroes_end   = "trp_tutorial_trainer"

# Custom Troops begin
customizable_troops_begin = "trp_custom_recruit"
customizable_troops_end = "trp_custom_troops_end"
# Custom  Troops end

town_seneschal_begin = "trp_town_1_seneschal"
town_seneschal_end = "trp_town_1_arena_master"

mystic_merchant_begin = "trp_mystic_merchant_1"
mystic_merchant_end   = "trp_kingdom_heroes_including_player_begin"

tavern_minstrels_begin = "trp_tavern_minstrel_1"
tavern_minstrels_end   = mystic_merchant_begin
## CC

tavern_booksellers_begin = "trp_tavern_bookseller_1"
tavern_booksellers_end   = tavern_minstrels_begin

tavern_travelers_begin = "trp_tavern_traveler_1"
tavern_travelers_end   = tavern_booksellers_begin

ransom_brokers_begin = "trp_ransom_broker_1"
ransom_brokers_end   = tavern_travelers_begin

taverngoers_begin = ransom_brokers_begin
taverngoers_end = tavern_minstrels_end
pool_troops_begin = "trp_temp_array_a"
pool_troops_end_minus_one = "trp_multiplayer_data"
pool_troops_end = "trp_book_read"

multiplayer_troops_begin = "trp_swadian_crossbowman_multiplayer"
multiplayer_troops_end = "trp_multiplayer_end"

multiplayer_ai_troops_begin = "trp_swadian_crossbowman_multiplayer_ai"
multiplayer_ai_troops_end = multiplayer_troops_begin

multiplayer_scenes_begin = "scn_multi_scene_1"
multiplayer_scenes_end = "scn_multiplayer_maps_end"

multiplayer_scene_names_begin = "str_multi_scene_1"
multiplayer_scene_names_end = "str_multi_scene_end"

multiplayer_flag_projections_begin = "mesh_flag_project_sw"
multiplayer_flag_projections_end = "mesh_flag_projects_end"

multiplayer_flag_taken_projections_begin = "mesh_flag_project_sw_miss"
multiplayer_flag_taken_projections_end = "mesh_flag_project_misses_end"

multiplayer_game_type_names_begin = "str_multi_game_type_1"
multiplayer_game_type_names_end = "str_multi_game_types_end"

quick_battle_troop_texts_begin = "str_quick_battle_troop_1"
quick_battle_troop_texts_end = "str_quick_battle_troops_end"

quick_battle_scenes_begin = "scn_quick_battle_scene_1"
quick_battle_scenes_end = "scn_quick_battle_maps_end"

quick_battle_scene_images_begin = "mesh_cb_ui_maps_scene_01"

quick_battle_battle_scenes_begin = quick_battle_scenes_begin
quick_battle_battle_scenes_end = "scn_quick_battle_scene_4"

quick_battle_siege_scenes_begin = quick_battle_battle_scenes_end
quick_battle_siege_scenes_end = quick_battle_scenes_end

quick_battle_scene_names_begin = "str_quick_battle_scene_1"

lord_quests_begin = "qst_deliver_message"
lord_quests_end   = "qst_follow_army"

lord_quests_begin_2 = "qst_destroy_bandit_lair"
lord_quests_end_2   = "qst_blank_quest_2"

enemy_lord_quests_begin = "qst_lend_surgeon"
enemy_lord_quests_end   = lord_quests_end

village_elder_quests_begin = "qst_deliver_grain"
village_elder_quests_end = "qst_eliminate_bandits_infesting_village"

village_elder_quests_begin_2 = "qst_blank_quest_6"
village_elder_quests_end_2   = "qst_blank_quest_6"

mayor_quests_begin  = "qst_move_cattle_herd"
mayor_quests_end    = village_elder_quests_begin

mayor_quests_begin_2 = "qst_blank_quest_11"
mayor_quests_end_2   = "qst_blank_quest_11"

lady_quests_begin = "qst_rescue_lord_by_replace"
lady_quests_end   = mayor_quests_begin

lady_quests_begin_2 = "qst_blank_quest_16"
lady_quests_end_2   = "qst_blank_quest_16"

army_quests_begin = "qst_deliver_cattle_to_army"
army_quests_end   = lady_quests_begin

army_quests_begin_2 = "qst_blank_quest_21"
army_quests_end_2   = "qst_blank_quest_21"

tavernkeepers_quests_begin = "qst_hunted_down_bandits"
tavernkeepers_quests_end   = "qst_deal_with_forest_bandit"

player_realm_quests_begin = "qst_resolve_dispute"
player_realm_quests_end = "qst_blank_quest_1"

player_realm_quests_begin_2 = "qst_blank_quest_26"
player_realm_quests_end_2 = "qst_blank_quest_26"

all_items_begin = 0
all_items_end = "itm_items_end"

all_quests_begin = 0
all_quests_end = "qst_quests_end"

towns_begin = "p_town_1"
castles_begin = "p_castle_1"
villages_begin = "p_village_1"

towns_end = castles_begin
castles_end = villages_begin
villages_end   = "p_salt_mine"

walled_centers_begin = towns_begin
walled_centers_end   = castles_end

centers_begin = towns_begin
centers_end   = villages_end
merc_parties_begin = "p_town_merc_1"
merc_parties_end = "p_zendar"

training_grounds_begin   = "p_training_ground_1"
training_grounds_end     = "p_Bridge_1"

scenes_begin = "scn_town_1_center"
scenes_end = "scn_castle_1_exterior"

spawn_points_begin = "p_zendar"
spawn_points_end = "p_spawn_points_end"

regular_troops_begin       = "trp_novice_fighter"
regular_troops_end         = "trp_tournament_master"

swadian_merc_parties_begin = "p_town_1_mercs"
swadian_merc_parties_end   = "p_town_8_mercs"

vaegir_merc_parties_begin  = "p_town_8_mercs"
vaegir_merc_parties_end    = "p_zendar"

arena_masters_begin    = "trp_town_1_arena_master"
arena_masters_end      = "trp_town_1_armorer"

training_gound_trainers_begin    = "trp_trainer_1"
training_gound_trainers_end      = "trp_ransom_broker_1"

town_walkers_begin = "trp_town_walker_1"
town_walkers_end = "trp_village_walker_1"

village_walkers_begin = "trp_village_walker_1"
village_walkers_end   = "trp_spy_walker_1"

spy_walkers_begin = "trp_spy_walker_1"
spy_walkers_end = "trp_tournament_master"

walkers_begin = town_walkers_begin
walkers_end   = spy_walkers_end

armor_merchants_begin  = "trp_town_1_armorer"
armor_merchants_end    = "trp_town_1_weaponsmith"

weapon_merchants_begin = "trp_town_1_weaponsmith"
weapon_merchants_end   = "trp_town_1_tavernkeeper"

tavernkeepers_begin    = "trp_town_1_tavernkeeper"
tavernkeepers_end      = "trp_town_1_merchant"

goods_merchants_begin  = "trp_town_1_merchant"
goods_merchants_end    = "trp_town_1_horse_merchant"

horse_merchants_begin  = "trp_town_1_horse_merchant"
horse_merchants_end    = "trp_town_1_mayor"

mayors_begin           = "trp_town_1_mayor"
mayors_end             = "trp_village_1_elder"

village_elders_begin   = "trp_village_1_elder"
village_elders_end     = "trp_merchants_end"

startup_merchants_begin = "trp_swadian_merchant"
startup_merchants_end = "trp_startup_merchants_end"

outlaws_begin = "trp_looter"
outlaws_end   = "trp_kidnapped_girl"

rogues_begin = "trp_vampire_assassin"
rogues_end   = "trp_wight"

goblin_outlaws_begin = "trp_goblin"
goblin_outlaws_end   = "trp_ogre_young"

orc_outlaws_begin = "trp_orc"
orc_outlaws_end   = "trp_woodelf_recruit"

elf_outlaws_begin = "trp_woodelf_recruit"
elf_outlaws_end   = "trp_ent_1"

darkelf_outlaws_begin = "trp_dwarf_miner"
darkelf_outlaws_end   = "trp_giant_1"

saracen_outlaws_begin = "trp_ogre_young"
saracen_outlaws_end   = "trp_troll_1"

fugitives_begin = "trp_demon_magic_1"
fugitives_end = "trp_demon_human_5_1"

bounties_begin = "qst_bounty_1"
bounties_end   = "qst_hunted_down_bandits"

num_max_items = 10000 #used for multiplayer mode

average_price_factor = 1000
minimum_price_factor = 100
maximum_price_factor = 10000

village_prod_min = 0 #was -5
village_prod_max = 20 #was 20

trade_goods_begin = "itm_spice"
trade_goods_end = "itm_siege_supply"
food_begin = "itm_smoked_fish"
food_end = "itm_quest_wine"
reference_books_begin = "itm_book_wound_treatment_reference"
reference_books_end   = trade_goods_begin
readable_books_begin = "itm_book_tactics"
readable_books_end   = reference_books_begin
books_begin = readable_books_begin
books_end = reference_books_end
horses_begin = "itm_sumpter_horse"
horses_end = "itm_arrows"
weapons_begin = "itm_wooden_stick"
weapons_end = "itm_wooden_shield"
ranged_weapons_begin = "itm_darts"
ranged_weapons_end = "itm_torch"
armors_begin = "itm_leather_gloves"
armors_end = "itm_wooden_stick"
shields_begin = "itm_wooden_shield"
shields_end = ranged_weapons_begin

# Banner constants

custom_banner_charges_begin = "mesh_custom_banner_charge_01"
custom_banner_charges_end = "mesh_tableau_mesh_custom_banner"

custom_banner_backgrounds_begin = "mesh_custom_banner_bg"
custom_banner_backgrounds_end = custom_banner_charges_begin

custom_banner_flag_types_begin = "mesh_custom_banner_01"
custom_banner_flag_types_end = custom_banner_backgrounds_begin

custom_banner_flag_map_types_begin = "mesh_custom_map_banner_01"
custom_banner_flag_map_types_end = custom_banner_flag_types_begin

custom_banner_flag_scene_props_begin = "spr_custom_banner_01"
custom_banner_flag_scene_props_end = "spr_banner_a"

custom_banner_map_icons_begin = "icon_custom_banner_01"
custom_banner_map_icons_end = "icon_banner_01"


banner_meshes_begin = "mesh_banner_a01"
banner_meshes_end_minus_one = "mesh_banner_f21"

arms_meshes_begin = "mesh_arms_a01"
arms_meshes_end_minus_one = "mesh_arms_f21"

banner_map_icons_begin = "icon_banner_01"
banner_map_icons_end_minus_one = "icon_banner_136"

banner_scene_props_begin = "spr_banner_a"
banner_scene_props_end_minus_one = "spr_banner_f21"


kingdom_8_banners_begin_offset = 189
kingdom_8_banners_end_offset = 210

kingdom_4_banners_begin_offset = 84
kingdom_4_banners_end_offset = 105

kingdom_7_banners_begin_offset = 0
kingdom_7_banners_end_offset = 21

kingdom_10_banners_begin_offset = 21
kingdom_10_banners_end_offset = 42

kingdom_5_banners_begin_offset = 42
kingdom_5_banners_end_offset = 63

teu_banners_begin_offset = 231
teu_banners_end_offset = 251

khergit_banners_begin_offset = 63
khergit_banners_end_offset = 84

sarranid_banners_begin_offset = 105
sarranid_banners_end_offset = 125


banners_end_offset = 273

# Some constants for merchant invenotries
merchant_inventory_space = 30
num_merchandise_goods = 40

num_max_river_pirates = 25
num_max_zendar_peasants = 25
num_max_zendar_manhunters = 10

num_max_dp_bandits = 10
num_max_refugees = 10
num_max_deserters = 10

num_max_militia_bands = 15
num_max_armed_bands = 12

num_max_vaegir_punishing_parties = 20
num_max_rebel_peasants = 25

num_max_frightened_farmers = 50
num_max_undead_messengers  = 20

num_forest_bandit_spawn_points = 2
num_mountain_bandit_spawn_points = 2
num_steppe_bandit_spawn_points = 2
num_taiga_bandit_spawn_points = 2
num_desert_bandit_spawn_points = 2
num_sea_raider_spawn_points = 2
num_black_khergit_spawn_points = 1

peak_prisoner_trains = 4
peak_kingdom_caravans = 12
peak_kingdom_messengers = 3


# Note positions
note_troop_location = 3

#battle tactics
btactic_hold = 1
btactic_follow_leader = 2
btactic_charge = 3
btactic_stand_ground = 4
btactic_cav_charge = 5
#default right mouse menu orders
cmenu_move = -7
cmenu_follow = -6

# Town center modes - resets in game menus during the options
tcm_default 		= 0
tcm_disguised 		= 1
tcm_prison_break 	= 2
tcm_escape      	= 3


# Arena battle modes
#abm_fight = 0
abm_training = 1
abm_visit = 2
abm_tournament = 3

# Camp training modes
ctm_melee    = 1
ctm_ranged   = 2
ctm_mounted  = 3
ctm_training = 4

# Village bandits attack modes
vba_normal          = 1
vba_after_training  = 2

arena_tier1_opponents_to_beat = 3
arena_tier1_prize = 20
arena_tier2_opponents_to_beat = 6
arena_tier2_prize = 40
arena_tier3_opponents_to_beat = 10
arena_tier3_prize = 100
arena_tier4_opponents_to_beat = 20
arena_tier4_prize = 150
arena_tier5_opponents_to_beat = 40
arena_tier5_prize = 240
arena_grand_prize = 1000


#Additions
price_adjustment = 25 #the percent by which a trade at a center alters price

fire_duration = 4 #fires takes 4 hours

#NORMAL ACHIEVEMENTS
ACHIEVEMENT_NONE_SHALL_PASS = 1,
ACHIEVEMENT_MAN_EATER = 2,
ACHIEVEMENT_THE_HOLY_HAND_GRENADE = 3,
ACHIEVEMENT_LOOK_AT_THE_BONES = 4,
ACHIEVEMENT_KHAAAN = 5,
ACHIEVEMENT_GET_UP_STAND_UP = 6,
ACHIEVEMENT_BARON_GOT_BACK = 7,
ACHIEVEMENT_BEST_SERVED_COLD = 8,
ACHIEVEMENT_TRICK_SHOT = 9,
ACHIEVEMENT_GAMBIT = 10,
ACHIEVEMENT_OLD_SCHOOL_SNIPER = 11,
ACHIEVEMENT_CALRADIAN_ARMY_KNIFE = 12,
ACHIEVEMENT_MOUNTAIN_BLADE = 13,
ACHIEVEMENT_HOLY_DIVER = 14,
ACHIEVEMENT_FORCE_OF_NATURE = 15,

#SKILL RELATED ACHIEVEMENTS:
ACHIEVEMENT_BRING_OUT_YOUR_DEAD = 16,
ACHIEVEMENT_MIGHT_MAKES_RIGHT = 17,
ACHIEVEMENT_COMMUNITY_SERVICE = 18,
ACHIEVEMENT_AGILE_WARRIOR = 19,
ACHIEVEMENT_MELEE_MASTER = 20,
ACHIEVEMENT_DEXTEROUS_DASTARD = 21,
ACHIEVEMENT_MIND_ON_THE_MONEY = 22,
ACHIEVEMENT_ART_OF_WAR = 23,
ACHIEVEMENT_THE_RANGER = 24,
ACHIEVEMENT_TROJAN_BUNNY_MAKER = 25,

#MAP RELATED ACHIEVEMENTS:
ACHIEVEMENT_MIGRATING_COCONUTS = 26,
ACHIEVEMENT_HELP_HELP_IM_BEING_REPRESSED = 27,
ACHIEVEMENT_SARRANIDIAN_NIGHTS = 28,
ACHIEVEMENT_OLD_DIRTY_SCOUNDREL = 29,
ACHIEVEMENT_THE_BANDIT = 30,
ACHIEVEMENT_GOT_MILK = 31,
ACHIEVEMENT_SOLD_INTO_SLAVERY = 32,
ACHIEVEMENT_MEDIEVAL_TIMES = 33,
ACHIEVEMENT_GOOD_SAMARITAN = 34,
ACHIEVEMENT_MORALE_LEADER = 35,
ACHIEVEMENT_ABUNDANT_FEAST = 36,
ACHIEVEMENT_BOOK_WORM = 37,
ACHIEVEMENT_ROMANTIC_WARRIOR = 38,

#POLITICALLY ORIENTED ACHIEVEMENTS:
ACHIEVEMENT_HAPPILY_EVER_AFTER = 39,
ACHIEVEMENT_HEART_BREAKER = 40,
ACHIEVEMENT_AUTONOMOUS_COLLECTIVE = 41,
ACHIEVEMENT_I_DUB_THEE = 42,
ACHIEVEMENT_SASSY = 43,
ACHIEVEMENT_THE_GOLDEN_THRONE = 44,
ACHIEVEMENT_KNIGHTS_OF_THE_ROUND = 45,
ACHIEVEMENT_TALKING_HELPS = 46,
ACHIEVEMENT_KINGMAKER = 47,
ACHIEVEMENT_PUGNACIOUS_D = 48,
ACHIEVEMENT_GOLD_FARMER = 49,
ACHIEVEMENT_ROYALITY_PAYMENT = 50,
ACHIEVEMENT_MEDIEVAL_EMLAK = 51,
ACHIEVEMENT_CALRADIAN_TEA_PARTY = 52,
ACHIEVEMENT_MANIFEST_DESTINY = 53,
ACHIEVEMENT_CONCILIO_CALRADI = 54,
ACHIEVEMENT_VICTUM_SEQUENS = 55,

#MULTIPLAYER ACHIEVEMENTS:
ACHIEVEMENT_THIS_IS_OUR_LAND = 56,
ACHIEVEMENT_SPOIL_THE_CHARGE = 57,
ACHIEVEMENT_HARASSING_HORSEMAN = 58,
ACHIEVEMENT_THROWING_STAR = 59,
ACHIEVEMENT_SHISH_KEBAB = 60,
ACHIEVEMENT_RUIN_THE_RAID = 61,
ACHIEVEMENT_LAST_MAN_STANDING = 62,
ACHIEVEMENT_EVERY_BREATH_YOU_TAKE = 63,
ACHIEVEMENT_CHOPPY_CHOP_CHOP = 64,
ACHIEVEMENT_MACE_IN_YER_FACE = 65,
ACHIEVEMENT_THE_HUSCARL = 66,
ACHIEVEMENT_GLORIOUS_MOTHER_FACTION = 67,
ACHIEVEMENT_ELITE_WARRIOR = 68,

#COMBINED ACHIEVEMENTS
ACHIEVEMENT_SON_OF_ODIN = 69,
ACHIEVEMENT_KING_ARTHUR = 70,
ACHIEVEMENT_KASSAI_MASTER = 71,
ACHIEVEMENT_IRON_BEAR = 72,
ACHIEVEMENT_LEGENDARY_RASTAM = 73,
ACHIEVEMENT_SVAROG_THE_MIGHTY = 74,

ACHIEVEMENT_MEN_HANDLER = 75,
ACHIEVEMENT_GIRL_POWER = 76,
ACHIEVEMENT_QUEEN = 77,
ACHIEVEMENT_EMPRESS = 78,
ACHIEVEMENT_TALK_OF_THE_TOWN = 79,
ACHIEVEMENT_LADY_OF_THE_LAKE = 80,

## CC
# constants
#proficiency_limit_increase       = 120
#reinforcement_cost_player        = 800
reinforcement_cost_player        = reinforcement_cost_moderate
reinforcement_cost_player_hoseman        = 2400
reinforcement_cost_player_footman        = 1800
reinforcement_cost_player_archer         = 1200

armor_cloth                   = 1
armor_armor                   = 0
armor_plate                   = 2

wpn_setting                   = 1
armor_setting                 = 2
horse_setting                 = 3

king_titles_begin = "str_faction_king_title_1"
king_titles_female_begin = "str_faction_king_female_title_1"
banner_scene_props_back_begin = "spr_banner_a_back"
banner_scene_props_back_end_minus_one = "spr_banner_f21_back"




# item slots
#slot_item_weight                  = 66
#slot_weapon_proficiency           = 68
#slot_item_cant_on_horseback       = 70
#slot_item_best_modifier           = 73
#slot_item_flying_missile          = 74
#slot_item_two_hand_one_hand       = 75
#slot_item_head_armor              = 76
#slot_item_body_armor              = 77
#slot_item_leg_armor               = 78
#slot_item_length                  = 79
#slot_item_speed                   = 80
slot_item_voice_get       = slot_item_book_read               


slot_item_is_magic_spell               = 75
slot_item_magic_cost                   = 66
slot_item_magic_type                   = 68
slot_item_magic_cooldown               = 70
slot_item_magic_difficulty             = slot_item_intelligence_requirement
slot_item_magic_cast_time              = 73

voice    =  1
spell    =  2
quick_spell    =  3
buff    =  4

special_ability = 5
special_ability_extra = 6
special_ability_passive = 7
bash = 8
drink = 9
 

slot_item_special_given           = 65 


slot_armor_type                   = 67
slot_item_food_portion            = 81
slot_item_modifier_quality        = 69
slot_item_type_not_for_sell       = 71
slot_item_modifier_multiplier     = 72
slot_item_num_for_necro           = 73

#======special item begin======
slot_item_special = 82 
slot_item_skill_need_attribute_id = 83 
slot_item_skill_need_skill_id = 84 
slot_item_skill_need_proficiency_id = 85
slot_item_skill_need_attribute_value = 86 
slot_item_skill_need_skill_value = 87 
slot_item_skill_need_proficiency_value = 88
slot_item_skill_need_join_guild = 89
#======special item end====== 
join_mine_guild  =  1
join_mage_guild =  2
join_orc_guild =  3
join_hunt_guild =  4
join_necro_guild =  5
join_demon_guild =  6
join_thief_guild =  7
join_order_guild =  8
join_elf_guild =  9



#slot_item_unique                    = 89
#slot_item_needs_two_hands	       = 90
#slot_item_couchable                = 91
#slot_item_accuracy                  = 92
#slot_item_shoot_speed               = 93
#slot_item_pike                      = slot_item_shoot_speed
#slot_item_is_magic_staff            = slot_armor_type                   = 67

# slots hack
  #### Autoloot improved by rubik begin
#slot_item_thrust_damage      = slot_item_head_armor
#slot_item_swing_damage       = slot_item_body_armor

#slot_item_horse_speed        = slot_item_head_armor
#slot_item_horse_armor        = slot_item_body_armor
#slot_item_horse_charge       = slot_item_length
  #### Autoloot improved by rubik end

# party slots
slot_player_star_as_king     = slot_town_seneschal
slot_player_game_level     = slot_town_center

slot_town_recruit_gold  = 40
slot_town_last_recruit_time  = 43
slot_town_last_recruit_time_2  = 44

slot_center_tavern_mystic_merchant = 100
slot_center_bandit_leader_quest    = 102
slot_center_bandit_leader_pt_no    = 103

slot_town_recruit_gold_hoseman           = 301
slot_town_recruit_gold_footman           = 302
slot_town_recruit_gold_archer            = 303
slot_town_upgrade_troop                  = 304
slot_town_player_debt      = slot_party_last_toll_paid_hours
slot_town_player_debt_days = slot_village_smoke_added
slot_party_is_in_water              = 305 
slot_party_spawn_faction            = slot_village_player_can_not_steal_cattle = 46
slot_party_use_extra_hp     = slot_center_player_enterprise 
slot_party_horse_use_extra_hp     = slot_center_player_enterprise_production_order    = 138
slot_party_use_special_item       = slot_center_player_enterprise_consumption_order   = 139  
slot_party_horse_use_charge       = slot_center_player_enterprise_balance   = 140  
slot_party_agent_never_running_away    = slot_center_player_enterprise_input_price   = 141  
slot_party_is_in_siege              = slot_party_is_in_water 
slot_party_is_daytime              = slot_production_sources_end 

#chenwz_building
slot_center_has_manor            = 305 #village
slot_center_has_watch_tower      = 306 #village
slot_center_has_school           = 307 #village
slot_center_has_fish_pond        = 308 #village
slot_center_has_messenger_post   = 309 #town, castle, village

slot_center_has_prisoner_tower   = 310 #town, castle
slot_center_has_blacksmith       = 311 #town, castle

slot_center_has_barracks         = 312 #town, castle, village
slot_center_has_archery_range    = 313 #town, castle
slot_center_has_stables          = 314 #town, castle  



slot_center_has_barracks_t2         = 315 #town, castle
slot_center_has_barracks_t3         = 318 #town, castle
slot_center_has_archery_range_t2    = 316 #town, castle
slot_center_has_archery_range_t3    = 317 #town, castle
slot_center_has_stables_t2          = 319 #town, castle  
slot_center_has_stables_t3          = 320 #town, castle  

village_improvements_begin = slot_center_has_manor
village_improvements_end          = 313

walled_center_improvements_begin = slot_center_has_manor
walled_center_improvements_end               = 315

barracks_begin = slot_center_has_barracks
barracks_end               = 315

slot_center_constable_training               = 322 
slot_center_constable_training_type1         = 323 
slot_center_constable_training_type2         = 324 

#chenwz_building






# troop slots
###################################################################################
# AutoLoot: Modified Constants
# Most of these are slot definitions, make sure they do not clash with your mod's other slot usage
###################################################################################

# These are troops slots
#slot_upgrade_armor = 155
#slot_upgrade_horse = 156
#slot_upgrade_weapon = 157

#slot_upgrade_wpn_0 = 157
#slot_upgrade_wpn_1 = 158
#slot_upgrade_wpn_2 = 159
#slot_upgrade_wpn_3 = 160



## CC

slot_upgrade_wpn_1_set_2  = 430
slot_upgrade_wpn_2_set_2  = 431
slot_upgrade_wpn_3_set_2  = 432
slot_upgrade_wpn_4_set_2  = 433

slot_upgrade_wpn_1  = 434
slot_upgrade_wpn_2  = 435
slot_upgrade_wpn_3  = 436
slot_upgrade_wpn_4  = 437

slot_upgrade_head   = 438
slot_upgrade_body   = 439
slot_upgrade_foot   = 440
slot_upgrade_hand   = 441

slot_upgrade_horse  = 442

slot_2nd_weapons_1             = 443
slot_2nd_weapons_2             = 444
slot_2nd_weapons_3             = 445
slot_2nd_weapons_4             = 446
slot_troop_weapons_set_no      = 447

## CC
###################################################################################
# End Autoloot
###################################################################################

kt_slot_troop_o_val           = 85
kt_slot_troop_d_val           = 86
kt_slot_troop_wage            = 87
kt_slot_troop_h_val           = 88
kt_slot_troop_r_val           = 89
slot_troop_cur_xp_for_wp      = 88
slot_troop_xp_limit_for_wp    = 89
slot_troop_kill_count         = 90
slot_troop_wound_count        = 91

slot_troop_job          = 92
slot_troop_2nd_job      = 93


slot_troop_current_reading_book = 94
slot_troop_commensalism_troop   = 95

slot_troop_hero_pt_a            = 96
slot_troop_hero_pt_b            = 97
slot_troop_hero_pt_c            = 98
slot_troop_hero_pt_d            = 99

slot_troop_last_recruit_time        = slot_troop_commensalism_troop

slot_troop_size                                = slot_troop_hero_pt_a
slot_troop_num_wounded                         = slot_troop_hero_pt_b
slot_troop_num_killed                          = slot_troop_hero_pt_c
slot_troop_num_routed                          = slot_troop_hero_pt_d

slot_player_reward_item                        = slot_troop_hero_pt_a
slot_player_reward_item_imod                   = slot_troop_hero_pt_b
slot_troop_upgrade_times                       = 94

slot_troop_upgrade_1            = 100

slot_troop_upgrade_freelance            = 101

slot_troop_special_troop = 57
slot_troop_special_troop_limit = 58

slot_troop_max_hp                       = 99

slot_troop_followers                           = 103
slot_troop_followers_size                      = 104

slot_troop_spell_1                             = 166
slot_troop_spell_2                             = 167
slot_troop_spell_3                             = 168
slot_troop_spell_4                             = 169
slot_troop_special_ability                     = 170
slot_troop_special_ability_extra               = 171
slot_troop_special_ability_passive             = 172
slot_troop_has_bash                            = 173
slot_troop_has_drink                           = 174
slot_troop_spell_end                           = slot_troop_special_ability

bookcase_troops_begin = "trp_bookcase_spell"
bookcase_troops_end_minus_one = "trp_bookcase_drink"
bookcase_troops_end = "trp_trainer_1"



slot_troop_upgrade_knight_days = slot_troop_first_encountered
slot_troop_upgrade_knight_item = slot_troop_home


slot_troop_contribution = slot_troop_wealth
slot_troop_player_soul_point              = 102

slot_troop_player_effect              = 103
slot_troop_player_class               = 104


wrath = "itm_skill_wrath"
berserk = "itm_skill_berserk"
frenzy = "itm_skill_frenzy"
awaken = "itm_skill_awaken"
skill_charge = "itm_skill_charge"
holy_light = "itm_skill_holy_light"
divine_ruling = "itm_skill_divine_ruling"
revelation = "itm_skill_revelation"
inspire = "itm_skill_inspire"
warcry = "itm_skill_warcry"
taunt = "itm_skill_taunt"
insight = "itm_skill_insight"
focus = "itm_skill_focus"
ambush = "itm_skill_ambush"
windforce = "itm_skill_windforce"
master_archer = "itm_skill_master_archer"
arrow_of_slaying = "itm_skill_arrow_of_slaying"
haste_reload = "itm_skill_haste_reload"
battlecry = "itm_skill_battlecry"
shadowstep = "itm_skill_shadowstep"
shadow_blade = "itm_skill_shadow_blade"
force_jump = "itm_skill_fly"
ironshield = "itm_skill_ironshield"
rush = "itm_skill_rush"
powercharge = "itm_skill_powercharge"
fright_aura = "itm_skill_fright_aura"
hero_dreams = "itm_skill_hero_dreams"
charm = "itm_skill_charm"
bubble_dreams = "itm_skill_bubble_dreams"
battlerage = "itm_skill_battlerage"
cleave = "itm_skill_cleave"
deadly_strike = "itm_skill_deadly_strike"
fear_attack = "itm_skill_fear_attack"
rend = "itm_skill_rend"
wound_strike = "itm_skill_wound_strike"
power_strike = "itm_skill_power_strike"
cull_the_weak = "itm_skill_cull_the_weak"
bloodlust = "itm_skill_bloodlust"
khorne_blessing = "itm_skill_khorne_blessing"
Khorne_blessing = "itm_skill_khorne_blessing"
mana_burn = "itm_skill_mana_burn"
mark_of_khorne = "itm_skill_mark_of_khorne"
nurgle_blessing = "itm_skill_nurgle_blessing"
Nurgle_blessing = "itm_skill_nurgle_blessing"
curse_of_the_leper = "itm_skill_curse_of_the_leper"
poisoned_attacks = "itm_skill_poisoned_attacks"
tzeentch_arcane = "itm_skill_tzeentch_arcane"
mana_burst = "itm_skill_mana_burst"
diffusal_blade = "itm_skill_diffusal_blade"
master_of_ice = "itm_skill_master_of_ice"
call_storm = "itm_skill_call_storm"
master_of_storms = "itm_skill_master_of_storms"
master_of_fire = "itm_skill_master_of_fire"
spirit_link = "itm_skill_spirit_link"
confession = "itm_skill_confession" 
Confession = "itm_skill_confession" 
summon_undead = "itm_skill_summon_undead"
summon_neutral = "itm_skill_summon_neutral"
summon_demon = "itm_skill_summon_demon"
summon_hallow = "itm_skill_summon_hallow"

dive = "itm_skill_dive"
flamestrike = "itm_skill_flamestrike"
flameswave = "itm_skill_flameswave"
call_lightning = "itm_skill_call_lightning"
lightning_attack = "itm_skill_lightning_attack"
mummy_curse = "itm_skill_mummy_curse"
shadowking = "itm_skill_shadowking"
mummy = "itm_skill_mummy"
block = "itm_skill_block"
roll = "itm_skill_roll"
ground_stomp = "itm_skill_ground_stomp"
seismic_slam = "itm_skill_seismic_slam"
power_cleave = "itm_skill_power_cleave"
counterstrike = "itm_skill_counter_strike"
life_drain = "itm_skill_life_drain"
smite_evil = "itm_skill_smite_evil"
bane_evil = "itm_skill_bane_evil" 
smite_undead = "itm_skill_smite_undead"
bane_undead = "itm_skill_bane_undead" 
smite_orc = "itm_skill_smite_orc"
bane_orc = "itm_skill_bane_orc" 
head_hunted = "itm_skill_head_hunted" 
smite_human = "itm_skill_smite_human" 
smite_outsider = "itm_skill_smite_outsider"
bane_outsider = "itm_skill_bane_outsider" 

skeletal = "itm_skill_skeletal"
entangle = "itm_skill_entangle"
rage_strike = "itm_skill_rage_strike"
rage_charge = "itm_skill_rage_charge"
sinper_shot = "itm_skill_sinper_shot"
steady_aim = "itm_skill_steady_aim"
grasp = "itm_skill_grasp"
divine_strength = "itm_skill_divine_strength"
weakness = "itm_skill_weakness"
mass_slow = "itm_skill_mass_slow"
slow = "itm_skill_slow"
mass_haste = "itm_skill_mass_haste"
haste = "itm_skill_haste"
regeneration = "itm_skill_regeneration"
stoneskin = "itm_skill_stoneskin"
dragons_fear = "itm_skill_dragons_fear"
spell_dispel = "itm_skill_spell_dispel"
dragron_flame_burst = "itm_skill_dragron_flame_burst"
flame_burst = "itm_skill_flame_burst"
forst_ring = "itm_skill_forst_ring"
power_blade = "itm_skill_power_blade"
earth_shock = "itm_skill_earth_shock"
heal = "itm_skill_heal"
mass_heal = "itm_skill_mass_heal"
reaper = "itm_skill_reaper"
smite_life = "itm_skill_smite_life"
it_is_high_noon = "itm_skill_it_is_high_noon"
sidearm_1 = "itm_skill_sidearm_1" 
sidearm_2 = "itm_skill_sidearm_2" 
sidearm = "itm_skill_sidearm_2" 
luanwu = "itm_skill_luanwu"
wushuang = "itm_skill_wushuang"
undead_horse = "itm_skill_undead_horse"
retribution = "itm_skill_retribution"
magic_mirror = "itm_skill_magic_mirror"
fire_shield = "itm_skill_fire_shield"
meditation = "itm_skill_meditation"
counter = "itm_skill_counter"
dragon_voice = "itm_skill_dragon_voice"
avatar = "itm_skill_avatar"
multishot = "itm_skill_multishot"
dragon_blade = "itm_skill_dragon_blade_slash"
swift_strike = "itm_skill_swift_strike"
deflect = "itm_skill_deflect"
omnislash = "itm_skill_omnislash"
oneshot = "itm_skill_oneshot"
autoshot = "itm_skill_autoshot"

bash_oneshot = "itm_bash_oneshot"
bash_shadow_blade = "itm_bash_shadow_blade"
bash_rush = "itm_bash_rush"
bash_cleave = "itm_bash_cleave"
bash_power_strike = "itm_bash_power_strike"
bash_roll = "itm_bash_roll"
bash_seismic_slam = "itm_bash_seismic_slam"
bash_earth_shock = "itm_bash_earth_shock"
bash_flame_burst = "itm_bash_flame_burst"
bash_forst_ring = "itm_bash_forst_ring"
bash_grasp = "itm_bash_grasp"
bash_summon_undead = "itm_bash_summon_undead"

bash_swift_strike = "itm_bash_swift_strike"
bash_sidearm_1 = "itm_bash_sidearm_1"
bash_shield_bash = "itm_bash_shield_bash"
bash_kick = "itm_bash_kick"
bash_heal = "itm_bash_heal"
bash_mass_heal = "itm_bash_mass_heal"



#slot_all_proficiency_limit        = 336
#slot_one_handed_proficiency_limit = 337
#slot_two_handed_proficiency_limit = 338
#slot_polearm_proficiency_limit    = 339
#slot_archery_proficiency_limit    = 340
#slot_crossbow_proficiency_limit   = 341
#slot_throwing_proficiency_limit   = 342

#======special item begin======
#======special item end====== 

## CC

##diplomacy begin 
# recruiter kit begin
dplmc_slot_party_recruiter_needed_recruits = 233           # Amount of recruits the employer ordered.
dplmc_slot_party_recruiter_origin = 234                    # Walled center from where the recruiter was hired.
dplmc_slot_village_reserved_by_recruiter = 235            # This prevents recruiters from going to villages targeted by other recruiters.
dplmc_slot_party_recruiter_needed_recruits_faction = 236   # Alkhadias Master, you forgot this one from the PM you sent me :D
dplmc_slot_party_recruiter_recruitment_type = 237
# recruiter kit end

recruitment_cost_village = 20
recruitment_cost_town = 50
recruitment_cost_castle = 500


###################################################################################
# End Autoloot
###################################################################################

dplmc_npc_mission_war_request                 = 9
dplmc_npc_mission_alliance_request            = 10
dplmc_npc_mission_spy_request                 = 11
dplmc_npc_mission_gift_fief_request           = 12
dplmc_npc_mission_gift_horses_request         = 13
dplmc_npc_mission_threaten_request            = 14
dplmc_npc_mission_prisoner_exchange           = 15
dplmc_npc_mission_defensive_request           = 16
dplmc_npc_mission_trade_request               = 17
dplmc_npc_mission_nonaggression_request       = 18
dplmc_npc_mission_persuasion                  = 19
dplmc_slot_troop_mission_diplomacy            = 162
dplmc_slot_troop_mission_diplomacy2           = 163
dplmc_slot_troop_political_stance             = 164
dplmc_slot_troop_affiliated                   = 165
dplmc_slot_center_taxation                    = slot_party_next_looted_item_slot
dplmc_slot_party_mission_diplomacy            = slot_party_looted_item_1

##diplomacy end 


## Prebattle Orders & Deployment Begin
max_battle_size = 1000 #RESET if you've modded the battlesize
skirmish_min_distance = 1500 #Min distance you wish maintained, in cm. Where agent will retreat
skirmish_max_distance = 2500 #Max distance to maintain, in cm. Where agent will stop retreating

slot_party_pbod_mod_version           = 46  #slot_village_player_can_not_steal_cattle
#Deployment

slot_troop_prebattle_first_round      = 37  #slot_lady_no_messages 
#slot_troop_prebattle_array            = 38  #slot_lady_last_suitor 
slot_troop_prebattle_num_upgrade      = 52  #slot_lord_reputation_type  
slot_troop_prebattle_preupgrade_check = 39  #slot_troop_betrothal_time   
slot_party_prebattle_customized_deployment = 47  #slot_center_accumulated_rents  
slot_party_prebattle_battle_size           = 48  #slot_center_accumulated_tariffs 
slot_party_prebattle_size_in_battle        = 49  #slot_town_wealth  
slot_party_prebattle_in_battle_count       = 50  #slot_town_prosperity
#Split Divisions
slot_party_prebattle_customized_divisions  = 51  #slot_town_player_odds 
slot_party_reinforcement_stage 		       = 107 #for main_party_backup
slot_troop_prebattle_alt_division          = 48  #slot_troop_set_decision_seed
slot_troop_prebattle_alt_division_percent  = 49  #slot_troop_temp_decision_seed 
slot_troop_prebattle_alt_division_amount   = 50  #slot_troop_recruitment_random 
#Troop slots--for soldiers (non-heros, non-lords, non-player) only
#Party slots--for the main party and main party backup only
#Orders
slot_party_prebattle_plan                  = 231 #slot_center_shipyards
slot_party_prebattle_num_orders            = 232 #slot_center_household_gardens 
slot_party_prebattle_order_array_begin     = 250 #slot_town_trade_good_prices_begin 
#Party slots--for the main party only--up to 290 used in this version
#reg()s from 15-45 used in this version (only during order presentation)
slot_team_d0_order_weapon     = 300 #plus 8 more for the other divisions
slot_team_d0_order_shield     = 309 #plus 8 more for the other divisions
slot_team_d0_order_skirmish   = 318 #plus 8 more for the other divisions
slot_team_d0_order_volley     = 327 #plus 8 more for the other divisions
slot_team_d0_order_sp_brace   = 336 #plus 8 more for the other divisions

slot_team_d0_formation_to_resume = 350

slot_party_pref_prefs_set    = 72
slot_party_pref_div_dehorse  = slot_town_village_product         #76
slot_party_pref_div_no_ammo  = slot_town_rebellion_readiness     #77
slot_party_pref_wu_lance     = slot_town_arena_melee_mission_tpl #78
slot_party_pref_wu_harcher   = slot_town_arena_torny_mission_tpl #79
slot_party_pref_wu_spear     = slot_town_arena_melee_1_num_teams #80
slot_party_pref_dmg_tweaks   = slot_town_arena_melee_1_team_size #81
slot_party_pref_spear_brace  = slot_town_arena_melee_2_num_teams #82
slot_party_pref_formations   = slot_town_arena_melee_2_team_size #83
slot_party_pref_bodyguard    = slot_town_arena_melee_3_num_teams #84
slot_party_pref_bc_continue  = slot_town_arena_melee_3_team_size #85
slot_party_pref_bc_charge_ko = slot_town_arena_melee_cur_tier    #86
slot_party_gk_order          = 108
slot_party_gk_order_hold_over_there = slot_party_gk_order #for party #2 at the moment




password  = 903509640

two_handed_wp           = 39
pike_wp                 = 40
spear_wp                = 41
one_handed_wp           = 42
lance_wp                = 42
footbow                 = 43
horsebow                = 44

ranged    = 0
onehand   = 1
twohands  = 2
polearm   = 3
shield    = 4
noshield  = 5
free      = 6 #shield
clear     = -1
begin     = 1
end       = 0
from header_triggers import *
keys_list = [ 
              ("$key_camera_forward",key_up),
              ("$key_camera_backward",key_down),
              ("$key_camera_left", key_left),
              ("$key_camera_right", key_right),
              ("$key_camera_zoom_plus",key_numpad_plus),     #Num + to zoom in
              ("$key_camera_zoom_min",key_numpad_minus),     #Num - to zoom out
              ("$key_camera_next",key_z),    #right key to jump to next bot
              ("$key_camera_prev",key_x),   #left key to jump to prev bot
              ("$key_camera_toggle",key_end),                #END button to toggle camera mode
              ("$key_order_7", key_f7),
              ("$key_order_8", key_f8),
              ("$key_order_9", key_f9),
              ("$key_order_10", key_f10),
              ("$key_special_0", key_v), #Pike Bracingkey_left_alt
              ("$key_special_1", key_h), #Whistle for Horse 			 
              ("$key_special_2", key_q),
              ("$key_special_3", key_left_control), 
              ("$key_special_4", key_left_alt),
              ("$key_special_5", key_right_mouse_button),
              
              ("$key_special_6", key_b),
              ("$key_special_7", key_mouse_scroll_up),
              ("$key_special_8", key_mouse_scroll_down),
              
              
			]
#--------------------------------------------------
             
all_keys_list   = [ 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x1e, 0x30, 0x2e, 0x20, 0x12, 0x21, 0x22, 0x23, 0x17, 0x24,
                    0x25, 0x26, 0x32, 0x31, 0x18, 0x19, 0x10, 0x13, 0x1f, 0x14, 0x16, 0x2f, 0x11, 0x2d, 0x15, 0x2c, 0x52, 0x4f, 0x50, 0x51, 
                    0x4b, 0x4c, 0x4d, 0x47, 0x48, 0x49, 0x45, 0xb5, 0x37, 0x4a, 0x4e, 0x9c, 0x53, 0xd2, 0xd3, 0xc7, 0xcf, 0xc9, 0xd1, 0xc8, 
                    0xd0, 0xcb, 0xcd, 0x3b, 0x3c, 0x3d, 0x3e, 0x3f, 0x40, 0x41, 0x42, 0x43, 0x44, 0x57, 0x58, 0x39, 0x1c, 0x0f, 0x0e, 0x1a, 
                    0x1b, 0x33, 0x34, 0x35, 0x2b, 0x0d, 0x0c, 0x27, 0x28, 0x29, 0x3a, 0x2a, 0x36, 0x1d, 0x9d, 0x38, 0xb8, 0xe0, 0xe1, 0xe2, 
                    0xe3, 0xe4, 0xe5, 0xe6, 0xe7, 0xee, 0xef, ]

number_of_keys            = len(keys_list)
number_of_all_keys        = len(all_keys_list)
two_columns_limit         = 20

slot_default_keys_begin   = 0
slot_keys_begin           = slot_default_keys_begin + number_of_keys
slot_key_overlay_begin    = slot_keys_begin         + number_of_keys
slot_key_defs_begin       = slot_key_overlay_begin  + number_of_keys + number_of_keys

key_config_data = "trp_temp_array_c" #"trp_key_config"
key_names_begin = "str_key_no1"
key_label_begin = "str_0x02"
#-- Dunde's Key Config END

## Prebattle Orders & Deployment End

slot_troop_freelancer_start_xp   =  slot_troop_signup   #110 -only used for player
slot_troop_freelancer_start_date =  slot_troop_signup_2 #111 -only used for player


slot_party_orig_morale = slot_party_ai_rationale
slot_freelancer_equip_start = 100 #only used for freelancer_party_backup

slot_current_version = 1

begin_wealth_reward_for_adventurer = 15000
adventurer_join_faction_renown = 500
adventurer_budget_gold = 10000
least_adventurer_budget_gold = 10050 #use for recruitment

adventurer_join_player_relation = 0
adventurer_renown_gain = 20
adventurer_trade_gold = 3000
adventurer_recruit_member_number = 11 #Use for recruitment, per members for second

party_mission_recruit = 1
party_mission_tournament = 2
party_mission_patrol = 3
party_mission_sell_inventory_item = 4
party_mission_trade = 5
party_mission_join_faction = 6

party_mission_attack_party = 7
party_mission_besieging_center = 8
party_mission_feast = 9

slot_party_had_mission               = 43
slot_party_last_recruit_time         = 44
slot_troop_is_use               = slot_troop_cur_xp_for_wp      = 88
slot_troop_prisoner_time        = slot_troop_xp_limit_for_wp    = 89
slot_troop_last_recruit_hero_time         = slot_troop_player_relation

slot_party_is_hunting = 351 #HUNTING MOD ADD RAMARAUNT 1 = hunting 2 = poaching
slot_party_hunting_time = 352 #HUNTING MOD ADD RAMARAUNT end time of hunt
slot_party_hunting_land = 353 #HUNTING MOD ADD RAMARAUNT land hunting in
slot_party_hunting_found = 354 #HUNTING MOD ADD RAMARAUNT animal type found 1 = deer 2 = boar 3 = unicorn
slot_party_hunting_amount = 355 #HUNTING MOD ADD RAMARAUNT animal amount found

game_mode_basic     = 0
game_mode_heroes    = 1

game_mode_greatwar   = 3
game_mode_chaos      = 4
game_mode_invasion   = 5
game_mode_0808       = 6

custom_caravan_masters_begin = "trp_caravan_master_01"
custom_caravan_masters_end = "trp_caravan_masters_end"


first_names_begin = "str_first_name_1"
first_names_end = "str_first_name_end"
male_names_begin = "str_male_name_1"
male_names_end = "str_male_name_end"
female_names_begin = "str_female_name_1"
female_names_end = "str_female_name_end"

# modmerger_start version=201 type=1
try:
    from util_common import logger
    from modmerger_options import mods_active
    modcomp_name = "constants"
    for mod_name in mods_active:
        try:
            logger.info("Importing constants from mod \"%s\"..."%(mod_name))
            code = "from %s_constants import *" % mod_name
            exec code
        except ImportError:
            errstring = "Component \"%s\" not found for mod \"%s\"." % (modcomp_name, mod_name)
            logger.debug(errstring)
except:
    raise
# modmerger_end
