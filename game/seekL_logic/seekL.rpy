
init python: 
    seekL_button_color = "#48cb3a"
    seekL_button_color_inactive = "#4e4e4e"
    seekL_button_color_unclicked = "#3c6837"
    seekL_button_color_execute = "#30abe4"
    seekL_button_color_clear = "#eb7c7c"
    seekL_window_size = 800
    seekL_sidebar_size = 200 
    seekL_height = 950
    seekL_height_half = 475
    seekL_button_height = 50 

    seekL_chat_text_size = 25 
    seekL_choice_window_height = 200

    seekL_text_entry = ""
    seekL_text_send = ""

    # autoscroll vars
    xadjValue_sl = float("inf")
    xadj_sl = ui.adjustment()
    xadj_sl.value = float("inf")

    seekL_window_active = 1

    rulebook = [
        """{font=HELLO.ttf.ttf}{size=25}1. SELECT
Use this to select specific columns (comma separated) or all columns at once (*).{color=ffffff69}
    EX: SELECT * 
    EX: SELECT id, date, part_no
        {/color}{/size}{/font}""",
        """{font=HELLO.ttf.ttf}{size=25}2. FROM 
Indicate which table you'd like to see. {color=ffffff69}
    EX: SELECT * FROM tablename 
        {/color}{/size}{/font}"""
    ]

screen seekL_ui: 
    hbox: 
        xalign 0.5 
        yalign 0.5
        spacing 50
        # chats
        vbox:
            # chat labels 
            frame: 
                xsize seekL_sidebar_size + seekL_window_size
                ysize seekL_button_height
                background None 
                hbox: 
                    spacing 5
                    button: 
                        xsize seekL_sidebar_size 
                        background seekL_button_color
                        text "chat" xalign 0.5 bold True
                    # button: 
                    #     xsize seekL_sidebar_size
                    #     background seekL_button_color 
                    #     text "odxny" xalign 0.5 bold True
            # actual chat 
            frame: 
                xsize seekL_window_size + seekL_sidebar_size
                ysize seekL_height - seekL_button_height
                vbox:
                    viewport  yadjustment yadj: 
                        ysize seekL_height - seekL_choice_window_height
                        draggable True
                        scrollbars "vertical"
                        mousewheel "change"
                        yinitial 1.0

                        vbox: 
                            box_wrap True
                            spacing 20 
                            null height 10
                            for idx, t in enumerate(channels[current_window]): 
                                vbox: 
                                    xpos 20
                                    ysize None 
                                    # has fixed:
                                    #     yfit True # only for window 
                                    if idx != 0: 
                                        if channels_names[current_window][idx] == channels_names[current_window][idx-1]:
                                            null height 0
                                            # text channels_names[current_window][idx] + ">":
                                            #     xanchor 1.0
                                            #     text_align 1.0
                                            #     xpos 130
                                            #     xsize 100
                                            #     size seekL_chat_text_size 
                                            #     if channels_names[current_window][idx] in character_colors: 
                                            #         color character_colors[channels_names[current_window][idx]] + "85"
                                            #     else: 
                                            #         color "#FFFFFF85"
                                        else: 
                                            vbox:
                                                null height 30 
                                                # text channels_times[current_window][idx]:
                                                #     size seekL_chat_text_size-10
                                                #     xanchor 1.0
                                                #     text_align 1.0
                                                #     xpos 120
                                                #     xsize 80
                                                if channels_names[current_window][idx] != "SYSTEM":
                                                    text channels_names[current_window][idx] + ">" + channels_times[current_window][idx]: 
                                                        #xanchor 1.0
                                                        #text_align 1.0
                                                        #xpos 130
                                                        xsize 100
                                                        size seekL_chat_text_size 
                                                        if channels_names[current_window][idx] in character_colors: 
                                                            color character_colors[channels_names[current_window][idx]] + "85"
                                                        else: 
                                                            color "#FFFFFF85"
                                    else:   
                                        vbox:
                                            #null height 30 
                                            # text channels_times[current_window][idx]:
                                            #     size seekL_chat_text_size-10
                                            #     xanchor 1.0
                                            #     text_align 1.0
                                            #     xpos 120
                                            #     xsize 80
                                            if channels_names[current_window][idx] != "SYSTEM":
                                                text channels_names[current_window][idx] + ">" + channels_times[current_window][idx]: 
                                                    # xanchor 1.0
                                                    # text_align 1.0
                                                    # xpos 130
                                                    xsize 100
                                                    size seekL_chat_text_size 
                                                    if channels_names[current_window][idx] in character_colors: 
                                                        color character_colors[channels_names[current_window][idx]] + "85"
                                                    else: 
                                                        color "#FFFFFF85"
                                    vbox:
                                        #xpos 20 
                                        #xanchor 0.0
                                        # if idx != 0: 
                                        #     if channels_names[current_window][idx] != channels_names[current_window][idx-1]:
                                        #         null height 50 
                                                # text " ":
                                                #     size seekL_chat_text_size-10
                                        if channels_names[current_window][idx] != "SYSTEM":
                                            text t: 
                                                text_align 0.0
                                                size seekL_chat_text_size 
                                                xmaximum seekL_window_size
                                                if channels_names[current_window][idx] in character_colors: 
                                                    color "#ffffffba"#character_colors[channels_names[current_window][idx]]
                                                else: 
                                                    color "#FFFFFF"
                                        else: 
                                            text t + " ------": 
                                                text_align 0.5
                                                font "HELLO.ttf.ttf"
                                                size seekL_chat_text_size 
                                                bold True 
                                                xmaximum seekL_window_size
                                                color character_colors[channels_names[current_window][idx]] + "85"
                                            # line_spacing 10
                            null height 50 
                    frame: 
                        background "#ffffff15"
                        xfill True 
                        yfill True 
                        # text " > ": 
                        #     size seekL_chat_text_size
                # frame: 
                #     xsize 2 
                #     ysize seekL_height - seekL_choice_window_height
                #     xpos 139
                #     background "#ffffff23"



        # interactive other stuff 
        hbox: 
            spacing 10 
            # area to interact
            # seekL program 
            vbox: 
                # command history 
                hbox: 
                    xalign 0.0
                    spacing 5
                    button: 
                        xalign 0.5
                        if seekL_window_active == 1: 
                            background seekL_button_color
                        else: 
                            background seekL_button_color_unclicked
                        ysize seekL_button_height
                        text "console" 
                        action Play("sound", "audio/sfx/tab_swap.ogg"), SetVariable("seekL_window_active", 1)
                    button: 
                        xalign 0.5
                        if seekL_window_active == 0: 
                            background seekL_button_color
                        else: 
                            background seekL_button_color_unclicked
                        ysize seekL_button_height
                        text "history" 
                        action Play("sound", "audio/sfx/tab_swap.ogg"), SetVariable("seekL_window_active", 0)
                    button: 
                        xalign 0.5
                        if seekL_window_active == -1: 
                            background seekL_button_color
                        else: 
                            background seekL_button_color_unclicked
                        ysize seekL_button_height
                        text "guide" 
                        action Play("sound", "audio/sfx/tab_swap.ogg"), SetVariable("seekL_window_active", -1)
                frame: 
                    xsize seekL_window_size 
                    ysize seekL_height_half - seekL_button_height
                    padding(20,20,20,20)
                    viewport: 
                        scrollbars "both"
                        mousewheel True 
                        #xinitial 1.0 
                        if seekL_window_active == 1:
                            input default "":
                                caret_blink True 
                                multiline True 
                                copypaste True 
                                xmaximum seekL_window_size-40
                                font "HELLO.ttf.ttf"
                                color "#d6fa9d"
                                #text_size seekL_chat_text_size
                                value VariableInputValue("seekL_text_send")
                        elif seekL_window_active == 0: 
                            vbox: 
                                spacing 5
                                xmaximum seekL_window_size-40
                                for i in range(len(previous_commands)): 
                                    vbox: 
                                        spacing 0 
                                        text previous_commands[len(previous_commands)-(i+1)] color "#ffffff69" font "HELLO.ttf.ttf"
                                        text "--------" color "#ffffff69" font "HELLO.ttf.ttf"
                        elif seekL_window_active == -1: 
                            vbox: 
                                xmaximum seekL_window_size-40
                                for i in range(len(rulebook)): 
                                    text rulebook[i]
    
    
                frame: 
                    xsize seekL_window_size 
                    ysize seekL_height_half
                    padding(30,30,30,30)
                    viewport: 
                        draggable True
                        scrollbars "horizontal"
                        mousewheel "change"

                        hbox: 
                            spacing 30
                            for o in seekL_output: 
                                text o line_spacing 5 size 30 font "HELLO.ttf.ttf"

    if current_window == active_window: 
        text who_is_typing:
            color "#FFFFFF85" 
            size 15 
            #yalign 1.0 
            ypos 840
            #xalign 0.0
            xpos 50

    hbox: 
        xpos 1920-525 
        ypos seekL_height_half+20
        #xalign 0.5 
        spacing 10 
        # execute 
        button: 
            xalign 0.5
            if seekL_window_active == 1 and seekL_text_send != "": 
                background seekL_button_color_execute
                text "execute" bold True 
            else: 
                background seekL_button_color_inactive
                text "execute" bold True color "#b1b1b1"
            ysize seekL_button_height
            
            if seekL_window_active == 1:
                action Function(process_seekL, seekL_text_send) 
        button: 
            xalign 0.5
            if seekL_window_active == 1 and seekL_text_send != "": 
                background seekL_button_color_clear
                text "clear" bold True
            else: 
                background seekL_button_color_inactive
                text "clear" bold True  color "#b1b1b1"
            ysize seekL_button_height
            if seekL_window_active == 1:
                action Play("sound", "audio/sfx/query_clear.ogg"), SetVariable("seekL_text_send", "")

    hbox: 
        ypos 50
        xpos 500 
        textbutton "slow": 
            action SetVariable("chat_speed", 2)
        textbutton "normal": 
            action SetVariable("chat_speed", 3)
        textbutton "hyperspeed": 
            action SetVariable("chat_speed", 100)

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