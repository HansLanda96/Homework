from random import *
"""Create list that will have numbers from 1 to 7 and will have range from 5 symbols to 55 symbols"""

random_list = [randint(1, 7) for random_number in range(randint(5, 55))]
check = 0
for random_number in range(1, len(random_list) - 1):
    if random_list[random_number - 1] < random_list[random_number] > random_list[random_number + 1]:
        check += 1
print(f'Program generated random list: {random_list} '
      f'\n\nNumbers in random list that bigger than neighbours equals: {check}\n')


"""ANOTHER SOLUTION"""


def random_list():
    """
    with this func you can create own random list with needed params
    Also can use this in different tasks where I need randomly generated list with integers(in task_7 for example:D)

    :return: gives randomly generated list with input params
    """
    number_start = int(input("Insert start number for generating numbers into a random list : "))
    number_end = int(input("Insert on what number you want to end the generation of numbers into a random list: "))
    range_start = int(input("Insert the minimum desired amount of numbers in the random list: "))
    range_end = int(input("Insert the maximum desired amount of numbers in the random list: "))
    r_list = [randint(number_start, number_end) for _ in range(randint(range_start, range_end))]
    return r_list


def main():
    """main func take random list from upper def and checking how many
       generated numbers bigger than 'neighboring' numbers"""
    rando_list = random_list()
    checker = 0
    for random_number in range(1, len(rando_list) - 1):
        if rando_list[random_number - 1] < rando_list[random_number] > rando_list[random_number + 1]:
            checker += 1

    print(f'\n\nProgram generated random list: {rando_list} '
          f'\n\nNumbers in random list that bigger than neighbours equals: {checker}')


if __name__ == "__main__":
    main()


"""also I can do func random_list in another way. With required parameters
   it will look like this:                                              """


def random_list1(number_start, number_end, range_start, range_end):
    """
    :param number_start:  insert num which "random" module will generate in list
    :param number_end:    insert num on which "random" should stop generate numbers in list
    :param range_start:   insert start number of amount numbers in your list
    :param range_end:     insert end number in which "random" should stop in your list
    :return:              will give your random list with yours parameters
    """
    r_list = [randint(number_start, number_end) for _ in range(randint(range_start, range_end))]
    return r_list


"""if i create func like this i will insert required param in random_list(1, 5, 10, 45)"""
