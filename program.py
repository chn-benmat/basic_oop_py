from programer import Programmer
from acounting import Accounting
from sale import Sale

accout = Accounting("n", 25000, 25)
programmer = Programmer("m", 50000, 2, 'พัฒนาเกม')
sale = Sale("c", 30000, 'เชียงใหม่')

accout._showData()
programmer._showData()
sale._showData()
        