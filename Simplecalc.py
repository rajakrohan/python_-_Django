from tkinter import *

master = Tk()
display = Entry(master, width=15, justify='center', bd=0, bg='yellow')

master.title("SimpleC")


class Calculator:
#constructor
    def __init__(self):
        self.var1 = ""
        self.var2 = ""
        self.result = 0
        self.current = 0
        self.operator = 0

    def set_op(self, op):
        self.operator = op
        display.delete(0, END)
        if self.current is 0:
            self.current = 1
        else:
            self.equate()
            self.var2 = ""

    def numb_butt(self, index):
        if self.current is 0:
            self.var1 = str(self.var1) + str(index)
            display.delete(first=0, last=END)
            display.insert(0, string=self.var1)
        else:
            self.var2 = str(self.var2) + str(index)
            display.delete(first=0, last=END)
            display.insert(0, self.var2)

    def equate(self):
        if self.operator is 0:
            self.result = float(self.var1) + float(self.var2)
        elif self.operator is 1:
            self.result = float(self.var1) - float(self.var2)
        elif self.operator is 2:
            self.result = float(self.var1) * float(self.var2)
        elif self.operator is 3:
            self.result = float(self.var1) / float(self.var2)
        display.delete(first=0, last=END)
        display.insert(0, self.result)
        self.var1 = self.result

    def clear(self):
        self.__init__()
        display.delete(0, END)


calc = Calculator()

b0 = Button(master, text="0", command=lambda: calc.numb_butt(0))
b1 = Button(master, text="1", command=lambda: calc.numb_butt(1))
b2 = Button(master, text="2", command=lambda: calc.numb_butt(2))
b3 = Button(master, text="3", command=lambda: calc.numb_butt(3))
b4 = Button(master, text="4", command=lambda: calc.numb_butt(4))
b5 = Button(master, text="5", command=lambda: calc.numb_butt(5))
b6 = Button(master, text="6", command=lambda: calc.numb_butt(6))
b7 = Button(master, text="7", command=lambda: calc.numb_butt(7))
b8 = Button(master, text="8", command=lambda: calc.numb_butt(8))
b9 = Button(master, text="9", command=lambda: calc.numb_butt(9))
b_dot = Button(master, text=".", command=lambda: calc.numb_butt("."))

plus = Button(master, text="+", command=lambda: calc.set_op(0))
minus = Button(master, text="-", command=lambda: calc.set_op(1))
times = Button(master, text="*", command=lambda: calc.set_op(2))
divide = Button(master, text="/", command=lambda: calc.set_op(3))

equals = Button(master, text="=", command=calc.equate)
clear = Button(master, text="c", command=calc.clear)

# Position#

display.place(x=0, y=2)
b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)
b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)
b0.grid(row=4, column=0)
b_dot.grid(row=4, column=1)
clear.grid(row=4, column=2)
plus.grid(row=0, column=3)
minus.grid(row=1, column=3)
times.grid(row=2, column=3)
divide.grid(row=3, column=3)
equals.grid(row=4, column=3)

master.mainloop()
