"""
Create txt file with the necessary information
"""


def save_txt(name: str):
    """Simple save of file with needed information into txt file.
    \
    :param name: Enter file name for save
    :return: Saved file with info in txt format
    """
    with open(name, 'a') as f:
        text = " "
        while text != "":
            text = str(input("Enter information into file: "))
            text_tuple = (text, '\n')
            f.writelines(text_tuple)


if __name__ == '__main__':
    print("If You want to stop add information tap 'ENTER' button twice\n")
    save_txt("amazing.txt")
