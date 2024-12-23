guests=['Arjit','Kartikeya','Arsh','Adarsh']
print("Adarsh can not come to dinner.")
guests.pop()
print(guests)
# print(f"\nMyself Jitin,invite for dinner to {guests[0]}.\n")
# print(f"Myself Jitin,invite for dinner to {guests[1]}.\n")
# print(f"Myself Jitin,invite for dinner to {guests[2]}.\n")
#       Adding new members to the list
guests.insert(0,'Arpit')
guests.append('Divyansh')
print(guests)
print(f"\nMyself Jitin,invite for dinner to {guests[0]}.\n")
print(f"Myself Jitin,invite for dinner to {guests[1]}.\n")
print(f"Myself Jitin,invite for dinner to {guests[2]}.\n")
print(f"Myself Jitin,invite for dinner to {guests[3]}.\n")
print(f"Myself Jitin,invite for dinner to {guests[4]}.\n")
print(sorted(guests))


