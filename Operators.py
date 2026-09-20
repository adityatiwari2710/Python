#arithmetic operators
a = 7
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) # % we call this modulo (modulous operator) this is used to get the remainder of a division
print(a ** b) # ** we call it the power operator and it is a^b that is a raised to the power of b

# relational/comparison operators
a = 50
b = 20
print(a == b) # relational operators gives us either true or false value i.e; Boolean value
print(a != b)
print(a >= b)
print(a <= b)
print(a > b)
print(a < b)

# Assignment Operators
num1 = 10
num1 += 5 # this means we are adding 5 in the variable num1
print(num1)
num2 = 14
num2 -= 2 # this means we are subtrating 2 from the variable num2
print(num2)
num3 = 18
num3 *= 3 # this means we are multiplying by 3 to the variable num3
print(num3)
num4 = 12
num4 /= 4 # this means we are dividing by 4 to the variable num4
print(num4)
num5 = 16
num5 %= 3 # this means we are finding the remainder of the variable num5
print(num5)
num6 = 7
num6 **= 8 # this means we are raising 7 by power 8 i.e; 7^8
print(num6)

#logical operators ( these are basically boolean type data types)
a = 58
b = 89
print(not a > b) # a>b , in this case the ans is False and not of False means True
print(not True) # basically not means opposite of it like opposite of True is False
print(not False)
#for eg
value1 = False
value2 = True
print("AND Operator;",value1 and value2) #basically and means intersection
print("OR Operator;",value1 or value2) # or stands here for union
print("AND OPERATOR;",(a == b) and (a < b))
print("OR OPERATOR;", (a < b) or (a > b))