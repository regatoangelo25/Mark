# Task 2: Student class with name, age, and course attributes

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hi, I am {self.name}. I am {self.age} years old and I am studying {self.course}.")

# Create three student objects
student1 = Student("Alice", 20, "Computer Science")
student2 = Student("Bob", 22, "Mathematics")
student3 = Student("Charlie", 21, "Physics")

# Call their introduce method
student1.introduce()
student2.introduce()
student3.introduce()