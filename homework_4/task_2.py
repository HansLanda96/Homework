def input_number(number: str) -> int:
    """return input of number"""
    result = ''
    while not result.isdigit():
        result = input(number)
    return int(result)


def amount(sequence: list) -> int:
    """return length of sequence"""
    return len(sequence)


def summary(sequence: list) -> int:
    """return sum of sequence"""
    summa = 0
    for element in sequence:
        summa += element
    return summa


def multiplication(sequence: list) -> int:
    """return multiplication of sequence"""
    multipl_operation = 1
    for integers in sequence:
        multipl_operation *= integers
    return multipl_operation


def average_sequence(sequence: list) -> float:
    """return average mean of sequence"""
    avg = (summary(sequence) / amount(sequence)) * 10 // 1 / 10
    return avg


def highest_value_index(sequence: list) -> tuple:
    """return highest val in sequence with index"""
    highest = 0
    _index_ = 0
    for index, integers in enumerate(sequence):
        if highest < integers:
            highest = integers
            _index_ = index + 1
    return _index_, highest


def even_nums(sequence: list) -> int:
    """return even numbers of sequence"""
    result = 0
    for integer in sequence:
        if integer % 2 == 0:
            result += 1
    return result


def odd_nums(sequence: list) -> int:
    """return odd numbers of sequence"""
    result = 0
    for integer in sequence:
        if integer % 2 != 0:
            result += 1
    return result


def second_highest(sequence: list, highest_num: int) -> tuple:
    """return second high number in sequence"""
    sec_high = 0
    for integer in sequence:
        if sec_high < integer < highest_num:
            sec_high = integer
    return sec_high


def highest_ints_from_sequence(sequence: list, number: int) -> int:
    """return high amounts"""
    high_amount = 0
    for nums in sequence:
        if nums == number:
            high_amount += 1
    return high_amount


def main():
    """create main func that will run all func in file"""
    sequence_list = []
    sequence = ''
    while sequence != 0:
        sequence = input_number("Insert positive integers in sequence (press '0' if you want to stop): ")
        if sequence != 0:
            sequence_list.append(sequence)
    else:   # add additional var for normal work of two last funcs
        highest_num = highest_value_index(sequence_list)

    print(f"\nYou insert this nums in sequence: {sequence_list}"
          f"\n\nAmount of nums that inserted in sequence: {amount(sequence_list)}"
          f"\nSum of nums in sequence: {summary(sequence_list)}"
          f"\nMultiplication for all numbers in sequence: {multiplication(sequence_list)}"
          f"\nAverage in sequence: {average_sequence(sequence_list)}"
          f"\nHighest number in sequence: {highest_value_index(sequence_list)[1]} "
          f"with index {highest_value_index(sequence_list)[0]}"
          f"\nAmount of even numbers in sequence: {even_nums(sequence_list)}"
          f"\nAmount of odd numbers in sequence: {odd_nums(sequence_list)}"
          f"\nSecond highest number in sequence: {second_highest(sequence_list, highest_num[1])}"
          f"\nHighest number(s) in sequence occur: {highest_ints_from_sequence(sequence_list, highest_num[1])} times ")


if __name__ == '__main__':
    """enter point of program"""
    main()
