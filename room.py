from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x560+233+237")

        #============variables=======================
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailabe=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()

        #===========title=============
        lbl_title=Label(self.root,text="ROOM BOOKINGS DETAILS",font=("Britannic Bold",20),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        
        img2=Image.open(r"C:\Users\rasif\OneDrive\Desktop\HOTEL PICS FOR PROJECT\hotel logo.png")
        img2=img2.resize((80,50),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=80,height=40)

        #======label frame=======
        LabelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Rooms & Bookings",font=("Britannic Bold",14),padx=2)
        LabelFrameleft.place(x=5,y=50,width=425,height=490)

        #====================labels and entrys====================
        # Custcontact
        lbl_cust_contact=Label(LabelFrameleft,text="Customer Contact:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(LabelFrameleft,textvariable=self.var_contact,width=20,font=("arial",12))
        entry_contact.grid(row=0,column=1,padx=5,sticky=W)

        #fetch data btn
        btnFetchData=Button(LabelFrameleft,command=self.Fetch_contact,text="Fetch Data",font=("arial",10),bg="black",fg="gold",width=7,padx=3)
        btnFetchData.place(x=345,y=4,height=25)

        #Check_in date
        check_in_date=Label(LabelFrameleft,text="Check_in_Date:",font=("arial",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)

        txtcheck_in_date=ttk.Entry(LabelFrameleft,textvariable=self.var_checkin,width=28,font=("arial",12))
        txtcheck_in_date.grid(row=1,column=1,padx=5)

        #check_out date
        Check_Out_Date=Label(LabelFrameleft,text="Check_Out_Date:",font=("arial",12,"bold"),padx=2,pady=6)
        Check_Out_Date.grid(row=2,column=0,sticky=W)

        txtCheck_out_Date=ttk.Entry(LabelFrameleft,textvariable=self.var_checkout,width=28,font=("arial",12))
        txtCheck_out_Date.grid(row=2,column=1,padx=5)

        #room ComboBox
        label_RoomType=Label(LabelFrameleft,text="Room Type:",font=("arial",12,"bold"),padx=2,pady=6)
        label_RoomType.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="Moihoikela@1#",database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute("Select RoomType from details")
        ide=my_cursor.fetchall()

        combo_RoomType=ttk.Combobox(LabelFrameleft,textvariable=self.var_roomtype,font=("arial",12),width=26,state="readonly")
        combo_RoomType["value"]=ide
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)

        # Available Room
        lblRoomAvailable=Label(LabelFrameleft,text="Available Room:",font=("arial",12,"bold"),padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="Moihoikela@1#",database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute("Select RoomNo from details")
        rows=my_cursor.fetchall()

        combo_RoomNo=ttk.Combobox(LabelFrameleft,textvariable=self.var_roomavailabe,font=("arial",12),width=26,state="readonly")
        combo_RoomNo["value"]=rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4,column=1)
        

        #meal
        lbl_meal=Label(LabelFrameleft,text="Meal:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_meal.grid(row=5,column=0,sticky=W)

        combo_nationality=ttk.Combobox(LabelFrameleft,textvariable=self.var_meal,font=("arial",12),width=26,state="readonly")
        combo_nationality["value"]=("BreakFast","Lunch","Dinner")
        combo_nationality.current(0)
        combo_nationality.grid(row=5,column=1,padx=5)

        #no of days
        lbl_NoOfDays=Label(LabelFrameleft,text="No Of Days:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_NoOfDays.grid(row=6,column=0,sticky=W)

        txtNoOfDays=ttk.Entry(LabelFrameleft,textvariable=self.var_noofdays,width=28,font=("arial",12))
        txtNoOfDays.grid(row=6,column=1,padx=5)

        # paid tax
        lbl_paidtax=Label(LabelFrameleft,text="Paid Tax:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_paidtax.grid(row=7,column=0,sticky=W)

        txtpaidtax=ttk.Entry(LabelFrameleft,textvariable=self.var_paidtax,width=28,font=("arial",12))
        txtpaidtax.grid(row=7,column=1,padx=5)

        # Sub Total
        lbl_sub_total=Label(LabelFrameleft,text="Sub Total:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_sub_total.grid(row=8,column=0,sticky=W)

        txtsub_total=ttk.Entry(LabelFrameleft,textvariable=self.var_actualtotal,width=28,font=("arial",12))
        txtsub_total.grid(row=8,column=1,padx=5)

        #total cost
        lbl_total_cost=Label(LabelFrameleft,text="Total Cost",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_total_cost.grid(row=9,column=0,sticky=W)

        txttotal_cost=ttk.Entry(LabelFrameleft,textvariable=self.var_total,width=28,font=("arial",12))
        txttotal_cost.grid(row=9,column=1,padx=5)

        #===============bill btn=================
        btnBill=Button(LabelFrameleft,text="Bill",command=self.total,font=("arial",12),bg="black",fg="gold",width=10,padx=3)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)
        #==================btns===================
        btn_frame=Frame(LabelFrameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=417,height=35)

        btnadd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12),bg="black",fg="gold",width=10,padx=3)
        btnadd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12),bg="black",fg="gold",width=10,padx=3)
        btnupdate.grid(row=0,column=1,padx=1)

        btndelete=Button(btn_frame,text="Delete",command=self.delete_room,font=("arial",12),bg="black",fg="gold",width=10,padx=3)
        btndelete.grid(row=0,column=2,padx=1)

        btnreset=Button(btn_frame,text="Reset",command=self.reset_data,font=("arial",12),bg="black",fg="gold",width=10,padx=3)
        btnreset.grid(row=0,column=3,padx=1)

        #==============right side img====================
        img3=Image.open(r"C:\Users\rasif\OneDrive\Desktop\HOTEL PICS FOR PROJECT\rightsideimage.jpg")
        img3=img3.resize((530,280),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=760,y=55,width=530,height=280)

        #=================table frame search system=================
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Customer details And Search System",font=("Britannic Bold",14),padx=2)
        table_frame.place(x=435,y=280,width=855,height=260)

        lbl_SearchBy=Label(table_frame,text="Search By",font=("arial",12,"bold"),bg="red",fg="white")
        lbl_SearchBy.grid(row=0,column=0,sticky=W,padx=5)


        self.search_var=StringVar()
        combo_Search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("arial",12),width=24,state="readonly")
        combo_Search["value"]=("Contact","Room")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=5)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(table_frame,textvariable=self.txt_search,width=24,font=("arial",12))
        txtSearch.grid(row=0,column=2,padx=5)

        btnSearch=Button(table_frame,text="Search",command=self.search,font=("arial",10),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=5)

        btnshowall=Button(table_frame,text="Show All",command=self.fetch_data,font=("arial",10),bg="black",fg="gold",width=10)
        btnshowall.grid(row=0,column=4,padx=5)

        #================Show Details============
        Details_table=Frame(table_frame,bd=2,relief=RIDGE)
        Details_table.place(x=0,y=50,width=850,height=180)

        Scroll_x=ttk.Scrollbar(Details_table,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(Details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(Details_table,columns=("Contact","Checkin","Checkout","Roomtype","Roomavailable","Meal","NoOfDays",),xscrollcommand=Scroll_x,yscrollcommand=Scroll_y)
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.room_table.xview)
        Scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("Contact",text="Contact")
        self.room_table.heading("Checkin",text="Check_in_Date")
        self.room_table.heading("Checkout",text="Check_Out_Date")
        self.room_table.heading("Roomtype",text="Room Type")
        self.room_table.heading("Roomavailable",text="Room No")
        self.room_table.heading("Meal",text="Meal")
        self.room_table.heading("NoOfDays",text="No_Of_Days")
        
        self.room_table["show"]="headings"

        self.room_table.column("Contact",width=100)
        self.room_table.column("Checkin",width=100)
        self.room_table.column("Checkout",width=100)
        self.room_table.column("Roomtype",width=100)
        self.room_table.column("Roomavailable",width=100)
        self.room_table.column("Meal",width=100)
        self.room_table.column("NoOfDays",width=100)
        
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

        #==========add data=================

    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All fillings are requaired",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Moihoikela@1#",database="hotel_management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_contact.get(),
                                                                                    self.var_checkin.get(),
                                                                                    self.var_checkout.get(),
                                                                                    self.var_roomtype.get(),
                                                                                    self.var_roomavailabe.get(),
                                                                                    self.var_meal.get(),
                                                                                    self.var_noofdays.get()
                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Room Has Been Booked Successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"Some thing went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Moihoikela@1#",database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
            conn.close()

    #================Get Cursor=================

    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailabe.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])

    #==================update======================

    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter Contact Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Moihoikela@1#",database="hotel_management")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set Check_in=%s,Check_out=%s,RoomType=%s,RoomAvailable=%s,Meal=%s,NoOfDays=%s where Contact=%s",(
                                                                                                                                            
                                                                                                                                            self.var_checkin.get(),
                                                                                                                                            self.var_checkout.get(),
                                                                                                                                            self.var_roomtype.get(),
                                                                                                                                            self.var_roomavailabe.get(),
                                                                                                                                            self.var_meal.get(),
                                                                                                                                            self.var_noofdays.get(),
                                                                                                                                            self.var_contact.get() 
                                                                                                                                        ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated",parent=self.root)
    
    #=======================delete=========================

    def delete_room(self):
        delete=messagebox.askyesno("System Querry","Do you want to delete this Room details ?",parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Moihoikela@1#",database="hotel_management")
            my_cursor=conn.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    #=======================reset=============================

    def reset_data(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailabe.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set(""),
        self.var_paidtax.set(""),
        self.var_actualtotal.set(""),
        self.var_total.set("")


    #======================all data fetch========================

    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter contact Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Moihoikela@1#",database="hotel_management")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

        if row==None:
            messagebox.showerror("Error","This number is not found",parent=self.root)
        else:
            conn.commit()
            conn.close()

            showDataFrame=Frame(self.root,bd=4,relief=RIDGE,padx=2)
            showDataFrame.place(x=450,y=55,width=300,height=180)

            lblName=Label(showDataFrame,text="Name:",font=("arial",12,"bold"))
            lblName.place(x=0,y=0)

            lbldata=Label(showDataFrame,text=row,font=("arial",10,"bold"))
            lbldata.place(x=90,y=0)

            #=====================Gender===================

            conn=mysql.connector.connect(host="localhost",username="root",password="Moihoikela@1#",database="hotel_management")
            my_cursor=conn.cursor()
            query=("select Gender from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            lblgender=Label(showDataFrame,text="Gender:",font=("arial",12,"bold"))
            lblgender.place(x=0,y=30)

            lbldata1=Label(showDataFrame,text=row,font=("arial",10,"bold"))
            lbldata1.place(x=90,y=30)

            #========================Email==========================

            conn=mysql.connector.connect(host="localhost",username="root",password="Moihoikela@1#",database="hotel_management")
            my_cursor=conn.cursor()
            query=("select Email from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            lblemail=Label(showDataFrame,text="Email:",font=("arial",12,"bold"))
            lblemail.place(x=0,y=60)

            lbldata2=Label(showDataFrame,text=row,font=("arial",10,"bold"))
            lbldata2.place(x=90,y=60)

            #=====================Nationality=====================

            conn=mysql.connector.connect(host="localhost",username="root",password="Moihoikela@1#",database="hotel_management")
            my_cursor=conn.cursor()
            query=("select Nationality from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            lblnationality=Label(showDataFrame,text="Nationality:",font=("arial",12,"bold"))
            lblnationality.place(x=0,y=90)

            lbldata3=Label(showDataFrame,text=row,font=("arial",10,"bold"))
            lbldata3.place(x=90,y=90)

            #======================Address====================

            conn=mysql.connector.connect(host="localhost",username="root",password="Moihoikela@1#",database="hotel_management")
            my_cursor=conn.cursor()
            query=("select Address from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            lbladdress=Label(showDataFrame,text="Address:",font=("arial",12,"bold"))
            lbladdress.place(x=0,y=120)

            lbldata4=Label(showDataFrame,text=row,font=("arial",10,"bold"))
            lbldata4.place(x=90,y=120)

    #==============Search System==============
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Moihoikela@1#",database="hotel_management")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)

        if (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Single"):
            q1=float(200)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            

        elif (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Double"):
            q1=float(200)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Luxury"):
            q1=float(300)
            q2=float(1200)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Deluxe"):
            q1=float(300)
            q2=float(1400)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Duplex"):
            q1=float(400)
            q2=float(1800)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Sweets"):
            q1=float(400)
            q2=float(2000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Single"):
            q1=float(400)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Double"):
            q1=float(400)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Luxury"):
            q1=float(600)
            q2=float(1200)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Deluxe"):
            q1=float(600)
            q2=float(1400)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Duplex"):
            q1=float(800)
            q2=float(1800)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Sweets"):
            q1=float(800)
            q2=float(2000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Double"):
            q1=float(300)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Luxury"):
            q1=float(400)
            q2=float(1200)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Deluxe"):
            q1=float(400)
            q2=float(1400)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Duplex"):
            q1=float(550)
            q2=float(1800)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Sweets"):
            q1=float(600)
            q2=float(2000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        

        

if __name__ == "__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()