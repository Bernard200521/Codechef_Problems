t = int(input())
for _ in range(t):
    n = int(input())
    w = list(map(int, input().split()))

    mn = min(w)
    moves = 0

    for salary in w:
        moves += salary - mn

    print(moves)