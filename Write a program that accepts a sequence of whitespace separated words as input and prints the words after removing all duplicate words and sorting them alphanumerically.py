data=input("Enter space seperated words: ")
li=[ i for i in data.split()]
li=list(set(li))
li.sort()
for i in li:
    print(i,end=" ")
