t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    if arr != arr[::-1]:
        print("no")
        continue
    
    if set(arr) != {1,2,3,4,5,6,7}:
        print("no")
        continue
    
    flag = True
    
    for i in range(n - 1):
        if abs(arr[i] - arr[i + 1]) > 1:
            flag = False
            break
    
    if flag:
        print("yes")
    else:
        print("no")