# -*- coding: utf-8 -*-

import unittest

import ivrc2country


class TestIVRCListings(unittest.TestCase):
    def test_all_codes(self):
        codelist = ivrc2country.ivrcodes
        self.assertTrue(len(codelist) > 100)

    def test_by_iso(self):
        table = ivrc2country.ivrc_by_iso3166

        self.assertEqual(table["DEU"].ivrc, "D")
        self.assertTrue(len(table) > 100)
