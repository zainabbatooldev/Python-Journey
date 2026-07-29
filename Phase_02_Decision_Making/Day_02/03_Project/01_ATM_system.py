# ATM System
password = "12345"
balance = 2000
password_user = input("Enter your password:")

if password_user == password:
    print("Login Successful")
    print("Your balance is ", balance)
    withdraw = input("withdraw yes / no ")
    deposit = input("You want to deposit money? yes /no")
    if withdraw == "yes":
        withdraw_amount= int(input("Amount: "))
        if withdraw_amount <=2000:
            updated_balance = balance - withdraw_amount
            print(f"Now your balance is {updated_balance}")

        else :
            print("Insufficient Balance")

    elif deposit == "yes":
        deposit_amount= int(input("Amount: "))
        updated_balance = balance + deposit_amount
     
        print(f"Now your balance is {updated_balance}")


            

         
else:
    print("Incorrect Password.")
    