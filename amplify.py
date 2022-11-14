'''
list map lamda solution
'''

def dict_list_map(list_dict: list):
    dict_output = dict()

    def append_item(key, value):
        if dict_output.get(key):
            dict_output[key].append(value)
        else:
            dict_output[key] = [value]

    list(map(lambda dict_item: list(map(lambda key, value: append_item(key, value), dict_item)), list_dict))
    return dict_output



'''
simple loop solution
'''


def dict_entryes(list_dict: list):
    out_dict = dict()
    for item in list_dict:
        for key in item:
            if out_dict.get(key):
                out_dict[key].append(item.get(key))
            else:
                out_dict[key] = [item.get(key)]
    return out_dict


if __name__ == '__main__':
    list_dict = [{"a": "x"},
     {"a": "y", "b": "z"},
     {"a": "x", "c": "y"}]

    assert dict_entryes(list_dict) == {"a": ["x", "y", "x"], "b": ["z"], "c": ["y"]}
    assert dict_list_map(list_dict) == {"a": ["x", "y", "x"], "b": ["z"], "c": ["y"]}
