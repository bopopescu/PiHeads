import tkinter as tk
import cyride
import time

class GUI:
    def __init__(self, master):
        self.p = cyride.Predictions(930)
        self.cyrideLabel1 = tk.Label(master)
        self.cyrideLabel1.grid(row=0, column=0)
        self.cyrideLabel1.configure(text=self.p.getPrediction(), fg='white', bg='black', font=("Helvetica", 50))

        self.count = 0
        self.update_label()
    def update_label(self):
        if self.count < 10:
            self.cyrideLabel1.configure(text=self.p.getPrediction())
            self.cyrideLabel1.after(1000, self.update_label)
            self.count += 1


root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(background='black')
GUI(root)
root.mainloop()