from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title("learn To Code")
root.iconbitmap("icone.ico")


def open():
    root.filename = filedialog.askopenfilename(initialdir=r"C:\Users\aleksandr.balandin\Downloads\Python\Codemy",
                                               title="Select a file",
                                               filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    global my_image
    my_image = ImageTk.PhotoImage(Image.open(root.filename))

    my_image_label = Label(image=my_image).pack()


my_btn = Button(root, text="Open File", command=open).pack()

root.mainloop()
