# Inheritance อนุญาตให้คลาสหรืออ็อบเจกต์สามารถสืบทอดคุณสมบัติและเมธอดจากคลาสหรืออ็อบเจกต์อื่น ๆ
class Employee:
    minSalary = 12000
    maxSalary = 50000
    _companyName = 'บริษัท xaa จำกัด'

    def __init__(self, name, salary, department):
        self.__name = name
        self.__salary = salary
        self._department = department

    def _showData(self):
        print('-----------------------------------------------')
        print(f'ชื่อพนักงาน {self.__name} ')
        print(f'เงินเดือน {self.__salary} ')
        print(f'ตำแหน่ง {self._department} ')
        print('-----------------------------------------------')


class Accounting(Employee):
    _departmentName = 'แผนกบัญชี'
    def __init__(self):
        pass

class Programmer(Employee):
    _departmentName = 'แผนกพัฒนาระบบ'
    
    def __init__(self):
        pass


class Sale(Employee):
    _departmentName = 'ฝ่ายชายสินค้า'
    
    def __init__(self):
        pass

accout = Accounting()
programmer = Programmer()
sale = Sale()
print(accout.minSalary)
