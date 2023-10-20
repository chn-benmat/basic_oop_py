# การสร้าง class
class Employee:
    # การสร้าง method
    def detail(self, name, salary):
        self.name = name
        self.salary = salary

    def showData(self):
        print('กำหนดคุณสมบัติเรียบร้อย')
        print(f'ชื่อพนักงาน {self.name} มีเงินเดือน {self.salary}')


# การสร้าง object
obj1 = Employee()
obj1.detail('M', 23999)
obj2 = Employee()
obj2.detail('B', 50000)
obj3 = Employee()
obj3.detail('C', 25000)

obj1.showData()
obj2.showData()
