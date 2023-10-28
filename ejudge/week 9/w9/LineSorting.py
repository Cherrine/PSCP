"""LineSorting"""
def main():
    """eiei"""
    count = int(input())
    sens = []
    for text in range(count):
        text = str(input())
        sens.append(text)
    sens2 = sorted(sens, key=len)
    for word in sens2:
        print(word)
main()
