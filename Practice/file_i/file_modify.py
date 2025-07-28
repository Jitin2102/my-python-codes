import time
time= time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
f = open("newfile.txt", "a+")
f.write(f"Hello, Universe!\n this file is modified at {time}.\n")
f.seek(0)
text = f.readlines()
f.close()
for line in text:
    if line.strip():  # Check if the line is not empty
        print(line.strip())