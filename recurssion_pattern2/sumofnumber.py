def calculatesum(x,i,n):
    # 0+1+2+3+4

    if i>n:
        print(x)
    else:
     calculatesum(x+i,i+1,n)


calculatesum(0,1,4)