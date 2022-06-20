from string import punctuation
"""from built-in library importing punctuation"""


def amount_words(words: str) -> int:
    """Strip punctuation symbols in my string, so punctuation can't be count as 'word' """
    return sum([words.strip(punctuation).isalpha() for words in words.split()])


def amount_symbols(symbols: str) -> int: return len(symbols) - symbols.count(' ')


def main():
    string = input("Insert any text: ")
    print(f'\nAmount of words in text: {amount_words(string)}')
    print(f'Symbols in text: {amount_symbols(string)}')


if __name__ == '__main__':
    main()
