# cook your dish here
T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    
    minimum = min(A)
    
    if A.count(minimum) >= 2:
        print("YES")
    else:
        print("NO")