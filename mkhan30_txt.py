import string

def word_count_and_frequency():

    word_dict = {}
    master_dict = {}

    with open("abstract.txt", 'r') as file:
        contents = file.read().lower()
    
    for char in string.punctuation:
        contents = contents.replace(char,"")
    
    words = contents.split()

    for word in words:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1

    ranked_word_dict = sorted(word_dict.items(),key = lambda pair: pair[1], reverse = True)

    for key, value in ranked_word_dict:

        if len(master_dict) >= 10:
            break

        valid_word = len(key) > 1 or key in ('a','i')

        if valid_word and key not in master_dict:
            master_dict[key] = value
        
    
    print(master_dict)

word_count_and_frequency()