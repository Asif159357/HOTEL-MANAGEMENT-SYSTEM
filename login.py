from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from customer import Cust_Win
from room import Roombooking
from details import DetailsRoom
from Hotel import HotelManagementSystem



def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management")
        self.root.geometry("1550x810+0+0")

        self.var_email=StringVar()
        self.var_pass=StringVar()


        img1=Image.open(r"C:\Users\rasif\OneDrive\Desktop\HOTEL PICS FOR PROJECT\hotel1.jpg")
        img1=img1.resize((1530,810),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1530,height=810)

        frame=Frame(self.root,bg="black",bd=5)
        frame.place(x=610,y=170,width=340,height=450)

        img2=Image.open(r"C:\Users\rasif\OneDrive\Desktop\HOTEL PICS FOR PROJECT\PP_logo-removebg.png")
        img2=img2.resize((100,100),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimg2,bg="black",borderwidth=0)
        lblimg.place(x=735,y=170,width=100,height=100)

        get_str=Label(frame,text="Get started",font=("times new roman",20,"bold"),fg="gold",bg="black")
        get_str.place(x=100,y=85)


        #====================Labels====================
        username=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=60,y=135)

        self.txtuser=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txtuser.place(x=30,y=170,width=270)

        password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=60,y=220)

        self.txtpass=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"),show='*')
        self.txtpass.place(x=30,y=255,width=270)

        #=======================Icon Images=====================
        img3=Image.open(r"C:\Users\rasif\OneDrive\Desktop\HOTEL PICS FOR PROJECT\user icon.png")
        img3=img3.resize((25,25),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg=Label(self.root,image=self.photoimg3,bg="black",borderwidth=0)
        lblimg.place(x=650,y=312,width=25,height=25)

        img4=Image.open(r"C:\Users\rasif\OneDrive\Desktop\HOTEL PICS FOR PROJECT\Password_icon.png")
        img4=img4.resize((22,22),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        lblimg=Label(self.root,image=self.photoimg4,bg="black",borderwidth=0)
        lblimg.place(x=650,y=400,width=22,height=22)

        #================Login btns=================
        loginbtn=Button(frame,command=self.login,text="Login",font=("arial",15,"bold"),cursor="hand2",bd=3,relief=RAISED,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=100,y=310,width=120,height=30)

        #================register btn===============
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("arial",10),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=10,y=355,width=120)

        #===================Forgot btn================
        forgotbtn=Button(frame,text="Forgot Password ?",command=self.forgot_password_window,font=("arial",10),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgotbtn.place(x=11,y=380,width=120)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
        

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All Feilds Required !",parent=self.root)
        elif self.txtuser.get()=="TSO_ASIF" and self.txtpass.get()=="asif123":
            messagebox.showinfo("Success","Welcome To COURTYARD management system")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Moihoikela@1#",database="hotel_management")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where Email=%s and Password=%s",(
                                                                                self.var_email.get(),
                                                                                self.var_pass.get()                                                                                
                                                                            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username Or Password")
            else:
                open_main=messagebox.askyesno("YesNo","Are You An Admin?")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    #========================reset password======================
    def reset_pass(self):
        if self.combo_security.get()=="Select":
            messagebox.showerror("Error","Select Security Quetion",parent=self.root2)
        elif self.S_answer_entry.get()=="":
            messagebox.showerror("Error","Please Enter The Answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please Enter The New Password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Moihoikela@1#",database="hotel_management")
            my_cursor=conn.cursor()
            query=("select * from register where Email=%s and SecurityQ=%s and SecurityA=%s")
            value=(self.txtuser.get(),self.combo_security.get(),self.S_answer_entry.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter Currect Answer",parent=self.root2)
            else:
                query2=("update register set Password=%s where Email=%s")
                value2=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query2,value2)

                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Your Password Has Been Reset,Please LogIn With New Password",parent=self.root2)
                self.root2.destroy()

    #==========================forgot password window=====================

    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter The Email Address")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Moihoikela@1#",database="hotel_management")
            my_cursor=conn.cursor()
            query=("select * from register where Email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter The Valid User Name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")


                lbl=Label(self.root2,text="Forgot Password",font=("times new roman",20),borderwidth=0,fg="red",bg="white")
                lbl.place(x=0,y=10,relwidth=1)

                SecurityQ=Label(self.root2,text="Select Security Quetion",font=("times new roman",15,"bold"),bg="white")
                SecurityQ.place(x=50,y=80)

                self.combo_security=ttk.Combobox(self.root2,font=("arial",12),state="readonly")
                self.combo_security["value"]=("Select","Your Birth Place Name","Your Mother's Name","Your Pet Name","Your School Name","Your Favorite Food")
                self.combo_security.current(0)
                self.combo_security.place(x=50,y=120,width=250)

                SecurityA=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
                SecurityA.place(x=50,y=160)

                self.S_answer_entry=ttk.Entry(self.root2,font=("arial",12))
                self.S_answer_entry.place(x=50,y=200,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white")
                new_password.place(x=50,y=240)

                self.txt_newpass=ttk.Entry(self.root2,font=("arial",12))
                self.txt_newpass.place(x=50,y=280,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",12,"bold"),fg="white",bg="green")
                btn.place(x=115,y=320,width=100)


            


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
        b1=Button(frame,image=self.photoimg4,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),bg="white")
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
                                                                                    self.var_pass.get(),
                                                                                    self.var_securityQ.get(),
                                                                                    self.var_securityA.get(),
                                                                                    self.var_email.get()
                                                                                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Login Now to Enter CourtYard System")
    
    def return_login(self):
        self.root.destroy()



class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        #first image
        img1=Image.open(r"C:\Users\rasif\OneDrive\Desktop\HOTEL PICS FOR PROJECT\hotel1.jpg")
        img1=img1.resize((1550,150),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=150)

        #===========logo============
        img2=Image.open(r"C:\Users\rasif\OneDrive\Desktop\HOTEL PICS FOR PROJECT\hotel logo.png")
        img2=img2.resize((250,150),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=250,height=150)

        #============title============
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("Britannic Bold",40,),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=150,width=1550,height=50)


        #=================main frame==============
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=200,width=1550,height=620)


        #=================menu=========================
        lbl_menu=Label(main_frame,text="MENU",font=("Britannic Bold",20,),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

        #=================btn frame==============
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=148)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("Britannic Bold",14,),bg="black",fg="gold",bd=0,cursor="hand2")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="ROOM",command=self.roombooking,width=22,font=("Britannic Bold",14,),bg="black",fg="gold",bd=0,cursor="hand2")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text="DETAILS",command=self.detailsroom,width=22,font=("Britannic Bold",14,),bg="black",fg="gold",bd=0,cursor="hand2")
        details_btn.grid(row=2,column=0,pady=1)
        
        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=22,font=("Britannic Bold",14,),bg="black",fg="gold",bd=0,cursor="hand2")
        logout_btn.grid(row=3,column=0,pady=1)


        #=========================== right side image===================
        img3=Image.open(r"C:\Users\rasif\OneDrive\Desktop\HOTEL PICS FOR PROJECT\rightsidepic.jpg")
        img3=img3.resize((1310,595),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1310,height=595)

        #============= extra images=================
        img4=Image.open(r"C:\Users\rasif\OneDrive\Desktop\HOTEL PICS FOR PROJECT\hotel in evening.jpg")
        img4=img4.resize((230,205),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg2=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg2.place(x=0,y=180,width=230,height=205)

        img5=Image.open(r"C:\Users\rasif\OneDrive\Desktop\HOTEL PICS FOR PROJECT\cook.jpg")
        img5=img5.resize((230,210),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg3=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg3.place(x=0,y=385,width=230,height=210)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)
    
    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)

    def detailsroom(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)

    def logout(self):
        self.root.destroy()

    


if __name__=="__main__":
    main()