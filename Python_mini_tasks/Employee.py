class Employee:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def best_score(self):
        return max(self.scores)

    def average_score(self):
        return sum(self.scores) / len(self.scores)

    def count_above_80(self):
        count = 0
        for s in self.scores:
            if s > 80:
                count += 1
        return count


name = input("Employee Name: ")
scores = list(map(int, input("Scores: ").split()))

e = Employee(name, scores)

print("Best Score:", e.best_score())
print("Average Score:", round(e.average_score(), 1))
print("Months Above 80:", e.count_above_80())