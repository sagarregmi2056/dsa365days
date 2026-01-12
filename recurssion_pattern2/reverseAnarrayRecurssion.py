


# # [2,3,4,45,23,23,1,3,3]

# # len(num)-1


# def reverseanarray( num):
#     # 3 2 4 5 63 2334 90 0

#     if num==[]:
#         return 
#     else: 
#      return reverseanarray(num[len(num[]-1)])





  



# result = reverseanarray([3,2,4,5,62,2334,90,0])
# print(result)
# # individual number ma extract and append gardai jani


# listnum= [1,2,3,4]


# length=len(listnum)

# lastelement=listnum[length-1]
# print(lastelement)




def reverseaarray(num):
    # here num=[1,2,3,4,5,6,7]
    # first extract the last number add it to the new list and remove it from the original
     if num==[]:
      return []
     else:
        last_number=num[len(num)-1]
        remaining_number=num[:-1]

        return [last_number] +reverseaarray(remaining_number)
     
     
    
     
    
     


result = reverseaarray([1,2,3,4,5,6,7])
print(result)
# 


# First call: num = [1,2,3,4,5,6,7]

# last_number = 7

# remaining_number = [1,2,3,4,5,6]

# return [7] + reverseaarray([1,2,3,4,5,6])

# Second call: num = [1,2,3,4,5,6]

# last_number = 6

# remaining_number = [1,2,3,4,5]

# return [6] + reverseaarray([1,2,3,4,5])

# Third call: num = [1,2,3,4,5]

# last_number = 5

# remaining_number = [1,2,3,4]

# return [5] + reverseaarray([1,2,3,4])

# This continues until the last recursive call:

# num = [1]

# last_number = 1

# remaining_number = []

# return [1] + reverseaarray([])

# Base case: num = []

# return []
# Step 1 resolves (FINAL):
#    [7] + [6, 5, 4, 3, 2, 1] = [7, 6, 5, 4, 3, 2, 1]  



# [7] + [6] + [5] + [4] + [3] + [2] + [1] + []
#      ↓
# [7] + [6] + [5] + [4] + [3] + [2] + [1]
#      ↓
# [7] + [6] + [5] + [4] + [3] + [2, 1]
#      ↓
# [7] + [6] + [5] + [4] + [3, 2, 1]
#      ↓
# [7] + [6] + [5] + [4, 3, 2, 1]
#      ↓
# [7] + [6] + [5, 4, 3, 2, 1]
#      ↓
# [7] + [6, 5, 4, 3, 2, 1]
#      ↓
# [7, 6, 5, 4, 3, 2, 1]  