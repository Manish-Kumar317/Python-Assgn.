myList = ['ram','sita','laxman','hanuman','ravana']
if('shiva' in myList == 1):
    print("The name is present in the list\n")
else:
    print('The name is  not present in the list\n')
flag=0
for i in range(len(myList)):
    if('ram'==myList[i]):
        print("The name is present in the list\n")
        flag=1
        break
if(flag==0):
     print('The name is  not present in the list\n')
myList.reverse()
print(myList)
