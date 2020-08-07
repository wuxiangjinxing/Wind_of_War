from header_skins import *
from ID_particle_systems import *
####################################################################################################################
#  Each skin record contains the following fields:
#  1) Skin id: used for referencing skins.
#  2) Skin flags. Not used yet. Should be 0.
#  3) Body mesh.
#  4) Calf mesh (left one).
#  5) Hand mesh (left one).
#  6) Head mesh.
#  7) Face keys (list)
#  8) List of hair meshes.
#  9) List of beard meshes.
# 10) List of hair textures.
# 11) List of beard textures.
# 12) List of face textures.
# 13) List of voices.
# 14) Skeleton name
# 15) Scale (doesn't fully work yet)
# 16) Blood particles 1 (do not add this if you wish to use the default particles)
# 17) Blood particles 2 (do not add this if you wish to use the default particles)
# 17) Face key constraints (do not add this if you do not wish to use it)
####################################################################################################################

man_face_keys = [
(240,0,-0.4,0.3, "Chin Size"), 
(230,0,-0.4,0.8, "Chin Shape"), 
(250,0,-0.25,0.55, "Chin Forward"), 
(130,0,-0.5,1.0, "Jaw Width"),
(120,0,-0.5,0.6, "Lower Lip"),
(110,0,-0.2,0.6, "Upper Lip"),
(100,0,0.2,-0.2, "Mouth-Nose Distance"),
(90,0,0.55,-0.55, "Mouth Width"),

(30,0,-0.3,0.3, "Nostril Size"),
(60,0,0.25,-0.25, "Nose Height"),
(40,0,-0.2,0.3, "Nose Width"),
(70,0,-0.3,0.4, "Nose Size"),
(50,0,0.2,-0.3, "Nose Shape"),
(80,0,-0.3,0.65, "Nose Bridge"),

(160,0,-0.2,0.25, "Eye Width"),
(190,0,-0.25,0.15, "Eye to Eye Dist"),
(170,0,-0.85,0.85, "Eye Shape"),
(200,0,-0.3,0.7, "Eye Depth"),
(180,0,-1.5,1.5, "Eyelids"),

(20,0,0.6,-0.25, "Cheeks"),
(260,0,-0.6,0.5, "Cheek Bones"),
(220,0,0.8,-0.8, "Eyebrow Height"),
(210,0,-0.75,0.75, "Eyebrow Shape"),
(10,0,-0.6,0.5, "Temple Width"),

(270,0,-0.3,1.0, "Face Depth"),
(150,0,-0.25,0.45, "Face Ratio"),
(140,0,-0.4,0.5, "Face Width"),

(280,0,1.0,1.0, "Post-Edit"),
]
# Face width-Jaw width Temple width
woman_face_keys = [
(230,0,0.7,-0.7, "Chin Size"), 
(220,0,-0.6,0.6, "Chin Shape"), 
(10,0,-0.5,0.5, "Chin Forward"),
(20,0,-0.5,0.6, "Jaw Width"), 
(40,0,-0.7,0.7, "Jaw Position"),
(90,0,-1.2,1.2, "Jaw Neck"),
(50,0,-0.8,0.8, "Cheeks 2"),
(210,0,-0.5,0.5, "Cheeks 1"),
(100,0,-0.8,0.8, "Cheek Bones"),
(270,0,0.8,-0.8, "Mouth-Nose Distance"),
(30,0,-0.6,1.0, "Mouth Width"),
(160,0,1.0,-0.7, "Lips Position"),

(60,0,-0.5,0.5, "Nose Height"),
(70,0,-0.7,0.7, "Nose Width"),
(80,0,0.5,-1.0, "Nose Size"),
(240,0,-0.5,0.5, "Nose Shape"),

(150,0,-0.8,0.8, "Eye Width"),
(110,0,0.5,-0.5, "Eye to Eye Dist"),
(120,0,-0.7,0.8, "Eye Shape"),
(130,0,-1.0,0.7, "Eye Position"),
(140,0,-1.0,1.0, "Eyelids"),

(170,0,-0.7,0.7, "Eyebrow Height"),
(180,0,-1.0,0.7, "Eyebrow Shape"),
(260,0,0.8,-0.8, "Temple Width"),

(200,0,0.7,-0.7, "Face tall-short"),
(250,0,0.8,-0.8, "Face up-down"),
(190,0,-0.6,1.0, "Face Width"),

(280,0,0.0,0.7, "Post-Edit"),
]
undead_face_keys = []


male_elf_face_keys = [
(20,0, 0.7,-0.6, "Chin Size"),
(260,0, -0.6,1.4, "Chin Shape"),
(10,0,-0.5,0.9, "Chin Forward"),
(240,0,0.9,-0.8, "Jaw Width"),
(210,0,-0.5,1.0, "Jaw Position"),
(250,0,0.8,-1.0, "Mouth-Nose Distance"),
(200,0,-0.3,1.0, "Mouth Width"),
(50,0,-1.5,1.0, "Cheeks"),

(60,0,-0.4,1.35, "Nose Height"),
(70,0,-0.6,0.7, "Nose Width"),
(80,0,1.0,-0.1, "Nose Size"),
(270,0,-0.5,1.0, "Nose Shape"),
(90,0,-0.2,1.4, "Nose Bridge"),

(100,0,-0.3,1.0, "Cheek Bones"),
(150,0,-0.2,1.0, "Eye Width"),
(110,0,1.0,-0.8, "Eye to Eye Dist"),
(120,0,0.2,-1.0, "Eye Shape"),
(130,0,-0.5, 0.5, "Eye Depth"),
(140,0,1.0,-0.1, "Eyelids"),

(160,0,1.0,-0.2, "Eyebrow Position"),
(170,0,-0.1,1.0, "Eyebrow Height"),
(220,0,-0.1,0.9, "Eyebrow Depth"),
(180,0,-1.0,1.0, "Eyebrow Shape"),
(230,0,1.2,-0.7, "Temple Width"),

(30,0,-0.6,0.9, "Face Depth"),
(40,0,0.2,-0.8, "Face Ratio"),
(190,0,0.0,0.95, "Face Width"),

(280,0,-1.0,1.0, "Post-Edit"), 
]

elf_face_keys = [
(20,0, 0.7,-0.6, "Chin Size"),
(260,0, -0.6,1.4, "Chin Shape"),
(10,0,-0.5,0.9, "Chin Forward"),
(240,0,0.9,-0.3, "Jaw Width"),
(210,0,-0.5,0.5, "Jaw Position"),
(250,0,0.8,-1.0, "Mouth-Nose Distance"),
(200,0,-0.3,0.4, "Mouth Width"),
(50,0,-1.5,0.5, "Cheeks"),

(60,0,-0.4,1.35, "Nose Height"),
(70,0,-0.6,-0.2, "Nose Width"),
(80,0,1.0,0.2, "Nose Size"),
(270,0,-0.5,1.0, "Nose Shape"),
(90,0,-0.2,1.4, "Nose Bridge"),

(100,0,-0.3,1.5, "Cheek Bones"),
(150,0,-0.2,3.0, "Eye Width"),
(110,0,1.1,-0.5, "Eye to Eye Dist"),
(120,0,0.9,-1.0, "Eye Shape"),
(130,0,-0.5, 1.1, "Eye Depth"),
(140,0,1.0,-1.2, "Eyelids"),

(160,0,1.0,-0.2, "Eyebrow Position"),
(170,0,-0.1,1.9, "Eyebrow Height"),
(220,0,-0.1,0.9, "Eyebrow Depth"),
(180,0,-0.5,1.6, "Eyebrow Shape"),
(230,0,1.2,-0.7, "Temple Width"),

(30,0,-0.6,0.9, "Face Depth"),
(40,0,0.9,-0.6, "Face Ratio"),
(190,0,0.0,0.95, "Face Width"),

(280,0,0.0,1.0, "Post-Edit"),
]
# Face width-Jaw width Temple width
female_elf_face_keys = [
(230,0,0.8,-1.0, "Chin Size"), 
(220,0,-1.0,1.0, "Chin Shape"), 
(10,0,-1.2,1.0, "Chin Forward"),
(20,0, -0.6, 1.2, "Jaw Width"), 
(40,0,-0.7,1.0, "Jaw Position"),
(270,0,0.9,-0.9, "Mouth-Nose Distance"),
(30,0,-0.5,1.0, "Mouth Width"),
(50,0, -0.5,1.0, "Cheeks"),

(60,0,-0.5,1.0, "Nose Height"),
(70,0,-0.5,1.1, "Nose Width"),
(80,0,1.5,-0.3, "Nose Size"),
(240,0,-1.0,0.8, "Nose Shape"),
(90,0, 0.0,1.1, "Nose Bridge"),

(100,0,-0.5,1.5, "Cheek Bones"),
(150,0,-0.4,1.0, "Eye Width"),
(110,0,1.0,0.0, "Eye to Eye Dist"),
(120,0,-0.2,1.0, "Eye Shape"),
(130,0,-0.1,1.6, "Eye Depth"),
(140,0,-0.2,1.0, "Eyelids"),


(160,0,-0.2,1.2, "Eyebrow Position"),
(170,0,-0.2,0.7, "Eyebrow Height"),
(250,0,-0.4,0.9, "Eyebrow Depth"),
(180,0,-1.5,1.2, "Eyebrow Shape"),
(260,0,1.0,-0.7, "Temple Width"),

(200,0,-0.5,1.0, "Face Depth"),
(210,0,-0.5,0.9, "Face Ratio"),
(190,0,-0.4,0.8, "Face Width"),

(280,0,0.0,1.0, "Post-Edit"),
]

blackhorn_org_face_keys = [
(20,0, 0.7,-0.6, "Chin Size"),
(260,0, -0.6,1.4, "Chin Shape"),
(10,0,-0.5,0.9, "Chin Forward"),
(240,0,0.9,-0.8, "Jaw Width"),
(210,0,-0.5,1.0, "Jaw Position"),
(250,0,0.8,-1.0, "Mouth-Nose Distance"),
(200,0,-0.3,1.0, "Mouth Width"),
(50,0,-1.5,1.0, "Cheeks"),

(60,0,-0.4,1.35, "Nose Height"),
(70,0,-0.6,0.7, "Nose Width"),
(80,0,1.0,-0.1, "Nose Size"),
(270,0,-0.5,1.0, "Nose Shape"),
(90,0,-0.2,1.4, "Nose Bridge"),

(100,0,-0.3,1.5, "Cheek Bones"),
(150,0,-0.2,3.0, "Eye Width"),
(110,0,1.5,-0.9, "Eye to Eye Dist"),
(120,0,1.9,-1.0, "Eye Shape"),
(130,0,-0.5, 1.1, "Eye Depth"),
(140,0,1.0,-1.2, "Eyelids"),

(160,0,1.3,-0.2, "Eyebrow Position"),
(170,0,-0.1,1.9, "Eyebrow Height"),
(220,0,-0.1,0.9, "Eyebrow Depth"),
(180,0,-1.1,1.6, "Eyebrow Shape"),
(230,0,1.2,-0.7, "Temple Width"),

(30,0,-0.6,0.9, "Face Depth"),
(40,0,0.9,-0.6, "Face Ratio"),
(190,0,0.0,0.95, "Face Width"),

(280,0,0.0,1.0, "Post-Edit"),
]

woman_face_keys_2 = [
(40, 0, -1, 1, "caucas_kelb"), 
(30, 0, 0, 1, "caucas_std"), 
(10, 0, 0, 1, "Forehead"),
(280,0,0.0,1.0, "Post-Edit"),
]

chin_size = 0
chin_shape = 1
chin_forward = 2
jaw_width = 3
jaw_position = 4
mouth_nose_distance = 5
mouth_width = 6
cheeks = 7
nose_height = 8
nose_width = 9
nose_size = 10
nose_shape = 11
nose_bridge = 12
cheek_bones = 13
eye_width = 14
eye_to_eye_dist = 15
eye_shape = 16
eye_depth = 17
eyelids = 18
eyebrow_position = 19
eyebrow_height = 20
eyebrow_depth = 21
eyebrow_shape = 22
temple_width = 23
face_depth = 24
face_ratio = 25
face_width = 26

comp_less_than = -1;
comp_greater_than = 1;

skins = [
  (
    "man", 0,
    "man_body", "man_calf_l", "m_handL",
    "male_head", man_face_keys,
    ["man_hair_s","man_hair_m","man_hair_n","man_hair_o", "man_hair_y10", "man_hair_y12","man_hair_p","man_hair_r","man_hair_q","man_hair_v","man_hair_t","man_hair_y6","man_hair_y3","man_hair_y7","man_hair_y9","man_hair_y11","man_hair_u","man_hair_y","man_hair_y2","man_hair_y4"], #man_hair_meshes ,"man_hair_y5","man_hair_y8",
    ["beard_e","beard_d","beard_k","beard_l","beard_i","beard_j","beard_z","beard_m","beard_n","beard_y","beard_p","beard_o",   "beard_v", "beard_f", "beard_b", "beard_c","beard_t","beard_u","beard_r","beard_s","beard_a","beard_h","beard_g",], #beard meshes ,"beard_q"
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
    ["beard_blonde","beard_red","beard_brunette","beard_black","beard_white"], #beard_materials
    [("manface_young_2",0xffcbe0e0,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19]),
     ("manface_midage",0xffdfefe1,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_young",0xffd0e0e0,["hair_blonde"],[0xff83301a, 0xff502a19, 0xff19100c, 0xff0c0d19]),     
#     ("manface_old",0xffd0d0d0,["hair_white","hair_brunette","hair_red","hair_blonde"],[0xffffcded, 0xffbbcded, 0xff99eebb]),
     ("manface_young_3",0xffdceded,["hair_blonde"],[0xff2f180e, 0xff171313, 0xff007080c]),
     ("manface_7",0xffc0c8c8,["hair_blonde"],[0xff171313, 0xff007080c]),
     ("manface_midage_2",0xfde4c8d8,["hair_blonde"],[0xff502a19, 0xff19100c, 0xff0c0d19]),
     ("manface_rugged",0xffb0aab5,["hair_blonde"],[0xff171313, 0xff007080c]),
#     ("manface_young_4",0xffe0e8e8,["hair_blonde"],[0xff2f180e, 0xff171313, 0xff007080c]),
     ("manface_asian1",0xffe3e8e1,["hair_blonde"],[0xff171313, 0xff007080c]),
     ("manface_asian2",0xffe3e8e1,["hair_blonde"],[0xff171313, 0xff007080c]),
	 ("manface_asian3",0xffbbb6ae,["hair_blonde"],[0xff171313, 0xff007080c]),
	 ("manface_mideast1",0xffaeb0a6,["hair_blonde"],[0xff171313, 0xff007080c]),
	 ("manface_mideast2",0xffd0c8c1,["hair_blonde"],[0xff171313, 0xff007080c]),
	 ("manface_mideast3",0xffe0e8e8,["hair_blonde"],[0xff171313, 0xff007080c]),
     ("manface_black1",0xff87655c,["hair_blonde"],[0xff171313, 0xff007080c]),
	 ("manface_black2",0xff5a342d,["hair_blonde"],[0xff171313, 0xff007080c]),
	 ("manface_black3",0xff634d3e,["hair_blonde"],[0xff171313, 0xff007080c]),
	 ("manface_white1",0xffe0e8e8,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
	 ("manface_white2",0xffe0e8e8,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
	 ("manface_white3",0xffe0e8e8,["hair_blonde"],[0xff83301a, 0xff502a19, 0xff19100c, 0xff0c0d19]),
     ("manface_african",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),     
#     ("manface_old_2",0xffd5d5c5,["hair_white"],[0xffffcded, 0xffbbcded, 0xff99eebb]),
     ], #man_face_textures,
    [(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_man_yell"),(voice_stun,"snd_man_stun"),(voice_victory,"snd_man_victory")], #voice sounds
    "skel_human", 1.0,
    psys_game_blood,psys_game_blood_2,
	[[1.6, comp_greater_than, (1.0,eye_to_eye_dist), (1.0,temple_width)], #constraints: ex: 1.7 > (face_width + temple_width)
     [0.6, comp_less_than, (1.0,eye_to_eye_dist), (1.0,temple_width)],  
	 [1.5, comp_greater_than, (1.0,face_ratio), (1.0,mouth_width)],  # face ratio and mouth to nose distance
	 [0.6, comp_greater_than, (-1.0,nose_width), (1.0,mouth_width)],  # nose height and mouth to nose distance
	 [-1.0, comp_less_than, (-1.0,nose_width), (1.0,mouth_width)],  # nose height and mouth to nose distance
     ]
  ),
  
  (
    "woman", skf_use_morph_key_10,
    "woman_body",  "woman_calf_l", "f_handL",
    "corprus_female_head", woman_face_keys_2,
    ["woman_hair_01","woman_hair_02","woman_hair_03","woman_hair_04","woman_hair_05","woman_hair_06","woman_hair_07","woman_hair_08","woman_hair_09","woman_hair_10","woman_hair_11","woman_hair_12","woman_hair_13","woman_hair_14","woman_hair_15","woman_hair_16","woman_hair_17","woman_hair_18","woman_hair_19","woman_hair_20","woman_hair_21","woman_hair_22","woman_hair_23","woman_hair_24","woman_hair_25"], #woman_hair_meshes
    [],
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
    [],
    [("womanface_young_gaolu",0xfff2f9f7,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
     ("womanface_b_gaolu",0xffeaf7ff,["hair_blonde"],[0xffa5481f, 0xff502a19, 0xff19100c, 0xff0c0d19]),
     ("womanface_caucas_gaolu",0xffe4eded,["hair_blonde"],[0xff502a19, 0xff19100c, 0xff0c0d19]),
     ("womanface_brown_gaolu",0xffd5d3b8,["hair_blonde"],[0xff19100c, 0xff0c0d19, 0xff007080c]),
     ("womanface_african_gaolu",0xff7e7c85,["hair_blonde"],[0xff120808, 0xff007080c]),
     ("womanface_c_gaolu",0xffeaf0f5,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
#     ("womanface_midage",0xffe5eaf0,["hair_black","hair_brunette","hair_red","hair_white"],[0xffffcded, 0xffbbcded, 0xff99eebb]),
     ],#woman_face_textures
    [(voice_die,"snd_woman_die"),(voice_hit,"snd_woman_hit"),(voice_yell,"snd_woman_yell")], #voice sounds
    "skel_human", 0.95,
    psys_game_blood,psys_game_blood_2,
  ),
  
  (
    "male_elf", 0,
    "man_body", "man_calf_l", "m_handL",
    "elf_head", woman_face_keys,
    ["elf_hair_4","elf_hair_3","elf_hair_1","elf_hair_2","man_hair_p","elf_hair_6", "elf_hair_7","man_hair_r","man_hair_q","elf_hair_5","elf_hair_8"], #man_hair_meshes ,"man_hair_y5","man_hair_y8",
    [], #beard meshes ,"beard_q"
    ["hair_blonde_elf", "hair_blonde_elf", "hair_blonde_elf", "hair_blonde_elf", "hair_blonde_elf"], #hair textures
    ["beard_blonde"], #beard_materials
    [("elfface_young"  ,0xffcbe0e0,["hair_blonde_elf"],[0xffffffff, 0xffb04717, 0xff502a19]),
     ("elfface_young_2",0xffdfefe1,["hair_blonde_elf"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("elfface_young_3",0xffdceded,["hair_blonde_elf"],[0xff2f180e, 0xff171313, 0xff07080c]),
   ], #face_textures,
    [(voice_die,"snd_elf_die"),(voice_hit,"snd_elf_hit"),(voice_grunt,"snd_elf_grunt"),(voice_grunt_long,"snd_elf_grunt"),(voice_yell,"snd_elf_grunt"), (voice_warcry, "snd_man_warcry"),(voice_victory,"snd_man_victory")], #voice sounds
    
    "skel_human", 1.0,
    psys_game_blood,psys_game_blood_2,
    [[1.7, comp_greater_than, (1.0,face_width), (1.0,temple_width)], #constraints: ex: 1.7 > (face_width + temple_width)
     [0.3, comp_less_than, (1.0,face_width), (1.0,temple_width)],
     [1.7, comp_greater_than, (1.0,face_width), (1.0,face_depth)],
     [0.3, comp_less_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [1.7, comp_greater_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [-0.7, comp_less_than, (1.0,nose_size), (-1.0,nose_shape)],
     [0.7, comp_greater_than, (1.0,nose_size), (-1.0,nose_shape)],
     [2.7, comp_greater_than, (1.0,chin_size), (1.0,mouth_nose_distance), (1.0,nose_height), (-1.0,face_width)],
    ],
  ),

  
  (#vampire
    "vampire", 0,
    "darkelf_body", "dark_calf_l", "dark_handL",
    "darkelf_head", man_face_keys,
    ["v_hair_1","v_hair_2","v_hair_3","v_hair_4","man_hair_v","man_hair_s","woman_hair_03","woman_hair_09","woman_hair_10", "man_hair_y9", "man_hair_y12","man_hair_p","man_hair_r","man_hair_q","man_hair_y9","man_hair_y4","v_hair_4"], #man_hair_meshes ,"man_hair_y5","man_hair_y8",
    [], #beard meshes ,"beard_q"
    ["hair_blonde","hair_black", "hair_white"], #hair textures
    ["beard_black","beard_white"], #beard_materials
    [("vampire_face_a",0xffcbe0e0,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19]),
     ("vampire_face_b",0xffdfefe1,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("vampire_face_c",0xffd0e0e0,["hair_blonde"],[0xff83301a, 0xff502a19, 0xff19100c, 0xff0c0d19]),     
     ], #man_face_textures,
    [(voice_die,"snd_skeleton_death"),(voice_hit,"snd_skeleton_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_skeleton_yell"),(voice_stun,"snd_man_stun"),(voice_victory,"snd_man_victory")], #voice sounds
    "skel_human", 1.1,
    psys_no_blood,psys_no_blood,
    [[1.7, comp_greater_than, (1.0,face_width), (1.0,temple_width)], #constraints: ex: 1.7 > (face_width + temple_width)
     [0.3, comp_less_than, (1.0,face_width), (1.0,temple_width)],
     [1.7, comp_greater_than, (1.0,face_width), (1.0,face_depth)],
     [0.3, comp_less_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [1.7, comp_greater_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [-0.7, comp_less_than, (1.0,nose_size), (-1.0,nose_shape)],
     [0.7, comp_greater_than, (1.0,nose_size), (-1.0,nose_shape)],
     [2.7, comp_greater_than, (1.0,chin_size), (1.0,mouth_nose_distance), (1.0,nose_height), (-1.0,face_width)],
     ]
  ),
      
  
  (
    "goblin", 0,
    "blackhorn_org_body", "org_calf_01_L", "blackhorn_org_hand_L",
    "blackhorn_org_head", blackhorn_org_face_keys,
    [], #hair_meshes 
    [], #beard meshes 
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
    ["beard_blonde","beard_red","beard_brunette","beard_black","beard_white"], #beard_materials
    [("blackhorn_org_head",0xffcbe0e0,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19]),
     ("blackhorn_org_head",0xffcbe0e0,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19]),
     ("blackhorn_org_head",0xffdfefe1,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("blackhorn_org_head",0xffd0e0e0,["hair_blonde"],[0xff83301a, 0xff502a19, 0xff19100c, 0xff0c0d19]),     
     ("blackhorn_org_head",0xffdceded,["hair_blonde"],[0xff2f180e, 0xff171313, 0xff007080c]),
     ("blackhorn_org_head",0xffc0c8c8,["hair_blonde"],[0xff171313, 0xff007080c]),
     ("blackhorn_org_head",0xfde4c8d8,["hair_blonde"],[0xff502a19, 0xff19100c, 0xff0c0d19]),
     ("blackhorn_org_head",0xffb0aab5,["hair_blonde"],[0xff171313, 0xff007080c]),
     ("blackhorn_org_head",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),
    ], #face textures
    #[(voice_die,"snd_goblin_die"),(voice_hit,"snd_goblin_hit"),(voice_grunt,"snd_goblin_grunt"),(voice_yell,"snd_goblin_warcry"),(voice_victory,"snd_goblin_warcry")], #voice sounds
    #[(voice_die,"snd_troll_die"),(voice_hit,"snd_troll_hit"),(voice_grunt,"snd_troll_grunt"),(voice_grunt_long,"snd_troll_grunt"),(voice_yell,"snd_troll_yell"),(voice_victory,"snd_troll_victory")], #voice sounds
    [(voice_die, "snd_hbgoblin_die"), (voice_hit, "snd_hbgoblin_hit"), (voice_grunt, "snd_hbgoblin_grunt"), (voice_warcry, "snd_hbgoblin_warcry"), (voice_victory, "snd_hbgoblin_warcry")],
    "skel_human", 0.8,
    psys_game_blood,psys_game_blood_2,
    [[1.7, comp_greater_than, (1.0,face_width), (1.0,temple_width)], #constraints: ex: 1.7 > (face_width + temple_width)
     [0.3, comp_less_than, (1.0,face_width), (1.0,temple_width)],
     [1.7, comp_greater_than, (1.0,face_width), (1.0,face_depth)],
     [0.3, comp_less_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [1.7, comp_greater_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [-0.7, comp_less_than, (1.0,nose_size), (-1.0,nose_shape)],
     [0.7, comp_greater_than, (1.0,nose_size), (-1.0,nose_shape)],
     [2.7, comp_greater_than, (1.0,chin_size), (1.0,mouth_nose_distance), (1.0,nose_height), (-1.0,face_width)],
     ]
   ),


  (
    "ogre", 0,
    #"ogre_body", "orge_calf_L", "ogre_handL",#    "ogre_armor-nema", "ogre_calf_nema_l", "ogre_hand_nema_l",
    "ogre_body", "barbar_calf_l", "ogre_handL",#    "ogre_armor-nema", "ogre_calf_nema_l", "ogre_hand_nema_l",
    "ogre_head", undead_face_keys,#    "ogre_head-nema",
    ["man_hair_y6","man_hair_v"],#hair_meshes 
    [],
    ["hair_blonde", "hair_black", "hair_white"], #hair textures
    [],
    [
     ("orc_face",0xffe3e8e1,["hair_blonde"],[0xff171313, 0xff007080c]),
     ("orc_face",0xffe3e8e1,["hair_blonde"],[0xff171313, 0xff007080c]),
     ("orc_face",0xffbbb6ae,["hair_blonde"],[0xff171313, 0xff007080c]),
    ], #face textures
    [(voice_die,"snd_troll_die"),(voice_hit,"snd_troll_hit"),(voice_grunt,"snd_troll_grunt"),(voice_grunt_long,"snd_troll_grunt"),(voice_yell,"snd_troll_yell"),(voice_victory,"snd_troll_victory")], #voice sounds
      "skel_human", 1.3, # "skel_human", 1.8,
    psys_game_blood,psys_game_blood_2,
  ),
  
  
  (
    "skeleton", 0,
    "barf_skeleton", "barf_skeleton_calf_l", "barf_skeleton_handL",
    "barf_skull", undead_face_keys,
    [], #man_hair_meshes ,"man_hair_y5","man_hair_y8",
    [], #beard meshes ,"beard_q"
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
    [], #beard_materials
    [
     ("barf_skull",0xffcbe0e0,["hair_black"],[0xffffffff, 0xffb04717, 0xff502a19]),
     ], #man_face_textures,
    [(voice_die,"snd_skeleton_death"),(voice_hit,"snd_skeleton_hit"),(voice_yell,"snd_skeleton_yell"),(voice_grunt,"snd_skeleton_yell"),(voice_stun,"snd_skeleton_hit"),(voice_victory,"snd_skeleton_death")], #voice sounds
    "skel_human", 1.0,
    psys_no_blood,psys_no_blood,
    []
  ),
  
  (
    "beastman", 0,
    "beastman_bodys", "beast_calf_l", "beast_handL",
    "beastmen", undead_face_keys,
    [], #man_hair_meshes ,"man_hair_y5","man_hair_y8",
    [], #beard meshes ,"beard_q"
    ["hair_black"], #hair textures
    ["hair_black"], #beard_materials
    [
     ("beastheads",0xffcbe0e0,["hair_black"],[0xffffffff, 0xffb04717, 0xff502a19]),
     ], #man_face_textures,
    #[(voice_die,"snd_skeleton_death"),(voice_hit,"snd_skeleton_hit"),(voice_yell,"snd_skeleton_yell"),(voice_grunt,"snd_undead_grunt"),(voice_stun,"snd_skeleton_hit"),(voice_victory,"snd_skeleton_death")], #voice sounds
    [(voice_die, "snd_beastmen_die"), (voice_hit, "snd_beastmen_hit"), (voice_warcry, "snd_beastmen_warcry"),(voice_grunt, "snd_beastmen_grunt"), (voice_grunt_long, "snd_beastmen_grunt"), (voice_yell, "snd_beastmen_grunt"), (voice_stun, "snd_beastmen_hit"), (voice_victory, "snd_beastmen_warcry")],
    
    "skel_human", 1.2,
    psys_no_blood,psys_no_blood,
    []
  ),
      
  (
    "dwarf", 0,
    "dwarf_body", "man_calf_l", "m_handL",
    "male_head", man_face_keys,
    ["man_hair_s","man_hair_m","man_hair_n","man_hair_o", "man_hair_y10", "man_hair_y12","man_hair_p","man_hair_r","man_hair_q","man_hair_v","man_hair_t","man_hair_y6","man_hair_y3","man_hair_y7","man_hair_y9","man_hair_y11","man_hair_u","man_hair_y","man_hair_y2","man_hair_y4","dwarf_hair_b","dwarf_hair_c"], #man_hair_meshes ,"man_hair_y5","man_hair_y8",
    ["beard_va","beard_ya","beard_big","beard_longer","beard_z","beard_long","beard_n","beard_y","beard_yad","beard_o",], #beard meshes ,"beard_q"
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
    ["beard_blonde","beard_red","beard_brunette","beard_black","beard_white"], #beard_materials
    [
     ("manface_young_2",0xffcbe0e0,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19]),
     ("manface_young",0xffd0e0e0,["hair_blonde"],[0xff83301a, 0xff502a19, 0xff19100c, 0xff0c0d19]),     
     ("manface_young_3",0xffdceded,["hair_blonde"],[0xff2f180e, 0xff171313, 0xff007080c]),
     ("manface_midage",0xffdfefe1,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_7",0xffc0c8c8,["hair_blonde"],[0xff171313, 0xff007080c]),
     ("manface_midage_2",0xfde4c8d8,["hair_blonde"],[0xff502a19, 0xff19100c, 0xff0c0d19]),
     ("manface_rugged",0xffb0aab5,["hair_blonde"],[0xff171313, 0xff007080c]),
     ], #man_face_textures,
    [(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_man_yell"),(voice_stun,"snd_man_stun"),(voice_victory,"snd_man_victory")], #voice sounds
    "skel_dwarf_2", 0.9,
    psys_game_blood,psys_game_blood_2,
    [[1.7, comp_greater_than, (1.0,face_width), (1.0,temple_width)], #constraints: ex: 1.7 > (face_width + temple_width)
     [0.3, comp_less_than, (1.0,face_width), (1.0,temple_width)],
     [1.7, comp_greater_than, (1.0,face_width), (1.0,face_depth)],
     [0.3, comp_less_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [1.7, comp_greater_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [-0.7, comp_less_than, (1.0,nose_size), (-1.0,nose_shape)],
     [0.7, comp_greater_than, (1.0,nose_size), (-1.0,nose_shape)],
     [2.7, comp_greater_than, (1.0,chin_size), (1.0,mouth_nose_distance), (1.0,nose_height), (-1.0,face_width)],
     ]
  ),

  (
    "troll", 0,
    "troll_body", "toumingshen", "troll_handL",#    "ogre_armor-nema", "ogre_calf_nema_l", "ogre_hand_nema_l",
    "dummy_mesh", undead_face_keys,#    "ogre_head-nema",
    ["ogre_hair_t","ogre_hair_t2"],#hair_meshes 
    [],
    ["hair_blonde"], #hair textures
    [],
    [
     ("troll",0xffdfefe1,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),   
    ], #face textures
    #[(voice_die,"snd_troll_die"),(voice_hit,"snd_troll_hit"),(voice_grunt,"snd_troll_grunt")], #voice sounds
    [(voice_die,"snd_troll_die"),(voice_hit,"snd_troll_hit"),(voice_grunt,"snd_troll_grunt"),(voice_grunt_long,"snd_troll_grunt"),(voice_yell,"snd_troll_yell"),(voice_victory,"snd_troll_victory")], #voice sounds
      "skel_troll", 0.9, # "skel_human", 1.8,
    psys_game_blood,psys_game_blood_2,
    []
  ),
      
  (#female_elf
    "female_elf", skf_use_morph_key_10,
    "dwoman_body",  "dwoman_calf_l", "df_handL",
    "elf_head", woman_face_keys,
    ["woman_hair_12","woman_hair_10","welf_hair_3","welf_hair_4","welf_hair_5","welf_hair_6","welf_hair_7","welf_hair_8","woman_hair_15","woman_hair_16","woman_hair_20","woman_hair_23","woman_hair_gaolu_0"], #woman_hair_meshes
    [],
    ["hair_white", "hair_white", "hair_white", "hair_white", "hair_white"], #hair textures
    [],
    [("womanface_a_elf",0xffe3e8ef,["hair_white"],[0xffffffff]),
     ],#woman_face_textures
    [(voice_die,"snd_woman_die"),(voice_hit,"snd_woman_hit"),(voice_yell,"snd_woman_yell")], #voice sounds
    "skel_human", 0.95,
    psys_game_blood,psys_game_blood_2,
  ),
      
  (#dwarf_giant
    "dwarf_giant", 0,
    "tld_dwarf_body", "tld_dwarf_calf_l", "tld_dwarf_handL",
    "dwarf_head", man_face_keys,
    
    ["man_hair_s","man_hair_n","man_hair_p","man_hair_r","man_hair_q","man_hair_v","man_hair_y9"], #man_hair_meshes ,"man_hair_y5","man_hair_y8",
    ["beard_va","beard_ya","beard_big","beard_longer","beard_z","beard_long","beard_n","beard_y","beard_yad","beard_o",], #beard meshes ,"beard_q"
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
    ["beard_blonde","beard_red","beard_brunette","beard_black","beard_white"], #beard_materials
    [("manface_young"   ,0xffd0e0e0,["hair_blonde"],[0xffb04717, 0xffb04717, 0xff502a19]),
     ("manface_young_2" ,0xffcbe0e0,["hair_blonde"],[0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_7",0xffc0c8c8,["hair_blonde"],[0xff171313, 0xff007080c]),
     ("manface_midage",0xffdfefe1,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_midage_2",0xfde4c8d8,["hair_blonde"],[0xff502a19, 0xff19100c, 0xff0c0d19]),
     ("manface_rugged",0xffb0aab5,["hair_blonde"],[0xff171313, 0xff007080c]),
     ], #man_face_textures,
    [(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_man_yell"),(voice_stun,"snd_man_stun"),(voice_warcry, "snd_man_warcry"),(voice_victory,"snd_man_victory")], #voice sounds
    "skel_dwarf", 1.8,
    psys_game_blood,psys_game_blood_2,
    [[1.7, comp_greater_than, (1.0,face_width), (1.0,temple_width)], #constraints: ex: 1.7 > (face_width + temple_width)
     [0.3, comp_less_than, (1.0,face_width), (1.0,temple_width)],
     [1.7, comp_greater_than, (1.0,face_width), (1.0,face_depth)],
     [0.3, comp_less_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [1.7, comp_greater_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [-0.7, comp_less_than, (1.0,nose_size), (-1.0,nose_shape)],
     [0.7, comp_greater_than, (1.0,nose_size), (-1.0,nose_shape)],
     [2.7, comp_greater_than, (1.0,chin_size), (1.0,mouth_nose_distance), (1.0,nose_height), (-1.0,face_width)],
     ]
  ),
      
  (
    "titan", 0,
    "man_body", "man_calf_l", "m_handL",
    "male_head", man_face_keys,
    ["man_hair_s","man_hair_m","man_hair_n","man_hair_o", "man_hair_y10", "man_hair_y12","man_hair_p","man_hair_r","man_hair_q","man_hair_v","man_hair_t","man_hair_y6","man_hair_y3","man_hair_y7","man_hair_y9","man_hair_y11","man_hair_u","man_hair_y","man_hair_y2","man_hair_y4"], #man_hair_meshes ,"man_hair_y5","man_hair_y8",
    ["beard_e","beard_d","beard_k","beard_l","beard_i","beard_j","beard_z","beard_m","beard_n","beard_y","beard_p","beard_o",   "beard_v", "beard_f", "beard_b", "beard_c","beard_t","beard_u","beard_r","beard_s","beard_a","beard_h","beard_g",], #beard meshes ,"beard_q"
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
    ["beard_blonde","beard_red","beard_brunette","beard_black","beard_white"], #beard_materials
    [("manface_young_2",0xffcbe0e0,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19]),
     ("manface_midage",0xffdfefe1,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
     ("manface_young",0xffd0e0e0,["hair_blonde"],[0xff83301a, 0xff502a19, 0xff19100c, 0xff0c0d19]),     
#     ("manface_old",0xffd0d0d0,["hair_white","hair_brunette","hair_red","hair_blonde"],[0xffffcded, 0xffbbcded, 0xff99eebb]),
     ("manface_young_3",0xffdceded,["hair_blonde"],[0xff2f180e, 0xff171313, 0xff007080c]),
     ("manface_7",0xffc0c8c8,["hair_blonde"],[0xff171313, 0xff007080c]),
     ("manface_midage_2",0xfde4c8d8,["hair_blonde"],[0xff502a19, 0xff19100c, 0xff0c0d19]),
     ("manface_rugged",0xffb0aab5,["hair_blonde"],[0xff171313, 0xff007080c]),
#     ("manface_young_4",0xffe0e8e8,["hair_blonde"],[0xff2f180e, 0xff171313, 0xff007080c]),
     ("manface_african",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),     
#     ("manface_old_2",0xffd5d5c5,["hair_white"],[0xffffcded, 0xffbbcded, 0xff99eebb]),
     ], #man_face_textures,
    [(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_man_yell"),(voice_stun,"snd_man_stun"),(voice_victory,"snd_man_victory")], #voice sounds
    "skel_human", 1.6,
    psys_no_blood,psys_no_blood,
    [[1.7, comp_greater_than, (1.0,face_width), (1.0,temple_width)], #constraints: ex: 1.7 > (face_width + temple_width)
     [0.3, comp_less_than, (1.0,face_width), (1.0,temple_width)],
     [1.7, comp_greater_than, (1.0,face_width), (1.0,face_depth)],
     [0.3, comp_less_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [1.7, comp_greater_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [-0.7, comp_less_than, (1.0,nose_size), (-1.0,nose_shape)],
     [0.7, comp_greater_than, (1.0,nose_size), (-1.0,nose_shape)],
     [2.7, comp_greater_than, (1.0,chin_size), (1.0,mouth_nose_distance), (1.0,nose_height), (-1.0,face_width)],
     ]
  ),
      
  (
    "demon", 0,
    "devil_body_1", "demon_foot_l", "herald_handL",
    "devilhead", man_face_keys,
    ["man_hair_s","man_hair_m","man_hair_n","man_hair_o", "man_hair_y10", "man_hair_y12","man_hair_p","man_hair_r","man_hair_q","man_hair_v","man_hair_t","man_hair_y6","man_hair_y3","man_hair_y7","man_hair_y9","man_hair_y11","man_hair_u","man_hair_y","man_hair_y2","man_hair_y4"], #man_hair_meshes ,"man_hair_y5","man_hair_y8",
    ["beard_e","beard_d","beard_k","beard_l","beard_i","beard_j","beard_z","beard_m","beard_n","beard_y","beard_p","beard_o",   "beard_v", "beard_f", "beard_b", "beard_c","beard_t","beard_u","beard_r","beard_s","beard_a","beard_h","beard_g",], #beard meshes ,"beard_q"
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
    ["beard_blonde","beard_red","beard_brunette","beard_black","beard_white"], #beard_materials
    [("demon_skin",0xffcbe0e0,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19]),
     ], #man_face_textures,
    [(voice_die,"snd_skeleton_death"),(voice_hit,"snd_skeleton_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_skeleton_yell"),(voice_stun,"snd_skeleton_hit"),(voice_victory,"snd_skeleton_death")], #voice sounds    
    "skel_human", 1.2,
    psys_game_blood,psys_game_blood_2,
    [[1.7, comp_greater_than, (1.0,face_width), (1.0,temple_width)], #constraints: ex: 1.7 > (face_width + temple_width)
     [0.3, comp_less_than, (1.0,face_width), (1.0,temple_width)],
     [1.7, comp_greater_than, (1.0,face_width), (1.0,face_depth)],
     [0.3, comp_less_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [1.7, comp_greater_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [-0.7, comp_less_than, (1.0,nose_size), (-1.0,nose_shape)],
     [0.7, comp_greater_than, (1.0,nose_size), (-1.0,nose_shape)],
     [2.7, comp_greater_than, (1.0,chin_size), (1.0,mouth_nose_distance), (1.0,nose_height), (-1.0,face_width)],
     ]
  ),
     
  ("orc", 0,
    "orcbody", "orcmale_calf_l", "orcmale_handL", "orchead_half",
    [(20, 0, -0.300000, 1.100000, "Mouth Shape"),
     (40, 0, -0.500000, 1.500000, "Eye Size"),
     (60, 0, -0.300000, 1.500000, "Nose Position"),
     (80, 0, -0.600000, 1.000000, "Tusks Size"),
     (100, 0, -0.600000, 1.000000, "Teeth Size"),
     (280, 0, 0.000000, 0.000000, "Post-Edit"),
    ],
   [],
   [],
   ["hair_black"],
   ["hair_black"],
   [("orchead", 0xffaf9f7e, ["hair_black"], []),
    ("orchead2", 0xffaf9f7e, ["hair_black"], []),
   ],
    [(voice_die,"snd_troll_die"),(voice_hit,"snd_troll_hit"),(voice_grunt,"snd_troll_grunt"),(voice_grunt_long,"snd_troll_grunt"),(voice_yell,"snd_troll_yell"),(voice_victory,"snd_troll_victory")], #voice sounds
   "skel_big", 1.000000,
   psys_game_blood, psys_game_blood_2, 
   []
  ),
      
#new magic begin
##  (
##    "undead", 0,
##    "undead_body", "undead_calf_l", "undead_handL",
##    "undead_head", undead_face_keys,
##    [],
##    [],
##    [],
##    [],
##    [("undeadface_a",0xffffffff,[]),
##     ("undeadface_b",0xffcaffc0,[]),
##     ], #undead_face_textures
##    [], #voice sounds
##    "skel_human", 1.0,
##  ),
#new magic end
]

# modmerger_start version=201 type=2
try:
    component_name = "skins"
    var_set = { "skins" : skins }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
