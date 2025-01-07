x=input("Enter number: ")
x=int(x)
def collatz( number):
    if number % 2==0:
        return number//2
    else:
        return (3 * number + 1)
 
while collatz(x)!=1:
    
    x=int(input())
    print(collatz(x))

print("Done")   