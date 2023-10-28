"""Future Message"""
def futuremessage(text):
    """condition"""
    if text.isupper():
        print("Uppercase")
    elif text.isdigit():
        print("Number")
    elif text.islower():
        print("Lowercase")
    elif text.istitle():
        print("Title")
    elif text.isspace():
        print("Space")
    else:
        print("Other")
futuremessage(input())
