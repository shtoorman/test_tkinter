from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("learn To Code")
root.iconbitmap("icone.ico")
#root.geometry('800x800')

my_img_list = []
for i in range(1, 6):
    my_img_list.append(ImageTk.PhotoImage(Image.open("photo" + str(i) + ".jpg")))

my_label = Label(image=my_img_list[0])
my_label.grid(row=0, column=0, columnspan=3)

status = Label(root, text="Image 1 of " + str(len(my_img_list)), bd=1, relief=SUNKEN, anchor=E)


def forward(image_number):
    global my_label
    global forward
    global back

    my_label.grid_forget()

    my_label = Label(image=my_img_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 5:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

    status = Label(root, text="Image " + str(image_number) + " of " + str(len(my_img_list)), bd=1, relief=SUNKEN,
                   anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


def back(image_number):
    global my_label
    global forward
    global back

    my_label.grid_forget()

    my_label = Label(image=my_img_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

    status = Label(root, text="Image " + str(image_number) + " of " + str(len(my_img_list)), bd=1, relief=SUNKEN,
                   anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


button_back = Button(root, text="<<", state=DISABLED, command=lambda: back())
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1, pady=10)
button_forward.grid(row=1, column=2)
status.grid(row=2, column=0, columnspan=3, sticky=W + E)

root.mainloop()