from task_6 import random_list as rl
"""import module random_list into a file"""


def set_creator():
    """func creating random list and converts it to set"""
    rlist = set(rl())
    return rlist


def main():
    """create two random set -> printing two random sets in lists equivalent -> work with set for information """
    rlist1 = set_creator()
    rlist2 = set_creator()
    print(f'\n\nFirst created list: {list(rlist1)} '
          f'\n\nSecond created list: {list(rlist2)}'
          f'\nNumbers that exist in first and second list: {rlist1 & rlist2}'
          f'\nNumbers that are in the first list and not in the second: {rlist1.difference(rlist2)}'
          f'\nUnique numbers for each list: {rlist1.difference(rlist2)} | {rlist2.difference(rlist1)}')


if __name__ == "__main__":
    """enter point of program"""
    main()


"""SOLUTION WITHOUT FUNC"""
any_list = set(rl())
any_list2 = set(rl())
# print(f'\n\nFirst created list: {list(any_list)} '
#       f'\n\nSecond created list: {list(any_list2)}'
#       f'\nNumbers that exist in first and second list: {any_list & any_list2}'
#       f'\nNumbers that are in the first list and not in the second: {any_list.difference(any_list2)}'
#       f'\nUnique numbers for each list: {any_list.difference(any_list2)} | {any_list2.difference(any_list)}')

