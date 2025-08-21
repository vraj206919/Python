a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a < b:
    if a < c:
        print("Minimum =", a)
    else:
        print("Minimum =", c)
else:
    if b < c:
        print("Minimum =", b)
    else:
        print("Minimum =", c)
