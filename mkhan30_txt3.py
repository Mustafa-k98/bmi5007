import os
import string


def keyword_count(filename, keyword):
    """
    Counts the occurrences of a specific keyword in a given text file,
    ignoring case and punctuation.

    Args:
        filename (str): The path to the text file.
        keyword (str): The keyword to search for.

    Returns:
        int: The total count of the keyword found in the file.
    """
    # Initialize a counter for the keyword
    count = 0

    # Use a 'with' statement to open the file, ensuring it is automatically closed
    with open(filename, 'r') as file:
        # Read the entire file content and convert it to lowercase for case-insensitive matching
        contents=file.read().lower()
        
        # Iterate through all punctuation characters from the 'string' module
        for char in string.punctuation:
            # Replace each punctuation character with an empty string (remove it)
            contents = contents.replace(char,"")

        # Split the cleaned content into a list of words using whitespace as a delimiter
        words=contents.split()

        # Iterate through each word in the list
        for word in words:
            # Check if the current word matches the keyword
            if word == keyword:
                # If it matches, increment the counter
                count += 1
    # Return the final count of the keyword
    return(count)


def main():
    """
    Scans a directory named 'notes' for text files (.txt), finds the file
    with the most occurrences of a specific keyword, and prints the result.
    """
    # Define the path to the 'notes' directory
    dir_path = './notes'  
    # Construct the full, absolute path to the directory by joining the current working directory
    base_dir = os.path.join(os.getcwd(), dir_path)
    # Define the keyword to search for
    keyword = "diabetes"
    # Initialize a variable to track the highest count found so far
    leader_count = 0
    # Initialize a variable to store the name of the file with the highest count
    leader_file_name = ""
    
    # Iterate through each filename in the specified directory
    for filename in os.listdir(base_dir):

         # Check if the file has a '.txt' extension and is not a '.md' file
        if filename.endswith('.txt') and '.md' not in filename:
            
            # Construct the full path to the current file
            file_path = os.path.join(base_dir, filename)

            # Call the keyword_count function to get the count for the current file
            file_word_count = keyword_count(file_path, keyword)

            # Check if the current file's count is greater than the highest count found so far
            if file_word_count > leader_count:
                # If so, update the highest count and the corresponding filename
                leader_count = file_word_count  
                leader_file_name = filename 

    # Print the name of the file with the most occurrences and the count in the specified format
    print(f"File with most occurrences: {leader_file_name} ({leader_count} times)")

    
 

if __name__ == "__main__":
    main()
