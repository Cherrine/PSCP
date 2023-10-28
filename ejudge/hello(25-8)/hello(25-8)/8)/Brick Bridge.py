"""Brick Bridge"""
def brickbridge(small_brick, large_brick, goal):
    """cal"""
    large_brick_use = goal // 5
    if large_brick_use < large_brick:
        large_brick = large_brick_use
    remain = goal - (large_brick * 5)
    if remain > small_brick:
        print("-1")
    else:
        print(remain)
brickbridge(int(input()), int(input()), int(input()))
