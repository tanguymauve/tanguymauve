from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

window = Tk()
window.title("Address Entry Form")
style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")

frame1 = Frame(
            master = window,
            relief=SUNKEN,
            borderwidth=3,
            )
frame1.grid(row=0,column=0)

#First Name
lbl_FirstName = Label(frame1, text = "First Name:")
lbl_FirstName.grid(row=1, column=1, sticky="e")
ent_FirstName = Entry(frame1, width= 40)
ent_FirstName.grid(row=1, column=2, sticky="e")

#Last Name
lbl_LastName = Label(frame1, text = "Last Name:")
lbl_LastName.grid(row=2, column=1, sticky="e")
ent_LastName = Entry(frame1, width= 40)
ent_LastName.grid(row=2, column=2, sticky="e") 

#AdressLine1
lbl_AdressLine1 = Label(frame1, text= "Adress Line 1:")
lbl_AdressLine1.grid(row=3, column=1, sticky="e") 
ent_AdressLine1 = Entry(frame1, width= 40)
ent_AdressLine1.grid(row=3, column=2, sticky="e") 

#AdressLine2
lbl_AdressLine2 = Label(frame1, text= "Adress Line 2:")
lbl_AdressLine2.grid(row=4, column=1, sticky="e") 
ent_AdressLine2 = Entry(frame1, width= 40)
ent_AdressLine2.grid(row=4, column=2, sticky="e") 

#CityName
lbl_CityName = Label(frame1, text= "City:")
lbl_CityName.grid(row=5, column=1, sticky="e") 
ent_CityName = Entry(frame1, width= 40)
ent_CityName.grid(row=5, column=2, sticky="e") 

#State Province
lbl_State_Province = Label(frame1, text= "State/Province:")
lbl_State_Province.grid(row=6, column=1, sticky="e") 
ent_StateProvince = Entry(frame1, width= 40)
ent_StateProvince.grid(row=6, column=2, sticky="e") 

#Postal Code
lbl_PostalCode = Label(frame1, text="Postal Code:")
lbl_PostalCode.grid(row=7, column=1, sticky="e") 
ent_PostalCode = Entry(frame1, width= 40)
ent_PostalCode.grid(row=7, column=2, sticky="e") 

#Country
lbl_Country = Label(frame1, text="Country:")
lbl_Country.grid(row=8, column=1, sticky="e") 
ent_Country = Entry(frame1, width= 40)
ent_Country.grid(row=8, column=2, sticky="e") 


#Deuxième Frame
frame2 = Frame(master=window,
               width=470,
               height=35)

frame2.grid(row=10, padx=5)
frame2.grid_propagate(0)

frame2.columnconfigure(1, weight=1)
frame2.columnconfigure(2, weight=1)


#Button
btn_Clear = Button(frame2, text="Clear")
btn_Clear.grid(row= 1, column=2, sticky="e", padx=80)

btn_Submit = Button(frame2, text="Submit")
btn_Submit.grid(row=1, column=2, sticky="e")

#lbl_Test = Label(frame2, text="je comprends r")
#lbl_Test.grid()

window.mainloop()