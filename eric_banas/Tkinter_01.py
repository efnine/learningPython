from tkinter import *
from tkinter import ttk

# --- Example 6 (See below) Creating a button event
def getSum(event):
    num1 = int(num1Entry.get())
    num2 = int(num2Entry.get())
    
    sum = num1 + num2
    
    sumEntry.delete(0, 'end')
    
    sumEntry.insert(0, sum)
    
# Creating a GUI window
root = Tk()

# Giving HUI a title
root.title("My GUI")

# ---- COMPONENTS AVAILABLE ----
# Button, Label, Canvas, Meny, Text, Scale, OptionMenu
# Frame, CheckButton, LabelFrame, MenuButton, PanedWindow, 
# Entry, ListBox, Message, RadioButton, ScrollBar, 
# Bitmap, SpinBox, Image
# ------------------------------

# --- Example 1
# ttk.Button(root, text='Hello There').grid()


# --- Example 2
# frame = Frame(root)
# labelText = StringVar()
# label = Label(frame, textvariable=labelText)
# button = Button(frame, text='Click Me')
# labelText.set("I am a Label")
# label.pack()
# button.pack()
# frame.pack()


# --- Example 3
# frame = Frame(root)
# Label(frame, text="A bunch of Buttons").pack()
# Button(frame, text="Button 1").pack(side=LEFT, fill=Y)
# Button(frame, text="Button 2").pack(side=TOP, fill=X)
# Button(frame, text="Button 3").pack(side=RIGHT, fill=X)
# Button(frame, text="Button 4").pack(side=LEFT, fill=X)
# frame.pack()


# --- Example 4 User Form
# Label(root, text='First Name:').grid(row=0, column=0, sticky=W, padx=4)
# Entry(root).grid(row=0, column=1, stick=E,pady=4)
# 
# Label(root, text='Last Name:').grid(row=1, column=0, sticky=W, padx=4)
# Entry(root).grid(row=1, column=1, stick=E,pady=4)
# 
# Button(root, text='Submit').grid(row=3, column=1, stick=E,pady=4)


# --- Example 5 
# Label(root, text='Description').grid(row=0, column=0, sticky=W)
# Entry(root, width=50).grid(row=0, column=1)
# Button(root, text='Submit').grid(row=0, column=2)
# 
# Label(root, text='Quality').grid(row=1, column=0, sticky=W)
# Radiobutton(root, text='New', value=1).grid(row=2, column=0, sticky=W)
# Radiobutton(root, text='Good', value=2).grid(row=3, column=0, sticky=W)
# Radiobutton(root, text='Poor', value=3).grid(row=4, column=0, sticky=W)
# Radiobutton(root, text='Damage', value=4).grid(row=5, column=0, sticky=W)
# 
# Label(root, text='Benefits').grid(row=1, column=1, sticky=W)
# Checkbutton(root, text='Free Shipping').grid(row=2, column=1, sticky=W)
# Checkbutton(root, text='Bonus Gift').grid(row=3, column=1, sticky=W)


# --- Example 6 (See above) Creating a button event
num1Entry = Entry(root)
num1Entry.pack(side=LEFT)

Label(root, text='+').pack(side=LEFT)

num2Entry = Entry(root)
num2Entry.pack(side=LEFT)

equalButton = Button(root, text='=')
equalButton.bind("<Button-1>", getSum)
equalButton.pack(side=LEFT)

sumEntry = Entry(root)
sumEntry.pack(side=LEFT)


# Ensuring the GUI window remains visible
root.mainloop()


































