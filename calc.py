#!/usr/bin/env python3

import tkinter as tk

cellwidth = 2
cellheight = 2

CLR = 0
DIV = 1
MUL = 2
SUB = 3
ADD = 4
NOP = 5

cmdvalue = [MUL, SUB, ADD]
cmdlist = ["*", "-", "+"]

class Calculator(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.reset()
        #self.display to create the display that the current number is written
        self.display = tk.Label(self, height=2, width=18,
                                      bg="#43326E",
                                      fg="yellow",
                                      text="",
                                      font = ("Courier", 32))
        self.display.grid(row=0, column=0, columnspan=4, rowspan=1, sticky='NEWS')

        digitframe = tk.Frame(self)
        digitframe.grid(row=1, column=0, rowspan=5, columnspan=4)

        for i in range(9):
            lab = tk.Label(digitframe, text = str(i+1),
                                       padx = 20,
                                       pady = 20,
                                       bg = '#c0c0c0',
                                       border = 4,
                                       width = cellwidth,
                                       relief = 'raised',
                                       font = ('Courier', 48))
            lab.value = i+1
            lab.bind('<ButtonPress-1>', self.digit)
            lab.bind('<ButtonRelease-1>', self.release)
            lab.grid(row=(i // 3) + 2, column = i % 3)

        lab = tk.Label(digitframe, text = '0',
                                   padx = 20,
                                   pady = 20,
                                   bg = '#c0c0c0',
                                   border = 4,
                                   width = cellwidth*2,
                                   relief = 'raised',
                                   font = ('Courier', 48))
        lab.value = 0
        lab.bind('<ButtonPress-1>', self.digit)
        lab.bind('<ButtonRelease-1>', self.release)
        lab.grid(row=5, column=0, columnspan=2, sticky = 'news')

        #commandframe = tk.Frame(self)
        #commandframe.grid(row=5, column=0, rowspan=2, columnspan=3)

        lab = tk.Label(digitframe, text = "AC",
                                    bg = 'lightblue',
                                    fg = 'black',
                                    padx = 20,
                                    pady = 20,
                                    width = cellwidth,
                                    border = 4,
                                    relief = 'raised',
                                    font = ('Courier', 48))
        lab.bind('<Button-1>', self.command)
        lab.value = CLR
        lab.grid(row = 1, column = 0)

        lab = tk.Label(digitframe, text = "/",
                                    bg = 'lightblue',
                                    fg = 'black',
                                    padx = 20,
                                    pady = 20,
                                    width = cellwidth,
                                    border = 4,
                                    relief = 'raised',
                                    font = ('Courier', 48))
        lab.bind('<Button-1>', self.command)
        lab.value = DIV
        lab.grid(row = 1, column = 2)

        for i in range(3):
            lab = tk.Label(digitframe, text=cmdlist[i],
                                        bg = 'lightblue',
                                        fg = 'black',
                                        padx = 20,
                                        pady = 20,
                                        width = cellwidth,
                                        border = 4,
                                        relief = 'raised',
                                        font = ('Courier', 48))
            lab.bind('<Button-1>', self.command)
            lab.value = cmdvalue[i]
            lab.grid(row = i+1, column = 3)

        lab = tk.Label(digitframe, text = "=",
                                    bg = 'lightblue',
                                    fg = 'black',
                                    padx = 20,
                                    pady = 20,
                                    width = cellwidth,
                                    border = 4,
                                    relief = 'raised',
                                    font = ('Courier', 48))
        lab.bind('<Button-1>', self.command)
        lab.value = NOP
        lab.grid(row = 4, column = 3, rowspan=2, sticky='news')
    
    def doOperation(self, cmd):
        if self.pending == ADD:
            self.total += self.current
        elif self.pending == SUB:
            self.total -= self.current
        elif self.pending == MUL:
            self.total *= self.current
        elif self.pending == DIV:
            self.total //= self.current
        elif self.pending == NOP:
            self.total = self.current
        self.pending = cmd

    def reset(self):
        self.total = self.current = 0
        self.pending = NOP

    #digit is run when a digit button is pressed
    def digit(self, event):
        self.current = 10*self.current + event.widget.value
        self.display.config(text=f'{self.current:12d}')
        event.widget.config(bg='#808080')

    def release(self, event):
        event.widget.config(bg='#c0c0c0')
    
    def command(self, event):
        cmd = event.widget.value
        if cmd == CLR:
            self.reset()
            self.display.config(text=f'{self.current:12d}')
        else:
            self.doOperation(cmd)
            self.current = 0
            self.display.config(text=f'{self.total:12d}')

if __name__ == "__main__":
    calc = Calculator()
    calc.mainloop()