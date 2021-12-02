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
class FRReport_Per:
    def __init__(self,root):
        self.root=root

        width= self.root.winfo_screenwidth() 
        height= self.root.winfo_screenheight()
        self.root.geometry("%dx%d" % (width/1.2, height/1.2-10))
        width=width/1.2
        height=height/1.2-10
        
        #self.root.geometry('1530x790+0+0')
        self.root.title("Face Recoganization System")
        #variable1
        self.var_roll=StringVar()

        img3=Image.open(r"IMG\img18.JFIF")
        img3=img3.resize((1500,790),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=width,height=790)

        title_lb=Label(bg_img,text="Report Percentage",font=("times new roman",20,"bold"),bg="white",fg="black")
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
        search_label.grid(row=0,column=0,padx=40,pady=20,sticky=W)
        
        self.frmDt = DateEntry(R_frame, width=10, background='darkblue', foreground='white', borderwidth=1,month=int(cmnth)-1, year=int(curnt_yr),  locale='en_US', date_pattern='dd-mm-y')
        self.frmDt.grid(row=0,column=3, padx=5)

        self.ToDt = DateEntry(R_frame, width=10, background='darkblue', foreground='white', borderwidth=1, year=int(curnt_yr),  locale='en_US', date_pattern='dd-mm-y')
        self.ToDt.grid(row=0,column=9,padx=5)

 
        view_btn=Button(R_frame,text="View",width=10,command=self.GetBindDataToTable,font=("times new roman",12,"bold"),bg="pink",fg="black")
        view_btn.grid(row=0,column=17,padx=10)

        ex_btn=Button(R_frame,text="Export",command=self.export, width=12,font=("times new roman",12,"bold"),bg="pink",fg="black")
        ex_btn.grid(row=0,column=19,padx=5)


        
        lblPathNm=Label(R_frame,text="Folder Path:",width=12,font=("times new roman",12,"bold"),fg="black")
        lblPathNm.grid(row=0,column=35,padx=5)
        
        lblFullPath=Button(R_frame,text="Browse file",width=12,command=self.browseFiles,font=("times new roman",12,"bold"),fg="black")
        lblFullPath.grid(row=0,column=45,padx=5)
        
        
#==========================First Table================================================
        table_frame=Frame(R_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=80,width=width-25,height=height-150)
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.stud_table=ttk.Treeview(table_frame,column=("roll","name","days","per"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.stud_table.xview)
        scroll_y.config(command=self.stud_table.yview)
        
        self.stud_table.heading("roll",text="RollNo")
        self.stud_table.heading("name",text="Name")
        self.stud_table.heading("days",text="Number of days present ")
        self.stud_table.heading("per",text="Percentage")
        
        
        self.stud_table["show"]="headings"
        self.stud_table.column("roll",width=50)
        self.stud_table.column("name",width=150)
        self.stud_table.column("days",width=50)    
        self.stud_table.column("per",width=50)       
        self.stud_table.pack(fill=BOTH,expand=1)


    def GetBindDataToTable(self):
        if self.ToDt.get()=="":
            messagebox.showerror("Error","Select Date",parent=self.root)
            return
               
        self.stud_table.delete(*self.stud_table.get_children())
        try:
            query2=" select zz.rollno,zz.fullname,sum(prcnt), to_char((sum(prcnt)*100)/(case when totDays=0 then 1 else totDays end),999.99),totDays  from ( "
            query2=query2+" select s.rollno,s.fullname,(case when nvl(a.ISPRESENT,0)='0' then 0 else 1 end) prcnt,"
            query2=query2+" ((abs(to_date('"+self.frmDt.get()+"','dd-mm-yyyy')-to_date('"+self.ToDt.get()+"','dd-mm-yyyy'))+1)-"   
            query2=query2+" floor((abs(to_date('"+self.frmDt.get()+"','dd-mm-yyyy')-to_date('"+self.ToDt.get()+"','dd-mm-yyyy'))+1)/7)) totDays "
            query2=query2+" from student_mst s left join attendace a on a.srno=s.srno and a.rollno=a.rollno and odt between "
            query2=query2+" to_date('"+self.frmDt.get()+"','dd-mm-yyyy') and to_date('"+self.ToDt.get()+"','dd-mm-yyyy'))zz "
            query2=query2+" group by zz.rollno,zz.fullname,totDays order by rollno"
            
            print(query2)
            db_connection = con.connect(connString)
            db_cursor = db_connection.cursor()
            db_cursor.execute(query2)
            rows=db_cursor.fetchall()
            db_connection.close()
            if(db_cursor.rowcount>0):
                
                for row in rows:
                    print("**********Got Data*********")
                    self.stud_table.insert("",'end',text=str(row),values=(row))
        except  Exception as e:
            db_connection.close()
            print(e)
            messagebox.showinfo('Information', "Data fetching error!!!")
 
    
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

    def export(self):
        workbook = xlsxwriter.Workbook(r'CLSWISEATDNC.xlsx')
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
        messagebox.showinfo('Information', "Attendance Exported Successfully")
        return
    #================================browse file=======================================
    def browseFiles(self):
        filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
        if filename:
            try:
                self.settings["template"].set(filename)
            except: 
                tkMessageBox.showerror("Open Source File", "Failed to read file \n'%s'"%filename)
        
    

        
if __name__ == "__main__":
    root=Tk()
    obj=FRReport_Per(root)
    root.mainloop()


