class Person:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__ is a special method that is called when you use print() or str() on an object
    def __str__(self):
        return f"{self.name} is {self.age} years old ... ."
    
# this is how we extend the class
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def __str__(self):
        return f"{self.name} is {self.age} years old and has a student ID of {self.student_id}."
person1 = Student("John", 36, 1)

print(person1) # John is 36 years old