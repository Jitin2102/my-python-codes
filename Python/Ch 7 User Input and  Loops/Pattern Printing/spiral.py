n=5
matrix=[[0] * n for _ in range(n)]
row,col=0,0
dx,dy=0,1
for i in range(1,n*n+1):
    matrix[row][col]=i
    if matrix[(row+dx) % n][(col+ dy) % n]:
        dx,dy=dy,-dx
    row+= dx
    col+= dy
    
for row in matrix:
    print(' '.join(f'{num:02d}' for num in row))     