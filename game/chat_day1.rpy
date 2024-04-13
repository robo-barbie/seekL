

label day1_start: 
    #jump day1_30
    #$ $ chat_message("odxny: testing testing")

    #$ chat_message("incri: and then i beat him to death with hammers")

    $ chat_message("SYSTEM: THRIM joined")

    pause 1 

    $ chat_message("incri: who the fuck", ot="elimf, wnpep")

    $ chat_message("elimf: ?????????? ", ot="wnpep")

    $ chat_message("elimf: who is this lol ", ot="wnpep, incri")

    $ chat_message("wnpep: speak please ................")


    # [1] MC: uhhhh, hi! sorry! i'm not sure what this is

    $ player_choice(
        [
            ("uhhhh, hi! sorry! i'm not sure what this is", "day1_1"), 
            ("hello", "day1_2")
        ]
    )

label day1_1: 
    $ chat_message("incri: fed ")

    $ chat_message("incri: fucking fed ")

    $ chat_message("incri: od needs 2 log on ", ot="elimf")

    $ chat_message("elimf: lol imagine a fed infiltrating with a \"uhhhh, hi! sorry!\" ")

    $ chat_message("elimf: no way this is a fed ", ot="wnpep")

    $ chat_message("wnpep: that's exactly why they'd do it that way ")

    pause 1 

    $ chat_message("elimf: oh shit ")

    jump day1_3


    # [2] MC: hello 
label day1_2: 
    $ chat_message("wnpep: speak more things please", ot="elimf")

    $ chat_message("elimf: hello ", ot="incri")

    $ chat_message("incri: UR SOOOOO SUS DUDE ",fastmode=True)

    $ chat_message("elimf: could be not a dude ",ot="incri")

    $ chat_message("incri: lick my hole ")

    $ chat_message("elimf: oh my! ")

    jump day1_3

label day1_3: 
    # end choices 

    $ chat_message("wnpep: but don't worry. i checked them out")

    $ chat_message("wnpep: this person is not a threat of any kind ")

    $ chat_message("wnpep: ...to anyone ")

    $ chat_message("elimf: lolllll ")

    $ player_choice(
        [
            ("you...... checked?", "x")
        ]
    )

    $ chat_message("wnpep: maybe they are a threat to themself actually. in an existential way ")

    $ chat_message("incri: they're calling u a idiot")

    $ chat_message("wnpep: no i'm not ", ot="incri")

    $ chat_message("incri: idiot vibes so far definnitely ")

    $ chat_message("elimf: very silly vibes", ot="wnpep")

    $ chat_message("wnpep: do you like the life you lead, thrim? ")

    $ player_choice(
        [
            ("what the hell are you looking at??", "day1_4"), 
            ("you're bluffing. i'm super secure", "day1_5")
        ]
    )

    # [1] MC: what the hell are you looking at?? 
label day1_4:

    $ chat_message("wnpep: does it matter? it's all the same dull boring nonsense ")

    $ chat_message("wnpep: you should aim higher. i think you can do better ")

    $ chat_message("elimf: i found them too ")

    $ chat_message("incri: this isnt wort hh the effort ")

    $ chat_message("incri: where is od")

    $ chat_message("incri: od come kick them. boring ass ")

    jump day1_6


    # [2] MC: you're bluffing. i'm super secure 
label day1_5: 

    $ chat_message("wnpep: what haha because you're on a vpn or something")

    $ chat_message("elimf: looolllllllllll easiest shit to get around. i love vpn ads ")

    $ chat_message("elimf: really good for our business ")

    # MC: ... i'm more secure than that. 
    $ player_choice(
        [
            ("... i'm more secure than that.", "x"), 
        ]
    )

    $ chat_message("wnpep: uh huh! :] ")

    jump day1_6
    

    # end choices
label day1_6:

    $ chat_message("incri: wnpep run the thing on their shit ")

    $ chat_message("elimf: lol \"welcome new person, now give us all of your savings\" ")

    $ player_choice(
        [
            ("ok, sure, take my whole ten american dollars", "day1_7"), 
            ("please don't do that. ", "day1_8")
        ]
    )

    # [1] MC: ok, sure, take my whole ten american dollars 
label day1_7: 

    $ chat_message("elimf: are they lying wn")

    $ chat_message("wnpep: you know. i don't think they are ")

    $ chat_message("elimf: well now i feel mean.")

    $ chat_message("incri: who fcking cares $10 is $10 run the fcommand ")

    jump day1_9


    # [2] MC: please don't do that. 
label day1_8:

    $ chat_message("incri: give us a funny reason not to ")

    $ chat_message("elimf: nah this is lame ")

    $ chat_message("elimf: we have better things to do today than like ")

    $ chat_message("elimf: ruin a random life ")

    $ chat_message("wnpep: i'm not draining anything, don't worry ")

    jump day1_9

    # end choices 
label day1_9: 

    $ chat_message("wnpep: inc please shut up a bit, in the kindest way possible ")

    $ chat_message("incri: this chat fckin g blows ")

    $ chat_message("elimf: log off then lol")

    $ chat_message("incri: ud like that wouldnt u")

    $ chat_message("elimf: bro")

    $ chat_message("wnpep: well at any rate youre here now. tools are on the right")

    $ chat_message("elimf: wdym incris right there")

    $ chat_message("incri: ..I...")

    $ chat_message("elimf: is that u flipping me off")

    $ chat_message("elimf: do u have six fingers")

    $ chat_message("incri: uggghhgh")

    # SEEKL SEGMENT 

    # MC: so how does this all work? 
    $ player_choice(
        [
            ("so how does this all work? ", "x"), 
        ]
    )

    $ chat_message("wnpep: do you know SQL? ")

    $ player_choice(
        [
            ("yes", "day1_10"), 
            ("no", "day1_11")
        ]
    )

    # [1] MC: yes 
label day1_10: 

    $ chat_message("wnpep: then you've got a great head start champ ")

    $ chat_message("wnpep: but, don't think it can do all that SQL can. it's pretty limited ")

    jump day1_12

    # [2] MC: no 
label day1_11: 

    $ chat_message("wnpep: no issue. it's not a hard language to pick up") 

    $ chat_message("wnpep: if you find it difficult...")

    $ chat_message("elimf: concerning")

    jump day1_12

    # end choices 
label day1_12:

    $ chat_message("wnpep: we can access a plethora of databases from a variety of companies/government agencies in here ")

    $ chat_message("wnpep: how this works is there's a giant backend program constantly breaking into them and copying different tables of data over into a massive warehouse ")

    $ chat_message("wnpep: and that's what the interface you work with here will run on. does that make sense so far? ")

    $ player_choice(
        [
            ("yeah, simple ", "day1_13"), 
            ("not really...", "day1_14")
        ]
    )

    # [1] MC: yeah, simple 
label day1_13:

    $ chat_message("elimf: phew ")

    jump day1_15

    # [2] MC: not really...
label day1_14:

    $ chat_message("elimf: lollllllllllll")

    $ chat_message("wnpep: hm. well. maybe an example will help ")

    jump day1_15

    # end choices 
label day1_15: 

    $ chat_message("wnpep: go ahead and type this into console on the top right ")

    $ chat_message("wnpep: `select * \nfrom glowparkzoo.inc_0V67`")

    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = None 
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["glowparkzoo.inc_0V67"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = None 
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 

    $ player_choice(
        [
            ("ok, one moment", "day1_18"), 
            ("why is that so long and ugly...", "day1_17")
        ]
    )

# [1] MC: ok, one moment 

# [2] MC: why is that so long and ugly... 
label day1_17:

    $ chat_message("elimf: JUST LIKE MY EX", ot="incri") 

    $ chat_message("incri: JUST LIKE MY EX", fastmode=True)

    $ chat_message("elimf: i fucking beat you") 

    $ chat_message("incri: no way ur message is under mine",ot="wnpep") 

    $ chat_message("wnpep: elimf's came up first.") 

    $ chat_message("elimf: AHAHAHAHAHA") 

    $ chat_message("incri: FUCKING",fastmode=True,ot="wnpep") 

    $ chat_message("wnpep: sorry.") 

    jump day1_18

label day1_18:
    # wait for input 
    $ player_is_waiting = True 
    $ waiting_label = "day1_19"

    # if they arrive already ready to pass 
    if player_can_pass:
        $ player_is_waiting = False 
        jump day1_19 
    $ renpy.pause(hard=True)

label day1_19: 
    $ player_is_waiting = False 
    
    # MC: done 
    $ player_choice(
        [
            ("done", "x"), 
        ]
    )

    $ chat_message("wnpep: okay, so. what you see here is a small table recording negative behavior from an animal at a zoo ") 

    $ chat_message("wnpep: only 5 records will ever be shown, so that's why you don't see all of the incidents ") 

    $ chat_message("wnpep: the table should show some columns like incident_no_0v67 -- 0v67 is the animal's id number, and incident_no is the uh incident number") 

    $ chat_message("wnpep: you can see the times these things happened, how bad it was, and if any notes were left by the staff ") 

    # MC: this doesn't say what the animal did though? 
    $ player_choice(
        [
            ("this doesn't say what the animal did though?", "x"), 
        ]
    )

    $ chat_message("wnpep: no. it doesnt ") 

    $ chat_message("wnpep: the data isn't perfect. you'll run into that a lot ") 

    # MC: can i see a list of all the tables we have access to? 
    $ player_choice(
        [
            ("can i see a list of all the tables we have access to?", "x"), 
        ]
    )

    $ chat_message("elimf: no. we actually can't ", ot="wnpep") 

    $ chat_message("wnpep: only odxny has that level of access ") 

    $ chat_message("wnpep: but with some hard work, we manage. it's just about knowing where to look. ") 

    $ chat_message("wnpep: for example, if i tell you there's another animal with bad behavior at the zoo with an id of X77S, what would you run? ") 

    $ player_choice(
        [
            ("easy. i can do this", "day1_20"), 
            ("no idea tbh", "day1_21")
        ]
    )

    # [1] MC: easy. i can do this 
label day1_20: 

    $ chat_message("wnpep: go on then thrim")

    jump day1_24

    #[2] MC: no idea tbh  
label day1_21: 

    $ chat_message("elimf: ur doing amazing ", ot="wnpep")

    $ chat_message("wnpep: look at the name of the table. see the animal's id in there? ")
    
    $ player_choice(
        [
            ("oh, i get it now", "day1_22"), 
            ("???????", "day1_23")
        ]
    )

    #[2-A] MC: oh, i get it now 
label day1_22:

    $ chat_message("wnpep: okay! try to run something then thrim ")

    jump day1_24

    #[2-B] MC: ??????? 
label day1_23: 

    $ chat_message("incri: just give them the fufcking table i can't stand this")

    $ chat_message("wnpep: haha. oh boy ")

    $ chat_message("wnpep: `select * from glowparkzoo.inc_X77S`")
    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = None 
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["glowparkzoo.inc_X77S"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = None 
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 

    $ chat_message("wnpep: notice the end of the table name has changed ")

    $ chat_message("wnpep: try running that ")

    $ chat_message("elimf: is this how much hand massaging ur gonna need lol ")

    $ chat_message("wnpep: ?? hand what? ")

    $ chat_message("elimf: like how did you even figure out where we were ",fastmode=True)

    # MC: fuck you 
    $ player_choice(
        [
            ("fuck you", "x")
        ]
    )

    $ chat_message("incri: fuck you ")

    $ chat_message("wnpep: oh you meant hand holding",fastmode=True)

    $ chat_message("elimf: fuck you harder ")

    $ chat_message("incri: prmise? ")

    $ chat_message("wnpep: stop please ")

    $ chat_message("elimf: ok ")

    $ chat_message("wnpep: let me know when you've run that thrim ")

    jump day1_24 


    # end choices 
label day1_24: 

    # MC: my name isn't thrim. idk why my user was set to that 
    $ player_choice(
        [
            ("my name isn't thrim. idk why my user was set to that", "x")
        ]
    )

    $ chat_message("elimf: it's randomized when u join")

    # MC: ohhhh 
    $ player_choice(
        [
            ("ohhhh", "x")
        ]
    )

    $ chat_message("wnpep: code please")

    jump day1_25 

    # wait for the code to be executed 
label day1_25:
    # wait for input 
    $ player_is_waiting = True 
    $ waiting_label = "day1_26"

    # if they arrive already ready to pass 
    if player_can_pass:
        $ player_is_waiting = False 
        jump day1_26 
    $ renpy.pause(hard=True)

label day1_26: 
    $ player_is_waiting = False 

    # MC: i see. this one barely had any problems at all 
    $ player_choice(
        [
            ("i see. this one barely had any problems at all ", "x")
        ]
    )

    $ chat_message("wnpep: yes! not a very interesting table ")

    $ chat_message("wnpep: anyway, that's some of the basics")

    # odxny online

    $ chat_message("SYSTEM: ODXNY online")

    $ chat_message("elimf: sup big cheese")

    $ chat_message("wnpep: got someone new while you were gone")

    $ chat_message("odxny: Did you check on them?")

    $ chat_message("wnpep: yeah i'm sure ur already checking but i didnt see anything to worry about")

    $ chat_message("incri: ban them",fastmode=True)

    pause 1 

    $ chat_message("odxny: For?")

    $ chat_message("incri: boring")

    $ chat_message("incri: annoying")

    $ chat_message("incri: dumbass")

    $ chat_message("wnpep: you're going to need better reasons")

    $ chat_message("incri: what so we jst let randos in here??? ")

    $ chat_message("elimf: you were a rando once ")

    $ chat_message("elimf: unfortunately we do now know you ")

    $ chat_message("odxny: I'll be doing my own vetting, unrelated to being a boring annoying dumbass.")

    $ chat_message("odxny: Thrim, let's arrange a brief call just to verify.")

    $ chat_message("odxny: Won't pry beyond what's necessary.")

    # MC: i dont mind abt privacy stuff. call whenever
    $ player_choice(
        [
            ("i dont mind abt privacy stuff. call whenever", "x")
        ]
    )

    $ chat_message("odxny: .")

    pause 2

    $ chat_message("wnpep: HUH")

    $ chat_message("odxny: LMAO",fastmode=True)

    $ chat_message("wnpep: thats a new one",fastmode=True)

    $ chat_message("incri: do u see now")

    $ chat_message("odxny: That's hilarious actually")

    $ chat_message("incri: theyll drag us down with them",fastmode=True)

    $ chat_message("odxny: Nah")

    $ chat_message("odxny: I'll take care of this")

    # MC: um?
    $ player_choice(
        [
            ("um?", "x")
        ]
    )

    $ chat_message("odxny: Let's take your word for it and call now.")

    $ chat_message("odxny: Unless that was just bluster")

    $ player_choice(
        [
            ("UH", "day1_27"), 
            ("like i said, anytime. hit me up", "day1_28")
        ]
    )

    # [1] MC: UH
label day1_27: 

    $ chat_message("odxny: Hmmm")

    # MC: NO I'LL DO IT
    $ player_choice(
        [
            ("NO I'LL DO IT", "x")
        ]
    )

    jump day1_29

    # [2] MC: like i said, anytime. hit me up
label day1_28: 

    $ chat_message("odxny: Well then.")

    $ chat_message("odxny: I was expecting to call your bluff.")

    # MC: i will never back down
    $ player_choice(
        [
            ("i will never back down", "x")
        ]
    )

    jump day1_29 

    # end choices
label day1_29: 

    $ chat_message("odxny: Interesting resolve")

    $ chat_message("wnpep: or foolish")

    $ chat_message("odxny: We'll see.")

    jump day1_30 
    
    
    
    # CALL

label day1_30: 

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
        "No laughing! This is serious stuff!": 
            pass 

    show spr open smile_open 
    odxny "I'm not– a little. But I'm more fascinated than anything. Really?" 
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


    $ renpy.pause(hard=True)

