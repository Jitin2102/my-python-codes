num=input("Enter the number:")
num=int(num)
fact=1
def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num - 1)
fact=factorial(num)
print(f"factorial of {num} is {fact}.")   
    