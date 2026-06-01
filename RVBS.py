T = int(input())

for _ in range(T):
    N = int(input())
    A = input().strip()
    B = input().strip()

    posA = []
    posB = []
    for i in range(N):
        if A[i] == '1':
            posA.append(i)

        if B[i] == '1':
            posB.append(i)

  
    if len(posA) != len(posB):
        print(-1)
    else:
        operations = 0
        for i in range(len(posA)):
            if posA[i] != posB[i]:
                operations += 1

        print(operations)