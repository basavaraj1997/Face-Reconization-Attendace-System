from tkinter import*
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
import cx_Oracle as con
from datetime import date,timedelta
import xlsxwriter
import DAL

connString = 'FRAS/FRAS@localhost:1521/xe'
connString = DAL.getDbConn()

class FRReport_Course:
    def __init__(self,root):
        self.root=root

        width= self.root.winfo_screenwidth() 
        height= self.root.winfo_screenheight()
        self.root.geometry("%dx%d" % (width/1.2, height/1.2-10))
        width=width/1.2
        height=height/1.2-10
        
        #self.root.geometry('1530x790+0+0')
        self.root.title("Face Recoganization System")

        img3=Image.open(r"IMG\img18.JFIF")
        img3=img3.resize((1500,790),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=width,height=790)

        title_lb=Label(bg_img,text="Course Wise Report",font=("times new roman",20,"bold"),bg="white",fg="black")
        title_lb.place(x=0,y=0,width=width,height=60)
        # report table frame
        R_frame=LabelFrame(bg_img,bd=2,bg="white",relief=RIDGE,text="Report Details",font=("times new roman",10,"bold"))
        R_frame.place(x=5,y=45,width=width,height=740)

       #buttons frame
        todays_date = date.today()
        # fetching the current year, month and day of today
        curnt_yr=todays_date.year
        cmnth=todays_date.month #cday=todays_date.day

        search_label=Label(R_frame,text="Select Date: ",font=("times new roman",15,"bold"))
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        
        self.frmDt = DateEntry(R_frame, width=10, background='darkblue', foreground='white', borderwidth=1,month=int(cmnth)-1, year=int(curnt_yr),  locale='en_US', date_pattern='dd-mm-y')
        self.frmDt.grid(row=0,column=3, padx=5)
        
        self.ToDt = DateEntry(R_frame, width=10, background='darkblue', foreground='white', borderwidth=1, year=int(curnt_yr),  locale='en_US', date_pattern='dd-mm-y')
        self.ToDt.grid(row=0,column=9,padx=5)

        procss_btn=Button(R_frame,text="Process",width=10,command=self.cwaDataProcess,font=("times new roman",12,"bold"),bg="pink",fg="black")
        procss_btn.grid(row=0,column=12,padx=10)
         
        self.view_btn=Button(R_frame,text="View",width=10,command=self.GetBindDataToTable,font=("times new roman",12,"bold"),bg="pink",fg="black")
        self.view_btn.grid(row=0,column=17,padx=10)
        self.view_btn["state"] = DISABLED

        self.ex_btn=Button(R_frame,text="Export",command=self.export, width=12,font=("times new roman",12,"bold"),bg="pink",fg="black")
        self.ex_btn.grid(row=0,column=19,padx=5)
        self.ex_btn["state"] = DISABLED
    
        CourseVal=self.Get_Course_data()
        lblCourse=Label(R_frame,text="Course: ",font=("times new roman",15,"bold"),bg="white",fg="black")
        #lblCourse.place(x=5,y=60)
        lblCourse.grid(row=1,column=0)
        self.course_combo=ttk.Combobox(R_frame,font=("times new roman",12,"bold"),width=20)
        self.course_combo["values"]=CourseVal
        print(CourseVal)
        self.course_combo.current(0)
        
        self.course_combo.grid(row=1,column=3,padx=5,pady=1)
        
#==========================First Table================================================
        table_frame=Frame(R_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=100,width=width-25,height=height-150)
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.stud_table=ttk.Treeview(table_frame,column=("roll","name","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.stud_table.xview)
        scroll_y.config(command=self.stud_table.yview)
        
        self.stud_table.heading("roll",text="RollNo")
        self.stud_table.heading("name",text="Name")
        self.stud_table.heading("1",text="1")
        self.stud_table.heading("2",text="2")
        self.stud_table.heading("3",text="3")
        self.stud_table.heading("4",text="4")
        self.stud_table.heading("5",text="5")
        self.stud_table.heading("6",text="6")
        self.stud_table.heading("7",text="7")
        self.stud_table.heading("8",text="8")
        self.stud_table.heading("9",text="9")
        self.stud_table.heading("10",text="10")
        self.stud_table.heading("11",text="11")
        self.stud_table.heading("12",text="12")
        self.stud_table.heading("13",text="13")
        self.stud_table.heading("14",text="14")
        self.stud_table.heading("15",text="15")
        self.stud_table.heading("16",text="16")
        self.stud_table.heading("17",text="17")
        self.stud_table.heading("18",text="18")
        self.stud_table.heading("19",text="19")
        self.stud_table.heading("20",text="20")
        self.stud_table.heading("21",text="21")
        self.stud_table.heading("22",text="22")
        self.stud_table.heading("23",text="23")
        self.stud_table.heading("24",text="24")
        self.stud_table.heading("25",text="25")
        self.stud_table.heading("26",text="26")
        self.stud_table.heading("27",text="27")
        self.stud_table.heading("28",text="28")
        self.stud_table.heading("29",text="29")
        self.stud_table.heading("30",text="30")
        self.stud_table.heading("31",text="31")
        
        self.stud_table["show"]="headings"
        self.stud_table.column("roll",width=100)
        self.stud_table.column("name",width=150)
        self.stud_table.column("1",width=50)    
        self.stud_table.column("2",width=50)
        self.stud_table.column("3",width=50)   
        self.stud_table.column("4",width=50)
        self.stud_table.column("5",width=50)
        self.stud_table.column("6",width=50)
        self.stud_table.column("7",width=50)
        self.stud_table.column("8",width=50)
        self.stud_table.column("9",width=50)
        self.stud_table.column("10",width=50)
        self.stud_table.column("11",width=50)
        self.stud_table.column("12",width=50)
        self.stud_table.column("13",width=50)
        self.stud_table.column("14",width=50)
        self.stud_table.column("15",width=50)
        self.stud_table.column("16",width=50)
        self.stud_table.column("17",width=50)
        self.stud_table.column("18",width=50)
        self.stud_table.column("19",width=50)
        self.stud_table.column("20",width=50)
        self.stud_table.column("21",width=50)
        self.stud_table.column("22",width=50)
        self.stud_table.column("23",width=50)
        self.stud_table.column("24",width=50)
        self.stud_table.column("25",width=50)
        self.stud_table.column("26",width=50)
        self.stud_table.column("27",width=50)
        self.stud_table.column("28",width=50)
        self.stud_table.column("29",width=50)
        self.stud_table.column("30",width=50)
        self.stud_table.column("31",width=50)       
        self.stud_table.pack(fill=BOTH,expand=1)
        

    def GetBindDataToTable(self):
        A_PCases=""
        A_PDays=""
        print(self.ToDt.get())
        if self.ToDt.get()=="":
            messagebox.showerror("Error","Select Date",parent=self.root)
            return

        d1, m1, y1 = [int(x) for x in self.frmDt.get().split('-')]
        frmdate = date(y1, m1, d1)
        if(int(frmdate.strftime("%d"))!=1):
            messagebox.showinfo('Information', "Start Date Must be Begining of Month !!")
            return
        d2, m2, y2 = [int(x) for x in self.ToDt.get().split('-')]
        todate = date(y2, m2, d2)
        
        mEndDate=self.getLstDateOfMonth(self.frmDt.get())
        num_months = (todate.year - frmdate.year) * 12 + (todate.month - frmdate.month)
        if(int(num_months)>7):
            messagebox.showinfo('Information', "Date Differeace Should Be 6 Months")
            return
        FirsDate=self.frmDt.get()
        EndDate=mEndDate
        self.stud_table.delete(*self.stud_table.get_children())
        while 0 <= num_months:
            num_months=num_months-1            
            print("**")
            mTempDate=mEndDate
            if(mEndDate.split('-')[0] != int(self.ToDt.get().split('-')[0]) and int(mEndDate.split('-')[1])== int(self.ToDt.get().split('-')[1]) and int(mEndDate.split('-')[2])== int(self.ToDt.get().split('-')[2])):
                mEndDate=self.ToDt.get()
                EndDate=mEndDate
            print(mEndDate)
            #BUILD CASE AND DAY QUERY
            try:                
                i=0
                print("loope being "+str(FirsDate)+" "+str(EndDate))
                d1, m1, y1 = [int(x) for x in FirsDate.split('-')]
                frmdate = date(y1, m1, d1)

                d2, m2, y2 = [int(x) for x in EndDate.split('-')]
                todate = date(y2, m2, d2)
                         
                A_PDays=""
                A_PCases=""
                tempdt=frmdate
                while(todate >= tempdt):                                       
                    A_PDays= A_PDays+" nvl(D"+str(tempdt.day).zfill(2)+", 'A')  D"+str(tempdt.day).zfill(2)+","

                    tempdt=tempdt+timedelta(days=1)
                    print("loop END")
                A_PDays=A_PDays[0:len(A_PDays)-1]
            except Exception as e:
                print(e)
                messagebox.showinfo('Information', " Date is Not Currect !!")
                return
            ##GET DATA BETWEEN TWO DATES FROM DATABASE
            try:
                #self.stud_table.delete(*self.stud_table.get_children())
                query2=" select S.ROLLNO,S.FULLNAME, "+A_PDays+"  from CourseWiseAttendace CW,Student_mst s where Cw.srno=s.srno and s.rollno=CW.rollno"
                query2=query2+" AND frdt=to_date('"+FirsDate+"','dd-mm-yyyy') "
                # to_date('"+FirsDate+"','dd-mm-yyyy')
                print(query2)
                db_connection = con.connect(connString)
                db_cursor = db_connection.cursor()
                db_cursor.execute(query2)
                rows=db_cursor.fetchall()
                db_connection.close()
                if(db_cursor.rowcount>0):
                       self.stud_table.insert("",'end',text=str(""),values=("The Student Attendace Between",FirsDate+" To "+EndDate+" ("+str(self.course_combo.get())+")"))
                for row in rows:
                     print("**********Got Data*********")                 
                     self.stud_table.insert("",'end',text=str(row),values=(row))
            except  Exception as e:
                db_connection.close()
                print(e)
                messagebox.showinfo('Information', "Data fetching error!!!")

            print("Before.."+mEndDate)
            mEndDate=self.AddNoOfMonth(EndDate,1)
            if(mEndDate.split('-')[0] != d2 and int(mEndDate.split('-')[1])== int(m2) and int(mEndDate.split('-')[2])== int(y2)):
               mEndDate=self.ToDt.get() 
            FirsDate="01-"+str(str(mEndDate).split('-')[1])+"-"+ str(str(mEndDate).split('-')[2])
            EndDate=mEndDate
            self.ex_btn['state']="normal"
            

    
    def getLstDateOfMonth(self,curDate):
        retval=curDate
        try:
            query1=" select to_char(Last_day(to_date('"+curDate+"','dd-mm-yyyy')),'dd-mm-yyyy') from dual "            
            print(query1)
            db_connection = con.connect(connString)
            db_cursor = db_connection.cursor()
            db_cursor.execute(query1)
            rows=db_cursor.fetchall()
            db_connection.close()
            for row in rows:
               retval=row[0]            
            return retval
        except con.DatabaseError as e:
            db_connection.close()           
            messagebox.showinfo('Information', "Error In Get Last Of Month!!!")
            return retval

    def AddNoOfMonth(self,CurDate,NoOfMnts):
        retVal=CurDate
        try:
            query1=" select to_char(ADD_MONTHS(to_date('"+CurDate+"','dd-mm-yyyy'),"+str(NoOfMnts)+"),'dd-mm-yyyy') from dual "
            print(query1)
            db_connection = con.connect(connString)
            db_cursor = db_connection.cursor()
            db_cursor.execute(query1)
            rows=db_cursor.fetchall()
            db_connection.close()
            for row in rows:
                retVal=row[0]
            return retVal
        except con.DatabaseError as e:
            db_connection.close()
            messagebox.showinfo('Information', "Error In Get Last Of Month!!!")
            return retVal

    def AddNoOfDays(self,CurDate,NoOfMnts):
        retVal=CurDate
        try:
            query1=" select to_char((to_date('"+CurDate+"','dd-mm-yyyy')+"+str(NoOfMnts)+"),'dd-mm-yyyy') from dual "
            print(query1)
            db_connection = con.connect(connString)
            db_cursor = db_connection.cursor()
            db_cursor.execute(query1)
            rows=db_cursor.fetchall()
            db_connection.close()
            for row in rows:
                retVal=row[0]
            return retVal
        except con.DatabaseError as e:
            db_connection.close()
            messagebox.showinfo('Information', "Error In Get Last Of Month!!!")
            return retVal

    def export(self):
        if(self.course_combo.get()=="--Select--"):
            messagebox.showinfo('Information', "Select Course!!!")
            return
            
        
        
        open_file = filedialog.askdirectory()
        if(open_file==""):
            messagebox.showinfo('alert', "Select folder to save file!!!")
            return
            
            
            
            
        fpath=open_file
        fullpath=''+fpath+'\Attendace'+str(self.course_combo.get())+'.xlsx'
        workbook = xlsxwriter.Workbook(r''+fullpath)
        #workbook = xlsxwriter.Workbook('hello.xlsx')
        worksheet = workbook.add_worksheet()
        print(self.stud_table.column)
        i=1
        j=0
        for child in self.stud_table.get_children():
            print(len(self.stud_table.item(child)["values"]))
            for j in range(len(self.stud_table.item(child)["values"])):
                #print(self.stud_table.item(child)["values"])
                print(self.stud_table.item(child)["values"][j])                
                worksheet.write(i,j,self.stud_table.item(child)["values"][j])
                j=j+1
            i=i+1
        #workbook.save('xlwt example.xls')
        workbook.close()
        messagebox.showinfo('Information', "Exporting Completed Successfully !!")
        return

        #Course...
    def Get_Course_data(self):
        try:
            deprtValue=()
            query2="  select '--Select--' CO_NAME from dual union all select CO_NAME from COURSE where stats='A' "
            print("*******************")
            print(query2)
            db_connection = con.connect(connString)
            db_cursor = db_connection.cursor()
            db_cursor.execute(query2)
            rows=db_cursor.fetchall()
            db_connection.close()
            if(db_cursor.rowcount>1):
                deprtValue=rows
            else:
                deprtValue=["--Select--","ADBMS","AIT","OT","SMP"]
            return deprtValue
        except con.DatabaseError as e:
            print(e)
            db_connection.rollback()
            db_connection.close()
            messagebox.showinfo('Information', "Data fetching error!!!")
            return deprtValue



    def cwaDataProcess(self):
        A_PCases=""
        A_PDays=""
        print(self.ToDt.get())
        if self.ToDt.get()=="":
            messagebox.showerror("Error","Select Date",parent=self.root)
            return
        if self.course_combo.get()=="--Select--":
            messagebox.showerror("Error","Select Course",parent=self.root)
            return

        d1, m1, y1 = [int(x) for x in self.frmDt.get().split('-')]
        frmdate = date(y1, m1, d1)
        if(int(frmdate.strftime("%d"))!=1):
            messagebox.showinfo('Information', "Start Date Must be Begining of Month !!")
            return
        d2, m2, y2 = [int(x) for x in self.ToDt.get().split('-')]
        todate = date(y2, m2, d2)
                #Truncate table
        db_connection1 = con.connect(connString)
        db_cursor1 = db_connection1.cursor()
        db_cursor1.execute("truncate table CourseWiseAttendace")
        db_cursor1.close()
        db_connection1.close()
        #mEndDate=self.getLstDateOfMonth(self.frmDt.get())
        mEndDate=self.frmDt.get()
        num_Days = (todate - frmdate)
        num_Days=num_Days.days
        if(int(num_Days)>180):
            messagebox.showinfo('Information', "Date Differeace Should Be 6 Months")
            return
        FirsDate=self.frmDt.get()
        EndDate=mEndDate
        
        #Truncate Table...
        while 0 <= num_Days:
            num_Days=num_Days-1       
            print("**=>"+str(num_Days))
            mTempDate=mEndDate
                                
            try:                
                query2=" MERGE INTO CourseWiseAttendace CWA USING(SELECT SRNO,ROLLNO, "
                query2=query2+" to_date('"+"01-"+str(FirsDate.split('-')[1])+"-"+str(FirsDate.split('-')[2])+"','dd-mm-yyyy') FRDT, to_date('"+self.getLstDateOfMonth(FirsDate)+"','dd-mm-yyyy') TODT, "
                query2=query2+" 'P' D"+str(FirsDate.split('-')[0]).zfill(2)+" FROM STUDENT_MST WHERE SRNO NOT IN"
                query2=query2+" (SELECT SRNO FROM CWA WHERE DT=to_date('"+FirsDate+"','dd-mm-yyyy') and CORSNM like '%"+self.course_combo.get()+"%') " 
                query2=query2+" and rollno in(select ROLLNO from attendace where odt=to_date('"+FirsDate+"','dd-mm-yyyy') ))CA "
                query2=query2+" ON "
                query2=query2+" (CWA.SRNO=CA.SRNO AND CWA.ROLLNO=CA.ROLLNO AND CWA.FRDT=CA.FRDT AND CWA.TODT=CA.TODT) "
                query2=query2+" WHEN MATCHED THEN UPDATE SET CWA.D"+str(FirsDate.split('-')[0]).zfill(2)+"=CA.D"+str(FirsDate.split('-')[0]).zfill(2)+" "
                query2=query2+" WHEN NOT MATCHED THEN INSERT(SRNO,ROLLNO,FRDT,TODT,D"+str(FirsDate.split('-')[0]).zfill(2)+") "
                query2=query2+" VALUES(CA.SRNO,CA.ROLLNO,CA.FRDT,CA.TODT,CA.D"+str(FirsDate.split('-')[0]).zfill(2)+") "
                print(query2)
                
                db_connection = con.connect(connString)
                db_cursor = db_connection.cursor()
                db_cursor.execute(query2)
                db_connection.commit()
                db_connection.close() 
            except  Exception as e:
                db_connection.rollback()
                db_connection.close()
                print(e)
                messagebox.showinfo('Information', " Error in Data Process!!!")
                break

            print("Before.."+mEndDate)
            FirsDate=EndDate
            mEndDate=self.AddNoOfDays(EndDate,1)

           
            EndDate=mEndDate
        messagebox.showinfo("Info","Process Completed Successfully")
        self.view_btn["state"] = "normal"

#=========================code to select/browse file=====================================
        
    def browseFiles(self):
        open_file = filedialog.askdirectory()
        if open_file:
            try:
                self.settings["template"].set(open_file)
            except:
                messagebox.showerror("Open Source File", "Failed to read file \n'%s'"%open_file)
 
if __name__ == "__main__":
    root=Tk()
    obj=FRReport_Course(root)
    root.mainloop()
    

