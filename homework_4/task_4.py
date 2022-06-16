def ladder(start: int, end=9):
    """func allows us to print new string for each iteration"""
    ladder_step = ''
    for num in range(start, end + 1):
        ladder_step += str(num)
        print(ladder_step)


def main():
    ladder(1)


if __name__ == "__main__":
    """enter point of program"""
    main()
