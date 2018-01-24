n = int(input())
c = []
Y = 0
X = []
 
 
for i in range(n):
    x, y = [int(j) for j in input().split()]
    c+=[[x,y]]
    X+=[x]
    Y+=y
    
    
X.sort()
Y=round(Y/n)
c.sort()
p=0


for i in c:
    p+=abs(i[1]-Y)


print(X[-1]-X[0]+p)
