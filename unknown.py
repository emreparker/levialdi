#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.21
#  in conjunction with Tcl version 8.6
#    Mar 05, 2019 03:44:27 AM +03  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import unknown_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    unknown_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    unknown_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Blacksword} -size 9"

        top.geometry("979x624+254+40")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.LevialdiCanvas = tk.Canvas(top)
        self.LevialdiCanvas.place(relx=0.01, rely=0.112, relheight=0.838
                , relwidth=0.32)
        self.LevialdiCanvas.configure(background="#FFECB3")
        self.LevialdiCanvas.configure(borderwidth="20")
        self.LevialdiCanvas.configure(highlightbackground="#d9d9d9")
        self.LevialdiCanvas.configure(highlightcolor="black")
        self.LevialdiCanvas.configure(insertbackground="black")
        self.LevialdiCanvas.configure(relief='ridge')
        self.LevialdiCanvas.configure(selectbackground="#c4c4c4")
        self.LevialdiCanvas.configure(selectforeground="black")
        self.LevialdiCanvas.configure(width=313)

        self.TSF = tk.Button(top)
        self.TSF.place(relx=0.398, rely=0.16, height=24, width=207)
        self.TSF.configure(activebackground="#ececec")
        self.TSF.configure(activeforeground="#000000")
        self.TSF.configure(background="#d9d9d9")
        self.TSF.configure(disabledforeground="#a3a3a3")
        self.TSF.configure(foreground="#000000")
        self.TSF.configure(highlightbackground="#d9d9d9")
        self.TSF.configure(highlightcolor="black")
        self.TSF.configure(pady="0")
        self.TSF.configure(text='''TSF''')

        self.LEV = tk.Button(top)
        self.LEV.place(relx=0.398, rely=0.112, height=24, width=207)
        self.LEV.configure(activebackground="#ececec")
        self.LEV.configure(activeforeground="#000000")
        self.LEV.configure(background="#d9d9d9")
        self.LEV.configure(disabledforeground="#a3a3a3")
        self.LEV.configure(foreground="#000000")
        self.LEV.configure(highlightbackground="#d9d9d9")
        self.LEV.configure(highlightcolor="black")
        self.LEV.configure(pady="0")
        self.LEV.configure(text='''Levialdi''')

        self.Binary = tk.Text(top)
        self.Binary.place(relx=0.358, rely=0.208, relheight=0.744, relwidth=0.3)
        self.Binary.configure(background="#FFECB3")
        self.Binary.configure(borderwidth="2")
        self.Binary.configure(font="TkTextFont")
        self.Binary.configure(foreground="black")
        self.Binary.configure(highlightbackground="#d9d9d9")
        self.Binary.configure(highlightcolor="black")
        self.Binary.configure(insertbackground="black")
        self.Binary.configure(selectbackground="#c4c4c4")
        self.Binary.configure(selectforeground="black")
        self.Binary.configure(width=294)
        self.Binary.configure(wrap='word')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg='#d82b87',fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.TSFCanvas = tk.Canvas(top)
        self.TSFCanvas.place(relx=0.684, rely=0.112, relheight=0.838
                , relwidth=0.299)
        self.TSFCanvas.configure(background="#FFECB3")
        self.TSFCanvas.configure(borderwidth="20")
        self.TSFCanvas.configure(highlightbackground="#d9d9d9")
        self.TSFCanvas.configure(highlightcolor="black")
        self.TSFCanvas.configure(insertbackground="black")
        self.TSFCanvas.configure(relief='ridge')
        self.TSFCanvas.configure(selectbackground="#c4c4c4")
        self.TSFCanvas.configure(selectforeground="black")
        self.TSFCanvas.configure(width=293)

        self.Reset = tk.Button(top)
        self.Reset.place(relx=0.123, rely=0.032, height=34, width=77)
        self.Reset.configure(activebackground="#ececec")
        self.Reset.configure(activeforeground="#000000")
        self.Reset.configure(background="#d9d9d9")
        self.Reset.configure(disabledforeground="#a3a3a3")
        self.Reset.configure(foreground="#000000")
        self.Reset.configure(highlightbackground="#d9d9d9")
        self.Reset.configure(highlightcolor="black")
        self.Reset.configure(pady="0")
        self.Reset.configure(text='''Reset''')
root
        self.Open = tk.Button(top)
        self.Open.place(relx=0.02, rely=0.032, height=34, width=77)
        self.Open.configure(activebackground="#ececec")
        self.Open.configure(activeforeground="#000000")
        self.Open.configure(background="#d9d9d9")
        self.Open.configure(disabledforeground="#a3a3a3")
        self.Open.configure(font=font9)
        self.Open.configure(foreground="#000000")
        self.Open.configure(highlightbackground="#d9d9d9")
        self.Open.configure(highlightcolor="black")
        self.Open.configure(pady="0")
        self.Open.configure(text='''Open''')

        self.itercounter = tk.Label(top)
        self.itercounter.place(relx=0.46, rely=0.048, height=31, width=54)
        self.itercounter.configure(activebackground="#f9f9f9")
        self.itercounter.configure(activeforeground="black")
        self.itercounter.configure(background="#d9d9d9")
        self.itercounter.configure(disabledforeground="#a3a3a3")
        self.itercounter.configure(foreground="#000000")
        self.itercounter.configure(highlightbackground="#d9d9d9")
        self.itercounter.configure(highlightcolor="black")
        self.itercounter.configure(text='''Label''')

        self.ncccounter = tk.Label(top)
        self.ncccounter.place(relx=0.572, rely=0.048, height=31, width=54)
        self.ncccounter.configure(activebackground="#f9f9f9")
        self.ncccounter.configure(activeforeground="black")
        self.ncccounter.configure(background="#d9d9d9")
        self.ncccounter.configure(disabledforeground="#a3a3a3")
        self.ncccounter.configure(foreground="#000000")
        self.ncccounter.configure(highlightbackground="#d9d9d9")
        self.ncccounter.configure(highlightcolor="black")
        self.ncccounter.configure(text='''Label''')

        self.ITER = tk.Message(top)
        self.ITER.place(relx=0.398, rely=0.048, relheight=0.053, relwidth=0.067)
        self.ITER.configure(background="#d9d9d9")
        self.ITER.configure(foreground="#000000")
        self.ITER.configure(highlightbackground="#d9d9d9")
        self.ITER.configure(highlightcolor="black")
        self.ITER.configure(text='''Iterations:''')
        self.ITER.configure(width=66)

        self.NCC = tk.Message(top)
        self.NCC.place(relx=0.531, rely=0.048, relheight=0.053, relwidth=0.043)
        self.NCC.configure(background="#d9d9d9")
        self.NCC.configure(foreground="#000000")
        self.NCC.configure(highlightbackground="#d9d9d9")
        self.NCC.configure(highlightcolor="black")
        self.NCC.configure(text='''NCC:''')
        self.NCC.configure(width=42)

        root.Creator = tk.Button(root)
        root.Creator.place(relx=0.225, rely=0.032, height=34, width=97)
        root.Creator.configure(activebackground="#ececec")
        root.Creator.configure(activeforeground="#000000")
        root.Creator.configure(background="#d9d9d9")
        root.Creator.configure(disabledforeground="#a3a3a3")
        root.Creator.configure(foreground="#000000")
        root.Creator.configure(highlightbackground="#d9d9d9")
        root.Creator.configure(highlightcolor="black")
        root.Creator.configure(pady="0")
        root.Creator.configure(text='''Create a Shape''')
        root.Creator.configure(width=97)

if __name__ == '__main__':
    vp_start_gui()





