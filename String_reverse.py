# Write a program to print the reverse of the given string.
# Input
# codecode
# Output
# edocedoc
# Input Constraints
# 1<=Length of string<=100
# Input string contains only lowercase characters ['a' to 'z'].


def rev_str(input_str):
    return input_str[::-1]

input_string= input("Enter a string: ")
reversed_string = rev_str(input_string)
print("Reversed String:", reversed_string)