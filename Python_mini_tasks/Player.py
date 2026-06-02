class Player:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def highest_score(self):
        return max(self.scores)

    def lowest_score(self):
        return min(self.scores)

    def average_score(self):
        return sum(self.scores) / len(self.scores)

    def half_centuries(self):
        count = 0
        for s in self.scores:
            if s >= 50:
                count += 1
        return count


name = input("Player Name: ")
scores = list(map(int, input("Scores: ").split()))

p = Player(name, scores)

print("Highest Score:", p.highest_score())
print("Lowest Score:", p.lowest_score())
print("Average Score:", round(p.average_score(), 1))
print("Half Centuries:", p.half_centuries())