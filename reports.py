from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from save_stock_data import getStockData
from tweetclassifier import getTwitterData
from test_model import plotPredictions

class DisplayReports():

    def __init__(self, master):
        # Window 
        self.master = master

        topFrame = Frame(master)
        topFrame.pack()
        
        master.geometry('600x600')
        master.title('Stock Predictor')
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

    def selectedTicker(self, value):
        if value == 'AMZN':
            plotPredictions(self,'AMZN')
        elif value == 'AAPL':
            print('no')

    def middlePart(self):
        # company stock
        
        self.head = Label(self.master,text = 'Stock Predictor',font = ('',35),pady = 10)
        self.head.pack()
        
        self.middleFrame = Frame(self.master)
       
        Label(self.middleFrame,text = 'Stream Tweets: ',font = ('',20), pady=5,padx=5).grid(sticky = W)
        Button(self.middleFrame,text = 'Get Tweets!      ' ,bd = 3 ,font = ('',15),padx=5,pady=5, command = getTwitterData).grid(row=0,column=1, sticky=W)
        Label(self.middleFrame,text = 'Stream Stock Data: ',font = ('',20), pady=5,padx=5).grid(sticky = W)
        Button(self.middleFrame,text = 'Get Stock Data!' ,bd = 3 ,font = ('',15),padx=5,pady=5, command=getStockData).grid(row=1,column=1, sticky=W)
        Label(self.middleFrame,text = 'Select Company Ticker: ',font = ('',20), pady=5,padx=5).grid(sticky = W)

        # create dropdown list
        tickerList = ['AAPL', 'AMZN']
        defaultValue = StringVar(self.middleFrame)
        defaultValue.set(tickerList[0])
        tickerDropdown = OptionMenu(self.middleFrame, defaultValue, *tickerList, command=self.selectedTicker)
        tickerDropdown.grid(row=2, column=1)

        #Button(self.middleFrame,text = 'Visualize' , font = ('',12),padx=2,pady=5, command=getStockData).grid(row=2,column=3, sticky=W)

        self.middleFrame.pack(ipadx=10, ipady=10)

root = Tk()
reportsClass = DisplayReports(root)
root.mainloop()