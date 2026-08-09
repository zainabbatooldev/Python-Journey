print("="*5,"Shopping List Manager","="*5)
shopping_list = []

while True:

    print("1. Add Item")
    print("2. Remove Item")
    print("3. Update Item")
    print("4. Search Item")
    print("5. Show All Item")
    print("6. Count Total Item")
    print("7. Sort Item")
    print("8. Clear Item")
    print("9. Exit")

    print("-"*35)
    user_input = input("\n").title()

    if user_input == "1" :
        item = input("\nEnter Item: ").title()

        if item not in shopping_list:
            
            shopping_list.append(item)
            print(f"{item} added successfully.")

        else:
            print("it already exists.")

    elif user_input == "2" :
        item = input("\nEnter Item: ").title()
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed successfully.")
        else:
            print(f"{item} not found.")

    elif user_input == "3":
        item= input("\nChange Item:").title()
        new_item = input("New Item: ").title()
        if item in shopping_list:

            item_index=shopping_list.index(item)
            shopping_list[item_index]= new_item
            
            print(f" Your list updated successfully.")

        else:
            print("Item not found.")

    elif user_input == "4":
        item = input("\nEnter Item:").title()
        if item in shopping_list:
            print("Item found.")
        else:
            print("Item not found.")

    elif user_input == "5":
        print("-"*5,"Shopping list","-"*5)
        i = 1
        if not shopping_list:
            print("\nList is empty.")
        else:
            for item in shopping_list:
                print(f"\n{i}.  {item}")
                i+=1



    elif user_input == "6":
        print("Total item:",len(shopping_list))

    elif user_input == "7":
        shopping_list.sort()
        
        print("-"*5,"Shopping list","-"*5)
        i = 1
        for item in shopping_list:
            print(f"\n{i}.  {item}")
            i+=1

    
    elif user_input == "8":
        shopping_list.clear()
        print("Shopping list is empty.")

    elif user_input == "9":
        print("Program ends.")
        break

    else:
        print("Invalid choice! \n Please enter number between 1 and 9.")

    print("-"*35)

   

        