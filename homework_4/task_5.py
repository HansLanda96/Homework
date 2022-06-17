def string_input():
    """func will return input letters and numbers in string"""
    string = ""
    while not string.isalnum():
        string = input("Program will not count a row if you'll input any specific symbol including 'space bar'!!!"
                       "\n\nInsert letters and numbers to create a row: ")
    return str(string)


def main():
    """func work with input and printing needed results"""
    string = string_input()
    print(f'\nYou created a row that includes this elements: {string}'
          f'\nThird element in a row: {string[2]}'
          f'\nPenultimate element in a row: {string[-2]}'
          f'\nFirst five elements in a row: {string[0:5]}'
          f'\nWhole row without two last elements: {string[0:-2]}'
          f'\nEvery "even" element in a row: {string[0::2]}'
          f'\nEvery "odd" element in a row: {string[1::2]}'
          f'\nReversed row: {string[::-1]}'
          f'\nReversed row with every second element: {string [-1::-2]}'
          f'\nLength of row: {len(string)}'
          f'\n')


if __name__ == "__main__":
    """enter point of program"""
    main()


"""ALSO possible to solve this task like this
And we will not have any probs with specific symbols or space bar
In this case very funny to write message for example, that's give funny results:D"""

row = str(input("Insert any elements in a row: "))
# print(f'\nYou created a row that includes this elements: {row}'
#       f'\nThird element in a row: {row[2]}'
#       f'\nPenultimate element in a row: {row[-2]}'
#       f'\nFirst five elements in a row: {row[0 : 5]}'
#       f'\nWhole row without two last elements: {row[0 : -2]}'
#       f'\nEvery "even" element in a row: {row[0 : : 2]}'
#       f'\nEvery "odd" element in a row: {row[1 : : 2]}'
#       f'\nReversed row: {row[ : : -1]}'
#       f'\nReversed row with every second element: {row [-1 : : -2  ]}'
#       f'\nLength of row: {len(row)}')
