# trying to create a list and perform various operations on it
print("Welcome to the list operations program!")
list=[]
while True:
    item = input("Enter an item to add to the list (or 'done' to finish): ")
    if item == 'done':
        break
    list.append(item)
print("Your list:", list)
list.sort()
print("Sorted list:", list)
print("Reversed list:", list[::-1])
list.insert(0,"start")
print("List after inserting 'start' at the beginning:", list)
print("List after inserting 'end' at the end:", list + ["end"])
list.pop()
print("updated_list:", list)
list.remove("start")
print("List after removing 'start':", list)