
label day4_call: 
    menu: 
        "Hm? What's up?":
            pass 
    pause 1
    o "No real reason this time. Just felt like calling."
    o "And why not keep up the streak?"

    menu: 
        "Odd for someone so eager to leave soon. ":
            o "Don't press your luck. "
            o "Nothing's changed. "
            menu:
                "Sure.":
                    pass
        "Good point. Anything you want to talk about then?":
            o "I haven't thought of anything yet."
            menu: 
                "Just say the first thing that comes to mind then.":
                    pass

    o "Uhh. Hm."
    o "Do you smoke?"
    o "Sorry, the first thing that came to mind was elimf's victory bowl."

    menu: 
        "I have been known to partake, yes.":
            o "That's a fun way of putting it."
            pause 1
            o "Were you partaking when you joined the server–"
            menu: 
                "No.": 
                    pass 
            o "Sorry. Had to ask."
        "Nah, it's not for me.":
            o "All good. It's not for everyone."
        "I'm more of an edibles person.":
            o "Oh, it's that much of a difference?"
            menu: 
                "Yeah, I don't care for the smoke or mess.":
                    pass
            o "That's pretty practical."

    menu:
        "What about you?":
            pass 
    o "No, I don't. Tried it once and it didn't really add anything."
    o "Which was actually incredibly disappointing. "
    o "Everyone around me seemed to easily float away into their own little worlds. "
    o "And there I was. Staring at drywall. "
    menu:
        "Anything interesting on the drywall?":
            pass
    o "No. What? "
    menu:
        "I don't know. Like a stain or something. ":
            pass
    o "Why in the world would that be interesting? "
    menu:
        "Have you no curiosity for odd stains? ":
            pass
    o "Stupid, ha. "
    o "But, anyway, easier on my wallet to not get into all that. More for the fund. "
    pause 1
    menu:
        "Yeah... that fund.":
            pass
    o "We talked about this. "
    o "I don't even understand why you feel this strongly in the first place."
    menu:
        "Is it hard to believe I've come to like you in a few days?":
            pass
    o "In a way that matters, yes."
    o "We have fun, but it's not... you know..."
    o "This should be like never seeing a fond acquaintance again. Feeling sad for a minute before it fades off."
    menu: 
        "I don't think that little of you.":
            pass 
    o "Well- I don't- it-"
    o "Gah."
    o "I– it's not a matter of thinking little of me. It's just fact."
    o "It's life. It's normal. People come, people go."

    menu:
        "Not for me. I can't just forget you that easily.":
            o "Then–try!"
            o "You're putting so much on yourself, and for what?"
            o "You don't stand to gain anything."
            menu:
                "Peace of mind. Knowing you're still out there.":
                    pass
            o "I'll be living outside society, not–"
            pause 2
            o "I couldn't go that far. "
        "I thought you said you weren't a person anymore. ":
            pause 1
            o "You're right. Apologies. Slip of the tongue. "
            o "\"Not a person\". That's me. "
            o "Wasting space better occupied by an actual person. "
            o "Someone who hasn't thought how much better it would all be if it just ended."
            o "If it just–"
            pause 2
            o "But I couldn't... wouldn't do that. "

    menu:
        "You...sound like you've thought of it.":
            pass
    o "...I have. But it's not something I consider anymore."
    menu:
        "What changed?":
            pass
    pause 2
    o "Nothing. "
    o "Nothing changed at all. "
    o "This is just what my mind settled on. "

    menu:
        "Were you scared?":
            o "I wasn't. This was more practical. "
            o "I'm not scared of not existing. I'm not. "
            o "Why should I be? "
            menu:
                "Okay. ":
                    pass
            o "I'm not. "
        "Why?":
            o "(sigh) How the hell would I know? "
            o "Nothing seems to make sense anymore. "
            o "Everything used to be so certain and now..."
            o "...Now I'm just..."

    pause 2
    o "Don't read into what I'm about to say, okay?"
    menu:
        "Sure. ":
            pass
    o "How does anyone even start over? "
    o "It's all gone. It's just me now. Alone."
    o "And I don't understand how this happened."
    o "It's like I'm suffocating while watching everyone else easily breathe fresh air."
    o "So, I can either leave it all behind and accept this new normal, or... what?"
    o "How do you make real connections? I don't understand anymore."

    menu:
        "I'm not sure, but...I think I feel a connection with you.":
            o "Stop that. "
            o "You feel pity, is what you feel."
            menu:
                "I know myself. ":
                    pass
        "I think you just have to try. Go outside, talk to people, all that.":
            o "\"Go outside?\" Are you serious? "
            o "You think I haven't tried that?"
            menu:
                "No? ":
                    pass

    pause 1
    menu:
        "What about those friends you mentioned? ":
            pass
    o "Which friends? "
    menu:
        "The ones you smoked with. ":
            pass
    o "I told you. Everyone is gone. "
    o "I don't even remember really what happened with them. "
    o "We haven't spoken in years. "
    menu:
        "Maybe reach out?":
            pass
    o "And say what, exactly? "
    o "It's been years. It wouldn't make sense. "
    pause 1
    o "Is it really that easy for you? "
    menu:
        "It's not. But I still have to try.":
            pass
    o "Is that...is that what you're doing with me?"
    menu:
        "What?":
            pass
    o "Is this..."
    pause 2
    o "I have work to do. "
    o "See you tomorrow. "
    menu:
        "Wait!":
            pass

    $ renpy.pause(hard=True)