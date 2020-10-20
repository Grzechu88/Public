# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 20:29:37 2020

@author: Grzechu
"""
from tkinter import *
import random
root = Tk()
root.title("Dice Generator")
root.geometry("600x600")

resultd4_label = Label(root)
resultd6_label = Label(root)
resultd8_label = Label(root)
resultd10_label = Label(root)
resultd12_label = Label(root)
resultd20_label = Label(root)

def roll():
    global resultd4_label
    global resultd6_label
    global resultd8_label
    global resultd10_label
    global resultd12_label
    global resultd20_label 

    clear()    
    if  len(entryd4.get())!=0:
        resultfinal = 0
        for i in range(int(entryd4.get())):
            result = random.randint(1,4)
            resultfinal = resultfinal + result
            if i == 0:
                resultd4 = str(result)
            else:
                resultd4 = str(resultd4) + ", " + str(result)
        resultd4_label = Label(root, text= str(resultfinal) + " (" + str(resultd4) + ")", font=("Helvetica", 12))
        resultd4_label.grid(row=2, column=2, sticky=W)

    if  len(entryd6.get())!=0:
        resultfinal = 0
        for i in range(int(entryd6.get())):
            result = random.randint(1,6)
            resultfinal = resultfinal + result
            if i == 0:
                resultd6 = str(result)
            else:
                resultd6 = str(resultd6) + ", " + str(result)
        resultd6_label = Label(root, text= str(resultfinal) + " (" + str(resultd6) + ")", font=("Helvetica", 12))
        resultd6_label.grid(row=4, column=2, sticky=W)        
        
    if  len(entryd8.get())!=0:
        resultfinal = 0
        for i in range(int(entryd8.get())):
            result = random.randint(1,8)
            resultfinal = resultfinal + result
            if i == 0:
                resultd8 = str(result)
            else:
                resultd8 = str(resultd8) + ", " + str(result)
        resultd8_label = Label(root, text= str(resultfinal) + " (" + str(resultd8) + ")", font=("Helvetica", 12))
        resultd8_label.grid(row=6, column=2, sticky=W)     
        
    if  len(entryd10.get())!=0:
        resultfinal = 0
        for i in range(int(entryd10.get())):
            result = random.randint(1,10)
            resultfinal = resultfinal + result
            if i == 0:
                resultd10 = str(result)
            else:
                resultd10 = str(resultd10) + ", " + str(result)
        resultd10_label = Label(root, text= str(resultfinal) + " (" + str(resultd10) + ")", font=("Helvetica", 12))
        resultd10_label.grid(row=8, column=2, sticky=W)     

    if  len(entryd12.get())!=0:
        resultfinal = 0
        for i in range(int(entryd12.get())):
            result = random.randint(1,12)
            resultfinal = resultfinal + result
            if i == 0:
                resultd12 = str(result)
            else:
                resultd12 = str(resultd12) + ", " + str(result)
        resultd12_label = Label(root, text= str(resultfinal) + " (" + str(resultd12) + ")", font=("Helvetica", 12))
        resultd12_label.grid(row=10, column=2, sticky=W)     
        
    if  len(entryd20.get())!=0:
        resultfinal = 0
        for i in range(int(entryd20.get())):
            result = random.randint(1,20)
            resultfinal = resultfinal + result
            if i == 0:
                resultd20 = str(result)
            else:
                resultd20 = str(resultd20) + ", " + str(result)
        resultd20_label = Label(root, text= str(resultfinal) + " (" + str(resultd20) + ")", font=("Helvetica", 12))
        resultd20_label.grid(row=12, column=2, sticky=W)     

def clear():
    resultd4_label.destroy()
    resultd6_label.destroy()
    resultd8_label.destroy()
    resultd10_label.destroy()
    resultd12_label.destroy()
    resultd20_label.destroy()


header = Label(root, text="Dice Generator", font=("Helvetica", 32))
#header.grid(row=0, column=3, padx=(10,200))
header.place(relx=0.5, anchor="n")

placeholder = Label(root).grid(row=0, column=0, pady=25)


labeld4 = Label(root, text="d4", font=("Helvetica", 12)).grid(row=2, column=0, sticky=W)
entryd4 = Entry(root)
entryd4.grid(row=2, column=1, pady=5)

labeld6 = Label(root, text="d6", font=("Helvetica", 12)).grid(row=4, column=0, sticky=W)
entryd6 = Entry(root)
entryd6.grid(row=4, column=1, pady=5)

labeld8 = Label(root, text="d8", font=("Helvetica", 12)).grid(row=6, column=0, sticky=W)
entryd8 = Entry(root)
entryd8.grid(row=6, column=1, pady=5)
               
labeld10 = Label(root, text="d10", font=("Helvetica", 12)).grid(row=8, column=0, sticky=W)
entryd10 = Entry(root)
entryd10.grid(row=8, column=1, pady=5)

labeld12 = Label(root, text="d12", font=("Helvetica", 12)).grid(row=10, column=0, sticky=W)
entryd12 = Entry(root)
entryd12.grid(row=10, column=1, pady=5)


labeld20 = Label(root, text="d20", font=("Helvetica", 12)).grid(row=12, column=0, sticky=W)
entryd20 = Entry(root)
entryd20.grid(row=12, column=1, pady=5)

rollButton = Button(root, text="Roll", command=roll).grid(row=13, column=0, pady=5)

root.mainloop()