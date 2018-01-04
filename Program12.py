i=0
li=[]
avg=0
sum=0
while(i<10):
    avg=input("enter the element :")
    li.append(avg)
    sum=sum+avg
    i=i+1
print li
aver=sum/10
maxcount=0
for i in li:
    if(i>aver):
        maxcount+=1
mincount=0
for i in li:
    if(i>aver):
        mincount+=1
print(maxcount)
print(mincount)
print(li.count(aver))
