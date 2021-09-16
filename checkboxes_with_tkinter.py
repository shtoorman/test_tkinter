from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title("learn To Code")
root.iconbitmap("icone.ico")
root.geometry("400x400")

# var = IntVar()
#
# c = Checkbutton(root, text="Check this box, I dare you!", variable=var)
# c.pack()

# var = IntVar()
# c = Checkbutton(root, text="Check this box, I dare you!", variable=var)
# c.pack()

var = StringVar()

c = Checkbutton(root, text="Check this box, I dare you!", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()


def show():
    myLabel = Label(root, text=var.get()).pack()


myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()
