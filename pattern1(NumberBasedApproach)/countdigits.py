num=-1234
number = abs(num)

count = 0


if number ==0 :
 count=1

else:

 while number > 0:
  extracted_digits=number%10
#  this will be increament how much time the loops executed until the number is greater than 0 
  count+=1
#   print(extracted_digits ,end="")
  number= number//10
  

print(count)