t = int(input())

for i in range(t):
    h, c, ts = map(float, input().split())

    x = h > 50
    y = c < 0.7
    z = ts > 5600

    if x and y and z:
        print(10)
    elif x and y:
        print(9)
    elif y and z:
        print(8)
    elif x and z:
        print(7)
    elif x or y or z:
        print(6)
    else:
        print(5)