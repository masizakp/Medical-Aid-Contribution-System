from printable import Printable

class Employee(Printable):
    def __init__(self, employee_num: str, name: str, surname: str, annual_salary: float):
        self.employee_num = employee_num
        self.name = name
        self.surname = surname
        self.annual_salary = annual_salary

    def get_monthly_salary(self) -> float:
        return self.annual_salary / 12

    def calculate_medical_aid(self) -> float:
        raise NotImplementedError("Subclasses must implement this method.")

class Administrator(Employee):
    def calculate_medical_aid(self) -> float:
        contribution = self.get_monthly_salary() * 0.10
        return max(800, min(2000, contribution))

    def print(self) -> str:
        return f"[Administrator] {self.employee_num} - {self.name} {self.surname} | Medical Aid: R{self.calculate_medical_aid():,.2f}"

class Manager(Employee):
    def calculate_medical_aid(self) -> float:
        contribution = self.get_monthly_salary() * 0.075
        return max(1200, min(3000, contribution))

    def print(self) -> str:
        return f"[Manager] {self.employee_num} - {self.name} {self.surname} | Medical Aid: R{self.calculate_medical_aid():,.2f}"

class Director(Employee):
    def calculate_medical_aid(self) -> float:
        return 5000.00

    def print(self) -> str:
        return f"[Director] {self.employee_num} - {self.name} {self.surname} | Medical Aid: R{self.calculate_medical_aid():,.2f}"

