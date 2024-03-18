def armstrong (number):
    num = number
    digit=0
    cube =0
    sum = 0
    while(num>0):
        digit = num%10
        cub = digit * digit * digit
        sum = sum+cub
        num //=10
    
    if (number == sum):
        return "Armstrong"
    else:
        return "Not Armstrong"
    

number = 0
print("Enter to check the Armstrong number ") 
number = int(input())
print(armstrong(number))

