

label day1_start: 
    #jump day1_30
    #$ $ chat_message("odxny: testing testing")

    #$ chat_message("incri: and then i beat him to death with hammers")

    #jump day2_start

    #jump day1_15

    #jump day2_7

    $ chat_message("SYSTEM: THRIM joined")

    pause 1 

    $ chat_message("elimf: and that's when i started breaking down in the waffle house")

    $ chat_message("elimf: wait who")

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

    $ chat_message("wnpep: don't worry. i'm checking them out")

    $ chat_message("elimf: anything juicy")

    pause 1 

    $ chat_message("wnpep: this person is not a threat of any kind ")

    pause 1

    $ chat_message("wnpep: ...to anyone ")

    $ chat_message("elimf: lolllll ")

    $ player_choice(
        [
            ("you're..... checking", "x")
        ]
    )

    $ chat_message("wnpep: maybe they are a threat to themself actually. in an existential way ")

    $ chat_message("incri: they're calling u a idiot")

    $ chat_message("wnpep: no i'm not ", ot="incri")

    $ chat_message("incri: idiot vibes so far definnitely ")

    $ player_choice(
        [
            ("i've barely said anything", "x")
        ]
    )

    $ chat_message("elimf: very silly vibes", ot="wnpep")

    $ chat_message("wnpep: do you like the life you lead, thrim? ")

    $ player_choice(
        [
            ("what the hell are you looking at", "day1_4"), 
            ("you're bluffing. i'm super secure", "day1_5")
        ]
    )

    # [1] MC: what the hell are you looking at?? 
label day1_4:

    $ chat_message("wnpep: does it matter? it's all the same dull boring nonsense ")

    $ chat_message("wnpep: you should aim higher. i think you can do better ")

    $ chat_message("elimf: i found them too ")

    $ player_choice(
        [
            ("wtf", "x")
        ]
    )

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

    $ chat_message("wnpep: we access data from a variety of companies/government agencies")

    $ chat_message("wnpep: a giant backend program is constantly breaking into places and copying information to us")

    $ chat_message("wnpep: and we use that information for a uh")

    $ chat_message("wnpep: range of things")

    $ player_choice(
        [
            ("like ethical hacking ", "x"), 
        ]
    )

    $ chat_message("elimf: bastions of goodness, us")

    $ chat_message("incri: what did u jst call me")

    $ chat_message("wnpep: uh some of us are more ethical than others")

    $ chat_message("wnpep: do you know SQL? ")

    $ player_choice(
        [
            ("yes", "day1_10"), 
            ("no (tutorial)", "day1_11")
        ]
    )

    # [1] MC: yes 
label day1_10: 

    $ chat_message("wnpep: then you've got a great head start champ ")

    $ chat_message("elimf: but, don't think it can do all that SQL can. it's pretty limited ")

    $ chat_message("wnpep: seekL is very similar but has small differences")

    jump day1_12

    # [2] MC: no 
label day1_11: 

    $ chat_message("wnpep: no issue. it's not a hard language to pick up") 

    $ chat_message("elimf: if you find it difficult...")

    $ chat_message("incri: concerning")

    $ chat_message("wnpep: let's explain some syntax")

    $ chat_message("wnpep: when we want to look at some data, we run commands like this:")

    $ chat_message("wnpep: `select *\nfrom table_name`")

    $ chat_message("elimf: (that's not a real table so don't try typing that in quite yet)")

    $ chat_message("wnpep: {color=ccff11}SELECT{/color} is used to tell the table which information we want from it")

    $ player_choice(
        [
            ("what does a star mean? that asterisk *", "x")
        ]
    )

    $ chat_message("wnpep: it means we are telling the table we want all information it has")

    $ chat_message("elimf: {color=ccff11}* = all{/color}")

    $ chat_message("wnpep: {color=ccff11}FROM{/color} says which table we want to grab this information from")

    $ chat_message("wnpep: so, you'd put a real table name there where it says \"table_name\"")

    $ chat_message("wnpep: put it all together and this query is saying-")

    $ chat_message("wnpep: \"please give me all the information you have from table_name\"")

    jump day1_12

    # end choices 
label day1_12:

    $ chat_message("wnpep: any questions? ")

    $ player_choice(
        [
            ("no, this is simple", "day1_13"), 
            ("i might.......", "day1_14")
        ]
    )

    # [1] MC: yeah, simple 
label day1_13:

    $ chat_message("elimf: phew ")

    $ chat_message("wnpep: let's go through an example anyway")

    jump day1_15

    # [2] MC: not really...
label day1_14:

    $ chat_message("incri: lollllllllllll")

    $ chat_message("wnpep: let's go through an actual example now")

    jump day1_15

    # end choices 
label day1_15: 

    $ chat_message("wnpep: go ahead and type this into console on the top right ")

    $ chat_message("wnpep: `select * from table.example`")
    pause 0.5 
    $ tables_seen.append("table.example")
    play sound "audio/sfx/message_notification_01_002 new table.ogg"
    show highlight_small onlayer screens: 
        xpos 1590 ypos 130 
    $ renpy.notify("TABLE LIST UPDATED")

    $ chat_message("elimf: or, notice how a table just appeared under the tables list on the far right?")

    $ chat_message("elimf: {color=ccff11}any time you encounter a new table, it gets added to your personal little reference bank there{/color}")

    $ chat_message("wnpep: if you click it, it will pre-fill the console with a basic query to look at the table")

    $ chat_message("wnpep: {color=ccff11}pretty useful to just look at a table when you aren't familiar with what's in it{/color}")

    $ chat_message("elimf: there's also an {color=ccff11}info sheet{/color} in the same area where we share notes")

    $ chat_message("elimf: useful to look in there for information when you're stuck")

    $ chat_message("wnpep: either way, typing or clicking, go ahead and take a look in there thrim")

    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = None 
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["table.example"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = None 
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 

    $ player_choice(
        [
            ("ok, one moment", "day1_18"), 
            ("but... why is that so long and ugly...", "day1_17")
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
    if first_flash:
        pause 0.5 
        play sound "audio/sfx/message_notification_01_001 tutorial.ogg"
        show highlight_large onlayer screens: 
            pos highlight_frame_console_pos
        $ first_flash = False 
    
    # wait for input 
    $ player_is_waiting = True 
    $ waiting_label = "day1_19"

    # if they arrive already ready to pass 
    if player_can_pass:
        $ player_is_waiting = False 
        jump day1_19 
    $ renpy.pause(hard=True)

label day1_19: 
    hide highlight_large onlayer screens 
    $ first_flash = True 
    $ player_is_waiting = False 
    #$ tables_seen.append("table.example")
    
    # MC: done 
    $ player_choice(
        [
            ("done", "x"), 
        ]
    )

    $ chat_message("wnpep: okay, so. what you see here is just a small example table we built ages ago.", ot="elimf") 

    $ chat_message("elimf: do you already know how tables of data work?") 

    # MC: done 
    $ player_choice(
        [
            ("yes! i'm well versed", "day1_19_1"), 
            ("no (tutorial)", "day1_19_2"), 
        ]
    )

label day1_19_1: 
    $ chat_message("wnpep: great. then we can skip all that, thrim.") 
    jump day1_24


label day1_19_2: 

    $ chat_message("wnpep: no problem! let's explain a bit.") 

    $ chat_message("elimf: a table is just storage of information about things") 

    $ chat_message("incri: stupid summary",ot="elimf") 

    $ chat_message("elimf: each row is a thing and each column is information") 

    $ chat_message("wnpep: ok no no ur being confusing") 

    $ chat_message("wnpep: thrim, in this table there are 5 columns:") 

    $ chat_message("wnpep: {color=ccff11}table_id{/color} - this is just a unique thing for each row. you can mostly ignore this") 

    $ chat_message("wnpep: {color=ccff11}hacker_name{/color} - this tells you who each row is about among the four of us here. minus you") 

    $ chat_message("elimf: we should update and add thrim", ot="wnpep")

    $ chat_message("wnpep: {color=ccff11}chat_join_date{/color} - this tells you when each of us joined seekL") 

    $ chat_message("elimf: so, like i'm on row 3, and it says i joined 2023-12-12 right before christmas")

    $ chat_message("elimf: make sense?")

    $ player_choice(
        [
            ("i think so", "x")
        ]
    )

    $ chat_message("wnpep: {color=ccff11}favorite_fruit{/color} - everyone's favorite fruits from a poll") 

    $ chat_message("wnpep: {color=ccff11}number_of_hacks{/color} - how many successful hacks we've each pulled off")  

    $ chat_message("incri: my number shuld b higher")

    $ chat_message("wnpep: successful being the key word here")

    $ chat_message("elimf: lmao")

    $ chat_message("wnpep: so, based off of that information, {color=ccff11}can you tell me who in here has the most hacks completed?{/color}")  

    $ player_choice(
        [
            ("wnpep.", "day1_19_2_1"), 
            ("incri.", "day1_19_2_2"), 
            ("odxny.", "day1_19_2_3"), 
        ]
    )

label day1_19_2_1: 
    $ chat_message("wnpep: lol i wish, but not quite.")
    jump day1_19_2_cont

label day1_19_2_2: 
    $ chat_message("incri: secretly ur right. these losers can't count")

    $ chat_message("elimf: ya tru probs")

    $ player_choice(
        [
            ("damn it", "x")
        ]
    )

    jump day1_19_2_cont


## correct choice
label day1_19_2_3: 
    $ chat_message("wnpep: yes! that's right!")

    $ chat_message("wnpep: if you want to see it even clearer, you can run this: `select hacker_name, number_of_hacks \nfrom table.example`")

    $ chat_message("wnpep: but, essentially, {color=ccff11}the row that has 50 hacks also has odxny's name on it{/color}")

    $ chat_message("wnpep: which means that's the number of hacks he's done!")

    $ chat_message("elimf: nice job thrim")

    jump day1_24


## cont if wrong through tutorial 
label day1_19_2_cont: 

    $ chat_message("wnpep: it might help you see better if you run this: \n`select hacker_name, number_of_hacks \nfrom table.example`")

    $ chat_message("wnpep: or, just, you know, {color=ccff11}try taking a look at those columns again{/color}. hit execute again i mean.")

    $ chat_message("wnpep: let us know when you're done")
    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["hacker_name", "number_of_hacks"] = None 
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["table.example"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = None 
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
    
    jump day1_19_2_cont_2

label day1_19_2_cont_2:
    if first_flash:
        pause 0.5 
        play sound "audio/sfx/message_notification_01_001 tutorial.ogg"
        show highlight_large onlayer screens: 
            pos highlight_frame_console_pos 
        $ first_flash = False 

    # wait for input 
    $ player_is_waiting = True 
    $ waiting_label = "day1_19_2_cont_3"

    # if they arrive already ready to pass 
    if player_can_pass:
        $ player_is_waiting = False 
        jump day1_19_2_cont_3 
    $ renpy.pause(hard=True)



label day1_19_2_cont_3: 
    hide highlight_large onlayer screens 
    $ first_flash = True 
    $ player_is_waiting = False 
    $ player_choice(
        [
            ("done!", "x")
        ]
    )

    $ chat_message("wnpep: neat! so who has their name next to the highest number of hacks?")

    $ player_choice(
        [
            ("elimf.", "day1_19_2_cont_3_1"), 
            ("odxny.", "day1_19_2_cont_3_2"), 
        ]
    )

label day1_19_2_cont_3_1:
    $ chat_message("incri: IT'S ODXNY DIPSHIT")

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

    $ chat_message("wnpep: we can help you out as you go thrim. just ask")

    $ player_choice(
        [
            ("okay....", "x")
        ]
    )

    jump day1_24


label day1_19_2_cont_3_2: 

    $ chat_message("elimf: my god they've done it")

    $ chat_message("wnpep: yayyyy!!")

    $ chat_message("incri: this is so fkin boring")

    $ chat_message("wnpep: shut up inc")

    $ chat_message("incri: no")

    $ chat_message("wnpep: yay thrim!!")

    jump day1_24


    # end choices 
label day1_24: 

    # MC: my name isn't thrim. idk why my user was set to that 
    $ player_choice(
        [
            ("my name isn't thrim. idk why my user was set to that", "x")
        ]
    )

    $ chat_message("wnpep: it's randomized when u join, for anonymity purposes")

    # MC: ohhhh 
    $ player_choice(
        [
            ("ohhhh", "x")
        ]
    )

    $ chat_message("elimf: lol imagine being named incri")

    $ chat_message("incri: imagine not having the highest number of hacks in here")

    $ chat_message("elimf: yea you can imagine that. since you have like 4 total right")

    $ chat_message("incri: WHAT")

    # odxny online

    $ chat_message("SYSTEM: ODXNY online")

    $ chat_message("elimf: sup big cheese")

    $ chat_message("wnpep: got someone new while you were gone")

    $ chat_message("odxny: Did you check them out?")

    $ chat_message("wnpep: yeah i'm sure ur already doing that too but i didnt see anything to worry about")

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

    show screen video_call_window("day1_call")

    $ renpy.pause(hard=True)
    # pause
    # hide screen video_call_window 
   
    #jump day1_call


    
    
