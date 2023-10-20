# Class/instance Variable 
class Employee:
    # class variable ใช้เพื่อเก็บข้อมูลที่เป็นร่วมกันในทุกอ็อบเจกต์ของคลาส และใช้เป็นตัวบอกสถานะหรือข้อมูลที่เป็นร่วมในคลาสนั้น
    _minSalary = 12000
    _maxSalary = 50000
    _companyName = 'บริษัท xaa จำกัด'
    def __init__(self, name, salary, department):
        # instance variable ช่วยให้คุณเก็บข้อมูลที่เฉพาะแต่ละอ็อบเจกต์และมีความยืดหยุนในการใช้งานข้อมูลของแต่ละอ็อบเจกต์ในคลาสเดียวกัน
        self.__name = name
        self.__salary = salary
        self._department = department
        
    # private method
    def __showData(self):
        print('-----------------------------------------------')
        print(f'ชื่อพนักงาน {self.__name} ')
        print(f'เงินเดือน {self.__salary} ')
        print(f'ตำแหน่ง {self._department} ')
        print('-----------------------------------------------')

# การสร้าง object
obj1 = Employee('M', 23999, 'โปรแกรมเมอร์')
# class variable
print(Employee._minSalary)
# instance variable
print(obj1._department)