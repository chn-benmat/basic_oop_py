# Super
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
    __departmentName = 'แผนกบัญชี'
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)
        super()._showData()
class Programmer(Employee):
    __departmentName = 'แผนกพัฒนาระบบ'
    
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)
        super()._showData()


class Sale(Employee):
    __departmentName = 'ฝ่ายชายสินค้า'
    
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)
        super()._showData()


accout = Accounting("n",25000)
programmer = Programmer("m",50000)
sale = Sale("c",30000)
