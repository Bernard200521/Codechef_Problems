t = int(input())
for _ in range(t):
    n, b = map(int, input().split())
    max_area = 0
    for _ in range(n):
        w, h, p = map(int, input().split())
        if p <= b:
            max_area = max(max_area, w * h)
    if max_area == 0:
        print("no tablet")
    else:
        print(max_area)