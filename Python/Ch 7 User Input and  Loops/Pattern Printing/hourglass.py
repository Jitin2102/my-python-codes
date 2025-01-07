rows=5
for i in range(rows):
    print(' ' * i + '*' * (2 * (rows-i) -1))
for i in range(1,rows):
    print(' ' * (rows -i -1) + '*' * (2 * i + 1))    