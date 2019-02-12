from importer.importwiki import SignParser


def test_parse_line():
    sp = SignParser(['|ARU* ||{{ABW}} ||AW || || ||'])
    assert sp.parse() == ('ARU', 'ABW')

def test_parse_other_line():
    assert SignParser(['| AXA | | {{AIA}} | | AI | | | | | |']).parse() == ('AXA', 'AIA')

def test_two_liner():
    indata = ["|[[Kfz-Kennzeichen (Österreich)|A]]", "|{{AUT}} ||AT ||1910 || ||[[Austria|'''A'''ustria]] ({{laS}})"]
    assert SignParser(indata).parse() == ('A', 'AUT')

def test_other_two_liner():
    indata = ["|[[Kfz-Kennzeichen (Afghanistan)|AFG]]", "|{{AFG}} ||AF ||1971 || ||"]
    assert SignParser(indata).parse() == ('AFG', 'AFG')

def test_multiliner():
    indata = ["| [[Kfz - Kennzeichen(Belgien) | B]]", "| {{BEL}}" ,"| BE", "| 1910", "|", "|"]
    assert SignParser(indata).parse() == ('B', 'BEL')

def test_other_multiliner():
    indata = ["|BRU", "|{{BRN}}", "|BN", "|1956","|", "|"]
    assert SignParser(indata).parse() == ('BRU', 'BRN')

def test_missing_country():
    indata = ["|[[Kfz-Kennzeichen (Kronbesitzungen der britischen Krone)#Alderney|GBA]]", "|[[Alderney]]", "|",
              "|1924", "|", "|'''G'''reat '''B'''ritain '''A'''lderney (englisch)" ]
    assert SignParser(indata).parse() == ('GBA', 'GGY')

def test_missing_and_not_official():
    indata = ["| [[Kfz - Kennzeichen(Transnistrien) | PMR]] *", "| [[Transnistrien]]", "|" ]  # skipped useless data
    assert SignParser(indata).parse() == ('PMR', '')

def test_no_data():
    assert SignParser([]).parse() is None

    try:
        SignParser(None).parse() is None
        assert False == 'shall raise Assertion error'
    except AssertionError:
        pass

