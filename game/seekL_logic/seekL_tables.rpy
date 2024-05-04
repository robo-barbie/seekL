
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

        ## secretsmooch.users
        tname = "secretsmooch.users"
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

        ## azgov.insurance
        tname = "azgov.insurance"
        tables[tname] = {
            "ins_id": [], 
            "ins_name": [], 
            "ins_alias": [], 
            "ins_type": [],      
            "ins_hsp_partners": []      
            }
        t5 = renpy.file("tables/seekL Tables - "+tname+".tsv")
        for l in t5:
            l = l.decode("utf-8")
            a = l.rstrip().split("\t")
            tables[tname]["ins_id"].append(a[0])
            tables[tname]["ins_name"].append(a[1])
            tables[tname]["ins_alias"].append(a[2])
            tables[tname]["ins_type"].append(a[3])
            tables[tname]["ins_hsp_partners"].append(a[4])
        tables[tname]["ins_id"].pop(0)
        tables[tname]["ins_name"].pop(0)
        tables[tname]["ins_alias"].pop(0)
        tables[tname]["ins_type"].pop(0)
        tables[tname]["ins_hsp_partners"].pop(0)

        ## azgov.hospitals
        tname = "azgov.hospitals"
        tables[tname] = {
            "hsp_id": [], 
            "hsp_name": [], 
            "ins_betma": [], 
            "ins_gered": [],      
            "ins_digma": [],       
            "ins_medicaid": [],       
            "ins_define": []      
            }
        t6 = renpy.file("tables/seekL Tables - "+tname+".tsv")
        for l in t6:
            l = l.decode("utf-8")
            a = l.rstrip().split("\t")
            tables[tname]["hsp_id"].append(a[0])
            tables[tname]["hsp_name"].append(a[1])
            tables[tname]["ins_betma"].append(a[2])
            tables[tname]["ins_gered"].append(a[3])
            tables[tname]["ins_digma"].append(a[4])
            tables[tname]["ins_medicaid"].append(a[5])
            tables[tname]["ins_define"].append(a[6])
        tables[tname]["hsp_id"].pop(0)
        tables[tname]["hsp_name"].pop(0)
        tables[tname]["ins_betma"].pop(0)
        tables[tname]["ins_gered"].pop(0)
        tables[tname]["ins_digma"].pop(0)
        tables[tname]["ins_medicaid"].pop(0)
        tables[tname]["ins_define"].pop(0)

        ## pride.claims
        tname = "pride.claims"
        tables[tname] = {
            "claim_no": [], 
            "claim_type": [], 
            "claim_doctor": [], 
            "claim_patient_id": [],      
            "claim_date": [],       
            "ins_name": []     
            }
        t7 = renpy.file("tables/seekL Tables - "+tname+".tsv")
        for l in t7:
            l = l.decode("utf-8")
            a = l.rstrip().split("\t")
            tables[tname]["claim_no"].append(a[0])
            tables[tname]["claim_type"].append(a[1])
            tables[tname]["claim_doctor"].append(a[2])
            tables[tname]["claim_patient_id"].append(a[3])
            tables[tname]["claim_date"].append(a[4])
            tables[tname]["ins_name"].append(a[5])
        tables[tname]["claim_no"].pop(0)
        tables[tname]["claim_type"].pop(0)
        tables[tname]["claim_doctor"].pop(0)
        tables[tname]["claim_patient_id"].pop(0)
        tables[tname]["claim_date"].pop(0)
        tables[tname]["ins_name"].pop(0)
        
        ## pride.paystubs23
        tname = "pride.paystubs23"
        tables[tname] = {
            "pay_no": [], 
            "pay_year": [], 
            "full_name": [], 
            "pay_total": []    
            }
        t8 = renpy.file("tables/seekL Tables - "+tname+".tsv")
        for l in t8:
            l = l.decode("utf-8")
            a = l.rstrip().split("\t")
            tables[tname]["pay_no"].append(a[0])
            tables[tname]["pay_year"].append(a[1])
            tables[tname]["full_name"].append(a[2])
            tables[tname]["pay_total"].append(a[3])
        tables[tname]["pay_no"].pop(0)
        tables[tname]["pay_year"].pop(0)
        tables[tname]["full_name"].pop(0)
        tables[tname]["pay_total"].pop(0)

        ## irs.income23 
        tname = "irs.income23"
        tables[tname] = {
            "pstb_no": [], 
            "tax_year": [], 
            "full_name": [], 
            "irs_total": []    
            }
        t9 = renpy.file("tables/seekL Tables - "+tname+".tsv")
        for l in t9:
            l = l.decode("utf-8")
            a = l.rstrip().split("\t")
            tables[tname]["pstb_no"].append(a[0])
            tables[tname]["tax_year"].append(a[1])
            tables[tname]["full_name"].append(a[2])
            tables[tname]["irs_total"].append(a[3])
        tables[tname]["pstb_no"].pop(0)
        tables[tname]["tax_year"].pop(0)
        tables[tname]["full_name"].pop(0)
        tables[tname]["irs_total"].pop(0)