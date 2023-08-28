class Employee:
    COMPANY_NAME = "google"
    num_of_emps = 0
    raise_amount = 100

    def __init__(self,first,last,department,pay):
        self._first_name = first
        self._last_name = last
        self._fullname = self._first_name + self._last_name
        self.departmant= department
        self.pay = pay
        Employee.num_of_emps += 1

    def __eq__(self, other):
        if isinstance(other,Employee):
            return self._first_name == other._first_name and self._last_name == other._last_name
        return False

    def __hash__(self):
        hash((self._first_name,self._last_name))

    def __str__(self):
        return f"{self._fullname} works as {self.departmant} in {Employee.COMPANY_NAME}"

    def apply_raise(self):
        #use self.x in class variables to see change effect in class variable inheritance classes
        self.pay = self.pay + self.raise_amount

    @classmethod
    def set_raise_amount(cls,new_amount):
        cls.raise_amount = new_amount

    @staticmethod
    def is_work_day(day):
        return day.weekday() != 6 and day.weekday() !=5

    #declare email as property
    #so that email is updated with new department when nonprivate department is updated
    @property
    def email(self):
        return f"{self._fullname}@{self.departmant}.{Employee.COMPANY_NAME}.com"


class Manager(Employee):
    raise_amount = 200

    def __init__(self, first, last, department, pay, employees=None):
        super().__init__(first, last, department, pay)
        if employees == None:
            self.employees = []

        else:
            self.employees = employees

    def add_employees(self,employee):
        if employee in self.employees:
            return False
        else:
            self.employees.append(employee)
            return True

emp1 = Employee("ece","sena","IT",50000)
emp2 = Employee("lexa","lee","Architect",30000)
print(emp1)
print(emp2)