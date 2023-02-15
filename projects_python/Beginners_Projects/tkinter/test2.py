from tkinter import *

window = Tk()

label = []
entry = []
for i in range(8):
    label = Label(text="hello there")
    label.grid(row = i, column=1)
    entry = Entry()
    entry.grid(row = i, column=2)
        #First Name
    lbl_FirstName = Label(text = "First Name:")
    lbl_FirstName.grid(row=1, column=1, sticky="e")
    label.append(lbl_FirstName)
    ent_FirstName = Entry(width= 40)
    entry.append
    ent_FirstName.grid(row=1, column=2, sticky="e")

    #Last Name
    lbl_LastName = Label(text = "Last Name:")
    lbl_LastName.grid(row=2, column=1, sticky="e")
    ent_LastName = Entry(width= 40)
    ent_LastName.grid(row=2, column=2, sticky="e")


window.mainloop()