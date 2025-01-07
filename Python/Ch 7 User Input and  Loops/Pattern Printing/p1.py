# rows=6
# for i in range(rows +1):
#     for j in range(i):          # PATTERN  1 22 333 4444 55555
#         print(i,end=' ')
#     print("") 
   
# for i in range(rows+1):
#     for j in range(1,i):        # PATTERN  1 12 123 1234 12345
#         print(j,end=" ")
#     print("")
    
    
    
    
rows=5
k=2 * rows -1                                       #PATTERN ***** **** *** ** *      
for i in range(rows,-1,-1):
    for j in range(k,0,-1):
        print(end="")
    k+=1
    for j in range(0,i+1) :
        print("*", end=" ")
    print("")       