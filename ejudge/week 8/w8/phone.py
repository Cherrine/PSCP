"""iPhone 13 Again"""
def price_1(name, size):
    if name == "iPhone 13 mini":
        if size == "128 GB":
            print("25900")
        elif size == "256 GB":
            print("29900")
        elif size == "512 GB":
            print("37900")
        else:
            print("Not Available")
    elif name == "iPhone 13":
        if size == "128 GB":
            print("29000")
        elif size == "256 GB":
            print("33900")
        elif size == "512 GB":
            print("41900")
        else:
            print("Not Available")
    else:
        print("Not Available")
def price_2(name_2, size_2):
    if name == "iPhone 13 Pro":
        if size == "128 GB":
            print("38900")
        elif size == "256 GB":
            print("42900")
        elif size == "512 GB":
            print("50900")
        elif size == "1 TB":
            print("58900")
        else:
            print("Not Available")

    elif name == "iPhone 13 Pro Max":
        if size == "128 GB":
            print("42900")
        elif size == "256 GB":
            print("46900")
        elif size == "512 GB":
            print("54900")
        elif size == "1 TB":
            print("62900")
        else:
            print("Not Available")
    else:
        print("Not Available")


price(str(input()), str(input()))
