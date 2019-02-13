__all__ = ["ivrcodes"]

from collections import namedtuple

IVRCode = namedtuple('IVRCode',
                     'ivrc iso3166')  # 3-letter iso3166-1
records = [
	IVRCode('A', 'AUT'),
	IVRCode('AFG', 'AFG'),
	IVRCode('AG', 'ATG'),
	IVRCode('AL', 'ALB'),
	IVRCode('AND', 'AND'),
	IVRCode('ANG', 'AGO'),
	IVRCode('AM', 'ARM'),
	IVRCode('ARU', 'ABW'),
	IVRCode('AUS', 'AUS'),
	IVRCode('AX', 'ALA'),
	IVRCode('AXA', 'AIA'),
	IVRCode('AZ', 'AZE'),
	IVRCode('B', 'BEL'),
	IVRCode('BD', 'BGD'),
	IVRCode('BDS', 'BRB'),
	IVRCode('BF', 'BFA'),
	IVRCode('BG', 'BGR'),
	IVRCode('BHT', 'BTN'),
	IVRCode('BIH', 'BIH'),
	IVRCode('BJ', 'BEN'),
	IVRCode('BOL', 'BOL'),
	IVRCode('BR', 'BRA'),
	IVRCode('BRN', 'BHR'),
	IVRCode('BRU', 'BRN'),
	IVRCode('BS', 'BHS'),
	IVRCode('BVI', 'VGB'),
	IVRCode('BW', 'BWA'),
	IVRCode('BY', 'BLR'),
	IVRCode('BZ', 'BLZ'),
	IVRCode('C', 'CUB'),
	IVRCode('CAM', 'CMR'),
	IVRCode('CDN', 'CAN'),
	IVRCode('CGO', 'COD'),
	IVRCode('CH', 'CHE'),
	IVRCode('CHN', 'CHN'),
	IVRCode('CI', 'CIV'),
	IVRCode('CL', 'LKA'),
	IVRCode('CO', 'COL'),
	IVRCode('COM', 'COM'),
	IVRCode('CR', 'CRI'),
	IVRCode('CV', 'CPV'),
	IVRCode('CY', 'CYP'),
	IVRCode('CZ', 'CZE'),
	IVRCode('D', 'DEU'),
	IVRCode('DJI', 'DJI'),
	IVRCode('DK', 'DNK'),
	IVRCode('DOM', 'DOM'),
	IVRCode('DZ', 'DZA'),
	IVRCode('E', 'ESP'),
	IVRCode('EAK', 'KEN'),
	IVRCode('EAT', 'TZA'),
	IVRCode('EAU', 'UGA'),
	IVRCode('EC', 'ECU'),
	IVRCode('ER', 'ERI'),
	IVRCode('ES', 'SLV'),
	IVRCode('EST', 'EST'),
	IVRCode('ET', 'EGY'),
	IVRCode('ETH', 'ETH'),
	IVRCode('F', 'FRA'),
	IVRCode('FIN', 'FIN'),
	IVRCode('FJI', 'FJI'),
	IVRCode('FL', 'LIE'),
	IVRCode('FO', 'FRO'),
	IVRCode('FSM', 'FSM'),
	IVRCode('G', 'GAB'),
	IVRCode('GB', 'GBR'),
	IVRCode('GBA', 'GGY'),
	IVRCode('GBG', 'GGY'),
	IVRCode('GBJ', 'JEY'),
	IVRCode('GBM', 'IMN'),
	IVRCode('GBZ', 'GIB'),
	IVRCode('GCAGT', 'GTM'),
	IVRCode('GE', 'GEO'),
	IVRCode('GH', 'GHA'),
	IVRCode('GQ', 'GNQ'),
	IVRCode('GR', 'GRC'),
	IVRCode('GUB', 'GNB'),
	IVRCode('GUI', 'GIN'),
	IVRCode('GUY', 'GUY'),
	IVRCode('H', 'HUN'),
	IVRCode('HK', 'HKG'),
	IVRCode('HN', 'HND'),
	IVRCode('HR', 'HRV'),
	IVRCode('I', 'ITA'),
	IVRCode('IL', 'ISR'),
	IVRCode('IND', 'IND'),
	IVRCode('IR', 'IRN'),
	IVRCode('IRL', 'IRL'),
	IVRCode('IRQ', 'IRQ'),
	IVRCode('IS', 'ISL'),
	IVRCode('J', 'JPN'),
	IVRCode('JA', 'JAM'),
	IVRCode('JOR', 'JOR'),
	IVRCode('K', 'KHM'),
	IVRCode('KAN', 'KNA'),
	IVRCode('KG', 'KGZ'),
	IVRCode('KIR', 'KIR'),
	IVRCode('KN', 'GRL'),
	IVRCode('KP', 'PRK'),
	IVRCode('KSA', 'SAU'),
	IVRCode('KWT', 'KWT'),
	IVRCode('KZ', 'KAZ'),
	IVRCode('L', 'LUX'),
	IVRCode('LAO', 'LAO'),
	IVRCode('LAR', 'LBY'),
	IVRCode('LB', 'LBR'),
	IVRCode('LS', 'LSO'),
	IVRCode('LT', 'LTU'),
	IVRCode('LV', 'LVA'),
	IVRCode('M', 'MLT'),
	IVRCode('MA', 'MAR'),
	IVRCode('MAL', 'MYS'),
	IVRCode('MC', 'MCO'),
	IVRCode('MD', 'MDA'),
	IVRCode('MEX', 'MEX'),
	IVRCode('MGL', 'MNG'),
	IVRCode('MH', 'MHL'),
	IVRCode('MK', 'MKD'),
	IVRCode('MNE', 'MNE'),
	IVRCode('MOC', 'MOZ'),
	IVRCode('MS', 'MUS'),
	IVRCode('MV', 'MDV'),
	IVRCode('MW', 'MWI'),
	IVRCode('MYA', 'MMR'),
	IVRCode('N', 'NOR'),
	IVRCode('NA', 'ANT'),
	IVRCode('NAM', 'NAM'),
	IVRCode('NAU', 'NRU'),
	IVRCode('NCL', 'NCL'),
	IVRCode('NEP', 'NPL'),
	IVRCode('NGR', 'NGA'),
	IVRCode('NI', 'NIR'),
	IVRCode('NIC', 'NIC'),
	IVRCode('NL', 'NLD'),
	IVRCode('NZ', 'NZL'),
	IVRCode('OM', 'OMN'),
	IVRCode('P', 'PRT'),
	IVRCode('PA', 'PAN'),
	IVRCode('PAL', 'PLW'),
	IVRCode('PE', 'PER'),
	IVRCode('PK', 'PAK'),
	IVRCode('PL', 'POL'),
	#IVRCode('PMR', ''),  # Transnistrien unofficial
	IVRCode('PNG', 'PNG'),
	IVRCode('PRI', 'PRI'),
	IVRCode('PY', 'PRY'),
	IVRCode('Q', 'QAT'),
	IVRCode('RA', 'ARG'),
	IVRCode('RB', 'BWA'),
	IVRCode('RC', 'TWN'),
	IVRCode('RCA', 'CAF'),
	IVRCode('RCB', 'COG'),
	IVRCode('RCH', 'CHL'),
	IVRCode('RG', 'GIN'),
	IVRCode('RH', 'HTI'),
	IVRCode('RI', 'IDN'),
	IVRCode('RIM', 'MRT'),
	IVRCode('RKS', 'KOS'),
	IVRCode('RL', 'LBN'),
	IVRCode('RM', 'MDG'),
	IVRCode('RMM', 'MLI'),
	IVRCode('RN', 'NER'),
	IVRCode('RO', 'ROU'),
	IVRCode('ROK', 'KOR'),
	IVRCode('RUM', 'ROU'),
	IVRCode('ROU', 'URY'),
	IVRCode('RP', 'PHL'),
	IVRCode('RSM', 'SMR'),
	IVRCode('RT', 'TGO'),
	IVRCode('RU', 'BDI'),
	IVRCode('RUS', 'RUS'),
	IVRCode('RWA', 'RWA'),
	IVRCode('S', 'SWE'),
	IVRCode('SD', 'SWZ'),
	IVRCode('SGP', 'SGP'),
	IVRCode('SK', 'SVK'),
	IVRCode('SLE', 'SLE'),
	IVRCode('SLO', 'SVN'),
	IVRCode('SME', 'SUR'),
	IVRCode('SMOM', 'MLT'),
	IVRCode('SN', 'SEN'),
	IVRCode('SO', 'SOM'),
	IVRCode('SOL', 'SLB'),
	IVRCode('SRB', 'SRB'),
	IVRCode('SSD', 'SSD'),
	IVRCode('STP', 'STP'),
	IVRCode('SUD', 'SDN'),
	IVRCode('SY', 'SYC'),
	IVRCode('SYR', 'SYR'),
	IVRCode('T', 'THA'),
	IVRCode('TD', 'TCD'),
	IVRCode('TG', 'TGO'),
	IVRCode('TJ', 'TJK'),
	IVRCode('TL', 'TLS'),
	IVRCode('TM', 'TKM'),
	IVRCode('TN', 'TUN'),
	IVRCode('TON', 'TON'),
	IVRCode('TR', 'TUR'),
	IVRCode('TT', 'TTO'),
	IVRCode('TUV', 'TUV'),
	IVRCode('UA', 'UKR'),
	IVRCode('UAE', 'ARE'),
	IVRCode('USA', 'USA'),
	IVRCode('UZ', 'UZB'),
	IVRCode('V', 'VAT'),
	IVRCode('VAN', 'VUT'),
	IVRCode('VG', 'VGB'),
	IVRCode('VN', 'VNM'),
	IVRCode('WAG', 'GMB'),
	IVRCode('WAL', 'SLE'),
	IVRCode('WB', 'PSE'),
	IVRCode('WD', 'DMA'),
	IVRCode('WG', 'GRD'),
	IVRCode('WL', 'LCA'),
	IVRCode('WS', 'WSM'),
	IVRCode('WSA', 'ESH'),
	IVRCode('WV', 'VCT'),
	IVRCode('YEM', 'YEM'),
	IVRCode('YV', 'VEN'),
	IVRCode('Z', 'ZMB'),
	IVRCode('ZA', 'ZAF'),
]


def _build_index(idx):
    return dict((r[idx].upper(), r) for r in records)


# Internal country indexes
_by_ivrc = _build_index(0)
_by_iso3166 = _build_index(1)


# public use
ivrc_by_code = _by_ivrc
ivrc_by_iso3166 = _by_iso3166


NOT_FOUND = object()


class _IVRCLookup:

    def get_for_country(self, key, default=NOT_FOUND):
        r = default
        if isinstance(key, str):
            r = _by_iso3166.get(key, default)

        if r == NOT_FOUND:
            raise KeyError('No registration code found for Country "%s"', key)

        return r

    def get(self, key, default=NOT_FOUND):
        r = default
        if isinstance(key, str):
            r = _by_ivrc.get(key, default)

        if r == NOT_FOUND:
            raise KeyError('No country registered with code "%s"', key)

        return r

    __getitem__ = get

    def __len__(self):
        return len(records)

    def __iter__(self):
        return iter(records)

    def __contains__(self, item):
        try:
            self.get(item)
            return True
        except KeyError:
            return False

ivrcodes = _IVRCLookup()