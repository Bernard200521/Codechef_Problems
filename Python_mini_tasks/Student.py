class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def total(self):
        return sum(self.marks)

    def average(self):
        return sum(self.marks)/len(self.marks)
    
    def highest_mark(self):
        return max(self.marks)
    
    def status(self):
        for mark in self.marks:
            if mark < 35:
                return "Fail"
        return "Pass"
    
    def display(self):
        print("Total Marks : ",self.total())
        print("Average : ",self.average())
        print("Highest Mark : ",self.highest_mark())
        print("Status : ",self.status())
    
name = input("Name : ")
marks = list(map(int,input().split()))
s = Student(name,marks)
s.display()