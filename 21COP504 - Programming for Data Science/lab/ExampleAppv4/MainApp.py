
# Topic: Application Development File Operation with Menu
# Date:
# By Firat Batmaz
# Version 4: use of pandas module
"""
Main App functions 
"""
import fileoperations as db

def say_hello():
    print ("hello")
def say_bye():
    print ("bye")

def list_student_marks(): #updated 
    #print (testMarks.to_string(index=False))#without index number
    print(testMarks) #new 

def update_student_mark(name,mark): #updated 

    testMarks.loc[testMarks["name"]==name,"mark"]=mark #new
def add_student_mark(name,mark): #updated 
    global testMarks #new
    studentMark={"name":name,"mark":mark}
    testMarks=testMarks.append(studentMark,ignore_index=True) #new 
    print ("New student mark has been added successfully.")
    
    
def display_menu():
    """
    Building Menu Options
    
    """
    print ("\n")
    print ("**********************")
    print ("*------Menu----------*")
    print ("**********************")
    print ("Please select an option below")
    print ("\t(h) say 'hello'")
    print ("\t(r) read student marks from the file")
    print ("\t(g) get student marks from the db")
    print ("\t(l) list student marks")
    print ("\t(a) add a student mark")
    print ("\t(u) update a student mark")
    print ("\t(s) save student marks to the file")
    print ("\t(d) save student marks to the db")
    print ("\t(b) say 'bye'")

#################################################
#------------------Main-------------------------#
#################################################


while True:
    display_menu()
    menuoption=input("\t\n:>") 
    if menuoption=="h":
        say_hello()
    elif menuoption=="b":
        say_bye()
        break 
    elif menuoption=="r":
        testMarks=db.read_student_marks_from_file()
    elif menuoption=="l":
        list_student_marks()
    elif menuoption=="g":
        testMarks=db.read_student_marks_from_db()
    elif menuoption=="a":
        add_student_mark("tim",80)
    elif menuoption=="u":
        update_student_mark("tom",90)
    elif menuoption=="s":
        db.save_student_marks_into_file(testMarks)
    elif menuoption=="d":
        db.save_student_marks_into_db(testMarks)
    else:
        print ("sorry we don't have that option")

