"""almostmean"""
def almostmean():
    """function"""
    scid = []
    scorestudent = []
    scoresum = 0
    numstudent = int(input())
    for _ in range(numstudent):
        tmp = input().split()
        scid.append(tmp[0])
        scorestudent.append(float(tmp[1]))
        tmp = []
    for i in scorestudent:
        scoresum += float(i)
    mean = scoresum/numstudent
    scoresort = sorted(scorestudent)
    indexscore = 0
    while True:
        if float(scoresort[indexscore]) >= mean:
            indexscore -= 1
            break
        indexscore += 1
    for i in range(len(scorestudent)):
        if float(scorestudent[i]) == float(scoresort[indexscore]):
            print("%s\t%s"%(scid[i], str(scorestudent[i])))
almostmean()
