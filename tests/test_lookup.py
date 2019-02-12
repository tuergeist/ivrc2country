import unittest

from ivrc2country import ivrcodes


class TestIVRCLookup(unittest.TestCase):
    def test_germany(self):
        r = ivrcodes.get('D')
        self.assertEqual(r.iso3166, 'DEU')

    def test_germany_reverse(self):
        r = ivrcodes.get_for_country('DEU')
        self.assertEqual(r.ivrc, 'D')

    def test_no_match(self):
        missing_key = 'NONEXISTING'
        try:
            r = ivrcodes.get(missing_key)
        except KeyError as e:
            self.assertTrue(missing_key in str(e))

    def test_no_match_reverse(self):
        missing_key = 'NONEXISTING'
        try:
            r = ivrcodes.get_for_country(missing_key)
        except KeyError as e:
            self.assertTrue(missing_key in str(e))

