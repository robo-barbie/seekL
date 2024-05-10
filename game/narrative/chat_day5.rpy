

label day5_seekLove_chat: 

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
    
    ## maybe instead of showing the screen, we have the player execute a command 
    ## and that command will let you start up a call if the number works 
    show screen secure_dial 
    $ renpy.pause(hard=True)