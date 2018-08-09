from tkinter import *
import tkinter.messagebox

class DisplayReports():

    def __init__(self, master):
        # Window 
        self.master = master

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

        # middle Frame
        self.middlePart()
        # status bar
        status = Label(root, text="Everything is ok :)", bd=1, relief=SUNKEN, anchor = W)
        status.pack(side=BOTTOM, fill=X)
        
  
    def about(self):
        tkinter.messagebox.showinfo('Stock Predictor', 'Version: 1.0.0\nDeveloper: Mbadi Atieno Sheila')

    def middlePart(self):
        # company stock
        '''
        self.head = Label(self.master,text = 'Login',font = ('',35),pady = 10)
        self.head.pack()
        '''
        self.middleFrame = Frame(self.master)
       
        Label(self.middleFrame,text = 'Stream Tweets: ',font = ('',20), pady=5,padx=5).grid(sticky = W)
        Button(self.middleFrame,text = 'Get Tweets!      ' ,bd = 3 ,font = ('',15),padx=5,pady=5).grid(row=0,column=1, sticky=W)
        Label(self.middleFrame,text = 'Stream Stock Data: ',font = ('',20), pady=5,padx=5).grid(sticky = W)
        Button(self.middleFrame,text = 'Get Stock Data!' ,bd = 3 ,font = ('',15),padx=5,pady=5).grid(row=1,column=1, sticky=W)
        self.middleFrame.pack()


root = Tk()
reportsClass = DisplayReports(root)
root.mainloop()