

import pymysql as m
import getpass as g
import time as t
import sys as s


global p,d,db,c,a


w="x"

p='3071'
d='data'

db = m.connect(user='root', password=p,host='localhost',database="data")
c= db.cursor()

def datab():
    c=db.cursor()
    c.execute(("create database if not exists {};").format(d))
    c.execute(("use {};").format(d))
    



def tbl():
    c.execute("create table if not exists biodata(uid int primary key,roll int,name varchar(255),dob date,classs int,address varchar(255),contact bigint,mail varchar(90),age int);")
    c.execute("create table if not exists work(uids int,phy_copycheck varchar(22),chem_copycheck varchar(22),eng_copycheck varchar(22),maths_copycheck varchar(22),cs_copycheck varchar(22),hindi_copycheck varchar(22),bio_copycheck varchar(22),foreign key (uids) references biodata(uid) on delete cascade on update cascade); ") 
    c.execute("create table if not exists remark(uids int,remarks varchar(255),suggestions varchar(255),fees_pending varchar(255), foreign key (uids) references biodata(uid) on delete cascade on update cascade);")
    
tbl()

    
def gap(x):
    print("\n"*x)
    return " "
    


def selection():
    datab()
    tbl()
    
    db = m.connect(user='root', password=p,host='localhost',database=d)
    print('-----------------------------------\nWELCOME TO STUDENT MANAGEMENT SYSTEM\n-----------------------------------')
    print("1 :- STUDENT\'s BIODATA")
    print("2 :- STUDENT\'s  CLASSWORKS")
    print("3 :- STUDENT\'s  REMARKS")
    print("4 :- TO REMOVE A STUDENT")
    print("5 :- TO JOIN MULTI TABLES AND VIEW")
    print("6 :- TO UPDATE RECORD")
    print("7 :- CUSTOM QUERY")
    mi()
    

    
def mi():
    for i in range(1):
        ch=int(input("\nEnter your choice (1-7) : "))        
        if ch==1:
            a=input("want to insert -> enter 1 \nwant to see -> nothing : ")
            if a=="1":
                i1()
            elif a=="":
                d1() 
            
        elif ch==2:                
           a=input("want to insert -> enter 1 \nwant to see -> nothing : ")
           if a=="1":
               i2()
           elif a=="":
               d2() 
    
        elif ch==3:   
            a=input("want to insert -> enter 1 \nwant to see -> nothing : ")
            if a=="1":
                i3()
            elif a=="":
                d3() 
                
        elif ch==4: 
            d4()
        
        elif ch==5:
            d5()
        elif ch==6:
            u()
        elif ch==7:
            tom()
        else:
            print("\nenter valid numbers only..")
            mi()
            
         
        
def slow(x,y=0.2):
    for i in x.split():
        s.stdout.write(i+" ")
        t.sleep(y)
    return " "    

        

def password():
    o=t.ctime()
    o=o.split()
    o=o[3].split(":")
    o=o[0]+o[1]
    return(o)



def pass_():
    
    r=g.getpass(prompt="ENTER PASSWORD -> ")
    password()
    w="x"
    if r==password():
        print("\nPASSWORD CORRECT....",time())
        while w=="x" or w=="X":

            selection()
            w=input("continue to menu press [x] -> ")
        else:
            slow("\nthx for using this project..\n please visit again..")
            

    else:
        slow("\nPASSWORD WRONG..ENTER CORRECT PASSWORD..")
        print()
        pass_()



        
def i1():
    uids=int(input("enter uid of student : "))
    roll=int(input("enter roll no. : "))
    names=input("Enter Student Name : ")
    dob=input("Enter Date of Birth(yyyy-mm-dd): ")
    classs=int(input("Enter class : "))
    address=input("enter address of student : ")
    cont=int(input ("enter contact no. : "))
    mail=input("enter email id : ")
    age=int(input("enter age : "))
    
    sql="INSERT INTO biodata VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(uids,roll,names,dob,classs,address,cont,mail,age)
    try:
        c.execute(sql)
        db.commit()
        slow("\ncommitted ->")
        a=input("want to enter more...[y] -> ")
        if a=="y" or a=="Y":
            i1()
    except:
        print("execution error")        
        db.rollback()
        db.close()
    


        
        
        
def i3():
    uid=input("Enter Student uid : ")
    rem=input("Enter your remarks : ")
    sug=input("any suggections : ")
    fee=input("is any fee pending : ")
    db = m.connect(user='root', password=p,host='localhost',database=d)
    c = db.cursor()
    sql="INSERT INTO remark VALUES ( '{}','{}','{}','{}')".format(uid,rem,sug,fee) 
    try:
        c.execute(sql)
        db.commit()
        print("committed ->")
        a=input("want to enter more...[y] -> ")
        if a=="y" or a=="Y":
            i3()
    except:
        print("execution error")
        db.rollback()
        db.close()
    



        
def tom():
    print("""tables and columns for your convinience ->
    <biodata>       <remark>            <class>              
    uid             remarks             disturb
    roll            uids                attention  
    name            suggestions         regular_copycheck                                
    dob                                 project_submit
    classs                              manners_
    addres                              anything_else
    contact                   
    mail                                     
    age                       
""",gap(1))
    i=input("enter query syntax including [;] ->\n")
    try:
        c.execute(i)
        print("executed ->")
        m=c.fetchall()
        for n in m:
            print(n)
        a=input("more query...[y] -> ")
        if a=="y" or a=="Y":
            tom()
        
            
            
    except:
        print("execution error\n")
        db.rollback()
        db.close()

        
        
        

def i2():
    uids=input("Enter uid of student: ")    
    phy=input("Is phy copy checked? :")
    chem=input("Is chem copy checked? : ")
    eng=input("is eng copy checked? :")
    math=input("is maths copy checked? :")
    cs=input("is cs copy checked? :")
    hindi=input("is hindi copy checked? : ")
    bio=input("is bio copy checked? : ")
    db = m.connect(user='root', password=p, host='localhost',database=d)
    c = db.cursor()
    sql="INSERT INTO class VALUES ('{}','{}', '{}','{}','{}','{}','{}','{}')".format(uids,phy,chem,eng,math,cs,hindi,bio)
    try:
        c.execute(sql)
        db.commit()
        print("committed ->",gap(1))
        a=input("want to enter more...[y] -> ")
        if a=="y" or a=="Y":
            i2()
            
    except:
        print("execution error",gap(1))
        db.rollback()
        db.close()
    
    
    
        

         
         
         
def d3():
    try:
        db = m.connect(user='root', password=p, host='localhost',database=d)
        c = db.cursor()
        c = db.cursor()
        field=input("""enter colunm from:
uid : remarks : suggections : fee_pending : *[ALL] : -> """)             
        cond=input("enter your condition syntax as \n <where > <condition>  -> ")
        sql="select {} from remark {" "};".format(field,cond)
        c.execute(sql)
        results = c.fetchall()
        for i in results:
            print(i)
            
        a=input("want to show again??? [y] -> ")
        if a=="y" or a=="Y":
            d3()

    except:
        print ("Error: unable to fetch data",gap(1))
        
        a=input("want to show again??? [y] -> ") 
        if a=="y" or a=="Y":
            d3()  
        db.close()
    

    
        
        
def d1():
    try:
        db = m.connect(user='root', password=p, host='localhost',database=d)
        c = db.cursor()
        a=print('''to show  record ->''')
        field=input("""enter colunm from->
uid :  roll : name : dob : classs : address : contact : mail : age : *[ALL] :  """)
        cond=input("enter your condition syntax as \n <where> <condition> -> ")
        sql="select {} from biodata {" "};".format(field,cond)
        c.execute(sql)
        results = c.fetchall()
        for i in results:
            print(i)
        a=input("want to show again??? [y] -> ")
        if a=="y" or a=="Y":
            d1()
    except:
        print ("Error: unable to fetch data",gap(1))
        
        a=input("want to show again??? [y] -> ")
        if a=="y" or a=="Y":
            d1()
        db.close()
    

     
         
         
def d2():
    try:
        db = m.connect(user='root', password=p, host='localhost',database=d)
        c = db.cursor()        
        field=input("""enter colunm from:
uids : phy_copycheck : chem_copycheck : eng_copycheck : maths_copycheck 
cs_copycheck : hindi_copycheck : bio_copycheck : *[ALL] :""")
        cond=input("enter your condition syntax as \n <where> <conditions>  -> ")
        sql="select {} from class {" "};".format(field,cond)
        c.execute(sql)
        results = c.fetchall()
        for i in results:
            print(i)
        a=input("want to show again??? [y] -> ")
        if a=="y" or a=="Y":
            d2()                  
    except:
        print ("Error: unable to fetch data",gap(1))
        
        a=input("want to show again??? [y] -> ")
        if a=="y" or a=="Y":
            d2()
        db.close()
    



def d4():
    try:
        db = m.connect(user='root', password=p, host='localhost',database=d)
        c= db.cursor()
        a=int(input ("enter uid no :"))
        sql = "delete from biodata where uid={};".format(a) 
        ans=input("Are you sure you want to delete the record  [y] -> ")
        if ans=='y' or ans=='Y':
            c.execute(sql)
            db.commit()
            print("uid deleted\ncommitted ",gap(1))
  
        a=input("want to see the table now? [y] -> ")
        if a=="y" or a=="Y":
            sql="select * from biodata;"
            c.execute(sql)
            results = c.fetchall()
            for c in results:
                print(c)
        
        n=input("WANT TO DELETE MORE??...[y] -> ")
        if n=="y" or n=="Y":
            d4()
            
        
    except:
        db.close()

    



def d5():
    global db,d
    try:
        db = m.connect(user='root', password=p, host='localhost',database=d)
        c = db.cursor()
        i=input("""\t\nenter colunm <separated by ','> which u want to see :

<biodata>       <work>               <remark>          *[ALL]
uid             uids                  remarks
roll            eng_copycheck         uids
name            phy_copycheck         suggestions  
dob             chem_copycheck        fees_pending
classs          maths_copycheck                     
addres          cs_copycheck                     
contact         hindi_copycheck           
mail            bio_copycheck                          
age                        
                          
-> """)


        tk=input("""\t\nenter tables <separated by ','> from:
biodata     remark      class
-> """)

        
        #d=input("enter tables you are connecting using 'uid(s)'\nuse *uid* for biodata and *uids* for rest of the colomns\nfor eg:<tbl_1.uid=tbl_2=uids=tbl_3=uids> \n -> ")
        h=input("enter your condition syntax here as \n <and> <conditions> <or>/<and>\nfor eg:and con_1 or/and con_2> \n -> ")
        
        
        sql="select {} from {} where uid=uids {" "};".format(i,tk,h)
        c.execute(sql)
        d=c.fetchall()
        for i in d:
            print(i)
        a=input("want to show again??? [y] ->") 
        if a=="y" or a=="Y":
            d5()
        
      
        
    except:
        print ("Error: unable to fetch data",gap(1))
        a=input("want to show again??? [y] -> ")
        if a=="y" or a=="Y":
            d5()
        db.close()
    
   
        
        

def time():
    for i in range(5):
        s.stdout.write("\r   | ")
        t.sleep(0.1)
        s.stdout.write("\r   / ")
        t.sleep(0.1)    
        s.stdout.write("\r   - ")
        t.sleep(0.1)
        s.stdout.write("\r   \ ")
        t.sleep(0.1)
        s.stdout.write("\r   | ")
        t.sleep(0.1)
        s.stdout.write("\r   / ")
        t.sleep(0.1)    
        s.stdout.write("\r   - ")
        t.sleep(0.1)
        s.stdout.write("\r   \ ")
        t.sleep(0.1)
    return " "
    


def u():
    db = m.connect(user='root', password=p, host='localhost',database=d)
    c=db.cursor()
    print("""tables and columns for your convinience ->

<biodata>       <work>               <remark>          *[ALL]
uid             uids                  remarks
roll            eng_copycheck         uids
name            phy_copycheck         suggestions  
dob             chem_copycheck        fees_pending
classs          maths_copycheck                     
addres          cs_copycheck                     
contact         hindi_copycheck           
mail            bio_copycheck                          
age                        
                          
-> """,gap(1))

    a=input("enter table to update -> ")
    b=input("enter old value -> ")
    c=input("enter new value -> ")
    cond=input("enter your condition syntax as \n <where> <condition> -> ")
    sql="update {} set {}={} {" "};".format(a,b,c,cond)
    try:
        c.execute(sql)
        db.commit()
        print("committed ->",gap(1))
        a=input("want to update more...[y] -> ")
        if a=="y" or a=="Y":
            u()
            
    except:
        print("execution error",gap(1))
        db.rollback()
        db.close()
    
    
    

slow("project is starting in few sec....")
print("\n")
slow("This project is a prototype .. further advancements can be done in future based on requirements...\n")
print("\n")                                
slow("\nthis is school info thus we put a password lock here to ensure any misshappen,incase any....\n")

pass_()