from tkinter import *
from PIL import ImageTk,Image
from tkinter import Button



root=Tk()
root.title("Login")
root.geometry("1300x1500")


Profile= Button(root, text="Profile", width=9, height=2, background="#2B3856", fg="white", command="Profile").place(x=400,y=170)
Attendance= Button(root, text="Attendance", width=9, height=2, background="#2B3856", fg="white", command="Attendance").place(x=540,y=170)
Routine= Button(root, text="Routine", width=9, height=2, background="#2B3856", fg="white", command="Routine").place(x=680,y=170)
Result= Button(root, text="Result", width=9, height=2, background="#2B3856", fg="white", command="Result").place(x=820,y=170)
Attendance = Label(root,text="Attendence", font="Helvetica 25 bold").place(x=615,y=250)


Student= Label(root,text="Student").place(x=480,y=300)
e1= Entry(root, width=40).place(x=480 ,y=325)
Attendance= Label(root,text="Attendence").place(x=700,y=300)
e2= Entry(root, width=40).place(x=480 ,y=345)



Update_info = Button(root,text="Update",height=2, background="#2B3856", fg="white").place(x=615,y=555)



root.mainloop()