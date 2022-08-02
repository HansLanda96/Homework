"""
    Program allows you to format UA phone numbers and check operator of number.
"""
import re


class UAPhoneNumber:
    """
        Class represent UA phone number
        __________

        Attributes:
        __________
            phone_number: str
                Inputted phone number

            ua_number: str
                UA number without non-digits characters

            formatted_ua: str
                Formatted UA number with needed parameters
        __________

        Methods:
        __________

        format_ua_num:
            If inputted phone number is less than 13 digits, it will be formatted.
            Else it will be returned as is.
    """
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.ua_number = re.sub(r'\D', '', self.phone_number)
        self.formatted_ua = self.format_ua_num()

    def format_ua_num(self):
        if len(self.ua_number) < 13:
            format_phone = re.sub(r"^(.*?)(0\d{2})(\d{3})(\d{2})(\d{2})$", r"(+38) \2 \3-\4-\5", self.ua_number)
            return format_phone
        else:
            return self.phone_number

    # def __str__(self):
    #     return f'\nInput number: {self.phone_number}' \
    #             f'\nFormatted number: {self.formatted_ua}'    Use if you want to print formatted number
    #
    # def __repr__(self):
    #     return self.__str__()


class UAOperatorPatterns(UAPhoneNumber):
    """
        Class depends on UAPhoneNumber class. Check operator of inputted number.
        __________

        Attributes:
        __________
        operators: dict
            Dictionary with regex patterns as key and operators name as value.
        __________

        Methods:
        __________
        check_cellular_number:
            If inputted number pass formatting rules, it will be checked.
            Else it will be not recognized as UA phone number and will be not formatted.
    """
    def __init__(self, phone_number: str):
        super().__init__(phone_number)
        self.operators = {
            r'^(?:(\+)?38)?(0(66|95|99)\d{7})$': 'Vodafone',
            r'^(?:(\+)?38)?(0(67|68|96|97|98)\d{7})$': 'Kyivstar',
            r'^(?:(\+)?38)?(0[679]3\d{7})$': 'Lifecell'
        }

    def check_cellular_number(self):
        if self.formatted_ua is not self.phone_number:
            for regex, operator in self.operators.items():
                if re.match(regex, self.ua_number):
                    return f'\n{self.formatted_ua} -> Phone number is {operator}'
            else:
                return f'\n{self.formatted_ua} -> UA mobile operator is not recognized'
        else:
            return '\nFailed to recognize phone number'


# if __name__ == '__main__':
#     number_string = str(input('Enter phone number: '))
#     number = UAPhoneNumber(number_string)
#     exc = UAOperatorPatterns(number_string)
#     print(exc.check_cellular_number())

