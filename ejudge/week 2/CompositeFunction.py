"""CompositeFunction"""
def result(num):
    """result"""
    print("{:.2f}".format(funcf(funcg(num))))
    print("{:.2f}".format(funcg(funcf(num))))

def funcf(num):
    """f(x)"""
    return 2 * num

def funcg(num):
    """g(x)"""
    return num / 2 + 1

result(int(input()))
