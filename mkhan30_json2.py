import json

def group_and_average_systolic():
    """
    Reads a JSON file containing patient data, groups the patients by age range,
    and calculates the average systolic blood pressure for each age group.
    """

    # Open the JSON file in read mode
    jfile = open("json_final_1.json", "r")
    # Read the file content and parse it into a Python dictionary
    data = json.loads(jfile.read())

    # Initialize a dictionary to store the total systolic pressure and count for each age group
    age_group_dict = {
        "<24" : {"Systolic_Pressure":0,"Count":0},
        "25-44": {"Systolic_Pressure":0,"Count":0},
        "45-65": {"Systolic_Pressure":0,"Count":0}, 
        ">65": {"Systolic_Pressure":0,"Count":0},
    }

    # Iterate through each patient's data in the "Dataset" list
    for patient in data["Data"]["Dataset"]:


        try:
            # Convert 'Age' and 'Systolic' values to floats
            age = float(patient['Age'])
            systolic_pressure = float(patient["Systolic"])

            # Check which age range the patient belongs to and update the dictionary
            if age <24:
                age_group_dict["<24"]["Systolic_Pressure"] += systolic_pressure
                age_group_dict["<24"]["Count"] += 1
            
            elif age >= 25 and age <= 44:
                age_group_dict["25-44"]["Systolic_Pressure"] += systolic_pressure
                age_group_dict["25-44"]["Count"] += 1

            elif age >= 45 and age <= 65:
                age_group_dict["45-65"]["Systolic_Pressure"] += systolic_pressure
                age_group_dict["45-65"]["Count"] += 1
            else:
                age_group_dict[">65"]["Systolic_Pressure"] += systolic_pressure
                age_group_dict[">65"]["Count"] += 1
                
        except (ValueError,KeyError):
            continue
    
    jfile.close()

    # Iterate through the age groups and their data in the dictionary
    for group, data in age_group_dict.items():

        # Check if the count for the group is not zero to prevent a division-by-zero error
        if age_group_dict[group]["Count"] != 0:
            # Calculate the average systolic pressure for the group
            group_avg_systolic = age_group_dict[group]["Systolic_Pressure"]/age_group_dict[group]["Count"]
        else:
            # If there is no data for a group, set the average to 0.
            group_avg_systolic = 0

        # Print the group and its calculated average in the specified format
        print(f"Group:{group},AvgBP:{group_avg_systolic}")            

group_and_average_systolic()