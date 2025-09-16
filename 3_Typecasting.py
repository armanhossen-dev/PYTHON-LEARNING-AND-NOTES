# Typecasting = the processof converting a variable from one data type to another 
# using ->    str(), int(), float(), bool()
# this is especially useful while handling user input or doing any conversion

name = "Arman Hossen"
age = 22
cgpa = 3.5
is_student = True

print(f"1.  name = {name} and type = ", type(name), "\n")
print(f"2.  age = {age} and type = "  , type(age), "\n")
print(f"3.  cgpa = {cgpa} and type = " ,  type(cgpa), "\n")
print(f"4.  is_student = {is_student} and type = " ,  type(is_student), "\n")

cgpa = int(cgpa) # now this will only store 3 not .5
print(f"5.  cgpa = {cgpa} and type = " ,  type(cgpa), "\n")


age = float(age) 
print(f"6.  age = {age} and type = ", type(age),  "\n")

age = str(age)
print(f"7.  age = {age} and type = ", type(age),  "\n")

#while name was a string variable prev, and it contains any word or letter, while converting it to boolean then it will contain True, 
# if the name variable was containing an empty string, then after converting it to boolean it will cotain false
# thats how we can check if the user entered any stirng or not!
name = bool(name)
print(f"8.  name = {name} and type = ", type(name), "\n")

emptyString = ""
emptyString = bool(emptyString)
print(f"9.  emptyString = {emptyString} and type = ", type(emptyString), "\n")