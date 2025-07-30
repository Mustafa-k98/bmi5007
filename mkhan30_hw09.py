import collections

class Patient:
    def __init__(self, patient_ID, total_visits, physicians, diagnosis):
        """
        Initializes a new Patient object.
        
        :param patient_ID: A string, the unique identifier for the patient
        :param total_visits: An integer, the total number of visits for the patient
        :param physicians: A list of strings, the unique physician IDs the patient has seen
        :param diagnosis: A list of strings, the diagnoses codes for the patient
        """
        # Initializes the attributes
        self.patient_ID = patient_ID
        self.total_visits = total_visits
        self.physicians = physicians
        self.diagnosis = diagnosis

    def most_frequent_diagnosis(self):
        """
        Calculates the most frequent diagnosis for the patient.

        :return: A string, the most frequent diagnosis code
        """

        # Handle case of no diagnoses
        if not self.diagnosis:
            return None
    
        diagnosis_counter = collections.Counter(self.diagnosis)

        # most_common returns a list of the most common diagnosis
        most_common = diagnosis_counter.most_common(1)
        return most_common[0][0]
    


patient_sample = {
    'Patient_ID': '00016F745862898F',
    'Total_Visits': 2,
    'Physicians': ['2963419753', '5737807753'],
    'Diagnosis': ['V5832', 'V5861', '2724', '3182', 'V5869', '42731', '9594', 'E9174', '4019', '2724', 'V5869']
}

# Create an instance of the Patient class
patient_instance = Patient(
    patient_sample['Patient_ID'],
    patient_sample['Total_Visits'],
    patient_sample['Physicians'],
    patient_sample['Diagnosis']
)

# Call the most_frequent_diagnosis method and print the result
frequent_diagnosis = patient_instance.most_frequent_diagnosis()
print(frequent_diagnosis)

