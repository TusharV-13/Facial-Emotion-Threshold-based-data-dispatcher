import tkinter
import sys
import os
from tkinter import messagebox
from tkinter import *
from tkinter import ttk

root = tkinter.Tk()
root.title("Instructions")
v = tkinter.IntVar()

tkinter.Label(root, 
        text="Instructions"+"\n"+"\n",
        justify = tkinter.LEFT,
        padx = 20).pack()

scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill=Y )

w = Label(root, text="Label: ")#some label



mylist = Listbox(root, yscrollcommand = scrollbar.set )

mylist.insert(END,"  *The following app requires the use of webcam/camera for scanning the face")
# mylist.insert(END,"   face")
mylist.insert(END,"  *It also takes the ip address from the user to calculate the cordinates on the map while")
mylist.insert(END,"   attaching the report")
mylist.insert(END,"  *Please ensure that the room is completely lit so that the application can function properly ")
# mylist.insert(END,"   application can function properly")
mylist.insert(END,"  *As the following product is in prototype stage there is a high chance of application crashing")
# mylist.insert(END,"   chance of the application crashing.")
mylist.insert(END,"  *Users are advised to check the spam folder as well if they could not find the report on the")
mylist.insert(END,"   email account")
mylist.insert(END,"  *Please be aware thatDelicate informations of the user is taken to analyze the data so to be ")
mylist.insert(END,"   authentic")
mylist.insert(END,"  *The app is built on tkinter and takes help of other modules which has been included in the")
mylist.insert(END,"   help section on the github page")



mylist.pack(  fill = BOTH )
scrollbar.config( command = mylist.yview )

tkinter.Radiobutton(root, 
              text="I agree with the above rules and guidelines",
              padx = 20, 
              variable=v, 
              value=1).pack(anchor=tkinter.W)


canvas1 = tkinter.Canvas(root, width = 500, height = 200)
canvas1.pack()
def facedetect():
    MsgBox = tkinter.messagebox.askquestion('Emotion Dispatcher',"Do you wish to proceed?",icon = 'warning')
    if MsgBox == 'yes':
        os.system('python real_time_video.py')
    else:
        root.destroy()
def cancel():
    root.destroy()
button1 = tkinter.Button (root, text='Continue',command=facedetect,bg='green',fg='black').place(x=360,y=300) 
button2 = tkinter.Button (root, text='Cancel',command=cancel,bg='red',fg='black').place(x=260,y=300) 
canvas1.create_window(150, 150, window=button1)
root.mainloop()