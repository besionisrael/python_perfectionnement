############### Label.py

from tkinter import *
from tkinter import ttk        
    
root = Tk()

label = ttk.Label(root, text = "Hello, Tkinter!")
label.pack()
label.config(text = 'Howdy, Tkinter!')
label.config(text = 'Howdy, Tkinter! It\'s been a really long time since we last met.  Great to see you again!')
label.config(wraplength = 150)
label.config(justify = CENTER)
label.config(foreground = 'blue', background = 'yellow')
label.config(font = ('Courier', 18, 'bold'))
label.config(text = 'Howdy, Tkinter!')

logo = PhotoImage(file = 'python.png') # change path to image as necessary
label.config(image = logo)
label.config(compound = 'text')
label.config(compound = 'center')
label.config(compound = 'left')

root.mainloop()


############### Button.py

from tkinter import *
from tkinter import ttk        
    
root = Tk()

button = ttk.Button(root, text = "Click Me")
button.pack()

def callback():
    print('Clicked!')

button.config(command = callback)
button.invoke() #simulate a click

button.state(['disabled'])
print(button.instate(['disabled']))
button.state(['!disabled'])
print(button.instate(['!disabled']))

logo = PhotoImage(file = 'python.png') # change path to image as necessary
button.config(image = logo, compound = LEFT)
small_logo = logo.subsample(5, 5)
button.config(image = small_logo)

root.mainloop()


############### SelectionButtons.py

from tkinter import *
from tkinter import ttk        
    
root = Tk()

checkbutton = ttk.Checkbutton(root, text = 'SPAM?')
checkbutton.pack()
# all features are like button (command, state, instate)
spam = StringVar()
spam.set('SPAM!')
print(spam.get())

checkbutton.config(variable = spam, onvalue = 'SPAM Please!',
		   offvalue = 'Boo SPAM!')
print(spam.get())


#Radio Button (choices are exclusive)
breakfast = StringVar()
ttk.Radiobutton(root, text = 'SPAM', variable = breakfast,
		value = 'SPAM').pack()
ttk.Radiobutton(root, text = 'Eggs', variable = breakfast,
		value = 'Eggs').pack()
ttk.Radiobutton(root, text = 'Sausage', variable = breakfast,
		value = 'Sausage').pack()
ttk.Radiobutton(root, text = 'SPAM', variable = breakfast,
		value = 'SPAM').pack()
print(breakfast.get()) # Note: value will be empty if no selection is made

checkbutton.config(textvariable = breakfast) #link text to a variable
root.mainloop()


############### Entry.py

from tkinter import *
from tkinter import ttk        
    
root = Tk()

entry = ttk.Entry(root, width = 30)
entry.pack()

entry.get()
entry.delete(0, 1)
entry.delete(0, END)
entry.insert(0, 'Enter your password')

entry.config(show = '*')
entry.state(['disabled'])
entry.state(['readonly'])
entry.state(['!disabled'])

root.mainloop()


############### Combobox


from tkinter import *
from tkinter import ttk        
    
root = Tk()

month = StringVar()
combobox = ttk.Combobox(root, textvariable = month)
combobox.pack()
combobox.config(values = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print(month.get())
month.set('Dec')

year = StringVar()
Spinbox(root, from_ = 1990, to = 2014, textvariable = year).pack()
print(year.get())

