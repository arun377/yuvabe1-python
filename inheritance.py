class Developer(Employee):
    def __init__(self, name):
        super().__init__(name, "Developer")

    def code(self):
        return f"{self.name} is coding the next feature."



class Designer(Employee):
    def __init__(self, name):
        super().__init__(name, "Designer")

    def create_design(self):
        return f"{self.name} is working on a new design."




arun = Developer("Arun")
print(arun.introduce())
print(arun.code())

yuvabe = Employee("Yuvabe", "Founder")
print(yuvabe.introduce())

yuvaraj = Designer("Yuvaraj")
print(yuvaraj.introduce())
print(yuvaraj.create_design())