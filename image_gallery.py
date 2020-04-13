from tkinter import *
from PIL import ImageTk, Image
i = 0

root = Tk()


def prev_pic(my_label):
    my_label.grid_forget()  # to delete widget
    global i
    if(i == 0):
        i = len(images)-1
    else:
        i = i-1
    my_label = Label(root, image=images[i])
    my_label.grid(row=0, column=0, columnspan=6)


def next_pic(my_label):
    my_label.grid_forget()
    global i
    if(i == len(images)-1):
        i = 0
    else:
        i = i+1
    my_label = Label(root, image=images[i])
    my_label.grid(row=0, column=0, columnspan=6)


root.title("learning tkinter")
my_image1 = ImageTk.PhotoImage(Image.open("c.jpg"))
my_image2 = ImageTk.PhotoImage(Image.open("b.jpg"))
my_image3 = ImageTk.PhotoImage(Image.open("c.jpg"))
my_image4 = ImageTk.PhotoImage(Image.open("b.jpg"))
images = [my_image1, my_image2, my_image3, my_image4]
my_label = Label(root, image=my_image1)
my_label.grid(row=0, column=0, columnspan=6)
back_button = Button(root, text="<", command=lambda: prev_pic(my_label))
button_exit = Button(root, text="Exit", width=40, command=root.quit)
forward_button = Button(root, text=">", command=lambda: next_pic(my_label))
back_button.grid(row=1, column=0)
forward_button.grid(row=1, column=5)
button_exit.grid(row=1, column=1, columnspan=3)


root.mainloop()
