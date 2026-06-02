class University:
    def __init__(self, attendance):
        self.attendance = attendance

    def highest_attendance(self):
        return max(self.attendance)

    def lowest_attendance(self):
        return min(self.attendance)

    def eligible_students(self):
        count = 0

        for a in self.attendance:
            if a >= 75:
                count += 1

        return count

attendance = list(map(int, input("Attendance: ").split()))

s = University(attendance)

print("Highest Attendance:", s.highest_attendance())
print("Lowest Attendance:", s.lowest_attendance())
print("Eligible Students:", s.eligible_students())