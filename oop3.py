# function เสริม
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


class Customer:
    name = 'B'

    def __init__(self, age):
        self.age = age

    def showData(self):
        print('กำหนดคุณสมบัติเรียบร้อย')
        print(f'ชื่อลูกค้า {self.name} มีอายุ {self.age}')


# การสร้าง object
obj1 = Employee('M', 23999)
obj2 = Customer(29)

# isinstance เช็คObjectในClassนั้นใช่หรือไม่
print(isinstance(obj1, Employee))  # True
print(isinstance(obj2, Employee))  # False

# dir เช็ค attribute และ method ว่ามีไรให้เรียกใช้บ้าง
print(dir(obj1))

# __class__ เช็คว่า object นั้นสร้างมาจาก class นั้นมั้ย
print(obj1.__class__)
