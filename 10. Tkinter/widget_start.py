from tkinter import *
from tkinter import ttk        
    
root = Tk()


root.mainloop()
####1
ttk.Label(root, text = 'Hello, Tkinter!', background = 'yellow').pack(side = LEFT, anchor = 'nw')
ttk.Label(root, text = 'Hello, Tkinter!', background = 'blue').pack(side = LEFT)
label = ttk.Label(root, text = 'Hello, Tkinter!',background = 'green').pack(side = LEFT)
