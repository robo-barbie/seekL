label day2_call: 
    show spr o1 smile
    voice "audio/voice/day2/o2-001.ogg"
    o "You know, now that I think about it I should be thanking you."

    play music "audio/music/little_hand_on_the_clock.mp3" loop fadein 2.0 fadeout 2.0 

    voice "audio/voice/day2/o2-002.ogg"
    o "By giving incri a reason to show off you gave them less room to be sloppy."
    menu: 
        "Are they...not good at hacking?":
            pass

    show spr o1 side neutral
    voice "audio/voice/day2/o2-003.ogg"
    o "I wouldn't say they're bad, but they're not the best either. "

    show spr o1 neutral
    voice "audio/voice/day2/o2-004.ogg"
    o "If they were really hopeless I would have booted them a while ago."
    menu: 
        "You vet newcomers by skill?":
            pass

    show spr o1 happy
    voice "audio/voice/day2/o2-005.ogg"
    o "More like by risk of exposure."

    show spr o1 smile
    voice "audio/voice/day2/o2-006.ogg"
    o "I try to be fair."
    menu: 
        "Glad I made the cut.":
            pass

    show spr o1 eyes closed
    voice "audio/voice/day2/o2-007.ogg"
    o "You did, though based on your programming choices I'm letting you stay with a raised eyebrow."

    show spr o1 done
    voice "audio/voice/day2/o2-008.ogg"
    o "Like really, why ArnoldC? Why any of the esoteric languages, actually?"
    menu: 
        "Well, I couldn't resist the opportunity to write something based on the Terminator himself.":
            pass
    voice "audio/voice/day2/o2-009.ogg"
    o "I think you could, actually."
    menu: 
        "No love for his movies?":
            pass

    show spr o1 eyes closed
    voice "audio/voice/day2/o2-010.ogg"
    o "I mean, yeah, but I don't like them enough to learn a language based on quotes."

    show spr o1 done
    voice "audio/voice/day2/o2-011.ogg"
    o "Are you really that big of a fan?"

    menu: 
        "Oh, absolutely. ":
            show spr o1 smile
            voice "audio/voice/day2/o2-012.ogg"
            o "I see. "
            menu:
                "But it's not really why I started using ArnoldC.":
                    pass
        "I mean I guess.":
            show spr o1 neutral
            voice "audio/voice/day2/o2-013.ogg"
            o "That's less enthusiastic than I expected." 
            voice "audio/voice/day2/o2-014.ogg"
            o "Why so dull about it? "
            menu: 
                "It's not really why I started using ArnoldC.":
                    pass
        "Not really, no. ":
            voice "audio/voice/day2/o2-015.ogg"
            o "Confusing, then. "

    menu: 
        "I just like picking up esoteric languages because it's fun, you know?":
            pass
    show spr o1 done
    voice "audio/voice/day2/o2-016.ogg"
    o "...Uh huh."
    show spr o3 neutral
    voice "audio/voice/day2/o2-017.ogg"
    o "Odd. "
    menu: 
        "Why odd?":
            pass
    show spr o2 side frown 
    voice "audio/voice/day2/o2-018.ogg"
    o "I don't know, just..."

    show spr o3 shocked
    voice "audio/voice/day2/o2-019.ogg"
    o "It's really just for the love of the game, huh?"
    show spr o3 neutral

    menu: 
        "Mhm. I like my little collection.":
            show spr o1 grin 
            voice "audio/voice/day2/o2-020.ogg"
            o "Your trophy case of ridiculous languages?"
            menu:
                "Wait, a real trophy case would actually be so cool.":
                    pass
            show spr o3 eyes closed
            voice "audio/voice/day2/o2-021.ogg"
            o "That was not meant to enable you."
            show spr o3 neutral
            menu:
                "Too late. I'm already looking up the ugliest wood trim display cases I can find.":
                    pass
        "You laugh now, but someday my expertise could come in handy.":
            show spr o1 closed eye grin
            voice "audio/voice/day2/o2-022.ogg"
            o "Really."
            menu:
                "Really really. ":
                    pass
            show spr o1 smile
            voice "audio/voice/day2/o2-023.ogg"
            o "Name one scenario."
            menu:
                "Um...uh...hm.":
                    pass
            show spr o3 silly 
            voice "audio/voice/day2/o2-024.ogg"
            o "Yeah?"
            menu:
                "When I think of a response to that tomorrow it'll be over for you.":
                    pass

    show spr o1 happy grin
    voice "audio/voice/day2/o2-025.ogg"                
    o "( laughs ) "

    show spr o1 smile
    voice "audio/voice/day2/o2-026.ogg"
    o "You really are just like this?"
    menu: 
        "What, fun?":
            pass

    show spr o1 side smile
    voice "audio/voice/day2/o2-027.ogg"
    o "Baffling."
    menu: 
        "Baffling?!":
            pass

    show spr o1 neutral
    voice "audio/voice/day2/o2-028.ogg"
    o "Yeah. The way you find fun in stuff like that."

    show spr o1 side nervous
    voice "audio/voice/day2/o2-029.ogg"
    o "That's not meant as an insult, I really am just confused."
    show spr o1 neutral
    menu: 
        "You don't have fun coding?":
            pass

    show spr o1 side neutral 
    voice "audio/voice/day2/o2-030.ogg"
    o "At this point, it's just a means to an end. Same as most things."
    show spr o1 neutral 
    menu: 
        "Then what do you do for fun?":
            pass

    show spr o1 closed eye happy
    voice "audio/voice/day2/o2-031.ogg"
    o "Call strange people who don't care about privacy."
    menu: 
        "Ha. Just that, though?":
            pass
    pause 2
    show spr o2 side frown
    voice "audio/voice/day2/o2-032.ogg"
    o "Don't really do much besides this anymore."


    menu:
        "That sounds...a little lonely.":
            show spr o2 sad 
            voice "audio/voice/day2/o2-033.ogg"
            o "Maybe. Sure. "
            show spr o3 eyes closed
            voice "audio/voice/day2/o2-034.ogg"
            o "Little consequence now, however."
        "Oh, uh. Sounds like a very peaceful life. ":
            show spr o1 side neutral
            voice "audio/voice/day2/o2-035.ogg"
            o "Say what you mean, ha. I get it. "
            show spr o1 eyes closed
            voice "audio/voice/day2/o2-036.ogg"
            o "But it doesn't matter anymore. "

    show spr o1 neutral 
    voice "audio/voice/day2/o2-037.ogg"
    o "Needing to have fun isn't important to my life anymore. "

    show spr o1 eyes closed 
    voice "audio/voice/day2/o2-038.ogg"
    o "And, we'll be saying our goodbyes soon anyway."

    show spr o1 neutral 
    voice "audio/voice/day2/o2-039.ogg"
    o "So don't worry about it."
    menu: 
        "...What is your 'end', exactly?":
            pass

    show spr o1 side neutral 
    voice "audio/voice/day2/o2-040.ogg"
    o "Simple."
    show spr o1 neutral 
    voice "audio/voice/day2/o2-041.ogg"
    o "I'm going to go entirely off the grid soon. "

    show spr o1 neutral 
    voice "audio/voice/day2/o2-042.ogg"
    o "I take a cut from the others' hacks, and between their hacks and my own I've built a fund for supplies."

    show spr o3 neutral parted
    voice "audio/voice/day2/o2-043.ogg"
    o "As soon as I shutter the server I'll do one last supply run and make my exit from society."
    show spr o1 neutral 
    
    
    menu:
        "What're you gonna buy? ":
            show spr o1 eyes closed
            voice "audio/voice/day2/o2-044.ogg"
            o "I have most of the food I need, so... probably just last minute things. "
            show spr o1 neutral 
            voice "audio/voice/day2/o2-045.ogg"
            o "A jacket or two, some medical supplies, the works. "
            voice "audio/voice/day2/o2-046.ogg"
            show spr o3 neutral
            o "Then I'm out, as soon as possible. "
        "Wait, what? Why?!":
            show spr o1 side smile
            voice "audio/voice/day2/o2-047.ogg"
            o "Think I'm crazy? "
            show spr o1 neutral
            menu:
                "No, I'm just confused.":
                    pass
            show spr o3 neutral
            voice "audio/voice/day2/o2-048.ogg"
            o "I mean, I don't think it's hard to understand. "

    show spr o1 side neutral 
    voice "audio/voice/day2/o2-049.ogg"
    o "I don't have any reasons to stay. I'm just-- tired. Of everything. "


    menu:
        "You're fed up with people?":
            show spr o1 eyes closed
            voice "audio/voice/day2/o2-050.ogg"
            o "No, there's no real frustration on my end. Just apathy."
            voice "audio/voice/day2/o2-051.ogg"
            show spr o1 neutral 
            o "Everyone I thought I cared about are simply not people in my life anymore. All for random, dull reasons. Nothing dramatic. "
            show spr o2 sad
            voice "audio/voice/day2/o2-052.ogg"
            o "I just woke up one day and realized I was alone."
            show spr o3 eyes closed
            voice "audio/voice/day2/o2-053.ogg"
            o "So, without those connections there's nothing to hold me here."
        "No reasons? Nothing makes you happy here?":
            show spr o3 neutral
            voice "audio/voice/day2/o2-054.ogg"
            o "Not for a long time."
            show spr o1 neutral 
            voice "audio/voice/day2/o2-055.ogg"
            o "I don't feel much of anything, really. It is what it is. "


    menu: 
        "That's...":
            pass
    
    show spr o1 side neutral
    voice "audio/voice/day2/o2-056.ogg"
    o "Don't say it."
    show spr o1 neutral 
    voice "audio/voice/day2/o2-057.ogg"
    o "Sorry, I've just already heard this before. It won't change my mind."
    show spr o1 eyes closed
    voice "audio/voice/day2/o2-058.ogg"
    o "We just met. And we'll be strangers again soon enough."
    show spr o1 neutral 
    voice "audio/voice/day2/o2-059.ogg"
    o "So, not to be cold, but... you know. "
    menu: 
        "...You have a point.":
            pass
    show spr o1 eyes closed
    voice "audio/voice/day2/o2-060.ogg"
    o "Yep."
    show spr o3 neutral 
    voice "audio/voice/day2/o2-061.ogg"
    o "And with that I think that's enough for today."
    menu: 
        "Alright.":
            pass
    show spr o3 neutral parted
    voice "audio/voice/day2/o2-062.ogg"
    o "We, ah."
    show spr o1 smile
    voice "audio/voice/day2/o2-063.ogg"
    o "We can call again if the opportunity arises."
    show spr o1 neutral


    menu:
        "I'd like that.":
            show spr o1 smile
            voice "audio/voice/day2/o2-064.ogg"
            o "I'll try to come up with a more engaging topic next time."
            menu: 
                "Is that a promise?":
                    pass
            show spr o1 side smile
            voice "audio/voice/day2/o2-065.ogg"
            o "I said I'll try."
            menu: 
                "Haha!": 
                    pass
        "Yeah. Sounds good.":
            pass 

    show spr o1 grin
    voice "audio/voice/day2/o2-066.ogg"
    o "Catch you later, then."
    #"You too."


    ## must run these two lines to swap to next day 
    $ next_day_number = "3"
    jump day_swap

    $ renpy.pause(hard=True)