from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("learn To Code")
root.iconbitmap("icone.ico")

frame = LabelFrame(root, text="This is my Frame...", padx=100, pady=100)  # http://prntscr.com/15fx9fs
frame.pack(padx=50, pady=50)


b = Button(frame, text="Don't click here!")
b2 = Button(frame, text="..............")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)















root.mainloop()