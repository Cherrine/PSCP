"""bookworm"""
def main():
    """function"""
    test = int(input())
    for _ in range(test):
        minute = float(input())
        timebook = sorted([float(input()) for _ in range(int(input()))])
        ans = 0
        for j in range(len(timebook)):
            if sum(timebook[:j+1]) > minute:
                break
            ans += 1
        print(ans)
main()
