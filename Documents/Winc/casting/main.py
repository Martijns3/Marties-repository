# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line
from ast import Num


leek_price = 2
print('Leek is ' + str(leek_price) + ' euro per kilo.')

leek_string = 'leek 4'
item_count = (leek_string[(leek_string.find(' ')): ])
sum_total = int(item_count) * leek_price
print(sum_total)

broccoli_per_kilo = 2.34
order = 'broccoli 1.6'
order_amount = (float(order[order.find(' ') : ]))
number = (order_amount * broccoli_per_kilo)
order_total = round(number, 2) 
#print(str(order_amount) +'kg broccoli costs ' + str(order_total) + 'e' )
print(f'{order_amount} kg broccoli costs {order_total}e')

