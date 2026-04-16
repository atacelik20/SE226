def strip_whitespaces(string_list):
    return [item.strip() for item in string_list]

def remove_duplicates(data_list):
    unique_list = []
    for item in data_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list