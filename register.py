from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1550x810+0+0")

        #========================= text variables==================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        
        #=====================bgimage===================
        img1=Image.open(r"C:\Users\rasif\OneDrive\Desktop\HOTEL PICS FOR PROJECT\funtime.jpg")
        img1=img1.resize((1530,810),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1530,height=810)

        #=====================leftimage===================
        img2=Image.open(r"C:\Users\rasif\OneDrive\Desktop\HOTEL PICS FOR PROJECT\Your Nature.png")
        img2=img2.resize((470,550),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimg2)
        lblimg.place(x=50,y=100,width=470,height=550)

        #==========================Main frame====================
        frame=Frame(self.root,bg="white")
        frame.place(x=580,y=100,width=850,height=550)

        lbl_title=Label(self.root,text="REGISTER HERE",font=("Britannic Bold",20,"bold"),bg="white",fg="Dark green")
        lbl_title.place(x=600,y=120)

        #=====================labels and entry==============
        #======================= 1st row===========================
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=80,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("arial",12))
        fname_entry.place(x=80,y=130,width=250)

        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        lname.place(x=380,y=100)

        self.lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("arial",12))
        self.lname_entry.place(x=380,y=130,width=250) 

        #==========================2nd row============================
        contact=Label(frame,text="Contact",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=80,y=170)

        self.contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("arial",12))
        self.contact_entry.place(x=80,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white")
        email.place(x=380,y=170)

        self.email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("arial",12))
        self.email_entry.place(x=380,y=200,width=250)

        #===========================3rd Row===========================
        SecurityQ=Label(frame,text="Select Security Quetion",font=("times new roman",15,"bold"),bg="white")
        SecurityQ.place(x=80,y=240)

        self.combo_security=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("arial",12),state="readonly")
        self.combo_security["value"]=("Select","Your Birth Place Name","Your Mother's Name","Your Pet Name","Your School Name","Your Favorite Food")
        self.combo_security.current(0)
        self.combo_security.place(x=80,y=270,width=250)

        SecurityA=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
        SecurityA.place(x=380,y=240)

        self.S_answer_entry=ttk.Entry(frame,textvariable=self.var_securityA,font=("arial",12))
        self.S_answer_entry.place(x=380,y=270,width=250)
         
        #============================4th Row=========================
        Password=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        Password.place(x=80,y=310)

        self.Password_entry=ttk.Entry(frame,textvariable=self.var_pass,font=("arial",12))
        self.Password_entry.place(x=80,y=340,width=250)

        confirm=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white")
        confirm.place(x=380,y=310)

        self.confirm_entry=ttk.Entry(frame,textvariable=self.var_confpass,font=("arial",12))
        self.confirm_entry.place(x=380,y=340,width=250)

        #=================check btn===================
        self.var_check=IntVar()
        Checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree All The Terms & Conditions",font=("times new roman",12),bg="white",onvalue=1,offvalue=0)
        Checkbtn.place(x=50,y=380)

        #================btns====================
        img3=Image.open(r"C:\Users\rasif\OneDrive\Desktop\HOTEL PICS FOR PROJECT\register_btn.png")
        img3=img3.resize((180,35),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        b1=Button(frame,image=self.photoimg3,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),bg="white")
        b1.place(x=80,y=430,width=180)


        img4=Image.open(r"C:\Users\rasif\OneDrive\Desktop\HOTEL PICS FOR PROJECT\log_in btn.png")
        img4=img4.resize((180,40),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(frame,image=self.photoimg4,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),bg="white")
        b1.place(x=400,y=430,width=180)

    #=====================function declaration==================
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm Password Must Be Same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our Terms & Condition")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Moihoikela@1#",database="hotel_management")
            my_cursor=conn.cursor()
            query=("select * from register where Email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist, please try another email")
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
            messagebox.showinfo("Success","Login Now to Enter CourtYard System",parent=self.root)

            




if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()