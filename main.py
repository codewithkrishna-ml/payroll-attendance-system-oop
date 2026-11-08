#PROJECT-Payroll-Attendance-System
class Employee:
    def __init__(self, emp_id, name, role, base_salary, attendance_count):
        self.emp_id = int(emp_id)
        self.name = name
        self.role = role
        self.base_salary = float(base_salary)
        self.attendance_count = int(attendance_count)

    def __str__(self):
        return f"Employee ID: {self.emp_id} | Name: {self.name} | Role: {self.role} | Salary: {self.base_salary:.2f} | Attendance: {self.attendance_count}"


class PayrollSystem:
    def __init__(self):
        self.employee_db = {}
        self.total_payout_month = 0.0
        self.id_counter = 101

    def add_new_employee(self, name, role, base_salary):
        if name == "" or role == "":
            print("Error: Name or Role cannot be empty.")
            return False
        
        if float(base_salary) <= 0:
            print("Error: Salary must be greater than 0.")
            return False

        emp_id = self.id_counter
        new_emp = Employee(emp_id, name, role, base_salary, 0)
        self.employee_db[emp_id] = new_emp
        print(f"Employee added successfully! Assigned ID: {emp_id}")
        self.id_counter += 1
        return True

    def mark_attendance(self, emp_id, status):
        if emp_id not in self.employee_db:
            print("Error: Employee ID not found.")
            return False

        if status != "P" and status != "A":
            print("Error: Invalid status. Use P for Present or A for Absent.")
            return False

        emp = self.employee_db[emp_id]
        if status == "P":
            emp.attendance_count += 1
            print(f"Attendance marked Present for {emp.name}.")
        else:
            print(f"Attendance marked Absent for {emp.name}.")
        return True

    def calculate_monthly_pay(self, emp_id):
        if emp_id not in self.employee_db:
            print("Error: Employee ID not found.")
            return False

        emp = self.employee_db[emp_id]
        if emp.attendance_count == 0:
            print(f"Payout Details for {emp.name}: Net Salary is $0.00 (0 days present).")
            return 0.0

        per_day_pay = emp.base_salary / 30
        net_salary = per_day_pay * emp.attendance_count
        
        print(f"\n--- Salary Slip for ID: {emp.emp_id} ---")
        print(f"Name: {emp.name} | Role: {emp.role}")
        print(f"Base Salary: ${emp.base_salary:.2f}")
        print(f"Total Days Present: {emp.attendance_count}/30")
        print(f"Net Payable Salary: ${net_salary:.2f}")
        print("---------------------------------")
        return net_salary

    def view_dashboard(self):
        if len(self.employee_db) == 0:
            print("No employees registered in the system yet.")
            return

        print("\n" + "-"*80)
        print(f"{'EMP ID':<10} | {'NAME':<20} | {'ROLE':<15} | {'BASE SALARY':<12} | {'PRESENT DAYS':<12}")
        print("-"*80)
        for emp_id in self.employee_db:
            emp = self.employee_db[emp_id]
            print(f"{emp.emp_id:<10} | {emp.name:<20} | {emp.role:<15} | ${emp.base_salary:<11.2f} | {emp.attendance_count:<12}")
        print("-"*80)

    def export_ledger_to_csv(self):
        if len(self.employee_db) == 0:
            print("No records available to export.")
            return False

        try:
            file = open("employee_attendance_ledger.csv", mode="w")
            file.write("EmployeeID,Name,Role,BaseSalary,PresentDays\n")
            for emp_id in self.employee_db:
                emp = self.employee_db[emp_id]
                file.write(f"{emp.emp_id},{emp.name},{emp.role},{emp.base_salary},{emp.attendance_count}\n")
            file.close()
            print("Data successfully exported to employee_attendance_ledger.csv")
            return True
        except:
            print("Error writing data to CSV file.")
            return False


manager = PayrollSystem()

while True:
    print("\n------------ PAYROLL & ATTENDANCE SYSTEM -----------------")
    print("1. Add New Employee Profile")
    print("2. Mark Daily Attendance")
    print("3. Calculate Monthly Payroll")
    print("4. View Employee Performance Dashboard")
    print("5. Export Attendance Ledger to CSV")
    print("6. Exit System")

    choice = input("Select an option (1-6): ").strip()

    if choice == "1":
        name = input("Enter Employee Name: ").strip()
        role = input("Enter Role/Designation: ").strip()
        try:
            salary = float(input("Enter Monthly Base Salary: ").strip())
            manager.add_new_employee(name, role, salary)
        except ValueError:
            print("Error: Salary must be a numerical value.")

    elif choice == "2":
        try:
            e_id = int(input("Enter Employee ID: ").strip())
            stat = input("Enter Status (P for Present / A for Absent): ").strip().upper()
            manager.mark_attendance(e_id, stat)
        except ValueError:
            print("Error: ID must be a valid number.")

    elif choice == "3":
        try:
            e_id = int(input("Enter Employee ID: ").strip())
            manager.calculate_monthly_pay(e_id)
        except ValueError:
            print("Error: ID must be a valid number.")

    elif choice == "4":
        manager.view_dashboard()

    elif choice == "5":
        manager.export_ledger_to_csv()

    elif choice == "6":
        print("Exiting Payroll System. Goodbye!")
        break

    else:
        print("Invalid choice! Please select an option between 1 and 6.")
