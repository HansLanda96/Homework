from homework_4.task_7 import set_creator as st
"""import module that`s allow to create set with random integers"""


def main():
    rlist1 = st()
    rlist2 = st()
    rlist3 = list(rlist1.intersection(rlist2))
    print(f'\nFirst random list: {list(rlist1)}'
          f'\nSecond random list: {list(rlist2)}'
          f'\nNumbers that exist in first and second list: {rlist3}'
          f'\n\nAmount of numbers in both lists equal: {len(rlist3)}')


if __name__ == '__main__':
    main()
