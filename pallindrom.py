def pallindrome(number):
    num = number
    digit = 0
    rev=0
    while(num>0):
        digit = num %10
        rev = rev*10 +digit
        num //=10
    
    if rev == number :
        return "Pallindrome"
    else:
        return " Not Pallindrome"
    
print("Enter a number to check for pallindrome")
number= int(input())
print(pallindrome(number))