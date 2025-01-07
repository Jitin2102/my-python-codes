print("Enter Pizza Toppings:")
list=[]
prompt=""
while prompt!='quit':
    prompt=input()
    if prompt!='quit':
        list.append(prompt)
print("\n")        
for item in list:
    print(item)