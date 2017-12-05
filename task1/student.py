from Exercise6.task1.module import *  # REMARK: imports had to be changed in order to be found in PyCharm!
from Exercise6.task1.moduleElement import *

class Student(object):

    def __init__(self, name):
        self.name = name

        self.modules = []
        self.grades = {}

    def add_module(self, mod):
        self.modules.append(mod)
        self.grades[mod.get_title()] = mod.get_grade()

    def get_list_modules(self):
        print("Modules of Student {}".format(self.name))
        for m in self.modules:
            print("\t{}".format(m.get_title()))

    def get_grades(self):
        print("Grades of Student {}".format(self.name))
        for key, value in self.grades.items():
            print("\t{}: {}".format(key, value))


### test cases ###

me = Student("FirstName LastName")
me.add_module(info1)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#   Info 1

me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#   Info 1: 6
