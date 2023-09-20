# TASK 1
# Open a tk window with a LabelFrame and a Frame in it.
# Check the pack or grid methods for Tk Widgets.
# Add an Entry (input field) and a button inside the LabelFrame.
# Add a Button bellow your input field inside the LabelFrame.
# When it’s clicked: the content of your Entry box is printed in UPPERCASE in your terminal.


from tkinter import * 

 #------------------------------------

def addBox():
    print ("ADD")

    ent = Entry(root)
    ent.pack()

    all_entries.append( ent )

#------------------------------------

def showEntries():

    for number, ent in enumerate(all_entries):
        print (number, ent.get().upper())

#------------------------------------
# Create Tkinter Object
root = Tk()
all_entries = []
 
showButton = Button(root, text='Show all text', command=showEntries)
showButton.pack()

addboxButton = Button(root, text='<Add Time Input>', fg="Red", command=addBox)
addboxButton.pack()



root.mainloop()
