
# set is un order collection of unique elements

# unique

number={1,2,3,1,2,3,4,5,6}

print("set",number)


# add

number.add(10)

print("number added",number)

# remove


number.pop()

print("any value will be removed due to un order",number)

# will delete everything
number.clear()


print("empty",number)




num1= {1,2,3}

num2={3,4,5}


print("intersection",num1.intersection(num2))


print("symmetric difference",num1.symmetric_difference(num2))

print("union",num1.union(num2))

print("difference",num1.difference(num2))