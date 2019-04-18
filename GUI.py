import tkinter as tk  # python 3
from tkinter import font  as tkfont  # python 3
import cyride
import time
import weather
import IsRoomMateHome as home
import GoogleCalendar as calendar
from tkinter import Canvas
from tkinter import ttk


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
        self.currFrame = 2
        self.weatherCount = 360
        self.start()

    def show_frame(self):
        '''Show a frame for the given page name'''
        if self.currFrame == 0:
            frame = self.frames["PageOne"]
            frame.tkraise()
            self.currFrame = 1
        elif self.currFrame == 1:
            PageTwo.update_home(self.frames["PageTwo"])
            frame = self.frames["PageTwo"]
            frame.tkraise()
            self.currFrame = 2
        else:
            StartPage.update_label(self.frames["StartPage"])
            frame = self.frames["StartPage"]
            frame.tkraise()
            self.currFrame = 0

    def start(self):
        if self.weatherCount == 360:
            PageOne.update_weather(self.frames["PageOne"])
            PageTwo.update_cal(self.frames["PageTwo"])
            self.weatherCount = 0
        else:
            self.weatherCount += 1
        self.show_frame()
        self.id = self.after(5000, self.start)


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

        self.Label = tk.Label(self, text="CyRide Predictions at Coover Hall:", fg='white', bg='black',font=("Helvetica", 50))
        self.Label.pack(pady=25)

        self.CardinalPrediction = tk.Label(self)
        self.CardinalLabel = tk.Label(self, text=" 21 Cardinal:", fg='Red', bg='black', font=("Helvetica", 40))
        self.GoldPrediction = tk.Label(self)
        self.GoldLabel = tk.Label(self, text="\n25 Gold:", fg='Yellow', bg='black', font=("Helvetica", 40))
        self.GreenPrediction = tk.Label(self)
        self.GreenLabel = tk.Label(self, text="\n2 Green:", fg='Green', bg='black', font=("Helvetica", 40))
        self.BrownPrediction = tk.Label(self)
        self.BrownLabel = tk.Label(self, text="\n6 Brown:", fg='Brown', bg='black', font=("Helvetica", 40))
        self.BluePrediction = tk.Label(self)
        self.BlueLabel = tk.Label(self, text="\n3 Blue:", fg='Blue', bg='black', font=("Helvetica",40))

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

        self.CardinalPrediction.configure(text=self.Cardinal.getPrediction(), fg='white', bg='black', font=("Helvetica", 35))
        self.GoldPrediction.configure(text=self.Gold.getPrediction(), fg='white', bg='black', font=("Helvetica", 35))
        self.GreenPrediction.configure(text=self.Green.getPrediction(), fg='white', bg='black', font=("Helvetica", 35))
        self.BrownPrediction.configure(text=self.Brown.getPrediction(), fg='white', bg='black', font=("Helvetica", 35))
        self.BluePrediction.configure(text=self.Blue.getPrediction(), fg='white', bg='black', font=("Helvetica", 35))

        self.Clock = tk.Label(self, text=time.strftime("%A, %B %d | %I:%M %p"), fg='white', bg='black',
                              font=("Helvetica", 15))
        self.Clock.pack(side='bottom')

    def update_label(self):
        self.CardinalPrediction.configure(text=self.Cardinal.getPrediction())
        self.GoldPrediction.configure(text=self.Gold.getPrediction())
        self.GreenPrediction.configure(text=self.Green.getPrediction())
        self.BrownPrediction.configure(text=self.Brown.getPrediction())
        self.BluePrediction.configure(text=self.Blue.getPrediction())
        self.Clock.configure(text=time.strftime("%A, %B %d | %I:%M %p"))

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        colSize = 120
        self.w = weather.Weather()
        self.tempLabel = tk.Label(self)
        self.tempLabel.grid(row=0, column=1, sticky="WS")
        self.tempLabel.configure(text=self.w.temp, fg='white', bg='black', font=("Helvetica", 120))

        self.conditionLabel = tk.Label(self)
        self.conditionLabel.grid(row=1, column=0)
        self.conditionLabel.configure(text=self.w.condition, fg='white', bg='black', font=("Helvetica", 50))

        self.conditionImage = tk.PhotoImage(file=self.w.conditionFile)
        self.conditionImageLabel = tk.Label(self)
        self.conditionImageLabel.grid(row=0, column=0)
        self.conditionImageLabel.configure(image=self.conditionImage, bg='black')

        self.windLabel = tk.Label(self)
        self.windLabel.grid(row=1, column=1, sticky="W")
        self.windLabel.configure(text=self.w.wind, fg='white', bg='black', font=("Helvetica", 50))


        # Sunrise / Sunset
        self.sunriseLabel = tk.Label(self)
        self.sunriseLabel.grid(row=1, column=2, sticky="N")
        self.sunriseLabel.configure(text="Rise:\n{}".format(self.w.sunrise()), fg='white', bg='black', font=("Helvetica", 50))

        self.sunsetLabel = tk.Label(self)
        self.sunsetLabel.grid(row=1, column=3, sticky="N")
        self.sunsetLabel.configure(text="Set:\n{}".format(self.w.sunset()), fg='white', bg='black', font=("Helvetica", 50))

        # High / Low
        self.highLabel = tk.Label(self)
        self.highLabel.grid(row=0, column=2)
        self.highLabel.configure(text="High:\n{}".format(self.w.high), fg='white', bg='black', font=("Helvetica", 70))

        self.lowLabel = tk.Label(self)
        self.lowLabel.grid(row=0, column=3)
        self.lowLabel.configure(text="Low:\n{}".format(self.w.low), fg='white', bg='black', font=("Helvetica", 70))

        # Line
        self.line = Canvas(self)
        self.line.grid(row=8, column=0, columnspan=100, pady=50)
        self.line.config(bg='white', width=tk.Frame.winfo_screenwidth(self), height=2)

        # Forecast
        self.f = weather.Forecast()
        days = self.f.getForecast()
        day1 = "{}\nH: {}\nL: {}".format(days['day1']['name'], days['day1']['high'], days['day1']['low'], days['day1']['description'])
        day2 = "{}\nH: {}\nL: {}".format(days['day2']['name'], days['day2']['high'], days['day2']['low'], days['day2']['description'])
        day3 = "{}\nH: {}\nL: {}".format(days['day3']['name'], days['day3']['high'], days['day3']['low'], days['day3']['description'])
        day4 = "{}\nH: {}\nL: {}".format(days['day4']['name'], days['day4']['high'], days['day4']['low'], days['day4']['description'])

        self.d1Image = tk.PhotoImage(file=self.w.displayConditions(days['day1']['description']))
        self.d1ImageLabel = tk.Label(self)
        self.d1ImageLabel.grid(row=9, column=0)
        self.d1ImageLabel.configure(image=self.d1Image, bg='black')
        self.d2Image = tk.PhotoImage(file=self.w.displayConditions(days['day2']['description']))
        self.d2ImageLabel = tk.Label(self)
        self.d2ImageLabel.grid(row=9, column=1)
        self.d2ImageLabel.configure(image=self.d1Image, bg='black')
        self.d3Image = tk.PhotoImage(file=self.w.displayConditions(days['day3']['description']))
        self.d3ImageLabel = tk.Label(self)
        self.d3ImageLabel.grid(row=9, column=2)
        self.d3ImageLabel.configure(image=self.d1Image, bg='black')
        self.d4Image = tk.PhotoImage(file=self.w.displayConditions(days['day4']['description']))
        self.d4ImageLabel = tk.Label(self)
        self.d4ImageLabel.grid(row=9, column=3)
        self.d4ImageLabel.configure(image=self.d1Image, bg='black')

        self.day1Label = tk.Label(self, text=day1, fg='white', bg='black', font=("Helvetica", 50))
        self.day2Label = tk.Label(self, text=day2, fg='white', bg='black', font=("Helvetica", 50))
        self.day3Label = tk.Label(self, text=day3, fg='white', bg='black', font=("Helvetica", 50))
        self.day4Label = tk.Label(self, text=day4, fg='white', bg='black', font=("Helvetica", 50))

        self.day1Label.grid(row=10, column=0, padx=colSize, pady=25)
        self.day2Label.grid(row=10, column=1, padx=colSize, pady=25)
        self.day3Label.grid(row=10, column=2, padx=colSize, pady=25)
        self.day4Label.grid(row=10, column=3, padx=colSize, pady=25)

        # Clock
        self.Clock = tk.Label(self, text=time.strftime("%A, %B %d | %I:%M %p"), fg='white', bg='black',
                              font=("Helvetica", 15))
        self.Clock.grid(row=11, column=1, columnspan=2, pady=19)

    def update_weather(self):
        self.w = weather.Weather()
        self.tempLabel.configure(text=self.w.temp)
        self.conditionLabel.configure(text=self.w.condition)
        self.conditionImageLabel.configure(image=self.conditionImage)
        self.windLabel.configure(text=self.w.wind)
        self.highLabel.configure(text="Low:\n{}".format(self.w.high))
        self.lowLabel.configure(text="High:\n{}".format(self.w.low))

        # Forecast
        self.f = weather.Forecast()
        days = self.f.getForecast()
        self.d1Image = tk.PhotoImage(file=self.w.displayConditions(days['day1']['description']))
        self.d1ImageLabel.configure(image=self.d1Image, bg='black')
        self.d2Image = tk.PhotoImage(file=self.w.displayConditions(days['day2']['description']))
        self.d2ImageLabel.configure(image=self.d1Image, bg='black')
        self.d3Image = tk.PhotoImage(file=self.w.displayConditions(days['day3']['description']))
        self.d3ImageLabel.configure(image=self.d1Image, bg='black')
        self.d4Image = tk.PhotoImage(file=self.w.displayConditions(days['day4']['description']))
        self.d4ImageLabel.configure(image=self.d1Image, bg='black')

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Roommate Status:", fg='white', bg='black', font=("Helvetica", 50))
        label.grid(row=0, column=2, pady=25)

        self.kyleLabel = tk.Label(self)
        self.kyleLabel.configure(text=home.check_if_home('Kyle'), fg='white', bg='black', font=("Helvetica", 25))
        self.kyleLabel.grid(row=1, column=0, sticky='N')
        self.columnconfigure(0, minsize=450)

        self.line1 = Canvas(self)
        self.line1.grid(row=1, column=1, padx=15, rowspan=100)
        self.line1.config(bg='black', width=1, height=775)

        self.samLabel = tk.Label(self)
        self.samLabel.configure(text=home.check_if_home('Sam'), fg='white', bg='black', font=("Helvetica", 25))
        self.samLabel.grid(row=1, column=2, sticky='N')
        self.columnconfigure(2, minsize=450)

        self.line2 = Canvas(self)
        self.line2.grid(row=1, column=3, padx=15, rowspan=100)
        self.line2.config(bg='black', width=1, height=775)

        self.seanLabel = tk.Label(self)
        self.seanLabel.configure(text=home.check_if_home('Sean'), fg='white', bg='black', font=("Helvetica", 25))
        self.seanLabel.grid(row=1, column=4, sticky='N')
        self.columnconfigure(4, minsize=450)
        ##Calendars
        self.kyleCal = tk.Label(self)
        self.kyleCal.configure(text=calendar.Get_Google_Calendar('Kyle'), fg='white', bg='black', font=("Helvetica", 25))
        self.kyleCal.grid(row=3, column=0)

        self.samCal = tk.Label(self)
        self.samCal.configure(text=calendar.Get_Google_Calendar('Sam'), fg='white', bg='black',font=("Helvetica", 25))
        self.samCal.grid(row=3, column=2)

        self.seanCal = tk.Label(self)
        self.seanCal.configure(text=calendar.Get_Google_Calendar('Sean'), fg='white', bg='black',font=("Helvetica", 25))
        self.seanCal.grid(row=3, column=4)

    def update_home(self):
        self.kyleLabel.configure(text=home.check_if_home('Kyle'))
        self.samLabel.configure(text=home.check_if_home('Sam'))
        self.seanLabel.configure(text=home.check_if_home('Sean'))

    def update_cal(self):
        self.kyleCal.configure(text=calendar.Get_Google_Calendar("Kyle"))
        self.samCal.configure(text=calendar.Get_Google_Calendar("Sam"))
        self.seanCal.configure(text=calendar.Get_Google_Calendar("Sean"))

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
