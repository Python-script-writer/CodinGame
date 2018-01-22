input()
print(min(sorted(input().split() or '0')[::-1], key = lambda x: int(x)**2))
