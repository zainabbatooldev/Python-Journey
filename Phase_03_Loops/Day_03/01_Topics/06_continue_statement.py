#continueʼ is used to stop the current iteration of the loop and continue with the next one. It instructs the
#Program to “skip this iteration”.

print("Continue statement in for loop")

for i in range(0,5):
    if i == 3:
        continue
    print(i)

count=1

print("Continue statement in while loop")
while count < 5:
    count+=1
    if count ==3:
        continue
    print(count)