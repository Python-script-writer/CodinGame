k, v = int,input
l = v().split()
s = dict(v().split() for i in range(k(l[7])))

while True:
    f, p, d = v().split()
    t = k((s.get(f,0), l[4])[f==l[3]])
    print(['WAIT','BLOCK'][t>k(p) and d=='LEFT' or t<k(p) and d[0]=='R'])
    
