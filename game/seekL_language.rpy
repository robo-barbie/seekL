

init python: 
    seekL_output = []
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
        }
    }

    def process_seekL(t): 
        global tables 
        global seekL_output

        t = t.lower() 

        error_msg = ""
        loc_select = ""
        loc_from = ""

        # get what's in the query 
        if "select " in t:
            loc_select = t.index("select")
        if "from" in t: 
            loc_from = t.index("from")
        
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
            for idx in range(loc_from + len("from") + 1, len(t)):
                table_name = table_name + t[idx]
            table_name = table_name.replace(" ", "")

        # check for errors 
        if table_name in tables and error_msg == "": 
            cols_final = []
            if "*" in cols_list: 
                cols_final = list(tables[table_name].keys())
            else: 
                for c in cols_list: 
                    if c in list(tables[table_name].keys()): 
                        cols_final.append(c)
            if not cols_final: 
                error_msg = "ERROR: COLUMN NAMES NOT FOUND"
        elif error_msg == "": 
            error_msg = "ERROR: TABLE NAME NOT FOUND"

        if error_msg != "": 
            seekL_output = [error_msg]
        else: 
            output_strings = []
            first_c = True
            for c in cols_final: 
                # the line thing 
                max_len = len(c)
                for v in tables[table_name][c]:
                    if len(v) > max_len:
                        max_len = len(v)

                output_string = c + "\n{color=8c8c8c}" + "-"*max_len + "{/color}"
                alt_string = "{color=8c8c8c}|\n|{/color}"
        
                for v in tables[table_name][c]: 
                    alt_string = alt_string + "\n" + "{color=8c8c8c}|{/color}"
                    output_string = output_string + "\n" + v 
                if first_c: 
                    output_strings.append(alt_string)
                    first_c = False 
                output_strings.append(output_string)
                output_strings.append(alt_string)
            seekL_output = output_strings



        





