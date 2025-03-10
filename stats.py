def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    char_dict = {}

    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict

def sort_on(dict):
    return dict["count"]

def sort_char_dict(dict):
    dict_list = []

    for key in dict:
        dict_list.append({"char": key, "count": dict[key]})
    
    dict_list.sort(reverse=True, key=sort_on)

    return dict_list