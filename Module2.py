#Q.1: Even or odd number:
# num = int(input("Enter your number:- "))
# if num%2 == 0:
#     print(f"{num} is even number.")
# else:
#     print(f"{num} is odd number.")


#Q.2: Valid voter or not:
# name = input("Enter your name:- ")
# age = int(input("Enter your age:- "))
# if age >= 18:
#     print(f"Hello {name}, you are a valid voter.")
# else:
#     rem_age = 18-age
#     print(f"Hello {name}, you will be eligible to vote in {rem_age} years.")


#Q.11: Weekdays:
# days = int(input("Enter a day between (1 to 7):-"))
# if days == 1:
#     print("Monday")
# elif days == 2:
#     print("Tuesday")
# elif days == 3:
#     print("Wednesday")
# elif days == 4:
#     print("Thursday")
# elif days == 5:
#     print("Friday")
# elif days == 6:
#     print("Saturday")
# elif days == 7:
#     print("Sunday")
# else:
#     print("Invalid Input")


#Q.12: Leap Year:
# year = int(input("Enter year please:- "))
# if year % 100 == 0 and year % 400 == 0:
#     print(f"{year} is a leap year.")
# elif year % 100 != 0 and year % 4 == 0:
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")


#Q.13: Calculate Electricity Bill:
# units = int(input("Enter the number of units:- "))
# cost = 0
# if units <= 100:
#     cost = units*4.2      # For the first 100 units the rate is rs.4.2 per unit.
    
# elif units <= 200:
#     cost = (100*4.2) + ((units-100)*6)      # For the next 100 units the rate is rs 6 per unit.
    
# elif units <= 400:
#     cost = (100*4.2) + (100*6) + ((units-200)*8)   #For the next 200 units the rate is rs 8 per unit.
    
# else:                  # For the above 400 units the rate is rs 13 per unit.
#     cost = (100*4.2) + (100*6) + (200*8) + ((units-400)*13)
# print(f"Total bill amount:{cost}")


#Q.14: Shop Discount:t
# totalPrice = int(input("Enter Your Total price amount:- "))
# payable = 0
# if totalPrice <= 5000:
#     payable = totalPrice
# elif 5000 < totalPrice <= 7000:
#     payable = totalPrice - (totalPrice * 5 / 100)
# elif 7000 < totalPrice <= 9000:
#     payable = totalPrice - (totalPrice * 10 / 100)
# else:
#     payable = totalPrice - (totalPrice * 20 / 100)
# print(f"Total payable amount is {payable}")

n = 5
for i in  range(1,6):
    print("Hello World")
