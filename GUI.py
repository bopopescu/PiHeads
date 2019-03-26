import tkinter as tk
import cyride
import time
import weather as w

class GUI:
    def __init__(self, master):
        self.p = cyride.Predictions(822)
        self.cyrideLabel1 = tk.Label(master)
        self.cyrideLabel1.grid(row=0, column=0)
        self.cyrideLabel1.configure(text=self.p.getPrediction(), fg='white', bg='black', font=("Helvetica", 50))

        # Weather
        self.weather = w.Weather()
        self.temp = self.weather.temp, " °F"
        self.tempLabel = tk.Label(master)
        self.tempLabel.grid(row=4, column=0)
        self.tempLabel.configure(text=self.temp, fg='white', bg='black', font=("Helvetica", 50))
        self.conditionLabel = tk.Label(master)
        self.conditionLabel.grid(row=2, column=0)
        self.conditionLabel.configure(text=self.weather.condition, fg='white', bg='black', font=("Helvetica", 50))
        self.conditionPict = tk.PhotoImage(file=self.weather.conditionFile)
        self.conditionPictLabel = tk.Label(master)
        self.conditionPictLabel.grid(row=3, column=0)
        self.conditionPictLabel.configure(image=self.conditionPict, bg='black')

        self.count = 0
        self.update_label()
    def update_label(self):
        if self.count < 10:
            self.cyrideLabel1.configure(text=self.p.getPrediction())
            self.cyrideLabel1.after(1000, self.update_label)
            self.count += 1
        else:
            root.destroy()


root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(background='black')
while(True):
    GUI(root)
    root.mainloop()