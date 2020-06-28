from tkinter import *

root = Tk()
content = ""


class Calculator:
    def hist(self):
        self.f = open("history_calc.txt", "r")
        self.temp = Tk()
        self.temp.title("history")
        self.temp.geometry("100x300")
        self.t = Text(self.temp, height=300, width=100)
        self.t.pack()
        self.t.insert(END, self.f.read())

    def click_button(self, val):
        global content
        content += str(val)
        self.result.set(content)

    def equal_btn(self):
        global content
        data = content + "="
        final_data = eval(content)
        self.result.set(final_data)
        content = ""
        data += str(final_data)
        f = open("history_calc.txt", "a")
        f.write("\n" + data)
        f.close()

    def clear_btn(self):
        global content
        content = ""
        self.result.set(content)

    def __init__(self, master):
        # title and size
        master.title("Calculator")
        master.geometry("500x500+450+100")
        # menu bar
        menubar = Menu(master)
        menu_list = Menu(menubar, tearoff=0)
        menu_list.add_command(label="history", command=self.hist)
        menu_list.add_command(label="Exit", command=master.quit)
        menubar.add_cascade(label="Options", menu=menu_list)
        master.config(menu=menubar)
        # display field
        self.result = StringVar()
        top_frame = Frame(master, width=500, height=50, bd=3, relief="raised")
        top_frame.pack(side=TOP)
        input_field = Entry(top_frame, textvariable=self.result, width=60, justify="right", bd=3)
        input_field.grid(row=0, column=0)
        # label
        main_label = Label(master, width=30, height=10, bd=5, bg="#425e51", relief="raised")
        main_label.pack(side=LEFT, fill=BOTH, expand=True)
        l7 = Label(main_label, bg="black")
        l7.grid(row=1, column=0)
        b7 = Button(l7, text='7', font=('Helvetica', '16'), command=lambda: self.click_button(7), bg='black',
                    fg='#823E30')
        b7.pack()

        l8 = Label(main_label, bg="black")
        l8.grid(row=1, column=1)
        b8 = Button(l8, text='8', font=('Helvetica', '16'), command=lambda: self.click_button(8), bg='black',
                    fg='#823E30')
        b8.pack()

        l9 = Label(main_label, bg="black")
        l9.grid(row=1, column=2)
        b9 = Button(l9, text='9', font=('Helvetica', '16'), command=lambda: self.click_button(9), bg='black',
                    fg='#823E30')
        b9.pack()

        l4 = Label(main_label, bg="black")
        l4.grid(row=2, column=0)
        b4 = Button(l4, text='4', font=('Helvetica', '16'), command=lambda: self.click_button(4), bg='black',
                    fg='#823E30')
        b4.pack()

        l5 = Label(main_label, bg="black")
        l5.grid(row=2, column=1)
        b5 = Button(l5, text='5', font=('Helvetica', '16'), command=lambda: self.click_button(5), bg='black',
                    fg='#823E30')
        b5.pack()

        l6 = Label(main_label, bg="black")
        l6.grid(row=2, column=2)
        b6 = Button(l6, text='6', font=('Helvetica', '16'), command=lambda: self.click_button(6), bg='black',
                    fg='#823E30')
        b6.pack()

        l1 = Label(main_label, bg="black")
        l1.grid(row=3, column=0)
        b1 = Button(l1, text='1', font=('Helvetica', '16'), command=lambda: self.click_button(1), bg='black',
                    fg='#823E30')
        b1.pack()

        l2 = Label(main_label, bg="black")
        l2.grid(row=3, column=1)
        b2 = Button(l2, text='2', font=('Helvetica', '16'), command=lambda: self.click_button(2), bg='black',
                    fg='#823E30')
        b2.pack()

        l3 = Label(main_label, bg="black")
        l3.grid(row=3, column=2)
        b3 = Button(l3, text='3', font=('Helvetica', '16'), command=lambda: self.click_button(3), bg='black',
                    fg='#823E30')
        b3.pack()

        l0 = Label(main_label, bg="black")
        l0.grid(row=4, column=0)
        b0 = Button(l0, text='0', font=('Helvetica', '16'), command=lambda: self.click_button(0), bg='black',
                    fg='#823E30')
        b0.pack()

        lpoint = Label(main_label, bg="black")
        lpoint.grid(row=4, column=1)
        bpoint = Button(lpoint, text='.', font=('Helvetica', '16'), command=lambda: self.click_button('.'), bg='black',
                        fg='#823E30')
        bpoint.pack()

        ldif = Label(main_label, bg="black")
        ldif.grid(row=4, column=2)
        bdif = Button(ldif, text='-', font=('Helvetica', '16'), command=lambda: self.click_button('-'), bg='black',
                      fg='#823E30')
        bdif.pack()

        ladd = Label(main_label, bg="black")
        ladd.grid(row=2, column=3)
        badd = Button(ladd, text='+', font=('Helvetica', '16'), command=lambda: self.click_button('+'), bg='black',
                      fg='#823E30')
        badd.pack()

        ldiv = Label(main_label, bg="black")
        ldiv.grid(row=3, column=3)
        bdiv = Button(ldiv, text='/', font=('Helvetica', '16'), command=lambda: self.click_button('/'), bg='black',
                      fg='#823E30')
        bdiv.pack()

        lclear = Label(main_label, bg="black")
        lclear.grid(row=1, column=3)
        bclear = Button(lclear, text='C', font=('Helvetica', '16'), command=lambda: self.clear_btn(), bg='black',
                        fg='#823E30')
        bclear.pack()

        leq = Label(main_label, bg="black")
        leq.grid(row=4, column=3)
        beq = Button(leq, text='=', font=('Helvetica', '16'), command=lambda: self.equal_btn(), bg='black',
                     fg='#823E30')
        beq.pack()


my_calc = Calculator(root)
root.mainloop()
