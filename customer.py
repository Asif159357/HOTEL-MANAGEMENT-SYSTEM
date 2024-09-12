from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox



class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x560+233+237")

        #=============variables===================
        self.var_ref=StringVar()
        x=random.randint(100,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_fathers_name=StringVar()
        self.var_gender=StringVar()
        self.var_zipcode=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_idproof=StringVar()
        self.var_idnumber=StringVar()
        self.var_address=StringVar()



        #===========title=============
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("Britannic Bold",20),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        
        img2=Image.open(r"C:\Users\rasif\OneDrive\Desktop\HOTEL PICS FOR PROJECT\hotel logo.png")
        img2=img2.resize((80,50),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=80,height=40)

        #======label frame=======
        LabelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("Britannic Bold",14),padx=2)
        LabelFrameleft.place(x=5,y=50,width=425,height=490)


        #====================labels and entrys====================
        # Custref
        lbl_cust_ref=Label(LabelFrameleft,text="Customer Ref",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(LabelFrameleft,textvariable=self.var_ref,width=28,font=("arial",12),state="readonly")
        entry_ref.grid(row=0,column=1,padx=5)

        #CustName
        cust_name=Label(LabelFrameleft,text="Customer Name",font=("arial",12,"bold"),padx=2,pady=6)
        cust_name.grid(row=1,column=0,sticky=W)

        textCname=ttk.Entry(LabelFrameleft,textvariable=self.var_cust_name,width=28,font=("arial",12))
        textCname.grid(row=1,column=1,padx=5)

        # fathers name
        fathers_name=Label(LabelFrameleft,text="Father's Name",font=("arial",12,"bold"),padx=2,pady=6)
        fathers_name.grid(row=2,column=0,sticky=W)

        textFname=ttk.Entry(LabelFrameleft,textvariable=self.var_fathers_name,width=28,font=("arial",12))
        textFname.grid(row=2,column=1,padx=5)

        #Gender ComboBox
        lbl_gender=Label(LabelFrameleft,text="Gender",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(LabelFrameleft,textvariable=self.var_gender,font=("arial",12),width=26,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

        # Postel Code
        lbl_post_code=Label(LabelFrameleft,text="Zip Code",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_post_code.grid(row=4,column=0,sticky=W)

        txtpostcode=ttk.Entry(LabelFrameleft,textvariable=self.var_zipcode,width=28,font=("arial",12))
        txtpostcode.grid(row=4,column=1,padx=5)

        #mobile number
        lbl_mobile=Label(LabelFrameleft,text="Mobile No",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_mobile.grid(row=5,column=0,sticky=W)

        txtmobile=ttk.Entry(LabelFrameleft,textvariable=self.var_mobile,width=28,font=("arial",12))
        txtmobile.grid(row=5,column=1,padx=5)

        # email
        lbl_email=Label(LabelFrameleft,text="Email",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_email.grid(row=6,column=0,sticky=W)

        txtemail=ttk.Entry(LabelFrameleft,textvariable=self.var_email,width=28,font=("arial",12))
        txtemail.grid(row=6,column=1,padx=5)

        # Nationality
        lbl_nationality=Label(LabelFrameleft,text="Nationality",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_nationality.grid(row=7,column=0,sticky=W)

        combo_nationality=ttk.Combobox(LabelFrameleft,textvariable=self.var_nationality,font=("arial",12),width=26,state="readonly")
        combo_nationality["value"]=("Indian","Pakistani","Bangladeshi","Nepali","Bhutani","shilankan","American","British","African","indonasian")
        combo_nationality.current(0)
        combo_nationality.grid(row=7,column=1)

        #==========id proof type combobox===========
        lbl_id_proof=Label(LabelFrameleft,text="Id Proof",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_id_proof.grid(row=8,column=0,sticky=W)

        combo_idproof=ttk.Combobox(LabelFrameleft,textvariable=self.var_idproof,font=("arial",12),width=26,state="readonly")
        combo_idproof["value"]=("Adhar Card","Pan Card","Driving Licence","Passport","Voter Id")
        combo_idproof.current(0)
        combo_idproof.grid(row=8,column=1)


        #id number
        lbl_id_num=Label(LabelFrameleft,text="Id Number",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_id_num.grid(row=9,column=0,sticky=W)

        txtidname=ttk.Entry(LabelFrameleft,textvariable=self.var_idnumber,width=28,font=("arial",12))
        txtidname.grid(row=9,column=1,padx=5)

        # Address
        lbl_address=Label(LabelFrameleft,text="Address",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_address.grid(row=10,column=0,sticky=W)

        txtadddress=ttk.Entry(LabelFrameleft,textvariable=self.var_address,width=28,font=("arial",12))
        txtadddress.grid(row=10,column=1,padx=5)

        #==================btns===================
        btn_frame=Frame(LabelFrameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=417,height=35)

        btnadd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12),bg="black",fg="gold",width=10,padx=3)
        btnadd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12),bg="black",fg="gold",width=10,padx=3)
        btnupdate.grid(row=0,column=1,padx=1)

        btndelete=Button(btn_frame,text="Delete",command=self.delete_details,font=("arial",12),bg="black",fg="gold",width=10,padx=3)
        btndelete.grid(row=0,column=2,padx=1)

        btnreset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12),bg="black",fg="gold",width=10,padx=3)
        btnreset.grid(row=0,column=3,padx=1)

        #=================table frame search system=================
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Customer details And Search System",font=("Britannic Bold",14),padx=2)
        table_frame.place(x=435,y=50,width=855,height=490)

        lbl_SearchBy=Label(table_frame,text="Search By",font=("arial",12,"bold"),bg="red",fg="white")
        lbl_SearchBy.grid(row=0,column=0,sticky=W,padx=5)


        self.search_var=StringVar()
        combo_Search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("arial",12),width=24,state="readonly")
        combo_Search["value"]=("Mobile","Ref")
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
        Details_table.place(x=0,y=50,width=850,height=350)

        Scroll_x=ttk.Scrollbar(Details_table,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(Details_table,orient=VERTICAL)

        self.cust_details_table=ttk.Treeview(Details_table,columns=("ref","name","fname","gender","zipcode","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=Scroll_x,yscrollcommand=Scroll_y)
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.cust_details_table.xview)
        Scroll_y.config(command=self.cust_details_table.yview)

        self.cust_details_table.heading("ref",text="Refer No")
        self.cust_details_table.heading("name",text="Customer Name")
        self.cust_details_table.heading("fname",text="Fathers Name")
        self.cust_details_table.heading("gender",text="Gender")
        self.cust_details_table.heading("zipcode",text="Postal Code")
        self.cust_details_table.heading("mobile",text="Mobile No")
        self.cust_details_table.heading("email",text="Email")
        self.cust_details_table.heading("nationality",text="Nationality")
        self.cust_details_table.heading("idproof",text="Id Proof")
        self.cust_details_table.heading("idnumber",text="Id Number")
        self.cust_details_table.heading("address",text="Address")

        self.cust_details_table["show"]="headings"

        self.cust_details_table.column("ref",width=100)
        self.cust_details_table.column("name",width=100)
        self.cust_details_table.column("fname",width=100)
        self.cust_details_table.column("gender",width=100)
        self.cust_details_table.column("zipcode",width=100)
        self.cust_details_table.column("mobile",width=100)
        self.cust_details_table.column("email",width=100)
        self.cust_details_table.column("nationality",width=100)
        self.cust_details_table.column("idproof",width=100)
        self.cust_details_table.column("idnumber",width=100)
        self.cust_details_table.column("address",width=100)

        self.cust_details_table.pack(fill=BOTH,expand=1)
        self.cust_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_mobile.get()=="" or self.var_fathers_name.get()=="":
            messagebox.showerror("Error","All fillings are requaired",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Moihoikela@1#",database="hotel_management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_ref.get(),
                                                                                    self.var_cust_name.get(),
                                                                                    self.var_fathers_name.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_zipcode.get(),
                                                                                    self.var_mobile.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_nationality.get(),
                                                                                    self.var_idproof.get(),
                                                                                    self.var_idnumber.get(),
                                                                                    self.var_address.get()
                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"Some thing went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Moihoikela@1#",database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("",END,values=i)
            conn.commit()
            conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.cust_details_table.focus()
        content=self.cust_details_table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_fathers_name.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_zipcode.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_idproof.set(row[8]),
        self.var_idnumber.set(row[9]),
        self.var_address.set(row[10])

    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please Enter Mobile Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Moihoikela@1#",database="hotel_management")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Name=%s,Fname=%s,Gender=%s,Zipcode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where Ref=%s",(
                                                                                                                                                                self.var_cust_name.get(),
                                                                                                                                                                self.var_fathers_name.get(),
                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                self.var_zipcode.get(),
                                                                                                                                                                self.var_mobile.get(),
                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                self.var_nationality.get(),
                                                                                                                                                                self.var_idproof.get(),
                                                                                                                                                                self.var_idnumber.get(),
                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                self.var_ref.get()
                                                                                                                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated",parent=self.root)

    def delete_details(self):
        delete_details=messagebox.askyesno("System Querry","Do you want to delete this customer details ?",parent=self.root)
        if delete_details>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Moihoikela@1#",database="hotel_management")
            my_cursor=conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete_details:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_cust_name.set(""),
        self.var_fathers_name.set(""),
        self.var_zipcode.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        self.var_idnumber.set(""),
        self.var_address.set("")

        x=random.randint(100,9999)
        self.var_ref.set(str(x))


    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Moihoikela@1#",database="hotel_management")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()


        



if __name__ == "__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()