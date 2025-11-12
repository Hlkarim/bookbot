def count_words(book):
    words_array = book.split()
    return len(words_array)


def count_characters(book):
    book = book.lower()
    alphabet = {}
    for char in book:
        if char not in alphabet:
            alphabet[char] = 1
        else :
            alphabet[char] += 1
    return alphabet


def sort_list_char(char_dict : dict):
    num_char_list=[]
    
    for char in char_dict:
        
        num_char_list.append({"char":char, "num":char_dict[char]})


    num_char_list.sort(reverse = True, key = lambda num : num['num'])

    return num_char_list

