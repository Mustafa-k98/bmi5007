import os
import re

def isolate_sentences(filename):
    """
    Reads a text file and extracts sentences that contain specific keywords
    related to "follow up".

    Args:
        filename (str): The path to the text file.

    Returns:
        list: A list of sentences from the file that contain the keywords.
    """

    # Initialize an empty list to store the found sentences
    found_sentences = []

    # Use a 'with' statement to open the file for reading, ensuring it's closed automatically
    with open(filename, 'r') as file:
        # Read the entire content of the file into a string
        contents=file.read()

    # Split the content into sentences using a regex that handles periods (not in abbreviations like Mr. or Ms.),
    # question marks, and exclamation points as delimiters.
    # Then, iterate through each resulting sentence.
    for sentence in re.split(r'(?<!\bMr|Ms)\.\s+|[?!]\s+', contents):
        # Search for the keywords "follow up", "follow-up", or "f/u" in the current sentence,
        # ignoring case.
        if re.search(r'\b[Ff]ollow[\s-]*[Uu]p\b|\b[Ff]/[Uu]\b', sentence):
            # If the keyword is found, append the sentence to the list of found sentences.
            found_sentences.append(sentence)

    # Return the list of sentences found
    return found_sentences


def write_setences_to_file(data, output_file):
    """
    Writes a list of filenames and sentences to an output file.

    Args:
        data (list): A list of tuples, where each tuple contains a filename and a sentence.
        output_file (str): The path to the output file.
    """
    # Open the output file in write mode ('w'), creating it if it doesn't exist.    
    with open(output_file, mode = 'w', newline = '') as outputfile:
        
        # Iterate through each tuple (filename, sentence) in the provided data list.
        for filename,sentence in data:
            # Write the filename and sentence to the output file in the specified format,
            # followed by a newline character.
            outputfile.write(f'{filename} "{sentence}"\n')
 

def main():
    """
    Scans a directory for text files, extracts sentences containing "follow up",
    and writes them to a master output file along with their filenames.
    """
    # Define the path to the 'notes' directory
    dir_path = './notes'  
    # Construct the full, absolute path to the directory by joining the current working directory
    base_dir = os.path.join(os.getcwd(), dir_path)
    # Initialize a master list to store all (filename, sentence) tuples
    master_list = []
    # Define the name of the output file
    output_file = "mkhan30_mid.txt"

    # Iterate through each filename in the specified directory
    for filename in os.listdir(base_dir): 

        # Check if the file has a '.txt' extension and is not a '.md' file
        if filename.endswith('.txt') and '.md' not in filename:

            # Construct the full path to the current file
            file_path = os.path.join(base_dir, filename)

            # Call the isolate_sentences function to get the sentences from the current file
            processed_sentences = isolate_sentences(file_path)

            # Create a list of (filename, sentence) tuples for each processed sentence
            sentences_to_write = [(filename, sentence) for sentence in processed_sentences]

            # Add these new tuples to the master list
            master_list.extend(sentences_to_write)
            
    # Call the function to write all the collected sentences to the output file
    write_setences_to_file(master_list, output_file)

if __name__ == "__main__":
    main()