# def hello():
#     '''This function does not return value,  it prints only'''
#     print("Hello, World 1")
# hello()
# print(hello.__doc__)

# def hello2():
#     '''This function returns a value'''
#     return "Hello, World 2"

# print(hello2())
# print(hello2.__doc__)

def calculationMenu():
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

def userChoice():
    calculationMenu()
    print("Enter your choice..")
    choice = int(input("Choice: "))
    return choice
    

def calculation():
    ch = userChoice()
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    if ch == 1:
        print(f"Sum is {num1+num2}")
    elif ch == 2:
        print(f"Difference is {num1-num2}")
    elif ch == 3:
        print(f"Product is {num1*num2}")
    elif ch == 4:
        try:
            print(f"Quotient is {num1/num2}")
            print(f"Reminder is {num1%num2}")
        except:
            print("Second number cannot be zero")
        
calculation()