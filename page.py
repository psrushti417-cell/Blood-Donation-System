from tkinter import  *
import subprocess


class shambhu:
    def __init__(self,root):
        self.root=root
        self.root.title("Welcome Page!")
        self.root.geometry("1500x600")
        root.configure(bg="lightblue")  # Set background color of the main window
        self.root.resizable(0,0)
        def submit():
            root.destroy()
            subprocess.run(["python", "register.py"])

        def search():
            root.destroy()
            subprocess.run(["python", "search.py"])

        def view():
            root.destroy()
            subprocess.run(["python", "view.py"])

        def exit():
            self.root.destroy()



        t= Label(self.root,text="❤️ WELCOME TO BLOOD DONATION SYSTEM   ❤",font=("Impact",35,"bold"),fg="red",bg="lightblue").place(x=300,y=100)

        Button(self.root, text="Registor  Donor", font=("Impact",25),command=submit, height=1,width=23).place(x=300, y=250)
        Button(self.root, text="Search  Donor", font=("Impact",25),command=search, height=1,width=23).place(x=870, y=250)
        Button(self.root, text="View  Donations", font=("Impact",25),command=view, height=1,width=23).place(x=300, y=400)
        Button(self.root, text="Exit", font=("Impact",25),command=exit, height=1,width=23).place(x=870, y=400)



root =Tk()

o=shambhu(root)
root.mainloop()
