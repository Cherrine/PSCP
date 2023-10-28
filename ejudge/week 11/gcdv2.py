"""gcd"""
def gcd(numa, numb):
    """func"""
    while numb:
        numa, numb = numb, numa % numb
    return numa

def cal(num1, num2):
    """func"""
    result = gcd(num1, num2)
    print(result)
cal(int(input()), int(input()))
