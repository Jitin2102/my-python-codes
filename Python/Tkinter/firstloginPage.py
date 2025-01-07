import tkinter as tk

class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("400x300")
        
        self.logo = tk.Label(self, text="Login",fg="green", font=("Helvetica", 13)) 
        self.logo.grid(row=0,column=2,columnspan=1,padx=5,pady=10)
        self.usernameLabel=tk.Label(self,text="Username")
        self.usernameLabel.grid(row=1,column=1,padx=5,pady=5,sticky='e')
        self.usernameEntry=tk.Entry(self)
        self.usernameEntry.grid(row=1,column=2,padx=5,pady=5)
        
        self.passwordLabel=tk.Label(self,text="Password")
        self.passwordLabel.grid(row=2,column=1,padx=5,pady=5,sticky='e')
        self.passwordEntry=tk.Entry(self,show="*")
        self.passwordEntry.grid(row=2,column=2,padx=5,pady=5)
        
        
        self.loginButton =tk.Button(self,text="login",command=self.login)
        self.loginButton.grid(row=3,column=2,columnspan=2,pady=10)
        
        #self.signupLabel0=tk.Label(self,text="Don't have an account",fg="red")
        #self.signupLabel0.grid(row=4,column=2,columnspan=1,padx=5,pady=5,sticky='w')                           
        self.signupLabel=tk.Label(self,text=" SignUp here",fg="blue",cursor="hand2")
        self.signupLabel.grid(row=5,column=2,columnspan=1,padx=5,pady=8,)
        self.signupLabel.bind("<Button-1>",self.signup)
        
    def login(self):
        username=self.usernameEntry.get()
        password=self.passwordEntry.get()
        print(f"Username:{username},Password:{password}")   
    def signup(self,event):
        print("Redirecting to SignUp page ")
if __name__=="__main__":
    LoginWindow=LoginWindow()
    LoginWindow.mainloop()            
            