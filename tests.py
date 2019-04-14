import unittest

from format_price import format_price


class FormatPriceTestCase(unittest.TestCase):
    def test_returns_price_for_intstr(self):
        pretty_price = format_price('123456789')
        self.assertEqual(pretty_price, '123 456 789')


    def test_returns_price_for_floatstr(self):
        pretty_price = format_price('12345.6789')
        self.assertEqual(pretty_price, '12 345.68')


    def test_returns_price_for_neg_intstr(self):
        pretty_price = format_price('-123456789')
        self.assertEqual(pretty_price, '-123 456 789')


    def test_returns_price_for_neg_floatstr(self):
        pretty_price = format_price('-12345.6789')
        self.assertEqual(pretty_price, '-12 345.68')


    def test_returns_none_for_nondigit(self):
        pretty_price = format_price('1.1a')
        self.assertIsNone(pretty_price)


    def test_returns_none_for_none(self):
        pretty_price = format_price(None)
        self.assertIsNone(pretty_price)


    def test_returns_none_for_object(self):
        pretty_price = format_price([1])
        self.assertIsNone(pretty_price)


    def test_returns_price_for_exponential(self):
        pretty_price = format_price('123456789e-3')
        self.assertEqual(pretty_price, '123 456.79')


if __name__ == '__main__':
    unittest.main()
