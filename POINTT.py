X, Y, A, B = map(int, input().split())
if X > A:
    print("Alice")
elif A > X:
    print("Bob")
else:
    if Y > B:
        print("Alice")
    elif B > Y:
        print("Bob")
    else:
        print("Alice")