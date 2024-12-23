# x=str(input("Enter your name: "))
# print(f"you entered {x} just now.")
# x=int(input("Enter any number: "))
# print(f"you entered {x} just now.")
response=input("Do you like Python ?(yes/no)")
if response=="yes":
    likes_python="True"
elif response=="no":
    likes_python="No" 
else:
    likes_python="None"
    print("Invlid response.Please enter 'yes'or 'no'.")
print(f"likes_python:{likes_python}")        
       