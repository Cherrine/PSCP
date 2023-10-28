"""isprime_large"""
import math
def prime(num):
    """function"""
    if num > 1:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                print("NO")
                break
        else:
            print("YES")
    else:
        print("NO")
prime(int(input()))
