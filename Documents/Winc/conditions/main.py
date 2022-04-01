# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line

def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_the_cows, Season, Slurry_tank, Grass_status):
    if (Location_of_the_cows == 'pasture' and Time_of_day == 'night') or (Weather == 'rainy'and Location_of_the_cows == 'pasture'):
        return('take cows to cowshed') 
    elif Location_of_the_cows == 'pasture' and Cow_milking_status is True:    
        return('take cows to cowshed\nmilk cows\ntake cows back to pasture') 
    elif Location_of_the_cows == 'cowshed' and Cow_milking_status is True:
        return('milk cows')
    elif Slurry_tank is True and Location_of_the_cows == 'pasture' and Weather !='sunny'and Weather !='windy':   
        return('take cows to cowshed\nfertilize pasture\ntake cows back to pasture') 
    elif Slurry_tank is True and Location_of_the_cows == 'cowshed' and Weather !='sunny'and Weather !='windy':
        return('fertilize pasture')
    elif Grass_status is True and Season == 'spring' and Weather == 'sunny' and Location_of_the_cows == 'pasture':
        return('take cows to cowshed\nmow grass\ntake cows back to pasture') 
    elif Grass_status is True and Season == 'spring' and Weather == 'sunny' and Location_of_the_cows != 'pasture' and Time_of_day == 'day':
        return('mow grass')
    else:
        return('wait')


#farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True)
#farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True)
#farm_action('windy', 'night', True, 'cowshed', 'winter', True, True)
#farm_action('sunny', 'day', True, 'pasture', 'spring', False, True)

