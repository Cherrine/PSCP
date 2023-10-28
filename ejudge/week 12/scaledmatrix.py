"""ScaledMatrix"""
def main():
    """ScaledMatrix"""
    rows = int(input())
    columns = int(input())
    num = []
    grid = []
    for _ in range(rows*columns):
        num.append(float(input()))
    for numbers in num:
        sol = (numbers - min(num)) / (max(num) - min(num))
        grid.append("%.2f" %sol)

    for _ in range(columns):
        mylist = [grid[i:int(i)+columns] for i in range(0, rows*columns, columns)]

    for rows in mylist:
        print(' '.join(str(mylist) for mylist in rows))
main()
