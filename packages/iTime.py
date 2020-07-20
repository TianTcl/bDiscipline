# ~~~~~~~~~~~~~~~~~~~~~~~

# Import
from packages import forceInput, iSmart

# Functions
def name(n_sport): # Gets default sport name
    with open("database/sports.txt","r") as db_f_sports:
        db_c_sports = db_f_sports.read().splitlines()
        for db_c_sports_each in db_c_sports:
            db_c_each_upper = list(())
            for db_c_each in db_c_sports_each.split(" : ")[1].split(", ")[:-1]:
                db_c_each_upper.append(db_c_each.upper())
            if n_sport.upper() == db_c_sports_each.split(" : ")[0].upper():
                n_content = n_sport
                break
            elif n_sport.upper() in db_c_each_upper:
                n_content = db_c_sports_each.split(" : ")[0]
                break
        db_f_sports.close()
    return n_content

def get(g_sport, g_goal): # Convert kcal to time (goal)
    g_name = name(g_sport)
    if g_name == "weight":
        g_time = g_goal * 30 / 112
    elif g_name == "aerobic":
        g_time = g_goal * 30 / 205
    elif g_name == "machine":
        g_time = g_goal * 30 / 335
    elif g_name == "golf":
        g_time = g_goal * 30 / 130
    elif g_name == "run":
        g_time = g_goal * 30 / 298
    elif g_name == "yoga":
        g_time = g_goal * 30 / 149
    elif g_name == "bike":
        g_time = g_goal * 30 / 260
    elif g_name == "volleyball":
        g_time = g_goal * 30 / 112
    elif g_name == "swimming":
        g_time = g_goal * 30 / 223
    elif g_name == "walk":
        g_time = g_goal * 30 / 149
    elif g_name == "football":
        g_time = g_goal * 30 / 260
    elif g_name == "basketball":
        g_time = g_goal * 30 / 298
    elif g_name == "rope":
        g_time = g_goal * 30 / 372
    elif g_name == "gardening":
        g_time = g_goal * 30 / 167
    elif g_name == "tennis":
        g_time = g_goal * 30 / 267
    elif g_name == "cooking":
        g_time = g_goal * 30 / 93
    g_content = iSmart.convert("time", g_time)
    return g_content

def convert(c_sport, c_time): # Convert time to kcal (record)
    c_name = name(c_sport)
    if c_name == "weight":
        c_kcal = c_time / 30 * 112
    elif c_name == "aerobic":
        c_kcal = c_time / 30 * 205
    elif c_name == "machine":
        c_kcal = c_time / 30 * 335
    elif c_name == "golf":
        c_kcal = c_time / 30 * 130
    elif c_name == "run":
        c_kcal = c_time / 30 * 298
    elif c_name == "yoga":
        c_kcal = c_time / 30 * 149
    elif c_name == "bike":
        c_kcal = c_time / 30 * 260
    elif c_name == "volleyball":
        c_kcal = c_time / 30 * 112
    elif c_name == "swimming":
        c_kcal = c_time / 30 * 223
    elif c_name == "walk":
        c_kcal = c_time / 30 * 149
    elif c_name == "football":
        c_kcal = c_time / 30 * 260
    elif c_name == "basketball":
        c_kcal = c_time / 30 * 298
    elif c_name == "rope":
        c_kcal = c_time / 30 * 372
    elif c_name == "gardening":
        c_kcal = c_time / 30 * 167
    elif c_name == "tennis":
        c_kcal = c_time / 30 * 267
    elif c_name == "cooking":
        c_kcal = c_time / 30 * 93
    c_content = round(c_kcal, 2)
    return c_content