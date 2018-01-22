s = ''
n = int(input())
for i in range(n):s+=input()

q = i = n = u = 0
t = ''

for c in s:
    if c== '\'':q = q^1
    if q==1 or (c!=' ' and c!='\t' and c!='\n'):t+=c

s = t

for k in range(len(s)):
    c = s[k]

    if n==1:print('\n'+' '*i, end="");u=i;n=0

    if c!='\'' and q==1:print(c, end="");u+=1

    elif c=='(':
        if u!=i:print('\n'+' '*i, end="");u=i
        print("(", end="")
        u+=1
        i+=4
        if k!=len(s)-1 and s[k+1]!=')':n = 1

    elif c==';':print(c, end="");u+=1;n=1

    elif c==')':
        print('\n', end="")
        i-=4
        print(' '*i+c, end="")
        u=i
        u+=1
        if k!=len(s)-1 and (s[k+1]!=';' and s[k+1]!=')'):n = 1

    elif c=='\'':q^=1;print(c, end="");u+=1
    
    else:print(c, end="");u+=1
