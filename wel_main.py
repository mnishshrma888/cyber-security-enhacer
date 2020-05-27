from tkinter import*
from tkinter import messagebox
import sqlite3
def welcome():
    
    db=sqlite3.connect("test.db")
    conn=db.cursor()
    def register ():
        def insert():
            a=t1.get()
            b=t2.get()
            c=t3.get()
            d=t4.get()
            f=t5.get()
            g=var.get()
            fn=re.findall("[0-9.?!@#$%^&*()_=<>]",a)
            ln=re.findall("[0-9.?!@#$%^&*()_=<>]",b)
            em=re.findall(r'[\w\.-]+@[\w\.-]+',d)
            
            if a=='' or b=='' or c=='' or d=='' or f=='':
                messagebox.showinfo("warning","please enter the all details")
            elif fn!=[] or ln!=[] or em==[]:
                messagebox.showinfo("warning","please enter the correct details")
            else:
                

                sql="""INSERT INTO COUSTOMER(FIRST_NAME,
                LAST_NAME,USER_NAME,EMAIL,PASSWORD,GENDER)
                VALUES(?,?,?,?,?,?)"""
                try:
                    conn.execute(sql,(a,b,c,d,f,g,))
                    db.commit()
                    l7.config(text="Registered Successfully")
                except Exception as e:
                    print(e)
                    db.rollback()
        register=Tk()
        width_of_window=250
        height_of_window=300
        screen_width=register.winfo_screenwidth()
        screen_height=register.winfo_screenheight()
        x=(screen_width/2)-(width_of_window/2)
        y=(screen_height/2)-(height_of_window/2)
        register.geometry("%dx%d+%d+%d"%(width_of_window,height_of_window,x,y)) 
        register.title("REGISTER")
        l1=Label(register,text="firstname",bg="darkblue",fg="white")
        t1=Entry(register,bd=5)
        l2=Label(register,text='lastname',bg="darkblue",fg="white")
        t2=Entry(register,bd=5)
        l3=Label(register,text="username",bg="darkblue",fg="white")
        t3=Entry(register,bd=5)
        l4=Label(register,text="email",bg="darkblue",fg="white")
        t4=Entry(register,bd=5)
        l5=Label(register,text="password",bg="darkblue",fg="white")
        t5=Entry(register,bd=5)
        l6=Label(register,text="gender",bg="darkblue",fg="white")
        l7=Label(register,text="")
        var=StringVar()
        b1=Radiobutton(register,text='male',variable=var,value='M')
        b2=Radiobutton(register,text='female',variable=var,value='F')
        b=Button(register,text='register',command=insert,bg="darkblue",fg="white")
        b3=Button(register,text='close',command=register.destroy,bg="darkblue",fg="white")
        l1.pack()
        l1.place(x=10,y=20)
        t1.pack()
        t1.place(x=70,y=20)
        l2.pack()
        l2.place(x=10,y=50)
        t2.pack()
        t2.place(x=70,y=50)
        l3.pack()
        l3.place(x=10,y=80)
        t3.pack()
        t3.place(x=70,y=80)
        l4.pack()
        l4.place(x=10,y=110)
        t4.pack()
        t4.place(x=70,y=110)
        l5.pack()
        l5.place(x=10,y=140)
        t5.pack()
        t5.place(x=70,y=140)
        l6.pack()
        l6.place(x=10,y=170)
        l7.pack()
        l7.place(x=80,y=250)
        b1.pack()
        b1.place(x=60,y=170)
        b2.pack()
        b2.place(x=110,y=170)
        b.pack()
        b.place(x=150,y=210)
        b3.pack()
        b3.place(x=80,y=210)
        register.mainloop()

    def login():

        def check():
            a=t1.get()
            b=t2.get()
            if a=='' or b=='':
                messagebox.showinfo("warning","please enter the all details")
            else:
                
                try:
                    sql=" SELECT * FROM COUSTOMER Where USER_NAME=? and PASSWORD=? "
                    conn.execute(sql,(a,b,))
                    c=conn.fetchall()
                    if c==[]:
                        messagebox.showinfo("warning","enter valid username and password")
                        login.destroy()
                    for i in c:
                        if a==i[2] and b==i[4]:
                            welcome.destroy()
                            login.destroy()
                            import cyberpro
                            
                        db.commit()
                except Exception as e:
                    print(e)
                    db.rollback()
        


        login=Tk()
        width_of_window=250
        height_of_window=300
        screen_width=login.winfo_screenwidth()
        screen_height=login.winfo_screenheight()
        x=(screen_width/2)-(width_of_window/2)
        y=(screen_height/2)-(height_of_window/2)
        login.geometry("%dx%d+%d+%d"%(width_of_window,height_of_window,x,y))
        login.title("LOGIN")
        l1=Label(login,text="username",bg="darkblue",fg="white")
        t1=Entry(login,bd=5)
        l2=Label(login,text="password",bg="darkblue",fg="white")
        t2=Entry(login,bd=5)
        l7=Label(login,text="")
        b=Button(login,text="LOGIN",command=check,bg="darkblue",fg="white")
        b3=Button(login,text='close',command=login.destroy,bg="darkblue",fg="white")
        b.pack()
        b.place(x=150,y=100)
        b3.pack()
        b3.place(x=80,y=100)
        l1.pack()
        l1.place(x=10,y=20)
        t1.pack()
        t1.place(x=70,y=20)
        l2.pack()
        l2.place(x=10,y=60)
        t2.pack()
        t2.place(x=70,y=60)
        l7.pack()
        l7.place(x=80,y=120)

    welcome=Tk()
    width_of_window=1200
    height_of_window=700
    screen_width=welcome.winfo_screenwidth()
    screen_height=welcome.winfo_screenheight()
    x=(screen_width/2)-(width_of_window/2)
    y=(screen_height/2)-(height_of_window/2)
    welcome.geometry("%dx%d+%d+%d"%(width_of_window,height_of_window,x,y))
    welcome.title("WELCOME")

    '''sql="""CREATE TABLE COUSTOMER(FIRST_NAME CHAR(20) ,
            LAST_NAME CHAR(20),
            USER_NAME CHAR(20) NOT NULL,
            EMAIL CHAR(20),
            PASSWORD CHAR(10),
            GENDER CHAR(5))"""
    conn.execute(sql)'''
    b3=Button(welcome,text='REGISTER',command=register,font=("Courier",30),bg="darkblue",fg="white")
    b4=Button(welcome,text='LOGIN',command=login,font=("Courier",30),width=9,bg="darkblue",fg="white")
    b3.pack()
    b3.place(x=480,y=300)
    b4.pack()
    b4.place(x=480,y=400)

welcome()
