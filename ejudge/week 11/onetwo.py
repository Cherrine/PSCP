"""onetwo"""
def onetwo(num):
    """function"""
    if num == 1:
        return "1"
    elif num == 2:
        return "2"
    else:
        return onetwo(num - 1) + onetwo(num - 2)

def calculate(num):
    """function"""
    print(onetwo(num))
calculate(int(input()))
