"""
    Program will help you to check region of Ukraine auto number. Or check other numbers in the future.
"""

import csv
import re
from transliterate import translit


class AutoCodes:
    """
        Class represent auto numbers
        __________

        Attributes:
        __________
            region: str
                Region of auto number

            old: str
                Old auto number code for region

            new: str
                New auto number code for region
        __________

        Methods:
        __________

        __str__:
            Represent imported auto numbers as string

        __repr__:
            Same as __str__ method
    """
    def __init__(self, region: str, old: str, new: str):
        self.region = region
        self.old = old
        self.new = new

    def __str__(self):
        return f'\n{self.region} {self.old} {self.new}\n'

    def __repr__(self):
        return self.__str__()


class AutocodeList:
    """
        Class create auto code list from csv file
        __________

        Attributes:
        __________
            codes: list
                Create list of AutoCodes from filename.csv

        __________
    """
    def __init__(self):
        self.codes = []

    def import_data(self, filename: str):
        with open(filename, 'r') as f:
            reader = csv.reader(f, dialect='excel')
            next(f)
            for row in reader:
                self.codes.append(AutoCodes(row[0], row[1], row[2]))
            return self.codes


class UARegularExpression(AutocodeList):
    """
        Class check auto number code with regular expression
        __________

        Attributes:
        __________
            auto_code: str
                Auto number code

            latina: str
                Converted auto number code from latina to cyrillic

            codes: list
                List of AutoCodes from AutocodeList class

            pattern: re.compile
                Regular expression for check UA auto number code

        __________

        Methods:
        __________

        latina to cyrilla:
            Method takes inputed code and split it by elements.
            If elements is in Dictionary, replacing them with dict.values() that is cyrillic letters.
            Return converted code that iterate through all others methods.

        check_vehicle_code:
            Method check created code from last method with regular expression.
            If code matching with regular expression, return True.

    """
    translit = {
        "A": "А", "B": "В", "C": "С", "E": "Е", "H": "Н", "I": "І", "K": "К", "M": "М", "O": "О", "P": "Р", "T": "Т",
        "X": "Х"
    }

    def __init__(self, code: str):
        super().__init__()
        self.auto_code = self.latina_to_cyrillic(code)
        self.codes = self.import_data('ua_auto.csv')
        self.pattern = re.compile(r'[АВСЕНІКМОРТХ]{2}(?!0{4})\d{4}[АВСЕНІКМОРТХ]{2}')

    def latina_to_cyrillic(self, code: str):
        var = list(code)
        code = ''
        for element in var:
            if element in self.translit:
                code += self.translit[element]
            else:
                code += element
        return code

    def check_vehicle_code(self):
        if self.pattern.match(self.auto_code):
            return True
        else:
            return False


class UAFindAutoRegion(UARegularExpression):
    """
        Class depends on UARegularExpression class.
        __________

        Method:
        __________
            find_auto_code:
                If code pass regular expression, return string with information about region of Ukraine.
                If code pass, but doesn't exist in AutocodeList, return string with additional information.

    """
    def find_auto_code(self):
        if self.check_vehicle_code() is True:
            for code in self.codes:
                if self.auto_code[:2] in (code.old, code.new):
                    code.region = translit(code.region, 'uk', reversed=True)
                    return f'{self.auto_code} -> is auto code of {code.region}'
            return f'{self.auto_code} -> is not code of any region of Ukraine'
        else:
            return f'{self.auto_code} -> is not Ukrainian auto code'


class UACheckAutoNumber:
    """
        Class starts program. It will check auto number code.
        __________
        \nIf code is correct, it will return string with information about region of Ukraine.
        __________
        \nIf code is incorrect, it will return string with additional information.
        __________
    """
    def __init__(self):
        self.code = str(input('Enter vehicle code: ')).upper().replace(' ', '')
        self.find_number = UAFindAutoRegion(self.code)

    def check_auto_number(self):
        return self.find_number.find_auto_code()


def main():
    exc = UACheckAutoNumber()
    print(exc.check_auto_number())


if __name__ == '__main__':
    main()
