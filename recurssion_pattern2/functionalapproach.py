# print 1 to N sum N=10
# approach n=10
# 10+10-1=9 n+n-1=9
# 9+9-1=8 n+n-1=8



def functionalsum(n):
    
    if n==1:
        return 1
    else:
        
        return n+functionalsum(n-1)


print(functionalsum(10))