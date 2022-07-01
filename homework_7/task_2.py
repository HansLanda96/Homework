def celsius_convert(temp: float | int):
    fahrenheit = 1.8 * temp + 32
    kelvin = 273.15 + temp
    return fahrenheit, kelvin


def fahrenheit_convert(temp: float | int):
    celsius = (temp - 32) * 5 / 9
    kelvin = celsius + 273.15
    return celsius, kelvin


def kelvin_convert(temp: float | int):
    celsius = temp - 273.15
    fahrenheit = celsius * 1.8 + 32
    return celsius, fahrenheit


def main():
    temp_value = str(input("Enter which temperature you want to convert (C or F or K): ").capitalize())
    temp = float(input("Enter temperature in degrees: "))
    match temp_value:
        case "C":
            print(f'{temp} °C equals: {round(celsius_convert(temp)[0], 2)} °F '
                  f'and {round(celsius_convert(temp)[1], 2)} °K')
        case "F":
            print(f'{temp} °F equals: {round(fahrenheit_convert(temp)[0], 2)} °C '
                  f'and {round(fahrenheit_convert(temp)[1], 2)} °K')
        case "K":
            print(f'{temp} °K equals: {round(kelvin_convert(temp)[0], 2)} °C '
                  f'and {round(kelvin_convert(temp)[1], 2)} °F')
        case _:
            print(f'\n\'{temp_value}\' - Unknown command!')


if __name__ == '__main__':
    main()
