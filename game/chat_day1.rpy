

label day1_start: 
    #$ $ chat_message("odxny: testing testing")

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

    $ chat_message("incri: UR SOOOOO SUS DUDE ")

    $ chat_message("elimf: could be not a dude ")

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

    $ chat_message("wnpep: `select * \nfrom glowpark_zoo.risk.incident_reports_0V67`")

    $ player_choice(
        [
            ("ok, one moment", "day1_18"), 
            ("why is that so long and ugly...", "day1_17")
        ]
    )

# [1] MC: ok, one moment 

# [2] MC: why is that so long and ugly... 
label day1_17:

    $ chat_message("elimf: JUST LIKE MY EX") 

    $ chat_message("incri: JUST LIKE MY EX")

    $ chat_message("elimf: i fucking beat you") 

    $ chat_message("incri: no way ur message is under mine") 

    $ chat_message("wnpep: elimf's came up first.") 

    $ chat_message("elimf: AHAHAHAHAHA") 

    $ chat_message("incri: FUCKING") 

    $ chat_message("wnpep: sorry.") 

    jump day1_18

label day1_18:

    $ renpy.pause(hard=True)

