
label day5_seekLove_call: 
    hide screen seekL_ui 
    scene black 
    hide screen phonecall_window_real with pixellate 
    stop music fadeout 0.5
    $ first_line = True 
    $ quick_menu = False 

    $ in_call = True 
    #$ chat_location = "DAY " +next_day_number+ " - CALL"

    $ _preferences.afm_enable = False 

    pause 2 
    menu: 
        "Hello?":
            pass
    $ first_line = False 
    play music "audio/music/Digital_Dream.mp3" loop fadein 2.0 fadeout 2.0 
    
    voice "audio/voice/day5/o5-001.ogg"
    o "So you've held up your end of the bargain."

    menu:
        "Did you think I wouldn't?":
            voice "audio/voice/day5/o5-002.ogg"
            o "No, but I still had to give you a hard time somehow."
            menu:
                "I'm destined to never get my appreciation, am I?":
                    pass
            voice "audio/voice/day5/o5-003.ogg"
            o "I do appreciate that you picked up."
            menu:
                "That's more like it.":
                    pass 
        "Ahh! It's you! ":
            voice "audio/voice/day5/o5-004.ogg"
            o "What– did you think I was just giving you a random number?"
            menu:
                "No! I just...really hoped it was yours but didn't want to assume.":
                    pass
            voice "audio/voice/day5/o5-005.ogg"
            o "That's...nice to hear."
            voice "audio/voice/day5/o5-006.ogg"
            o "Well, no need to stay on tenterhooks. I'm mostly done yanking your chain."
            menu:
                "Aw, thanks–huh?! Mostly?!":
                    pass

    voice "audio/voice/day5/o5-007.ogg"
    o "So now that that's over with–"
    menu:
        "Hey!":
            pass

    show cg romantic 
    camera:
        ypos -522 xpos 1395 zoom 1.58
        linear 5.0 xpos 324
    with dissolve
    voice "audio/voice/day5/o5-008.ogg"
    o "Now that that's over with, I am glad to hear from you."
    voice "audio/voice/day5/o5-009.ogg"
    o "I should have planned out a conversation but I honestly didn't think beyond this step."

    menu:
        "That's unlike you.":
            pass

    show cg romantic 
    camera:
        xpos -1494 ypos 1683 zoom 2.0
        linear 5.0 ypos 2169
    with dissolve
    voice "audio/voice/day5/o5-010.ogg"
    o "I know."
    voice "audio/voice/day5/o5-011.ogg"
    o "I was trying to channel you a little bit."
    menu:
        "You were?":
            pass
    voice "audio/voice/day5/o5-012.ogg"
    o "I was. Felt strange, but almost a little thrilling. "
    voice "audio/voice/day5/o5-013.ogg"
    o "Is that how you feel when you pull things like this?"
    menu:
        "Sometimes! Try it more often to see.":
            pass
    voice "audio/voice/day5/o5-014.ogg"
    o "I guess I will."
    voice "audio/voice/day5/o5-015.ogg"
    o "Unrelated, how's the weather where you are?"

    menu:
        "Pretty nice, wish you could feel it.":
            voice "audio/voice/day5/o5-016.ogg"
            o "If only I had some newfound disposable income."
            menu:
                "What a shame.":
                    pass
            voice "audio/voice/day5/o5-017.ogg"
            o "Guess we'll just leave it to imagination."
        "Terrible!":
            voice "audio/voice/day5/o5-018.ogg"
            o "Sounds like you need to get out of there for a bit, then."
            menu:
                "Oh, do I?":
                    pass
            voice "audio/voice/day5/o5-019.ogg"
            o "Just making a suggestion."
        "Why, need some travel ideas?":
            voice "audio/voice/day5/o5-020.ogg"
            o "I'm just making conversation."
            menu:
                "Mhm. Sure.":
                    pass
            voice "audio/voice/day5/o5-021.ogg"
            o "What?"

    menu:
        "You are so transparent.":
            pass
    voice "audio/voice/day5/o5-022.ogg"
    o "I know. Wasn't worth even trying on that one."
    voice "audio/voice/day5/o5-023.ogg"
    o "Still, the offer's there."
    menu:
        "I think I'd like that. But only on one condition.":
            pass
    voice "audio/voice/day5/o5-024.ogg"
    o "What's that?"
    menu:
        "Answer your own question. How's the weather where you are?":
            pass
    voice "audio/voice/day5/o5-025.ogg"
    o "And why would I tell you that? "
    voice "audio/voice/day5/o5-026.ogg"
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
    voice "audio/voice/day5/o5-027.ogg"
    o "Hah. It's not bad, actually. There's a nice breeze."
    voice "audio/voice/day5/o5-028.ogg"
    o "It's...weird."
    voice "audio/voice/day5/o5-029.ogg"
    o "Not unusual, but somehow it just feels different. Good different."

    menu: 
        "Maybe it's a sign.":
            voice "audio/voice/day5/o5-030.ogg"
            o "Could be. Could also be nothing."
            menu:
                "Does it matter?":
                    pass
            voice "audio/voice/day5/o5-031.ogg"
            o "I don't think it does...I just like it."
            voice "audio/voice/day5/o5-032.ogg"
            o "I like it."
        "Is it cold? Warm?":
            voice "audio/voice/day5/o5-033.ogg"
            o "A bit cool. But I like it that way. "
            voice "audio/voice/day5/o5-034.ogg"
            o "Always been used to my cold server rooms."
            voice "audio/voice/day5/o5-035.ogg"
            o "I like that. I like the cold. "
            voice "audio/voice/day5/o5-036.ogg"
            o "I like...this feeling. "

    pause 2
    voice "audio/voice/day5/o5-037.ogg"
    o "Thank you."
    menu:
        "For what?":
            pass
    show cg romantic 
    camera:
        zoom 1.0 xpos -891 ypos 1091
        linear 4.0 xpos -729
    with dissolve 
    voice "audio/voice/day5/o5-038.ogg"
    o "Being here."
    voice "audio/voice/day5/o5-039.ogg"
    o "For calling me and... talking about nothing with me."
    voice "audio/voice/day5/o5-040.ogg"
    o "For letting me ramble nonsense about the weather and whatever. "
    pause 1
    voice "audio/voice/day5/o5-041.ogg"
    o "It feels like a door's been cracked open. Like better things might be coming."
    voice "audio/voice/day5/o5-042.ogg"
    o "Um. If that makes sense."
    menu:
        "It does. That makes me happy to hear.":
            pass 
    voice "audio/voice/day5/o5-043.ogg"
    o "I'm glad. "
    voice "audio/voice/day5/o5-044.ogg"
    o "I like hearing that you're happy."
    menu:
        "Yeah?":
            pass 
    voice "audio/voice/day5/o5-045.ogg"
    o "Yeah. "
    pause 1 
    voice "audio/voice/day5/o5-046.ogg"
    o "I have to start unpacking, but...can we talk again soon?"
    menu: 
        "I'd like that. See you then?":
            pass 
    show cg romantic 
    camera:
        zoom 0.5 xpos 486 ypos 540
    with dissolve 
    voice "audio/voice/day5/o5-047-seeyousoon.ogg"
    o "See you soon."

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
