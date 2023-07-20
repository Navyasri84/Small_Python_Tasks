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

# Test the function
input_list = [int(x) for x in input("Enter the list of elements: ").split(",")]
max_num, min_num = find_max_min(input_list)
print("Maximum:", max_num)
print("Minimum:", min_num)
