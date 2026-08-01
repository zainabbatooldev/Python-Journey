print("Number Guessing Game")
secret_num= 67
max_attempt = 5
attempt = 0
play= input("Play  (yes /no): ").lower()
while max_attempt<=5:
     if play == "yes":
        guess = int(input("Enter a Number: "))
    

        if guess < secret_num:
    
            print("Too Low")

        elif guess > secret_num:
    
            print("Too High")

        else:
            print("congratulations😍")

        max_attempt = attempt+1
        play= input("Play Again  (yes /no): ").lower()
   
if play== "no":  
    print("You guessed the number.")
    print(f"Attempt : {attempt}")

    




