from header_particle_systems import *
#psf_always_emit         = 0x0000000002
#psf_global_emit_dir     = 0x0000000010
#psf_emit_at_water_level = 0x0000000020
#psf_billboard_2d        = 0x0000000100 # up_vec = dir, front rotated towards camera
#psf_billboard_3d        = 0x0000000200 # front_vec point to camera.
#psf_billboard_drop      = 0x0000000300
#psf_turn_to_velocity    = 0x0000000400
#psf_randomize_rotation  = 0x0000001000
#psf_randomize_size      = 0x0000002000
#psf_2d_turbulance       = 0x0000010000

####################################################################################################################
#   Each particle system contains the following fields:
#  
#  1) Particle system id (string): used for referencing particle systems in other files.
#     The prefix psys_ is automatically added before each particle system id.
#  2) Particle system flags (int). See header_particle_systems.py for a list of available flags
#  3) mesh-name.
####
#  4) Num particles per second:    Number of particles emitted per second.
#  5) Particle Life:    Each particle lives this long (in seconds).
#  6) Damping:          How much particle's speed is lost due to friction.
#  7) Gravity strength: Effect of gravity. (Negative values make the particles float upwards.)
#  8) Turbulance size:  Size of random turbulance (in meters)
#  9) Turbulance strength: How much a particle is affected by turbulance.
####
# 10,11) Alpha keys :    Each attribute is controlled by two keys and 
# 12,13) Red keys   :    each key has two fields: (time, magnitude)
# 14,15) Green keys :    For example scale key (0.3,0.6) means 
# 16,17) Blue keys  :    scale of each particle will be 0.6 at the
# 18,19) Scale keys :    time 0.3 (where time=0 means creation and time=1 means end of the particle)
#
# The magnitudes are interpolated in between the two keys and remain constant beyond the keys.
# Except the alpha always starts from 0 at time 0.
####
# 20) Emit Box Size :   The dimension of the box particles are emitted from.
# 21) Emit velocity :   Particles are initially shot with this velocity.
# 22) Emit dir randomness
# 23) Particle rotation speed: Particles start to rotate with this (angular) speed (degrees per second).
# 24) Particle rotation damping: How quickly particles stop their rotation
####################################################################################################################

particle_systems = [
  
#    ("game_rain", psf_billboard_2d|psf_global_emit_dir|psf_always_emit, "prtcl_rain",
#     500, 0.5, 0.33, 1.0, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
#     (1.0, 0.3), (1, 0.3),        #alpha keys
#     (1.0, 1.0), (1, 1.0),      #red keys
#     (1.0, 1.0), (1, 1.0),      #green keys
#     (1.0, 1.0), (1, 1.0),      #blue keys
#     (1.0, 1.5),   (1.0, 1.5),   #scale keys
#     (8.2, 8.2, 0.2),           #emit box size
#     (0, 0, -10.0),               #emit velocity
#     0.0,                       #emit dir randomness
#     0,                       #rotation speed
#     0.5                        #rotation damping
#    ),
    
    ("game_rain", psf_billboard_2d|psf_global_emit_dir|psf_always_emit, "new_prtcl_rain",
     500, 0.5, 0.33, 1.0, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (1.0, 0.3), (1, 0.3),        #alpha keys
     (1.0, 1.0), (1, 1.0),      #red keys
     (1.0, 1.0), (1, 1.0),      #green keys
     (1.0, 1.0), (1, 1.0),      #blue keys
     (1.0, 1.5),   (1.0, 1.5),   #scale keys
     (8.2, 8.2, 0.2),           #emit box size
     (0, 0, -10.0),               #emit velocity
     0.0,                       #emit dir randomness
     0,                       #rotation speed
     0.5                        #rotation damping
    ),
    
    ("game_snow", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_snow_fall_1",
     150, 2, 0.2, 0.1, 30, 20,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.2, 1), (1, 1),        #alpha keys
     (1.0, 1.0), (1, 1.0),      #red keys
     (1.0, 1.0), (1, 1.0),      #green keys
     (1.0, 1.0), (1, 1.0),      #blue keys
     (1.0, 1.7),   (1.0, 1.7),   #scale keys
     (10, 10, 0.5),           #emit box size
     (0, 0, -5.0),               #emit velocity
     1,                       #emit dir randomness
     200,                       #rotation speed
     0.5                        #rotation damping
    ),
    
##    ("game_blood", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation, "prtcl_dust_a",
##     50, 0.65, 0.95, 1.0, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
##     (0.3, 0.3), (1, 0.2),        #alpha keys
##     (1.0, 0.4), (1, 0.05),      #red keys
##     (1.0, 0.05),(1, 0.05),      #green keys
##     (1.0, 0.05),(1, 0.05),      #blue keys
##     (0.3, 0.5),   (1.0, 2.5),   #scale keys
##     (0.04, 0.01, 0.01),           #emit box size
##     (0, 1, 0.0),               #emit velocity
##     0.05,                       #emit dir randomness
##     0,                       #rotation speed
##     0.5                        #rotation damping
##    ),
##    
("game_blood", psf_billboard_3d | psf_randomize_size|psf_randomize_rotation,  "prt_mesh_blood_3",
     500, 0.65, 3.5, 0.6, 0, 0,        #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength 
     (0.0, 0.7), (0.7, 0.7),          #alpha keys
     (0.1, 0.2), (1, 0.2),      #red keys
     (0.1, 0.2), (1, 0.2),       #green keys
     (0.1, 0.2), (1, 0.2),      #blue keys
     (0.0, 0.015),   (0.5, 0.300),  #scale keys
     (0, 0.05, 0),               #emit box size
     (0, 1.1, 0.4),                #emit velocity
     0.9,                       #emit dir randomness
     100,                         #rotation speed
     0,                         #rotation damping
    ),
    
    ("game_blood_2", psf_billboard_3d | psf_randomize_size|psf_randomize_rotation ,  "prt_mesh_blood_3",
     2000, 0.6, 3, 0.3, 0, 0,        #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 0.25), (0.7, 0.1),        #alpha keys
     (0.1, 0.2), (1, 0.2),      #red keys
     (0.1, 0.2), (1, 0.2),       #green keys
     (0.1, 0.2), (1, 0.2),      #blue keys
     (0.0, 0.15),   (0.5, 0.45),    #scale keys
     (0.01, 0.2, 0.01),             #emit box size
     (1.0, 1.0, 0.2),                 #emit velocity
     0.3,                         #emit dir randomness
     150,                       #rotation speed
     0,                       #rotation damping
     ),
    
    ("game_blood_3", psf_billboard_3d |psf_randomize_size|psf_randomize_rotation,  "prt_mesh_blood_1",
     4500, 2, 2, 1.2, 10, 10,        #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 1), (1, 1),          #alpha keys
     (0.1, 0.2), (1, 0.2),      #red keys
     (0.1, 0.15), (1, 0.15),       #green keys
     (0.1, 0.15), (1, 0.15),      #blue keys
     (0.1, 0.02),   (1, 0.06),  #scale keys
     (0, 0.05, 0),               #emit box size
     (0.6, 1.0, 1.1),                #emit velocity
     0,                       #emit dir randomness
     0,                         #rotation speed
     0,                         #rotation damping
    ),
    ("game_blood_4", psf_billboard_3d | psf_randomize_size|psf_randomize_rotation ,  "prt_mesh_blood_3",
     5000, 1.9, 2.75, 1.1, 10, 10,        #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.17), (0.9, 0.0),          #alpha keys
     (0.1, 0.37), (1, 0.4),      #red keys
     (0.1, 0.37), (1, 0.4),       #green keys
     (0.1, 0.37), (1, 0.4),      #blue keys
     (0.1, 0.3),   (1, 0.75),  #scale keys
     (0, 0.05, 0),               #emit box size
     (0.7, 0.1, 0.9 ),                #emit velocity
     0.5,                       #emit dir randomness
     0,                         #rotation speed
     0,                         #rotation damping
    ),

	("blood_decapitation", psf_billboard_3d|psf_global_emit_dir|psf_randomize_size|psf_randomize_rotation,  "prt_mesh_blood_3", 
     230, 2, 0.07, 1.0, 8, 11,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 0.6), (0.3, 0.6),          #alpha keys
     (0.1, 0.4), (1, 0.5),      #red keys
     (0.1, 0.4), (1, 0.5),       #green keys
     (0.1, 0.4), (1, 0.5),      #blue keys
     (0.1, 0.20),   (1, 1.5),    #scale keys
     (0.05, 0.05, 0.0),           #emit box size
     (0, 0, 3),                 #emit velocity
     0.25,                       #emit dir randomness
     300,                       #rotation speed
     0.5,                       #rotation damping
    ),
    
 #   ("game_hoof_dust", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation, "prtcl_dust_a",
 #    50, 1.0, 0.95, -0.1, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
 #    (0.0, 0.5), (1, 0.0),        #alpha keys
 #    (1.0, 0.9), (1, 0.05),      #red keys
 #    (1.0, 0.8),(1, 0.05),      #green keys
 #    (1.0, 0.7),(1, 0.05),      #blue keys
 #    (0.0, 7.5),   (1.0, 15.5),   #scale keys
 #    (0.2, 0.3, 0.2),           #emit box size
 #    (0, 0, 2.5),               #emit velocity
 #    0.05,                       #emit dir randomness
 #    100,                       #rotation speed
 #    0.5                        #rotation damping
 #   ),
     ("game_hoof_dust", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation|psf_2d_turbulance, "prt_mesh_dust_1",#prt_mesh_dust_1
     5, 2.0,  10, 0.05, 10.0, 39.0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.2, 0.5), (1, 0.0),        #alpha keys
     (0, 1), (1, 1),        #red keys
     (0, 0.9),(1, 0.9),         #green keys
     (0, 0.78),(1, 0.78),         #blue keys
     (0.0, 2.0),   (1.0, 3.5),   #scale keys
     (0.2, 0.3, 0.2),           #emit box size
     (0, 0, 3.9),                 #emit velocity
     0.5,                         #emit dir randomness
     130,                       #rotation speed
     0.5                        #rotation damping
    ),

    ("game_hoof_dust_snow", psf_billboard_3d|psf_randomize_size, "prt_mesh_snow_dust_1",#prt_mesh_dust_1
     6, 2, 3.5, 1, 10.0, 0.0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.2, 1), (1, 1),        #alpha keys
     (0, 1), (1, 1),        #red keys
     (0, 1),(1, 1),         #green keys
     (0, 1),(1, 1),         #blue keys
     (0.5, 4),   (1.0, 5.7),   #scale keys
     (0.2, 1, 0.1),           #emit box size
     (0, 0, 1),                 #emit velocity
     2,                         #emit dir randomness
     0,                       #rotation speed
     0                        #rotation damping
    ),
     ("game_hoof_dust_mud", psf_billboard_2d|psf_randomize_size|psf_randomize_rotation|psf_2d_turbulance, "prt_mesh_mud_1",#prt_mesh_dust_1
     5, .7,  10, 3, 0, 0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 1), (1, 1),        #alpha keys
     (0, .7), (1, .7),        #red keys
     (0, 0.6),(1, 0.6),         #green keys
     (0, 0.4),(1, 0.4),         #blue keys
     (0.0, 0.2),   (1.0, 0.22),   #scale keys
     (0.15, 0.5, 0.1),           #emit box size
     (0, 0, 15),                 #emit velocity
     6,                         #emit dir randomness
     200,                       #rotation speed
     0.5                        #rotation damping
    ),

    ("game_water_splash_1", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation|psf_emit_at_water_level, "prtcl_drop",
     20, 0.85, 0.25, 0.9, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.3, 0.5), (1, 0.0),        #alpha keys
     (1.0, 1.0), (1, 1.0),      #red keys
     (1.0, 1.0), (1, 1.0),      #green keys
     (1.0, 1.0), (1, 1.0),      #blue keys
     (0.0, 0.3),   (1.0, 0.18),   #scale keys
     (0.3, 0.2, 0.1),           #emit box size
     (0, 1.2, 2.3),               #emit velocity
     0.3,                       #emit dir randomness
     50,                       #rotation speed
     0.5                        #rotation damping
    ),
    
    ("game_water_splash_2", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation|psf_emit_at_water_level, "prtcl_splash_b",
     30, 0.4, 0.7, 0.5, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.3, 1.0), (1, 0.3),        #alpha keys
     (1.0, 1.0), (1, 1.0),      #red keys
     (1.0, 1.0), (1, 1.0),      #green keys
     (1.0, 1.0), (1, 1.0),      #blue keys
     (0.0, 0.25),   (1.0, 0.7),   #scale keys
     (0.4, 0.3, 0.1),           #emit box size
     (0, 1.3, 1.1),               #emit velocity
     0.1,                       #emit dir randomness
     50,                       #rotation speed
     0.5                        #rotation damping
    ),

    ("game_water_splash_3", psf_emit_at_water_level , "prt_mesh_water_wave_1",
     5, 2.0, 0, 0.0, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.03, 0.2), (1, 0.0),        #alpha keys
     (1.0, 1.0), (1, 1.0),      #red keys
     (1.0, 1.0), (1, 1.0),      #green keys
     (1.0, 1.0), (1, 1.0),      #blue keys
     (0.0, 3),   (1.0, 10),   #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0, 0, 0),                 #emit velocity
     0.0,                       #emit dir randomness
     0,                       #rotation speed
     0.5                        #rotation damping
    ),

    ("torch_fire", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     50, 0.35, 0.2, 0.03, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.8), (1, 0),        #alpha keys
     (0.5, 1.0), (1, 0.9),      #red keys
     (0.5, 0.7),(1, 0.3),       #green keys
     (0.5, 0.2), (1, 0.0),      #blue keys
     (0, 0.15),   (0.4, 0.3),   #scale keys
     (0.04, 0.04, 0.01),      #emit box size
     (0, 0, 0.5),               #emit velocity
     0.0,                       #emit dir randomness
     200,                       #rotation speed
     0.5                        #rotation damping
    ),
    ("fire_glow_1", psf_billboard_3d|psf_global_emit_dir|psf_always_emit, "prt_mesh_fire_2",
     2, 0.55, 0.2, 0.0, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.9), (1, 0),          #alpha keys
     (0.0, 0.9), (1, 0.9),      #red keys
     (0.0, 0.7),(1, 0.7),       #green keys
     (0.0, 0.4), (1, 0.4),      #blue keys
     (0, 2),   (1.0, 2),        #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0, 0, 0),                 #emit velocity
     0.0,                       #emit dir randomness
     0,
     0
    ),

    ("fire_glow_fixed", psf_billboard_3d|psf_global_emit_dir, "prt_mesh_fire_2",
     4, 100.0, 0.2, 0.0, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (-0.01, 1.0), (1, 1.0),          #alpha keys
     (0.0, 0.9), (1, 0.9),      #red keys
     (0.0, 0.7),(1, 0.7),       #green keys
     (0.0, 0.4), (1, 0.4),      #blue keys
     (0, 2),   (1.0, 2),        #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0, 0, 0),                 #emit velocity
     0.0,                       #emit dir randomness
     0,
     0
    ),

    ("torch_smoke", psf_billboard_3d|psf_global_emit_dir|psf_always_emit, "prtcl_dust_a",
     15, 0.5, 0.2, -0.2, 10.0, 0.1,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.25), (1, 0),       #alpha keys
     (0.0, 0.2), (1, 0.1),      #red keys
     (0.0, 0.2),(1, 0.09),      #green keys
     (0.0, 0.2), (1, 0.08),     #blue keys
     (0, 0.5),   (0.8, 2.5),    #scale keys
     (0.1, 0.1, 0.1),           #emit box size
     (0, 0, 1.5),               #emit velocity
     0.1                        #emit dir randomness
    ),
     ("flue_smoke_short", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_rotation|psf_randomize_size, "prtcl_dust_a",
     15, 1.5, 0.1, -0.0, 10.0, 12, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 0.3), (1, 0),        #alpha keys
     (0.0, 0.2), (1, 0.1),      #red keys
     (0.0, 0.2),(1, 0.09),      #green keys
     (0.0, 0.2), (1, 0.08),     #blue keys
     (0, 1.5),   (1, 7),          #scale keys
     (0, 0, 0),           #emit box size
     (0, 0, 1.5),               #emit velocity
     0.1,                        #emit dir randomness
     150,
     0.8,
    ),
    ("flue_smoke_tall", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_rotation|psf_randomize_size, "prtcl_dust_a",
     15, 3, 0.5, -0.0, 15.0, 12,#num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 0.35), (1, 0),         #alpha keys
     (0.0, 0.3), (1, 0.1),      #red keys
     (0.0, 0.3),(1, 0.1),       #green keys
     (0.0, 0.3), (1, 0.1),      #blue keys
     (0, 2),   (1, 7),        #scale keys
     (0, 0, 0),                 #emit box size
     (0, 0, 1.5),               #emit velocity
     0.1,                       #emit dir randomness
     150,
     0.5,
    ),

    ("war_smoke_tall", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_rotation|psf_randomize_size, "prt_mesh_smoke_1",
     5, 12, 0, 0, 7, 7, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 0.25), (1, 0),          #alpha keys
     (0.0, 1), (1, 0.8),      #red keys
     (0.0, 1),(1, 0.8),      #green keys
     (0.0, 1), (1, 0.8),     #blue keys
     (0, 2.2),   (1, 15),        #scale keys
     (0, 0, 0),                 #emit box size
     (0, 0, 2.2),               #emit velocity
     0.1,                        #emit dir randomness
     100,
     0.2,
    ),
    
     ("ladder_dust_6m", psf_billboard_3d, "prt_mesh_smoke_1",
     700, 0.9, 0, 0, 7, 7, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 0.25), (1, 0),          #alpha keys
     (0.0, 1), (1, 0.8),      #red keys
     (0.0, 1),(1, 0.8),      #green keys
     (0.0, 1), (1, 0.8),     #blue keys
     (0, 1),   (1, 2),        #scale keys
     (0.75, 0.75, 3.5),                 #emit box size  (6.5 is equal to (12m / 2) + 0.5)
     (0, 0, 0),               #emit velocity
     0.1,                        #emit dir randomness
     100,
     0.2,
    ),

     ("ladder_dust_8m", psf_billboard_3d, "prt_mesh_smoke_1",
     900, 0.9, 0, 0, 7, 7, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 0.25), (1, 0),          #alpha keys
     (0.0, 1), (1, 0.8),      #red keys
     (0.0, 1),(1, 0.8),      #green keys
     (0.0, 1), (1, 0.8),     #blue keys
     (0, 1),   (1, 2),        #scale keys
     (0.75, 0.75, 4.5),                 #emit box size  (6.5 is equal to (12m / 2) + 0.5)
     (0, 0, 0),               #emit velocity
     0.1,                        #emit dir randomness
     100,
     0.2,
    ),

     ("ladder_dust_10m", psf_billboard_3d, "prt_mesh_smoke_1",
     1100, 0.9, 0, 0, 7, 7, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 0.25), (1, 0),          #alpha keys
     (0.0, 1), (1, 0.8),      #red keys
     (0.0, 1),(1, 0.8),      #green keys
     (0.0, 1), (1, 0.8),     #blue keys
     (0, 1),   (1, 2),        #scale keys
     (0.75, 0.75, 5.5),                 #emit box size  (6.5 is equal to (12m / 2) + 0.5)
     (0, 0, 0),               #emit velocity
     0.1,                        #emit dir randomness
     100,
     0.2,
    ),

     ("ladder_dust_12m", psf_billboard_3d, "prt_mesh_smoke_1",
     1300, 0.9, 0, 0, 7, 7, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 0.25), (1, 0),          #alpha keys
     (0.0, 1), (1, 0.8),      #red keys
     (0.0, 1),(1, 0.8),      #green keys
     (0.0, 1), (1, 0.8),     #blue keys
     (0, 1),   (1, 2),        #scale keys
     (0.75, 0.75, 6.5),                 #emit box size  (6.5 is equal to (12m / 2) + 0.5)
     (0, 0, 0),               #emit velocity
     0.1,                        #emit dir randomness
     100,
     0.2,
    ),

     ("ladder_dust_14m", psf_billboard_3d, "prt_mesh_smoke_1",
     1500, 0.9, 0, 0, 7, 7, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 0.25), (1, 0),          #alpha keys
     (0.0, 1), (1, 0.8),      #red keys
     (0.0, 1),(1, 0.8),      #green keys
     (0.0, 1), (1, 0.8),     #blue keys
     (0, 1),   (1, 2),        #scale keys
     (0.75, 0.75, 7.5),                 #emit box size  (7.5 is equal to (14m / 2) + 0.5)
     (0, 0, 0),               #emit velocity
     0.1,                        #emit dir randomness
     100,
     0.2,
    ),

    ("ladder_straw_6m", psf_randomize_size | psf_randomize_rotation,  "prt_mesh_straw_1",
     700, 1, 2, 0.9, 10, 2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 1), (1, 1),          #alpha keys
     (0.1, 0.6), (1, 0.6),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.4), (1, 0.4),      #blue keys
     (0.0, 0.3),   (1, 0.3),    #scale keys
     (0.75, 0.75, 3.5),           #emit box size
     (0, 0, 0),                 #emit velocity
     2.3,                       #emit dir randomness
     200,                       #rotation speed
     0,                       #rotation damping
    ),

    ("ladder_straw_8m", psf_randomize_size | psf_randomize_rotation,  "prt_mesh_straw_1",
     900, 1, 2, 0.9, 10, 2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 1), (1, 1),          #alpha keys
     (0.1, 0.6), (1, 0.6),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.4), (1, 0.4),      #blue keys
     (0.0, 0.3),   (1, 0.3),    #scale keys
     (0.75, 0.75, 4.5),           #emit box size
     (0, 0, 0),                 #emit velocity
     2.3,                       #emit dir randomness
     200,                       #rotation speed
     0,                       #rotation damping
    ),

    ("ladder_straw_10m", psf_randomize_size | psf_randomize_rotation,  "prt_mesh_straw_1",
     1100, 1, 2, 0.9, 10, 2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 1), (1, 1),          #alpha keys
     (0.1, 0.6), (1, 0.6),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.4), (1, 0.4),      #blue keys
     (0.0, 0.3),   (1, 0.3),    #scale keys
     (0.75, 0.75, 5.5),           #emit box size
     (0, 0, 0),                 #emit velocity
     2.3,                       #emit dir randomness
     200,                       #rotation speed
     0,                       #rotation damping
    ),

    ("ladder_straw_12m", psf_randomize_size | psf_randomize_rotation,  "prt_mesh_straw_1",
     1300, 1, 2, 0.9, 10, 2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 1), (1, 1),          #alpha keys
     (0.1, 0.6), (1, 0.6),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.4), (1, 0.4),      #blue keys
     (0.0, 0.3),   (1, 0.3),    #scale keys
     (0.75, 0.75, 6.5),           #emit box size
     (0, 0, 0),                 #emit velocity
     2.3,                       #emit dir randomness
     200,                       #rotation speed
     0,                       #rotation damping
    ),

    ("ladder_straw_14m", psf_randomize_size | psf_randomize_rotation,  "prt_mesh_straw_1",
     1500, 1, 2, 0.9, 10, 2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 1), (1, 1),          #alpha keys
     (0.1, 0.6), (1, 0.6),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.4), (1, 0.4),      #blue keys
     (0.0, 0.3),   (1, 0.3),    #scale keys
     (0.75, 0.75, 7.5),           #emit box size
     (0, 0, 0),                 #emit velocity
     2.3,                       #emit dir randomness
     200,                       #rotation speed
     0,                       #rotation damping
    ),

    ("torch_fire_sparks", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size,  "prt_sparks_mesh_1",
     10, 0.7, 0.2, 0, 10.0, 0.02,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.66, 1), (1, 0),          #alpha keys
     (0.1, 0.7), (1, 0.7),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.1), (1, 0.1),      #blue keys
     (0.1, 0.05),   (1, 0.05),  #scale keys
     (0.1, 0.1, 0.1),           #emit box size
     (0, 0, 0.9),               #emit velocity
     0.0,                       #emit dir randomness
     0,
     0,
    ),

    ("fire_sparks_1", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size,  "prt_sparks_mesh_1",
     10, 1.5, 0.2, 0, 3, 10,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.6, 1), (1, 1),          #alpha keys
     (0.1, 0.7), (1, 0.7),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.1), (1, 0.1),      #blue keys
     (0.1, 0.07),   (1, 0.03),    #scale keys
     (0.17, 0.17, 0.01),           #emit box size
     (0, 0, 1),                 #emit velocity
     0.0,                       #emit dir randomness
     0,
     0,
    ),
    
    ("pistol_smoke", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation|psf_next_effect_is_lod, "prtcl_dust_a",
     80, 5, 11, 0, 6, 60,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 0.9), (0.75, 0.5),       #alpha keys
     (0.0, 0.90), (1, 0.90),          #red keys
     (0.0, 0.95),(1, 0.95),           #green keys
     (0.0, 1), (1, 1),          #blue keys
     (0, 3),   (1, 11.0),     #scale keys
     (0, 0.1, 0),                 #emit box size
     (8, 8, 0),                 #emit velocity
     0.5,                        #emit dir randomness
     55,                        #rotation speed
     0.3                        #rotation damping
    ),
	
    ("pistol_smoke_far", psf_billboard_3d|psf_randomize_size, "prtcl_dust_a",
     80, 5, 11, 0, 6, 60,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 1), (0.75, 0.75),       #alpha keys
     (0.0, 0.90), (1, 0.90),          #red keys
     (0.0, 0.95),(1, 0.95),           #green keys
     (0.0, 1), (1, 1),          #blue keys
     (0, 3),   (1, 11.0),     #scale keys
     (0, 0.1, 0),                 #emit box size
     (8, 8, 0),                 #emit velocity
     0.5,                        #emit dir randomness
     55,                        #rotation speed
     0.3                        #rotation damping
    ),	
    
    ("musket_smoke", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation|psf_next_effect_is_lod, "prtcl_dust_a",
     80, 5, 20, 0, 3, 80,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 0.9), (0.75, 0.5),       #alpha keys
     (0.0, 0.90), (1, 0.90),          #red keys
     (0.0, 0.95),(1, 0.95),           #green keys
     (0.0, 1), (1, 1),          #blue keys
     (0, 5),   (1, 14.0),     #scale keys
     (0, 0.5, 0),                 #emit box size
     (0, 50, 0),                 #emit velocity
     0.5,                        #emit dir randomness
     50,                        #rotation speed
     0.3                        #rotation damping
    ),
	
    ("musket_smoke_far", psf_billboard_3d|psf_randomize_size, "prtcl_dust_a",
     80, 5, 20, 0, 1, 65,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 1), (0.75, 0.85),       #alpha keys
     (0.0, 0.90), (1, 0.90),          #red keys
     (0.0, 0.95),(1, 0.95),           #green keys
     (0.0, 1), (1, 1),          #blue keys
     (0, 8),   (1, 14.0),     #scale keys
     (0, 0.5, 0),                 #emit box size
     (0, 50, 0),                 #emit velocity
     0.5,                        #emit dir randomness
     50,                        #rotation speed
     0.3                        #rotation damping
    ),

     ("pistol_ogon", psf_billboard_3d|psf_randomize_size|psf_next_effect_is_lod, "prt_mesh_fire_1",
      25, 0.5, 0.7, 0, 5.0, 0.5, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
       (0.0, 0.5), (0.75, 0.4), #alpha keys
      (0.0, 0.3), (1, 0.3), #red keys
      (0.0, 0.1),(1, 0.2),  #green keys
      (0.0, 0.05), (1, 0.05),   #blue keys
      (0.2, 0.5), (0.0, 0.2),   #scale keys
      (0.1, 0.1, 0.1),          #emit box size
      (2, 2, 0),                #emit velocity
      0.05,                     #emit dir randomness
      50,                       #rotation speed
      0.2                       #rotation damping
      ),

     ("pistol_ogon_far", psf_billboard_3d|psf_randomize_size, "prt_mesh_fire_1",
      25, 0, 0.7, 0, 5.0, 0.5, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
       (0.0, 0.5), (0.75, 0.4), #alpha keys
      (0.0, 0.3), (1, 0.3), #red keys
      (0.0, 0.1),(1, 0.2),  #green keys
      (0.0, 0.05), (1, 0.05),   #blue keys
      (0.2, 0.5), (0.0, 0.2),   #scale keys
      (0.1, 0.1, 0.1),          #emit box size
      (2, 2, 0),                #emit velocity
      0.05,                     #emit dir randomness
      50,                       #rotation speed
      0.2                       #rotation damping
      ),
    
      ("musket_ogon", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation|psf_next_effect_is_lod, "prt_mesh_fire_1",
        40, 0.5, 0.7, 0, 5.0, 0.5, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
       (0.0, 0.5), (0.75, 0.4), #alpha keys
      (0.0, 0.3), (1, 0.3), #red keys
      (0.0, 0.1),(1, 0.2),  #green keys
      (0.0, 0.05), (1, 0.05),   #blue keys
      (0.2, 0.5), (0.0, 0.2),   #scale keys
      (0.1, 0.1, 0.1),          #emit box size
      (0, 2, 0),                #emit velocity
      0.05,                     #emit dir randomness
      50,                       #rotation speed
      0.2                       #rotation damping
      ),

      ("musket_ogon_far", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
        40, 0, 0.7, 0, 5.0, 0.5, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
       (0.0, 0.5), (0.75, 0.4), #alpha keys
      (0.0, 0.3), (1, 0.3), #red keys
      (0.0, 0.1),(1, 0.2),  #green keys
      (0.0, 0.05), (1, 0.05),   #blue keys
      (0.2, 0.5), (0.0, 0.2),   #scale keys
      (0.1, 0.1, 0.1),          #emit box size
      (0, 2, 0),                #emit velocity
      0.05,                     #emit dir randomness
      50,                       #rotation speed
      0.2                       #rotation damping
      ),

        ("musket_svet", psf_billboard_3d|psf_randomize_size|psf_next_effect_is_lod, "prt_sparks_mesh_1",
         900, 0.3, 0.6, 0, 10.0, 0.5, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
        (0.0, 0.75), (0.7, 0.2), #alpha keys
        (0.0, 0.75), (1, 0.75), #red keys
        (0.0, 0.5),(1, 0.5),  #green keys
        (0.0, 0.0), (1, 0.0),   #blue keys
        (0.3, 2), (1, 0), #scale keys
        (0.0, 0.1, 0.1), #emit box size
        (0, 2, 0), #emit velocity
        0.0 #emit dir randomness
        ),

       ("musket_svet_far", psf_billboard_3d|psf_randomize_size, "prt_sparks_mesh_1",
         900, 0.3, 0.6, 0, 10.0, 0.5, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
        (0.0, 0.75), (0.7, 0.2), #alpha keys
        (0.0, 0.75), (1, 0.75), #red keys
        (0.0, 0.5),(1, 0.5),  #green keys
        (0.0, 0.0), (1, 0.0),   #blue keys
        (0.3, 2), (1, 0), #scale keys
        (0.0, 0.1, 0.1), #emit box size
        (0, 2, 0), #emit velocity
        0.0 #emit dir randomness
        ),
    
       ("pistol_svet", psf_billboard_3d|psf_randomize_size|psf_next_effect_is_lod, "prt_sparks_mesh_1",
        900, 0.3, 0.6, 0, 10.0, 0.5, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
        (0.0, 0.5), (0.7, 0.2), #alpha keys
        (0.0, 0.75), (1, 0.75), #red keys
        (0.0, 0.5),(1, 0.5),  #green keys
        (0.0, 0.0), (1, 0.0),   #blue keys
        (0.3, 1.5), (1, 0), #scale keys
        (0.1, 0.1, 0.1), #emit box size
        (2, 2, 0), #emit velocity
        0.0 #emit dir randomness
        ),
    
       ("pistol_svet_far", psf_billboard_3d|psf_randomize_size, "prt_sparks_mesh_1",
        900, 0.3, 0.6, 0, 10.0, 0.5, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
        (0.0, 0.5), (0.7, 0.2), #alpha keys
        (0.0, 0.75), (1, 0.75), #red keys
        (0.0, 0.5),(1, 0.5),  #green keys
        (0.0, 0.0), (1, 0.0),   #blue keys
        (0.3, 1.5), (1, 0), #scale keys
        (0.1, 0.1, 0.1), #emit box size
        (2, 2, 0), #emit velocity
        0.0 #emit dir randomness
        ),

       ("pistol_powder_a", psf_billboard_3d|psf_randomize_size|psf_next_effect_is_lod, "prtcl_dust_a",
        500, 4, 17, 0, 5, 40, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
        (0.0, 0.9), (0.75, 0.75),     #alpha keys
        (0.0, 0.95), (1, 0.95),          #red keys
        (0.0, 0.95),(1, 0.95),           #green keys
        (0.0, 1), (1, 1),          #blue keys
        (0, 1), (1, 5),  #scale keys
        (0, 0, 0),         #emit box size
        (-10, 0, 5),               #emit velocity
        0.0,                      #emit dir randomness
        100,                     #rotation speed
        0.2                       #rotation damping
        ),
       ("pistol_powder_a_far", psf_billboard_3d|psf_randomize_size, "prtcl_dust_a",
        500, 4, 17, 0, 5, 40, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
        (0.0, 0.9), (0.75, 0.75),     #alpha keys
        (0.0, 0.95), (1, 0.95),          #red keys
        (0.0, 0.95),(1, 0.95),           #green keys
        (0.0, 1), (1, 1),          #blue keys
        (0, 1), (1, 5),  #scale keys
        (0, 0, 0),         #emit box size
        (-10, 0, 5),               #emit velocity
        0.0,                      #emit dir randomness
        100,                     #rotation speed
        0.2                       #rotation damping
        ),
    
       ("pistol_powder_b", psf_billboard_3d|psf_randomize_size|psf_next_effect_is_lod, "prt_sparks_mesh_1",
        500, 0.45, 6, 0.4, 0, 0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
        (0.0, 1), (1, 1),     #alpha keys
        (0.0, 1), (1, 0.9),#red keys
        (0.0, 0.6),(1, 0.5), #green keys
        (0.0, 0.2), (1, 0.1),  #blue keys
        (0, 0.02), (1, 0),  #scale keys
        (0, 0, 0),         #emit box size
        (-1, 0.85, 0.3),               #emit velocity
        0.8,                      #emit dir randomness
        0,                     #rotation speed
        0                       #rotation damping
        ),
       ("pistol_powder_b_far", psf_billboard_3d|psf_randomize_size, "prt_sparks_mesh_1",
        500, 0, 6, 0.4, 0, 0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
        (0.0, 1), (1, 1),     #alpha keys
        (0.0, 1), (1, 0.9),#red keys
        (0.0, 0.6),(1, 0.5), #green keys
        (0.0, 0.2), (1, 0.1),  #blue keys
        (0, 0.02), (1, 0),  #scale keys
        (0, 0, 0),         #emit box size
        (-1, 0.85, 0.3),               #emit velocity
        0.8,                      #emit dir randomness
        0,                     #rotation speed
        0                       #rotation damping
        ),
       ("musket_powder_a", psf_billboard_3d|psf_randomize_size|psf_next_effect_is_lod, "prtcl_dust_a",
        500, 4, 17, 0, 5, 40, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
        (0.0, 0.9), (0.75, 0.75),     #alpha keys
        (0.0, 0.95), (1, 0.95),          #red keys
        (0.0, 0.95),(1, 0.95),           #green keys
        (0.0, 1), (1, 1),          #blue keys
        (0, 1), (1, 5),  #scale keys
        (0, 0, 0),         #emit box size
        (-10, 0, 5),               #emit velocity
        0.0,                      #emit dir randomness
        100,                     #rotation speed
        0.2                       #rotation damping
        ),

       ("musket_powder_a_far", psf_billboard_3d|psf_randomize_size, "prtcl_dust_a",
        500, 4, 17, 0, 5, 40, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
        (0.0, 1), (0.75, 0.75),     #alpha keys
        (0.0, 0.95), (1, 0.95),          #red keys
        (0.0, 0.95),(1, 0.95),           #green keys
        (0.0, 1), (1, 1),          #blue keys
        (0, 1), (1, 5),  #scale keys
        (0, 0, 0),         #emit box size
        (-10, 0, 5),               #emit velocity
        0.0,                      #emit dir randomness
        100,                     #rotation speed
        0.2                       #rotation damping
        ),

		##### WATER HIT ######
		
		("water_hit_a", psf_billboard_3d | psf_randomize_size | psf_randomize_rotation | psf_global_emit_dir, "prtcl_splash_b",
        80, 1.5, 4, 0.8, 0, 0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
        (0.0, 1), (1, 0),     #alpha keys
        (0.0, 0.95), (1, 0.95),          #red keys
        (0.0, 0.90), (1, 0.90),           #green keys
        (0.0, 0.70), (1, 0.70),          #blue keys
        (0, 0.3), (1, 2),  #scale keys
        (0, 0, 0),         #emit box size
        (0, 0, 6),               #emit velocity
        0,                      #emit dir randomness
        100,                     #rotation speed
        0.2                       #rotation damping
        ),
		
		("water_hit_b",psf_randomize_size | psf_randomize_rotation | psf_turn_to_velocity|psf_global_emit_dir, "prtcl_splash_b",
      4, 3, 0, 0, 0, 0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
      (0.0, 1), (1, 0),     #alpha keys
      (0.0, 0.95), (1, 0.95),          #red keys
      (0.0, 0.90), (1, 0.90),           #green keys
      (0.0, 0.70), (1, 0.70),          #blue keys
      (0, 1), (1, 5),  #scale keys
      (0.1, 0.1, 0),         #emit box size
      (0, 0, -0.01),               #emit velocity
      0,                      #emit dir randomness
      25,                     #rotation speed
      0.15                       #rotation damping
    ),
#    ("cooking_fire", psf_billboard_3d|psf_global_emit_dir|psf_always_emit, "prtcl_fire",
#    50, 0.5, 0.2, -0.05, 30.0, 0.3,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
#    (0.5, 1), (1, 1),          #alpha keys
#     (0.5, 1.0), (1, 0.9),     #red keys
#     (0.5, 0.4), (1, 0.1),     #green keys
#     (0.5, 0.2), (1, 0.0),     #blue keys
#     (0.3, 0.9),   (0.9, 2),   #scale keys
#     (0.07, 0.07, 0.01),       #emit box size
#     (0, 0, 0.1),              #emit velocity
#     0.1                       #emit dir randomness
#    ),

     ("brazier_fire_1", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     25, 0.5, 0.1, 0.0, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.4), (1.0, 0),        #alpha keys
     (0.5, 1.0), (1.0, 0.9),      #red keys
     (0.5, 0.7),(1.0, 0.3),       #green keys
     (0.5, 0.2), (1, 0.0),      #blue keys
     (0.1, 0.2),   (1.0, 0.5),      #scale keys
     (0.1, 0.1, 0.01),        #emit box size
     (0.0, 0.0, 0.4),                 #emit velocity
     0.0,                       #emit dir randomness
     100,                       #rotation speed
     0.2                        #rotation damping
     ),
#              ("cooking_smoke", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_rotation|psf_randomize_size, "prt_mesh_steam_1",
#     3, 3.5, 0.4, -0.03, 10.0, 10.9,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
#     (0.4, 1), (1, 0),          #alpha keys
 #    (0.0, 0.6), (1, 0.3),      #red keys
#     (0.0, 0.6),(1, 0.3),       #green keys
#     (0.0, 0.6), (1, 0.3),      #blue keys
#     (0, 2.5),   (0.9, 7.5),    #scale keys
 #    (0.1, 0.1, 0.06),          #emit box size
 #    (0, 0, 1.3),               #emit velocity
#     0.2,                       #emit dir randomness
 #    200,                       #rotation speed
 #    0.2,                       #rotation damping
 #   ),

    ("cooking_fire_1", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     25, 0.35, 0.1, 0.03, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.8), (1, 0),        #alpha keys
     (0.5, 0.5*1.0), (1, 0.3*0.9),      #red keys
     (0.5, 0.5*0.7),(1, 0.3*0.3),       #green keys
     (0.5, 0.5*0.2), (1, 0.0),      #blue keys
     (0.1, 0.5),   (1, 1),      #scale keys
     (0.05, 0.05, 0.01),        #emit box size
     (0, 0, 1),                 #emit velocity
     0.0,                       #emit dir randomness
     200,                       #rotation speed
     0.0                        #rotation damping
     ),
    
    ("cooking_smoke", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_rotation|psf_randomize_size, "prt_mesh_smoke_1",
     4, 4, 0.1, 0, 3, 5, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.2, 0.20), (1.0, 0.0),          #alpha keys
     (0.0, 0.8), (1.0, 1.0),      #red keys
     (0.0, 0.8),(1.0, 1.0),      #green keys
     (0.0, 0.85), (1.0, 1.0),     #blue keys
     (0.0, 0.65),   (1.0, 3.0),        #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0.0, 0.0, 1.2),               #emit velocity
     0.0,                        #emit dir randomness
     0,
     0,
    ),

    ("food_steam", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_rotation|psf_randomize_size, "prt_mesh_steam_1",
     3, 1, 0, 0, 8.0, 1,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.1), (1, 0),        #alpha keys
     (0.0, 1), (1, 0.1),        #red keys
     (0.0, 1),(1, 0.1),         #green keys
     (0.0, 1), (1, 0.1),        #blue keys
     (0, 0.2),   (0.9, 0.5),      #scale keys
     (0.05, 0.05, 0),          #emit box size
     (0, 0, 0.1),               #emit velocity
     0,                         #emit dir randomness
     100,                       #rotation speed
     0.5,                       #rotation damping
    ),

    ("candle_light", psf_billboard_3d|psf_global_emit_dir|psf_always_emit, "prt_mesh_candle_fire_1",
     7, 1.1, 0.6, -0.0, 10.0, 0.2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.5), (1, 0),        #alpha keys
     (0.5, 1.0), (1, 0.9),      #red keys
     (0.5, 0.6), (1, 0.1),      #green keys
     (0.5, 0.2), (1, 0.0),      #blue keys
     (0.3, 0.2),   (1, 0.0),    #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0, 0, 0.09),              #emit velocity
      0,                        #emit dir randomness
      0,                        #rotation speed
      0                         #rotation damping
    ),
    ("candle_light_small", psf_billboard_3d|psf_global_emit_dir|psf_always_emit, "prt_mesh_candle_fire_1",
     4, 1.1, 0.6, -0.0, 10.0, 0.2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.8), (1, 0),        #alpha keys
     (0.5, 1.0), (1, 0.9),      #red keys
     (0.5, 0.6), (1, 0.1),      #green keys
     (0.5, 0.2), (1, 0.0),      #blue keys
     (0.3, 0.13),   (1, 0.0),   #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0, 0, 0.06),              #emit velocity
      0,                        #emit dir randomness
      0,                        #rotation speed
      0                         #rotation damping
    ),
    ("lamp_fire", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_rotation|psf_randomize_size, "prt_mesh_fire_1",
     10, 0.8, 0.6, -0.0, 10.0, 0.4,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.5), (1, 0),        #alpha keys
     (0.5, 1.0), (1, 0.9),      #red keys
     (0.5, 0.8), (1, 0.1),      #green keys
     (0.5, 0.4), (1, 0.0),      #blue keys
     (0.3, 0.35), (0.9, 0.5),    #scale keys
     (0.01, 0.01, 0.0),         #emit box size
     (0, 0, 0.35),               #emit velocity
     0.03,                      #emit dir randomness
     100,                       #rotation speed
     0.5,                       #rotation damping
    ),
#*-*-*-*-* D U M M Y *-*-*-*-#
    ("dummy_smoke", psf_billboard_3d|psf_randomize_size,  "prt_mesh_dust_1",
     500, 3, 15, -0.05, 10.0, 0.2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.5), (1, 0),        #alpha keys
     (0.1, 0.8), (1, 0.8),      #red keys
     (0.1, 0.7),(1, 0.7),       #green keys
     (0.1, 0.6), (1, 0.7),      #blue keys
     (0.0, 0.7),   (1, 2.2),    #scale keys
     (0.2, 0.2, 0.5),           #emit box size
     (0, 0, 0.05),               #emit velocity
     2,                         #emit dir randomness
     10,                        #rotation speed
     0.1,                       #rotation damping
    ),

    ("dummy_straw", psf_randomize_size | psf_randomize_rotation,  "prt_mesh_straw_1",
     500, 1, 2, 0.9, 10, 2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 1), (1, 1),          #alpha keys
     (0.1, 0.6), (1, 0.6),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.4), (1, 0.4),      #blue keys
     (0.0, 0.3),   (1, 0.3),    #scale keys
     (0.2, 0.2, 0.5),           #emit box size
     (0, 0, 0),                 #emit velocity
     2.3,                       #emit dir randomness
     200,                       #rotation speed
     0,                       #rotation damping
    ),

    ("dummy_smoke_big", psf_billboard_3d|psf_randomize_size,  "prt_mesh_dust_1",
     500, 9, 15, -0.05, 10.0, 0.2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.9), (1, 0),        #alpha keys
     (0.1, 0.8), (1, 0.8),      #red keys
     (0.1, 0.7),(1, 0.7),       #green keys
     (0.1, 0.6), (1, 0.7),      #blue keys
     (0.0, 5),   (1, 15.0),    #scale keys
     (3, 3, 5),           #emit box size
     (0, 0, 0.05),               #emit velocity
     2,                         #emit dir randomness
     10,                        #rotation speed
     0.1,                       #rotation damping
    ),

    ("dummy_straw_big", psf_randomize_size | psf_randomize_rotation,  "prt_mesh_straw_1",
     500, 3, 2, 2.0, 10, 2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 1), (1, 1),          #alpha keys
     (0.1, 0.6), (1, 0.6),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.4), (1, 0.4),      #blue keys
     (0.0, 0.8),   (1, 0.8),    #scale keys
     (3, 3, 3),           #emit box size
     (0, 0, 0),                 #emit velocity
     2.3,                       #emit dir randomness
     200,                       #rotation speed
     0,                       #rotation damping
    ),

#*-*-*-*-* D U M M Y  E N D *-*-*-*-#
#*-*-*-*-* GOURD *-*-*-*-#
    ("gourd_smoke", psf_billboard_3d|psf_randomize_size,  "prt_mesh_dust_1",
     500, 3, 15, -0.05, 10.0, 0.2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.5), (1, 0),        #alpha keys
     (0.1, 0.8), (1, 0.8),      #red keys
     (0.1, 0.7),(1, 0.7),       #green keys
     (0.1, 0.6), (1, 0.7),      #blue keys
     (0.0, 0.5),   (1, 1),    #scale keys
     (0.2, 0.2, 0.5),           #emit box size
     (0, 0, 0.05),               #emit velocity
     2,                         #emit dir randomness
     10,                        #rotation speed
     0.1,                       #rotation damping
    ),

    ("gourd_piece_1", psf_randomize_rotation,  "prt_gourd_piece_1",
     15, 1, 2, 0.9, 10, 2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 1), (1, 1),          #alpha keys
     (0.1, 0.6), (1, 0.6),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.4), (1, 0.4),      #blue keys
     (0.0, 1),   (1, 1),    #scale keys
     (0.2, 0.2, 0.5),           #emit box size
     (0, 0, 0),                 #emit velocity
     2.3,                       #emit dir randomness
     200,                       #rotation speed
     0,                       #rotation damping
    ),
    
    ("gourd_piece_2", psf_randomize_size | psf_randomize_rotation,  "prt_gourd_piece_2",
     50, 1, 2, 0.9, 10, 2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 1), (1, 1),          #alpha keys
     (0.1, 0.6), (1, 0.6),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.4), (1, 0.4),      #blue keys
     (0.0, 1),   (1, 1),    #scale keys
     (0.2, 0.2, 0.5),           #emit box size
     (0, 0, 0),                 #emit velocity
     2.3,                       #emit dir randomness
     200,                       #rotation speed
     0,                       #rotation damping
    ),

    
##    ("rat_particle", psf_global_emit_dir|psf_2d_turbulance | psf_randomize_size |psf_billboard_3d,  "rat_particle",
##     500, 4, 0, 0, 20, 10,      #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
##     (0.1, 1), (1, 1),          #alpha keys
##     (0.1, 0.6), (1, 0.6),      #red keys
##     (0.1, 0.5),(1, 0.5),       #green keys
##     (0.1, 0.4), (1, 0.4),      #blue keys
##     (0.1, 1),   (1, 1),        #scale keys
##     (0.1, 0.1, 0.1),           #emit box size
##     (0, 0, 0),                 #emit velocity
##     5,                         #emit dir randomness
##    ),

#*-*-*-**** BLOOD ****-*-*-*#
    
##("blood_hit_1", psf_billboard_3d | psf_randomize_size ,  "prt_mesh_blood_1",
##     5000, 0.5, 6, 0.5, 0, 0,        #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
##     (0.1, 1), (1, 0),          #alpha keys
##     (0.1, 0.6), (1, 0.6),      #red keys
##     (0.1, 0.5),(1, 0.5),       #green keys
##     (0.1, 0.4), (1, 0.4),      #blue keys
##     (0.0, 0.05),   (1, 0.05),  #scale keys
##     (0, 0.5, 0),               #emit box size
##     (0, -1, 0),                #emit velocity
##     1.5,                       #emit dir randomness
##     0,                         #rotation speed
##     0,                         #rotation damping
##    ),
##    #("blood_hit_2", 0 ,  "prt_mesh_blood_2",
##    # 500, 0.3, 0,0, 0, 0,       #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
##    # (0.1, 1), (1, 0.0),        #alpha keys
##    # (0.1, 0.6), (1, 0.6),      #red keys
##    # (0.1, 0.5),(1, 0.5),       #green keys
##    # (0.1, 0.4), (1, 0.4),      #blue keys
##    # (0.0, 0.4),   (1, 2),      #scale keys
##    # (0.0, 0.0, 0.0),           #emit box size
##    # (0, -0.1, 0),              #emit velocity
##    # 0,                         #emit dir randomness
##    # 0,                         #rotation speed
##    # 0,                         #rotation damping
##    # ),
##    ("blood_hit_3", psf_billboard_3d | psf_randomize_size ,  "prt_mesh_blood_3",
##     500, 0.3, 1,0.0, 0, 0,        #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
##     (0.1, 1), (1, 0.0),        #alpha keys
##     (0.1, 0.6), (1, 0.6),      #red keys
##     (0.1, 0.5),(1, 0.5),       #green keys
##     (0.1, 0.4), (1, 0.4),      #blue keys
##     (0.0, 0.2),   (1, 0.8),    #scale keys
##     (0.0, 0.3, 0.0),           #emit box size
##     (0, 1, 0),                 #emit velocity
##     1,                         #emit dir randomness
##     250,                       #rotation speed
##     0,                       #rotation damping
##     ),
    
#*-*-*-**** BLOOD  END ****-*-*-*#

#-*-*-*- Fire Fly Deneme *-*-*-*-#    
     ("fire_fly_1", psf_billboard_3d|psf_global_emit_dir|psf_always_emit, "prt_sparks_mesh_1",
     2, 5, 1.2, 0, 50, 7,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.8), (1, 0.2),        #alpha keys
     (0.5, .7), (1, 0.7),      #red keys
     (0.5, 0.8), (1, 0.8),      #green keys
     (0.5, 1), (1, 1),      #blue keys
     (0, 0.1),   (1, 0.1),    #scale keys
     (20, 20, 0.5),             #emit box size
     (0, 0, 0),              #emit velocity
      5,                        #emit dir randomness
      0,                        #rotation speed
      0                         #rotation damping
       ),
     ("bug_fly_1", psf_billboard_2d | psf_always_emit, "prt_mesh_rose_a",
     20, 8, 0.02, 0.025, 1, 5,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 1), (1, 1),        #alpha keys
     (0, 0.5), (1, 0.5),      #red keys
     (0, 0.5), (1, 0.5),      #green keys
     (0, 0.5), (1, 0.5),      #blue keys
     (0, 0.25),   (1, 0.25),    #scale keys
     (10, 5, 0.1),             #emit box size
     (0, 0, -0.9),              #emit velocity
      0.01,                        #emit dir randomness
      10,                        #rotation speed
      0,                         #rotation damping
    ),
#-*-*-*- Fire Fly End*-*-*-*-#
#-*-*-*- Moon Beam *-*-*-*-*-*-*#
    ("moon_beam_1", psf_billboard_2d|psf_global_emit_dir|psf_always_emit|psf_randomize_size, "prt_mesh_moon_beam",#prt_mesh_moon_beam
     2, 4, 1.2, 0, 0, 0,          #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 1), (1, 0),            #alpha keys
     (0, 0.4), (1, 0.4),                #red keys
     (0, 0.5), (1, 0.5),                #green keys
     (0, 0.6), (1, 0.6),                #blue keys
     (0, 2),   (1, 2.2),        #scale keys
     (1, 1, 0.2),                 #emit box size
     (0, 0, -2),                     #emit velocity
      0,                            #emit dir randomness
      100,                          #rotation speed
      0.5,                          #rotation damping
       ),
     ("moon_beam_paricle_1", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size, "prt_sparks_mesh_1",
     10, 1.5, 1.5, 0, 10, 10,            #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 1), (1, 0.0),            #alpha keys
     (0.5, .5), (1, 0.5),           #red keys
     (0.5, 0.7), (1, 0.7),          #green keys
     (0.5, 1), (1, 1),              #blue keys
     (0, 0.1),   (1, 0.1),        #scale keys
     (1, 1, 4),                 #emit box size
     (0, 0, 0),                     #emit velocity
      0.5,                            #emit dir randomness
      0,                            #rotation speed
      0                             #rotation damping
       ),
#-*-*-*- Moon Beam End *-*-*-*-*-*-*#
#-*-*-*- Stone Smoke *-*-*-*-*-*-*#
("stone_hit_1", psf_billboard_3d | psf_randomize_size | psf_randomize_rotation,  "prt_mesh_dust_1",
    5000, 0.5, 6, 0.1, 0, 0,       #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
    (0.1, .2), (1, 0),             #alpha keys
    (0.5, 0.7), (1, 0.7),          #red keys
    (0.5, 0.6), (1, 0.6),          #green keys
    (0.5, 0.6), (1, 0.6),          #blue keys
    (0.0, .2),   (1, 0.7),         #scale keys
    (0, 0.3, 0),                   #emit box size
    (0, 0, 0),                     #emit velocity
    1.1,                           #emit dir randomness
    200,                           #rotation speed
    0.8,                           #rotation damping
   ),
#-*-*-*- Stone Smoke END -*-*-*-*-*#
    ("night_smoke_1", psf_billboard_3d|psf_global_emit_dir|psf_always_emit, "prt_mesh_dust_1",
     5, 10, 1.5, 0, 50, 2,      #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.3, 0.1), (1, 0),        #alpha keys
     (0.5, 0.5), (1, 0.5),      #red keys
     (0.5, 0.5), (1, 0.5),      #green keys
     (0.5, 0.5), (1, 0.6),      #blue keys
     (0, 10),   (1, 10),        #scale keys
     (25, 25, 0.5),               #emit box size
     (0, 1, 0),                 #emit velocity
      2,                        #emit dir randomness
      20,                       #rotation speed
      1                         #rotation damping
       ),
#-*-*-*- Fire For Fireplace -*-*-*-#
    ("fireplace_fire_small", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     25, 0.8, 0.2, -0.1, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.5), (1, 0),        #alpha keys
     (0.5, 1.0), (1, 0.9),      #red keys
     (0.5, 0.7),(1, 0.3),       #green keys
     (0.5, 0.2), (1, 0.0),      #blue keys
     (0, 0.2),   (1, 0.7),   #scale keys
     (0.2, 0.1, 0.01),      #emit box size
     (0, 0, 0.2),               #emit velocity
     0.1,                       #emit dir randomness
     100,                       #rotation speed
     0.5                        #rotation damping
    ),
    ("fireplace_fire_big", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     35, 0.6, 0.2, -0.2, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.5), (1, 0),        #alpha keys
     (0.5, 1.0), (1, 0.9),      #red keys
     (0.5, 0.7),(1, 0.3),       #green keys
     (0.5, 0.2), (1, 0.0),      #blue keys
     (0, 0.4),   (1, 1),   #scale keys
     (0.4, 0.2, 0.01),            #emit box size
     (0, 0, 0.4),               #emit velocity
     0.1,                       #emit dir randomness
     100,                       #rotation speed
     0.5                        #rotation damping
    ),  
#-*-*-*- Fire For Fireplace -*-*-*-#
#-*-*-*- Village Fire *-*-*-*-#
    ("village_fire_big", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     50, 1.0, 0, -1.2, 25.0, 10.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.2, 0.7), (1, 0),        #alpha keys
     (0.2, 1.0), (1, 0.9),      #red keys
     (0.2, 0.7),(1, 0.3),       #green keys
     (0.2, 0.2), (1, 0.0),      #blue keys
     (0, 2),   (1, 6),          #scale keys
     (2.2, 2.2, 0.2),           #emit box size
     (0, 0, 0.0),               #emit velocity
     0.0,                       #emit dir randomness
     250,                       #rotation speed
     0.3                        #rotation damping
    ),
    ("village_fire_smoke_big", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_smoke_1",
     30, 2, 0.3, -1, 50.0, 10.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.15), (1, 0),        #alpha keys
     (0.2, 0.4), (1, 0.2),      #red keys
     (0.2, 0.4),(1, 0.2),       #green keys
     (0.2, 0.4), (1, 0.2),      #blue keys
     (0, 6),   (1, 8),          #scale keys
     (2, 2, 1),           #emit box size
     (0, 0, 5),               #emit velocity
     0.0,                       #emit dir randomness
     0,                       #rotation speed
     0.1                        #rotation damping
    ), 
    ("map_village_fire", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     20, 1.0, 0, -0.2, 3.0, 3.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.2, 0.7), (1, 0),        #alpha keys
     (0.2, 1.0), (1, 0.9),      #red keys
     (0.2, 0.7),(1, 0.3),       #green keys
     (0.2, 0.2), (1, 0.0),      #blue keys
     (0, 0.15),   (1, 0.45),    #scale keys
     (0.2, 0.2, 0.02),           #emit box size
     (0, 0, 0.0),               #emit velocity
     0.0,                       #emit dir randomness
     250,                       #rotation speed
     0.3                        #rotation damping
    ),
    ("map_village_fire_smoke", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_smoke_1",
     25, 2.5, 0.3, -0.15, 3.0, 3.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.15), (1, 0),       #alpha keys
     (0.2, 0.4), (1, 0.3),      #red keys
     (0.2, 0.4),(1, 0.3),       #green keys
     (0.2, 0.4), (1, 0.3),      #blue keys
     (0, 0.6),   (1, 0.9),      #scale keys
     (0.2, 0.2, 0.1),           #emit box size
     (0, 0, 0.03),              #emit velocity
     0.0,                       #emit dir randomness
     0,                         #rotation speed
     0.1                        #rotation damping
    ), 
    ("map_village_looted_smoke", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_smoke_1",
     20, 3, 0.3, -0.11, 3.0, 2.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.15), (1, 0),       #alpha keys
     (0.2, 0.5), (1, 0.5),      #red keys
     (0.2, 0.5),(1, 0.5),       #green keys
     (0.2, 0.5), (1, 0.5),      #blue keys
     (0, 0.7),   (1, 1.3),      #scale keys
     (0.2, 0.2, 0.1),           #emit box size
     (0, 0, 0.015),             #emit velocity
     0.0,                       #emit dir randomness
     0,                         #rotation speed
     0.1                        #rotation damping
    ), 
##### Dungeon Water Drops #####
    ("dungeon_water_drops", psf_billboard_2d|psf_global_emit_dir|psf_always_emit, "prtcl_rain",
     1, 1, 0.33, 0.8, 0, 0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (1.0, 0.2), (1, 0.2),      #alpha keys
     (1.0, 1.0), (1, 1.0),      #red keys
     (1.0, 1.0), (1, 1.0),      #green keys
     (1.0, 1.0), (1, 1.0),      #blue keys
     (1.0, 0.8),   (1.0, 0.8),  #scale keys
     (0.05, 0.05, 0.5),         #emit box size
     (0, 0, -5.0),              #emit velocity
     0.0,                       #emit dir randomness
     0,                         #rotation speed
     0,                         #rotation damping
     ), 
##### Dungeon Water Drops  END #####
    ("wedding_rose", psf_billboard_2d | psf_always_emit, "prt_mesh_rose_a",
     50, 8, 0.02, 0.025, 1, 5,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 1), (1, 1),        #alpha keys
     (0, 0.5), (1, 0.5),      #red keys
     (0, 0.5), (1, 0.5),      #green keys
     (0, 0.5), (1, 0.5),      #blue keys
     (0, 0.25),   (1, 0.25),    #scale keys
     (4, 4, 0.1),             #emit box size
     (0, 0, -0.9),              #emit velocity
      0.01,                        #emit dir randomness
      10,                        #rotation speed
      0,                         #rotation damping
    ),
    ("sea_foam_a", psf_turn_to_velocity | psf_always_emit|psf_randomize_size, "prt_foam_a",
     1, 3.0, 1, 0.0, 0.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.7, 0.1), (1, 0.0),        #alpha keys
     (1.0, 1.0), (1, 1.0),      #red keys
     (1.0, 1.0), (1, 1.0),      #green keys
     (1.0, 1.0), (1, 1.0),      #blue keys
     (0.0, 4),   (1.0, 4.5),   #scale keys
     (10.0, 1.0, 0),           #emit box size
     (0, 1, 0),                 #emit velocity
     0.0,                       #emit dir randomness
     0,                       #rotation speed
     0.5                        #rotation damping
    ),
    ("fall_leafs_a", psf_billboard_2d | psf_always_emit, "prt_mesh_yrellow_leaf_a",
     1, 9, 0, 0.025, 4, 4,      #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 1), (1, 1),            #alpha keys
     (0, 0.5), (1, 0.5),        #red keys
     (0, 0.5), (1, 0.5),        #green keys
     (0, 0.5), (1, 0.5),        #blue keys
     (0, 0.25),   (1, 0.25),    #scale keys
     (4, 4, 4),                 #emit box size
     (0, 0.01, -0.9),           #emit velocity
      0.02,                     #emit dir randomness
      15,                       #rotation speed
      0,                        #rotation damping
    ),
("items_fire", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     400, 0.35, 0.2, 0.03, 00.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.8), (1, 0),        #alpha keys
     (0.5, 0.2), (1, 0.0),      #red keys
     (0.5, 0.7),(1, 0.3),       #green keys
     (0.5, 1.0), (1, 0.9),      #blue keys
     (0, 0.15),   (0.4, 0.3),   #scale keys
     (0.03, 0.8, 0.03),      #emit box size
     (0, 0, 0.5),               #emit velocity
     0.0,                       #emit dir randomness
     2000,                       #rotation speed
     0.5                        #rotation damping
    ),
("items_fire_red", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     150, 0.35, 0.2, 0.0, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.5), (1.0, 0.0),
     (0.5, 1.0), (1.0, 0.9),
     (0.5, 0.3), (1.0, 0.2),
     (0.5, 0.1), (1.0, 0.1),
     (0, 0.15),   (0.4, 0.3),   #scale keys
     (0.03, 0.8, 0.03),      #emit box size
     (0, 0, 0.5),               #emit velocity
     0.0,                       #emit dir randomness
     2000,                       #rotation speed
     0.0                        #rotation damping
    ),
  
("items_fire_blue", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     150, 0.35, 0.2, 0.0, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.5), (1, 0),        #alpha keys
     (0.5, 0.0), (1, 0.25),      #red keys
     (0.5, 0.28),(1, 1.0),       #green keys
     (0.5, 0.97), (1, 0.0),      #blue keys
     (0, 0.15),   (0.4, 0.3),   #scale keys
     (0.03, 0.8, 0.03),      #emit box size
     (0, 0, 0.5),               #emit velocity
     0.0,                       #emit dir randomness
     50,                       #rotation speed
     0.0                        #rotation damping
    ),
  

     ("aurora_blade_lightning", psf_turn_to_velocity|psf_randomize_rotation|psf_randomize_size, "prt_lightning",
      50, 0.35, 0.0, 0.0, 10.0, 0.0,
      (0.66, 0.7), (1.0, 0.0),
      (0.1, 0.7), (1.0, 0.5),
      (0.1, 0.5), (1.0, 0.5),
      (0.1, 0.1), (1.0, 0.7),
      (0.1, 0.2), (1.0, 0.6),
      (0.2, 0.2, 0.2),
      (0.1, 0.3, 0.1),
      1.0,
      20.0,
      0.5
     ),
  
  
    ("frostfang_snowflake", psf_always_emit|psf_global_emit_dir|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_Snowflake_a",
     150, 0.35, 140.0, 0.03, 10.0, 0.0,
     (0.5, 0.8), (1.0, 0.0),
     (0.5, 0.6), (1.0, 0.0),
     (0.5, 0.88), (1.0, 0.0),
     (0.5, 1.0), (1.0, 0.0),
     (0.0, 0.0), (1.0, 0.15),
     (0.05, 0.55, 0.05),
     (0.1, 0.1, 0.1),
     0.05,
     150.0,
     0.5
     ),
    ("frostfang_smoke", psf_always_emit|psf_global_emit_dir|psf_billboard_3d, "prtcl_dust_a",
     60, 0.5, 0.2, -0.1, 10.0, 0.1,
     (0.5, 1.0), (1.0, 0.5),
     (0.0, 0.19), (1.0, 0.0),
     (0.0, 0.6), (1.0, 0.0),
     (0.0, 1.0), (1.0, 0.0),
     (0.0, 0.1), (0.8, 1.0),
     (0.05, 0.55, 0.05),
     (0.0, 0.0, 0.0),
     0.1,
     0.0,
     0.0
     ),
       
  ("item_blood", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_blood_3",
     3, 1.5, 0.0, -0.11, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength   inc particles
     (0.5, 0.5), (1, 0),        #alpha keys
     (0.5, 1), (1, 0.9),      #red keys
     (0.5, 0.1),(1, 0.0),       #green keys
     (0.5, 0.0), (1, 0.0),      #blue keys
     (0, 0.5),   (1, 2),   #scale keys    change 
     (0.5, 0.5, 0.2),            #emit box size  change from 3 3 to 1 1
     (0, 0, 0),               #emit velocity
     0.1,                       #emit dir randomness
     100,                       #rotation speed
     0.5                        #rotation damping
    ),
     
  ("item_blood_Drop", psf_always_emit|psf_global_emit_dir|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_Drop_a",
     100, 2.0, 3.0, 0.5, 10.0, 10.0,
     (0.0, 1.0), (0.35, 0.0),
     (1.0, 1.0), (1.0, 1.0),
     (1.0, 1.0), (1.0, 1.0),
     (1.0, 1.0), (1.0, 1.0),
     (1.0, 0.05), (1.0, 0.05),
     (0.0, 0.1, 0.0),
     (0.0, 0.0, 0.0),
     0.05,
     50.0,
     0.5
     ),
     
  ("item_poison_Drop", psf_always_emit|psf_global_emit_dir|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_Drop_a",
     20, 2.0, 3.0, 0.5, 10.0, 10.0,
     (0.1, 0.5), (1, 0),        #alpha keys
     (0.1, 0.1), (1, 0.1),      #red keys
     (0.1, 1.0),(1, 0.9),       #green keys
     (0.1, 0.1), (1, 0.1),      #blue keys
     (1.0, 0.05), (1.0, 0.05),
     (0.0, 0.1, 0.0),
     (0.0, 0.0, 0.0),
     0.05,
     50.0,
     0.5
     ),

     
    ("mjolnir_lightning", psf_always_emit|psf_global_emit_dir|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_lightning",
     50, 0.3, 1.0, -0.03, 10.0, 0.0,
     (0.5, 1.0), (1.0, 0.0),
     (0.5, 1.0), (1.0, 0.98),
     (0.5, 0.54), (1.0, 0.59),
     (0.5, 0.32), (1.0, 0.38),
     (0.0, 0.7), (1.0, 2.5),
     (0.08, 0.95, 0.08),
     (0.1, 0.1, 0.1),
     0.1,
     10.0,
     0.5
     ),

("items_fire_white", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     150, 0.35, 0.2, 0.03, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.8), (1, 0),        #alpha keys
     (0.5, .8), (1, 0.6),        #red keys
     (0.5, .8), (1, 0.6),       #green keys
     (0.5, 1), (1, 0.6),      #blue keys
     (0, 0.15),   (0.4, 0.3),   #scale keys
     (0.03, 0.8, 0.03),      #emit box size
     (0, 0, 0.0),               #emit velocity
     0.0,                       #emit dir randomness
     1500,                       #rotation speed
     0.5                        #rotation damping
    ),
    
    
    ("cannon_fire", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     100, 0.35, 0.2, 0.03, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.8), (1, 0),        #alpha keys
     (0.5, 1.0), (1, 0.9),      #red keys
     (0.5, 0.7),(1, 0.3),       #green keys
     (0.5, 0.2), (1, 0.0),      #blue keys
     (0, 0.45),   (1.2, 0.9),   #scale keys
     (0.12, 0.12, 0.03),      #emit box size
     (0, 0, 0.5),               #emit velocity
     0.0,                       #emit dir randomness
     200,                       #rotation speed
     0.5                        #rotation damping
    ), 
    
      ("arrows_fire_big", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     50, 0.5, 0.0, -1.20, 25.0, 10.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.2, 0.7), (1, 0),        #alpha keys
     (0.2, 1.0), (1, 0.9),      #red keys
     (0.2, 0.7),(1, 0.3),       #green keys
     (0.2, 0.2), (1, 0.0),      #blue keys
     (0, 2),   (1, 6),          #scale keys
     (2.7, 2.7, 1.0),           #emit box size
     (0, 0, 0),               #emit velocity
     0.0,                       #emit dir randomness
     250,                       #rotation speed
     0.3                        #rotation damping
    ),
    
      ("arrows_fire_smoke_big", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_smoke_1",
     30, 2, 0.3, -1.0, 50.0, 10.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.15), (1, 0),        #alpha keys
     (0.2, 0.4), (1, 0.2),      #red keys
     (0.2, 0.4),(1, 0.2),       #green keys
     (0.2, 0.4), (1, 0.2),      #blue keys
     (0, 6),   (1, 8),          #scale keys
     (2.7, 2.7, 1.0),           #emit box size
     (0, 0, 5.0),               #emit velocity
     0.0,                       #emit dir randomness
     0,                       #rotation speed
     0.1                        #rotation damping
    ),

      ("arrows_fire_small", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     10, 0.5, 0.0, -1.20, 25.0, 10.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.2, 0.7), (1, 0),        #alpha keys
     (0.2, 1.0), (1, 0.9),      #red keys
     (0.2, 0.7),(1, 0.3),       #green keys
     (0.2, 0.2), (1, 0.0),      #blue keys
     (0, 2),   (1, 6),          #scale keys
     (0.65, 0.65, 0.05),           #emit box size
     (0, 0, 0),               #emit velocity
     0.0,                       #emit dir randomness
     250,                       #rotation speed
     0.3                        #rotation damping
    ),
      ("arrows_fire_smoke_small", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_smoke_1",
     20, 2, 0.3, -1.0, 50.0, 10.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.15), (1, 0),        #alpha keys
     (0.2, 0.4), (1, 0.2),      #red keys
     (0.2, 0.4),(1, 0.2),       #green keys
     (0.2, 0.4), (1, 0.2),      #blue keys
     (0, 6),   (1, 8),          #scale keys
     (0.9, 0.9, 1.0),           #emit box size
     (0, 0, 5.0),               #emit velocity
     0.0,                       #emit dir randomness
     0,                       #rotation speed
     0.1                        #rotation damping
    ),
             
	("bomb_fire_big", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     300, 2.3, 0.25, -0.08, 3, 40.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.2, 1), (1, 0),        #alpha keys
     (0.2, 1.0), (1, 0.9),      #red keys
     (0.2, 0.7),(1, 0.3),       #green keys
     (0.2, 0.2), (1, 0.0),      #blue keys
     (0, 0.5),   (1, 2),          #scale keys
     (1.8, 1.8, 1.8),           #emit box size
     (0, 0, 0.0),               #emit velocity
     0.0,                       #emit dir randomness
     250,                       #rotation speed
     0.3                        #rotation damping
    ),	
    
	("bomb_fire_1", psf_billboard_3d|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     10, 1, 6, 0.0, 0.0, 0.0,  #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 1.0), (1, 0.0),          #alpha keys
     (0.0, 1.0), (1, 1),          #red keys
     (0.0, 0.6), (1, 0.6),          #green keys
     (0.0, 0.2), (1, 0.1),          #blue keys
     (0, 1.5),   (1, 4),            #scale keys
     (0.5, 0.5, 2),                 #emit box size
     (0, 0, 8),                     #emit velocity
     5,                             #emit dir randomness
     200,                           #rotation speed
     0.2                           #rotation damping
    ), 

	("bomb_fire_2", psf_global_emit_dir|psf_turn_to_velocity, "prt_mesh_fire_2",
     60, 0.2, 0 , 0.0, 0.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 1.0), (1, 1.0),        #alpha keys
     (0.0, 1.0), (1, 1.0),      #red keys
     (0.0, 1.0), (1, 1.0),       #green keys
     (0.0, 1.0), (1, 1.0),      #blue keys
     (0, 10),   (1, 25),          #scale keys
     (0.1, 0.1, 0.1),           #emit box size
     (0, 0, 0.5),               #emit velocity
     0,                       #emit dir randomness
     0,                       #rotation speed
     0.0                        #rotation damping
    ), 
    
        ("bomb_smoke", psf_billboard_3d|psf_global_emit_dir|psf_randomize_size|psf_randomize_rotation, "prt_mesh_smoke_1",
     10, 3, 6, 0.3, 2.0, 50.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 0.35), (1, 0),        #alpha keys
     (0, 0.75), (1, 0.2),      #red keys
     (0, 0.70),(1, 0.2),       #green keys
     (0, 0.60), (1, 0.2),      #blue keys
     (0, 3),(0.75, 18),          #scale keys
     (0.5, 0.5, 2),           #emit box size
     (0, 0, 22),               #emit velocity
     6,                       #emit dir randomness
     75,                       #rotation speed
     0.3                        #rotation damping
    ), 
    
    ("bomb_dust", psf_randomize_size|psf_randomize_rotation|psf_billboard_3d, "shrapnel",#prt_mesh_dust_1
     20, 3,  0, 2, 0, 0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 1), (1, 1),        #alpha keys
     (0, 0.5), (1, 0.5),        #red keys
     (0, 0.5),(1, 0.5),         #green keys
     (0, 0.5),(1, 0.5),         #blue keys
     (0.0, 0.5),   (1.0, 0.2),   #scale keys
     (0.2, 0.2, 2),           #emit box size
     (0, 0, 12),                 #emit velocity
     4,                         #emit dir randomness
     150,                       #rotation speed
     0                       #rotation damping
    ),
    
    ("explosive_explosion_sparks_a", psf_billboard_3d|psf_randomize_size,  "prt_sparks_mesh_1",
     20, 0.15, 0.4, 0.2, 3, 10,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.6, 1), (0.7, 0),          #alpha keys
     (1.0, 1.0), (1, 0),      #red keys
     (1.0, 0.7),(0.3, 0),       #green keys
     (0.0, 0.0), (0.0, 0),      #blue keys
     (0, 40.0), (0.3, 0.3),    #scale keys
     (0.5, 0.5, 0.5),           #emit box size
     (0.5, 0.5, 0.5),                 #emit velocity
     30.0,                       #emit dir randomness
    ),

    ("explosive_explosion_sparks_b", psf_billboard_3d|psf_randomize_size,  "prt_sparks_mesh_1",
     20, 0.3, 0.4, 0.2, 3, 10,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.6, 1), (0.7, 0),          #alpha keys
     (1.0, 1.0), (1, 0),      #red keys
     (0.7, 0.5),(0.3, 0),       #green keys
     (0.0, 0.0), (0.0, 0),      #blue keys
     (0, 40.0), (0.3, 0.3),    #scale keys
     (0.5, 0.5, 0.5),           #emit box size
     (0.5, 0.5, 0.5),                 #emit velocity
     30.0,                       #emit dir randomness
    ),

    ("explosive_explosion_smoke", psf_billboard_3d|psf_randomize_size, "prtcl_dust_a",
     90, 10, 0.6, -0.2, 60.0, 1.5,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 1.0), (0.7, 0.5),       #alpha keys
     (0.0, 0.4), (0.3, 0.2),      #red keys
     (0.0, 0.4),(0.3, 0.2),       #green keys
     (0.0, 0.4), (0.3, 0.2),      #blue keys
     (0, 5),   (25, 60.0),   #scale keys
     (0.1, 0.1, 0.1),           #emit box size
     (2, 2, 0.0),                 #emit velocity
     0.1                        #emit dir randomness
    ),
    
        ("musket_hit", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation| psf_global_emit_dir, "prtcl_dust_a",
        500, 3, 8, 0.2, 2, 20, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
        (0.0, 1), (1, 0),     #alpha keys
        (0.0, 0.95), (1, 0.95),          #red keys
        (0.0, 0.90), (1, 0.90),           #green keys
        (0.0, 0.70), (1, 0.70),          #blue keys
        (0, 3), (0.8, 5),  #scale keys
        (0, 0, 0),         #emit box size
        (0, 0, 10),               #emit velocity
        3,                      #emit dir randomness
        100,                     #rotation speed
        0.2                       #rotation damping
        ),
		
		("musket_hit_particle", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation| psf_global_emit_dir, "prt_mesh_mud_1",
		2000, 2, 0.2, 2, 0, 0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
        (0.0, 1), (1, 1),     #alpha keys
        (0.0, 0.1), (1, 0.1),          #red keys
        (0.0, 0.1), (1, 0.1),           #green keys
        (0.0, 0.1), (1, 0.1),          #blue keys
        (0.0, 0.125), (0.8, 0.125),  #scale keys
        (0, 0, 0),         #emit box size
        (0, 0, 8),               #emit velocity
        3,                      #emit dir randomness
        100,                     #rotation speed
        0.1                       #rotation damping
        ),
		
		("musket_hit_objects", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation, "prtcl_dust_a",
        500, 3.5, 6, 0, 2, 40, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
        (0.0, 1), (1, 0),     #alpha keys
        (0.0, 0.95), (1, 0.95),          #red keys
        (0.0, 0.90), (1, 0.90),           #green keys
        (0.0, 0.80), (1, 0.80),          #blue keys
        (0, 1), (0.75, 10),  #scale keys
        (0, 0, 0),         #emit box size
        (0, -15, 0),               #emit velocity
        1,                      #emit dir randomness
        100,                     #rotation speed
        0.2                       #rotation damping
        ),

#Chronicles of Talera

    ("massive_fire", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     70, 3.0, 0.0, -1.3, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.5), (1, 0),        #alpha keys
     (0.5, 1.0), (1, 0.9),      #red keys
     (0.5, 0.7),(1, 0.3),       #green keys
     (0.5, 0.2), (1, 0.0),      #blue keys
     (0, 4.0),   (1, 10),   #scale keys
     (3.0, 3.0, 0.2),            #emit box size
     (0, 0, 0.4),               #emit velocity
     0.1,                       #emit dir randomness
     250,                       #rotation speed
     0.5                        #rotation damping
    ),

  ("massive_green_fire", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     50, 2.0, 0.0, -0.11, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength   inc particles
     (0.5, 0.5), (1, 0),        #alpha keys
     (0.5, 0.7), (1, 0.3),      #red keys
     (0.5, 1.0),(1, 0.9),       #green keys
     (0.5, 0.7), (1, 0.3),      #blue keys
     (0, 4.0),   (1, 10),   #scale keys    change 
     (1.0, 1.0, 0.2),            #emit box size  change from 3 3 to 1 1
     (0, 0, 0.015),               #emit velocity
     0.1,                       #emit dir randomness
     250,                       #rotation speed
     0.5                        #rotation damping
    ),

    ("gladeborn_arrow", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     50, 0.35, 0.2, 0.03, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.8), (1, 0),        #alpha keys
     (0.5, 1.0), (1, 0.9),       #red keys    # old red (0.5, 1.0), (1, 0.9),   inc front .2 back .2  looks good (0.5, 0.8), (1, 0.6),
     (0.5, 0.7),(1, 0.3),       #green keys
     (0.5, 1.0), (1, 0.9),      #blue keys    # old blue (0.5, 0.2), (1, 0.0),
     (0, 0.15),   (0.4, 0.3),   #scale keys
     (0.04, 0.04, 0.01),      #emit box size
     (0, 0, 0.5),               #emit velocity
     0.0,                       #emit dir randomness
     200,                       #rotation speed
     0.5                        #rotation damping
    ),

  

    
   ("waterfall", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation, "prtcl_splash_b",
     75, 2.5, 0.7, 0.8, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.8), (1, 0),        #alpha keys
     (0.5, 1.0), (1, 1.0),      #red keys
     (0.5, 0.7), (1, 0.3),      #green keys
     (0.5, 1.0), (1, 1.0),      #blue keys
     (0.0, 3.0),   (10.0, 7.0),   #scale keys
     (1.0, 1.0, 0.25),           #emit box size
     (0, 1.9, 1.6),               #emit velocity
     0.1,                       #emit dir randomness
     50,                       #rotation speed
     0.5                        #rotation damping
    ),
    ("planestep", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_smoke_1",
     50, 2.0, 0.0, -0.11, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength   inc particles
     (0.5, 0.8), (1, 0),        #alpha keys
     (0.5, 1.0), (1, 0.9),       #red keys    # old red (0.5, 1.0), (1, 0.9),   inc front .2 back .2  looks good (0.5, 0.8), (1, 0.6),
     (0.5, 0.7),(1, 0.3),       #green keys
     (0.5, 1.0), (1, 0.9),      #blue keys    # old blue (0.5, 0.2), (1, 0.0),
     (0, 4.0),   (1, 10),   #scale keys    change 
     (1.0, 1.0, 0.2),            #emit box size  change from 3 3 to 1 1
     (0, 0, 0.015),               #emit velocity
     0.1,                       #emit dir randomness
     250,                       #rotation speed
     0.5                        #rotation damping
    ),
  ("blightlord_aura", psf_always_emit|psf_global_emit_dir|psf_billboard_3d, "copy_prt_shield",
     30, 1, 120.0, 0.0, 0.0, 0.1,
     (0.5, 0.5), (1, 0.5),        #alpha keys
     (0.5, 0.0), (1, 0.0),      #red keys
     (0.5, 0.4),(1, 0.4),       #green keys
     (0.5, 0.8), (1, 0.8),      #blue keys
     (0, 1.5),   (1.0, 1.5),   #scale keys
     (0.0, 0.0, 0.0),
     (0.0, 0.0, 0.0),
     0.0,
     0.0,
     0.0
    ),

  ("holy_light_aura", psf_always_emit|psf_global_emit_dir|psf_billboard_3d, "copy_prt_shield",
     30, 1, 120.0, 0.0, 0.0, 0.1,
     (0, 0.5), (1, 0.5),          #alpha keys
     (0.0, 1), (1, 1),      #red keys
     (0.0, 1),(1, 1),      #green keys
     (0.0, 0), (1, 0),     #blue keys
     (0, 1.5),   (1.0, 1.5),   #scale keys
     (0.0, 0.0, 0.0),
     (0.0, 0.0, 0.0),
     0,                         #emit dir randomness
     0,                       #rotation speed
     0                        #rotation damping
    ),
        
  ("rage_light_aura", psf_always_emit|psf_global_emit_dir|psf_billboard_3d, "copy_prt_shield",
     30, 1, 120.0, 0.0, 0.0, 0.1,
     (0, 0.25), (1, 0),          #alpha keys
     (0.5, 1), (1, 0.9),      #red keys
     (0.5, 0.1),(1, 0.0),       #green keys
     (0.5, 0.0), (1, 0.0),      #blue keys
     (0, 1.5),   (1.0, 1.5),   #scale keys
     (0.0, 0.0, 0.0),
     (0.0, 0.0, 0.0),
     0,                         #emit dir randomness
     0,                       #rotation speed
     0                        #rotation damping
    ),
        
  ("green_light_aura", psf_always_emit|psf_global_emit_dir|psf_billboard_3d, "copy_prt_shield",
     30, 1, 120.0, 0.0, 0.0, 0.1,
     (0, 0.25), (1, 0),          #alpha keys
     (0.5, 0.0), (1, 0.0),      #red keys
     (0.5, 1.0),(1, 0.0),       #green keys
     (0.5, 0.0), (1, 0.0),      #blue keys
     (0, 1.5),   (1.0, 1.5),   #scale keys
     (0.0, 0.0, 0.0),
     (0.0, 0.0, 0.0),
     0,                         #emit dir randomness
     0,                       #rotation speed
     0                        #rotation damping
    ),
        
    ("stoneskin_aura", psf_always_emit|psf_global_emit_dir|psf_billboard_3d, "prt_AT_FIELD_a",
     1, 1, 120.0, 0.0, 0.0, 0.1,
     (0.0, 1.0), (1.0, 1.0),
     (0.0, 1.0), (1.0, 0.9),
     (0.0, 0.3), (1.0, 0.2),
     (0.0, 0.0), (1.0, 0.0),
     (0, 4.0),   (1, 10),   #scale keys    change 
     (0.0, 0.0, 0.0),
     (0.0, 0.0, 0.0),
     0.0,
     0.0,
     0.0
     ),
    
  ("fright_aura", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_sparks_mesh_1",
     50, 2.0, 0.0, -0.11, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength   inc particles
     (0.5, 0.8), (1, 0),        #alpha keys
     (0.5, 1.0), (1, 0.9),       #red keys    
     (0.5, 0.7),(1, 0.3),       #green keys
     (0.5, 1.0), (1, 0.9),      #blue keys    # old blue (0.5, 0.2), (1, 0.0),
     (0, 0.1),   (1, 0.8),
     (1.0, 1.0, 0.2),            #emit box size  change from 3 3 to 1 1
     (0, 0, 0.25),               #emit velocity
     0.1,                       #emit dir randomness
     250,                       #rotation speed
     0.5                        #rotation damping
    ),
    
  ("charm_rose", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_rose_a",
     50, 2.0, 0.0, -0.11, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength   inc particles
     (0, 1), (1, 1),        #alpha keys
     (0, 0.5), (1, 0.5),      #red keys
     (0, 0.5), (1, 0.5),      #green keys
     (0, 0.5), (1, 0.5),      #blue keys
     (0, 0.25),   (1, 0.25),    #scale keys
     (1.0, 1.0, 0.2),            #emit box size  change from 3 3 to 1 1
     (0, 0, 0.25),               #emit velocity
     0.1,                       #emit dir randomness
     10,                        #rotation speed
     0.5                        #rotation damping
    ),
        
  ("paladin_aura", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_rotation|psf_randomize_size, "prtcl_rain",
     50, 12, 0, 0, 7, 7, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 0.25), (1, 0),          #alpha keys
     (0.0, 1), (1, 0.9),      #red keys
     (0.0, 1),(1, 0.9),      #green keys
     (0.0, 0), (1, 0.9),     #blue keys
     (0, 2.2),   (1, 15),        #scale keys
     (3, 3, 3),                 #emit box size
     (0, 0, -5),               #emit velocity
     0.1,                        #emit dir randomness
     100,
     0.2,
    ),
  ("paladin_aura2", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size, "prtcl_rain",
     1, 2, 0, 0, 7, 7, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 0.25), (1, 0),          #alpha keys
     (0.0, 1), (1, 0.9),      #red keys
     (0.0, 1),(1, 0.9),      #green keys
     (0.0, 0), (1, 0.9),     #blue keys
     (1, 150),   (1, 150),        #scale keys
#     (3, 3, 3),                 #emit box size
     (1, 1, 0.2),                #emit box size
     (0, 0, -10),               #emit velocity
     0.0,                        #emit dir randomness
     0,
     0.5,
    ),
  ("paladin_aura3", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_sparks_mesh_1",
     50, 2.0, 0.0, -0.11, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength   inc particles
     (0.5, 0.5), (1, 0),        #alpha keys
     (0.0, 1), (1, 0.9),      #red keys
     (0.0, 1), (1, 0.9),      #green keys
     (0.0, 0), (1, 0.9),     #blue keys
#     (0, 2.0),   (1, 5),   #scale keys    change
#     (0, 0.5),   (1, 1.5),   #scale keys    change
     (0, 0.1),   (1, 0.8),
     (1.0, 1.0, 0.2),            #emit box size  change from 3 3 to 1 1
#     (0, 0, 0.075),               #emit velocity
     (0, 0, 0.25),               #emit velocity
   
     0.1,                       #emit dir randomness
     250,                       #rotation speed
     0.5                        #rotation damping
    ),
    
  ("focus_aura3", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_sparks_mesh_1",
     50, 2.0, 0.0, -0.11, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength   inc particles
     (0.5, 0.5), (1, 0),        #alpha keys
     (0.5, 0.0), (1, 0.0),      #red keys
     (0.5, 0.4),(1, 0.2),       #green keys
     (0.5, 0.8), (1, 0.6),      #blue keys
     (0, 0.1),   (1, 0.8),
     (1.0, 1.0, 0.2),            #emit box size  change from 3 3 to 1 1
     (0, 0, 0.25),               #emit velocity
   
     0.1,                       #emit dir randomness
     250,                       #rotation speed
     0.5                        #rotation damping
    ),

  ("haste_aura3", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_sparks_mesh_1",
     50, 2.0, 0.0, -0.11, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength   inc particles
     (0.5, 0.5), (1, 0),        #alpha keys
     (0.5, 0.0), (1, 0.0),      #red keys
     (0.5, 1.0),(1, 0.0),       #green keys
     (0.5, 0.0), (1, 0.0),      #blue keys
#     (0, 2.0),   (1, 5),   #scale keys    change
#     (0, 0.5),   (1, 1.5),   #scale keys    change
     (0, 0.1),   (1, 0.8),
     (1.0, 1.0, 0.2),            #emit box size  change from 3 3 to 1 1
#     (0, 0, 0.075),               #emit velocity
     (0, 0, 0.25),               #emit velocity
   
     0.1,                       #emit dir randomness
     250,                       #rotation speed
     0.5                        #rotation damping
    ),
   
  ("rage_aura3", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_sparks_mesh_1",
     50, 2.0, 0.0, -0.11, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength   inc particles
     (0.5, 0.5), (1, 0),        #alpha keys
     (0.5, 1), (1, 0.9),      #red keys
     (0.5, 0.1),(1, 0.0),       #green keys
     (0.5, 0.0), (1, 0.0),      #blue keys
#     (0, 2.0),   (1, 5),   #scale keys    change
#     (0, 0.5),   (1, 1.5),   #scale keys    change
     (0, 0.1),   (1, 0.8),
     (1.0, 1.0, 0.2),            #emit box size  change from 3 3 to 1 1
#     (0, 0, 0.075),               #emit velocity
     (0, 0, 0.25),               #emit velocity
   
     0.1,                       #emit dir randomness
     250,                       #rotation speed
     0.5                        #rotation damping
    ),
    
  ("smite_aura", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_sparks_mesh_1",
     50, 2.0, 0.0, -0.11, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength   inc particles
     (0.60, 1.00), (1.00, 1.00),
     (0.10, 0.95), (1.00, 0.95),
     (0.10, 0.10), (1.00, 0.10),
     (0.10, 0.20), (1.00, 0.20),
     (0, 0.1),   (1, 0.8),
     (1.0, 1.0, 0.2),            #emit box size  change from 3 3 to 1 1
     (0, 0, 0.25),               #emit velocity
     0.1,                       #emit dir randomness
     250,                       #rotation speed
     0.5                        #rotation damping
    ),
       
  ("rage_aura2", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size, "prtcl_rain",
     1, 2, 0, 0, 7, 7, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 0.25), (1, 0),          #alpha keys
     (0.5, 1), (1, 0.9),      #red keys
     (0.5, 0.1),(1, 0.0),       #green keys
     (0.5, 0.0), (1, 0.0),      #blue keys
     (1, 150),   (1, 150),        #scale keys
#     (3, 3, 3),                 #emit box size
     (1, 1, 0.2),                #emit box size
     (0, 0, -10),               #emit velocity
     0.0,                        #emit dir randomness
     0,
     0.5,
    ),
    
  ("feron_berserker_rage", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_blood_3",
     50, 1.5, 0.0, -0.11, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength   inc particles
     (0.5, 0.5), (1, 0),        #alpha keys
     (0.5, 1), (1, 0.9),      #red keys
     (0.5, 0.1),(1, 0.0),       #green keys
     (0.5, 0.0), (1, 0.0),      #blue keys
     (0, 1.0),   (1, 3),   #scale keys    change 
     (0.5, 0.5, 0.2),            #emit box size  change from 3 3 to 1 1
     (0, 0, 0.115),               #emit velocity
     0.1,                       #emit dir randomness
     250,                       #rotation speed
     0.5                        #rotation damping
    ),
  ("inquisitor_aura", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     50, 2.0, 0.0, -0.11, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength   inc particles
     (0.5, 0.5), (1, 0),        #alpha keys
     (0.5, 0.8), (1, 0.6),      #red keys             ORANGE
     (0.5, 0.4),(1, 0.2),       #green keys 
     (0.5, 0.0), (1, 0.0),      #blue keys
     (0, 1.0),   (1, 3),   #scale keys    change 
     (1.0, 1.0, 0.2),            #emit box size  change from 3 3 to 1 1
     (0, 0, 0.015),               #emit velocity
     0.1,                       #emit dir randomness
     250,                       #rotation speed
     0.5                        #rotation damping
    ),

  ("converted_effect", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prtcl_rain",
     10, 1, 0.0, -0.11, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength   inc particles
     (0.5, 0.5), (1, 0),        #alpha keys
     (0.5, 0.8), (1, 0.6),      #red keys             ORANGE
     (0.5, 0.4),(1, 0.2),       #green keys 
     (0.5, 0.0), (1, 0.0),      #blue keys
     (0, 0.5),   (1, 1.5),   #scale keys    change 
     (0.3, 0.3, 0.2),            #emit box size  change from 3 3 to 1 1
     (0, 0, 0.015),               #emit velocity
     0.1,                       #emit dir randomness
     360,                       #rotation speed
     0.5                        #rotation damping
    ),
  ("planelord_rain", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size, "prtcl_rain",
     80, 3, 0, 0, 7, 7, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 0.25), (1, 0),          #alpha keys
     (0.5, 1.0), (1, 0.95),       #red keys    # old red (0.5, 1.0), (1, 0.9),   inc front .2 back .2  looks good (0.5, 0.8), (1, 0.6),
     (0.5, 0.4),(1, 0.3),       #green keys
     (0.5, 1.0), (1, 0.95),      #blue keys    # old blue (0.5, 0.2), (1, 0.0),
     (0, 1.2),   (1, 1.2),        #scale keys
     (15, 15, 0.2),                 #emit box size
     (0, 0, -20),               #emit velocity
      0,                        #emit dir randomness
      0,
     0.2,
    ),

  ("unholy_grasp", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_smoke_1",
     50, 3.0, 0.0, -0.11, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength   inc particles
     (0.5, 0.5), (1, 0),        #alpha keys
     (0.5, 0.005), (1, 0.001),      #red keys             ORANGE
     (0.5, 0.005),(1, 0.001),       #green keys 
     (0.5, 0.005), (1, 0.001),      #blue keys
     (0, 1.0),   (1, 3),   #scale keys    change 
     (1.0, 1.0, 0.2),            #emit box size  change from 3 3 to 1 1
     (0, 0, 0.515),               #emit velocity
     0.1,                       #emit dir randomness
     250,                       #rotation speed
     0.5                        #rotation damping
    ),

  ("slow_auro", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     50, 3.0, 0.0, -0.11, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength   inc particles
     (0.5, 0.5), (1, 0),        #alpha keys
     (0.5, 0.005), (1, 0.001),      #red keys             ORANGE
     (0.5, 0.005),(1, 0.001),       #green keys 
     (0.5, 0.005), (1, 0.001),      #blue keys
     (0, 1.0),   (1, 3),   #scale keys    change 
     (1.0, 1.0, 0.2),            #emit box size  change from 3 3 to 1 1
     (0, 0, 0.515),               #emit velocity
     0.1,                       #emit dir randomness
     250,                       #rotation speed
     0.5                        #rotation damping
    ),

  ("feron_battlecry_buff", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prtcl_splash_b",
     5, 1.0, 0.0, -0.11, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength   inc particles
     (0.5, 0.5), (1, 0),        #alpha keys
     (0.5, 0.5), (1, 1.0),      #red keys
     (0.5, 0.0),(1, 0.0),       #green keys
     (0.5, 0.0), (1, 0.0),      #blue keys
     (0, 1.0),   (1, 1.5),   #scale keys    change 
     (0.4, 0.4, 0.2),            #emit box size  change from 3 3 to 1 1
     (0, 0, 0.045),               #emit velocity
     0.1,                       #emit dir randomness
     250,                       #rotation speed
     0.5                        #rotation damping
    ),

  ("asaleth_horn_buff", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     5, 1.0, 0.0, -0.11, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength   inc particles
     (0.5, 0.5), (1, 0),        #alpha keys
     (0.5, 0.0), (1, 0.0),      #red keys
     (0.5, 1.0),(1, 0.0),       #green keys
     (0.5, 0.0), (1, 0.0),      #blue keys
     (0, 1.0),   (1, 1.5),   #scale keys    change 
     (0.4, 0.4, 0.2),            #emit box size  change from 3 3 to 1 1
     (0, 0, 0.045),               #emit velocity
     0.1,                       #emit dir randomness
     250,                       #rotation speed
     0.5                        #rotation damping
    ),



  ("asaleth_archer_buff", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_snow_dust_1",
     5, 1.5, 0.0, -0.11, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength   inc particles
     (0.5, 0.5), (1, 0),        #alpha keys
     (0.5, 0.0), (1, 0.0),      #red keys
     (0.5, 1.0),(1, 0.0),       #green keys
     (0.5, 0.0), (1, 0.0),      #blue keys
     (0, 1.0),   (1, 3),   #scale keys    change 
     (0.4, 0.4, 0.2),            #emit box size  change from 3 3 to 1 1
     (0, 0, 0.045),               #emit velocity
     0.1,                       #emit dir randomness
     250,                       #rotation speed
     0.5                        #rotation damping
    ),
  ("asaleth_archer", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size, "prtcl_rain",
     25, 1.5, 0.0, -0.25, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength   inc particles
     (0.5, 0.5), (1, 0),        #alpha keys
     (0.5, 0), (1, 0.1),      #red keys
     (0.5, 0.5),(1, 1.0),       #green keys
     (0.5, 0.1), (1, 0.1),      #blue keys
     (0, 0.7),   (1, 0.7),   #scale keys    change 
     (0.5, 0.5, 0.2),            #emit box size  change from 3 3 to 1 1
     (0, 0, 0.755),               #emit velocity
     0,                       #emit dir randomness
     0,                       #rotation speed
     0.2                        #rotation damping
    ),
  ("feron_battlecry", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size, "prtcl_rain",
     25, 1.5, 0.0, -0.25, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength   inc particles
     (0.5, 0.5), (1, 0),        #alpha keys
     (0.5, 0.001), (1, 0.002),      #red keys
     (0.5, 0.001), (1, 0.002),       #green keys
     (0.5, 0.001), (1, 0.002),      #blue keys
     (0, 0.4),   (1, 0.4),   #scale keys    change 
     (0.5, 0.5, 0.2),            #emit box size  change from 3 3 to 1 1
     (0, 0, 0.955),               #emit velocity
     0,                       #emit dir randomness
     0,                       #rotation speed
     0.2                        #rotation damping
    ),
   
    ("fright_aura2", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size, "prtcl_rain",
     1, 2, 0, 0, 0, 0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 0.5), (1, 0.9),          #alpha keys
     (0.0, 1), (1, 0.8),      #red keys
     (0.0, 1),(1, 0.8),      #green keys
     (0.0, 1), (1, 0.8),     #blue keys
     (1, 150),   (1, 150),        #scale keys
     (1, 1, 0.2),                #emit box size
     (0, 0, -10),               #emit velocity
     0.0,                        #emit dir randomness
     0,
     0.5,
    ),

    ("heal_effect", psf_billboard_3d|psf_randomize_size, "prt_mesh_heal_1",
     25, 3, 15, -0.05, 10, 0.2, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.5), (1, 0.0),          #alpha keys
     (0.3, 0.1), (1, 0.1),      #red keys
     (0.3, 1.0),(1, 1.0),      #green keys
     (0.3, 0.1), (1, 0.1),     #blue keys
     (0, 0.1),   (1, 0.5),        #scale keys
     (0.2, 0.2, 0.5),                #emit box size
     (0, 0, 0.05),               #emit velocity
     2.0,                        #emit dir randomness
     10,
     0.1,
    ),

    ("entangle", psf_billboard_3d | psf_randomize_size, "prt_Leaf_a",
     25, 3, 15, -0.05, 10, 0.2, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 1), (1, 1),            #alpha keys
     (0, 0.5), (1, 0.5),        #red keys
     (0, 0.5), (1, 0.5),        #green keys
     (0, 0.5), (1, 0.5),        #blue keys
     (0, 0.01),   (1, 0.05),        #scale keys
     (0.2, 0.2, 0.5),                #emit box size
     (0, 0, 0.05),               #emit velocity
     2.0,                        #emit dir randomness
     10,
     0.1,
    ),

    ("bad_effect", psf_billboard_3d|psf_randomize_size, "prt_mesh_heal_1",
     25, 3, 15, -0.05, 10, 0.2, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.5), (1, 0.0),          #alpha keys
     (0.3, 1), (1, 1.0),      #red keys
     (0.3, 0.7),(1, 0.3),      #green keys
     (0.3, 0.2), (1, 0.0),     #blue keys
     (0, 0.1),   (1, 0.5),        #scale keys
     (0.2, 0.2, 0.5),                #emit box size
     (0, 0, 0.05),               #emit velocity
     2.0,                        #emit dir randomness
     10,
     0.1,
    ),

    ("snow_effect", psf_billboard_3d|psf_randomize_size, "prt_Snowflake_a",
     25, 3, 15, -0.05, 10, 0.2, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.8), (1.0, 0.0),
     (0.5, 0.6), (1.0, 0.0),
     (0.5, 0.88), (1.0, 0.0),
     (0.5, 1.0), (1.0, 0.0),
     (0, 0.1),   (1, 0.5),        #scale keys
     (0.2, 0.2, 0.5),                #emit box size
     (0, 0, 0.05),               #emit velocity
     2.0,                        #emit dir randomness
     10,
     0.1,
    ),

    ("poison_smoke_small", psf_always_emit|psf_global_emit_dir|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_dust_1",
     10, 0.2, 5, -0.3, 1.0, 1.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     
     (0.1, 0.5), (1, 0),        #alpha keys
     (0.3, 0.1), (1.0, 0.1),
     (0.3, 0.9), (1.0, 0.9),
     (0.3, 0.3), (1.0, 0.3),
     (0, 0.2),(1, 1.2),          #scale keys
     
     (0.1, 0.1, 1),           #emit box size
     (0, 0, 0.1),               #emit velocity
     2,                       #emit dir randomness
     2,                       #rotation speed
     0.3                        #rotation damping
    ),


    ("poison_blood", psf_billboard_3d|psf_randomize_size, "prt_mesh_Poison_a",
     10, 3, 15, -0.05, 10, 0.2, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.8), (1, 0.3),        #alpha keys
     (0.3, 0.1), (1.0, 0.1),
     (0.3, 0.9), (1.0, 0.9),
     (0.3, 0.3), (1.0, 0.3),
     (0, 0.1),   (1, 0.5),        #scale keys
     (0.2, 0.2, 0.5),                #emit box size
     (0, 0, 0.05),               #emit velocity
     2.0,                        #emit dir randomness
     10,
     0.1,
    ),

    ("curse_effect", psf_always_emit|psf_global_emit_dir|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_Poison_a",
     10, 3, 15, -0.05, 10, 0.2, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.5), (1, 0),        #alpha keys
     (0.5, 1), (1, 0.9),      #red keys
     (0.5, 0.1),(1, 0.0),       #green keys
     (0.5, 0.0), (1, 0.0),      #blue keys
     (0, 0.1),   (1, 0.5),        #scale keys
     (0.2, 0.2, 0.5),                #emit box size
     (0, 0, 0.05),               #emit velocity
     2.0,                        #emit dir randomness
     10,
     0.1,
    ),

    ("marked_for_death_effect", psf_always_emit|psf_global_emit_dir|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_Poison_a",
     10, 3, 15, -0.05, 10, 0.2, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.5), (1, 0),        #alpha keys
     (0.5, 1), (1, 0.5),      #red keys
     (0.5, 0.1),(1, 0.0),       #green keys
     (0.5, 0.0), (1, 0.5),      #blue keys
     (0, 0.1),   (1, 0.5),        #scale keys
     (0.2, 0.2, 0.5),                #emit box size
     (0, 0, 0.05),               #emit velocity
     2.0,                        #emit dir randomness
     10,
     0.1,
    ),

    ("block_effect", psf_always_emit|psf_global_emit_dir|psf_billboard_3d, "prt_AT_FIELD_a",
     1, 0.2, 120.0, 0.0, 0.0, 0.1,
     (0.0, 1.0), (1.0, 1.0),
     (0.0, 1.0), (1.0, 0.9),
     (0.0, 0.3), (1.0, 0.2),
     (0.0, 0.0), (1.0, 0.0),
     (0.0, 0.1), (1.0, 2.0),
     (0.0, 0.0, 0.0),
     (0.0, 0.0, 0.0),
     0.0,
     0.0,
     0.0
     ),

    ("fear_effect", psf_always_emit|psf_global_emit_dir|psf_billboard_3d, "prt_mesh_Poison_b",
     2, 2, 120.0, 0.0, 0.0, 0.1,
     (0.5, 0.5), (1, 1),        #alpha keys
     (0.5, 0.005), (1, 0.001),      #red keys             ORANGE
     (0.5, 0.005),(1, 0.001),       #green keys 
     (0.5, 0.005), (1, 0.001),      #blue keys
     (0.0, 4), (1.0, 10),
     (0.0, 0.0, 0.0),
     (0, 0, 0.015),               #emit velocity
     0.0,
     0.0,
     0.0
     ),

    ("fright_aura_effect", psf_always_emit|psf_global_emit_dir|psf_billboard_3d, "prt_mesh_Poison_b",
     1, 2, 120.0, 0.0, 0.0, 0.1,
     (0.5, 0.5), (1, 1),        #alpha keys
     (0.5, 1.0), (1, 0.9),       #red keys    # old red (0.5, 1.0), (1, 0.9),   inc front .2 back .2  looks good (0.5, 0.8), (1, 0.6),
     (0.5, 0.7),(1, 0.3),       #green keys
     (0.5, 1.0), (1, 0.9),      #blue keys    # old blue (0.5, 0.2), (1, 0.0),
     (0.0, 4), (1.0, 10),
     (0.0, 0.0, 0.0),
     (0, 0, 0.015),               #emit velocity
     0.0,
     0.0,
     0.0
     ),

    ("stun_effect", psf_billboard_3d|psf_randomize_size, "prt_Swirl_b",
     1, 1, 120.0, 10, 10, 1,
     (0.0, 1.0), (1.0, 0.3),
     (0.0, 1.0), (1.0, 0.9),
     (0.0, 0.3), (1.0, 0.2),
     (0.0, 0.0), (1.0, 0.0),
     (0.0, 1), (1.0, 2),
     (1, 1, 0.2),                #emit box size
     (0, 0, -10),               #emit velocity
     5.0,                        #emit dir randomness
     100,
     10,
     ),


     ("Burning_Trail", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation|psf_2d_turbulance, "prt_mesh_fire_1",
     15, 2,  10, 0.05, 10.0, 39.0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.5), (1, 0),        #alpha keys
     (3.0, 1.0), (5, 0.9),      #red keys
     (3.0, 0.7),(5, 0.3),       #green keys
     (3.0, 0.2), (5, 0.0),      #blue keys
     (0.5, 3),   (1.0, 3.7),   #scale keys
     (0.2, 0.4, 0.1),           #emit box size
     (0, 0, 1),                 #emit velocity
     2,                         #emit dir randomness
     0,                       #rotation speed
     0                        #rotation damping
    ),  
     ("Sandstorm", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation|psf_2d_turbulance, "prt_mesh_dust_1",#prt_mesh_dust_1
     155, 3,  10, 0.05, 10.0, 39.0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.2, 0.5), (1, 0.0),        #alpha keys
     (3, 1), (5, 1),        #red keys
     (3, 0.9),(5, 0.9),         #green keys
     (3, 0.78),(5, 0.78),         #blue keys
     (5.0, 8.0),   (3, 10),  #scale keys
     (10.0, 4.0, 3.0),           #emit box size
     (0, 0, 0.4),               #emit velocity
     0.5,                       #emit dir randomness
     130,                       #rotation speed
     0.5                        #rotation damping
    ),      
     ("Freezing_Trail", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation|psf_2d_turbulance, "prt_mesh_dust_1",#prt_mesh_dust_1
     15, 1,  10, 0.05, 10.0, 39.0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.3, 1.0), (1, 0.3),        #alpha keys
     (1.0, 1.0), (1, 1.0),      #red keys
     (1.0, 1.0), (1, 1.0),      #green keys
     (1.0, 1.0), (1, 1.0),      #blue keys
     (0.5, 3),   (1.0, 3.7),   #scale keys
     (0.2, 0.4, 0.1),           #emit box size
     (0, 0, 1),                 #emit velocity
     2,                         #emit dir randomness
     0,                       #rotation speed
     0                        #rotation damping
    ),  
     ("Ice_Storm", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation|psf_2d_turbulance, "prt_mesh_dust_1",#prt_mesh_dust_1
     155, 3,  10, 0.05, 10.0, 39.0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.3, 1.0), (1, 0.3),        #alpha keys
     (3.0, 1.0), (5, 1.0),      #red keys
     (3.0, 1.0), (5, 1.0),      #green keys
     (3.0, 1.0), (5, 1.0),      #blue keys
     (5.0, 8.0),   (3, 10),  #scale keys
     (10.0, 4.0, 3.0),           #emit box size
     (0, 0, 0.5),               #emit velocity
     0.5,                       #emit dir randomness
     130,                       #rotation speed
     0.5                        #rotation damping
    ),  

     ("incediary_cloud", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation|psf_2d_turbulance, "prt_mesh_fire_1",#prt_mesh_dust_1prt_mesh_fire_1
     155, 3,  10, 0.05, 10.0, 39.0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.5), (1, 0),        #alpha keys
     (3.0, 1.0), (5, 0.9),      #red keys
     (3.0, 0.7),(5, 0.3),       #green keys
     (3.0, 0.2), (5, 0.0),      #blue keys
     (5.0, 8.0),   (3, 10),  #scale keys
     (10.0, 4.0, 3.0),           #emit box size
     (0, 0, 0.5),               #emit velocity
     0.5,                       #emit dir randomness
     130,                       #rotation speed
     0.5                        #rotation damping
    ),  
    
     ("holy_fire_cloud", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation|psf_2d_turbulance, "prt_mesh_fire_1",#prt_mesh_dust_1prt_mesh_fire_1
     155, 3,  10, 0.05, 10.0, 39.0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.5), (1, 0),        #alpha keys
      (0.5, .8), (1, 0.6),        #red keys
      (0.5, .8), (1, 0.6),       #green keys
      (0.5, 1), (1, 0.6),      #blue keys
     (5.0, 8.0),   (3, 10),  #scale keys
     (10.0, 4.0, 3.0),           #emit box size
     (0, 0, 0.5),               #emit velocity
     0.5,                       #emit dir randomness
     130,                       #rotation speed
     0.5                        #rotation damping
    ),  

     ("poison_cloud", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation|psf_2d_turbulance, "prt_mesh_dust_1",#prt_mesh_dust_1
     15, 2,  10, 0.05, 10.0, 39.0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.3, 1.0), (1, 0.3),        #alpha keys
     (0.3, 0.1), (1.0, 0.1),
     (0.3, 0.9), (1.0, 0.9),
     (0.3, 0.3), (1.0, 0.3),
     (0.0, 2),   (1.0, 3.7),   #scale keys
     (0.2, 0.4, 0.1),           #emit box size
     (0, 0, 1),                 #emit velocity
     2,                         #emit dir randomness
     0,                       #rotation speed
     0                        #rotation damping
    ),  


("items_poison_cloud", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation|psf_2d_turbulance, "prt_mesh_dust_1",#prt_mesh_dust_1
     15, 2,  10, 0.05, 10.0, 39.0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.3, 1.0), (1, 0.3),        #alpha keys
     (0.5, 0.0), (1, 0.0),      #red keys
     (0.5, 1.0),(1, 0.0),       #green keys
     (0.5, 0.0), (1, 0.0),      #blue keys
     (0, 0.15),   (0.4, 0.3),   #scale keys
     (0.03, 0.8, 0.03),      #emit box size
     (0, 0, 0.5),               #emit velocity
     0.0,                       #emit dir randomness
     2000,                       #rotation speed
     0.0                        #rotation damping
    ),

     ("death_cloud", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation|psf_2d_turbulance, "prt_mesh_dust_1",#prt_mesh_dust_1
     155, 3,  10, 0.05, 10.0, 39.0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.3, 1.0), (1, 0.3),        #alpha keys
     (0.3, 0.1), (1.0, 0.1),
     (0.3, 0.9), (1.0, 0.9),
     (0.3, 0.3), (1.0, 0.3),
     (0.0, 8.0),   (3, 10),  #scale keys
     (10.0, 4.0, 3.0),           #emit box size
     (0, 0, 0.5),               #emit velocity
     0.5,                       #emit dir randomness
     130,                       #rotation speed
     0.5                        #rotation damping
    ),  

     ("death_cloud_blue", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation|psf_2d_turbulance, "prt_mesh_dust_1",#prt_mesh_dust_1
     155, 3,  10, 0.05, 10.0, 39.0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.3, 1.0), (1, 0.3),        #alpha keys
     (0.3, 0.1), (1.0, 0.1),
     (0.3, 0.3), (1.0, 0.3),
     (0.3, 0.9), (1.0, 0.9),
     (0.0, 8.0),   (3, 10),  #scale keys
     (10.0, 4.0, 3.0),           #emit box size
     (0, 0, 0.5),               #emit velocity
     0.5,                       #emit dir randomness
     130,                       #rotation speed
     0.5                        #rotation damping
    ),  

    ("thunder", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size, "thunder",
     1, 0.1, 0, 0, 7, 7, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.3, 1.0), (1, 0.3),        #alpha keys
     (3.0, 1.0), (5, 1.0),      #red keys
     (3.0, 1.0), (5, 1.0),      #green keys
     (3.0, 1.0), (5, 1.0),      #blue keys
     (0, 5),   (1, 1),        #scale keys
     (1, 1, 0.2),                #emit box size
     (0, 0, -10),               #emit velocity
     0.0,                        #emit dir randomness
     0,
     0.5,
    ),

    ("thunder2", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size, "thunder2",
     1, 0.1, 0, 0, 7, 7, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.3, 1.0), (1, 0.3),        #alpha keys
     (3.0, 1.0), (5, 1.0),      #red keys
     (3.0, 1.0), (5, 1.0),      #green keys
     (3.0, 1.0), (5, 1.0),      #blue keys
     (0, 5),   (1, 1),        #scale keys
     (1, 1, 0.2),                #emit box size
     (0, 0, -10),               #emit velocity
     0.0,                        #emit dir randomness
     0,
     0.5,
    ),
    ("thunder3", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size, "thunder3",
     1, 0.1, 0, 0, 7, 7, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.3, 1.0), (1, 0.3),        #alpha keys
     (3.0, 1.0), (5, 1.0),      #red keys
     (3.0, 1.0), (5, 1.0),      #green keys
     (3.0, 1.0), (5, 1.0),      #blue keys
     (0, 5),   (1, 1),        #scale keys
     (1, 1, 0.2),                #emit box size
     (0, 0, -10),               #emit velocity
     0.0,                        #emit dir randomness
     0,
     0.5,
    ),
    ("thunder4", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size, "thunder4",
     1, 0.1, 0, 0, 7, 7, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.3, 1.0), (1, 0.3),        #alpha keys
     (3.0, 1.0), (5, 1.0),      #red keys
     (3.0, 1.0), (5, 1.0),      #green keys
     (3.0, 1.0), (5, 1.0),      #blue keys
     (0, 5),   (1, 1),        #scale keys
     (1, 1, 0.2),                #emit box size
     (0, 0, -10),               #emit velocity
     0.0,                        #emit dir randomness
     0,
     0.5,
    ),
    ("thunder5", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size, "thunder5",
     1, 0.1, 0, 0, 7, 7, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.3, 1.0), (1, 0.3),        #alpha keys
     (3.0, 1.0), (5, 1.0),      #red keys
     (3.0, 1.0), (5, 1.0),      #green keys
     (3.0, 1.0), (5, 1.0),      #blue keys
     (0, 5),   (1, 1),        #scale keys
     (1, 1, 0.2),                #emit box size
     (0, 0, -10),               #emit velocity
     0.0,                        #emit dir randomness
     0,
     0.5,
    ),
    ("thunder6", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size, "thunder6",
     1, 0.1, 0, 0, 7, 7, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.3, 1.0), (1, 0.3),        #alpha keys
     (3.0, 1.0), (5, 1.0),      #red keys
     (3.0, 1.0), (5, 1.0),      #green keys
     (3.0, 1.0), (5, 1.0),      #blue keys
     (0, 5),   (1, 1),        #scale keys
     (1, 1, 0.2),                #emit box size
     (0, 0, -10),               #emit velocity
     0.0,                        #emit dir randomness
     0,
     0.5,
    ),
    ("thunder7", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size, "thunder7",
     1, 0.1, 0, 0, 7, 7, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.3, 1.0), (1, 0.3),        #alpha keys
     (3.0, 1.0), (5, 1.0),      #red keys
     (3.0, 1.0), (5, 1.0),      #green keys
     (3.0, 1.0), (5, 1.0),      #blue keys
     (0, 5),   (1, 1),        #scale keys
     (1, 1, 0.2),                #emit box size
     (0, 0, -10),               #emit velocity
     0.0,                        #emit dir randomness
     0,
     0.5,
    ),
    ("thunder8", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size, "thunder8",
     1, 0.1, 0, 0, 7, 7, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.3, 1.0), (1, 0.3),        #alpha keys
     (3.0, 1.0), (5, 1.0),      #red keys
     (3.0, 1.0), (5, 1.0),      #green keys
     (3.0, 1.0), (5, 1.0),      #blue keys
     (0, 5),   (1, 1),        #scale keys
     (1, 1, 0.2),                #emit box size
     (0, 0, -10),               #emit velocity
     0.0,                        #emit dir randomness
     0,
     0.5,
    ),



    ("small_thunder", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size, "copy_thunder",
     1, 0.1, 0, 0, 7, 7, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.3, 1.0), (1, 0.3),        #alpha keys
     (3.0, 1.0), (5, 1.0),      #red keys
     (3.0, 1.0), (5, 1.0),      #green keys
     (3.0, 1.0), (5, 1.0),      #blue keys
     (0, .5),   (1, .1),        #scale keys
     (1, 1, 0.2),                #emit box size
     (0, 0, -10),               #emit velocity
     0.0,                        #emit dir randomness
     0,
     0.5,
    ),
    
    ("holy_fire", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     35, 0.6, 0.2, -0.2, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.8), (1, 0),        #alpha keys
     (0.5, .8), (1, 0.6),        #red keys
     (0.5, .8), (1, 0.6),       #green keys
     (0.5, 1), (1, 0.6),      #blue keys
     (0, 0.4),   (1, 1),   #scale keys
     (0.4, 0.2, 0.01),            #emit box size
     (0, 0, 0.4),               #emit velocity
     0.1,                       #emit dir randomness
     100,                       #rotation speed
     0.5                        #rotation damping
    ),  
  #("holy_light", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size, "prtcl_rain_2",
  ("holy_light", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size, "prtcl_rain",
     1, 2, 0, 0, 7, 7, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 0.25), (1, 0),          #alpha keys
     (0.0, 1), (1, 0.9),      #red keys
     (0.0, 1),(1, 0.9),      #green keys
     (0.0, 0), (1, 0.9),     #blue keys
     (1, 150),   (1, 150),        #scale keys
     (1, 0.2, 1),                #emit box size
     (0, -10, 0),               #emit velocity
     0.0,                        #emit dir randomness
     0,
     0.5,
    ),
     ("Burning_Trail_holy", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation|psf_2d_turbulance, "prt_mesh_fire_1",
     150, 2,  10, 0.05, 10.0, 39.0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.25), (1, 0),        #alpha keys
     (0.5, .8), (1, 0.6),        #red keys
     (0.5, .8), (1, 0.6),       #green keys
     (0.5, 1), (1, 0.6),      #blue keys
     (0.5, 3),   (1.0, 3.7),   #scale keys
     (0.2, 0.4, 0.1),           #emit box size
     (0, 0, 1),                 #emit velocity
     2,                         #emit dir randomness
     0,                       #rotation speed
     0                        #rotation damping
    ),  
    
     ("flamethrower_fire_1", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
      10, 0.3, 0.2, -0.2, 10.0, 5, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
       (0.5, 0.5), (1.0, 0.0), #alpha keys
      (0.5, 1.0), (1, 0.9), #red keys
      (0.5, 0.7),(1, 0.3),  #green keys
      (0.5, 0.2), (1, 0.0),   #blue keys
      (0.0, 0.5), (1.0, 0.5),   #scale keys
      (0.2, 0.1, 0.01),          #emit box size
      (0, 0, 0.2),          #emit velocity
      0.1,               #emit dir randomness
      100,                 #rotation speed
      0.5                 #rotation damping
      ),
     ("flamethrower_fire_2", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
      12, 0.3, 0.2, -0.2, 10.0, 5, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
       (0.5, 0.5), (1.0, 0.0), #alpha keys
      (0.5, 1.0), (1, 0.9), #red keys
      (0.5, 0.7),(1, 0.3),  #green keys
      (0.5, 0.2), (1, 0.0),   #blue keys
      (0.0, 0.4), (1.0, 2.0),   #scale keys
      (0.2, 0.1, 0.01),          #emit box size
      (0, 0, 0.2),          #emit velocity
      0.1,               #emit dir randomness
      100,                 #rotation speed
      0.5                 #rotation damping
      ),
     ("flamethrower_fire_3", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
      15, 0.3, 0.2, -0.2, 10.0, 5, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
       (0.5, 0.5), (1.0, 0.0), #alpha keys
      (0.5, 1.0), (1, 0.9), #red keys
      (0.5, 0.7),(1, 0.3),  #green keys
      (0.5, 0.2), (1, 0.0),   #blue keys
      (0.0, 0.3), (1.0, 4.0),   #scale keys
      (0.2, 0.1, 0.01),          #emit box size
      (0, 0, 0.2),          #emit velocity
      0.1,               #emit dir randomness
      100,                 #rotation speed
      0.5                 #rotation damping
      ),
     ("flamethrower_fire_4", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
      17, 0.3, 0.2, -0.2, 10.0, 5, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
       (0.5, 0.5), (1.0, 0.0), #alpha keys
      (0.5, 1.0), (1, 0.9), #red keys
      (0.5, 0.7),(1, 0.3),  #green keys
      (0.5, 0.2), (1, 0.0),   #blue keys
      (0.0, 0.2), (1.0, 8.0),   #scale keys
      (0.2, 0.1, 0.01),          #emit box size
      (0, 0, 0.2),          #emit velocity
      0.1,               #emit dir randomness
      100,                 #rotation speed
      0.5                 #rotation damping
      ),
     ("flamethrower_fire_5", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
      20, 0.3, 0.2, -0.2, 10.0, 5, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
       (0.5, 0.5), (1.0, 0.0), #alpha keys
      (0.5, 1.0), (1, 0.9), #red keys
      (0.5, 0.7),(1, 0.3),  #green keys
      (0.5, 0.2), (1, 0.0),   #blue keys
      (0.0, 0.1), (1.0, 12.0),   #scale keys
      (0.2, 0.1, 0.01),          #emit box size
      (0, 0, 0.2),          #emit velocity
      0.1,               #emit dir randomness
      100,                 #rotation speed
      0.5                 #rotation damping
      ),
     ("flamethrower_fire_6", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
      18, 0.3, 0.2, -0.2, 10.0, 5, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
       (0.5, 0.5), (1.0, 0.0), #alpha keys
      (0.5, 1.0), (1, 0.9), #red keys
      (0.5, 0.7),(1, 0.3),  #green keys
      (0.5, 0.2), (1, 0.0),   #blue keys
      (0.0, 0.0), (1.0, 12.0),   #scale keys
      (0.2, 0.1, 0.01),          #emit box size
      (0, 0, 0.2),          #emit velocity
      0.1,               #emit dir randomness
      100,                 #rotation speed
      0.5                 #rotation damping
      ),
     ("flamethrower_fire_7", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
      15, 0.3, 0.2, -0.2, 10.0, 5, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
       (0.5, 0.5), (1.0, 0.0), #alpha keys
      (0.5, 1.0), (1, 0.9), #red keys
      (0.5, 0.7),(1, 0.3),  #green keys
      (0.5, 0.2), (1, 0.0),   #blue keys
      (0.0, 0.0), (1.0, 12.0),   #scale keys
      (0.2, 0.1, 0.01),          #emit box size
      (0, 0, 0.2),          #emit velocity
      0.1,               #emit dir randomness
      100,                 #rotation speed
      0.5                 #rotation damping
      ),
     ("flamethrower_fire_8", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
      10, 0.3, 0.2, -0.2, 10.0, 5, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
       (0.5, 0.5), (1.0, 0.0), #alpha keys
      (0.5, 1.0), (1, 0.9), #red keys
      (0.5, 0.7),(1, 0.3),  #green keys
      (0.5, 0.2), (1, 0.0),   #blue keys
      (0.0, 0.0), (1.0, 10.0),   #scale keys
      (0.2, 0.1, 0.01),          #emit box size
      (0, 0, 0.2),          #emit velocity
      0.1,               #emit dir randomness
      100,                 #rotation speed
      0.5                 #rotation damping
      ),
    
    ("burning_smoke", psf_billboard_3d|psf_global_emit_dir|psf_always_emit, "prt_mesh_smoke_1",
     10, 0.3, 0.2, -0.3, 10, 0.1, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.5), (1, 0),          #alpha keys
     (0.0, 0), (1, 0.0),      #red keys
     (0.0, 0),(1, 0.0),      #green keys
     (0.0, 0), (1, 0.0),     #blue keys
     (0, 0.5),   (0.8, 4),        #scale keys
     (1, 1, 1),                 #emit box size
     (0, 0, 1.5),               #emit velocity
     0.1,                        #emit dir randomness
     0,
     0,
    ),
    
     ("flamethrower_holy_fire_1", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
      10, 0.3, 0.2, -0.2, 10.0, 5, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
       (0.5, 0.5), (1.0, 0.0), #alpha keys
      (0.5, .8), (1, 0.6),        #red keys
      (0.5, .8), (1, 0.6),       #green keys
      (0.5, 1), (1, 0.6),      #blue keys
      (0.0, 0.5), (1.0, 0.5),   #scale keys
      (0.2, 0.1, 0.01),          #emit box size
      (0, 0, 0.2),          #emit velocity
      0.1,               #emit dir randomness
      100,                 #rotation speed
      0.5                 #rotation damping
      ),
     ("flamethrower_holy_fire_2", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
      12, 0.3, 0.2, -0.2, 10.0, 5, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
       (0.5, 0.5), (1.0, 0.0), #alpha keys
      (0.5, .8), (1, 0.6),        #red keys
      (0.5, .8), (1, 0.6),       #green keys
      (0.5, 1), (1, 0.6),      #blue keys
      (0.0, 0.4), (1.0, 2.0),   #scale keys
      (0.2, 0.1, 0.01),          #emit box size
      (0, 0, 0.2),          #emit velocity
      0.1,               #emit dir randomness
      100,                 #rotation speed
      0.5                 #rotation damping
      ),
     ("flamethrower_holy_fire_3", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
      15, 0.3, 0.2, -0.2, 10.0, 5, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
       (0.5, 0.5), (1.0, 0.0), #alpha keys
      (0.5, .8), (1, 0.6),        #red keys
      (0.5, .8), (1, 0.6),       #green keys
      (0.5, 1), (1, 0.6),      #blue keys
      (0.0, 0.3), (1.0, 4.0),   #scale keys
      (0.2, 0.1, 0.01),          #emit box size
      (0, 0, 0.2),          #emit velocity
      0.1,               #emit dir randomness
      100,                 #rotation speed
      0.5                 #rotation damping
      ),
     ("flamethrower_holy_fire_4", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
      17, 0.3, 0.2, -0.2, 10.0, 5, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
       (0.5, 0.5), (1.0, 0.0), #alpha keys
      (0.5, .8), (1, 0.6),        #red keys
      (0.5, .8), (1, 0.6),       #green keys
      (0.5, 1), (1, 0.6),      #blue keys
      (0.0, 0.2), (1.0, 8.0),   #scale keys
      (0.2, 0.1, 0.01),          #emit box size
      (0, 0, 0.2),          #emit velocity
      0.1,               #emit dir randomness
      100,                 #rotation speed
      0.5                 #rotation damping
      ),
     ("flamethrower_holy_fire_5", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
      20, 0.3, 0.2, -0.2, 10.0, 5, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
       (0.5, 0.5), (1.0, 0.0), #alpha keys
      (0.5, .8), (1, 0.6),        #red keys
      (0.5, .8), (1, 0.6),       #green keys
      (0.5, 1), (1, 0.6),      #blue keys
      (0.0, 0.1), (1.0, 12.0),   #scale keys
      (0.2, 0.1, 0.01),          #emit box size
      (0, 0, 0.2),          #emit velocity
      0.1,               #emit dir randomness
      100,                 #rotation speed
      0.5                 #rotation damping
      ),
     ("flamethrower_holy_fire_6", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
      18, 0.3, 0.2, -0.2, 10.0, 5, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
       (0.5, 0.5), (1.0, 0.0), #alpha keys
      (0.5, .8), (1, 0.6),        #red keys
      (0.5, .8), (1, 0.6),       #green keys
      (0.5, 1), (1, 0.6),      #blue keys
      (0.0, 0.0), (1.0, 12.0),   #scale keys
      (0.2, 0.1, 0.01),          #emit box size
      (0, 0, 0.2),          #emit velocity
      0.1,               #emit dir randomness
      100,                 #rotation speed
      0.5                 #rotation damping
      ),
     ("flamethrower_holy_fire_7", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
      15, 0.3, 0.2, -0.2, 10.0, 5, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
       (0.5, 0.5), (1.0, 0.0), #alpha keys
      (0.5, .8), (1, 0.6),        #red keys
      (0.5, .8), (1, 0.6),       #green keys
      (0.5, 1), (1, 0.6),      #blue keys
      (0.0, 0.0), (1.0, 12.0),   #scale keys
      (0.2, 0.1, 0.01),          #emit box size
      (0, 0, 0.2),          #emit velocity
      0.1,               #emit dir randomness
      100,                 #rotation speed
      0.5                 #rotation damping
      ),
     ("flamethrower_holy_fire_8", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
      10, 0.3, 0.2, -0.2, 10.0, 5, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
       (0.5, 0.5), (1.0, 0.0), #alpha keys
      (0.5, .8), (1, 0.6),        #red keys
      (0.5, .8), (1, 0.6),       #green keys
      (0.5, 1), (1, 0.6),      #blue keys
      (0.0, 0.0), (1.0, 8.0),   #scale keys
      (0.2, 0.1, 0.01),          #emit box size
      (0, 0, 0.2),          #emit velocity
      0.1,               #emit dir randomness
      100,                 #rotation speed
      0.5                 #rotation damping
      ),
    
      ("arrows_fire_holy", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     10, 0.5, 0.0, -1.20, 25.0, 10.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
       (0.5, 0.5), (1.0, 0.0), #alpha keys
      (0.5, .8), (1, 0.6),        #red keys
      (0.5, .8), (1, 0.6),       #green keys
      (0.5, 1), (1, 0.6),      #blue keys
     (0, 2),   (1, 6),          #scale keys
     (1.0, 1.0, 0.2),           #emit box size
     (0, 0, 0),               #emit velocity
     0.0,                       #emit dir randomness
     250,                       #rotation speed
     0.3                        #rotation damping
    ),
    
      ("arrows_fire_poison", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     10, 0.5, 0.0, -1.20, 25.0, 10.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.3, 1.0), (1, 0.3),        #alpha keys
     (0.5, 0.0), (1, 0.0),      #red keys
     (0.5, 1.0),(1, 0.0),       #green keys
     (0.5, 0.0), (1, 0.0),      #blue keys
     (0, 2),   (1, 6),          #scale keys
     (1.0, 1.0, 0.2),           #emit box size
     (0, 0, 0),               #emit velocity
     0.0,                       #emit dir randomness
     250,                       #rotation speed
     0.3                        #rotation damping
    ),
    
    
     ("lightning_victim", psf_turn_to_velocity|psf_randomize_rotation|psf_randomize_size, "prt_lightning",
      10, 0.1, 0.0, 0.0, 10.0, 0.02,
      (0.66, 0.7), (1.0, 0.0),
      (0.1, 0.7), (1.0, 0.5),
      (0.1, 0.5), (1.0, 0.5),
      (0.1, 0.1), (1.0, 0.7),
      (0.1, 0.2), (1.0, 0.6),
      (0.2, 0.2, 0.2),
      (0.0, 0.3, 0.0),
      1.0,
      0.0,
      0.0
     ),
     ("lightning_attack", psf_turn_to_velocity|psf_randomize_rotation|psf_randomize_size, "prt_lightning",
      10, 0.1, 0.0, 0.0, 10.0, 0.02,
      (0.66, 0.7), (1.0, 0.0),
      (0.1, 0.7), (1.0, 0.5),
      (0.1, 0.5), (1.0, 0.5),
      (0.1, 0.1), (1.0, 0.7),
      (0.1, 2), (1.0, 0.2),
      (0.2, 0.2, 0.2),
      (0.0, 0.3, 0.0),
      1.0,
      0.0,
      0.0
     ),
    ("imp_desummon", psf_always_emit|psf_global_emit_dir|psf_billboard_3d, "rune_circle_1",
     5, 2.0, 0, 0.0, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.50, 0.50), (1.00, 0.00),
     (0.00, 0.00), (1.00, 0.10),
     (0.00, 0.20), (1.00, 0.30),
     (0.00, 0.70), (1.00, 1.00),
     (0.0, 50),   (1.0, 50),   #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0, 0, 10),                 #emit velocity
     0.0,                       #emit dir randomness
     0,                       #rotation speed
     0.5                        #rotation damping
    ),
    
    ("skeleton_summoned", psf_always_emit|psf_global_emit_dir|psf_billboard_3d, "rune_circle_11",
     5, 2.0, 0, 0.0, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.20, 0.70), (1.00, 0.00),
     (0.00, 0.60), (1.00, 0.60),
     (0.00, 0.40), (1.00, 0.40),
     (0.00, 0.60), (1.00, 0.60),
     (0.0, 50),   (1.0, 50),   #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0, 0, 10),                 #emit velocity
     0.0,                       #emit dir randomness
     0,                       #rotation speed
     0.5                        #rotation damping
     ),
    ("demon_summoned", psf_always_emit|psf_global_emit_dir|psf_billboard_3d, "rune_circle_8",
     5, 2.0, 0, 0.0, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.20, 0.70), (1.00, 0.00),
     (0.20, 1.50), (1.00, 2.00),
     (0.20, 0.70), (1.00, 0.30),
     (0.20, 0.20), (1.00, 0.00),
     (0.0, 50),   (1.0, 50),   #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0, 0, 10),                 #emit velocity
     0.0,                       #emit dir randomness
     0,                       #rotation speed
     0.5                        #rotation damping
     ),
    
("warpstone_smoke", psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prtcl_dust_a",
60, 18.00, 2.00, -0.002030, 90.00, 1.80,
(0.00, 0.98), (0.94, 0.00),
(0.00, 0.20), (1.00, 0.20),
(0.00, 0.70), (1.00, 0.70),
(0.00, 0.40), (1.00, 0.40),
(-0.09, 3.20), (0.50, 11.00),
(0.04, 0.04, 0.04),
(0.00, 4.00, 0.00),
0.70,
70.00,
0.40
),
    
    ("torch_snow", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_Snowflake_a",
     15, 0.35, 0.2, 0.03, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.8), (1.0, 0.0),
     (0.5, 0.6), (1.0, 0.0),
     (0.5, 0.88), (1.0, 0.0),
     (0.5, 1.0), (1.0, 0.0),
     (0, 0.0),   (0.4, 0.15),   #scale keys
     (0.04, 0.04, 0.01),      #emit box size
     (0, 0, 0.5),               #emit velocity
     0.0,                       #emit dir randomness
     200,                       #rotation speed
     0.5                        #rotation damping
    ),

    ("torch_snow_smoke", psf_billboard_3d|psf_global_emit_dir|psf_always_emit, "prtcl_dust_a",
     15, 0.5, 0.2, -0.2, 10.0, 0.1,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 1.0), (1.0, 0.5),
     (0.0, 0.19), (1.0, 0.0),
     (0.0, 0.6), (1.0, 0.0),
     (0.0, 1.0), (1.0, 0.0),
     (0, 0.5),   (0.8, 2.5),    #scale keys
     (0.1, 0.1, 0.1),           #emit box size
     (0, 0, 1.5),               #emit velocity
     0.1                        #emit dir randomness
    ),

    ("torch_holy", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     50, 0.35, 0.2, 0.03, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.5), (1.0, 0.0), #alpha keys
     (0.5, .8), (1, 0.6),        #red keys
     (0.5, .8), (1, 0.6),       #green keys
     (0.5, 1), (1, 0.6),      #blue keys
     (0, 0.15),   (0.4, 0.3),   #scale keys
     (0.04, 0.04, 0.01),      #emit box size
     (0, 0, 0.5),               #emit velocity
     0.0,                       #emit dir randomness
     200,                       #rotation speed
     0.5                        #rotation damping
    ),

("fire_smierc", psf_always_emit|psf_global_emit_dir|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_fire_1",
20, 0.4, 0.2, 0.03, 10.0, 0.0,
(0.5, 0.8), (1.0, 0.0),
(0.5, 1.0), (1.0, 0.9),
(0.5, 0.7), (1.0, 0.3),
(0.5, 0.2), (1.0, 0.0),
(0.0, 0.3), (0.4, 2.9),
(0.4, 0.4, 0.3),
(0.0, 0.0, 0.5),
1.0,
200.0,
0.5
),

    ("dragon_smoke", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation, "prtcl_dust_a",
     80, 5, 20, 0, 3, 80,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.5), (1, 0),        #alpha keys
     (0.5, 1), (1, 0.9),      #red keys
     (0.5, 0.1),(1, 0.0),       #green keys
     (0.5, 0.0), (1, 0.0),      #blue keys
     (0, 5),   (1, 14.0),     #scale keys
     (0, 0.5, 0),                 #emit box size
     (0, 50, 0),                 #emit velocity
     0.5,                        #emit dir randomness
     50,                        #rotation speed
     0.3                        #rotation damping
    ),

    ("gorgon_smoke", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation, "prtcl_dust_a",
     80, 5, 20, 0, 3, 80,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.5), (1, 0),        #alpha keys
     (0.5, 0.0), (1, 0.0),      #red keys
     (0.5, 0.4),(1, 0.2),       #green keys
     (0.5, 0.8), (1, 0.6),      #blue keys
     (0, 5),   (1, 14.0),     #scale keys
     (0, 0.5, 0),                 #emit box size
     (0, 50, 0),                 #emit velocity
     0.5,                        #emit dir randomness
     50,                        #rotation speed
     0.3                        #rotation damping
    ),

    ("gorgon_smoke", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation, "prtcl_dust_a",
     80, 5, 20, 0, 3, 80,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.5), (1, 0),        #alpha keys
     (0.5, 0.0), (1, 0.0),      #red keys
     (0.5, 0.4),(1, 0.2),       #green keys
     (0.5, 0.8), (1, 0.6),      #blue keys
     (0, 5),   (1, 14.0),     #scale keys
     (0, 0.5, 0),                 #emit box size
     (0, 50, 0),                 #emit velocity
     0.5,                        #emit dir randomness
     50,                        #rotation speed
     0.3                        #rotation damping
    ),

   ("excalibur_light", 0, "prtcl_excalibur_light",
    1, 0.4, 0.0, 0.0, 2.5, 0.9,
    (0.0, 0.8), (0.0, 0.0),
    (0.0, 0.7), (1.0, 0.4),
    (0.0, 0.7), (1.0, 0.4),
    (0.0, 0.7), (1.0, 0.4),
    (1.0, 15), (0.0, 0.1),
    (0.1, 0.1, 0.1),
    (0.0, 0.0, 0.0),
    0.1,
    0.0,
    0.0
   ),
   ("element_burst_poisoning", psf_always_emit|psf_global_emit_dir|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_smoke_1",
    50, 0.6, 0.2, 0.0, 10.0, 10.0,
    (0.3, 0.7), (1.0, 0.0),
    (0.3, 0.1), (1.0, 0.1),
    (0.3, 0.9), (1.0, 0.9),
    (0.3, 0.3), (1.0, 0.3),
    (0.0, 1.0), (1.0, 4.0),
    (0.9, 0.9, 0.1),
    (1.0, 1.0, 0.1),
    2.0,
    200.0,
    0.5
   ),

   ("ligntaura_glow_red", psf_always_emit|psf_global_emit_dir|psf_billboard_3d, "prt_mesh_fire_2",
    1, 0.2, 0.0, 0.0, 1.0, 0.0,
    (0.5, 0.3), (1.0, 0.0),
    (0.0, 0.9), (1.0, 0.9),
    (0.0, 0.3), (1.0, 0.3),
    (0.0, 0.1), (1.0, 0.1),
    (0.0, 1.0), (1.0, 5.0),
    (0.0, 0.0, 0.0),
    (0.0, 0.0, 0.0),
    0.0,
    0.0,
    0.0
),

("element_burst_sky", psf_billboard_3d|psf_randomize_size, "prt_mesh_dust_1",
300, 0.6, 5.0, 0.0, 5.0, 10.0,
(0.1, 0.4), (1.0, 0.0),
(0.1, 0.1), (1.0, 0.1),
(0.1, 0.7), (1.0, 0.7),
(0.1, 0.3), (1.0, 0.3),
(0.0, 0.5), (1.0, 1.5),
(0.1, 0.1, 0.1),
(0.3, 0.3, 0.3),
2.0,
10.0,
0.1
),

("element_burst_water", psf_billboard_3d|psf_randomize_size, "prt_mesh_dust_1",
300, 0.6, 5.0, 0.0, 5.0, 10.0,
(0.1, 0.4), (1.0, 0.0),
(0.1, 0.1), (1.0, 0.1),
(0.1, 0.4), (1.0, 0.4),
(0.1, 0.7), (1.0, 0.7),
(0.0, 0.5), (1.0, 1.5),
(0.1, 0.1, 0.1),
(0.3, 0.3, 0.3),
2.0,
10.0,
0.1
),

("plus_ice_1", psf_always_emit|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_ice_1",
50, 0.3, 0.2, 1.0, 1.0, 2.0,
(0.5, 0.8), (1.0, 0.0),
(0.1, 0.9), (1.0, 0.9),
(0.1, 0.9), (1.0, 0.9),
(0.1, 0.9), (1.0, 0.9),
(0.4, 0.3), (1.0, 0.1),
(0.1, 0.1, 0.1),
(0.0, 0.0, 0.1),
2.0,
100.0,
0.2
),
("plus_ice_2", psf_always_emit|psf_global_emit_dir|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_ice_1",
30, 1.0, 0.2, 0.0, 10.0, 0.0,
(0.5, 0.7), (1.0, 0.2),
(0.1, 0.9), (1.0, 0.9),
(0.1, 0.9), (1.0, 0.9),
(0.1, 0.9), (1.0, 0.9),
(0.4, 0.5), (1.0, 0.5),
(0.2, 0.2, 0.2),
(0.0, 0.0, 0.0),
0.0,
0.0,
0.0
),
("vampire_rune_1", psf_randomize_rotation, "rune_circle_1",
1, 2.0, 8.0, 0.0, 0.0, 0.0,
(0.0, 1.0), (1.0, 0.0),
(0.0, 0.4), (1.0, 0.8),
(0.0, 0.1), (1.0, 0.2),
(0.0, 0.2), (1.0, 0.3),
(0.0, 2.0), (1.0, 2.0),
(1.0, 1.0, 0.1),
(0.0, 0.0, 0.5),
5.0,
2.0,
0.2
),
("rune_test", psf_randomize_rotation, "rune_circle_3",
1, 2.0, 8.0, 0.0, 0.0, 0.0,
(0.0, 1.0), (1.0, 0.0),
(0.0, 0.4), (1.0, 0.8),
(0.0, 0.1), (1.0, 0.2),
(0.0, 0.2), (1.0, 0.3),
(0.0, 2.0), (1.0, 2.0),
(1.0, 1.0, 0.1),
(0.0, 0.0, 0.5),
5.0,
2.0,
0.2
),
("rune_test_2", psf_randomize_rotation, "rune_circle_4",
1, 2.0, 8.0, 0.0, 0.0, 0.0,
(0.0, 1.0), (1.0, 0.0),
(0.0, 0.4), (1.0, 0.8),
(0.0, 0.1), (1.0, 0.2),
(0.0, 0.2), (1.0, 0.3),
(0.0, 2.0), (1.0, 2.0),
(1.0, 1.0, 0.1),
(0.0, 0.0, 0.5),
5.0,
2.0,
0.2
),

("heal_rune_1", psf_randomize_rotation, "rune_circle_3",
1, 2.0, 8.0, 0.0, 0.0, 0.0,
(0.0, 1.0), (1.0, 0.0),
(0.0, 0.1), (1.0, 0.2),
(0.0, 0.4), (1.0, 0.8),
(0.0, 0.2), (1.0, 0.4),
(0.0, 2.0), (1.0, 2.0),
(1.0, 1.0, 0.1),
(0.0, 0.0, 0.5),
5.0,
2.0,
0.2
),
("heal_rune_2", psf_randomize_rotation, "rune_circle_8",
1, 2.0, 8.0, 0.0, 0.0, 0.0,
(0.0, 1.0), (1.0, 0.0),
(0.0, 0.1), (1.0, 0.2),
(0.0, 0.4), (1.0, 0.8),
(0.0, 0.2), (1.0, 0.4),
(0.0, 2.0), (1.0, 2.0),
(1.0, 1.0, 0.1),
(0.0, 0.0, 0.5),
5.0,
2.0,
0.2
),

("trap_rune_1", psf_randomize_rotation, "rune_circle_10",
1, 2.0, 8.0, 0.0, 0.0, 0.0,
(0.0, 1.0), (1.0, 0.0),
(0.5, 0.7), (1.0, 0.3),
(0.5, 0.7), (1.0, 0.3),
(0.5, 1.0), (1.0, 0.9),
(0.0, 2.0), (1.0, 2.0),
(1.0, 1.0, 0.1),
(0.0, 0.0, 0.5),
5.0,
2.0,
0.2
),
("trap_rune_2", psf_randomize_rotation, "rune_circle_11",
1, 2.0, 8.0, 0.0, 0.0, 0.0,
(0.0, 1.0), (1.0, 0.0),
(0.5, 0.7), (1.0, 0.3),
(0.5, 0.7), (1.0, 0.3),
(0.5, 1.0), (1.0, 0.9),
(0.0, 2.0), (1.0, 2.0),
(1.0, 1.0, 0.1),
(0.0, 0.0, 0.5),
5.0,
2.0,
0.2
),
("trap_rune_3", psf_randomize_rotation, "rune_circle_2",
1, 2.0, 8.0, 0.0, 0.0, 0.0,
(0.0, 1.0), (1.0, 0.0),
(0.5, 0.7), (1.0, 0.3),
(0.5, 0.7), (1.0, 0.3),
(0.5, 1.0), (1.0, 0.9),
(0.0, 2.0), (1.0, 2.0),
(1.0, 1.0, 0.1),
(0.0, 0.0, 0.5),
5.0,
2.0,
0.2
),
("trap_rune_4", psf_randomize_rotation, "rune_circle_3",
1, 2.0, 8.0, 0.0, 0.0, 0.0,
(0.0, 1.0), (1.0, 0.0),
(0.5, 0.7), (1.0, 0.3),
(0.5, 0.7), (1.0, 0.3),
(0.5, 1.0), (1.0, 0.9),
(0.0, 2.0), (1.0, 2.0),
(1.0, 1.0, 0.1),
(0.0, 0.0, 0.5),
5.0,
2.0,
0.2
),

#phaiak begin sea battles chief
    ("front_water", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation, "prtcl_splash_b",
	#("front_water", psf_randomize_size|psf_randomize_rotation|psf_emit_at_water_level, "prtcl_splash_b",
     10, 1, 6, 4, 5, 2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.2, 1), (1, 0),        #alpha keys
     (1, 1.0), (1, 1.0),      #red keys
     (1, 1.0), (1, 1.0),      #green keys
     (1, 1.0), (1, 1.0),      #blue keys
     (0.2, 2),   (1, 0),   #scale keys
     (-1, 0.2, 0.5),           #emit box size
     (3, 0, 7),               #emit velocity
     0.2,                       #emit dir randomness
     30,                       #rotation speed
     0.5                        #rotation damping
    ),

    ("front_water_2", psf_emit_at_water_level, "prt_foam_a_new",	#"prtcl_splash_b",	#psf_randomize_size|
     2, 2, 0.15, 0, 0, 0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.3), (1, 0),        #alpha keys
     (1, 1.0), (1, 1.0),      #red keys
     (1, 1.0), (1, 1.0),      #green keys
     (1, 1.0), (1, 1.0),      #blue keys
     (0.1, 3.0), (1, 2.0),   #scale keys
     (0, 0, 0),           	#emit box size
     (0, 1, 0),               #emit velocity
     0,                       #emit dir randomness
     0,                       #rotation speed
     0.1                        #rotation damping
    ),
	
    ("heck_water", psf_emit_at_water_level, "prt_foam_a_new",	#"prtcl_splash_b",	#psf_randomize_size|
     1, 13, 0.3, 0, 0, 0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.2), (1, 0),        #alpha keys
     (1, 1), (1, 1),      #red keys
     (1, 1), (1, 1),      #green keys
     (1, 1), (1, 1),      #blue keys
     (0.1, 5.0), (1, 6.0),   #scale keys
     (0, 0, 0),           #emit box size
     (0, 0.5, 0),               #emit velocity
     0,                       #emit dir randomness
     0,                       #rotation speed
     0.1                        #rotation damping
    ),
	
    ("ocean_wave", psf_emit_at_water_level, "prt_foam_a_new",
     1, 3, 0, 0, 0, 0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.5), (1, 0),        #alpha keys
     (1, 1), (1, 1),      #red keys
     (1, 1), (1, 1),      #green keys
     (1, 1), (1, 1),      #blue keys
     (0.1, 10), (1, 9),   #scale keys
     (0, 0, 0),           #emit box size
     (0, 2, 0),               #emit velocity
     0,                       #emit dir randomness
     0,                       #rotation speed
     0                       #rotation damping
    ),
	
#phaiak end
    ####Map icons
    ("icon_smoke", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_smoke_1",
     20, 3, 0.3, -0.11, 3.0, 2.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.15), (1, 0),       #alpha keys
     (0.2, 0.5), (1, 0.5),      #red keys
     (0.2, 0.5),(1, 0.5),       #green keys
     (0.2, 0.5), (1, 0.5),      #blue keys
     (0, 0.7),   (1, 1.3),      #scale keys
     (0.2, 0.2, 0.1),           #emit box size
     (0, 0, 0.015),             #emit velocity
     0.0,                       #emit dir randomness
     0,                         #rotation speed
     0.1                        #rotation damping
    ), 
	
    ("icon_chimney_smoke", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_smoke_1",
     15, 4, 0.3, -0.04, 1.0, 0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.15), (1, 0),       #alpha keys
     (0.2, 0.5), (1, 0.5),      #red keys
     (0.2, 0.5),(1, 0.5),       #green keys
     (0.2, 0.5), (1, 0.5),      #blue keys
     (0, 0.1),   (1, 0.4),      #scale keys
     (0.01, 0.01, 0.1),           #emit box size
     (0, 0, 0.01),             #emit velocity
     0.0,                       #emit dir randomness
     0,                         #rotation speed
     0.1                        #rotation damping
    ), 
	
    #chief siege warfare 
	 ("piedra_dust", psf_billboard_3d, "prtcl_dust_a",
     1, 1, 0, -0.2, 60.0, 1.5,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 1), (1, 0),       #alpha keys
     (0.0, 0.4), (1, 0.2),      #red keys
     (0.0, 0.4),(1, 0.2),       #green keys
     (0.0, 0.4), (1, 0.2),      #blue keys
     (0, 10.0),   (15.0, 20.0),   #scale keys
     (0.1, 0.1, 0.1),           #emit box size
     (0, 0, 0),                 #emit velocity
     0,                        #emit dir randomness
    ),
	
	("dummy_stone", psf_randomize_size | psf_randomize_rotation,  "stone_ball",
     500, 1, 5, 0.9, 10, 2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 1), (1, 1),          #alpha keys
     (0.1, 0.6), (1, 0.6),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.4), (1, 0.4),      #blue keys
     (0.0, 0.3),   (1, 0.3),    #scale keys
     (0.2, 0.2, 0.5),           #emit box size
     (0, 0, 0),                 #emit velocity
     2.3,                       #emit dir randomness
     100,                       #rotation speed
     0,                       #rotation damping
    ),
	
	("dummy_salt", psf_randomize_size | psf_randomize_rotation,  "salt_a",
     500, 1, 3, 0.9, 10, 2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 1), (1, 1),          #alpha keys
     (0.1, 0.6), (1, 0.6),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.4), (1, 0.4),      #blue keys
     (0.0, 0.3),   (1, 0.3),    #scale keys
     (0.2, 0.2, 0.5),           #emit box size
     (0, 0, 0),                 #emit velocity
     2.3,                       #emit dir randomness
     100,                       #rotation speed
     0,                       #rotation damping
    ),

    ("decap_blood", psf_billboard_3d | psf_randomize_size|psf_randomize_rotation ,  "prt_mesh_blood_3",
     300, 1, 1, 1, 1, 5,        #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.7), (1, 0.2),        #alpha keys
     (0.1, 0.4), (1, 0.05),      #red keys
     (1.0, 0.05),(1, 0.05),      #green keys
     (1.0, 0.05),(1, 0.05),      #blue keys
     (0.1, 0.2),   (0.4, 0.8),  	#scale keys
     (0.2, 0.2, 0.2),               	#emit box size
     (0, 0, 3),             #emit velocity
     0.1,                       #emit dir randomness
     6,                         #rotation speed
     0,                         #rotation damping
    ),

    ("no_blood", psf_billboard_3d,  "empty",
     0, 0, 3, 0.5, 0, 0,        #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 0.7), (0, 0.7),          #alpha keys
     (0.1, 0.7), (1, 0.7),      #red keys
     (0.1, 0.7), (1, 0.7),       #green keys
     (0.1, 0.7), (1, 0.7),      #blue keys
     (0.0, 0.015),   (1, 0.018),  #scale keys
     (0, 0.05, 0),               #emit box size
     (0, 1.0, 0.3),                #emit velocity
     0.9,                       #emit dir randomness
     0,                         #rotation speed
     0,                         #rotation damping
    ),
    ("torch_fire_2", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     25, 0.15, 0.8, 0.03, 5.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.2, 0.8), (1, 0),        #alpha keys
     (0.2, 1.0), (1, 0.9),      #red keys
     (0.2, 0.7),(1, 0.3),       #green keys
     (0.2, 0.2), (1, 0.0),      #blue keys
     (0, 0.15),   (0.4, 0.3),   #scale keys
     (0.04, 0.04, 0.01),      #emit box size
     (0, 0, 0.5),               #emit velocity
     0.0,                       #emit dir randomness
     50,                       #rotation speed
     0.5                        #rotation damping
    ),

  ("frost_nails", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation|psf_2d_turbulance, "frost_nails",
     15, 0.2,  0.4, 0.05, 10.0, 39.0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 1), (1, 0.3),          #alpha keys
     (3.0, 1.0), (5, 1.0),      #red keys
     (3.0, 1.0), (5, 1.0),      #green keys
     (3.0, 1.0), (5, 1.0),      #blue keys
     (0, 0.1),   (0.5, 5),   #scale keys
     (0.0, 0.0, 0.0),
     (0.0, 0.0, 0.0),
     0,                         #emit dir randomness
     0,                       #rotation speed
     0                        #rotation damping
    ),

     ("magic_curse_small", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation|psf_2d_turbulance, "prt_mesh_Poison_b",
     2, 0.2,  0.4, 0.05, 10.0, 39.0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.3, 1.0), (1, 0.3),        #alpha keys
     (0.5, 1), (1, 0.9),      #red keys
     (0.5, 0.1),(1, 0.0),       #green keys
     (0.5, 0.0), (1, 0.0),      #blue keys
     (0.5, 3),   (1.0, 3.7),   #scale keys
     (0.2, 0.4, 0.1),           #emit box size
     (0, 0, 1),                 #emit velocity
     2,                         #emit dir randomness
     0,                       #rotation speed
     0                        #rotation damping
    ),  
        
    ("arcane_explosion", psf_billboard_3d|psf_randomize_size,  "flash_arcane_01",
     20, 0.15, 0.4, 0.2, 3, 10,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.6, 1), (0.7, 0),          #alpha keys
     (1.0, 0.0), (1, 0),      #red keys
     (1.0, 0.7),(0.3, 0),       #green keys
     (0.0, 1), (1.0, 0.5),      #blue keys
     (0, 20.0), (0.3, 0.3),    #scale keys
     (0.5, 0.5, 0.5),           #emit box size
     (0.5, 0.5, 0.5),                 #emit velocity
     30.0,                       #emit dir randomness
    ),
    
     ("black_hold", psf_billboard_2d|psf_randomize_size|psf_randomize_rotation|psf_2d_turbulance, "black_aura",
     2, 2,  0.4, 0.05, 10.0, 39.0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.3, 1.0), (1, 0.3),        #alpha keys
     (1.0, 1.0), (1, 1.0),      #red keys
     (1.0, 1.0), (1, 1.0),      #green keys
     (1.0, 1.0), (1, 1.0),      #blue keys
     (0.5, 30),   (2, 10),   #scale keys
     (0.2, 0.4, 0.1),           #emit box size
     (0, 0, 1),                 #emit velocity
     2,                         #emit dir randomness
     0,                       #rotation speed
     0                        #rotation damping
    ),  
    
    ("flame_explosion", psf_billboard_3d|psf_randomize_size,  "earthquakeRune_cost_moltenFlash_add",
     20, 0.8, 0.4, 0.2, 3, 10,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.3, .3), (0.7, 0.9),          #alpha keys
     (1.0, 1.0), (1, 0),      #red keys
     (0.7, 0.5),(0.3, 0),       #green keys
     (0.0, 0.0), (0.0, 0),      #blue keys
     (0, 40.0), (0.3, 0.3),    #scale keys
     (0.5, 0.5, 0.5),           #emit box size
     (0.5, 0.5, 0.5),                 #emit velocity
     30.0,                       #emit dir randomness
    ),

     ("spark_explosion_small", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation|psf_2d_turbulance, "earthquakeRune_cost_cracks_mask",#prt_mesh_dust_1
     15, 0.2,  0.4, 0.05, 10.0, 39.0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.3, 1.0), (1, 0.3),        #alpha keys
     (1.0, 1.0), (1, 1.0),      #red keys
     (1.0, 1.0), (1, 1.0),      #green keys
     (1.0, 1.0), (1, 1.0),      #blue keys
     (0.5, 3),   (1.0, 3.7),   #scale keys
     (0.2, 0.4, 0.1),           #emit box size
     (0, 0, 1),                 #emit velocity
     2,                         #emit dir randomness
     0,                       #rotation speed
     0                        #rotation damping
    ),  

     ("spark_explosion", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation|psf_2d_turbulance, "earthquakeRune_cost_cracks_mask",#prt_mesh_dust_1
     5, 0.2,  0.4, 0.05, 10.0, 39.0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.3, 1.0), (1, 0.3),        #alpha keys
     (1.0, 1.0), (1, 1.0),      #red keys
     (1.0, 1.0), (1, 1.0),      #green keys
     (1.0, 1.0), (1, 1.0),      #blue keys
     (0.5, 15),   (1.0, 10.7),   #scale keys
     (0.2, 0.4, 0.1),           #emit box size
     (0, 0, 1),                 #emit velocity
     2,                         #emit dir randomness
     0,                       #rotation speed
     0                        #rotation damping
    ),  

     ("spark_explosion_2", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation|psf_2d_turbulance, "hammeroftheAncientsRune_lava_magicCracks",#prt_mesh_dust_1
     5, 0.2,  0.4, 0.05, 10.0, 39.0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.3, 1.0), (1, 0.3),        #alpha keys
     (1.0, 1.0), (1, 1.0),      #red keys
     (1.0, 1.0), (1, 1.0),      #green keys
     (1.0, 0.0), (1, 0.0),      #blue keys
     (0.5, 15),   (1.0, 10.7),   #scale keys
     (0.2, 0.4, 0.1),           #emit box size
     (0, 0, 1),                 #emit velocity
     2,                         #emit dir randomness
     0,                       #rotation speed
     0                        #rotation damping
    ),  

    ("fat_arrow", psf_always_emit|psf_billboard_2d|psf_global_emit_dir, "arrow_up_rot",
     10, 0.1, 0.0, 0.0, 100.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 0.6), (1.0, 0.7),          #alpha keys
     (0.0, 0.0), (1.0, 0.0),      #red keys
     (0.0, 1.0), (1.0, 1.0),       #green keys
     (0.0, 0.0), (1.0, 0.0),      #blue keys
     (0, 20),    (1.0, 10.0),        #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0.0, 0.0, 0.0),                 #emit velocity
     0.0,                       #emit dir randomness
     0,
     0
    ),
    
    ("fat_arrow_red", psf_always_emit|psf_billboard_2d|psf_global_emit_dir, "arrow_up_rot",
     10, 0.1, 0.0, 0.0, 100.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 1.0), (1.0, 0.3),          #alpha keys
     (0.0, 1.0), (1.0, 1.0),      #red keys
     (0.0, 0.0), (1.0, 0.0),       #green keys
     (0.0, 0.0), (1.0, 0.0),      #blue keys
     (0, 10),    (1.0, 10),        #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0.0, 0.0, 0.0),                 #emit velocity
     0.0,                       #emit dir randomness
     0,
     0
    ),
    
    ("fat_arrow_blue", psf_always_emit|psf_billboard_2d|psf_global_emit_dir, "arrow_up_rot",
     50, 0.1, 0.0, 0.0, 100.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 0.3), (1.0, 1.0),          #alpha keys
     (0.0, 0.0), (1.0, 0.0),      #red keys
     (0.0, 0.0), (1.0, 0.0),       #green keys
     (0.0, 1.0), (1.0, 1.0),      #blue keys
     (0, 10),    (1.0, 10.0),        #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0.0, 0.0, 0.0),                 #emit velocity
     0.0,                       #emit dir randomness
     0,
     0
    ),
    
    ("fat_arrow_rising", psf_always_emit|psf_billboard_2d|psf_global_emit_dir, "arrow_up_rot",
     100, 0.1, 0.0, 0.0, 0.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 0.7), (1.0, 0.7),          #alpha keys
     (0.25, 0.0), (1, 1.0),      #red keys
     (0.0, 1.0),(0.5, 0.0),       #green keys
     (0.0, 0.0), (1, 0.0),      #blue keys
     (0, 30),   (1.0, 30),        #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0.0, 0, 3),                 #emit velocity
     0.0,                       #emit dir randomness
     0,
     0
    ),

("fire_enchantment", psf_always_emit|psf_global_emit_dir|psf_billboard_2d|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_fire_1",
550, 0.55, -0.70, -0.05, 0.02, 0.02,
(0.50, 1.00), (1.00, 0.00),
(0.50, 1.00), (1.00, 0.90),
(0.50, 0.70), (1.00, 0.30),
(0.50, 0.20), (1.00, 0.00),
(0.20, 0.05), (0.30, 0.20),
(0.06, 0.48, 0.06),
(0.00, 0.00, 0.00),
0.20,
50.00,
0.50
),
("fire_enchantment_sparks", psf_always_emit|psf_billboard_2d|psf_billboard_3d, "prt_sparks_mesh_1",
400, 0.70, 0.30, -0.20, 0.10, 10.00,
(0.10, 0.80), (1.00, 0.00),
(0.50, 1.00), (1.00, 0.90),
(0.50, 0.60), (1.00, 0.10),
(0.50, 0.20), (1.00, 0.00),
(0.10, 0.05), (1.00, 0.05),
(0.02, 0.45, 0.02),
(0.00, 0.00, 0.00),
0.10,
0.00,
0.00
),
("fire_enchantment_mace", psf_always_emit|psf_global_emit_dir|psf_billboard_2d|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_fire_1",
220, 0.55, -0.70, -0.05, 0.02, 0.02,
(0.50, 1.00), (1.00, 0.00),
(0.50, 1.00), (1.00, 0.90),
(0.50, 0.70), (1.00, 0.30),
(0.50, 0.20), (1.00, 0.00),
(0.20, 0.05), (0.30, 0.20),
(0.05, 0.05, 0.05),
(0.00, 0.00, 0.00),
0.20,
50.00,
0.50
),
("fire_enchantment_sparks_mace", psf_always_emit|psf_billboard_2d|psf_billboard_3d, "prt_sparks_mesh_1",
300, 0.70, 0.30, -0.20, 0.10, 10.00,
(0.10, 0.80), (1.00, 0.00),
(0.50, 1.00), (1.00, 0.90),
(0.50, 0.60), (1.00, 0.10),
(0.50, 0.20), (1.00, 0.00),
(0.10, 0.05), (1.00, 0.05),
(0.08, 0.08, 0.08),
(0.00, 0.00, 0.00),
0.10,
0.00,
0.00
),
("frost_enchantment", psf_always_emit|psf_global_emit_dir|psf_billboard_2d|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prtcl_dust_a",
550, 0.80, 0.20, 0.01, 0.20, 0.20,
(0.10, 0.75), (1.00, 0.00),
(0.00, 0.40), (0.90, 0.45),
(0.00, 0.40), (0.90, 0.45),
(0.00, 0.90), (1.00, 1.00),
(0.01, 0.40), (1.00, 0.90),
(0.04, 0.51, 0.04),
(0.00, 0.00, 0.00),
0.03,
10.00,
0.50
),
("frost_enchantment_sparks", psf_always_emit|psf_billboard_2d|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_snow_fall_1",
13, 4.10, -0.03, 0.001000, 0.001000, 0.001000,
(0.10, 0.80), (1.00, 0.00),
(0.00, 0.70), (1.00, 0.80),
(0.00, 0.70), (1.00, 0.80),
(0.00, 0.90), (1.00, 1.00),
(0.10, 0.10), (1.00, 0.15),
(0.17, 0.52, 0.17),
(0.00, 0.00, 0.00),
0.000200,
50.00,
0.50
),
("frost_enchantment_mace", psf_always_emit|psf_global_emit_dir|psf_billboard_2d|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prtcl_dust_a",
225, 0.80, 0.20, 0.01, 0.20, 0.20,
(0.10, 0.75), (1.00, 0.00),
(0.00, 0.40), (0.90, 0.45),
(0.00, 0.40), (0.90, 0.45),
(0.00, 0.90), (1.00, 1.00),
(0.01, 0.40), (1.00, 0.90),
(0.04, 0.04, 0.04),
(0.00, 0.00, 0.00),
0.03,
10.00,
0.50
),
("frost_enchantment_sparks_mace", psf_always_emit|psf_billboard_2d|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_snow_fall_1",
13, 4.10, -0.03, 0.001000, 0.001000, 0.001000,
(0.10, 0.80), (1.00, 0.00),
(0.00, 0.70), (1.00, 0.80),
(0.00, 0.70), (1.00, 0.80),
(0.00, 0.90), (1.00, 1.00),
(0.10, 0.10), (1.00, 0.15),
(0.17, 0.17, 0.17),
(0.00, 0.00, 0.00),
0.000200,
50.00,
0.50
),
("curse_enchantment", psf_always_emit|psf_global_emit_dir|psf_billboard_2d|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prtcl_dust_a",
550, 0.80, 0.20, 0.01, 0.20, 0.20,
(0.10, 0.75), (1.00, 0.00),
(0.00, 1.80), (1.00, 1.80),
(0.00, 0.30), (1.00, 0.30),
(0.00, 1.10), (1.00, 1.10),
(0.01, 0.40), (1.00, 0.90),
(0.04, 0.51, 0.04),
(0.00, 0.00, 0.00),
0.03,
10.00,
0.50
),
("curse_enchantment_sparks", psf_always_emit|psf_billboard_2d|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_snow_fall_1",
13, 4.10, -0.03, 0.001000, 0.001000, 0.001000,
(0.10, 0.80), (1.00, 0.00),
(0.00, 1.80), (1.80, 1.80),
(0.00, 0.30), (0.30, 0.30),
(0.00, 1.10), (1.10, 1.10),
(0.10, 0.10), (1.00, 0.15),
(0.17, 0.52, 0.17),
(0.00, 0.00, 0.00),
0.000200,
50.00,
0.50
),
("curse_enchantment_mace", psf_always_emit|psf_global_emit_dir|psf_billboard_2d|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prtcl_dust_a",
220, 0.80, 0.20, 0.01, 0.20, 0.20,
(0.10, 0.75), (1.00, 0.00),
(0.00, 1.80), (1.00, 1.80),
(0.00, 0.30), (1.00, 0.30),
(0.00, 1.10), (1.00, 1.10),
(0.01, 0.40), (1.00, 0.90),
(0.04, 0.04, 0.04),
(0.00, 0.00, 0.00),
0.03,
10.00,
0.50
),
("curse_enchantment_sparks_mace", psf_always_emit|psf_billboard_2d|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_snow_fall_1",
13, 4.10, -0.03, 0.001000, 0.001000, 0.001000,
(0.10, 0.80), (1.00, 0.00),
(0.00, 1.80), (1.80, 1.80),
(0.00, 0.30), (0.30, 0.30),
(0.00, 1.10), (1.10, 1.10),
(0.10, 0.10), (1.00, 0.15),
(0.17, 0.17, 0.17),
(0.00, 0.00, 0.00),
0.000200,
50.00,
0.50
),
("poison_enchantment", psf_always_emit|psf_global_emit_dir|psf_billboard_2d|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prtcl_dust_a",
200, 0.70, 5.20, 0.00, 0.00, 0.00,
(0.00, 0.60), (1.00, 0.00),
(0.00, 0.45), (1.00, 0.45),
(0.00, 0.90), (1.00, 1.00),
(0.00, 0.30), (1.00, 0.30),
(0.01, 0.70), (1.00, 1.10),
(0.01, 0.47, 0.01),
(0.00, 0.00, 0.00),
0.10,
10.00,
0.50
),
("poison_enchantment_2", psf_always_emit|psf_global_emit_dir|psf_billboard_2d|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_fire_1",
300, 0.50, 0.50, -0.00, 0.00, 0.00,
(0.00, 0.20), (1.00, 0.00),
(0.00, 0.40), (1.00, 0.40),
(0.00, 0.90), (1.00, 1.00),
(0.00, 0.30), (1.00, 0.30),
(1.00, 0.20), (0.01, 0.20),
(0.01, 0.47, 0.01),
(0.00, 0.00, 0.00),
0.000100,
1000.00,
0.001000
),
("poison_enchantment_sparks", psf_always_emit|psf_billboard_2d|psf_billboard_3d, "prt_sparks_mesh_1",
2, 4.00, 0.50, 0.00, 0.10, 1.00,
(0.10, 0.80), (1.00, 0.00),
(0.10, 0.50), (1.00, 0.60),
(0.00, 1.00), (1.00, 1.00),
(0.10, 0.00), (0.50, 0.10),
(0.10, 0.05), (1.00, 0.07),
(0.11, 0.55, 0.11),
(0.00, 0.00, 0.00),
0.000200,
0.00,
0.00
),
("poison_enchantment_mace", psf_always_emit|psf_global_emit_dir|psf_billboard_2d|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prtcl_dust_a",
200, 0.70, 5.20, 0.00, 0.00, 0.00,
(0.00, 0.60), (1.00, 0.00),
(0.00, 0.45), (1.00, 0.45),
(0.00, 0.90), (1.00, 1.00),
(0.00, 0.30), (1.00, 0.30),
(0.01, 0.70), (1.00, 1.10),
(0.02, 0.02, 0.02),
(0.00, 0.00, 0.00),
0.10,
10.00,
0.50
),
("poison_enchantment_2_mace", psf_always_emit|psf_global_emit_dir|psf_billboard_2d|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_fire_1",
300, 0.50, 0.50, -0.00, 0.00, 0.00,
(0.00, 0.20), (1.00, 0.00),
(0.00, 0.40), (1.00, 0.40),
(0.00, 0.90), (1.00, 1.00),
(0.00, 0.30), (1.00, 0.30),
(1.00, 0.20), (0.01, 0.20),
(0.02, 0.02, 0.02),
(0.00, 0.00, 0.00),
0.000100,
1000.00,
0.001000
),
("poison_enchantment_sparks_mace", psf_always_emit|psf_billboard_2d|psf_billboard_3d, "prt_sparks_mesh_1",
2, 4.00, 0.50, 0.00, 0.10, 1.00,
(0.10, 0.80), (1.00, 0.00),
(0.10, 0.50), (1.00, 0.60),
(0.00, 1.00), (1.00, 1.00),
(0.10, 0.00), (0.50, 0.10),
(0.10, 0.05), (1.00, 0.07),
(0.11, 0.11, 0.11),
(0.00, 0.00, 0.00),
0.000200,
0.00,
0.00
),
("holy_enchantment", psf_always_emit|psf_global_emit_dir|psf_billboard_2d|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prtcl_dust_a",
550, 0.80, 0.20, 0.01, 0.20, 0.20,
(0.10, 0.75), (1.00, 0.00),
(1.00, 1.00), (1.00, 255.00),
(1.00, 1.00), (1.00, 255.00),
(1.00, 1.00), (1.00, 255.00),
(0.01, 0.40), (1.00, 0.90),
(0.04, 0.51, 0.04),
(0.00, 0.00, 0.00),
0.03,
10.00,
0.50
),
("holy_enchantment_sparks", psf_always_emit|psf_billboard_2d|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_snow_fall_1",
13, 4.10, -0.03, 0.001000, 0.001000, 0.001000,
(0.10, 0.80), (1.00, 0.00),
(0.00, 0.70), (1.00, 255.00),
(0.00, 0.70), (1.00, 255.00),
(0.00, 0.90), (1.00, 255.00),
(0.10, 0.10), (1.00, 0.15),
(0.17, 0.52, 0.17),
(0.00, 0.00, 0.00),
0.000200,
50.00,
0.50
),
("holy_enchantment_mace", psf_always_emit|psf_global_emit_dir|psf_billboard_2d|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prtcl_dust_a",
550, 0.80, 0.20, 0.01, 0.20, 0.20,
(0.10, 0.75), (1.00, 0.00),
(1.00, 1.00), (1.00, 255.00),
(1.00, 1.00), (1.00, 255.00),
(1.00, 1.00), (1.00, 255.00),
(0.01, 0.40), (1.00, 0.90),
(0.05, 0.05, 0.05),
(0.00, 0.00, 0.00),
0.03,
10.00,
0.50
),
("holy_enchantment_sparks_mace", psf_always_emit|psf_billboard_2d|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_snow_fall_1",
13, 4.10, -0.03, 0.001, 0.001, 0.001,
(0.10, 0.80), (1.00, 0.00),
(0.00, 0.70), (1.00, 255.00),
(0.00, 0.70), (1.00, 255.00),
(0.00, 0.90), (1.00, 255.00),
(0.10, 0.10), (1.00, 0.15),
(0.17, 0.17, 0.17),
(0.00, 0.00, 0.00),
0.200,
50.00,
0.50
),
("vampire_enchantment", psf_always_emit|psf_global_emit_dir|psf_billboard_2d|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prtcl_dust_a",
550, 0.80, 0.20, 0.01, 0.20, 0.20,
(0.10, 0.75), (1.00, 0.00),
(1.00, 1.00), (1.00, 1.00),
(0.00, 0.00), (0.00, 0.00),
(0.00, 0.00), (0.00, 0.00),
(0.01, 0.40), (1.00, 0.90),
(0.04, 0.51, 0.04),
(0.00, 0.00, 0.00),
0.03,
10.00,
0.50
),
("vampire_enchantment_sparks", psf_always_emit|psf_billboard_2d|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_snow_fall_1",
13, 4.10, -0.03, 0.001, 0.001, 0.001,
(0.10, 0.80), (1.00, 0.00),
(0.00, 1.00), (1.00, 1.00),
(0.00, 0.00), (0.00, 0.00),
(0.00, 0.00), (0.00, 0.00),
(0.10, 0.10), (1.00, 0.15),
(0.17, 0.52, 0.17),
(0.00, 0.00, 0.00),
0.200,
50.00,
0.50
),
("vampire_enchantment_mace", psf_always_emit|psf_global_emit_dir|psf_billboard_2d|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prtcl_dust_a",
550, 0.80, 0.20, 0.01, 0.20, 0.20,
(0.10, 0.75), (1.00, 0.00),
(1.00, 1.00), (1.00, 1.00),
(0.00, 0.00), (0.00, 0.00),
(0.00, 0.00), (0.00, 0.00),
(0.01, 0.40), (1.00, 0.90),
(0.05, 0.05, 0.05),
(0.00, 0.00, 0.00),
0.03,
10.00,
0.50
),
("vampire_enchantment_sparks_mace", psf_always_emit|psf_billboard_2d|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_snow_fall_1",
13, 4.10, -0.03, 0.001, 0.001, 0.001,
(0.10, 0.80), (1.00, 0.00),
(0.00, 0.70), (1.00, 255.00),
(0.00, 0.70), (1.00, 255.00),
(0.00, 0.90), (1.00, 255.00),
(0.10, 0.10), (1.00, 0.15),
(0.17, 0.17, 0.17),
(0.00, 0.00, 0.00),
0.200,
50.00,
0.50
),

    ("explosion_1_cloud", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_rotation|psf_randomize_size, "prt_mesh_smoke_1",
     50, 5, 12, -0.6, 2, 2, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 0.75), (1, 0),          #alpha keys
     (0.0, 0.7), (1, 0.5),      #red keys
     (0.0, 0.7),(1, 0.5),      #green keys
     (0.0, 0.7), (1, 0.5),     #blue keys
     (0, 1.5),   (0.2, 12),        #scale keys
     (0.01, 0.01, 0.01),                 #emit box size
     (0, 0, 2.2),               #emit velocity
     0.1,                        #emit dir randomness
    ),

("portal1", psf_billboard_3d|psf_randomize_size|psf_2d_turbulance, "portal1",
1, 1, 10, 0, 7, 7,
(0.30, 1), (1, 0.30),
(3, 1), (5, 1),
(3, 1), (5, 1),
(3, 1), (5, 1),
(1, 0.3), (5, 4),
(1, 1, 0.20),
(0, 0, -10),
2,
0,
0
),
("portal2", psf_billboard_3d|psf_randomize_size|psf_2d_turbulance, "portal2",
1, 1, 10, 0, 7, 7,
(0.30, 1), (1, 0.30),
(3, 1), (5, 1),
(3, 1), (5, 1),
(3, 1), (5, 1),
(1, 0.3), (5, 4),
(1, 1, 0.20),
(0, 0, -10),
2,
0,
0
),
("portal3", psf_billboard_3d|psf_randomize_size|psf_2d_turbulance, "portal3",
1, 1, 10, 0, 7, 7,
(0.30, 1), (1, 0.30),
(3, 1), (5, 1),
(3, 1), (5, 1),
(3, 1), (5, 1),
(1, 0.3), (5, 4),
(1, 1, 0.20),
(0, 0, -10),
2,
0,
0
),
("portal4", psf_billboard_3d|psf_randomize_size|psf_2d_turbulance, "portal4",
1, 1, 10, 0, 7, 7,
(0.30, 1), (1, 0.30),
(3, 1), (5, 1),
(3, 1), (5, 1),
(3, 1), (5, 1),
(1, 0.3), (5, 4),
(1, 1, 0.20),
(0, 0, -10),
2,
0,
0
),
("portal5", psf_billboard_3d|psf_randomize_size|psf_2d_turbulance, "portal5",
1, 1, 10, 0, 7, 7,
(0.30, 1), (1, 0.30),
(3, 1), (5, 1),
(3, 1), (5, 1),
(3, 1), (5, 1),
(1, 0.3), (5, 4),
(1, 1, 0.20),
(0, 0, -10),
2,
0,
0
),
("teleport", psf_billboard_2d|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size|psf_2d_turbulance, "prt_mesh_dust_10",
1, 0.50, 10, 0.05, 10, 39,
(0.30, 1), (1, 0.30),
(0, 0), (0, 0),
(0, 0), (0, 0),
(1, 0.3), (5, 4),
(0.50, 3), (1, 3.70),
(0.20, 0.40, 0.10),
(0, 0, 1),
2,
0,
0
),

("iceexplode1", psf_billboard_3d|psf_randomize_size|psf_2d_turbulance, "iceexplode1",
1, 1, 10, 0, 7, 7,
(0.30, 1), (1, 0.0),
(3, 1), (5, 1),
(3, 1), (5, 1),
(3, 1), (5, 1),
(1, 0.3), (5, 4),
(1, 1, 0.20),
(0, 0, -10),
2,
0,
0
),
("iceexplode2", psf_billboard_3d|psf_randomize_size|psf_2d_turbulance, "iceexplode2",
1, 1, 10, 0, 7, 7,
(0.30, 1), (1, 0.0),
(3, 1), (5, 1),
(3, 1), (5, 1),
(3, 1), (5, 1),
(1, 0.3), (5, 4),
(1, 1, 0.20),
(0, 0, -10),
2,
0,
0
),
("iceexplode3", psf_billboard_3d|psf_randomize_size|psf_2d_turbulance, "iceexplode3",
1, 1, 10, 0, 7, 7,
(0.30, 1), (1, 0.0),
(3, 1), (5, 1),
(3, 1), (5, 1),
(3, 1), (5, 1),
(1, 0.3), (5, 4),
(1, 1, 0.20),
(0, 0, -10),
2,
0,
0
),
("iceexplode4", psf_billboard_3d|psf_randomize_size|psf_2d_turbulance, "iceexplode4",
1, 1, 10, 0, 7, 7,
(0.30, 1), (1, 0.0),
(3, 1), (5, 1),
(3, 1), (5, 1),
(3, 1), (5, 1),
(1, 0.3), (5, 4),
(1, 1, 0.20),
(0, 0, -10),
2,
0,
0
),
("iceexplode5", psf_billboard_3d|psf_randomize_size|psf_2d_turbulance, "iceexplode5",
1, 1, 10, 0, 7, 7,
(0.30, 1), (1, 0.0),
(3, 1), (5, 1),
(3, 1), (5, 1),
(3, 1), (5, 1),
(1, 0.3), (5, 4),
(1, 1, 0.20),
(0, 0, -10),
2,
0,
0
),
("iceexplode6", psf_billboard_3d|psf_randomize_size|psf_2d_turbulance, "iceexplode6",
1, 1, 10, 0, 7, 7,
(0.30, 1), (1, 0.0),
(3, 1), (5, 1),
(3, 1), (5, 1),
(3, 1), (5, 1),
(1, 0.3), (5, 4),
(1, 1, 0.20),
(0, 0, -10),
2,
0,
0
),
("iceexplode", psf_billboard_2d|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size|psf_2d_turbulance, "prt_mesh_dust_10",
1, 0.50, 10, 0.05, 10, 39,
(0.30, 1), (1, 0.0),
(1, 1), (1, 1),
(1, 1), (1, 1),
(1, 1), (1, 1),
(0.50, 3), (1, 3.70),
(0.20, 0.40, 0.10),
(0, 0, 1),
2,
0,
0
),

("earthexplode1", psf_billboard_3d|psf_randomize_size|psf_2d_turbulance, "earthexplode1",
1, 1, 10, 0, 7, 7,
(0.30, 1), (1, 0.0),
(3, 1), (5, 1),
(3, 1), (5, 1),
(3, 1), (5, 1),
(1, 0.3), (5, 4),
(1, 1, 0.20),
(0, 0, -10),
2,
0,
0
),
("earthexplode2", psf_billboard_3d|psf_randomize_size|psf_2d_turbulance, "earthexplode2",
1, 1, 10, 0, 7, 7,
(0.30, 1), (1, 0.0),
(3, 1), (5, 1),
(3, 1), (5, 1),
(3, 1), (5, 1),
(1, 0.3), (5, 4),
(1, 1, 0.20),
(0, 0, -10),
2,
0,
0
),
("earthexplode3", psf_billboard_3d|psf_randomize_size|psf_2d_turbulance, "earthexplode3",
1, 1, 10, 0, 7, 7,
(0.30, 1), (1, 0.0),
(3, 1), (5, 1),
(3, 1), (5, 1),
(3, 1), (5, 1),
(1, 0.3), (5, 4),
(1, 1, 0.20),
(0, 0, -10),
2,
0,
0
),
("earthexplode4", psf_billboard_3d|psf_randomize_size|psf_2d_turbulance, "earthexplode4",
1, 1, 10, 0, 7, 7,
(0.30, 1), (1, 0.0),
(3, 1), (5, 1),
(3, 1), (5, 1),
(3, 1), (5, 1),
(1, 0.3), (5, 4),
(1, 1, 0.20),
(0, 0, -10),
2,
0,
0
),
("earthexplode5", psf_billboard_3d|psf_randomize_size|psf_2d_turbulance, "earthexplode5",
1, 1, 10, 0, 7, 7,
(0.30, 1), (1, 0.0),
(3, 1), (5, 1),
(3, 1), (5, 1),
(3, 1), (5, 1),
(1, 0.3), (5, 4),
(1, 1, 0.20),
(0, 0, -10),
2,
0,
0
),
("earthexplode6", psf_billboard_3d|psf_randomize_size|psf_2d_turbulance, "earthexplode6",
1, 1, 10, 0, 7, 7,
(0.30, 1), (1, 0.0),
(3, 1), (5, 1),
(3, 1), (5, 1),
(3, 1), (5, 1),
(1, 0.3), (5, 4),
(1, 1, 0.20),
(0, 0, -10),
2,
0,
0
),
("mentalstrike", psf_billboard_2d|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size|psf_2d_turbulance, "prt_mesh_dust_10",
1, 0.50, 10, 0.05, 10, 39,
(0.30, 1), (1, 0.0),
(0.50, 0.70), (1, 0.30),
(0.50, 1), (1, 0.90),
(0.50, 0.70), (1, 0.30),
(0.50, 3), (1, 3.70),
(0.20, 0.40, 0.10),
(0, 0, 1),
2,
0,
0
),
("arcanerift1", psf_billboard_3d|psf_randomize_size|psf_2d_turbulance, "arcanerift1",
1, 1, 10, 0, 7, 7,
(0.30, 1), (1, 0.0),
(3, 1), (5, 1),
(3, 1), (5, 1),
(3, 1), (5, 1),
(1, 0.3), (5, 4),
(1, 1, 0.20),
(0, 0, -10),
2,
0,
0
),
("arcanerift2", psf_billboard_3d|psf_randomize_size|psf_2d_turbulance, "arcanerift2",
1, 1, 10, 0, 7, 7,
(0.30, 1), (1, 0.0),
(3, 1), (5, 1),
(3, 1), (5, 1),
(3, 1), (5, 1),
(1, 0.3), (5, 4),
(1, 1, 0.20),
(0, 0, -10),
2,
0,
0
),
("arcanerift3", psf_billboard_3d|psf_randomize_size|psf_2d_turbulance, "arcanerift3",
1, 1, 10, 0, 7, 7,
(0.30, 1), (1, 0.0),
(3, 1), (5, 1),
(3, 1), (5, 1),
(3, 1), (5, 1),
(1, 0.3), (5, 4),
(1, 1, 0.20),
(0, 0, -10),
2,
0,
0
),

("yellow_aura", psf_always_emit|psf_global_emit_dir|psf_billboard_3d|psf_randomize_size, "yellow_aura",
1, 1, 10, 0, 7, 7,
(0.30, 1), (1, 0.0),
(3, 1), (5, 1),
(3, 1), (5, 1),
(3, 1), (5, 1),
(0, 5), (1, 1),
(1, 1, 0.20),
(0, 0, -10),
2,
0,
0
),
("black_aura", psf_always_emit|psf_global_emit_dir|psf_billboard_3d|psf_randomize_size, "black_aura",
1, 1, 10, 0, 7, 7,
(0.30, 1), (1, 0.0),
(3, 1), (5, 1),
(3, 1), (5, 1),
(3, 1), (5, 1),
(0, 5), (1, 1),
(1, 1, 0.20),
(0, 0, -10),
2,
0,
0
),
("green_strike", psf_always_emit|psf_global_emit_dir|psf_billboard_3d|psf_randomize_size, "green_strike",
1, 1, 10, 0, 7, 7,
(0.30, 1), (1, 0.0),
(3, 1), (5, 1),
(3, 1), (5, 1),
(3, 1), (5, 1),
(0, 5), (1, 1),
(1, 1, 0.20),
(0, 0, -10),
2,
0,
0
),
("blood_strike", psf_always_emit|psf_global_emit_dir|psf_billboard_3d|psf_randomize_size, "blood_strike",
1, 1, 10, 0, 7, 7,
(0.30, 1), (1, 0.0),
(3, 1), (5, 1),
(3, 1), (5, 1),
(3, 1), (5, 1),
(0, 5), (1, 1),
(1, 1, 0.20),
(0, 0, -10),
2,
0,
0
),
("mana_strike", psf_billboard_3d|psf_2d_turbulance, "mana_strike",
1, 0.40, 0, 0, 0, 0,
(0.30, 1), (1, 0.0),
(3, 1), (5, 1),
(3, 1), (5, 1),
(3, 1), (5, 1),
(1, 0.3), (5, 4),
(0, 0, 0),
(0, 0, 0),
0,
0,
0
),
("green_strike_massive", psf_billboard_3d|psf_randomize_size|psf_2d_turbulance, "green_strike_massive",
1, 1, 10, 0, 7, 7,
(0.30, 1), (1, 0.0),
(3, 1), (5, 1),
(3, 1), (5, 1),
(3, 1), (5, 1),
(1, 0.3), (5, 4),
(1, 1, 0.20),
(0, 0, -10),
2,
0,
0
),

("blood_strike_massive", psf_billboard_3d|psf_randomize_size|psf_2d_turbulance, "blood_strike_massive",
1, 1, 10, 0, 7, 7,
(0.30, 1), (1, 0.0),
(3, 1), (5, 1),
(3, 1), (5, 1),
(3, 1), (5, 1),
(1, 0.3), (5, 4),
(1, 1, 0.20),
(0, 0, -10),
2,
0,
0
),

("mana_strike_massive", psf_billboard_3d|psf_randomize_size|psf_2d_turbulance, "mana_strike_massive",
1, 1, 10, 0, 7, 7,
(0.30, 1), (1, 0.0),
(3, 1), (5, 0),
(3, 1), (5, 1),
(3, 1), (5, 1),
(1, 0.3), (5, 4),
(1, 1, 0.20),
(0, 0, -10),
2,
0,
0
),

("fireexplode1", psf_billboard_3d|psf_randomize_size|psf_2d_turbulance, "fireexplode1",
1, 1, 10, 0, 7, 7,
(0.30, 1), (1, 0.0),
(3, 1), (5, 1),
(3, 1), (5, 1),
(3, 1), (5, 1),
(1, 0.3), (5, 4),
(1, 1, 0.20),
(0, 0, -10),
2,
0,
0
),
("fireexplode2", psf_billboard_3d|psf_randomize_size|psf_2d_turbulance, "fireexplode2",
1, 1, 10, 0, 7, 7,
(0.30, 1), (1, 0.0),
(3, 1), (5, 1),
(3, 1), (5, 1),
(3, 1), (5, 1),
(1, 0.3), (5, 4),
(1, 1, 0.20),
(0, 0, -10),
2,
0,
0
),
("fireexplode3", psf_billboard_3d|psf_randomize_size|psf_2d_turbulance, "fireexplode3",
1, 1, 10, 0, 7, 7,
(0.30, 1), (1, 0.0),
(3, 1), (5, 1),
(3, 1), (5, 1),
(3, 1), (5, 1),
(1, 0.3), (5, 4),
(1, 1, 0.20),
(0, 0, -10),
2,
0,
0
),
("fireexplode4", psf_billboard_3d|psf_randomize_size|psf_2d_turbulance, "fireexplode4",
1, 1, 10, 0, 7, 7,
(0.30, 1), (1, 0.0),
(3, 1), (5, 1),
(3, 1), (5, 1),
(3, 1), (5, 1),
(1, 0.3), (5, 4),
(1, 1, 0.20),
(0, 0, -10),
2,
0,
0
),
("fireexplode5", psf_billboard_3d|psf_randomize_size|psf_2d_turbulance, "fireexplode5",
1, 1, 10, 0, 7, 7,
(0.30, 1), (1, 0.0),
(3, 1), (5, 1),
(3, 1), (5, 1),
(3, 1), (5, 1),
(1, 0.3), (5, 4),
(1, 1, 0.20),
(0, 0, -10),
2,
0,
0
),
("fireexplode6", psf_billboard_3d|psf_randomize_size|psf_2d_turbulance, "fireexplode6",
1, 1, 10, 0, 7, 7,
(0.30, 1), (1, 0.0),
(3, 1), (5, 1),
(3, 1), (5, 1),
(3, 1), (5, 1),
(1, 0.3), (5, 4),
(1, 1, 0.20),
(0, 0, -10),
2,
0,
0
),
("fireexplode", psf_always_emit|psf_global_emit_dir|psf_billboard_2d|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "fireexplode6",
1, 0.50, 10, 0.05, 10, 39,
(0.30, 1), (1, 0.0),
(0.50, 1), (1, 0.90),
(0.50, 0.70), (1, 0.30),
(0.50, 0.20), (1, 0),
(0.50, 3), (1, 3.70),
(0.20, 0.40, 0.10),
(0, 0, 1),
2,
0,
0
),

     ("mana_tempest", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation|psf_2d_turbulance, "arcanerift1",#prt_mesh_dust_1prt_mesh_fire_1
     5, 2,  10, 0.05, 7, 7, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.3, 1), (1, 0.3),        #alpha keys
     (3.0, 1), (5, 1),      #red keys
     (3.0, 1), (5, 1),       #green keys
     (3.0, 1), (5, 1),      #blue keys
     (0.0, 0.1),(3, 5),  #scale keys
     (10.0, 4.0, 3.0),           #emit box size
     (0, 0, -10),               #emit velocity
     0.5,                       #emit dir randomness
     130,                       #rotation speed
     0.5                        #rotation damping
    ),  

("gold_beam_medium", psf_always_emit|psf_global_emit_dir|psf_billboard_3d, "prt_spellsphere",
1, 1, 0, 0, 0, 0,
(0.5, 0.10), (1, 0),
(0, 1.0), (1, 1.0),
(0, 0.73), (1, 0.658),
(0, 0), (1, 0),
(0, 6.0), (1, 8.0),
(0, 0, 0),
(0, 0, 0),
0,
100,
0.5
),

("light_beam_medium", psf_billboard_3d, "prt_spellsphere",
5, 1, 0, 0, 0, 0,
(0.5, 0.20), (1, 0),
(0, 0.992), (1, 0.992),
(0, 0.87), (1, 0.73),
(0, 0.407), (1, 0.407),
(0, 2.0), (1, 8.0),
(0, 0, 0),
(0, 0, 0),
0,
100,
0.5
),

("bironas_timewarp_oncaster_1", psf_billboard_3d, "prt_spellsphere",
1, 2, 0, 0, 0, 0,
(0.5, 0.10), (1, 0),
(0, 1.0), (1, 0),
(0, 0.92), (1, 0.72),
(0, 0.60), (1, 0.60),
(0.1, 4.0), (1, 40),
(0.2, 0.2, 0.2),
(0, 0, 0),
0,
0,
0
),

("bironas_timewarp_buff", psf_always_emit|psf_global_emit_dir|psf_billboard_3d, "prt_buff_13",
2, 0.8, 0, 0, 0, 0,
(0.2, 0.50), (1, 0.0),
(0, 1.0), (1, 1.0),
(0, 0.92), (1, 0.80),
(0, 0.60), (1, 0.60),
(0.1, 0.40), (1, 3.0),
(0, 0, 0.0),
(0, 0, 0.0),
0,
0,
0.0
),
("bironas_timewarp_buff_burst", psf_always_emit|psf_global_emit_dir|psf_billboard_3d, "prt_clock",
1, 1.5, 0, 0, 0, 0,
(0.1, 1.0), (1, 0.0),
(0, 1.0), (1, 1.0),
(0, 0.92), (1, 0.80),
(0, 0.60), (1, 0.60),
(0.1, 0.90), (1, 2.0),
(0, 0, 0.0),
(0, 0, 0.0),
0,
0,
0.0
),

("wind_of_death", psf_billboard_3d, "prt_spellsphere",
1, 0.6, 0, 0, 0, 0,
(0.1, 0.30), (1, 0),
(0, 1.0), (1, 1.0),
(0, 0), (1, 0),
(0, 0), (1, 0),
(0, 1.0), (1, 80),
(0, 0, 0),
(0, 0, 0),
0,
0,
0
),

("banishment_onimpact", psf_global_emit_dir|psf_billboard_2d, "prt_spellpyramid",
1, 1.8, 0, 0, 0, 0,
(0.1, 0.80), (1, 0),
(0, 1.0), (1, 1.0),
(0, 0.92), (1, 0.80),
(0, 0.60), (1, 0.60),
(0, 9.0), (1, 10),
(0, 0, 0),
(0, 0, 0),
0,
0,
0
),

("arcanebanishment_onimpact_1", psf_global_emit_dir|psf_billboard_2d, "prt_spellpyramid",
1, 1.8, 0, 0, 0, 0,
(0.1, 0.80), (1, 0.0),
(0, 1.0), (1, 1.0),
(0, 0.92), (1, 0.80),
(0, 0.60), (1, 0.60),
(0, 9.0), (1, 10.0),
(0, 0, 0.0),
(0, 0, 0.0),
0,
0,
0.0
),
("arcanebanishment_onimpact_2", psf_global_emit_dir|psf_billboard_2d, "prt_spellpyramid",
1, 1.8, 0, 0, 0, 0,
(0.1, 0.80), (1, 0.0),
(0, 1.0), (1, 1.0),
(0, 0.92), (1, 0.80),
(0, 0.60), (1, 0.60),
(0, 9.0), (1, 10.0),
(0, 0, 0.0),
(0, 0, 0.0),
0,
0,
0.0
),

("banishment", psf_billboard_3d, "prt_spellsphere",
1, 0.6, 0, 0, 0, 0,
(0.1, 0.30), (1, 0),
(0, 1.0), (1, 1.0),
(0, 0.80), (1, 0.76),
(0, 0), (1, 0),
(0, 1.0), (1, 80),
(0, 0, 0),
(0, 0, 0),
0,
0,
0
),
("banishment_onagent_lightning", psf_always_emit|psf_global_emit_dir|psf_billboard_2d|psf_randomize_rotation, "prt_sparks_mesh_1",
1, 0.8, 0, 0, 0, 0,
(0.5, 0.10), (1, 0.70),
(0, 1.0), (1, 1.0),
(0, 0.92), (1, 0.80),
(0, 0.60), (1, 0.60),
(0, 1.0), (1, 1.0),
(0.3, 0.3, 0.3),
(0, 0, 0),
0,
0,
0
),
("banishment_onimpact_sparkles", psf_always_emit|psf_global_emit_dir|psf_billboard_3d|psf_randomize_rotation, "prt_Halo_a",
100, 0.6, 0, 0.7, 50, 40,
(0.5, 1.0), (1, 0),
(0, 1.0), (1, 1.0),
(0, 0.92), (1, 0.90),
(0, 0.60), (1, 0.60),
(0.1, 2.0), (1, 2.0),
(0, 0, 0),
(0.2, 0.2, 0.2),
100,
0,
0
),

("net_of_amyntok", psf_always_emit, "propspell_netofamyntok",
1, 2., 0, 0.1, 0, 0,
(0, 1.0), (1, 0.0),
(0, 1.0), (1, 0.862),
(0, 1.0), (1, 0.607),
(0, 1.0), (1, 0.035),
(0.1, 3.50), (0.5, 1.70),
(0, 0, 0.0),
(0, 0, 0.0),
0,
0,
0.0
),

("phas_protection_oncaster", psf_always_emit|psf_turn_to_velocity, "prt_phasprotection",
100, 3., 0.2, 0, 0, 0,
(0, 1.0), (1, 0.0),
(0, 1.0), (1, 1.0),
(0, 1.0), (1, 1.0),
(0, 1.0), (1, 1.0),
(0, 2.0), (1, 6.0),
(0, 0, 0),
(5, 0, 0),
0,
0,
0
),

("tempest_oncaster", psf_always_emit|psf_turn_to_velocity, "prt_phasprotection",
100, 3., 0.2, 0, 0, 0,
(0, 1.0), (1, 0),
(0, 1.0), (1, 1.0),
(0, 1.0), (1, 1.0),
(0, 1.0), (1, 1.0),
(0, 2.0), (1, 6.0),
(0, 0, 0),
(5., 0, 0),
0,
0,
0
),

("poison_icon", psf_always_emit|psf_global_emit_dir|psf_billboard_3d, "prt_poison",
1, 1, 0, 0, 0, 0,
(0.1, 0.90), (1, 0),
(0, 0), (1, 0),
(0, 0.90), (1, 0.90),
(0, 0.10), (1, 0.10),
(0.1, 1.50), (1, 2.0),
(1, 1, 1.0),
(0, 0, 0),
0,
0,
0
),

("beastmen_icon", psf_always_emit|psf_global_emit_dir|psf_billboard_3d, "prt_beasticon",
1, 1.5, 0, 0, 0, 0,
(0.0, 1.0), (1.0, 0.0),
(0.0, 1.0), (1.0, 1.0),
(0.0, 1.0), (1.0, 1.0),
(0.0, 1.0), (1.0, 1.0),
(0.1, 4.0), (1.0, 4.0),
(1.0, 1.0, 1.0),
(0.0, 0.0, 0.0),
0.0,
0.0,
0.0
),

("harmonic_convergence", psf_always_emit|psf_global_emit_dir, "prt_harmonic",
10, 2.0, 0.0, 0.0, 0.0, 0.0,
(0.2, 0.5), (1.0, 0.0),
(0.0, 0.556), (1.0, 0.556),
(0.0, 0.878), (1.0, 0.878),
(0.0, 0.941), (1.0, 0.941),
(0.0, 6.0), (1.0, 0.1),
(0.0, 0.0, 0.2),
(0.0, 0.0, 0.0),
0.0,
0.0,
0.0
),
("harmonic_grey", psf_always_emit|psf_global_emit_dir, "prt_harmonic",
10, 2.0, 0.0, 0.0, 0.0, 0.0,
(0.2, 0.5), (1.0, 0.0),
(0.0, 0.25), (1.0, 0.25),
(0.0, 0.25), (1.0, 0.25),
(0.0, 0.25), (1.0, 0.25),
(0.0, 6.0), (1.0, 0.1),
(0.0, 0.0, 0.2),
(0.0, 0.0, 0.0),
0.0,
0.0,
0.0
),

("gift_of_the_spider_god_1", psf_always_emit|psf_global_emit_dir|psf_billboard_3d, "prt_poison",
5, 2., 0, 0, 0, 0,
(0.1, 0.80), (1, 0),
(0, 0), (1, 0),
(0, 0.90), (1, 0.90),
(0, 0.10), (1, 0.10),
(0.1, 0.80), (1, 1.20),
(0.3, 0.3, 0.30),
(0, 0, 0),
0,
0,
0
),

("golden_rays", psf_always_emit|psf_global_emit_dir|psf_billboard_2d, "prt_ray_particle",
1, 2., 0, 0, 0, 0,
(0.5, 1.0), (1, 0),
(0, 0.976), (1, 1.0),
(0, 0.749), (1, 0.713),
(0, 0.203), (1, 0.019),
(0.1, 0.30), (1, 0.30),
(0.6, 0.6, 0),
(0, 0, 1.40),
0,
0,
0
),


("transmutation_circle_ray_vertical", psf_always_emit|psf_global_emit_dir|psf_billboard_2d, "prt_ray_particle",
25, 2, 0, 0, 0, 0,
(0.5, 1.0), (1, 0),
(0, 0.976), (1, 1.0),
(0, 0.749), (1, 0.713),
(0, 0.203), (1, 0.019),
(0.1, 3.0), (1, 3.0),
(8, 8, 0),
(0, 0, 7.30),
0,
0,
0
),
("transmutation_circle_ray_vertical_grey", psf_always_emit|psf_global_emit_dir|psf_billboard_2d, "prt_ray_particle",
15, 1, 0, 0, 0, 0,
(0.5, 1.0), (1, 0),
(0, 0.545), (1, 0.69),
(0, 0.537), (1, 0.69),
(0, 0.537), (1, 0.69),
(0.1, 0.25), (1, 0.25),
(0.6, 0.6, 0),
(0, 0, 0.40),
0,
0,
0
),

("green_up_rays", psf_always_emit|psf_global_emit_dir|psf_billboard_2d, "prt_ray_particle",
20, 2, 1.2, -0.5, 0, 0,
(0.5, 0.50), (1, 0),
(0, 0.25), (1, 0.25),
(0, 0.25), (1, 0.25),
(0, 0.25), (1, 0.25),
(0.1, 1.0), (1, 1.0),
(1, 1, 0),
(0, 0, 0),
0,
0,
0
),
("jade_beam_medium", psf_always_emit|psf_global_emit_dir|psf_billboard_2d, "prt_ray_particle",
10, 2, 1.2, -0.5, 0, 0,
(0.5, 0.70), (1, 0),
(0, 0.098), (1, 0.027),
(0, 0.501), (1, 0.69),
(0, 0.239), (1, 0.258),
(0.1, 1.0), (1, 1.0),
(1, 1, -1),
(0, 0, 0),
0,
0,
0
),

("red_up_rays", psf_always_emit|psf_global_emit_dir|psf_billboard_2d, "prt_ray_particle",
20, 2, 1.2, -0.5, 0, 0,
(0.5, 0.50), (1, 0),
(0, 1.0), (1, 1.0),
(0, 0), (1, 0),
(0, 0), (1, 0),
(0.1, 1.0), (1, 1.0),
(1, 1, 0),
(0, 0, 0),
0,
0,
0
),

("sneaky_stabbin", psf_always_emit|psf_global_emit_dir|psf_billboard_3d, "prt_ray3",
10, 1, 0, 0.01, 0, 0,
(0.1, 0.20), (1, 0),
(0, 0), (1, 0.698),
(0, 0.90), (1, 0.941),
(0, 0.10), (1, 0.298),
(0.1, 0.30), (1, 0.90),
(0.8, 0.01, 0.01),
(0, 0, 0),
0,
0,
0
),


    ("propspell_transmutation_circle_lead", psf_billboard_3d|psf_global_emit_dir, "propspell_transmutation_circle_lead",
     1, 5.0, 0.0, 0.0, 0.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 1.0), (1, 1.0),          #alpha keys
     (0.0, 0), (1, 0),      #red keys
     (0.0, 0),(1, 0),       #green keys
     (0.0, 0), (1, 0),      #blue keys
     (0, 1),   (1.0, 1),        #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0, 0, 0),                 #emit velocity
     0.0,                       #emit dir randomness
     0,
     0
    ),

    ("propspell_transmutation_circle_lead", psf_billboard_3d|psf_global_emit_dir, "propspell_transmutation_circle_lead",
     1, 5.0, 0.0, 0.0, 0.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 1.0), (1, 1.0),          #alpha keys
     (0.0, 0), (1, 0),      #red keys
     (0.0, 0),(1, 0),       #green keys
     (0.0, 0), (1, 0),      #blue keys
     (0, 1),   (1.0, 1),        #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0, 0, 0),                 #emit velocity
     0.0,                       #emit dir randomness
     0,
     0
    ),
    ("propspell_transmutation_circle", psf_billboard_3d|psf_global_emit_dir, "propspell_transmutation_circle",
     1, 5.0, 0.0, 0.0, 0.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 1.0), (1, 1.0),          #alpha keys
     (0.0, 0), (1, 0),      #red keys
     (0.0, 0),(1, 0),       #green keys
     (0.0, 0), (1, 0),      #blue keys
     (0, 1),   (1.0, 1),        #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0, 0, 0),                 #emit velocity
     0.0,                       #emit dir randomness
     0,
     0
    ),
    
    
    ("propspell_vinecage", psf_always_emit|psf_billboard_3d|psf_global_emit_dir, "propspell_vinecage",
     10, 1, 120.0, 0.0, 0.0, 0.1,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 1.0), (1, 1.0),          #alpha keys
     (0.0, 0), (1, 0),      #red keys
     (0.0, 0),(1, 0),       #green keys
     (0.0, 0), (1, 0),      #blue keys
     (0, 1),   (1.0, 1),        #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0, 0, 0),                 #emit velocity
     0.0,                       #emit dir randomness
     0,
     0
    ),
    ("propspell_sword3", psf_always_emit|psf_billboard_3d|psf_global_emit_dir, "propspell_sword3",
     10, 1, 120.0, 0.0, 0.0, 0.1,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 1.0), (1, 1.0),          #alpha keys
     (0.0, 0), (1, 0),      #red keys
     (0.0, 0),(1, 0),       #green keys
     (0.0, 0), (1, 0),      #blue keys
     (0, 1),   (1.0, 1),        #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0, 0, 0),                 #emit velocity
     0.0,                       #emit dir randomness
     0,
     0
    ),
    ("propspell_sword2", psf_always_emit|psf_billboard_3d|psf_global_emit_dir, "propspell_sword2",
     10, 1, 120.0, 0.0, 0.0, 0.1,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 1.0), (1, 1.0),          #alpha keys
     (0.0, 0), (1, 0),      #red keys
     (0.0, 0),(1, 0),       #green keys
     (0.0, 0), (1, 0),      #blue keys
     (0, 1),   (1.0, 1),        #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0, 0, 0),                 #emit velocity
     0.0,                       #emit dir randomness
     0,
     0
    ),
    ("propspell_sword1", psf_always_emit|psf_billboard_3d|psf_global_emit_dir, "propspell_sword1",
     10, 1, 120.0, 0.0, 0.0, 0.1,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 1.0), (1, 1.0),          #alpha keys
     (0.0, 0), (1, 0),      #red keys
     (0.0, 0),(1, 0),       #green keys
     (0.0, 0), (1, 0),      #blue keys
     (0, 1),   (1.0, 1),        #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0, 0, 0),                 #emit velocity
     0.0,                       #emit dir randomness
     0,
     0
    ),
    ("propspell_runecage1", psf_always_emit|psf_billboard_3d|psf_global_emit_dir, "propspell_runecage1",
     10, 1, 120.0, 0.0, 0.0, 0.1,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 1.0), (1, 1.0),          #alpha keys
     (0.0, 0), (1, 0),      #red keys
     (0.0, 0),(1, 0),       #green keys
     (0.0, 0), (1, 0),      #blue keys
     (0, 1),   (1.0, 1),        #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0, 0, 0),                 #emit velocity
     0.0,                       #emit dir randomness
     0,
     0
    ),
    
    ("propspell_netofamyntok", psf_always_emit|psf_billboard_3d|psf_global_emit_dir, "propspell_netofamyntok",
     10, 1, 120.0, 0.0, 0.0, 0.1,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 1.0), (1, 1.0),          #alpha keys
     (0.0, 0), (1, 0),      #red keys
     (0.0, 0),(1, 0),       #green keys
     (0.0, 0), (1, 0),      #blue keys
     (0, 1),   (1.0, 1),        #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0, 0, 0),                 #emit velocity
     0.0,                       #emit dir randomness
     0,
     0
    ),
    
    ("propspell_netofslaanesh", psf_always_emit|psf_billboard_3d|psf_global_emit_dir, "propspell_netofamyntok",
     10, 1, 120.0, 0.0, 0.0, 0.1,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 1.0), (1, 1.0),          #alpha keys
     (0.0, 1), (1, 1),      #red keys
     (0.0, 0),(1, 0),       #green keys
     (0.0, 0.45), (1, 0.45),      #blue keys
     (0, 1),   (1.0, 1),        #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0, 0, 0),                 #emit velocity
     0.0,                       #emit dir randomness
     0,
     0
    ),

    ("pvengeful_hood", psf_always_emit|psf_billboard_3d|psf_global_emit_dir, "prt_vengeful_hood",
     10, 1, 120.0, 0.0, 0.0, 0.1,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 1.0), (1, 1.0),          #alpha keys
     (0.0, 0), (1, 0),      #red keys
     (0.0, 0), (1, 0),       #green keys
     (0.0, 0), (1, 0),      #blue keys
     (0, 1),   (1.0, 1),        #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0, 0, 0),                 #emit velocity
     0.0,                       #emit dir randomness
     0,
     0
    ),


    ("magic_circle_1", psf_always_emit|psf_billboard_2d|psf_global_emit_dir|psf_turn_to_velocity, "prt_transmutation_circle_1",
     10, 0.1, 0.0, 0.0, 0.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 0.7), (1.0, 0.7),          #alpha keys
     (0.0, 0.0), (1.0, 0.0),      #red keys
     (0.0, 0.0), (1.0, 0.0),       #green keys
     (0.0, 0.0), (1.0, 0.0),      #blue keys
     (0, 10),    (1.0, 10.0),        #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0.0, 0.0, 0.0),                 #emit velocity
     0.0,                       #emit dir randomness
     0,
     0
    ),

    ("magic_circle_2", psf_always_emit|psf_billboard_2d|psf_global_emit_dir|psf_turn_to_velocity, "prt_transmutation_circle_2",
     10, 0.1, 0.0, 0.0, 100.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 0.7), (1.0, 0.7),          #alpha keys
     (0.0, 0.0), (1.0, 0.0),      #red keys
     (0.0, 0.0), (1.0, 0.0),       #green keys
     (0.0, 0.0), (1.0, 0.0),      #blue keys
     (0, 10),    (1.0, 10.0),        #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0.0, 0.0, 0.0),                 #emit velocity
     0.0,                       #emit dir randomness
     0,
     0
    ),
    ("magic_circle_3", psf_always_emit|psf_billboard_2d|psf_global_emit_dir|psf_turn_to_velocity, "prt_transmutation_circle_3",
     10, 0.1, 0.0, 0.0, 100.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 0.7), (1.0, 0.7),          #alpha keys
     (0.0, 0.0), (1.0, 0.0),      #red keys
     (0.0, 0.0), (1.0, 0.0),       #green keys
     (0.0, 0.0), (1.0, 0.0),      #blue keys
     (0, 10),    (1.0, 10.0),        #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0.0, 0.0, 0.0),                 #emit velocity
     0.0,                       #emit dir randomness
     0,
     0
    ),
    ("magic_circle_4", psf_always_emit|psf_billboard_2d|psf_global_emit_dir|psf_turn_to_velocity, "prt_transmutation_circle_4",
     10, 0.1, 0.0, 0.0, 100.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 0.7), (1.0, 0.7),          #alpha keys
     (0.0, 0.0), (1.0, 0.0),      #red keys
     (0.0, 0.0), (1.0, 0.0),       #green keys
     (0.0, 0.0), (1.0, 0.0),      #blue keys
     (0, 10),    (1.0, 10.0),        #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0.0, 0.0, 0.0),                 #emit velocity
     0.0,                       #emit dir randomness
     0,
     0
    ),

("transmutation_lead", psf_always_emit|psf_global_emit_dir|psf_billboard_3d, "transmutation_lead",
1, 3, 0, 0, 0, 0,
(0.1, 1.0), (2, 0.0),
(0, 1.0), (1, 1.0),
(0, 0.0), (1, 0.0),
(0, 0.0), (1, 0.0),
(0.1, 0.90), (3, 2.0),
(0, 0, 0),
(0, 0, 0),
0,
0,
0
),
("tzeentch_beam_medium", psf_always_emit|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_spellsphere_big",
10, 0.3, 0.1, 0, 0, 0,
(0.5, 1.0), (1.00, 0.0),
(0.0, 0.02), (1.0, 0.02),
(0.0, 0.87), (1.0, 0.87),
(0.0, 0.93), (1.0, 0.93),
(0.0, 1.50), (1.0, 1.80),
(0.3, 0.30, 0.20),
(0.0, 0.0, -2.00),
0.0,
100.0,
0.5
),

("net_of_slaanesh", psf_always_emit, "propspell_netofamyntok",
1, 2., 0, 0.1, 0, 0,
(0.5, 0.8), (1.0, 0.0),
(0.0, 1.0), (1.0, 1.0),
(0.0, 0.0), (1.0, 0.0),
(0.0, 0.45), (1.0, 0.45),
(0.1, 3.50), (0.5, 1.70),
(0, 0, 0.0),
(0, 0, 0.0),
0,
0,
0.0
),

("massive_fire_pink", psf_always_emit|psf_global_emit_dir|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_fire_1",
50, 2.0, 0.0, -1.3, 10.0, 0.0,
(0.5, 0.5), (1.0, 0.0),
(0.0, 1.0), (1.0, 1.0),
(0.0, 0.2), (1.0, 0.2),
(0.0, 0.6), (1.0, 0.6),
(0.0, 6.0), (1.0, 15.),
(3.0, 3.0, 0.2),
(0.0, 0.0, 0.4),
0.1,
250.0,
0.5
),

("dummy_stone_boss", psf_randomize_rotation|psf_randomize_size, "prt_mesh_stone_1",
70, 0.1, 2, 0.9, 100, 2,
(0.1, 1), (1, 1),
(0.1, 0.6), (1, 0.6),
(0.1, 0.5), (1, 0.5),
(0.1, 0.4), (1, 0.4),
(0, 0.3), (1, 0.3),
(2.8, 2.8, 1),
(0, 0, 0),
2.3,
200,
0
),
("dummy_smoke_boss", psf_billboard_3d|psf_randomize_size, "prt_mesh_dust_1",
50, 0.1, 15, -0.05, 100, 0.2,
(0.1, 0.5), (1, 0),
(0.1, 0.3), (1, 0.3),
(0.1, 0.2), (1, 0.2),
(0.1, 0.1), (1, 0.2),
(0, 0.7), (1, 2.2),
(2.8, 2.8, 1),
(0, 0, 0.05),
2,
10,
0.1
),

]
# modmerger_start version=201 type=2
try:
    component_name = "particle_systems"
    var_set = { "particle_systems" : particle_systems }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
