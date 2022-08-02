def celsius_convert(temp: float):
    fahrenheit = 1.8 * temp + 32
    kelvin = 273.15 + temp
    return round(fahrenheit, 2), round(kelvin, 2)


def fahrenheit_convert(temp: float):
    celsius = (temp - 32) * 5 / 9
    kelvin = celsius + 273.15
    return round(celsius, 2), round(kelvin, 2)


def kelvin_convert(temp: float):
    celsius = temp - 273.15
    fahrenheit = celsius * 1.8 + 32
    return round(celsius, 2), round(fahrenheit, 2)


def choice_temp(temp_value: str, temp: float):
    if temp_value != "C" and temp_value != "F" and temp_value != "K":
        raise ValueError("{} -> Unknown command. Try again".format(temp_value))
    match temp_value:
        case "C":
            return (f'{temp} °C equals: {celsius_convert(temp)[0]} °F '
                    f'and {celsius_convert(temp)[1]} °K')
        case "F":
            return (f'{temp} °F equals: {fahrenheit_convert(temp)[0]} °C '
                    f'and {fahrenheit_convert(temp)[1]} °K')
        case "K":
            return (f'{temp} °K equals: {kelvin_convert(temp)[0]} °C '
                    f'and {kelvin_convert(temp)[1]} °F')

# def main():
#     temp_value = str(input("Enter which temperature you want to convert (C or F or K): ").capitalize())
#     temp = float(input("Enter temperature in degrees: "))
#     print(choice_temp(temp_value, temp))
#
#
# if __name__ == '__main__':
#     main()
