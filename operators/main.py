# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line
most_spoken_language_spain = 'Castilian'
most_spoken_language_switserland = 'German'
print(most_spoken_language_switserland == most_spoken_language_spain)

most_prevalent_religion_spain = 'Roman Catholic'
most_prevalent_religion_switserland = 'Roman Catholic'
print(most_prevalent_religion_switserland is most_prevalent_religion_spain)

capital_spain = 'Madrid'
capital_switserland ='Bern'
print(len(capital_spain) != (len(capital_switserland)))

GDP_spain = 1714860000000
GDP_switserland = 590710000000
print(GDP_switserland > GDP_spain)

population_growth_perecentage_switserland = 0.65
population_growth_percentag_spain = -0.03
print(population_growth_percentag_spain and population_growth_perecentage_switserland < 1)

population_count_spain = 47260584
population_count_switserland = 8453550
print((population_count_spain or population_count_spain) > 10000000)

#print((population_count_spain or population_count_switserland) == 10000000)
#Exactly one of the two countries has a population count of over 10 million.
print((population_count_spain > 10000000)^(population_count_switserland>10000000) )