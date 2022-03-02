from tkinter import Tk
from tkinter import Label
import time

root = Tk()
root.title("Clock")


def present_time():
    # to show in 24 hour format write %H instead of %I
    display_time = time.strftime("%I:%M:%S %p")
    digi_clock.config(text=display_time)

    # calling function again after 200 miliseconds
    digi_clock.after(200, present_time)


digi_clock = Label(root, font=("arial", 150), bg="red", fg="black")
digi_clock.pack()
present_time()  # function calling
root.mainloop()  # to display output
