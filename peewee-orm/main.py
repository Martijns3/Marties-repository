from os import name
import models
import peewee
from typing import List
from models import *
from peewee import fn
from datetime import time

__winc_id__ = "286787689e9849969c326ee41d8c53c4"
__human_name__ = "Peewee ORM"


def cheapest_dish() -> models.Dish:
    """You want ot get food on a budget
    Query the database to retrieve the cheapest dish available
    """
    for dish in Dish.select().order_by(Dish.price_in_cents.asc()):
        return(dish)

print(cheapest_dish())

def vegetarian_dishes() -> List[models.Dish]:
    """You'd like to know what vegetarian dishes are available
    Query the database to return a list of dishes that contain only
    vegetarian ingredients.
    """
    List = [dish 
            for dish in Dish.select()
            if all([i.is_vegetarian for i in dish.ingredients]
                )]
    return List
# print(vegetarian_dishes())

def best_average_rating() -> models.Restaurant:
    """You want to know what restaurant is best

    Query the database to retrieve the restaurant that has the highest
    rating on average
    """
    query = Rating.select(
    Rating.restaurant,
    Rating.rating,
    fn.AVG(Rating.rating).over(partition_by=[Rating.restaurant]).alias('ravg')).join(Restaurant)
    l ={}
    for r in query:
        if r.restaurant not in l:
            l[r.restaurant] = r.ravg
    l_s = sorted(l.items(), key=lambda item: item[1], reverse=True)
    best_restaurant =l_s[0][0]
    return (best_restaurant)

    #andere optie van Rishaan
    # Restaurant.select(
    #         Restaurant, peewee.fn.AVG(Rating.rating).alias("average")
    #     ).join(Rating).group_by(Restaurant).order_by(peewee.SQL('average').desc())    
    # // hier vervang je het door de SQL 'average' 
        # .first()  
# print(best_average_rating())



def add_rating_to_restaurant() -> None:
    """After visiting a restaurant, you want to leave a rating

    Select the first restaurant in the dataset and add a rating
    """
    query = Restaurant.select().where(Restaurant.id ==1)
    for i in query:
        rest =i
    Rating.create(restaurant = rest, rating =5, comment = "Everything good! Escpecially the fried Alien slices")
    
# (add_rating_to_restaurant())

def get_ratings():
#dit is even een hulpfunctie die niet onderdeel is van de opdracht
    q = Rating.select().where(Rating.restaurant ==1)
    for i in q:
        print(i.rating, i.restaurant.name, i.comment)

# (get_ratings())

def dinner_date_possible() -> List[models.Restaurant]:
    """You have asked someone out on a dinner date, but where to go?

    You want to eat at around 19:00 and your date is vegan.
    Query a list of restaurants that account for these constraints.
    """
    List_vegan =[]
    query = Dish.select()
    for i in query:
        if i.name not in List_vegan:
            List_vegan.append(i.name)
        d =Dish.get(Dish.name== i.name)
        for ingredient in d.ingredients:
            if ingredient.is_vegan == False:
                try:
                    List_vegan.remove(str(i.name))
                except:
                    pass
    List =[]
    for dish in Dish.select():
        if (str(dish.name)) in List_vegan:
            dinnertime = time.fromisoformat('19:00:00')
            for restaurant in Restaurant.select():
                if restaurant.opening_time <= dinnertime and restaurant.closing_time > dinnertime:
                    if restaurant == dish.served_at and restaurant not in List:
                        List.append(restaurant)
                        
    return List
    

# print(dinner_date_possible())

"""You have created a new dish for your restaurant and want to add it to the menu

    The dish you create must at the very least contain 'cheese'.
    You do not know which ingredients are in the database, but you must not
    create ingredients that already exist in the database. You may create
    new ingredients however.
    Return your newly created dish
    """
    
def add_dish_to_menu() -> models.Dish:    
    
    ingr_list =[('cheese', True, False, True), 
                        ('special herbs', False, False, False),
                        ("flour", True, True, False), 
                        ("beef", False, False, True),
                        ("wine", True, True, True)
                        ]
    q = Ingredient.select()
    for ingr in q:
        # print(ingr.name)
        for i in ingr_list:
                if str(i[0]) == str(ingr.name):
                    ingr_list.remove(i)
  
    for new_ingr in ingr_list:
            Ingredient.create(name=new_ingr[0], is_vegetarian=new_ingr[1], is_vegan=new_ingr[2], is_glutenfree=new_ingr[3])
            
    Martys_pasta = Dish.create(name = "Pasta a la Marty", served_at= models.Restaurant.get_by_id(1), 
        price_in_cents = 1250 )
    cheese = models.Ingredient.get(models.Ingredient.name == 'cheese')
    wine = models.Ingredient.get(models.Ingredient.name == 'wine')
    flour = models.Ingredient.get(models.Ingredient.name == 'flour')
    beef = models.Ingredient.get(models.Ingredient.name == 'beef')
    special_herbs = models.Ingredient.get(models.Ingredient.name == 'special herbs')
    
    Martys_pasta.ingredients.add([cheese,wine,flour,beef,special_herbs])
    
    return Martys_pasta
    
# add_dish_to_menu()
    
# deze code gebruik ik om aangemaakte dishes en ingredients weer te deleten.


# q = Dish.delete().where(Dish.name == "Pasta a la Marty")
# q.execute()
# z = Ingredient.delete().where(Ingredient.name == "special herbs")
# z.execute()
# y = Ingredient.delete().where(Ingredient.name == 'wine')
# y.execute()
    
# for dish in Dish.select():
#     for i in dish.ingredients:
#         print(dish.name, i.name, i.is_vegetarian, i.is_vegan)
    
# for ingredient in Ingredient.select():
#     print(ingredient.name)


