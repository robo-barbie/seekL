# The script of the game goes in this file.

###############################################################
######## sprite animation setup ###############################

init python:

    # This is set to the name of the character that is speaking, or
    # None if no character is currently speaking.
    speaking = None

    # This returns speaking if the character is speaking, and done if the
    # character is not.
    def while_speaking(name, speak_d, done_d, st, at):
        if speaking == name:
            return speak_d, .1
        else:
            return done_d, None

    # Curried form of the above.
    curried_while_speaking = renpy.curry(while_speaking)

    # Displays speaking when the named character is speaking, and done otherwise.
    def WhileSpeaking(name, speaking_d, done_d=Null()):
        return DynamicDisplayable(curried_while_speaking(name, speaking_d, done_d))

    # This callback maintains the speaking variable.
    def speaker_callback(name, event, **kwargs):
        global speaking
    
        if event == "show":
            speaking = name
        elif event == "slow_done":
            speaking = None
        elif event == "end":
            speaking = None

    # Curried form of the same.
    speaker = renpy.curry(speaker_callback)

    first_flash = True 

#############################################################


define o = Character("odxny", callback=speaker("odxny"))

default chat_location = "DAY 1 - CHAT"
default _game_menu_screen = None
screen ive_had_enough_of_the_fucking_scroll_up_rollback():
    key 'mousedown_4':
        action NullAction()

# The game starts here.

label start:
    show screen ive_had_enough_of_the_fucking_scroll_up_rollback
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    $ reset_chats()
    $ load_tables()

    play music "audio/music/Server_Room.mp3" loop fadein 2.0 fadeout 2.0 

    show screen seekL_ui 

    jump day1_start

    #$ renpy.input("xx")

    # $ chat_message("odxny: testing testing")
    # $ chat_message("wnpep: 12 x 4 = 48")
    # $ chat_message("wnpep: quotes test ready \"hello i'm in a quote 1 2 3\"")
    # $ chat_message("odxny: inline code test")
    # $ chat_message("odxny: `select * from test`")
    # $ chat_message("odxny: `select * \nfrom test\nwhere x > 12 \n  and id = \'yes\'`")

    #$ renpy.input("xx")


    $ renpy.pause(hard=True)

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
