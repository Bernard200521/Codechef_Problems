nested = [[1, 2, 3], [4, 5], [6]]
total = 0
for sublist in nested:
    for num in sublist:
        total += num
print("Sum =", total)
