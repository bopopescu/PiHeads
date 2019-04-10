import tkinter as tk  # python 3
from tkinter import font  as tkfont  # python 3
import cyride
import time
import weather
import IsRoomMateHome as home
import GoogleCalendar as calendar


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
        self.columnconfigure(0, weight=1)
        self.controller = controller
        self.Cardinal = cyride.Predictions(930)
        self.Gold = cyride.Predictions(952)
        self.Green = cyride.Predictions(822)
        self.Brown = cyride.Predictions(862)
        self.Blue = cyride.Predictions(830)

        self.Label = tk.Label(self, text="CyRide Predictions at Coover Hall:", fg='white', bg='black',
                              font=("Helvetica", 50))
        self.Label.pack(pady=25)

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

        self.Clock = tk.Label(self, text=time.strftime("%A, %B %d | %I:%M %p"), fg='white', bg='black',
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
        self.Clock.configure(text=time.strftime("%A, %B %d | %I:%M %p"))

        self.CardinalPrediction.after(5000, self.update_label)

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.w = weather.Weather()
        self.tempLabel = tk.Label(self)
        self.tempLabel.grid(row=4, column=1, columnspan=2, ipadx='400')
        self.tempLabel.configure(text=self.w.temp, fg='white', bg='black', font=("Helvetica", 50))

        self.conditionLabel = tk.Label(self)
        self.conditionLabel.grid(row=2, column=1, columnspan=2)
        self.conditionLabel.configure(text=self.w.condition, fg='white', bg='black', font=("Helvetica", 50))

        self.conditionImage = tk.PhotoImage(file=self.w.conditionFile)
        self.conditionImageLabel = tk.Label(self)
        self.conditionImageLabel.grid(row=3, column=1, columnspan=2)
        self.conditionImageLabel.configure(image=self.conditionImage, bg='black')

        # Sunrise / Sunset
        self.sunriseLabel = tk.Label(self)
        self.sunriseLabel.grid(row=7, column=0, sticky='W')
        self.sunriseLabel.configure(text=self.w.sunrise(), fg='white', bg='black', font=("Helvetica", 50))
        self.sunriseLabel1 = tk.Label(self)
        self.sunriseLabel1.grid(row=6, column=0, sticky='W')
        self.sunriseLabel1.configure(text="Sunrise: ", fg='white', bg='black', font=("Helvetica", 50))

        self.sunsetLabel = tk.Label(self)
        self.sunsetLabel.grid(row=7, column=3, sticky='E')
        self.sunsetLabel.configure(text=self.w.sunset(), fg='white', bg='black', font=("Helvetica", 50))
        self.sunsetLabel1 = tk.Label(self)
        self.sunsetLabel1.grid(row=6, column=3, sticky='E')
        self.sunsetLabel1.configure(text="Sunset: ", fg='white', bg='black', font=("Helvetica", 50))

        # High / Low
        self.highLabel = tk.Label(self)
        self.highLabel.grid(row=5, column=1)
        self.highLabel.configure(text=self.w.high, fg='white', bg='black', font=("Helvetica", 50))

        self.lowLabel = tk.Label(self)
        self.lowLabel.grid(row=5, column=2)
        self.lowLabel.configure(text=self.w.low, fg='white', bg='black', font=("Helvetica", 50))


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Roommates:", fg='white', bg='black', font=("Helvetica", 50))
        label.pack(side="top", fill="x", pady=25)

        self.kyleLabel = tk.Label(self)
        self.kyleLabel.configure(text=home.check_if_home('Kyle'), fg='white', bg='black', font=("Helvetica", 25))
        self.kyleLabel.pack(pady=10)

        self.samLabel = tk.Label(self)
        self.samLabel.configure(text=home.check_if_home('Sam'), fg='white', bg='black', font=("Helvetica", 25))
        self.samLabel.pack(pady=10)

        self.seanLabel = tk.Label(self)
        self.seanLabel.configure(text=home.check_if_home('Sean'), fg='white', bg='black', font=("Helvetica", 25))
        self.seanLabel.pack(pady=10)

        self.update_home()

        ##Calendars
        label2 = tk.Label(self, text="Calendars:", fg='white', bg='black', font=("Helvetica", 50))
        label2.pack(side="top", fill="x", pady=25)
        self.kyleCal = tk.Label(self)
        self.kyleCal.configure(text=calendar.Get_Google_Calendar('Kyle'), fg='white', bg='black', font=("Helvetica", 25))
        self.kyleCal.pack(pady=5)

        self.samCal = tk.Label(self)
        self.samCal.configure(text=calendar.Get_Google_Calendar('Sam'), fg='white', bg='black',font=("Helvetica", 25))
        self.samCal.pack(pady=5)

        self.seanCal = tk.Label(self)
        self.seanCal.configure(text=calendar.Get_Google_Calendar('Sean'), fg='white', bg='black',font=("Helvetica", 25))
        self.seanCal.pack(pady=5)


    def update_home(self):
        self.kyleLabel.configure(text=home.check_if_home('Kyle'))
        self.samLabel.configure(text=home.check_if_home('Sam'))
        self.seanLabel.configure(text=home.check_if_home('Sean'))
        self.kyleLabel.after(5000, self.update_home)
    #def update_calendar(self):
        #Get_Google_Calendar()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
