data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

list_from_data_structure = []


def list_to_list(elem):
    global list_from_data_structure
    for el in elem:
        list_from_data_structure.append(el)
    return list_from_data_structure


def set_to_list(elem):
    global list_from_data_structure
    for el in elem:
        list_from_data_structure.append(el)
    return list_from_data_structure


def dict_to_list(elem):
    global list_from_data_structure
    for el in elem.keys():
        list_from_data_structure.append(el)
    for el in elem.values():
        list_from_data_structure.append(el)
    return list_from_data_structure


def tuple_to_list(elem):
    global list_from_data_structure
    for i in elem:
        list_from_data_structure.append(i)
    return list_from_data_structure


def data_structure_to_list(data):
    global list_from_data_structure
    global data_structure
    count = -1
    while count != 0:
        list_from_data_structure = []
        count = 0
        for i in data:
            if isinstance(i, dict):
                count += 1
            elif isinstance(i, list):
                count += 1
            elif isinstance(i, set):
                count += 1
            elif isinstance(i, tuple):
                count += 1

        for i in data:
            if isinstance(i, dict):
                dict_to_list(i)
            elif isinstance(i, list):
                list_to_list(i)
            elif isinstance(i, tuple):
                tuple_to_list(i)
            elif isinstance(i, set):
                set_to_list(i)
            else:
                list_from_data_structure.append(i)

        data = list_from_data_structure

    return data


def calculate_structure_sum(data_):
    b = data_structure_to_list(data_)
    summ = 0
    for i in b:
        if isinstance(i, int):
            summ += i
        if isinstance(i, str):
            summ += len(i)
    return summ


result = calculate_structure_sum(data_structure)
print(result)
