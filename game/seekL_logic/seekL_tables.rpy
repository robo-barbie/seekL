
default tables = {

    ## TESTING TABLE 
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

    ## TESTING TABLE 
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
            ], 
        "num": [
            "11",  
            "31", 
            "41", 
            "81", 
            "91"
        ]
    }, 

    ## TRAINING TABLE 
    "table.example": {
        "table_id": [
            "T1",  
            "T2", 
            "T3", 
            "T4"
            ],
        "hacker_name": [
            "wnpep",  
            "incri", 
            "elimf", 
            "odxny"
            ],
        "chat_join_date": [
            "2023-11-2", 
            "2024-2-16", 
            "2023-12-12", 
            "2023-3-15"
            ], 
        "favorite_fruit": [
            "Apple",  
            "Mango", 
            "Banana", 
            "Date"
        ], 
        "number_of_hacks": [
            "12",  
            "27", 
            "19", 
            "50"
        ]
    }, 

    ## DAY 1 TUTORIAL TABLE  
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

    ## DAY 1 TUTORIAL TABLE  
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

init python: 
    def load_tables(): 
        global tables

        ## azgov.police_info
        tname = "azgov.police_info"
        tables[tname] = {
            "badge_no": [], 
            "full_name": [], 
            "hire_date": []    
            }
        t1 = renpy.file("tables/seekL Tables - "+tname+".tsv")
        for l in t1:
            l = l.decode("utf-8")
            a = l.rstrip().split("\t")
            tables[tname]["badge_no"].append(a[0])
            tables[tname]["full_name"].append(a[1])
            tables[tname]["hire_date"].append(a[2])
        tables[tname]["badge_no"].pop(0)
        tables[tname]["full_name"].pop(0)
        tables[tname]["hire_date"].pop(0)

        ## azgov.marriage
        tname = "azgov.marriage"
        tables[tname] = {
            "mid": [], 
            "marriage_date": [], 
            "full_name": [], 
            "spouse_name": []      
            }
        t2 = renpy.file("tables/seekL Tables - "+tname+".tsv")
        for l in t2:
            l = l.decode("utf-8")
            a = l.rstrip().split("\t")
            tables[tname]["mid"].append(a[0])
            tables[tname]["marriage_date"].append(a[1])
            tables[tname]["full_name"].append(a[2])
            tables[tname]["spouse_name"].append(a[3])
        tables[tname]["mid"].pop(0)
        tables[tname]["marriage_date"].pop(0)
        tables[tname]["full_name"].pop(0)
        tables[tname]["spouse_name"].pop(0)

        ## irs.contacts
        tname = "irs.contacts"
        tables[tname] = {
            "irs_id": [], 
            "full_name": [], 
            "phone": [], 
            "email": []      
            }
        t3 = renpy.file("tables/seekL Tables - "+tname+".tsv")
        for l in t3:
            l = l.decode("utf-8")
            a = l.rstrip().split("\t")
            tables[tname]["irs_id"].append(a[0])
            tables[tname]["full_name"].append(a[1])
            tables[tname]["phone"].append(a[2])
            tables[tname]["email"].append(a[3])
        tables[tname]["irs_id"].pop(0)
        tables[tname]["full_name"].pop(0)
        tables[tname]["phone"].pop(0)
        tables[tname]["email"].pop(0)

        ## godaddy.secretsmooch_users
        tname = "godaddy.secretsmooch_users"
        tables[tname] = {
            "ss_cid": [], 
            "ss_alias": [], 
            "ss_join_date": [], 
            "email": []      
            }
        t4 = renpy.file("tables/seekL Tables - "+tname+".tsv")
        for l in t4:
            l = l.decode("utf-8")
            a = l.rstrip().split("\t")
            tables[tname]["ss_cid"].append(a[0])
            tables[tname]["ss_alias"].append(a[1])
            tables[tname]["ss_join_date"].append(a[2])
            tables[tname]["email"].append(a[3])
        tables[tname]["ss_cid"].pop(0)
        tables[tname]["ss_alias"].pop(0)
        tables[tname]["ss_join_date"].pop(0)
        tables[tname]["email"].pop(0)
        