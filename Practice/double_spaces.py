s= input("Enter a string: ")
def detect_double_spaces(s):
    count=0
    for i in range(len(s)-1):
        if s[i] == ' ' and s[i+1] == ' ':
            count += 1
    return count > 0
    if detect_double_spaces(s):
        print("The string contains double spaces.")
def remove_double_spaces(s):
    return ' '.join(s.split())
result = remove_double_spaces(s)
print("String after removing double spaces:", result)
