import csv

storage = {}

input_file = 'myfile.csv'
output_file = 'aggregated_results.csv'

with open(input_file, newline='') as csvfile:
    data = csv.DictReader(csvfile)
    
    for i in data:
        industry_name = i['Industry_name_NZSIOC']
        value = i['Value']
    
        try:
            value = int(value)
        except ValueError:
            value = 0
        
        if industry_name in storage:
            storage[industry_name] += value
        else:
            storage[industry_name] = value

with open(output_file, mode='w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(['Industry_name_NZSIOC', 'Total_Value'])
    for industry, total in storage.items():
        writer.writerow([industry, total])

print(f"Aggregated results written to {output_file}")
