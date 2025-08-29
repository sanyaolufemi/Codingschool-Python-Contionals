from biggest import bigges
from smallest import small
pass1=123
pass2=456
currentpass=int(input("Enter pass1: "))
if currentpass==pass1:
    Userpass=int(input("Enter pass2: "))
if Userpass==pass2:
    print("Access Granted")
    Userchoice=int(input("Enter choice: "))
if Userchoice==1:
    print("you chose to find simple interest")
    p=int(input("Enter principal: "))
    r=int(input("Enter Rate: "))
    t=int(input("Enter Time: "))
    SI=p*t*r/100
    print(f"The simple interest for the principal{p},the time{t},and the rate{r} is {SI}")
elif Userchoice==2:
    print("you chose to find the area of a triangle")
    b=int(input("Enter base: "))
    h=int(input("Enter height: "))
    AOT=1/2*b*h
    print(f"The area of triangle for base{b},height {h} is {AOT}")
elif Userchoice==3:
    print("you chose to find the area pf a rectangle")
    l=int(input("Enter Length: "))
    b=int(input("Enter Breath: "))
    AOR=l*b
    print(f"The area of a rectangle for lenght{l}, breath{b} is {AOR}")
elif Userchoice==4:
    x=int(input("Enter x: "))
    Valuex=4*pow(x,3)+2*pow(x,2)+x+6
    print(f"The value of of x for valuex is {Valuex}")
elif Userchoice==5:    
    bigges()
    
elif Userchoice==6:
    #biggest
    small()
    print("biggest")
else:
    print("Incorrect Password, Try Again")

