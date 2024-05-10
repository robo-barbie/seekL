
label day4_call: 
    $ first_line = True 
    menu: 
        "Hm? What's up?":
            pass 
    $ first_line = False 
    pause 1
    show spr o1 side neutral 
    o "No real reason this time. Just felt like calling."
    show spr o1 neutral 

    play music "audio/music/little_hand_on_the_clock.mp3" loop fadein 2.0 fadeout 2.0 
    
    show spr o1 grin 
    o "And why not keep up the streak?"
    show spr o1 smile 

    menu: 
        "Odd for someone so eager to leave soon. ":
            show spr o1 done 
            o "Don't press your luck. "
            show spr o1 eyes closed 
            o "Nothing's changed. "
            show spr o1 neutral 
            menu:
                "Sure.":
                    pass
        "Good point. Anything you want to talk about then?":
            o "I haven't thought of anything yet."
            menu: 
                "Just say the first thing that comes to mind then.":
                    pass
    show spr o1 side frown
    o "Uhh. Hm."
    show spr o1 neutral 
    o "Do you smoke?"
    show spr o1 side nervous 
    o "Sorry, the first thing that came to mind was elimf's victory bowl."
    show spr o1 frown

    menu: 
        "I have been known to partake, yes.":
            show spr o1 smile 
            o "That's a fun way of putting it."
            pause 1
            show spr o1 neutral 
            o "Were you partaking when you joined the server–"
            menu: 
                "No.": 
                    pass 
            show spr o1 side nervous 
            o "Sorry. Had to ask."
            show spr o1 neutral 
        "Nah, it's not for me.":
            show spr o1 eyes closed
            o "All good. It's not for everyone."
            show spr o1 neutral 
        "I'm more of an edibles person.":

            o "Oh, it's that much of a difference?"
            menu: 
                "Yeah, I don't care for the smoke or mess.":
                    pass
            show spr o1 eyes closed 
            o "That's pretty practical."
            show spr o1 neutral 

    menu:
        "What about you?":
            pass 
    show spr o1 side frown 
    o "No, I don't. Tried it once and it didn't really add anything."
    show spr o1 frown 
    o "Which was actually incredibly disappointing. "
    show spr o2 sad
    o "Everyone around me seemed to easily float away into their own little worlds. "
    show spr o2 side frown
    o "And there I was. Staring at drywall. "
    menu:
        "Anything interesting on the drywall?":
            pass
    show spr o3 shocked 
    o "No. What? "
    menu:
        "I don't know. Like a stain or something. ":
            pass
    show spr o3 neutral 
    o "Why in the world would that be interesting? "
    menu:
        "Have you no curiosity for odd stains? ":
            pass
    show spr o1 closed eye happy 
    o "Stupid, ha. "
    show spr o1 neutral 
    o "But, anyway, easier on my wallet to not get into all that. More for the fund. "
    pause 1
    menu:
        "Yeah... that fund.":
            pass
    o "We talked about this. "
    show spr o1 frown 
    o "I don't even understand why you feel this strongly in the first place."
    show spr o1 neutral 
    menu:
        "Is it hard to believe I've come to like you in a few days?":
            pass
    show spr o1 mad 
    o "In a way that matters, yes."
    show spr o1 side frown 
    o "We have fun, but it's not... you know..."
    show spr o1 neutral 
    o "This should be like never seeing a fond acquaintance again. Feeling sad for a minute before it fades off."
    menu: 
        "I don't think that little of you.":
            pass 
    show spr o1 mad 
    o "Well- I don't- it-"
    show spr o2 side scowl 
    o "Gah."
    show spr o2 side frown 
    o "I– it's not a matter of thinking little of me. It's just fact."
    show spr o2 sad 
    o "It's life. It's normal. People come, people go."

    menu:
        "Not for me. I can't just forget you that easily.":
            show spr o2 scowl 
            o "Then–try!"
            o "You're putting so much on yourself, and for what?"
            show spr o2 side scowl 
            o "You don't stand to gain anything."
            menu:
                "Peace of mind. Knowing you're still out there.":
                    pass
            show spr o1 mad 
            o "I'll be living outside society, not–"
            pause 2
            show spr o1 closed eye frown 
            o "I couldn't go that far. "
            show spr o1 frown 
        "I thought you said you weren't a person anymore. ":
            pause 1
            show spr o1 neutral 
            o "You're right. Apologies. Slip of the tongue. "
            show spr o1 eyes closed 
            o "\"Not a person\". That's me. "
            show spr o1 neutral 
            o "Wasting space better occupied by an actual person. "
            show spr o1 side frown 
            o "Someone who hasn't thought how much better it would all be if it just ended."
            show spr o3 shocked
            o "If it just–"
            pause 2
            show spr o2 sad 
            o "But I couldn't... wouldn't do that. "

    menu:
        "You...sound like you've thought of it.":
            pass
    o "...I have. But it's not something I consider anymore."
    menu:
        "What changed?":
            pass
    pause 2
    show spr o2 side frown 
    o "Nothing. "
    o "Nothing changed at all. "
    show spr o2 sad 
    o "This is just what my mind settled on. "

    menu:
        "Were you scared?":
            show spr o2 side frown 
            o "I wasn't. This was more practical. "
            show spr o2 side scowl 
            o "I'm not scared of not existing. I'm not. "
            show spr o2 upset 
            o "Why should I be? "
            menu:
                "Okay. ":
                    pass
            show spr o3 neutral 
            o "I'm not. "
        "Why?":
            show spr o2 side frown 
            o "(sigh) How the hell would I know? "
            o "Nothing seems to make sense anymore. "
            show spr o2 upset 
            o "Everything used to be so certain and now..."
            show spr o2 sad 
            o "...Now I'm just..."

    pause 2
    show spr o3 neutral 
    o "Don't read into what I'm about to say, okay?"
    menu:
        "Sure. ":
            pass
    show spr o1 neutral 
    o "How does anyone even start over? "
    o "It's all gone. It's just me now. Alone."
    show spr o1 side frown 
    o "And I don't understand how this happened."
    show spr o1 frown 
    o "It's like I'm suffocating while watching everyone else easily breathe fresh air."
    show spr o1 mad 
    o "So, I can either leave it all behind and accept this new normal, or... what?"
    show spr o1 side frown 
    o "How do you make real connections? I don't understand anymore."
    show spr o1 neutral 

    menu:
        "I'm not sure, but...I think I feel a connection with you.":
            show spr o1 mad 
            o "Stop that. "
            show spr o1 neutral 
            o "You feel pity, is what you feel."
            menu:
                "I know myself. ":
                    pass
        "I think you just have to try. Go outside, talk to people, all that.":
            show spr o1 mad 
            o "\"Go outside?\" Are you serious? "
            o "You think I haven't tried that?"
            menu:
                "No? ":
                    pass

    pause 1
    menu:
        "What about those friends you mentioned? ":
            pass
    show spr o1 neutral 
    o "Which friends? "
    menu:
        "The ones you smoked with. ":
            pass
    show spr o1 mad 
    o "I told you. Everyone is gone. "
    show spr o1 side frown 
    o "I don't even remember really what happened with them. "
    show spr o1 neutral 
    o "We haven't spoken in years. "
    menu:
        "Maybe reach out?":
            pass
    o "And say what, exactly? "
    show spr o1 eyes closed 
    o "It's been years. It wouldn't make sense. "
    pause 1
    show spr o1 neutral 
    o "Is it really that easy for you? "
    menu:
        "It's not. But I still have to try.":
            pass
    show spr o3 shocked 
    o "Is that...is that what you're doing with me?"
    menu:
        "What?":
            pass
    o "Is this..."
    pause 2
    show spr o3 neutral 
    o "I have work to do. "
    show spr o3 eyes closed 
    o "See you tomorrow. "
    menu:
        "Wait!":
            pass

    $ _preferences.afm_enable = False 
    $ renpy.pause(hard=True)