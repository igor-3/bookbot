def count_words(text):
    count = len(text.split())
    return count

def count_characters(text):
    count = {}
    for c in text.lower():
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
    return count

def sort_key(dict):
    return dict["num"]

def sort_dictionary(char_count):
    dict_list = []
    for c in char_count:
        new_dict = { "char": c, "num": char_count[c] }
        dict_list.append(new_dict)
    dict_list.sort(reverse=True, key=sort_key)
    return dict_list
    