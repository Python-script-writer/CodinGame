input()
print(min(map(int, input().split() or '0'), key=lambda x: x*x-x))
