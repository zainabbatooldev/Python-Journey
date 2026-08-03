# university admission system

matric = float(input("Enter your Matric %:"))

intermediate = float(input("Enter your Intermediate %:"))
entry_test = float(input("Enter your Entry Test %:"))

merit = (matric*0.20)+(intermediate*0.30)+(entry_test*0.50)
print(f"Merit = {merit}")

if merit>=85:
    print("Admission Confirm")
elif merit>=75 :
    print("Waiting List")
else:
    print("Not Selected")