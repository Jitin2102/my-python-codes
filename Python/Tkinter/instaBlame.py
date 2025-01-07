import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import csv


def load_csv_data():
    with open('new.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            tree.insert("", tk.END, values=row)

def toggle_treeview():
    if tree.winfo_viewable():
        tree.grid_remove()
        toggle_button.config(text="Show CSV Data")
    else:
        password = tk.simpledialog.askstring("Password", "Enter password:", show='*')
        if password == "developer_password":  # Change this to your developer password
            tree.grid()
            toggle_button.config(text="Hide CSV Data")
        else:
            messagebox.showerror("Error", "Invalid password")

def Login():
    name = entry1.get()
    username = entry6.get()
    email = entry3.get()
    contact = entry4.get()
    password = entry2.get()
    reEnterpassword = entry7.get()
    
    if password != reEnterpassword:
        messagebox.showerror("Invalid Error", "Password not matched")
    elif not name or not username or not password or not email or not contact:
        messagebox.showerror("Error", "Enter all asked details")
    else:
        # Print to terminal for debugging
        print(f"Name: {name}\nUsername: {username}\nPassword: {password}")
        
        # Save the information to the CSV file
        with open('new.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([name, username, password, contact, email])
        
        # Clear the entry fields after saving
        entry1.delete(0, tk.END)
        entry6.delete(0, tk.END)
        entry3.delete(0, tk.END)
        entry4.delete(0, tk.END)
        entry2.delete(0, tk.END)
        entry7.delete(0, tk.END)
        
        # Reload the data into the Treeview
        for row in tree.get_children():
            tree.delete(row)
        load_csv_data()

root = tk.Tk()
root.title("InstaBlame")
root.geometry("500x400+200+100")
fonts = ("Times New Roman", 10, "bold")

label0 = tk.Label(root, text="Welcome to InstaBlame", font=fonts, fg="red")
label0.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

label1 = tk.Label(root, text="Name:", font=fonts)
label1.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
entry1 = tk.Entry(root, bd=2)
entry1.grid(row=1, column=1, padx=5, pady=5)

label3 = tk.Label(root, text="Enter Email:", font=fonts)
label3.grid(row=2, column=0, sticky=tk.E, padx=5, pady=5)
entry3 = tk.Entry(root, bd=2)
entry3.grid(row=2, column=1, padx=5, pady=5)

label4 = tk.Label(root, text="Contact Number:", font=fonts)
label4.grid(row=3, column=0, sticky=tk.E, padx=5, pady=5)
entry4 = tk.Entry(root, bd=2)
entry4.grid(row=3, column=1, padx=5, pady=5)

gender_var = tk.StringVar(root)
label5 = tk.Label(root, text="Gender:", font=fonts)
label5.grid(row=4, column=0, sticky=tk.E, padx=5, pady=5)
gender_var.set("Select Gender")
gender_options = ['Male', 'Female', 'Other']
gender_menu = tk.OptionMenu(root, gender_var, *gender_options)
gender_menu.grid(row=4, column=1, padx=5, pady=5)

label6 = tk.Label(root, text="Username:", font=fonts)
label6.grid(row=5, column=0, sticky=tk.E, padx=5, pady=5)
entry6 = tk.Entry(root, bd=2)
entry6.grid(row=5, column=1, padx=5, pady=5)

label2 = tk.Label(root, text="Password:", font=fonts)
label2.grid(row=6, column=0, sticky=tk.E, padx=5, pady=5)
entry2 = tk.Entry(root, bd=2, show="*")
entry2.grid(row=6, column=1, padx=5, pady=5)

label7 = tk.Label(root, text="Re-enter Password:", font=fonts)
label7.grid(row=7, column=0, sticky=tk.E, padx=5, pady=5)
entry7 = tk.Entry(root, bd=2, show="*")
entry7.grid(row=7, column=1, padx=5, pady=5)

button = tk.Button(root, text="Login", command=Login)
button.grid(row=8, column=0, columnspan=2, pady=5)

# Toggle button to hide/show Treeview
toggle_button = tk.Button(root, text="Hide CSV Data", command=toggle_treeview)
toggle_button.grid(row=9, column=0, columnspan=2, pady=5)

# Create a Treeview widget to display the data
tree = ttk.Treeview(root, columns=("Name", "Username", "Password", "Contact", "Email"), show='headings')
tree.heading("Name", text="Name")
tree.heading("Username", text="Username")
tree.heading("Password", text="Password")
tree.heading("Contact", text="Contact")
tree.heading("Email", text="Email")
tree.grid(row=10, column=0, columnspan=2, sticky="nsew")

# Configure grid row and column weights for the Treeview
root.rowconfigure(10, weight=1)

# Load the CSV data into the Treeview
load_csv_data()

root.mainloop()
