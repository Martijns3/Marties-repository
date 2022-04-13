from tkinter import X
from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"




def unique_koala_facts(x):
    n = 1000     
    unique_fact_list = list()    
    while n > 0:
        fact_to_str = str(random_koala_fact())
        n -= 1
        if len(unique_fact_list) == x:
                break
        if fact_to_str not in unique_fact_list:
            unique_fact_list.append(fact_to_str)
            
    return unique_fact_list



joey_search_list = list()  

def num_joey_facts():
    n = 100000000
    joey_found = []  
    while n > 0:
        n -= 1
        list_data = str(random_koala_fact())
        joey_search_list.append(list_data)
        if joey_search_list.count('The koala weighs 15 to 30 pounds.') >= 10: 
            break
        
    for name in joey_search_list:
        s = str(name).split(" ")
        for i in s:
            if (i == 'joey'): 
                if name not in joey_found:
                    joey_found.append(name)
                    num_facts = len(joey_found)
    # print(joey_found)
    #print(num_facts)
    return num_facts

def koala_weight():      
    n = 10000000
    kg_collect = [] 
    while n > 0:
        n -= 1
        sentence = str(random_koala_fact())
        if'kg'in sentence:
            kg_collect.append(sentence)
            break
    str_collect = str(kg_collect)
    
    return (int(str_collect[(str_collect.index('kg')-3):(str_collect.find('kg'))]))   
    
    
    
# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    #print(random_koala_fact())


    unique_koala_facts(1)
    
    num_joey_facts()
    
    koala_weight()