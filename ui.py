from tkinter import *
import tkinter as tk
from test_model import plotPredictions, deleteCanvas
from test_hybrid import plotHybridPredictions

# declare main window
window = tk.Tk()

# Add a grid
mainframe = Frame(window)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 10, padx = 10)
 
# Create a Tkinter variable
tkvar = StringVar(window)
 
# Dictionary with options
choices = {'AAPL', 'AMZN', 'FB', 'GM', 'GOOGL', 'MSFT', 'NFLX', 'TSLA'}
tkvar.set('AAPL') # set the default option
 
popupMenu = OptionMenu(mainframe, tkvar, *choices)
Label(mainframe, text="Choose Stock Ticker").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)
 
def getTicker():
    return str(tkvar.get())

# on change dropdown value
def change_dropdown(*args):
    tkvar.get()
    #print( tkvar.get() )
    # print(getTicker())
 

# link function to change dropdown
tkvar.trace('w', change_dropdown)

window.title("Stock Predictor")
window.geometry("400x400")

# function to plot graph

def plotInUI():
    ticker = str(getTicker())
    print(ticker)
    plotPredictions(window, ticker)
    plotHybridPredictions(window, ticker)

display_button = tk.Button(text="Display", bg="green", command=plotInUI)
display_button.pack()

    
window.mainloop()