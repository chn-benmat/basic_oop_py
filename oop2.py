# การสร้าง Constructor และ Destructor
class Employee:
    # Constructor เริ่มโค้ดจะถูกเรียกใช้งานก่อน

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Method
    def showData(self):
        print('กำหนดคุณสมบัติเรียบร้อย')
        print(f'ชื่อพนักงาน {self.name} มีเงินเดือน {self.salary}')

    #  Destructor จบการทำงานของโค้ดจะถูกเรียกใช้
    def __del__(self):
        print('Call Destructor')


# การสร้าง object
obj1 = Employee('M', 23999)
obj1.salary = 70000
obj1.showData()
