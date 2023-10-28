"""heron of alexandria"""
def main():
    """function"""
    aaa = float(input())
    bbb = float(input())
    ccc = float(input())
    sss = ((aaa+bbb+ccc)/2)
    ans = (((sss)*((sss-aaa)*(sss-bbb)*(sss-ccc)))**0.5)
    print("%.3f" %ans)
main()
