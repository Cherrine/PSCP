"""inverter"""
def inverter(binary):
    """function"""
    check = ""
    for char in binary:
        if char == "0":
            check += "1"
        else:
            check += "0"
    for num in range(len(check)):
        if check[num] == "1":
            print(check[num:])
            break
inverter(input())
