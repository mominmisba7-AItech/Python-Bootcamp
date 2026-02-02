#Q.1: Sum of two integers:
# a = 5
# b = 7
# sum = a+b
# print(sum)


#Q.2: Sum and message:
# a = 12
# b = 7
# sum = a+b
# print(f"Sum of {a} and {b} is {sum}")


#Q.3: Accept numbers from user and print their sum:
# a = int(input("Enter the value of a:"))
# b = int(input("Enter the value of b:"))
# sum = a+b
# print(f"Sum of {a} and {b} is {sum}")


#Q.4: Read text from user and print it:
# name = input("Enter your name please:")
# age = int(input("Enter your age please:"))
# print(f"Hello {name}, You are {age} years old.")


#Q.5: Find Area and Perimeter of a rectangle:
# length = float(input("Enter your length: "))
# width = float(input("Enter your width: "))
# area = length * width
# perimeter = 2 * (length+width)
# print(f"Area = {area} sq units, Perimeter = {perimeter} units")


#Q.6: Find Area of Triangle using Heron's Formula:
# import math
# s1 = int(input("Enter the length of first side: "))
# s2 = int(input("Enter the length of second side: "))
# s3 = int(input("Enter the length of third side: "))
# s = (s1+s2+s3)/2                #first find semi-perimeter of triangle
# Area = math.sqrt(s*(s-s1)*(s-s2)*(s-s3))         #Area using Heron's formula 
# print(f"Area of Triangle is: {Area} sq.units")
       

#Q.7: Compund Intrest:
# P = float(input("Enter your principal amount: "))
# r = float(input("Enter your rate of interest: "))
# t = int(input("Enter time period in years: "))
# A = P*(1+r/100)**t
# CompoundInterest = A-P
# print("Total amount is",A)
# print(f"Compound Interest in Rs is {CompoundInterest}")


#Q.8: Greatest between Two:
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
greatest = a if a > b else b                #Using ternary operator:
print("Greatest number is",greatest)
print("Greatest number between two is",max(a,b))         #Using max: