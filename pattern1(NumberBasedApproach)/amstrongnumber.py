num =153 

number = abs(num)
power  = len(str(num))
# print(power)
sum = 0

while number> 0:

    extracted_digits=number%10
    sum = sum+(extracted_digits**power)
    number= number//10
print(sum)
if sum==num :
    print("the given number is amstrong number ")
else :
    print("the given number is not amstrong number")


