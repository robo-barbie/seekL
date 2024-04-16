
init python: 
    required_runs = {
        "columns":None, 
        "tables":None, 
        "idx":None
    }

    player_can_pass = False
    player_is_waiting = False
    waiting_label = ""
    tables_active = []

    def player_input_confirm(ta=None, cols=None, idx=None): 
        global player_input_confirm_label_jump
        global player_can_pass
        global player_is_waiting 
        global waiting_label 
        global tables_active 
        tables_active = ta 

        player_proceed = 0

        if required_runs["columns"]: 
            for c in required_runs["columns"]: 
                if c.lower() not in [x.lower() for x in cols]: 
                    player_proceed +=1
        
        if required_runs["tables"]: 
            for t in required_runs["tables"]: 
                if t.lower() not in [x.lower() for x in ta]:
                    player_proceed +=1

        if required_runs["idx"]: 
            for i in required_runs["idx"]:
                if i.lower() not in [x.lower() for x in idx]: 
                    player_proceed +=1
        
        if player_proceed > 0: 
            player_can_pass = False 
        else: 
            player_can_pass = True 
            if player_is_waiting: 
                renpy.jump(waiting_label)
        #return(player_proceed)
                    