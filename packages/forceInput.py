# ~~~~~~~~~~~~~~~~~~~~~~~

# Initialize
stb_integer = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
stb_float = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".")
stb_lowercase = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
stb_uppercase = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")

# Functions
def get_sport(gs_mode):
    if gs_mode == "initialize":
        gs_i_data = list(())
        with open("database/sports.txt","r") as db_f_sports:
            db_c_sports = db_f_sports.read().splitlines()
            for db_c_sports_each in db_c_sports:
                gs_i_data.append(db_c_sports_each.split(" : ")[0])
                gs_i_data.extend(db_c_sports_each.split(" : ")[1].split(", ")[:-1])
            db_f_sports.close()
        gs_i_content = tuple(gs_i_data)
        return gs_i_content
    elif gs_mode == "main":
        gs_m_data = list(())
        gs_m_text = ""
        with open("database/sports.txt","r") as db_f_sports:
            db_c_sports = db_f_sports.read().splitlines()
            for db_c_sports_each in db_c_sports:
                gs_m_data.append(db_c_sports_each.split(" : ")[0])
            db_f_sports.close()
        for gs_m_text_row in range(4):
            gs_m_text += "\t\t"
            for gs_m_text_col in range(4):
                gs_m_text += "\t" + gs_m_data[4 * gs_m_text_row + gs_m_text_col]
            gs_m_text += "\n"
        gs_m_content = gs_m_text[2:-1]
        return gs_m_content

def integers(i_ask, i_error = "Please enter a value", i_choice = None):
    while True:
        i_input = input(i_ask)
        if i_input != "":
            i_check = set(())
            for i_each in i_input:
                i_check.add(i_each in stb_integer)
            if False not in i_check:
                i_convert = int(i_input)
                if i_choice != None:
                    if i_convert in i_choice:
                        break
                    else:
                        print("Unavailable choice")
                else:
                    break
            else:
                print("Input contains invalid characters")
        else:
            print(i_error)
    return i_convert

def strings(s_ask, s_error = "Please enter a value", s_choice = None):
    while True:
        s_input = input(s_ask)
        if s_input != "":
            s_check = set(())
            for s_each in s_input:
                s_check.add(s_each in stb_lowercase or s_each in stb_uppercase)
            if False not in s_check:
                s_convert = str(s_input).lower()
                if s_choice != None:
                    if s_convert in s_choice:
                        break
                    else:
                        print("Unavailable choice")
                else:
                    break
            else:
                print("Input contains invalid characters")
        else:
            print(s_error)
    return s_convert

def floats(f_ask, f_error = "Please enter a value"):
    while True:
        f_input = input(f_ask)
        if f_input != "":
            f_check = set(())
            for f_each in f_input:
                f_check.add(f_each in stb_float)
            if False not in f_check:
                f_convert = float(f_input)
                break
            else:
                print("Input contains invalid characters")
        else:
            print(f_error)
    return f_convert