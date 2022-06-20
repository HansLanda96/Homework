from homework_4.task_6 import random_list1 as rl
"""
   Import module random list from previous home task
   So I can create random list with parameters
"""


def main():
    my_list = rl(1, 100, 20, 20)
    print(f'\nGenerated list: \t\t{my_list}')
    for numbers, elements in enumerate(my_list):
        if elements % 2 != 0:
            my_list[numbers] = 0
    print(f'\nList without odd nums: \t{my_list}'
          f'\n\nAmount of zeros in list: {my_list.count(0)}')


if __name__ == "__main__":
    main()
