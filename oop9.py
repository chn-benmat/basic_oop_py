# แปลง object เป็น string
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

    # รายได้ต่อปี
    def _getIncome(self):
        return self.__salary * 12
    
    # แปลงเป็น str
    def __str__(self):
        return(f"ขื่อพนักงาน = {self.__name} , แผนก = {self._department} , เงินเดือน = {self.__salary} , รายได้ต่อปี = {self._getIncome()}, บริษัท = {self._companyName}")

class Accounting(Employee):
    __departmentName = 'แผนกบัญชี'
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)
        print(self)
        
class Programmer(Employee):
    __departmentName = 'แผนกพัฒนาระบบ'
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)
        print(self)

class Sale(Employee):
    __departmentName = 'ฝ่ายขายสินค้า'
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)
        print(self)


accout = Accounting("n",25000)
programmer = Programmer("m",50000)
sale = Sale("c",30000)
