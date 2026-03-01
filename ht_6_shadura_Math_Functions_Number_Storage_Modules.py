"""Mathematical Rounding
Write a program that takes a floating-point number and rounds it to an integer according to the rules of school mathematics,
not banker's rounding. The program must work correctly with both positive and negative numbers.

Example output:

Enter a real number: 2.5
Rounded value: 3
"""

import math

num_init = float(input("Enter float number: "))

whole_part = math.floor(num_init)
fraction = num_init - whole_part

if num_init >= 0:
    if fraction < 0.5:
        print("Rounded number =", whole_part)
    else:
        print("Rounded number =", whole_part + 1)
else:
    whole_part = math.ceil(num_init)
    fraction = whole_part - num_init
    if fraction < 0.5:
        print("Rounded number =", whole_part)
    else:
        print("Rounded number =", whole_part - 1)

print("---------------------------------------------")

"""Hypotenuse of a Triangle

Write a program that asks the user for the lengths of the two legs of a right triangle
and calculates the length of the hypotenuse.
The hypotenuse is equal to the square root of the sum of the squares of the legs.

Example output:
Enter the length of the first leg: 3
Enter the length of the second leg: 4
Hypotenuse length: 5.0
"""

side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
hypotenuse = math.sqrt(pow(side_a, 2) + pow(side_b, 2))
print("hypotenuse =", hypotenuse)