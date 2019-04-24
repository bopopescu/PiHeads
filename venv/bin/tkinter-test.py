import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
import cyride
import datetime

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.attributes('-fullscreen', True)
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.configure(background='black')
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        self.currFrame = 3
        self.id = self.after(1000, self.start)


    def show_frame(self):
        '''Show a frame for the given page name'''
        if self.currFrame == 0:
            frame = self.frames["PageOne"]
            frame.tkraise()
            self.currFrame = 1
        elif self.currFrame == 1:
            frame = self.frames["PageTwo"]
            frame.tkraise()
            self.currFrame = 2
        else:
            frame = self.frames["StartPage"]
            frame.tkraise()
            self.currFrame = 0

    def start(self):
        self.show_frame()
        self.id = self.after(10000, self.start)



class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.controller = controller
        self.Cardinal = cyride.Predictions(930)
        self.Gold = cyride.Predictions(952)
        self.Green = cyride.Predictions(822)
        self.Brown = cyride.Predictions(862)
        self.Blue = cyride.Predictions(830)

        self.Label = tk.Label(self, text="CyRide Predictions at Coover Hall:", fg='white', bg='black',
                              font=("Helvetica", 50))
        self.Label.pack()

        self.CardinalPrediction = tk.Label(self)
        self.CardinalLabel = tk.Label(self, text="21 Cardinal:", fg='Red', bg='black', font=("Helvetica", 25))
        self.GoldPrediction = tk.Label(self)
        self.GoldLabel = tk.Label(self, text="25 Gold:", fg='Yellow', bg='black', font=("Helvetica", 25))
        self.GreenPrediction = tk.Label(self)
        self.GreenLabel = tk.Label(self, text="2 Green:", fg='Green', bg='black', font=("Helvetica", 25))
        self.BrownPrediction = tk.Label(self)
        self.BrownLabel = tk.Label(self, text="6 Brown:", fg='Brown', bg='black', font=("Helvetica", 25))
        self.BluePrediction = tk.Label(self)
        self.BlueLabel = tk.Label(self, text="3 Blue:", fg='Blue', bg='black', font=("Helvetica", 25))

        self.CardinalLabel.pack()
        self.CardinalPrediction.pack()
        self.GoldLabel.pack()
        self.GoldPrediction.pack()
        self.GreenLabel.pack()
        self.GreenPrediction.pack()
        self.BrownLabel.pack()
        self.BrownPrediction.pack()
        self.BlueLabel.pack()
        self.BluePrediction.pack()

        self.CardinalPrediction.configure(text=self.Cardinal.getPrediction(), fg='white', bg='black',
                                          font=("Helvetica", 20))
        self.GoldPrediction.configure(text=self.Gold.getPrediction(), fg='white', bg='black', font=("Helvetica", 20))
        self.GreenPrediction.configure(text=self.Green.getPrediction(), fg='white', bg='black', font=("Helvetica", 20))
        self.BrownPrediction.configure(text=self.Brown.getPrediction(), fg='white', bg='black', font=("Helvetica", 20))
        self.BluePrediction.configure(text=self.Blue.getPrediction(), fg='white', bg='black', font=("Helvetica", 20))

        self.Time = datetime.datetime.now()
        self.Clock = tk.Label(self, text=self.Time.strftime("%Y-%m-%d %H:%M"), fg='white', bg='black',
                              font=("Helvetica", 15))
        self.Clock.pack(side='bottom')

        self.count = 0
        self.update_label()

    def update_label(self):
        self.CardinalPrediction.configure(text=self.Cardinal.getPrediction())
        self.GoldPrediction.configure(text=self.Gold.getPrediction())
        self.GreenPrediction.configure(text=self.Green.getPrediction())
        self.BrownPrediction.configure(text=self.Brown.getPrediction())
        self.BluePrediction.configure(text=self.Blue.getPrediction())

        self.CardinalPrediction.after(5000, self.update_label)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
