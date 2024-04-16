define o = Character("odxny", callback=speaker("odxny"))

default in_call = False 

#########################################################
###### IMAGES ###########################################
image bg odxny_bg = "bg_video.jpg"
image fg odxny_fg = "grain_filter.png"
image fade_lower = "gui/fade.png"
image cg platonic = "cg_platonic.jpg"
image cg romantic = "cg_romantic.jpg"


########################################################
#### ODXNY SPIRITE EXPRESSIONS #########################

##### BODY 1 #################

image o1 neutral = LiveComposite(
    (0.5, 1.0),
    (0, 0), "body1.png", #body image
    (0, 0), "o1 eyes neutral", #eye animation
    (0, 0), WhileSpeaking("odxny", "o1 mouth neutral", "body1_mouth_neutral.png"), #(character, mouth animation, mouth image when not speaking)
    )

image o1 eyes closed = LiveComposite(
    (0.5, 1.0),
    (0, 0), "body1.png", #body image
    (0, 0), "o1 eyes closed", #eye animation
    (0, 0), WhileSpeaking("odxny", "o1 mouth neutral", "body1_mouth_neutral.png"), #(character, mouth animation, mouth image when not speaking)
    )

image o1 side neutral = LiveComposite(
    (0.5, 1.0),
    (0, 0), "body1.png", #body image
    (0, 0), "o1 eyes side", #eye animation
    (0, 0), WhileSpeaking("odxny", "o1 mouth neutral", "body1_mouth_neutral.png"), #(character, mouth animation, mouth image when not speaking)
    )

image o1 side frown = LiveComposite(
    (0.5, 1.0),
    (0, 0), "body1.png", #body image
    (0, 0), "o1 eyes side", #eye animation
    (0, 0), WhileSpeaking("odxny", "o1 mouth frown", "body1_mouth_frown.png"), #(character, mouth animation, mouth image when not speaking)
    )

image o1 happy = LiveComposite(
    (0.5, 1.0),
    (0, 0), "body1.png", #body image
    (0, 0), "o1 eyes happy", #eye animation
    (0, 0), WhileSpeaking("odxny", "o1 mouth smile", "body1_mouth_smiling.png"), #(character, mouth animation, mouth image when not speaking)
    )

image o1 closed eye happy = LiveComposite(
    (0.5, 1.0),
    (0, 0), "body1.png", #body image
    (0, 0), "o1 eyes closed", #eye animation
    (0, 0), WhileSpeaking("odxny", "o1 mouth smile", "body1_mouth_smiling.png"), #(character, mouth animation, mouth image when not speaking)
    )

image o1 happy grin = LiveComposite(
    (0.5, 1.0),
    (0, 0), "body1.png", #body image
    (0, 0), "o1 eyes happy", #eye animation
    (0, 0), WhileSpeaking("odxny", "o1 mouth grin", "body1_mouth_grin.png"), #(character, mouth animation, mouth image when not speaking)
    )

image o1 closed eye grin = LiveComposite(
    (0.5, 1.0),
    (0, 0), "body1.png", #body image
    (0, 0), "o1 eyes closed", #eye animation
    (0, 0), WhileSpeaking("odxny", "o1 mouth grin", "body1_mouth_grin.png"), #(character, mouth animation, mouth image when not speaking)
    )

image o1 grin = LiveComposite(
    (0.5, 1.0),
    (0, 0), "body1.png", #body image
    (0, 0), "o1 eyes neutral", #eye animation
    (0, 0), WhileSpeaking("odxny", "o1 mouth grin", "body1_mouth_grin.png"), #(character, mouth animation, mouth image when not speaking)
    )

image o1 side smile = LiveComposite(
    (0.5, 1.0),
    (0, 0), "body1.png", #body image
    (0, 0), "o1 eyes side", #eye animation
    (0, 0), WhileSpeaking("odxny", "o1 mouth happy", "body1_mouth_smiling.png"), #(character, mouth animation, mouth image when not speaking)
    )

image o1 done frown = LiveComposite(
    (0.5, 1.0),
    (0, 0), "body1.png", #body image
    (0, 0), "o1 eyes done", #eye animation
    (0, 0), WhileSpeaking("odxny", "o1 mouth frown", "body1_mouth_frown.png"), #(character, mouth animation, mouth image when not speaking)
    )

image o1 done = LiveComposite(
    (0.5, 1.0),
    (0, 0), "body1.png", #body image
    (0, 0), "o1 eyes done", #eye animation
    (0, 0), WhileSpeaking("odxny", "o1 mouth neutral", "body1_mouth_neutral.png"), #(character, mouth animation, mouth image when not speaking)
    )



image o1 mad = LiveComposite(
    (0.5, 1.0),
    (0, 0), "body1.png", #body image
    (0, 0), "o1 eyes mad", #eye animation
    (0, 0), WhileSpeaking("odxny", "o1 mouth frown", "body1_mouth_frown.png"), #(character, mouth animation, mouth image when not speaking)
    )

####### BODY 2 ####################

image o2 sad = LiveComposite(
    (0.5, 1.0),
    (0, 0), "body2.png", #body image
    (0, 0), "o2 eyes sad", #eye animation
    (0, 0), WhileSpeaking("odxny", "o2 mouth frown", "body2_mouth_frown.png"), #(character, mouth animation, mouth image when not speaking)
    )

image o2 scowl = LiveComposite(
    (0.5, 1.0),
    (0, 0), "body2.png", #body image
    (0, 0), "o2 eyes upset", #eye animation
    (0, 0), WhileSpeaking("odxny", "o2 mouth scowl", "body2_mouth_scowl.png"), #(character, mouth animation, mouth image when not speaking)
    )

image o2 side frown = LiveComposite(
    (0.5, 1.0),
    (0, 0), "body2.png", #body image
    (0, 0), "o2 eyes side", #eye animation
    (0, 0), WhileSpeaking("odxny", "o2 mouth frown", "body2_mouth_frown.png"), #(character, mouth animation, mouth image when not speaking)
    )

image o2 side scowl = LiveComposite(
    (0.5, 1.0),
    (0, 0), "body2.png", #body image
    (0, 0), "o2 eyes side", #eye animation
    (0, 0), WhileSpeaking("odxny", "o2 mouth scowl", "body2_mouth_scowl.png"), #(character, mouth animation, mouth image when not speaking)
    )

###### BODY 3 #####################

image o3 shocked = LiveComposite(
    (0.5, 1.0),
    (0, 0), "body3.png", #body image
    (0, 0), "o3 eyes shocked", #eye animation
    (0, 0), WhileSpeaking("odxny", "o3 mouth parted", "body3_mouth_parted.png"), #(character, mouth animation, mouth image when not speaking)
    )

image o3 neutral = LiveComposite(
    (0.5, 1.0),
    (0, 0), "body3.png", #body image
    (0, 0), "o3 eyes neutral", #eye animation
    (0, 0), WhileSpeaking("odxny", "o3 mouth neutral", "body3_mouth_neutral.png"), #(character, mouth animation, mouth image when not speaking)
    )

image o3 eyes closed = LiveComposite(
    (0.5, 1.0),
    (0, 0), "body3.png", #body image
    (0, 0), "o3 eyes closed", #eye animation
    (0, 0), WhileSpeaking("odxny", "o3 mouth neutral", "body3_mouth_neutral.png"), #(character, mouth animation, mouth image when not speaking)
    )

image o3 silly = LiveComposite(
    (0.5, 1.0),
    (0, 0), "body3.png", #body image
    (0, 0), "o3 eyes silly", #eye animation
    (0, 0), WhileSpeaking("odxny", "o3 mouth parted", "body3_mouth_parted.png"), #(character, mouth animation, mouth image when not speaking)
    )

image o3 neutral parted = LiveComposite(
    (0.5, 1.0),
    (0, 0), "body3.png", #body image
    (0, 0), "o3 eyes neutral", #eye animation
    (0, 0), WhileSpeaking("odxny", "o3 mouth parted", "body3_mouth_parted.png"), #(character, mouth animation, mouth image when not speaking)
    )






##################################################################
### EYES #########################################################

## BODY 1 ############

image o1 eyes closed = "body1_eyes_blink.png"

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

image o1 eyes side: 
    "body1_eyes_side.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "body1_eyes_blink.png"
    0.1
    repeat

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

image o1 eyes happy: 
    "body1_eyes_smiling.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "body1_eyes_blink.png"
    0.1
    repeat


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

image o3 eyes closed = "body3_eyes_neutral_blink.png"

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
    .2
    "body1_mouth_neutral_open.png"
    .2
    repeat

image o1 mouth smile:
    "body1_mouth_smiling.png"
    .2
    "body1_mouth_neutral_open.png"
    .2
    repeat

image o1 mouth grin:
    "body1_mouth_grin.png"
    .2
    "body1_mouth_grin_open.png"
    .2
    repeat

image o1 mouth frown:
    "body1_mouth_frown.png"
    .2
    "body1_mouth_neutral_open.png"
    .2
    repeat

####### BODY 2 ####################

image o2 mouth frown:
    "body2_mouth_frown.png"
    .2
    "body2_mouth_frown_open.png"
    .2
    repeat

image o2 mouth scowl:
    "body2_mouth_scowl.png"
    .2
    "body2_mouth_scowl_open.png"
    .2
    repeat

##### BODY 3 ########################

image o3 mouth neutral:
    "body3_mouth_neutral.png"
    .2
    "body3_mouth_neutral_open.png"
    .2
    repeat

image o3 mouth parted:
    "body3_mouth_parted.png"
    .2
    "body3_mouth_neutral_open.png"
    .2
    repeat






image money_rain = Fixed(SnowBlossom("images/temp/dollar.png", 1000, xspeed=(-500, 500), yspeed=(300, 500), start=10))
        


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
        