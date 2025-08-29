def bigges():
    print("you chose to find the biggest of 5 numbers")
    n1=int(input("Enter num1: "))
    n2=int(input("Enter num2: "))
    n3=int(input("Enter num3: "))
    n4=int(input("Enter num4: "))
    n5=int(input("Enter num5: "))
    Maxnum=max(n1,n2,n3,n4,n5)

    print(f"The biggest of 5 numbers is {Maxnum}")

    return Maxnum