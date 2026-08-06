# After creating a dictionary, you can access its values using the key.

# There are two main ways:

# Square Brackets []
# get() Method


# Square Brackets []

# dictionary_name["key"]

dic = {
    "name" : "Ali",
    "age" : 20
}



print(dic)

print(dic["name"])

# print(dic["city"]) KeyError: 'city'
# get() Method


# dictionary.get("key")

print(dic.get("age"))
print(dic.get("city")) # none output  ✅ No error occurs.
print(dic.get("city" , "not found")) 

