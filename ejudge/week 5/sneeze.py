"""sneeze"""
def main():
    """function"""
    text = input()
    btext = ""
    for txt in text:
        if txt.isupper():
            btext += txt.lower()
        elif txt.islower():
            btext += txt.upper()
        else:
            btext += txt
    print(btext)
main()
