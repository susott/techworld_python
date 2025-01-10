import unittest

# from student import Student
from professor import Professor


class TestProfessor(unittest.TestCase):
    # prof1 = Professor('Daisy', 'Duck', 88, ['maths', 'literature'])

    def has_age(self):
        prof1 = Professor('Daisy', 'Duck', 88, ['maths', 'literature'])
        self.assertEqual(prof1.age, 88)
