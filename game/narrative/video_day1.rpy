label day1_call: 

    voice "audio/voice/day1/o1-001.ogg"
    o "There we are."

    play music "audio/music/little_hand_on_the_clock.mp3" loop fadein 2.0 fadeout 2.0 

    menu: 
        "You know, for someone concerned by security this is kind of a weird move.": 
            pass 

    voice "audio/voice/day1/o1-002.ogg"
    o "What, the call?"

    show spr o1 eyes closed 
    voice "audio/voice/day1/o1-003.ogg"
    o "This is more secure than the server, and that's already locked tight."
    #show spr o1 neutral 
    menu: 
        "Your lack of concern unnerves me.": 
            pass

    show spr o1 frown
    voice "audio/voice/day1/o1-004.ogg"
    o "I'm not afraid of a quick call like this. And the little risk is worth sussing out a larger one."

    menu: 
        "Am I looking like a larger risk?": 
            pass 

    show spr o1 neutral 
    voice "audio/voice/day1/o1-005.ogg"
    o "Unknown."

    menu: 
        "I'm not one to blab about my less than legal doings.": 
            pass

    show spr o1 done
    voice "audio/voice/day1/o1-006.ogg"
    o "I see."
    #show spr o1 neutral 

    menu: 
        "So…?": 
            pass 

    show spr o1 done
    voice "audio/voice/day1/o1-007.ogg"
    o "So nothing. This was just to see who you are."
    #show spr o1 neutral 

    menu: 
        "Maybe I should have dressed up nicer, then.":

            show spr o1 mad 
            voice "audio/voice/day1/o1-008.ogg"
            o "This isn't a job interview."

            menu:
                "True, but \"dress to impress\" still holds.": 
                    pass

            show spr o1 done
            voice "audio/voice/day1/o1-009.ogg"
            o "It might do you good to set more attainable goals."
            #show spr o1 neutral 

        "What's your read? Dangerous? Useful? Alluring?":
            $ points_seekLove += 2

            show spr o1 done frown 
            voice "audio/voice/day1/o1-010.ogg"
            o "One of those was distinctly different."

            menu: 
                "I have to assess all possibilities.": 
                    pass

            show spr o1 done 
            voice "audio/voice/day1/o1-011.ogg"
            o "Note the root word \"possible\"."
            #show spr o1 neutral 


    menu:
        "Oh, ouch. Noted.":
            pass

    show spr o1 eyes closed 
    voice "audio/voice/day1/o1-012.ogg"
    o "...I'm sorry. This call wasn't to insult you."

    show spr o1 neutral
    voice "audio/voice/day1/o1-013.ogg"
    o "I was looking more to hear about your methods. How you work."

    menu: 
        "I, uh. You can't laugh at this.": 
            pass 

    show spr o1 frown 
    voice "audio/voice/day1/o1-014.ogg"
    o "Very promising."

    menu: 
        "I actually mostly program with esoteric languages.": 
            pass

    show spr o1 done
    voice "audio/voice/day1/o1-015.ogg"
    o "Esoteric... I don't know what that means." 

    show spr o3 neutral parted 
    voice "audio/voice/day1/o1-016.ogg"
    o "Searching." 
    show spr o3 neutral

    pause 2 

    show spr o3 neutral parted
    voice "audio/voice/day1/o1-017.ogg"
    o "Is this a joke?"
    #show spr o1 neutral

    menu: 
        "I'm being completely serious.": 
            pass 

    show spr o3 shocked 
    voice "audio/voice/day1/o1-018.ogg"
    o "...\"designed to test the boundaries of computer programming language design, as a proof of concept, as software art, as a hacking interface to another language, or as a joke.\""

    show spr o1 closed eye happy  
    voice "audio/voice/day1/o1-019.ogg"
    o "\"Software art.\" Ha. Funny."

    show spr o1 happy
    voice "audio/voice/day1/o1-020.ogg"
    o "Which reason is it for you?" 

    menu: 
        "...It will become obvious when I say the language I use.": 
            pass 

    show spr o1 neutral 
    voice "audio/voice/day1/o1-021.ogg"
    o "Which is...?" 

    menu: 
        "ArnoldC, lately.": 
            pass 

    show spr o1 done
    voice "audio/voice/day1/o1-022.ogg"
    o "What's special about it?" 


    menu: 
        "...It's built around the one liners of Arnold Schwarzenegger.": 
            pass 
    
    pause 1

    show spr o1 closed eye grin
    voice "audio/voice/day1/o1-023.ogg"
    o "Oh, my god."
    show spr o1 happy

    menu: 
        "No laughing. This is serious stuff.": 
            show spr o1 happy
            voice "audio/voice/day1/o1-024.ogg"
            o "I'm not– a little. But I'm more fascinated than anything. Really?" 
            menu: 
                "Yes!": 
                    pass 
        "I know. Advanced. Intimidated yet?": 
            $ points_seekLove += 2
            show spr o1 happy
            voice "audio/voice/day1/o1-025.ogg"
            o "A little. Moreso because of how freely you admitted to this." 
            voice "audio/voice/day1/o1-026.ogg"
            o "How did you of all people find this server again? " 
            menu: 
                "I'm, like, the best at ArnoldC. ": 
                    pass 
            voice "audio/voice/day1/o1-027.ogg"
            o "Uh-huh." 

    show spr o1 happy grin
    voice "audio/voice/day1/o1-028.ogg"
    o "This is going to be interesting watching you interact with everyone else."
    show spr o1 happy
    menu: 
        "Well now I'm nervous.": 
            pass 

    show spr o1 eyes closed
    voice "audio/voice/day1/o1-029.ogg"
    o "Don't be."

    menu: 
        "I'll try. ":
            $ points_seekLove += 2

            show spr o1 neutral
            voice "audio/voice/day1/o1-030.ogg"
            o "Good enough. Just keep doing that."

        "The others don't exactly help.": 

            voice "audio/voice/day1/o1-031.ogg"
            o "That's how they are. Don't pay them much mind."

    # end choices

    #show spr o2 side frown 
    show spr o3 neutral 
    voice "audio/voice/day1/o1-032.ogg"
    o "And with that, we're good. I'll see you around on the server."
    #show spr o3 neutral
    menu: 
        "That was short. Does that mean you trust me now?": 
            pass 
    
    #show spr o3 eyes closed
    voice "audio/voice/day1/o1-033.ogg"
    o "Enough to keep you around."
    #show spr o3 neutral 
    voice "audio/voice/day1/o1-034.ogg"
    o "See you later."

    menu: 
        "See you.": 
            pass

    ## must run these two lines to swap to next day 
    $ next_day_number = "2"
    jump day_swap
