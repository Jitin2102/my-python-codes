def Sum(x,y):
    return (x+y)
def Difference(x,y):
    return (x-y)
def Product(x,y):
    return (x*y)
def Division(x,y):
    return (x/y)
def Calculator(a,b):
    print("1 for Addition\n2 for Substraction\n3 for Multiplication\n4 for Division")
    ch=input("Enter your choice:")
    ch= int(ch)
    if ch==1:
        result=Sum(a,b)
        print(f"Sum of {a} and {b} is {result}.")
    elif ch==2:
        result=Difference(a,b)
        print(f"Substraction of {a} and {b} is {result}.")
    elif ch==3:
        result=Product(a,b)
        print(f"Multiplication of {a} and {b} is {result}.") 
    elif ch==4:
        result=Division(a,b)
        print(f"Quotient of {a} divided by {b} is {result}.")
    else:
        print("Sorry Bro, Error 404 not found this choice!")
   
a=input("Enter first number:")
a=int(a)
b=input("Enter second number:")
b=int(b)
Calculator(a,b)                
           
    