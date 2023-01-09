#python3
#Author Vivek Kumar

import tkinter
from tkinter import *
from PIL import Image, ImageTk
import pyshorteners


def submit():
    long_url = name_var.get()
    type_tiny = pyshorteners.Shortener()
    short_url = type_tiny.tinyurl.short(long_url)
    name_label = Label(main, text=short_url,
                       bg='#ffffff', font=('calibre', 12, 'bold'))
    name_label.grid(row=7, column=4)


def Shortner():
    global name_var, main
    main = Tk()
    main.title("Url Shortner")
    main.geometry("700x550")
    main.config(background="#ffffff")
    main.resizable(height=0, width=0)
    name_var = tkinter.StringVar()

    name_label = Label(main, text='URL', bg='#ffffff',
                       font=('calibre', 10, 'bold'))
    name_entry = Entry(main, textvariable=name_var, width=50,
                       font=('calibre', 10, 'normal'))
    sub_btn = Button(main, text='Submit', command=submit)
    sub_btn.grid(row=5, column=4)
    name_label.grid(row=2, column=2)
    name_entry.grid(row=2, column=4)
    main.mainloop()


def startIspressed():
    root.destroy()
    Shortner()


root = tkinter.Tk()
root.title("Url Shortner")
root.geometry("700x550")
root.config(background="#ffffff")
root.resizable(height=0, width=0)

img = Image.open("start-button.png")
resize_image = img.resize((60, 60))
start_img = ImageTk.PhotoImage(resize_image)

img2 = Image.open("link.png")
resize_image2 = img2.resize((100, 100))
start_img2 = ImageTk.PhotoImage(resize_image2)
labeltext2 = Label(
    root,
    image=start_img2,
    background="#ffffff",
)
labeltext2.pack(pady=(20))
labeltext = Label(
    root,
    text="Url Shortner",
    font=("Consolas", 24, "italic"),
    background="#ffffff",
)
labeltext.pack(pady=(0, 50))

btnStart = Button(
    root,
    image=start_img,
    border=0,
    relief=FLAT,
    command=startIspressed
    # background="#ffffff",
)
btnStart.pack(pady=(40, 0))


lblInstruction = Label(
    root,
    text="Read The Rules And\nClick Start Once You Are ready",
    background="#ffffff",
    font=("Consolas", 14),
    justify="center",
)
lblInstruction.pack(pady=(10, 10))

lblRules = Label(
    root,
    text="When you click on the start Button\nYou will have to Enter\nThe url of the site and then pressed the\nSHORTNER \nand your Url will be shorted",
    width=100,
    font=("Times", 14),
    background="#534b4f",
    foreground="#fdee00",
)
lblRules.pack(pady=(10, 0))

root.mainloop()
