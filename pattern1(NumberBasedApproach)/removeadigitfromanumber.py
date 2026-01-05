num = 11234

# remove 1 from this number 

number = abs(num)
newnumber =[]

while number>0:
    extracted_digits= number%10
    if extracted_digits==1:
      print("the 1 from the number is extracted ")
    else :
       newnumber.append(str(extracted_digits))
       newnumber.reverse()
    
    number = number//10
finalresult="".join(newnumber)

print(int(finalresult))

      

