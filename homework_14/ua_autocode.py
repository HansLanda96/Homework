# /^[АВCEHIKMOPTX|ABCEHIKMOPTX]{2}\d{4}[АВCEHIKMOPTX|ABCEHIKMOPTX]{2}$/
import csv
import re


class AutoCodes:
    def __init__(self, region: str, old: str, new: str):
        self.region = region
        self.old = old
        self.new = new

    def __str__(self):
        return f'{self.region} {self.old} {self.new}\n'

    def __repr__(self):
        return self.__str__()


class UAAutocode:
    def __init__(self):
        self.codes = []

    def import_data(self):
        with open('ua_auto.csv', 'r') as f:
            reader = csv.reader(f, dialect='excel')
            next(f)
            for row in reader:
                self.codes.append(AutoCodes(row[0], row[1], row[2]))
            return self.codes


class UARegularExpression(UAAutocode):
    def __init__(self, code: str):
        super().__init__()
        self.vehicle_code = code
        self.codes = self.import_data()
        self.pattern = re.compile(r'[ABCEHIKMOPTX|АВСЕНІКМОРТХ]{2}(?!0{4})\d{4}[ABCEHIKMOPTX|АВСЕНІКМОРТХ]{2}')

    def check_vehicle_code(self):
        if self.pattern.fullmatch(self.vehicle_code):
            return True
        else:
            return False


class FindAutoRegion(UARegularExpression):
    def __init__(self, code: str):
        super().__init__(code)

    def find_vehicle_code(self):
        if self.check_vehicle_code() is True:
            for code in self.codes:
                if self.vehicle_code[:2] in (code.old or code.new):
                    return f'{self.vehicle_code} -> is auto code of {code.region}'
            return f'{self.vehicle_code} -> is not code of any region of Ukraine'
        else:
            return f'{self.vehicle_code} -> is not Ukrainian auto code'


class CheckAutoNumber:
    def __init__(self):
        self.code = str(input('Enter vehicle code: ')).upper()
        # self.ua_autocode = UAAutocode().import_data()
        # self.regular_expression = RegularExpression(self.code)
        # self.vehicle_check = AutoNumCheck(self.code)
        self.find_vehicle = FindAutoRegion(self.code)

    def check_auto_number(self):
        # self.vehicle_check.check_vehicle_code()
        self.find_vehicle.find_vehicle_code()

go = CheckAutoNumber()
print(go.find_vehicle.find_vehicle_code())





#

# codes = UAAutocode().import_data()
# print(codes)
#
#
# codes = UACodes()
# codes.import_codes()
# print(codes.check_region())
 # self.codes[row['Region']] = {'Code 2004': row['Code 2004'], 'Code 2013': row['Code 2013']}
# def __init__(self):
#     self.codes = []
#
#     # import codes from ua_auto.csv
#
#
# def import_codes(self):
#     with open('ua_auto.csv', 'r') as f:
#         codes = csv.reader(f)
#         for row in codes:
#             self.codes.append(row[0], row[1], row[2])
#
#
# def check_code(self):
#     if re.match(r'^[АВCEHIKMOPTX|ABCEHIKMOPTX]{2}\d{4}(?!0{4})[АВCEHIKMOPTX|ABCEHIKMOPTX]{2}$', self.code):
#         return True
#     else:
#         return False
#
#     # if code True check region in  self.codes
#
#
# def check_region(self):
#     if self.check_code():
#         if self.code[0:2] in self.codes['Region'].values():
#             return self.codes['Region']
#         else:
#             return False