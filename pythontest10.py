class Student():
    def __init__(self, age, gender, major):
        self.age = age
        self.gender = gender
        self.major = major
stu_001 = Student(16, "f", "computer science")
print(stu_001.age)