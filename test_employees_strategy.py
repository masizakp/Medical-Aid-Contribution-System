from employee_strategy import Employee
from medical_strategy import AdminMedicalAid, ManagerMedicalAid, DirectorMedicalAid

def main():
    employees = [
        Employee("A001", "john", "smith", 120_000, "Administrator", AdminMedicalAid()),
        Employee("A002", "jane", "doe", 80_000, "Administrator", AdminMedicalAid()),
        Employee("A003", "gary", "sinise", 250_000, "Administrator", AdminMedicalAid()),
        Employee("A010", "craig", "bart", 300_000, "Manager", ManagerMedicalAid()),
        Employee("A011", "shirley", "norman", 520_000, "Manager", ManagerMedicalAid()),
        Employee("A020", "vincent", "radebe", 600_000, "Director", DirectorMedicalAid()),
        Employee("A021", "sipho", "msimanga", 1_200_000, "Director", DirectorMedicalAid())
    ]

    for emp in employees:
        print(emp.print())

if __name__ == "__main__":
    main()
