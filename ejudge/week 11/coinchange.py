"""coinchange"""
def coinchange(num):
    """function"""
    ans = 0
    ans += num//25
    num = num%25
    ans += num//10
    num = num%10
    ans += num//5
    num = num%5
    ans += num//1
    print(ans)
coinchange(int(input()))
