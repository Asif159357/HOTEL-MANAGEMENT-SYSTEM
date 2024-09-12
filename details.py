from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x560+233+237")


        #===========title=============
        lbl_title=Label(self.root,text="ROOM ADDING SYSTEM",font=("Britannic Bold",20),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        
        img2=Image.open(r"C:\Users\rasif\OneDrive\Desktop\HOTEL PICS FOR PROJECT\hotel logo.png")
        img2=img2.resize((80,50),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=80,height=40)

        #======label frame=======
        LabelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("Britannic Bold",14),padx=2)
        LabelFrameleft.place(x=5,y=50,width=540,height=350)

        # Floor
        lbl_floor=Label(LabelFrameleft,text="Floor:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)

        self.var_floor=StringVar()
        entry_floor=ttk.Entry(LabelFrameleft,textvariable=self.var_floor,width=24,font=("arial",12))
        entry_floor.grid(row=0,column=1,padx=5,sticky=W)

        #Room No
        lbl_RoomNo=Label(LabelFrameleft,text="Room No:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W)

        self.var_roomNo=StringVar()
        entry_RoomNo=ttk.Entry(LabelFrameleft,textvariable=self.var_roomNo,width=24,font=("arial",12))
        entry_RoomNo.grid(row=1,column=1,padx=5,sticky=W)

        #Room Type
        lbl_RoomType=Label(LabelFrameleft,text="Room Type:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W)

        self.var_RoomType=StringVar()
        self.search_var=StringVar()
        combo_Search=ttk.Combobox(LabelFrameleft,textvariable=self.var_RoomType,font=("arial",12),width=22,state="readonly")
        combo_Search["value"]=("Single","Double","Luxury","Deluxe","Duplex","Sweets")
        combo_Search.current(0)
        combo_Search.grid(row=2,column=1,padx=5,sticky=W)

        #=======================BTNS=============================
        btn_frame=Frame(LabelFrameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=417,height=35)

        btnadd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12),bg="black",fg="gold",width=10,padx=3)
        btnadd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12),bg="black",fg="gold",width=10,padx=3)
        btnupdate.grid(row=0,column=1,padx=5)

        btndelete=Button(btn_frame,text="Delete",command=self.delete_room,font=("arial",12),bg="black",fg="gold",width=10,padx=3)
        btndelete.grid(row=0,column=2,padx=1)

        btnreset=Button(btn_frame,text="Reset",command=self.reset_data,font=("arial",12),bg="black",fg="gold",width=10,padx=3)
        btnreset.grid(row=0,column=3,padx=1)

        #=================table frame search system=================
        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Rooms Details",font=("Britannic Bold",14),padx=2)
        Table_frame.place(x=580,y=50,width=650,height=350)

        Scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.room_table=ttk.Treeview(Table_frame,columns=("floor","roomno","roomtype"),xscrollcommand=Scroll_x,yscrollcommand=Scroll_y)
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.room_table.xview)
        Scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomno",text="Room No")
        self.room_table.heading("roomtype",text="Room Type")
        
        self.room_table["show"]="headings"

        self.room_table.column("floor",width=100)
        self.room_table.column("roomno",width=100)
        self.room_table.column("roomtype",width=100)
        
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_floor.get()=="" or self.var_RoomType.get()=="":
            messagebox.showerror("Error","All fillings are requaired",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Moihoikela@1#",database="hotel_management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                        self.var_floor.get(),
                                                                        self.var_roomNo.get(),
                                                                        self.var_RoomType.get()
                                                                            
                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","New Room Added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"Some thing went wrong:{str(es)}",parent=self.root)


    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Moihoikela@1#",database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from details")
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

        self.var_floor.set(row[0])
        self.var_roomNo.set(row[1])
        self.var_RoomType.set(row[2])

    #==================update======================

    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please Enter Floor Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Moihoikela@1#",database="hotel_management")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set Floor=%s,RoomType=%s where RoomNo=%s",(
                                                                                                                                            
                                                                                        self.var_floor.get(),
                                                                                        self.var_RoomType.get(),                                                                                                                                           
                                                                                        self.var_roomNo.get() 
                                                                                        ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","New Room details has been updated Successfully",parent=self.root)

    #=======================delete=========================

    def delete_room(self):
        delete=messagebox.askyesno("System Querry","Do you want to delete this Room details ?",parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Moihoikela@1#",database="hotel_management")
            my_cursor=conn.cursor()
            query="delete from details where RoomNo=%s"
            value=(self.var_roomNo.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

     #=======================reset=============================

    def reset_data(self):
        self.var_floor.set(""),
        self.var_roomNo.set(""),
        self.var_RoomType.set("")

    
        
        



if __name__ == "__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()