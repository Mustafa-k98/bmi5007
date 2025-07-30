import xml.etree.ElementTree as ET


def extract_data_calc_average():
    """
    Loads an XML file, extracts datasets with both 'cost' and 'days' information,
    calculates their averages, and prints the result.
    """   

    # Loads the XML file 
    tree = ET.parse("xml_final_1.xml")
    root = tree.getroot()

    # Initialize counters
    total_cost = 0
    total_days = 0
    count = 0

    # Iterate through all <dataset> tags in the XML file
    for dataset in root.iter('dataset'):
        
        # Use a try-except block to handle potential errors.
        # This will skip any 'dataset' that doesn't have both 'Cost' and 'Days' tags,
        # or if their text content cannot be converted to a float.
        try:
            # Find the 'Cost' and 'Days' child elements, get their text content,
            # convert the text to a float, and add it to the running totals.
            total_cost += float(dataset.find("Cost").text)
            total_days += float(dataset.find("Days").text)
            
            # If the above lines execute without an error, increment the counter.
            count += 1
            
        except:
            # If an error occurs (e.g., a tag is not found),
            # this 'continue' statement will skip the rest of the loop for the current 'dataset'
            # and move on to the next one.            
            continue
    
    # Check if 'count' is not zero to prevent a division-by-zero error   
    if count != 0:
        # Calculate the average cost and average days
        average_cost = total_cost / count
        average_days = total_days / count
    else:
        # If no valid datasets were found, set the averages to 0
        average_cost = 0
        average_days = 0

    # Print the final calculated averages in the specified format using an f-string
    print(f"AvgCost:{average_cost},AvgDays:{average_days}")

# Call the function to execute the code
extract_data_calc_average()