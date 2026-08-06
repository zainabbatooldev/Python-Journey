# list convert into set

numbers =[1,3,1,5,6]  

new_numbers = set(numbers)

print(new_numbers)

print(type(numbers))
print(type(new_numbers))

#tuple convert into set

fruits = ("Apple","Banana","Orange","Mango")

new_set = set(fruits)

print(new_set)

print(type(fruits))
print(type(new_set))

empty = {}  # is it empty set?? 

print(type(empty)) # its a dictionary , not a set

#empty set

empty = set()
print(type(empty))


# indexing not allowed

# access element of set method 

# Method 1   using for loop

for item in fruits:
    print(item)

# check a specific value

print("Apple" in fruits)