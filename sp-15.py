# Python Program to Read a Number n And Print the Series “1+2+…..+n= “

num=int(input("Enter number :"))

series=[]

for i in range(1,num+1):
    print(i,end=" ")
    if(i<num):
        print("+",end=" ")
    series.append(i)

print("=",sum(series))

