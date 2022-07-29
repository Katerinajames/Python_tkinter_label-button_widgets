
import tkinter as tk
from tkinter import *

root=Tk()
root.title("Hi")
label=Label(root,text="I am a label widget")
label.pack()
button=Button(root ,text="I am a button widget")
button.pack()

root.geometry('300x300')
root.mainloop()
