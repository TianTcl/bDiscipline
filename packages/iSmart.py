# ~~~~~~~~~~~~~~~~~~~~~~~

# Functions
def read(r_type, r_data):
    if r_type == "time":
        r_time = ""
        for r_time_char in r_data:
            if r_time_char == "h":
                if int(r_time) == 0:
                    r_time = ""
                elif int(r_time) == "1":
                    r_time += " hour "
                else:
                    r_time += " hours "
            elif r_time_char == "m":
                if " h" in r_time:
                    if int(r_time.split(" ")[2]) == "0":
                        r_time = r_time[:-3]
                    elif int(r_time.split(" ")[2]) == "1":
                        r_time += " minute"
                    else:
                        r_time += " minutes"
                else:
                    if int(r_time) == 0:
                        r_time = "Done!"
                    elif int(r_time) == "1":
                        r_time += " minute"
                    else:
                        r_time += " minutes"
            else:
                r_time += r_time_char
        return r_time
    elif r_type == "record":
        if r_data == "":
            return "-"
        else:
            r_record_each = r_data[:-1].split(";")[:-1]
            r_record_new = ""
            r_record_total = 0
            for r_record_convert in r_record_each:
                r_record_number = float(r_record_convert)
                r_record_new += " + "+ str(r_record_number)
                r_record_total += r_record_number
            r_record = r_record_new[2:] +" = "+ str(r_record_total) +" kcal"
            return r_record

def convert(c_type, c_data):
    if c_type == "list":
        c_l_content = ""
        for c_l_each in c_data:
            c_l_content += c_l_each +","
        c_l_data = c_l_content[:-1]
        return c_l_data
    elif c_type == "appointment":
        c_a_content = ""
        for c_a_each in c_data:
            c_a_content += c_a_each +"\n"
        c_a_data = c_a_content[:-1]
        return c_a_data
    elif c_type == "time":
        c_t_total = int(round(float(c_data)))
        c_t_hour = c_t_total // 60
        c_t_minute = c_t_total % 60
        c_t_data = str(c_t_hour) +"h"+ str(c_t_minute) +"m"
        return c_t_data

def lists(l_max):
    l_content = list(())
    for l_each in range(l_max + 1):
        l_content.append(l_each)
    return l_content