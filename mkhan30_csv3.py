import csv

def cal_glucose_avg():
    """
    Reads a CSV file, calculates the average glucose level for each group,
    and prints the result.
    """
    # Open the CSV file in read mode
    cfile = open("csv_final_1.csv", "r")

    # Use csv.DictReader to read the data, treating each row as a dictionary
    # with keys from the header row.    
    cdata = csv.DictReader(cfile,delimiter=",")

    # Initialize a dictionary to store glucose values, grouped by 'Group'
    # The keys will be group names, and the values will be lists of glucose readings.
    group_data = {}

    # Iterate through each row in the CSV data
    for row in cdata:

        # Use setdefault to get the list for a group. If the group doesn't exist yet,
        # it creates a new empty list and adds it to the dictionary.
        group_list = group_data.setdefault(str(row['Group']), [])
        
        try:
            # Convert the 'Glucose' value from the row to a float and append it to the list
            # for the corresponding group.
            group_list.append(float(row['Glucose']))
        except ValueError:
            continue
    cfile.close()

    # Iterate through the items in the 'group_data' dictionary to calculate averages
    for group, glucose in group_data.items():
        
        count = len(glucose)

        total = sum(glucose)

         # Check if the count is not zero to prevent a division-by-zero error
        if count != 0:
            # Calculate the average glucose for the group
            average_glucose = total / count

        else:
            average_glucose = "Data Not avialable"
            
        # Print the group and its calculated average in the specified format
        print(f"Group:{group},AvgGlucose:{average_glucose}")

cal_glucose_avg()
