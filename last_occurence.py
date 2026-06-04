arr = [10, 20, 30, 20, 40]
x = 20
for i in range(len(arr) - 1, -1, -1):
    if arr[i] == x:
        print("Last occurrence index:", i)
        break
