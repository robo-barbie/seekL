

default in_call = False 
default points_seekLoss = 0 
default points_seekLife = 0 
default points_seekLove = 0 

# default persistent.seekLoss = False 
# default persistent.FBIBanner = True 

# default persistent.seekLife = False 

# default persistent.seekLove = False 

## emotes 
image e_serious = "images/emote_serious.jpg"
image e_pain = "images/emote_pain.png"
image e_sparkle = "images/emote_sparkle.png"
image e_wink = "images/emote_wink.png"
image e_baby = "images/emote_baby.png"
image e_crying = "images/emote_crying.png"
image e_heart = "images/emote_heart.png" 
image e_letsgo = "images/emote_letsgo.png" 
image e_orz = "images/emote_orz.png"


#########################################################
###### IMAGES ###########################################
# image bg odxny_bg:
#     "bg_video1.jpg"
#     3.0
#     "bg_video2.jpg"
#     0.3
#     "bg_video3.jpg"
#     3.0
#     "bg_video1.jpg"
#     0.5
#     "bg_video2.jpg"
#     repeat

# router 
image bg_odxny_3: 
    "bg_video3a.png" # slightly on 
    choice: 
        0.2
    choice: 
        0.5 
    choice: 
        0.1
    choice: 
        0.3 
    "bg_video3b.png" # off mode (quick) 
    choice: 
        0.1
    choice: 
        0.2
    choice: 
        0.05
    "bg_video3c.png" # full on 
    choice: 
        2.0
    choice: 
        6.0
    choice: 
        3.0
    choice: 
        8.0
    repeat 

# big server column 
# just rotates steadily through all modes
image bg_odxny_2: 
    ease 0.1 alpha 0.0 
    "bg_video2a.png"  
    ease 0.1 alpha 1.0 
    choice: 
        8.0
    choice: 
        10.0 
    ease 0.1 alpha 0.0 
    "bg_video2b.png" 
    ease 0.1 alpha 1.0 
    choice: 
        8.0
    choice: 
        10.0 
    ease 0.1 alpha 0.0 
    "bg_video2c.png" 
    ease 0.1 alpha 1.0 
    choice: 
        8.0
    choice: 
        10.0 
    repeat 

# small top right object (i call it the odxbox)
# flashes more randomly from mode to mode 
image bg_odxny_1: 
    ease 0.5 alpha 0.0 
    "bg_video1a.png"
    ease 0.5 alpha 1.0 
    choice: 
        0.2
    choice: 
        1.0 
    choice: 
        5.0 
    choice: 
        9.0 
    ease 0.5 alpha 0.0 
    "bg_video1b.png" 
    ease 0.5 alpha 1.0 
    choice: 
        0.1
    choice: 
        2.0
    choice: 
        7.0 
    choice: 
        10.0 
    ease 0.5 alpha 0.0 
    "bg_video1c.png" 
    ease 0.5 alpha 1.0 
    choice: 
        0.5
    choice: 
        1.5
    choice: 
        3.0
    choice: 
        8.0
    repeat  


layeredimage bg odxny_bg: 

    always "bg_video1.jpg" 
    always "bg_odxny_1"
    always "bg_odxny_2"
    always "bg_odxny_3" 



image fg odxny_fg = "grain_filter.png"
image fade_lower = "gui/fade.png"
image call_frame = "call_frame.png"

image cg platonic = "cg_platonic.jpg"
image cg romantic = "cg_romantic.jpg"
image cg bad = "cg_bad.png"

image cg platonic_zoom: 
    "cg platonic"
    zoom 0.5 
image cg romantic_zoom: 
    "cg romantic"
    zoom 0.5 

image chatscreen_bg = "images/chat_screenbg.jpg" 

image video_call_popup:
    "videocall_window3.png"
    1.0
    "videocall_window2.png"
    1.0
    "videocall_window1.png"
    repeat

screen video_call_window:
    on "show" action Play("music", "audio/music/call_incoming_002_-_seekL.ogg")
    on "hide" action Stop("music")
    zorder 3
    modal True 
    add "#00000077"
    add "video_call_popup" at game_menu_popup_video 
    button: 
        area (867, 683, 80, 72)
        action Jump("go_to_call2")

screen phonecall_window_real:
    on "show" action Play("music", "audio/music/call_outgoing_002_-_seekL.ogg")
    on "hide" action Stop("music")
    zorder 3
    modal True 
    add "#00000077"
    add "phonecall_window.png" at game_menu_popup_video 

    timer 4.0 action [Jump("day5_seekLove_call")]
    # button: 
    #     area (908, 678, 82, 82)
    #     action Jump("go_to_call2")

screen black_window: 
    add "#000000"
    
    

########################################################
#### ODXNY SPIRITE EXPRESSIONS #########################

##### BODY 1 #################

image spr o1 neutral = LiveComposite(
    (1.0, 1.0),
    (0, 0), "body1.png", #body image
    (0, 0), "o1 eyes neutral", #eye animation
    (0, 0), WhileSpeaking("odxny", "o1 mouth neutral", "body1_mouth_neutral.png"), #(character, mouth animation, mouth image when not speaking)
    )

image spr o1 eyes closed = LiveComposite(
    (1.0, 1.0),
    (0, 0), "body1.png", #body image
    (0, 0), "o1 eyes blink", #eye animation
    (0, 0), WhileSpeaking("odxny", "o1 mouth neutral", "body1_mouth_neutral.png"), #(character, mouth animation, mouth image when not speaking)
    )

image spr o1 side neutral = LiveComposite(
    (1.0, 1.0),
    (0, 0), "body1.png", #body image
    (0, 0), "o1 eyes side", #eye animation
    (0, 0), WhileSpeaking("odxny", "o1 mouth neutral", "body1_mouth_neutral.png"), #(character, mouth animation, mouth image when not speaking)
    )

image spr o1 frown = LiveComposite(
    (1.0, 1.0),
    (0, 0), "body1.png", #body image
    (0, 0), "o1 eyes neutral", #eye animation
    (0, 0), WhileSpeaking("odxny", "o1 mouth frown", "body1_mouth_frown.png"), #(character, mouth animation, mouth image when not speaking)
    )

image spr o1 closed eye frown = LiveComposite(
    (1.0, 1.0),
    (0, 0), "body1.png", #body image
    (0, 0), "o1 eyes blink", #eye animation
    (0, 0), WhileSpeaking("odxny", "o1 mouth frown", "body1_mouth_frown.png"), #(character, mouth animation, mouth image when not speaking)
    )

image spr o1 side frown = LiveComposite(
    (1.0, 1.0),
    (0, 0), "body1.png", #body image
    (0, 0), "o1 eyes side", #eye animation
    (0, 0), WhileSpeaking("odxny", "o1 mouth frown", "body1_mouth_frown.png"), #(character, mouth animation, mouth image when not speaking)
    )

image spr o1 smile = LiveComposite(
    (1.0, 1.0),
    (0, 0), "body1.png", #body image
    (0, 0), "o1 eyes neutral", #eye animation
    (0, 0), WhileSpeaking("odxny", "o1 mouth smile", "body1_mouth_smiling.png"), #(character, mouth animation, mouth image when not speaking)
    )

image spr o1 happy = LiveComposite(
    (1.0, 1.0),
    (0, 0), "body1.png", #body image
    (0, 0), "o1 eyes happy", #eye animation
    (0, 0), WhileSpeaking("odxny", "o1 mouth smile", "body1_mouth_smiling.png"), #(character, mouth animation, mouth image when not speaking)
    )

image spr o1 closed eye happy = LiveComposite(
    (1.0, 1.0),
    (0, 0), "body1.png", #body image
    (0, 0), "o1 eyes blink", #eye animation
    (0, 0), WhileSpeaking("odxny", "o1 mouth smile", "body1_mouth_smiling.png"), #(character, mouth animation, mouth image when not speaking)
    )

image spr o1 happy grin = LiveComposite(
    (1.0, 1.0),
    (0, 0), "body1.png", #body image
    (0, 0), "o1 eyes happy", #eye animation
    (0, 0), WhileSpeaking("odxny", "o1 mouth grin", "body1_mouth_grin.png"), #(character, mouth animation, mouth image when not speaking)
    )

image spr o1 closed eye grin = LiveComposite(
    (1.0, 1.0),
    (0, 0), "body1.png", #body image
    (0, 0), "o1 eyes blink", #eye animation
    (0, 0), WhileSpeaking("odxny", "o1 mouth grin", "body1_mouth_grin.png"), #(character, mouth animation, mouth image when not speaking)
    )

image spr o1 grin = LiveComposite(
    (1.0, 1.0),
    (0, 0), "body1.png", #body image
    (0, 0), "o1 eyes neutral", #eye animation
    (0, 0), WhileSpeaking("odxny", "o1 mouth grin", "body1_mouth_grin.png"), #(character, mouth animation, mouth image when not speaking)
    )

image spr o1 side smile = LiveComposite(
    (1.0, 1.0),
    (0, 0), "body1.png", #body image
    (0, 0), "o1 eyes side", #eye animation
    (0, 0), WhileSpeaking("odxny", "o1 mouth grin", "body1_mouth_smiling.png"), #(character, mouth animation, mouth image when not speaking)
    )

image spr o1 done frown = LiveComposite(
    (1.0, 1.0),
    (0, 0), "body1.png", #body image
    (0, 0), "o1 eyes done", #eye animation
    (0, 0), WhileSpeaking("odxny", "o1 mouth frown", "body1_mouth_frown.png"), #(character, mouth animation, mouth image when not speaking)
    )

image spr o1 done = LiveComposite(
    (1.0, 1.0),
    (0, 0), "body1.png", #body image
    (0, 0), "o1 eyes done", #eye animation
    (0, 0), WhileSpeaking("odxny", "o1 mouth neutral", "body1_mouth_neutral.png"), #(character, mouth animation, mouth image when not speaking)
    )


image spr o1 mad = LiveComposite(
    (1.0, 1.0),
    (0, 0), "body1.png", #body image
    (0, 0), "o1 eyes mad", #eye animation
    (0, 0), WhileSpeaking("odxny", "o1 mouth frown", "body1_mouth_frown.png"), #(character, mouth animation, mouth image when not speaking)
    )

image spr o1 side nervous = LiveComposite(
    (1.0, 1.0),
    (0, 0), "body1.png", #body image
    (0, 0), "o1 eyes nervous", #eye animation
    (0, 0), WhileSpeaking("odxny", "o1 mouth neutral", "body1_mouth_neutral.png"), #(character, mouth animation, mouth image when not speaking)
    )


####### BODY 2 ####################

image spr o2 sad = LiveComposite(
    (1.0, 1.0),
    (0, 0), "body2.png", #body image
    (0, 0), "o2 eyes sad", #eye animation
    (0, 0), WhileSpeaking("odxny", "o2 mouth frown", "body2_mouth_frown.png"), #(character, mouth animation, mouth image when not speaking)
    )

image spr o2 upset = LiveComposite(
    (1.0, 1.0),
    (0, 0), "body2.png", #body image
    (0, 0), "o2 eyes upset", #eye animation
    (0, 0), WhileSpeaking("odxny", "o2 mouth frown", "body2_mouth_frown.png"), #(character, mouth animation, mouth image when not speaking)
    )

image spr o2 scowl = LiveComposite(
    (1.0, 1.0),
    (0, 0), "body2.png", #body image
    (0, 0), "o2 eyes upset", #eye animation
    (0, 0), WhileSpeaking("odxny", "o2 mouth scowl", "body2_mouth_scowl.png"), #(character, mouth animation, mouth image when not speaking)
    )

image spr o2 side frown = LiveComposite(
    (1.0, 1.0),
    (0, 0), "body2.png", #body image
    (0, 0), "o2 eyes side", #eye animation
    (0, 0), WhileSpeaking("odxny", "o2 mouth frown", "body2_mouth_frown.png"), #(character, mouth animation, mouth image when not speaking)
    )

image spr o2 side scowl = LiveComposite(
    (1.0, 1.0),
    (0, 0), "body2.png", #body image
    (0, 0), "o2 eyes side", #eye animation
    (0, 0), WhileSpeaking("odxny", "o2 mouth scowl", "body2_mouth_scowl.png"), #(character, mouth animation, mouth image when not speaking)
    )

###### BODY 3 #####################

image spr o3 shocked = LiveComposite(
    (1.0, 1.0),
    (0, 0), "body3.png", #body image
    (0, 0), "o3 eyes shocked", #eye animation
    (0, 0), WhileSpeaking("odxny", "o3 mouth parted", "body3_mouth_parted.png"), #(character, mouth animation, mouth image when not speaking)
    )

image spr o3 neutral = LiveComposite(
    (1.0, 1.0),
    (0, 0), "body3.png", #body image
    (0, 0), "o3 eyes neutral", #eye animation
    (0, 0), WhileSpeaking("odxny", "o3 mouth neutral", "body3_mouth_neutral.png"), #(character, mouth animation, mouth image when not speaking)
    )

image spr o3 eyes closed = LiveComposite(
    (1.0, 1.0),
    (0, 0), "body3.png", #body image
    (0, 0), "o3 eyes blink", #eye animation
    (0, 0), WhileSpeaking("odxny", "o3 mouth neutral", "body3_mouth_neutral.png"), #(character, mouth animation, mouth image when not speaking)
    )

image spr o3 silly = LiveComposite(
    (1.0, 1.0),
    (0, 0), "body3.png", #body image
    (0, 0), "o3 eyes silly", #eye animation
    (0, 0), WhileSpeaking("odxny", "o3 mouth parted", "body3_mouth_parted.png"), #(character, mouth animation, mouth image when not speaking)
    )

image spr o3 neutral parted = LiveComposite(
    (1.0, 1.0),
    (0, 0), "body3.png", #body image
    (0, 0), "o3 eyes neutral", #eye animation
    (0, 0), WhileSpeaking("odxny", "o3 mouth parted", "body3_mouth_parted.png"), #(character, mouth animation, mouth image when not speaking)
    )






##################################################################
### EYES #########################################################

## BODY 1 ############

image o1 eyes blink = "body1_eyes_blink.png"

image o1 eyes neutral: 
    "body1_eyes_neutral.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "body1_eyes_blink.png"
    0.1
    repeat

image o1 eyes side = "body1_eyes_side.png"

image o1 eyes nervous = "body1_eyes_side_sweat.png"


image o1 eyes done: 
    "body1_eyes_done.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
        pause 0.5
    "body1_eyes_blink.png"
    0.1
    repeat

image o1 eyes mad: 
    "body1_eyes_mad.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "body1_eyes_blink.png"
    0.1
    repeat

image o1 eyes happy = "body1_eyes_smiling.png"
   


#### BODY 2 ####################

image o2 eyes sad: 
    "body2_eyes_sad.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "body2_eyes_blink.png"
    0.1
    repeat

image o2 eyes upset: 
    "body2_eyes_upset.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "body2_eyes_blink.png"
    0.1
    repeat

image o2 eyes side: 
    "body2_eyes_side.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "body2_eyes_blink.png"
    0.1
    repeat


##### BODY 3 EYES ##############

image o3 eyes blink = "body3_eyes_neutral_blink.png"

image o3 eyes neutral: 
    "body3_eyes_neutral.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "body3_eyes_neutral_blink.png"
    0.1
    repeat

image o3 eyes shocked: 
    "body3_eyes_shocked.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "body3_eyes_shocked_blink.png"
    0.1
    repeat

image o3 eyes silly: 
    "body3_eyes_silly.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "body3_eyes_silly_blink.png"
    0.1
    repeat

############################################################################
###### MOUTHS ##############################################################

##### BODY 1 ###################

image o1 mouth neutral:
    "body1_mouth_neutral.png"
    .1
    "body1_mouth_neutral_open.png"
    .1
    repeat

image o1 mouth smile:
    "body1_mouth_smiling.png"
    .1
    "body1_mouth_neutral_open.png"
    .1
    repeat

image o1 mouth grin:
    "body1_mouth_grin.png"
    .1
    "body1_mouth_grin_open.png"
    .1
    repeat

image o1 mouth frown:
    "body1_mouth_frown.png"
    .1
    "body1_mouth_neutral_open.png"
    .1
    repeat

####### BODY 2 ####################

image o2 mouth frown:
    "body2_mouth_frown.png"
    .1
    "body2_mouth_frown_open.png"
    .1
    repeat

image o2 mouth scowl:
    "body2_mouth_scowl.png"
    .1
    "body2_mouth_scowl_open.png"
    .1
    repeat

##### BODY 3 ########################

image o3 mouth neutral:
    "body3_mouth_neutral.png"
    .1
    "body3_mouth_neutral_open.png"
    .1
    repeat

image o3 mouth parted:
    "body3_mouth_parted.png"
    .1
    "body3_mouth_neutral_open.png"
    .1
    repeat






image money_rain = Fixed(SnowBlossom("images/temp/dollar.png", 200, xspeed=(-500, 500), yspeed=(100, 300), start=10))
        


#layeredimage spr odxny_1: 
    #always "body1.png" 

    #group eyes:
        #attribute open default:
            #"o1_neutral"
        #attribute sweat:
            #"o1_side"
        #attribute closed:
            #"body1_eyes_blink.png"
        #attribute done: 
            #"o1_done" 
        #attribute mad: 
            #"o1_mad" 
        #attribute happy: 
            #"o1_smiling"
    
    #group mouth: 
        #attribute frown: 
            #"body1_mouth_frown.png"
        #attribute smile: 
            #"body1_mouth_smiling.png" 
        #attribute smile_open: 
            #"body1_mouth_grin.png" 
        #attribute smile_open_big: 
            #"body1_mouth_grin_open.png" 
        #attribute neutral default: 
            #"body1_mouth_neutral.png"
        #attribute neutral_open: 
            #"body1_mouth_neutral_open.png" 

#layeredimage spr odxny_2: 
    #always "body2.png" 

    #group eyes:
        #attribute sad:
            #"o2_sad"
        #attribute upset:
            #"o2_upset"
        #attribute side default:
            #"o2_side"
        #attribute closed:
            #"body2_eyes_blink.png"
        
    #group mouth: 
        #attribute frown default: 
            #"body2_mouth_frown.png"
        #attribute frown_open: 
            #"body2_mouth_frown_open.png"
        #attribute scowl: 
            #"body2_mouth_scowl.png" 
        #attribute scowl_open: 
            #"body2_mouth_scowl_open.png" 

    #layeredimage spr odxny_3: 
    #always "body3.png" 

    #group eyes:
        #attribute open default:
            #"o3_neutral"
        #attribute closed:
            #"body3_eyes_neutral_blink.png"
        #attribute shocked:
            #"o3_shocked"
        #attribute silly:
            #"o3_silly"
    
    #group mouth: 
        #attribute neutral default: 
            #"body3_mouth_neutral.png"
        #attribute neutral_open: 
            #"body3_mouth_neutral_open.png"
        #attribute parted: 
            #"body3_mouth_parted.png" 
        