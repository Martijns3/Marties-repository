# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line
countries = get_countries()
from datetime import date


def create_passport(name,date_of_birth,place_of_birth,height,nationality):
    
    try:
        date.fromisoformat(date_of_birth)
    except ValueError:
        date_of_birth = ("Invalid isoformat date")

    nationality_list = []
    if nationality.capitalize() in countries:
        nationality_list.append(countries[(countries.index(nationality.capitalize()))])
    else:
        nationality_list.append('country not found')
        
    passport = dict([
        ('name',name),
        ('date_of_birth',date_of_birth),
        ('place_of_birth',place_of_birth),
        ('height',height),
        ('nationality', str(nationality_list[0]))
        # ('nationality',str(countries[(countries.index(nationality))]))
        ])
    return passport
    
    
create_passport('Martijn Spierenburg','1975-01-30','Rotterdam','1.93','Netherlands')



# ----------------------------------------------------------------------------------------------------------------------------
passport_data = {'name': 'Martijn Spierenburg', 
                 'date_of_birth': '1975-30-01', 
                 'place_of_birth': 'Rotterdam', 
                 'height': '1.93', 
                 'nationality': 'Netherlands' }

def add_stamp(passport_data, country) : 
      
    if 'stamps' not in passport_data:
        passport_data['stamps'] = []
    if country.capitalize() not in passport_data['stamps']:
            if passport_data['nationality'] != country.capitalize(): 
                passport_data['stamps'].append(country.capitalize())
    return(passport_data)



add_stamp(passport_data, 'japan')
print(passport_data)

add_stamp(passport_data, 'netherlands')
print(passport_data)

add_stamp(passport_data, 'belgium')
print(passport_data)

add_stamp(passport_data, 'germany')
print(passport_data)

add_stamp(passport_data, 'germany')
print(passport_data)
# ----------------------------------------------------------------------------------------------------------------------------

martijn = {'name': 'Martijn Spierenburg', 
                 'date_of_birth': '1975-30-01', 
                 'place_of_birth': 'Rotterdam', 
                 'height': '1.93', 
                 'nationality': 'Netherlands' }

def add_biometric_data(martijn, biometric_type, biometric_value, date_added) : 
    
    try:
        date.fromisoformat(str(date_added))
    except ValueError:
        date_added = ("Invalid isoformat date")
    biometric_data = {'date' : date_added, 'value' : biometric_value}
    if 'biometric' not in martijn:
        martijn['biometric'] = {}
    if biometric_type not in martijn['biometric']:
            martijn['biometric'][biometric_type]= biometric_data
    else:
        martijn['biometric'][biometric_type]= biometric_data
    return martijn



add_biometric_data(martijn, 'eye left', 'blue', '2022-11-30')
print(martijn)

add_biometric_data(martijn, 'eye right', 'blue', '2022-12-01')
print(martijn)

add_biometric_data(martijn, 'eye right', 'brown', '2022-12-02')
print(martijn)

fingerprint_data = {
    "left_pinky": "2378945",
    "left_ring": "2349081",
    "left_middle": "132890",
    "left_index": "9823234",
    "left_thumb": "0924131",
    "right_thumb": "6234923",
    "right_index": "13249734",
    "right_middle": "34023784",
    "right_ring": "12332538",
    "right_pinky": "32458970",
}
add_biometric_data(martijn,'fingerprints',fingerprint_data, '2022-12-02')
print(martijn)

