label day1_call: 

    $ in_call = True 

    show bg odxny_bg
    show spr odxny_1 
    show fade_lower
    show fg odxny_fg onlayer screens
    hide screen seekL_ui 

    odxny "There we are."

    menu: 
        "You know, for someone concerned by security this is kind of a weird move.": 
            pass 

    odxny "What, the call?"

    show spr closed neutral_open 
    odxny "This is more secure than the server, and that's already locked tight."
    show spr neutral 
    menu: 
        "Your lack of concern unnerves me.": 
            pass

    show spr open frown
    odxny "I'm not afraid of a quick call like this. And the little risk is worth sussing out a larger one."

    menu: 
        "Am I looking like a larger risk?": 
            pass 

    show spr neutral 
    odxny "Unknown."

    menu: 
        "I'm not one to blab about my less than legal doings.": 
            pass

    show spr neutral_open 
    odxny "I see."
    show spr neutral 

    menu: 
        "So…?": 
            pass 

    show spr neutral_open
    odxny "So nothing. This was just to see who you are."
    show spr neutral 

    menu: 
        "Maybe I should have dressed up nicer, then.":

            show spr mad 
            odxny "This isn't a job interview."

            menu:
                "True, but \"dress to impress\" still holds.": 
                    pass

            show spr done neutral_open 
            odxny "It might do you good to set more attainable goals."
            show spr neutral 

        "What's your read? Dangerous? Useful? Alluring?":

            show spr done frown 
            odxny "One of those was distinctly different."

            menu: 
                "I have to assess all possibilities.": 
                    pass

            show spr done neutral_open 
            odxny "Note the root word \"possible\"."
            show spr neutral 


    menu:
        "Oh, ouch. Noted.":
            pass

    show spr closed neutral 
    odxny "...I'm sorry. This call wasn't to insult you."

    show spr open neutral_open 
    odxny "I was looking more to hear about your methods. How you work."
    show spr neutral 

    menu: 
        "I, uh. You can't laugh at this.": 
            pass 

    show spr frown 
    odxny "Very promising."

    menu: 
        "I actually mostly program with esoteric languages.": 
            pass

    show spr done neutral_open 
    odxny "Esoteric... I don't know what that means." 

    show spr odxny_3 open parted 
    odxny "Searching." 
    show spr neutral  

    pause 2 

    show spr parted
    odxny "Is this a joke?"
    show spr neutral

    menu: 
        "I'm being completely serious.": 
            pass 

    show spr shocked neutral_open 
    odxny "...\"designed to test the boundaries of computer programming language design, as a proof of concept, as software art, as a hacking interface to another language, or as a joke.\""

    show spr odxny_1 closed smile_open  
    odxny "\"Software art.\" Ha. Funny."

    show spr open smile
    odxny "Which reason is it for you?" 

    menu: 
        "...It will become obvious when I say the language I use.": 
            pass 

    show spr neutral_open 
    odxny "Which is...?" 
    show spr neutral 

    menu: 
        "ArnoldC, lately.": 
            pass 

    show spr neutral_open 
    odxny "What's special about it?" 
    show spr neutral 

    menu: 
        "...It's built around the one liners of Arnold Schwarzenegger.": 
            pass 
    
    pause 1

    show spr closed smile_open 
    odxny "Oh, my god."

    menu: 
        "No laughing. This is serious stuff.": 
            show spr open smile_open 
            odxny "I'm not– a little. But I'm more fascinated than anything. Really?" 
            show spr smile 
            menu: 
                "Yes!": 
                    pass 
        "I know. Advanced. Intimidated yet?": 
            show spr open smile_open 
            odxny "A little. Moreso because of how freely you admitted to this." 
            show spr smile 
            menu: 
                "Yes!": 
                    pass 

    show spr smile_open_big 
    odxny "This is going to be interesting watching you interact with everyone else."
    show spr smile 
    menu: 
        "Well now I'm nervous.": 
            pass 

    show spr closed neutral 
    odxny "Don't be."

    menu: 
        "I'll try. ":

            show spr open 
            odxny "Good enough. Just keep doing that."

        "The others don't exactly help.": 

            show spr open 
            odxny "That's how they are. Don't pay them much mind."

    # end choices

    show spr odxny_3 open parted 
    odxny "And with that, we're good. I'll see you around on the server."
    show spr neutral 
    menu: 
        "That was short. Does that mean you trust me now?": 
            pass 
    
    show spr closed neutral_open 
    odxny "Enough to keep you around."
    show spr open parted 
    odxny "See you later."
    show spr neutral 

    menu: 
        "See you.": 
            pass

    # end day

    pause  

    jump day2_start


    $ renpy.pause(hard=True)