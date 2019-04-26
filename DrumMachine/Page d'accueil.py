from tkinter import *
from tkinter import messagebox
top = Tk()

C = Canvas(top, bg="blue", height=500, width=800)
filename = PhotoImage(file = "Images/FondPapier.png")
background_label = Label(top, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()
top.mainloop