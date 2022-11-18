# Lab 5 
# Topics: Function concepts, String and File operations
# Date :18/11/2021
# By Firat



# Defining a function and calling a function  
"""
def drawLine():
    print ("--------------")

drawLine()
"""

# Defining a function with a parameter  
"""
def drawLine(s):
    
    print (s*10)

drawLine("*")
drawLine("?")
drawLine("-")
"""
# Defining a function with parameters  
"""
def drawLine(s,size):
    
    print (s*size)

drawLine("*",20)
drawLine("?",10)
drawLine("-",20)
"""
# Defining a function with parameters  -v2

def drawLine(s,size):
    
    print (s*size)
"""
drawLine(size=20,s="*")
drawLine(s="?",size=10)
drawLine(s="-",size=20)
"""

# Function with return

def getuserinput(msg):
    sign=input(msg)
    return sign
"""
x=getuserinput(msg="please enter a char")
drawLine(size=20,s=x)
"""

# function call whithin a function

def showMsg(msg,boxsize=20,sign="*"):
    """
    this function shows a message in a box

    """
    drawLine(size=boxsize,s=sign)
    msgsize=len(msg)
    sizesideline=int((boxsize-msgsize)/2)
    print (sizesideline*sign,msg,sizesideline*sign)
    drawLine(size=boxsize,s=sign)
"""
m=getuserinput(msg="please enter your msg")
showMsg(m)
showMsg(m,sign="$")
showMsg(m,sign="*",boxsize=10)
"""


# file operations (input file) ex1
"""
f = open("poem.txt","r")
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
line4 = f.readline()
line5 = f.readline()
line6 = f.readline()
f.close()
print (line1 + line2 + line3+ line4+ line5+line6)
"""

# file operations ex2
"""
f = open("poem.txt","r")
while True:
    line = f.readline()
    if line=="":
        break
    print (line)
f.close()
"""

# file operations ex3
"""
f = open("poem.txt","r")
for line in f:
    print (line)
f.close()
"""
# file operations (output file)ex4
"""
f = open("poem.txt","a")
mystr="This is my newline"
f.write(mystr)
f.close()
"""

# file operations (reading a record ) ex5
"""
f = open("studentrecord.txt","r")
for line in f:
    s=line.strip() # Strip off the \n
    strings=s.split(":") # Split the string
    print (strings)
f.close()
"""
# file operations (reading records and search a record) ex6
"""
records=[]
f = open("studentrecord.txt","r")
for line in f:
    s=line.strip() # Strip off the \n
    record=s.split(":") # Split the string
    records.append (record)
f.close()

#print (records)

for record in records:
    if record[0]=='A111111':
        print ("he is here")
        print (record)
"""
# file operation and funtions ex6 v2

records=[]
def getStudentRecords():  
    f = open("studentrecord.txt","r")
    for line in f:
        s=line.strip() # Strip off the \n
        record=s.split(":") # Split the string
        records.append (record)
    f.close()
    
def findStudent(s_id):
    for record in records:
        if record[0]==s_id:
            return record
    return "this student is not in the system"
"""
getStudentRecords()
student=findStudent(s_id='A111111')
print (student)
student=findStudent(s_id='A222222')
print (student)        
"""







































