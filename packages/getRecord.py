# ~~~~~~~~~~~~~~~~~~~~~~~

# Import
from packages import getData

# Functions
def goal(g_id, g_sport):
    with open("database/appointment.csv","r") as db_f_appointment:
        for db_c_appointment_category in db_f_appointment.readlines():
            if db_c_appointment_category.split(",")[0] == g_id and db_c_appointment_category.split(",")[1].upper() == g_sport.upper():
                g_goal = float(db_c_appointment_category.split(",")[2])
        db_f_appointment.close()
    return g_goal

def total(t_id, t_sport):
    with open("database/appointment.csv","r") as db_f_appointment:
        for db_c_appointment_category in db_f_appointment.readlines():
            if db_c_appointment_category.split(",")[0] == t_id and db_c_appointment_category.split(",")[1].upper() == t_sport.upper():
                t_record = db_c_appointment_category.split(",")[4]
        db_f_appointment.close()
    if t_record == "":
        return 0
    else:
        t_record_each = t_record[:-1].split(";")[:-1]
        t_record_total = 0
        for t_record_convert in t_record_each:
            t_record_number = float(t_record_convert)
            t_record_total += t_record_number
        t_content = float(t_record_total)
    return t_content

def count(c_user, c_sport):
    c_id = getData.id(c_user)
    with open("database/appointment.csv","r") as db_f_appointment:
        for db_c_appointment_category in db_f_appointment.readlines():
            if db_c_appointment_category.split(",")[0] == c_id and db_c_appointment_category.split(",")[1].upper() == c_sport.upper():
                c_count = len(db_c_appointment_category.split(",")[4].split(";")[:-1])
                break
        db_f_appointment.close()
    return c_count

def each_record(er_user, er_sport):
    er_id = getData.id(er_user)
    with open("database/appointment.csv","r") as db_f_appointment:
        for db_c_appointment_category in db_f_appointment.readlines():
            if db_c_appointment_category.split(",")[0] == er_id and db_c_appointment_category.split(",")[1].upper() == er_sport.upper():
                er_record = db_c_appointment_category.split(",")[4].split(";")[:-1]
                break
        db_f_appointment.close()
    er_content = [0.0]
    for er_conv_each in er_record:
        er_content.append(float(er_conv_each))
    return er_content

def users_ar(ua_age_min, ua_age_max):
    ua_list = list(())
    with open("database/user.csv","r") as db_f_user:
        for db_c_each in db_f_user.readlines():
            if db_c_each.split(",")[2] != "age":
                db_c_age = int(db_c_each.split(",")[2])
                if db_c_age > ua_age_min and db_c_age <= ua_age_max:
                    ua_list.append(db_c_each.split(",")[0])
        db_f_user.close()
    return ua_list

def users_avg_kcal(uak_users):
    uak_count = 0
    uak_total = 0
    with open("database/appointment.csv","r") as db_f_appointment:
        for db_c_appointment_category in db_f_appointment.readlines():
            if db_c_appointment_category.split(",")[0] in uak_users:
                for uak_each_record in db_c_appointment_category.split(",")[4].split(";")[:-1]:
                    uak_total += float(uak_each_record)
                uak_count += 1
        db_f_appointment.close()
    if uak_count > 0:
        uak_avg = round(uak_total / uak_count, 2)
        return uak_avg
    else:
        return 0

def users_avg_goal(uag_users):
    uag_count = 0
    uag_total = 0
    with open("database/appointment.csv","r") as db_f_appointment:
        for db_c_appointment_category in db_f_appointment.readlines():
            if db_c_appointment_category.split(",")[0] in uag_users:
                uag_total += float(db_c_appointment_category.split(",")[2])
                uag_count += 1
        db_f_appointment.close()
    if uag_count > 0:
        uag_avg = round(uag_total / uag_count, 2)
        return uag_avg
    else:
        return 0

def users_ag(ua_age_min, ua_age_max, ua_gender):
    ua_list = list(())
    with open("database/user.csv","r") as db_f_user:
        for db_c_each in db_f_user.readlines():
            if db_c_each.split(",")[2] != "age":
                db_c_age = int(db_c_each.split(",")[2])
                db_c_gender = db_c_each.split(",")[3]
                ua_condition_1 = db_c_age > ua_age_min and db_c_age <= ua_age_max
                ua_condition_2 = ua_gender == db_c_gender
                if ua_condition_1 and ua_condition_2:
                    ua_list.append(db_c_each.split(",")[0])
        db_f_user.close()
    return ua_list