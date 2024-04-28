##-----------------------------------------------------
## chat program setup 

default chat_speed = 3 

    # this is for formatting the text 
default who_is_typing = ""
default who_was_typing_list = []
default last_sender = ""
default last_window = "X"
default wait_time_prev = 0

    # this is also for formatting 
default current_window = "all"
default active_window = "all"

default seekL_recent_example = ""

    # character info 
    # character_names = {
    #     "Felix" : "Doyle", 
    #     "Jerri" : "Ngo", 
    #     "Major" : "Alstone", 
    #     "Sungho" : "Go"
    # }

default character_colors = {
    "thrim": "#ffa1a1", 
    "odxny": "#dd95ff", 
    "wnpep": "#aeff9a", 
    "incri": "#e4ff9a", 
    "elimf": "#9affd0", 
    "SYSTEM": "#999999"
}

    # chat groups 
default channels = {
    "all" : [], 
    "admin" : []
}

    # chat groups names 
default channels_names = {
    "all" : [], 
    "admin" : []
}

    # chat times
default channels_times = {
    "all" : [], 
    "admin" : []
}

    # indicator for when a new message arrives 
default channels_new_message = {
    "all" : False, 
    "admin" : False
}

    # who sent the last message in the channel 
default channels_last_sender = {
    "all" : "", 
    "admin" : ""
}


init python: 

    import time 
    from datetime import datetime 

    ### code to add choices to history window
    def log_menu_choice(item_text):
        if item_text != "Menu Prediction":
            """Log a choice-menu choice, which is passed in as item_text.
            Implementation based on add_history() in renpy/character.py."""
            h = renpy.character.HistoryEntry()
            h.who = ""
            h.what = ">> " + item_text
            h.what_args = []

            if renpy.game.context().rollback:
                h.rollback_identifier = renpy.game.log.current.identifier
            else:
                h.rollback_identifier = None

            _history_list.append(h)

            while len(_history_list) > renpy.config.history_length:
                _history_list.pop(0)

    ## basic variables 

    player_fname = "thrim"
    # player_lname = ""

    # autoscroll vars
    yadjValue = float("inf")
    yadj = ui.adjustment()


    ## chat functions 

    # function to call to reset/clear everything 
    def reset_chats(): 
        global current_window
        global active_window
        # global character_names 
        global channels 
        global channels_names
        global channels_times
        global channels_new_message 
        global who_is_typing
        global who_was_typing_list  
        global last_sender
        global last_window 
        global previous_commands

        previous_commands = []

        current_window = "all"
        active_window = "all"
        last_window = "X"

        who_is_typing = ""
        who_was_typing_list = []
        last_sender = ""

        # character info 
        # character_names = {
        #     "Felix" : "Doyle", 
        #     "Jerri" : "Ngo", 
        #     "Major" : "Alstone", 
        #     "Sungho" : "Go", 
        #     "Player" : "Name"
        # }

        # chat groups 
        channels = {
            "all" : [], 
            "admin" : []
        }

        # chat groups names 
        channels_names = {
            "all" : [], 
            "admin" : []
        }

        # chat times
        channels_times = {
            "all" : [], 
            "admin" : []
        }

        # indicator for when a new message arrives 
        channels_new_message = {
            "all" : False, 
            "admin" : False 
        }

        # who sent the last message in the channel 
        channels_last_sender = {
            "all" : "", 
            "admin" : ""
        }

    # player makes a choice 
    def player_choice(l): 
        global active_window
        global player_fname
        global chat_speed

        if chat_speed != 100: 
            renpy.pause(1)

        selected = renpy.display_menu(l)
        x = "_"
        for i in l: 
            if i[1] == selected: 
                x = i[0]
        chat_message(player_fname + ": " + x, c = active_window, is_player = True)
        if len(l) > 1:
            renpy.jump(selected)

    def click_text(): 
        global seekL_text_send 
        global seekL_recent_example 
        seekL_text_send = seekL_recent_example

    # new message
    def chat_message(s, c="all", ot="", is_player = False, fastmode=False): # string, channel, others typing, is player
        global chat_speed 
        global channels
        global channels_names
        global channels_times
        global channels_new_message
        global channels_last_sender
        global current_window
        global active_window 
        global who_is_typing
        global last_sender
        global last_window 
        # global character_names
        global yadj 
        global yadjValue
        global wait_time_prev
        global seekL_recent_example

        # split into name / content, get new active channel  
        n = s.split(': ', 1)[0]
        t = s.split(': ', 1)[1]

        if t == "no (tutorial)": 
            t = "no"
        t0 = t

        t_out = ""
        quote_open = False
        code_block_open = False 
        table_name_open = False
        word_open = False 
        l_insert = ""
        for idx, letter in enumerate([*t]):
            if letter == "`": 
                ##### IF YOU CHANGE THIS, YOU NEED TO CHANGE IT IN SEEKL AS WELL 
                if not code_block_open:
                    seekL_recent_example = ""
                    code_block_open = True
                    l_insert = "{color=ffb8f3}------------------------------\n{/color}{color=ff75e8}{font=HELLO.ttf.ttf}"
                else: 
                    code_block_open = False
                    l_insert = "{/font}{/color}\n{color=ffb8f3}------------------------------{/color}"
            elif letter == "#": 
                if not table_name_open:  
                    table_name_open = True 
                    l_insert = "{color=ccff11}{font=HELLO.ttf.ttf}"
                else: 
                    table_name_open = False 
                    l_insert = "{/font}{/color}"
            elif code_block_open: 
                seekL_recent_example = seekL_recent_example + letter 
                l_insert = letter 
            # "#ff75e8"
            # elif letter == "\"": 
            #     if not quote_open: 
            #         l_insert = "{color=ff9a41}\""
            #         quote_open = True 
            #     else: 
            #         l_insert = "\"{/color}"
            #         quote_open = False 
            # # numbers 
            # elif letter.isnumeric() and not quote_open and not code_block_open: 
            #     l_insert = "{color=ffe941}" + letter + "{/color}" # this will cause problems probably
            # # symbols 
            # elif letter in ["$"] and not quote_open and not code_block_open: 
            #     l_insert = "{color=ff2b2b}" + letter + "{/color}" # this will cause problems probably
            # elif letter in ["[", "]"] and not quote_open and not code_block_open: 
            #     l_insert = "{color=f13dca}" + letter + "{/color}" # this will cause problems probably
            # elif letter in ["(", ")"] and not quote_open and not code_block_open: 
            #     l_insert = "{color=ffbe0c}" + letter + "{/color}"
            # elif letter in ["=", "-", "+", "/", "*", ".", ",", ";", ":", "!", "?", "'"] and not quote_open and not code_block_open: 
            #     l_insert = "{color=FFFFFF}" + letter + "{/color}"
            # # for 
            # elif letter.lower() == "f" and (idx == 0 or t[idx-1] == " ") and not quote_open and not code_block_open and not word_open: 
            #     if len(t) >= idx+4: 
            #         if t[idx+1].lower() == "o" and t[idx+2].lower() == "r" and t[idx+3] == " ":
            #             if not word_open: 
            #                 l_insert = "{color=3945ee}f"
            #                 word_open = True 
            #             else:
            #                 l_insert = letter
            #         else:
            #             l_insert = letter
            #     elif len(t) >= idx+6: 
            #         if t[idx+1].lower() == "a" and t[idx+2].lower() == "l" and t[idx+3].lower() == "s" and t[idx+4].lower() == "e" and t[idx+5] == " ":
            #             if not word_open: 
            #                 l_insert = "{color=3945ee}w"
            #                 word_open = True 
            #             else:
            #                 l_insert = letter
            #         else:
            #             l_insert = letter
            #     else:
            #         l_insert = letter
            # # if  
            # elif letter.lower() == "i" and (idx == 0 or t[idx-1] == " ") and not quote_open and not code_block_open and not word_open: 
            #     if len(t) >= idx+2: 
            #         if t[idx+1].lower() == "f" and t[idx+2] == " ":
            #             if not word_open: 
            #                 l_insert = "{color=e839ee}i"
            #                 word_open = True 
            #             else:
            #                 l_insert = letter
            #         else:
            #             l_insert = letter
            #     else:
            #         l_insert = letter
            # # else 
            # elif letter.lower() == "e" and (idx == 0 or t[idx-1] == " ") and not quote_open and not code_block_open and not word_open: 
            #     if len(t) >= idx+5: 
            #         if t[idx+1].lower() == "l" and t[idx+2].lower() == "s" and t[idx+3].lower() == "e" and t[idx+4] == " ":
            #             if not word_open: 
            #                 l_insert = "{color=e839ee}e"
            #                 word_open = True 
            #             else:
            #                 l_insert = letter
            #         else:
            #             l_insert = letter
            #     else:
            #         l_insert = letter
            # # true 
            # elif letter.lower() == "t" and (idx == 0 or t[idx-1] == " ") and not quote_open and not code_block_open and not word_open: 
            #     if len(t) >= idx+5: 
            #         if t[idx+1].lower() == "r" and t[idx+2].lower() == "u" and t[idx+3].lower() == "e" and t[idx+4] == " ":
            #             if not word_open: 
            #                 l_insert = "{color=3945ee}t"
            #                 word_open = True 
            #             else:
            #                 l_insert = letter
            #         else:
            #             l_insert = letter
            #     else:
            #         l_insert = letter
            # # while 
            # elif letter.lower() == "w" and (idx == 0 or t[idx-1] == " ") and not quote_open and not code_block_open and not word_open: 
            #     if len(t) >= idx+6: 
            #         if t[idx+1].lower() == "h" and t[idx+2].lower() == "i" and t[idx+3].lower() == "l" and t[idx+4].lower() == "e" and t[idx+5] == " ":
            #             if not word_open: 
            #                 l_insert = "{color=3945ee}w"
            #                 word_open = True 
            #             else:
            #                 l_insert = letter
            #         else:
            #             l_insert = letter
            #     else:
            #         l_insert = letter
            # # and 
            # elif letter.lower() == "a" and (idx == 0 or t[idx-1] == " ") and not quote_open and not code_block_open and not word_open: 
            #     if len(t) >= idx+4: 
            #         if t[idx+1].lower() == "n" and t[idx+2].lower() == "d" and t[idx+3] == " ":
            #             if not word_open: 
            #                 l_insert = "{color=3945ee}a"
            #                 word_open = True 
            #             else:
            #                 l_insert = letter
            #         else:
            #             l_insert = letter
            #     else:
            #         l_insert = letter
            # # not 
            # elif letter.lower() == "n" and not quote_open and not code_block_open and not word_open: 
            #     if len(t) >= idx+4: 
            #         if t[idx+1].lower() == "o" and t[idx+2].lower() == "t" and t[idx+3] == " ":
            #             if not word_open: 
            #                 l_insert = "{color=3945ee}n"
            #                 word_open = True 
            #             else:
            #                 l_insert = letter
            #         else:
            #             l_insert = letter
            #     else:
            #         l_insert = letter
            # # def 
            # elif letter.lower() == "d" and not quote_open and not code_block_open and not word_open: 
            #     if len(t) >= idx+4: 
            #         if t[idx+1].lower() == "e" and t[idx+2].lower() == "f" and t[idx+3] == " ":
            #             if not word_open: 
            #                 l_insert = "{color=3945ee}d"
            #                 word_open = True 
            #             else:
            #                 l_insert = letter
            #         else:
            #             l_insert = letter
            #     else:
            #         l_insert = letter
            # elif letter == " " and word_open: 
            #     l_insert = "{/color} "
            #     word_open = False 
            else:
                l_insert = letter
            t_out = t_out + l_insert
            if idx == len([*t]) -1 and (quote_open or code_block_open): 
                t_out = t_out + "{/color}" 
            #"#d6fa9d" 
        t = t_out 
        #t.replace("\"", "{color=ff9a41}\"{/color}")
        active_window = c 

        # pause briefly if we are swapping windows 
        if last_window != active_window and chat_speed != 100: 
            renpy.pause(2)

        if not is_player:
            # pause before displaying the message + change who is typing 
            wait_time = len(t0)/5/chat_speed
            if ot != "" and chat_speed != 100: 
                set_is_typing(n + ", " + ot, wait_time, wait_time_prev, fastmode)
            elif n != "SYSTEM" and chat_speed != 100:
                set_is_typing(n, wait_time, wait_time_prev, fastmode)
            elif chat_speed != 100: 
                renpy.pause(1.0)

            wait_time_prev = wait_time/2

        # if we've never seen this channel before, add it 
        if c not in channels.keys(): 
            channels[c] = []
            channels_last_sender[c] = "" 

        # if not active in that channel, light up that button 
        if current_window != c: 
            channels_new_message[c] = True 

        # send the message 
        # if channels_last_sender[c] == n and last_window == active_window: 
        #     channels[c].append(t)
        # else: 
        #     channels[c].append("\n{b}" + n +  " " + character_names[n] +  "{/b}\n" + t)
        channels[c].append(t)
        channels_names[c].append(n)
        channels_times[c].append(str(datetime.now().strftime('%H:%M')))
        # channels = channels[-100:].copy()
        # channels_names = channels_names[-100:].copy()
        # channels_times = channels_times[-100:].copy()
        if chat_speed != 100:
            if n != "SYSTEM":
                #renpy.play("audio/sfx/message_notification_01_005 chat.ogg")
                renpy.play("audio/sfx/message_notification_03_002 message alt.ogg")
            else: 
                renpy.play("audio/sfx/message_notification_03_001 system.ogg")
        elif is_player: 
            #renpy.play("audio/sfx/message_notification_01_005 chat.ogg")
            renpy.play("audio/sfx/message_notification_03_002 message alt.ogg")

        if yadj.value == yadj.range:
            yadj.value = float('inf')
        #yadj.value = yadjValue

        # update who the new last sender is 
        channels_last_sender[c] = n

        # update what the last window is 
        last_window = c 

        if (is_player or n == "SYSTEM") and chat_speed != 100: 
            renpy.pause(0.5)

    # show who is typing + logic for timing 
    def set_is_typing(n, wt, wtp, fastmode=False): # names 
        #global who_is_typing 
        global who_is_typing
        global who_was_typing_list 

        # create new "who is typing" string 
        n_list = n.replace(" ", "").split(",")
        n_list.sort(key=lambda v: v.upper())

        # show only names that carry over from previous typing 
        pre_typers = []
        for i in n_list: 
            if i in who_was_typing_list: 
                pre_typers.append(i) 
        if len(pre_typers) > 0: 
            who_is_typing = format_typers(pre_typers)
        else: 
            who_is_typing = ""
        if not fastmode: 
            renpy.pause(wtp) 

        # show new list of typers 
        who_is_typing = format_typers(n_list)
        if not fastmode: 
            renpy.pause(wt) 
        else: 
            renpy.pause(0.1)
        

        # save off who was now typing + reset 
        who_was_typing_list = n_list 
        who_is_typing = ""
        
    # format logic for typing string 
    # this is only showing one person for some reason 
    def format_typers(n_list): 
        # global character_names 

        if len(n_list) > 3: 
            w = "Several people are typing..."
        else:
            w = ""
            for i in n_list: 
                if i != n_list[-1]:
                    w = w + i + ", " 
                else: 
                    w = w + i + " "
            if len(n_list) > 1: 
                w = w + "are typing..."
            else: 
                w = w+ "is typing..."
        #w = "people are typing..."
        return(w)

screen click_text_screen: 
    on "show" action Function(click_text), Hide("click_text_screen")

##-----------------------------------------------------
## screen 

# screen chat_messages_view: 
#     add "#372C3E" 

#     ## messages area 
#     window: 
#         padding (20,20)
#         background None 
#         area(750, 200, 1560, 1040) # 2560 x 1440 screen 
#         vbox:
#             spacing 20
#             text current_window color "#FFFFFF"
#             viewport  yadjustment yadj: 
#                 xmaximum 1500 
#                 scrollbars "vertical"
#                 mousewheel True 

#                 vbox: 
#                     box_wrap True
#                     for n in channels[current_window]: 
#                         hbox: 
#                             spacing 20 
#                             if n.split(" ")[0].startswith("\n"):
#                                 vbox: 
#                                     null height 50 # this i set after eyeballing how far to drop the icon 
#                                     if n.split(" ")[0][4:] == player_fname: 
#                                         add "Player.png"
#                                     else:
#                                         add n.split(" ")[0][4:] + ".png"
#                             else: 
#                                 null width 70 # width of the icons 
#                             text n:
#                                 size 30  
#                                 color "#FFFFFF"
#                                 line_spacing 10

#             if current_window == active_window: 
#                 text who_is_typing color "#FFFFFF" size 20 yalign 1.0 
                        
    
    # ## sidebar 
    # window: 
    #     padding (20,20)
    #     background "#262029"
    #     area(250, 200, 400, 1040)
    #     vbox: 
    #         spacing 20
    #         for l in channels.keys(): 
    #             textbutton l:
    #                 if channels_new_message[l]:
    #                     text_color "#EAC119"
    #                 else: 
    #                     text_color "#FFFFFF"
    #                 text_hover_color "#D6FF1B"
    #                 action SetDict(channels_new_message, l, False), SetVariable("current_window", l) 
