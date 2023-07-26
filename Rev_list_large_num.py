# Given an array of numbers, arrange them in a way that it forms the largest value.
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
    # Convert the numbers to strings
    arr = list(map(str, arr))

    # Custom sorting function
    def compare(a, b):
        if a + b > b + a:
            return -1
        else:
            return 1

    # Sort the array using the custom sorting function
    arr.sort(key=compare)

    # Join the sorted array elements into a single string
    largest_num = ''.join(arr)

    return largest_num

# Test the function
input_list = [int(x) for x in input("Enter the list of elements: ").split(",")]
largest_num = largest_number(input_list)
print("Largest number:", largest_num)
