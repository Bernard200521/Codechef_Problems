# cook your dish here
import math

t = int(input())

for _ in range(t):
    B, LS = map(int, input().split())

    mn = math.sqrt(LS * LS - B * B)
    mx = math.sqrt(LS * LS + B * B)

    print(mn, mx)