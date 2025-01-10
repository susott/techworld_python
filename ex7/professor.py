from person import Person


class Professor(Person):
    def __init__(self, first_name, last_name, age, subjects):
        super().__init__(first_name, last_name, age)
        self.subjects = subjects

    def list_subjects(self):
        return self.subjects

    def add_subjects(self, new_subject):
        self.subjects.append(new_subject)

    def remove_subject(self, subject_to_remove):
        if subject_to_remove in self.subjects:
            self.subjects.remove(subject_to_remove)
        else:
            print(f"Subject '{subject_to_remove}' not found. Can not be removed.")

# prof1 = Professor('Daisy', 'Duck', 88, ['maths', 'literature'])

# print(prof1.list_subjects())
# prof1.print_name()

# print(prof1.first_name)
# print(prof1.subjects)
