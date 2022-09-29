#!/usr/bin/env python3

# Todo:
# Create decimals.
# Create hamburger menu and figure out what to put on it.
# Enlarge display

import tkinter as tk
from Components import RoundLabel, WideLabel, TallLabel, Bar

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

PURPLE    = "#43326E"
YELLOW    = "#FAD652"
WHITE     = "#F4F7F5"
TMPPURPLE = "#53427E"

BUTTONROW = 2

class Calculator(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.app = tk.Frame(self)
        self.app.pack(padx=40, pady=40)

        self.configure(bg=PURPLE)
        self.reset()

# self.display to create the display that the current number is written.

        self.display = tk.Label(self.app, height=3, width=8,
                                      bg=PURPLE,
                                      fg=WHITE,
                                      border=2,
                                      text="",
                                      anchor="s",
                                      font = ("Courier", 64))
        self.display.grid(row=0, column=0, columnspan=4, rowspan=1, sticky="NEWS")

        bar = Bar(self.app,bg=PURPLE,fg=WHITE,width=640)
        bar.grid(row=1, column=0, rowspan=1, columnspan=4, padx=0, pady=0)

# The buttonframe holds the numbers and commands that can be issued to the calculator.
# The labs each create one of the various buttons, using the grid to determine location.

        buttonframe = tk.Frame(self.app,bg=PURPLE,bd=0,border=0,padx=0,pady=0)
        buttonframe.grid(row=BUTTONROW, column=0, rowspan=5, columnspan=4, padx=0, pady=0)

        bar = Bar(self.app,bg=PURPLE,fg='#ffffff',width=160)
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

        lab = RoundLabel(buttonframe, text = "C", bg = PURPLE, fg = WHITE, outline = YELLOW, fillcircle = PURPLE)
        lab.bind("<Button-1>", self.command)
        lab.value = CLR
        lab.grid(row = 1, column = 0, sticky="news", padx = 0, pady = 0)

        lab = RoundLabel(buttonframe, text = "/", bg = PURPLE, fg = PURPLE, outline = YELLOW, fillcircle = YELLOW)
        lab.bind("<Button-1>", self.command)
        lab.value = DIV
        lab.grid(row = 1, column = 2, sticky="news", padx = 0, pady = 0)

        for i in range(3):
            lab = RoundLabel(buttonframe, text=cmdlist[i], bg = PURPLE, fg = PURPLE, outline = YELLOW, fillcircle = YELLOW)
            lab.bind("<Button-1>", self.command)
            lab.value = cmdvalue[i]
            lab.grid(row = i+1, column = 3, sticky="news", padx = 0, pady = 0)

        lab = TallLabel(buttonframe, text = "=", bg = PURPLE, fg = PURPLE, outline = YELLOW, fillcircle = YELLOW)
        lab.bind("<Button-1>", self.command)
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
        self.display.config(text=f"{self.current:12d}")
        event.widget.config(bg=TMPPURPLE)

    def release(self, event):
        event.widget.config(bg=PURPLE)

    #Command is run when a command button is pressed.
    def command(self, event):
        cmd = event.widget.value
        if cmd == CLR:
            self.reset()
            self.display.config(text=f"{self.current:12d}")
        else:
            self.doOperation(cmd)
            self.current = 0
            self.display.config(text=f"{self.total:12d}")

if __name__ == "__main__":
    calc = Calculator()
    calc.mainloop()
