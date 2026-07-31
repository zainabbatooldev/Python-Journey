#Write a program to print multiplication table of a given number using for loop.
num = int(input("Enter a number for table:"))

for i in range (1,11):  # 1 including 11 excluding
    print(f"{num}X{i}={num*i}")
