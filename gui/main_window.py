#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Alexander Ledenev"
__copyright__ = "Copyleft (>)"
__license__ = "Public Domain"
__version__ = "0.0.01"

from tkinter import *

def mock():
    pass

def main_frames(window):
    buttons_frame = Frame(window)
    buttons_frame.pack(side=LEFT, expand=NO, fill=BOTH)

    content_frame = Frame(window)
    content_frame.pack(side=LEFT, expand=YES, fill=BOTH)

    Button(buttons_frame, text='Start', command=mock).pack(side=TOP, fill=X)
    Button(buttons_frame, text='Content', command=mock).pack(side=TOP, fill=X)
    Button(buttons_frame, text='Diff', command=mock).pack(side=TOP, fill=X)

    Label(content_frame, text='Directory:').pack(side=TOP)
    Label(content_frame, text='  folder content').pack(side=TOP)


def main_win():
    main_window = Tk()
    main_window.title('Avoska')
    main_frames(main_window)
    main_window.mainloop()

if __name__ == '__main__':
    main_win()
