# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorer_name0 = 'Ruud Gullit'
goal_0 = 32
scorer_name1 = 'Marco van Basten'
goal_1 = 54


scorers = str(scorer_name0) + ' ' + str(goal_0) + ', ' + str(scorer_name1) +' '+ str(goal_1)
print(scorers)
report = f'{scorer_name0} scored in the {goal_0}nd minute\n{scorer_name1} scored in the {goal_1}th minute'
print(report)

player = 'Jan Wouters'

#print(player.find(' '))

first_name = player[ :(player.find(' '))]
#print(first_name)

last_name_len = len(player[ (player.find(' ')):-1])
#print(last_name_len)

name_short = str(first_name[ :1])+ '.'+ str(player[(player.find(' ')):])
#name_short = (f'{first_name[ :1]}. { player[ 4 : ] }')
#print(name_short)

chant = ((first_name) + '! ') * (len(first_name)-1) + ((first_name) + '!')
#print(chant)

#good_chant = ((ord(chant[-1]) != ord(' '))) == True
good_chant = chant[-1] != ' '
#print(good_chant)