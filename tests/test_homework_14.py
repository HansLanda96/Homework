from unittest import TestCase, main
from homework_14.phone_regex import UAPhoneNumber, UAOperatorPatterns


class TestPhoneRegex(TestCase):
    def setUp(self):
        self.number = '066---515---395---5'
        self.phone_number = UAPhoneNumber(self.number)
        self.operator_patterns = UAOperatorPatterns(self.number)
        self.formatted_number = self.phone_number.format_ua_num()

    def test_UAPhoneNumber_class1(self):
        self.assertEqual(self.phone_number.ua_number, '0665153955')
        self.assertEqual(self.formatted_number, '(+38) 066 515-39-55')

    def test_UAPhoneNumber_class2(self):
        self.number = '12451205980000'
        self.assertEqual(UAPhoneNumber(self.number).ua_number, '12451205980000')
        self.assertEqual(UAPhoneNumber(self.number).format_ua_num(), '12451205980000')

    def test_UAPhoneNumber_class3(self):
        self.number = 'dlfjgjdlkfg'
        self.assertEqual(UAPhoneNumber(self.number).ua_number, '')
        self.assertEqual(UAPhoneNumber(self.number).format_ua_num(), '')

    def test_UAOperatorPatterns_Vodafone(self):
        self.assertEqual(self.operator_patterns.ua_number, '0665153955')
        self.assertEqual(self.operator_patterns.formatted_ua, '(+38) 066 515-39-55')
        self.assertEqual(
            self.operator_patterns.check_cellular_number(), '\n(+38) 066 515-39-55 -> Phone number is Vodafone'
        )

    def test_UAOperatorPatterns_Kyivstar(self):
        self.number = '$$$(067++++5--1---539----55)$$$'
        self.assertEqual(UAOperatorPatterns(self.number).ua_number, '0675153955')
        self.assertEqual(UAOperatorPatterns(self.number).formatted_ua, '(+38) 067 515-39-55')
        self.assertEqual(
            UAOperatorPatterns(self.number).check_cellular_number(), '\n(+38) 067 515-39-55 -> Phone number is Kyivstar'
        )

    def test_UAOperatorPattern_Lifecell(self):
        self.number = 'dflsdjfsdfl;jk063-----5153955'
        self.assertEqual(UAOperatorPatterns(self.number).ua_number, '0635153955')
        self.assertEqual(UAOperatorPatterns(self.number).formatted_ua, '(+38) 063 515-39-55')
        self.assertEqual(
            UAOperatorPatterns(self.number).check_cellular_number(), '\n(+38) 063 515-39-55 -> Phone number is Lifecell'
        )

    def test_UAOperatorPattern_UA_not_recognized(self):
        self.number = 'ssdlfsgsjhlkg 023-515-39-55'
        self.assertEqual(UAOperatorPatterns(self.number).ua_number, '0235153955')
        self.assertEqual(UAOperatorPatterns(self.number).formatted_ua, '(+38) 023 515-39-55')
        self.assertEqual(
            UAOperatorPatterns(self.number).check_cellular_number(),
            '\n(+38) 023 515-39-55 -> UA mobile operator is not recognized'
        )

    def test_UAOperatorPattern_not_recognized(self):
        self.number = 'ssdlfsgsjhlkg 1251235235235235'
        self.assertEqual(UAOperatorPatterns(self.number).ua_number, '1251235235235235')
        self.assertEqual(UAOperatorPatterns(self.number).formatted_ua, 'ssdlfsgsjhlkg 1251235235235235')
        self.assertEqual(
            UAOperatorPatterns(self.number).check_cellular_number(), '\nFailed to recognize phone number')


if __name__ == '__main__':
    main()
