t = int(input())

for i in range(t):
    quantity, price = map(int, input().split())

    total = quantity * price

    if quantity > 1000:
        total = total - (0.10 * total)

    print(f"{total:.6f}")