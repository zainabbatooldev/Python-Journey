# remove()
# discard()
# pop()
# clear()
# del

fruits = {"Apple","Banana","Orange","Mango"}

# remove()

#set_name.remove(value)

fruits.remove("Orange")  # remove orange
print(fruits) 
# fruits.remove("Grapes") # if element does not exists  error show
# print(fruits)

#discard()

#set_name.discard(value)


fruits.discard("Mango")
print(fruits)

fruits.discard("Grapes")  # if element does not exists  not show error
print(fruits)


#pop()

item = fruits.pop()  # remove random element
print(item)
print(fruits)


#clear()
fruits.clear()  # del set elements  
print(fruits)  # output empty set set()

#del 

del fruits  # del set

print(fruits) # error show
