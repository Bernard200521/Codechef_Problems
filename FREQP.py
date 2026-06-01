from collections import Counter

T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    mx = max(Counter(A).values())

    print(N - mx + 1)