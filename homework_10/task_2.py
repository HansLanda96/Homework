"""
Palindrome check
"""
from string import punctuation  # import built-in module for access to punctuation


def text_format(text: str) -> str:
    """
    In this part You give params to text.

    Also using translate and maketrans method create mapp table to replace what You need.\
    :param text: Any string that You want to modify
    :return: Modified string in lowercase and replaced spacebars
    """
    modified_text = text.translate(str.maketrans("", "", punctuation))
    return modified_text.replace(" ", "").lower()


def palindrome_check(text: str) -> bool:
    """Using module text_format check string for palindrome.\

    :param text: Any text that will be processed using module text_format.
    :return: "True" if original and reversed string equal. "False" otherwise.
    """
    return text_format(text) == text_format(text[::-1])


def main():
    print(
        f'\n{palindrome_check("Паліндром - і ні морд, ні лап")}'
        f'\n{palindrome_check("132231")}'
        f'\n{palindrome_check("Step on no pets!")}'
        f'\n{palindrome_check("Red roses run no risk, sir, on Nurses order.")}'
        f'\n{palindrome_check("Hello Hillel")}'
        f'\n{palindrome_check("((((!!!// SOS @@!!!  &&&$")}'
    )


if __name__ == '__main__':
    main()
