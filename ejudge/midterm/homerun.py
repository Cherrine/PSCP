"""homerun"""
def homerun():
    """function"""
    times = int(input())
    ranges = float(input())
    home = 0
    for _ in range(times):
        branges = float(input())
        if ranges > branges:
            home += 1
        else:
            pass
    print(home)
homerun()
            