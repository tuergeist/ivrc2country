# International Vehicle Registration Codes to ISO3166 3-letter Country code converter

Standalone license plate country code converter. 
Based on a International Vehicle Registration Code, i.e., 'D' for Germany, it will return 'DEU' 
as 3-letter ISO3166-1 alpha-3 code.


You may want to use [ISO166 Python lib](https://github.com/deactivated/python-iso3166) to get
the Country's name or numeric code.


## Installation


    $ pip install ivrc2country
    
    
## Usage

    >>> import ivrc2country
    >>> ivrc2country.ivrcodes.get('D')
    IVRCode(ivrc='D', iso3166='DEU')
    
    >>> ivrc2country.ivrc_by_iso3166.get('DEU')
    IVRCode(ivrc='D', iso3166='DEU')
    

### Get political name of the issuing country

    >>> import ivrc2country
    >>> import iso3166
    >>> r = ivrc2country.ivrcodes.get('D')
    >>> iso3166.countries_by_alpha3.get(r.iso3166)
    Country(name='Germany', alpha2='DE', alpha3='DEU', numeric='276', apolitical_name='Germany')


## Keywords

* Länderkennzeichen nach ISO3166-1 Ländercode Konverter
* Autokennzeichen Land
* license plate country converter
* distinguishing signs used on vehicles in international traffic
 