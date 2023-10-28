"""_"""
def main():
    """_"""
    size = int(input())
    for row in range(size):
        for num in range(2 + row, 2 + row + size):
            print(num, end=" ")
        print()
main()
