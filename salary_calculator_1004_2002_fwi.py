# 代码生成时间: 2025-10-04 20:02:50
# -*- coding: utf-8 -*-

"""
薪资计算器
本模块实现了一个简单的薪资计算器，可以根据员工的基本工资和工作小时数计算薪资。
"""

import scrapy

# 定义一个简单的员工类
class Employee:
    def __init__(self, base_salary, hours_worked):
        self.base_salary = base_salary  # 基本工资
        self.hours_worked = hours_worked  # 工作小时数

    def calculate_salary(self):
        """
        计算员工的薪资。
        如果工作小时数超过40小时，则超出部分按1.5倍工资计算。

        :return: 员工的薪资
        """
        if self.hours_worked <= 40:
            return self.base_salary * self.hours_worked
        else:
            return self.base_salary * 40 + (self.base_salary * 1.5) * (self.hours_worked - 40)

# 定义薪资计算器类
class SalaryCalculator:
    def __init__(self):
        self.employees = []  # 存储员工信息

    def add_employee(self, employee):
        """
        添加员工信息到列表。

        :param employee: Employee对象
        """
        if not isinstance(employee, Employee):
            raise ValueError("Invalid employee object")
        self.employees.append(employee)

    def calculate_salaries(self):
        """
        计算所有员工的薪资。

        :return: 员工薪资字典
        """
        salaries = {}
        for employee in self.employees:
            try:
                salary = employee.calculate_salary()
                salaries[employee] = salary
            except Exception as e:
                print(f"Error calculating salary for employee: {e}")
        return salaries

# 示例使用
if __name__ == '__main__':
    # 创建薪资计算器实例
    calculator = SalaryCalculator()

    # 创建员工实例
    employee1 = Employee(100, 40)  # 基本工资100，工作40小时
    employee2 = Employee(100, 45)  # 基本工资100，工作45小时

    # 添加员工到薪资计算器
    calculator.add_employee(employee1)
    calculator.add_employee(employee2)

    # 计算薪资
    salaries = calculator.calculate_salaries()
    for employee, salary in salaries.items():
        print(f"Employee base_salary: {employee.base_salary}, hours_worked: {employee.hours_worked}, salary: {salary}")