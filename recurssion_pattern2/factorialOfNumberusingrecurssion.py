# find the factorial of a n number using recurssion approach

# rules
# 1.create a a flow 
# create a exit point


# fact(5)=5*4*3*2*1
# fact(5)= 5*f(4)
# fact(n)=n*(n-1)
# fact(0)1
#fact(1)=1


# exist point = n==0 or n===1
# return 1



def findthefactorial(n):
  
    if n==0 or n==1:
        return 1;

    else: 
        return n*(n-1)

result = findthefactorial(5)
print(result)