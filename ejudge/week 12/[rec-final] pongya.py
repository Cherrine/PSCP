"""pongya"""
def pongya(num):
    """function"""
    if num % 3 == 0:
        print("PONG")
    elif str(num)[-1] == "3":
        print("PONG")
    else:
        print(num)
pongya(int(input()))
