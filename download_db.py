import wfdb
import os

def download_physionet_database(database_name, local_dir):
    wfdb.dl_database(database_name, dl_dir=local_dir)
    print(f"Downloaded database '{database_name}' to '{local_dir}'")

print("Enter Database Code to download: ")
database_name = input()
#database_name = 'slpdb' 
local_dir = os.getcwd() + '/' + database_name
download_physionet_database(database_name, local_dir)
