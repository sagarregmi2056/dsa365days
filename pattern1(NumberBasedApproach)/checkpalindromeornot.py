# step 1: 

number= 1234
# we need to store each extraction in a list 

original_number = number

reversed_number = 0
while number > 0:
    last_digit = number % 10
    # here the digit extract the digit from the last one by one 4 3 2 1 
    # now we need to store each digit in a list so that we can check if the number is palindrome or not
    reversed_number = reversed_number * 10 + last_digit
    # above the reversed number will have 0*10 + 4 = 4 , 4*10 + 3 = 43 , 43*10 + 2 = 432 , 432*10 + 1 = 4321
    number = number // 10

if original_number == reversed_number:
    print("The number is palindrome")
else:
    print("The number is not palindrome")

