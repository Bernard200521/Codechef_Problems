class Patient:
    def __init__(self, name, temps):
        self.name = name
        self.temps = temps

    def highest_temp(self):
        return max(self.temps)

    def lowest_temp(self):
        return min(self.temps)

    def abnormal_count(self):
        count = 0
        for t in self.temps:
            if t > 100:
                count += 1
        return count

name = input("Patient Name: ")
temps = list(map(float, input("Temperatures: ").split()))
p = Patient(name, temps)
print("Highest Temperature:", p.highest_temp())
print("Lowest Temperature:", p.lowest_temp())
print("Abnormal Readings:", p.abnormal_count())