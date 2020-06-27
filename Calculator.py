from tkinter import *

root = Tk()


class Calculator:
    def __init__(self, master):
        # title and size
        master.title("Calculator")
        master.geometry("500x500")
        # menu bar
        menubar = Menu(master)
        list=Menu(menubar,tearoff=0)
        list.add_command(label="history")
        menubar.add_cascade(label="Options",menu=list)
        master.config(menu=menubar)
        #display field
        result = StringVar()
        input_field = Entry(root, textvariable=result)
        input_field.place(width=500, height=50)


my_calc = Calculator(root)
root.mainloop()
