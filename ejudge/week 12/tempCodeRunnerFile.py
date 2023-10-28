    length = len(otp)
    if length == 4 and len(set(otp)) == 3:
        return True
    elif length == 6 and (len(set(otp)) == 4 or len(set(otp)) == 3):
        return True
    elif length == 8 and (len(set(otp)) == 5 or len(set(otp)) == 6):
        return True
    else:
        return False
check_otp()