

init python: 
    seekL_output = []
    previous_commands = []
    tables = {
        "test": {
            "id": [
                "1", 
                "2", 
                "3"
                ],
            "date": [
                "2023-01-01", 
                "2023-02-01", 
                "2023-02-03"
                ],
            "extra1": [
                "option 1", 
                "option 2", 
                "option 3"
                ], 
            "extra2": [
                "option 1", 
                "option 2", 
                "option 3"
                ], 
            "extra3": [
                "option 1", 
                "option 2", 
                "option 3"
                ]
        }, 
        "test2": {
            "id": [
                "1",  
                "3", 
                "4", 
                "8", 
                "9"
                ],
            "otherthing": [
                "A", 
                "B", 
                "C", 
                "D", 
                "E"
                ]
        }, 
        "glowparkzoo.inc_0v67":{
            "incident_no_0v67": [
                "15", 
                "14",
                "13",
                "12",
                "11", 
                "10" 
            ], 
            "event_mst_0v67": [
                "2021-01-02 12:30:00", 
                "2020-04-12 13:35:05", 
                "2018-11-19 09:06:47", 
                "2018-08-01 01:23:54", 
                "2017-10-31 18:59:58", 
                "2017-10-31 18:01:00"
            ], 
            "impact_0v67": [
                "10",
                "7", 
                "4",
                "1", 
                "2", 
                "1"
            ], 
            "cat_0v67": [
                "fecal projectiles", 
                "fecal projectiles", 
                "fecal projectiles", 
                "fecal projectiles", 
                "fecal projectiles", 
                "fecal projectiles"
            ], 
            "notes_0v67": [
                "immediate transfer recommended", 
                "wary", 
                "", 
                "some improvement..", 
                "", 
                ""
            ]
        }, 
        "glowparkzoo.inc_x77s":{
            "incident_no_x77s": [
                "2", 
                "1"
            ], 
            "event_mst_x77s": [
                "2020-01-02 12:34:00", 
                "2016-11-11 08:21:05"
            ], 
            "impact_x77s": [
                "3",
                "1"
            ], 
            "cat_x77s": [
                "illness", 
                "aggression"
            ], 
            "notes_x77s": [
                "let's see if they can work through it", 
                "no resources needed"
            ]
        }
    }

    def process_seekL(t): 
        global tables 
        global seekL_output
        global required_runs #use this to check to see if we can proceed (did they run the right thing)
        global previous_commands 
        global seekL_text_send

        if t != "":
            t_og = t
            seekL_text_send = ""

            t = t.lower() 
            t = t.replace("\n", " ")

            error_msg = ""
            loc_select = ""
            loc_from = ""
            loc_join = ""
            loc_where = ""
            row_counter = 0

            # get what's in the query 
            if "select " in t:
                loc_select = t.index("select")
            if " from " in t: 
                loc_from = t.index("from")
            if " join " in t: 
                loc_join = t.index("join") 
            if " where " in t: 
                loc_where = t.index("where")
            
            # columns 
            cols = ""
            if loc_select != "" and loc_from != "": 
                for idx in range(loc_select + len("select") + 1, loc_from):
                    cols = cols + t[idx]
                cols_list = cols.replace(" ", "").split(",")
            else: 
                cols_list = []
                error_msg = "ERROR: INCORRECT SYNTAX"

            # table 
            table_name = ""
            if loc_from != "" and error_msg == "":
                if loc_join != "": 
                    end_from = loc_join 
                elif loc_where != "": 
                    end_from = loc_where 
                else: 
                    end_from = len(t) 

                for idx in range(loc_from + len("from") + 1, end_from):
                    table_name = table_name + t[idx]

                table_name = table_name.replace(" ", "")
            
            # join -- ONLY ONE COMMON COLUMN 
            join_name = ""
            if loc_join != "" and error_msg == "":
                if loc_where != "": 
                    end_join = loc_where 
                else: 
                    end_join = len(t) 
                for idx in range(loc_join + len("join") + 1, end_join):
                    join_name = join_name + t[idx]
                join_name = join_name.replace(" ", "")

            # check for errors + check selected columns 
            tables = {k.lower():v for k,v in tables.items()}
            if table_name in tables and error_msg == "": 
                cols_final = []
                if join_name not in tables and join_name != "": 
                    error_msg = "ERROR: JOIN TABLE NOT FOUND-\n" + join_name 
                elif join_name != "": 
                    col_search = list(set(list(tables[join_name].keys()) + list(tables[table_name].keys())))
                else: 
                    col_search = list(tables[table_name].keys())
                if "*" in cols_list and error_msg == "": 
                    cols_final = col_search
                elif error_msg == "": 
                    for c in cols_list: 
                        if c in col_search: 
                            cols_final.append(c)
                if not cols_final and error_msg == "": 
                    error_msg = "ERROR: COLUMN NAMES NOT FOUND"
            elif error_msg == "": 
                error_msg = "ERROR: TABLE NAME NOT FOUND -\n" + table_name

            # how do they combine 
            join_columns = []
            if join_name != "" and table_name != "" and error_msg == "": 
                for f_k in list(tables[table_name].keys()): 
                    if f_k in list(tables[join_name].keys()): 
                        join_columns.append(f_k)

            if not join_columns and join_name != "" and error_msg == "": 
                error_msg = "ERROR: NO COMMON COLUMN BETWEEN TABLES"
            elif join_columns and error_msg == "": 
                join_dict = {}
                for j in join_columns: 
                    l = list(set(tables[table_name][j] + tables[join_name][j]))
                    l.sort()
                    join_dict[j] = l[:5]
            elif join_name == "" and error_msg == "": 
                join_dict = {}
                l = next(iter(tables[table_name]))
                join_dict[l] = tables[table_name][l][:5]

            # parse out where clause 
            where_clause = ""
            if loc_where != "" and error_msg == "":
                for idx in range(loc_where + len("join") + 1, len(t) ):
                    where_clause = where_clause + t[idx]
                where_clause = where_clause.replace(" ", "")
                split_me = ""
                if ">=" in where_clause: 
                    split_me = ">="
                elif "<=" in where_clause: 
                    split_me = "<="
                elif "=" in where_clause: 
                    split_me = "="
                elif ">" in where_clause: 
                    split_me = ">"
                elif "<" in where_clause: 
                    split_me = "<"
                if split_me == "": 
                    error_msg = "ERROR: WHERE MISSING DIRECTION (>, >=, =, <=, <)"
                
                if error_msg == "": 
                    where_column = ""
                    where_sides = where_clause.split(split_me)
                    for ws in where_sides: 
                        if ws in col_search: 
                            where_column = ws 
                    if where_column == "": 
                        error_msg = "ERROR: WHERE MISSING VALID COLUMN"
                    # fill in where logic here 
                    # else: 
                        



            # where does the where clause go? 
            # probably first 
            # like how we add records to the id thing, we now want to remove them 
            # so we can have a list of rows that can be added and those that can't 

            #"#ee6464"
            if error_msg != "": 
                seekL_output = ["{color=ee6464}"+error_msg+"{/color}"]
                previous_commands.append("{color=945050}{size=20}UNSUCCESSFUL{/size}\n"+t_og+"{/color}")
                renpy.play("audio/sfx/data_error.ogg")
            else: 
                previous_commands.append(t_og)
                output_strings = []
                first_c = True
                for c in cols_final: 
                    row_counter = 0 
                    max_len = len(c)

                    # only 1 table 
                    if join_name == "": 
                        # the line thing 
                        max_len = len(c)
                        for v in tables[table_name][c]:
                            if len(v) > max_len:
                                max_len = len(v)
                        output_string = c + "\n{color=8c8c8c}" + "-"*max_len + "{/color}"
                        alt_string = "{color=8c8c8c}|\n|{/color}"
                
                        
                        #for v in tables[table_name][c]: 
                            #alt_string = alt_string + "\n" + "{color=8c8c8c}|{/color}"
                            #output_string = output_string + "\n" + v 

                        for j in list(join_dict.keys()): 
                            for j_v in join_dict[j]: 
                                if join_dict[j].index(j_v) < 5:
                                    i = tables[table_name][j].index(j_v)
                                    v  = tables[table_name][c][i]
                                    alt_string = alt_string + "\n" + "{color=8c8c8c}|{/color}"
                                    output_string = output_string + "\n" + v 
                        if first_c: 
                            output_strings.append(alt_string)
                            first_c = False 
                        output_strings.append(output_string)
                        output_strings.append(alt_string)
                    
                    # join logic 
                    else: 
                        selected_table = ""
                        max_len = len(c)
                        alt_string = "{color=8c8c8c}|\n|{/color}"
                        if c in list(join_dict.keys()): 
                            for v in join_dict[c]: 
                                if len(v) > max_len: 
                                    max_len = len(v)
                            output_string = c + "\n{color=8c8c8c}" + "-"*max_len + "{/color}"
                            for v in join_dict[c]: 
                                alt_string = alt_string + "\n" + "{color=8c8c8c}|{/color}"
                                output_string = output_string + "\n" + v 
                            if first_c: 
                                output_strings.append(alt_string)
                                first_c = False 
                            output_strings.append(output_string)
                            output_strings.append(alt_string)
                        elif c in list(tables[table_name].keys()): 
                            selected_table = table_name 
                        elif c in list(tables[join_name].keys()): 
                            selected_table = join_name 
                        if selected_table != "": 
                            for v in tables[selected_table][c]: 
                                if len(v) > max_len: 
                                    max_len = len(v)
                            output_string = c + "\n{color=8c8c8c}" + "-"*max_len + "{/color}"
                            # this only works rn for 1 join
                            for j in list(join_dict.keys()): 
                                for j_v in join_dict[j]: 
                                    if join_dict[j].index(j_v) < 5:
                                        if j_v in tables[selected_table][j]: 
                                            # get the index of that value in table 
                                            i = tables[selected_table][j].index(j_v)
                                            v  = tables[selected_table][c][i]
                                        else: 
                                            v = " "
                                        alt_string = alt_string + "\n" + "{color=8c8c8c}|{/color}"
                                        output_string = output_string + "\n" + v 
                            if first_c: 
                                output_strings.append(alt_string)
                                first_c = False 
                            output_strings.append(output_string)
                            output_strings.append(alt_string)
                seekL_output = output_strings
                renpy.play("audio/sfx/data_success.ogg")
                player_input_confirm(tables=list([join_name, table_name]), cols = cols_final, idx = l)



        





