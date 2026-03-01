"""
1. Number in a range
Write a program that asks the user to enter two numbers
and checks whether the first number is in the range
from 1 to the second number (inclusive).

Example:

Enter the first number: 3
Enter the second number: 5
True
"""

print("1. Number in a range")
print("Enter the first number: ", end="")
num1 = int(input())
print("Enter the second number: ", end="")
num2 = int(input())
print(num2 >= num1 >= 1)


"""
2. Comparing numbers
Write a program that asks the user to enter three numbers
and compares the first number with the other two using
the operators greater than, less than, and equal to.

Example:

Enter the first number: 7
Enter the second number: 5
Enter the third number: 7

First greater than second: True
First less than third: False
First equal to third: True
"""

print()
print("2. Comparing numbers")

print("Enter the first number: ", end="")
number1 = int(input())
print("Enter the second number: ", end="")
number2 = int(input())
print("Enter the third number: ", end="")
number3 = int(input())

print("First greater than second: ", number1 > number2)
print("First less than third: ", number1 < number3)
print("First equal to third: ", number1 == number3)


"""
3. Logical operations
Write a program that asks the user to enter two boolean values
and prints the results of the logical operations:
and, or, and not.
Also print the results of equality and inequality comparisons.
Use the first value for the not operation.

Think about the best way to receive boolean input from the user.

Example:

Enter first value: <value1>
Enter second value: <value2>

and: True
or: True
not: False
equal: False
not equal: True
"""

print()
print("Logical operations")

print("Enter first boolean value (1/0): ", end="")
bool1 = bool(int(input()))
print("Enter second boolean value (1/0): ", end="")
bool2 = bool(int(input()))

print("and: ", bool1 and bool2)
print("or: ", bool1 or bool2)
print("not: ", not bool1)
print("equal: ", bool1 == bool2)
print("not equal: ", bool1 != bool2)


"""
4. Condition check
Write a program that takes two boolean values
(light is on and window is open) and checks:

- Whether both conditions are true.
- Whether at least one condition is true.

Example:

Light is on? True
Window is open? False
Both conditions true? False
At least one condition true? True
"""

print()
print("Condition check")

print("Light is on? (1/0): ", end="")
light_is_on = bool(int(input()))
print("Window is open? (1/0): ", end="")
win_is_open = bool(int(input()))

print("Light is on? ", light_is_on)
print("Window is open? ", win_is_open)
print("Both conditions true? ", light_is_on and win_is_open)
print("At least one condition true? ", light_is_on or win_is_open)


"""
5. Mobile tariff cost
Write a program that calculates the cost of a mobile plan:

- Base price: 30 euros.
- Each megabyte over 500 MB costs 0.2 euros.

The program should ask the user for the number of used megabytes
and print the total cost.

Example:

Enter used megabytes: 510
Total cost: 32.0
"""

print()
basic_max_mb = 500
basic_price = 30
extra_price = 0.2

print("Enter used megabytes: ", end="")
used_mb = float(input())

is_exceeded = used_mb > basic_max_mb
extra_mb = used_mb - basic_max_mb

total_price = float(is_exceeded * 0.2 * extra_mb + basic_price)

print("Total cost: ", total_price)