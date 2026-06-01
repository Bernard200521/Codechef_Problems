t = int(input())

for _ in range(t):
    x, y, k, n = map(int, input().split())
    
    need = x - y
    flag = False
    
    for _ in range(n):
        p, c = map(int, input().split())
        
        if p >= need and c <= k:
            flag = True
     
    if flag:
        print("LuckyChef")
    else:
        print("UnluckyChef")