# 1. Write a program to print the reverse of the given string.
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





# 2. Given a number, check whether it is a prime number or not.
# Input 1
# 3
# Output 1
# Yes
# Input 2
# 4
# Output 2
# No

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True

# Test the function
input_num = int(input("Enter a number: "))
if is_prime(input_num):
    print("Yes")
else:
    print("No")
    



# 3. Given an array of numbers, arrange them in a way that it forms the largest value.
# Input
# [54, 546, 548, 60]
# Output
# 6054854654

# Note
# The arrangement 6054854654 gives the largest value.
# Constraints
# 1<=N<=1000
# 1<=Number<=1000000

def largest_number(arr):
    arr = list(map(str, arr))

    def compare(a, b):
        if a + b > b + a:
            return -1
        else:
            return 1

    arr.sort(key=compare)

    largest_num = ''.join(arr)

    return largest_num

input_list = [int(x) for x in input("Enter the list of elements: ").split(",")]
largest_num = largest_number(input_list)
print("Largest number:", largest_num)




# Given a number N, print reverse of number N.
# Input
# 988
# Output
# 889
# Note
# Do not print leading zeros in output.
# For example N = 100
# Reverse of N should be 1 not 001.
# Constraints
# 1<=N<=10000

def reverse_number(n):
    reversed_num = 0

    while n > 0:
        last_digit = n % 10
        reversed_num = (reversed_num * 10) + last_digit
        n = n // 10

    return reversed_num

input_num = int(input("Enter a number: "))
reversed_num = reverse_number(input_num)
print("Reversed number:", reversed_num)




# 5. Given an array of numbers, find the maximum and minimum element in the array.
# Input
# [54, 546, 548, 60]
# Output
# 548 54

def find_max_min(arr):
    if len(arr) == 0:
        return None, None

    max_num = arr[0]
    min_num = arr[0]

    for num in arr:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    return max_num, min_num

input_list = [int(x) for x in input("Enter the list of elements: ").split(",")]
max_num, min_num = find_max_min(input_list)
print("Maximum:", max_num)
print("Minimum:", min_num)

