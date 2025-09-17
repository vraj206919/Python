
    # EXAM

print("Welcome to Inventory List Analyzer!")

items = ["Milk","Chocolate","Wafers","Biscuit0"]
categories = [ ]
quantities = [ ]

while True:
        name = input("Enter item name: ")
        category = input("Enter category: ")
        quantity = int(input("Enter quantity: "))

        items.append(name)
        categories.append(category.lower())
        quantities.append(quantity)

        choice = input("Do you want to add more items? (y/n): ")
        if choice.lower() != "y":
            break

total_items = len(items)

print("Total Different Items:", total_items)

print("Explanation: You entered", total_items, "different items:", ", ".join(items) + ".")


total_quantity = sum(quantities)

print("\nTotal Quantity in Stock:", total_quantity)

print("Explanation: Sum of all quantities:", " + ".join(map(str, quantities)), "=", total_quantity)


average_quantity = total_quantity / total_items

print("\nAverage Quantity per Item:", average_quantity)

print("Explanation: Average =", total_quantity, "total /", total_items, "items")



max_quantity = max(quantities)

max_item = items[quantities.index(max_quantity)]

print("\nMost Stocked Item:", max_item, "(", max_quantity, "units )")

print("Explanation:", max_item, "has the highest quantity among all items.")



min_quantity = min(quantities)

min_item = items[quantities.index(min_quantity)]

print("\nLeast Stocked Item:", min_item, "(", min_quantity, "units )")

print("Explanation:", min_item, "has the lowest quantity.")


unique_categories = set(categories)


print("Unique Categories in Inventory:", unique_categories)

print("Explanation: Categories are taken from user input and converted to lowercase.")
print("No duplicates are shown here.")

print("Items Sorted by Quantity (High to Low):")

sorted_items = sorted((quantities, items), reverse=True)

for idx, (qty, item) in enumerate(sorted_items, start=1):
        print(f"{idx}. {item} - {qty} units")

print("Explanation: Items are sorted using the quantity field from highest to lowest.")

print("Categories in Alphabetical Order:")

sorted_categories = sorted(unique_categories)

for idx, cat in enumerate(sorted_categories, start=1):
        print(f"{idx}. {cat}")
print("Explanation: The set of unique categories was sorted alphabetically for display.")