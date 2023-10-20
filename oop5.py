# Getter Setter Method
class Employee:

    def __init__(self, name, salary, department):
        self.__name = name
        self.__salary = salary
        self.__department = department

    def __del__(self):
        self.__showData()

    def __showData(self):
        print('-----------------------------------------------')
        print(f'ชื่อพนักงาน {self.__name} ')
        print(f'เงินเดือน {self.__salary} ')
        print(f'ตำแหน่ง {self.__department} ')
        print('-----------------------------------------------')

    # setter method ช่วยให้คุณควบคุมการกำหนดค่าและสามารถตรวจสอบความถูกต้อง
    def setName(self, newName):
        self.__name = newName

    def setSalary(self, newSalary):
        self.__salary = newSalary

    def setDepartment(self, newDepartment):
        self.__department = newDepartment

    # getter method อนุญาตให้คุณควบคุมการเข้าถึงค่าแอตทริบิวต์และการจัดรูปแบบการคืนค่า
    def getName(self):
        return self.__name

    def getSalary(self):
        return self.__salary

    def getDepartment(self):
        return self.__department


# การสร้าง object
obj1 = Employee('M', 23999, 'โปรแกรมเมอร์')
# setter method
obj1.setName('เอ็ม')
obj1.setSalary(50000)
obj1.setDepartment('Programer')

# getter method
print(f'พนักงานดีเด่นคือ {obj1.getName()}')
print(f'มีเงินเดือนเท่าไร {obj1.getSalary()}')
print(f'ตำแหน่งอะไร {obj1.getDepartment()}')
