"""sqfree"""
def sqfree(num):
    """function"""
    is_square_free = [True] * (num + 1)
    start = 2
    while start * start <= num:
        if is_square_free[start]:
            for j in range(start * start, num + 1, start * start):
                is_square_free[j] = False
        start += 1
    print(sum(is_square_free) - 1)
sqfree(int(input()))
