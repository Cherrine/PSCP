"""_"""
def main():
    """_"""
    name = str(input())
    age = float(input())
    if age >= 18 and age > 0:
        print(name + ", you shall not pass.")
    elif age > 0 and age < 18:
        print(name + ", you can pass.")
main()
