# Encapsulation
class Employee:

    def __init__(self, name, salary, department, age):
        # pubilc attribute เข้าถึงได้ทั้งจากภายใน Class, Subclass และจากภายนอก Class
        self.name = name
        self.salary = salary
        
        # protectes attribute เข้าถึงได้เฉพาะภายใน Class นี้ และภายใน Subclass ที่ extends หรือสืบทอดสมาชิกจาก Class นี้เท่านั้น
        self._department = department
        
        # private attribute เข้าถึงได้เฉพาะภายใน Class นี้เท่านั้น
        self.__age = age
        
        # ถ้าอยากเรียกใช้ private method ต้องเรียกภายใน class นั้น
        self.__showData3()
        
    # public method
    def showData1(self):
        print('กำหนดคุณสมบัติเรียบร้อย')
        print(f'ชื่อพนักงาน {self.name} มีเงินเดือน {self.salary}')
        print('-----------------------------------------------')
   
    # protectes method
    def _showData2(self):
        print('กำหนดคุณสมบัติเรียบร้อย')
        print(f'มีตำแหน่ง {self._department}')
        print('-----------------------------------------------')

    # private method
    def __showData3(self):
        print('กำหนดคุณสมบัติเรียบร้อย')
        print(f'อายุ {self.__age}')  # private
        print('-----------------------------------------------')


# การสร้าง object
obj1 = Employee('M', 23999, 'โปรแกรมเมอร์', 18)
obj1.salary = 50000
obj1.showData1()
obj1._showData2()
