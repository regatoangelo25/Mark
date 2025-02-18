class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):  
        print(f"Car Brand: {self.brand}")  
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")


car1 = Car("Lamborghini", "Huracan", 2022)  
car2 = Car("Toyota", "Corolla", 2022)  


car1.display_info()
print()
car2.display_info()