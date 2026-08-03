#check number enter by user is positive , neg or zero

num = int(input("Enter a number:"))

if num>0:
    print(f"{num} is positive.")

elif num<0:
    print(f"{num} is negative.")

else:
    print(" It's zero")