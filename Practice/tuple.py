t= (1, 2, 3, 4, 5)
print("Welcome to the tuple operations program!")
print("Original tuple:", t)
t = list(t)  
(one, two, three, four, five) = t # Unpacking the tuple
print("First element:", one)
print("Second element:", two)
print("Third element:", three)
print("Fourth element:", four)
print("Fifth element:", five)
t.append(6)  # Adding an element
print("Tuple after adding 6:", tuple(t))
t.sort()  # Sorting the list
print("Sorted tuple:", tuple(t))
t.reverse()  # Reversing the list
print("Reversed tuple:", tuple(t))
t.insert(0, 0)  # Inserting at the beginning
print("Tuple after inserting 0 at the beginning:", tuple(t))
t.append(7)  # Adding at the end
print("Tuple after adding 7 at the end:", tuple(t))
t.pop()  # Removing the last element
print("Tuple after popping the last element:", tuple(t))
t.remove(0)  # Removing the first element
print("Tuple after removing the first element:", tuple(t))
t = (1, 2, 3, 4, 5)
print("Final tuple:", t)
print(t.count(3))
print(t.index(3))