t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    r = list(map(int, input().split()))

    ans = 0

    for i in range(1, n):
        if l[i] * r[i] > l[ans] * r[ans]:
            ans = i
        elif l[i] * r[i] == l[ans] * r[ans]:
            if r[i] > r[ans]:
                ans = i
    print(ans + 1)