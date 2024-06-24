from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("Note Taking App")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


def save_note():
  note_to_save = note_core_text.get(1.0, END)
  note = open(f'{note_title_entry.get()}.txt', 'a')
  note.write(note_to_save)
  note.close()
  messagebox.showinfo("Success", "Note saved successfully!")
  note_title_entry.delete(0, 'end')
  note_core_text.delete(1.0, 'end')


note_title = StringVar()

note_title_entry = ttk.Entry(mainframe, width=10, textvariable=note_title)
note_title_entry.grid(column=1, row=1)

note_core_text = Text(mainframe, width=40, height=10)
note_core_text.grid(column=1, row=2)

note_save = ttk.Button(mainframe, text="Save note", command=save_note)
note_save.grid(column=1, row=3)

root.mainloop()
