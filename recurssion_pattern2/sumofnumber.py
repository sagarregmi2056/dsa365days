def calculatesum(x,i,n):
    # using head based approach
    # # 0+1+2+3+4

    # if i>n:
    #     print(x)
    # else:
    #  calculatesum(x+i,i+1,n)


     
    # using tailbased approach
      calculatesum(x+i,i,n)




calculatesum(0,1,4)