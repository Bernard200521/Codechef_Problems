t=int(input())

for _ in range(t):
    n = int(input())
    sum = 0
    while  n > 0:
        digit = n%10
        sum = sum + digit
        n //= 10
    print(sum)