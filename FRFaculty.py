# face recoganization Student Page
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
from datetime import date,timedelta
import cx_Oracle as con
import cv2
import DAL

connString = 'FRAS/FRAS@localhost:1521/xe'
connString = DAL.getDbConn()
print("Conn: "+connString)

class Faculty:
    def calbackFuncBindCrs(self, event):
        if(connString is None or connString==""):
           messagebox.showerror("Error","Connection String Not found",parent=self.root)
           return
        cours = event.widget.get()
        if(cours.upper()=="--SELECT--"):
            var_dep.focus
        retDepart=()
        try:
            db_connection = con.connect(connString)
            db_cursor = db_connection.cursor()
            SQLQ=" SELECT CO_NAME FROM COURSE WHERE DEPART_ID iN(SELECT DEPART_ID FROM DEPART WHERE DEPART_NAME LIKE '%"+cours+"%') "
            Query="select '--select--'  DEPART_NAME from dual union all" + SQLQ + " "
            db_cursor.execute(Query)
            print(Query)
            rows=db_cursor.fetchall()
            if db_cursor.rowcount>1:
                retDepart=rows
            else:
                retDepart=["--select--","NA"]
            #return retDepart
            
            db_connection.close()
        except Exception as es:
            messagebox.showerror("Error","department binding error",parent=self.root)
            retDepart=["--select--","NA"]
        print(retDepart)
        self.course_combo["values"]=retDepart
        self.course_combo.current(0)
        
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recoganization System")
    #=================variables============================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_facultyid=StringVar()
        self.var_fullname=StringVar()
        self.var_shortname=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_regidate=StringVar()
        self.var_radio1=StringVar()
        self.var_passkey=StringVar()
       
        
        #back img3
        img3=Image.open(r"D:\MCA_II\Project\IMG\Grey.jpg")
        img3=img3.resize((1530,790),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=790)

        title_lb=Label(bg_img,text="Faculty Management",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lb.place(x=0,y=0,width=1530,height=60)

        #main frame for stud details
        main_frame =Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=65,width=1510,height=715)

        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Faculty Details",font=("times new roman",15,"bold"))
        left_frame.place(x=5,y=0,width=730,height=710)


        img_left=Image.open(r"D:\MCA_II\Project\IMG\img19.JFIF")
        img_left=img_left.resize((720,200),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        flb=Label(left_frame,image=self.photoimg_left)
        flb.place(x=5,y=0,width=720,height=200)

        #current_course
        current_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Info",font=("times new roman",15,"bold"))
        current_frame.place(x=3,y=225,width=720,height=115)
        
        #Department 
        dep_label=Label(current_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        DCombo_val=self.bindDepart1()
        dep_combo=ttk.Combobox(current_frame ,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=20,state="readonly")
        #dep_combo["values"]=("Select Department","Computer","IT","civil","machanical")
        dep_combo["values"]=DCombo_val
        dep_combo.current(0)
        dep_combo.bind("<<ComboboxSelected>>", self.calbackFuncBindCrs)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course     
        course_label=Label(current_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        self.course_combo=ttk.Combobox(current_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),width=20,state="readonly")
        self.course_combo["values"]=("Select Course","FE","SE","TE","BE")   
        self.course_combo.current(0)
        self.course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year    
        year_label=Label(current_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(current_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),width=20,state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")   
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester   
        sem_label=Label(current_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)
        
        sem_combo=ttk.Combobox(current_frame,textvariable=self.var_sem,font=("times new roman",13,"bold"),width=20,state="readonly")
        sem_combo["values"]=("Select Semester","Sem-1","Sem-2")   
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Class Stud Info
        class_stud_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Stud Info",font=("times new roman",15,"bold"))
        class_stud_frame.place(x=3,y=350,width=720,height=329)

        #FACULTYID
        studId_label=Label(class_stud_frame,text="Faculty Id:",font=("times new roman",13,"bold"),bg="white")
        studId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studId_entry=ttk.Entry(class_stud_frame,textvariable=self.var_facultyid,state="readonly",width=20,font=("times new roman",13,"bold"))
        studId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #passkey
        pass_label=Label(class_stud_frame,text="Pass Key",font=("times new roman",13,"bold"),bg="white")
        pass_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        pass_entry=ttk.Entry(class_stud_frame,textvariable=self.var_passkey,width=20,font=("times new roman",13,"bold"))
        pass_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #FACULTY SHORT name
        studName_label=Label(class_stud_frame,text="Short Name:",font=("times new roman",13,"bold"),bg="white")
        studName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studName_entry=ttk.Entry(class_stud_frame,textvariable=self.var_shortname,width=20,font=("times new roman",13,"bold"))
        studName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        
        #FULL no
        roll_no_label=Label(class_stud_frame,text="Full Name:",font=("times new roman",13,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_stud_frame,textvariable=self.var_fullname,width=20,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
        gender_label=Label(class_stud_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_stud_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),width=18,state="readonly")
        gender_combo["values"]=("select gender","Male","Female")   
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #DOB
        dob_label=Label(class_stud_frame,text="DOB:",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        #dob_entry=ttk.Entry(class_stud_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        #dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        todays_date = date.today()
        curnt_yr=todays_date.year
        cmnth=todays_date.month
        dob_entry = DateEntry(class_stud_frame, width=15,background='darkblue',textvariable=self.var_dob,font=("times new roman",13,"bold"),bg="white", foreground='white', borderwidth=1,month=1, year=int(curnt_yr)-20,locale='en_US', date_pattern='dd-mm-y')
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Email
        email_label=Label(class_stud_frame,text="Email:",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_stud_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Phone no
        phone_label=Label(class_stud_frame,text="Phone No:",font=("times new roman",13,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_stud_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Address
        address_label=Label(class_stud_frame,text="Address:",font=("times new roman",13,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_stud_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Regi Date
        regidate_label=Label(class_stud_frame,text="Registration Date:",font=("times new roman",13,"bold"),bg="white")
        regidate_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        #regidate_entry=ttk.Entry(class_stud_frame,textvariable=self.var_regidate,width=20,font=("times new roman",13,"bold"))
        #regidate_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        regidate_entry = DateEntry(class_stud_frame, width=15,background='darkblue',textvariable=self.var_regidate,font=("times new roman",13,"bold"),bg="white", foreground='white', borderwidth=1,month=1, year=int(curnt_yr)-20,locale='en_US', date_pattern='dd-mm-y')
        regidate_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_stud_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

       
        radiobtn2=ttk.Radiobutton(class_stud_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)

         #buttons frame
        btn_frame=Frame(class_stud_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=235,width=715,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="pink",fg="black")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="pink",fg="black")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="pink",fg="black")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.Reset_entrybx,width=17,font=("times new roman",13,"bold"),bg="pink",fg="black")
        reset_btn.grid(row=0,column=3)

        #buttons
        #btn_frame1=Frame(class_stud_frame,bd=2,relief=RIDGE,bg="white")
        #btn_frame1.place(x=0,y=268,width=715,height=35)

        #take_photo_btn=Button(btn_frame1,text="Take photo Sample",width=35,font=("times new roman",13,"bold"),bg="pink",fg="black")
        #take_photo_btn.grid(row=0,column=0)

        #update_photo_btn=Button(btn_frame1,text="Update photo Sample",width=35,font=("times new roman",13,"bold"),bg="pink",fg="black")
        #update_photo_btn.grid(row=0,column=1)
        
         #right label frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Faculty Details",font=("times new roman",15,"bold"),bg="white")
        right_frame.place(x=750,y=0,width=748,height=710)

        #img_right=Image.open(r"D:\MCA_II\AITLab\Media\banner.jpg")
        #img_right=img_right.resize((720,200),Image.ANTIALIAS)
        #self.photoimg_right=ImageTk.PhotoImage(img_right)

        #flb=Label(right_frame,image=self.photoimg_right)
        #flb.place(x=5,y=0,width=720,height=200)
        
        #================Search System===============

        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search",font=("times new roman",15,"bold"))
        search_frame.place(x=3,y=3,width=737,height=70)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",13,"bold"),width=15,state="readonly")
        search_combo["values"]=("Select","FacultyId","Phone_No")   
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_frame,text="ShowAll",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        #================Table Frame==============

        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=3,y=100,width=737,height=380)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.stud_table=ttk.Treeview(table_frame,column=("SrNo","id","ShortN","FullN","dep","sem","course","phone","email","year","gender","dob","address","RegiDate","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.stud_table.xview)
        scroll_y.config(command=self.stud_table.yview)
        
        self.stud_table.heading("SrNo",text="SrNo")
        self.stud_table.heading("id",text="FacultyID")
        self.stud_table.heading("ShortN",text="ShortName")
        self.stud_table.heading("FullN",text="FullName")
        self.stud_table.heading("dep",text="Department")
        self.stud_table.heading("sem",text="Semester")
        self.stud_table.heading("course",text="Course")
        self.stud_table.heading("phone",text="PhoneNo")
        self.stud_table.heading("email",text="Email")
        self.stud_table.heading("year",text="Year")
        
        self.stud_table.heading("gender",text="Gender")
        self.stud_table.heading("dob",text="DOB")       
        
        self.stud_table.heading("address",text="Address")
        self.stud_table.heading("RegiDate",text="RegistrationDate")
        self.stud_table.heading("photo",text="PhotoStatus")
        
        self.stud_table["show"]="headings"

        self.stud_table.column("SrNo",width=100)
        self.stud_table.column("id",width=100)
        self.stud_table.column("ShortN",width=100)
        self.stud_table.column("FullN",width=100)
        self.stud_table.column("dep",width=100)    
        self.stud_table.column("sem",width=100)   
        self.stud_table.column("course",width=100)
        self.stud_table.column("phone",width=100)
        self.stud_table.column("email",width=100)
        self.stud_table.column("year",width=100)
             
        self.stud_table.column("gender",width=100)
        self.stud_table.column("dob",width=100)
        self.stud_table.column("address",width=100)
        self.stud_table.column("RegiDate",width=100)
        self.stud_table.column("photo",width=150)
        
        self.stud_table.pack(fill=BOTH,expand=1)
        self.getmxsrno()
        self.fetch_data()
        
        self.stud_table.bind("<ButtonRelease>",self.get_cursor)
    #======================function declaration=====================

    def add_data(self):
       if self.var_dep.get()=="Select Department" or self.var_fullname.get()=="" or self.var_facultyid.get()=="":
           messagebox.showerror("Error","All Fields are required",parent=self.root)
           return
       if self.var_facultyid.get()=="":
            messagebox.showerror("Error","Enter faculty id",parent=self.root)
            return
       else:
           #messagebox.showinfo("success","Welcome To Zeal Institute Of Management,Narhe,Pune")

        gender="M"
        try:
            if self.var_gender.get()=="Male":
                gender="M"
            else:
                gender="F"
                
            query2 = "INSERT INTO faculty (FSRNO,FACULTY_ID,SHORTNAME,FULLNAME,DEPART,SEM,CO_NAME,MOBILE,EMAIL,EDUYEAR,GENDER,dob,address,REGDATE,co_code,passkey)"
            query2 = query2 +" VALUES ((select nvl(max(fsrno),0)+1 from faculty),"+self.var_facultyid.get()+", '"+self.var_shortname.get()+"','"+self.var_fullname.get()+"' "
            query2=query2+",'"+ self.var_dep.get()+"','"+ self.var_sem.get()+"','"+self.var_course.get()+"','"+self.var_phone.get()+"','"+self.var_email.get()+"','"+self.var_year.get()+"','"+gender+"'"
            query2=query2+",to_char(to_date('"+self.var_dob.get()+"','dd-mm-yyyy'),'dd-MON-yyyy'),'"+self.var_address.get()+"',(select to_char(sysdate,'dd-mon-yyyy')  from dual),"
            query2=query2+"(SELECT CO_ID FROM course WHERE CO_NAME LIKE '%"+self.var_course.get()+"%'),'"+self.var_passkey.get()+"')"
    #impleme  SELECT DEPART_ID FROM DEPART WHERE DEPART_NAME LIKE '%"+cours+"%'

            
            print(query2)
            db_connection = con.connect(connString)
            db_cursor = db_connection.cursor()
            db_cursor.execute(query2)
           
        # Submit to database for execution
            db_connection.commit()
            self.Fcredential()
            self.Reset_entrybx()
            messagebox.showinfo('Information', "Student Registration Successfully")
            self.fetch_data()
           
        except con.DatabaseError as e:
             print(e)
             db_connection.rollback()
             messagebox.showinfo('Information', "Data insertion failed!!!")
        finally:
            db_connection.close()

     #fetching data to table
    def fetch_data(self):
        try:
            self.stud_table.delete(*self.stud_table.get_children())# 
            query2="select FSRNO,FACULTY_ID,SHORTNAME,FULLNAME,DEPART,SEM,CO_NAME,MOBILE,EMAIL,EDUYEAR,(case when GENDER='M' then 'Male' when GENDER='F' then 'Female' else GENDER end) GENDER,to_char(dob,'dd-mm-yyyy') dob,address,to_char(REGDATE,'dd-mm-yyyy') REGDATE,PHOTO from faculty"
            
            print(query2)
            #db_connection = con.connect(connString)
            #db_cursor = db_connection.cursor()
           # db_cursor.execute(query2)
           # rows=db_cursor.fetchall()
            rows=DAL.GetDataTableText(query2)
            for row in rows:                 
                 self.stud_table.insert("",'end',text=str(row[0]),values=(str(row[0]),str(row[1]),str(row[2]), str(row[3]),str(row[4]),str(row[5]),str(row[6]),str(row[7]),str(row[8]),str(row[9]),str(row[10]),str(row[11]),str(row[12]),str(row[13]),str(row[14])))
        except con.DatabaseError as e:
             print(e)
             db_connection.rollback()
             messagebox.showinfo('Information', "Data fetching error!!!")
        #finally:
            #db_connection.close()


    def getmxsrno(self):
        try:
            self.stud_table.delete(*self.stud_table.get_children()) 
            query2="select (nvl(max(FSRNO),0)+1) srno from faculty"
            print("*******************")
            print(query2)
            db_connection = con.connect(connString)
            db_cursor = db_connection.cursor()
            db_cursor.execute(query2)
            rows=db_cursor.fetchall()
            for row in rows:
                self.var_facultyid.set(row[0])
        except con.DatabaseError as e:
             print(e)
             db_connection.rollback()
             messagebox.showinfo('Information', "Data fetching error!!!")
        finally:
            db_connection.close()

    #===Reset===============================================================================

    def Reset_entrybx(self):
        cursor_focus=self.stud_table.focus()
        content=self.stud_table.item(cursor_focus)
        data=content["values"]
        self.var_facultyid.set(""),
        self.var_fullname.set(""),
        self.var_dep.set("select Department"),
        self.var_shortname.set("select division"),
        self.var_sem.set("select Semester"),
        self.var_course.set("select Course"),
        self.var_phone.set(""),
        self.var_email.set(""),
        self.var_year.set("Select Year"),
        self.var_gender.set("Select Gender"),
        self.var_dob.set(""),
        self.var_address.set(""),
        self.var_regidate.set(""),
        self.var_radio1.set(""),
        self.var_passkey.set("")
        self.getmxsrno()
        

    #=============get cursor=========================================================================
        
    def get_cursor(self,event=""):
        cursor_focus=self.stud_table.focus()
        content=self.stud_table.item(cursor_focus)
        data=content["values"]
        self.var_facultyid.set(data[0]),
        self.var_shortname.set(data[2]),
        self.var_fullname.set(data[3]),
        self.var_dep.set(data[4]),
        self.var_regidate.set(data[13]),
        self.var_sem.set(data[5]),
        self.var_course.set(data[6]),
        self.var_phone.set(data[7]),
        self.var_email.set(data[8]),
        self.var_year.set(data[9]),
        self.var_gender.set(data[10]),
        self.var_dob.set(data[11]),
        self.var_address.set(data[12]),
        self.var_radio1.set(data[14]);

    #=====update_function======================================================================================
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_fullname.get()=="" or self.var_facultyid.get()=="":
           messagebox.showerror("Error","All Fields are required",parent=self.root)
           return 
        else:
            try:
                gender="M"
                if self.var_gender.get()=="Male":
                    gender="M"
                else:
                    gender="F"
                update=messagebox.askyesno("update","Do you want to update this faculty details",parent=self.root)
                if update>0:
                    print("Hello Maau")
                    db_connection = con.connect(connString)
                    db_cursor = db_connection.cursor()
                    QueryString="update faculty set faculty_id='"+self.var_facultyid.get()+"',FULLNAME='"+self.var_fullname.get()+"',shortname='"+self.var_shortname.get()+"',MOBILE='"+self.var_phone.get()+"',EMAIL='"+self.var_email.get()+"',DEPART='"+self.var_dep.get()+"',SEM='"+self.var_sem.get()+"',"+ "dob=to_char(to_date('"+self.var_dob.get()+"','dd-mm-yyyy'),'dd-mon-yyyy'),passkey='"+self.var_passkey.get()+"',EDUYEAR='"+self.var_year.get()+"',"+"GENDER='"+gender+"',address='"+self.var_address.get()+"',co_name='"+self.var_course.get()+"' "+" where faculty_id="+self.var_facultyid.get()+""
                    db_cursor.execute(QueryString)
                    print(QueryString)
            
                else:
                    if not update:
                        return
                        
                    
                
                db_connection.commit()
                self.Fcredential()
                messagebox.showinfo("success","faculty details successfully updated",parent=self.root)
                self.Reset_entrybx()
                self.fetch_data()
                db_connection.close()
                
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #========================delete data====================================================================

    def delete_data(self):
        if self.var_facultyid.get()=="":
        
            messagebox.showerror("Error","faculty id must be require",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("faculty delete page","Do You want to delete this faculty",parent=self.root)
                if delete>0:
                    db_connection = con.connect(connString)
                    db_cursor = db_connection.cursor()
                    QueryString="delete from faculty where faculty_id="+self.var_facultyid.get()+""
                    db_cursor.execute(QueryString)
                    print(QueryString)
                else:
                    if not delete:
                        return
                    
                        
                db_connection.commit()
                self.fetch_data()
                db_connection.close()
                messagebox.showinfo("Delete","faculty details successfully Deleted",parent=self.root)
                
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #===================binding depart==========================

    def bindDepart1(self):
        retDepart=()
        try:
            db_connection = con.connect(connString)
            db_cursor = db_connection.cursor()
            Query="select '--select--'  DEPART_NAME from dual union all select DEPART_NAME from depart"
            db_cursor.execute(Query)
            print(Query)
            rows=db_cursor.fetchall()
            if db_cursor.rowcount>1:
                retDepart=rows
            else:
                retDepart=["--select--","MCA"]
            return retDepart
            
            db_connection.close()
        except Exception as es:
                messagebox.showerror("Error","Department binding error",parent=self.root)
                retDepart=["--select--","MCA"]
                return retDepart

    def Fcredential(self):
        try:
            db_connection = con.connect(connString)
            db_cursor = db_connection.cursor()
            Query="select u_id,EMAIL,upw from usermst where email='"+self.var_email.get()+"' and STATS='A'"
            db_cursor.execute(Query)
            print(Query)
            rows=db_cursor.fetchall()
            db_connection.close()
            if db_cursor.rowcount>0:
                Q1="update usermst set upw='"+self.var_passkey.get()+"' where email='"+self.var_email.get()+"' and STATS='A' " 
               
            else:
                Q1="insert into usermst(U_ID,UNM,UPW,EMAIL,MOBILE,STATS,SHRNM) values((select nvl(max(U_ID),0)+1 from usermst),'"+self.var_fullname.get()+"'"
                Q1=Q1+", '"+self.var_passkey.get()+"' ,'"+self.var_email.get()+"' , '"+self.var_phone.get()+"','A' , '"+self.var_shortname.get()+"')" 
            print("upto")
            DAL.executeQuery(Q1)
            
        except Exception as es:
                messagebox.showerror("Error","Login Credential Creation error",parent=self.root)
                print(es)
                
             

if __name__ == "__main__":
    root=Tk()
    obj=Faculty(root)
    root.mainloop()
      
