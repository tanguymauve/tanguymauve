from tkinter import *
from tkinter import ttk


def convert_kg_to_lbs():
  try:
    weight_kgs = float(weight_entry.get())
    result.set(f"{weight_kgs * 2.20462262:.2f} lbs")
  except ValueError:
    result.set("Invalid input")


def convert_lbs_to_kg():
  try:
    weight_lbs = float(weight_entry.get())
    result.set(f"{weight_lbs / 2.20462262:.2f} kg")
  except ValueError:
    result.set("Invalid input")


root = Tk()
root.title("Weight Converter")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

weight_label = ttk.Label(mainframe, text="Enter your weight")
weight_entry = ttk.Entry(mainframe, width=6)
weight_label.grid(column=1, row=1, sticky=(E))
weight_entry.grid(column=2, row=1, sticky=(W, E))

result = StringVar()
kgs_button = ttk.Button(mainframe, text="To kilos", command=convert_lbs_to_kg)
kgs_button.grid(column=1, row=2, sticky=(N, S))

lbs_button = ttk.Button(mainframe, text="To pounds", command=convert_kg_to_lbs)
lbs_button.grid(column=2, row=2, sticky=(N, S))

result_label = ttk.Label(mainframe, textvariable=result)
result_text = ttk.Label(mainframe, text="Result")
result_label.grid(column=2, row=3, columnspan=2, sticky=(E))
result_text.grid(column=1, row=3)

for child in mainframe.winfo_children():
  child.grid_configure(padx=5, pady=5)

weight_entry.focus()
root.mainloop()