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