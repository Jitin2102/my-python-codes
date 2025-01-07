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

root = tk.Tk()
root.title("Happy New Year")

canvas = tk.Canvas(root, width=500, height=500, bg="black")
canvas.pack()

label = tk.Label(root, text="Happy New Year 2025!", font=("Helvetica", 24), fg="red", bg="black")
label.pack()

firework_button = tk.Button(root, text="Show Fireworks", command=show_fireworks, font=("Helvetica", 16), fg="yellow", bg="black")
firework_button.pack()

root.mainloop()