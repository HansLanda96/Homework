from datetime import date
from homework_4.task_2 import input_number as inp
"""
import module date ,so I get access for 'date' class in module
import module input number from previous home task
"""


def is_date(day: int, month: int, year: int) -> bool:
    """Making exception with access to 'date' class. If ValueError happens will return false """
    valid_date = True
    try:
        date(year, month, day)
    except ValueError:
        valid_date = False
    return valid_date


def main():
    """input all parameters with imported module and make func work"""
    day = inp("Insert day: ")
    month = inp("Insert month: ")
    year = inp("Insert year: ")
    my_date = date(day=day, month=month, year=year)
    if is_date(day, month, year):
        print(f'\n{is_date(day, month, year)}'
              f'\nYour date {format(my_date, "%d/%m/%Y")} is correct')
    else:
        print(f'\n{is_date(day, month, year)}'
              f'\nYour date {format(my_date, "%d/%m/%Y")} is not correct')


if __name__ == "__main__":
    main()
