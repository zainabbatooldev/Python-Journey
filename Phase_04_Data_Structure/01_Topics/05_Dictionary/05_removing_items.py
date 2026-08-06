# pop()
# popitem()
# del
# clear()



dic = {
    "name" : "Ali",
    "age" : 20
}

# pop()

# Removes an item using its key.

dic.pop("age")
print(dic)

# popitem()

# Removes the last inserted key-value pair.
dic = {
    "name" : "Ali",
    "age" : 20
}

dic.popitem()
print(dic)

# del

# Deletes a specific key or the entire dictionary.

dic = {
    "name" : "Ali",
    "age" : 20
}
del dic["age"]

print(dic)

# clear()

# Removes all key-value pairs but keeps the dictionary.

dic.clear()

print(dic)
