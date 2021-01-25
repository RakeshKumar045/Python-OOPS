from Employee import EmployeeDatabase
from HR import PayrollSystem, HourlyPolicy
from Productivity import ProductivitySystem

productivity_system = ProductivitySystem()

payroll_system = PayrollSystem()

employee_database = EmployeeDatabase()

employees = employee_database.employees

manager = employees[0]

manager.payroll = HourlyPolicy(55)

productivity_system.track(employees, 40)

payroll_system.calculate_payroll(employees)
