from tkinter import *

root = Tk()


class Calculator:
    def hist(self):
        self.f=open("history_calc.txt","r")
        self.temp=Tk()
        self.temp.title("history")
        self.temp.geometry("100x300")
        self.t=Text(self.temp,height=300,width=100)
        self.t.pack()
        self.t.insert(END,self.f.read())

    def __init__(self, master):
        # title and size
        master.title("Calculator")
        master.geometry("500x500")
        # menu bar
        menubar = Menu(master)
        list=Menu(menubar,tearoff=0)
        list.add_command(label="history",command=self.hist)
        list.add_command(label="Exit",command=master.quit)
        menubar.add_cascade(label="Options",menu=list)
        master.config(menu=menubar)
        #display field
        result = StringVar()
        input_field = Entry(root, textvariable=result)
        input_field.place(width=500, height=50)


my_calc = Calculator(root)
root.mainloop()
