from tkinter import Tk, Label
import time
import sys
def create_clock():
    root = Tk()
    root.title("Digital Clock")

    clock_label = Label(root, font=("Times New Roman",90),bg="#3B177B",fg="#fff")
    clock_label.pack()

    def update_time():
        current_time = time.strftime("%H:%M:%S %p")
        clock_label.config(text=current_time)
        clock_label.after(200, update_time)

    update_time()
    root.mainloop()

create_clock()