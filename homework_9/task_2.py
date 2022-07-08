"""
Mail hider
"""


def sneaky_mail(email: str) -> str:
    name, domain = email.split('@')
    return f'Your hidden email: {name[:-3]}***@**{domain[2:]}'


if __name__ == '__main__':
    try:
        print(sneaky_mail("VasyaVoron@hillel.com"))
    except ValueError:
        print("Enter the valid email. You miss '@' sign")


# This func will count amount of letters and change them to "*"
# Also func separate domain name and domain tail
#
#
# def sneaky_mail(email: str) -> str:
#     email = email[0:2] + "*" * (len(email) - 3) + email[-1]
#     return email
#
#
# def asterisk_mail(email: str) -> str:
#     name, domain = email.split("@")
#     dom_name, dom_tail = domain.split(".")
#     name = sneaky_mail(name)
#     dom_name = sneaky_mail(dom_name)
#     return f'{name}@{dom_name}.{dom_tail}'
#
#
# if __name__ == '__main__':
#     try:
#         print(asterisk_mail("VasyaVoron@hillel.com"))
#     except ValueError:
#         print("Enter the valid email. You miss '@' sign")
