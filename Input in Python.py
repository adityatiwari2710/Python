name = input("enter your name: ")
print("WELCOME", name)

# we can do it in many ways
age = input("enter your age:")
print("Your Age is;", age)

"""
input (); result for input() is always a string(str)
int(input()) it is integer value
flaot(input()) it is flaoting value i.e; decimal value

"""

val = input("enter some value:")
print(type(val),val)

#for integer value
val1 = int(input("enter some value:"))
print(type(val1),val1)

#for floating value 
val2 = float(input("enter something:"))
print(type(val2),val2)
# for example
name1 = input("Enter Name:")
age1 = int(input("Enter Age:"))
marks = float(input("Enter Marks:"))
print("My name is:", name1)
print("And I am",age1)
print("I have obtained", marks)
