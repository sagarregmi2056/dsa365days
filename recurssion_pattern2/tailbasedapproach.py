# question print 1 to N using recurssion where n =10
# head based approach

# note: if there is a recurssion approach then always remember there is a stack and function will executed one by one 


def recurssioncall(i,n):
    # first step ma i=1 n=9
    # second 2,4
    # third 3,4
    # forth 4,4
   
    
   

    if i>n:
# check 1>4 no

        return 
    else:

     print(i)
        # 1+1,4 = 2,4
     recurssioncall(i+1,n)
    

recurssioncall(1,10)