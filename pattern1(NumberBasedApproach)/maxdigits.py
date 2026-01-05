num=2383437593


number=abs(num)
maxlist=[]

while number > 0 :
    extracted_digits=number%10
    maxlist.append(extracted_digits)
    number = number//10
maxnum= max(maxlist)
print(maxnum)
