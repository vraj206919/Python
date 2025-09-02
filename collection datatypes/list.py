


# list is order data collection and its mutable meaning we can modify the value or element of list 

fruits = ["apple","banana","mango"]


# add methods 


# append used to add element in list from last

fruits.append("cherry")

print("appending OP",fruits)

# insert method used to add element in list at specific position

fruits.insert(2,"blue-berry")

print("adding specific position",fruits)


#  extend method used to add more than one element in list 

fruits.extend(["pineapple","watermelon"])

print("adding multiple elements",fruits)




# remove methods

fruits.pop()

print("removing last element",fruits)


# 

fruits.pop(2)

print("removing element at specific position",fruits)



fruits.remove("banana")

print("removing specific element using value",fruits)

del fruits[0]

print("deleting first element in list",fruits)

# update 


fruits[0] = "pineapple"

print("updating first element",fruits)

# sort 

number = [5,8,4,6,9,1,1,1,1]

print("unordered number",number)

# ascending
number.sort()

print("sorted number",number)

# descending order 

number.sort(reverse=True)

print("number in descending order",number)

# count


print("counting value",number.count(1))


# index

print("index",number.index(1))