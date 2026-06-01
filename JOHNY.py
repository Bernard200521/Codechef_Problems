t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    johny = arr[k - 1]
    arr.sort()
    print(arr.index(johny) + 1)