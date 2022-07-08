"""
Mail hider
"""


def sneaky_mail(email: str) -> str:
    name, domain = email.split('@')
    return f'Your hidden email: {name[:-3]}***@**{domain[2:]}'


if __name__ == '__main__':
    try:
        print(sneaky_mail("VasyaVoron@gmail.com"))
    except ValueError:
        print("Enter the valid email. You miss '@' sign")
