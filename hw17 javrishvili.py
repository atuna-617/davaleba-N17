    #davaleba1
class Car:
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        print("Creating a new instance of Car")
        return instance

    def __init__(self, brand, model, year):
        print("Initializing attributes of Car")
        self.brand = brand
        self.model = model
        self.year = year

#mamachemis manqana
my_car = Car(brand="Toyota", model="Camry", year=2019)

print(f"Brand: {my_car.brand}")
print(f"Model: {my_car.model}")
print(f"Year: {my_car.year}")











    #davaleba2
from functools import wraps
import time

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        execution_time = end_time - start_time
        method_name = func.__name__
        arguments = ", ".join([str(arg) for arg in args])
        keyword_arguments = ", ".join([f"{key}={value}" for key, value in kwargs.items()])
        all_arguments = ", ".join(filter(None, [arguments, keyword_arguments]))

        print(f"{method_name} executed in {execution_time:.4f} seconds with arguments: {all_arguments}")
        return result

    return wrapper

class Calculator:
    @timing_decorator
    def add(self, a, b):
        return a + b

    @timing_decorator
    def subtract(self, a, b):
        return a - b

    @timing_decorator
    def multiply(self, a, b):
        return a * b

    @timing_decorator
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

calculator_instance = Calculator()

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operation = input("Enter the operation that you want: ")

if operation == '+':
    calculator_instance.add(a, b)
elif operation == '-':
    calculator_instance.subtract(a, b)
elif operation == '*':
    calculator_instance.multiply(a, b)
elif operation == '/':
    calculator_instance.divide(a, b)
else:
    print("Invalid operation")









    #davaleba3
class Car:
    def __init__(self, brand, model, year):
        self._brand = None
        self._model = None
        self._year = None
        self.set_brand(brand)
        self.set_model(model)
        self.set_year(year)

    def get_brand(self):
        return self._brand

    def set_brand(self, brand):
        if not isinstance(brand, str):
            raise ValueError("Brand must be a string")
        self._brand = brand

    def get_model(self):
        return self._model

    def set_model(self, model):
        if not isinstance(model, str):
            raise ValueError("Model must be a string")
        self._model = model

    def get_year(self):
        return self._year

    def set_year(self, year):
        if not isinstance(year, int) or year < 0:
            raise ValueError("Year must be a non-negative integer")
        self._year = year

    def update_attributes(self):
        brand = input("Enter the new brand: ")
        model = input("Enter the new model: ")
        year = int(input("Enter the new year: "))
        self.set_brand(brand)
        self.set_model(model)
        self.set_year(year)

my_car = Car(brand="Toyota", model="Camry", year=2019)

print(f"Brand: {my_car.get_brand()}")
print(f"Model: {my_car.get_model()}")
print(f"Year: {my_car.get_year()}")

my_car.update_attributes()


print(f"Updated Brand: {my_car.get_brand()}")
print(f"Updated Model: {my_car.get_model()}")
print(f"Updated Year: {my_car.get_year()}")
