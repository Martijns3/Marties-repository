def get_none():
    return None


# def flatten_dict(dict):
#     list = [*dict.values()]
#     return list

# print(flatten_dict(d))

final_list = []


def flatten_dict(d):

    for k, v in d.items():

        if type(v) == dict:
            flatten_dict(v)

        elif type(v) == list:
            for i in v:
                flatten_dict(i)
        else:
            final_list.append(v)

    return final_list

    # 1. Als het een dictionary is, ga dan door elke key heen en roep voor elke value flatten_dict weer aan. Voeg de waarde die je terugkrijgt aan final_list toe
    # 2. Als het een list is, ga door elk element van de lijst heen en roep voor elk element flatten_dict weer aan. Voeg de waarde die je terugkrijgt aan final_list toe
    # 3. Geen van beiden (else) dan zit je helemaal onderin je dictionary dus die voeg je dan sowieso to aan final_list (final_list += [in_dict])


dictA = {"a": {"inner_a": {"inner_inner_f": 34}, "inner_b": 350}, "b": 3.14}
dictB = {"a": {"inner_a": 42, "inner_b": 350}, "b": {3.14: "bleh"}}
dictC = {"a": [{"inner_inner_a": 42}]}

print(flatten_dict(dictC))
