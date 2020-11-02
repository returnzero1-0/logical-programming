#add 2 nos without using temp variable

num1=int(input("enter the num1 :"))
num2=int(input("enter the num2 :"))

print("before swap num1",num1)
print("before swap num2",num2)

num1=num1+num2
num2=num1-num2
num1=num1-num2

print("after swap num1",num1)
print("after swap num2",num2)
