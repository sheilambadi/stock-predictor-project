from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from save_stock_data import getStockData
from tweetclassifier import getTwitterData
from test_model import plotPredictions
from test_hybrid import plotHybridPredictions
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from sign_up import main

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
            plotPredictions('AMZN')
        elif value == 'AAPL':
            plotPredictions('AAPL')

    def selectedTickerHybrid(self, value):
        if value == 'AMZN':
            plotHybridPredictions('AMZN')
        elif value == 'AAPL':
            plotHybridPredictions('AAPL')

    def middlePart(self):
        # company stock
        
        self.head = Label(self.master,text = 'Stock Predictor',font = ('',35), fg='blue', pady = 10)
        self.head.pack()
        
        self.middleFrame = Frame(self.master)
       
        Label(self.middleFrame,text = 'Stream Tweets: ',font = ('',20), pady=5,padx=5).grid(sticky = W)
        Button(self.middleFrame,text = 'Get Tweets!      ' ,bd = 3 ,font = ('',15),padx=5,pady=5, bg='green',fg='white', command = getTwitterData).grid(row=0,column=1, sticky=W)
        Label(self.middleFrame,text = 'Stream Stock Data: ',font = ('',20), pady=5,padx=5).grid(sticky = W)
        Button(self.middleFrame,text = 'Get Stock Data!' ,bd = 3 ,font = ('',15),padx=5,pady=5,bg='green',fg='white', command=getStockData).grid(row=1,column=1, sticky=W)
        Label(self.middleFrame,text = 'Plot Stock Graph: ',font = ('',20), pady=5,padx=5).grid(sticky = W)
        Label(self.middleFrame,text = 'Plot Hybrid Graph: ',font = ('',20), pady=5,padx=5).grid(sticky = W)
        # create dropdown list
        tickerList = ['AAPL', 'AMZN']
        defaultValue = StringVar(self.middleFrame)
        defaultValue.set(tickerList[0])
        tickerDropdown = OptionMenu(self.middleFrame, defaultValue, *tickerList, command=self.selectedTicker)
        tickerDropdown.grid(row=2, column=1)

        tickerListHybrid = ['AAPL', 'AMZN']
        defaultValueHybrid = StringVar(self.middleFrame)
        defaultValueHybrid.set(tickerListHybrid[0])
        tickerDropdownHybrid = OptionMenu(self.middleFrame, defaultValueHybrid, *tickerListHybrid, command=self.selectedTickerHybrid)
        tickerDropdownHybrid.grid(row=3, column=1)

        #Button(self.middleFrame,text = 'Visualize' , font = ('',12),padx=2,pady=5, command=getStockData).grid(row=2,column=3, sticky=W)

        self.middleFrame.pack(ipadx=10, ipady=10)

root = Tk()
reportsClass = DisplayReports(root)
root.mainloop()