"""Phone Number"""
def phonenumber(phonenum, type):
    if type == "Domestic" and len(str(phonenum)) == 9:
        print("0{} {} {}".format(str(phonenum)[0], str(phonenum)[1:5], str(phonenum)[5:]))
    elif type == "International" and len(str(phonenum)) == 8:
        print("+66 {} {}".format(str(phonenum)[0:4], str(phonenum)[4:]))
    elif type == "International" and len(str(phonenum)) == 9:
        print("+66{} {} {}".format(str(phonenum)[0], str(phonenum)[1:5], str(phonenum)[5:]))
    else:
        print("0 {} {}".format(str(phonenum)[0:4], str(phonenum)[4:]))

phonenumber(int(input()), str(input()))