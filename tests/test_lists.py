# -*- coding: utf-8 -*-

import unittest

import iso3166

import ivrc2country


class TestIVRCListings(unittest.TestCase):
    def test_all_codes(self):
        codelist = ivrc2country.ivrcodes
        self.assertTrue(len(codelist) > 100)

    def test_by_iso(self):
        table = ivrc2country.ivrc_by_iso3166

        self.assertEqual(table["DEU"].ivrc, "D")
        self.assertTrue(len(table) > 100)

    def test_iso3_is_3letter_only(self):
        table = ivrc2country.ivrcodes
        for pair in table:
            self.assertTrue(len(pair[1]) == 3, pair)

    def test_is_valid_iso3166_1alpha3(self):
        table = ivrc2country.ivrcodes
        for pair in table:
            self.assertIsNotNone(iso3166.countries_by_alpha3.get(pair[1]), pair)
