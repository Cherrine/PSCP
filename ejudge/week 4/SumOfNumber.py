"""sumofnumber"""

def calculator(target, result=0):
    """cal"""
    num = 0
    while num != -1:
        result += num
        if result == target:
            break
        num = int(input())
    print(result)
calculator(int(input()))
