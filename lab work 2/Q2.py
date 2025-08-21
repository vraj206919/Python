a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a > b:
    if a > c:
        if a > d:
            print("Maximum =", a)
        else:
            print("Maximum =", d)
    else:
        if c > d:
            print("Maximum =", c)
        else:
            print("Maximum =", d)
else:
    if b > c:
        if b > d:
            print("Maximum =", b)
        else:
            print("Maximum =", d)
    else:
        if c > d:
            print("Maximum =", c)
        else:
            print("Maximum =", d)
