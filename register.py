from tkinter import *
import mysql.connector
from tkinter import messagebox
import subprocess

def no_selection():
    s1.delete(0, END)
    s2.delete(0, END)
    s3.delete(0, END)
    s4.delete(0, END)
    s5.delete(0, END)
    s6.delete(0, END)

    s=listBox.focus()
    v=listBox.item(s,"v")

    if v:
        s1.insert(0, values[0])
        s2.insert(0, values[1])
        s3.insert(0, values[2])
        s4.insert(0, values[3])
        s5.insert(0, values[4])
        s6.insert(0, values[5])
def submit():
    name = s1.get().strip()
    age = s2.get().strip()
    blodgroup = s3.get().strip()
    contactno = s4.get().strip()
    date=s5.get().strip()
    bloadq=s6.get().strip()

    if not name or not age or not blodgroup or not contactno or not date or not bloadq:
        messagebox.showwarning("Error","All filead is Required")
        return

    m=mysql.connector.connect(host="localhost",
                               user="root",
                               password="sagar",
                               database="bload_donation"
                               )

    mc=m.cursor()
    try:
        s = "INSERT INTO register1234(name, age, bloadgroup, contactno, date, bloadq ) VALUES ( %s, %s, %s, %s, %s, %s)"
        v = (name, age, blodgroup, contactno, date, bloadq)
        mc.execute(s , v)
        m.commit()
        messagebox.showinfo("Information","Recoard inserted successfull")
        clear_filelds()
    except Exception as e:
        messagebox.showerror("Database Error",str(e))
        m.rollback()
    finally:
        m.close()

def clear_filelds():
    s1.delete(0, END)
    s2.delete(0, END)
    s3.delete(0, END)
    s4.delete(0, END)
    s5.delete(0, END)
    s6.delete(0, END)

    


def back():
    root.destroy()
    subprocess.run(["python", "page.py"])

    

root=Tk()
root.title("Registor Donor")
root.geometry("510x400") 
root.resizable(0,0)

Label(root,text="Regaster", font=("Tempus Sans ITC",25),fg="red").place(x=190,y=10)

Label(root,text="Name",).place(x=30,y=80)

Label(root,text="Age").place(x=30,y=140)

Label(root,text="Bload Group").place(x=30,y=200)

Label(root,text="Contact No",).place(x=300,y=80)

Label(root,text="Date").place(x=300,y=140)

Label(root,text="ML").place(x=300,y=200)





s1 = Entry(root)
s1.place(x=30,y=110,width=150)

s2 = Entry(root)
s2.place(x=30,y=170,width=150)

s3 = Entry(root)
s3.place(x=30,y=230,width=150)

s4 = Entry(root)
s4.place(x=300,y=110,width=150)

s5 = Entry(root)
s5.place(x=300,y=170,width=150)

s6 = Entry(root)
s6.place(x=300,y=230,width=150)


Button(root,text="Submit",font=("Impact",20),command=submit,width=11).place(x=30,y=280)

Button(root,text="Back",font=("Impact",20),command=back,width=11).place(x=300,y=280)



root.mainloop()







