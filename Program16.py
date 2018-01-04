a= int(raw_input("Enter the number\n"))
i=2
flag=0
while(i<=a/2):
    if(a%i==0):
        flag=1

    i=i+1
if(flag==0):
    print("its a prime number\n")
else:
    print("its not a prime number\n")
r =int(raw_input("Enter the range\n"))
init =2
print("The prime numbers are :\n")
while (init<=r):
    i=2
    flag=0
    while(i<=init/2):
        if(init%i==0):

            flag=1
        i=i+1
    if(flag==0):
        print(init)
    init+=1
