def rev_list(input_list):
    return input_list[::-1]
list= [int(x) for x in input("Enter the list of elements: ").split(",")]
reverse_list= rev_list(list)
print(reverse_list)