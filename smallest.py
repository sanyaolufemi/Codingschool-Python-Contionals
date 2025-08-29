def small():
    print("you chose to find the smallest of 5 numbers")
    n1=int(input("Enter num1: "))
    n2=int(input("Enter num2: "))
    n3=int(input("Enter num3: "))
    n4=int(input("Enter num4: "))
    n5=int(input("Enter num5: "))
    smallestnum=min(n1,n2,n3,n4,n5)
    print(f"The smallest of 5 numbers is {smallestnum}")