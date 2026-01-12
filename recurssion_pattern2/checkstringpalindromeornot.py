
    # 0,1,2,3
    # s,a,a,s



def checkstringpalindrome(name):

    if name=="":
      return ""
    else:

     last_string=name[len(name)-1]
     remaining_string= name[:-1]

     return last_string + checkstringpalindrome(remaining_string)



name="saasa"
result=checkstringpalindrome(name)
finalresult=str(result)


if finalresult==name:
    print("the given number is palindrome")
else:
 print("the given number is not palindrome")

