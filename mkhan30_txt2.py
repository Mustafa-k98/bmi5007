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
        
        # Replace each punctuation character with an empty string (remove it)
        for char in string.punctuation:
            contents = contents.replace(char,"")

        # Split the cleaned content into a list of words using whitespace as a delimiter
        words=contents.split()

        # Iterate through each word in the list
        for word in words:
            # Check if the current word matches the keyword
            if word == keyword:
                count += 1

    # Return the final count of the keyword
    return(count)



def main():
    """
    Scans a directory named 'notes' for text files (.txt) and counts the total
    occurrences of a specific keyword across all files. It then prints the total count.
    """    

    # Define the path to the 'notes' directory
    dir_path = './notes'
    # Construct the full, absolute path to the directory by joining the current working directory
    base_dir = os.path.join(os.getcwd(), dir_path)
    # Initialize a counter for the total keyword count across all files
    total_count = 0
    # Define the keyword to search for
    keyword = "hypertension"

    # Iterate through each filename in the specified directory
    for filename in os.listdir(base_dir):
        # Check if the file has a '.txt' extension and is not a '.md' file
        if filename.endswith('.txt') and '.md' not in filename:
            
            # Construct the full path to the current file
            file_path = os.path.join(base_dir, filename)

             # Call the keyword_count function to get the count for the current file
            file_keyword_count = keyword_count(file_path, keyword)

            # Add the count from the current file to the total count
            total_count += file_keyword_count

    # Print the final total count in the specified format
    print(f"Total count:{total_count}")

        
if __name__ == "__main__":
    main()