num= 112234343433333330

number=abs(num)



frequency=[0]*10
# print(frequency)

while number>0:
    
    extracted_digits=number%10
    frequency[extracted_digits]= frequency[extracted_digits]+1
    number = number//10
print(frequency)
print(frequency[1])
print(frequency[2])
print(frequency[3])

