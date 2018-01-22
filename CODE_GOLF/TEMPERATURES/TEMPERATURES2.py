input()
print(sorted(map(int, input().split() or '0'), key = lambda x: (x**2, -x))[0])
