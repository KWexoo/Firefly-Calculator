#!/usr/bin/env python3

import tkinter as tk

SIZE = 80

class RoundLabel(tk.Canvas):

    def __init__(self, parent, fg='#FFFFFF', bg='#43326E', outline='#ffffff', fillcircle='#ffffff', width=SIZE, height=SIZE, text='X'):
        tk.Canvas.__init__(self,parent, bd=0, bg=bg, width=width, height=height, highlightthickness=0)
        tmp1 = 0.05 * width
        tmp2 = 0.95 * width
        tmp3 = 0.05 * height
        tmp4 = 0.95 * height
        self.light = self.create_oval(tmp1, tmp4, tmp2, tmp3, outline=outline,fill=fillcircle,width=3)
        self.create_text(width//2,height//2,text=text,fill=fg,font=('Courier 24'))

    def flash(self, color):
        self.itemconfig(self.light, fill=color)

class WideLabel(tk.Canvas):

    def __init__(self, parent, fg='#ffff00', bg='#ff0000', outline='#00ff00', fillcircle='#0000ff', width=2*SIZE, height=SIZE, text='X'):
        tk.Canvas.__init__(self,parent, border=0, bd=0, bg=bg, width=width, height=height, highlightthickness=0)
        tmp1 = 0.05 * width//2
        tmp2 = 0.95 * width//2
        tmp3 = 0.05 * height
        tmp4 = 0.95 * height
        tmp5 = width // 2 + 0.05 * width//2
        tmp6 = width // 2 + 0.95 * width//2
        tmp7 = 0.05 * height
        tmp8 = 0.95 * height
        self.light1 = self.create_oval(tmp1, tmp4, tmp2, tmp3, outline=outline, fill=fillcircle, width=3)
        self.light2 = self.create_oval(tmp5, tmp8, tmp6, tmp7, outline=outline, fill=fillcircle, width=3)
        self.light3 = self.create_rectangle(width // 4, tmp3, 3 * width // 4, tmp8, outline=outline, fill=fillcircle, width=3)
        self.create_text(width//2, height//2, text=text, fill=fg, font=('Courier 24'))

    def flash(self, color):
        self.itemconfig(self.light1, fill=color)
        self.itemconfig(self.light2, fill=color)
        self.itemconfig(self.light3, fill=color)

class TallLabel(tk.Canvas):

    def __init__(self, parent, fg='#ffff00', bg='#ff0000', outline='#00ff00', fillcircle='#0000ff', width=SIZE, height=2*SIZE, text='X'):
        tk.Canvas.__init__(self,parent, border=0, bd=0, bg=bg, width=width, height=height, highlightthickness=0)
        tmp1 = 0.05 * width
        tmp2 = 0.95 * width
        tmp3 = 0.05 * height // 2
        tmp4 = 0.95 * height // 2
        self.light1 = self.create_oval(tmp1, tmp4, tmp2, tmp3, outline=outline, fill=fillcircle, width=3)
        tmp5 = 0.05 * width
        tmp6 = 0.95 * width
        tmp7 = height //2 + 0.05 * height // 2
        tmp8 = height //2 + 0.95 * height // 2
        self.light2 = self.create_oval(tmp5, tmp8, tmp6, tmp7, outline=outline, fill=fillcircle, width=3)
        self.light3 = self.create_rectangle(tmp1, height // 4, tmp2, 3 * height // 4, outline=outline, fill=fillcircle, width=3)
        self.create_text(width//2, height//2, text=text, fill=fg, font=('Courier 24'))

    def flash(self, color):
        self.itemconfig(self.light1, fill=color)
        self.itemconfig(self.light2, fill=color)
        self.itemconfig(self.light3, fill=color)

class Bar(tk.Canvas):

    def __init__(self, parent, fg='#ffff00', bg='#ff0000', width=4*SIZE):

        tk.Canvas.__init__(self,parent, border=0, bd=0, bg=bg, width=4*SIZE, height=SIZE // 2, highlightthickness=0)
        leftend = (4*SIZE - width) // 2
        rightend = (4*SIZE + width) // 2
        self.create_line(leftend, SIZE // 5,rightend, SIZE // 5,fill=fg, width=4)