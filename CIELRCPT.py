t = int(input())

menus = [2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]

for i in range(t):
    p = int(input())

    count = 0
    for item in menus:
        count += p // item
        p = p % item

    print(count)