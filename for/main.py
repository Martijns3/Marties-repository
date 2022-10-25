from unicodedata import name
from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"

def shortest_names(countries):

    minimunNameLength = min([len(name) for name in countries])
    #print(minimunWordLength)
    ShortNameList = []
    for name in countries:
        
        if len(name) == minimunNameLength:
            ShortNameList.append(name)
    return ShortNameList






def most_vowels(countries):
    
    #countries_lower = countries #[x.lower() for x in countries]
    most_vowels = sorted(countries, key=lambda country_name: sum(vowel in 'aeiouAEIOU' for vowel in country_name), reverse=True)
    return(most_vowels[ :3])







letters = list("abcdefghijklmnopqrstuvwxyz")

def alphabet_set(countries):
    
    countries_lower = [x.lower() for x in countries]

    countries_most_char = sorted(countries_lower, key=lambda country_name: sum(char in 'abcdefghijklmnopqrstuvwxyz' for char in country_name), reverse=True)
    
            
    alphabet_set = []
    
    for country in countries_most_char:
        for char in letters:
            if char in country:
                letters.remove(char)
                if country not in alphabet_set:
                        alphabet_set.append(country)
   
    return alphabet_set

""" Write your functions here. """

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """

    shortest_names(countries)

    most_vowels(countries)

    alphabet_set(countries)