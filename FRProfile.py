from tkinter import*
from tkcalendar import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
from datetime import date,timedelta
import DAL

import cx_Oracle as con

connString = 'FRAS/FRAS@localhost:1521/xe'
connString = DAL.getDbConn()

class Profile:
    def __init__(self,root1):
        self.root1=root1
        self.root1.geometry('1520x790+0+0')
        self.root1.title("College Profile")

        img3=Image.open(r"D:\MCA_II\FinalProject\Project\IMG\zeal.JFIF")
        img3=img3.resize((1530,790),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root1,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=790)

       #================variables========================
        self.var_collcode=StringVar()
        self.var_collname=StringVar()
        self.var_hod=StringVar()
        self.var_phone=StringVar()
        self.var_mail=StringVar()
        self.var_A1=StringVar()
        self.var_A2=StringVar()
        self.var_Sdate=StringVar()
        self.var_Odate=StringVar()
        self.var_state=StringVar()
        

       #==============frame ==========
        P_frame=LabelFrame(bg_img,bd=2,bg="white",relief=RIDGE,text="Profile Info",font=("times new roman",15,"bold"))
        P_frame.place(x=380,y=100,width=720,height=300)

        #college code
        code_label=Label(P_frame,text="College Code:",font=("times new roman",13,"bold"),bg="white")
        code_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        code_entry=ttk.Entry(P_frame,textvariable=self.var_collcode,width=20,font=("times new roman",13,"bold"),state='readonly')
        code_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        self.var_collcode.set('1')
        #name
        collName_label=Label(P_frame,text="College Name:",font=("times new roman",13,"bold"),bg="white")
        collName_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        collName_entry=ttk.Entry(P_frame,textvariable=self.var_collname,width=20,font=("times new roman",13,"bold"))
        collName_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #1
        Dname_label=Label(P_frame,text="Director Name:",font=("times new roman",13,"bold"),bg="white")
        Dname_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        Dname_entry=ttk.Entry(P_frame,textvariable=self.var_hod,width=20,font=("times new roman",13,"bold"))
        Dname_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #2
        phone_label=Label(P_frame,text="Telephone:",font=("times new roman",13,"bold"),bg="white")
        phone_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(P_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #3
        mail_label=Label(P_frame,text="Mail ID:",font=("times new roman",13,"bold"),bg="white")
        mail_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        mail_entry=ttk.Entry(P_frame,textvariable=self.var_mail,width=20,font=("times new roman",13,"bold"))
        mail_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #4
        A1_label=Label(P_frame,text="Address1:",font=("times new roman",13,"bold"),bg="white")
        A1_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        A1_entry=ttk.Entry(P_frame,textvariable=self.var_A1,width=20,font=("times new roman",13,"bold"))
        A1_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #5
        A2_label=Label(P_frame,text="Address2:",font=("times new roman",13,"bold"),bg="white")
        A2_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        A2_entry=ttk.Entry(P_frame,textvariable=self.var_A2,width=20,font=("times new roman",13,"bold"))
        A2_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #6
        state_label=Label(P_frame,text="State:",font=("times new roman",13,"bold"),bg="white")
        state_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        state_entry=ttk.Entry(P_frame,textvariable=self.var_state,width=20,font=("times new roman",13,"bold"))
        state_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #7
        Sdate_label=Label(P_frame,text="Start Date:",font=("times new roman",13,"bold"),bg="white")
        Sdate_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        #code_entry=ttk.Entry(P_frame,width=20,font=("times new roman",13,"bold"))
        #code_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        todays_date = date.today()
        curnt_yr=todays_date.year
        cmnth=todays_date.month
        Sdate_entry = DateEntry(P_frame,textvariable=self.var_Sdate ,width=15,background='darkblue',font=("times new roman",13,"bold"),bg="white", foreground='white', borderwidth=1,month=1, year=int(curnt_yr)-20,locale='en_US', date_pattern='dd-mm-y')
        Sdate_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #8
        Odate_label=Label(P_frame,text="Online Date:",font=("times new roman",13,"bold"),bg="white")
        Odate_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        #Odate_entry=ttk.Entry(P_frame,width=20,font=("times new roman",13,"bold"))
        #Odate_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        Odate_entry = DateEntry(P_frame,textvariable=self.var_Odate, width=15,background='darkblue',font=("times new roman",13,"bold"),bg="white", foreground='white', borderwidth=1,month=1, year=int(curnt_yr)-20,locale='en_US', date_pattern='dd-mm-y')
        Odate_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        self.fetch_data()

#==========================buttons=============================================================================================

        btn_frame=Frame(P_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=120,y=205,width=485,height=35)

        self.save_btn=Button(btn_frame,text="Save",width=15,command=self.addP_data,font=("times new roman",13,"bold"),bg="pink",fg="black")
        self.save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Update",command=self.updateP_data,width=15,font=("times new roman",13,"bold"),bg="pink",fg="black")
        update_btn.grid(row=0,column=1)

        cancel_btn=Button(btn_frame,text="Cancel",width=15,command=self.exit, font=("times new roman",13,"bold"),bg="pink",fg="black")
        cancel_btn.grid(row=0,column=2)


#==========================insert data======================================================================================
    def addP_data(self):
       if self.var_collcode.get()=="" or self.var_collname.get()=="":
           messagebox.showerror("Error","college code & name Fields are required",parent=self.root)
           return
       if self.var_collcode.get()=="":
            messagebox.showerror("Error","Enter college code ",parent=self.root)
            return
       try:
           query2 = "INSERT INTO Profile(I_code,I_NAME,HOD,phone,mail,state,A1,A2,start_date,on_date) VALUES ("+self.var_collcode.get()+",'"+self.var_collname.get()+"','"+self.var_hod.get()+"','"+self.var_phone.get()+"','"+self.var_mail.get()+"','"+self.var_state.get()+"','"+self.var_A1.get()+"','"+self.var_A2.get()+"',to_char(to_date('"+self.var_Sdate.get()+"','dd-mm-yyyy'),'dd-MON-yyyy'),to_char(to_date('"+self.var_Odate.get()+"','dd-mm-yyyy'),'dd-MON-yyyy'))"
       # implement query Sentence
           print("Added data")
           print(query2)
           db_connection = con.connect(connString)
           db_cursor = db_connection.cursor()
           db_cursor.execute(query2)
           
        # Submit to database for execution
           db_connection.commit()
           messagebox.showinfo('Information', "Details added Successfully")
           
       except con.DatabaseError as e:
          print(e)
          db_connection.rollback()
          messagebox.showinfo('Information', "Data insertion failed!!!")
       finally:
           db_connection.close()

#==================update data=================================================================================================

    def updateP_data(self):
        if self.var_collcode.get()=="" or self.var_collname.get()=="":
           messagebox.showerror("Error","All Fields are required",parent=self.root)
           return
        if self.var_collcode.get()=="":
            messagebox.showerror("Error","Enter college code ",parent=self.root)
            return
        
        try:
            update=messagebox.askyesno("update","Do you want to update this college details",parent=self.root)
            if update>0:
                print("Update Fun Call")
                db_connection = con.connect(connString)
                db_cursor = db_connection.cursor()
                QueryString="update profile set I_NAME='"+self.var_collname.get()+"',HOD='"+self.var_hod.get()+"', phone='"+self.var_phone.get()+"', mail='"+self.var_mail.get()+"',state='"+self.var_state.get()+"',A1='"+self.var_A1.get()+"',A2='"+self.var_A2.get()+"',start_date=to_char(to_date('"+self.var_Sdate.get()+"','dd-mm-yyyy'),'dd-MON-yyyy'),on_date=to_char(to_date('"+self.var_Odate.get()+"','dd-mm-yyyy'),'dd-MON-yyyy') "+" where I_code="+self.var_collcode.get()+""
                print(QueryString)
                db_cursor.execute(QueryString)
                print(QueryString)
            else:
                if not update:
                    return
            messagebox.showinfo("success","college details successfully  updated",parent=self.root)
            db_connection.commit()
            db_connection.close()
        except Exception as es:
            messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
    #===============----
    def fetch_data(self):
        try:
            
            query2="select I_CODE,I_NAME,HOD,PHONE,MAIL,A1,A2,to_char(START_DATE,'dd-mm-yyyy') START_DATE,to_char(ON_DATE,'dd-mm-yyyy') ON_DATE,STATE FROM PROFILE where rownum=1 "
            print("********Getting Data***********")
            print(query2)
            db_connection = con.connect(connString)
            db_cursor = db_connection.cursor()
            db_cursor.execute(query2)
            rows=db_cursor.fetchall()
            for row in rows:
                print("********Found Data***********")
               #self.save_btn['state'] = 'disabled'
                self.var_collcode.set(row[0])
                self.var_collname.set(row[1])
                self.var_hod.set(row[2])
                self.var_phone.set(row[3])
                self.var_mail.set(row[4])
                self.var_A1.set(row[5])
                self.var_A2.set(row[6])
                self.var_Sdate.set(row[7])
                self.var_Odate.set(row[8])
                self.var_state.set(row[9])              
            db_connection.close()
        except con.DatabaseError as e:
            print(e)
            db_connection.close()
            messagebox.showinfo('Information', "Data fetching error!!!")
            
    def exit(self):
        try:
            root1.destroy()
        except Exception as es:
            print(es)

if __name__ == "__main__":
    root1=Tk()
    obj=Profile(root1)
    root1.mainloop()


