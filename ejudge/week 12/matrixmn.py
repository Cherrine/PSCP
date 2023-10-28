"""Matrix_MN"""
 
def main():
    """function"""
    rows = int(input())
    columns = int(input())
    num = []
    for _ in range(rows*columns):
        num.append(int(input()))
 
    for _ in range(columns):
        mylist = [num[i:int(i)+columns] for i in range(0, rows*columns, columns)]
 
    for rows in mylist:
        print(' '.join(str(mylist) for mylist in rows))
main()