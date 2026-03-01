"""
1. Sum of the digits
Write a program that asks the user to enter a four-digit number
and prints the sum of its digits.

Example:

Enter a four-digit number: 1634
Sum of digits: 14
"""

print("Task1. Sum of the digits")
print("Enter a 4-digit number, digit by digit:")

num1 = int(input("Digit 1: "))
num2 = int(input("Digit 2: "))
num3 = int(input("Digit 3: "))
num4 = int(input("Digit 4: "))

summa = num1 + num2 + num3 + num4
print("Sum =", summa)


"""
2. Multiplying numbers
Write a program that:
- asks the user to enter two numbers,
- multiplies them,
- and prints the result followed by both numbers separated by hyphens.
Do not store the multiplication result in a separate variable.

Example:

Enter the first number: 4
Enter the second number: 5
Result: 20-4-5
"""

print()
print("Task2. Multiplying numbers")

print("Enter first number:", end=" ")
num1 = int(input())

print("Enter second number:", end=" ")
num2 = int(input())

print("Result:", str(num1 * num2) + "-" + str(num1) + "-" + str(num2))


"""
3. Calculation without using % and //
Write a program that asks the user to enter two numbers
and calculates:
- the remainder of division
- the integer division result

Do not use the % or // operators.

Example input:
Enter the first number: 10
Enter the second number: 3

Example output:
Remainder: 1
Integer division: 3
"""

print()
print("Task3. Calculation without using % and //")

print("Enter first number:", end=" ")
number_1 = int(input())

print("Enter second number:", end=" ")
number_2 = int(input())

int_div_res = int(number_1 / number_2)
rest = number_1 - int_div_res * number_2

print("Remainder:", rest)
print("Integer division:", int_div_res)