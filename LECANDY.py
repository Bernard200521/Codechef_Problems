t = int(input())

for _ in range(t):
    n, c = map(int, input().split())
    a = list(map(int, input().split()))

    if sum(a) <= c:
        print("Yes")
    else:
        print("No")