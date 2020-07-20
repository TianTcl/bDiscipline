# ~~~~~~~~~~~~~~~~~~~~~~~

# Import
from packages import iSmart

# Functions
def user(u_mode = 0):
    db_c_user = list(())
    with open("database/user.csv","r") as db_f_user:
        for db_c_user_category in db_f_user.readlines():
            if db_c_user_category.split(",")[0] == "id":
                db_c_user_index = int(db_c_user_category.split(",").index("name"))
            else:
                if u_mode == 0:
                    db_c_user.append(db_c_user_category.split(",")[db_c_user_index])
                elif u_mode == 1:
                    db_c_user.append(db_c_user_category.split(",")[db_c_user_index].upper())
        db_f_user.close()
    return db_c_user

def new_id():
    with open("database/user.csv","r") as db_f_user:
        for db_c_user_category in db_f_user.readlines():
            ni_last_id = db_c_user_category.split(",")[0]
        ni_new_id = int(ni_last_id) + 1
        ni_new_text = ""
        ni_new_len = len(str(ni_new_id))
        if ni_new_len <= 5:
            ni_req_zero = 5 - ni_new_len
            for ni_each_zero in range(ni_req_zero):
                ni_new_text += "0"
            del ni_each_zero
            ni_new_text += str(ni_new_id)
        db_f_user.close()
    return ni_new_text

def id(i_user):
    with open("database/user.csv","r") as db_f_user:
        for db_c_user_category in db_f_user.readlines():
            if db_c_user_category.split(",")[1].upper() == i_user.upper():
                i_id = db_c_user_category.split(",")[0]
                break
        db_f_user.close()
    return i_id

def sport(s_id, s_mode = 0):
    s_sport = list(())
    with open("database/appointment.csv","r") as db_f_appointment:
        for db_c_appointment_category in db_f_appointment.readlines():
            if db_c_appointment_category.split(",")[0] == s_id:
                if s_mode == 0:
                    s_sport.append(db_c_appointment_category.split(",")[1])
                elif s_mode == 1:
                    s_sport.append(db_c_appointment_category.split(",")[1].upper())
        db_f_appointment.close()
    return s_sport

def bio(b_id):
    with open("database/user.csv","r") as db_f_user:
        for db_c_user_category in db_f_user.readlines():
            if db_c_user_category.split(",")[0] == b_id:
                b_name = db_c_user_category.split(",")[1]
                b_age = db_c_user_category.split(",")[2]
                b_gender = db_c_user_category.split(",")[3]
                break
        db_f_user.close()
    b_content = "ID\t: "+ b_id +"\nName\t: "+ b_name +"\nAge\t: "+ b_age +"\nGender\t: "+ b_gender
    return b_content

def workout(w_id, w_sport):
    with open("database/appointment.csv","r") as db_f_appointment:
        for db_c_appointment_category in db_f_appointment.readlines():
            if db_c_appointment_category.split(",")[0] == w_id and db_c_appointment_category.split(",")[1] == w_sport:
                w_goal = db_c_appointment_category.split(",")[2]
                w_time = db_c_appointment_category.split(",")[3]
                w_record = db_c_appointment_category.split(",")[4]
                break
        db_f_appointment.close()
    w_time_read = iSmart.read("time", w_time)
    w_record_read = iSmart.read("record", w_record)
    w_content = "Sport\t: "+ w_sport +"\nGoal\t: "+ w_goal +" kcal\nTime recommend\t: "+ w_time_read +"\nRecords\t: "+ w_record_read
    return w_content