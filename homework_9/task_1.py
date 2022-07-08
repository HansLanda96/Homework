"""
Point counter
"""


def count_points(win: int, draw: int, loss: int) -> int:
    """
    Description
    :param win: 3 points
    :param draw: 1 point
    :param loss: -1 point
    :return: result of points
    """
    return win * 3 + draw - loss

    # Uncomment if you u want to add exceptions
    # Any of the params cannot equal zero or less than zero
    # Also points do not go negative
    # result = 0
    # if win >= 0 and draw >= 0 and loss >= 0:
    #     points = win * 3 + draw - loss
    #     result += points
    #     while result <= 0:
    #         result = 0
    #         return result
    # else:
    #     raise ValueError
    # return result


if __name__ == '__main__':
    print(count_points(4, 3, 2))

    # Uncomment if you u want to add exceptions
    # try:
    #     print(count_points(4, 3, 2))
    # except ValueError as e:
    #     print("There is no chance of negative number in params")
