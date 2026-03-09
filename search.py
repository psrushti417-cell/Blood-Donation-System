import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import subprocess

def search_record():
    bload_g = entry_Bload_group.get()
    if bload_g == "":
        messagebox.showerror("Error", "Please enter an ID")
        return

    try:
        conn = mysql.connector.connect(
            host="localhost", user="root", password="sagar", database="bload_donation"
        )
        cursor = conn.cursor()
        query = "SELECT * FROM register1234 WHERE bloadgroup = %s"
        cursor.execute(query, (bload_g,))
        rows = cursor.fetchall()

        for item in tree.get_children():
            tree.delete(item)

        if rows:
            for row in rows:
                tree.insert("", tk.END, values=row)
        else:
            messagebox.showinfo("No Record", "No data found for this ID")

        conn.close()
    except Exception as e:
        messagebox.showerror("Database Error", str(e))

def back():
    root.destroy()
    subprocess.run(["python", "page.py"])

root = tk.Tk()
root.title("Search Record by ID")
root.geometry("900x400")

tk.Label(root, text="Enter Bload Group:").pack(pady=10)
entry_Bload_group = tk.Entry(root)
entry_Bload_group.pack(pady=5)

tk.Button(root, text="Search", command=search_record).pack(pady=10)

tk.Button(root, text="Back", command=back).pack(pady=10)



cols = ("ID", "Name", "Age", "Contact","Bload_group")
tree = ttk.Treeview(root, columns=cols, show="headings")

for col in cols:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.pack(fill="both", expand=True)

root.mainloop()
