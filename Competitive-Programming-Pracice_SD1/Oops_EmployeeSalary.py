'''Write a python class Employee with attributes like emp_id,emp_name,emp_salary and emp_department and methods like calculate
emp_salary,emp_assign_dept and print emp_details'''
class Employee():
    def __init__(self):
        self.emp_id=int(input("Enter emplyee ID:"))
        self.emp_name=input("Enter emplyee Name:")
        self.emp_salary=float(input("Enter emplyee Salary:"))
        self.emp_department=input("Enter emplyee Departmet:")
    def cal_emp_sal(self,working_hrs,sal):
        overtime=working_hrs-50
        if overtime>0:
            overtime_salary=overtime*(self.emp_salary/50)
            print("Salary Increased=",overtime_salary)
            print("Total Salary=",sal+overtime_salary)
        else:
            print("Salary=",sal)
    def assg_dept(self):
        print(self.emp_id,"is assigned to",self.emp_department)
    def emp_details(self):
        print("------------Employee Details------------")
        print("Employee Name:",self.emp_name)
        print("Employee ID:",self.emp_id)
        print("Employee salary:",self.emp_salary)
        print("Employee Department:",self.emp_department)
e1=Employee()
e1
e1.cal_emp_sal(5,20000)
e1.assg_dept()
e1.emp_details()
        