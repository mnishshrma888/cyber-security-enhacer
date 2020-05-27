import requests
import pandas as pd
df=pd.read_csv("crimedata1.csv")
from tkinter import*
from tkinter import messagebox
import socket



def statewise():
    
    top1=Tk()
    width_of_window=400
    height_of_window=250
    screen_width=top1.winfo_screenwidth()
    screen_height=top1.winfo_screenheight()
    x=(screen_width/2)-(width_of_window/2)
    y=(screen_height/2)-(height_of_window/2)
    top1.geometry("%dx%d+%d+%d"%(width_of_window,height_of_window,x,y))
    top1.title("***STATEWISE ANALYSIS***")
    state_names=['SELECT','ANDHRA PRADESH', 'ARUNACHAL PRADESH', 'ASSAM', 'BIHAR', 'CHHATTISGARH', 'GOA', 'GUJARAT', 'HARYANA', 'HIMACHAL PRADESH', 'JAMMU & KASHMIR', 'JHARKHAND', 'KARNATAKA', 'KERALA', 'MADHYA PRADESH', 'MAHARASHTRA', 'MANIPUR', 'MEGHALAYA', 'MIZORAM', 'NAGALAND', 'ODISHA', 'PUNJAB', 'RAJASTHAN', 'SIKKIM', 'TAMIL NADU', 'TRIPURA', 'UTTAR PRADESH', 'UTTARAKHAND', 'WEST BENGAL',  'A & N ISLANDS', 'CHANDIGARH', 'D & N HAVELI', 'DAMAN & DIU', 'DELHI', 'LAKSHADWEEP', 'PUDUCHERRY']
    var1=StringVar(top1)
    var1.set(state_names[0])
    w=OptionMenu(top1,var1,*state_names)
    l1=Label(top1,text="STATE",bg="darkblue",fg="white")
    l1.pack()
    l1.place(x=110,y=50)
    w.pack()
    w.place(x=200,y=50)
    year=['SELECT',2012,2013,"BOTH"]
    var2=StringVar(top1)
    var2.set(year[0])
    w1=OptionMenu(top1,var2,*year)
    l2=Label(top1,text="year",bg="darkblue",fg="white")
    l2.pack()
    l2.place(x=110,y=80)
    w1.pack()
    w1.place(x=200,y=80)
    
    def ok():
        a=var1.get()
        b=var2.get()
        if a=="SELECT" or b=="SELECT":
            messagebox.showinfo("WARNING","Select the all options")
        elif b=='2012':
            l=df[(df.STATE==a)]
            m=l.iloc[:,1:12]
            print(m)
            print("done")
            k=m.plot.bar()
            fig = k.get_figure()
            fig.savefig("output.png")
        elif b=='BOTH':
            l=df[(df.STATE==a)]
            m=l.iloc[:,23:50]
            print(m)
            print("done")
            k=m.plot.bar()
            fig = k.get_figure()
            fig.savefig("output.png")
        else:
             l=df[(df.STATE==a)]
             m=l.iloc[:,12:23]
             print(m)
             print("done")
             k=m.plot.bar()
             fig = k.get_figure()
             fig.savefig("output.png")
        top1.destroy()

    button=Button(top1,text="ok",command=ok,width=10,bg="darkblue",fg="white")
    button.pack()
    button.place(x=260,y=130)
    button1=Button(top1,text="close",command=top1.destroy,width=10,bg="darkblue",fg="white")
    button1.pack()
    button1.place(x=110,y=130)
    top1.mainloop()       

def crimewise():
    top1=Tk()
    width_of_window=400
    height_of_window=250
    screen_width=top1.winfo_screenwidth()
    screen_height=top1.winfo_screenheight()
    x=(screen_width/2)-(width_of_window/2)
    y=(screen_height/2)-(height_of_window/2)
    top1.geometry("%dx%d+%d+%d"%(width_of_window,height_of_window,x,y))
    top1.title("***CRIMEWISE ANALYSIS***")
    crime_names=["SELECT",'Tampering computer source documents','Loss/Damage to computer resource/utility','Hacking','Obscene publication/transmission in electronic form','Faliure : Of compliance/Orders of Certifying Authority','Faliure : To assist in decrypting the information intercepted by Govt. Agency','Un-authorised access/attempt to access of protected Computer System','Publishing false digital Signature Certificate','Fraud Digital Signature Certificate','Breach of confidentiality/privacy','Other']
    var1=StringVar(top1)
    var1.set(crime_names[0])
    w=OptionMenu(top1,var1,*crime_names)
    l1=Label(top1,text="CRIME",bg="darkblue",fg="white")
    l1.pack()
    l1.place(x=110,y=50)
    w.pack()
    w.place(x=200,y=50)
    year=['SELECT',2012,2013,"BOTH"]
    var2=StringVar(top1)
    var2.set(year[0])
    w1=OptionMenu(top1,var2,*year)
    l2=Label(top1,text="year",bg="darkblue",fg="white")
    l2.pack()
    l2.place(x=110,y=80)
    w1.pack()
    w1.place(x=200,y=80)
    no=[0,1,2,3,4,5,6,7,8,9,10]
    var3=StringVar(top1)
    var3.set(no[0])
    w2=OptionMenu(top1,var3,*no)
    l3=Label(top1,text="maximum",bg="darkblue",fg="white")
    l3.pack()
    l3.place(x=110,y=110)
    w2.pack()
    w2.place(x=200,y=110)
    
   
    
    def ok():
        a=var1.get()
        b=var2.get()
        f=int(var3.get())
        if a=="SELECT" or b=="SELECT" or f==0:
            messagebox.showinfo("WARNING","Select the all options")
        elif b=="BOTH":
            e=df.nlargest(f,a).reset_index()
            d=e[["STATE",a]]
            print(d)
            print("done")
            k=d.plot(kind="bar",x="STATE",y=a)
            fig = k.get_figure()
            fig.savefig("output.png")
        else:
            c=a+b
            e=df.nlargest(f,c).reset_index()
            d=e[["STATE",c]]
            print(d)
            print("done")
            k=d.plot(kind="bar",x="STATE",y=c)
            fig = k.get_figure()
            fig.savefig("output.png")
        top1.destroy()
    button=Button(top1,text="ok",command=ok,width=10,bg="darkblue",fg="white")
    button.pack()
    button.place(x=260,y=150)
    button1=Button(top1,text="close",command=top1.destroy,width=10,bg="darkblue",fg="white")
    button1.pack()
    button1.place(x=110,y=150)
    top1.mainloop()

def software():
    
    top1=Tk()
    width_of_window=620
    height_of_window=250
    screen_width=top1.winfo_screenwidth()
    screen_height=top1.winfo_screenheight()
    x=(screen_width/2)-(width_of_window/2)
    y=(screen_height/2)-(height_of_window/2)
    top1.geometry("%dx%d+%d+%d"%(width_of_window,height_of_window,x,y))
    top1.title("***SOFTWARE SCANNER***")
    l1=Label(top1,text="Copy the path of software",bg="darkblue",fg="white")
    l1.pack()
    l1.place(x=10,y=50)
    output=Text(top1,width=70,height=1,fg="black")
    output.pack()
    output.place(x=40,y=120)
    l2=Label(top1,text="your scan id is :",bg="darkblue",fg="white")
    l2.pack()
    l2.place(x=10,y=120)
    l3=Label(top1,text="",font="10")
    l3.pack()
    l3.place(x=20,y=210)
    e1=Entry(top1,bd=5,width=40)
    e1.pack()
    e1.place(x=170,y=50)
    def ok():
        e=e1.get()
        print(e)
        if e=='':
            messagebox.showinfo("warning","please enter the url")
        else:
            url = 'https://www.virustotal.com/vtapi/v2/file/scan'
            params = {'apikey': '9ea535c2af0d3e17abdd4f019cc3100b16c4fb02f7945787b4e6c44281588e05'}
            files = {'file': (e, open(e, 'rb'))}
            response = requests.post(url, files=files, params=params)
            a=response.json()
            print(a)
            b=a['scan_id']
            output.insert(0.0,b)
            l3.config(text="Copy the Scan_id and check the report after sometime")

    button=Button(top1,text="ok",command=ok,width=10,bg="darkblue",fg="white")
    button.pack()
    button.place(x=290,y=170)
    button1=Button(top1,text="close",command=top1.destroy,width=10,bg="darkblue",fg="white")
    button1.pack()
    button1.place(x=140,y=170)
def url():
    
    top1=Tk()
    width_of_window=620
    height_of_window=250
    screen_width=top1.winfo_screenwidth()
    screen_height=top1.winfo_screenheight()
    x=(screen_width/2)-(width_of_window/2)
    y=(screen_height/2)-(height_of_window/2)
    top1.geometry("%dx%d+%d+%d"%(width_of_window,height_of_window,x,y))
    top1.title("***URL SCANNER***")
    l1=Label(top1,text="enter the url",bg="darkblue",fg="white")
    l1.pack()
    l1.place(x=50,y=50)
    output=Text(top1,width=70,height=1,fg="black")
    output.pack()
    output.place(x=40,y=120)
    l2=Label(top1,text="your scan id is :",bg="darkblue",fg="white")
    l2.pack()
    l2.place(x=10,y=120)
    l3=Label(top1,text="",font="10")
    l3.pack()
    l3.place(x=20,y=210)
    e1=Entry(top1,bd=5,width=40)
    e1.pack()
    e1.place(x=170,y=50)
    def ok():
        e=e1.get()
        print(e)
        if e=='':
            messagebox.showinfo("warning","please enter the url")
        else:
            url = 'https://www.virustotal.com/vtapi/v2/url/scan'
            params = {'apikey': '9ea535c2af0d3e17abdd4f019cc3100b16c4fb02f7945787b4e6c44281588e05', 'url':e}
            response = requests.post(url, data=params)
            a=response.json()
            print(a)
            print(type(a))
            b=a['scan_id']
            output.insert(0.0,b)
            l3.config(text="Copy the Scan_id and check the report after sometime")

    button=Button(top1,text="ok",command=ok,width=10,bg="darkblue",fg="white")
    button.pack()
    button.place(x=290,y=170)
    button1=Button(top1,text="close",command=top1.destroy,width=10,bg="darkblue",fg="white")
    button1.pack()
    button1.place(x=140,y=170)
def report():
    top1=Tk()
    width_of_window=700
    height_of_window=700
    screen_width=top1.winfo_screenwidth()
    screen_height=top1.winfo_screenheight()
    x=(screen_width/2)-(width_of_window/2)
    y=(screen_height/2)-(height_of_window/2)
    top1.geometry("%dx%d+%d+%d"%(width_of_window,height_of_window,x,y))
    top1.title("***REPORT***")
    l1=Label(top1,text="enter the scan id:",bg="darkblue",fg="white")
    l1.pack()
    l1.place(x=50,y=50)
    l2=Label(top1,text="")
    l2.pack()
    l2.place(x=10,y=120)
    e1=Entry(top1,bd=5,width=40)
    e1.pack()
    e1.place(x=170,y=50)
    output=Text(top1,width=85,height=200,fg="black")
    output.pack()
    output.place(x=10,y=200)
    def ok():
        e=e1.get()
        print(e)
        if e=='':
            messagebox.showinfo("warning","please enter the scan id")
        try:
            url1 = 'https://www.virustotal.com/vtapi/v2/file/report'

            params1 = {'apikey': '9ea535c2af0d3e17abdd4f019cc3100b16c4fb02f7945787b4e6c44281588e05', 'resource':e}

            response1 = requests.get(url1, params=params1)

            a=response1.json()
            print(a)
            for i in a:
                for j in a[i]:
                    for k in a[i][j]:
                        print(a[i][j])
                        output.insert(0.0,a[i][j])
        except:
            print("")

    button=Button(top1,text="ok",command=ok,width=10,bg="darkblue",fg="white")
    button.pack()
    button.place(x=290,y=170)
    button1=Button(top1,text="close",command=top1.destroy,width=10,bg="darkblue",fg="white")
    button1.pack()
    button1.place(x=140,y=170)

def port_scanner():
    top1=Tk()
    width_of_window=500
    height_of_window=600
    screen_width=top1.winfo_screenwidth()
    screen_height=top1.winfo_screenheight()
    x=(screen_width/2)-(width_of_window/2)
    y=(screen_height/2)-(height_of_window/2)
    top1.geometry("%dx%d+%d+%d"%(width_of_window,height_of_window,x,y))
    top1.title("***PORT SCANNER***")
    l1=Label(top1,text="what web to scan:",bg="darkblue",fg="white")
    l1.pack()
    l1.place(x=50,y=50)
    l2=Label(top1,text="Port_no",bg="darkblue",fg="white")
    l2.pack()
    l2.place(x=50,y=90)
    port_no=['SELECT',21,22,23,25,53,135,433,1433]
    var1=StringVar(top1)
    var1.set(port_no[0])
    w=OptionMenu(top1,var1,*port_no)
    w.pack()
    w.place(x=165,y=90)
    l2=Label(top1,text="")
    l2.pack()
    l2.place(x=10,y=210)
    l3=Label(top1,text="")
    l3.pack()
    l3.place(x=12,y=230)
    e1=Entry(top1,bd=5,width=40)
    e1.pack()
    e1.place(x=170,y=50)
    def ok():
        e=e1.get()
        c=var1.get()
        print(e)
        if e==''or c=="SELECT":
            messagebox.showinfo("warning","please enter all options")
        try:
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            target=e
            b=int(c)
            def pscan(b):
                try:
                    con=s.connect((target,b))
                    return True
                except:
                    return False
            dic={21:'Packet Sniffing,  Bounce attack',22:'Brute Force attack',23:'DDOS,  Virtualmachine connection',25:'Account enumeration,  Countermeasures against SMTP relay attack',53:'DDOS-Amplification, Reflection',443:'Click Jacking, Traffic outbound',135:'Botnet attack',1433:'Microsoft SQL Brute force attack'}
            if pscan(b):
                print(" Port %d Open"%b)
                l2.config(text=" Port %d Open"%b)
                l3.config(text="Possible attacks are :%s"%dic[b])
            else:
                print(" Port %d close"%b)
                l2.config(text=" Port %d close"%b)
                l3.config(text="")
        except Exception as e:
            print(e)
    button=Button(top1,text="ok",command=ok,width=10,bg="darkblue",fg="white")
    button.pack()
    button.place(x=290,y=170)
    button1=Button(top1,text="close",command=top1.destroy,width=10,bg="darkblue",fg="white")
    button1.pack()
    button1.place(x=140,y=170)


    
top=Toplevel()
top.geometry("1200x900")
width_of_window=1200
height_of_window=700
screen_width=top.winfo_screenwidth()
screen_height=top.winfo_screenheight()
x=(screen_width/2)-(width_of_window/2)
y=(screen_height/2)-(height_of_window/2)
top.geometry("%dx%d+%d+%d"%(width_of_window,height_of_window,x,y))
top.title("MAIN")
menubar=Menu(top)
amenu=Menu(menubar,tearoff=0)
amenu.add_command(label="Statewise",command=statewise)
amenu.add_command(label="Crimewise",command=crimewise)
amenu.add_separator()
amenu.add_command(label="Exit",command=top.destroy)
menubar.add_cascade(label="Analysis",menu=amenu)
bmenu=Menu(menubar,tearoff=0)
bmenu.add_command(label="Software Scan",command=software)
bmenu.add_command(label="URL Scan",command=url)
bmenu.add_command(label="Report",command=report)
bmenu.add_separator()
bmenu.add_command(label="Exit",command=top.destroy)
menubar.add_cascade(label="Virus Scanner",menu=bmenu)
top.config(menu=menubar)
cmenu=Menu(menubar,tearoff=0)
cmenu.add_command(label="Port Scan",command=port_scanner)
cmenu.add_separator()
cmenu.add_command(label="Exit",command=top.destroy)
menubar.add_cascade(label="Port Scanner",menu=cmenu)
top.config(menu=menubar)
img=PhotoImage(file="C:/Users/SAMSUNG/Desktop/New folder/ab.png")
l5=Label(top,image=img,height=700,width=1200,anchor=NW)
l5.pack()
l5.place(x=0,y=0)
top.mainloop()
   
