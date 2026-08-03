print("="*5, "ATM MENU", "="*5)
correct_pin =  1234
balance = 100000
attempt= 1
attempt_left =3

user_pin = int(input("Enter PIN: "))

while attempt <= attempt_left:

    if user_pin != correct_pin :
        attempt_leftt = attempt_left - attempt
        print(f"Attempt left? {attempt_leftt}")
        attempt+=1
        print("\n","-"*35,"\n")

        if attempt_leftt ==0:
            print("Too many incorrect attempts.\nAccount locked")
            print("\n","-"*35,"\n") 

        elif attempt <= attempt_left :
            user_pin = int(input("Enter PIN: "))

    elif user_pin == correct_pin:
        print("1.  Check Balance")
        print("2.  Deposit")
        print("3.  Withdraw")
        print("4.  Exit")

        user_input = input("\n")

        if user_input == "1" or user_input == "Check Balance":

             print(f"Your Balance: {balance}")

        elif user_input == "2" or user_input == "Deposit":

            deposit_amount = int(input("Enter deposit amount pkr : "))

            if deposit_amount > 0 :

                balance = balance + deposit_amount
                print(f"New Balance: {balance} pkr")

            else:
                print("Negative amount reject.")

                



        elif user_input == "3" or user_input == "Withdraw":

            withdraw_amount = int(input("Enter withdraw amount pkr: "))

            if withdraw_amount <= balance:
                print("Please collect your cash.")

                balance = balance - withdraw_amount
                print(f"New Balance: {balance} pkr")

            else:

                print("Insufficient Amount")
                

        elif user_input  == "4" or user_input == "Exit":
            print(" 👏Thank you for using our ATM.")
            break

        else:
            print("Invalid input")
            

        print("\n","-"*35,"\n")




        
        

    