define odxny = Character("odxny")

default in_call = False 

image bg odxny_bg = "bg_video.jpg"
image fg odxny_fg = "grain_filter.png"
image fade_lower = "gui/fade.png"

image o1_neutral: 
    "body1_eyes_neutral.png"
    choice:
        pause 10
    choice:
        pause 6
    choice:
        pause 4
    choice:
        pause 1
    choice:
        pause 0.5
    "body1_eyes_blink.png"
    choice:
        pause 0.2
    choice:
        pause 0.1
    repeat
image o1_side: 
    "body1_eyes_side.png"
    choice:
        pause 10
    choice:
        pause 6
    choice:
        pause 4
    choice:
        pause 1
    choice:
        pause 0.5
    "body1_eyes_blink.png"
    choice:
        pause 0.2
    choice:
        pause 0.1
    repeat

image o1_done: 
    "body1_eyes_done.png"
    choice:
        pause 10
    choice:
        pause 6
    choice:
        pause 4
    choice:
        pause 1
    choice:
        pause 0.5
    "body1_eyes_blink.png"
    choice:
        pause 0.2
    choice:
        pause 0.1
    repeat

image o1_mad: 
    "body1_eyes_mad.png"
    choice:
        pause 10
    choice:
        pause 6
    choice:
        pause 4
    choice:
        pause 1
    choice:
        pause 0.5
    "body1_eyes_blink.png"
    choice:
        pause 0.2
    choice:
        pause 0.1
    repeat

image o1_happy: 
    "body1_eyes_smiling.png"
    choice:
        pause 10
    choice:
        pause 6
    choice:
        pause 4
    choice:
        pause 1
    choice:
        pause 0.5
    "body1_eyes_blink.png"
    choice:
        pause 0.2
    choice:
        pause 0.1
    repeat

layeredimage spr odxny_1: 
    always "body1.png" 

    group eyes:
        attribute open default:
            "o1_neutral"
        attribute sweat:
            "o1_side"
        attribute closed:
            "body1_eyes_blink.png"
        attribute done: 
            "o1_done" 
        attribute mad: 
            "o1_mad" 
        attribute happy: 
            "o1_smiling"
    
    group mouth: 
        attribute frown: 
            "body1_mouth_frown.png"
        attribute smile: 
            "body1_mouth_smiling.png" 
        attribute smile_open: 
            "body1_mouth_grin.png" 
        attribute smile_open_big: 
            "body1_mouth_grin_open.png" 
        attribute neutral default: 
            "body1_mouth_neutral.png"
        attribute neutral_open: 
            "body1_mouth_neutral_open.png" 
        

image o2_sad: 
    "body2_eyes_sad.png"
    choice:
        pause 10
    choice:
        pause 6
    choice:
        pause 4
    choice:
        pause 1
    choice:
        pause 0.5
    "body2_eyes_blink.png"
    choice:
        pause 0.2
    choice:
        pause 0.1
    repeat

image o2_upset: 
    "body2_eyes_upset.png"
    choice:
        pause 10
    choice:
        pause 6
    choice:
        pause 4
    choice:
        pause 1
    choice:
        pause 0.5
    "body2_eyes_blink.png"
    choice:
        pause 0.2
    choice:
        pause 0.1
    repeat

image o2_side: 
    "body2_eyes_side.png"
    choice:
        pause 10
    choice:
        pause 6
    choice:
        pause 4
    choice:
        pause 1
    choice:
        pause 0.5
    "body2_eyes_blink.png"
    choice:
        pause 0.2
    choice:
        pause 0.1
    repeat

layeredimage spr odxny_2: 
    always "body2.png" 

    group eyes:
        attribute sad:
            "o2_sad"
        attribute upset:
            "o2_upset"
        attribute side default:
            "o2_side"
        attribute closed:
            "body2_eyes_blink.png"
        
    group mouth: 
        attribute frown default: 
            "body2_mouth_frown.png"
        attribute frown_open: 
            "body2_mouth_frown_open.png"
        attribute scowl: 
            "body2_mouth_scowl.png" 
        attribute scowl_open: 
            "body2_mouth_scowl_open.png" 


image o3_neutral: 
    "body3_eyes_neutral.png"
    choice:
        pause 10
    choice:
        pause 6
    choice:
        pause 4
    choice:
        pause 1
    choice:
        pause 0.5
    "body3_eyes_neutral_blink.png"
    choice:
        pause 0.2
    choice:
        pause 0.1
    repeat

image o3_shocked: 
    "body3_eyes_shocked.png"
    choice:
        pause 10
    choice:
        pause 6
    choice:
        pause 4
    choice:
        pause 1
    choice:
        pause 0.5
    "body3_eyes_shocked_blink.png"
    choice:
        pause 0.2
    choice:
        pause 0.1
    repeat

image o3_silly: 
    "body3_eyes_silly.png"
    choice:
        pause 10
    choice:
        pause 6
    choice:
        pause 4
    choice:
        pause 1
    choice:
        pause 0.5
    "body3_eyes_silly_blink.png"
    choice:
        pause 0.2
    choice:
        pause 0.1
    repeat

layeredimage spr odxny_3: 
    always "body3.png" 

    group eyes:
        attribute open default:
            "o3_neutral"
        attribute closed:
            "body3_eyes_neutral_blink.png"
        attribute shocked:
            "o3_shocked"
        attribute silly:
            "o3_silly"
    
    group mouth: 
        attribute neutral default: 
            "body3_mouth_neutral.png"
        attribute neutral_open: 
            "body3_mouth_neutral_open.png"
        attribute parted: 
            "body3_mouth_parted.png" 

image money_rain = Fixed(SnowBlossom("images/temp/dollar.png", 1000, xspeed=(-500, 500), yspeed=(300, 500), start=10))
        