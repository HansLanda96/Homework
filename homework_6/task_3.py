from string import ascii_lowercase as asciis


def dict_from_list(value: list) -> dict:
    letters_dict = {key: item for key, item in enumerate(value, 1)}
    return letters_dict


def main():
    letters = list(asciis[:5])
    print(dict_from_list(letters))


if __name__ == '__main__':
    main()


