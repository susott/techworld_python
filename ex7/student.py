from person import Person


class Student(Person):
    def __init__(self, first_name, last_name, age, lectures):
        super().__init__(first_name, last_name, age)
        self.lectures = lectures

    def add_lecture(self, new_lecture):
        self.lectures.append(new_lecture)

    def remove_lecture(self, lecture_to_remove):
        if lecture_to_remove in self.lectures:
            self.lectures.remove(lecture_to_remove)
        else:
            print(f"Lecture '{lecture_to_remove}' not found. Can not be removed.")


# student1 = Student('Jane', 'Doe', 111, ['arabic', 'chinese'])
# print(student1.first_name)


# student1.print_name()
# student1.add_lecture('french')
# student1.remove_lecture('french')

# print(student1.lectures)
