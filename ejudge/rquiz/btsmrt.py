"""BTS MRT"""
def btsmrt(day, age, height):
    """Price list"""
    if age < 14 and height < 90:
        print("FREE")
    elif day == "Children Day" and age < 14 and height <= 140:
        print("FREE")
    elif day == "Senior Day" and age >= 60:
        print("FREE")
    elif day == "Normal Day":
        print("PAY")
    else:
        print("PAY")
btsmrt(str(input()), float(input()), float(input()))
