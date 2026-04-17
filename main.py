class Student:
    total_students = 0

    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        Student.total_students += 1

    def info(self):
        return f"Talaba: {self.name} ({self.grade}-sinf) | Jami talabalar: {Student.total_students}"

s1 = Student("ST001", "Ziyoda", 10)
s2 = Student("ST002", "Madina", 9)
print(s1.info())
