a=3
i=2
flag=0
while(i<=a/2):
    if(a%i==0):
        flag=1

    i=i+1
if(flag==0):
    print("its a prime number")
else:
    print("its not a prime number")
