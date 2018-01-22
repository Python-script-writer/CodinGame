a,b,x,y=map(int,input().split())

while True:
    print("S"*(y<b)+"N"*(x==a)+"E"*(x<a)+"W"*(x>a))
    y+=b>y-b<y
