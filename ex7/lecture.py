class Lecture:
    def __init__(self, name, max_num_students, duration, professors):
        self.name = name
        self.max_num_students = max_num_students
        self.duration = duration  # weeks
        self.professors = professors

    def print_lecture(self):
        print(f"Name: {self.name}, Duration: {self.duration} weeks")

    def add_professor(self, new_professor):
        self.professors.append(new_professor)

# lecture1 = Lecture('Introduction to Chemistry', 500, 6, ['Mr. Bean'])

# lecture1.add_professor('Mama Mia')
# lecture1.print_lecture()
# print(lecture1.professors)
