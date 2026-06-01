# cook your dish here
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    
    count = 0
    
    for i in a:
        if i in b:
            count += 1
    
    print(count)