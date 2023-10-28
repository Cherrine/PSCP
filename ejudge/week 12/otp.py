"""otp"""
def check_otp():
    """function"""
    while True:
        otp = input()
        if otp == '0':
            break
        else: 
            length = len(otp)
            unique_digits = len(set(otp))
            if (length == 4 and unique_digits == 3) or \
               (length == 6 and 3 <= unique_digits <= 4) or \
               (length == 8 and 5 <= unique_digits <= 6):
                print("Valid")
            else:
                print("Invalid")
check_otp()
