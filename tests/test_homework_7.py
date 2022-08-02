from unittest import TestCase, main
from homework_7.task_2 import celsius_convert, fahrenheit_convert, kelvin_convert, choice_temp


class TestTemperatureConvert(TestCase):
    def test_celsius_convert(self):
        self.assertEqual(celsius_convert(-100), (-148, 173.15))

    def test_fahrenheit_convert(self):
        self.assertEqual(fahrenheit_convert(-100), (-73.33, 199.82))

    def test_kelvin_convert(self):
        self.assertEqual(kelvin_convert(-100), (-373.15, -639.67))

    def test_choice_temp(self):
        self.assertEqual(choice_temp("C", 78), '78 °C equals: 172.4 °F and 351.15 °K')
        self.assertEqual(choice_temp("F", 451), '451 °F equals: 232.78 °C and 505.93 °K')
        self.assertEqual(choice_temp("K", 1500), '1500 °K equals: 1226.85 °C and 2240.33 °F')

    def test_choice_temp_wrong_value(self):
        with self.assertRaises(ValueError) as e:
            choice_temp("X", 0)
        self.assertEqual('X -> Unknown command. Try again', e.exception.args[0])


if __name__ == '__main__':
    main()
