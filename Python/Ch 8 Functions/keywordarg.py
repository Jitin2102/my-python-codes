# def info_pet(animal_type,pet_name):
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is \'{pet_name.title()}\'.")
# info_pet(pet_name='harry',animal_type='dog')
        # HERE ORDER DOES NOT MATTER
        # PASSING ARBITRARY NUMBER OF ARGUMENTS
def make_pizza(*toppings):

 print(toppings)
 
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')