class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year Published: {self.year_published}")
        print("-" * 3)

# Creating three book objects
book1 = Book("Stone", "Mc Cannon", 2000)
book2 = Book("Smoke", "George ", 2001)
book3 = Book("Plastic", "Morgan", 2002)

# Displaying book details
book1.describe()
book2.describe()
book3.describe()