
def get_none():
    return None

# def flatten_dict(dict):
#     list = [*dict.values()]
#     return list

# print(flatten_dict(d))


def flatten_dict(in_dict, dict_out=None, parent_key=None):
    if dict_out is None:
        dict_out = {}

    for k, v in in_dict.items():
        k = f"{parent_key}{k}" if parent_key else k
        if isinstance(v, dict):
            flatten_dict(in_dict=v, dict_out=dict_out, parent_key=k)
            continue
        
        dict_out[k] = v
        list = [*dict_out.values()]
    return list

dictA = {'a': {'inner_a': {"inner_inner_f": 34}, 'inner_b': 350}, 'b': 3.14}
# d = {'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14}
# di = {'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14}
# ei = {'a': [{'inner_inner_a': 42}]}

print(flatten_dict(dictA))
