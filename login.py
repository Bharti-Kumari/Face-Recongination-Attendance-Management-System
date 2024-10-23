from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk        #pip install pillow
from tkinter import messagebox
import mysql.connector
from main import Face_Recongnition_System
from register import Register

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()



class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1360x760+0+0")
        self.root.title("Login")
        #first img
        img1=Image.open(r"C:\Users\Bharti Soni\Desktop\Attendance management system\college_images\A1.jpg")
        img1=img1.resize((510,200))

        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=510,height=200)
        #second img
        img2=Image.open(r"C:\Users\Bharti Soni\Desktop\Attendance management system\college_images\A2.jpg")
        img2=img2.resize((510,200))

        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=510,y=0,width=510,height=200)
        #third img
        img3=Image.open(r"C:\Users\Bharti Soni\Desktop\Attendance management system\college_images\A3.jpg")
        img3=img3.resize((510,200))

        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1020,y=0,width=510,height=200)

       # background img
        img4=Image.open(r"C:\Users\Bharti Soni\Desktop\Attendance management system\college_images\AM1.jpg")
        img4=img4.resize((1530,710))

        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=200,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="Navy")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #frame of login window
        frame=Frame(self.root,bg="#6fb0fc")
        frame.place(x=600,y=250,width=360,height=450)
        imgL=Image.open(r"C:\Users\Bharti Soni\Desktop\Attendance management system\college_images\icon.jpg")
        imgL=imgL.resize((100,90))
        self.photoimgL=ImageTk.PhotoImage(imgL)

        lblimgL=Label(image=self.photoimgL,bg="#6fb0fc",borderwidth=0)
        lblimgL.place(x=735,y=250,width=100,height=90)

       

        get_str_label=Label(frame,text="Get Started",font=("times new roman",22,"bold"),fg="white",bg="#6fb0fc")
        get_str_label.place(x=110,y=90)


        username=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="#6fb0fc")
        username.place(x=50,y=145)
        self.txtuser=ttk.Entry(frame,width=30,font=("times new roman",12,"bold"))
        self.txtuser.place(x=54,y=175,width=270)


        password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="#6fb0fc")
        password.place(x=50,y=215)
        self.txtpass=ttk.Entry(frame,width=30,font=("times new roman",12,"bold"))
        self.txtpass.place(x=54,y=245,width=270)

        #button
        #login button
        Login_btn=Button(frame,text="Login",command=self.login,font=("times new roman",13,"bold"),bd=3,relief=RIDGE,fg="white",bg="#233a8c",activeforeground="white",activebackground="white")
        Login_btn.place(x=110,y=300,width=120,height=40)

        #register button
        register_btn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",13,"bold"),borderwidth=0,fg="white",bg="#233a8c",activeforeground="white",activebackground="white")
        register_btn.place(x=0,y=350,width=160)

        #forgot password button
        register_btn=Button(frame,text="Forget Password",font=("times new roman",13,"bold"),borderwidth=0,fg="white",bg="#233a8c",activeforeground="white",activebackground="white")
        register_btn.place(x=0,y=380,width=160)


    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="Simran" and self.txtpass.get()=="123456":
            messagebox.showinfo("Success","welcome to nce face recognition attendance system")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Kittu@123",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(

                                                                                        self.var_email.get(),
                                                                                        self.var_pass.get()
                                                                                        ))
            
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","invalid username and password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.new_window)
                    self.app=Face_Recongnition_System(self.new_window)  
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()















if __name__=="__main__":
    main()
 