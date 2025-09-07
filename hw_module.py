from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees

current_date = datetime.now().date()

if __name__ == '__main__':
    calculate_salary(150000, 3)
    get_employees(145)
    print(f'Текущая дата: {current_date}')

