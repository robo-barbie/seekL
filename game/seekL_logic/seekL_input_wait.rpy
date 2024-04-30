
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

label wait_start:
    if first_flash:
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
                    