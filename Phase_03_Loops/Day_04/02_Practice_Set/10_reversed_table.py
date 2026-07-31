#Write a program to print multiplication table of n using for loops in reversed order
num = int(input("Enter a number for table:"))

for i in range (10,0,-1):  # -1 for reversed
    print(f"{num}X{i}={num*i}")
