#Q.1) Accept an integer and print "Hello World" n times using loops.
# n = 5
# for i in range(1,6):
#     print("Hello World")


# Q.2) Print all natural numbers up to a given limit.
# n = 10
# for i in range(1,11):
#     print(i)


#Q.3) Calculate the sum of the first 'n' natural numbers.
# n = 10
# sum = 0
# for i in range(1,11):
#     sum = sum + i 
# print(f"Sum of the first 10 natural numbers is {sum}")


#Q.4) Calculate the factorial of a given number.
# n = int(input("Enter your number:- "))
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# print(f"Factorial of a given number is {fact}")


#Q.5) Check if a given number is a prime number or not.
# n = int(input("Enter your number:- "))
# if n <= 1:               # Prime number starts from 2 so.
#     print(f"{n} is not a prime number")
# else:
#     is_prime = True            # We assume the number is prime first.
#     for i in range(2,n):
#         if n % i == 0:        # if remainder becomes 0 break the statement and mark it as not prime
#          is_prime = False
#         break
#     if is_prime:
#       print(f"{n} is a prime number")
#     else:
#       print(f"{n} is not a prime number")  


#Q.6) Calculate the sum of the digits of a given number.
# num = input("Enter your number:- ")                   # Here we don't take int because int in for loop is not iterable.
# sum_digit = 0 
# for digit in num:                                     # means take one character at a time from the string & store it in digit
#     sum_digit = sum_digit + int(digit)                # Converts char to an int
# print(f"Total sum of your numbers is {sum_digit}")

# Using While loop:
# num = int(input("Enter your number:- "))
# sum_digit = 0
# while num > 0:                         # Check upto n becomes zero
#     digit = num % 10                   # Remove last digit and add to the sum_digit
#     sum_digit = sum_digit + digit
#     num = num // 10
# print(f"Sum of digits = {sum_digit}")


#Q.7) Print the reverse number: ex., 12345 = 54321.
# n = int(input("Enter your number:-"))
# rev = 0
# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10
# print(f"Reverse order of your number is {rev}")


