print("="*5,"MENU","="*5)
students = (
    ("Ali",19,"BSCS"),
    ("Saira",20,"BBA"),
    ("Alia",24,"BS Physics"),
)

search = input("\n Enter Name:").title()
for item in students:

    if search in item:
        print("found",item)

    # index found
    
for i,item in enumerate(students):
                
    
    if search in item:
        print("found at index",i)