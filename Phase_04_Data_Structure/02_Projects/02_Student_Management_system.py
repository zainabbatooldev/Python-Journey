
# Menu 

# empty dic
students = {}

topper = None 
max_marks = 0
physics = 0
maths = 0
physics_topper = None

while True: 
    print('''
1. Add Student
2. View All Students
3. Search Student
4. Delete Student
5. Calculate Average Marks
6. Find Topper
7. Show Maximum Marks
8. Exit''')
    
# input fom user
    user_input = input("\n")

# if else

        # 1. Add Student


    if user_input == "1":

        rollno = int(input("\nEnter Roll Number: "))

        name = input("\nEnter Student Name: ").title()
        age = int(input("\nEnter Age: "))

        phy_marks = int(input("Enter Physics Marks: "))
        maths_marks = int(input("Enter Maths Marks: "))

        if rollno in students:
            print("Already Exist.")
        else:

            students[rollno]={
                "name" : name,
                "age"  : age,
                "marks": {
                    "physics" : phy_marks, 
                    "maths"  : maths_marks

                }
            }
        print("-"*35,"\n")

            # 2. View All Students

    elif user_input == "2":

        for rollno , details in students.items():

            print("Roll Number: ", rollno)
            print("Name: ", details["name"])
            print("Age: ", details["age"])
            print("Physics Marks: " , details["marks"]["physics"])
            print("Maths Marks: " , details["marks"]["maths"],"\n")
            print("-"*35,"\n")
                
        #  3. Search Student       

    elif user_input == "3":

        rollno = int(input("\nEnter Roll Number: "))
        
        if rollno in students:
                
                

            print("Name : ", students[rollno]["name"])
            print("Age : ", students[rollno]["age"])
            print("Physics Marks : ", students[rollno]["marks"]["physics"])
            print("Maths Marks : ", students[rollno]["marks"]["maths"])
            print("-"*35,"\n")
            

        else:
            print("Not Found")  

        # 4. Delete Student

    elif user_input == "4":
        rollno = int(input("\nEnter Roll Number: "))
                
        if rollno in students:

            del students[rollno]

        else:
            print("Not Found")

                  
        # 5. Calculate Average Marks            

    elif user_input == "5":
        for rollno, details in students.items():

            phy_marks = details["marks"]["physics"]
            maths_marks = details["marks"]["maths"]

            average = (phy_marks + maths_marks) /2

            
               
                
            print(details["name"],"Average:", average)

            # 6. Find Topper

    elif user_input == "6":
        for rollno, details in students.items():

            phy_marks = details["marks"]["physics"]
            maths_marks = details["marks"]["maths"]

            average = (phy_marks + maths_marks) /2

            if average >  max_marks:
                max_marks = average 
                topper = details["name"]

        print("Topper : ", topper)
        print("Average:", max_marks)

# 7. Show Maximum Marks

    elif user_input == "7":
        for rollno,details in students.items():
            phy_marks = details["marks"]["physics"]

            if phy_marks> physics:
                physics = phy_marks
                physics_topper = details["name"]

            print("Physics Highest:", physics_topper )

            if maths_marks> maths:
                maths = phy_marks
                maths_topper = details["name"]
            
            print("Maths Highest:",maths_topper )



     # 8. Exit
    
    elif user_input == "8":

        print("Program Ends.")
        break
    
    else:
        print("Invalid choice! \n Please enter number between 1 and 8.")


     
        
          
                
                

                
                    
                       
        

    

