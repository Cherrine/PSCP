"""fibonacci recursion"""

def fibonacci(num):
    """function"""
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

def main():
    """function"""
    print(fibonacci(int(input())))
main()
