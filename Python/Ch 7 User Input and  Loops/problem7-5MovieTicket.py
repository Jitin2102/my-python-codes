print("Enter your age to get your ticket price and prompt 'clear' after getting ticket ticket price.")
def ticket_price(age):
    if age < 3:
        return 0
    elif age < 12:
        return 10
    else:
        return 15           
prompt=True
while prompt:
    age=input("Enter your age :")
    age=int(age)
    x=ticket_price(age)
    print(f" Your ticket price is ${x}.")
    response=input("Do you want to enter another age ?(yes/no)") 
    if response=='no':
        prompt=False
print("Thank you so much for coming to our Cinema. See you again.")      