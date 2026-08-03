#nested if ------  a if with in a if 

age = int(input("Enter your age:"))
cnic = input("Do you have CNIC(yes/no);")

if age>=18:
    if cnic == "yes":
        print("You can vote.")

    else:
        print("Your need CNIC.")

else:
    print("You can not vote.")
