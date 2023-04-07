'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 
13, 17, 31, 37, 71, 73, 79, and 97.
Write a python program to find and display the number of 
circular primes less than the given limit.
'''
def is_prime(num):
    cnt = 0
    for i in range(1,num//2):
        if num % i == 0:
            cnt += 1
    if cnt == 1:
        return True
    else:
        return False
print(is_prime(4))