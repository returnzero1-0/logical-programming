#program to calculate avg of numbers in a give list

n=int(input("Enter number of elements :"))

lst1=[]

for i in range(0,n):
    elem=int(input("Enter element :"))
    lst1.append(elem)

avg=sum(lst1)/n

print("Avg of list elements :",avg)
