num = 123

number = abs(num)

product = 1



while number > 0:
    extracted_last_digit = number % 10
    product = product*extracted_last_digit
    number= number//10

print(product)