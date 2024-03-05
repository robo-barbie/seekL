# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    $ reset_chats()

    show screen seekL_ui 

    #$ renpy.input("xx")

    $ chat_message("odxny: testing testing")
    $ chat_message("wnpep: 12 x 4 = 48")
    $ chat_message("wnpep: quotes test ready \"hello i'm in a quote 1 2 3\"")
    $ chat_message("odxny: inline code test")
    $ chat_message("odxny: `select * from test`")
    $ chat_message("odxny: `select * \nfrom test\nwhere x > 12 \n  and id = \'yes\'`")

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
