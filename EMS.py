import customtkinter as ctk
from tabulate import tabulate
import mysql.connector
con = mysql.connector.connect(host="localhost",user="root",password="ram2007",database="empdb")


r = ctk.CTk()
r.title("EMPLOYEE MANAGEMENT SYSTEM")
emp = ctk.CTkLabel(r,text = "EMPLOYEE DETAILS",text_color="red",font=("plasma",18))
emp.grid(row=0,column=4)
def Add_Option():
    Id = emp_id1.get()
    Name = emp_name1.get()
    Phono = emp_phono1.get()
    City = emp_city1.get()
    Salary = emp_salary1.get()
    cur = con.cursor()
    qry = "insert into employee(id,name,phono,city,salary) values (%s,%s,%s,%s,%s)"
    val = (Id,Name,Phono, City, Salary)
    cur.execute(qry,val)
    con.commit()

def Update_Option():
        Id = emp_id1.get()
        Name = emp_name1.get()
        Phono = emp_phono1.get()
        City = emp_city1.get()
        Salary = emp_salary1.get()
        cur = con.cursor()
        qry = "update employee set name=%s,phono=%s,city=%s,salary=%s where (id=%s)"
        val = (Name, Phono, City, Salary, Id)
        cur.execute(qry, val)
        con.commit()

def Delete_Option():
        Id = emp_id1.get()
        cur = con.cursor()
        qry = "delete from employee where (id=%s)"
        val = (Id,)
        cur.execute(qry, val)
        con.commit()

def Clear_option():
        emp_id1.delete(0,'end')
        emp_name1.delete(0,'end')
        emp_phono1.delete(0,'end')
        emp_city1.delete(0,'end')
        emp_salary1.delete(0,'end')

def View_Option():
        cur = con.cursor()
        qry = "select id,name,phono,city,salary from employee"
        cur.execute(qry)
        result = cur.fetchall()
        p=tabulate(result,headers=['id','name','phono','city','salary'],tablefmt="grid")
        f=open("emp tab.txt", "w")
        f.write(p)
        f.close()
        f1 = open("emp tab.txt", "r")
        print(f1.read())
        f1.close()

    #ID LABEL
emp_id = ctk.CTkLabel(r,text="ID",text_color="blue")
emp_id.grid(row=2,column=0,padx=20,pady=20,sticky='w')

    #ID ENTRY
emp_id1 = ctk.CTkEntry(r,placeholder_text="Enter Your ID",width=250)
emp_id1.grid(row=2,column=1,columnspan=3,pady=20,sticky='w')

    #NAME LABEL
emp_name = ctk.CTkLabel(r,text="NAME",text_color="blue")
emp_name.grid(row=3,column=0,padx=20,pady=20,sticky='w')

    #NAME ENTRY
emp_name1 = ctk.CTkEntry(r,placeholder_text="Enter Your NAME",width=250)
emp_name1.grid(row=3,column=1,columnspan=3,pady=20,sticky='w')

    #PHONO LABEL
emp_phono = ctk.CTkLabel(r,text="PHONE_NUMBER",text_color="blue")
emp_phono.grid(row=4,column=0,padx=20,pady=20,sticky='w')

    #PHONO ENTRY
emp_phono1 = ctk.CTkEntry(r,placeholder_text="Enter Your Phono Number",width=250)
emp_phono1.grid(row=4,column=1,columnspan=3,pady=20,sticky='w')

    #CITY LABEL
emp_city = ctk.CTkLabel(r, text="CITY", text_color="blue")
emp_city.grid(row=2, column=4, padx=20, pady=20, sticky='w')

    #CITY ENTRY
emp_city1 = ctk.CTkEntry(r, placeholder_text="Enter Your City", width=300)
emp_city1.grid(row=2, column=5, columnspan=3, pady=20, sticky='w')

    #SALARY LABEL
emp_salary = ctk.CTkLabel(r, text="SALARY", text_color="blue")
emp_salary.grid(row=3, column=4, padx=20, pady=20, sticky='w')

    #SALARY ENTRY
emp_salary1 = ctk.CTkEntry(r, placeholder_text="Enter Your Salary", width=300)
emp_salary1.grid(row=3, column=5, columnspan=3, pady=20, sticky='w')

    # ---> ADD  OPTION
add = ctk.CTkButton(r,text="add details",width=150,fg_color='green',command=Add_Option)
add.grid(row=6,column=0,padx=20,pady=20,sticky='w')

 #  INFORMATION
add_info = ctk.CTkLabel(r,text="--->  If you want to add the given details, fill it all widget then click that.",text_color="magenta2")
add_info.grid(row=6, column=1, columnspan=10,padx=20, pady=20, sticky='w')

    #---> UPDATE  OPTION
update = ctk.CTkButton(r, text='update details', width=150, fg_color='green', command=Update_Option)
update.grid(row=7, column=0, padx=20, pady=20, sticky='w')

 #  INFORMATION
update_info = ctk.CTkLabel(r,text="--->  If you want to update the given details or already given id, fill it all widget.",text_color="magenta2")
update_info.grid(row=7, column=1, columnspan=10,padx=20, pady=20, sticky='w')

    #---> DELETE OPTION
delete = ctk.CTkButton(r, text='delete details', width=150, fg_color='green', command=Delete_Option)
delete.grid(row=8, column=0, padx=20, pady=20, sticky='w')

  #  INFORMATION
delete_info = ctk.CTkLabel(r,text="--->  If you want to delete the given details, give the id number then,That id details are deleted",text_color="magenta2")
delete_info.grid(row=8, column=1, columnspan=10,padx=20, pady=20, sticky='w')

    #---> CLEAR OPTION
clear = ctk.CTkButton(r, text='clear details', width=150, fg_color='green', command=Clear_option)
clear.grid(row=9, column=0, padx=20, pady=20, sticky='w')

 #  INFORMATION
clear_info = ctk.CTkLabel(r,text="--->  If you want to clear the given details in the widget, just click on that.",text_color="magenta2")
clear_info.grid(row=9, column=1, columnspan=10,padx=20, pady=20, sticky='w')

    #   ---> VIEW  OPTION
view = ctk.CTkButton(r, text='view details', width=150, fg_color='green', command=View_Option)
view.grid(row=10, column=0, padx=20, pady=20, sticky='w')

 #  INFORMATION
view_info = ctk.CTkLabel(r,text="--->  If you see view details click after that go to start here serach bar type this content emp tab.txt then you can see if employee details.",text_color="magenta2")
view_info.grid(row=10, column=1, columnspan=10,padx=20, pady=20, sticky='w')

r.mainloop()

