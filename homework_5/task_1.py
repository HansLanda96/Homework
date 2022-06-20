from homework_4.task_2 import input_number as inp


def is_prime(num: int) -> bool:
    if num > 1:
        for number in range(2, num):
            if (num % number) == 0:
                return False
        return True


def main():
    your_number = inp("Insert number from 0 to 1000: ")
    if your_number > 1000 or your_number < 0:
        print(f'\nNumber {your_number} is out of scope')
    elif is_prime(your_number):
        print(f'\n{is_prime(your_number)}'
              f'\nNumber {your_number} is prime')
    else:
        print(f'\n{is_prime(your_number)}'
              f'\nNumber {your_number} is not prime')


if __name__ == '__main__':
    main()
