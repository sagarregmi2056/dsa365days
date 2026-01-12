

# reverse an array

# arr=[1,2,3,4,5,6]
# let takes a two different pointer on start pointer that will start from 0 index and another endpointer that will start from last index

# 0 1 2 3 4 5
# start=0 
# end=5

# start=1
# end=4

# start=2
# end=3
# # here the start >=end (base case )
# start=3
# end=2


def reverseanarraytwopointer(arr,start,end):
    # start=0
    # end=len(arr)
    if start>=end:
        return arr
    else:
        arr[start], arr[end] = arr[end], arr[start]
        return reverseanarraytwopointer(arr,start + 1,end - 1)



arr=[1,2,3,4,5,6]
result=reverseanarraytwopointer(arr,0,len(arr)-1)
print(result)