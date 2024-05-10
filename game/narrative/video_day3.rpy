label day3_call: 

    show spr o1 eyes closed
    voice "audio/voice/day3/o3-001.ogg"
    o "Well, here we are. Two hacks down, two to go."

    play music "audio/music/Digital_Dream.mp3" loop fadein 2.0 fadeout 2.0 

    show spr o1 neutral 
    voice "audio/voice/day3/o3-002.ogg"
    o "I still have some things to wrap up so elimf will probably finish before me."
    menu: 
        "Best for last, right?": 
            pass 

    show spr o1 smile
    voice "audio/voice/day3/o3-003.ogg"
    o "Ha. We can go with that."

    #show spr o1 neutral 
    voice "audio/voice/day3/o3-004.ogg"
    o "Feel like you're getting used to everything?"

    menu: 
        "We'll have to see when the best for last decides to give me some tips.":
            show spr o1 eyes closed
            voice "audio/voice/day3/o3-005.ogg"
            o "You're assuming I teach you anything."
            menu: 
                "And you're going to let me leave with only what incri taught me?":
                    pass
            show spr o1 done
            voice "audio/voice/day3/o3-006.ogg"
            o "...Maybe I shouldn't set that loose on the world."
        "I'd say so. Shame I won't get to test everything out with you guys.":
            show spr o1 smile 
            voice "audio/voice/day3/o3-007.ogg"
            o "You'll live. Not sure if your opsec will, though."
            show spr o1 closed eye happy 
            voice "audio/voice/day3/o3-008.ogg"
            o "I'll keep an eye out for you on the news."
            show spr o1 smile
            menu: 
                "So little faith in me.":
                    pass 
            show spr o1 done
            voice "audio/voice/day3/o3-009.ogg"
            o "Says the person who had their IP found within an hour of joining. By everyone."
            show spr o1 side nervous
            voice "audio/voice/day3/o3-010.ogg"
            o "Sorry, that felt rude. Sorry."
            menu: 
                "And now you're bullying me??": 
                    pass 
            show spr o1 grin 
            voice "audio/voice/day3/o3-011.ogg"
            o "I said sorry! "
            show spr o1 smile 

    menu: 
        "I think I can pull off something good, in time. Stick around and find out?":
            pass 
    show spr o1 frown
    voice "audio/voice/day3/o3-012.ogg"
    o "Mm. I should've known it would come back to this."
    
    show spr o1 eyes closed 
    voice "audio/voice/day3/o3-013.ogg"
    o "Why do you care about what I choose to do with myself?"
    menu: 
        "Am I not allowed to care about another person?":
            pass 

    show spr o1 side frown 
    voice "audio/voice/day3/o3-014.ogg"
    o "You are, but... I'm not really a person anymore."

    menu: 
        "What do you mean?":   
            #show spr o1 eyes closed  
            show spr o2 side frown
            voice "audio/voice/day3/o3-015.ogg"
            o "I'm no one. I'm going to be no one. You have other things to fill your life with."
            #show spr o1 neutral 
            menu: 
                "I do. But I can care about multiple things at once.": 
                    pass 
            #show spr o1 done frown 
            show spr o2 sad
            voice "audio/voice/day3/o3-016.ogg"
            o "That sounds burdensome."

            #show spr o1 side frown
            voice "audio/voice/day3/o3-017.ogg"
            o "Isn't that exhausting? "
            menu: 
                "Sometimes. But it's worth the trouble.":
                    pass
            #show spr o2 side frown
            voice "audio/voice/day3/o3-018.ogg"
            o "Why?"
            menu: 
                "Because I like your company.": 
                    pass 
        "You still look like a person.":
            show spr o1 done frown
            voice "audio/voice/day3/o3-019.ogg"
            o "You know what I mean."
            menu: 
                "I know I'm arguing semantics. But you're still here, aren't you?": 
                    pass 
            show spr o2 side frown
            voice "audio/voice/day3/o3-020.ogg"
            o "Never been in a spot where you wanted to vanish? "
            menu: 
                "Didn't say that. ": 
                    pass 
            menu: 
                "But I've never followed through. ":
                    pass 
            show spr o2 scowl
            voice "audio/voice/day3/o3-021.ogg"
            o "You haven't felt how I feel, then. "

            show spr o2 sad
            voice "audio/voice/day3/o3-022.ogg"
            o "Otherwise, you would have. "
            menu: 
                "Not true. I just worked through the feeling. ": 
                    pass 

    show spr o2 scowl
    voice "audio/voice/day3/o3-023.ogg"
    o "It can't be that simple."
    #show spr o3 neutral
    menu: 
        "Why not?": 
            pass 
    show spr o2 side frown
    voice "audio/voice/day3/o3-024.ogg"
    o "If it was that simple, then–"
    pause 1
    show spr o2 sad
    voice "audio/voice/day3/o3-025.ogg"
    o "I don't know why I'm bothering to argue."
    show spr o2 side frown
    voice "audio/voice/day3/o3-026.ogg"
    o "Why do I feel like I need to prove this to you?"
    menu: 
        "Are you sure it's me?": 
            pass 
    #show spr o3 shocked
    pause 3
    show spr o2 sad
    voice "audio/voice/day3/o3-027.ogg"
    o "No, no. Nope. No. "
    show spr o3 eyes closed 
    voice "audio/voice/day3/o3-028.ogg"
    o "I think that's enough for today."
    show spr o3 neutral 
    voice "audio/voice/day3/o3-029.ogg"
    o "Let's talk about anything else."
    pause 3
    show spr o1 eyes closed 
    voice "audio/voice/day3/o3-030.ogg"
    o "Sorry. I'll think of something."
    show spr o1 side nervous 
    voice "audio/voice/day3/o3-031.ogg"
    o "What, um, what else do you do? Besides programming-related things."
    #show spr o1 neutral 

    menu: 
        "Finding an excuse to get on my opsec again?":
            show spr o1 done 
            voice "audio/voice/day3/o3-032.ogg"
            o "I mean, if you answer with something identifiable–"
            menu:
                "I get it, I get it! Umm. Hm.": 
                    pass 
        "Well, well, well. Look who is caring now.":
            show spr o1 done
            voice "audio/voice/day3/o3-033.ogg"
            o "Hovering over the 'end call' button as we speak."
            menu: 
                "Fine, fine, I'll answer!": 
                    pass 

    pause 1

    menu: 
        "I like trying out the dumbest sounding burger or sandwich on restaurant menus.":
            show spr o1 neutral 
            voice "audio/voice/day3/o3-034.ogg"
            o "Dumbest name or composition?"
            menu: 
                "Whichever strikes me more. Sometimes I find one that's both.": 
                    pass 
            show spr o1 done 
            voice "audio/voice/day3/o3-035.ogg"
            o "Such as...?"
            menu: 
                "The Preposterous PB&J burger– as in peanut butter and jalapeño jelly.": 
                    pass 
            show spr o1 done frown 
            voice "audio/voice/day3/o3-036.ogg"
            o "That sounds...unpleasant."
            #show spr o1 neutral 
            menu: 
                "It wasn't the worst!": 
                    pass 
            show spr o1 smile
            voice "audio/voice/day3/o3-037.ogg"
            o "I'll take your word for it."
            show spr o1 eyes closed
            voice "audio/voice/day3/o3-038.ogg"
            o "Ugh. That's going to be stuck in my head now."
            menu: 
                "Sorry!":
                    pass 
            show spr o1 smile
            voice "audio/voice/day3/o3-039.ogg"
            o "I'll recover. Eventually."
            show spr o3 shocked 
            voice "audio/voice/day3/o3-040.ogg"
            o "...Is it strange that a sick part of me wants to try it?"
            #show spr o3 neutral 
        "I like browsing niche community forums and trying to sneak my way in. ":
            show spr o1 smile 
            voice "audio/voice/day3/o3-041.ogg"
            o "What, like on Reddit? "

            show spr o1 closed eye happy 
            voice "audio/voice/day3/o3-042.ogg"
            o "Hardly niche. "
            #show spr o1 smile 
            menu: 
                "No, no. I'm talkin' Facebook groups. ": 
                    pass 
            show spr o1 done frown
            voice "audio/voice/day3/o3-043.ogg"
            o "Huh? "
            menu: 
                "Like neighborhood groups I live at least a thousand miles away from. ": 
                    pass 
            show spr o1 mad 
            voice "audio/voice/day3/o3-044.ogg"
            o "What? Why? What is wrong with you? "
            menu: 
                "To taste the drama without being affected by it. ": 
                    pass 
            show spr o1 done frown 
            voice "audio/voice/day3/o3-045.ogg"
            o "Who likes chasing drama? "
            #show spr o1 side frown 
            show spr o3 silly 
            voice "audio/voice/day3/o3-046.ogg"
            o "But, I can't believe I'm curious now."
            #show spr o1 grin 
            voice "audio/voice/day3/o3-047.ogg"
            o "Am I missing out? Should I go seek out some suburban drama? "
            #show spr o1 smile 

    menu: 
        "You should. It's an acquired taste at first, but before you know it, {i}you'll be back.{/i}":
            pass
    #show spr o3 silly 
    pause 2
    show spr o1 done 
    voice "audio/voice/day3/o3-048.ogg"
    o "Was that you trying to do the Terminator?"
    menu: 
        "I know it's terrible! I know!":
            pass
    #show spr o1 eyes closed
    voice "audio/voice/day3/o3-049.ogg"
    o "That was the worst setup and impression I've ever heard."
    #show spr o1 smile 
    menu: 
        "You liked it. Look, here's another one–":
            pass
    show spr o3 shocked
    voice "audio/voice/day3/o3-050.ogg"
    o "Put the quotebook down! Now!"
    menu: 
        "...":
            pass
    voice "audio/voice/day3/o3-051.ogg"
    show spr o1 side nervous
    o "Look–"
    menu: 
        "That one was even worse!":
            pass
    show spr o1 mad 
    voice "audio/voice/day3/o3-052.ogg"
    o "Stop being so gleeful about it!"
    menu: 
        "It was so bad!":
            pass
    show spr o1 happy grin 
    voice "audio/voice/day3/o3-053.ogg"
    o "It was a lapse in judgment."
    voice "audio/voice/day3/o3-054.ogg"
    o "( laughing )"

    menu: 
        "I will remember this day forever.":
            show spr o1 grin 
            voice "audio/voice/day3/o3-055.ogg"
            o "Will you, really?"
            show spr o1 smile 
            menu: 
                "I can't account for every contingency. But I can try.": 
                    pass 
            show spr o1 closed eye happy 
            voice "audio/voice/day3/o3-056.ogg"
            o "I'll take that."
        "I like your laugh, by the way. ":
            show spr o3 silly 
            voice "audio/voice/day3/o3-057.ogg"
            o "Oh, my laugh? "
            show spr o1 side nervous
            voice "audio/voice/day3/o3-058.ogg"
            o "Um...thank you. Hm. "
            show spr o1 side smile 
            voice "audio/voice/day3/o3-059.ogg"
            o "I've been laughing quite a bit, haven't I? "
            menu: 
                "Sure have. ": 
                    pass 
            show spr o1 side nervous 
            voice "audio/voice/day3/o3-060.ogg"
            o "Ha...odd. "

    pause 2
    show spr o1 frown 
    voice "audio/voice/day3/o3-061.ogg"
    o "I like your laugh, I think."
    menu: 
        "You think???":
            pass
    show spr o1 eyes closed
    voice "audio/voice/day3/o3-062.ogg"
    o "Yeah... I think. "
    show spr frown
    voice "audio/voice/day3/o3-063.ogg"
    o "Laugh again."
    #show spr o1 smile
    menu: 
        "No, no, you have to earn that. Make me laugh. ":
            pass
    show spr o1 done
    voice "audio/voice/day3/o3-064.ogg"
    o "Never mind, shut up. "
    menu: 
        "( laugh )" :
            pass
    show spr o1 grin 
    voice "audio/voice/day3/o3-065.ogg"
    o "And now you laugh?? At me?? ( laughing )"
    show spr o1 side smile 
    voice "audio/voice/day3/o3-066.ogg"
    o "Unbelievable... "
    pause 1
    show spr o1 smile 
    menu: 
        "Can I ask just one thing about you?":
            pass
    show spr o1 neutral 
    voice "audio/voice/day3/o3-067.ogg"
    o "Sure. Shoot. "
    menu: 
        "What was your first programming language? ":
            pass
    voice "audio/voice/day3/o3-068.ogg"
    o "Why do you want to know that? "
    menu: 
        "No reason. Just curious. ":
            pass
    voice "audio/voice/day3/o3-069.ogg"
    o "It was Python. "
    
    show spr o1 eyes closed 
    voice "audio/voice/day3/o3-070.ogg"
    o "I was twelve and found a site dedicated to fun exercises using Python.  "

    show spr o1 neutral 
    voice "audio/voice/day3/o3-071.ogg"
    o "Snake games, Tower of Hanoi... silly things. "
    pause 2

    show spr o1 side frown 
    voice "audio/voice/day3/o3-072.ogg"
    o "I really liked that language. "
    menu: 
        "Do you not use it anymore?":
            pass
    show spr o3 eyes closed 
    voice "audio/voice/day3/o3-073.ogg"
    o "No, Python can't cover everything I need to do in this server. "
    show spr o3 neutral 
    voice "audio/voice/day3/o3-074.ogg"
    o "But it was beginner friendly. Really easy to read and understand, you know? "
    show spr o1 eyes closed 
    voice "audio/voice/day3/o3-075.ogg"
    o "I'm grateful I found that language first. "
    show spr o1 neutral 
    voice "audio/voice/day3/o3-076.ogg"
    o "Maybe I wouldn't have gotten into coding without it. "
    menu: 
        "So you do like coding. ":
            pass
    show spr o1 side smile 
    voice "audio/voice/day3/o3-077.ogg"
    o "Ha."
    show spr o1 happy
    voice "audio/voice/day3/o3-078.ogg"
    o "Maybe a little."
    #show spr o1 side smile 
    voice "audio/voice/day3/o3-079.ogg"
    o "You remember far too much of what I say. "
    pause 1
    show spr o1 side smile 
    voice "audio/voice/day3/o3-080.ogg"
    o "Thank you for talking with me, these past couple days. "
    voice "audio/voice/day3/o3-081.ogg"
    show spr o1 happy
    o "It's been nice. "
    menu: 
        "Can always talk for many more days, if you want.":
            pass
    show spr o1 closed eye happy
    voice "audio/voice/day3/o3-082.ogg"
    o "Cheeky. "
    show spr o1 happy
    voice "audio/voice/day3/o3-083.ogg"
    o "I don't know about that, Thrim."
    menu: 
        "Was worth a shot. ":
            pass
    show spr o1 side smile
    voice "audio/voice/day3/o3-084.ogg"
    o "Did you actually think it would work? "
    menu: 
        "Not really. But one can always hope. ":
            pass
    voice "audio/voice/day3/o3-085.ogg"
    show spr o1 closed eye happy
    o "Ha. "
    voice "audio/voice/day3/o3-086.ogg"
    show spr o1 neutral
    o "Anyway, it's late. About time for me to head out."
    voice "audio/voice/day3/o3-087.ogg"
    o "I presume you'll be on tomorrow?"
    menu: 
        "You know it.":
            pass
    show spr o1 eyes closed
    voice "audio/voice/day3/o3-088.ogg"
    o "See you then."

    ## must run these two lines to swap to next day 
    $ next_day_number = "4"
    jump day_swap

    $ renpy.pause(hard=True)