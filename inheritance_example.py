
class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class SalaryEmployee(Employee):
    def __init__(self, id, name):
        super().__init__(id, name)


class Manager(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} screams and yells for {hours} hours.')


class Secretary(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} does paperwork for {hours} hours.')
