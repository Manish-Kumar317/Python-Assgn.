eid = [1001,1002,1003,1004,1005,1006,1007,1008,1009,1010]
ename = ['Sam','Ram','Tin','Vin','Fox','Vix','Eve','Mou','Xiao','Stu']
print (ename)
index = int(raw_input("Enter the index to find the employee\n"))
print(eid[index-1],ename[index-1])
print(ename[3:9])
print(ename[2:])
rep = int(raw_input("Enter the repatition\n"))
print(ename*rep)
print(eid+ename)
for i in range(10):
    print(eid[i],ename[i])
