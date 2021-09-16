from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("learn To Code")
root.iconbitmap("icone.ico")
#root.geometry('800x800')

image_list = []
for i in range(1, 6):
    image_list.append(ImageTk.PhotoImage(Image.open("photo" + str(i) + ".jpg")))

my_label = Label(image=image_list[0])
my_label.grid(row=0, column=0, columnspan=3)

status = Label(root, text="Image 1 of "+ str(len(image_list)), bd = 1, relief = SUNKEN, anchor = E)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])

    my_label.grid(row=0, column=0, columnspan=3)

    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    if image_number == 4:
        print(image_number)
        button_forward = Button(root, text=">>", state=DISABLED)


def back(image_number):
    global my_label
    global button_forward
    global button_back

    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    print(image_number)
    if image_number == 1:
        button_forward = Button(root, text=">>", state=DISABLED)


button_back = Button(root, text="<<", command=back)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)
status.grid(row = 2, column = 0, columnspan = 3, sticky = W+E)
root.mainloop()
