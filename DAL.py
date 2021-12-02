import cx_Oracle
#import config

connString = 'FRAS/FRAS@localhost:1521/xe'
def __init__():
    return

def getDbConn():
  return connString




def executeQuery(queryStr):
    try:
        con = cx_Oracle.connect(connString)        
        cursor = con.cursor()
        cursor.execute(queryStr)
        con.commit()
        if cursor:
            cursor.close()
        if con:
            con.close()

        print("Data selected Successfully..")
    except cx_Oracle.DatabaseError as e:
        con.rollback()
        if cursor:
            cursor.close()
        if con:
            con.close()

def GetDataTableText(queryStr):
    try:
        con = cx_Oracle.connect(connString)
        print(con.version)
        cursor = con.cursor()
        cursor.execute(queryStr)
        myresult = cursor.fetchall()
        return myresult
        
    except cx_Oracle.DatabaseError as e:
        print("There is a problem with Oracle", e)
        return 'error'
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()

def GetToDayDate():
    try:
        query2="select to_char(sysdate,'dd/mm/yyyy') todydt,I_NAME FROM PROFILE where rownum=1 "
        db_connection = cx_Oracle.connect(connString)
        retval="Collage/Institute Name"
         
        db_cursor = db_connection.cursor()
        db_cursor.execute(query2)
        rows=db_cursor.fetchall()
        for row in rows:
            print("********Found Data***********")
            #self.save_btn['state'] = 'disabled'
            retval=str(row[0])+"  "+str(row[1])
        if db_cursor:
            db_cursor.close()
        if db_connection:
            db_connection.close()
        return retval
    except cx_Oracle.DatabaseError as e:
        print("There is a problem with Oracle", e)
        if db_cursor:
            db_cursor.close()
        if db_connection:
            db_connection.close()

        return retval
 

def GetCollgeNameText():
    try:
        query2="select I_NAME FROM PROFILE where rownum=1 "
        db_connection = cx_Oracle.connect(connString)
        retval="Collage/Institute Name"
         
        db_cursor = db_connection.cursor()
        db_cursor.execute(query2)
        rows=db_cursor.fetchall()
        for row in rows:
            print("********Found Data***********")
            #self.save_btn['state'] = 'disabled'
            retval=str(row[0])
        if db_cursor:
            db_cursor.close()
        if db_connection:
            db_connection.close()
        return retval
    except cx_Oracle.DatabaseError as e:
        print("There is a problem with Oracle", e)
        if db_cursor:
            db_cursor.close()
        if db_connection:
            db_connection.close()
        return retval
 
 



