import tkinter as tk # providing classes for defining later

class Snake(tk.Canvas): # creating Canvas widgets to display text, lines, & graphics
    def __init__(self): # constructing a parent widget
        super().__init__(width=600, height=620, background="black", highlightthickness=0)

root=tk.Tk()
root.title("Snake")
root.resizable(False, False) #  tells window manager whether this is resizeable

board = Snake()

root.mainloop() #calling the mainloop of tk
