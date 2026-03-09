import tkinter as tk
from tkinter import ttk
import mysql.connector
import subprocess

# MySQL connection setup
def fetch_data():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sagar",
            database="shrava"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clint1")
        rows = cursor.fetchall()

        
        for row in tree.get_children():
            tree.delete(row)

        
        for row in rows:
            tree.insert("", tk.END, values=row)

        cursor.close()
        conn.close()
    except Exception as e:
        print("Error:", e)

def back():
    root.destroy()
    subprocess.run(["python", "shambhu.py"])


# GUI setup
root = tk.Tk()
root.title("MySQL Data Viewer")
root.geometry("1100x300")
root.resizable(0,0)

# Treeview widget to show table data
tree = ttk.Treeview(root, columns=(1, 2, 3, 4, 5), show="headings", height=10)
tree.pack()

tree.heading(1, text="Sr_no")
tree.heading(2, text="Clint name")
tree.heading(3, text="Clint Website")
tree.heading(4, text="Website REenwal Date")
tree.heading(5, text="Website Domain Renewal Date")



# Button to fetch data
btn = tk.Button(root, text="Load Data", command=fetch_data)
btn.pack(pady=10)

btn = tk.Button(root, text="Back", command=back).place(x=600, y=240)

root.mainloop()
