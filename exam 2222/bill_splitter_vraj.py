


print("Welcome to the Bill Splitter App!\n")

while True:
 
    bill = float(input("\n Enter total bill amount: "))

    number = int(input("\nEnter number of people: "))

    per = int(input("\nEnter tip percentage (0/5/10/15/20): "))

    amount=(per/100)*bill

    total_tip= bill + amount

    person = total_tip / number

    print(f"\nTip Amount: ₹{amount:}")

    print(f"\n Total Bill (with Tip): ₹{total_tip:}")

    print(f"\n Each person should pay: ₹{person:}\n")

    Bill = input("Would you like to calculate another bill? (y/n): ").lower()

    if Bill != 'y':

        print("\n Thank's for Visit!")

        break
