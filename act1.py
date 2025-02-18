class ProgramDoe:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}! Welcome to the Program.")

# Create an object of the class
user = ProgramDoe("John")

# Call the greet method
user.greet()