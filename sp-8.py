# Python Program to Accept Three Digits and Print all Possible Combinations from the Digits

dig1=int(input("Enter digit 1 :"))
dig2=int(input("Enter digit 2 :"))
dig3=int(input("Enter digit 3 :"))

com=[]

com.append(dig1)
com.append(dig2)
com.append(dig3)

for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i!=j & j!=k & k!=i):
                print(com[i],com[j],com[k])