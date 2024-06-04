import csv
import wfdb
import requests
from bs4 import BeautifulSoup

# Get available databases
available_databases = wfdb.get_dbs()
number_of_databases = len(available_databases)
print(f"Number of available databases: {number_of_databases}")

def get_dataset_description(dataset_name):
    physionet_url = f"https://physionet.org/content/{dataset_name}/1.0.0/"
    print(f"Fetching description for {dataset_name}...")
    page = requests.get(physionet_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    description_tag = soup.find('h3', string="Data Description")
    description_tag1 = soup.find('h2', string="Data Description")
    description_tag2 = soup.find('h3', string="Abstract")
    if description_tag:
        description = description_tag.find_next('p').get_text(strip=True)
        print(f"Description found for {dataset_name}.")
        return description
    elif description_tag1:
        description = description_tag1.find_next('p').get_text(strip=True)
        return description
    elif description_tag2:
        description = description_tag2.find_next('p').get_text(strip=True)
        return description
    else:
        print("NO DESCRIPTION FOUND")
        return ""

ecg_datasets = []
for db in available_databases:
    keywords = ['ECG', 'Electrocardiogram', 'Electrocardiography']
    description = get_dataset_description(db[0])
    if any(keyword in description for keyword in keywords):
        print(f"Adding {db[0]} to ECG datasets.")
        ecg_datasets.append(db)
    else:
        print(f"{db[0]} does not match ECG keywords.")

csv_filename = "Metadata.csv"
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Name', 'Description'])
    for db_name, db_description in ecg_datasets:
        csv_writer.writerow([db_name, db_description])

print("Total ECG Datasets: ")        
print(len(ecg_datasets))
    
