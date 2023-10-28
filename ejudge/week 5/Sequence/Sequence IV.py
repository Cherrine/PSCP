"""_"""
def main():
    """_"""
    size = int(input())
    start = 1
    for _ in range(size):
        for num in range(start, start+size):
            print(num, end=" ")
        print()
        start += size
main()
