num= 9

number= abs(num)

sum=0


# handling edge case for the single digits number only 
if number < 10 :
    sum= number

else :
# same pattern as the all extract the number and sum it 
 while number > 0 :
    extracted_digit= number%10

    sum= sum+extracted_digit
    number= number//10
print(sum)
