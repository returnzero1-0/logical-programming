#program to reverse a given number

#number is 546

num=int(input("Enter a number :"))

rev=0

while(num>0):
    rev_digit=num%10
    rev=rev*10+rev_digit
    num=num//10

print(rev)

