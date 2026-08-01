print("Student Grade Manager")

names = []
marks = []
grade = []
add = input("Do you want to add a student(yes/no): ").lower()
while add == "yes":
    
    name = input("Enter student name: ").title()
    mark = float(input("Enter your marks: "))

    
    
    if 0 > mark or mark > 100:
        print("Invalid Marks ")

    else:
        names.append(name)
        marks.append(mark)
        
       
        

    if 90<=mark<=100 :
        grade.append("A+")

    elif 80<=mark <=89:
        grade.append("A")

    elif 70<=mark <=79:
        grade.append("B")

    elif 60<=mark <=69:
        grade.append("C")

    elif 50<=mark <=59:
        grade.append("D")

    elif 40<=mark <=49:
        grade.append("E")

    else:
        grade.append("F")
    add = input("Do you want to add another student(yes/no): ").lower()


print("\nStudent Reports")
print("-" * 30)

for i in range(len(names)):
    
        print(f"Name : {names[i]}")
        print(f"Marks: {marks[i]}")
        print(f"Grade: {grade[i]}")
        print("-" * 30)
    
        




    

