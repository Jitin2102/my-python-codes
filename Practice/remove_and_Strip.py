print("Enter words:")
list=[]
word=""
while word!= "exit":
    word = input()
    if word != "exit":
        list.append(word)

print("You entered:", list)
word_to_be_removed = input("Enter a word to remove: ")
if word_to_be_removed in list:
    word_strip= word_to_be_removed.strip()
    list.remove(word_to_be_removed)
else:
    print("Word not found in the list.")     
print("Updated list:", list)