# A dictionary is a built-in Python data structure that stores data as key-value pairs.

# Key → A unique identifier.
# Value → The data associated with that key.

# Think of it like a real dictionary:

# Word → Meaning
# Key → Value


dic = {
    "name" : "Ali",
    "age" : 20
}

print(dic)

# Features of a Dictionary

# Stores data in key-value pairs.
# Keys are unique (no duplicate keys).
# Values can be duplicated.
# Mutable (you can add, update, or delete items).
# Ordered (Python 3.7+ preserves insertion order).
# Can store different data types.

# empty dic

student = {}
print(student)
print(type(student))

# using dic() constructure

student = dict(name= "zainab", age= 40)
print(student)


# create from a list of tuple

dic = dict([
    ("name", "ahmed"),
    ("age", 23) 
])

print(dic)