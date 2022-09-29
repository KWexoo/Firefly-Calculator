#!/usr/bin/env python3

import tkinter as tk

class RoundLabel(tk.Canvas):

    def __init__(self, parent, fg='#FFFFFF', bg='#43326E', outline='#ffffff', fillcircle='#ffffff', width=160, height=160, text='X'):
        tk.Canvas.__init__(self,parent, bd=0, bg=bg, width=width, height=height, highlightthickness=0)
        tmp1 = 0.05 * width
        tmp2 = 0.95 * width
        tmp3 = 0.05 * height
        tmp4 = 0.95 * height
        self.create_oval(tmp1, tmp4, tmp2, tmp3, outline=outline,fill=fillcircle,width=3)
        self.create_text(width//2,height//2,text=text,fill=fg,font=('Courier 48'))

class WideLabel(tk.Canvas):

    def __init__(self, parent, fg='#ffff00', bg='#ff0000', outline='#00ff00', fillcircle='#0000ff', width=320, height=160, text='X'):
        tk.Canvas.__init__(self,parent, border=0, bd=0, bg=bg, width=width, height=height, highlightthickness=0)
        tmp1 = 0.05 * width//2
        tmp2 = 0.95 * width//2
        tmp3 = 0.05 * height
        tmp4 = 0.95 * height
        tmp5 = width // 2 + 0.05 * width//2
        tmp6 = width // 2 + 0.95 * width//2
        tmp7 = 0.05 * height
        tmp8 = 0.95 * height
        self.create_oval(tmp1, tmp4, tmp2, tmp3, outline=outline, fill=fillcircle, width=3)
        self.create_oval(tmp5, tmp8, tmp6, tmp7, outline=outline, fill=fillcircle, width=3)
        self.create_rectangle(width // 4, tmp3, 3 * width // 4, tmp8, outline=outline, fill=fillcircle, width=3)
        self.create_text(width//2, height//2, text=text, fill=fg, font=('Courier 48'))

class TallLabel(tk.Canvas):

    def __init__(self, parent, fg='#ffff00', bg='#ff0000', outline='#00ff00', fillcircle='#0000ff', width=160, height=320, text='X'):
        tk.Canvas.__init__(self,parent, border=0, bd=0, bg=bg, width=width, height=height, highlightthickness=0)
        tmp1 = 0.05 * width
        tmp2 = 0.95 * width
        tmp3 = 0.05 * height // 2
        tmp4 = 0.95 * height // 2
        self.create_oval(tmp1, tmp4, tmp2, tmp3, outline=outline, fill=fillcircle, width=3)
        tmp5 = 0.05 * width
        tmp6 = 0.95 * width
        tmp7 = height //2 + 0.05 * height // 2
        tmp8 = height //2 + 0.95 * height // 2
        self.create_oval(tmp5, tmp8, tmp6, tmp7, outline=outline, fill=fillcircle, width=3)
        self.create_rectangle(tmp1, height // 4, tmp2, 3 * height // 4, outline=outline, fill=fillcircle, width=3)
        self.create_text(width//2, height//2, text=text, fill=fg, font=('Courier 48'))

class Bar(tk.Canvas):

    def __init__(self, parent, fg='#ffff00', bg='#ff0000', width=640):

        tk.Canvas.__init__(self,parent, border=0, bd=0, bg=bg, width=640, height=40, highlightthickness=0)
        leftend = (640 - width) // 2
        rightend = (640 + width) // 2
        self.create_line(leftend,20,rightend,20,fill=fg,width=4)