from Exercise6.task2.vehicle import *  # REMARK: imports had to be changed in order to be found in PyCharm!
from Exercise6.task2.customer import *

class Employee(object):

    emp_id = 0

    def __init__(self, name):
        self.__name = name

        Employee.emp_id += 1
        self.__id = Employee.emp_id

    def __str__(self):
        return "Employee: {} is of type {}".format(self.get_name(), self.get_title())

    def get_name(self):
        return self.__name

    def get_title(self):
        return "Subordinate"


class Manager(Employee):
    def get_title(self):
        return "Manager"

    def get_sales_report(self, salesman):
        sum = 0
        if salesman not in salesman.sales:
            raise KeyError("{} doesn't have any sales yet".format(salesman.get_name()))
        for sale in salesman.sales.items():
            if sale[0] == salesman:
                sum += sale[1]
        print("{}'s current cumulative sales:\n{}".format(salesman.get_name(), sum))


class Salesman(Employee):
    sales = {}

    def sale(self, vehicle, sales_price, customer):
        if customer.get_score():
            self.sales[self] = self.sales.get(self, 0) + sales_price
        else:
            print("Customer does not have enough credit score.")


### test cases ###

## initialising employee instances

Eric = Manager("Eric")
Kyle = Employee("Kyle")
Stan = Salesman("Stan")
Kenny = Salesman("Kenny")
Craig = Salesman("Craig")

## printing employee instances

print(Eric) # expected output: Employee: Eric is of type Manager
print(Kyle) # expected output: Employee: Kyle is of type Subordinate
print(Stan) # expected output: Employee: Stan is of type Subordinate
print(Kenny) # expected output: Employee: Kenny is of type Subordinate
print(Craig) # expected output: Employee: Craig is of type Subordinate


## registering sales

Kenny.sale(Veh2,6000,Heidi)
Stan.sale(Veh1,9000,Wendy)


## printing an individual sales report:

Eric.get_sales_report(Kenny)
# expected output:
# Kenny's current cumulative sales:
# 6000
