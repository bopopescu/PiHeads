import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
import cyride

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
        self.controller = controller
        self.p = cyride.Predictions(822)
        self.Label1 = tk.Label(self)
        self.Label1.grid(row=0, column=0)
        self.Label1.configure(text=self.p.getPrediction(), fg='white', bg='black', font=("Helvetica", 50))

        self.count = 0
        self.update_label()

    def update_label(self):
        if self.count < 10:
            self.Label1.configure(text=self.p.getPrediction())
            self.Label1.after(1000, self.update_label)
            self.count += 1


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