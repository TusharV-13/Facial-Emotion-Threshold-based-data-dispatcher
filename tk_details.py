from tkinter import *
import sqlite3
import os

root = Tk()
root.geometry('500x500')
root.title("Details")


Fullname=StringVar()
Age=StringVar()
Phonenumber=StringVar()
var = StringVar(value="1")
c=StringVar()
illness=StringVar()


def submit_and_next():
    name1=Fullname.get()
    age=Age.get()
    phone=Phonenumber.get()
    gender=var.get()
    region=c.get()
    disorder=illness.get()
    f = open("details.txt","w+")
    f.truncate(0)
    f.write("Name: "+str(name1)+"\n")
    f.write("Age: "+str(age)+"\n")
    f.write("Phone: "+str(phone)+"\n")
    f.write("Gender: "+str(gender)+ "\n")
    f.write("Region: "+str(region)+"\n")
    f.write("illness: "+str(disorder)+"\n")
    f.close()
    os.system('python tkt.py')

def cancel():
    root.destroy()
   
             
label_0 = Label(root, text="Details",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="Full Name",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,textvar=Fullname)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Age",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root,textvar=Age)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Phone Number",width=20,font=("bold", 10))
label_3.place(x=70,y=230)

entry_3 = Entry(root,textvar=Phonenumber)
entry_3.place(x=240,y=230)

label_4 = Label(root, text="Gender",width=20,font=("bold", 10))
label_4.place(x=70,y=280)

Radiobutton(root, text="Male",padx = 5, variable=var, value="Male").place(x=235,y=280)
Radiobutton(root, text="Female",padx = 20, variable=var, value="Female").place(x=300,y=280)

label_5 = Label(root, text="Region",width=20,font=("bold", 10))
label_5.place(x=70,y=330)

list1 = ['Andhra Pradesh','Maharashtra', 'TamilNadu','Karnataka','Delhi'];


droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('select your region') 
droplist.place(x=240,y=330)

label_6 = Label(root, text="Medical illness",width=20,font=("bold", 10))
label_6.place(x=70,y=380)

entry_6 = Entry(root,textvar=illness)
entry_6.place(x=240,y=380)

Button(root, text='Continue',width=20,bg='green',fg='black',command=submit_and_next).place(x=280,y=430)
Button(root, text='Cancel',width=20,bg='red',fg='black',command=cancel).place(x=60,y=430)

root.mainloop()