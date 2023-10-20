# Overloading
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
    def _getIncome(self,bonus = 0):
        return (self.__salary * 12) + bonus

    # แปลงเป็น str
    def __str__(self):
        return (f"ขื่อพนักงาน = {self.__name} , แผนก = {self._department} , เงินเดือน = {self.__salary} , รายได้ต่อปี = {self._getIncome()}, บริษัท = {self._companyName} ")


class Accounting(Employee):
    __departmentName = 'แผนกบัญชี'

    def __init__(self, name, salary, age):
        super().__init__(name, salary, self.__departmentName)
        self.__age = age

    def _showData(self):
        super()._showData()
        print(f'อายุ {self.__age} ')

    def __str__(self):
        return (super().__str__() + f'อายุ {self.__age}')


class Programmer(Employee):
    __departmentName = 'แผนกพัฒนาระบบ'

    def __init__(self, name, salary, experience, skill):
        super().__init__(name, salary, self.__departmentName)
        self.__exp = experience
        self.__skill = skill

    def _showData(self):
        super()._showData()
        print(f'ประสบการณ์ {self.__exp} ')
        print(f'ทักษะ {self.__skill} ')

    def __str__(self):
        return (super().__str__() + f'ประสบการณ์ {self.__exp} ทักษะ {self.__skill}')


class Sale(Employee):
    __departmentName = 'ฝ่ายขายสินค้า'

    def __init__(self, name, salary, area):
        super().__init__(name, salary, self.__departmentName)
        self.__area = area

    def _showData(self):
        super()._showData()
        print(f'พื้นที่รับผิดชอบ {self.__area} ')

    def __str__(self):
        return (super().__str__() + f'พื้นที่รับผิดชอบ {self.__area}')

accout = Accounting("n", 25000, 25)
programmer = Programmer("m", 50000, 2, 'พัฒนาเกม')
sale = Sale("c", 30000, 'เชียงใหม่')
print(accout._getIncome())
print(programmer._getIncome())
print(sale._getIncome())
        
