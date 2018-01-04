a=raw_input("Enter input 1")
b=raw_input("Enter input 2")
c=raw_input("Enter input 3")
d=raw_input("Enter input 4")
e=raw_input("Enter input 5")

if(a>b and a>c)and(a>d)and(a>e):
    print("A is bigger")

elif(b>a and b>c and b>d and b>e):
    print("B is bigger")
elif(c>a and c>b and c>d and c>e):
    print("C is bigger")
elif(d>a and d>c and d>b and d>e):
    print("D is bigger")
else:
    print("E is bigger")
   
