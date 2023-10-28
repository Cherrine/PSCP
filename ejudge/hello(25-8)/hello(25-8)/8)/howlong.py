"""howlong"""
def howlong(text):
    """cal"""
    hotdog = 0
    if int(text) < 0:
        for _ in text:
            hotdog += 1
        print(hotdog-1)
    elif int(text) > 0:
        for _ in text:
            hotdog += 1
        print(hotdog)
    else:
        for _ in text:
            hotdog += 1
        print(hotdog)
howlong(input())
