from tkinter import *

window = Tk()

class Point :
    def __init__(self, todo, deadline):
        self.todo = todo
        self.deadline = deadline
        
    def toDo(self):
        # imprimer des objets dans des labels et les afficher
        label = Label(text = todo)
        label.pack()
        
todo1 = Point("Finish the financial accounting video", "End of 22.11.22")
todo2 = Point("Learn about the Central's DD and prepare the interview", "30.11.22")
todo3 = Point("Prepare the interview for Amorino", "End of Wenesday")

todo1.toDo()


window.mainloop()
        
