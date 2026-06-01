# cook your dish here
t = int(input())
for _ in range(t):
    s = input().strip()
    n = len(s)
    if n % 2 == 0:
        left = s[:n // 2]
        right = s[n // 2:]
    else:
        left = s[:n // 2]
        right = s[n // 2 + 1:]
    if sorted(left) == sorted(right):
        print("YES")
    else:
        print("NO")