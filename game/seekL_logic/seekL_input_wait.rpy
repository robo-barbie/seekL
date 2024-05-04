
default required_runs = {
    "columns":None, 
    "tables":None, 
    "idx":None
}

default player_can_pass = False
default player_is_waiting = False
default waiting_label = ""
default tables_active = []
default look_at_idx = {}
default next_day_number= "1"

label wait_start:
    if first_flash and not player_can_pass:
        pause 0.5 
        play sound "audio/sfx/message_notification_01_001 tutorial.ogg"
        show highlight_large onlayer screens: 
            pos highlight_frame_console_pos
        $ first_flash = False 
    
    # wait for input 
    $ player_is_waiting = True 
    $ _preferences.afm_enable = False 

    # if they arrive already ready to pass 
    if player_can_pass:
        $ player_is_waiting = False 
        jump wait_end
    $ renpy.pause(hard=True)

label wait_end: 
    hide highlight_large onlayer screens 
    $ first_flash = True 
    $ player_is_waiting = False 
    $ _preferences.afm_enable = True 
    $ renpy.jump(waiting_label)

init python:
    def player_input_confirm(ta=None, cols=None, idx=None): 
        global player_input_confirm_label_jump
        global player_can_pass
        global player_is_waiting 
        global waiting_label 
        global tables_active 
        global look_at_idx
        tables_active = ta 
        look_at_idx = idx 

        player_proceed = 0

        if required_runs["columns"]: 
            for c in required_runs["columns"]: 
                if c.lower() not in [x.lower() for x in cols]: 
                    player_proceed +=1
        
        if required_runs["tables"]: 
            for t in required_runs["tables"]: 
                if t.lower() not in [x.lower() for x in ta]:
                    player_proceed +=1

        if required_runs["idx"]: 
            for i in required_runs["idx"]:
                if i[0].lower() not in idx.keys(): 
                    player_proceed +=1
                elif i[1].lower() not in [x.lower() for x in idx[i[0]]]: 
                    player_proceed +=1
        
        if player_proceed > 0: 
            player_can_pass = False 
        else: 
            player_can_pass = True 
            if player_is_waiting: 
                renpy.jump("wait_end")
        #return(player_proceed)
                    
## OTHER WAITING / CHANGE THINGS 
label day_swap: 
    ## END CALL + CLICK TO CONTINUE ## 
    pause 1 
    play sound "audio/sfx/ui_menu_back_001 hangup.ogg"
    stop music fadeout 1.0
    show black_bg
    $ _preferences.afm_enable = False 
    pause  
    pause 0.5
    hide black_bg
    # jump day2_start

    ## GLITCH EFFECT ## 
    $ quick_menu = False
    #$show day2_glitch 
    $ renpy.show("day"+next_day_number+"_glitch")
    pause
    play sound "audio/sfx/ui_start_game_002 day swap.ogg"
    #show chat2_glitch 
    $ renpy.show("chat"+next_day_number+"_glitch")
    pause 0.5
    $ quick_menu = True

    ## SETUP AND START THE CHAT ## 
    $ chat_location = "DAY " + next_day_number + " - CHAT"
    $ reset_chats(in_day = True) 
    $ seekL_text_send = "" 
    $ seekL_output = []
    show screen seekL_ui 
    #hide day2_glitch 
    $ renpy.hide("day"+next_day_number+"_glitch")
    #hide chat2_glitch 
    $ renpy.hide("chat"+next_day_number+"_glitch")
    $ in_call = False
    hide screen black_window 
    $ _preferences.afm_enable = True 

    ## JUMP TO DAY LABEL ## 
    $ renpy.jump("day"+next_day_number+"_start")
    $ renpy.pause(hard=True)

label go_to_call: 
    $ _preferences.afm_enable = False 
    pause 2 
    show screen video_call_window
    $ renpy.pause(hard=True)

label go_to_call2: 
    $ in_call = True 
    $ chat_location = "DAY " +next_day_number+ " - CALL"

    show bg odxny_bg
    show spr o1 neutral 
    show fade_lower
    show fg odxny_fg onlayer screens
    show call_frame
    hide screen seekL_ui 

    show screen black_window with Dissolve(0.01) zorder 2 
    hide screen video_call_window with Pixellate(0.2, 5)
    hide screen black_window with Dissolve(0.3)

    camera:
        subpixel True pos (0,0) zoom 1.0
    with dissolve

    $ _preferences.afm_enable = True 

    $ renpy.jump("day"+next_day_number+"_call")
    $ renpy.pause(hard=True)