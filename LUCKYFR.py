

t = int(input())

for i in range(t):
    num = input()
    count = 0

    for digit in num:
        if digit == '4':
            count += 1

    print(count)