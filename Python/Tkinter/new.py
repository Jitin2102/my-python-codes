import tkinter as tk
import random

def create_firework(canvas, x, y):
    colors = ['red', 'yellow', 'blue', 'green', 'white', 'orange', 'purple']
    for _ in range(10):
        x1 = x + random.randint(-20, 20)
        y1 = y + random.randint(-20, 20)
        color = random.choice(colors)
        canvas.create_oval(x1, y1, x1+5, y1+5, fill=color, outline=color)

def show_fireworks():
    for _ in range(5):
        x = random.randint(50, 450)
        y = random.randint(50, 450)
        create_firework(canvas, x, y)
    root.after(1000, show_fireworks) 

def add_text():
    canvas.create_text(250, 250, text="Happy New Year \n         2025!", font=("Helvetica", 38), fill="blue")

root = tk.Tk()
root.title("Happy New Year")

canvas = tk.Canvas(root, width=500, height=500, bg="black")
canvas.pack()


add_text()

root.after(1000, show_fireworks)  

root.mainloop()
