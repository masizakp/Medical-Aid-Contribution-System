from printable import Printable
from medical_strategy import MedicalAidStrategy

class Employee(Printable):
    def __init__(self, employee_num: str, name: str, surname: str, annual_salary: float, role: str, strategy: MedicalAidStrategy):
        self.employee_num = employee_num
        self.name = name
        self.surname = surname
        self.annual_salary = annual_salary
        self.role = role
        self.strategy = strategy

    def get_monthly_salary(self) -> float:
        return self.annual_salary / 12

    def calculate_medical_aid(self) -> float:
        return self.strategy.calculate(self.get_monthly_salary())

    def print(self) -> str:
        return f"[{self.role}] {self.employee_num} - {self.name} {self.surname} | Medical Aid: R{self.calculate_medical_aid():,.2f}"
