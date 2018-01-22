n = int(input())
print('.'+' '*(2*(n-1))+'*')
for i in range(2,n+1):
    print(' '*(2*n-i)+'*'*(2*i-1))
for i in range(1,n+1):
    print(' '*(n-i)+'*'*(2*i-1)+' '*(2*n-2*i+1)+'*'*(2*i-1))
