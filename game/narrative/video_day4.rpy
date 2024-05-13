
label day4_call: 
    $ first_line = True 
    menu: 
        "Hm? What's up?":
            pass 
    $ first_line = False 
    pause 1
    show spr o1 side neutral 
    voice "audio/voice/day4/o4-001.ogg"
    o "No real reason this time. Just felt like calling."
    show spr o1 neutral 

    play music "audio/music/Reflection_in_the_Blank_Screen.mp3" loop fadein 2.0 fadeout 2.0 
    
    show spr o1 grin 
    voice "audio/voice/day4/o4-002.ogg"
    o "And why not keep up the streak?"
    show spr o1 smile 

    menu: 
        "Odd for someone so eager to leave soon. ":
            show spr o1 done 
            voice "audio/voice/day4/o4-003.ogg"
            o "Don't press your luck. "
            show spr o1 eyes closed 
            voice "audio/voice/day4/o4-004.ogg"
            o "Nothing's changed. "
            #show spr o1 neutral 
            menu:
                "Sure.":
                    pass
        "Good point. Anything you want to talk about then?":
            $ points_seekLove += 2
            show spr o1 neutral 
            voice "audio/voice/day4/o4-005.ogg"
            o "I haven't thought of anything yet."
            menu: 
                "Just say the first thing that comes to mind then.":
                    pass
    show spr o1 side frown
    voice "audio/voice/day4/o4-006.ogg"
    o "Uhh. Hm."
    show spr o1 neutral 
    voice "audio/voice/day4/o4-007.ogg"
    o "Do you smoke?"
    show spr o1 side nervous 
    voice "audio/voice/day4/o4-008.ogg"
    o "Sorry, the first thing that came to mind was elimf's victory bowl."
    show spr o1 frown

    menu: 
        "I have been known to partake, yes.":
            show spr o1 smile 
            voice "audio/voice/day4/o4-009.ogg"
            o "That's a fun way of putting it."
            pause 1
            #show spr o1 neutral 
            voice "audio/voice/day4/o4-010.ogg"
            o "Were you partaking when you joined the server–"
            menu: 
                "No.": 
                    pass 
            show spr o1 grin 
            voice "audio/voice/day4/o4-011.ogg"
            o "Sorry. Had to ask."
            show spr o1 smile 
            #show spr o1 neutral 
        "Nah, it's not for me.":
            show spr o1 eyes closed
            voice "audio/voice/day4/o4-012.ogg"
            o "All good. It's not for everyone."
            #show spr o1 neutral 
        "I'm more of an edibles person.":
            voice "audio/voice/day4/o4-013.ogg"
            o "Oh, it's that much of a difference?"
            menu: 
                "Yeah, I don't care for the smoke or mess.":
                    pass
            show spr o1 eyes closed 
            voice "audio/voice/day4/o4-014.ogg"
            o "That's pretty practical."
            #show spr o1 neutral 

    menu:
        "What about you?":
            pass 
    show spr o1 side frown 
    voice "audio/voice/day4/o4-015.ogg"
    o "No, I don't. Tried it once and it didn't really add anything."
    show spr o1 eyes closed 
    voice "audio/voice/day4/o4-016.ogg"
    o "Which was actually incredibly disappointing. "
    show spr o1 eyes closed 
    voice "audio/voice/day4/o4-017.ogg"
    o "Everyone around me seemed to easily float away into their own little worlds. "
    show spr o1 side frown 
    voice "audio/voice/day4/o4-018.ogg"
    o "And there I was. Staring at drywall. "
    menu:
        "Anything interesting on the drywall?":
            pass
    show spr o3 neutral 
    voice "audio/voice/day4/o4-019.ogg"
    o "No. What? "
    menu:
        "I don't know. Like a stain or something. ":
            pass
    show spr o3 shocked 
    voice "audio/voice/day4/o4-020.ogg"
    o "Why in the world would that be interesting? "
    menu:
        "Have you no curiosity for odd stains? ":
            pass
    show spr o1 closed eye happy 
    voice "audio/voice/day4/o4-021.ogg"
    o "Stupid, ha. "
    show spr o1 neutral 
    voice "audio/voice/day4/o4-022.ogg"
    o "But, anyway, easier on my wallet to not get into all that. More for the fund. "
    pause 1
    menu:
        "Yeah... that fund.":
            pass
    voice "audio/voice/day4/o4-023.ogg"
    o "We talked about this. "
    show spr o1 frown 
    voice "audio/voice/day4/o4-024.ogg"
    o "I don't even understand why you feel this strongly in the first place."
    show spr o1 neutral 
    menu:
        "Is it hard to believe I've come to like you in a few days?":
            pass
    show spr o1 mad 
    voice "audio/voice/day4/o4-025.ogg"
    o "In a way that matters, yes."
    show spr o1 side frown 
    voice "audio/voice/day4/o4-026.ogg"
    o "We have fun, but it's not... you know..."
    #show spr o1 neutral 
    voice "audio/voice/day4/o4-027.ogg"
    o "This should be like never seeing a fond acquaintance again. Feeling sad for a minute before it fades off."
    menu: 
        "I don't think that little of you.":
            pass 
    show spr o1 mad 
    voice "audio/voice/day4/o4-028.ogg"
    o "Well- I don't- it-"
    show spr o2 side scowl 
    voice "audio/voice/day4/o4-029.ogg"
    o "Gah."
    show spr o2 side frown 
    voice "audio/voice/day4/o4-030.ogg"
    o "I– it's not a matter of thinking little of me. It's just fact."
    show spr o2 sad 
    voice "audio/voice/day4/o4-031.ogg"
    o "It's life. It's normal. People come, people go."

    menu:
        "Not for me. I can't just forget you that easily.":
            $ points_seekLove += 2
            show spr o2 scowl 
            voice "audio/voice/day4/o4-032.ogg"
            o "Then–try!"
            voice "audio/voice/day4/o4-033.ogg"
            o "You're putting so much on yourself, and for what?"
            show spr o2 upset
            voice "audio/voice/day4/o4-034.ogg"
            o "You don't stand to gain anything."
            menu:
                "Peace of mind. Knowing you're still out there.":
                    pass
            #show spr o3 neutral
            voice "audio/voice/day4/o4-035.ogg"
            o "I'll be living outside society, not–"
            show spr o2 sad 
            pause 2
            #show spr o2 sad 
            voice "audio/voice/day4/o4-036.ogg"
            o "I couldn't go that far. "
            #show spr o1 frown 
        "I thought you said you weren't a person anymore. ":
            show spr o2 upset
            pause 1
            #show spr o1 neutral 
            show spr o2 scowl 
            voice "audio/voice/day4/o4-037.ogg"
            o "You're right. Apologies. Slip of the tongue. "
            show spr o2 side scowl
            voice "audio/voice/day4/o4-038.ogg"
            o "\"Not a person\". That's me. "
            #show spr o1 neutral 
            voice "audio/voice/day4/o4-039.ogg"
            o "Wasting space better occupied by an actual person. "
            #show spr o1 side frown 
            #show spr o2 scowl 
            voice "audio/voice/day4/o4-040.ogg"
            o "Someone who hasn't thought how much better it would all be if it just ended."
            #show spr o3 shocked
            voice "audio/voice/day4/o4-041.ogg"
            o "If I just–"
            #show spr o2 sad 
            pause 1
            show spr o2 sad 
            pause 1
            voice "audio/voice/day4/o4-042.ogg"
            o "But I couldn't... wouldn't do that. "

    menu:
        "You...sound like you've thought of it.":
            pass
    show spr o2 side frown
    voice "audio/voice/day4/o4-043.ogg"
    o "...I have. But it's not something I consider anymore."
    menu:
        "What changed?":
            pass
    pause 2
    #show spr o3 neutral
    show spr o2 sad 
    voice "audio/voice/day4/o4-044.ogg"
    o "Nothing. "
    voice "audio/voice/day4/o4-045.ogg"
    o "Nothing changed at all. "
    #show spr o3 eyes closed 
    voice "audio/voice/day4/o4-046.ogg"
    o "This is just what my mind settled on. "

    menu:
        "Were you scared?":
            #show spr o2 side frown 
            show spr o3 eyes closed 
            voice "audio/voice/day4/o4-047.ogg"
            o "I wasn't. This was more practical. "
            show spr o3 shocked
            voice "audio/voice/day4/o4-048.ogg"
            o "I'm not scared of not existing. I'm not. "
            #show spr o2 upset 
            voice "audio/voice/day4/o4-049.ogg"
            o "Why should I be? "
            menu:
                "Okay. ":
                    pass
            #show spr o3 neutral 
            show spr o1 side frown
            voice "audio/voice/day4/o4-050.ogg"
            o "I'm not. "
        "Why?":
            $ points_seekLove += 2
            show spr o2 side frown 
            voice "audio/voice/day4/o4-051.ogg"
            o "How the hell would I know? "
            voice "audio/voice/day4/o4-052.ogg"
            o "Nothing seems to make sense anymore. "
            show spr o2 upset 
            voice "audio/voice/day4/o4-053.ogg"
            o "Everything used to be so certain and now..."
            show spr o2 sad 
            voice "audio/voice/day4/o4-054.ogg"
            o "...Now I'm just..."

    pause 2
    show spr o3 neutral 
    #show spr o1 side frown
    voice "audio/voice/day4/o4-055.ogg"
    o "Don't read into what I'm about to say, okay?"
    menu:
        "Sure. ":
            pass
    pause 1
    show spr o1 side frown
    pause 1 
    voice "audio/voice/day4/o4-056.ogg"
    o "How does anyone even start over? "
    voice "audio/voice/day4/o4-057.ogg"
    o "It's all gone. It's just me now. Alone."
    #show spr o1 side frown 
    voice "audio/voice/day4/o4-058.ogg"
    o "And I don't understand how this happened."
    #show spr o1 frown 
    voice "audio/voice/day4/o4-059.ogg"
    o "It's like I'm suffocating while watching everyone else easily breathe fresh air."
    show spr o1 mad 
    voice "audio/voice/day4/o4-060.ogg"
    o "So, I can either leave it all behind and accept this new normal, or... what?"
    show spr o1 side frown 
    voice "audio/voice/day4/o4-061.ogg"
    o "How do you make real connections? I don't understand anymore."
    #show spr o1 neutral 

    menu:
        "I'm not sure, but...I think I feel a connection with you.":
            $ points_seekLove += 2
            show spr o1 mad 
            voice "audio/voice/day4/o4-062.ogg"
            o "Stop that. "
            #show spr o1 neutral 
            voice "audio/voice/day4/o4-063.ogg"
            o "You feel pity, is what you feel."
            menu:
                "I know myself. ":
                    pass
        "I think you just have to try. Go outside, talk to people, all that.":
            show spr o1 mad 
            voice "audio/voice/day4/o4-064.ogg"
            o "\"Go outside?\" Are you serious? "
            voice "audio/voice/day4/o4-065.ogg"
            o "You think I haven't tried that?"
            menu:
                "No? ":
                    pass

    pause 1
    menu:
        "What about those friends you mentioned? ":
            pass
    show spr o1 neutral 
    voice "audio/voice/day4/o4-066.ogg"
    o "Which friends? "
    menu:
        "The ones you smoked with. ":
            pass
    show spr o1 mad 
    voice "audio/voice/day4/o4-067.ogg"
    o "I told you. Everyone is gone. "
    show spr o1 side frown 
    voice "audio/voice/day4/o4-068.ogg"
    o "I don't even remember really what happened with them. "
    #show spr o1 neutral 
    voice "audio/voice/day4/o4-069.ogg"
    o "We haven't spoken in years. "
    menu:
        "Maybe reach out?":
            pass
    voice "audio/voice/day4/o4-070.ogg"
    show spr o1 mad 
    o "And say what, exactly? "
    #show spr o1 eyes closed 
    voice "audio/voice/day4/o4-071.ogg"
    o "It's been years. It wouldn't make sense. "
    pause 2
    show spr o1 side frown
    pause 2 
    #show spr o1 neutral 
    voice "audio/voice/day4/o4-073.ogg"
    o "Is it really that easy for you? "
    menu:
        "It's not. But I still have to try.":
            pass
    show spr o3 shocked 
    voice "audio/voice/day4/o4-074.ogg"
    o "Is that what you're doing with me?"
    menu:
        "What?":
            pass
    voice "audio/voice/day4/o4-075.ogg"
    o "Is this..."
    pause 2
    show spr o3 neutral 
    voice "audio/voice/day4/o4-076.ogg"
    o "I have work to do. "
    show spr o3 eyes closed 
    voice "audio/voice/day4/o4-077.ogg"
    o "See you tomorrow. "
    menu:
        "Wait!":
            pass

    ## must run these two lines to swap to next day 
    $ next_day_number = "5"
    jump day_swap

    $ renpy.pause(hard=True)