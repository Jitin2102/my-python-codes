import tkinter as tk
import random
def change_bg():
    colours=["#FF5733","#33FF57","#3357FF","#F3FF33","#FF33A6","#33FFF0","#66AD18","#AD7823","#64A325","#DBA37E","#FA590A"]
    bg_color=random.choice(colours)
    canvas.config(bg=bg_color)
    root.after(1000,change_bg)
    
root=tk.Tk()
root.geometry("1500x1200")
root.title("Birthday Wish To My Veeru!")
canvas=tk.Canvas(root,width=500,height=300)
canvas.pack(fill="both",expand=True)

canvas.create_text(750,400,text="Happy Birthday Mere Veeru 18\nEquipped With Special Powers!\nWhere Your Name Ends Bro, My Name Starts!\n                      -    \"ARJITIN\"",font=("algerian",28,"italic"),fill="black")

change_bg()

root.mainloop()