f= open("twinkle.txt","r")
# f.write("Twinkle, twinkle, little star,\n")
# f.write("How I wonder what you are!\n")
# f.write("Up above the world so high,\n")
# f.write("Like a diamond in the sky.\n")
text= f.readlines()
print(text)
for line in text:
    if "twinkle" in line.lower():  
        print("Yes,Go and Chill!")       
f.close()