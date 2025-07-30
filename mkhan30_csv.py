import csv

def calculate_total_los_and_sofa():

    cfile = open('icu_data.csv')
    cdata = csv.DictReader(cfile, delimiter= ',')
    column_data  ={
        'RecordID' : 0,
        'Length_of_stay' : 0,
        'Length_of_stay Count': 0,
        'SOFA': 0,
        'SOFA Count': 0
    }

    for row in cdata:
        
        try:
        
            column_data['RecordID'] += 1
                
            
        except (ValueError,TypeError):
            pass

        try:

            if row['Length_of_stay'] not in ('-1','NA'):
                    los = row['Length_of_stay']
                    column_data['Length_of_stay'] += float(los)
                    column_data['Length_of_stay Count'] += 1

        except (ValueError,TypeError):
            pass

        try:
            if row['SOFA'] not in ('-1','NA'):
                    sofa = row['SOFA']
                    column_data['SOFA'] += float(sofa)
                    column_data['SOFA Count'] += 1
        except (ValueError, TypeError):
            pass

    cfile.close()

    column_names = ['Length_of_stay', 'SOFA']
    
    for name in column_names:

        if column_data[name+ ' Count'] != 0:
                average = column_data[name]/column_data[name+ ' Count']
        else:
            average = 0

        print(f"{name}:{average}")
    
    recordID_count = ['RecordID']

    for name in recordID_count:

        recordID_total = column_data[name]

        print(f"Total Records:{recordID_total}")

calculate_total_los_and_sofa()