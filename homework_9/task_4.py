"""
Replace words func
"""


def replace_str(original: str, old_word: str, new_word: str, amount: int) -> str:
    """
    :param original: text in which you want to change some words
    :param old_word: word to be replaced
    :param new_word: the word to which the old word will change
    :param amount: amount of words to be replaced
    :return: string with changed words
    """
    return original.replace(old_word, new_word, amount)


if __name__ == '__main__':
    print(replace_str("My name is Iegor, James Iegor!", "Iegor", "Bond", 2))
