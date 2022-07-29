import csv
import re


class AutoCodes:
    def __init__(self, region: str, old: str, new: str):
        self.region = region
        self.old = old
        self.new = new

    def __str__(self):
        return f'\n{self.region} {self.old} {self.new}\n'

    def __repr__(self):
        return self.__str__()


class AutocodeList:
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
    translit = {
        "A": "А", "B": "В", "C": "С", "E": "Е", "H": "Н", "I": "І", "K": "К", "M": "М", "O": "О", "P": "Р", "T": "Т",
        "X": "Х"
    }

    def __init__(self, code: str):
        super().__init__()
        self.auto_code = code
        self.latina = self.latina()
        self.codes = self.import_data('ua_auto.csv')
        self.pattern = re.compile(r'[АВСЕНІКМОРТХ]{2}(?!0{4})\d{4}[АВСЕНІКМОРТХ]{2}')

    def latina(self):
        var = list(self.auto_code)
        code_ua = ''
        for letter in var:
            if letter in self.translit:
                code_ua += self.translit[letter]
            else:
                code_ua += letter
        return code_ua

    def check_vehicle_code(self):
        if self.pattern.match(self.latina):
            return True
        else:
            return False


class UAFindAutoRegion(UARegularExpression):
    def find_auto_code(self):
        if self.check_vehicle_code() is True:
            for code in self.codes:
                if self.latina[:2] in (code.old, code.new):
                    return f'{self.latina} -> is auto code of {code.region}'
            return f'{self.latina} -> is not code of any region of Ukraine'
        else:
            return f'{self.latina} -> is not Ukrainian auto code'


class UACheckAutoNumber:
    def __init__(self):
        self.code = str(input('Enter vehicle code: ')).upper()
        self.find_number = UAFindAutoRegion(self.code)

    def check_auto_number(self):
        return self.find_number.find_auto_code()


def main():
    check_auto = UACheckAutoNumber()
    print(check_auto.check_auto_number())


if __name__ == '__main__':
    main()
