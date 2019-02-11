# -*- coding: utf-8 -*-

import re
from numbers import Integral
from collections import namedtuple

__all__ = ["ivrcodes"]

# 2.7 comp
try:
    basestring
except NameError:
    basestring = str

IVRCode = namedtuple('IVRCode',
                     'ivrc iso3166 political_name')

_records = [
    IVRCode("D", "DE", u"Germany"),

]


def _build_index(idx):
    return dict((r[idx].upper(), r) for r in _records)


# Internal country indexes
_by_ivrc = _build_index(0)
_by_iso3166 = _build_index(1)
_by_political_name = _build_index(2)

# public use
ivrc_by_code = _by_ivrc
ivrc_by_iso3166 = _by_iso3166
ivrc_by_name = _by_political_name


NOT_FOUND = object()


class _IVRCLookup:

    def get_for_country(self, key, default=NOT_FOUND):
        r = default
        if isinstance(key, basestring):
            r = _by_iso3166.get(key, default)

        if r == NOT_FOUND:
            raise KeyError('No registration code found for Country "%s"', key)

        return r

    def get(self, key, default=NOT_FOUND):
        r = default
        if isinstance(key, basestring):
            r = _by_ivrc.get(key, default)

        if r == NOT_FOUND:
            raise KeyError('No country registered with code "%s"', key)

        return r

    __getitem__ = get

    def __len__(self):
        return len(_records)

    def __iter__(self):
        return iter(_records)

    def __contains__(self, item):
        try:
            self.get(item)
            return True
        except KeyError:
            return False


ivrcodes = _IVRCLookup()