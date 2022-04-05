# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line

from turtle import clear


def alphabetical_order(film_name_list):     
    film_name_list.sort()
    #return(film_name_list)
    return(film_name_list)
    
alphabetical_order([ 'Jaws (1975)', 'Star Wars (1977)','Close Encounters of the Third Kind (1977)', 'Superman (1978)', 'The Empire Strikes Back (1980)', 'Raiders of the Lost Ark (1981)' ,'E.T. the Extra-Terrestrial (1982)', 'Return of the Jedi (1983)', 'Indiana Jones and the Temple of Doom (1984)' ,'Empire of the Sun (1987)', 'Indiana Jones and the Last Crusade (1989)', 'Home Alone (1990)', 'JFK (1991)', 'Home Alone 2: Lost in New York (1992)', 'Jurassic Park (1993)', 'Schindler s List (1993)', 'The Lost World: Jurassic Park (1997) ', 'Saving Private Ryan (1998)', 'Star Wars: Episode I The Phantom Menace (1999) ', 'Angela\'s Ashes (1999) The Patriot (2000)', 'A.I. Artificial Intelligence (2001)', 'Harry Potter and the Sorcerers Stone (2001)', 'Star Wars: Episode II  Attack of the Clones (2002) ', 'Harry Potter and the Chamber of Secrets (2002)', 'Catch Me If You Can (2002)', 'Harry Potter and the Prisoner of Azkaban (2004)', 'Star Wars: Episode III  Revenge of the Sith (2005) ', 'Memoirs of a Geisha (2005)', ' Munich (2005)', 'Indiana Jones and the Kingdom of the Crystal Skull (2008)', 'The Adventures of Tintin (2011)', 'Star Wars: The Force Awakens (2015)', 'Star Wars: The Last Jedi (2017)', 'Star Wars: The Rise of Skywalker (2019)'])

def won_golden_globe(movie_name):
    movie_name1 = str.lower(movie_name)
    #print(movie_name1)
    return (movie_name1 in ['jaws','star wars: episode iv – a new hope','e.t. the extra-terrestrial', 'memoirs of a geisha'])
        

won_golden_globe('memoirs of a geisha')



#film_name_list = [ 'Jaws (1975)', 'Star Wars (1977)','Close Encounters of the Third Kind (1977)', 'Superman (1978)', 'The Empire Strikes Back (1980)', 'Raiders of the Lost Ark (1981)' ,'E.T. the Extra-Terrestrial (1982)', 'Return of the Jedi (1983)', 'Indiana Jones and the Temple of Doom (1984)' ,'Empire of the Sun (1987)', 'Indiana Jones and the Last Crusade (1989)', 'Home Alone (1990)', 'JFK (1991)', 'Home Alone 2: Lost in New York (1992)', 'Jurassic Park (1993)', 'Schindler s List (1993)', 'The Lost World: Jurassic Park (1997) ', 'Saving Private Ryan (1998)', 'Star Wars: Episode I The Phantom Menace (1999) ', 'Angelas Ashes (1999) The Patriot (2000)', 'A.I. Artificial Intelligence (2001)', 'Harry Potter and the Sorcerers Stone (2001)', 'Star Wars: Episode II  Attack of the Clones (2002) ', 'Harry Potter and the Chamber of Secrets (2002)', 'Catch Me If You Can (2002)', 'Harry Potter and the Prisoner of Azkaban (2004)', 'Star Wars: Episode III  Revenge of the Sith (2005) ', 'Memoirs of a Geisha (2005)', ' Munich (2005)', 'Indiana Jones and the Kingdom of the Crystal Skull (2008)', 'The Adventures of Tintin (2011)', 'Star Wars: The Force Awakens (2015)', 'Star Wars: The Last Jedi (2017)', 'Star Wars: The Rise of Skywalker (2019)']

# movie_list = ['Fahrenheit','The Seventh One','Toto XX','Falling in Between','Toto XIV','Old Is New','Jaws (1975)','Star Wars (1977)','Close Encounters of the Third Kind (1977)','Superman (1978)', 'The Empire Strikes Back (1980)', 'Raiders of the Lost Ark (1981)' ,'E.T. the Extra-Terrestrial (1982)', 'Return of the Jedi (1983)', 'Indiana Jones and the Temple of Doom (1984)','Empire of the Sun (1987)','Indiana Jones and the Last Crusade (1989)','Home Alone (1990)','JFK (1991)', 'Home Alone 2: Lost in New York (1992)', 'Jurassic Park (1993)', 'Schindler s List (1993)', 'The Lost World: Jurassic Park (1997) ', 'Saving Private Ryan (1998)', 'Star Wars: Episode I The Phantom Menace (1999) ', 'Angela\'s Ashes (1999) The Patriot (2000)', 'A.I. Artificial Intelligence (2001)', 'Harry Potter and the Sorcerers Stone (2001)', 'Star Wars: Episode II  Attack of the Clones (2002) ', 'Harry Potter and the Chamber of Secrets (2002)', 'Catch Me If You Can (2002)', 'Harry Potter and the Prisoner of Azkaban (2004)', 'Star Wars: Episode III  Revenge of the Sith (2005) ', 'Memoirs of a Geisha (2005)', ' Munich (2005)', 'Indiana Jones and the Kingdom of the Crystal Skull (2008)', 'The Adventures of Tintin (2011)', 'Star Wars: The Force Awakens (2015)', 'Star Wars: The Last Jedi (2017)', 'Star Wars: The Rise of Skywalker (2019)']
# def remove_toto_albums(toto_albums):
    
#     #print(len(movie_list))
#     tidy_list = list(set(movie_list) - set(toto_albums))
#     return(tidy_list)
#     #print(len(tidy_list))

# remove_toto_albums(['Fahrenheit','The Seventh One','Toto XX','Falling in Between','Toto XIV','Old Is New'])

#remove_toto_albums(['Fahrenheit', 'The Seventh One', 'Toto XX', 'Falling in Between','Toto XIV', 'Old Is New'])


# # Deze optie was goed. Ik moest alleen de lijst met films NIET in de functie definitie plaatsen. 
movie_list = ['Fahrenheit','The Seventh One','Toto XX','Falling in Between','Toto XIV','Old Is New','Jaws (1975)','Star Wars (1977)','Close Encounters of the Third Kind (1977)','Superman (1978)', 'The Empire Strikes Back (1980)', 'Raiders of the Lost Ark (1981)' ,'E.T. the Extra-Terrestrial (1982)', 'Return of the Jedi (1983)', 'Indiana Jones and the Temple of Doom (1984)','Empire of the Sun (1987)','Indiana Jones and the Last Crusade (1989)','Home Alone (1990)','JFK (1991)', 'Home Alone 2: Lost in New York (1992)', 'Jurassic Park (1993)', 'Schindler s List (1993)', 'The Lost World: Jurassic Park (1997) ', 'Saving Private Ryan (1998)', 'Star Wars: Episode I The Phantom Menace (1999) ', 'Angela\'s Ashes (1999) The Patriot (2000)', 'A.I. Artificial Intelligence (2001)', 'Harry Potter and the Sorcerers Stone (2001)', 'Star Wars: Episode II  Attack of the Clones (2002) ', 'Harry Potter and the Chamber of Secrets (2002)', 'Catch Me If You Can (2002)', 'Harry Potter and the Prisoner of Azkaban (2004)', 'Star Wars: Episode III  Revenge of the Sith (2005) ', 'Memoirs of a Geisha (2005)', ' Munich (2005)', 'Indiana Jones and the Kingdom of the Crystal Skull (2008)', 'The Adventures of Tintin (2011)', 'Star Wars: The Force Awakens (2015)', 'Star Wars: The Last Jedi (2017)', 'Star Wars: The Rise of Skywalker (2019)']

def remove_toto_albums(movie_list):
    
    if 'Fahrenheit' in movie_list: movie_list.remove('Fahrenheit')
    if 'The Seventh One' in movie_list: movie_list.remove('The Seventh One')
    if 'Toto XX' in movie_list: movie_list.remove('Toto XX')
    if 'Falling in Between' in movie_list: movie_list.remove('Falling in Between')
    if 'Toto XIV' in movie_list: movie_list.remove('Toto XIV')
    if 'Old Is New' in movie_list: movie_list.remove('Old Is New')

    return(movie_list)

remove_toto_albums(['Fahrenheit', 'The Seventh One', 'Toto XX', 'Falling in Between','Toto XIV', 'Old Is New'])




# def remove_toto_albums(movies):
#     if "Fahrenheit" in movies: movies.remove("Fahrenheit")
#     if "The Seventh One" in movies: movies.remove("The Seventh One")
#     if "Toto XX" in movies: movies.remove("Toto XX")
#     if "Falling in Between" in movies: movies.remove("Falling in Between")
#     if "Toto XIV" in movies: movies.remove("Toto XIV")
#     if "Old Is New" in movies: movies.remove("Old Is New")
#     return(movies)

# movies = ['Fahrenheit','The Seventh One','Toto XX','Falling in Between','Toto XIV','Old Is New','Jaws (1975)','Star Wars (1977)','Close Encounters of the Third Kind (1977)','Superman (1978)', 'The Empire Strikes Back (1980)', 'Raiders of the Lost Ark (1981)' ,'E.T. the Extra-Terrestrial (1982)', 'Return of the Jedi (1983)', 'Indiana Jones and the Temple of Doom (1984)','Empire of the Sun (1987)','Indiana Jones and the Last Crusade (1989)','Home Alone (1990)','JFK (1991)', 'Home Alone 2: Lost in New York (1992)', 'Jurassic Park (1993)', 'Schindler s List (1993)', 'The Lost World: Jurassic Park (1997) ', 'Saving Private Ryan (1998)', 'Star Wars: Episode I The Phantom Menace (1999) ', 'Angela\'s Ashes (1999) The Patriot (2000)', 'A.I. Artificial Intelligence (2001)', 'Harry Potter and the Sorcerers Stone (2001)', 'Star Wars: Episode II  Attack of the Clones (2002) ', 'Harry Potter and the Chamber of Secrets (2002)', 'Catch Me If You Can (2002)', 'Harry Potter and the Prisoner of Azkaban (2004)', 'Star Wars: Episode III  Revenge of the Sith (2005) ', 'Memoirs of a Geisha (2005)', ' Munich (2005)', 'Indiana Jones and the Kingdom of the Crystal Skull (2008)', 'The Adventures of Tintin (2011)', 'Star Wars: The Force Awakens (2015)', 'Star Wars: The Last Jedi (2017)', 'Star Wars: The Rise of Skywalker (2019)']
# remove_toto_albums(movies)