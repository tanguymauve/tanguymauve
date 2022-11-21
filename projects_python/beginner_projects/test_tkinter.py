from tkinter import *

window = Tk()

for l in range(8):
    for j in range(2):
        frame1 = Frame(
            master=window,
            relief=SUNKEN,
            borderwidth=1
        )

#First Name
lbl_FirstName = Label(frame1,text = "First Name:", justify= RIGHT)
lbl_FirstName.grid(row=1, column=1)
ent_FirstName = Entry(frame1)
ent_FirstName.grid(row=1, column=2)

#Last Name
lbl_LastName = Label(frame1, text = "Last Name:", justify= RIGHT)
lbl_LastName.grid(row=2, column=1)
ent_LastName = Entry(frame1)
ent_LastName.grid(row=2, column=2) 

#AdressLine1
lbl_AdressLine1 = Label(frame1, text= "Adress Line 1:", justify= RIGHT)
lbl_AdressLine1.grid(row=3, column=1) 
ent_AdressLine1 = Entry(frame1)
ent_AdressLine1.grid(row=3, column=2) 

#AdressLine2
lbl_AdressLine2 = Label(frame1, text= "Adress Line 2:", justify= RIGHT)
lbl_AdressLine2.grid(row=4, column=1) 
ent_AdressLine2 = Entry(frame1)
ent_AdressLine2.grid(row=4, column=2) 

#CityName
lbl_CityName = Label(frame1, text= "City:", justify= RIGHT)
lbl_CityName.grid(row=5, column=1) 
ent_CityName = Entry(frame1)
ent_CityName.grid(row=5, column=2) 

#State Province
lbl_State_Province = Label(frame1, text= "State/Province:", justify= RIGHT)
lbl_State_Province.grid(row=6, column=1) 
ent_StateProvince = Entry(frame1)
ent_StateProvince.grid(row=6, column=2) 

#Postal Code
lbl_PostalCode = Label(frame1, text="Postal Code:", justify= RIGHT)
lbl_PostalCode.grid(row=7, column=1) 
ent_PostalCode = Entry(frame1)
ent_PostalCode.grid(row=7, column=2) 

#Country
lbl_Country = Label(frame1, text="Country:", justify= RIGHT)
lbl_Country.grid(row=8, column=1) 
ent_Country = Entry(frame1)
ent_Country.grid(row=8, column=2) 

frame2 = Frame(master=window)
#Button
btn_Clear = Button(frame2, text="Clear", justify= RIGHT)
btn_Clear.grid(row= 9, column=1)
btn_Submit = Button(frame2, text="Submit")
btn_Submit.grid(row=9, column=2)

window.mainloop()