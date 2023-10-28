"""badkeyboard"""
def main(text):
    """function"""
    blank = ""
    for char in text:
        if char == "i":
            blank += "o"
        elif char == "I":
            blank += "O"
        elif char == "O":
            blank += "I"
        elif char == "o":
            blank += "i"
        else:
            blank += char
    print(blank)
main(input())
