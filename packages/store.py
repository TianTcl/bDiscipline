# ~~~~~~~~~~~~~~~~~~~~~~~

# Import
from packages import forceInput, getData, iSmart, iTime, plot

# Functions
def execute():
    while True:
        check_u(forceInput.strings("\nUser : "))

def check_u(c_user):
    db_c_user = getData.user(1)
    if c_user.upper() not in db_c_user:
        new_u(c_user)
    print("Available exercises :" + forceInput.get_sport("main"))
    check_s(c_user, forceInput.strings("Sport to record : ", "Please choose a sport", forceInput.get_sport("initialize")))

def check_s(c_user, c_sport):
    db_c_user_sport = getData.sport(getData.id(c_user), 1)
    if c_sport.upper() not in db_c_user_sport:
        new_s(c_user, c_sport)
    update(c_user, c_sport)

def update(u_user, u_sport):
    # Get biodata
    u_id = getData.id(u_user)
    u_bio = getData.bio(u_id)
    u_dat = getData.workout(u_id, u_sport)
    # Show : Data
    print(u_bio +"\n"+ u_dat)
    # Input : Record
    u_record_time = forceInput.integers("Enter your record (minutes) : ", "Please enter your record")
    u_record_kcal = iTime.convert(u_sport, u_record_time)
    # Update : Sport data
    add_update(u_id, u_sport, u_record_kcal)
    # Check : Completed to plot
    if plot.auto("check", u_user, u_sport):
        plot.auto("generate", u_user, u_sport)

def add_update(au_id, au_sport, au_record):
    with open("database/appointment.csv","r") as db_f_appointment:
        db_c_appointment = db_f_appointment.read().splitlines()
        for au_content_each in db_c_appointment:
            if au_content_each.split(",")[0] == au_id and au_content_each.split(",")[1].upper() == au_sport.upper():
                au_record_old = au_content_each.split(",")[4]
                au_content_index = db_c_appointment.index(au_content_each)
                au_content = au_content_each.split(",")
                break
        au_record_new = au_record_old + str(au_record) + ";"
        au_content.pop(4)
        au_content.append(au_record_new)
        au_content_text = iSmart.convert("list", au_content)
        db_f_appointment.close()
    db_c_appointment.pop(au_content_index)
    db_c_appointment.insert(au_content_index, au_content_text)
    au_update_text = iSmart.convert("appointment", db_c_appointment)
    with open("database/appointment.csv","w") as db_f_appointment:
        db_f_appointment.write(au_update_text)
        db_f_appointment.close()

def new_u(n_name):
    # Input : Biodata
    new_age = forceInput.integers("Enter your age : ")
    new_gender = forceInput.strings("Enter you gender (male/female) : ", "Please enter your gender", ["male", "female"])
    # Generate : ID
    new_id = getData.new_id()
    # Generate : Data
    content = "\n"+ new_id +","+ n_name +","+ str(new_age) +","+ new_gender
    # Store : New user
    with open("database/user.csv","a") as db_f_user:
        db_f_user.write(content)
        db_f_user.close()

def new_s(n_user, n_sport):
    # Setting up data
    n_id = getData.id(n_user)
    n_goal = forceInput.floats("Enter your goal (kcal) : ")
    n_time = iTime.get(n_sport, n_goal)
    n_data = "\n"+ n_id +","+ n_sport.lower() +","+ str(n_goal) +","+ n_time +","
    # Store : New sport
    with open("database/appointment.csv","a") as db_f_appointment:
        db_f_appointment.write(n_data)
        db_f_appointment.close()