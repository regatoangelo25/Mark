class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hi, my name is {self.name}, I am {self.age} years old, and I am studying {self.course}.")


student1 = Student("Baldo", 20, "Computer Science")
student2 = Student("Totoy", 22, "Criminology")
student3 = Student("Bototoy", 19, "IT")

# Calling the introduce method for each student
student1.introduce()
student2.introduce()
student3.introduce()