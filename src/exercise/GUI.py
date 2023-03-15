# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 17:33:39 2023

@author: He
"""

import tkinter

# root = tkinter.Tk() # Main window.

# c = tkinter.Canvas(root, width=200, height=200)
# c.pack() # Layout
# c.create_rectangle(0, 0, 200, 200, fill="blue")

# tkinter.mainloop() # Wait for interactions.

def run():
    pass

# Menu elements
root = tkinter.Tk()
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

tkinter.mainloop() # Wait for interactions.