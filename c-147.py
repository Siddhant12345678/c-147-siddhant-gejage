# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 14:01:53 2023

@author: LENOVO
"""

from tkinter import *

root = Tk()
root.title("ENCRYPTION WITH ASCII CODE")

root.geometry("400x400")
root.configure(background="blue")

enter_word = Entry(root)
enter_word.place(relx=0.5 , rely=0.4 ,anchor=CENTER)
 
label= Label(root,text="Name in ASCII : ", bg="white" , fg="black")
label2=Label(root,text="Encryted Name : ", bg="white", fg="black")


def asciiConverter():
    input_word=str(enter_word.get())
    
    for letter in input_word:
        label["text"] += str(ord(letter)) + " "
        ascii = int(ord(letter))
        encrypted = ascii - 1
        label2["text"] += str(chr(encrypted))
        
btn = Button(root, text = "Display the Ascii Code & Encrypted value", command = asciiConverter, bg = 'cornflower blue', fg = 'white')
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

label.place(relx = 0.5, rely = 0.6, anchor = CENTER)
label2.place(relx = 0.5, rely = 0.7, anchor = CENTER)

root.mainloop()
    
