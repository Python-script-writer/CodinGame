width = int(input())
height = int(input())
s=[]
for i in range(height):
    line = input()
    for j in range(len(line)):
        if line[j]=='0':
            s.append(str(j)+' '+str(i))

s.reverse()

for k in range(len(s)-1):
    m=s.pop()
    if str(s[len(s)-1][2])==m[2]:p=m+' '+s[len(s)-1]+' ' 
    else:p=m+' '+'-1 -1'+' ' 
    for l in range(len(s)):
        if s[len(s)-l-1][0]==m[0]:p=p+s[len(s)-l-1];break
        if l==len(s)-1:p=p+'-1 -1'
    print(p)
    
print(s[0]+' -1 -1 -1 -1')
