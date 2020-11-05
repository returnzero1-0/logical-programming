# Python Program to Check if a Number is a Palindrome

# 343

num=int(input("Enter the Number :"))
tmp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10

if(tmp==rev):
    print(tmp," is Palindrome")
else:
    print(tmp," is not palindrome")