import datetime

print("welcome to the interactive personal data collector!")


name=input("please enter your name:\n")

age=int(input("please enter your age:\n"))

height = float(input("please enter your Height in meters:\n"))

FavouriteNumber =  int(input("please enter your favorite number:\n"))

print("thank you! Here is the information we collected:\n")

print(f"Name:{name},(Type:{type(name)},Memory Address:{id(name)})")

print(f"Age:{age},(Type:{type(age)},Memory Address:{id(age)})")

print(f"Height:{height},(Type:{type(height)},Memory Address:{id(height)})")

print(f"Favourite:{FavouriteNumber},(Type:{type(FavouriteNumber)},Memory Address:{id(FavouriteNumber)}) ")


currentYear =datetime.datetime.now().year

user_age=currentYear - age;

print(currentYear)

print(f"Your birth year is {user_age}, based on your {age}\n")

print(f"thank you using the Personal Data Collector. GoodBye!")