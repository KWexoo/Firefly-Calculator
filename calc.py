#!/usr/bin/env python3

import tkinter as tk
from decimal import *
from Components import RoundLabel, WideLabel, TallLabel, Bar, SIZE

cellwidth = 2
cellheight = 2

CLR = 0
DIV = 1
MUL = 2
SUB = 3
ADD = 4
NOP = 5
DEC = 6

cmdvalue = [MUL, SUB, ADD]
cmdlist = ["x", "-", "+"]

PURPLE    = "#43326E"
YELLOW    = "#FAD652"
WHITE     = "#F4F7F5"
TMPPURPLE = "#53427E"
TMPYELLOW = "#FAE662"

BUTTONROW = 2

def format(x):
    s = f'{x:.10f}'
    n = len(s)-1
    while s[n] == '0':
        n -= 1
    if s[n] == '.':
        n -= 1
    s = s[:n+1]
    return s

class Calculator(tk.Tk):
    isdecimal = False
    decinum = 0

    def __init__(self):
        tk.Tk.__init__(self)

        #Self.history is a list of previous equations done by the calculator. It does not do anything or is used for anything currently.
        self.history = []
        self.app = tk.Frame(self)
        self.app.pack(padx=SIZE//3, pady=SIZE//3)

        self.configure(bg=PURPLE)
        self.reset()

# self.display to create the display that the current number is written.

        self.display = tk.Label(self.app, height=3, width=8,
                                      bg=PURPLE,
                                      fg=WHITE,
                                      border=2,
                                      text=format(0),
                                      anchor="se",
                                      font = ("Courier", 32))
        self.display.grid(row=0, column=0, columnspan=4, rowspan=1, sticky="NEWS")

        bar = Bar(self.app,bg=PURPLE,fg=WHITE,width=4*SIZE)
        bar.grid(row=1, column=0, rowspan=1, columnspan=4, padx=0, pady=0)

# The buttonframe holds the numbers and commands that can be issued to the calculator.
# The labs each create one of the various buttons, using the grid to determine location.

        buttonframe = tk.Frame(self.app,bg=PURPLE,bd=0,border=0,padx=0,pady=0)
        buttonframe.grid(row=BUTTONROW, column=0, rowspan=5, columnspan=4, padx=0, pady=0)

        bar = Bar(self.app,bg=PURPLE,fg='#ffffff',width=SIZE)
        bar.grid(row=7, column=0, rowspan=1, columnspan=4, padx=0, pady=0)

        for i in range(9):
            lab = RoundLabel(buttonframe, text = str(i+1),
                                       bg = PURPLE, fg = WHITE, outline = WHITE, fillcircle = PURPLE)
            lab.value = i+1
            lab.bind("<ButtonPress-1>", self.digit)
            lab.bind("<ButtonRelease-1>", self.release)
            lab.grid(row=BUTTONROW + 2 - (i // 3), column = i % 3, sticky="news", padx = 0, pady = 0)

        lab = WideLabel(buttonframe, text = "0", bg = PURPLE, fg = WHITE, outline = WHITE, fillcircle = PURPLE)
        lab.value = 0
        lab.bind("<ButtonPress-1>", self.digit)
        lab.bind("<ButtonRelease-1>", self.release)
        lab.grid(row=5, column=0, columnspan=2, sticky = "news", padx = 0, pady = 0)

        lab = RoundLabel(buttonframe, text = ".", bg = PURPLE, fg = WHITE, outline = WHITE, fillcircle = PURPLE)
        lab.bind("<Button-1>", self.command)
        lab.bind("<ButtonRelease-1>", self.release)
        lab.value = DEC
        lab.grid(row=5, column=2, sticky = "news", padx = 0, pady = 0)

        lab = RoundLabel(buttonframe, text = "C", bg = PURPLE, fg = WHITE, outline = YELLOW, fillcircle = PURPLE)
        lab.bind("<Button-1>", self.command)
        lab.bind("<ButtonRelease-1>", self.release)
        lab.value = CLR
        lab.grid(row = 1, column = 0, sticky="news", padx = 0, pady = 0)

        lab = RoundLabel(buttonframe, text = "÷", bg = PURPLE, fg = PURPLE, outline = YELLOW, fillcircle = YELLOW)
        lab.bind("<Button-1>", self.command)
        lab.bind("<ButtonRelease-1>", self.release2)
        lab.value = DIV
        lab.grid(row = 1, column = 2, sticky="news", padx = 0, pady = 0)

        for i in range(3):
            lab = RoundLabel(buttonframe, text=cmdlist[i], bg = PURPLE, fg = PURPLE, outline = YELLOW, fillcircle = YELLOW)
            lab.bind("<Button-1>", self.command)
            lab.bind("<ButtonRelease-1>", self.release2)
            lab.value = cmdvalue[i]
            lab.grid(row = i+1, column = 3, sticky="news", padx = 0, pady = 0)

        lab = TallLabel(buttonframe, text = "=", bg = PURPLE, fg = PURPLE, outline = YELLOW, fillcircle = YELLOW)
        lab.bind("<Button-1>", self.command)
        lab.bind("<ButtonRelease-1>", self.release2)
        lab.value = NOP
        lab.grid(row = 4, column = 3, rowspan=2, sticky="news", padx = 0, pady = 0)

#doOperation creates the commands such as +, -, and x.

    def doOperation(self, cmd):
        if self.pending == ADD:
            self.total += self.current
        elif self.pending == SUB:
            self.total -= self.current
        elif self.pending == MUL:
            self.total *= self.current
        elif self.pending == DIV:
            self.total /= self.current
        elif self.pending == NOP:
            self.total = self.current
        self.pending = cmd

    def reset(self):
        self.total = self.current = 0
        self.isdecimal = False
        self.pending = NOP

    #digit is run when a digit button is pressed
    def digit(self, event):
        if len(format(self.current)) < 12:
            if self.isdecimal:
                self.decinum += 1
                self.current = self.current + event.widget.value*((0.1)**self.decinum)
                self.display.config(text=format(self.current))
            else:
                self.current = 10*self.current + event.widget.value
                self.display.config(text=format(self.current))
        event.widget.flash(TMPPURPLE)

    #The two release defs are run when a button is released to return the button color to its default state. 
    def release(self, event):
        event.widget.flash(PURPLE)

    #Command is run when a command button is pressed.
    def command(self, event):
        cmd = event.widget.value
        if cmd == CLR:
            self.reset()
            self.display.config(text=format(self.current))
        elif cmd == DEC:
            self.isdecimal = True
        else:
            self.doOperation(cmd)
            self.current = 0
            result = format(self.total)
            self.display.config(text=result)
            self.history.append(result)
            self.isdecimal = False
            self.decinum = 0
        event.widget.flash(TMPYELLOW)
    
    def release2(self, event):
        event.widget.flash(YELLOW)

if __name__ == "__main__":
    calc = Calculator()
    calc.mainloop()
