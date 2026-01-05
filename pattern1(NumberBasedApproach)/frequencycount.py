num= 112234343433333330

number=abs(num)



frequency=[0]*10
print(frequency)
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 0 1 2 3 4 5 6 7 8 9 10 

while number>0:
    
    extracted_digits=number%10
    # initally let say 0
    frequency[extracted_digits]= frequency[extracted_digits]+1
    # 0th index will have = 0+1=1 
    # again fre[3]=initally 0+1=1
    # again freq[3]=fre[3]+1  = 1+1 and keep repeating 
    number = number//10
print(frequency)
# here the new frequency list will have the index=digits and numbervalue=count of that number 
print(frequency[1])
print(frequency[2])
print(frequency[3])

