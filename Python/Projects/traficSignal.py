import tkinter as tk

# Constants for timing
RED_TIME = 2000
YELLOW_TIME = 2000
GREEN_TIME = 2000

def set_traffic_signal(canvas):
    # Red light
    red_light =canvas.create_oval(25,50,75,100,fill="gray",outline="gray")
    # Yellow light
    yellow_light =canvas.create_oval(25,125,75,175,fill="gray",outline="gray")
    # Green light
    green_light =canvas.create_oval(25,200,75,250,fill="gray",outline="gray")
    return red_light,yellow_light,green_light

def start_simulation(canvas,lights):
    def change_light_and_schedule_next(color,next_color,delay):
        change_light(canvas,lights,color)
        print(f"{color.capitalize()} light on")
        canvas.after(delay,lambda:change_light_and_schedule_next(next_color,"red" if next_color == "green" else "green" if next_color == "yellow" else "yellow", RED_TIME if next_color == "red" else GREEN_TIME if next_color == "green" else YELLOW_TIME))

    # Start the cycle with the red light
    change_light_and_schedule_next("red","yellow",RED_TIME)

def change_light(canvas,lights,color):
    for light in lights.values():
        canvas.itemconfig(light,fill="gray")
    canvas.itemconfig(lights[color],fill=color)


root=tk.Tk()
root.title('Traffic Signal Simulator')
canvas=tk.Canvas(root,width=100,height=300,bg="white")
canvas.pack()
    
    # Set up traffic signals
lights ={"red":None,"yellow":None,"green":None}
lights["red"],lights["yellow"],lights["green"] = set_traffic_signal(canvas)
    
start_button =tk.Button(root,text="Start",command=lambda:start_simulation(canvas,lights))
start_button.pack(pady=10)
    
root.mainloop()


               

               