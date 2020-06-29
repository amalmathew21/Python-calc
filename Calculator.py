from tkinter import *

root = Tk()
content = ""
first = ""


class Calculator:
    def hist(self):
        self.f = open("history_calc.txt", "r")
        self.temp = Tk()
        self.temp.title("history")
        self.temp.geometry("300x300+300+100")
        self.t = Text(self.temp, height=200, width=100)
        self.t.pack()
        self.t.insert(END, self.f.read())
        menubar = Menu(self.temp)
        menu_list = Menu(menubar, tearoff=0)
        menu_list.add_command(label='history clear', command=self.hist_clear)
        menu_list.add_command(label="Exit", command=self.temp.destroy)
        menubar.add_cascade(label="Options", menu=menu_list)
        self.temp.config(menu=menubar)

    def hist_clear(self):
        self.fc = open("history_calc.txt", "r+")
        self.fc.truncate(0)
        self.fc.close()
        self.temp.destroy()
        self.hist()

    def click_button(self, val):
        global content
        content += str(val)
        self.result.set(content)

    def equal_btn(self):
        global content
        global first
        data = first + content + "="
        final = str(first) + str(content)
        final_data = eval(final)
        self.result.set(final_data)
        content = ""
        first = ""
        data += str(final_data)
        f = open("history_calc.txt", "a")
        f.write("\n" + data)
        f.close()

    def clear_btn(self):
        global content
        content = ""
        self.result.set(content)

    def opr(self, opr):
        global first
        global content
        first = content
        first += opr
        content = ""

    def ce(self):
        global content
        content = ""
        self.result.set(content)

    def __init__(self, master):
        # title and size
        master.title("Calculator")
        master.geometry("330x240+450+100")
        # menu bar
        menubar = Menu(master)
        menu_list = Menu(menubar, tearoff=0)
        menu_list.add_command(label="history", command=self.hist)
        menu_list.add_command(label="Exit", command=master.quit)
        menubar.add_cascade(label="Options", menu=menu_list)
        master.config(menu=menubar)
        # display field
        self.result = StringVar()
        top_frame = Frame(master, width=350, height=50, bd=3, relief="raised")
        top_frame.pack(side=TOP)
        input_field = Entry(top_frame, textvariable=self.result, width=39, justify="right", bd=3)
        input_field.grid(row=0, column=0)
        # label
        main_label = Label(master, width=30, height=10, bd=5, bg="#2b2727", relief="raised", )
        main_label.pack(side=LEFT, fill=BOTH, expand=True)
        l7 = Label(main_label, bg="black")
        l7.grid(row=1, column=0, padx=5, pady=5)
        b7 = Button(l7, text='7', font=('Helvetica', '16'), command=lambda: self.click_button(7), bg='black',
                    fg='#823E30', width=2)
        b7.pack()

        l8 = Label(main_label, bg="black")
        l8.grid(row=1, column=1, padx=5, pady=5)
        b8 = Button(l8, text='8', font=('Helvetica', '16'), command=lambda: self.click_button(8), bg='black',
                    fg='#823E30', width=2)
        b8.pack()

        l9 = Label(main_label, bg="black")
        l9.grid(row=1, column=2, padx=5, pady=5)
        b9 = Button(l9, text='9', font=('Helvetica', '16'), command=lambda: self.click_button(9), bg='black',
                    fg='#823E30', width=2)
        b9.pack()

        l4 = Label(main_label, bg="black")
        l4.grid(row=2, column=0, padx=5, pady=5)
        b4 = Button(l4, text='4', font=('Helvetica', '16'), command=lambda: self.click_button(4), bg='black',
                    fg='#823E30', width=2)
        b4.pack()

        l5 = Label(main_label, bg="black")
        l5.grid(row=2, column=1, padx=5, pady=5)
        b5 = Button(l5, text='5', font=('Helvetica', '16'), command=lambda: self.click_button(5), bg='black',
                    fg='#823E30', width=2)
        b5.pack()

        l6 = Label(main_label, bg="black")
        l6.grid(row=2, column=2, padx=5, pady=5)
        b6 = Button(l6, text='6', font=('Helvetica', '16'), command=lambda: self.click_button(6), bg='black',
                    fg='#823E30', width=2)
        b6.pack()

        l1 = Label(main_label, bg="black")
        l1.grid(row=3, column=0, padx=5, pady=5)
        b1 = Button(l1, text='1', font=('Helvetica', '16'), command=lambda: self.click_button(1), bg='black',
                    fg='#823E30', width=2)
        b1.pack()

        l2 = Label(main_label, bg="black")
        l2.grid(row=3, column=1, padx=5, pady=5)
        b2 = Button(l2, text='2', font=('Helvetica', '16'), command=lambda: self.click_button(2), bg='black',
                    fg='#823E30', width=2)
        b2.pack()

        l3 = Label(main_label, bg="black")
        l3.grid(row=3, column=2, padx=5, pady=5)
        b3 = Button(l3, text='3', font=('Helvetica', '16'), command=lambda: self.click_button(3), bg='black',
                    fg='#823E30', width=2)
        b3.pack()

        l0 = Label(main_label, bg="black")
        l0.grid(row=4, column=0, padx=5, pady=5)
        b0 = Button(l0, text='0', font=('Helvetica', '16'), command=lambda: self.click_button(0), bg='black',
                    fg='#823E30', width=2)
        b0.pack()

        lpoint = Label(main_label, bg="black")
        lpoint.grid(row=4, column=1, padx=5, pady=5)
        bpoint = Button(lpoint, text='.', font=('Helvetica', '16'), command=lambda: self.click_button('.'), bg='black',
                        fg='#823E30', width=2)
        bpoint.pack()

        ldif = Label(main_label, bg="black")
        ldif.grid(row=4, column=3, padx=5, pady=5)
        bdif = Button(ldif, text='-', font=('Helvetica', '16'), command=lambda: self.opr('-'), bg='#003366',
                      fg='#823E30', width=2)
        bdif.pack()

        ladd = Label(main_label, bg="black")
        ladd.grid(row=2, column=3, padx=5, pady=5)
        badd = Button(ladd, text='+', font=('Helvetica', '16'), command=lambda: self.opr('+'), bg='#003366',
                      fg='#823E30', width=2)
        badd.pack()

        ldiv = Label(main_label, bg="black")
        ldiv.grid(row=3, column=3, padx=5, pady=5)
        bdiv = Button(ldiv, text='/', font=('Helvetica', '16'), command=lambda: self.opr('/'), bg='#003366',
                      fg='#823E30', width=2)
        bdiv.pack()

        lclear = Label(main_label, bg="black")
        lclear.grid(row=1, column=4, padx=5, pady=5)
        bclear = Button(lclear, text='C', font=('Helvetica', '16'), command=lambda: self.clear_btn(), bg='RED',
                        fg='#823E30', width=2)
        bclear.pack()

        leq = Label(main_label, bg="black")
        leq.grid(row=4, column=2, padx=5, pady=5)
        beq = Button(leq, text='=', font=('Helvetica', '16'), command=lambda: self.equal_btn(), bg='#3d0a19',
                     fg='#823E30', width=2)
        beq.pack()
        lmul = Label(main_label, bg="black")
        lmul.grid(row=1, column=3, padx=5, pady=5)
        bmul = Button(lmul, text='x', font=('Helvetica', '16'), command=lambda: self.opr('*'), bg='#003366',
                      fg='#823E30', width=2)
        bmul.pack()

        lce = Label(main_label, bg="black")
        lce.grid(row=2, column=4, padx=5, pady=5)
        bce = Button(lce, text='CE', font=('Helvetica', '16'), command=lambda: self.ce(), bg='#003366',
                     fg='#823E30', width=2)
        bce.pack()

        l_left_Bracket = Label(main_label, bg="black")
        l_left_Bracket.grid(row=3, column=4, padx=5, pady=5)
        b_left_bracket = Button(l_left_Bracket, text='(', font=('Helvetica', '16'),
                                command=lambda: self.click_button('('), bg='#003366',
                                fg='#823E30', width=2)
        b_left_bracket.pack()

        l_right_Bracket = Label(main_label, bg="black")
        l_right_Bracket.grid(row=4, column=4, padx=5, pady=5)
        b_right_bracket = Button(l_right_Bracket, text=')', font=('Helvetica', '16'),
                                 command=lambda: self.click_button(')'), bg='#003366',
                                 fg='#823E30', width=2)
        b_right_bracket.pack()


my_calc = Calculator(root)
root.mainloop()
