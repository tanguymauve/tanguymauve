import tkinter as tk
from datetime import datetime

root = tk.Tk()

def update_window():
    label.config(text="Time is " + currentTime.strftime("%H:%M:%S"), font = "helvetica 20")
    root.after(1000, update_window)

currentTime = datetime.now()

label = tk.Label(text = "Time is " + currentTime.strftime("%H:%M:%S"), font ="helvetica 20")
label.pack(padx = 50, pady = 50)

update_window()

root.mainloop()

