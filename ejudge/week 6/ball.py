"""ball"""
def ball(metre, time=0):
    """function"""
    while True:
        metre = (metre / 5) * 3
        if metre < 0.01:
            break
        time += 1
    print(time)
ball(float(input()))
