def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2 
def div(n1, n2):
    return n1 / n2
print("Please select operation -\n 1. Add\n 2. Subtract\n 3. Multiply\n and 4. Divide\n")
sel = int(input("Select operations (1-4): "))
n1= int(input("Enter first number: "))
n2= int(input("Enter second number: "))
while sel == 4 and n2 == 0:
    print("Error! Division by zero is not allowed.")
    n2= int(input("Enter second number: "))
if sel == 1:
  print(n1, "+", n2, "=", add(n1, n2))
elif sel == 2:
    print(n1, "-", n2, "=", sub(n1, n2))
elif sel == 3:
    print(n1, "*", n2, "=", mul(n1, n2))
elif sel == 4:
    if n2 == 0:
        print("Error! Division by zero is not allowed.")
    print(n1, "/", n2, "=", div(n1, n2)) 
else:
    print("Invalid input")
  
