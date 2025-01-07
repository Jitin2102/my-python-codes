# import tkinter as tk
# from functools import partial

# def call_result(label_result, n1, n2):
#     num1 = n1.get()
#     num2 = n2.get()
    
#     # Check and clear placeholder text
#     if num1 == "First Number":
#         num1 = ""
#     if num2 == "Second Number":
#         num2 = ""
    
#     try:
#         result = int(num1) + int(num2)
#         label_result.config(text="Sum = %d" % result)
#     except ValueError:
#         label_result.config(text="Please enter valid numbers")
#     return 

# root = tk.Tk()
# root.geometry('400x200+100+200')
# root.title('Addition')

# number1 = tk.StringVar()
# number2 = tk.StringVar()

# entryNum1 = tk.Entry(root, textvariable=number1)
# entryNum1.grid(row=1, column=2)
# entryNum1.insert(0,"")  # Insert placeholder text

# entryNum2 = tk.Entry(root, textvariable=number2)
# entryNum2.grid(row=2, column=2)
# entryNum2.insert(0,"")  # Insert placeholder text

# labelResult = tk.Label(root)
# labelResult.grid(row=7, column=2)

# call_result = partial(call_result, labelResult, number1, number2)
# buttonCall = tk.Button(root, text="Addition", command=call_result)
# buttonCall.grid(row=3, column=2)

# root.mainloop()
import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello Tkinter")
        self.label = tk.Label(self, text="Choose One")
        self.label.pack(fill=tk.BOTH, expand=1, padx=100, pady=30)
        
        hello_button = tk.Button(self, text="Say Hello", command=self.say_hello)
        hello_button.pack(side=tk.LEFT, padx=(20, 0), pady=(0, 20))
        
        goodbye_button = tk.Button(self, text="Say Goodbye", command=self.say_goodbye)
        goodbye_button.pack(side=tk.RIGHT, padx=(0, 20), pady=(0, 20))
    
    def say_hello(self):
        self.label.config(text="Hello, World!")
    
    def say_goodbye(self):
        self.label.config(text="Goodbye, World!")

if __name__ == "__main__":
    window = Window()
    window.mainloop()
