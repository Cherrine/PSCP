"""ddadadad"""
def main():
    """dadadada"""
    number = int(input())
    for row in range(number):
        for col in range(row+1):
            print(col+1, end=" ")
        print()
    for row in reversed(range(number)):
        for col in range(row):
            print(col+1, end=" ")
        print()
main()
