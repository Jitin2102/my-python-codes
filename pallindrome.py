def Pallindrome(x):
    temp=x
    r=0
    sum=0
    while temp>0:
        n= temp % 10
        sum= sum + n
        r= (r*10)+ n
        temp=temp//10
    if r==x:
        print("Pallindrome.")
    else:
        print("Not pallindrome.")
    if r!=x:
        print(f"{r} is the reverse of {x}.") 
    print(f"Sum of digits of {x} is {sum}.")       
# x=input("Enter a number: ")
# x=int(x)
# Pallindrome(x)
list=[123,131,1331,454,897]
for num in list:
    Pallindrome(num)
    print("\n")
                
       