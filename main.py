from tkinter import*
from tkinter import ttk
import tkinter
import tkinter.messagebox
from PIL import Image,ImageTk 
from student import Student 
from train import Train
from face_recongnition import Face_Recognition
from Attendance import Attendance
from developer import Developer
import os
from time import strftime
from datetime import datetime
from helpdesk import HelpDesk
class Face_Recongnition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition system")
         #first img
        img1=Image.open(r"C:\Users\Bharti Soni\Desktop\Attendance management system\college_images\Nce.jpg")
        img1=img1.resize((510,130))

        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=510,height=130)
        #second img
        img2=Image.open(r"C:\Users\Bharti Soni\Desktop\Attendance management system\college_images\college.jpg")
        img2=img2.resize((510,130))

        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=510,y=0,width=510,height=130)
        #third img
        img3=Image.open(r"C:\Users\Bharti Soni\Desktop\Attendance management system\college_images\Nce.jpg")
        img3=img3.resize((510,130))

        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1020,y=0,width=510,height=130)

       # background img
        img4=Image.open(r"C:\Users\Bharti Soni\Desktop\Attendance management system\college_images\bg2.jpg")
        img4=img4.resize((1530,710))

        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="Navy")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        #======================time=====================
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(title_lbl,font=('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()
        #student button
        img5=Image.open(r"C:\Users\Bharti Soni\Desktop\Attendance management system\college_images\SD3.jpg")
        img5=img5.resize((220,220))
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",20,"bold"),bg="white",fg="Navy")
        b1_1.place(x=200,y=300,width=220,height=40)
       #detect face
        img6=Image.open(r"C:\Users\Bharti Soni\Desktop\Attendance management system\college_images\FD1.jpg")
        img6=img6.resize((220,220))
        self.photoimg6=ImageTk.PhotoImage(img6)
        b1=Button(bg_img,image=self.photoimg6,command=self.face_data,cursor="hand2")
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",20,"bold"),bg="white",fg="Navy")
        b1_1.place(x=500,y=300,width=220,height=40)
        #Attendance Mangement
        img7=Image.open(r"C:\Users\Bharti Soni\Desktop\Attendance management system\college_images\attend1.jpg")
        img7=img7.resize((220,220))
        self.photoimg7=ImageTk.PhotoImage(img7)
        b1=Button(bg_img,image=self.photoimg7,command=self.attendance,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",command=self.attendance,cursor="hand2",font=("times new roman",20,"bold"),bg="white",fg="Navy")
        b1_1.place(x=800,y=300,width=220,height=40)

        #Help desk
        img8=Image.open(r"C:\Users\Bharti Soni\Desktop\Attendance management system\college_images\help.png")
        img8=img8.resize((220,220))
        self.photoimg8=ImageTk.PhotoImage(img8)
        b1=Button(bg_img,image=self.photoimg8, command=self.help_desk ,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk",command=self.help_desk,cursor="hand2",font=("times new roman",20,"bold"),bg="white",fg="Navy")
        b1_1.place(x=1100,y=300,width=220,height=40)
        # trained Data
        img9=Image.open(r"C:\Users\Bharti Soni\Desktop\Attendance management system\college_images\traind1.jpg")
        img9=img9.resize((220,220))
        self.photoimg9=ImageTk.PhotoImage(img9)
        b1=Button(bg_img,image=self.photoimg9,command=self.train_data,cursor="hand2")
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",20,"bold"),bg="white",fg="Navy")
        b1_1.place(x=200,y=580,width=220,height=40)
        # Photos 
        img10=Image.open(r"C:\Users\Bharti Soni\Desktop\Attendance management system\college_images\images.jpg")
        img10=img10.resize((220,220))
        self.photoimg10=ImageTk.PhotoImage(img10)
        b1=Button(bg_img,image=self.photoimg10,command=self.open_img,cursor="hand2")
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",20,"bold"),bg="white",fg="Navy")
        b1_1.place(x=500,y=580,width=220,height=40)
        # Developer
        img11=Image.open(r"C:\Users\Bharti Soni\Desktop\Attendance management system\college_images\dv.jpg")
        img11=img11.resize((220,220))
        self.photoimg11=ImageTk.PhotoImage(img11)
        b1=Button(bg_img,image=self.photoimg11,command=self.developer,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2" ,command=self.developer,font=("times new roman",20,"bold"),bg="white",fg="Navy")
        b1_1.place(x=800,y=580,width=220,height=40)
       # exit
        img12=Image.open(r"C:\Users\Bharti Soni\Desktop\Attendance management system\college_images\exit.jpg")
        img12=img12.resize((220,220))
        self.photoimg12=ImageTk.PhotoImage(img12)
        b1=Button(bg_img,image=self.photoimg12,command=self.IExit,cursor="hand2")
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="exit",cursor="hand2",command=self.IExit,font=("times new roman",20,"bold"),bg="white",fg="Navy")
        b1_1.place(x=1100,y=580,width=220,height=40)

    def open_img(self):
        os.startfile("data")
    def IExit(self):
        self.IExit=tkinter.messagebox.askyesno("Face Recongination","Are you sure to exit",parent=self.root)
        if self.IExit>0:
            self.root.destroy()
        else:
            return 


    # functions button

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def developer(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    def help_desk(self):
        self.new_window=Toplevel(self.root)
        self.app=HelpDesk(self.new_window)    

if  __name__ =="__main__":
    root=Tk()
    obj=Face_Recongnition_System(root)
    root.mainloop()