try:
    a = "100"
    b = int(a)
    print(b)
except:
    print("Error")
    
    
try:
    a = "hi"
    b = int(a)
    print(b)
except:
    print("Error")
    
# a = 10
# b = 0
# print(a/b)

try:
    a = 10
    b = 0
    print(a/b)
except ZeroDivisionError:
    print("Division by zero not possible")
    
try:
    a = "hi"
    b = int(a)
    raise TypeError
except:
    print("Type Error")
finally:
    print("Finally Block")
    
    

try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    if number2<0:
        raise TypeError
    division = number1/number2
    division2 = num1/num2
    print(f"Result of {number1}/{number2} is {division}")
except ZeroDivisionError:
    print("Division by zero is not possible")
except ValueError:
    print("Numbers are allowed")
except TypeError:
    print("Numbers below zero are not allowed")
except NameError:
    print("Variables are not defined")