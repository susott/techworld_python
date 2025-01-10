# EXERCISE 7: Working with Classes and Objects

Imagine you are working in a university and need to write a program, which handles data of students, professors and lectures. To work with this data you create classes and objects:

a) Create a Student class

with properties:

    first name
    last name
    age
    lectures they attend

with methods:

    can print the full name
    can list the lectures, which the student attends
    can add new lectures to the lectures list (attend a new lecture)
    can remove lectures from the lectures list (leave a lecture)

b) Create a Professor class

with properties:

    first name
    last name
    age
    subjects they teach

with methods:

    can print the full name
    can list the subjects they teach
    can add new subjects to the list
    can remove subjects from the list

c) Create a Lecture class

with properties:

    name
    max number of students
    duration
    list of professors giving this lecture

with methods:

    printing the name and duration of the lecture
    adding professors to the list of professors giving this lecture

d) Bonus task

As both students and professors have a first name, last name and age, you think of a cleaner solution:

Inheritance allows us to define a class that inherits all the methods and properties from another class.

    Create a Person class, which is the parent class of Student and Professor classes
    This Person class has the following properties: "first_name", "last_name" and "age"
    and following method: "print_name", which can print the full name
    So you don't need the properties and the method in the other two classes. You can easily inherit these.
    Change Student and Professor classes to inherit "first_name", "last_name", "age" properties and "print_name" method from the Person class

