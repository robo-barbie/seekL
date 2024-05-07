label day3_call: 

    #voice "audio/voice/day2/o2-001.ogg"
    o "Well, here we are. Two hacks down, two to go."

    play music "audio/music/little_hand_on_the_clock.mp3" loop fadein 2.0 fadeout 2.0 

    o "I still have some things to wrap up so elimf will probably finish before me."
    menu: 
        "Best for last, right?": 
            pass 
    o "Ha. We can go with that."
    o "Feel like you're getting used to everything?"

    menu: 
        "We'll have to see when the best for last decides to give me some tips.":
            o "You're assuming I teach you anything."
            menu: 
                "And you're going to let me leave with only what incri taught me?":
                    pass
            o "...Maybe I shouldn't set that loose on the world."
        "I'd say so. Shame I won't get to test everything out with you guys.":
            o "You'll live. Not sure if your opsec will, though."
            o "I'll keep an eye out for you on the news."
            menu: 
                "So little faith in me.":
                    pass 
            o "Says the person who had their IP found within an hour of joining. By everyone."
            o "Sorry, that felt rude. Sorry."
            menu: 
                "And now you're bullying me??": 
                    pass 
            o "I said sorry! "

    menu: 
        "I think I can pull off something good, in time. Stick around and find out?":
            pass 
    o "Mm. I should've known it would come back to this."
    o "Why do you care about what I choose to do with myself?"
    menu: 
        "Am I not allowed to care about another person?":
            pass 
    o "You are, but... I'm not really a person anymore."

    menu: 
        "What do you mean?":    
            o "I'm no one. I'm going to be no one. You have other things to fill your life with."
            menu: 
                "I do. But I can care about multiple things at once.": 
                    pass 
            o "That sounds burdensome."
            o "Isn't that exhausting? "
            menu: 
                "Sometimes. But it's worth the trouble.":
                    pass
            o "Why?"
            menu: 
                "Because I like your company.": 
                    pass 
        "You still look like a person.":
            o "You know what I mean."
            menu: 
                "I know I'm arguing semantics. But you're still here, aren't you?": 
                    pass 
            o "Never been in a spot where you wanted to vanish? "
            menu: 
                "Didn't say that. ": 
                    pass 
            menu: 
                "But I've never followed through. ":
                    pass 
            o "You haven't felt how I feel, then. "
            o "Otherwise, you would have. "
            menu: 
                "Not true. I just worked through the feeling. ": 
                    pass 

    o "It can't be that simple."
    menu: 
        "Why not?": 
            pass 
    o "If it was that simple, then–"
    pause 1
    o "I don't know why I'm bothering to argue."
    o "Why do I feel like I need to prove this to you?"
    menu: 
        "Are you sure it's me?": 
            pass 
    pause 3
    o "No, no. Nope. No. "
    o "I think that's enough for today."
    o "Let's talk about anything else."
    pause 3
    o "Sorry. I'll think of something."
    o "What, um, what else do you do? Besides programming-related things."

    menu: 
        "Finding an excuse to get on my opsec again?":
            o "I mean, if you answer with something identifiable–"
            menu:
                "I get it, I get it! Umm. Hm.": 
                    pass 
        "Well, well, well. Look who is caring now.":
            o "Hovering over the 'end call' button as we speak."
            menu: 
                "Fine, fine, I'll answer!": 
                    pass 

    pause 1

    menu: 
        "I like trying out the dumbest sounding burger or sandwich on restaurant menus.":
            o "Dumbest name or composition?"
            menu: 
                "Whichever strikes me more. Sometimes I find one that's both.": 
                    pass 
            o "Such as...?"
            menu: 
                "The Preposterous PB&J burger– as in peanut butter and jalapeño jelly.": 
                    pass 
            o "That sounds...unpleasant."
            menu: 
                "It wasn't the worst!": 
                    pass 
            o "I'll take your word for it."
            o "Ugh. That's going to be stuck in my head now."
            menu: 
                "Sorry!":
                    pass 
            o "I'll recover. Eventually."
            o "...Is it strange that a sick part of me wants to try it?"
        "I like browsing niche community forums and trying to sneak my way in. ":
            o "What, like on Reddit? "
            o "Hardly niche. "
            menu: 
                "No, no. I'm talkin' Facebook groups. ": 
                    pass 
            o "Huh? "
            menu: 
                "Like neighborhood groups I live at least a thousand miles away from. ": 
                    pass 
            o "What? Why? What is wrong with you? "
            menu: 
                "To taste the drama without being affected by it. ": 
                    pass 
            o "Who likes chasing drama? "
            o "But, I can't believe I'm curious now."
            o "Am I missing out? Should I go seek out some suburban drama? "

    menu: 
        "You should. It's an acquired taste at first, but before you know it, {i}you'll be back.{/i}":
            pass
    pause 2
    o "Was that you trying to do the Terminator?"
    menu: 
        "I know it's terrible! I know!":
            pass
    o "That was the worst setup and impression I've ever heard."
    menu: 
        "You liked it. Look, here's another one–":
            pass
    o "Put the quotebook down! Now!"
    menu: 
        "...":
            pass
    o "Look–"
    menu: 
        "That one was even worse!":
            pass
    o "Stop being so gleeful about it!"
    menu: 
        "It was so bad!":
            pass
    o "It was a lapse in judgment."
    o "( laughing )"

    menu: 
        "I will remember this day forever.":
            o "Will you, really?"
            menu: 
                "I can't account for every contingency. But I can try.": 
                    pass 
            o "I'll take it."
        "I like your laugh, by the way. ":
            o "Oh, my laugh? "
            o "Um...thank you. Hm. "
            o "I've been laughing quite a bit, haven't I? "
            menu: 
                "Sure have. ": 
                    pass 
            o "Ha...odd. "

    pause 2
    o "I like your laugh, I think."
    menu: 
        "You think???":
            pass
    o "Yeah... I think. "
    o "Laugh again."
    menu: 
        "No, no, you have to earn that. Make me laugh. ":
            pass
    o "Never mind, shut up. "
    menu: 
        "( laugh )" :
            pass
    o "And now you laugh?? At me?? ( laughing )"
    o "Unbelievable... "
    pause 1
    menu: 
        "Can I ask just one thing about you?":
            pass
    o "Sure. Shoot. "
    menu: 
        "What was your first programming language? ":
            pass
    o "Why do you want to know that? "
    menu: 
        "No reason. Just curious. ":
            pass
    o "It was Python. "
    o "I was twelve and found a site dedicated to fun exercises using Python.  "
    o "Snake games, Tower of Hanoi... silly things. "
    pause 2
    o "I really liked that language. "
    menu: 
        "Do you not use it anymore?":
            pass
    o "No, Python can't cover everything I need to do in this server. "
    o "But it was beginner friendly. Really easy to read and understand, you know? "
    o "I'm grateful I found that language first. "
    o "Maybe I wouldn't have gotten into coding without it. "
    menu: 
        "So you do like coding. ":
            pass
    o "Ha."
    o "Maybe a little."
    o "You remember far too much of what I say. "
    pause 1
    o "Thank you for talking with me, these past couple days. "
    o "It's been nice. "
    menu: 
        "Can always talk for many more days, if you want.":
            pass
    o "Cheeky. "
    o "I don't know about that, Thrim."
    menu: 
        "Was worth a shot. ":
            pass
    o "Did you actually think it would work? "
    menu: 
        "Not really. But one can always hope. ":
            pass
    o "Ha. "
    o "Anyway, it's late. About time for me to head out."
    o "I'm presuming you'll be on tomorrow?"
    menu: 
        "You know it.":
            pass
    o "See you then."

    ## must run these two lines to swap to next day 
    $ next_day_number = "4"
    jump day_swap

    $ renpy.pause(hard=True)