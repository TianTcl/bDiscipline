# ~~~~~~~~~~~~~~~~~~~~~~~

# Import
from packages import forceInput, getData, getRecord, iSmart
from pylab import *

# Functions
def auto(a_mode, a_user, a_sport):
    a_id = getData.id(a_user)
    if a_mode == "check":
        a_c_goal = getRecord.goal(a_id, a_sport)
        a_c_total = getRecord.total(a_id, a_sport)
        if a_c_total >= a_c_goal:
            return True
        else:
            return False
    elif a_mode == "generate":
        print("You've completed your task")
        each_kcal(a_user, a_sport)
        remove(a_user, a_sport)

def each_kcal(ek_user, ek_sport):
    ek_exercise_count = getRecord.count(ek_user, ek_sport)
    ek_p_x = iSmart.lists(ek_exercise_count) # x = each exercise
    ek_p_y = getRecord.each_record(ek_user, ek_sport) # y = each record
    plot(ek_p_x, ek_p_y)
    grid(True)
    xlabel("Record")
    ylabel("kcal burned")
    show()

def remove(r_user, r_sport):
    r_id = getData.id(r_user)
    with open("database/appointment.csv","r") as db_f_appointment:
        db_c_appointment = db_f_appointment.read().splitlines()
        for r_content_each in db_c_appointment:
            if r_content_each.split(",")[0] == r_id and r_content_each.split(",")[1].upper() == r_sport.upper():
                r_content_index = db_c_appointment.index(r_content_each)
                break
        db_f_appointment.close()
    db_c_appointment.pop(r_content_index)
    r_update_text = iSmart.convert("appointment", db_c_appointment)
    with open("database/appointment.csv","w") as db_f_appointment:
        db_f_appointment.write(r_update_text)
        db_f_appointment.close()

def execute():
    mode = forceInput.integers("1) Overall\t2) Male\t\t3) Female\nMode : ","Please choose a graph to plot",[1, 2, 3])
    if mode == 1:
        ak_ar()
    elif mode == 2:
        ak_bg("male")
    elif mode == 3:
        ak_bg("female")

def ak_ar():
    aa_ak_g_1 = getRecord.users_avg_kcal(getRecord.users_ar(0, 10))
    aa_ak_g_2 = getRecord.users_avg_kcal(getRecord.users_ar(10, 20))
    aa_ak_g_3 = getRecord.users_avg_kcal(getRecord.users_ar(20, 30))
    aa_ak_g_4 = getRecord.users_avg_kcal(getRecord.users_ar(30, 40))
    aa_ak_g_5 = getRecord.users_avg_kcal(getRecord.users_ar(40, 50))
    aa_ak_g_6 = getRecord.users_avg_kcal(getRecord.users_ar(50, 60))
    aa_ak_g_7 = getRecord.users_avg_kcal(getRecord.users_ar(60, 70))
    aa_ak_g_8 = getRecord.users_avg_kcal(getRecord.users_ar(70, 80))
    aa_ak_g_9 = getRecord.users_avg_kcal(getRecord.users_ar(80, 90))
    aa_ak_g_10 = getRecord.users_avg_kcal(getRecord.users_ar(90, 100))
    aa_ag_g_1 = getRecord.users_avg_goal(getRecord.users_ar(0, 10))
    aa_ag_g_2 = getRecord.users_avg_goal(getRecord.users_ar(10, 20))
    aa_ag_g_3 = getRecord.users_avg_goal(getRecord.users_ar(20, 30))
    aa_ag_g_4 = getRecord.users_avg_goal(getRecord.users_ar(30, 40))
    aa_ag_g_5 = getRecord.users_avg_goal(getRecord.users_ar(40, 50))
    aa_ag_g_6 = getRecord.users_avg_goal(getRecord.users_ar(50, 60))
    aa_ag_g_7 = getRecord.users_avg_goal(getRecord.users_ar(60, 70))
    aa_ag_g_8 = getRecord.users_avg_goal(getRecord.users_ar(70, 80))
    aa_ag_g_9 = getRecord.users_avg_goal(getRecord.users_ar(80, 90))
    aa_ag_g_10 = getRecord.users_avg_goal(getRecord.users_ar(90, 100))
    aa_lg_x = ["0 - 10","11 - 20","21 - 30","31 - 40","41 - 50","51 - 60","61 - 70","71 - 80","81 - 90","91 - 100"]
    aa_lg_y_k = [aa_ak_g_1,aa_ak_g_2,aa_ak_g_3,aa_ak_g_4,aa_ak_g_5,aa_ak_g_6,aa_ak_g_7,aa_ak_g_8,aa_ak_g_9,aa_ak_g_10]
    aa_lg_y_g = [aa_ag_g_1,aa_ag_g_2,aa_ag_g_3,aa_ag_g_4,aa_ag_g_5,aa_ag_g_6,aa_ag_g_7,aa_ag_g_8,aa_ag_g_9,aa_ag_g_10]
    plot(aa_lg_x, aa_lg_y_k)
    plot(aa_lg_x, aa_lg_y_g)
    grid(True)
    xlabel("Age range")
    ylabel("Average kcal burned | Average goal")
    show()

def ak_bg(ab_gender):
    ab_ak_g_1 = getRecord.users_avg_kcal(getRecord.users_ag(0, 10, ab_gender))
    ab_ak_g_2 = getRecord.users_avg_kcal(getRecord.users_ag(10, 20, ab_gender))
    ab_ak_g_3 = getRecord.users_avg_kcal(getRecord.users_ag(20, 30, ab_gender))
    ab_ak_g_4 = getRecord.users_avg_kcal(getRecord.users_ag(30, 40, ab_gender))
    ab_ak_g_5 = getRecord.users_avg_kcal(getRecord.users_ag(40, 50, ab_gender))
    ab_ak_g_6 = getRecord.users_avg_kcal(getRecord.users_ag(50, 60, ab_gender))
    ab_ak_g_7 = getRecord.users_avg_kcal(getRecord.users_ag(60, 70, ab_gender))
    ab_ak_g_8 = getRecord.users_avg_kcal(getRecord.users_ag(70, 80, ab_gender))
    ab_ak_g_9 = getRecord.users_avg_kcal(getRecord.users_ag(80, 90, ab_gender))
    ab_ak_g_10 = getRecord.users_avg_kcal(getRecord.users_ag(90, 100, ab_gender))
    ab_ag_g_1 = getRecord.users_avg_goal(getRecord.users_ag(0, 10, ab_gender))
    ab_ag_g_2 = getRecord.users_avg_goal(getRecord.users_ag(10, 20, ab_gender))
    ab_ag_g_3 = getRecord.users_avg_goal(getRecord.users_ag(20, 30, ab_gender))
    ab_ag_g_4 = getRecord.users_avg_goal(getRecord.users_ag(30, 40, ab_gender))
    ab_ag_g_5 = getRecord.users_avg_goal(getRecord.users_ag(40, 50, ab_gender))
    ab_ag_g_6 = getRecord.users_avg_goal(getRecord.users_ag(50, 60, ab_gender))
    ab_ag_g_7 = getRecord.users_avg_goal(getRecord.users_ag(60, 70, ab_gender))
    ab_ag_g_8 = getRecord.users_avg_goal(getRecord.users_ag(70, 80, ab_gender))
    ab_ag_g_9 = getRecord.users_avg_goal(getRecord.users_ag(80, 90, ab_gender))
    ab_ag_g_10 = getRecord.users_avg_goal(getRecord.users_ag(90, 100, ab_gender))
    ab_lg_x = ["0 - 10","11 - 20","21 - 30","31 - 40","41 - 50","51 - 60","61 - 70","71 - 80","81 - 90","91 - 100"]
    ab_lg_y_k = [ab_ak_g_1,ab_ak_g_2,ab_ak_g_3,ab_ak_g_4,ab_ak_g_5,ab_ak_g_6,ab_ak_g_7,ab_ak_g_8,ab_ak_g_9,ab_ak_g_10]
    ab_lg_y_g = [ab_ag_g_1,ab_ag_g_2,ab_ag_g_3,ab_ag_g_4,ab_ag_g_5,ab_ag_g_6,ab_ag_g_7,ab_ag_g_8,ab_ag_g_9,ab_ag_g_10]
    plot(ab_lg_x, ab_lg_y_k)
    plot(ab_lg_x, ab_lg_y_g)
    grid(True)
    xlabel("Age range")
    ylabel("Average kcal burned | Average goal")
    show()