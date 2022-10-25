# Do not modify these lines
__winc_id__ = '63ce21059cf34d3d8ffef497ede7e317'
__human_name__ = 'comments'

# Add your code after this line

"""It is quite common to start a Python file with a few lines of comments. 
These lines state information regarding the project, the purpose of the file, 
the programmer who developed it or has worked on it, and the software license that is used for the code."""

# Ik heb hier een klein scriptje geschreven om korting te berekenen.
name = "Martijn" # Hier vraag ik de naam.
product = "TV"
price = 999
price = int(price)
discount = 20 #Hier kun je de korting invoeren

total_price = price - (discount/100 * price)
x = round(total_price, 2)
greeting = f"Hallo {name}, de normale prijs van dit {product} is {price}. Met {discount} % korting is dit {x}"
print(greeting) 

# Dit is het einde van het script.

""" The Style Guide for Python Code (PEP8) recommends less than 79 characters per line. 
In practice, 70 or 72 characters per line are easier to read, and thus is recommended. 
If your comment is approaching or exceeding this length then you will want to spread it out over multiple lines."""