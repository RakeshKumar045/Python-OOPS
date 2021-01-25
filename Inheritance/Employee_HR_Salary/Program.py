import Employee as employees

salary_employee = employees.SalaryEmployee(1, 'John Smith', 1500)

hourly_employee = employees.HourlyEmployee(2, 'Jane Doe', 40, 15)

commission_employee = employees.CommissionEmployee(3, 'Kevin Bacon', 1000, 250)

payroll_system = HR.PayrollSystem()

payroll_system.calculate_payroll([
    salary_employee,
    hourly_employee,
    commission_employee
])
