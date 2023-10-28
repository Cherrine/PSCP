"""median"""
def main():
    """cal"""
    count = int(input())
    number = []
    for _ in range(count):
        numb = int(input())
        number.append(numb)
    number.sort()
    if len(number) % 2 == 0:
        median1 = number[len(number)//2]
        median2 = number[len(number)//2 - 1]
        median = (median1 + median2) / 2
    else:
        median = number[len(number) // 2]
    print("%.1f" %median)
main()
