from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk        #pip install pillow
from tkinter import messagebox
import mysql.connector



class Register:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1360x760+0+0")
        self.root.title("Register")

        #===============variables================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


        #image background 
        img=Image.open(r"C:\Users\Bharti Soni\Desktop\Attendance management system\college_images\A1.jpg")
        img=img.resize((1360,760))
        self.photoimg=ImageTk.PhotoImage(img)

        lbl_bg=Label(self.root,image=self.photoimg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)


        #=================left image==============
        #image background 
        img1=Image.open(r"C:\Users\Bharti Soni\Desktop\Attendance management system\college_images\R2.jpg")
        img1=img1.resize((470,620))
        self.photoimg1=ImageTk.PhotoImage(img1)

        lbl_bg=Label(self.root,image=self.photoimg1)
        lbl_bg.place(x=50,y=70,width=470,height=620)

        #frame of register window
        frame=Frame(self.root,bg="Navy")
        frame.place(x=520,y=70,width=800,height=620)

        register_label=Label(frame,text="Register Here",font=("times new roman",20,"bold"),bg="#6fb0fc",fg="white")
        register_label.place(x=20,y=20)

        #=================Labels and entry fields===================
        #---------row1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),fg="white",bg="#6fb0fc")
        fname.place(x=50,y=100)
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),fg="white",bg="#6fb0fc")
        lname.place(x=370,y=100)
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)


        #=========row2========
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),fg="white",bg="#6fb0fc")
        contact.place(x=50,y=185)
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=50,y=215,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),fg="white",bg="#6fb0fc")
        email.place(x=370,y=185)
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_email.place(x=370,y=215,width=250)


        #=========row3========
        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),fg="white",bg="#6fb0fc")
        security_Q.place(x=50,y=270)
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("select","your birth place","your school name","your favourite color","your favourite food")
        self.combo_security_Q.place(x=50,y=300,width=250)
        self.combo_security_Q.current(0)


        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),fg="white",bg="#6fb0fc")
        security_A.place(x=370,y=270)
        self.txt_security_A=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.txt_security_A.place(x=370,y=300,width=250)


        #=========row4=========
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="#6fb0fc")
        pswd.place(x=50,y=350)
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txt_pswd.place(x=50,y=380,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),fg="white",bg="#6fb0fc")
        confirm_pswd.place(x=370,y=350)
        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.txt_confirm_pswd.place(x=370,y=380,width=250)


        #===================checkbutton=================
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree to The Terms and Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=430)


        #=====================buttons=============
        img3=Image.open(r"C:\Users\Bharti Soni\Desktop\Attendance management system\college_images\L1.jpg")
        img3=img3.resize((200,55))
        self.photoimg3=ImageTk.PhotoImage(img3)
        b1=Button(frame,image=self.photoimg3,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",13,"bold"),fg="white")
        b1.place(x=50,y=480,width=200)


        img4=Image.open(r"C:\Users\Bharti Soni\Desktop\Attendance management system\college_images\R1.jpg")
        img4=img4.resize((200,55))
        self.photoimg4=ImageTk.PhotoImage(img4)
        b2=Button(frame,image=self.photoimg4,borderwidth=0,cursor="hand2",font=("times new roman",13,"bold"),fg="white")
        b2.place(x=370,y=480,width=200)


    #==================function declarations=============
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password are not same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree to our terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Kittu@123",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exists,please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(

                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()
                                                                                        
                                                                                        ))  
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")








if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()
    