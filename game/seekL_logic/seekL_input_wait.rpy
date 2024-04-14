
init python: 
    required_runs = {
        "columns":None, 
        "tables":None, 
        "idx":None
    }

    player_can_pass = False
    player_is_waiting = False
    waiting_label = ""

    def player_input_confirm(tables=None, cols=None, idx=None): 
        global player_input_confirm_label_jump
        global player_can_pass
        global player_is_waiting 
        global waiting_label 

        player_proceed = True 

        if required_runs["columns"]: 
            for c in required_runs["columns"]: 
                if c not in cols: 
                    player_proceed = False 
        
        if required_runs["tables"]: 
            for t in required_runs["tables"]: 
                if t not in tables:
                    player_proceed = False 

        if required_runs["idx"]: 
            for i in required_runs["idx"]:
                if i not in idx: 
                    player_proceed = False 
        
        player_can_pass = player_proceed 
        if player_is_waiting: 
            renpy.jump(waiting_label)
        #return(player_proceed)
                    