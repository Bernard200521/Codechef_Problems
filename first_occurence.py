arr = [10, 20, 30, 20, 40]
x = 20

for i in range(len(arr)):
    if arr[i] == x:
        print("First occurrence index:", i)
        break
