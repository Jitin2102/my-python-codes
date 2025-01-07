responses={}
polling_active=True
while polling_active:
    name=input("\nWhat is your name ?")
    response=input("Which mountain would you like to climb someday ?")
    responses[name]=response
    repeat=input("Would you like to another person to respond ?(yes/no)")
    if repeat=='no':
        polling_active=False
print("\n              ____Poll Results____") 
for name,response in responses.items():
    print(f"{name} would like to climb {response}.")       