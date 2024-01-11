
def greet(name):
    return f"Hello, {name}!"


#Person

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"


#Employee

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Employee ID: {self.employee_id}"


#Main


person = Person("arunk", 25)
print(person.display_info())

employee = Employee("Arun", 30, "E1123465")
print(employee.display_info())

greeting = greet("arjun")
print(greeting)