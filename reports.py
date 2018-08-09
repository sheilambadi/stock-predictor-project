from tkinter import *
import tkinter.messagebox

class DisplayReports():

    def __init__(self, master):
        topFrame = Frame(master)
        topFrame.pack()
        master.geometry('600x600')
        # menu at top
        menu = Menu(master)

        master.config(menu=menu)

        fileMenu = Menu(menu)
        menu.add_cascade(label='File', menu=fileMenu)
        # add command to save graph
        fileMenu.add_command(label='Save Graph')
        fileMenu.add_separator()
        fileMenu.add_command(label='Exit', command=topFrame.quit)

        helpMenu = Menu(menu)
        menu.add_cascade(label='Help', menu=helpMenu)
        helpMenu.add_command(label='About', command=self.about)
  
    def about(self):
        tkinter.messagebox.showinfo('Stock Predictor', 'Version: 1.0.0\nDeveloper: Mbadi Atieno Sheila')

        


root = Tk()
reportsClass = DisplayReports(root)
root.mainloop()