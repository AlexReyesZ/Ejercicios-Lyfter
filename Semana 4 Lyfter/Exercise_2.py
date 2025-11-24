def get_info():
    name=input("Enter your name: ")
    lastname=input("Enter your lastname: ")
    age=int(input("Enter your age "))

    if age < 3:
        stage = "baby"
    elif age < 12:
        stage = "child"
    elif age < 15:
        stage = "preteen"
    elif age < 18:
        stage = "teenager"
    elif age < 30:
        stage = "young adult"
    elif age < 60:
        stage = "adult"
    else:
        stage = "older adult "

    print(f"{name} {lastname}, you are {stage}.") 

get_info()



