n= [int(x) for x in input("Enter numbers: ").split()]

a= list(filter(lambda x: (x%2 == 0), n))
b= list(filter(lambda x: (x%2 != 0), n))
print("List of  Even numbers:",a)
print("List of Odd numbers:",b)