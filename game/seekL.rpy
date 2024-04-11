
init python: 
    seekL_button_color = "#48cb3a"
    seekL_window_size = 800
    seekL_sidebar_size = 200 
    seekL_height = 950
    seekL_height_half = 475
    seekL_button_height = 50 

    seekL_chat_text_size = 25 
    seekL_choice_window_height = 200

    seekL_text_entry = ""
    seekL_text_send = ""

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
                                        text t: 
                                            text_align 0.0
                                            size seekL_chat_text_size 
                                            xmaximum seekL_window_size
                                            if channels_names[current_window][idx] in character_colors: 
                                                color "#ffffffba"#character_colors[channels_names[current_window][idx]]
                                            else: 
                                                color "#FFFFFF"
                                            # line_spacing 10
                            null height 20 
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

                if current_window == active_window: 
                    text who_is_typing:
                        color "#FFFFFF85" 
                        size 20 
                        #yalign 1.0 
                        ypos 720
                        xalign 0.9



        # interactive other stuff 
        hbox: 
            spacing 10 
            # area to interact
            # seekL program 
            vbox: 
                frame: 
                    xsize seekL_window_size 
                    ysize seekL_height_half - seekL_button_height
                    padding(10,10,10,10)
                    input default "":
                        caret_blink True 
                        multiline True 
                        copypaste True 
                        #text_size seekL_chat_text_size
                        value VariableInputValue("seekL_text_send")
                hbox: 
                    xalign 0.5 
                    spacing 100 
                    # button: 
                    #     xalign 0.5
                    #     background seekL_button_color
                    #     ysize seekL_button_height
                    #     text "commands" bold True
                    button: 
                        xalign 0.5
                        background seekL_button_color
                        ysize seekL_button_height
                        text "execute" bold True
                        action Play("sound", "audio/sfx/data_success.ogg"), Function(process_seekL, seekL_text_send) #SetVariable("seekL_text_entry", seekL_text_send)
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
                                text o line_spacing 5 size 30

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