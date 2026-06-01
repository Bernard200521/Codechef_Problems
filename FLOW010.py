t = int(input())
for i in range (t):
    ab = input()
    if (ab == 'b' or ab=='B'):
        print("BattleShip")
    elif (ab == 'c' or ab=='C'):
        print("Cruiser")
    elif (ab == 'd' or ab=='D'):
        print("Destroyer")
    elif (ab=='f' or ab=='F'):
        print("Frigate")