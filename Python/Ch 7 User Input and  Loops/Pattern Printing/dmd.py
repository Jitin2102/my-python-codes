rows=3
for i in range(rows):
    spaces=rows - i - 1
    stars=2 * i + 1
    print(' ' * spaces + '*' * stars)
for i in range(rows-1,-1,-1):
    spaces=rows - i  
    stars=2 * i - 1 
    print(' ' * spaces + '*' * stars)  