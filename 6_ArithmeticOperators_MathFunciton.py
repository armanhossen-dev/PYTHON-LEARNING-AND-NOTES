friends = 0
friends = friends + 1   # '+' addition operator
friends += 8            # '+=' argumented assignment operator

friends = friends - 2
friends -= 4            #3

friends = friends * 3   #9
friends *= 2            #18  

friends = friends/2     #9.0
# so if we devide any integer in python the next time it becomes float!!!
friends /= 3            #3.0

# exponens, power 
friends = friends **2   #9.0      # this is like ² of the frinds number, making square 
friends **= 2           #81.0     # 9² = 81.0  
# print(friends)

# modulus = give any remainder of devision
remainder = friends % 2 #1.0     # how much friend will be remain if i devide my friends number by 2  
# print(remainder)

#######################################################################################
# some build in math related functions
x = 3.14
y = 4.6
z = 5.5

# --------------------------------------------------------------------
#round(variable) returns a int

#round makes the float into the  nearest int number, 
# if less than .5 then makes it to lower int number, 
# if big from .5 or same then upper int number

result  =  round(x)
# print(result) #3
result  =  round(y)
# print(result) #5 
result  =  round(z)
# print(result) #6



# --------------------------------------------------------------------
#abs(variable) reutrns a possitive int 
a = -3
#absolute value of a number or variable
result = abs(a) #abs() - the absolute value is the distance between number and zero alwasy possitve
# print(result) #3



# --------------------------------------------------------------------
# pow(base, power)
b = 3
result = pow(b, 4)
# print(result) #81



# --------------------------------------------------------------------
# max(a, b, c, . . . ) finding max value among lots of number , it returns the max value

x1 = 21
y1 = 30
z1 = 23

result = max (x1, y1, z1) 
# print(result) #30



# --------------------------------------------------------------------
# min(a,b,c, . . . ) finding min value among lots of number, it returns the min value

x2 = 2
y2 = -1
z2 = -1.5
result = min(x2, y2, z2)
# print(result) #-1.5



# --------------------------------------------------------------------
# https://youtu.be/ix9cRaBkVe0?t=2670