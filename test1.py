
password = 502615

UserPass = int(input("ENter your password: "))
if UserPass == password:
    print("correct")
    UserChoice = int(input("Enter choice of operations: "))

    if UserChoice == 1:
        print("you chose 1")
        num1 = int(input("Input the first number: "))
        num2 = int(input("Input the first number: "))

        Average = (num1+num2)/2

        print(f"")
    elif UserChoice == 2:
        print("you chose 2")
    elif UserChoice == 3:
        print("you chose 3")
    elif UserChoice == 4:
        print("you chose 4")
    else:
        print("invalid")
        
    
else:
    print("incoorect")


