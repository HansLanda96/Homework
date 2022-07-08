"""
Longest word in a string
"""
from string import digits, punctuation


def str_strip(text: str) -> str:
    """Strip and return text without digits and punctuation symbols"""
    return text.strip(digits + punctuation)


def long_word(text: str) -> str:
    """
    :return: return longest word in a string
    """
    word = max(str_strip(text).split(), key=len)
    return word


def main():
    sentence = str(input("Enter any text: "))
    print(long_word(sentence))


if __name__ == '__main__':
    try:
        main()
    except ValueError:
        print("Dude, you didn't even enter a single letter")
