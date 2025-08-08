
class calculate:
    def __init__(self,x,operator,y):
        self.x = x
        self.operator = operator
        self.y = y
    def add(self):
        print(f'{self.x + self.y}')
    def sub(self):
        print(f'{self.x - self.y}')
    def mult(self):
        print(f'{self.x * self.y}')
    def div(self):
        print(f'{self.x / self.y}')
    def exp(self):
        print(f'{self.x ** self.y}')

try:
    x = float(input("Enter first number: "))
except ValueError:
    print("Enter valid number.")

print("Select an operator:\n1. Addition\n2. Subtraction\n3. Multiplication\n" \
"4. Division\n5. Exponential")
