print("\nAlright, to start this off, pick your first number!")
x = float(input("Enter first number: "))

print("\nNext, select from these options what operation you would like to use!")
print("Here are the options:\n1: Addition\n2: Subtraction\n3: Multiplication\n4: Division")
y = input("Enter your operation: ")

print("\nLastly, select your second number!")
z = float(input("Enter second number: "))

if y == "1" or y == 'Addition':
    print(x+z)
if y == "2" or y == 'Subtraction':
    print(x-z)
if y == "3" or y == 'Multiplification':
    print(x*z)
if y == "4" or y == 'Division':
    if z == 0:
        print("Error: division by zero")
    else:
        if x%z == 0:
            print(int(x/z))
        if x%z != 0:
            print(x/z)











"""def addNums(x, y):
    return x + y

def subNums(x, y):
    return x - y

def multNums(x, y):
    return x * y

def divNums(x, y):
    if (y == 0):
        return "Error division by 0"
    else:
        return x / y

operator = int(input("1. Addition \n2. Subtract\n3. Multiply\n4. Divide\nWhich operation would you like to perform?: "))

firstNum = int(input("Enter first number: "))
secondNum = int(input("Enter second number: "))

match operator:
    case 1:
        print(addNums(firstNum, secondNum))
    case 2:
        print(subNums(firstNum, secondNum))
    case 3:
        print(multNums(firstNum, secondNum))
    case 4:
        print(divNums(firstNum, secondNum))
    case _:
        print("Error with operator")"""

