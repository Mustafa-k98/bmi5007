import csv

def process_outpatient_data(filename):
    """
    Process the outpatient data to calculate the required statistics for each patient.
    
    Args:
    - filename (str): Path to the outpatient_sample.csv
    
    Returns:
    - result (list): List of dictionaries with patient data.
    """

    # Initializes an empty dictionary to store data
    patient_data = {}
   
    # Opens target file, and ensures header isnt being analyzed
    cfile = open(filename, "r", newline = '')
    cdata = csv.reader(cfile, delimiter=',')
    header = next(cdata)
    
    # Number of Columns being used to ensure no blank data is read
    Expected_Num_Columns = 15

    # Iterates through every single row to ensure all data is captured
    for row in cdata:

        # Ensures that the len of row is not too short
        if len(row) < Expected_Num_Columns:
            continue
        
        # Extracts patient ID from the first column
        # .strip() ensures no whitespace characters are present
        patient_id = row[0].strip()

        # Adds patient ID to patient_data dict if this is the first encountered visit
        if patient_id not in patient_data:
            patient_data[patient_id] = {
                'total_visits' : 0,
                'physicians_seen': set(),
                'diagnoses_seen': set(),
                'diagnosis_counts': {}
            }
        
        # Increments total visit count by 1 for each visit of the current patient
        patient_data[patient_id]['total_visits'] += 1
        
        # Identifies which columns the physician information is in
        physician_columns = [2,3,4]

        # Iterates through each physician column
        # Adds unique and non-empty physician IDs to the patient's set of seen physicians
        for idx in physician_columns:
            physician_id = row[idx].strip()
            if physician_id:
                patient_data[patient_id]['physicians_seen'].add(physician_id)
        

        # Identifies which columns the diagnosis information is in
        diagnosis_columns = range(5,15)

        # Iterates through each diagnosis column
        # Adds unique diagnosis code to the patient's set of seen diagnoses.
        for idx in diagnosis_columns:
            diagnosis_code = row[idx].strip()
            if diagnosis_code:
                patient_data[patient_id]['diagnoses_seen'].add(diagnosis_code)

                # If diagnosis code is not in the dictionary, a counter is initialized
                # If diagnosis code is already in the dictionary, counter has 1 incremented to it
                if diagnosis_code not in patient_data[patient_id]['diagnosis_counts']:
                    patient_data[patient_id]['diagnosis_counts'][diagnosis_code] = 0
                patient_data[patient_id]['diagnosis_counts'][diagnosis_code] += 1
    
    # Closes file after reading all data
    cfile.close() 
    
    # Initializes a result list for final processed data for each patient
    result = []

    # Sorts patient IDs to ensure consistency
    sorted_patients = sorted(patient_data.keys())

    # Iterates through each patient ID
    for patient_id in sorted_patients:
        # Retrieves accumulated data
        data = patient_data[patient_id]

        # Calculates variables required for final results list
        total_visits = data['total_visits']
        total_physicians = len(data['physicians_seen'])
        total_diagnosis = len(data['diagnoses_seen'])
        # Initializes an empty string that will be updated
        most_freq_diagnosis = ''

        # Check if the patient has any diagnoses recorded to process
        if data['diagnosis_counts']:
            max_freq = 0
            # Finds the highest frequency amongst all diagnoses
            for count in data['diagnosis_counts'].values():
                if count > max_freq:
                    max_freq = count
            
            # Initializes a list to hold all diagnoses that have maximum frequency
            leading_most_freq_diagnosis = []
            
            # Iterate through each diagnois and its counts
            for ICD, count in data ['diagnosis_counts'].items():
                if count == max_freq:
                    leading_most_freq_diagnosis.append(ICD)

            # If there is a tie, sorts list and selects the first in the list since random module not available   
            if leading_most_freq_diagnosis:
                leading_most_freq_diagnosis.sort()
                most_freq_diagnosis = leading_most_freq_diagnosis[0]
        
        # Appends the final information to the results list as a dictionary to ensure name matches
        result.append({
            "Patient_ID": patient_id,
            "Total_Visits": total_visits,
            "Total_Physicians": total_physicians,
            "Total_Diagnosis": total_diagnosis,
            "Most_Freq_Diagnosis": most_freq_diagnosis
        })
        
    # Returns the final list of dictionaries containining target data
    return result

def write_summary_to_csv(data, filename):

    """
    Write the processed patient data to a csv file.
    
    Args:
    - data (list): List of dictionaries with patient data.
    - filename (str): Path to the output csv.
    """
    # Defines the column headers for the output CSV file
    fieldnames = ["Patient_ID", "Total_Visits", "Total_Physicians", "Total_Diagnosis", "Most_Freq_Diagnosis"]
    
    # Open the new output CSV file in write mode
    # newline = '' is added to ensure no rows inbetween each row of data
    with open(filename, mode = 'w', newline = '') as outputfile:
        
        # Creates a csv.DictWriter object, which maps dictionaries to csv rows using fieldnames as the header
        writer = csv.DictWriter(outputfile, fieldnames=fieldnames)

        # Writes the header row to the csv file using the defined fieldnames.
        writer.writeheader()

        # Writes all the processed patient data rows to the CSV file.
        writer.writerows(data)
    

def main():
    input_file = "outpatient_sample.csv"
    output_file = "mkhan30_hw04.csv"  
    
    processed_data = process_outpatient_data(input_file)
    write_summary_to_csv(processed_data, output_file)

if __name__ == "__main__":
    main()