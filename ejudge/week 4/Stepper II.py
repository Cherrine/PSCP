"""_"""
def main():
    """_"""
    count1 = int(input())
    count2 = int(input())
    if count1 < count2:
        for i in range(count1, count2+1):
            print(i)
    else:
        for i in range(count1, count2-1, -1):
            print(i)
main()
