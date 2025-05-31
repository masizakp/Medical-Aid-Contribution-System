from employee import Administrator, Manager, Director

def main():
    employees = [
        Administrator("A001", "john", "smith", 120_000),
        Administrator("A002", "jane", "doe", 80_000),
        Administrator("A003", "gary", "sinise", 250_000),
        Manager("A010", "craig", "bart", 300_000),
        Manager("A011", "shirley", "norman", 520_000),
        Director("A020", "vincent", "radebe", 600_000),
        Director("A021", "sipho", "msimanga", 1_200_000)
    ]

    for employee in employees:
        print(employee.print())

if __name__ == "__main__":
    main()
