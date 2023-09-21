# TASK 3
# Draw a stickman figure using Tkinter’s drawing functions.
# It should be done with 5 lines and 1 circle.
# Moreover, put some text near your stickman’s head.
# Get familiar with how coordinates work in computer graphic.

from tkinter import *

root = Tk()
root.geometry("1500x1500")

canvas = Canvas(root, width = 1500, height = 850)
canvas.create_text(650, 50, text="Bonjour", fill="black", font=("Helvetica 15 bold"))
canvas.pack()
canvas.create_oval(800, 50, 700, 150, fill="green", width=3)
canvas.create_line(750,150,750,350, fill="black", width=3)
canvas.create_line(750,200,850,240, fill="blue", width=3)
canvas.create_line(750,200,650,240, fill="blue", width=3)
canvas.create_line(750,350,850,500, fill="red", width=3)
canvas.create_line(750,350,650,500, fill="red", width=3)

root.mainloop()