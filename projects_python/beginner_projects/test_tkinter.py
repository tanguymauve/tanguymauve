from tkinter import *

window = Tk()
window.configure(bg='blue')
#for l in range(8):
    #for j in range(2):
frame1 = Frame(
            master = window,
            relief=SUNKEN,
            borderwidth=3,
            )
frame1.grid(row=0,column=0)

#First Name
lbl_FirstName = Label(frame1, text = "First Name:")
lbl_FirstName.grid(row=1, column=1)
ent_FirstName = Entry(frame1, width= 40)
ent_FirstName.grid(row=1, column=2)

#Last Name
lbl_LastName = Label(frame1, text = "Last Name:")
lbl_LastName.grid(row=2, column=1)
ent_LastName = Entry(frame1, width= 40)
ent_LastName.grid(row=2, column=2) 

#AdressLine1
lbl_AdressLine1 = Label(frame1, text= "Adress Line 1:")
lbl_AdressLine1.grid(row=3, column=1) 
ent_AdressLine1 = Entry(frame1, width= 40)
ent_AdressLine1.grid(row=3, column=2) 

#AdressLine2
lbl_AdressLine2 = Label(frame1, text= "Adress Line 2:")
lbl_AdressLine2.grid(row=4, column=1) 
ent_AdressLine2 = Entry(frame1, width= 40)
ent_AdressLine2.grid(row=4, column=2) 

#CityName
lbl_CityName = Label(frame1, text= "City:")
lbl_CityName.grid(row=5, column=1) 
ent_CityName = Entry(frame1, width= 40)
ent_CityName.grid(row=5, column=2) 

#State Province
lbl_State_Province = Label(frame1, text= "State/Province:")
lbl_State_Province.grid(row=6, column=1) 
ent_StateProvince = Entry(frame1, width= 40)
ent_StateProvince.grid(row=6, column=2) 

#Postal Code
lbl_PostalCode = Label(frame1, text="Postal Code:")
lbl_PostalCode.grid(row=7, column=1) 
ent_PostalCode = Entry(frame1, width= 40)
ent_PostalCode.grid(row=7, column=2) 

#Country
lbl_Country = Label(frame1, text="Country:")
lbl_Country.grid(row=8, column=1) 
ent_Country = Entry(frame1, width= 40)
ent_Country.grid(row=8, column=2) 


#Deuxième Frame
frame2 = Frame(master=window,
               borderwidth=1,
               width=470,
               height=50,
               background="bisque")

frame2.grid(row=10, column=0, padx=5, pady=5)
frame2.grid_propagate(0)

frame2.columnconfigure(1, weight=1)
frame2.columnconfigure(2, weight=1)


#Button
btn_Clear = Button(frame2, text="Clear", bg='red')
btn_Clear.grid(row= 1, column=1, sticky="n")

btn_Submit = Button(frame2, text="Submit", bg='yellow')
btn_Submit.grid(row=1, column=2, sticky="e")

#lbl_Test = Label(frame2, text="je comprends r")
#lbl_Test.grid()

window.mainloop()