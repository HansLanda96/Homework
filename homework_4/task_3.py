from task_2 import input_number as inp
"""import module(input_number) from task_2"""


def sequence_nums(first_num: int, second_num: int, var_list: list):
    """create func that allows us to iterate and append list"""
    while first_num > second_num or first_num < second_num:
        if first_num < second_num:
            var_list.append(first_num)
            first_num += 1
        else:
            var_list.append(first_num)
            first_num -= 1
    var_list.append(second_num)


def main():
    """create main function with imported module from task_2"""
    var_list = []
    first_num = inp("Insert first number: ")
    second_num = inp("Insert second number: ")
    sequence_nums(first_num, second_num, var_list)
    print(f'Sequence of numbers equal : {var_list}')


if __name__ == "__main__":
    """enter point of program"""
    main()
