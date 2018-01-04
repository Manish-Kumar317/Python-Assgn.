myList=[]
nn= int(raw_input('enter the range for the list\n'))
for i in range(nn):
    temp=int(raw_input("enter the item\n"))
    myList.append(temp)
big=0
small=myList[0]
for i in range(len(myList)):
    if(big<myList[i]):
        big=myList[i]
    if(small>myList[i]):
        small = myList[i]
print(big,small)
