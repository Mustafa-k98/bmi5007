import xml.etree.ElementTree as ET

def extract_data_calc_avg_and_diff():
    """
    Loads an XML file, extracts blood pressure data, and calculates the average
    difference (BP_After - BP_Before) for each location. It then prints the
    results for each location.
    """

    # Loads the XML file 
    tree = ET.parse("xml_final_2.xml")
    root = tree.getroot()

    # Initialize an empty dictionary to store blood pressure data grouped by location
    bp_data = {}

    # Iterate through every 'dataset' element found in the XML file
    for dataset in root.iter('dataset'):

        # Use a try-except block to handle cases where a 'dataset' might be missing
        # 'Location', 'BP_Before', or 'BP_After' tags, or if the data is invalid.        
        try:
            # Find the 'Location', 'BP_Before', and 'BP_After' child elements within the current dataset
            location = dataset.find("Location").text
            bp_before = float(dataset.find("BP_Before").text)
            bp_after = float(dataset.find("BP_After").text)

            # Calculate the difference between BP_After and BP_Before
            bp_diff = bp_after - bp_before
            
            # Check if the location is already a key in the bp_data dictionary
            if location not in bp_data:

                # If the location is new, initialize a new dictionary for it
                # and store the first difference and set count to 1            
                bp_data[location] ={
                    'total_bp_diff' : bp_diff,
                    'count' : 1
                }
            else:
                # If the location already exists, add the new difference to the total
                # and increment the count for that location                
                bp_data[location]['total_bp_diff'] += bp_diff
                bp_data[location]['count'] += 1
        
        except:
            continue
    
    # Iterate through the keys (locations) in the bp_data dictionary
    for location in bp_data:
        # Check if the count for the current location is not zero to prevent division by zero
        if bp_data[location]['count'] != 0:
            # Calculate the average blood pressure difference for the location
            location_average = bp_data[location]['total_bp_diff']/bp_data[location]['count']
        else:
            # If the count is zero (though this case is unlikely with your current logic),
            # set the average to 0.            
            location_average = 0

        # Print the location and its calculated average BP difference in the specified format    
        print(f"Location:{location},AvgBPDiff:{location_average}")

# Call the function to execute the code
extract_data_calc_avg_and_diff()






