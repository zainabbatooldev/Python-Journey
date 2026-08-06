dic =  {
    "Ali" : {
        "age" : 20,
        "marks" : 90
    },
    
    "Alia" : {
        "age" : 20,
        "marks" : 90
    }
    
}

print(dic)
print(dic["Ali"]["age"])


# traversing

for name,details in dic.items():
    print("\n",name)
    for key , value in details.items():
        print(key , " : ", value)

