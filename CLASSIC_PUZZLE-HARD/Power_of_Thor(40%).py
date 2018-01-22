a, b = [int(i) for i in input().split()]
r=[]
l=[]

while True:
    c="WAIT"
    h, n = [int(i) for i in input().split()]
    for i in range(n):
        x, y = [int(j) for j in input().split()]
        if i==0:r+=[x];l+=[y]
        if a-1==x and b-1==y:c="STRIKE"
        elif a-1==x and b+1==y:c="STRIKE"
        elif a+1==x and b-1==y:c="STRIKE"
        elif a+1==x and b+1==y:c="STRIKE"
        elif a+1==x and b==y:c="STRIKE"
        elif a==x and b+1==y:c="STRIKE"
        elif a-1==x and b==y:c="STRIKE"
        elif a==x and b-1==y:c="STRIKE"
        print(a,b,x,y, file=sys.stderr)
    print(c)   
