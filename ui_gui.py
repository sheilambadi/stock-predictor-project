import tkinter as tk
from tkinter import ttk
from test_model import plotPredictions
from test_hybrid import plotHybridPredictions

LARGE_FONT= ("Verdana", 12)

class DisplayPlots(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Stock Predictor")
        tk.Tk.wm_geometry(self, "650x650")
        
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Choose Stock Ticker:", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = ttk.Button(self, text="AAPL",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = ttk.Button(self, text="AMZN",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="AAPL", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="AMZN",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        plotPredictions(self, "AAPL")
        plotHybridPredictions(self, "AAPL")


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="AMZN", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="AAPL",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()
        
        plotPredictions(self, "AMZN")
        plotHybridPredictions(self, "AMZN")

app = DisplayPlots()
app.mainloop()
        