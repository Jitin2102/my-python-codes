# student record in list   30/08/2025
students =[]
n =int(input("Enter the number of students: "))
for _ in range(n):
    name =input("Enter name: ")
    rollno =int(input("Enter rollno: "))
    m1 =float(input("Enter marks for phy: "))
    m2 =float(input("Enter marks for chem: "))
    m3 =float(input("Enter marks for math: "))
    print()
    student =[
        name,               
        rollno,             
        [m1, m2, m3],       
        sum([m1, m2, m3]) / 3
    ]
    students.append(student)

for student in students:
    name = student[0]
    marks = student[2]
    max_marks =max(marks)
    print(f"Highest marks for {name} is {max_marks:.2f}.")
