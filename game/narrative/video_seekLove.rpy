
label day5_seekLove_call: 
    stop music fadeout 0.5
    $ first_line = True 
    $ quick_menu = False 
    hide screen seekL_ui 

    $ in_call = True 
    #$ chat_location = "DAY " +next_day_number+ " - CALL"

    $ _preferences.afm_enable = False 

    scene black 

    pause 2 
    menu: 
        "Hello?":
            pass
    $ first_line = False 
    play music "audio/music/Digital_Dream.mp3" loop fadein 2.0 fadeout 2.0 
    
    o "So you've held up your end of the bargain."

    menu:
        "Did you think I wouldn't?":
            o "No, but I still had to give you a hard time somehow."
            menu:
                "I'm destined to never get my appreciation, am I?":
                    pass
            o "I do appreciate that you picked up."
            menu:
                "That's more like it.":
                    pass 
        "Ahh! It's you! ":
            o "What– did you think I was just giving you a random number?"
            menu:
                "No! I just...really hoped it was yours but didn't want to assume.":
                    pass
            o "That's...nice to hear."
            o "Well, no need to stay on tenterhooks. I'm mostly done yanking your chain."
            menu:
                "Aw, thanks–huh?! Mostly?!":
                    pass

    o "So now that that's over with–"
    menu:
        "Hey!":
            pass

    show cg romantic 
    camera:
        ypos -522 xpos 1395 zoom 1.58
        linear 5.0 xpos 324
    with dissolve
    o "Now that that's over with, I am glad to hear from you."
    o "I should have planned out a conversation but I honestly didn't think beyond this step."

    menu:
        "That's unlike you.":
            pass

    show cg romantic 
    camera:
        xpos -1494 ypos 1683 zoom 2.0
        linear 5.0 ypos 2169
    with dissolve
    o "I know."
    o "I was trying to channel you a little bit."
    menu:
        "You were?":
            pass
    o "I was. Felt strange, but almost a little thrilling. "
    o "Is that how you feel when you pull things like this?"
    menu:
        "Sometimes! Try it more often to see.":
            pass
    o "I guess I will."
    o "Unrelated, how's the weather where you are?"

    menu:
        "Pretty nice, wish you could feel it.":
            o "If only I had some newfound disposable income."
            menu:
                "What a shame.":
                    pass
            o "Guess we'll just leave it to imagination."
        "Terrible!":
            o "Sounds like you need to get out of there for a bit, then."
            menu:
                "Oh, do I?":
                    pass
            o "Just making a suggestion."
        "Why, need some travel ideas?":
            o "I'm just making conversation."
            menu:
                "Mhm. Sure.":
                    pass
            o "What?"

    menu:
        "You are so transparent.":
            pass
    o "I know. Wasn't worth even trying on that one."
    o "Still, the offer's there."
    menu:
        "I think I'd like that. But only on one condition.":
            pass
    o "What's that?"
    menu:
        "Answer your own question. How's the weather where you are?":
            pass
    o "And why would I tell you that? "
    o "Some of us still care about our privacy. "
    menu:
        "Uh huh. Sure. ":
            pass
    pause 1
    show cg romantic 
    camera:
        zoom 0.57 xpos 486 ypos 540
        linear 4.0 zoom 0.5
    with dissolve 
    o "Hah. It's not bad, actually. There's a nice breeze."
    o "It's...weird."
    o "Not unusual, but somehow it just feels different. Good different."

    menu: 
        "Maybe it's a sign.":
            o "Could be. Could also be nothing."
            menu:
                "Does it matter?":
                    pass
            o "I don't think it does...I just like it."
            o "I like it."
        "Is it cold? Warm?":
            o "A bit cool. But I like it that way. "
            o "Always been used to my cold server rooms."
            o "I like that. I like the cold. "
            o "I like...this feeling. "

    pause 2
    o "Thank you."
    menu:
        "For what?":
            pass
    show cg romantic 
    camera:
        zoom 1.0 xpos -891 ypos 1091
        linear 4.0 xpos -729
    with dissolve 
    o "Being here."
    o "For calling me and... talking about nothing with me."
    o "For letting me ramble nonsense about the weather and whatever. "
    pause 1
    o "It feels like a door's been cracked open. Like better things might be coming."
    o "Um. If that makes sense."
    menu:
        "It does. That makes me happy to hear.":
            pass 
    o "I'm glad. "
    o "I like hearing that you're happy."
    menu:
        "Yeah?":
            pass 
    o "Yeah. "
    pause 1 
    o "I have to start unpacking, but...can we talk again soon?"
    menu: 
        "I'd like that. See you then?":
            pass 
    show cg romantic 
    camera:
        zoom 0.5 xpos 486 ypos 540
    with dissolve 
    o "See you, stranger."

    $ persistent.seekLove = True

    pause 1 
    show screen game_over_good_text with Dissolve(2.0) 
    
    pause 

    hide screen game_over_good_text with dissolve

    scene black 
    camera: 
        subpixel True pos (0,0) zoom 1.0
    with dissolve

    stop music fadeout 3.0 

    pause 4 

    return 
