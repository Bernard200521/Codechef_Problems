# cook your dish here
t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    if 'I' in s:
        print("INDIAN")
    elif 'Y' in s:
        print("NOT INDIAN")
    else:
        print("NOT SURE")