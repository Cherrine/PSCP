"""fizzbuzz"""
def main():
    """function"""
    num = int(input())
    for count in range(1, num+1):
        if count % 3 == 0 and count % 5 == 0:
            print("FizzBuzz")
        elif count % 3 == 0:
            print("Fizz")
        elif count % 5 == 0:
            print("Buzz")
        else:
            print(count)
main()
