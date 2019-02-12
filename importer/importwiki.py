from pprint import pprint

import pytest
from bs4 import BeautifulSoup
import urllib.request

url = 'https://de.wikipedia.org/wiki/Liste_der_Kfz-Nationalit%C3%A4tszeichen'
url = 'https://de.wikipedia.org/w/index.php?title=Liste_der_Kfz-Nationalit%C3%A4tszeichen&action=edit&section=3'


import re

class SignParser:
    SPECIALS = {
        'Alderney': 'GGY',  # https://www.iso.org/obp/ui/#iso:code:3166:GG
        'Malteserorden': 'MLT',  # is Malta
    }

    def __init__(self, lines: list):
        assert isinstance(lines, list)
        self.lines = lines
        self.regex = re.compile('[^a-zA-Z]')
        self.sign = None
        self.countrycode = None

    def __get_clean_line_parts(self, nr):
        # return [s.replace('*', '').replace(' ', '').replace('{', '').replace('}', '').strip() for s in self.lines[nr].split('|')]
        return [self.regex.sub('', s) for s in self.lines[nr].split('|')]

    def is_not_official(self):
        # if line contains * at the end
        return self.lines[0][-1] == '*'

    def _parse_oneliner(self):

        try:
            parts = self.__get_clean_line_parts(0)
            self.sign = parts[1]
            self.countrycode = parts[3]
        except IndexError:
            print('ERRROR', self.lines)

    def _parse_twoliner(self):
        p0 = self.__get_clean_line_parts(0)
        p1 = self.__get_clean_line_parts(1)
        self.sign = p0[-1]
        self.countrycode = p1[1]

    def _parse_multi(self):
        self._parse_twoliner()

        # map specials
        if self.countrycode in self.SPECIALS:
            self.countrycode = self.SPECIALS[self.countrycode]
        # if there is no countrycode and the sing is not official, skip country
        if self.is_not_official() and len(self.countrycode) != 3:
            self.countrycode = ''


    def parse(self):
        lines = len(self.lines)
        if lines == 1 and self.lines[0]:
            # all in one
            self._parse_oneliner()

        elif lines == 2:
            self._parse_twoliner()

        elif lines > 2:
            self._parse_multi()

        if self.sign:
            return self.sign, self.countrycode



def main():
    local_filename, headers = urllib.request.urlretrieve(url)
    html = open(local_filename, 'r')
    txt = html.read()
    html.close()

    with open('ivrc2country/records.py', 'w') as outfile:
        outfile.write('## auto-generated ##\n')
        outfile.write('from ivrc2country import IVRCode\n')
        outfile.write('\nrecords = [\n')

        start = False
        lines = []
        for line in txt.split('\n'):
            line = line.strip()

            if line.find('{|') == 0:
                start = True
                continue
            if line.find('|}') == 0:
                start = False
                continue

            if not line or line[0] != '|':
                continue

            if start:
                if line == '|-':  # parse old
                    if lines:
                        r = SignParser(lines).parse()
                        print(f"\tIVRCode{r},")
                        outfile.write(f"\tIVRCode{r},\n")
                    lines = []
                else:
                    lines.append(line)
        outfile.write(']\n')
#main()
