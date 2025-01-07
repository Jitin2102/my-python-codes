import tkinter as tk
from tkinter import ttk
import csv
root=tk.Tk()
def load_csv_data():
    with open('new.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            tree.insert("", tk.END, values=row)

tree = ttk.Treeview(root, columns=("Name", "Username", "Password"), show='headings')
tree.heading("Name", text="Name")
tree.heading("Username", text="Username")
tree.heading("Password", text="Password")
tree.pack(fill=tk.BOTH, expand=True)


load_csv_data()


root.mainloop()
