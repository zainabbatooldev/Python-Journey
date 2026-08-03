#‘breakʼ is used to come out of the loop when encountered. It instructs the program to – exit the loop now.

print("Break statement in for loop")

for i in range(0,30):
    print(i)
    if i == 15:
        break

count=1

print("Break statement in while loop")
while count<=5:
    print(count)
    if count ==3:
        break
    count+=1

    