from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1360x760+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",28,"bold"),bg="white",fg="purple")
        title_lbl.place(x=0,y=0,width=1510,height=50)


        #full bg image 
        img_top=Image.open(r"C:\Users\Bharti Soni\Desktop\Attendance management system\college_images\Dev1.jpg")
        img_top=img_top.resize((1360,720))
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1360,height=720)


        #developer frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=850,y=0,width=600,height=720)
         
        img_frame=Image.open(r"C:\Users\Bharti Soni\Desktop\Attendance management system\college_images\Bharti.jpg")
        img_frame=img_frame.resize((200,170))
        self.photoimg_frame=ImageTk.PhotoImage(img_frame)

        f_lbl=Label(main_frame,image=self.photoimg_frame)
        f_lbl.place(x=300,y=0,width=200,height=170)
        #developer group  info
        #first 
        
        dep_label=Label(main_frame,text="Hello My name is Bharti Kumari",font=("times new roman",15,"bold"))
        dep_label.place(x=0,y=5)

        dep_label=Label(main_frame,text="I am a full stack developer",font=("times new roman",15,"bold"))
        dep_label.place(x=0,y=30)
        dep_label=Label(main_frame,text="Registration No=20105109041",font=("times new roman",15,"bold"))
        dep_label.place(x=0,y=60)
     
        #second
        img_frame2=Image.open(r"C:\Users\Bharti Soni\Desktop\Attendance management system\college_images\rishav.jpg")
        img_frame2=img_frame2.resize((200,170))
        self.photoimg_frame2=ImageTk.PhotoImage(img_frame2)

        f_lbl=Label(main_frame,image=self.photoimg_frame2)
        f_lbl.place(x=300,y=170,width=200,height=170)
        dep_label=Label(main_frame,text="Hello My name is Rishav Kumar ",font=("times new roman",15,"bold"))
        dep_label.place(x=0,y=200)

        dep_label=Label(main_frame,text="I am a full stack developer",font=("times new roman",15,"bold"))
        dep_label.place(x=0,y=230)
        dep_label1=Label(main_frame,text="Registration No=20105109013",font=("times new roman",15,"bold"))
        dep_label1.place(x=0,y=263)
       #third
        img_frame3=Image.open(r"C:\Users\Bharti Soni\Desktop\Attendance management system\college_images\mypic.jpg")
        img_frame3=img_frame3.resize((200,170))
        self.photoimg_frame3=ImageTk.PhotoImage(img_frame3)

        f_lbl=Label(main_frame,image=self.photoimg_frame3)
        f_lbl.place(x=300,y=340,width=200,height=170)
        dep_label=Label(main_frame,text="Hello My name is Simran Sania",font=("times new roman",15,"bold"))
        dep_label.place(x=0,y=400)

        dep_label=Label(main_frame,text="I am a full stack developer",font=("times new roman",15,"bold"))
        dep_label.place(x=0,y=430)
        dep_label2=Label(main_frame,text="Registration No=20105109038",font=("times new roman",15,"bold"))
        dep_label2.place(x=0,y=463)
        #fourth
        img_frame4=Image.open(r"C:\Users\Bharti Soni\Desktop\Attendance management system\college_images\mypic.jpg")
        img_frame4=img_frame4.resize((200,170))
        self.photoimg_frame4=ImageTk.PhotoImage(img_frame4)

        f_lbl=Label(main_frame,image=self.photoimg_frame4)
        f_lbl.place(x=300,y=510,width=200,height=170)
        dep_label=Label(main_frame,text="Hello My name is Mirdulla Anand",font=("times new roman",15,"bold"))
        dep_label.place(x=0,y=570)

        dep_label=Label(main_frame,text="I am a full stack developer",font=("times new roman",15,"bold"))
        dep_label.place(x=0,y=600)
        dep_label3=Label(main_frame,text="Registration No=20105109038",font=("times new roman",15,"bold"))
        dep_label3.place(x=0,y=630)
     
        









if __name__ =="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()







