
number=int(input("Enter Decimal No.: "))
ans=""
while(number):
    rem=number%2
    ans+=str(rem)
    number//=2
ans=ans[::-1]
print("Binary Representation is",ans)

