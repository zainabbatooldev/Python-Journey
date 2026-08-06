dic = {
    "name" : "Ali",
    "age" : 20
}

# in operator

print("name" in dic)

# not in 

print("city" not in dic)

# check values

print("Alia" in dic.values())

# using membership in an if statement

if "name" in dic:
    print("Name is available")

else:
    print("Name is not available")