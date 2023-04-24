# n = [int(x) for x in input("Enter the list of numbers: ").split()]
# n.sort()
# print(*n)

n = [int(x) for x in input("Enter the list of numbers: ").split()]
n.sort(reverse=True)
print(*n)