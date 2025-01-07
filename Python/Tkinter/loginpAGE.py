# import tkinter as tk
# from tkinter import messagebox 
# from tkinter import ttk
# import csv

# # Function to load data from CSV
# def load_csv_data():
#     with open('new.csv', newline='') as csvfile:
#         reader = csv.reader(csvfile)
#         for row in reader:
#             tree.insert("", tk.END, values=row)

# # Function to collect user information and save it to CSV
# def collectInfo():
#     name = entry0.get()
#     username = entry.get()
#     password = entry1.get()
    
#     if not name or not username or not password:
#         messagebox.showerror("Error", "Enter name, username, and password!")
#     else:
#         # Print to terminal for debugging
#         print(f"Name: {name}\nUsername: {username}\nPassword: {password}")
        
#         # Save the information to the CSV file
#         with open('new.csv', 'a', newline='') as csvfile:
#             writer = csv.writer(csvfile)
#             writer.writerow([name, username, password])
        
#         # Clear the entry fields after saving
#         entry0.delete(0, tk.END)
#         entry.delete(0, tk.END)
#         entry1.delete(0, tk.END)
        
#         # Reload the data into the Treeview
#         for row in tree.get_children():
#             tree.delete(row)
#         load_csv_data()

# # Function to toggle the visibility of the Treeview widget
# def toggle_treeview():
#     if tree.winfo_viewable():
#         tree.pack_forget()
#         toggle_button.config(text="Show CSV Data")
#     else:
#         tree.pack(fill=tk.BOTH, expand=True)
#         toggle_button.config(text="Hide CSV Data")

# # Create the main window
# root = tk.Tk()
# root.title('Login Page')
# root.geometry("400x400")

# # StringVar variables for labels
# var0 = tk.StringVar()
# var1 = tk.StringVar()
# var2 = tk.StringVar()
# var3 = tk.StringVar()

# # Label for the title
# label0 = tk.Label(root, textvariable=var0, fg="green")
# var0.set("Login")
# label0.pack(pady=10)

# # Label for name
# label2 = tk.Label(root, textvariable=var3)
# var3.set("Name:")
# label2.pack()

# # Entry for name
# entry0 = tk.Entry(root, bd=5)
# entry0.pack()

# # Label for username
# label = tk.Label(root, textvariable=var1)
# var1.set("Username:")
# label.pack()

# # Entry for username
# entry = tk.Entry(root, bd=5)
# entry.pack()

# # Label for password
# label1 = tk.Label(root, textvariable=var2)
# var2.set("Password:")
# label1.pack()

# # Entry for password
# entry1 = tk.Entry(root, bd=5, show="*")
# entry1.pack()

# # Login button
# button = tk.Button(root, text="Login", command=collectInfo)
# button.pack(pady=5)

# # Toggle button to hide/show Treeview
# toggle_button = tk.Button(root, text="Hide CSV Data", command=toggle_treeview)
# toggle_button.pack(pady=5)

# # Create a Treeview widget to display the data
# tree = ttk.Treeview(root, columns=("Name", "Username", "Password"), show='headings')
# tree.heading("Name", text="Name")
# tree.heading("Username", text="Username")
# tree.heading("Password", text="Password")
# tree.pack(fill=tk.BOTH, expand=True)

# # Load the CSV data into the Treeview
# load_csv_data()

# # Start the Tkinter main loop
# root.mainloop()
import tkinter as tk
from tkinter import messagebox 
from tkinter import ttk
import csv

# Function to load data from CSV
def load_csv_data():
    with open('new.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            tree.insert("", tk.END, values=row)

# Function to collect user information and save it to CSV
def collectInfo():
    name = entry0.get()
    username = entry.get()
    password = entry1.get()
    
    if not name or not username or not password:
        messagebox.showerror("Error", "Enter name, username and password!")
    else:
        # Print to terminal for debugging
        print(f"Name: {name}\nUsername: {username}\nPassword: {password}")
        
        # Save the information to the CSV file
        with open('new.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([name, username, password])
        
        # Clear the entry fields after saving
        entry0.delete(0, tk.END)
        entry.delete(0, tk.END)
        entry1.delete(0, tk.END)
        
        # Reload the data into the Treeview
        for row in tree.get_children():
            tree.delete(row)
        load_csv_data()

# Function to toggle the visibility of the Treeview widget
def toggle_treeview():
    if tree.winfo_viewable():
        tree.grid_remove()
        toggle_button.config(text="Show CSV Data")
    else:
        tree.grid()
        toggle_button.config(text="Hide CSV Data")

# Create the main window
root = tk.Tk()
root.title('Login Page')
root.geometry("400x400")

# StringVar variables for labels
var0 = tk.StringVar()
var1 = tk.StringVar()
var2 = tk.StringVar()
var3 = tk.StringVar()

# Configure grid layout
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# Label for the title
label0 = tk.Label(root,textvariable=var0, fg="green")
var0.set("Login")
label0.grid(row=0, column=0, columnspan=2, pady=10)

# Label for name
label2 = tk.Label(root, textvariable=var3)
var3.set("Name:")
label2.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)

# Entry for name
entry0 = tk.Entry(root, bd=5)
entry0.grid(row=1, column=1, padx=5, pady=5)

# Label for username
label = tk.Label(root, textvariable=var1)
var1.set("Username:")
label.grid(row=2, column=0, sticky=tk.E, padx=5, pady=5)

# Entry for username
entry = tk.Entry(root, bd=5)
entry.grid(row=2, column=1, padx=5, pady=5)

# Label for password
label1 = tk.Label(root, textvariable=var2)
var2.set("Password:")
label1.grid(row=3, column=0, sticky=tk.E, padx=5, pady=5)

# Entry for password
entry1 = tk.Entry(root, bd=5, show="*")
entry1.grid(row=3, column=1, padx=5, pady=5)

# Login button
button = tk.Button(root, text="Login", command=collectInfo)
button.grid(row=4, column=0, columnspan=2, pady=10)

# Toggle button to hide/show Treeview
toggle_button = tk.Button(root, text="Hide CSV Data", command=toggle_treeview)
toggle_button.grid(row=5, column=0, columnspan=2, pady=5)

# Create a Treeview widget to display the data
tree = ttk.Treeview(root, columns=("Name", "Username", "Password"), show='headings')
tree.heading("Name", text="Name")
tree.heading("Username", text="Username")
tree.heading("Password", text="Password")
tree.grid(row=6, column=0, columnspan=2, sticky="nsew")

# Configure grid row and column weights for the Treeview
root.rowconfigure(6, weight=1)

# Load the CSV data into the Treeview
load_csv_data()

# Start the Tkinter main loop
root.mainloop()


