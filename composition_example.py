

class ManagerRole:
    def perform_duties(self, hours):
        return f'screams and yells for {hours} hours.'


class SecretaryRole:
    def perform_duties(self, hours):
        return f'does paperwork for {hours} hours.'


class Employee:
    def __init__(self, id, name, role):
        self.id = id
        self.name = name
        self.role = role

    def work(self, hours):
        self.role.perform_duties(hours)
