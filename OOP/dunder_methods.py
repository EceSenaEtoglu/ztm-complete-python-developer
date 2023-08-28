class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

    def __eq__(self, other):
        #don't compare unrelated objects
        if isinstance(other,Employee):
            return self._first_name == other._first_name and self._last_name == other._last_name
        return False

    def __gt__(self, other):
        if isinstance(other,Employee):
            return self.pay > other.pay
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Employee):
            return self.pay < other.pay
        return NotImplemented

    def __hash__(self):
        return hash((self._first_name,self._last_name))


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

# print(emp_1 + emp_2)

print(len(emp_1))