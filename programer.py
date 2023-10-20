from employee import Employee
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
