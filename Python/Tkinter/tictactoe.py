#tic tac toe
import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.geometry("500x400")
turn=0
flag=0
def change(button,index):
    global turn, flag
    if turn == 0:
        button["text"] = "X"
        turn = 1
    else:
        button["text"] = "O"
        turn = 0
    button.config(state="disabled")
    flag += 1
    winner(index)
# def change2():
#     global turn, flag
#     if turn == 0:
#         b2["text"] = "X"
#         turn = 1
#     else:
#         b2["text"] = "O"
#         turn = 0
#     b2.config(state="disabled")
#     flag += 1
#    # winner() 
# def change3():
#     global turn, flag
#     if turn == 0:
#         b3["text"] = "X"
#         turn = 1
#     else:
#         b3["text"] = "O"
#         turn = 0
#     b3.config(state="disabled")
#     flag += 1
#    # winner() 
# def change4():
#     global turn, flag
#     if turn == 0:
#         b4["text"] = "X"
#         turn = 1
#     else:
#         b4["text"] = "O"
#         turn = 0
#     b4.config(state="disabled")
#     flag += 1
#     #winner() 
# def change5():
#     global turn, flag
#     if turn == 0:
#         b5["text"] = "X"
#         turn = 1
#     else:
#         b5["text"] = "O"
#         turn = 0
#     b5.config(state="disabled")
#     flag += 1
#     #winner() 
# def change6():
#     global turn, flag
#     if turn == 0:
#         b6["text"] = "X"
#         turn = 1
#     else:
#         b6["text"] = "O"
#         turn = 0
#     b6.config(state="disabled")
#     flag += 1
#     winner() 

# def change7():
#     global turn, flag
#     if turn == 0:
#         b7["text"] = "X"
#         turn = 1
#     else:
#         b7["text"] = "O"
#         turn = 0
#     b7.config(state="disabled")
#     flag += 1
#     winner() 
# def change8():
#     global turn, flag
#     if turn == 0:
#         b8["text"] = "X"
#         turn = 1
#     else:
#         b8["text"] = "O"
#         turn = 0
#     b8.config(state="disabled")
#     flag += 1
#     winner()
# def change9():
#     global turn, flag
#     if turn == 0:
#         b9["text"] = "X"
#         turn = 1
#     else:
#         b9["text"] = "O"
#         turn = 0
#     b9.config(state="disabled")
#     flag += 1
#     winner()
   
def winner(index):
    global flag                                                                                                                                                                                                      
    Button=(b1,b2,b3,b4,b5,b6,b7,b8,b9)     
    win_combinations= [(0, 1, 2), (3, 4, 5),(6, 7, 8),(0, 3, 6), (1, 4, 7), (2, 5, 8),(0, 4, 8), (2, 4, 6)]
        
    for combo in win_combinations:
        if all(Button[i]["text"] == "X" for i in combo):
            messagebox.showinfo("Winner", "Player X wins!")
            reset_game()
            return 
        if all(Button[i]["text"] == "O" for i in combo):
            messagebox.showinfo("Winner", "Player O wins!")
            reset_game()
            return 
        if flag == 9:
            messagebox.showinfo("Tie", "It's a tie!",)
            reset_game()

def reset_game():
    global turn,flag
    turn=0
    flag=0
    for button in (b1, b2, b3, b4, b5, b6, b7, b8, b9):
        button["text"] = " "
        button.config(state="active")
     
def exit():
    root.destroy()
   
b1 =tk.Button(root,text=" ",width=6,height=3,font=("arial",18),command=lambda:change(b1,0),bg="yellow")
b1.grid(row=2,column=4)
b2 =tk.Button(root,text=" ",width=6,height=3,font=("arial",18),command=lambda:change(b2,1),bg="yellow")
b2.grid(row=2,column=5)
b3 =tk.Button(root,text=" ",width=6,height=3,font=("arial",18),command=lambda:change(b3,2),bg="yellow")
b3.grid(row=2,column=6)
b4 =tk.Button(root,text=" ",width=6,height=3,font=("arial",18),command=lambda:change(b4,3),bg="yellow")
b4.grid(row=3,column=4)
b5 =tk.Button(root,text=" ",width=6,height=3,font=("arial",18),command=lambda:change(b5,4),bg="yellow")
b5.grid(row=3,column=5)
b6 =tk.Button(root,text=" ",width=6,height=3,font=("arial",18),command=lambda:change(b6,5),bg="yellow")
b6.grid(row=3,column=6)
b7 =tk.Button(root,text=" ",width=6,height=3,font=("arial",18),command=lambda:change(b7,6),bg="yellow")
b7.grid(row=4,column=4)
b8 =tk.Button(root,text=" ",width=6,height=3,font=("arial",18),command=lambda:change(b8,7),bg="yellow")
b8.grid(row=4,column=5)
b9 =tk.Button(root,text=" ",width=6,height=3,font=("arial",18),command=lambda:change(b9,8),bg="yellow")
b9.grid(row=4,column=6)
b10 =tk.Button(root,text="restart ",width=6,height=3,font=("arial",16),command=reset_game,bg="light green")
b10.grid(row=3,column=1)
b11 =tk.Button(root,text="exit",width=6,height=3,font=("arial",16),command=exit,bg="red")
b11.grid(row=4,column=1,padx=5,pady=1)
l1=tk.Label(root,text="first chance of X :",font=("arial",14))
l1.grid(row=1,column=1)
root.mainloop()