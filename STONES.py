t = int(input())
for _ in range(t):
    J = input().strip()
    S = input().strip()
    jewels = set(J)
    count = 0
    for ch in S:
        if ch in jewels:
            count += 1
    print(count)