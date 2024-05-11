    # chat
    # day1: 7 total, 5 possible
    # day2: 16 total, 14 possible 
    # day3: 16 total, 12 possible
    # day4: 14 total, 12 possible 

    # 5+14+12+12 = 43

    # call (2 each)
    # day1: 3 total, 3 possible (6)
    # day2: 5 total, 5 possible (10)
    # day3: 4 total, 4 possible (8)
    # day4: 4 total, 4 possible (8)

    # 6+10+8+8 = 32

    # 75 total 

    # which end 
    # points_seekLove <= 25 = loss 
    # points_seekLove 25-50 = life 
    # points_seekLove >= 50 = love 

label day5_start: 

    $ chat_message("elimf: sup thrim")

    # MC: sup!
    $ player_choice(
        [
            ("sup!", "x")
        ]
    )

    $ chat_message("elimf: r u READY")

    $ chat_message("elimf: r u PSYCHED")

    $ player_choice(
        [
            ("for???", "day5_1"), 
            ("YEAH", "day5_2")
        ]
    )


    #[1] MC: for???
label day5_1: 
    $ points_seekLove -= 1

    $ chat_message("elimf: the finalest of hacks")

    #MC: oh!
    $ player_choice(
        [
            ("oh!", "x")
        ]
    )

    $ chat_message("wnpep: and then there was one",ot="elimf")

    $ chat_message("elimf: such a moment it is")

    jump day5_3


    #[2] MC: YEAH
label day5_2: 
    $ points_seekLove += 1

    $ chat_message("elimf: YEAHHHHHHHH",ot="incri")

    $ chat_message("incri: u dont even knwo whats happening")

    $ chat_message("elimf: dont squash their ungirdled enthusiasm")

    $ chat_message("wnpep: unbridled")

    $ chat_message("elimf: their ungirded enticement")

    $ chat_message("wnpep: sigh")

    jump day5_3


    # end choices
label day5_3: 

    $ chat_message("elimf: the day is upon us")

    $ chat_message("elimf: the suspense. its like suspension")

    $ chat_message("odxny: Yes, I will be finishing and executing my hack today.")

    $ chat_message("incri: hows it feel being in last")

    $ chat_message("odxny: I believe the saying goes \"save the best for last\"?")

    $ chat_message("incri: thats some insane coping")

    $ chat_message("odxny: What happened to calling me 'boss'?")

    $ chat_message("incri: that was a mistake",ot="wnpep")

    $ chat_message("wnpep: so whats the job?")

    $ chat_message("odxny: It's a pretty simple hack. No money involved this time.")

    $ chat_message("incri: then why do it")

    $ chat_message("elimf: for the good of our fellow men or smth right pep")

    $ chat_message("wnpep: close enough",ot="odxny")

    $ chat_message("odxny: More like for our good. Have to manage some final things for the server.")

    $ chat_message("incri: boring")

    $ chat_message("wnpep: is anything not boring to you")

    $ chat_message("incri: money")

    $ chat_message("elimf: LOL")

    ## seekL segment 

    $ chat_message("odxny: Thrim, feel like helping? ")

    $ player_choice(
        [
            ("i would like that!", "day5_4"), 
            ("sure why not", "day5_5")
        ]
    )


    #[1] MC: i would like that!
label day5_4: 
    $ points_seekLove += 1

    $ chat_message("odxny: Great. Cool.")

    jump day5_6


    #[2] MC: sure why not
label day5_5: 
    $ points_seekLove -= 1

    $ chat_message("odxny: k")

    jump day5_6


    # end choices
label day5_6: 

    $ chat_message("elimf: ooooo how chivalrous")

    $ chat_message("wnpep: or daring")

    $ chat_message("wnpep: just a few days in and od's already letting thrim touch the server")

    $ chat_message("elimf: so this is how it all ends")

    #MC: ty for the votes of confidence
    $ player_choice(
        [
            ("ty for the votes of confidence", "x")
        ]
    )

    $ chat_message("elimf: dw i am confident abt you")

    $ chat_message("elimf: r ability to break stuff",ot="incri")

    $ chat_message("incri: if yr gonna kill the server let me do it i desevre it")

    $ chat_message("odxny: A couple of your hacks have already tried.")

    pause 1 

    $ chat_message("incri: my hacks r perfect")

    $ chat_message("elimf: ly bad")

    $ chat_message("incri: stfu  u wish u cld hack like me asshole")

    $ chat_message("wnpep: we all quiver in awe of your feats")

    $ chat_message("incri: y tf are u asking abt my feet perv")

    $ chat_message("incri: thts not even how u fckn spell it")

    pause 1 

    $ chat_message("wnpep: i must not react. reacting is the mind-killer")

    $ chat_message("wnpep: i will permit it to pass over me and thru me.",ot="elimf")

    $ chat_message("elimf: LOLLLLLLLLLLLLLLLLLLL")

    $ chat_message("odxny: Missed a few lines there.")

    $ chat_message("wnpep: please just start the hack")

    $ chat_message("odxny: Lmao")

    #MC: so whatre we doing today?
    $ player_choice(
        [
            ("so whatre we doing today?", "x")
        ]
    )

    $ chat_message("odxny: Prepping the server shutdown, actually. Just need to get everything in place.")

    $ player_choice(
        [
            ("oh...", "day5_7"), 
            ("finally. say ur prayers hacker scum", "day5_8")
        ]
    )


    #[1] MC: oh...
label day5_7: 
    $ points_seekLove += 1

    $ chat_message("odxny: Had to be done sometime.",ot="incri")

    $ chat_message("incri: thrim crying alrdy lmao")

    $ chat_message("elimf: let em focus ")

    jump day5_9


    #[2] MC: finally. say ur prayers hacker scum 
label day5_8: 
    $ points_seekLove -= 1

    $ chat_message("wnpep: rude")

    $ chat_message("elimf: make it painless lord please we pray ",ot="incri")

    $ chat_message("incri: lets jst get this started",fastmode=True)

    jump day5_9 


    # end choices 
label day5_9: 

    $ chat_message("elimf: theyve gotta lay down the wire and the big red button")

    $ chat_message("elimf: or the handle box things miners use")

    $ chat_message("wnpep: the plunger?")

    $ chat_message("elimf: is that actually what its called")

    $ chat_message("elimf: insane",ot="odxny")

    $ chat_message("odxny: It's not going to be anything special. No Solitaire fireworks.")

    $ chat_message("odxny: We can do a countdown, though.")

    $ chat_message("wnpep: what like right now")

    $ chat_message("elimf: we need time to teach incy to count to 5")

    $ chat_message("incri: i can count to 5 ")

    $ chat_message("elimf: prove it")

    $ chat_message("incri: 1")

    $ chat_message("odxny: Ok that's enough.")

    $ chat_message("elimf: aw",ot="odxny")

    ## instructions

    $ chat_message("odxny: Thrim, this one will be a little different. ")

    $ chat_message("odxny: In order to shut the server down, we need to know the execution password. ")

    #MC: i'm assuming u already know that, right? 
    $ player_choice(
        [
            ("i'm assuming u already know that, right? ", "x")
        ]
    )

    $ chat_message("odxny: Right, but...")

    $ chat_message("odxny: ...where is the fun in that? ")

    $ chat_message("elimf: intriguing ",ot="wnpep")

    $ chat_message("wnpep: od? ",fastmode=True)

    $ chat_message("odxny: I've hidden pieces of the password in some tables you've scoured the past few days. ")

    $ chat_message("odxny: Ready for a hunt? ")

    $ player_choice(
        [
            ("is this going to be hard...............", "day5_10"), 
            ("omg. YES", "day5_11")
        ]
    )


    #[1] MC: is this going to be hard............... 
label day5_10: 
    $ points_seekLove -= 1

    $ chat_message("odxny: No harder than what you've done already? ")

    $ chat_message("odxny: Sorry. I thought this would be fun. ")

    jump day5_12


    #[2] MC: omg. YES 
label day5_11: 
    $ points_seekLove += 1

    $ chat_message("odxny: LMAO ")

    $ chat_message("odxny: Yes. Ha. Okay, cool. ",ot="wnpep")

    $ chat_message("wnpep: love the enthusiasm thrim ")

    jump day5_12


    # exit choices 
label day5_12: 

    $ chat_message("incri: don't fuck up thrim ")

    $ chat_message("incri: uve had like")

    $ chat_message("incri: THREE teachers ")

    $ chat_message("elimf: but if u do fuck up, its ok ")

    $ chat_message("elimf: to be clear we wont forgive u but. ")

    $ chat_message("elimf: u wont ever see us again after this anyway so who cares",ot="wnpep")

    $ chat_message("wnpep: i'll forgive you! ")

    $ chat_message("incri: shut up ",ot="odxny")

    $ chat_message("odxny: Ready to start? ")

    $ player_choice(
        [
            ("as i'll ever be...", "day5_13"), 
            ("yes!! let's go!! ", "day5_14")
        ]
    )


    #[1] MC: as i'll ever be...
label day5_13: 
    $ points_seekLove -= 1

    $ chat_message("odxny: Alright.")

    jump day5_15


    #[2] MC: yes!! let's go!! 
label day5_14: 
    $ points_seekLove += 1

    $ chat_message("odxny: Perfect. ")

    jump day5_15


    # end choices 
label day5_15: 

    ## PART ONE 

    $ chat_message("odxny: Part one-- if someone was cheating on their spouse, I think a great alias would be \"butt_slutt_wutt\"")
    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        exec_needed = None 
        required_runs["columns"] = ["email"]
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["secretsmooch.users"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = [("ss_cid", "98605-SS")]
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day5_19"

    $ chat_message("elimf: WHAT ",ot="incri")

    $ chat_message("incri: ??F????? ",ot="wnpep",fastmode=True)

    $ chat_message("wnpep: why are we back on this... ",ot="elimf")

    $ chat_message("elimf: LMAOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",fastmode=True)

    $ player_choice(
        [
            ("i'm sorry. WHAT ", "day5_16"), 
            ("oh, a most DIGNIFIED alias to use", "day5_17")
        ]
    )


    #[1] MC: i'm sorry. WHAT 
label day5_16: 
    $ points_seekLove -= 1

    $ chat_message("odxny: ROLL WITH IT BEFORE MY CONFIDENCE WEARS OFF PLEASE...")

    jump day5_18


    #[2] MC: oh, a most DIGNIFIED alias to use
label day5_17: 
    $ points_seekLove += 1

    $ chat_message("odxny: Please LOL ")

    jump day5_18


    # end choices 
label day5_18: 

    $ chat_message("elimf: genius. i shouldve had that idea")

    $ chat_message("elimf: od where'd you pull that from ")

    $ chat_message("odxny: Deep, deep within. ")

    $ chat_message("elimf: oh but of course, of course",ot="odxny")

    $ chat_message("odxny: Thrim. Mind fetching an email that is just perfect for that alias? ")

    # MC: right away! 
    $ player_choice(
        [
            ("right away! ", "x")
        ]
    )

    jump wait_start 


    # runs code -- searches for "butt_slutt_wutt" in secretsmooch.users 
label day5_19: 

    #MC: got it! "4242" 
    $ player_choice(
        [
            ("got it! \"4242\"", "x")
        ]
    )

    $ chat_message("incri: pattern reeks of cringe meaning UGH ")

    $ chat_message("incri: just sayi t and get it ovr with")

    $ chat_message("odxny: Not a guess? ")

    $ chat_message("wnpep: i think i know what it is lol")

    $ chat_message("elimf: ??? ",ot="wnpep")

    $ chat_message("wnpep: ever have a T9 cellphone, thrim? ")

    $ player_choice(
        [
            ("no, but...", "day5_20"), 
            ("omg. yes. 4242 is... ", "day5_21")
        ]
    )


    #[1] MC: no, but... 
label day5_20: 
    $ points_seekLove -= 1

    $ chat_message("wnpep: 4242 = haha.")

    jump day5_22


    #[2] MC: omg. yes. 4242 is... 
label day5_21: 
    $ points_seekLove += 1

    #MC: \"haha\". LOL 
    $ player_choice(
        [
            ("\"haha\". LOL", "x")
        ]
    )

    $ chat_message("wnpep: are we right, od? ")

    jump day5_22


    # end choices
label day5_22: 

    $ chat_message("odxny: Lmao. Yes. ",ot="incri")

    $ chat_message("incri: it just gets cringier ",ot="elimf")

    $ chat_message("elimf: boss. you've changed. ")

    $ chat_message("odxny: Am I not allowed to have fun here and there? ")

    $ chat_message("elimf: tell me where od is tied up pls ")

    $ chat_message("odxny: LMAO ")

    $ player_choice(
        [
            ("that's so cute lol. love that", "day5_23"), 
            ("T9 in current year. crazy", "day5_24")
        ]
    )


    #[1] MC: that's so cute lol. love that 
label day5_23:
    $ points_seekLove += 1

    $ chat_message("odxny: Uh. Yeah, thanks ",ot="incri")

    $ chat_message("incri: EWWWWWW ",ot="elimf",fastmode=True)

    $ chat_message("elimf: the mood is weird stop thsi ")

    pause 1 

    $ chat_message("elimf: or include me ")

    $ chat_message("odxny: No. ")

    jump day5_25


    #[2] MC: T9 in current year. crazy 
label day5_24: 
    $ points_seekLove -= 1

    $ chat_message("wnpep: i'd argue they should bring it back! it was so much faster to text ")

    $ chat_message("elimf: that just has to be a lie ")

    $ chat_message("wnpep: it's not! ")

    jump day5_25 


    # end choices 
label day5_25: 

    $ chat_message("odxny: Ready for the next one?")


    ## PART TWO 

    $ chat_message("odxny: Part two -- Someone at PRIDE has put in a strange coverage request for claim_type = \"TERMINATE\". Mind grabbing his email?") 
    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        exec_needed = None 
        required_runs["columns"] = ["email"]
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["irs.contacts"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = [("irs_id", "I83277-164")]
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day5_29"

    $ chat_message("incri: ?? ",ot="elimf")

    $ chat_message("elimf: aw is this an inside joke... ")

    $ chat_message("elimf: i feel so left out :( ")

    $ player_choice(
        [
            ("brother. me too", "day5_26"), 
            ("oh hooooooooo i got this! ", "day5_27")
        ]
    )


    #[1] MC: brother. me too 
label day5_26: 
    $ points_seekLove -= 1

    $ chat_message("wnpep: oh that's a great start ",ot="incri")

    $ chat_message("incri: lolllllll",ot="odxny")

    $ chat_message("odxny: It'll come to you. ")

    jump day5_28


    #[2] MC: oh hooooooooo i got this! 
label day5_27: 
    $ points_seekLove += 1

    $ chat_message("odxny: Never doubted. ")

    jump day5_28


    # end choices 
label day5_28: 

    $ chat_message("odxny: Use whatever seekL logic you'd like. ")

    $ chat_message("odxny: And let me know when you've found the email. ")

    jump wait_start 


    # runs code -- "Arnold Schwarzenegger" in joins pride.claims to irs.contacts 
label day5_29: 

    #MC: \"OWIE\"?? 
    $ player_choice(
        [
            ("\"OWIE\"??", "x")
        ]
    )

    $ chat_message("elimf: me when i ")

    $ chat_message("elimf: me when i when ",ot="incri")

    $ chat_message("incri: tf kind of password is sthis")

    $ chat_message("odxny: It's the original members' initials... ")

    pause 2

    $ chat_message("wnpep: aw. that's so sweet! ",ot="incri,elimf")

    $ chat_message("incri: cringe ",ot="elimf",fastmode=True)

    $ chat_message("elimf: cringe af ",fastmode=True)

    $ player_choice(
        [
            ("no \"T\" :( ", "day5_30"), 
            ("aw. a lil memorial in the sendoff", "day5_31")
        ]
    )


    #[1] MC: no "T" :( 
label day5_30: 
    $ points_seekLove -= 1

    $ chat_message("odxny: ....\"TOWIE\"? ",ot="elimf")

    $ chat_message("elimf: are we verging into babytalk here ")

    $ chat_message("incri: nononononononono")

    jump day5_32 


    #[2] MC: aw. a lil memorial in the sendoff 
label day5_31: 
    $ points_seekLove += 1

    $ chat_message("odxny: A bit. ",ot="wnpep")

    $ chat_message("wnpep: awwww. ")

    jump day5_32


    # end choices 
label day5_32:

    $ chat_message("odxny: Okay. Second part, \"OWIE\". Nice job. ")

    #MC: tytyty! 
    $ player_choice(
        [
            ("tytyty!", "x")
        ]
    )

    ## PART THREE 

    $ chat_message("odxny: Part three -- \"seekL\" may be about to die, but someone has to make sure nothing falls apart after and cover all our tracks. ")
    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        exec_needed = None 
        required_runs["columns"] = ["email"]
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["irs.contacts"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = [("irs_id", "I36375-168")]
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day5_36"

    $ chat_message("odxny: Can you find me the email for that living_contact? ")

    $ player_choice(
        [
            ("... this is VAGUE", "day5_33"), 
            ("okay... i think i know the table to go to.", "day5_34")
        ]
    )



    #[1] MC: ... this is VAGUE 
label day5_33: 
    $ points_seekLove -= 1

    $ chat_message("wnpep: cmon thrim! don't give up! ")

    $ chat_message("elimf: yea!! rah rah rah",ot="incri")

    $ chat_message("incri: trivial ")

    #MC: I'M THINKING.... 
    $ player_choice(
        [
            ("I'M THINKING....", "x")
        ]
    )

    jump day5_35 


    #[2] MC: okay... i think i know the table to go to. 
label day5_34: 
    $ points_seekLove += 1

    $ chat_message("odxny: Excellent. ",ot="wnpep")

    $ chat_message("wnpep: too easy for thrim! ")

    jump day5_35


    # end choices 
label day5_35: 

    $ chat_message("wnpep: is this the last part? ")

    $ chat_message("odxny: Yep. Nearing the end. ")

    $ chat_message("incri: go thrim. kill us ")

    $ chat_message("elimf: LOL ",ot="odxny")

    $ chat_message("odxny: Let me know when you have it. ")

    jump wait_start 


    # runs code -- finds odxny in living_contact and connects to irs.contacts for email 
label day5_36: 

    #MC: \"TYVM\"?
    $ player_choice(
        [
            ("\"TYVM\"?", "x")
        ]
    )

    $ chat_message("incri: no more cheesey bullsht no ")

    $ chat_message("odxny: Hold on, now. It means...")

    $ chat_message("odxny: \"Thank you very much. For all the cold hard cash.\" ")

    $ chat_message("incri: ok. i agree ")

    $ chat_message("incri: thank u stupid world",ot="elimf")

    $ chat_message("elimf: mm yes. thank u ")

    $ chat_message("elimf: my life has most definitely improved due to their stupidness ")

    pause 1

    $ chat_message("odxny: \"...And thank you for being here with me.\" ")

    $ chat_message("incri: NO MORE",ot="elimf,wnpep")

    $ chat_message("elimf: BOOOOOOOOOOO",ot="wnpep",fastmode=True)

    $ chat_message("wnpep: thank you as well. ")

    #MC: aww. thought you all didn't care about each other 
    $ player_choice(
        [
            ("aww. thought you all didn't care about each other ", "x")
        ]
    )

    $ chat_message("incri: I HATE ALL OF U A LOT ")

    $ chat_message("elimf: even me </3 ")

    $ chat_message("incri: fkin espcially u ")

    $ chat_message("elimf: how will my shattered heart mend again ",ot="wnpep")

    $ chat_message("wnpep: that the whole thing then? ")

    $ chat_message("odxny: \"4242OWIETYVM\". That's it.") 

    $ chat_message("odxny: Thank you for indulging me, Thrim. ")

    ## END SEGMENT 

    $ chat_message("elimf: our flawless marvelous leader wins again")

    $ chat_message("wnpep: always a pleasure to see you work")

    # if low favor
    if points_seekLove < 25: 

        $ chat_message("odxny: Not the most elegant, but it'll get the response I need.")

    # if good favor
    else: 

        $ chat_message("odxny: You flatter me.")

        $ chat_message("odxny: But yes, I think that went pretty well.")

    # end branches

    $ chat_message("incri: it was.. .  fine")

    $ chat_message("elimf: all thanks to our baby prodigy thrim")

    $ player_choice(
        [
            ("thank u for the very sincere compliment", "day5_37"), 
            ("always glad to assist", "day5_38")
        ]
    )


    #[1] MC: thank u for the very sincere compliment
label day5_37: 

    $ chat_message("elimf: yw my incredibly talented companion")

    #MC: truly we are both great minds
    $ player_choice(
        [
            ("truly we are both great minds", "x")
        ]
    )

    $ chat_message("elimf: the most gifted",ot="incri")

    $ chat_message("incri: ur gonna make me sick")

    jump day5_41

    

    #[2] MC: always glad to assist
label day5_38: 

    $ chat_message("elimf: ur our lil Igor")

    $ player_choice(
        [
            ("are u all frankenstein then?", "day5_39"), 
            ("????", "day5_40")
        ]
    )


    #[2-1] MC: are u all frankenstein then?
label day5_39: 

    $ chat_message("wnpep: i dont claim that")

    $ chat_message("elimf: not even for the kickass lab coat?")

    $ chat_message("wnpep: what?? no")

    $ chat_message("elimf: :^(")

    jump day5_41


    #[2-2] MC: ????
label day5_40: 

    $ chat_message("elimf: nvm",ot="wnpep")

    $ chat_message("wnpep: your new homework is to read frankenstein")

    $ chat_message("elimf: or watch young frankenstein")

    $ chat_message("wnpep: an acceptable substitute")

    jump day5_41


    # end subchoices

    # end choices
label day5_41: 

    $ chat_message("incri: ughhhhhh")

    $ chat_message("elimf: what ails u")

    $ chat_message("incri: how long do we have to wait")

    #$ chat_message("odxny: We can't all target chronically online cops.")

    $ chat_message("elimf: so impatient to see us go")

    $ chat_message("elimf: wont u miss us dear incy")

    $ chat_message("incri: dear what")

    $ chat_message("elimf: my incy")

    $ chat_message("elimf: like inky but with a c",ot="incri")

    $ chat_message("incri: bad",fastmode=True)

    $ chat_message("wnpep: it is pretty bad")

    $ chat_message("wnpep: reads like in-see")

    $ player_choice(
        [
            ("i read it as inky!", "day5_42"), 
            ("oh... it does...", "day5_43")
        ]
    )


    #[1] MC: i read it as inky!
label day5_42: 

    $ chat_message("elimf: my baby prodigys always got me")

    jump day5_44


    #[2] MC: oh... it does...
label day5_43: 

    $ chat_message("elimf: no one acknowledges my crafts and labors")

    jump day5_44


    # end choices
label day5_44: 

    $ chat_message("odxny: To get back on track, I'll start the countdown in a few minutes.")

    $ chat_message("incri: do we have t wait for that")

    $ chat_message("incri: bc im bored")

    $ chat_message("elimf: what a development")

    $ chat_message("incri: stfu",ot="odxny")

    $ chat_message("odxny: It gives us extra time to say our goodbyes.")

    $ chat_message("elimf: awwwwwwwwwwwwwwww")

    $ chat_message("incri: thrims rubbing off on fckin both of u")

    $ chat_message("incri: fckn saps")

    #MC: pls
    $ player_choice(
        [
            ("pls", "x")
        ]
    )

    $ chat_message("incri: i cld be doing oether things")

    $ chat_message("elimf: getting more parking tickets so u have more hacks to hack")

    $ chat_message("incri: that was one time and their fault i wasnt even over time")

    $ chat_message("incri: fkn asshole just wanted to make pme pay")

    $ chat_message("incri: honeslty 50k wasnt even enough i shouldve charged more")

    # incri typing

    jump day5_choose_end 



label day5_choose_end: 

    python: 
        if points_seekLove <= 25: 
            renpy.jump("day5_seekLoss_chat")
        elif points_seekLove <= 50: 
            renpy.jump("day5_seekLife_chat")
        else: 
            renpy.jump("day5_seekLove_chat")


label day5_seekLoss_chat: 

    $ chat_message("wnpep: well. we prob should do smth before we set off")

    $ chat_message("wnpep: any ideas?")

    $ chat_message("odxny: None at the moment.",ot="elimf")

    $ chat_message("elimf: i have one",fastmode=True)

    $ chat_message("wnpep: i think i can guess what youre going for.")

    pause 1 

    $ chat_message("incri: fbi in house")

    $ chat_message("elimf: fuck")

    $ player_choice(
        [
            ("what?", "x")
        ]
    )

    pause 2 

    ## NEED A CRASH SOUND 
    stop music 
    #play sound "audio/sfx/ui_menu_back_001 hangup.ogg"

    $ quick_menu = False
    $ _preferences.afm_enable = False 

    $ persistent.seekLoss = True 

    show screen game_over
    pause 4.0 
    show screen game_over_text with Dissolve(2.0) 
    #pause 3.0 
    #play sound "audio/sfx/ui_menu_back_001 hangup.ogg"

    

    # program shuts down

    # end

    $ renpy.pause(hard=True)


label day5_seekLife_chat: 

    $ chat_message("wnpep: whats important is that now we can celebrate and send ourselves off")

    $ chat_message("elimf: ofc we gotta pop some bottles before we go",ot="incri")

    $ chat_message("incri: im just here to see u idiots not realize ohw much ull miss me")

    $ chat_message("elimf: uhhhhhhh")

    $ chat_message("wnpep: i'll admit i'll miss this a bit but we knew the terms going in")

    $ chat_message("wnpep: on to better things")

    $ chat_message("incri: like what")

    $ chat_message("incri: wats better than me")

    $ player_choice(
        [
            ("ur kind of setting yourself up there", "day5_seekLife_1"), 
            ("nothing honestly. they just dont get it", "day5_seekLife_2")
        ]
    )


    #[1] MC: ur kind of setting yourself up there
label day5_seekLife_1: 

    $ chat_message("incri: whatever they say theyre wrong")

    $ chat_message("wnpep: sorry for putting my daughter in first place")

    $ chat_message("incri: can ur daughter do the hacks i can")

    $ chat_message("elimf: theyve got u there")

    $ chat_message("wnpep: yeah sure u got me")

    $ chat_message("wnpep: ill concede that u are better than the daughter i held and raised")

    $ chat_message("incri: thats right bich")

    jump day5_seekLife_3


    #[2] MC: nothing honestly. they just dont get it
label day5_seekLife_2: 

    $ chat_message("incri: thank u")

    pause 1

    $ chat_message("incri: wait")

    $ chat_message("elimf: LOL",ot="incri")

    $ chat_message("incri: fuck u stop fuckign clowning")

    $ chat_message("odxny: What do you mean, they're undoubtedly being sincere.",ot="wnpep")

    $ chat_message("wnpep: ahahahaha",fastmode=True)

    jump day5_seekLife_3


    # end choices
label day5_seekLife_3: 

    $ chat_message("elimf: lololol")

    $ chat_message("elimf: this was fun while it lasted tho")

    $ chat_message("elimf: we're a lot of ships leaving at the same time. friendly ships waving our sails")

    # dms

    # SET ADMIN CHAT ON OR SOMTH

    $ chat_message("odxny: Final words before the end?", c="admin")

    #$ active_window = "admin"

    #MC: last call already huh
    $ player_choice(
        [
            ("last call already huh", "x")
        ]
    )

    $ chat_message("odxny: Yup. Even elimf didn't drag their feet about it.", c="admin")

    $ chat_message("odxny: They were all at least a little clear headed when it came to their goals.", c="admin")

    #MC: that almost sounded like a compliment
    $ player_choice(
        [
            ("that almost sounded like a compliment", "x")
        ]
    )

    $ chat_message("odxny: I can give those out from time to time. They've earned it.", c="admin")

    #MC: you sound like youve grown a little fond of them
    $ player_choice(
        [
            ("you sound like youve grown a little fond of them", "x")
        ]
    )

    $ chat_message("odxny: Maybe. ", c="admin")

    $ chat_message("odxny: Doesn't mean I won't shut things down, though.", c="admin")

    #MC: I wasnt expecting you to change course
    $ player_choice(
        [
            ("I wasnt expecting you to change course", "x")
        ]
    )

    $ chat_message("odxny: But you do want something.", c="admin")

    #MC: ha. you got me
    $ player_choice(
        [
            ("ha. you got me", "x")
        ]
    )

    #MC: i was just hoping that maybe...our talks and your time with everyone swayed you to give people another shot
    $ player_choice(
        [
            ("i was just hoping that maybe...our talks and your time with everyone swayed you to give people another shot", "x")
        ]
    )

    $ chat_message("odxny: You think talking to incri pushed the needle in a positive direction?", c="admin")

    $ chat_message("odxny: I kid. I've been thinking a lot, to tell you the truth.", c="admin")

    $ chat_message("odxny: And I think you may be right.", c="admin")

    #MC: i'm glad.
    $ player_choice(
        [
            ("i'm glad.", "x")
        ]
    )

    $ chat_message("odxny: It may not fix anything. ", c="admin")

    #MC: that's true
    $ player_choice(
        [
            ("that's true", "x")
        ]
    )

    $ chat_message("odxny: But I'll try.", c="admin")

    #MC: thats more than enough for me
    $ player_choice(
        [
            ("thats more than enough for me", "x")
        ]
    )

    $ chat_message("odxny: Thank you.", c="admin")

    # general

    $ chat_message("incri: so r we blowing this up or what")

    $ chat_message("odxny: I'll shut everything down in, let's say, 60 seconds. Enough time for one last goodbye.")

    $ chat_message("wnpep: sounds good",ot="elimf")

    $ chat_message("elimf: ill miss u all a little. and then forget it all wasnt a dream")

    $ chat_message("elimf: u will be there at the bottom of every bong")

    $ chat_message("wnpep: what an honor.",ot="incri")

    $ chat_message("incri: goodbye i will miss none of u")

    $ chat_message("incri: cry bc u wont get to see me nymore")

    $ chat_message("elimf: already got the tissues ready",ot="odxny")

    $ chat_message("odxny: 30 seconds.",fastmode=True)

    $ chat_message("wnpep: i cant reuse the muppets quote but i will think somewhat kindly of this meeting and parting")

    $ chat_message("incri: wow deep")

    $ chat_message("wnpep: let it be known that i tried",ot="odxny")

    $ chat_message("odxny: I will say that I also enjoyed this somewhat.")

    $ chat_message("odxny: Thank you all for participating and I wish you well.")

    #MC: thank you all for tolerating me in the short time i was here
    $ player_choice(
        [
            ("thank you all for tolerating me in the short time i was here", "x")
        ]
    )

    $ chat_message("wnpep: it was no trouble",ot="elimf")

    $ chat_message("elimf: i had fun with it dw")

    $ chat_message("odxny: Agreed. Thanks for being here.")

    #MC: of course!
    $ player_choice(
        [
            ("of course!", "x")
        ]
    )

    $ chat_message("odxny: And with that, we are at 5")

    $ chat_message("odxny: 4",ot="wnpep")

    $ chat_message("wnpep: goodbye everyone!")

    $ chat_message("odxny: 3",ot="incri,elimf",fastmode=True)

    $ chat_message("incri: bye losrs ",ot="elimf")

    $ chat_message("elimf: see u never :^)",fastmode=True)

    $ chat_message("odxny: 2",fastmode=True)

    $ player_choice(
        [
            ("goodbye!!!!!!", "day5_seekLife_4"), 
            ("AHHHHHHHHHHHHH", "day5_seekLife_5")
        ]
    )


    #[1] MC: goodbye!!!!!!
label day5_seekLife_4: 

    $ chat_message("wnpep: live well!")

    jump day5_seekLife_6


    #[2] MC: AHHHHHHHHHHHHH
label day5_seekLife_5: 

    $ chat_message("elimf: AHHHHHHHHHHHHHHHHHHHHHHH!!!!")

    jump day5_seekLife_6


    # end choices
label day5_seekLife_6: 

    $ chat_message("odxny: 1",fastmode=True)

    # server shut down

    pause 1 

    play sound "audio/sfx/ui_menu_back_001 hangup.ogg"

    $ quick_menu = False
    $ _preferences.afm_enable = False 

    hide screen seekL_ui 

    pause 4 

    ##### for platonic route camera pans ###########################
    show cg platonic 
    camera:
        zoom 1.60 xpos -2313 ypos -486
        linear 5.0 xpos -1602
    with dissolve
    pause 4.8

    show cg platonic 
    camera:
        zoom 1.60 xpos 144 ypos 423
        linear 5.0 ypos 792
    with dissolve
    pause 4.8

    show cg platonic 
    camera:
        zoom 0.57 xpos 486 ypos 540
        linear 10.0 zoom 0.5
    with dissolve 

    pause 1.0 
    show screen game_over_neutral_text with Dissolve(2.0) 
    $ persistent.seekLife = True 
    $ _preferences.afm_enable = False

    pause 

    hide screen game_over_neutral_text with dissolve

    scene black 
    camera: 
        subpixel True pos (0,0) zoom 1.0
    with dissolve

    stop music fadeout 3.0 

    pause 4 

    return 



label day5_seekLove_chat: 

    $ chat_message("wnpep: id say it's abt time to pop the proverbial bottles")

    $ chat_message("elimf: or real ones?? haha imagine")

    pause 1 

    $ chat_message("elimf: unless??",ot="wnpep")

    $ chat_message("wnpep: ill crack open a beer just for you")

    $ chat_message("elimf: we will have a spring wedding")

    $ chat_message("wnpep: i dont think")

    $ chat_message("elimf: it should be ok bc ur not married right")

    $ chat_message("wnpep: im gonna go get that beer")

    $ chat_message("incri: left before u even got to the altar. BRUTAL")

    $ player_choice(
        [
            ("this party vibe is getting kind of weird", "day5_seekLove_1"), 
            ("i was just about to offer to be your wedding dj", "day5_seekLove_2")
        ]
    )


    #[1] MC: this party vibe is getting kind of weird
label day5_seekLove_1: 

    $ chat_message("elimf: sorry im not good enough for pep")

    jump day5_seekLove_3


    #[2] MC: i was just about to offer to be your wedding dj
label day5_seekLove_2: 

    $ chat_message("elimf: god damn it we couldve had it all")

    jump day5_seekLove_3


    # end choices
label day5_seekLove_3: 

    $ chat_message("odxny: We still have our current party.")

    $ chat_message("elimf: the day is saved",ot="wnpep")

    $ chat_message("wnpep: back",fastmode=True)

    $ chat_message("elimf: nobody address my ex")

    $ chat_message("incri: dw u can leave it when u begin the rest of ur sad life after this")

    $ chat_message("elimf: thats the nicest thing uve ever said to me",ot="incri")

    $ chat_message("incri: ur sad pathetic life",ot="wnpep")

    $ chat_message("wnpep: itll always be a little wistful")

    $ chat_message("wnpep: especially when it comes to my jilted ex")

    $ chat_message("elimf: did u hear something",ot="wnpep")

    $ chat_message("wnpep: what times we had ",ot="incri")

    $ chat_message("incri: UGH",fastmode=True)

    $ chat_message("incri: can we talk abt smth else")

    $ chat_message("elimf: after all our work incri is still allergic to love")

    $ chat_message("wnpep: surely this experience has softened them a little?")

    $ chat_message("wnpep: i feel like incris gotten smth out of this, even if they wont admit to it")

    $ chat_message("incri: i alrdy know everything")

    # dms

    $ chat_message("odxny: Hey.",c="admin")

    $ player_choice(
        [
            ("hey?", "day5_seekLove_4"), 
            ("hey!!!!", "day5_seekLove_5")
        ]
    )


    #[1] MC: hey?
label day5_seekLove_4: 

    $ chat_message("odxny: Yes. Hey. Why the confusion?",c="admin")

    #MC: dunno actually. maybe the informality of it
    $ player_choice(
        [
            ("dunno actually. maybe the informality of it", "x")
        ]
    )

    $ chat_message("odxny: I'm capable of more than one register.",c="admin")

    #MC: there really is no end to ur skill
    $ player_choice(
        [
            ("there really is no end to ur skill", "x")
        ]
    )

    $ chat_message("odxny: We're getting off track.",c="admin")

    jump day5_seekLove_6


    #[2] MC: hey!!!!
label day5_seekLove_5: 

    $ chat_message("odxny: Such an enthused reception.",c="admin")

    #MC: i'm just happy to see u!
    $ player_choice(
        [
            ("i'm just happy to see u!", "x")
        ]
    )

    $ chat_message("odxny: I'm that exciting?",c="admin")

    #MC: yea!!!
    $ player_choice(
        [
            ("yea!!!", "x")
        ]
    )

    # typing
    pause 2

    $ chat_message("odxny: Interesting.",c="admin")

    $ chat_message("odxny: But we're getting off track.",c="admin")

    jump day5_seekLove_6


    # end choices
label day5_seekLove_6: 

    $ chat_message("odxny: I'm just sending you something before the program shuts down.",c="admin")

    #MC: oh?
    $ player_choice(
        [
            ("oh?", "x")
        ]
    )

    $ chat_message("odxny: A new function.",c="admin")

    $ chat_message("odxny: `exec dial()`",c="admin")

    $ player_choice(
        [
            ("and what exactly do i put in those parentheses this time?", "x")
        ]
    )

    $ chat_message("odxny: Heard a phone number might work.",c="admin")

    #MC: hmm. suspicious
    $ player_choice(
        [
            ("hmm. suspicious", "x")
        ]
    )

    $ chat_message("odxny: Oh, now we're worried about privacy.",c="admin")

    #MC: i was joking!!
    $ player_choice(
        [
            ("i was joking!!", "x")
        ]
    )

    $ chat_message("odxny: Mhm.",c="admin")

    #MC: i will call it, promise
    $ player_choice(
        [
            ("i will use it, promise", "x")
        ]
    )

    $ chat_message("odxny: You're so trusting.",c="admin")

    #MC: oh my god!! enough!!
    $ player_choice(
        [
            ("oh my god!! enough!!", "x")
        ]
    )

    $ chat_message("odxny: Sorry, couldn't resist.",c="admin")

    $ chat_message("odxny: But thank you for promising.",c="admin")

    #MC: youre WELCOME
    $ player_choice(
        [
            ("youre WELCOME", "x")
        ]
    )

    $ chat_message("odxny: LMAO",c="admin")

    $ player_choice(
        [
            ("but, wait, i need your number!", "x")
        ]
    )

    $ chat_message("odxny: Yes! And, I've left it for you.",c="admin")

    $ chat_message("odxny: I'm sure you can find it.",c="admin")

    $ player_choice(
        [
            ("wow.", "x")
        ]
    )

    # general

    $ chat_message("wnpep: spose we should get this show on the road")

    $ chat_message("elimf: what a dad-ism")

    $ chat_message("wnpep: i can't deny who i am")

    $ chat_message("incri: ya u alrdy outed urself ")

    $ chat_message("wnpep: yes i remember thank you")

    $ chat_message("incri: as u should. thank me more")

    $ chat_message("wnpep: thank you for making me miss this a little less")

    $ chat_message("incri: YOULL MISS ME AND U KNOW IT")

    $ chat_message("elimf: dw we all will every time the tinnitus kicks in")

    $ chat_message("odxny: I'll set the timer to 60 seconds so everyone can say their goodbyes before I hit the switch.")

    $ chat_message("wnpep: thats fair")

    #wnpep typing
    $ chat_message("wnpep: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",ot="elimf",nooutput=True)

    $ chat_message("elimf: yea its almost enough time for one of ur shorter speeches")

    #stops, types again

    pause 1 

    $ chat_message("wnpep: touche")

    $ chat_message("incri: i have nothing to say to u clowns")

    $ player_choice(
        [
            ("honk honk", "day5_seekLove_7"), 
            ("</3", "day5_seekLove_8")
        ]
    )


    #[1] MC: honk honk
label day5_seekLove_7: 

    $ chat_message("elimf: LOL",ot="incri")

    $ chat_message("incri: shutf the fuck up")

    jump day5_seekLove_9


    #[2] MC: </3
label day5_seekLove_8: 

    $ chat_message("incri: get tht away form me")

    jump day5_seekLove_9


    # end choices
label day5_seekLove_9: 

    # $ chat_message("elimf: has our time frolicking together meant nothing 2 u </3")

    # $ chat_message("incri: wtf")

    $ chat_message("elimf: ur so heartless")

    $ chat_message("incri: ur beneath me")

    $ chat_message("elimf: im p versatile :^)")

    $ chat_message("incri: UGH",ot="odxny")

    $ chat_message("odxny: If we're ready I'm starting the timer.")

    $ chat_message("wnpep: ill start and say i think this has amounted to a pretty alright experience")

    $ chat_message("wnpep: you all have at least some good qualities")

    $ chat_message("elimf: awwwww",ot="incri")

    $ chat_message("incri: ew",ot="elimf",fastmode=True)

    $ chat_message("elimf: u too pep")

    $ chat_message("wnpep: i try")

    $ chat_message("elimf: yes often")

    $ chat_message("elimf: very very very often")

    $ chat_message("wnpep: alright already",ot="elimf")

    $ chat_message("elimf: in return as a show of my magnum gratitude i will bestow my sincerity upon u all")

    #MC: oh???
    $ player_choice(
        [
            ("oh???", "x")
        ]
    )

    $ chat_message("incri: hate")

    $ chat_message("incri: dont want it",ot="elimf")

    $ chat_message("elimf: i will bestow it nonetheless")

    $ chat_message("wnpep: o frabjous day",ot="odxny")

    $ chat_message("odxny: 30 seconds",fastmode=True)

    $ chat_message("elimf: u were all at least entertaining ")

    $ chat_message("elimf: not like a movie but like. a good tv episode or a special")

    $ chat_message("elimf: i will dedicate to u at least one bong hit each")

    $ chat_message("wnpep: i have never felt so honored",ot="incri")

    $ chat_message("incri: choke n cough on it ",fastmode=True)

    $ chat_message("elimf: in the spirit of harmony i will not take the opening u just gave me")

    $ chat_message("odxny: For my part I'll say I enjoyed this at least somewhat. You all were certainly interesting.")

    $ chat_message("wnpep: we really never had a dull moment")

    $ chat_message("incri: speak for urself u all were boring")

    $ chat_message("wnpep: were we?")

    $ chat_message("incri: u all were mostly boring",ot="odxny")

    $ chat_message("odxny: 15 seconds.",fastmode=True)

    $ player_choice(
        [
            ("even tho our time was short i'll miss u guys!", "day5_seekLove_10"), 
            ("thanks for teaching me, ill do my best w what ive learned!", "day5_seekLove_11")
        ]
    )
    

    #[1] MC: even tho our time was short i'll miss u guys!
label day5_seekLove_10: 

    $ chat_message("incri: undertsandable but try not to cry over me")

    $ chat_message("wnpep: im both glad and sorry to have made that much of an impression that quickly")

    #MC: its ok!! im happy to have been here!
    $ player_choice(
        [
            ("its ok!! im happy to have been here!", "x")
        ]
    )

    $ chat_message("odxny: I second the sentiment.")

    $ chat_message("elimf: aww u even got the boss")

    $ chat_message("wnpep: no one is immune to sincerity")

    jump day5_seekLove_12


    #[2] MC: thanks for teaching me, ill do my best w what ive learned!
label day5_seekLove_11: 

    $ chat_message("elimf: go forth brave one. i believe")

    #MC: thank u for ur support
    $ player_choice(
        [
            ("thank u for ur support", "x")
        ]
    )

    $ chat_message("incri: wait whats ur info i get a cut as ur teacher")

    $ chat_message("odxny: A little late for that.")

    $ chat_message("incri: NO",ot="wnpep")

    $ chat_message("wnpep: well, good luck and godspeed. just dont credit us if u get caught by the feds")

    $ chat_message("incri: amns, d,ml",ot="elimf")

    $ chat_message("elimf: LOL",fastmode=True)

    jump day5_seekLove_12


    #end choices
label day5_seekLove_12: 

    $ chat_message("odxny: And with that, we are at 5")

    $ chat_message("odxny: 4")

    $ chat_message("incri: bye",ot="odxny")

    $ chat_message("odxny: 3",fastmode=True)

    $ chat_message("wnpep: farewell and thanks for all the fish!")

    $ chat_message("odxny: 2",ot="elimf",fastmode=True)

    $ chat_message("elimf: bye forever :^)")

    $ chat_message("odxny: 1",fastmode=True)

    $ func_access_dial = True 

    # server shut down

    # short credits

    pause 1 

    # shut down server stuff 

    stop music 
    play sound "audio/sfx/data_loaded_001.ogg"
    #$ defenses = True 
    hide screen seekL_ui with Dissolve(0.1)
    pause 0.2
    $ server_kill = True
    $ at_end = True 
    $ player_is_waiting = True 
    $ _preferences.afm_enable = False 

    $ reset_chats() 

    pause 2

    show screen seekL_ui with Dissolve(2.0)
    
    #show screen phonecall_window_real

    #jump day5_seekLove_call

    ## maybe instead of showing the screen, we have the player execute a command 
    ## and that command will let you start up a call if the number works 
    #show screen secure_dial 
    $ renpy.pause(hard=True)