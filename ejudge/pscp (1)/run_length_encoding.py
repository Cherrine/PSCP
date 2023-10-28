"""Run Length Encoding"""


def encoder(text):
    """Encode the text"""
    encoded = ""
    previous = text[0]
    count = 0
    for char in text:
        if previous != char:
            encoded += "{}{}".format(count, previous)
            count = 1
        else:
            count += 1
        previous = char
    encoded += "{}{}".format(count, previous)
    return encoded


print(encoder(str(input())))
