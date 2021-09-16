from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("learn To Code")
root.iconbitmap("icone.ico")


def open_new_window():
    global my_img
    top = Toplevel()
    top.title("My Second window")
    top.iconbitmap("icone.ico")
    my_img = ImageTk.PhotoImage(Image.open("photo1.jpg"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="close window", command=top.destroy).pack()


btn = Button(root, text="Open Second Windows", command=open_new_window).pack()

root.mainloop()
