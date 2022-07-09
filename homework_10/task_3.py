"""
List shift func
"""
from collections import deque   # import built in method deque for fast append and pop into list


def list_shift(arr: list, num: int) -> list:
    """Func that allow fast-shift list.

    By using 'deque' class you have access to 'rotate' method that allow
    to move 'num' elements in list from beginning to the end.
    If 'num' is negative then from the end to the beginning. \

    :param arr: List that you want to shift
    :param num: A number that determines in which direction the list will move
    :return: New shifted list
    """
    sequence = deque(arr)
    if num >= 0:
        sequence.rotate(1)
    else:
        sequence.rotate(-1)
    new_list = list(sequence)
    return new_list


def main():
    deque_list = [i for i in range(1, 21)]
    print(f'{list_shift(deque_list, 1)}\n{list_shift(deque_list, -1)}')


if __name__ == '__main__':
    main()
