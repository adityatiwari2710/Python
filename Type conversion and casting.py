#type conversion
a = 2
b = 4.35
sum1 = a + b # 2.0 + 4.35 = 6.35
print(sum1)

"""
we cannot add a string and int or float it shows error
for eg.
a = "2"
b = 1
sum = a + b # it will show error
"""
#type casting
a = int("2") # also we can write it as float("2") or in any data type we want to convert it
b = 3.35
sum2 = a + b
print(sum2)

# we can also convert something in string for eg
a = 2.14
a = str(a)
print(type(a))