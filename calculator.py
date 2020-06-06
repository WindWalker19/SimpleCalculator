from math import *

def add(a,b):
    return (a + b)

def sub(a,b):
    return(a - b)

def mul(a,b):
    return(a*b)

def div(a,b):
    return(a/b)

def power(a,b):
    return(pow(a,b))

i = 1
print("Thank you for choosing this calculator!")


while(i != 0):
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    operation = input("Enter the operation to be performed.")

    first = float(num1)
    second = float(num2)

    if(operation == "+"):
        answer = add(first,second)
        print(answer)
    elif(operation == "-"):
        answer = sub(first,second)
        print(answer)
    elif(operation == "*"):
        answer = mul(first,second)
        print(answer)
    elif(operation == "/"):
        answer = div(first,second)
        print(answer)
    elif(operation == "^"):
        answer = power(first,second)
        print(answer)
    else:
        print("Such operation does not exist.")

    choice = input("Enter 0 -> quit or 1 ->continue.")
    try:
        i =int(choice)
    except:
        print("You have entered the invalid input.")
        choice = input("ReEnter 0 -> quit or 1 ->continue.")
        i =int(choice)
