from task_2 import input_number


def sequence_nums(first_num: int, second_num: int, var_list: list):
    while first_num > second_num or first_num < second_num:
        if first_num < second_num:
            var_list.append(first_num)
            first_num += 1
        else:
            var_list.append(first_num)
            first_num -= 1
    var_list.append(second_num)


def main():
    var_list = []
    first_num = input_number("Insert first num: ")
    second_num = input_number("Insert second num: ")
    sequence_nums(first_num, second_num, var_list)
    print(f'Sequence of numbers equal : {var_list}')


if __name__ == "__main__":
    main()
