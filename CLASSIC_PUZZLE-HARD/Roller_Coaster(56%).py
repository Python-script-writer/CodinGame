l,d,n=[int(i) for i in input().split()]

r=[]
c=[int(input()) for i in range(n)]
c.reverse()


for j in range(d):
    for i in range(n):
        if c[n-1-i]+c[n-2-i]<=l:t=c.pop();r+=[t];c.insert(0,t)
        else:t=c.pop();r+=[t];c.insert(0,t);break


print(sum(i for i in r))
