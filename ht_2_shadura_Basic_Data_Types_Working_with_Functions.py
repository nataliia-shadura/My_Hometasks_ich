"""
1. Greeting with an exclamation mark
Write a program that prints the string "Hello, world!".
Use the end parameter so that the output ends with an exclamation markinstead of a newline.
"""

print("Task1. Greeting with an exclamation mark")
string = "Hello, world"
print(string, end='!')


"""
2. Quotation
Write a program that prints the following string:
She said: "It's amazing!"

Solve the task in two different ways while producing the same output.
"""

print('\n')
print("Task2. Quotation")

string_1 = "She said:"
string_2 = '"It\'s amazing!"'
print(string_1, string_2)
print(string_1 + " " + string_2)


"""
3. Number sequence
Write a program that prints the numbers from 1 to 5 inclusive.
The numbers must be separated by "---".
Use the sep parameter.

Example output:
1---2---3---4---5
"""

print()
print("Task3. Number sequence")
print(1, 2, 3, 4, 5, sep='---')


"""
4. Whitespace characters
Write a program that prints two lines using a single print() call:
- The first line should start with a tab character.
- The second line should appear on a new line.

Example output:

    First line with a tab

Second line on a new line
"""

print()
print("Task4. Whitespace characters")

string_t = "First line with a tab"
string_n = "Second line on a new line"
print("\t" + string_t)
print(string_n)


"""
5. Text with quotation marks
Write a program that prints the following string:
This is the file "example.txt"

Solve the task in multiple ways.
"""

print()
print("Task5. Text with quotation marks")
string_file = "This is the file"
string_fname = "example.txt"

print(string_file, '"', string_fname, '"', sep='')
print(string_file + " " + '"' + string_fname + '"')