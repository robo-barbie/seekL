label day3_call: 

    show spr o1 eyes closed
    #voice "audio/voice/day2/o2-001.ogg"
    o "Well, here we are. Two hacks down, two to go."

    play music "audio/music/little_hand_on_the_clock.mp3" loop fadein 2.0 fadeout 2.0 

    show spr o1 neutral 
    o "I still have some things to wrap up so elimf will probably finish before me."
    menu: 
        "Best for last, right?": 
            pass 

    show spr o1 smile
    o "Ha. We can go with that."

    show spr o1 neutral 
    o "Feel like you're getting used to everything?"

    menu: 
        "We'll have to see when the best for last decides to give me some tips.":
            show spr o1 eyes closed
            o "You're assuming I teach you anything."
            menu: 
                "And you're going to let me leave with only what incri taught me?":
                    pass
            show spr o1 done
            o "...Maybe I shouldn't set that loose on the world."
        "I'd say so. Shame I won't get to test everything out with you guys.":
            show spr o1 smile 
            o "You'll live. Not sure if your opsec will, though."
            show spr o1 closed eye happy 
            o "I'll keep an eye out for you on the news."
            show spr o1 smile
            menu: 
                "So little faith in me.":
                    pass 
            show spr o1 done
            o "Says the person who had their IP found within an hour of joining. By everyone."
            show spr o1 side nervous
            o "Sorry, that felt rude. Sorry."
            menu: 
                "And now you're bullying me??": 
                    pass 
            show spr o1 grin 
            o "I said sorry! "
            show spr o1 smile 

    menu: 
        "I think I can pull off something good, in time. Stick around and find out?":
            pass 
    show spr o1 frown
    o "Mm. I should've known it would come back to this."
    
    show spr o1 neutral 
    o "Why do you care about what I choose to do with myself?"
    menu: 
        "Am I not allowed to care about another person?":
            pass 

    show spr o1 side frown 
    o "You are, but... I'm not really a person anymore."

    menu: 
        "What do you mean?":   
            show spr o1 eyes closed  
            o "I'm no one. I'm going to be no one. You have other things to fill your life with."
            show spr o1 neutral 
            menu: 
                "I do. But I can care about multiple things at once.": 
                    pass 
            show spr o1 done frown 
            o "That sounds burdensome."

            show spr o1 side frown
            o "Isn't that exhausting? "
            menu: 
                "Sometimes. But it's worth the trouble.":
                    pass
            show spr o2 side frown
            o "Why?"
            menu: 
                "Because I like your company.": 
                    pass 
        "You still look like a person.":
            show spr o1 done frown
            o "You know what I mean."
            menu: 
                "I know I'm arguing semantics. But you're still here, aren't you?": 
                    pass 
            show spr o2 side frown
            o "Never been in a spot where you wanted to vanish? "
            menu: 
                "Didn't say that. ": 
                    pass 
            menu: 
                "But I've never followed through. ":
                    pass 
            show spr o2 scowl
            o "You haven't felt how I feel, then. "

            show spr o2 sad
            o "Otherwise, you would have. "
            menu: 
                "Not true. I just worked through the feeling. ": 
                    pass 

    show spr o3 shocked
    o "It can't be that simple."
    show spr o3 neutral
    menu: 
        "Why not?": 
            pass 
    show spr o2 side frown
    o "If it was that simple, then–"
    pause 1
    show spr o3 eyes closed 
    o "I don't know why I'm bothering to argue."
    show spr o2 side frown
    o "Why do I feel like I need to prove this to you?"
    menu: 
        "Are you sure it's me?": 
            pass 
    show spr o3 shocked
    pause 3
    show spr o2 side scowl
    o "No, no. Nope. No. "
    show spr o3 eyes closed 
    o "I think that's enough for today."
    show spr o3 neutral 
    o "Let's talk about anything else."
    pause 3
    show spr o1 eyes closed 
    o "Sorry. I'll think of something."
    show spr o1 side nervous 
    o "What, um, what else do you do? Besides programming-related things."
    show spr o1 neutral 

    menu: 
        "Finding an excuse to get on my opsec again?":
            show spr o1 done 
            o "I mean, if you answer with something identifiable–"
            menu:
                "I get it, I get it! Umm. Hm.": 
                    pass 
        "Well, well, well. Look who is caring now.":
            show spr o1 done
            o "Hovering over the 'end call' button as we speak."
            menu: 
                "Fine, fine, I'll answer!": 
                    pass 

    pause 1

    menu: 
        "I like trying out the dumbest sounding burger or sandwich on restaurant menus.":
            show spr o1 neutral 
            o "Dumbest name or composition?"
            menu: 
                "Whichever strikes me more. Sometimes I find one that's both.": 
                    pass 
            show spr o1 done 
            o "Such as...?"
            menu: 
                "The Preposterous PB&J burger– as in peanut butter and jalapeño jelly.": 
                    pass 
            show spr o1 done frown 
            o "That sounds...unpleasant."
            show spr o1 neutral 
            menu: 
                "It wasn't the worst!": 
                    pass 
            show spr o1 smile
            o "I'll take your word for it."
            show spr o2 scowl 
            o "Ugh. That's going to be stuck in my head now."
            menu: 
                "Sorry!":
                    pass 
            show spr o1 eyes closed 
            o "I'll recover. Eventually."
            show spr o3 shocked 
            o "...Is it strange that a sick part of me wants to try it?"
            show spr o3 neutral 
        "I like browsing niche community forums and trying to sneak my way in. ":
            show spr o1 smile 
            o "What, like on Reddit? "

            show spr o1 closed eye happy 
            o "Hardly niche. "
            show spr o1 smile 
            menu: 
                "No, no. I'm talkin' Facebook groups. ": 
                    pass 
            show spr o1 done frown
            o "Huh? "
            menu: 
                "Like neighborhood groups I live at least a thousand miles away from. ": 
                    pass 
            show spr o1 mad 
            o "What? Why? What is wrong with you? "
            menu: 
                "To taste the drama without being affected by it. ": 
                    pass 
            show spr o1 done frown 
            o "Who likes chasing drama? "
            show spr o1 side frown 
            o "But, I can't believe I'm curious now."
            show spr o1 grin 
            o "Am I missing out? Should I go seek out some suburban drama? "
            show spr o1 smile 

    menu: 
        "You should. It's an acquired taste at first, but before you know it, {i}you'll be back.{/i}":
            pass
    pause 2
    show spr o1 done 
    o "Was that you trying to do the Terminator?"
    menu: 
        "I know it's terrible! I know!":
            pass
    show spr o1 closed eye happy 
    o "That was the worst setup and impression I've ever heard."
    show spr o1 smile 
    menu: 
        "You liked it. Look, here's another one–":
            pass
    show spr o1 done frown
    o "Put the quotebook down! Now!"
    menu: 
        "...":
            pass
    o "Look–"
    menu: 
        "That one was even worse!":
            pass
    show spr o1 mad 
    o "Stop being so gleeful about it!"
    menu: 
        "It was so bad!":
            pass
    show spr o1 happy grin 
    o "It was a lapse in judgment."
    o "( laughing )"

    menu: 
        "I will remember this day forever.":
            show spr o1 grin 
            o "Will you, really?"
            show spr o1 smile 
            menu: 
                "I can't account for every contingency. But I can try.": 
                    pass 
            show spr o1 closed eye happy 
            o "I'll take it."
        "I like your laugh, by the way. ":
            show spr o3 silly 
            o "Oh, my laugh? "
            show spr o1 side nervous
            o "Um...thank you. Hm. "
            show spr o1 side smile 
            o "I've been laughing quite a bit, haven't I? "
            menu: 
                "Sure have. ": 
                    pass 
            show spr o1 side nervous 
            o "Ha...odd. "

    pause 2
    show spr o1 smile 
    o "I like your laugh, I think."
    menu: 
        "You think???":
            pass
    show spr o1 closed eye smile 
    o "Yeah... I think. "
    show spr closed eye grin
    o "Laugh again."
    show spr o1 smile
    menu: 
        "No, no, you have to earn that. Make me laugh. ":
            pass
    show spr o1 done
    o "Never mind, shut up. "
    menu: 
        "( laugh )" :
            pass
    show spr o1 grin 
    o "And now you laugh?? At me?? ( laughing )"
    show spr o1 side smile 
    o "Unbelievable... "
    pause 1
    show spr o1 smile 
    menu: 
        "Can I ask just one thing about you?":
            pass
    show spr o1 neutral 
    o "Sure. Shoot. "
    menu: 
        "What was your first programming language? ":
            pass
    o "Why do you want to know that? "
    menu: 
        "No reason. Just curious. ":
            pass
    o "It was Python. "
    
    show spr o1 eyes closed 
    o "I was twelve and found a site dedicated to fun exercises using Python.  "

    show spr o1 neutral 
    o "Snake games, Tower of Hanoi... silly things. "
    pause 2

    show spr o1 side frown 
    o "I really liked that language. "
    menu: 
        "Do you not use it anymore?":
            pass
    show spr o3 eyes closed 
    o "No, Python can't cover everything I need to do in this server. "
    show spr o3 neutral 
    o "But it was beginner friendly. Really easy to read and understand, you know? "
    show spr o1 closed eye smile 
    o "I'm grateful I found that language first. "
    show spr o1 neutral 
    o "Maybe I wouldn't have gotten into coding without it. "
    menu: 
        "So you do like coding. ":
            pass
    show spr o1 side smile 
    o "Ha."
    show spr o1 happy
    o "Maybe a little."
    show spr o1 side smile 
    o "You remember far too much of what I say. "
    pause 1
    show spr 
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