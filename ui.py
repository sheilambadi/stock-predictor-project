import tkinter as tk
from test_model import plotPredictions
from test_hybrid import plotHybridPredictions

# declare main window
window = tk.Tk()

window.title("Stock Predictor")
window.geometry("400x400")

# function to plot graph

plotPredictions(window)
plotHybridPredictions(window)
    
window.mainloop()