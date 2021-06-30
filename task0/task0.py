from tkinter import *
import math
a=[]
b=[]
class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 21, "bold"), bg="#000", foreground="#FFF")
        self.lbl.place(x=11, y=50)

        btns = [
            "C", "DEL", "*", "=",
            "1", "2", "3", "/",
            "4", "5", "6", "+",
            "7", "8", "9", "-",
            "(", "0", ")", "X^2",
            "cos","sin","tan","ctg",
            "log","ln", "%", "bin",
            "^"
        ]

        x = 10
        y = 140
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            Button(text=bt, bg="#FFF",font=("Times New Roman", 15),command=com).place(x=x, y=y,width=115,height=79)
            x += 117
            if x > 400:
                x = 10
                y += 81

    def logicalc(self, operation):

        if operation == "C":
            self.formula = ""
        elif operation == "DEL":
            self.formula = self.formula[0:-1]
        elif operation == "X^2":
            self.formula = str((eval(self.formula))**2)
        elif operation == "cos":
            self.formula = str(math.cos(eval(self.formula)))
        elif operation == "sin":
            self.formula = str(math.sin(eval(self.formula)))
        elif operation == "tan":
            self.formula = str(math.tan(eval(self.formula)))
        elif operation == "ln":
            self.formula = str(math.log1p(eval(self.formula)))
        elif operation == "log":
            self.formula = str(math.log(eval(self.formula)))
        elif operation == "ctg":
            self.formula = str(math.cos (eval(self.formula)) / math.sin (eval(self.formula)))
        elif operation == "bin":
            self.formula = str(bin(eval(self.formula)))
        elif operation == "=":
            if '%' in self.formula:
                print(self.formula)
                a = float(self.formula.split('%')[0])
                print(a)
                b = float(self.formula.rsplit('%', 1)[-1])
                print(b)
                print(a, b)
                self.formula = str((a / 100) * b)
            if '^' in self.formula:
                print(self.formula)
                a = float(self.formula.split('^')[0])
                print(a)
                b = float(self.formula.rsplit('^', 1)[-1])
                print(b)
                print(a, b)
                self.formula = str(math.pow(a, b))
            else:
             self.formula = str(eval(self.formula))
             math.pow(X, Y)
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)


if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#000"
    root.geometry("480x800")
    root.title("Калькулятор")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()