# Given a number, check whether it is a prime number or not.
# Input 1
# 3
# Output 1
# Yes
# Input 2
# 4
# Output 2
# No

def is_prime(num):
    if num<2:
        return False
    
    for i in range(2, int(num**0.5)+1):
        if num % i== 0:
            return False
    return True

input_num = int(input("Enter a number: "))
if is_prime(input_num):
    print("Yes")
else:
    print("No")