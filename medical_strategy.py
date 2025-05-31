from abc import ABC, abstractmethod

class MedicalAidStrategy(ABC):
    @abstractmethod
    def calculate(self, monthly_salary: float) -> float:
        pass

class AdminMedicalAid(MedicalAidStrategy):
    def calculate(self, monthly_salary: float) -> float:
        return max(800, min(2000, monthly_salary * 0.10))

class ManagerMedicalAid(MedicalAidStrategy):
    def calculate(self, monthly_salary: float) -> float:
        return max(1200, min(3000, monthly_salary * 0.075))

class DirectorMedicalAid(MedicalAidStrategy):
    def calculate(self, monthly_salary: float) -> float:
        return 5000.00
