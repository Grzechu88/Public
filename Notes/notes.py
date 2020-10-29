# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 18:16:22 2020

@author: Grzechu
"""

from tkinter import *

root = Tk()

root.title("Notes")
root.geometry("300x300")

global mainText, newText
newText = ""

def newNote():
    newWindow = Toplevel()

    newWindow.title("Notes")
    newWindow.geometry("300x300")

    #create scroll bar
    scrolly = Scrollbar(newWindow)
    scrolly.pack(side=RIGHT, fill=Y)
    #create text box and fill the entire window with it
    textBox = Text(newWindow, bg="magenta")
    textBox.columnconfigure(0, weight=1)
    textBox.pack(expand=TRUE, fill=BOTH)
    #attach the scrollbar to the text box
    textBox.config(yscrollcommand=scrolly.set)
    scrolly.config(command=textBox.yview)
    
    newText = textBox.get("1.0", "end-1c")
    
    newNote.mainloop()
    
def saveNotes():
    mainText = textBox.get("1.0", "end-1c")
    print("Text from the main window: " + str(mainText))
    if newText is True:
        print("Text from the secondwindow: " + str(newText))
    
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


#adding the menu widget
topMenu = Menu(root)
fileMenu = Menu(topMenu, tearoff=0)
fileMenu.add_command(label="New note", command=newNote)
fileMenu.add_command(label="Save notes", command=saveNotes)
fileMenu.add_separator()
fileMenu.add_command(label="New category")
fileMenu.add_command(label="Category list")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.destroy)
        
topMenu.add_cascade(label="File", menu=fileMenu)

root.config(menu=topMenu)

root.mainloop()