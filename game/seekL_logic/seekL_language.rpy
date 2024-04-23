default seekL_output = []
default previous_commands = []
default where_idx = []
default j_list = []
default j_v_idx = []
default where_value = ""
default where_place = ""
default where_column_list = []
default where_value_list = []
default where_split_list = []
default where_parts = []

init python: 


    def is_float(element: any) -> bool:
        if element is None: 
            return False
        try:
            float(element)
            return True
        except ValueError:
            return False

    def process_seekL(t): 
        global tables 
        global seekL_output
        global required_runs #use this to check to see if we can proceed (did they run the right thing)
        global previous_commands 
        global seekL_text_send
        global where_idx
        global j_list
        global j_v_idx
        global where_value
        global where_place
        global where_column_list 
        global where_value_list 
        global where_split_list 
        global where_parts

        if t != "":
            t_og = t
            #seekL_text_send = ""

            t = t.lower() 
            t = t.replace("\n", " ")

            error_msg = ""
            loc_select = ""
            loc_from = ""
            loc_join = ""
            loc_where = ""
            row_counter = 0

            # get what's in the query 
            sort_order = []
            if "select " in t:
                loc_select = t.index("select")
                sort_order.append(("select", loc_select))
            if " from " in t: 
                loc_from = t.index("from")
                sort_order.append(("from", loc_from))
            if " join " in t: 
                loc_join = t.index("join") 
                sort_order.append(("join", loc_join))
            if " where " in t: 
                loc_where = t.index("where")
                sort_order.append(("where", loc_where))

            sort_order_test = []
            if sort_order: 
                sort_order_test = sorted(sort_order, key=lambda x: x[1])
            for x in range(len(sort_order_test)): 
                if x == 0 and sort_order_test[x][0] != "select": 
                    error_msg = "ERROR: INCORRECT COMMAND ORDER"
                elif x == 1 and sort_order_test[x][0] != "from": 
                    error_msg = "ERROR: INCORRECT COMMAND ORDER"
                elif x == 2 and ((sort_order_test[x][0] != "join" and loc_join != "") or (sort_order_test[x][0] != "where" and loc_join == "" and loc_where != "")): 
                    error_msg = "ERROR: INCORRECT COMMAND ORDER"
                elif x == 3 and sort_order_test[x][0] != "where": 
                    error_msg = "ERROR: INCORRECT COMMAND ORDER"

            if t.count(" join ") > 1 and error_msg == "": 
                error_msg = "ERROR: TOO MANY JOINS"
            elif t.count(" or ") > 1 or t.count(" and ") > 1 or (t.count(" and ") > 0 and t.count(" or ") > 0) and error_msg == "": 
                error_msg = "ERROR: TOO MANY WHERE CONDITIONS"
            
            # columns 
            cols = ""
            if loc_select != "" and loc_from != "": 
                for idx in range(loc_select + len("select") + 1, loc_from):
                    cols = cols + t[idx]
                cols_list = cols.replace(" ", "").split(",")
            elif error_msg == "": 
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

            # parse out where clause 
            where_clause = ""
            where_value = ""
            where_column_list = []
            where_value_list = []
            where_split_list = []
            where_cond = ""
            if loc_where != "" and error_msg == "":
                for idx in range(loc_where + len("join") + 1, len(t) ):
                    where_clause = where_clause + t[idx]
                if " or " in where_clause.lower(): 
                    where_parts = where_clause.lower().split(" or ")
                    where_cond = "or"
                elif " and " in where_clause.lower(): 
                    where_parts = where_clause.lower().split(" and ")
                    where_cond = "and"
                else:
                    where_parts = [where_clause]
                
                for wp in where_parts:
                    split_me = ""
                    if ">=" in wp: 
                        split_me = ">="
                    elif "<=" in wp: 
                        split_me = "<="
                    elif "=" in wp: 
                        split_me = "="
                    elif ">" in wp: 
                        split_me = ">"
                    elif "<" in wp: 
                        split_me = "<"
                    if split_me == "": 
                        error_msg = "ERROR: WHERE MISSING DIRECTION \n(>, >=, =, <=, <)"
                    else: 
                        where_split_list.append(split_me)
                    
                    if error_msg == "": 
                        where_column = ""
                        where_sides = wp.split(split_me)

                        if where_sides[0].strip() not in cols_final: 
                            cols_final.append(where_sides[0].strip())
                        for ws in where_sides: 
                            ws = ws.strip()#replace(" ", "")
                            if ws in col_search: 
                                where_column = ws 
                            else: 
                                where_value = ws 
                        if where_column == "": 
                            error_msg = "ERROR: WHERE MISSING VALID COLUMN"
                        else: 
                            where_column_list.append(where_column)
                        if where_value == "": 
                            error_msg = "ERROR: WHERE MISSING VALID VALUE"
                        else: 
                            where_value_list.append(where_value)
     
            # i feel like this would all be easier if we combine the tables first 
            # then use the basic where logic 
            # damn 
            # LOLLLLLLLLLLLLLLLLLL 

            # how do they combine 
            join_columns = []
            if join_name != "" and table_name != "" and error_msg == "": 
                for f_k in list(tables[table_name].keys()): 
                    if f_k in list(tables[join_name].keys()): 
                        join_columns.append(f_k)
                        if f_k not in cols_final: 
                            cols_final.append(f_k)
            if not join_columns and join_name != "" and error_msg == "": 
                error_msg = "ERROR: NO COMMON COLUMN BETWEEN TABLES"
            elif join_columns and error_msg == "": 
                join_dict = {}
                for j in join_columns: 
                    l = list(set(tables[table_name][j] + tables[join_name][j]))
                    l.sort()
                    join_dict[j] = l.copy()#[:5] 
                    j_list = join_dict[j].copy()
            elif join_name == "" and error_msg == "": 
                join_dict = {}
                l = next(iter(tables[table_name]))
                join_dict[l] = tables[table_name][l].copy()#[:5]
                j_list = join_dict[l].copy()
            ## filter out the where stuff then choose top 5 

            if error_msg == "":
                final_table = {}
                # only 1 table 
                if join_name == "": 
                    final_table = tables[table_name]
                # join logic 
                else: 
                    for c in cols_final: 
                        #row_counter = 0 
                        #max_len = len(c)
                        final_table[c] = []
                        selected_table = ""
                        if c in list(join_dict.keys()): 
                            for v in join_dict[c]: 
                                final_table[c].append(v)
                        elif c in list(tables[table_name].keys()): 
                            selected_table = table_name 
                        elif c in list(tables[join_name].keys()): 
                            selected_table = join_name 

                        if selected_table != "": 
                            # this only works rn for 1 join
                            for j in list(join_dict.keys()): 
                                for j_v in join_dict[j]: 
                                    #if join_dict[j].index(j_v) < 5:
                                    if j_v in tables[selected_table][j]: 
                                        final_table[c].append(tables[selected_table][c][tables[selected_table][j].index(j_v)])
                                    else: 
                                        final_table[c].append(" ")

            # filtering time 
            if error_msg == "" and where_clause != "":
                # set up baseline 
                for j in list(join_dict.keys()): 
                    j_list = join_dict[j].copy()
                    j_v_idx = []
                    for j_v in join_dict[j]: 
                        j_v_idx.append(join_dict[j].index(j_v))
                    j_list_2 = j_list.copy()
                    j_v_idx_2 = j_v_idx.copy()
                where_idx = []
                for wlv in range(len(where_column_list)):

                    # # get the column we filter on 
                    # where_place = ""
                    # if join_name != "": 
                    #     t_list = [table_name, join_name]
                    #     if where_column_list[wlv] in list(tables[join_name].keys()) and where_column_list[wlv] in list(tables[table_name].keys()): 
                    #         where_place = "special" 
                    #     elif where_column_list[wlv] in list(tables[join_name].keys()): 
                    #         where_place = join_name 
                    #     else: 
                    #         where_place = table_name 
                    # else: 
                    #     t_list = [table_name] 
                    #     where_place = table_name 

                    # get indexes that pass the where in the table 
                    if wlv > 0: 
                        where_idx_old = where_idx.copy() 
                    where_idx = []
                    # t_search = []
                    # if where_place == "special": 
                    #     t_search = j_list
                    # else: 
                    #     t_search = tables[where_place][where_column_list[wlv]]
                    t_search = final_table[where_column_list[wlv]]

                    if where_split_list[wlv] == "=": 
                        if is_float(where_value_list[wlv]):
                            where_idx = [i for i in range(len(t_search)) if t_search[i] == where_value_list[wlv]]
                        elif where_value_list[wlv].startswith("'") and where_value_list[wlv].endswith("'") or  where_value_list[wlv].startswith('"') and where_value_list[wlv].endswith('"'):
                            where_value_list[wlv] = where_value_list[wlv].replace("'", "").lower()
                            where_value_list[wlv] = where_value_list[wlv].replace('"', "").lower()
                            where_idx = [i for i in range(len(t_search)) if t_search[i].lower() == where_value_list[wlv]]
                        else: 
                            error_msg = "ERROR: WHERE VALUE STRING MISSING \nSINGLE QUOTES"
                    elif(is_float(where_value_list[wlv])): 
                        try:
                            if where_split_list[wlv] == ">=":
                                where_idx = [i for i in range(len(t_search)) if float(t_search[i]) >= float(where_value_list[wlv])]
                            elif where_split_list[wlv] == "<=":
                                where_idx = [i for i in range(len(t_search)) if float(t_search[i]) <= float(where_value_list[wlv])]
                            elif where_split_list[wlv] == ">":
                                where_idx = [i for i in range(len(t_search)) if float(t_search[i]) > float(where_value_list[wlv])]
                            elif where_split_list[wlv] == "<":
                                where_idx = [i for i in range(len(t_search)) if float(t_search[i]) < float(where_value_list[wlv])]
                        except ValueError:
                            error_msg = "ERROR: CANNOT APPLY WHERE CONDITION \nTO NON-NUMERIC COLUMN"
                    else: 
                        error_msg = "ERROR: CANNOT APPLY WHERE CONDITION \nTO NON-NUMERIC VALUE"

                    where_idx = list(set(where_idx))

                    if wlv == 1 and where_cond == "and": 
                        where_idx_0 = [i for i in where_idx if i in where_idx_old]
                        where_idx = where_idx_0.copy() 
                    elif wlv == 1 and where_cond == "or": 
                        where_idx_0 = list(set(where_idx + where_idx_old))
                        where_idx = where_idx_0.copy() 



                    
                if error_msg == "": 
                    for j in list(join_dict.keys()): 
                        # j_list = join_dict[j].copy()
                        # j_v_idx = []
                        # for j_v in join_dict[j]: 
                        #     j_v_idx.append(join_dict[j].index(j_v))
                            #if str(j_v) not in where_place[j] or int(join_dict[j].index(j_v)) not in where_idx:
                            #if j_v not in where_place[j]: #or int(join_dict[j].index(j_v)) not in where_idx:
                        for j_v_i in j_v_idx:
                            # if where_place == 'special':
                            #     if j_list.index(j_list[j_v_i]) not in where_idx and len(j_list)-1 >= j_v_i:
                            #         join_dict[j].remove(j_list[j_v_i])
                            # else: 
                            if j_v_i not in where_idx and len(j_list)-1 >= j_v_i and j_list[j_v_i] in join_dict[j]:
                                join_dict[j].remove(j_list[j_v_i])
                                #j_list.remove(j_v)
                        
            if error_msg == "": 
                for j in list(join_dict.keys()): 
                    join_dict[j] = join_dict[j][:5]
                    j_list = join_dict[j]
                    l = j_list.copy() 



            # where does the where clause go? 
            # probably first 
            # like how we add records to the id thing, we now want to remove them 
            # so we can have a list of rows that can be added and those that can't 

            #"#ee6464"
            if error_msg != "": 
                seekL_output = ["{color=ee6464}"+error_msg+"{/color}"]
                previous_commands.append("{color=945050}{size=20}UNSUCCESSFUL{/size}{/color}\n"+t_og)
                renpy.play("audio/sfx/message_received_001 data error.ogg")
            else: 
                previous_commands.append(t_og)
                output_strings = []
                first_c = True
                l_out = {}
                for c in cols_final: 
                    l_out[c] = []
                    row_counter = 0 
                    max_len = len(c)

                    # only 1 table 
                    #if join_name == "": 
                    # the line thing 
                    max_len = len(c)
                    for v in final_table[c]:
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
                                i = final_table[j].index(j_v)
                                v  = final_table[c][i]
                                l_out[c].append(v)
                                alt_string = alt_string + "\n" + "{color=8c8c8c}|{/color}"
                                output_string = output_string + "\n" + v 
                    if first_c: 
                        output_strings.append(alt_string)
                        first_c = False 
                    output_strings.append(output_string)
                    output_strings.append(alt_string)
                    
                    # # join logic 
                    # else: 
                    #     selected_table = ""
                    #     max_len = len(c)
                    #     alt_string = "{color=8c8c8c}|\n|{/color}"
                    #     if c in list(join_dict.keys()): 
                    #         for v in join_dict[c]: 
                    #             if len(v) > max_len: 
                    #                 max_len = len(v)
                    #         output_string = c + "\n{color=8c8c8c}" + "-"*max_len + "{/color}"
                    #         for v in join_dict[c]: 
                    #             alt_string = alt_string + "\n" + "{color=8c8c8c}|{/color}"
                    #             output_string = output_string + "\n" + v 
                    #         if first_c: 
                    #             output_strings.append(alt_string)
                    #             first_c = False 
                    #         output_strings.append(output_string)
                    #         output_strings.append(alt_string)
                    #     elif c in list(tables[table_name].keys()): 
                    #         selected_table = table_name 
                    #     elif c in list(tables[join_name].keys()): 
                    #         selected_table = join_name 
                    #     if selected_table != "": 
                    #         for v in tables[selected_table][c]: 
                    #             if len(v) > max_len: 
                    #                 max_len = len(v)
                    #         output_string = c + "\n{color=8c8c8c}" + "-"*max_len + "{/color}"
                    #         # this only works rn for 1 join
                    #         for j in list(join_dict.keys()): 
                    #             for j_v in join_dict[j]: 
                    #                 #if join_dict[j].index(j_v) < 5:
                    #                 if j_v in tables[selected_table][j]: 
                    #                     # get the index of that value in table 
                    #                     i = tables[selected_table][j].index(j_v)
                    #                     v  = tables[selected_table][c][i]
                    #                 else: 
                    #                     v = " "
                    #                 alt_string = alt_string + "\n" + "{color=8c8c8c}|{/color}"
                    #                 output_string = output_string + "\n" + v 
                    #         if first_c: 
                    #             output_strings.append(alt_string)
                    #             first_c = False 
                    #         output_strings.append(output_string)
                    #         output_strings.append(alt_string)
            

                seekL_output = output_strings
                renpy.play("audio/sfx/data_loaded_001.ogg")
                player_input_confirm(ta=list([join_name, table_name]), cols = cols_final, idx = l_out)



        





