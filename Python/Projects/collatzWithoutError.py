def collatz( number):
    if number % 2==0:
        result=number//2
        return result
    else:
        return (3 * number + 1)
x=("Enter number: ")    
     # ERROR
try:
    while collatz(x)!=1:
    
            x=int(input())
            print(collatz(x))

    print("Done")
except x is int:
    print("Error :\"Invalid Argument\"\n Please enter an integer")