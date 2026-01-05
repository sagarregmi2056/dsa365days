# question 1: Number extraction approach 
# export the number from back side one by one

# optimized approach:
# ---->>> modulas approach always remember num %10 will give you last digit and num//10 will give you remaining number 
# 
num = 123
while num > 0:
    last_digit = num % 10    # this will give you last digit 3 ,2,1
    print(last_digit  , end="")
    num = num // 10

    # calculating time complexity of this approach : O(d) where d is the number of digits in the number
    # space complexity: O(1) because we are not using any extra space

    # calculating space complexity of this approach: O(1)
    # space complexity: O(1)

    # calculating space complexity of this approach: O(1)
    # space complexity: O(1)

    # calculating space complexity of this approach: O(1)
    # space complexity: O(1)





# this is bad approach because we are converting number to string and then converting string to number again
# not optimized approach:
# ---->>> using string conversion

num = 123
num_str = str(num)

# loop will run from index 0 to len(num_str) - 1
for index in range(len(num_str)):
    print(num_str[index], end=" ")