import math

l = float(input().replace(',','.'))
k = float(input().replace(',','.'))
n = int(input())
r = {}
u = []


for i in range(n):
    d = input().split(";")
    u += [d]
    a = float(d[-2].replace(',','.'))
    b = float(d[-1].replace(',','.'))
    x = (a-l)*math.cos((b+k)/2)
    y = (b-k)
    dist = (math.sqrt(x**2+y**2)*6371)
    r[dist] = i


print(u[r[min(r)]][1])
