# input() = A function that prompts the user to enter data
#           Returns the entered data as string!

name = input("Enter name: ")
# age = input("Enter age: ")
# here age is a string, not int so we have to make convert it to be an integer
age = int(input("Enter age: "))
age += 1

print("\nAssalamu Alikum!")
print(f"Hello {name}, so your are {age} years old")


#########################################################################
# Exercise 1 Rectangle Area Calculate
# Area = Width X Length 

print("\n---Rectangle Area Calculate---")
unit = input("Unit: ")
len = float(input("length: "))
wid = float(input("width: "))
area = len * wid
print(f"Area of the Rectangle: {area} {unit}²\n")
# to have superscript of 2 -> (²) press alt then type 1789
# in windows: Numlock on, Alt + 0178 = ²
# in mac: control + command + space = ²
# alt + 0179 = ³
print()

#########################################################################
# Exercise 2 shopping cart program
print("------Shopping cart program!------")
curency = input("What is the curency?: ")
item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many you like/want?: "))
total = price * quantity
print(f"You have bought {quantity} x {item}/s")
print(f"You have to pay: {total} {curency}.")
print()