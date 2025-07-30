import csv

def filter_and_avg_glucose():
    """
    Reads a CSV file, filters out rows containing "NA" values in any column,
    and then calculates the average glucose level for each location.
    It prints the average glucose for each valid location.
    """    
    # Open the CSV file in read mode
    cfile = open("csv_final_2.csv", "r")
    # Use csv.DictReader to read the data, treating each row as a dictionary
    # with keys from the header row.
    cdata = csv.DictReader(cfile,delimiter=",")

    # Initialize a dictionary to store the total glucose and count for each location.
    # The keys will be location names, and the values will be dictionaries
    # with 'total_glucose' and 'count'.
    location_data = {}

    # Iterate through each row in the CSV data
    for row in cdata:
        # Initialize a flag to determine if the current row is valid
        is_valid_row = True

        # Iterate through the values in the current row's dictionary
        for value in row.values():
            # Check if any value in the row is "NA"
            if value == "NA":
                # If "NA" is found, set the flag to False and break the inner loop
                is_valid_row = False
                break

        # After checking all values in the row, if the row is not valid,
        # skip to the next row in the outer loop.            
        if not is_valid_row:
                continue
        
        # Extract the 'Location' from the row
        location = row['Location']
        # Use setdefault to get the dictionary for a location. If the location doesn't exist,
        # it creates a new dictionary with initial totals and count set to 0.        
        location_dict = location_data.setdefault(location, {'total_glucose' : 0, 'count' : 0})
        # Extract the 'Glucose' value from the row
        glucose = row['Glucose']
            

        try:
            # Convert the glucose value to a float and add it to the total for the location.
            location_dict['total_glucose'] += float(glucose)
            # Increment the count for the location.
            location_dict['count'] += 1
            
        except ValueError:
            continue

    cfile.close()

    # Iterate through the items (location and their data) in the location_data dictionary
    for location, data in location_data.items():

        # Check if the count for the current location is not zero to prevent a division-by-zero error
        if location_data[location]['count'] != 0:
            # Calculate the average glucose for the location
            average_glucose = location_data[location]['total_glucose']/location_data[location]['count']

        else:
            # If the count is zero, set the average to 0.
            average_glucose = 0

        # Print the location and its calculated average in the specified format
        print(f"Location:{location},AvgGlucose:{average_glucose}")

filter_and_avg_glucose()