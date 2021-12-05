#### PACK

from tkinter import *
from tkinter import ttk        
    
root = Tk()

ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'yellow').pack(side = LEFT, anchor = 'nw') #nord west = top left
ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'blue').pack(side = LEFT, padx = 10, pady = 10) #External padding
label = ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'green')
label.pack(side = LEFT, ipadx = 10, ipady = 10) #Internal padding
print(label)

#Config to all slaves widgets
for widget in root.pack_slaves():
    widget.pack_configure(fill = BOTH, expand = True)
    print(widget.pack_info())

label.pack_forget()

root.mainloop()


#########G RID


from tkinter import *
from tkinter import ttk        
    
root = Tk()

ttk.Label(root, text = 'Yellow', background = 'yellow').grid(row = 0, column = 2, rowspan = 2, sticky = 'nsew')
ttk.Label(root, text = 'Blue', background = 'Blue').grid(row = 1, column = 0, columnspan = 2, sticky = 'nsew')
ttk.Label(root, text = 'Green', background = 'Green').grid(row = 0, column = 0, sticky = 'nsew', padx = 10, pady = 10)
ttk.Label(root, text = 'Orange', background = 'Orange').grid(row = 0, column = 1, sticky = 'nsew', ipadx = 25, ipady = 25)


root.rowconfigure(0, weight = 1) #Expand Mode
root.rowconfigure(1, weight = 3) #Expand Mpde
root.columnconfigure(2, weight = 1) #Expand Mode of column

root.mainloop()



 
####GEOMETRY

from tkinter import *
from tkinter import ttk        
    
root = Tk()

root.geometry('640x480+200+200')


ttk.Label(root, text = 'Yellow', background = 'yellow').place(x = 100, y = 50, width = 100, height = 50)
ttk.Label(root, text = 'Blue', background = 'blue').place(relx = 0.5, rely = 0.5, anchor = 'center', relwidth = 0.5, relheight = 0.5) #relative location
ttk.Label(root, text = 'Green', background = 'green').place(relx = 0.5, x = 100, rely = 0.5, y = 50) 
ttk.Label(root, text = 'Orange', background = 'orange').place(relx = 1.0, x = -5, y = 5, anchor = 'ne')

root.mainloop()
