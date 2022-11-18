"""
Database and File operations

"""

import sqlite3
import pandas as pd #new

def save_student_marks_into_db(dfTestMarks): #updated
    try:
        sqliteConnection = sqlite3.connect('studentDB.db')
        print("Connected to SQLite")
        dfTestMarks.to_sql("TestMark",       #new 
                           sqliteConnection,
                           if_exists='append',
                           index=False)

        print("student records have been inserted successfully into the TestMark table")

        sqliteConnection.close()
    except sqlite3.Error as error:
        print("Failed to insert student records into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")

def read_student_marks_from_db(): #updated 
    
    try:
        sqliteConnection = sqlite3.connect('studentDB.db')
        print("Connected to SQLite")
            
        sqlite_read_record_query = """ SELECT *             
                                       FROM TestMark"""
        
        dfTestMarks=pd.read_sql(sqlite_read_record_query, #new
                                sqliteConnection)

        sqliteConnection.close()
    except sqlite3.Error as error:
        print("Failed to insert a new student record into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")
    return dfTestMarks


def read_student_marks_from_file(): #updated 
    

    dfTestMarks=pd.read_csv("testmark.txt") #new


    return dfTestMarks

def save_student_marks_into_file(dfTestMarks): # updated
    dfTestMarks.to_csv("testmark.txt",index=False) #new

#new testing code 
if __name__=="__main__":  
   #testing the functions 
    sampleData={"name":["bob","tom"],
                "mark":["60","70"]
        }
    
    dfSampleData=pd.DataFrame(sampleData)
    save_student_marks_into_file(dfSampleData)
    x=read_student_marks_from_file()
    print(x)
    
    x=read_student_marks_from_db()
    save_student_marks_into_db(x)
    x=read_student_marks_from_db()
    print(x)
    
