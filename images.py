from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("learn To Code")
root.iconbitmap("icone.ico")

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

my_img = ImageTk.PhotoImage(Image.open("photo1.jpg"))
my_label = Label(image=my_img)
my_label.pack()

root.mainloop()
