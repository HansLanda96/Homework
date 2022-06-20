def delete_none(dictionary: dict):
    """Function check dictionary for 'None' value and deleting 'Key' if founds it"""
    for key, value in dict(dictionary).items():
        if value is None:
            del dictionary[key]
    return dictionary


def main():
    my_dict = {
        "Ukraine": "Kyiv", "USA": "Washington", "Germany": "Berlin",
        "russia": None, "belarus": None, "syria": None, "UK": "London"
    }
    print(f'\nMy dict before upgrade: \t{my_dict}'
          f'\n\nMy dict after upgrade: \t\t{delete_none(my_dict)}')


if __name__ == '__main__':
    main()
