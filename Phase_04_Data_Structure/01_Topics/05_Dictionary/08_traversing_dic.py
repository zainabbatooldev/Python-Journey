dic = {
    "name" : "Ali",
    "age" : 20
}

for key in dic:
    print(key)

for value in dic.values():
    print(value)

for key,value in dic.items():  # most commonly used
    print(key, ":" ,value)

    if key == "age":
        print("Age is : ",value)

