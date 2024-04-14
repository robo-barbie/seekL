label day2_start: 
    show screen seekL_ui 
    $ in_call = False

    $ player_choice(
        [
            ("hi again", "day2_1"), 
            ("im back. boo me again", "day2_2"), 
            ("goooooooooooooooooooooooooooood mornin!", "day2_3")
        ]
    )


label day2_1: 

    $ chat_message("wnpep: the not fed returns")

    #MC: what a title. can i earn a cooler one?
    $ player_choice(
        [
            ("what a title. can i earn a cooler one?", "x")
        ]
    )

    $ chat_message("wnpep: well this isnt the nineties so. no")

    $ chat_message("elimf: speak for yourself i've got a hugeass Hackerman banner")

    $ chat_message("elimf: for motivation and courage", ot="wnpep")

    $ chat_message("wnpep: thats not")

    $ chat_message("wnpep: you know what im just going to let this pass")

    $ chat_message("elimf: so unlike u", ot="wnpep")

    $ chat_message("wnpep: i refuse to let you force my hand")

    $ chat_message("wnpep: explaining things will just make me feel old again")

    $ chat_message("elimf: your loss")

    $ chat_message("elimf: i couldve learned something")

    pause 1 

    $ chat_message("wnpep: i mean. do you want to learn something? ")
    
    jump day2_4


label day2_2: 

    $ chat_message("incri: dont tell me what to do ")

    $ chat_message("incri: maybe ill eb nice just becuause then")

    #MC: well i'm not going to stop you
    $ player_choice(
        [
            ("well i'm not going to stop you", "x")
        ]
    )

    $ chat_message("wnpep: can we see some of that?")

    $ chat_message("incr: kindly fuck off")

    $ chat_message("wnpep: yea alright")

    $ chat_message("elimf: shocking")
    
    jump day2_4


label day2_3:

    $ chat_message("elimf: thaaaaaaaaaaaaaaaaaaaaaaaaaaaaank youuuuuuuuuuuuuuuu")

    #MC: yyyouuuureeeeeeee weeeellcoommmmeeeeeeeeeeee
    $ player_choice(
        [
            ("yyyouuuureeeeeeee weeeellcoommmmeeeeeeeeeeee", "x")
        ]
    )

    $ chat_message("elimf: ur like. a ripple in my puddle. ur good")

    $ chat_message("wnpep: my opinion might be worsening actually.")

    $ chat_message("elimf: embrace the newfound presence of someone useless but entertaining")

    #MC: now hold on
    $ player_choice(
        [
            ("now hold on", "x")
        ]
    )

    jump day2_4
 

label day2_4: 
    $ chat_message("incri: shut up shut up shutup")

    $ chat_message("elimf: careful we'll distract incri and ruin their \"art\" ")

    $ chat_message("incri: shut upppp")

    $ chat_message("incri: ur such a fking loser. bitch. idiot")

    $ chat_message("elimf: dumb also")

    # incri typing

    $ chat_message("wnpep: lets redirect the conversation a little")

    $ chat_message("wnpep: incri, hows progress? ")

    $ chat_message("incri: up yuours")

    $ chat_message("wnpep: alright ")

    $ chat_message("elimf: u keep letting this happen")

    $ chat_message("wnpep: i know i am, and yet i keep stepping on that rake")

    $ chat_message("incri: not that u care but im almost done")

    $ chat_message("incri: low lvl gov sht is easyyyy")

    #MC: is that what ur looking at? 
    $ player_choice(
        [
            ("is that what ur looking at? ", "x")
        ]
    )

    $ chat_message("incri: wat do u care. fed. narc")

    $ chat_message("elimf: does ur head explode when cashiers ask if u found everything okay")

    $ chat_message("wnpep: i would hope not, theyre just trying to do their jobs")

    #MC: sorry, i was just curious about your process w the program
    $ player_choice(
        [
            ("sorry, i was just curious about your process w the program", "x")
        ]
    )

    $ chat_message("elimf: not the sincerity. bold maneuver")

    $ chat_message("incri: sucking up wont work")

    $ chat_message("incri: my techniques r beyond u")

    pause 1

    $ chat_message("incri: acutlaly")

    $ chat_message("incri: i  just thought of smth")

    $ chat_message("elimf: oh boy")

    $ chat_message("incri: i will teach u onet hing ONLY")

    $ chat_message("incri: its so easy even u should get it")

    #MC: …thanks
    $ player_choice(
        [
            ("...thanks", "x")
        ]
    )

    $ chat_message("incri: databse searching n stuff")

    $ chat_message("incri: u find the stuff and tell me and i'll do the advanced shit")

    $ chat_message("wnpep: now that sounds a little")

    $ chat_message("elimf: incri uncovers a 1000 iq chess move: making someone else do the work")

    $ chat_message("wnpep: took the words out of my mouth")

    $ chat_message("wnpep: couldnt resist the siren call of unpaid labor")

    $ chat_message("incri: jealous fcking blowhards thats not it")

    $ chat_message("incri: its educational")

    $ chat_message("incri: im being so HELPFUL")

    $ chat_message("elimf: uh huh absolutely")

    $ chat_message("wnpep: we would never doubt you")

    #MC: I would be very grateful
    $ player_choice(
        [
            ("I would be very grateful", "x")
        ]
    )

    $ chat_message("incri: never ask me for anyhhing again")

    $ chat_message("elimf: my god theyre still going for it")

    $ chat_message("wnpep: we have to give credit for the sheer lack of shame")

    #MC: er, you didn't have to do all this
    $ player_choice(
        [
            ("er, you didn't have to do all this", "x")
        ]
    )

    $ chat_message("incri: no now i  have to")

    $ chat_message("incri: lets show thse fucking clowns")

    $ chat_message("incri: get in the program")

    #### SEEKL SEGMENT BEGINS 

    #MC: i'm in. like since i logged in
    $ player_choice(
        [
            ("i'm in. like since i logged in", "day2_5"), 
            ("you get in the program", "day2_6")
        ]
    )

label day2_5: 
    $ chat_message("incri: shut up and listen ")
    jump day2_7


label day2_6: 
    $ chat_message("incri: ur sooooo funny hahahahaha")
    jump day2_7

label day2_7:

    $ chat_message("incri: i already have his badge numbr ")

    $ chat_message("incri: go pull up the table azgov.police_info")
    
    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = None 
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["azgov.police_info"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = None 
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 

    $ chat_message("elimf: ur in arizona????")

    $ chat_message("incri: no i'm not ufcker ")

    $ chat_message("incri: i just passed through ",ot="wnpep")

    $ chat_message("wnpep: i'm uncomfortable knowing this much about incri ",ot="elimf")

    $ chat_message("elimf: arizona... ",ot="incri")

    $ chat_message("incri: fuck ",fastmode=True)

    $ chat_message("incri: pull it up thrim ",ot="wnpep")

    $ chat_message("wnpep: remember ")

    $ chat_message("wnpep: `select * from azgov.police_info`")

    jump day2_8

label day2_8:
    # wait for input 
    $ player_is_waiting = True 
    $ waiting_label = "day2_9"

    # if they arrive already ready to pass 
    if player_can_pass:
        $ player_is_waiting = False 
        jump day2_9 
    $ renpy.pause(hard=True)

label day2_9:
    $ player_is_waiting = False 
    #MC: I see the table now. 
    $ player_choice(
        [
            ("I see the table now. ", "x")
        ]
    )

    $ chat_message("incri: ok do u see ths badge number ")

    $ chat_message("incri: 55242 ")

    $ player_choice(
        [
            ("yes, i see it ", "day2_10"), 
            ("no?", "day2_11")
        ]
    )

    #[1] MC: yes, i see it 
label day2_10: 

    $ chat_message("incri: ez ")
    jump day2_12


    #[2] MC: no? 
label day2_11: 

    $ chat_message("incri: under the badge_no column idiot ")

    #MC: ok. yes. i see it. 
    $ player_choice(
        [
            ("ok. yes. i see it.", "x")
        ]
    )

    $ chat_message("incri: ya idiot ")
    jump day2_12


label day2_12: 
    $ chat_message("incri: name pls ")

    #MC: Bruce Johnson 
    $ player_choice(
        [
            ("says \"Bruce Johnson\"", "x")
        ]
    )

    $ chat_message("wnpep: did the cop look like a bruce? ")

    $ chat_message("incri: looked like a bicth ")

    $ chat_message("incri: ok can u look at this table now ")

    $ chat_message("incri: azgov.marriage")
    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = None 
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["azgov.marriage"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = None 
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 

    #MC: why? 
    $ player_choice(
        [
            ("why a marriage table??", "x")
        ]
    )

    $ chat_message("incri: ????") 

    $ chat_message("incri: who cares??????",ot="elimf, wnpep")

    $ chat_message("elimf: why are you chasing a cop incri ",ot="wnpep")

    $ chat_message("incri: bc he fucked p ",ot="wnpep")

    $ chat_message("wnpep: did you get a parking ticket? ")

    $ chat_message("incri: i wa sbarely out of time on my spot") 

    $ chat_message("incri: stupid dumbfuck ass gulping time dictator ")

    $ chat_message("elimf: how late were u ")

    $ chat_message("incri: like 1 min ")

    $ chat_message("elimf: o ",ot="wnpep")

    $ chat_message("wnpep: only 1 min late? ")

    $ chat_message("incri: YES ")

    $ chat_message("wnpep: ok. i understand ",ot="incri")

    $ chat_message("incri: I AM GOING TO FKCIN G GUT HIS WALLET ")

    $ chat_message("wnpep: you go superstar! ")

    $ chat_message("elimf: that's what this is all about") 

    $ chat_message("wnpep: let's massacre this savings account! ")

    $ player_choice(
        [
            ("all over a parking ticket? what??", "day2_13"), 
            ("yay!", "day2_14")
        ]
    )


    # [1] MC: all over a parking ticket? what?? 
label day2_13:

    $ chat_message("incri: U DON'T NEED TO BE HERE") 

    $ chat_message("incri: U CAN LEAVE")

    #MC: I'M NOT LEAVING I WAS JUST ASKING A QUESTION 
    $ player_choice(
        [
            ("I'M NOT LEAVING I WAS JUST ASKING A QUESTION", "x")
        ]
    )

    $ chat_message("incri: STOP DOING THAT ")
    jump day2_15

    #[2] MC: yay! 
label day2_14:

    $ chat_message("incri: DESTROY ")
    jump day2_15


   
label day2_15:

    # MC: but, how are we getting to his savings account through marriage records? 
    $ player_choice(
        [
            ("but, how are we getting to his savings account through marriage records? ", "x")
        ]
    )

    $ chat_message("elimf: every1 has secrets ")

    $ chat_message("elimf: and some ppl have spouises ")

    $ chat_message("elimf: who dont know all secrets ",ot="incri, wnpep")

    $ chat_message("incri: ^ that ",ot="wnpep")

    $ chat_message("wnpep: i tell my wife everything. this extortion stuff would never work on me ")

    $ chat_message("elimf: UR MARRIED?? ")

    pause 1 

    $ chat_message("wnpep: what ")

    pause 1

    $ chat_message("wnpep: oh ")

    pause 1 

    $ chat_message("wnpep: autocorrect haha ")

    $ chat_message("wnpep: wife = friend ",ot="elimf")

    $ chat_message("elimf: how does that autocorrect to th at") 

    $ chat_message("elimf: i can't take this information stop speaking immediately ",ot="wnpep")

    $ chat_message("wnpep: i'm not married ")

    $ chat_message("elimf: ok now stop speaking ",ot="incri")

    $ chat_message("incri: OKAY ")

    $ chat_message("incri: GO LOOK AT THE TABLE ")

    $ chat_message("incri: azgov.marriage")

    jump day2_16


label day2_16:
    # wait for input 
    $ player_is_waiting = True 
    $ waiting_label = "day2_17"

    # if they arrive already ready to pass 
    if player_can_pass:
        $ player_is_waiting = False 
        jump day2_17 
    $ renpy.pause(hard=True)

label day2_17:
    $ player_is_waiting = False 

    #MC: i see it 
    $ player_choice(
        [
            ("i see it", "x")
        ]
    )

    $ chat_message("incri: see bruce? ")

    #MC: no... i don't think so 
    $ player_choice(
        [
            ("no... i don't think so", "x")
        ]
    )

    $ chat_message("incri: then add a where clause dumb ass ")

    $ chat_message("wnpep: we didn't show thrim where clauses yet ")

    $ chat_message("elimf: UR MARRIED ")

    $ chat_message("wnpep: i'm not married ")

    #MC: i heard wnpep was married 
    $ player_choice(
        [
            ("i heard wnpep is married", "x")
        ]
    )

    $ chat_message("elimf: I ALSO HEARD WNPEP IS MARRIED")

    $ chat_message("wnpep: ok thrim, a where clause is something you would put after the from statement. ")

    $ chat_message("wnpep: it's like a filter you use when you only care about certain records ")

    $ chat_message("wnpep: like, if we were in the zoo table again, and i just wanted information on incident number 14 ")

    $ chat_message("wnpep: i would add this to the end of my code: where incident_no_0v67 = 14")

    $ chat_message("wnpep: does that make sense? ")

    $ chat_message("wnpep: the whole statement would become `select * from glowparkzoo.inc_0v67 where incident_no_0v67 = 14`")

    $ chat_message("wnpep: just like that. yea? ")

    $ chat_message("elimf: except u have to put anything that's a word in a set of quotes")

    $ chat_message("elimf: make sense?")

    $ player_choice(
        [
            ("i get it. i know what to do", "day2_18"), 
            (".................", "day2_19")
        ]
    )

    #[1] MC: i get it. i know what to do 
label day2_18:

    $ chat_message("wnpep: great! ")

    jump day2_20

    #[2] MC: ................. 
label day2_19:

    $ chat_message("incri: this is like so bsi c are u fucking kidding me ")

    #MC: dick
    $ player_choice(
        [
            ("dick", "x")
        ]
    )

    $ chat_message("wnpep: yes. well. here. might as well help ")

    $ chat_message("wnpep: `select * \nfrom azgov.marriage \nwhere full_name_party_one = 'bruce johnson'`")

    jump day2_20 

label day2_20: 
    $ chat_message("incri: let me know when ur fuckin g done")

    $ renpy.pause(hard=True)




