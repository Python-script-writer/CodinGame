input()
print(min(input().split() or "0", key = lambda x:(int(x) - .1)**2))
