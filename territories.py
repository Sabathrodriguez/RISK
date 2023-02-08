#enum representing all territories in the Game Risk

from enum import Enum

class Territories(Enum):
    #NORTH AMERICA
    ALASKA = ['ALASKA', 'NORTH AMERICA']
    NORTH_WESTERN_TERRITORY = ['NORTH WESTERN TERRITORY', 'NORTH AMERICA']
    GREENLAND = ['GREENLAND', 'NORTH AMERICA']
    ALBERTA = ['ALBERTA', 'NORTH AMERICA']
    ONTARIO = ['ONTARIO', 'NORTH AMERICA']
    QUEBEC = ['QUEBEC', 'NORTH AMERICA']
    WESTERN_UNITED_STATES = ['WESTERN UNITED STATES', 'NORTH AMERICA']
    EASTERN_UNITED_STATES = ['EASTERN UNITED STATES', 'NORTH AMERICA']
    CENTRAL_AMERICA = ['CENTRAL AMERICA', 'NORTH AMERICA']

    #SOUTH AMERICA
    VENEZUELA = ['VENEZUELA', 'SOUTH AMERICA']
    BRAZIL = ['BRAZIL', 'SOUTH AMERICA']
    PERU = ['PERU', 'SOUTH AMERICA']
    ARGENTINA = ['ARGENTINA', 'SOUTH AMERICA']

    #EUROPE
    ICELAND = ['ICELAND', 'EUROPE']
    SCANDINAVIA = ['SCANDINAVIA', 'EUROPE']
    UKRAINE = ['UKRAINE', 'EUROPE']
    GREAT_BRITAIN = ['GREAT BRITAIN', 'EUROPE']
    NORTHERN_EUROPE = ['NORTHERN EUROPE', 'EUROPE']
    WESTERN_EUROPE = ['WESTERN EUROPE', 'EUROPE']
    SOUTHERH_EUROPE = ['SOUTHERN_EUROPE', 'EUROPE']

    #AFRICA
    NORTH_AFRICA = ['NORTH AFRICA', 'AFRICA']
    EGYPT = ['EGPYT', 'AFRICA']
    CONGO = ['CONGO', 'AFRICA']
    EAST_AFRICA = ['EAST AFRICA', 'AFRICA']
    SOUTH_AFRICA = ['SOUTH AFRICA', 'AFRICA']
    MADAGASCAR = ['MADAGASCAR', 'AFRICA']

    #ASIA
    SIBERIA = ['SIBERIA', 'ASIA']
    YAKUTSK = ['YAKUTSK', 'ASIA']
    IRKUTSK = ['IRKUTSK', 'ASIA']
    KAMCHATKA = ['KAMCHATKA', 'ASIA']
    URAL = ['URAL', 'ASIA']
    MONGOLIA = ['MONGOLIA', 'ASIA']
    JAPAN = ['JAPAN', 'ASIA']
    AFGHANISTAN = ['AFGHANISTAN', 'ASIA']
    CHINA = ['CHINA', 'ASIA']
    MIDDLE_EAST = ['MIDDLE EAST', 'ASIA']
    INDIA = ['INDIA', 'ASIA']
    SLAM = ['SLAM', 'ASIA']

    #AUSTRALIA
    INDONESIA = ['INDONESIA', 'AUSTRALIA']
    NEW_GUINEA = ['NEW GUINEA', 'AUSTRALIA']
    WESTERN_AUSTRALIA = ['WESTERN AUSTRALIA', 'AUSTRALIA']
    EASTERN_AUSTRALIA = ['EASTERN_AUSTRALIA', 'AUSTRALIA']