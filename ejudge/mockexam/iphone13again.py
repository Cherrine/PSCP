"""iPhone 13 Again"""
def ip13mini(size):
    """ip13mini"""
    if size == "128 GB":
        return "25900"
    elif size == "256 GB":
        return "29900"
    elif size == "512 GB":
        return "37900"
    else:
        return "Not Available"

def ip13(size):
    """ip13"""
    if size == "128 GB":
        return "29000"
    elif size == "256 GB":
        return "33900"
    elif size == "512 GB":
        return "41900"
    else:
        return "Not Available"

def ip13pro(size):
    """ip13pro"""
    if size == "128 GB":
        return "38900"
    elif size == "256 GB":
        return "42900"
    elif size == "512 GB":
        return "50900"
    elif size == "1 TB":
        return "58900"
    else:
        return "Not Available"

def ip13promax(size):
    """ip13promax"""
    if size == "128 GB":
        return "42900"
    elif size == "256 GB":
        return "46900"
    elif size == "512 GB":
        return "54900"
    elif size == "1 TB":
        return "62900"
    else:
        return "Not Available"

def price(name, size):
    """prices"""
    if "mini" in name:
        return ip13mini(size)
    elif "Pro Max" in name:
        return ip13promax(size)
    elif "Pro" in name:
        return ip13pro(size)
    elif "iPhone 13" in name:
        return ip13(size)
    else:
        return "Not Available"



print(price(input(), input()))
