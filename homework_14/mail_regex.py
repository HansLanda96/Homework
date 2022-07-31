"""
    The Program allows you to check the correctness of the password.
"""
import re


class Password:
    """
        Class represent password
        __________

        Attributes:
        __________
        password: str
            Inputted password

        pattern: str
            Regex pattern for password
        __________

        Methods:
        __________

        check_pattern:
            Check password with regex pattern. If password is correct, it will return True.\n\n
            Else it will return False.
    """
    def __init__(self):
        self.password = str(input('\nEnter password: '))
        self.pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$\-+=])[a-zA-Z\d@#$\-+=]{8,}$")

    def check_pattern(self):
        if self.pattern.match(self.password):
            return True
        else:
            return False


class PasswordRequirements(Password):
    """
        Class depends on Password class. Check password requirements.
        __________

        Attributes:
        __________
        requirements: dict
            Dictionary with regex patterns as key and requirements name as value.
        __________

        Methods:
        __________

        check_requirements:
            Check password with regex pattern. If password is correct, it will return your inputted password.\n\n
            Else it will return password and report which requirements are not met.
    """
    def __init__(self):
        super().__init__()
        self.requirements = {
            r'(?=.{8,})': 'at least 8 characters',
            r'[a-z]': 'at least 1 lowercase letter',
            r'[A-Z]': 'at least 1 uppercase letter',
            r'\d': 'at least 1 digit',
            r'[$#@%\-+=]': 'at least 1 special symbol ($ # @ % - + =)',

        }
        self.check = self.check_pattern()

    def check_requirements(self):
        if self.check is False:
            for key, value in self.requirements.items():
                if re.search(key, self.password) is None:
                    return f'{self.password} -> must contain {value}'
                else:
                    return f'{self.password} -> have unacceptable characters'
        else:
            return f'Password is correct'


class Execute:
    """
        Class starts validation. If password is correct, it will return your inputted password and program will break.
        Otherwise, it will return password and report which requirements are not met. And program will continue.
    """
    def __init__(self):
        while True:
            password = PasswordRequirements()
            print(password.check_requirements())
            if password.check_requirements() != 'Password is correct':
                continue
            else:
                break


if __name__ == '__main__':
    Execute()
