from tkinter import * 

win = Tk()

win.geometry("300x300")

bg = PhotoImage(file = "photo.png")

canvas = Canvas(win)
canvas.pack()

lf = LabelFrame(canvas, text= "image ")

label = Label(lf, image = bg)
label.pack(padx = 20, pady = 20)

lf.pack()
win.mainloop()