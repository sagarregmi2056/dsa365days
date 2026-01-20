nums=[1,2,3,4,5,6,7]
# 7654321
# ans =[5,6,7,1,2,3,4]
first_index=0
last_index=len(nums)-1
while first_index<last_index:
 nums[first_index],nums[last_index]=nums[last_index],nums[first_index]
 first_index+=1
 last_index-=1
print(nums)










    




