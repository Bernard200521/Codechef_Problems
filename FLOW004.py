t = int(input())
for _ in range(t):
    n = int(input())
    
    last_digit = n % 10
    
    first_digit = n
    while first_digit >= 10:
        first_digit //= 10
    
    print(first_digit + last_digit)