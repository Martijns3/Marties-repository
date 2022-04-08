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






a= ['a']
b= ['z']
c= ['c']
d= ['d']
e= ['e']
f= ['f']
g= ['g']
h= ['h']
i= ['i']
j= ['j']
k= ['k']
l= ['l']
m= ['m']
n= ['n']
o= ['o']
p= ['p']
q= ['q']
r= ['r']
s= ['s']
t= ['t']
u= ['u']
v= ['v']
w= ['w']
x= ['x']
y= ['y']
z= ['z']


def alphabet_set(countries):
    
    countries_lower = [x.lower() for x in countries]

    countries_most_char = sorted(countries_lower, key=lambda country_name: sum(char in 'abcdefghijklmnopqrstuvwxyz' for char in country_name), reverse=True)
    
            
    alphabet_set = []
    for country in countries_most_char:
        
        for char in a: 
            if char in country:
                a.pop(0)
                if country not in alphabet_set:
                    alphabet_set.append(country)
                #print(a)
        for char in b: 
            if char in country:
                b.pop(0)
                if country not in alphabet_set:
                    alphabet_set.append(country)
                #print(b)
        for char in c: 
            if char in country:
                c.pop(0)
                if country not in alphabet_set:
                    alphabet_set.append(country)
                #print(c)
        for char in d: 
            if char in country:
                d.pop(0)
                if country not in alphabet_set:
                    alphabet_set.append(country)
                #print(d)        
        for char in e: 
            if char in country:
                e.pop(0)
                if country not in alphabet_set:
                    alphabet_set.append(country)
                #print(e)
        for char in f: 
            if char in country:
                f.pop(0)
                if country not in alphabet_set:
                    alphabet_set.append(country)
                #print(f)
        for char in g: 
            if char in country:
                g.pop(0)
                if country not in alphabet_set:
                    alphabet_set.append(country)
                #print(g)
        for char in h: 
            if char in country:
                h.pop(0)
                if country not in alphabet_set:
                    alphabet_set.append(country)
                #print(h)        
        for char in i: 
            if char in country:
                i.pop(0)
                if country not in alphabet_set:
                    alphabet_set.append(country)
                #print(i)
        for char in j: 
            if char in country:
                j.pop(0)
                if country not in alphabet_set:
                    alphabet_set.append(country)
                #print(j)
        for char in k: 
            if char in country:
                k.pop(0)
                if country not in alphabet_set:
                    alphabet_set.append(country)
                #print(k)
        for char in l: 
            if char in country:
                l.pop(0)
                if country not in alphabet_set:
                    alphabet_set.append(country)
                #print(l)        
        for char in m: 
            if char in country:
                m.pop(0)
                if country not in alphabet_set:
                    alphabet_set.append(country)
                #print(m)
        for char in n: 
            if char in country:
                n.pop(0)
                if country not in alphabet_set:
                    alphabet_set.append(country)
                #print(n)
        for char in o: 
            if char in country:
                o.pop(0)
                if country not in alphabet_set:
                    alphabet_set.append(country)
                #print(o)
        for char in p: 
            if char in country:
                p.pop(0)
                if country not in alphabet_set:
                    alphabet_set.append(country)
                #print(p)        
        for char in q: 
            if char in country:
                q.pop(0)
                if country not in alphabet_set:
                    alphabet_set.append(country)
                #print(q)
        for char in r: 
            if char in country:
                r.pop(0)
                if country not in alphabet_set:
                    alphabet_set.append(country)
                #print(r)
        for char in s: 
            if char in country:
                s.pop(0)
                if country not in alphabet_set:
                    alphabet_set.append(country)
                #print(s)
        for char in t: 
            if char in country:
                t.pop(0)
                if country not in alphabet_set:
                    alphabet_set.append(country)
                #print(t)        
        for char in u: 
            if char in country:
                u.pop(0)
                if country not in alphabet_set:
                    alphabet_set.append(country)
                #print(u)
        for char in v: 
            if char in country:
                v.pop(0)
                if country not in alphabet_set:
                    alphabet_set.append(country)
                #print(v)
        for char in w: 
            if char in country:
                w.pop(0)
                if country not in alphabet_set:
                    alphabet_set.append(country)
                #print(w)
        for char in x: 
            if char in country:
                x.pop(0)
                if country not in alphabet_set:
                    alphabet_set.append(country)
                #print(x)        
        for char in y: 
            if char in country:
                y.pop(0)
                if country not in alphabet_set:
                    alphabet_set.append(country)
                #print(y)
        for char in z: 
            if char in country:
                z.pop(0)
                if country not in alphabet_set:
                    alphabet_set.append(country)
                #print(z)
    
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
