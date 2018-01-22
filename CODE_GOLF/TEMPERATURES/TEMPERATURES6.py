r=m=5527;input()
for i in input().split():t = int(i);r=[r,[t,abs(t)][abs(r)==abs(t) and r!=t]][abs(r)>=abs(t)]
print([r,0][m==r])
