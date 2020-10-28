# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 18:16:22 2020

@author: Grzechu
"""

from tkinter import *

root = Tk()

root.title("Notes")
root.geometry("300x300")

#create scroll bar
scrolly = Scrollbar(root)
scrolly.pack(side=RIGHT, fill=Y)
#create text box and fill the entire window with it
textBox = Text(root, bg="yellow")
textBox.columnconfigure(0, weight=1)
textBox.pack(expand=TRUE, fill=BOTH)
#attach the scrollbar to the text box
textBox.config(yscrollcommand=scrolly.set)
scrolly.config(command=textBox.yview)

root.mainloop()