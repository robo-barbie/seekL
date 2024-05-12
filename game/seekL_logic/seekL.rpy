
init python: 
    seekL_button_color = "#48cb3a"
    seekL_button_color_inactive = "#4154cc"
    seekL_button_color_unclicked = "#3c6837"
    seekL_button_color_execute = "#4154cc"
    seekL_button_color_clear = "#eb7c7c"
    seekL_window_size = 550
    seekL_sidebar_size = 330
    seekL_height = 950
    seekL_height_half = 475
    seekL_button_height = 50 

    seekL_chat_text_size = 20
    seekL_choice_window_height = 200

    xadjValue_sl = float("inf")
    xadj_sl = ui.adjustment()
    xadj_sl.value = float("inf")

    seekL_cmd_color = "#28a9ff"
    #seekL_cmd_color = "#28a9ff"

    def run_history(hist): 
        global seekL_text_send 
        global seekL_window_active 
        #"{color=945050}{size=20}UNSUCCESSFUL{/size}\n"+t_og+"{/color}"
        hist = hist.replace("{color=945050}{size=20}UNSUCCESSFUL{/size}{/color}\n", "")
        #hist = hist.replace("{/color}", "")
        seekL_text_send = hist
        seekL_window_active = 1



    # this is annoying and i'm not doing it rn LOL 
    # there's a single character lag that is fucking stuff up for syntax styling 
    def change_seekl_text_shown(v=""): 
        #renpy.pause(0.01)
        global seekL_text_send
        global seekL_text_send_previous
        global seekL_text_show 
        # why am i doing this letter by letter 
        # just read the hwole thing in SILLY 

        #seekL_text_send = v
        value = seekL_text_send

        seekL_text_show = value.lower()

        if "select " in value.lower():
            seekL_text_show = seekL_text_show.replace("select ", "{color=28a9ff}select{/color} ")
        if " from " in value.lower(): 
            seekL_text_show = seekL_text_show.replace(" from ", " {color=28a9ff}from{/color} ")
        if " join " in value.lower(): 
            seekL_text_show = seekL_text_show.replace(" join ", " {color=28a9ff}join{/color} ")
        if " where " in value.lower(): 
            seekL_text_show = seekL_text_show.replace(" where ", " {color=28a9ff}where{/color} ")
        if " on " in value.lower(): 
            seekL_text_show = seekL_text_show.replace(" where ", " {color=28a9ff}on{/color} ")

default rulebook = [
        """{font=HELLO.ttf.ttf}{size=25}1. SELECT
Use this to select specific columns (comma separated) or all columns at once (*).
    {/size}{/font}""",
        """{font=HELLO.ttf.ttf}{size=25}2. FROM 
Indicate which table you'd like to see. {color=ffffff69}

EX: SELECT * 
    FROM table.example 

EX: SELECT hacker_name, favorite_fruit 
    FROM table.example 
    {/color}{/size}{/font}""", 
    """{font=HELLO.ttf.ttf}{size=25}3. WHERE 
Filter your data down to records you care about. The columns filtered on will always be displayed. 
Can run up to two statements in the where clause, separated by an OR or an AND. 
WHERE must appear at the end of the query. {color=ffffff69}

EX: SELECT * 
    FROM table.example 
    WHERE hacker_name = 'incri'

EX: SELECT hacker_name  
    FROM table.example 
    WHERE number_of_hacks > 15 
        and number_of_hacks < 45 
    {/color}{/size}{/font}""", 
    """{font=HELLO.ttf.ttf}{size=25}4. JOIN 
Join two tables together that share a common column name. The common column will always be displayed.
JOIN must appear after the FROM statement.{color=ffffff69}

EX: SELECT * 
    FROM irs.contacts
    JOIN azgov.marriage  

EX: SELECT * 
    FROM irs.contacts
    JOIN godaddy.secretsmooch_users 
    WHERE full_name = 'bruce johnson'
    {/color}{/size}{/font}""", 

    """{font=HELLO.ttf.ttf}{size=25}5. EXEC
Execute a function with an input. This does not run with any other seekL query.{color=ffffff69}

EX: EXEC out('bruce.johnson@copmail.com')
    {/color}{/size}{/font}""",

    """{font=HELLO.ttf.ttf}{size=25}MORE EXAMPLES {color=ffffff69}

EX: SELECT phone, full_name, badge_no 
    FROM irs.contacts
    JOIN azgov.police_info
    WHERE badge_no = 55242  

EX: SELECT ss_alias, phone  
    FROM irs.contacts
    JOIN godaddy.secretsmooch_users 
    WHERE full_name = 'bruce johnson'
    {/color}{/size}{/font}"""
    ]

default seekL_text_entry = ""
default seekL_text_send = ""
default seekL_text_send_previous = ""
default seekL_text_show = ""
default seekL_text_formatting_open = ""

default t2 = "" 

default seekL_window_active = 1
default seekL_chat_active = 0 
default seekL_help_active = 0 

# these need to be moved out to DEFAULT in order to persist across saves
default tables_seen = []
default hack_notes = []

image new_message_all: 
    "gui/button/allchat_idle.png"
    alpha 1.0 
    pause 0.2 
    "gui/button/allchat_idle.png"
    alpha 0.2 
    pause 0.2 
    repeat 

image new_message_admin: 
    "gui/button/adminchat_idle.png"
    alpha 1.0 
    pause 0.5
    "gui/button/adminchat_idle.png"
    alpha 0.2 
    pause 0.5 
    repeat 

image highlight_large: 
    "images/UI_highlight_large.png" 
    alpha 1.0 
    ease 0.5 alpha 0.2 
    alpha 1.0 
    ease 0.5 alpha 0.0 
    Null() 
image highlight_small:
    "images/UI_highlight_small.png" 
    alpha 1.0 
    ease 1.0 alpha 0.0 
    Null() 

define highlight_tab_table_pos = (1510, 50)
define highlight_tab_info_pos = (1710, 50)
define highlight_frame_console_pos = (850, 50)

default defenses = False 
default defenses_off = False 
default server_kill = False 
image defenses_top: 
    "#000000"
    alpha 0.0 
    ease 0.1 alpha 1.0
    ease 0.3 alpha 0.0 
    Null()  


## good end 
screen secure_dial: 
    # modal True 
    add "#000000d0"
    frame: 
        background "#00000050"
        xalign 0.5 
        yalign 0.5
        xminimum 400 
        vbox: 
            text "enter number":
                size 20
            input default "":
                caret_blink False 
                multiline False 
                copypaste True 
                font "HELLO.ttf.ttf"
                color "#d6fa9d"
                size 24
    # textbutton _("RETURN"):
    #     xalign 0.5 
    #     yalign 0.95
    #     action Hide("secure_dial")

screen seekL_ui: 
    if server_kill: 
        add "images/chat_screenbg_kill.png"
    elif defenses: 
        add "images/chat_screenbg_defense.jpg"
    else: 
        add "images/chat_screenbg.jpg"
    #add "#000000af" # dark tint 
 
    frame: 
        area (40, 52, 896, 62)
        background None 
        hbox: 
            spacing 5
            button: 
                xalign 0.5
                if channels_new_message["all"]: 
                    add "new_message_all"
                    action Play("sound", "audio/sfx/tab_swap.ogg"), SetVariable("current_window", "all"), SetDict(channels_new_message, "all", False), SetVariable("seekL_chat_active", 0)
                elif seekL_chat_active == 0: 
                    add "gui/button/allchat_active.png"
                else: 
                    add "gui/button/allchat_idle.png"
                    action Play("sound", "audio/sfx/tab_swap.ogg"), SetVariable("current_window", "all"), SetDict(channels_new_message, "all", False), SetVariable("seekL_chat_active", 0)
    
            button: 
                xalign 0.5
                if channels_new_message["admin"]: 
                    add "new_message_admin"
                    action Play("sound", "audio/sfx/tab_swap.ogg"), SetVariable("current_window", "admin"), SetDict(channels_new_message, "admin", False), SetVariable("seekL_chat_active", 1)
                elif seekL_chat_active == 1: 
                    add "gui/button/adminchat_active.png"
                else: 
                    add "gui/button/adminchat_idle.png"
                    action Play("sound", "audio/sfx/tab_swap.ogg"), SetVariable("current_window", "admin"), SetDict(channels_new_message, "admin", False), SetVariable("seekL_chat_active", 1)
       
            null width 200
            button: 
                xalign 0.5
                if seekL_chat_active == 2: 
                    add "gui/button/seeklguide_active.png"
                else: 
                    add "gui/button/seeklguide_active.png"
                    action Play("sound", "audio/sfx/tab_swap.ogg"), SetVariable("current_window", "guide"), SetVariable("seekL_chat_active", 2)
  
    # actual chat + guide
    frame: 
        area (53, 143, 856, 700)
        background None 
        vbox:
            viewport  yadjustment yadj: 
                # ysize seekL_height - seekL_choice_window_height
                draggable True
                scrollbars "vertical"
                mousewheel "change"
                yinitial 1.0

                vbox: 
                    box_wrap True
                    spacing 15 
                    null height 10
                    if seekL_chat_active in [0,1]: 
                        for idx, t in enumerate(channels[current_window][-100:]): 
                            vbox: 
                                spacing 5
                                xpos 20
                                ysize None 
                                # has fixed:
                                #     yfit True # only for window 
                                if idx != 0: 
                                    if channels_names[current_window][-100:][idx] == channels_names[current_window][-100:][idx-1] and ((abs(int(channels_times[current_window][-100:][idx][-2:]) - int(channels_times[current_window][-100:][idx-1][-2:])) < 5 and int(channels_times[current_window][-100:][idx][:2].replace(":","")) == int(channels_times[current_window][-100:][idx-1][:2].replace(":",""))) or (abs(int(channels_times[current_window][-100:][idx][-2:]) - int(channels_times[current_window][-100:][idx-1][-2:])) > 55 and int(channels_times[current_window][-100:][idx][:2].replace(":","")) - int(channels_times[current_window][-100:][idx-1][:2].replace(":","") == 1))):
                                        null height 0
                                    else: 
                                        vbox:
                                            null height 30 
                                            if channels_names[current_window][-100:][idx] != "SYSTEM":
                                                hbox:
                                                    yalign 0.5 
                                                    spacing 5
                                                    frame:  
                                                        area(0,0,18,18)
                                                        background Frame(character_colors[channels_names[current_window][-100:][idx]] + "85",0,0,0,0) 
                                                        text channels_names[current_window][-100:][idx][0] size 15 yalign 0.5 xalign 0.5
                                                    text channels_names[current_window][-100:][idx] + "{size=12} " + channels_times[current_window][-100:][idx] + "{/size}": 
                                    
                                                        yalign 0.5 
                                                        size seekL_chat_text_size 
                                                        if channels_names[current_window][-100:][idx] in character_colors: 
                                                            color character_colors[channels_names[current_window][-100:][idx]] + "85"
                                                        else: 
                                                            color "#FFFFFF85"
                                else:   
                                    vbox:
                                        if channels_names[current_window][-100:][idx] != "SYSTEM":
                                            hbox:
                                                yalign 0.5 
                                                spacing 5
                                                frame:  
                                                    area(0,0,18,18)
                                                    background Frame(character_colors[channels_names[current_window][-100:][idx]] + "85",0,0,0,0) 
                                                    text channels_names[current_window][-100:][idx][0] size 15 yalign 0.5 xalign 0.5
                                                text channels_names[current_window][-100:][idx] + "{size=12} " + channels_times[current_window][-100:][idx] + "{/size}": 
                                                    #xanchor 1.0
                                                    #text_align 1.0
                                                    #xpos 130
                                                    #xsize 100
                                                    yalign 0.5 
                                                    size seekL_chat_text_size 
                                                    if channels_names[current_window][-100:][idx] in character_colors: 
                                                        color character_colors[channels_names[current_window][-100:][idx]] + "85"
                                                    else: 
                                                        color "#FFFFFF85"
                                vbox:
                                    if channels_names[current_window][-100:][idx] != "SYSTEM" and "------------------------------" not in t:
                                        text t: 
                                            text_align 0.0
                                            size seekL_chat_text_size 
                                            line_spacing 5 
                                            xmaximum seekL_window_size + seekL_sidebar_size - 100 
                                            if channels_names[current_window][-100:][idx] in character_colors: 
                                                color "#ffffffba"#character_colors[channels_names[current_window][idx]]
                                            else: 
                                                color "#FFFFFF"
                                    elif channels_names[current_window][-100:][idx] != "SYSTEM" and "------------------------------" in t:
                                        vbox:
                                            text t.split("{color=ffb8f3}------------------------------\n{/color}{color="+color_syntax+"}{font=HELLO.ttf.ttf}")[0]: 
                                                text_align 0.0
                                                size seekL_chat_text_size 
                                                xmaximum seekL_window_size + seekL_sidebar_size - 100 
                                                if channels_names[current_window][-100:][idx] in character_colors: 
                                                    color "#ffffffba"#character_colors[channels_names[current_window][idx]]
                                                else: 
                                                    color "#FFFFFF"
                                            text "{color=ffb8f3}------------------------------{/color}"
                                            textbutton t.split("{color=ffb8f3}------------------------------\n{/color}{color="+color_syntax+"}{font=HELLO.ttf.ttf}")[1].replace("{color=ffb8f3}------------------------------\n{/color}{color="+color_syntax+"}{font=HELLO.ttf.ttf}", "").replace("{/font}{/color}\n{color=ffb8f3}------------------------------{/color}", ""): 
                                                text_align 0.0
                                                text_size seekL_chat_text_size 
                                                xmaximum seekL_window_size + seekL_sidebar_size - 100 
                                                text_font "HELLO.ttf.ttf"
                                                text_color color_syntax
                                                action SetVariable("seekL_text_send", t.split("{color=ffb8f3}------------------------------\n{/color}{color="+color_syntax+"}{font=HELLO.ttf.ttf}")[1].replace("{color=ffb8f3}------------------------------\n{/color}{color="+color_syntax+"}{font=HELLO.ttf.ttf}", "").replace("{/font}{/color}\n{color=ffb8f3}------------------------------{/color}", "")), SetVariable("seekL_window_active", 1)
                              
                                            text "{color=ffb8f3}------------------------------{/color}"
                                    else: 
                                        text ">>" + t : 
                                            # text_align 0.5
                                            # xalign 0.5
                                            font "HELLO.ttf.ttf"
                                            size seekL_chat_text_size 
                                            bold True 
                                            xmaximum seekL_window_size + seekL_sidebar_size - 100
                                            color character_colors[channels_names[current_window][-100:][idx]] + "85"
                                        # line_spacing 10
                    elif seekL_chat_active == 2: 
                        for i in range(len(rulebook)): 
                            text rulebook[i]: 
                                xpos 20 
                                xmaximum seekL_window_size + seekL_sidebar_size - 100 
                    null height 10 



        # inputs + data 
    hbox: 
        area (997, 58, 424, 66)
        button: 
            #xalign 0.5
            if seekL_window_active == 1: 
                add "gui/button/console_active.png"
            else: 
                add "gui/button/console_idle.png"
                action Play("sound", "audio/sfx/tab_swap.ogg"), SetVariable("seekL_window_active", 1)
        button: 
            #xalign 0.5
            if seekL_window_active == 0: 
                add "gui/button/historytab_active.png"

            else: 
                add "gui/button/historytab_idle.png"
                action Play("sound", "audio/sfx/tab_swap.ogg"), SetVariable("seekL_window_active", 0)
                                
    frame: 
        area (1000, 142, 480, 292)
        background None
        viewport: 
            #scrollbars "both"
            if seekL_window_active == 0: 
                scrollbars "vertical"
            mousewheel True 
            draggable True 
            ymaximum 250
            #xinitial 1.0 
            if seekL_window_active == 1:
                input default "":
                    caret_blink True 
                    multiline True 
                    copypaste True 
                    xmaximum seekL_window_size-100
                    font "HELLO.ttf.ttf"
                    color "#d6fa9d"
                    size 24
                    #color "#00000000"
                    #size 1
                    #text_size seekL_chat_text_size
                    #changed change_seekl_text_shown
                    value VariableInputValue("seekL_text_send")
            elif seekL_window_active == 0: 
                vbox: 
                    spacing 5
                    xmaximum seekL_window_size-100
                    for i in range(len(previous_commands)): 
                        vbox: 
                            spacing 5
                            textbutton previous_commands[len(previous_commands)-(i+1)]:
                                background "#FFFFFF20"
                                xfill True 
                                text_color "#ffffff69" 
                                text_hover_color gui.hover_color
                                text_font "HELLO.ttf.ttf"
                                text_size 22
                                action Play("sound", "audio/sfx/message_notification_02_003 reload query.ogg"), Function(run_history, previous_commands[len(previous_commands)-(i+1)])

    hbox: 
        #xalign 0.0
        #spacing 5
        area (1490, 58, 200, 66)
        button: 
            xalign 0.5
            if seekL_help_active == 0: 
                add "gui/button/tables_active.png"
            else: 
                add "gui/button/tables_idle.png"
                action Play("sound", "audio/sfx/tab_swap.ogg"), SetVariable("seekL_help_active", 0)
        button: 
            xalign 0.5
            if seekL_help_active == 1: 
                add "gui/button/info_active.png"
            else: 
                add "gui/button/info_idle.png"
                action Play("sound", "audio/sfx/tab_swap.ogg"), SetVariable("seekL_help_active", 1)                   
    if seekL_help_active == 0: 
        frame: 
            area (1534, 142, 298, 282)
            background None
            viewport: 
                scrollbars "vertical"
                #scrollbars "vertical"
                mousewheel True 
                draggable True 
                ymaximum 250
                vbox: 
                    xmaximum seekL_sidebar_size - 70
                    spacing 10 
                    for i in range(len(tables_seen)): 
                        textbutton tables_seen[len(tables_seen)-(i+1)]: 
                            background "#FFFFFF20"
                            xfill True 
                            text_font "HELLO.ttf.ttf"
                            text_color "#ffffff69" 
                            text_size 20
                            text_hover_color gui.hover_color
                            action Play("sound", "audio/sfx/message_notification_02_003 reload query.ogg"), SetVariable("seekL_text_send", "select * \nfrom " + tables_seen[len(tables_seen)-(i+1)]), SetVariable("seekL_window_active", 1)
    elif seekL_help_active == 1: 
        frame: 
            area (1534, 142, 298, 282)
            background None
            #xmaximum seekL_sidebar_size - 20
            viewport: 
                scrollbars "vertical"
                #scrollbars "vertical"
                mousewheel True 
                draggable True 
                ymaximum 250
                vbox: 
                    xmaximum seekL_sidebar_size - 100
                    spacing 10 
                    for i in range(len(hack_notes)): 
                        textbutton hack_notes[len(hack_notes)-(i+1)]:
                            text_font "HELLO.ttf.ttf"
                            text_color "#FFFFFF"
                            text_size 20
    
    
    frame: 
        area (1006, 591, 844, 350)
        #padding(30,30,30,30)
        background None
        viewport: 
            draggable True
            scrollbars "horizontal"
            mousewheel "horizontal"

            hbox: 
                spacing 30
                for o in seekL_output: 
                    text o line_spacing 5 size 24 font "HELLO.ttf.ttf"
            

    if current_window == active_window: 
        text who_is_typing:
            color "#FFFFFF85" 
            size 15 
            #yalign 1.0 
            ypos 840
            #xalign 0.0
            xpos 70

    button: 
        xalign 0.83
        ypos seekL_height_half+17
        if seekL_window_active == 1 and seekL_text_send != "": 
            background None
            text "{font=Teko-VariableFont_wght.ttf}{size=44}EXECUTE" color "#000000"
        else: 
            background None
            text "{font=Teko-VariableFont_wght.ttf}{size=44}EXECUTE" color "#d0ffd1"
        ysize seekL_button_height
            
        if seekL_window_active == 1:
            action Hide("timer_window"),Show("timer_window")#Function(process_seekL, seekL_text_send) 

    button: 
        xalign 0.93
        ypos seekL_height_half+17
        if seekL_window_active == 1 and seekL_text_send != "": 
            background None
            text "{font=Teko-VariableFont_wght.ttf}{size=45}CLEAR"  color "#95ec96"
        else: 
            background None
            text "{font=Teko-VariableFont_wght.ttf}{size=45}CLEAR"  color "#3f3f3f"
        ysize seekL_button_height
        if seekL_window_active == 1:
            action Play("sound", "audio/sfx/query_clear.ogg"), SetVariable("seekL_text_send", "")
            #if seekL_window_active == 1:
                #action Hide("timer_window"),Show("timer_window")#Function(process_seekL, seekL_text_send) 
        #button: 
            #xalign 0.5
            #if seekL_window_active == 1 and seekL_text_send != "": 
                #background seekL_button_color_clear
                #text "clear" bold True
            #else: 
                #background seekL_button_color_inactive
                #text "clear" bold True  color "#b1b1b1"
            #ysize seekL_button_height
            #if seekL_window_active == 1:
                #action Play("sound", "audio/sfx/message_notification_02_006 clear.ogg"), SetVariable("seekL_text_send", "")

    hbox: 
        # ypos 0.0
        # xalign 0.04

        ypos 0.94 
        xalign 0.3
        spacing -20
        button:
            if chat_speed == 2:
                add "gui/button/slow_hover.png"
            else: 
                add "gui/button/slow_idle.png"
                action SetVariable("chat_speed", 2)

        button:
            if chat_speed == 3:
                add "gui/button/normal_active.png"
            else:
                add "gui/button/normal_idle.png"
                action SetVariable("chat_speed", 3)

        button:
            if chat_speed == 8:
                add "gui/button/hyperspeed_active.png"
            else:
                add "gui/button/hyperspeed_idle.png" 
                action SetVariable("chat_speed", 8)

        button:
            if chat_speed == 100:
                add "gui/button/superfast_active.png"
            else:
                add "gui/button/superfast_idle.png" 
                action SetVariable("chat_speed", 100)
    
    if defenses: 
        add "defenses_top" 
    elif defenses_off: 
        add "defenses_top" 

        # hbox:
        #     yalign 1.0 
        #     textbutton "disable autoplay chat": 
        #         if is_paused: 
        #             text_color gui.hover_color
        #         else: 
        #             text_color gui.idle_color
        #         text_size 26
        #         yalign 1.0
        #         action SetVariable("is_paused", True), SetVariable("player_set_pause", True)
        #     if not is_paused: 
        #         textbutton "(click around to restart the chat)":
        #             text_size 20 
        #             yalign 1.0 
        #             text_color gui.idle_color 
        #             action NullAction()
        #     else: 
        #         textbutton "                                    ":
        #             text_size 20 
        #             yalign 1.0 
        #             text_color gui.idle_color 
        #             action NullAction()
        
    # qa hell 
    hbox: 
        spacing 10 
        text str(points_seekLove)
        # text str(is_paused) 
        # text str(player_set_pause) 
        text str(_preferences.afm_enable)
        # text current_window 
        # text active_window 
    #     if tables_active: 
    #         vbox: 
    #             for i in tables_active: 
    #                 text i 
    #         vbox:
    #             for i in look_at_idx: # filtered idx
    #                 text str(i)
    #                 hbox: 
    #                     spacing 10 
    #                     for j in look_at_idx[i]: 
    #                         text str(j)
        # vbox:
        #     for i in j_v_idx: # all avail idx 
        #         text str(i) color "#fcf945"
        # if j_list: 
        #     vbox:
        #         for i in j_list: # filtered value 
        #             text str(i) color "#fc2626"
        # text where_value color "#42e774" # what the value submitted was 
        # text where_place color "#fd93f8" # did we find this column in 1 table or both 
        # vbox:
        #     for i in where_column_list: 
        #         text i color "#f8df6e"
        # vbox:
        #     for i in where_split_list: 
        #         text i color "#bea638"
        # vbox:
        #     for i in where_value_list: 
        #         text i color "#4b4010"
        # vbox:
        #     for i in where_parts: 
        #         text i color "#fc5252"

            # # sidebar 
            # frame: 
            #     xsize seekL_sidebar_size
            #     ysize seekL_height
            #     vbox: 
            #         spacing 5 
            #         button: 
            #             xfill True 
            #             background seekL_button_color 
            #             text "seekL" bold True
            #         button: 
            #             xfill True 
            #             background seekL_button_color 
            #             text "phoneLog" bold True
            #         button: 
            #             xfill True 
            #             background seekL_button_color 
            #             text "emailFeed" bold True

# screen entire_keyboard(w="chat",turnip=False): 
#     zorder 10

#     if not in_call:
#         key "q" action Function(next_letter, "q")
#         key "w" action Function(next_letter, "w")
#         key "e" action Function(next_letter, "e")
#         key "r" action Function(next_letter, "r")
#         key "t" action Function(next_letter, "t")
#         key "y" action Function(next_letter, "y")
#         key "u" action Function(next_letter, "u")
#         key "i" action Function(next_letter, "i")
#         key "o" action Function(next_letter, "o")
#         key "p" action Function(next_letter, "p")

#         key "a" action Function(next_letter, "a")
#         key "s" action Function(next_letter, "s")
#         key "d" action Function(next_letter, "d")
#         key "f" action Function(next_letter, "f")
#         key "g" action Function(next_letter, "g")
#         key "h" action Function(next_letter, "h")
#         key "j" action Function(next_letter, "j")
#         key "k" action Function(next_letter, "k")
#         key "l" action Function(next_letter, "l")

#         key "z" action Function(next_letter, "z")
#         key "x" action Function(next_letter, "x")
#         key "c" action Function(next_letter, "c")
#         key "v" action Function(next_letter, "v")
#         key "b" action Function(next_letter, "b")
#         key "n" action Function(next_letter, "n")
#         key "m" action Function(next_letter, "m")

#         key "shift_K_q" action Function(next_letter, "q")
#         key "shift_K_w" action Function(next_letter, "w")
#         key "shift_K_e" action Function(next_letter, "e")
#         key "shift_K_r" action Function(next_letter, "r")
#         key "shift_K_t" action Function(next_letter, "t")
#         key "shift_K_y" action Function(next_letter, "y")
#         key "shift_K_u" action Function(next_letter, "u")
#         key "shift_K_i" action Function(next_letter, "i")
#         key "shift_K_o" action Function(next_letter, "o")
#         key "shift_K_p" action Function(next_letter, "p")

#         key "shift_K_a" action Function(next_letter, "a")
#         key "shift_K_s" action Function(next_letter, "s")
#         key "shift_K_d" action Function(next_letter, "d")
#         key "shift_K_f" action Function(next_letter, "f")
#         key "shift_K_g" action Function(next_letter, "g")
#         key "shift_K_h" action Function(next_letter, "h")
#         key "shift_K_j" action Function(next_letter, "j")
#         key "shift_K_k" action Function(next_letter, "k")
#         key "shift_K_l" action Function(next_letter, "l")

#         key "shift_K_z" action Function(next_letter, "z")
#         key "shift_K_x" action Function(next_letter, "x")
#         key "shift_K_c" action Function(next_letter, "c")
#         key "shift_K_v" action Function(next_letter, "v")
#         key "shift_K_b" action Function(next_letter, "b")
#         key "shift_K_n" action Function(next_letter, "n")
#         key "shift_K_m" action Function(next_letter, "m")

#         key "K_SPACE" action Function(next_letter, " ")
#         key "K_PERIOD" action Function(next_letter, ".")
#         key "K_COMMA" action Function(next_letter, ",")
#         key "shift_K_SEMICOLON" action Function(next_letter, ":")
#         key "shift_K_9" action Function(next_letter, "(")
#         key "shift_K_0" action Function(next_letter, ")")
#         key "shift_K_1" action Function(next_letter, "!")
#         key "shift_K_8" action Function(next_letter, "*")
#         key "shift_K_SLASH" action Function(next_letter, "?")
#         key "K_QUOTE" action Function(next_letter, "'")
#         key "K_UNDERSCORE" action Function(next_letter, "_")
#         key "K_QUOTEDBL" action Function(next_letter, "\"")

#         key "K_BACKSPACE" action Function(next_letter, "DELETE")
#         key "K_TAB" action Function(next_letter, "TAB")

default is_paused = False  
default player_set_pause = False 

image fbi_lock: 
    "cg_bad.png"
    alpha 0.0
    pause 3 
    alpha 1.0 

image cg_platonic_arrive: 
    "cg platonic_zoom"
    alpha 0.0
    pause 3 
    ease 2.0 alpha 1.0 

screen game_over: 
    #modal True 
    add "#000000"
    add "fbi_lock"

screen game_over_text: 
    text "end: seek{color=b3b3af80}Loss{/color}": 
        xalign 0.5 
        yalign 1.0 
        font "Teko-VariableFont_wght.ttf"
        size 100
        color "#FFFFFF80"

screen game_over_neutral: 
    #modal True 
    add "#000000"
    #add "cg_platonic_arrive"

screen game_over_neutral_text: 
    text "end: seek{color=ecde8f80}Life{/color}": 
        xalign 0.95 
        yalign 1.0 
        font "Teko-VariableFont_wght.ttf"
        size 100
        color "#FFFFFF80"
screen game_over_good_text: 
    text "end: seek{color=f57cdf80}Love{/color}": 
        xalign 0.95 
        yalign 1.0 
        font "Teko-VariableFont_wght.ttf"
        size 100
        color "#FFFFFF80"

screen timer_window: 
    on "show" action  SetVariable("seekL_output", "")
    timer 0.1 action [Function(process_seekL, seekL_text_send), Hide("timer_window")]