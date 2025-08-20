
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result =", a + b)
elif op == "-":
    print("Result =", a - b)
elif op == "*":
    print("Result =", a * b)
elif op == "/":
    if b != 0:
        print("Result =", a / b)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operator")
