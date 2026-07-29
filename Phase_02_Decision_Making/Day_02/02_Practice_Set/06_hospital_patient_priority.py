# Hospital Patient Priority
print("Patient Information")
age = int(input("Enter your age:"))
emergency = input("Emergency Yes/No:")
oxygen_level = int(input("Enter your oxygen level:"))
if emergency == "yes" or oxygen_level < 90:
    print("High Priority ")
elif age > 60 and oxygen_level <=95 and oxygen_level >=90:
    print("Medium Priority")
else:
    print("Low Priority")