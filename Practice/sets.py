s = set([1, 2, 3, 4, 5])
print("Welcome to the set operations program!")
print("Original set:", s)
s.add(6)  # Adding an element
print("Set after adding 6:", s)
s.remove(1)  # Removing an element
print("Set after removing 1:", s)
s.discard(2)  # Discarding an element
print("Set after discarding 2:", s)
s.update([7, 8])  # Updating with multiple elements
print("Set after updating with [7, 8]:", s)
s.intersection_update([3, 4, 5])  # Keeping only elements that are also in the given set
print("Set after intersection update with [3, 4, 5]:", s)
s.clear()  # Clearing the set
print("Set after clearing:", s)