#!/usr/bin/env python3

import tkinter as tk

#create new default label for all circular buttons, so it's easier to write in the main/calc. This label also creates the circular buttons themselves.
class RoundLabel(tk.Canvas):

    def __init__(self, parent, fg='#FFFFFF', bg='#43326E', outline='#ffffff', fillcircle='#ffffff', width=160, height=160, text='X'):
        tk.Canvas.__init__(self,parent, bg=bg, width=width, height=height)
        tmp1 = 0.05 * width
        tmp2 = 0.95 * width
        tmp3 = 0.05 * height
        tmp4 = 0.95 * height
        self.create_oval(tmp1, tmp4, tmp2, tmp3, outline=outline,fill=fillcircle,width=3)
        self.create_text(width//2,height//2,text=text,fill=fg,font=('Courier 48'))