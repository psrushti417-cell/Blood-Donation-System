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
            password="",
            database="bload_donation"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM register1234")
        rows = cursor.fetchall()

        # Clear previous content
        for row in tree.get_children():
            tree.delete(row)

        # Insert new data into the treeview
        for row in rows:
            tree.insert("", tk.END, values=row)

        cursor.close()
        conn.close()
    except Exception as e:
        print("Error:", e)

def back():
    root.destroy()
    subprocess.run(["python", "page.py"])


# GUI setup
root = tk.Tk()
root.title("MySQL Data Viewer")
root.geometry("1400x680")
root.resizable(0,0)

# Treeview widget to show table data
tree = ttk.Treeview(root, columns=(1, 2, 3, 4, 5, 6, 7), show="headings", height=30)
tree.pack()

tree.heading(1, text="ID")
tree.heading(2, text="Name")
tree.heading(3, text="Age")
tree.heading(4, text="Bload Group")
tree.heading(5, text="Contact No")
tree.heading(6, text="Date")
tree.heading(7, text="Weight(ml)")



# Button to fetch data
btn = tk.Button(root, text="Load Data", command=fetch_data)
btn.pack(pady=10)

btn = tk.Button(root, text="Back", command=back).place(x=750, y=638)

root.mainloop()
