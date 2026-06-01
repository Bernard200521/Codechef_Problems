# cook your dish here
n = int(input())

p1 = 0
p2 = 0

max_lead = 0
winner = 0

for _ in range(n):
    a, b = map(int, input().split())
    
    p1 += a
    p2 += b
    
    lead = abs(p1 - p2)
    
    if lead > max_lead:
        max_lead = lead
        
        if p1 > p2:
            winner = 1
        else:
            winner = 2

print(winner, max_lead)