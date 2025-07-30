import json

def group_and_average_glucose():
    """
    Reads a JSON file containing patient data, groups the patients by BMI range,
    and calculates the average glucose level for each BMI group.
    """
    # Open the JSON file in read mode    
    jfile = open("json_final_1.json", "r")
    # Read the file content and parse it into a Python dictionary
    data = json.loads(jfile.read())

    # Initialize a dictionary to store the total glucose and count for each BMI group
    BMI_group_dict = {
        "<18.5" : {"Glucose":0,"Count":0},
        "18.5-24.9": {"Glucose":0,"Count":0},
        "25-29.9": {"Glucose":0,"Count":0}, 
        ">30": {"Glucose":0,"Count":0},
    }

    # Iterate through each patient's data in the "Dataset" list
    for patient in data["Data"]["Dataset"]:

        # Use a try-except block to handle cases where 'BMI' or 'Glucose'
        # data might be missing or non-numeric.
        try:
            # Convert 'BMI' and 'Glucose' values to floats
            bmi = float(patient['BMI'])
            gluc = float(patient["Glucose"])

            # Check which BMI range the patient belongs to and update the dictionary
            if bmi < 18.5:
                BMI_group_dict["<18.5"]["Glucose"] += gluc
                BMI_group_dict["<18.5"]["Count"] += 1
            
            elif bmi >= 18.5 and bmi <= 24.9:
                BMI_group_dict["18.5-24.9"]["Glucose"] += gluc
                BMI_group_dict["18.5-24.9"]["Count"] += 1

            elif bmi >= 25 and bmi <= 29.9:
                BMI_group_dict["25-29.9"]["Glucose"] += gluc
                BMI_group_dict["25-29.9"]["Count"] += 1
            else:
                BMI_group_dict[">30"]["Glucose"] += gluc
                BMI_group_dict[">30"]["Count"] += 1

        except (ValueError,KeyError):
            continue
    
    jfile.close()

    # Iterate through the BMI groups and their data in the dictionary
    for group, data in BMI_group_dict.items():

        # Check if the count for the group is not zero to prevent a division-by-zero error
        if BMI_group_dict[group]["Count"] != 0:
            # Calculate the average glucose for the group
            group_avg_glucose = BMI_group_dict[group]["Glucose"]/BMI_group_dict[group]["Count"]
        else:
            # If there is no data for a group, set the average to 0.
            group_avg_glucose = 0

        # Print the group and its calculated average in the specified format
        print(f"Group:{group},AvgGlucose:{group_avg_glucose}")            

group_and_average_glucose()