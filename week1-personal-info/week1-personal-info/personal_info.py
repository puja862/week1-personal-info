# =========================================
# Personal Information Manager
# Author: Vemula Puja
# Description: A beginner Python program
# =========================================

print("=" * 40)
print("    PERSONAL INFORMATION MANAGER")
print("=" * 40)
print()

name = "Vemula Puja"
age = 21
city = "Hyderabad"
hobby = "Learning Python"

print("Please tell me about yourself:")
print("-" * 30)

favorite_food = input("What's your favorite food? ").strip()
while favorite_food == "":
    print("Food cannot be empty!")
    favorite_food = input("What's your favorite food? ").strip()

favorite_color = input("What's your favorite color? ").strip()
while favorite_color == "":
    print("Color cannot be empty!")
    favorite_color = input("What's your favorite color? ").strip()

age_in_months = age * 12

print()
print("=" * 40)
print("        YOUR INFORMATION")
print("=" * 40)
print()

print(f"Name           : {name}")
print(f"Age            : {age} years ({age_in_months} months)")
print(f"City           : {city}")
print(f"Hobby          : {hobby}")
print()
print(f"Favorite Food  : {favorite_food.title()}")
print(f"Favorite Color : {favorite_color.capitalize()}")

print()
print("=" * 40)
print("Thank you for using the program!")
print("=" * 40)
