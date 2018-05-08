def moveTower(height,fromPole, toPole, viaPole):
    if height >= 1:
        moveTower(height-1,fromPole,viaPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,viaPole,toPole,fromPole)

def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)


moveTower(5,"A","B","C")
