from tkinter import *

def clickItem():
    print('Clicked!!!')


root = Tk()

# menu at top
menu = Menu(root)

root.config(menu=menu)

submenu = Menu(menu)
menu.add_cascade(label='File', menu=submenu)
submenu.add_command(label='Save', command=clickItem)
submenu.add_command(label='New', command=clickItem)
submenu.add_separator()
submenu.add_command(label='Exit', command=clickItem)

editmenu = Menu(menu)
menu.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Save', command=clickItem)
editmenu.add_command(label='New', command=clickItem)
editmenu.add_separator()
submenu.add_command(label='Exit', command=clickItem)

# create toolbar
toolbar = Frame(root, bg='blue')
insertButton = Button(toolbar, text='Insert Image', command=clickItem)
insertButton.pack(side=LEFT, padx=2, pady=2)

insertButton = Button(toolbar, text='Print', command=clickItem)
insertButton.pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side=TOP, fill=X)

# status bar
status = Label(root, text="File Saved", bd=1, relief=SUNKEN, anchor = W)
status.pack(side=BOTTOM, fill=X)



root =  mainloop()