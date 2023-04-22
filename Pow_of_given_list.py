list1=[int(x) for x in input("Enter the list of numbers: ").split()]
n = int(input("Enter the power number: "))
list2 = list(map(lambda x: x**n, list1))
print(list2)