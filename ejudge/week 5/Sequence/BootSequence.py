"""_"""
def main():
    """_"""
    size = int(input())
    for num in range(1, size+1):
        if num == size:
            print(num, end="")
        else:
            print(num, end="_")
main()
