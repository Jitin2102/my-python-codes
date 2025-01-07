import math
from turtle import tracer, bgcolor, goto, color,done

def heart(n):
    return 16 * (math.sin(n)**3)
#instagram.com/parthjindal_7
def heart_b(n):
    return 15 * math.cos(n) - 4 * math.cos(2*n) - 2 * math.cos(3*n) - math.cos(4*n)

tracer(2)
bgcolor("black")
color("red")
for i in range(800):
    goto(heart(i)*16, heart_b(i)*16)
done()
    