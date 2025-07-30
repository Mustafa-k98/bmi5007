import os
import string

def word_count_from_file(filename):
    """
    Count the words in a file and return a dictionary with word and word count.
    Args:
    - filename (str): Path to the file
    
    Returns:
    - Dictionary with word as key and its count as value
    """
    # Creates an empty dictionary to place words in
    word_dict = {}

    # Opens file in read only form, converts all contents to lower case.
    with open(filename, 'r') as file:
        contents = file.read().lower()

    # Cleans up text by removing all punctuation.
    for char in string.punctuation:
        contents = contents.replace(char,"")
    
    # Cleans up text by removing all numbers(digits).
    for char in string.digits:
        contents = contents.replace(char,"")
    
    # Seperates all words in the text file.
    words = contents.split()

    # Loop through each word in the list to count its occurrences.
    for word in words:

        # If the word isn't in the dictionary, it is added and given a value of 1
        if word not in word_dict:
            word_dict[word] = 1

        # If the word is already in the dictionary, its value is increased by 1
        else:
             word_dict[word] += 1

    # Return the dictionary containing all the words and their final counts.
    return word_dict

def top_3_words(word_dict):
    """
    Return top 3 words from a word count dictionary.
    Args:
    - word_dict (dict): Dictionary with word as key and its count as value
    
    Returns:
    - Dictionary with top 3 words and their count
    """
    
    # Initializes an empty dictionary to place new words in
    unique_sorted_dict = {}

    # Initializes a variable that sorts the dictionary, as a tuple
    ranked_words = sorted(word_dict.items(), key=lambda pair: pair[1], reverse = True)
    
    # Iterate through the newly sorted list of (word, count) pairs.
    for key,value in ranked_words:

        # Stops the loop if the dictionary has more than 3 words.
        if len(unique_sorted_dict) >= 3:
            break
        
        # Ensures single letter's (such as p), were not included in word count.
        valid_word = len(key) > 1 or key in ('a', 'i')

        # Add the key and value to the new dictionary from the sorted dictionary
        if valid_word and value not in unique_sorted_dict.values():
            unique_sorted_dict[key] = value

    # Return the final dictionary containing the top 3 words.    
    return unique_sorted_dict




def main():
    """
    Finds and analyzes the frequency of each word in files.

    The function first locates all .txt files in the 'medline' directory, 
    in then counts the word occurrences and aggregates the total counts from all files.
    The top 3 most frequest words are then printed out.
    """

    # Initializes an empty dictionary to place all words in
    master_dict = {}
    dir_path = './medline'  # path to point to the 'medline' folder. Do not change this.

    # Creates a full path to the target directory
    base_dir = os.path.join(os.getcwd(), dir_path)

    # Loop through every file and folder in the specified directory.
    for filename in os.listdir(base_dir):

        # Ensures all files being analyzed are text files
        if filename.endswith('.txt'):

            # Construct the full path to the current file. 
            file_path = os.path.join(base_dir, filename)
            # Call the function to get the word counts for this single file.
            file_word_count = word_count_from_file(file_path)

            # Loop through the results of the current file to aggregate them.
            for word,count in file_word_count.items():
                master_dict[word] = master_dict.get(word,0) + count
    
    # Fetch top 3 words from master dictionary
    result = top_3_words(master_dict)
    print(result)

if __name__ == "__main__":
    main()


