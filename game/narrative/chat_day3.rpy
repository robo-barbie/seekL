
## INSERT SIDE WORD GAME WITH ODXNY STARTING THIS DAY 

label day3_start: 

    #play music "audio/music/server_room_chiller_version.mp3" loop fadein 2.0 fadeout 2.0 
    play music "audio/music/cracking_the_code.mp3" loop fadein 2.0 fadeout 2.0 

    $ chat_message("elimf: alright uhhh hh h")

    $ chat_message("elimf: hold on i had")

    $ chat_message("elimf: i had somethin in mind")

    $ chat_message("wnpep: well go on then")

    $ chat_message("elimf: itll come to me")

    $ chat_message("wnpep: you do that")

    $ chat_message("wnpep: i'm getting back to work")

    # MC: what are you working on wnpep?
    $ player_choice(
        [
            ("what are you working on wnpep?", "x")
        ]
    )

    $ chat_message("wnpep: just collecting data for my final hack. a very no-frills affair but its gotta be done")

    $ chat_message("wnpep: guess that means it's my turn to use you next?")

    $ player_choice(
        [
            ("errrr I don't know about that", "day3_1"),
            ("oh. saucy", "day3_2"),
            ("finally i have a purpose", "day3_3")
        ]
    )


    # [1] MC: errrr I don't know about that
label day3_1: 
    $ chat_message("wnpep: that was a joke! i just wanted to see if you'd like to follow along and get some guidance")

    $ chat_message("incri: oh ym god its mother fuckin theresa")

    $ chat_message("elimf: *teresa")

    $ chat_message("incri: shut up")

    jump day3_4 


    # [2] MC: oh. saucy
label day3_2: 

    # wnpep typing a while

    $ chat_message("incri: ROFL")

    $ chat_message("incri: ROFLMAOOOOO")

    $ chat_message("wnpep: very funny but we all know thats not what i meant")

    $ chat_message("elimf: is it?????")

    # MC: i just can't be sure
    $ player_choice(
        [
            ("i just can't be sure", "x")
        ]
    )

    $ chat_message("incri: u sick old man sicko")
    
    jump day3_4


    # [3] MC: finally i have a purpose
label day3_3: 

    $ chat_message("odxny: HA")

    $ chat_message("elimf: pls")

    $ chat_message("elimf: i take it all back ur not useless anymore")

    $ chat_message("elimf: ur like a blender or a couch")

    $ chat_message("incri: o those r good ")

    # MC: uh. thanks
    $ player_choice(
        [
            ("uh. thanks", "x")
        ]
    )

    jump day3_4



    # end choices
label day3_4: 

    $ chat_message("wnpep: this is getting away from us. the point is that if you want to chip in i can give you some pointers in return")

    $ chat_message("odxny: A fair exchange.")

    $ chat_message("incri: as if u could beat my teaching skills. loser")

    $ chat_message("elimf: i really feel like not a lot of teaching happened from u ")

    $ chat_message("incri: not true ")

    $ chat_message("wnpep: not to pull the old card but i have the experience to say otherwise")

    $ chat_message("wnpep: i think i could provide some pretty good advice actually")

    $ chat_message("odxny: They do have their moments.")

    $ chat_message("incri: im just hearing coping")

    $ chat_message("wnpep: you'd know this if you ever accepted my advice")

    $ chat_message("incri: didnt need it. whatver")

    $ chat_message("incri: ur just using them too")

    $ chat_message("elimf: incri i thought u taught them bc of ur golden heart or smth lol")

    $ chat_message("incri: its DIFFERENT")

    $ chat_message("wnpep: we both may be benefiting but thats where the similarities end")

    $ chat_message("wnpep: im going into this with a different mindset and a lot more patience")

    $ chat_message("elimf: theyve got mindfulness on their side")

    $ chat_message("incri: boring")

    $ chat_message("wnpep: it's not the most exciting but it's important")

    $ chat_message("incri: CRINGE")

    $ chat_message("wnpep: are we in grade school now?")

    $ chat_message("incri: ur skills r")

    $ chat_message("wnpep: alright well i have a hack to run")

    $ chat_message("wnpep: thrim, if u want to help out my offers still on the table")

    # MC: oh yeah lets do it
    $ player_choice(
        [
            ("oh yeah lets do it", "x")
        ]
    )

    $ chat_message("wnpep: awesome")

    $ chat_message("wnpep: let me load everything in")

    $ chat_message("elimf: incri hows it feel getting two timed")

    $ chat_message("incri: i left first dumbass")

    $ chat_message("elimf: oo sorry my bad")

    $ chat_message("odxny: Your ability to create drama in so little time is astounding.")

    $ chat_message("incri: sry for making everyone obsessed w me")

    #$ chat_message("odxny: All is forgiven.")

    $ chat_message("wnpep: alright everythings ready")

    $ chat_message("wnpep: lets get to it")

    jump day3_5


## SEEKL SEGMENT 
label day3_5: 

    # MC: sweet!
    $ player_choice(
        [
            ("sweet", "x")
        ]
    )

    $ chat_message("wnpep: did some poking earlier once we got that big irs data reveal ")

    $ chat_message("elimf: sick last minute add od ")

    $ chat_message("incri: wld hv been sickr to have tht like. this whole time ")

    $ chat_message("odxny: Lmao. ")

    $ chat_message("wnpep: and i think we have just the table i need ")

    $ chat_message("wnpep: can you take a look at this thrim? ")

    $ chat_message("wnpep: `select * \nfrom azgov.insurance` ")
    pause 0.5
    $ tables_seen.append("azgov.insurance")
    play sound "audio/sfx/message_notification_01_002 new table.ogg"
    show highlight_small onlayer screens: 
        pos highlight_tab_table_pos
    $ renpy.notify("TABLE LIST UPDATED")

    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = None
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["azgov.insurance"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = None
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day3_8"

    $ chat_message("odxny: Insurance? ")

    $ chat_message("elimf: not arizona again")

    $ player_choice(
        [
            ("sure, one moment ", "day3_6"), 
            ("are we chasing an insurance company?", "day3_7")
        ]
    )


    # [1] MC: sure, one moment 
label day3_6:

    $ chat_message("wnpep: ty. i'll explain in a sec ")

    jump wait_start


    # [2] MC: are we chasing an insurance company? 
label day3_7:

    $ chat_message("wnpep: not exactly, but kind of")

    $ chat_message("wnpep: take a look first please ")

    jump wait_start


    # complete the query 
label day3_8: 

    $ chat_message("wnpep: see it? ")

    # MC: yes -- looks like a list of insurance companies 
    $ player_choice(
        [
            ("yes -- looks like a list of insurance companies ", "x")
        ]
    )

    $ chat_message("elimf: letsgoooo")

    $ chat_message("wnpep: good. now... ")

    $ chat_message("wnpep: I need you to track down a company in there that matches the following two criteria - ")

    $ chat_message("wnpep: {color="+color_help+"}1) has INS_TYPE = 'medical'{/color}, and ")

    $ chat_message("wnpep: {color="+color_help+"}2) has INS_HSP_PARTNERS = 1{/color} ")
    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = ["ins_name"]
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["azgov.insurance"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = [("ins_id", "INS91983-AZ")]
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day3_12"

    $ player_choice(
        [
            ("okay, i know what to do. ", "day3_9"),
            ("with a where clause again? ", "day3_10")
        ]
    )


    # [1] MC: okay, i know what to do. 
label day3_9:

    $ chat_message("incri: we'll see abt that ")

    $ chat_message("elimf: they did fine yesterday wdym ")

    $ chat_message("incri: \"did fine\" r u stupid ")

    $ chat_message("incri: what part of that was fine ")

    $ chat_message("odxny: Looked fine to me. ")

    $ chat_message("odxny: It wasn't like you were doing a complicated hack regardless, though. ")

    $ chat_message("incri: tf ")

    jump day3_11 


    # [2] MC: with a where clause again? 
label day3_10:

    $ chat_message("wnpep: yes! exactly ")

    $ chat_message("elimf: {color="+color_help+"}instead of using \"OR\" like before, you can use \"AND\"{/color} ")

    # in dms 

    $ chat_message("odxny: Need the answer? ",c="admin")

    $ player_choice(
        [
            ("oh, no, but thanks", "day3_10A"),
            ("maybe... please?", "day3_10B")
        ]
    )


    # [2-A] MC: oh, no, but thanks 
label day3_10A:

    $ chat_message("odxny: Np ",c="admin")

    $ chat_message("odxny: Good luck ",c="admin")

    jump day3_11


    # [2-B] MC: maybe... please? 
label day3_10B:

    $ chat_message("odxny: Of course. ",c="admin")

    $ chat_message("odxny: `select ins_name \nfrom azgov.insurance \nwhere ins_type = 'medical' \n   and ins_hsp_partners = 1`",c="admin")

    jump day3_11 


    # exit bronches
label day3_11: 

    $ chat_message("wnpep: go ahead and give it a try thrim ")

    # MC: can i ask why we’re looking this up? 
    $ player_choice(
        [
            ("can i ask why we’re looking this up?", "x")
        ]
    )

    $ chat_message("wnpep: oh, sure, yeah ")

    $ chat_message("wnpep: i'm searching for confirmation of something i've had suspicions about for a while ")

    $ chat_message("wnpep: rumors of an insurance-hospital scam going about. asking for procedures that aren't needed, and paying a doctor a little extra under the table for doing it ")

    $ chat_message("elimf: any reason to hunt it down? ")

    $ chat_message("wnpep: is it not in our best interest to do good for our fellow man? ")

    $ chat_message("incri: l;et them worry abt themselves")

    $ chat_message("elimf: who let ayn rand in here")

    $ chat_message("incri: stfu")

    $ chat_message("incri: what does theat even mean")

    $ chat_message("elimf: ill tell u when ur older")

    $ chat_message("odxny: Are everyone's final hacks vengeance related? ")

    $ chat_message("wnpep: whoa whoa whoa ")

    $ chat_message("wnpep: i'm not vengeful ")

    $ chat_message("wnpep: i'm morally right.")

    $ chat_message("elimf: interesting ")

    $ chat_message("incri: so was i ")

    $ chat_message("wnpep: you and i are not the same ")

    $ chat_message("incri: yea thnk god ")

    $ chat_message("wnpep: anyway. go ahead and try to find that hospital name thrim ")

    $ chat_message("wnpep: {color="+color_help+"}1) has INS_TYPE = 'medical'{/color}, and ")

    $ chat_message("wnpep: {color="+color_help+"}2) has INS_HSP_PARTNERS = 1{/color} ")

    jump wait_start


    # query runs 
label day3_12:

    $ chat_message("wnpep: any matches? ")

    $ chat_message("wnpep: in order to pull off a scam of this magnitude, it's likely gotta be one hospital and insurance company in cahoots ")

    $ chat_message("incri: \"cahoots\" ")

    $ chat_message("incri: ur so fuckn old ")

    # MC: i did find a match. 
    $ player_choice(
        [
            ("i did find a match. ", "x")
        ]
    )

    # MC: one name -- "Gered Group" 
    $ player_choice(
        [
            ("one name -- \"Gered Group\" ", "x")
        ]
    )

    pause 0.2
    $ hack_notes.append("insurance: \nGered Group")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    show highlight_small onlayer screens: 
        pos highlight_tab_info_pos
    $ renpy.notify("INFO TAB UPDATED")
    pause 0.5

    $ chat_message("wnpep: just the one? ")

    $ player_choice(
        [
            ("just the one", "day3_13"),
            ("maybe.", "day3_14")
        ]
    )



    # [1] MC: just the one 
label day3_13:

    $ chat_message("wnpep: ok, thank you. ")

    jump day3_15


    # [2] MC: maybe. 
label day3_14:

    $ chat_message("elimf: maybe? ")

    $ chat_message("wnpep: please. ")

    # MC: yes, one. sorry
    $ player_choice(
        [
            ("yes, one. sorry", "x")
        ]
    )

    $ chat_message("wnpep: k ")

    jump day3_15



label day3_15: 

    $ chat_message("odxny: So, you're sure that has to be the scam one? ")

    $ chat_message("wnpep: wouldn't say 100% sure, but close enough ")

    $ chat_message("wnpep: like 98% ")

    $ chat_message("elimf: i mean isnt it all scams")

    $ chat_message("elimf: in the scheming of things. the world of stuff")

    $ chat_message("incri: life is a fcking scam.")

    $ chat_message("elimf: ^ the joker")

    $ chat_message("incri: SHUT UP")

    $ chat_message("incri: ur life is a scam")

    $ chat_message("elimf: that was also too easy")

    $ chat_message("wnpep: can we focus please")

    $ chat_message("elimf: right")

    $ chat_message("elimf: cant forget the real scam")

    $ chat_message("odxny: Just keep going, pep.")

    $ chat_message("wnpep: next step -- we need to identify the hospital that works with them ")

    $ chat_message("wnpep: you can get that from here: #azgov.hospitals#")
    pause 0.5
    $ tables_seen.append("azgov.hospitals")
    play sound "audio/sfx/message_notification_01_002 new table.ogg"
    show highlight_small onlayer screens: 
        pos highlight_tab_table_pos
    $ renpy.notify("TABLE LIST UPDATED")

    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = ["hsp_name"]
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["azgov.hospitals"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = [("hsp_id", "H5212-03")]
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day3_16"

    $ chat_message("elimf: ur shitting me ")

    $ chat_message("odxny: LMAO")

    $ chat_message("elimf: why is it always so straightforward ")

    $ chat_message("wnpep: look at the big man i aint in charge")

    $ chat_message("odxny: The back end program does a good job sometimes assembling data like that. ")

    $ chat_message("elimf: wild ")

    $ chat_message("wnpep: go take a peek at that table and {color="+color_help+"}see if you can figure out how to find which one works with that insurance company{/color}")

    jump wait_start


    # query runs 
label day3_16:

    # MC: i think i got it? 
    $ player_choice(
        [
            ("i think i got it? ", "x")
        ]
    )

    $ chat_message("odxny: And?") 

    # MC: "PRIDE" 
    $ player_choice(
        [
            ("\"PRIDE\"", "x")
        ]
    )

    pause 0.2
    $ hack_notes.append("hospital: \nPRIDE")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    show highlight_small onlayer screens: 
        pos highlight_tab_info_pos
    $ renpy.notify("INFO TAB UPDATED")
    pause 0.5

    pause 2 

    $ chat_message("wnpep: ....really?") 

    $ chat_message("odxny: ?") 

    # MC: why surprised? 
    $ player_choice(
        [
            ("why surprised? ", "x")
        ]
    )

    pause 1 

    $ chat_message("wnpep: doesn't make sense ")

    $ chat_message("wnpep: thinking ")

    pause 3  

    $ chat_message("wnpep: aren't there any other insurances listed with that hospital? i thought i checked that one ")

    $ chat_message("wnpep: maybe ins_define? is that set to true?")

    $ chat_message("odxny: Yes, it is.")

    $ chat_message("wnpep: wtf")

    $ chat_message("wnpep: but gered only works with PRIDE?")

    $ chat_message("odxny: Wn, if you go back to #azgov.insurance#, take a look at the ins_alias column for Gered Group's row. ")

    $ chat_message("wnpep: looking") 

    pause 3 

    $ chat_message("wnpep: \"Define\". god ")

    $ chat_message("elimf: i dont get it. pls explain in small words ")

    $ chat_message("wnpep: PRIDE looks like it takes two insurances, Define and Gered -- but they're just the same company. ")

    $ chat_message("odxny: Bit sneaky. ")

    # MC: what's the point of doing that? 
    $ player_choice(
        [
            ("what's the point of doing that?", "x")
        ]
    )

    $ chat_message("odxny: To make themselves look not shady, ha. ")

    $ chat_message("wnpep: should have put that together. idk how i missed it ")

    $ chat_message("wnpep: my daughter has been saying i need new glasses ")

    $ chat_message("elimf: a daughter ")

    $ chat_message("odxny: Makes sense that you're a parent. ")

    $ chat_message("elimf: yea i can't even b mad at that one. it would be weird if u werent tbh ")

    $ chat_message("wnpep: lol ")

    $ chat_message("wnpep: sorry, i keep letting things slip somehow")

    $ chat_message("wnpep: must be my love and affection for you all allowing me to open up more freely")

    $ chat_message("elimf: fuck off ")

    $ chat_message("incri: it's fucking thrim ")

    # MC: i didn't do shit 
    $ player_choice(
        [
            ("i didnt do shit ", "day3_17"), 
            ("no its the love and affection for sure", "day3_18")
        ]
    )

label day3_17: 

    $ chat_message("incri: tainted us ")

    $ chat_message("odxny: I wouldn't say tainted. ")

    $ chat_message("odxny: Thrim's brought some life back to this server. ")

    # MC: aw. 
    $ player_choice(
        [
            ("aw. do u mean it", "x")
        ]
    )

    $ chat_message("odxny: Course.")

    $ chat_message("elimf: lmao rush of life before the end ")

    $ chat_message("elimf: there's a poem in thre somewhere ")

    jump day3_19


label day3_18: 

    $ chat_message("elimf: BOOOOOOOOOOOOOOOOO",ot="incri")

    $ chat_message("incri: BOOOOOOOOOOOOOOOOOOOOOOOOOO",fastmode=True)

    $ chat_message("incri: FUCKASS IDEA",ot="elimf")

    $ chat_message("elimf: GET OFF THE STAGE",fastmode=True)

    $ player_choice(
        [
            ("wow. od do u see this", "x")
        ]
    )

    $ chat_message("odxny: LMAO")

    jump day3_19



label day3_19:

    $ chat_message("wnpep: ok. time to focus ")

    $ chat_message("wnpep: let's go figure out who is filing the claims here ")

    $ chat_message("wnpep: #pride.claims# ")
    pause 0.5
    $ tables_seen.append("pride.claims")
    play sound "audio/sfx/message_notification_01_002 new table.ogg"
    show highlight_small onlayer screens: 
        pos highlight_tab_table_pos
    $ renpy.notify("TABLE LIST UPDATED")

    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = ["claim_doctor"]
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["pride.claims"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = None
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day3_20"

    $ chat_message("wnpep: if you check that table, you'll see some info about hospital procedures and which doctor ordered each ")

    $ chat_message("wnpep: can you take a look at that table? ")

    # MC: sure, one moment 
    $ player_choice(
        [
            ("sure", "x")
        ]
    )

    jump wait_start 


    # query runs 
label day3_20: 

    # MC: I see two names in here 
    $ player_choice(
        [
            ("I see two names in here", "x")
        ]
    )

    pause 0.2
    $ hack_notes.append("name 1: \nBailey Yang")
    $ hack_notes.append("name 2: \nAdriel Humphrey")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    show highlight_small onlayer screens: 
        pos highlight_tab_info_pos
    $ renpy.notify("INFO TAB UPDATED")
    pause 0.5

    $ chat_message("elimf: small ass hospital lmao ")

    $ chat_message("odxny: Pros at staying under the radar. Like us. ")

    $ chat_message("wnpep: great! how about claim amounts? ")

    # MC: not in here, unfortunately 
    $ player_choice(
        [
            ("not in here, unfortunately ", "x")
        ]
    )

    $ chat_message("wnpep: huh? what? really? ")

    # MC: why?
    $ player_choice(
        [
            ("why?", "x")
        ]
    )

    $ chat_message("wnpep: well... i thought we need to see who is filing for most of the expensive things")

    $ chat_message("elimf: it's not just both of them? ")

    $ chat_message("wnpep: it could be... but i'd rather be sure. hm ")

    $ chat_message("wnpep: how to confirm... ")

    $ chat_message("odxny: What do you think we should do, thrim? ")

    python:
        if has_sql_knowledge: 
            renpy.jump("day3_20_SQL") 
        else: 
            renpy.jump("day3_20_cont")


    # if stated sql knowledge
    # [1] MC: can't we just use a group by or something to see who has which type of claims most often? 
label day3_20_SQL:

    $ player_choice(
        [
            ("can't we just use a group by or something to see who has which type of claims most often?", "x")
        ]
    )

    $ chat_message("elimf: LOLLLLL ")

    $ chat_message("elimf: yea od where's the fucken group by ")

    $ chat_message("odxny: Sorry. SeekL isn't perfect. ")

    $ chat_message("odxny: Can't do a lot of those type of queries.")

    $ chat_message("elimf: still crazy ")

    $ chat_message("odxny: Look. ")

    jump day3_20_cont


label day3_20_cont: 

    $ player_choice(
        [
            ("can we just threaten both of them? ", "day3_21"), 
            ("didn't you say one of the doctors was pocketing extra money? can we track that?", "day3_22")
        ]
    )

    # [2] MC: can we just threaten both of them? 
label day3_21: 

    $ chat_message("incri: it's th most effcien t strat ")

    $ chat_message("elimf: incri stop ruining the new persson ")

    $ chat_message("wnpep: lol. i'd rather avoid blackmailing an innocent if i can avoid it ")

    $ chat_message("incri: boring ")

    $ chat_message("odxny: How about paystubs? Let's go trace the money. ")

    $ chat_message("wnpep: oh, right. that would make sense ")

    jump day3_23


    # [3] MC: didn't you say one of the doctors was pocketing extra money? can we track that? 
label day3_22: 

    $ chat_message("wnpep: excellent thinking thrim. and we can indeed")

    $ chat_message("wnpep: now that we have the wonderful world of irs data ")

    $ chat_message("elimf: CHA CHING ")

    jump day3_23


label day3_23: 

    $ chat_message("wnpep: for this, {color="+color_help+"}let's compare the output of two tables{/color}")

    $ chat_message("wnpep: table 1 - #pride.paystubs23#")

    pause 0.5
    $ tables_seen.append("pride.paystubs23")
    play sound "audio/sfx/message_notification_01_002 new table.ogg"
    show highlight_small onlayer screens: 
        pos highlight_tab_table_pos
    $ renpy.notify("TABLE LIST UPDATED")

    $ chat_message("wnpep: table 2 - #irs.income23# ")

    pause 0.5
    $ tables_seen.append("irs.income23")
    play sound "audio/sfx/message_notification_01_002 new table.ogg"
    show highlight_small onlayer screens: 
        pos highlight_tab_table_pos
    $ renpy.notify("TABLE LIST UPDATED")

    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = ["pay_total", "irs_total", "full_name"]
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["pride.paystubs23", "irs.income23"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = [
            ("pay_no", "P3406"), ("pay_no", "P1282"), 
            ("pstb_no", "P73604-437"), ("pstb_no", "P24992-474")
            ]
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day3_27"


    $ chat_message("wnpep: we can compare how much each person made in these two tables") 

    # MC: ohh so... 
    $ player_choice(
        [
            ("ohh so...", "x")
        ]
    )

    # MC: the one who is pocketing extra cash should have reported less to the irs 
    $ player_choice(
        [
            ("the one who is pocketing extra cash should have reported less to the irs ", "x")
        ]
    )

    $ chat_message("elimf: bingo bango bongo ")

    $ chat_message("wnpep: this might be a great point to show you a new seekL function -- {color="+color_help+"}JOIN{/color}")

    $ chat_message("wnpep: {color="+color_help+"}do you already know how natural joins work?{/color}")

    $ player_choice(
        [
            ("oh yeah, i'm good!", "day3_24"), 
            ("no (tutorial)", "day3_25")
        ]
    )



    # [1] MC: oh yeah, i'm good! 
label day3_24:

    $ chat_message("wnpep: ok ")

    $ chat_message("wnpep: use it in this exercise")

    jump day3_26 


    # [2] MC: no (tutorial)
label day3_25: 

    $ chat_message("wnpep: no problem! let's sit down and learn ")

    $ chat_message("elimf: r u not sitting wn ")

    $ chat_message("wnpep: i'm sitting. ")

    $ chat_message("elimf: confusing ")

    $ chat_message("incri: it's  figure of speech idiot ")

    $ chat_message("elimf: i'm not an idiot ")

    $ chat_message("incri: idiot ")

    $ chat_message("odxny: I can help out here. ")

    $ chat_message("odxny: A {color="+color_syntax+"}JOIN{/color} can be used to combine the columns of two tables together. ")

    $ chat_message("odxny: {color="+color_help+"}It will search for a common column between the two tables and, if one exists, it will output those two tables combined together.{/color}")

    $ chat_message("odxny: So, if you want to get information about someone from two different tables, run it with a {color="+color_syntax+"}JOIN{/color} and you can get a clean view of everything you need. ")

    $ chat_message("odxny: Here's an example. Remember \"OfficerOral\"? ")

    # MC: how could i forget 
    $ player_choice(
        [
            ("how could i forget ", "x")
        ]
    )

    $ chat_message("odxny: So, so true. ")

    $ chat_message("odxny: `SELECT ss_alias \nFROM irs.contacts \nJOIN secretsmooch.users \nWHERE full_name = 'bruce johnson'`")

    $ chat_message("odxny: (If you run that, it'll help you understand what I'm gonna say next.)")

    $ chat_message("odxny: You got to that alias yesterday through where clauses and looking between tables, but you also could have gotten there just by running this directly. ")

    $ chat_message("odxny: #irs.contacts# and #secretsmooch.users# both {color="+color_help+"}share the column \"email\", which lets you join those tables together{/color} and take a look at Bruce's alias in there. ")

    $ chat_message("odxny: notice too how {color="+color_help+"}whichever column is joined on is printed out as well{/color}, even if you don't specifically list it in your {color="+color_syntax+"}SELECT{/color} statement. Same for the column in the {color="+color_syntax+"}WHERE{/color} clause. ")

    $ chat_message("odxny: It helps keep track of things. ")

    $ chat_message("wnpep: wow. a natural teacher")

    $ chat_message("elimf: why do we even need wnpep ")

    $ chat_message("wnpep: true ")

    $ chat_message("odxny: Shut up lol ")

    $ chat_message("wnpep: did that all make sense thrim? ")

    $ player_choice(
        [
            ("i think so", "day3_25A"), 
            ("ur like. rly wordy", "day3_25B")
        ]
    )


    # [2-A] MC: i think so 
label day3_25A: 

    $ chat_message("wnpep: nice stuff od")

    $ chat_message("odxny: Thank you, thank you. More praise please.") 

    $ chat_message("incri: ur mask is only mildly cringe")

    $ chat_message("elimf: i think ur mask is very cool od")

    $ chat_message("odxny: Ok. No more praise please.")
    
    jump day3_26


    # [2-B] MC: ur like. rly wordy 
label day3_25B:

    $ chat_message("elimf: i take it back. u suck od ")

    $ chat_message("odxny: Damn.")

    $ chat_message("wnpep: eli")

    $ chat_message("elimf: ? ")

    jump day3_26


    # exit bronches
label day3_26:

    $ chat_message("wnpep: thrim, if u ever need reminders on how stuff works, {color="+color_help+"}you can always check the seekL guide tab{/color}")

    $ chat_message("wnpep: so, {color="+color_help+"}go ahead and see if you can tell who has mis-matching records between #pride.paystubs23# and #irs.income23# only between those two names in the claims table{/color}")

    $ chat_message("wnpep: {color="+color_help+"}you'll want to utilize a JOIN and a WHERE clause to get the info we need.{/color}")

    # MC: u got it 
    $ player_choice(
        [
            ("u got it", "x")
        ]
    )

    jump wait_start


    # query wait 
label day3_27: 

    # MC: i am so skilled. i got it 
    $ player_choice(
        [
            ("i am so skilled. i got it ", "x")
        ]
    )

    $ chat_message("wnpep: that's the spirit! heck yeah you are! ")

    $ chat_message("odxny: Nice job. ")

    $ chat_message("wnpep: so, who is it? {color="+color_help+"}which paystub totals don't match for 2023?{/color}")

    $ player_choice(
        [
            ("Bailey Yang", "day3_28"), 
            ("Adriel Humphrey", "day3_29")
        ]
    )


    # [1] MC: Bailey Yang 
label day3_28: 

    # MC: PRIDE has them down as making 190k, irs as 120k 
    $ player_choice(
        [
            ("PRIDE has them down as making 190k, irs as 120k ", "x")
        ]
    )

    pause 0.2
    $ hack_notes.append("fraudster: \nBailey Yang")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    show highlight_small onlayer screens: 
        pos highlight_tab_info_pos
    $ renpy.notify("INFO TAB UPDATED")
    pause 0.5

    $ chat_message("elimf: i love how skilled u r at stating basic facts")

    $ chat_message("elimf: ur stunning thrim ")

    # MC: omg thank u 
    $ player_choice(
        [
            ("omg thank u", "x")
        ]
    )

    jump day3_30


    # [2] MC: Adriel Humphrey 
label day3_29: 

    $ chat_message("incri: widdle iddy biddy numbr comparsn 2 hard 4 u? ")

    $ chat_message("incri: widdle baby needs ther hand held ? ")

    # MC: ????? am i wrong? 
    $ player_choice(
        [
            ("????? am i wrong? ", "x")
        ]
    )

    $ chat_message("incri: yeah ur fuckin wrong IDIOT ")

    # MC: omg... 
    $ player_choice(
        [
            ("omg...", "x")
        ]
    )

    $ chat_message("odxny: Don't sweat it. It's the other one. Bailey Yang.")

    $ chat_message("odxny: The pay amounts don't match. ")

    pause 0.2
    $ hack_notes.append("fraudster: \nBailey Yang")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    show highlight_small onlayer screens: 
        pos highlight_tab_info_pos
    $ renpy.notify("INFO TAB UPDATED")
    pause 0.5

    jump day3_30



    # end choices
label day3_30: 

    $ chat_message("odxny: That enough confirmation that this is the doctor? ")

    $ chat_message("wnpep: for me? yes ")

    $ chat_message("wnpep: usually i'd be more thorough but ")

    $ chat_message("wnpep: given my intel, this seems pretty straightforward ")

    $ chat_message("wnpep: {color="+color_help+"}mind grabbing me Bailey Yang's email from {/color}#irs.contacts#, thrim? ")

    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = ["email"]
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["irs.contacts"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = [("irs_id", "I93999-218")]
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day3_33"

    $ player_choice(
        [
            ("am i just here to do petty work for you all", "day3_31"), 
            ("sure thing, one moment ", "day3_32")
        ]
    )


    # [1] MC: am i just here to do petty work for you all 
label day3_31: 

    $ chat_message("incri: yes ")

    $ chat_message("elimf: LOL ")

    $ chat_message("wnpep: we're all learning together! ")

    # MC: are we? 
    $ player_choice(
        [
            ("are we?", "x")
        ]
    )


    $ chat_message("wnpep: maybe! ")

    $ chat_message("wnpep: please grab it ")

    # MC: fine, fine 
    $ player_choice(
        [
            ("fine, fine ", "x")
        ]
    )

    jump day3_32


    # [2] MC: sure thing, one moment 
label day3_32: 

    $ chat_message("wnpep: thanks champ!")

    jump wait_start 


    # query wait 
label day3_33: 

    # MC: itsssbaeley@baver.net
    $ player_choice(
        [
            ("itsssbaeley@baver.net", "x")
        ]
    )

    pause 0.2
    $ hack_notes.append("email: \nitsssbaeley@baver.net")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    show highlight_small onlayer screens: 
        pos highlight_tab_info_pos
    $ renpy.notify("INFO TAB UPDATED")
    pause 0.5

    $ chat_message("wnpep: wonderful ")

    $ chat_message("wnpep: ah ")

    $ chat_message("elimf: the moment we've all been waiting for ")

    $ chat_message("incri: BLACKMAIL BLACKMAIL BLACKMAIL ")

    $ chat_message("wnpep: one moment, i must perfect this ")

    $ chat_message("odxny: Sure. ")

    $ chat_message("elimf: thought they would have had that already ready to go ")

    $ chat_message("incri: sometimes u need like ")

    $ chat_message("incri: 2 feel it ")

    $ chat_message("incri: in th moment ")

    $ chat_message("elimf: uh huh ")

    $ chat_message("SYSTEM: EXTORTION SENT -- ITSSSBAELEY@BAVER.NET")

    $ chat_message("odxny: Nice. ")

    $ chat_message("wnpep: this one will likely take a while. we can check in tomorrow")

    # MC: why? 
    $ player_choice(
        [
            ("why a while?", "x")
        ]
    )

    $ chat_message("wnpep: bc this involves a giant scam getting exposed lol ")

    $ chat_message("elimf: LMAO ")

    $ chat_message("odxny: They're gonna strategize on their side. ")

    $ chat_message("wnpep: last one... all done. huh ")


    ## WRAP UP 

    $ chat_message("elimf: thats a wrap everyone clap")

    $ chat_message("elimf: and rhyme. in time")

    $ chat_message("incri: i got mine done faster")

    $ chat_message("elimf: i said clap")

    $ chat_message("odxny: Good work as always.")

    $ chat_message("wnpep: thanks")

    # MC: how do u feel?
    $ player_choice(
        [
            ("how do u feel?", "x")
        ]
    )

    $ chat_message("wnpep: i'm not quite feeling happy per se more like")

    $ chat_message("wnpep: trying to think of a good word for it")

    # MC: satisfied?
    $ player_choice(
        [
            ("satisfied?", "x")
        ]
    )

    $ chat_message("wnpep: in a way")

    $ chat_message("elimf: wnpep is lacking the pep")

    $ chat_message("incri: stop rhymuing dumbass")

    $ chat_message("elimf: my whimsy :^(")

    $ chat_message("odxny: I'm sure it feels a little odd to finally be finished.")

    $ chat_message("wnpep: i suppose that's part of it")

    $ player_choice(
        [
            ("it'll come in time!", "day3_34"), 
            ("thought it would feel better?", "day3_35")
        ]
    )


    # [1] MC: it'll come in time!
label day3_34: 

    $ chat_message("wnpep: mm")

    $ chat_message("wnpep: perhaps")

    jump day3_36


    # [2] MC: thought it would feel better?
label day3_35: 

    $ chat_message("wnpep: maybe a little")

    $ chat_message("wnpep: thats on me for not managing my expectations")

    jump day3_36


    # end choices
label day3_36: 

    $ chat_message("odxny: Would it help if we did a victory shot? I think I have something I can use.")

    $ chat_message("wnpep: appreciate the thought but no thanks")

    $ chat_message("wnpep: think im just gonna get a beer and sit for a while")

    $ chat_message("odxny: All good.")

    $ chat_message("wnpep: take care")

    # wnpep offline
    $ chat_message("SYSTEM: WNPEP offline") 

    $ chat_message("incri: u didnt offer me a celebratory shot")

    $ chat_message("odxny: Sorry for the oversight.")

    $ chat_message("incri: liar")

    pause 2 

    $ chat_message("odxny: You've seen through me.")

    $ chat_message("elimf: masterful gambit")

    $ chat_message("incri: fukc you all im getting my own shot")

    $ chat_message("elimf: ill do a shot with u")

    $ chat_message("incri: im not enabling u getting fkcing crossfaded")

    $ chat_message("elimf: every day i suffer a million tortures")

    $ chat_message("odxny: It's a hard life you lead.")

    $ chat_message("elimf: it is")

    # dms

    $ chat_message("odxny: Since wnpep isn't up to it, would you like to call instead? No shot required.",c="admin")

    $ chat_message("odxny: We can celebrate your participation in two successful hacks.",c="admin")

    $ player_choice(
        [
            ("id be up for a toast!", "day3_37"), 
            ("sure we can do that", "day3_38")
        ]
    )


    # [1] MC: id be up for a toast!
label day3_37: 

    $ chat_message("odxny: Let's take a minute to get our beverages of choice then.",c="admin")

    $ chat_message("odxny: I'll call once I've scrounged mine up.",c="admin")

    jump day3_39 


    # [2] MC: sure we can do that
label day3_38: 

    $ chat_message("odxny: Alright, let me grab a drink.",c="admin")
    
    jump day3_39


label day3_39: 

    $ chat_message("odxny: One sex",c="admin")

    $ player_choice(
        [
            ("damn. already?", "day3_40"), 
            ("kk", "day3_41")
        ]
    )


label day3_40: 

    $ chat_message("odxny: What?",c="admin") 

    $ player_choice(
        [
            ("could, like, at least shower me in compliments first", "day3_40A"), 
            ("nvm", "day3_40B")
        ]
    )


label day3_40A: 

    pause 2 

    $ chat_message("odxny: One sec*",c="admin") 

    $ chat_message("odxny: Fuck you lol",c="admin") 

    $ player_choice(
        [
            ("LOL", "x")
        ]
    )

    jump day3_41


label day3_40B: 

    pause 2 

    $ chat_message("odxny: k",c="admin") 

    jump day3_41


label day3_41: 

    ## call time 
    jump go_to_call

    $ renpy.pause(hard=True)


