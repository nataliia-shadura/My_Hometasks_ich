"""
1. Sign of a Number

Write a program that asks the user to enter a number
and determines whether the number is positive, negative, or equal to zero.
"""

num = float(input("Enter a number: "))

if num > 0:
    print("This number is greater than zero.")
elif num == 0:
    print("This number is equal to zero.")
else:
    print("This number is less than zero.")


print("--------------------------------------------------")

"""
2. Ticket Price Calculation

Write a program for an event ticket system.

The user enters the ticket type (standard or VIP) and their age.

Conditions:
- Children under 12 receive a 50% discount on all tickets.
- Adults (12 to 60 years old) pay the full price.
- Seniors (over 60 years old) receive a 30% discount only on standard tickets.

Ticket prices:
- Standard: 1000
- VIP: 3000
"""

price_std = 1000
price_vip = 3000

ticket_type = input("Enter ticket type (std/vip): ").lower()
age = float(input("Enter age: "))

if ticket_type == "std":
    price = price_std
elif ticket_type == "vip":
    price = price_vip
else:
    print("Invalid ticket type.")
    price = None

if price is not None:
    if age < 12:
        price *= 0.5
    elif age > 60 and ticket_type == "std":
        price *= 0.7

    print("Price =", price)


print("--------------------------------------------------")

"""
3. Sorting Numbers

Write a program that asks the user to enter three numbers
and prints them in ascending order, separated by commas.
"""

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 <= num2 and num1 <= num3:
    first = num1
    if num2 <= num3:
        second = num2
        third = num3
    else:
        second = num3
        third = num2

elif num2 <= num1 and num2 <= num3:
    first = num2
    if num1 <= num3:
        second = num1
        third = num3
    else:
        second = num3
        third = num1

else:
    first = num3
    if num1 <= num2:
        second = num1
        third = num2
    else:
        second = num2
        third = num1

print("Numbers in ascending order:", first, ",", second, ",", third)


print("--------------------------------------------------")

"""
4. Leap Year

Write a program that asks the user to enter a year
and checks whether it is a leap year.

A year is a leap year if:
- It is divisible by 4,
- It is not divisible by 100,
- Except when it is divisible by 400.

Display the appropriate message using print().
"""

year = int(input("Enter year: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Year", year, "is a leap year.")
else:
    print("Year", year, "is not a leap year.")