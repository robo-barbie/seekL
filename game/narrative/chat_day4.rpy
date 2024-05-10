

label day4_start: 

    play music "audio/music/server_room.mp3" loop fadein 2.0 fadeout 2.0 

    $ chat_message("wnpep: hmm")

    $ chat_message("elimf: ?")

    $ chat_message("wnpep: no response yet")

    $ chat_message("odxny: I'm sure it'll come soon. There's no way their legal team wasn't up all night.")

    $ chat_message("wnpep: ha. true")

    $ player_choice(
        [
            ("think theyll cave?", "day4_1"), 
            ("thats a plus in a way- u know youre making em sweat", "day4_2")
        ]
    )

    # [1] MC: think theyll cave?
label day4_1: 

    $ chat_message("wnpep: unlikely")

    $ chat_message("wnpep: w the funding they have theyll try to weasel or threaten their way out first")

    $ chat_message("odxny: Probably a mix of both.")

    jump day4_3 


    # [2] MC: thats a plus in a way- u know youre making em sweat
label day4_2: 

    $ chat_message("wnpep: i do enjoy knowing that im racking up billable hours for them")

    $ chat_message("odxny: Not to mention the overtime.")

    $ chat_message("wnpep: nearly enough to make up for what theyre doing")

    jump day4_3 


    # end choices
label day4_3: 

    $ chat_message("wnpep: if only it made the wait any less mindnumbing")

    $ chat_message("elimf: we can always play a game in the meantime")

    $ chat_message("incri: bet all ur money on it")

    $ chat_message("incri: ill kick ur ass at any game")

    $ chat_message("wnpep: a promising start")

    $ chat_message("elimf: bold claim inc :^)")

    $ chat_message("incri: do it")

    $ chat_message("incri: coward")

    pause 0.5

    $ chat_message("SYSTEM: RESPONSE - ITSSSBAELEY - We will not be cowed by threats of extortion. Cease and desist, or expect a followup from law enforcement.")

    $ chat_message("elimf: poor timing incri for today the cowards feast")

    $ chat_message("wnpep: youre not getting a cut elimf")

    $ chat_message("elimf: aww")

    $ chat_message("odxny: Looks like you'll have to work for your dinner, pep.")

    $ chat_message("wnpep: not fussed about it. i expected pushback")

    $ chat_message("wnpep: so let's just hit send on this")

    pause 0.5

    $ chat_message("SYSTEM: EXTORTION SENT -- ITSSSBAELEY@BAVER.NET")

    $ chat_message("odxny: Just took a look. Nice play.")

    $ chat_message("wnpep: theyll likely try to pry us open first. bit more of a well funded op than bruce")

    $ chat_message("odxny: Fair point, I'll put something up just in case.")

    pause 1.0

    $ chat_message("SYSTEM: SUPPLEMENTARY DEFENSES ENABLED")
    $ defenses = True 

    # $ player_choice(
    #     [
    #         ("what just happened??", "x")
    #     ]
    # )

    # $ chat_message("odxny: They're pissed lol. They're trying to attack us back.")

    $ chat_message("elimf: \"supplmentary defenses\" what is this the military")

    $ chat_message("incri: elimf in US")

    $ chat_message("elimf: ???")

    $ chat_message("odxny: You can come up with fun names when you make your own server.")

    $ chat_message("elimf: could u be swayed by ANTI-HACK ARMOR or TURBOSHIELD")

    $ chat_message("odxny: No.")

    $ chat_message("elimf: MAGIC FUCKOFF WALL")

    $ chat_message("incri: i like tha t one")

    pause 1.0

    $ chat_message("SYSTEM: RESPONSE - ITSSSBAELEY - We will transfer the funds per the stated agreement. Consider this matter closed.")

    play chat "audio/sfx/Casino_Jackpot_001.ogg" loop fadeout 0.2

    # make it rain money??  
    show money_rain onlayer screens

    pause 0.5

    $ chat_message("SYSTEM: PAYMENT PLAN INITIATED FOR - $ 1 , 000 , 000")

    $ chat_message("wnpep: there we go")

    $ chat_message("odxny: Nice job, pep.")

    pause 0.2

    hide money_rain onlayer screens with Dissolve(0.5)
    stop chat fadeout 0.5

    pause 0.5 

    $ defenses = False
    $ defenses_off = True 

    pause 0.5

    $ chat_message("SYSTEM: SUPPLEMENTARY DEFENSES DISABLED")
    

    $ chat_message("incri: i want a cut")

    $ chat_message("wnpep: youre not getting a cut either inc")

    $ chat_message("incri: bullsht")

    $ chat_message("incri: i trained thrim who helped u")

    $ chat_message("odxny: Bit of a stretch.")

    $ chat_message("incri: cmonnn")

    $ chat_message("elimf:  well")
    $ defenses_off = False 

    $ chat_message("elimf: its my turn to finish up huh")

    $ chat_message("odxny: You do need to get a move on at some point.")

    $ chat_message("wnpep: theres still time for a respectable third place")

    $ chat_message("elimf: still on the podium, sick")

    $ chat_message("incri: thats what losers who dnt get gold say")

    $ chat_message("elimf: i was busy")

    $ chat_message("incri: getting too too hgih to move doesnt count")

    $ chat_message("elimf: ok look")

    $ chat_message("wnpep: thisll be good")

    $ chat_message("elimf: i have vowed to stay sober until my hack is done")

    $ chat_message("odxny: Very admirable.")

    $ chat_message("wnpep: and when did you last partake again")

    $ chat_message("elimf: thats not important")

    $ chat_message("elimf: i will henceforth eschew the devils lettuce until it is done")

    $ chat_message("elimf: so sayeth me-eth")

    $ chat_message("incri: is this what ur like hwen u dont smoke")

    $ chat_message("incri: i hate it")

    $ chat_message("elimf: ur not being helpful about my sobriety")

    $ chat_message("wnpep: unrelated i have started a countdown clock")

    $ chat_message("elimf: et tu pep")

    $ chat_message("wnpep: dont worry i wont be around to collect")

    $ chat_message("wnpep: taking my daughter out as promised")

    $ chat_message("elimf: booo")

    $ chat_message("elimf: what am i gonna do then")

    $ chat_message("wnpep: teach thrim something? everyone else is")

    $ chat_message("elimf: im not a mentor type")

    $ player_choice(
        [
            ("why not kick incri's ass at teaching?", "day4_4"), 
            ("no pressure tho!", "day4_5")
        ]
    )


    # [1] MC: why not kick incri's ass at teaching?
label day4_4: 

    $ chat_message("elimf: ohohoho")

    $ chat_message("incri: u fckn wiishhhhh")

    $ chat_message("elimf: this gets more tempting by the second")

    jump day4_6


    # [2] MC: no pressure tho!
label day4_5: 

    $ chat_message("elimf: this feels like pressure")

    # MC: i'm being sincere!!!
    $ player_choice(
        [
            ("i'm being sincere!!!", "x")
        ]
    )

    $ chat_message("elimf: hmmmmmmmm")

    jump day4_6


    # end choices
label day4_6:

    $ chat_message("wnpep: consider getting to also use thrim for free labor")

    $ chat_message("elimf: compelling compelling")

    # MC: i never get a break do i
    $ player_choice(
        [
            ("wait. not like that", "x")
        ]
    )

    $ chat_message("elimf: dont worry abt pep")

    $ chat_message("elimf: on another note ")

    $ chat_message("elimf: wanna learn some more seekL today")

    # MC: i knew it
    $ player_choice(
        [
            ("i knew it", "x")
        ]
    )

    $ chat_message("wnpep: guess we'll have you paying dues until the last")

    $ chat_message("odxny: Elimf teaching? This should be good.")

    $ chat_message("elimf: dw im sober today thisll be cake")

    $ chat_message("elimf: if you trust me less than incri on this i may just have to hang up the towel")

    # MC: ok fair
    $ player_choice(
        [
            ("i trust you. slightly more", "x")
        ]
    )


    $ chat_message("incri: wht did i do to deserve this")

    $ chat_message("elimf: uhhhhhhhhhhhhhhhhh")

    $ chat_message("wnpep: id love to put up a list but i really do have to go now")

    $ chat_message("incri: COWARD")

    $ chat_message("odxny: Later, pep.")

    $ chat_message("wnpep: good luck thrim")

    # MC: uhh thanks!
    $ player_choice(
        [
            ("uhh thanks!", "x")
        ]
    )

    $ chat_message("elimf: trust in me pep")

    pause 0.5

    $ chat_message("SYSTEM: WNPEP offline")

    $ chat_message("elimf: this is gonna go great")

    $ chat_message("odxny: Should probably elaborate on what \"this\" is.")

    $ chat_message("elimf: ah yes of course")


    ## seekl segment 

    $ chat_message("elimf: today we ")

    $ chat_message("elimf: brave the dank stinky waters ")

    $ chat_message("elimf: of the past ")

    $ chat_message("odxny: Interesting.")

    $ player_choice(
        [
            ("your past? ", "day4_7"), 
            ("why not the future ", "day4_8")
        ]
    )


    # [1] MC: your past? 
label day4_7: 

    $ chat_message("elimf: who knows ")

    jump day4_9 


    # [2] MC: why not the future 
label day4_8: 

    $ chat_message("elimf: god ")

    $ chat_message("elimf: one step at a time pls ")

    jump day4_9 


    # end choices
label day4_9: 

    $ chat_message("incri: where")

    $ chat_message("elimf: we must find one very stupid, stupid stupid boy")

    $ chat_message("elimf: are u ready to be useful again thrim ")

    $ player_choice(
        [
            ("i don't really want to do this", "day4_10"), 
            ("absolutely captain!", "day4_11")
        ]
    )


    # [1] MC: i don't really want to do this 
label day4_10: 

    $ chat_message("elimf: 2 bad ahaaaaa")

    $ chat_message("incri: get to fkcn work ")

    # MC: y'all are so mean to me 
    $ player_choice(
        [
            ("y'all are so mean to me", "x")
        ]
    )

    $ chat_message("incri: wa wa wa wa wa ")

    jump day4_12 


    # [2] MC: absolutely captain! 
label day4_11: 

    $ chat_message("elimf: oooooooo! ")

    $ chat_message("odxny: Who's captain? ")

    $ chat_message("incri: neither of u r qualfied ")

    $ chat_message("odxny: Aw")

    $ chat_message("elimf: i think ur qualified to be capt od ")

    $ chat_message("elimf: but i'm the captain ")

    $ chat_message("odxny: Unsure about that. ")

    jump day4_12 


    # end choices
label day4_12:

    $ chat_message("elimf: ok, now. listen up children ")

    $ chat_message("elimf: there was once a young boy with a freckled face")

    $ chat_message("elimf: who disappeared from earth without a trace")

    $ chat_message("incri: stop that ")

    $ chat_message("elimf: despite a long hunt")

    $ chat_message("elimf: which wasn't that fun ")

    $ chat_message("elimf: the mystery continues to be annoying ")

    $ chat_message("odxny: That's not a rhyme. ")

    $ chat_message("elimf: what ")

    $ chat_message("elimf: i wasn't rhyming ")

    $ chat_message("odxny: What ")

    $ chat_message("elimf: thrim, go look in #irs.contacts# for {color="+color_help+"}\"Darren Horton\"{/color}")
    pause 0.2
    $ hack_notes.append("name: \nDarren Horton")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("INFO TAB UPDATED")
    pause 0.5
    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = None
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["irs.contacts"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = [("irs_id", "I23066-809")]
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day4_13"

    $ chat_message("elimf: u will. understand ")

    # MC: ....ok 
    $ player_choice(
        [
            ("....ok", "x")
        ]
    )

    jump wait_start

    # wait for code 


label day4_13: 
    # MC: why is it all \"NULL\"? 
    $ player_choice(
        [
            ("why is it all \"NULL\"? ", "x")
        ]
    )
    pause 0.2
    $ hack_notes.append("contact info: \nmissing")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("INFO TAB UPDATED")
    pause 0.5

    $ chat_message("odxny: It is?? ")

    $ chat_message("odxny: That shouldn't be possible. ")

    $ chat_message("elimf: ALAS ")

    $ chat_message("elimf: WE WANDER STILL THROUGH THE FOG... ")

    $ chat_message("incri: oh m y god shut th fck up ")

    $ chat_message("incri: did you check the death tables?? ")

    $ chat_message("elimf: ofc i checked the death tables fuckass ")

    $ chat_message("incri: doubt ")

    $ chat_message("odxny: If they were in the death tables, they'd still be in the contact tables.")

    $ chat_message("odxny: They must have had the record wiped somehow.")

    # MC: death tables?? 
    $ player_choice(
        [
            ("death tables??", "x")
        ]
    )

    $ chat_message("odxny: There's a lot of IRS data in here right now. Including some death data.")

    $ chat_message("odxny: Why don't you check it out if ur curious? {color="+color_help+"}Search up \"Darren Horton\" in {/color}#irs.death#")
    pause 0.5
    $ tables_seen.append("irs.death")
    play sound "audio/sfx/message_notification_01_002 new table.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_table_pos
    $ renpy.notify("TABLE LIST UPDATED")

    $ chat_message("elimf: YET YOU WILL FIND NO RECORD...")

    $ chat_message("odxny: Lmao. ")

    # MC: if there's no record... where is this guy? 
    $ player_choice(
        [
            ("idk. maybe later", "day4_14"), 
            ("if there's no record... where is this guy?", "day4_15")
        ]
    )


label day4_14: 

    $ chat_message("incri: fkin lazy")

    $ chat_message("odxny: I mean. If elimf already checked...")

    $ chat_message("incri: FKIN LAZY")

    jump day4_16 


label day4_15: 

    $ chat_message("elimf: i know not...")

    $ chat_message("elimf: but hunt on... we must hunt on...")

    jump day4_16 


label day4_16:

    $ chat_message("odxny: Do you remember anything else about him? ")

    $ chat_message("elimf: i've never claimed to member this person at all ")

    $ chat_message("elimf: they are simply ")

    $ chat_message("elimf: the past ")

    $ chat_message("incri: i'm not reading this sht rn ")

    pause 0.5

    $ chat_message("SYSTEM: INCRI offline")

    $ chat_message("elimf: wow")

    $ chat_message("odxny: Ignore them, let's focus. ")

    $ chat_message("elimf: pushy pushy ")

    $ chat_message("elimf: what's the rush ")

    $ chat_message("odxny: Ha ha. ")

    $ player_choice(
        [
            ("that eager to get this all over with, huh?", "day4_17"), 
            ("listen to the boss elimf", "day4_18")
        ]
    )


    # [1] MC: that eager to get this all over with, huh? 
label day4_17: 

    $ chat_message("odxny: It's not like that. ")

    # MC: oh? 
    $ player_choice(
        [
            ("oh?", "x")
        ]
    )

    $ chat_message("odxny: And it's not like that either. ")

    $ chat_message("elimf: like what")

    $ chat_message("odxny: Nothing ")

    jump day4_19 



    # [2] MC: listen to the boss elimf
label day4_18: 

    $ chat_message("elimf: wow ")

    $ chat_message("elimf: demanding ")

    pause 2

    $ chat_message("elimf: be demanding again")

    $ chat_message("odxny: Focus. ")

    $ chat_message("elimf: omg ")

    $ chat_message("elimf: i'm feelin something ")

    $ chat_message("odxny: No you aren't. ")

    $ chat_message("elimf: LOL ")

    jump day4_19 



    # end choices
label day4_19: 

    $ chat_message("elimf: now ")

    $ chat_message("elimf: there is another fact i know about him")

    $ chat_message("elimf: he was in the foster system ")

    $ chat_message("elimf: and methinks we may be able to ")

    $ chat_message("elimf: get at hi m there ")

    $ chat_message("elimf: #txgov.foster_parents#")
    pause 0.5
    $ tables_seen.append("txgov.foster_parents")
    play sound "audio/sfx/message_notification_01_002 new table.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_table_pos
    $ renpy.notify("TABLE LIST UPDATED")

    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = ["email"]
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["irs.contacts"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = [("irs_id", "I85863-307")]
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day4_23"

    $ chat_message("odxny: Not Arizona? ")

    $ chat_message("elimf: yeah no i live in t")

    pause 2 

    $ chat_message("elimf: ahhhahahahahahaha")

    $ chat_message("elimf: AHAHAHAAHAHHAHAAAAA HAAAA")

    $ chat_message("elimf: GRRRAAAAAUUUUUGGGGHHHHHHHHHHHHHHHH")

    $ chat_message("odxny: o ")

    $ chat_message("elimf: RRRRRAAAAAUUUUUGGGHGHGHGHHHGHHHGHGHGHHHHHHHHHH")

    $ player_choice(
        [
            ("normal texan behavior ", "day4_20"), 
            ("tf r you doing ", "day4_21")
        ]
    )


    # [1] MC: normal texan behavior 
label day4_20: 

    $ chat_message("odxny: LMAO ")

    $ chat_message("elimf: I\"M GONNAAAAAAAAA GGGGRRRARUAUAUAUUAUUGHGGHHHHHHGHH")

    $ chat_message("elimf: RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")

    jump day4_odm_1 


    # [2] MC: tf r you doing 
label day4_21: 

    $ chat_message("elimf: THE FUTILITY OF EVERYTHING ")

    $ chat_message("elimf: EVERYTHIGN WE HOLD DEAR")

    $ chat_message("elimf: VANISHES ")

    $ chat_message("elimf: DESPITE HOW WE ")

    $ chat_message("elimf: MADLY GR IP ")

    pause 1 

    # MC: what 
    $ player_choice(
        [
            ("what", "x")
        ]
    )

    jump day4_odm_1 

label day4_odm_1: 

    $ chat_message("odxny: Well this is turning out to be a ride.", c="admin")

    $ chat_message("odxny: elimf was only half this obnoxious for their other hacks.", c="admin")

    #MC: looks like this is smth personal for them
    $ player_choice(
        [
            ("looks like this is smth personal for them", "x")
        ]
    )

    $ chat_message("odxny: Most likely. The trend of vengeance hacks seems to be continuing as well.", c="admin")

    $ player_choice(
        [
            ("is your last hack also going to be a revenge thing?", "day4_odm_2"), 
            ("did you guys all get into hacking for personal reasons?", "day4_odm_3")
        ]
    )


    #[1] MC: is your last hack also going to be a revenge thing?
label day4_odm_2: 

    $ chat_message("odxny: No, nothing like that lmao.", c="admin")

    $ chat_message("odxny: I'm sure I'll get booed for being the combo breaker.", c="admin")

    jump day4_odm_4


    #[2] MC: did you guys all get into hacking for personal reasons?
label day4_odm_3:

    $ chat_message("odxny: I don't know everyone else's reasons. I could guess if I had to think about it.", c="admin")

    $ chat_message("odxny: Incri's seems the most transparent- petty vengeance, possibly boredom.", c="admin")

    jump day4_odm_4


    # end choices
label day4_odm_4: 

    #MC: what are your reasons for getting into hacking then?
    $ player_choice(
        [
            ("what are your reasons for getting into hacking then?", "x")
        ]
    )

    $ chat_message("odxny: Oh. That.", c="admin")

    $ chat_message("odxny: I found some hacking forums early in my programming days, and just kind of fell into it.", c="admin")

    $ chat_message("odxny: It was mostly just exercises and hackathons. Then it proved useful for the fund.", c="admin")

    #MC: That's practical.
    $ player_choice(
        [
            ("That's practical.", "x")
        ]
    )

    $ chat_message("odxny: And unsurprising, I imagine.", c="admin")

    $ chat_message("odxny: Let’s get back to it. Without us elimf’s going to go careening off a cliff.", c="admin")

    jump day4_22



    # end choices
label day4_22: 

    pause 2 

    $ chat_message("elimf: ok i'm back in human form")

    $ chat_message("odxny: Thank god. ")

    $ chat_message("elimf: please {color="+color_help+"}take a look in the foster table for our foster child{/color} ")

    $ chat_message("elimf: and {color="+color_help+"}charter to me the email for the parent{/color}... please.... from our favorite contact table....") 

    $ chat_message("odxny: You could tackle this with either {color="+color_help+"}a join or a where clause{/color}. Up to you.")

    $ chat_message("elimf: GO") 

    # wait for code

    jump wait_start 


label day4_23: 

    # MC: I've got it -- kenneth.stafford@copmail.com, fostered Darren in 2002 
    $ player_choice(
        [
            ("I've got it -- kenneth.stafford@copmail.com, fostered Darren in 2002", "x")
        ]
    )
    pause 0.2
    $ hack_notes.append("foster parent: \nKenneth Stafford")
    $ hack_notes.append("foster email: \nkenneth.stafford\n@copmail.com")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("INFO TAB UPDATED")
    pause 0.5

    $ chat_message("odxny: Targeting a lot of law enforcement lately.")

    # MC: is that a bad thing? 
    $ player_choice(
        [
            ("is that a bad thing?", "x")
        ]
    )

    $ chat_message("odxny: No.... but it does put more eyes on us. ")

    # MC: oh. that's probably not good 
    $ player_choice(
        [
            ("oh. that's probably not good", "x")
        ]
    )

    $ chat_message("elimf: dw we're almost done w all this anyway right ")

    $ chat_message("odxny: True. ")

    $ chat_message("elimf: ok time to GET ")

    $ chat_message("elimf: SOME INFO ")

    pause 0.5

    $ chat_message("SYSTEM: EXTORTION SENT - KENNETH.STAFFORD@COPMAIL.COM ")

    $ chat_message("elimf: OHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH ")

    pause 0.5

    $ chat_message("SYSTEM: EXTORTION BOUNCE - BAD CONTACT ")

    $ chat_message("elimf: WHAT ")

    $ chat_message("elimf: MSUJGHUIHUOH???? ")

    $ chat_message("odxny: ....Not used to the IRS data being this wrong. ")

    $ chat_message("odxny: Are you sure that was the right email, thrim? ")

    $ player_choice(
        [
            ("that was the only email there", "day4_24"), 
            ("i mean... i'm not sure. i think that was it ", "day4_25")
        ]
    )


    #$ [1] MC: that was the only email there 
label day4_24: 

    $ chat_message("odxny: I see.") 

    jump day4_26


    # [2] MC: i mean... i'm not sure. i think that was it 
label day4_25: 

    $ chat_message("odxny: Hm.") 
    
    jump day4_26


    # end choices 
label day4_26:

    # MC: maybe they're dead...? 
    $ player_choice(
        [
            ("maybe they're dead...?", "x")
        ]
    )

    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = ["full_name"]
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["irs.death"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = [("d_no", "D68141-771")]
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day4_27"

    $ chat_message("odxny: Kenneth? ")

    $ chat_message("odxny: Worth a check, I suppose. ")

    $ chat_message("elimf: devastating if real..... ")

    $ chat_message("elimf: thrim... can u.... {color="+color_help+"}please check for kenneth{/color}.... ")

    $ chat_message("elimf: #irs.death#.......... ")

    # MC: lol ok 
    $ player_choice(
        [
            ("lol ok", "x")
        ]
    )

    jump wait_start 
    

    # wait for code 


label day4_27:
    pause 0.2
    $ hack_notes.append("kenneth status: \ndead af")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("INFO TAB UPDATED")
    pause 0.5

    # MC: .......... uh. Kenneth is in here. 
    $ player_choice(
        [
            (".......... uh. Kenneth is in here.", "day4_28"), 
            ("good news! kenneth lives", "day4_29")
        ]
    )


label day4_28: 

    pause 1 

    $ chat_message("elimf: please picture me fa llen on my delicate hands and knee s")

    $ chat_message("elimf: a tear dripping to the floor ")

    jump day4_30 


label day4_29: 

    $ chat_message("odxny: ?? That's not...")

    $ chat_message("elimf: oh WHEW")

    $ chat_message("elimf: okay, i can breathe again")

    $ player_choice(
        [
            ("lives in the afterlife", "x")
        ]
    )

    pause 1 

    $ chat_message("elimf: HUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU")

    $ chat_message("odxny: Clever.")

    jump day4_30



label day4_30: 

    # MC: but there is a living contact listed here. Elsie Patrick
    $ player_choice(
        [
            ("but there is a living contact listed here. Elsie Patrick", "x")
        ]
    )
    pause 0.2
    $ hack_notes.append("death contact: \nElsie Patrick")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("INFO TAB UPDATED")
    pause 0.5

    $ chat_message("elimf: ALIVE")

    pause 2 

    $ chat_message("elimf: FUCK I HITMY HEAD ")

    $ chat_message("odxny: LMAO")

    pause 0.5

    $ chat_message("SYSTEM: INCRI online") 

    $ chat_message("incri: i sense sum1 getting ownd ")

    $ chat_message("incri: who ")

    $ chat_message("odxny: elimf for sure ")

    $ chat_message("incri: good ")

    $ chat_message("elimf: cease")

    $ chat_message("elimf: thrim")

    $ chat_message("elimf: {color="+color_help+"}pls go get me the email for that contact{/color}")
    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = ["email"]
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["irs.contacts"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = [("irs_id", "I73094-157")]
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day4_31"

    $ chat_message("incri: lol thrim ur still fetching for this idiot ")

    $ chat_message("odxny: Thrim is very helpful, you know.")

    $ chat_message("incri: cringe")

    $ chat_message("elimf: pls thrim. {color="+color_help+"}pls find me elsie patrick's email{/color}")

    # wait for code 

    jump wait_start 


label day4_31: 

    # MC: here you go -- elsie.patrick@copmail.com
    $ player_choice(
        [
            ("here you go -- elsie.patrick@copmail.com", "x")
        ]
    )

    pause 0.2
    $ hack_notes.append("elsie email: \nelsie.patrick\n@copmail.com")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("INFO TAB UPDATED")
    pause 0.5

    $ chat_message("odxny: Still another cop. ")

    $ chat_message("elimf: hey at lesast the last one was dead ")

    $ chat_message("incri: dead cops???? ")

    $ chat_message("odxny: We did NOT kill a cop. ")

    $ chat_message("incri: tf ")

    $ chat_message("elimf: EMAIL TIME ")

    $ chat_message("elimf: OHHHHHHHHHHHHHHHHH")

    pause 0.5

    $ chat_message("SYSTEM: EXTORTION SENT - ELSIE.PATRICK@COPMAIL.COM ")

    # MC: are u actually like extorting all these people lol 
    $ player_choice(
        [
            ("are u actually like extorting all these people lol ", "x")
        ]
    )

    $ chat_message("elimf: no no no")

    $ chat_message("elimf: it just sends that whenever we send emails out from this service lol ")

    $ chat_message("elimf: u wanna try sending something though? ")

    # MC: oh? 
    $ player_choice(
        [
            ("oh? ", "x")
        ]
    )

    $ chat_message("elimf: run this in ur console ")

    $ chat_message("elimf: `exec out('elsie.patrick@copmail.com')`")
    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # IF EXEC, WHAT NEEDS TO BE EXEC 
        exec_needed = ["out", "elsie.patrick@copmail.com"]
        exec_condition = ["day4_32", "day4_33"]
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = None 
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = None
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = None
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day4_32"

        # make it jump this time to a diff new label depending on if you sent it to the right email or not 

    pause 0.2
    $ hack_notes.append("new function: \nout('email')")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("INFO TAB UPDATED")
    pause 0.5

    $ func_access_email = True 

    $ chat_message("odxny: ...Granted you access to the function, Thrim.")

    $ chat_message("elimf: {color="+color_syntax+"}EXEC{/color} runs a specific pre-built function, and that function we are running today is called \"out\"")

    $ chat_message("elimf: this function just sends like. a default scary message to w/e email u put in there")

    $ chat_message("odxny: I feel like an additional message will lessen the impact of whatever you just sent. ")

    $ chat_message("elimf: i think it will enhance it ")

    $ player_choice(
        [
            ("if od thinks it's a bad idea tho... ", "day4_31_A"), 
            ("dw od. ur overthinking", "day4_31_B")
        ]
    )


label day4_31_A: 

    $ chat_message("odxny: I mean, you can...idk. It's up to elimf. Their hack.")

    $ chat_message("elimf: ty. ur probs right but. LMAO")

    $ chat_message("odxny: Lmao")

    $ chat_message("elimf: {color="+color_help+"}ship it thrimmy{/color}")

    jump wait_start


label day4_31_B: 

    $ chat_message("odxny: k")

    $ chat_message("elimf: go on thrim {color="+color_help+"}SHIP IT OUT{/color}")

    # wait for code 

    jump wait_start


label day4_32: 

    $ chat_message("odxny: Crazy lmao ")

    $ chat_message("incri: ur a part of ths now")

    $ chat_message("incri: blackmailer ")

    # MC: omg does this mean u accept me 
    $ player_choice(
        [
            ("omg does this mean u accept me ", "x")
        ]
    )

    $ chat_message("incri: u wish ")

    jump day4_34 


label day4_33: 

    $ chat_message("odxny: Wait what was that email?")

    $ chat_message("incri: LMAO??? THRIM???")

    $ chat_message("elimf: omg thrim what have u done")

    # MC: I THOUGHT YOU SAID IT WAS JUST A GENERIC EMAIL 
    $ player_choice(
        [
            ("I THOUGHT YOU SAID IT WAS JUST A GENERIC EMAIL", "x")
        ]
    )

    $ chat_message("elimf: a very SCARY generic email")

    $ chat_message("incri: HAHAHAHAHAHA")

    $ chat_message("odxny: Thrim...")

    jump day4_34 


label day4_34: 

    pause 0.5

    $ chat_message("SYSTEM: RESPONSE - ELSIE.PATRICK - ??? I've never heard of Darren. Kenneth didn't foster anyone. Go away. ")

    $ chat_message("elimf: LIAR U ARE LYINGGGG LIAR LIAR ")

    $ chat_message("elimf: TIME TO PULL OUT THE BIG GUNS ")

    # MC: ? 
    $ player_choice(
        [
            ("?", "x")
        ]
    )

    $ chat_message("elimf: the email archive") 

    $ chat_message("odxny: Ohhhhh")

    # MC: what's the email archive 
    $ player_choice(
        [
            ("what's the email archive?", "x")
        ]
    )

    $ chat_message("odxny: Sometimes we get short windows of access into huge databases full of emails sent and received ")

    $ chat_message("odxny: We use that to skim and grab as many emails as we can but ")

    $ chat_message("odxny: It's a little limited. ")

    $ chat_message("elimf: welcome to the glorious world of #emails.content#")
    pause 0.5
    $ tables_seen.append("emails.content")
    play sound "audio/sfx/message_notification_01_002 new table.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_table_pos
    $ renpy.notify("TABLE LIST UPDATED")
    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        exec_needed = None 
        required_runs["columns"] = None
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["emails.content"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = [("email_id", "X66352")]
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day4_35"

    $ chat_message("elimf: i sniff luck tonight ")

    $ chat_message("elimf: search thrim search ")

    $ chat_message("elimf: {color="+color_help+"}search for elsie's email in there!!!!!!{/color}")

    $ chat_message("odxny: {color="+color_help+"}The email column isn't named email this time{/color}, so you won't be able to join. Use a {color="+color_syntax+"}WHERE{/color} alone instead.")

    $ chat_message("odxny: Just a heads up. Sorry.")

    $ chat_message("odxny: This table got fucked up somehow in the scanning.")

    # wait for code 

    jump wait_start


label day4_35: 

    $ chat_message("odxny: LMAO how are you so lucky eli")

    
    $ player_choice(
        [
            ("lucky how??", "day4_36"), 
            ("u see this too lol?", "day4_37")
        ]
    )


label day4_36: 

    $ chat_message("odxny: Look at the content column lol ")

    jump day4_38 


label day4_37: 

    $ chat_message("odxny: Yeah lol. ")

    $ chat_message("odxny: So fucking stupid lol ")

    jump day4_38 

 
label day4_38: 

    $ chat_message("elimf: YES? ")

    $ chat_message("odxny: Lot of emails with subject \"RE: DARREN HORTON\" ")

    $ chat_message("elimf: AND? ")

    $ chat_message("odxny: You wanna give it thrim? ")

    $ player_choice(
        [
            ("oh no, go for it!", "day4_39"), 
            ("if u don't mind", "day4_40")
        ]
    )


    # [1] MC: oh no, go for it! 
label day4_39: 

    $ chat_message("odxny: Thanks.")

    # MC: having fun, huh?
    $ player_choice(
        [
            ("having fun, huh?", "x")
        ]
    )

    $ chat_message("odxny: You're funny. ") 

    $ chat_message("odxny: It's \"fdhj398fh@notmail.com\" ") 

    jump day4_41


    # [2] MC: if u don't mind
label day4_40: 

    $ chat_message("odxny: Stage is yours. ") 

    # MC: "fdhj398fh@notmail.com" 
    $ player_choice(
        [
            ("\"fdhj398fh@notmail.com\"", "x")
        ]
    )

    jump day4_41


    # end choices 
label day4_41: 
    pause 0.2
    $ hack_notes.append("darren email: \nfdhj398fh\n@notmail.com")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("INFO TAB UPDATED")
    pause 0.5

    pause 2 

    $ chat_message("elimf: all this time... he's been hiding away from the world...") 

    $ chat_message("elimf: this young boy... ifnally found... god bless... god bless.... ")

    $ chat_message("odxny: And you said don't know this person? ")

    $ chat_message("elimf: well i know of ")

    $ chat_message("elimf: something he once was ")

    $ chat_message("elimf: a youth in a park ")

    $ chat_message("elimf: smiling ")

    $ chat_message("elimf: brimming with ")

    $ chat_message("elimf: hope ")

    $ chat_message("incri: gonna log off agn i swear 2 gd ")

    $ chat_message("elimf: a young youth who ")

    $ chat_message("elimf: who happened to lose ")

    $ chat_message("elimf: a bet ")

    $ chat_message("elimf: and this bet had ")

    $ chat_message("elimf: INTEREST ATTACHED")

    $ chat_message("incri: wait LMAO")

    $ chat_message("elimf: AND THOUGH HE'S BEEN TRYING TO HIDE ")

    $ chat_message("elimf: HE CANNOT HIDE FROM THE ALL-SEEING EYE OF ")

    $ chat_message("elimf: PETTY GREED ")

    pause 0.5

    $ chat_message("SYSTEM: EXTORTION SENT - FDHJ398FH@NOTMAIL.COM ")

    $ player_choice(
        [
            ("omg did you just extort someone over a childhood bet", "day4_42"), 
            ("they were in hiding??? from you?????", "day4_43")
        ]
    )

    
    # [1] MC: omg did you just extort someone over a childhood bet 
label day4_42: 

    $ chat_message("elimf: THEY CAN RUN BUT THEY CANT HIDE ")

    $ chat_message("odxny: I see friendship meant a lot to you.") 

    $ chat_message("elimf: we are nothing without our principles ")

    $ chat_message("elimf: god where tf is wnpep when i need them ")

    jump day4_44 


    # [2] MC: they were in hiding??? from you????? 
label day4_43: 

    $ chat_message("elimf: a waste of time i AGREE ")

    $ chat_message("elimf: this was inevitable ")

    $ chat_message("incri: holy shit letsGOOOOOOOOOOOOOOO")

    $ chat_message("incri: FUCKIN G SICK END ELI ")

    $ chat_message("elimf: thank u inc <3 ")

    jump day4_44 


    # end choices 
label day4_44: 

    pause 0.5

    $ chat_message("SYSTEM: WNPEP online")

    $ chat_message("wnpep: alright! i'm back! ")

    $ chat_message("wnpep: how'd it go? ")

    # MC: um. elimf had a productive extortion 
    $ player_choice(
        [
            ("um. elimf had a productive extortion ", "x")
        ]
    )

    $ chat_message("elimf: i'm so zen rn ")

    $ chat_message("elimf: i'm gonna. make bank")

    pause 1.0

    $ chat_message("SYSTEM: RESPONSE - Fine. Fuck you. I fucking hate you. I'm gonna fucking find you you sack of rank shit. Take your fucking money. I'm tired of dealing with you. ")

    $ chat_message("elimf: WOOOOOOO ")

    $ chat_message("wnpep: what the fuck ")

    play chat "audio/sfx/Casino_Jackpot_001.ogg" loop fadeout 0.2

    # make it rain money??  
    show money_rain onlayer screens

    pause 0.5

    $ chat_message("SYSTEM: PAYMENT PLAN INITIATED FOR - $ 1 , 253 , 390 ")

    $ chat_message("incri: TF IS THAT ALL INTEREST??? ")

    $ chat_message("elimf: i am ")

    $ chat_message("elimf: the best at making deals ")

    pause 0.2

    hide money_rain onlayer screens with Dissolve(0.5)
    stop chat fadeout 0.5

    pause 0.5 

    $ chat_message("wnpep: holy crap ")

    $ chat_message("odxny: Cut? ")

    $ chat_message("elimf: shit u can have lke")

    $ chat_message("elimf: half of it ")

    $ chat_message("odxny: Are you sure?? ")

    $ chat_message("elimf: dude th moral victory was like. the most important thing ")

    $ chat_message("elimf: thank u thrim. couldn't have done this without you. ")

    # MC: ur welcome????? omg
    $ player_choice(
        [
            ("ur welcome????? omg", "x")
        ]
    )


    $ chat_message("elimf: excellent")

    $ chat_message("elimf: this calls for a victory bowl")

    $ chat_message("wnpep: couldnt handle one day of sobriety?")

    $ chat_message("elimf: this was just me riding a different high")

    $ chat_message("elimf: of righteous vengeance")

    $ chat_message("elimf: of IMMINENT VICTORY")

    $ chat_message("wnpep: alright alright")

    $ chat_message("odxny: I'd say you've earned your bowl.")

    $ chat_message("elimf: damn right")

    # MC: what a texan thing to say
    $ player_choice(
        [
            ("what a texan thing to say", "x")
        ]
    )

    $ chat_message("elimf: UUUUUUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA") 

    pause 0.5

    $ chat_message("SYSTEM: ELIMF offline")

    $ chat_message("wnpep: ???????")

    $ chat_message("odxny: Don't worry about it.")

    $ chat_message("odxny: Are you up for a call right now?",c="admin")

    # MC: o sure, go ahead
    $ player_choice(
        [
            ("o sure, go ahead", "x")
        ]
    )

    ## call time 
    jump go_to_call

    $ renpy.pause(hard=True)
