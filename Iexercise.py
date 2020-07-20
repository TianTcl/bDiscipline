# ~~~~~~~~~~~~~~~~~~~~~~~

# Imports
from packages import forceInput, plot, store
from tkinter import messagebox as w_messagebox, simpledialog as w_inputbox

# Functions
def welcome():
    Tk().withdraw()
    w_messagebox.showinfo("Iexercise", "Welcome\nThis program will help you records and remind you to exercise\nand help build your discipline in exercising")

def mode(prefill = None):
    if prefill == None:
        mode = forceInput.integers("1) Store | keep\n2) Analyse\nSelect what you want to do : ", "Please select a choice", [1, 2])
    elif prefill != None:
        mode = prefill
    if mode == 1:
        store.execute()
    elif mode == 2:
        plot.execute()

def select():
    # Init screen
    s_window = Tk()
    s_window.loadtk()
    s_window.title("Select")
    s_window.geometry("640x480")
    #s_window.geometry("800x600")
    s_window.mainloop()
    s_app = Frame(s_window)
    s_app.grid()
    # Init button
    s_b_record = Button(s_window, text = "Record", command = mode(1), )
    s_b_record.size(width = 200, height = 200)
    s_b_record.place(x = 40, y = 240)
    s_b_plot = Button(s_window, text = "Record", command = mode(2), )
    s_b_plot.size(width = 200, height = 200)
    s_b_plot.place(x = 400, y = 240)

# Code starts
welcome()
#select()
mode()